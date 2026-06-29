相关文章

  * [Convert FLAC to MP3#With FFmpeg](</wzh/index.php?title=Convert_FLAC_to_MP3&action=edit&redlink=1> "Convert FLAC to MP3（页面不存在）")

**翻译状态：**

  * 本文（或部分内容）译自 [FFmpeg](<https://wiki.archlinux.org/title/FFmpeg> "arch:FFmpeg")，最近一次同步于 2024-01-19，若英文版本有所[更改](<https://wiki.archlinux.org/title/FFmpeg?diff=0&oldid=793884>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/FFmpeg_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

摘自项目[主页](<https://www.ffmpeg.org/>)： 

    FFmpeg 是一个完整的跨平台音视频录制、转换及串流方案。它包含了 libavcodec - 业界领先的音视频编解码器库。

##  安装

**注意：** 你可能会碰到像是 _libav_ 或是 _avconv_ 这样的 FFmpeg 分支，可以参考博客 [FFmpeg/Libav 现状](<http://blog.pkh.me/p/13-the-ffmpeg-libav-situation.html>)一文来了解各项目区别及 FFmpeg 的现状。

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [ffmpeg](<https://archlinux.org/packages/?name=ffmpeg>)包 包。 

如需开发版本，可安装 [ffmpeg-git](<https://aur.archlinux.org/packages/ffmpeg-git/>)AUR。同时另有 [ffmpeg-full](<https://aur.archlinux.org/packages/ffmpeg-full/>)AUR，它尽可能地提供了所有可用的的可选特性。 

##  编码案例

**注意：**

  * 将参数按顺序排列非常重要（像是 输入，视频，过滤器，音频，输出）。不这么做可能导致参数被略过，或是使 FFmpeg 无法运行。
  * FFmpeg 应该自动使用所有 CPU 线程。但你也可以通过 `-threads _number_` 参数指定使用的线程数。

参考 [FFmpeg 编码维基](<https://trac.ffmpeg.org/wiki#Encoding>)和 [ffmpeg(1) § EXAMPLES](<https://man.archlinux.org/man/ffmpeg.1#EXAMPLES>)。 

###  屏幕捕获

FFmpeg 包含了 [x11grab](<https://www.ffmpeg.org/ffmpeg-devices.html#x11grab>) 及 [ALSA](<https://www.ffmpeg.org/ffmpeg-devices.html#alsa-1>) 虚拟设备，可用于捕获用户的全部音频及显示输入。 

使用如下命令创建截图 `screen.png`： 
    
    $ ffmpeg -f x11grab -video_size 1920x1080 -i $DISPLAY -vframes 1 screen.png
    
其中 `-video_size` 指定了截图区域大小。 

使用如下命令创建无损编码且不含音频的录屏 `screen.mkv`： 
    
    $ ffmpeg -f x11grab -video_size 1920x1080 -framerate 25 -i $DISPLAY -c:v ffvhuff screen.mkv
    
这里使用了 Huffyuv 编码器，速度很快，但输出文件体积非常大。 

使用如下命令创建有损编码且包含音频的录屏 `screen.mp4`： 
    
    $ ffmpeg -f x11grab -video_size 1920x1080 -framerate 25 -i $DISPLAY -f alsa -i default -c:v libx264 -preset ultrafast -c:a aac screen.mp4
    
这里使用了 x264 编码器及最快编码速度选项。你也可以使用其它编码器；如果由于磁盘速度低或是编码速度慢导致帧写入速度太慢，帧率将会下降，导致输出的视频出现卡顿。 

If the video stream should not be saved as a file, but used as a virtual webcam for screen sharing purposes, see [v4l2loopback#Casting X11 using FFmpeg](</wzh/index.php?title=V4l2loopback&action=edit&redlink=1> "V4l2loopback（页面不存在）"). 

另外可参考[官方文档](<https://trac.ffmpeg.org/wiki/Capture/Desktop#Linux>)。 

###  录制摄像头

FFmpeg 包含了 [video4linux2](<https://www.ffmpeg.org/ffmpeg-devices.html#video4linux2_002c-v4l2>) 及 [ALSA](<https://www.ffmpeg.org/ffmpeg-devices.html#alsa-1>) 虚拟设备，可用于捕获摄像头及音频输入。 

假设摄像头位于 `/dev/video0`，下面的命令将会录制摄像头的输入到 `webcam.mp4`，不包含音频： 
    
    $ ffmpeg -f v4l2 -video_size 640x480 -i /dev/video0 -c:v libx264 -preset ultrafast webcam.mp4
    
其中 `-video_size` 指定了来自摄像头的最大图像大小。 

上述命令将生成一个无声视频。如果要从摄像头录制视频和声音到 `webcam.mp4`： 
    
    $ ffmpeg -f v4l2 -video_size 640x480 -i /dev/video0 -f alsa -i default -c:v libx264 -preset ultrafast -c:a aac webcam.mp4
    
这里使用了 x264 编码器及最快编码速度选项。你也可以使用其它编码器；如果由于磁盘速度低或是编码速度慢导致帧写入速度太慢，帧率将会下降，导致输出的视频出现卡顿。 

另外可参考[官方文档](<https://trac.ffmpeg.org/wiki/Capture/Webcam#Linux>)。 

### VOB to any container

Concatenate the desired [VOB](<https://en.wikipedia.org/wiki/VOB> "wikipedia:VOB") files into a single stream and mux them to MPEG-2: 
    
    $ cat f0.VOB f1.VOB f2.VOB | ffmpeg -i - out.mp2
    
### x264

####  无损

_ultrafast_ 预设提供了最快的编码速度，适用于快速捕获（例如录屏）： 
    
    $ ffmpeg -i input -c:v libx264 -preset ultrafast -qp 0 -c:a copy output
    
与之相反， _veryslow_ 的编码速度比 _ultrafast_ 慢，但生成文件会更小： 
    
    $ ffmpeg -i input -c:v libx264 -preset veryslow -qp 0 -c:a copy output
    
上述两个实例都提供一致的输出质量。 

**提示：** 如果你的电脑能实时处理 `-preset superfast`，就不要使用 `-preset ultrafast`。Ultrafast 的压缩效率 _远低于_ superfast。

####  恒定速率因子

在需要特定输出质量时使用，通常在输出质量可接受的情况下使用尽可能高的 `-crf` 值。值越低质量越高：0 代表无损，18 为视觉上无损，默认为 23，正常使用的范围为 18~28。在你有耐心的情况下可以使用最慢的 `-preset`。详细信息可参考 [x264 编码指南](<https://ffmpeg.org/trac/ffmpeg/wiki/x264EncodingGuide>)。 
    
    $ ffmpeg -i _video_ -c:v libx264 -tune film -preset slow -crf 22 -x264opts fast_pskip=0 -c:a libmp3lame -aq 4 _output_.mkv
    
`-tune` 选项可用于[匹配正在编码的媒体类型及内容](<https://forum.doom9.org/showthread.php?t=149394>)。 

####  二次编码（非常高质量）

第一次编码仅记录视频分析数据，因此在输入中禁用音频： 
    
    $ ffmpeg -i _video_.VOB -an -vcodec libx264 -pass 1 -preset veryslow \
    -threads 0 -b:v 3000k -x264opts frameref=15:fast_pskip=0 -f rawvideo -y /dev/null
    
容器格式将被自动检测，并混合到输出文件扩展名（`.mkv`）中： 
    
    $ ffmpeg -i _video_.VOB -acodec aac -b:a 256k -ar 96000 -vcodec libx264 \
    -pass 2 -preset veryslow -threads 0 -b:v 3000k -x264opts frameref=15:fast_pskip=0 _video_.mkv
    
####  视频消抖

视频消抖将用到 vid.stab 插件，其需要使用二次编码。 

#####  第一次编码

第一次编码将消抖参数记录到文件和/或测试视频中以用于视觉分析。 

  * 使用该命令仅将消抖参数记录到文件中：
        
        $ ffmpeg -i input -vf vidstabdetect=stepsize=4:mincontrast=0:result=transforms.trf -f null -

  * 使用该命令将消抖参数记录到文件中，并创建名为“output-stab”的测试视频用于视觉分析：
        
        $ ffmpeg -i input -vf vidstabdetect=stepsize=4:mincontrast=0:result=transforms.trf output-stab

#####  第二次编码

第二次编码将应用第一次编码生成的参数，并输出“output-stab_final”文件。你可能需要在该阶段应用其它滤镜以避免后续转码，从而尽可能地提高视频质量。 

  * `unsharp` 由 vid.stab 的作者建议，在这里我们使用默认的 5:5:1.0:5:5:1.0
  * **提示：** fade=t=in:st=0:d=4

在文件开头加入4秒从黑色淡入
  * **提示：** fade=t=out:st=60:d=4

在第60秒加入4秒淡出到黑色
  * `-c:a pcm_s16le` 使用 XAVC-S 编码器以 pcm_s16be 格式录制，即有损转码为 pcm_s16le

    $  ffmpeg -i input -vf vidstabtransform=smoothing=30:interpol=bicubic:input=transforms.trf,unsharp,fade=t=in:st=0:d=4,fade=t=out:st=60:d=4 -c:v libx264 -tune film -preset veryslow -crf 8 -x264opts fast_pskip=0 -c:a pcm_s16le output-stab_final
    
### x265

Example command showing the defaults when libx265 is invoked without any parameters (Constant Rate Factor encoding): 
    
    ffmpeg -i input -c:v libx265 -crf 28 -preset medium -c:a libvorbis output.mp4
    
See FFmpeg [H.265/HEVC Video Encoding Guide](<https://trac.ffmpeg.org/wiki/Encode/H.265>) for more information. 

###  Single-pass MPEG-2 (near lossless)

Allow FFmpeg to automatically set DVD standardized parameters. Encode to DVD [MPEG-2](<https://en.wikipedia.org/wiki/MPEG-2> "wikipedia:MPEG-2") at ~30 FPS: 
    
    $ ffmpeg -i _video_.VOB -target ntsc-dvd _output_.mpg
    
Encode to DVD MPEG-2 at ~24 FPS: 
    
    $ ffmpeg -i _video_.VOB -target film-dvd _output_.mpg
    
###  字幕

####  提取

字幕被嵌入到像 MPEG-2 和 Matroska 这样的容器文件中，可以被提取和转换成 SRT，SSA，WebVTT 等字幕格式 [[1]](<https://trac.ffmpeg.org/wiki/ExtractSubtitles>)。 

  * 检查文件是否包含字幕流：

    $ ffprobe -hide_banner foo.mkv
    
    ...
    Stream #0:0(und): Video: h264 (High), yuv420p, 1920x800 [SAR 1:1 DAR 12:5], 23.98 fps, 23.98 tbr, 1k tbn, 47.95 tbc (default)
      Metadata:
      CREATION_TIME   : 2012-06-05 05:04:15
      LANGUAGE        : und
    Stream #0:1(und): Audio: aac, 44100 Hz, stereo, fltp (default)
     Metadata:
     CREATION_TIME   : 2012-06-05 05:10:34
     LANGUAGE        : und
     HANDLER_NAME    : GPAC ISO Audio Handler
    **Stream #0:2: Subtitle: ssa (default)**
    
  * `foo.mkv` 嵌入了一个 SSA 字幕，可以被提取到单独的文件中：

    $ ffmpeg -i foo.mkv foo.ssa
    
使用 `-c:s srt` 可以将字幕保存为目标格式，以 [SubRip](<https://en.wikipedia.org/wiki/SubRip> "wikipedia:SubRip") 为例： 
    
    $ ffmpeg -i foo.mkv -c:s srt foo.srt
    
在处理多个字幕时，你可能需要使用 `-map _key_ :_stream_` 参数指定要提取的流： 
    
    $ ffmpeg -i foo.mkv -map 0:2 foo.ssa
    
####  硬字幕嵌入

（以下操作基于 FFmpeg 维基的 [HowToBurnSubtitlesIntoVideo](<https://trac.ffmpeg.org/wiki/HowToBurnSubtitlesIntoVideo>) 一文） 

[硬字幕嵌入](<https://en.wikipedia.org/wiki/Hardsub> "wikipedia:Hardsub")将把字幕整合到视频中。硬字幕无法被编辑，也无法切换语言。 

  * 将 `foo.ssa` 整合到 `foo.mpg` 中：

    $ ffmpeg -i foo.mpg -vf subtitles=foo.ssa out.mpg
    
###  音量增益

可以通过 **ffmpeg** 的过滤器功能来修改音量增益。首先通过 `-af` 或是 `-filter:a` 参数选定音频流，然后选择 _volume_ 过滤器，后接你要将流改成的目标值。例如： 
    
    $ ffmpeg -i input.flac -af **volume=1.5** ouput.flac
    
在这一例子中，`volume=1.5` 指 150% 音量增益，也可以使用 0.5 将音量减半。也可以对音量过滤器使用分贝值，例如 `volume=3dB` 可以将音量提升 3dB，`volume=-3dB` 可以将音量降低 3dB。 

**注意：** 将文件的音量增益增倍与增倍其音量不同。你需要通过试验才能找出合适的音量。

**提示：** 可以通过 _volumedetect_ 过滤器查看当前文件的平均及最大音量：`ffmpeg -i input.flac -af volumedetect -f null -`。然后可以将目标值与当前值相减，把结果输入到 _volume_ 过滤器来达到目标增益。

### Volume normalization

A given average and peak volume can also be achieved through normalization using the _loudnorm_ filter. To normalize the perceived loudness of a file using _fmpeg'_ s default values for target average, peak and range loudness (respectively -24 LUFS, -2 dBTP and 7 LU), use: 
    
    $ ffmpeg -i input.flac -af **loudnorm** output.flac
    
To obtain a different loudness profile, use the `i`, `tp` and `lra` parameters of the filter to indicate respectively the _i_ ntegrated, _t_ rue _p_ eak and _l_ oudness _ra_ nge. For example for a higher perceived loudness than the default, use: 
    
    $ ffmpeg -i input.flac -af loudnorm=i=-16:tp=-1.5:lra=11:print_format=summary output.flac
    
In this example, `print_format=summary` is also added to display the input and output loudness values of the audio file. 

**注意：** The filter also supports two-pass mode, extracting the measured loudness values from a first run and using them in a second run to perform a linear normalization. See [ffmpeg loudnorm documentation](<https://ffmpeg.org/ffmpeg-filters.html#loudnorm>) for more information.

**提示：** To know the current loudness measures of a file, use `ffmpeg -i input.flac -af loudnorm=print_format=summary -f null -`.

### Extracting audio
    
    $ ffmpeg -i _video_.mpg output.ext
    
    ...
    Input #0, avi, from '_video_.mpg':
      Duration: 01:58:28.96, start: 0.000000, bitrate: 3000 kb/s
        Stream #0.0: Video: mpeg4, yuv420p, 720x480 [PAR 1:1 DAR 16:9], 29.97 tbr, 29.97 tbn, 29.97 tbc
        Stream #0.1: Audio: ac3, 48000 Hz, stereo, s16, 384 kb/s
        Stream #0.2: Audio: ac3, 48000 Hz, 5.1, s16, 448 kb/s
        Stream #0.3: Audio: dts, 48000 Hz, 5.1 768 kb/s
    ...
    
Extract the first (`-map 0:1`) [AC-3](<https://en.wikipedia.org/wiki/Dolby_Digital> "wikipedia:Dolby Digital") encoded audio stream exactly as it was multiplexed into the file: 
    
    $ ffmpeg -i _video_.mpg -map 0:1 -acodec copy -vn _video_.ac3
    
Convert the third (`-map 0:3`) [DTS](<https://en.wikipedia.org/wiki/DTS_\(sound_system\)> "wikipedia:DTS \(sound system\)") audio stream to an [AAC](<https://en.wikipedia.org/wiki/Advanced_Audio_Coding> "wikipedia:Advanced Audio Coding") file with a bitrate of 192 kb/s and a [sampling rate](<https://en.wikipedia.org/wiki/Sampling_rate> "wikipedia:Sampling rate") of 96000 Hz: 
    
    $ ffmpeg -i _video_.mpg -map 0:3 -acodec aac -b:a 192k -ar 96000 -vn _output_.aac
    
`-vn` disables the processing of the video stream. 

Extract audio stream with certain time interval: 
    
    $ ffmpeg -ss 00:01:25 -t 00:00:05 -i _video_.mpg -map 0:1 -acodec copy -vn _output_.ac3
    
`-ss` specifies the start point, and `-t` specifies the duration. 

### Stripping audio

  1. Copy the first video stream (`-map 0:0`) along with the second AC-3 audio stream (`-map 0:2`).
  2. Convert the AC-3 audio stream to two-channel MP3 with a bitrate of 128 kb/s and a sampling rate of 48000 Hz.

    $ ffmpeg -i _video_.mpg -map 0:0 -map 0:2 -vcodec copy -acodec libmp3lame \
    -b:a 128k -ar 48000 -ac 2 _video_.mkv
    
    $ ffmpeg -i _video_.mkv
    
    ...
    Input #0, avi, from '_video_.mpg':
      Duration: 01:58:28.96, start: 0.000000, bitrate: 3000 kb/s
        Stream #0.0: Video: mpeg4, yuv420p, 720x480 [PAR 1:1 DAR 16:9], 29.97 tbr, 29.97 tbn, 29.97 tbc
        Stream #0.1: Audio: mp3, 48000 Hz, stereo, s16, 128 kb/s
    
**注意：** Removing undesired audio streams allows for additional bits to be allocated towards improving video quality.

### Splitting files

You can use the `copy` codec to perform operations on a file without changing the encoding. For example, this allows you to easily split any kind of media file into two: 
    
    $ ffmpeg -i file.ext -t 00:05:30 -c copy part1.ext -ss 00:05:30 -c copy part2.ext
    
###  硬件加速

可以使用[硬件加速 API](<https://trac.ffmpeg.org/wiki/HWAccelIntro>) 来提升编解码性能，但只有特定编解码器受支持，且输出与软件编码相比不一定每次都一样。 

#### VA-API

[VA-API](<../zh-cn/%E7%A1%AC%E4%BB%B6%E8%A7%86%E9%A2%91%E5%8A%A0%E9%80%9F.html> "VA-API")适用于 Intel CPU（需要安装 [intel-media-driver](<https://archlinux.org/packages/?name=intel-media-driver>)包 或 [libva-intel-driver](<https://archlinux.org/packages/?name=libva-intel-driver>)包）及部分使用开源 [AMDGPU](<../zh-cn/AMDGPU.html> "AMDGPU") 驱动的 AMD GPU（需要安装 [libva-mesa-driver](<https://archlinux.org/packages/?name=libva-mesa-driver>)包），可用于编码及解码。 详细可用参数及受支持平台清单可参考 [FFmpeg 文档](<https://trac.ffmpeg.org/wiki/Hardware/VAAPI>)。 

以使用受支持的 H.264 编解码器进行编码为例： 
    
    $ ffmpeg -threads 1 -i file.ext -vaapi_device /dev/dri/renderD128 -vcodec h264_vaapi -vf format='nv12|vaapi,hwupload' output.mp4
    
**注意：** 只要检测到了 [libva](<https://archlinux.org/packages/?name=libva>)包 （应为 FFmpeg 的依赖之一）包含的相关头文件及库，VA-API 通常在构建阶段就被通过 [ffmpeg](<https://archlinux.org/packages/?name=ffmpeg>)包 的自动检测功能启用。

作为参考，可以使用如下命令生成固定质量的编码： 
    
    $ ffmpeg -vaapi_device /dev/dri/renderD128 -i input.mp4 -vf 'format=nv12,hwupload' -c:v hevc_vaapi -f mp4 -rc_mode 1 -qp 25 output.mp4
    
如果使用 hevc_vaapi，可以将 -qp 参数提到 25（视觉上相同）及以上（从 28 开始视觉上损失极小）。如果使用 h264_vaapi，可以调整到 18（视觉上相同）及以上（从 20 开始视觉上损失极小）。另外，hevc_vaapi 似乎编码速度比 h264_vaapi 高 50%。 

####  NVIDIA NVENC/NVDEC

在通过 [nvidia-utils](<https://archlinux.org/packages/?name=nvidia-utils>)包 安装私有的 [NVIDIA](<../zh-cn/NVIDIA.html> "NVIDIA") 驱动后，可以使用 [NVENC](<https://en.wikipedia.org/wiki/Nvidia_NVENC> "wikipedia:Nvidia NVENC") 和 [NVDEC](<https://en.wikipedia.org/wiki/Nvidia_NVDEC> "wikipedia:Nvidia NVDEC") 进行编/解码加速。最低支持的 GPU 为 [600 系列](<https://en.wikipedia.org/wiki/GeForce_600_series> "wikipedia:GeForce 600 series")，详情可参考[硬件视频加速#NVIDIA](<../zh-cn/%E7%A1%AC%E4%BB%B6%E8%A7%86%E9%A2%91%E5%8A%A0%E9%80%9F.html#NVIDIA> "硬件视频加速")。 

[这个旧 gist](<https://web.archive.org/web/20190808223352/https://gist.github.com/Brainiarc7/8b471ff91319483cdb725f615908286e>) 提供了一些技巧。NVENC 似乎与 [CUDA](<../zh-cn/GPGPU.html#CUDA> "CUDA") 类似，因此它甚至可以在命令行会话中被调用。按照硬件不同，NVENC 可以比 Intel 的 VA-API 编码器速度快上几倍。 

可以使用如下命令查看可用选项（也可使用 `hevc_nvenc`）： 
    
    $ ffmpeg -help encoder=h264_nvenc
    
用例： 
    
    $ ffmpeg -i source.ext -c:v h264_nvenc -rc constqp -qp 28 output.mkv
    
####  Intel QuickSync (QSV)

[Intel® Quick Sync Video](<https://www.intel.com/content/www/us/en/architecture-and-technology/quick-sync-video/quick-sync-video-general.html>) 利用了 [Intel](<../zh-cn/Intel_%E5%9B%BE%E5%BD%A2%E5%A4%84%E7%90%86%E5%99%A8.html> "Intel") GPU 的媒体处理能力加速编解码，使得处理器可忙于其它任务，提升系统响应。 

这一功能需要安装 **libmfx** 运行时实现。 **libmfx** 是一个调度库，可根据所在硬件平台实时加载对应的实现。 

在 Iron Lake（Gen5）到 [Ice Lake（Gen10）](<https://en.wikipedia.org/wiki/Ice_Lake_\(microprocessor\)> "wikipedia:Ice Lake \(microprocessor\)")GPU 上运行时，它会加载 [intel-media-sdk](<https://archlinux.org/packages/?name=intel-media-sdk>)包 作为运行时实现。 

在 [Tiger Lake（Gen11）](<https://en.wikipedia.org/wiki/Tiger_Lake> "wikipedia:Tiger Lake")及更新的 GPU 上运行时，**libmfx** 会加载 [vpl-gpu-rt](<https://archlinux.org/packages/?name=vpl-gpu-rt>)包。另外可参考 [oneVPL-intel-gpu system-requirements](<https://github.com/oneapi-src/oneVPL-intel-gpu#system-requirements>)。 

在只有单个 Intel GPU 的设备上无法更改或选择运行时实现，且在运行时需已安装对应的实现。 

未安装运行时将产生如下报错： 
    
    [AVHWDeviceContext @ 0x558283838c80] Error initializing an MFX session: -3.
    Device creation failed: -1313558101.
    
QuickSync 的用法已在 [FFmpeg 维基](<https://trac.ffmpeg.org/wiki/Hardware/QuickSync>)中描述。建议使用 [VA-API](<../zh-cn/%E7%A1%AC%E4%BB%B6%E8%A7%86%E9%A2%91%E5%8A%A0%E9%80%9F.html> "VA-API") [[2]](<https://trac.ffmpeg.org/wiki/Hardware/VAAPI>) 搭配 _iHD_ 或 _i965_ 驱动，而不是直接使用 _libmfx_ ，详情可参考 FFmpeg 维基中 _Hybrid transcode_ 部分的编码示例，以及通过[硬件视频加速#Configuring VA-API](<../zh-cn/%E7%A1%AC%E4%BB%B6%E8%A7%86%E9%A2%91%E5%8A%A0%E9%80%9F.html#Configuring_VA-API> "硬件视频加速") 了解驱动配置。 

#### AMD AMF

AMD 通过 [AMDGPU PRO](<../zh-cn/AMDGPU_PRO.html> "AMDGPU PRO") 专有包为 Linux 仅提供了 H.264 使用 AMD Video Coding Engine（GPU 编码）进行视频编码的支持，ffmpeg 另外添加了 AMF 视频编码支持。因此，如果要使用 h264_amf 视频编码器进行编码，需要安装 [amf-amdgpu-pro](<https://aur.archlinux.org/packages/amf-amdgpu-pro/>)AUR。你可能需要将 [AMDGPU PRO](<../zh-cn/AMDGPU_PRO.html> "AMDGPU PRO") 包提供的 ICD 文件以变量形式进行链接，否则 ffmpeg 可能会使用开源 AMDGPU 的 ICD 文件，使得无法使用该视频编码器。编码的命令示例如下： 
    
    $ VK_DRIVER_FILES=/usr/share/vulkan/icd.d/amd_pro_icd64.json ffmpeg -hwaccel auto -vaapi_device /dev/dri/renderD128 -i input.mkv -c:v h264_amf -rc 1 -b:v 8M h264_amf_8M.mp4
    
作为参考，可以使用如下命令生成固定质量的编码： 
    
    $ VK_DRIVER_FILES=/usr/share/vulkan/icd.d/amd_pro_icd64.json ffmpeg -hwaccel auto -vaapi_device /dev/dri/renderD128 -i input.mp4 -c:v h264_amf -f mp4 -rc 0 -qp_b 22 -qp_i 22 -qp_p 22 -quality 2 output.mp4
    
可以将三个 -qp_(b|i|p) 参数同时提到 18（视觉上相同）及以上（从 22 开始视觉上损失极小）。 

### Animated GIF

Whilst animated GIFs are generally a poor choice of video format due to their poor image quality, relatively large file size and lack of audio support, they are still in frequent use on the web. The following command can be used to turn a video into an animated GIF: 
    
    $ ffmpeg -i input.mp4 -vf "fps=10,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" -loop -1 output.gif
    
See <http://blog.pkh.me/p/21-high-quality-gif-with-ffmpeg.html> for more information on using the palette filters to generate high quality GIFs. 

##  预设文件

将默认[预设文件](<https://ffmpeg.org/ffmpeg.html#Preset-files>)放入 `~/.ffmpeg`： 
    
    $ cp -iR /usr/share/ffmpeg ~/.ffmpeg
    
参考如下方法创建新配置文件或修改现有默认预设文件： 
    
    ~/.ffmpeg/libavcodec-vhq.ffpreset
    
    vtag=DX50
    mbd=2
    trellis=2
    flags=+cbp+mv0
    pre_dia_size=4
    dia_size=4
    precmp=4
    cmp=4
    subcmp=4
    preme=2
    qns=2

###  使用预设文件

在声明要使用的 `-vcodec` 后启用 `-vpre` 选项 

#### libavcodec-vhq.ffpreset

  * `libavcodec` **=** 音/视频编解码器名称
  * `vhq` **=** 要调用的预设名称
  * `ffpreset` **=** FFmpeg 预设文件后缀

## Tips and tricks

### Reduce verbosity

Use a combination of the following options to reduce verbosity to the desired level: 

  * `-hide_banner`: prevents _ffmpeg_ from outputting its copyright notice, build options and library versions
  * `-loglevel`: modulates verbosity (fine-tuning options are available), e.g. `-loglevel warning`
  * `-nostats`: disables printing of encoding progress/statistics

### Output the duration of a video
    
    $ ffprobe -select_streams v:0 -show_entries stream=duration -of default=noprint_wrappers=1:nokey=1 file.ext
    
### Output stream information as JSON
    
    $ ffprobe -v quiet -print_format json -show_format -show_streams file.ext
    
### Create a screen of the video every X frames
    
    $ ffmpeg -i file.ext -an -s 319x180 -vf fps=1/**100** -qscale:v 75 %03d.jpg
    
##  参考

  * [FFmpeg 文档](<https://ffmpeg.org/ffmpeg.html>) \- 官方文档
  * [FFmpeg 维基](<https://trac.ffmpeg.org/wiki>) \- 官方维基
  * [使用 x264 编码器进行编码](<http://www.mplayerhq.hu/DOCS/HTML/en/menc-feat-x264.html>) \- MEncoder 文档
  * [H.264 编码指南](<https://avidemux.org/admWiki/doku.php?id=tutorial:h.264>) \- Avidemux 维基
  * [使用 FFmpeg](<http://howto-pages.org/ffmpeg/>) \- Linux 教程页
  * 受支持的音频及视频流[列表](<https://ffmpeg.org/general.html#Supported-File-Formats_002c-Codecs-or-Features>)
