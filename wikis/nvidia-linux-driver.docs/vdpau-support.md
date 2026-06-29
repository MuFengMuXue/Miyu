## Appendix G. VDPAU Support

## Implementation Limits

VDPAU is specified as a generic API - the choice of which features to support, and performance levels of those features, is left up to individual implementations. The details of NVIDIA's implementation are provided below.

### VdpVideoSurface

The maximum supported resolution is 8192x8192 for GPUs with VDPAU feature sets H and I, and 4096x4096 for all other GPUs.

The following surface formats and get-/put-bits combinations are supported:

- VDP_CHROMA_TYPE_420 (Supported get-/put-bits formats are VDP_YCBCR_FORMAT_NV12, VDP_YCBCR_FORMAT_YV12)

- VDP_CHROMA_TYPE_422 (Supported get-/put-bits formats are VDP_YCBCR_FORMAT_UYVY, VDP_YCBCR_FORMAT_YUYV)

### VdpBitmapSurface

The maximum supported resolution is 16384x16384 pixels.

The following surface formats are supported:

- VDP_RGBA_FORMAT_B8G8R8A8

- VDP_RGBA_FORMAT_R8G8B8A8

- VDP_RGBA_FORMAT_B10G10R10A2

- VDP_RGBA_FORMAT_R10G10B10A2

- VDP_RGBA_FORMAT_A8

Note that VdpBitmapSurfaceCreate's frequently_accessed parameter directly controls whether the bitmap data will be placed into video RAM (VDP_TRUE) or system memory (VDP_FALSE). Note that if the bitmap data cannot be placed into video RAM when requested due to resource constraints, the implementation will automatically fall back to placing the data into system RAM.

### VdpOutputSurface

The maximum supported resolution is 16384x16384 pixels.

The following surface formats are supported:

- VDP_RGBA_FORMAT_B8G8R8A8

- VDP_RGBA_FORMAT_R10G10B10A2

For all surface formats, the following get-/put-bits indexed formats are supported:

- VDP_INDEXED_FORMAT_A4I4

- VDP_INDEXED_FORMAT_I4A4

- VDP_INDEXED_FORMAT_A8I8

- VDP_INDEXED_FORMAT_I8A8

For all surface formats, the following get-/put-bits YCbCr formats are supported:

- VDP_YCBCR_FORMAT_Y8U8V8A8

- VDP_YCBCR_FORMAT_V8U8Y8A8

### VdpDecoder

In all cases, VdpDecoder objects solely support 8-bit 4:2:0 streams, and only support writing to VDP_CHROMA_TYPE_420 surfaces.

The exact set of supported VdpDecoderProfile values depends on the GPU in use. [Appendix A, *Supported NVIDIA GPU Products*](supportedchips.html "Appendix A. Supported NVIDIA GPU Products") lists which GPUs support which video feature set. An explanation of each video feature set may be found below. When reading these lists, please note that VC1_SIMPLE and VC1_MAIN may be referred to as WMV, WMV3, or WMV9 in other contexts. Partial acceleration means that VLD (bitstream) decoding is performed on the CPU, with the GPU performing IDCT and motion compensation. Complete acceleration means that the GPU performs all of VLD, IDCT, and motion compensation.

#### VDPAU Feature Sets A and B

GPUs with VDPAU feature sets A and B are not supported by this driver.

#### VDPAU Feature Sets C, D, and E

GPUs with VDPAU feature set C, D, or E support at least the following VdpDecoderProfile values, and associated limits:

- VDP_DECODER_PROFILE_MPEG1, VDP_DECODER_PROFILE_MPEG2_SIMPLE, VDP_DECODER_PROFILE_MPEG2_MAIN:

  - Complete acceleration.

  - Minimum width or height: 3 macroblocks (48 pixels).

  - Maximum width or height: 128 macroblocks (2048 pixels) for feature set C, 252 macroblocks (4032 pixels) wide by 253 macroblocks (4048 pixels) high for feature set D, 255 macroblocks (4080 pixels) for feature set E.

  - Maximum macroblocks: 8192 for feature set C, 65536 for feature sets D or E.

- VDP_DECODER_PROFILE_H264_MAIN, VDP_DECODER_PROFILE_H264_HIGH, VDP_DECODER_PROFILE_H264_CONSTRAINED_BASELINE, VDP_DECODER_PROFILE_H264_PROGRESSIVE_HIGH, VDP_DECODER_PROFILE_H264_CONSTRAINED_HIGH:

  - Complete acceleration.

  - Minimum width or height: 3 macroblocks (48 pixels).

  - Maximum width or height: 128 macroblocks (2048 pixels) for feature set C, 252 macroblocks (4032 pixels) wide by 255 macroblocks (4080 pixels) high for feature set D, 256 macroblocks (4096 pixels) for feature set E.

  - Maximum macroblocks: 8192 for feature set C, 65536 for feature sets D or E.

