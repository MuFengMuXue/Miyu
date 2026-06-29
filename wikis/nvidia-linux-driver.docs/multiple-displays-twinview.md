## Chapter 12. Configuring Multiple Display Devices on One X Screen

Multiple display devices (digital flat panels, CRTs, and TVs) can display the contents of a single X screen in any arbitrary configuration. Configuring multiple display devices on a single X screen has several distinct advantages over other techniques (such as Xinerama):

- A single X screen is used. The NVIDIA driver conceals all information about multiple display devices from the X server; as far as X is concerned, there is only one screen.

- Both display devices share one frame buffer. Thus, all the functionality present on a single display (e.g., accelerated OpenGL) is available with multiple display devices.

- No additional overhead is needed to emulate having a single desktop.

If you are interested in using each display device as a separate X screen, see [Chapter 14, *Configuring Multiple X Screens on One Card*](configmultxscreens.html "Chapter 14. Configuring Multiple X Screens on One Card").

### Relevant X Configuration Options

When the NVIDIA X driver starts, by default it will enable as many display devices as are connected and as the GPU supports driving simultaneously. Most NVIDIA GPUs support driving up to four display devices simultaneously.

If multiple X screens are configured on the GPU, the NVIDIA X driver will attempt to reserve display devices and GPU resources for those other X screens (honoring the "UseDisplayDevice" and "MetaModes" X configuration options of each X screen) and then allocate all remaining resources to the first X screen configured on the GPU.

There are several X configuration options that influence how multiple display devices are used by an X screen:

``` screen
    Option "MetaModes"                "<list of MetaModes>"

    Option "HorizSync"                "<hsync range(s)>"
    Option "VertRefresh"              "<vrefresh range(s)>"

    Option "MetaModeOrientation"      "<relationship of head 1 to head 0>"
    Option "ConnectedMonitor"         "<list of connected display devices>"
```

See detailed descriptions of each option below.

### Detailed Description of Options

HorizSync, VertRefresh
With these options, you can specify a semicolon-separated list of frequency ranges, each optionally prepended with a display device name. In addition, if SLI Mosaic mode is enabled, a GPU specifier can be used. For example:

``` screen
    Option "HorizSync"   "CRT-0: 50-110; DFP-0: 40-70"
    Option "VertRefresh" "CRT-0: 60-120; GPU-0.DFP-0: 60"
```

See [Appendix C, *Display Device Names*](displaydevicenames.html "Appendix C. Display Device Names") on Display Device Names for more information.

These options are normally not needed: by default, the NVIDIA X driver retrieves the valid frequency ranges from the display device's EDID (see the [UseEdidFreqs](xconfigoptions.html#UseEdidFreqs) option). The "HorizSync" and "VertRefresh" options override any frequency ranges retrieved from the EDID.

MetaModes
MetaModes are "containers" that store information about what mode should be used on each display device.

Multiple MetaModes list the combinations of modes and the sequence in which they should be used. In MetaMode syntax, modes within a MetaMode are comma separated, and multiple MetaModes are separated by semicolons. For example:

``` screen
    "<mode name 0>, <mode name 1>; <mode name 2>, <mode name 3>"
```

Where \<mode name 0\> is the name of the mode to be used on display device 0 concurrently with \<mode name 1\> used on display device 1. A mode switch will then cause \<mode name 2\> to be used on display device 0 and \<mode name 3\> to be used on display device 1. Here is an example MetaMode:

``` screen
    Option "MetaModes" "1280x1024,1280x1024; 1024x768,1024x768"
```

If you want a display device to not be active for a certain MetaMode, you can use the mode name "NULL", or simply omit the mode name entirely:

``` screen
    "1600x1200, NULL; NULL, 1024x768"
```

or

``` screen
    "1600x1200; , 1024x768"
```

Optionally, mode names can be followed by offset information to control the positioning of the display devices within the virtual screen space; e.g.,

