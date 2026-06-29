With the release (and beta) of OBS 28, there is now a new AMD AMF Encoder implementation named "AMD HW".
You'll find it in both H.264 and HEVC flavors.

The new implementation includes a more up to date AMF version, and simplifies the interface/settings drastically.
![image](https://user-images.githubusercontent.com/50419942/183417894-f4b458b1-b8b1-4253-837e-d800fc2f4e78.png)


***
## Max Throughput 
There is a check in place to query the encoder for how much throughput its able to handle. This is mainly to guard older and lower end GPUs from performance issues.
If a user tries to do 4k resolution at 60fps, and the GPU is not able to handle it at the "Quality" preset, then it will automatically drop to a faster preset, which can be observed in the OBS log. If the driver/hardware is not able to deliver this throughput information, it defaults to "balanced".

## AMF/FFmpeg Options
It is recommend to use the defaults. There is no "best settings" that will fit every scenario, hardware and intent.

There are times where it could be useful to make some adjustments to the default, and that can be done in this field.

![image](https://user-images.githubusercontent.com/50419942/183474036-974951c4-2135-4338-bfa5-9bda8eba5a86.png)

The input needs to be formatted as such: `parameter=value parameter=value` (space between each). For instance `RateControlPreanalysisEnable=false EnableVBAQ=false`

[Simplified list of AMF options.](https://github.com/obsproject/obs-studio/wiki/AMF-Options)

# Examples

### B-frames
Only RDNA2 and beyond (RX 6000+) have access to B-Frames.

B-Frames are tiny small in size but lower-quality. In theory, they boost the quality of motion scenes by allowing more bits to be dedicated to I- and P-frames by saving bits; see this [Big Buck Bunny benchmark](https://codecalamity.com/amd-re-introduces-the-b-frame/). In practice, high-motion gaming footage with fast head turns easily defeat B-frames.

More B-frames is slower to encode. More is not necessarily better, so try 1 or 2 first (for 30 fps; maybe scale it for more, e.g. 4 for 120 fps).

### Pre Analysis
This option is disabled by default, and it has some impact on GPU performance. If you're running games + obs, please be aware that in-game performance will take an additional\* hit if this is enabled. It disables "VBAQ"; the PAQ component of pre-analysis is supposed to  provide a similar benefit.

\*: Regular video encode runs on a separate part (VCE/VCN) of the AMD GPU. Pre-analysis needs to use the graphical part to work.

It essentially works a bit like pseudo two-pass for a short number of frames, and will analyze the incoming video frames to try to make better decisions. Pre-analysis provides scene change detection (so key/intra frames are inserted as needed, reducing the blur spike on e.g. closing a game’s the map interface), offers general improvements of quantization decisions on image (if PAQ is enabled) and motion (if high-motion quality boost is enabled).

Ref:
* [AMF PreAnalysis Doc](https://github.com/GPUOpen-LibrariesAndSDKs/AMF/blob/master/amf/doc/AMF_Video_PreAnalysis_API.md)

### Other
VBAQ (Variance Based Adaptive Quantization). Set using `EnableVBAQ=true/false`.

Explanation: Adaptive quantization. Tries to prioritize bits to parts of the image human vision tend to care about. Similar to "Psycho Visual Tuning" on the NVIDIA side.

# Defaults
It is recommended to try the default settings first as it tries to strike balance between quality and performance. Should you run into performance or image quality issues, please try with the defaults first (remove any extra options).

As a baseline the encoder uses the defaults of AMF (see [AMF docs](https://github.com/GPUOpen-LibrariesAndSDKs/AMF/blob/master/amf/doc/AMF_Video_Encode_API.pdf)).

In addition, OBS makes the following adjustments to the defaults:

## H264    
Option | Value | 
-- | -- |
VBAQ | True
Enforce HRD | True
High Motion Quality Boost | False
Deblocking Filter | True
Low Latency Mode | False
CABAC | True
RateControlPreAnalysis (Pre-Encode) | True
B-frames | 0

## HEVC    
Option | Value | 
-- | -- |
VBAQ | True
Enforce HRD | True
High Motion Quality Boost | False
Low Latency Mode | False