- VDP_DECODER_PROFILE_H264_BASELINE, VDP_DECODER_PROFILE_H264_EXTENDED:

  - Partial acceleration. The NVIDIA VDPAU implementation does not support flexible macroblock ordering, arbitrary slice ordering, redundant slices, data partitioning, SI slices, or SP slices. Content utilizing these features may decode with visible corruption.

  - Minimum width or height: 3 macroblocks (48 pixels).

  - Maximum width or height: 128 macroblocks (2048 pixels) for feature set C, 252 macroblocks (4032 pixels) wide by 255 macroblocks (4080 pixels) high for feature set D, 256 macroblocks (4096 pixels) for feature set E.

  - Maximum macroblocks: 8192 for feature set C, 65536 for feature sets D or E.

- VDP_DECODER_PROFILE_VC1_SIMPLE, VDP_DECODER_PROFILE_VC1_MAIN, VDP_DECODER_PROFILE_VC1_ADVANCED:

  - Complete acceleration.

  - Minimum width or height: 3 macroblocks (48 pixels).

  - Maximum width or height: 128 macroblocks (2048 pixels).

  - Maximum macroblocks: 8190

- VDP_DECODER_PROFILE_MPEG4_PART2_SP, VDP_DECODER_PROFILE_MPEG4_PART2_ASP, VDP_DECODER_PROFILE_DIVX4_QMOBILE, VDP_DECODER_PROFILE_DIVX4_MOBILE, VDP_DECODER_PROFILE_DIVX4_HOME_THEATER, VDP_DECODER_PROFILE_DIVX4_HD_1080P, VDP_DECODER_PROFILE_DIVX5_QMOBILE, VDP_DECODER_PROFILE_DIVX5_MOBILE, VDP_DECODER_PROFILE_DIVX5_HOME_THEATER, VDP_DECODER_PROFILE_DIVX5_HD_1080P

  - Complete acceleration.

  - Minimum width or height: 3 macroblocks (48 pixels).

  - Maximum width or height: 128 macroblocks (2048 pixels).

  - Maximum macroblocks: 8192

  The following features are currently not supported:

  - GMC (Global Motion Compensation)

  - Data partitioning

  - reversible VLC

These GPUs also support VDP_VIDEO_MIXER_FEATURE_HIGH_QUALITY_SCALING_L1.

GPUs with VDPAU feature set E support an enhanced error concealment mode which provides more robust error handling when decoding corrupted video streams. This error concealment is on by default, and may have a minor CPU performance impact in certain configurations. To disable this, set the environment variable VDPAU_NVIDIA_DISABLE_ERROR_CONCEALMENT to 1.

#### VDPAU Feature Set F

GPUs with VDPAU feature set F support all of the same VdpDecoderProfile values and other features as VDPAU feature set E. Feature set F adds:

- VDP_DECODER_PROFILE_HEVC_MAIN, VDP_DECODER_PROFILE_HEVC_MAIN_10:

  - Complete acceleration.

  - Minimum width or height: 128 luma samples (pixels).

  - Maximum width or height: 4096 luma samples (pixels) wide by 2304 luma samples (pixels) tall.

  - Maximum macroblocks: not applicable.

- VDP_DECODER_PROFILE_VP9_PROFILE_0:

  - Complete acceleration.

  - Minimum width or height: 128 luma samples (pixels).

  - Maximum width or height: 4096 luma samples (pixels) wide by 2304 luma samples (pixels) tall.

  - Maximum macroblocks: not applicable.

#### VDPAU Feature Set G

GPUs with VDPAU feature set G support all of the same VdpDecoderProfile values and other features as VDPAU feature set F. Feature set G adds:

- VDP_DECODER_PROFILE_HEVC_MAIN_12:

  - Complete acceleration.

  - Minimum width or height: 128 luma samples (pixels).

  - Maximum width or height: 4096 luma samples (pixels) wide by 4096 luma samples (pixels) tall.

  - Maximum macroblocks: not applicable.

#### VDPAU Feature Set H

GPUs with VDPAU feature set H support all of the same VdpDecoderProfile values and other features as VDPAU feature set G. Feature set H adds:

