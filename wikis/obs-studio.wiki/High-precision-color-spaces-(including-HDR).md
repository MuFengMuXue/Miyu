# Background

**NOTE: This is still a work-in-progress. Features are subject to change.**

Given increasing HDR display adoption across users and industry, it makes sense for OBS to expand its support for color spaces.

OBS has been upgraded in the following areas:

- Composition
- Sources
- Preview
- Video format conversion

# Composition

OBS operates by combining video from various sources, and it does so in a master texture that we don't have a formal name for. I'll refer to it as the canvas.

Prior to version 28, OBS has only supported sRGB implicitly using 8 bits per channel. OBS now supports four color spaces for canvas composition.

The first three of these color spaces are "relative" in that the values do not have a specific luminance. OBS has a new setting "SDR White Level (nits)" to allow users to specify the absolute value for 1.0. Our default of 300 nits is a common recommendation in game development to composite SDR UI against HDR gameplay.

![image](https://user-images.githubusercontent.com/10396506/163323274-7cff145f-a3e7-42f9-b32a-b1a5b0f79bdd.png)

This setting is analogous to "SDR content brightness" in Windows HDR settings. They have a [0, 100] scale that defaults to 40. That translates to [80, 480] nits with a default of 240 nits. It should be noted that OBS does not use the OS setting for any of its computations, so don't be surprised if SDR content looks different in OBS on an HDR monitor.

![image](https://user-images.githubusercontent.com/10396506/162563005-6695dc6b-3adf-48b6-986f-3145710ad837.png)

## sRGB (SDR, 8 bits per channel, unsigned normalized, [0, 1] range used)

This is the color space OBS has always supported, the tried-and-true SDR color space for desktops since the 1990s. Color is stored nonlinearly to give more precision to darks, which humans are better able to perceive.

GPUs typically have support for "SRGB" textures, which can convert color values to and from linear space, where most color math should be performed. This support can be enabled or disabled as desired, which OBS uses extensively.

## sRGB (SDR, 16 bits per channel, floating-point, [0, 1] range used)

The same color space, but with more bits of precision. This can be helpful to reduce banding typically seen by 8-bit sRGB.

Unlike its 8-bit counterpart, GPUs do not have automatic linear/nonlinear conversions, and values are always stored/manipulated "linearly." This is fine for floating-point numbers because they are implicitly nonlinear, and also give more precision to the small numbers that represent dark colors.

If you look at our codebase, you may notice that between sRGB, Rec. 709, and Rec. 601, OBS only performs YCbCr conversions, but does not convert primaries or transfer functions. We treat Rec. 709 and Rec. 601 as if they are sRGB for various reasons. One being that we don't want to exacerbate banding, and another being that most media players that we have tested also aliased other SDR color spaces as sRGB.

## "Extended Dynamic Range" (EDR) (HDR, 16 bits per channel, floating-point, [0, 125] range used)

This is similar to our 16-bit sRGB space, but values above 1.0 are valid, and represent colors that are "whiter" than diffuse white, e.g. the Sun, specular highlights. The EDR term comes from Apple as far we know.

The reason why we cannot use EDR for 16-bit sRGB despite having a bit-identical representation from [0, 1] is that we need to know whether we are SDR vs. HDR to apply tonemapping in the appropriate situations.

## "Canonical Compositing Color Space" (CCCS) (HDR, 16 bits per channel, floating-point, [0, 125] range used)

Similar to EDR, but 1.0 has an absolute value of 80 nits. You may also see this referred to as scRGB or "floating-point scRGB" since scRGB didn't originally involve a floating-point representation. The CCCS term comes from Microsoft as far we know.

It should be noted that this color space is mainly used by HDR windows on Windows. OBS uses this space only for window preview and not for composition because the math simplifies if diffuse white is consistently 1.0.

Mac preview can use EDR directly; CCCS preview may be useful when Linux eventually receives HDR support.

The canvas color space is chosen implicitly by "Color Format" and "Color Space" settings.

![image](https://user-images.githubusercontent.com/10396506/163323502-abb1ec23-7e64-4de6-b181-41b67d560bc7.png)

Video color format/space -> Canvas color space:
- NV12/I420/I444/RGB + sRGB/Rec. 709/Rec. 601 = sRGB (8-bit)
- P010/I010 + sRGB/Rec. 709/Rec. 601 = sRGB (16-bit floating-point)
- ~~NV12/I420/I444/RGB + Rec. 2100~~ These combinations are not valid.
- P010/I010 + Rec. 2100 = EDR

# Sources

There are three public types of sources: input, filter, transition. It is important to us not to break the existing ecosystem of external plugins, so OBS has decided on an important guideline.

**Sources are 8-bit sRGB by default, and need to opt into extended color spaces.**

For an input source, this is not such a big deal, but you have to be careful with filters and transitions. If you have a setup like this:

Input [HDR] -> Scene [HDR] -> Transition [HDR] -> Canvas [HDR]

Adding an legacy filter that lacks knowledge of extended color spaces will lead to premature tonemapping:

Input [HDR] -> (implicit HDR to SDR conversion) -> Filter [SDR] -> Scene [SDR] -> Transition [SDR] -> (implicit SDR to HDR conversion) -> Canvas [HDR]

Note: By the time you read this, all filter/transition sources included with OBS should have been upgraded to support HDR to avoid this problem.

Input Sources that have been upgraded to support HDR include:

- Media Source
- Display Capture (Windows)
- Game Capture (Windows)
- Window Capture (Windows)

## Automatic color space conversion

libobs will automatically convert colors when it detects color space mismatches along a source chain.

- sRGB8 -> sRGB8, sRGB16F -> sRGB16F, EDR -> EDR, CCCS -> CCCS: No extra draw
- sRGB8 -> sRGB16F, sRGB16F -> sRGB8: Regular draw with GPU SRGB automatic conversions enabled
- sRGB8/sRGB16F -> EDR: Regular draw since the [0, 1] range maps identically to the [0, 1] range of EDR
- sRGB8/sRGB16F/EDR -> CCCS: Draw that multiplies RGB with a factor of SDR white level divided by 80.0 to go from relative to absolute.
- EDR -> sRGB8/sRGB16F: Draw that tonemaps HDR to SDR.
- CCCS -> EDR: Draw that multiplies RGB with a factor of 80.0 divided by SDR white level.
- CCCS -> sRGB8/sRGB16F: Draw that multiplies RGB with a factor of 80.0 divided by SDR white level to go from absolute to relative, then tonemaps from HDR to SDR.

A source opts into extended color space support by supplying a `video_get_color_space` callback. The signature looks like this:
`enum gs_color_space (*video_get_color_space)(void *data, size_t count, const enum gs_color_space *preferred_spaces);`

It is important that a source be able to change its answer from frame to frame. For example, someone might change Display Capture to point from an SDR monitor to an HDR monitor.

Prior to rendering a source, libobs (or perhaps a filter/transition) will "ask" the next source what color space it wants to render in, providing the set of "preferred spaces" that will lead to fewest unnecessary conversions and/or highest quality. A source is free to ignore the preferred spaces to simplify its implementation, but matching a preferred source is generally, well, preferred, and usually leads to better performance.

As an example, let's say a video game streamer is playing an HDR game, and sending an SDR video stream to a popular streaming service. If Game Capture were to pass the signal through naively:

- libobs: "Hey Game Capture, what color space are you going to render to? I prefer SDR."
- Game Capture: "HDR"
- libobs: "Okay, here's an HDR render target."
- Game Capture renders HDR.
- libobs re-renders from HDR to SDR.
- GPU is sad.

If Game Capture is implemented to also process the color space difference:

- libobs: "Hey Game Capture, what color space are you going to render to? I prefer SDR."
- Game Capture: "SDR"
- libobs: "Okay, here's an SDR render target."
- Game Capture renders its HDR image, tonemapping to SDR in the process.
- libobs does not need to re-render from HDR to SDR.
- GPU is happy.

## Color conversion examples

For the purposes of understanding the color values better, here are some example calculations performed under the following conditions:

* SDR monitor - full white calibrated to 120 nits
* HDR monitor - can display up to 1000 nits
* Windows SDR setting - 240 nits
* OBS SDR setting - 300 nits
* Theoretical player that uses Reinhard, and Windows SDR setting for HDR to SDR

Calculations:

* Rec. 709 color space
  * SDR source white (1.0)
    * SDR monitor
      * source preview = 1.0 * 120 = 120 nits
      * scene preview = 1.0 * 120 = 120 nits
      * theoretical media player = 1.0 * 120 = 120 nits
    * HDR monitor
      * source preview = 1.0 * 300 = 300 nits (use OBS SDR setting)
      * scene preview = 1.0 * 300 = 300 nits (use OBS SDR setting)
      * theoretical media player = 1.0 * 240 = 240 nits (use Windows SDR setting)
  * HDR source color (1000 nits)
    * SDR monitor
      * source preview = ((1000/300) / ((1000/300) + 1)) * 120 = 92 nits
      * scene preview = ((1000/300) / ((1000/300) + 1)) * 120 = 92 nits
      * media player = ((1000/300) / ((1000/300) + 1)) * 120 = 92 nits
    * HDR monitor
      * source preview = 1000 nits (show pure source)
      * scene preview = ((1000/300) / ((1000/300) + 1)) * 300 = 231 nits (use OBS SDR setting)
      * theoretical media player = ((1000/300) / ((1000/300) + 1)) * 240 = 185 nits (use Windows SDR setting)
* Rec. 2100 (PQ) color space
  * SDR source white (1.0)
    * SDR monitor
      * source preview = 1.0 * 120 = 120 nits (show pure source)
      * scene preview = ((300/300) / ((300/300) + 1)) * 120 = 60 nits
      * theoretical media player = ((300/240) / ((300/240) + 1)) * 120 = 67 nits (300 in video, tonemap for 240)
    * HDR monitor
      * source preview = 1.0 * 300 = 300 nits
      * scene preview = 1.0 * 300 = 300 nits
      * theoretical media player = 300 nits (300 in video, Windows SDR setting unused)
  * HDR source color (1000 nits)
    * SDR monitor
      * source preview = ((1000/300) / ((1000/300) + 1)) * 120 = 92 nits
      * scene preview = ((1000/300) / ((1000/300) + 1)) * 120 = 92 nits
      * theoretical media player = ((1000/240) / ((1000/240) + 1)) * 120 = 97 nits (1000 in video, tonemap for 240)
    * HDR monitor
      * source preview = 1000 nits
      * scene preview = 1000 nits
      * theoretical media player = 1000 nits

# Preview

Preview windows on OBS take many forms. There's the main preview, the scene preview in Studio Mode, source/filter previews, windows/fullscreen projectors, and multiview. These are backed by Direct3D or OpenGL swap chains. There is an important rule to keep in mind.

**Previews do not care what your OBS settings are. If it is on an SDR monitor, the preview will be SDR. If it on an HDR monitor, the preview will be HDR.**

On Windows, a monitor is HDR if this setting is enabled.

![image](https://user-images.githubusercontent.com/10396506/162563197-3a6682b0-d8fd-45a0-b5fd-9ed3534abfe8.png)

For the time being, Mac and Linux are limited to SDR previews. Mac support is a bit challenging at the moment, and no compositor on Linux has HDR capabilities ready to go as far as we know.

This is how preview windows handle content:
- sRGB content on sRGB window: Use color value
- sRGB content on EDR (Mac) window: Use color value
- sRGB/EDR content on CCCS (Windows) window: Multiply color value by SDR White Level / 80.0
- EDR content on sRGB window: Tonemap color value (Reinhard), lossy
- EDR content on EDR (Mac) window: Use color value

Another important note:

**Previews are just previews. They do not play a role in composition. You can still process and make HDR videos with OBS without an HDR monitor although it's obviously a better experience if you can see the real colors instead of tonemapped colors.**

# Video format conversion

There are two new input/output video formats in the settings: P010/I010. You can read more about them elsewhere, but they are 10-bit formats appropriate for high-precision SDR or HDR.

There are also two new video color spaces in the settings, Rec. 2100 (PQ), and Rec. 2100 (HLG).

![image](https://user-images.githubusercontent.com/10396506/163323502-abb1ec23-7e64-4de6-b181-41b67d560bc7.png)

- P010 works well with NVENC HEVC to generate both high-precision sRGB, and PQ/HLG video.
- I010 can be used by AOM AV1 to generate PQ/HLG video. SVT-AV1 does not currently support HDR.

(NVENC HEVC support may or may not be available at this time.)

OBS can leverage the new 10-bit formats both as input in the media source for video playback, and as output for streaming/recording.

## Display primaries and white point

For PQ and HLG metadata, we always set the primaries and white point in metadata to match P3-D65 for sanity. Someday we may expose these as configurable fields if more capable displays emerge, but for simplicity, we will set this metadata automatically. Please ensure your content does not use colors outside of this range.

## HDR Nominal Peak Level

You can find this setting near the other new color space settings.

![image](https://user-images.githubusercontent.com/10396506/163323634-02b0d680-df18-4841-bca4-3a832d692e35.png)

This value has a few uses.

- For PQ output video, we set this value in the metadata to relay how bright a pixel can get. It is up to the discretion of the video player/device on the other end how to react to this number, but my understanding is that the receiving end should generally tonemap down the signal if it goes beyond the playback display's capabilities, or pass the color values through untouched otherwise. This is what Chromium does.
- For HLG output video, We use this value for converting our absolute nits representation to HLG's unitless relative representation. If the HDR nominal peak value is greater than 1000 nits, we tonemap down to 1000 nits using maxRGB EETF as specified in BT.2408. Otherwise, we do not modify the color values. From there, we use the standard PQ -> HLG conversion algorithm for 1000 nits, but without the PQ part since we already have the linear nit values. This is the recommendation of MovieLabs, which has ties to the big movie studios, and is therefore infallible. We set 1000 nits in metadata on output even though it technically isn't needed since HLG is relative.
- For PQ input video using Media Source, we use the HDR nominal peak value as the maxRGB EETF target if the source video luminance, as reported by MaxCLL or falling back to ST 2086 Maximum Luminance, is brighter than than the HDR nominal peak level. Otherwise the color values are passed through untouched.
- For HLG input video using Media Source, we use the HDR nominal peak value to unpack the HLG video signal up to 1000 nits. If the setting is greater than 1000 nits, the HLG video peak will still be treated as 1000 nits because it's unlikely for an HLG stream to have been authored higher than that.

It is up to the user of OBS to ensure that the HDR nominal peak value is accurate, so be careful!