Parameters and options are written as such in the config window:

`Usage=transcoding Quality=speed`

Parameter types:

* i = int (whole number),
  * enum is also whole number. technically means something non-numeric, but...
* b = boolean (true/false),
* s = string

This table is currently only reasonably complete for H.264. Reasonably, as in "options that matter".

## H.264

### General

Parameter | Options | Default | Explanation
-- | -- | -- | --
**Usage**| transcoding, ultralowlatency, lowlatency, webcam, hq, hqll | Transcoding | Changes a lot of settings based on usage. Highly recommend sticking to "transcoding".
**Quality**| speed, balanced, quality | Quality | Controls the speed vs quality. **Note: Can fall back to faster presets if throughput is too high vs max throughput.**
**Profile**| main, high, constrained_baseline, constrained_high | High | h264 profile. "High" should work for all modern devices (think iphone 4 and later).
**ProfileLevel** | i (10-62) | 42 (4.2) | H264 profile level. Specifies constraints for decode.
**MaxNumRefFrames** | i | 4 | Limits the max number of reference frames (0-16). This max is also limited by hardware and h264 levels. More ref frames means more encoder work, but potentially better compression. Stick to 4 or less, for the sake of compatibility and profile conformity. The encoder is currently likely to use a single reference frame unless b-frames are active.

### Rate Control
Parameter | Options | Default | Explanation
-- | -- | -- | --
**RateControlPreanalysisEnable** | enum (0 or 1) | 1 (enabled) | Pre-encode assisted rate control.
**EnforceHRD** | b | True | Enforce Hypothetical Reference Decoder. Constraints on QP variation within a picture to meet HRD requirements.
**FillerDataEnable** | b | False (True if CBR) | Filler data. Useful for strict CBR encoding, like live streaming.
**VBVBufferSize** | i | N/A | Note: in bits (bps)
**InitialVBVBufferFullness** | i | 64 (100%) | Note: 0=0%, 64=100%
**PeakBitrate** | i | N/A | Note: in bits (bps)
**MinQP** | i | 0 | 
**MaxQP** | i | 51 | 

### B-Frames
**B-Frames and its features currently require RDNA2 (RX 6000 and higher). Seems to currently cause some issues, try `BPicturesPattern` set to 1 or 2. Only H.264 has B-frame support.**
Parameter | Options | Default | Explanation
-- | -- | -- | --
**MaxConsecutiveBPictures** | I (0-3) | 3 (if supported) | Max consecutive b-frames. Is overridden by `BPicturesPattern=0`.
**BPicturesPattern** | i (0-3) | 0 | Sets the number of consecutive b-frames per GOP (area between two i-frames). 0=off.
**AdaptiveMiniGOP** | b | False | Variable amount of b-frames between p-frames. **Note: Might require Pre-Analysis, or at least works better with it.**
**BReferenceEnable** | b | True | Enable/Disable the use of b-frames as reference frames.

### Psy
Parameter | Options | Default | Explanation
-- | -- | -- | --
**DeBlockingFilter** | b | True | Enable/Disable the de-blocking filter. Only for H.264.
**EnableVBAQ** | b | True (Unless CQP) | Adaptive quantization (H.264). Prioritize bits to parts of the image humans care about.
**HighMotionQualityBoostEnable** | b | False | 

### Motion Estimation
Parameter | Options | Default | Explanation
-- | -- | -- | --
**HalfPixel** | b | True | 
**QuarterPixel** | b | True

## H.265

Parameter | Options | Default | Explanation
-- | -- | -- | --
**Usage**| transcoding, ultralowlatency, lowlatency, webcam, hq, hqll | Transcoding | Changes a lot of settings based on usage. Highly recommend sticking to "transcoding".
**Quality**| speed, balanced, quality | Quality | Controls the speed vs quality. **Note: Can fall back to faster presets if throughput is too high vs max throughput.**
**Profile**| main, main10| main | h265 profile. main10 is for 10-bit (HDR).
**Tier**|main, high|high|h265 tier.
**ProfileLevel** | i (10-62) | 62 (6.2) | H264 profile level. Specifies constraints for decode.