- VDP_DECODER_PROFILE_HEVC_MAIN, VDP_DECODER_PROFILE_HEVC_MAIN_10 VDP_DECODER_PROFILE_HEVC_MAIN_12:

  - Complete acceleration.

  - Minimum width or height: 128 luma samples (pixels).

  - Maximum width or height: 8192 luma samples (pixels) wide by 8192 luma samples (pixels) tall.

  - Maximum macroblocks: not applicable.

- VDP_DECODER_PROFILE_VP9_PROFILE_0, VDP_DECODER_PROFILE_VP9_PROFILE_2:

  - Complete acceleration.

  - Minimum width or height: 128 luma samples (pixels).

  - Maximum width or height: 8192 luma samples (pixels) wide by 8192 luma samples (pixels) tall.

  - Maximum macroblocks: not applicable.

#### VDPAU Feature Set I

GPUs with VDPAU feature set I support all of the same VdpDecoderProfile values and other features as VDPAU feature set H.

#### VDPAU Feature Set J

GPUs with VDPAU feature set J support all of the same VdpDecoderProfile values and other features as VDPAU feature set H. Feature set J adds:

- VDP_DECODER_PROFILE_HEVC_MAIN_444, VDP_DECODER_PROFILE_HEVC_MAIN_444_10 VDP_DECODER_PROFILE_HEVC_MAIN_444_12:

  - Complete acceleration.

  - Minimum width or height: 128 luma samples (pixels).

  - Maximum width or height: 8192 luma samples (pixels) wide by 8192 luma samples (pixels) tall.

  - Maximum macroblocks: not applicable.

#### VDPAU Feature Set K

GPUs with VDPAU feature set K support all of the same VdpDecoderProfile values and other features as VDPAU feature set J.Feature set K adds:

- VDP_DECODER_PROFILE_AV1_MAIN:

  - Complete acceleration.

  - Minimum width or height: 128 luma samples (pixels).

  - Maximum width or height: 8192 luma samples (pixels) wide by 8192 luma samples (pixels) tall.

  - Maximum macroblocks: not applicable.

#### VDPAU Features Note 2

Note that all GPUs with VDPAU feature sets H and above, except GPUs with this note, support VDP_DECODER_PROFILE_VP9_PROFILE_2. Please check "VDPAU information" page in nvidia-settings for the list of supported profiles.

#### VDPAU Features Note 3

Note that codec support may vary by product manufacturer and region. For further details, please consult the documentation provided by the Add-In Card manufacturer or system manufacturer of your product.

### VdpVideoMixer

The maximum supported resolution is 8192x8192 for GPUs with VDPAU feature set H, and 4096x4096 for all other GPUs.

The video mixer supports all video and output surface resolutions and formats that the implementation supports.

The video mixer supports at most 4 auxiliary layers.

The following features are supported:

- VDP_VIDEO_MIXER_FEATURE_DEINTERLACE_TEMPORAL

- VDP_VIDEO_MIXER_FEATURE_DEINTERLACE_TEMPORAL_SPATIAL

- VDP_VIDEO_MIXER_FEATURE_INVERSE_TELECINE

- VDP_VIDEO_MIXER_FEATURE_NOISE_REDUCTION

- VDP_VIDEO_MIXER_FEATURE_SHARPNESS

- VDP_VIDEO_MIXER_FEATURE_LUMA_KEY

In order for either VDP_VIDEO_MIXER_FEATURE_DEINTERLACE_TEMPORAL or VDP_VIDEO_MIXER_FEATURE_DEINTERLACE_TEMPORAL_SPATIAL to operate correctly, the application must supply at least 2 past and 1 future fields to each VdpMixerRender call. If those fields are not provided, the VdpMixer will fall back to bob de-interlacing.

Both regular de-interlacing and half-rate de-interlacing are supported. Both have the same requirements in terms of the number of past/future fields required. Both modes should produce equivalent results.

In order for VDP_VIDEO_MIXER_FEATURE_INVERSE_TELECINE to have any effect, one of VDP_VIDEO_MIXER_FEATURE_DEINTERLACE_TEMPORAL or VDP_VIDEO_MIXER_FEATURE_DEINTERLACE_TEMPORAL_SPATIAL must be requested and enabled. Inverse telecine has the same requirement on the minimum number of past/future fields that must be provided. Inverse telecine will not operate when "half-rate" de-interlacing is used.

While it is possible to apply de-interlacing algorithms to progressive streams using the techniques outlined in the VDPAU documentation, NVIDIA does not recommend doing so. One is likely to introduce more artifacts due to the inverse telecine process than are removed by detection of bad edits etc.

### VdpPresentationQueue