``` screen
    "1600x1200 +0+0, 1024x768 +1600+0; ..."
```

Offset descriptions follow the conventions used in the X "-geometry" command line option; i.e., both positive and negative offsets are valid, though negative offsets are only allowed when a virtual screen size is explicitly given in the X config file.

When no offsets are given for a MetaMode, the offsets will be computed following the value of the MetaModeOrientation option (see below). Note that if offsets are given for any one of the modes in a single MetaMode, then offsets will be expected for all modes within that single MetaMode; in such a case offsets will be assumed to be +0+0 when not given.

When not explicitly given, the virtual screen size will be computed as the bounding box of all MetaMode bounding boxes. MetaModes with a bounding box larger than an explicitly given virtual screen size will be discarded.

A MetaMode string can be further modified with a "Panning Domain" specification; e.g.,

``` screen
    "1024x768 @1600x1200, 800x600 @1600x1200"
```

A panning domain is the area in which a display device's viewport will be panned to follow the mouse. Panning actually happens on two levels with MetaModes: first, an individual display device's viewport will be panned within its panning domain, as long as the viewport is contained by the bounding box of the MetaMode. Once the mouse leaves the bounding box of the MetaMode, the entire MetaMode (i.e., all display devices) will be panned to follow the mouse within the virtual screen, unless the "PanAllDisplays" X configuration option is disabled. Note that individual display devices' panning domains default to being clamped to the position of the display devices' viewports, thus the default behavior is just that viewports remain "locked" together and only perform the second type of panning.

The most beneficial use of panning domains is probably to eliminate dead areas -- regions of the virtual screen that are inaccessible due to display devices with different resolutions. For example:

``` screen
    "1600x1200, 1024x768"
```

produces an inaccessible region below the 1024x768 display. Specifying a panning domain for the second display device:

``` screen
    "1600x1200, 1024x768 @1024x1200"
```

provides access to that dead area by allowing you to pan the 1024x768 viewport up and down in the 1024x1200 panning domain.

Offsets can be used in conjunction with panning domains to position the panning domains in the virtual screen space (note that the offset describes the panning domain, and only affects the viewport in that the viewport must be contained within the panning domain). For example, the following describes two modes, each with a panning domain width of 1900 pixels, and the second display is positioned below the first:

``` screen
    "1600x1200 @1900x1200 +0+0, 1024x768 @1900x768 +0+1200"
```

Because it is often unclear which mode within a MetaMode will be used on each display device, mode descriptions within a MetaMode can be prepended with a display device name. For example:

``` screen
    "CRT-0: 1600x1200,  DFP-0: 1024x768"
```

If no MetaMode string is specified, then the X driver uses the modes listed in the relevant "Display" subsection, attempting to place matching modes on each display device.

Each mode of the MetaMode may also have extra attributes associated with it, specified as a comma-separated list of token=value pairs inside curly brackets. The value for each token can optionally be enclosed in parentheses, to prevent commas within the value from being interpreted as token=value pair separators. Currently, the only token that requires a parentheses-enclosed value is "Transform".

The possible tokens within the curly bracket list are:

- "Stereo": possible values are "PassiveLeft" or "PassiveRight". When used in conjunction with stereo mode "4", this allows each display to be configured independently to show any stereo eye. For example:

``` screen
      "CRT-0: 1600x1200 +0+0 { Stereo = PassiveLeft }, CRT-1: 1600x1200 +1600+0 { Stereo=PassiveRight }"

```

  If the X screen is not configured for stereo mode "4", these options are ignored. See the [Stereo](xconfigoptions.html#Stereo) X configuration option for more details about stereo configurations.

- "Rotation": this rotates the content of an individual display device. Possible values are "0" (with synonyms "no", "off" and "normal"), "90" (with synonyms "left" and "CCW"), "180" (with synonyms "invert" and "inverted") and "270" (with synonyms "right" and "CW"). For example:

``` screen
      "DFP-0: nvidia-auto-select { Rotation=left }, DFP-1: nvidia-auto-select { Rotation=right }"

```

  Independent rotation configurability of each display device is also possible through RandR. See [Chapter 15, *Support for the X Resize and Rotate Extension*](xrandrextension.html "Chapter 15. Support for the X Resize and Rotate Extension") for details.

- "Reflection": this reflects the content of an individual display device about either the X axis, the Y axis, or both the X and Y axes. Possible values are "X", "Y" and "XY". For example:

``` screen
      "DFP-0: nvidia-auto-select { Reflection=X }, DFP-1: nvidia-auto-select"

```

  Independent reflection configurability of each display device is also possible through RandR. See [Chapter 15, *Support for the X Resize and Rotate Extension*](xrandrextension.html "Chapter 15. Support for the X Resize and Rotate Extension") for details.

- "Transform": this is a 3x3 matrix of floating point values that defines a transformation from the ViewPortOut for a display device to a region within the X screen. This is equivalent to the transformation matrix specified through the RandR 1.3 RRSetCrtcTransform request. As in RandR, the transform is applied before any specified rotation and reflection values to compute the complete transform.

  The 3x3 matrix is represented in the MetaMode syntax as a comma-separated list of nine floating point values, stored in row-major order. This is the same as the value passed to the xrandr(1) '--transform' command line option.

  Note that the transform value must be enclosed in parentheses, so that the commas separating the nine floating point values are interpreted correctly.

  For example:

``` screen
      "DFP-0: nvidia-auto-select { Transform=(43.864288330078125, 21.333328247070312, -16384, 0, 43.864288330078125, 0, 0, 0.0321197509765625, 19.190628051757812) }"

```

- "PixelShiftMode": This allows a display to be configured in pixel shift mode, in which a display overlays multiple downscaled images to simulate a higher effective resolution. This is used in certain JVC e-shift projectors. All pixel shift modes require an NVIDIA RTX/Quadro GPU. Possible values are "4kTopLeft", "4kBottomRight", and "8k".

  In 4K pixel shift mode, two cloned displays are configured in pixel shift mode, and either display is configured to display either the top left or bottom right pixels of every pixel quad. Note that the mode timings used by each display are one quarter of the resolution read from the X screen and one quarter of the effective resolution displayed (e.g., "1920x1080" rather than "3840x2160").

  For example, here is the configuration of a 4K pixel shift mode, with an effective desktop resolution of 3840x2160:

``` screen
      "DFP-0: 1920x1080 +0+0 { PixelShiftMode = 4kTopLeft, ViewPortIn = 3840x2160 }, DFP-1: 1920x1080 +0+0 { PixelShiftMode = 4kBottomRight, ViewPortIn = 3840x2160 }"

```

  In 8K pixel shift mode, the image is downscaled from the ViewPortIn resolution to the mode timing resolution, to produce two different images: one for the top left pixel of every pixel quad and one for the bottom right of every pixel quad. The display alternates between the two images each vblank. This requires an NVIDIA RTX/Quadro graphics card with a 3-pin DIN stereo connector.

  For example, here is the configuration for an 8K pixel shift mode, with an effective desktop resolution and refresh rate of 8192x4800 @30Hz, split across 4 1024x2400@60Hz displays. Note that the panning offsets of each display are in X screen (ViewPortIn) coordinates:

``` screen
      "DFP-0: 1024x2400 +0+0 { PixelShiftMode=8k, ViewPortIn = 2048x4800 }, DFP-1: 1024x2400 +2048+0 { PixelShiftMode=8k, ViewPortIn = 2048x4800 }, DFP-2: 1024x2400 +4096+0 { PixelShiftMode=8k, ViewPortIn = 2048x4800 }, DFP-4: 1024x2400 +6144+0 { PixelShiftMode=8k, ViewPortIn = 2048x4800 }"

```

  In both examples above, the ViewPortIn is provided here for illustrative purposes only. When PixelShiftMode is used, the ViewPortIn and ViewPortOut are always inferred from the mode timings: the ViewPortOut will match the mode timing resolution, which is half the intended resolution. The ViewPortIn will be twice the ViewPortOut, in order to achieve the pixel shift effect.

- "ViewPortOut": this specifies the region within the mode sent to the display device that will display pixels from the X screen. The region of the mode outside the ViewPortOut will contain black. The format is "WIDTH x HEIGHT +X +Y".

  This is useful, for example, for configuring overscan compensation. E.g., if the mode sent to the display device is 1920x1080, to configure a 10 pixel border on all four sides:

``` screen
      "DFP-0: 1920x1080 { ViewPortOut=1900x1060+10+10 }"

```

  Or, to only display an image in the lower right quarter of the 1920x1080 mode:

``` screen
      "DFP-0: 1920x1080 { ViewPortOut=960x540+960+540 }"

```

  When not specified, the ViewPortOut defaults to the size of the mode.

- "ViewPortIn": this defines the size of the region of the X screen which will be displayed within the ViewPortOut. The format is "WIDTH x HEIGHT".

  ViewPortIn is useful for configuring scaling between the X screen and the display device. For example, to display an 800x600 region from the X screen on a 1920x1200 mode:

``` screen
      "DFP-0: 1920x1200 { ViewPortIn=800x600 }"

```

  Or, to display a 2560x1600 region from the X screen on a 1920x1200 mode:

``` screen
      "DFP-0: 1920x1200 { ViewPortIn=2560x1600 }"

```

  Or, in conjunction with ViewPortOut, to scale an 800x600 region of the X screen within a 1920x1200 mode while preserving the aspect ratio:

``` screen
      "DFP-0: 1920x1200 { ViewPortIn=800x600, ViewPortOut=1600x1200+160+0 }"

```

  Scaling from ViewPortIn to ViewPortOut is also expressible through the "Transform" attribute. In fact, ViewPortIn is just a shortcut for populating the transformation matrix. If both ViewPortIn and Transform are specified in the MetaMode for a display device, ViewPortIn is ignored.

  ViewPortIn is also ignored if PixelShiftMode is enabled, as PixelShiftMode implies a transformation of double width and height.

- "PanningTrackingArea": this defines the region of the MetaMode inside which cursor movement will influence panning of the display device. The format is "WIDTH x HEIGHT + X + Y", to describe the size and offset of the region within the X screen. E.g.,

``` screen
      "DFP-0: 1920x1200 +0+0 { PanningTrackingArea = 1920x1200 +0+0 }"

```

  If not specified in the MetaMode, this will default to the entire X screen. If the [PanAllDisplays](xconfigoptions.html#PanAllDisplays) X configuration option is explicitly set to False, then PanningTrackingArea will default to the panning domain of the display device.

  This is equivalent to the panning tracking_area region in the RRSetPanning RandR 1.3 protocol request.

- "PanningBorder": this defines the distances from the edges of the ViewPortIn that will activate panning if the pointer hits them. If the borders are 0, the display device will pan when the pointer hits the edge of the ViewPortIn (the default). If the borders are positive, the display device will pan when the pointer gets close to the edge of the ViewPortIn. If the borders are negative, the display device will pan when the pointer is beyond the edge of the ViewPortIn.

  The format is "LeftBorder/TopBorder/RightBorder/BottomBorder". E.g.,

``` screen
      "DFP-0: 1920x1200 +0+0 { PanningBorder = 10/10/10/10 }"

```

  This is equivalent to the panning border in the RRSetPanning RandR 1.3 protocol request.

- "ForceCompositionPipeline": possible values are "On" or "Off". The NVIDIA X driver can use a composition pipeline to apply X screen transformations and rotations. "ForceCompositionPipeline" can be used to force the use of this pipeline, even when no transformations or rotations are applied to the screen.

- "ForceFullCompositionPipeline": possible values are "On" or "Off". This option implicitly enables "ForceCompositionPipeline" and additionally makes use of the composition pipeline to apply ViewPortOut scaling.

- "WarpMesh", "BlendTexture", "OffsetTexture": these string attributes control the operation of Warp and Blend, an advanced transformation feature available on select NVIDIA RTX/Quadro GPUs. Warp and Blend can adjust a display's geometry (warp) with a greater level of control than a simple matrix transformation: for example, to facilitate projecting an image onto a non-planar surface, and its intensity (blend) per pixel: for example, to seamlessly combine images from multiple overlapping projectors into a single large image. Each of the "WarpMesh", "BlendTexture", and "OffsetTexture" MetaMode tokens can be set to the name of a pixmap which has already been bound to a name via the XNVCtrlBindWarpPixmapName() NV_CONTROL call. See the `nv-control-warpblend` sample application distributed with the **nvidia-settings** source code for a more detailed description of the functionality of each of these pixmaps, how to lay data out into the pixmaps, and an example implementation of an X application that loads and binds pixmaps so that they are ready to use in a MetaMode.

  If driving the current mode in the RGB 4:4:4 color space would require a pixel clock that exceeds the display's or GPU's capabilities, and the display and GPU are capable of driving that mode in the YCbCr 4:2:0 color space, then the color space will be overridden to YCbCr 4:2:0. In this case, if a Turing or earlier GPU is in use, or if a DisplayPort display device is in use regardless of GPU, then Warp and Blend will be disabled.

  Warp and Blend is not yet supported with the GLX_NV_swap_group OpenGL extension.

- "BlendOrder": Controls the order of warping and blending when using Warp and Blend. By default, warping is performed first, followed by blending; setting the "BlendOrder" MetaMode token to "BlendAfterWarp" will reverse the default order.

- "ResamplingMethod": Controls the filtering method used to smooth the display image when scaling screen transformations (such as a WarpMesh or scaling ViewPortOut) are in use. Possible values are "Bilinear" (default), "BicubicTriangular", "BicubicBellShaped", "BicubicBspline", "BicubicAdaptiveTriangular", "BicubicAdaptiveBellShaped", "BicubicAdaptiveBspline", and "Nearest".

  Bicubic resampling is only available on NVIDIA RTX/Quadro GPUs. If a mode requiring a YCbCr 4:2:0 color space is in use on a DisplayPort display device or a Turing or earlier GPU, then bicubic resampling is unavailable. Bicubic resampling is not supported with the GLX_NV_swap_group OpenGL extension.

- "AllowGSYNC" or "AllowGSYNCCompatible": Controls whether capable monitors are put into G-SYNC or G-SYNC Compatible mode or left in continuous refresh mode.

  By default, G-SYNC monitors are put into G-SYNC mode when a mode is set, and transition into and out of variable refresh mode seamlessly. However, this prevents certain other features, such as Ultra Low Motion Blur and Frame Lock, from working. Set this to "Off" to use continuous refresh rates that are compatible with these features.

  In addition, G-SYNC Compatible monitors are supported via DisplayPort on Pascal and newer GPUs, and via HDMI on Turing and newer GPUs. Supported monitors will enable variable refresh mode by default. This behavior may be overridden by setting the AllowGSYNCCompatible=Off MetaMode attribute. Pascal GPUs only support G-SYNC Compatible monitors in systems containing no more than one monitor in variable refresh mode. Monitors that have not been validated as G-SYNC Compatible have G-SYNC Compatible mode disabled by default, and can be forced into G-SYNC Compatible mode by setting the AllowGSYNCCompatible=On MetaMode attribute. A list of supported G-SYNC and G-SYNC Compatible monitors can be found at https://www.nvidia.com/en-us/geforce/products/g-sync-monitors/specs/

  Note: Vulkan direct-to-display applications may allow or disallow G-SYNC or G-SYNC Compatible at modeset time using the VKDirectGSYNCAllowed and VKDirectGSYNCCompatibleAllowed environment variables. VKDirectGSYNCAllowed is set to true by default (allowing VRR on all G-SYNC monitors) and VKDirectGSYNCCompatibleAllowed may be set to 0 (disallowing VRR on all G-SYNC Compatible monitors), 1 (default, allowing VRR only on monitors validated as G-SYNC Compatible), or 2 (allowing VRR regardless of whether a monitor has been validated as G-SYNC Compatible).

- "VRRMinRefreshRate": Overrides a G-SYNC Compatible monitor's minimum refresh rate. Some monitors that have not been validated as G-SYNC Compatible may flicker when applications are swapping close to the monitor's minimum refresh rate, and this MetaMode flag may be used to compensate for this. This MetaMode flag has no effect on G-SYNC monitors.

- "OutputBitsPerComponent": Overrides the number of bits per color component transmitted via a display connector. If not specified, the driver will choose an optimal color format.

Note that the current MetaMode can also be configured through the NV-CONTROL X extension and the nvidia-settings utility. For example:

``` screen
    nvidia-settings --assign CurrentMetaMode="DFP-0: 1920x1200 { ViewPortIn=800x600, ViewPortOut=1600x1200+160+0 }"
```

MetaModeOrientation
This option controls the positioning of the display devices within the virtual X screen, when offsets are not explicitly given in the MetaModes. The possible values are:

``` screen
    "RightOf"  (the default)
    "LeftOf"
    "Above"
    "Below"
    "SamePositionAs"
```

When "SamePositionAs" is specified, all display devices will be assigned an offset of 0,0. For backwards compatibility, "Clone" is a synonym for "SamePositionAs".

Because it is often unclear which display device relates to which, MetaModeOrientation can be confusing. You can further clarify the MetaModeOrientation with display device names to indicate which display device is positioned relative to which display device. For example:

``` screen
    "CRT-0 LeftOf DFP-0"
```

ConnectedMonitor
With this option you can override what the NVIDIA kernel module detects is connected to your graphics card. This may be useful, for example, if any of your display devices do not support detection using Display Data Channel (DDC) protocols. Valid values are a comma-separated list of display device names; for example:

``` screen
    "CRT-0, CRT-1"
    "CRT"
    "CRT-1, DFP-0"
```

WARNING: this option overrides what display devices are detected by the NVIDIA kernel module, and is very seldom needed. You really only need this if a display device is not detected, either because it does not provide DDC information, or because it is on the other side of a KVM (Keyboard-Video-Mouse) switch. In most other cases, it is best not to specify this option.

Just as in all X config entries, spaces are ignored and all entries are case insensitive.

<table style="width:1%;" data-border="0" data-summary="Q and A Set">
<colgroup>
<col style="width: 1%" />
</colgroup>
<tbody>
<tr class="qandadiv">
<td style="text-align: left;" data-valign="top">
<h3 id="frequently-asked-twinview-questions" class="title">12.1. Frequently Asked TwinView Questions</h3></td>
</tr>
<tr class="question">
<td style="text-align: left;" data-valign="top"></td>
</tr>
<tr class="answer">
<td style="text-align: left;" data-valign="top"></td>
</tr>
<tr class="question">
<td style="text-align: left;" data-valign="top"></td>
</tr>
<tr class="answer">
<td style="text-align: left;" data-valign="top"></td>
</tr>
<tr class="question">
<td style="text-align: left;" data-valign="top"></td>
</tr>
<tr class="answer">
<td style="text-align: left;" data-valign="top"></td>
</tr>
<tr class="question">
<td style="text-align: left;" data-valign="top"></td>
</tr>
<tr class="answer">
<td style="text-align: left;" data-valign="top"></td>
</tr>
</tbody>
</table>