This above is a (still incomplete) list of main options. Some are really specific to H.265. Others are basically the same, but with an annoying name prefix. For example, `EnableVBAQ` becomes `HevcEnableVBAQ`. Use the AMF documentation linked below in "See also".

## AV1

Parameter | Options | Default | Explanation
-- | -- | -- | --
**Usage**| transcoding, ultralowlatency, lowlatency, webcam, hq, hqll | Transcoding | Changes a lot of settings based on usage. Highly recommend sticking to "transcoding".
**Quality**| speed, balanced, quality | Quality | Controls the speed vs quality. **Note: Can fall back to faster presets if throughput is too high vs max throughput.**
**Profile**| main | main | av1 profile. Can only be main.
**ProfileLevel** | i (20-73) | 62 (6.2) | AV1 profile level. Specifies constraints for decode.

Same deal here: some options really specific, others renamed. 

## Pre-Analysis
Parameter | Options | Default | Explanation
-- | -- | -- | --
**EnablePreAnalysis** | b | False | Pseudo 2-pass for a certain number of frames. Enabling will disable VBAQ. GPU load hit (spends traditional 3d/render resources). This is the _only_ PA property that gets affected by codec names (`EnablePreAnalysis` for H.264, `HevcEnablePreAnalysis` for H.265, `Av1EnablePreAnalysis` for AV1).
**PASceneChangeDetectionEnable** | b | True | Akin to scenecut (adaptive I-frame insertion). Safest to disable for HLS transcode platforms, as is potentially risky for muxer segment/split.
**PAFrameSadEnable** | b | True | Frame SAD (Sum of Absolute Difference) algorithm
**PALookAheadBufferDepth** | i | 0 | Pre-Analysis lookahead buffer size
**PAPerceptualAQMode** | Enum 0/1 | 0 (None, off) | PA Perceptual adaptive quantization mode.
**PATemporalAQMode** | Enum 0-2 | 0 (None, off) | PA Temporal adaptive quantization mode. 1 for non-gaming applications, 2 gaming applications.
**PAHighMotionQualityBoostMode** | Enum 0/1 | 0 (None, off) | PA High motion quality boost mode
**PACAQStrength** | Enum (0-2) | 1 (medium) | 0=low, 1=med, 2=high. Content Adaptive Quantization (CAQ) strength

## References
### AMF documentation
All the parameter names come directly from the AMD AMF library at https://github.com/GPUOpen-LibrariesAndSDKs/AMF/tree/master/amf. For example, to find how `PATemporalAQMode` is defined, simply use the search box on top to look for `PATemporalAQMode` in the code. That will bring you to a `#define AMF_PA_TAQ_MODE`, so you go on and search for `AMF_PA_TAQ_MODE` in the documentation.

AMF documentation corresponding to sections of this page:
* "General", "Rate Control", "B frame", "Psy", "Motion Estimation" are documented in codec-specific pages. See [AMF_Video_Encode_API.md](https://github.com/GPUOpen-LibrariesAndSDKs/AMF/blob/master/amf/doc/AMF_Video_Encode_API.md), [AMF_Video_Encode_HEVC_API.md](https://github.com/GPUOpen-LibrariesAndSDKs/AMF/blob/master/amf/doc/AMF_Video_Encode_HEVC_API.md), [AMF_Video_Encode_AV1_API.md](https://github.com/GPUOpen-LibrariesAndSDKs/AMF/blob/master/amf/doc/AMF_Video_Encode_AV1_API.md)
* "Pre-Analysis" is its own component, documented in [AMF_Video_PreAnalysis_API.md](https://github.com/GPUOpen-LibrariesAndSDKs/AMF/blob/master/amf/doc/AMF_Video_PreAnalysis_API.md). It is not dependent on the choice of codec.

The AMF documentation uses `#define` names for parameters and values. Use the search box on top to convert them into the `L"string"` names.

## TODOs
* Evaluate the "HQ" usage mode, which sacrifices throughput for quality.