The resolution of VdpTime is approximately 10 nanoseconds. At some arbitrary point during system startup, the initial value of this clock is synchronized to the system's real-time clock, as represented by nanoseconds since since Jan 1, 1970. However, no attempt is made to keep the two time-bases synchronized after this point. Divergence can and will occur.

NVIDIA's VdpPresentationQueue supports two methods for displaying surfaces; overlay and blit. The overlay method will be used wherever possible, with the blit method acting as a more general fallback.

Whenever a presentation queue is created, the driver determines whether the overlay method may ever be used, based on system configuration, and whether any other application already owns the overlay. If overlay usage is potentially possible, the presentation queue is marked as owning the overlay.

Whenever a surface is displayed, the driver determines whether the overlay method may be used for that frame, based on both whether the presentation queue owns the overlay, and the set of overlay usage limitations below. In other words, the driver may switch back and forth between overlay and blit methods dynamically. The most likely cause for dynamic switching is when a compositing manager is enabled or disabled, and the window becomes redirected or unredirected.

The following conditions or system configurations will prevent usage of the overlay path:

- Overlay hardware already in use, e.g. by another VDPAU, GL, or X11 application.

- Desktop rotation enabled on the given X screen.

- The presentation target window is redirected, due to a compositing manager actively running.

- The environment variable VDPAU_NVIDIA_NO_OVERLAY is set to a string representation of a non-zero integer.

- The driver determines that the performance requirements of overlay usage cannot be met by the current hardware configuration.

Both the overlay and blit methods sync to VBLANK. The overlay path is guaranteed never to tear, whereas the blit method is classed as "best effort".

When TwinView is enabled, the blit method can only sync to one of the display devices; this may cause tearing corruption on the display device to which VDPAU is not syncing. You can use the environment variable VDPAU_NVIDIA_SYNC_DISPLAY_DEVICE to specify the display device to which VDPAU should sync. You should set this environment variable to the name of a display device, for example "CRT-1". Look for the line "Connected display device(s):" in your X log file for a list of the display devices present and their names. You may also find it useful to review [Chapter 12, *Configuring Multiple Display Devices on One X Screen*](configtwinview.html "Chapter 12. Configuring Multiple Display Devices on One X Screen") "Configuring Twinview" and the section on Ensuring Identical Mode Timings in [Chapter 18, *Programming Modes*](programmingmodes.html "Chapter 18. Programming Modes").

A VdpPresentationQueue allows a maximum of 8 surfaces to be QUEUED or VISIBLE at any one time. This limit is per presentation queue. If this limit is exceeded, VdpPresentationQueueDisplay blocks until an entry in the presentation queue becomes free.

## Performance Levels

This documentation describes the capabilities of the NVIDIA VDPAU implementation. Hardware performance may vary significantly between cards. No guarantees are made, nor implied, that any particular combination of system configuration, GPU configuration, VDPAU feature set, VDPAU API usage, application, video stream, etc., will be able to decode streams at any particular frame rate.

## Getting the Best Performance from the API

System performance (raw throughput, latency, and jitter tolerance) can be affected by a variety of factors. One of these factors is how the client application uses VDPAU; i.e. the number of surfaces allocated for buffering, order of operations, etc.

NVIDIA GPUs typically contain a number of separate hardware modules that are capable of performing different parts of the video decode, post-processing, and display operations in parallel. To obtain the best performance, the client application must attempt to keep all these modules busy with work at all times.

Consider the decoding process. At a bare minimum, the application must allocate one video surface for each reference frame that the stream can use (2 for MPEG or VC-1, a variable stream-dependent number for H.264) plus one surface for the picture currently being decoded. However, if this minimum number of surfaces is used, performance may be poor. This is because back-to-back decodes of non-reference frames will need to be written into the same video surface. This will require that decode of the second frame wait until decode of the first has completed; a pipeline stall.

Further, if the video surfaces are being read by the video mixer for post-processing, and eventual display, this will "lock" the surfaces for even longer, since the video mixer needs to read the data from the surface, which prevents any subsequent decode operations from writing to the surface. Recall that when advanced de-interlacing techniques are used, a history of video surfaces must be provided to the video mixer, thus necessitating that even more video surfaces be allocated.

For this reason, NVIDIA recommends the following number of video surfaces be allocated:

- (num_ref + 3) for progressive content, and no de-interlacing.

- (num_ref + 5) for interlaced content using advanced de-interlacing.

Next, consider the display path via the presentation queue. This portion of the pipeline requires at least 2 output surfaces; one that is being actively displayed by the presentation queue, and one being rendered to for subsequent display. As before, using this minimum number of surfaces may not be optimal. For some video streams, the hardware may only achieve real-time decoding on average, not for each individual frame. Using compositing APIs to render on-screen displays, graphical user interfaces, etc., may introduce extra jitter and latency into the pipeline. Similarly, system level issues such as scheduler algorithms and system load may prevent the CPU portion of the driver from operating for short periods of time. All of these potential issues may be solved by allocating more output surfaces, and queuing more than one outstanding output surface into the presentation queue.

The reason for using more than the minimum number of video surfaces is to ensure that the decoding and post-processing pipeline is not stalled, and hence is kept busy for the maximum amount of time possible. In contrast, the reason for using more than the minimum number of output surfaces is to hide jitter and latency in various GPU and CPU operations.

The choice of exactly how many surfaces to allocate is a resource usage v.s. performance trade-off; Allocating more than the minimum number of surfaces will increase performance, but use proportionally more video RAM. This may cause allocations to fail. This could be particularly problematic on systems with a small amount of video RAM. A stellar application would automatically adjust to this by initially allocating the bare minimum number of surfaces (failures being fatal), then attempting to allocate more and more surfaces, provided the allocations kept succeeding, up to the suggested limits above.

The video decoder's memory usage is also proportional to the maximum number of reference frames specified at creation time. Requesting a larger number of reference frames can significantly increase memory usage. Hence it is best for applications that decode H.264 to request only the actual number of reference frames specified in the stream, rather than e.g. hard-coding a limit of 16, or even the maximum number of surfaces allowable by some specific H.264 level at the stream's resolution.

Note that the NVIDIA implementation correctly implements all required interlocks between the various pipelined hardware modules. Applications never need worry about correctness (providing their API usage is legal and sensible), but simply have to worry about performance.

## Additional Notes

Note that output and bitmap surfaces are not cleared to any specific value upon allocation. It is the application's responsibility to initialize all surfaces prior to using them as input to any function. Video surfaces are cleared to black upon allocation.

## Debugging and Tracing

The VDPAU wrapper library supports tracing VDPAU function calls, and their parameters. This tracing is controlled by the following environment variables:

VDPAU_TRACE
Enables tracing. Set to 1 to trace function calls. Set to 2 to trace all arguments passed to the function.

VDPAU_TRACE_FILE
Filename to write traces to. By default, traces are sent to stderr. This variable may either contain a plain filename, or a reference to an existing open file-descriptor in the format "&N" where N is the file descriptor number.

The VDPAU wrapper library is responsible for determining which vendor-specific driver to load for a given X11 display/screen. At present, it hard-codes "nvidia" as the driver. The environment variable VDPAU_DRIVER may be set to override this default. The actual library loaded will be libvdpau\_\${VDPAU_DRIVER}.so. Setting VDPAU_DRIVER to "trace" is not advised.

The NVIDIA VDPAU driver can emit some diagnostic information when an error occurs. To enable this, set the environment variable VDPAU_NVIDIA_DEBUG. A value of 1 will request a small diagnostic that will enable NVIDIA engineers to locate the source of the problem. A value of 3 will request that a complete stack backtrace be printed, which provide NVIDIA engineers with more detailed information, which may be needed to diagnose some problems.

## Multi-threading

VDPAU supports multiple threads actively executing within the driver, subject to certain limitations.

If any object is being created or destroyed, the VDPAU driver will become single-threaded. This includes object destruction during preemption cleanup.

Otherwise, up to one thread may actively execute VdpDecoderRender per VdpDecoder object, and up to one thread may actively execute any other rendering API per VdpDevice (or child) object. Note that the driver enforces these restrictions internally; applications are not required to implement the rules outlined above.

Finally, some of the "query" or "get" APIs may actively execute irrespective of the number of rendering threads currently executing.

## Xwayland support in VDPAU

The NVIDIA VDPAU driver supports running within the X Window System: either on the native X.org X server, or on the Xwayland X server within an Xwayland environment. VDPAU applications do not have to change their VDPAU API usage depending on the X server.

### Requirements

In order to make use of Xwayland for decode and presentation purposes, certain requirements need to be satisfied. See section "39B. REQUIREMENTS" for the list of requirements.

### Known issues

- The current implementation of VDPAU with Xwayland does not honor the "Presentation Time Stamp" passed by the application to the VDPAU driver.

- The NVIDIA VDPAU driver running in an Xwayland environment in some cases may lead to corruption and flickering during a video playback. This is a known issue and is tracked by: https://gitlab.freedesktop.org/xorg/xserver/-/issues/1317
