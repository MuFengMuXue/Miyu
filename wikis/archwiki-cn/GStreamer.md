**翻译状态：**

  * 本文（或部分内容）译自 [GStreamer](<https://wiki.archlinux.org/title/GStreamer> "arch:GStreamer")，最近一次同步于 2024-11-16，若英文版本有所[更改](<https://wiki.archlinux.org/title/GStreamer?diff=0&oldid=820801>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/GStreamer_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[GStreamer](<https://en.wikipedia.org/wiki/GStreamer> "wikipedia:GStreamer") 是一个基于管道的多媒体框架。Gstreamer使用C语言编写，基于GObject。 

Gstreamer允许程序员创建各种媒体处理组件，包括简单的音频播放，音频与视频播放，录制，流媒体控制与媒体编辑。其管道式设计是创建多种多媒体程序的基础，例如视频编辑器，流媒体服务器，以及媒体播放器。 

Gstreamer是跨平台框架，目前已知可在下列平台上工作：Linux (x86, PowerPC 以及 ARM), Solaris (Intel 和 SPARC), Mac OS X, Microsoft Windows 以及 OS/400。GStreamer 提供了多种编程语言的绑定，包括 Python、C++、Perl、GNU Guile（guile）和 Ruby。GStreamer 是自由软件，采用 GNU宽通用公共许可证（LGPL）授权。。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")软件包 [gstreamer](<https://archlinux.org/packages/?name=gstreamer>)包 . 

为了使 GStreamer 更好用，请安装所需的插件包。请参阅[官方文档](<https://gstreamer.freedesktop.org/documentation/plugins_doc.html>)了解每个插件的功能列表。 

  * [gst-libav](<https://archlinux.org/packages/?name=gst-libav>)包 \- 基于Libav的插件，包含众多编解码器。
  * [gst-plugins-bad](<https://archlinux.org/packages/?name=gst-plugins-bad>)包 \- 需要更多改进，测试以及资料的插件。
  * [gst-plugins-base](<https://archlinux.org/packages/?name=gst-plugins-base>)包 \- 基本的Gstreamer组件。
  * [gst-plugins-good](<https://archlinux.org/packages/?name=gst-plugins-good>)包 \- 发布于LGPL许可证下，质量较高的插件。
  * [gst-plugins-ugly](<https://archlinux.org/packages/?name=gst-plugins-ugly>)包 \- 质量较高，但是可能造成分发问题的插件。
  * [gst-plugin-libde265](<https://aur.archlinux.org/packages/gst-plugin-libde265/>)AUR \- [libde265](<https://archlinux.org/packages/?name=libde265>)包 插件 (开源的h.265视频解码实现)。

##  使用方法

###  使用 gst-launch-1.0

GStreamer 的一个有用工具是 [gst-launch-1.0(1)](<https://man.archlinux.org/man/gst-launch-1.0.1>) 命令。它是一个用途广泛的命令行工具，用于创建 GStreamer 管道。它与 [FFmpeg](<../zh-cn/FFmpeg.html> "FFmpeg") 命令非常相似，并且可以执行许多相同的操作。以下是一些示例： 

将 MP4 文件转换为 MKV： 
    
    $ gst-launch-1.0 filesrc location=source.mp4 ! qtdemux name=demux matroskamux name=mux ! filesink location=dest.mkv  demux.audio_0 ! queue ! aacparse ! queue ! mux.audio_0  demux.video_0 ! queue ! h264parse ! queue ! mux.video_0
    
###  使用 gst-discoverer-1.0

另一个有用的工具是 [gst-discoverer-1.0(1)](<https://man.archlinux.org/man/gst-discoverer-1.0.1>)，它是 GStreamer 等同于 FFmpeg 的 [ffprobe(1)](<https://man.archlinux.org/man/ffprobe.1>) 的工具。 

获取视频文件信息： 
    
    $ gst-discoverer-1.0 file.mp4
    
    Properties:
      Duration: 0:02:55.613000000
      Seekable: yes
      Live: no
      container: Quicktime
        audio: MPEG-4 AAC
          Stream ID: c910ef2fa357f9f4ad365aebc98cfca88d23fdca99d832645f5113efa43b0cd3/002
          Language: <unknown>
          Channels: 2 (front-left, front-right)
          Sample rate: 44100
          Depth: 16
          Bitrate: 125588
          Max bitrate: 125588
        video: H.264 (Constrained Baseline Profile)
          Stream ID: c910ef2fa357f9f4ad365aebc98cfca88d23fdca99d832645f5113efa43b0cd3/001
          Width: 192
          Height: 144
          Depth: 24
          Frame rate: 15000/1001
          Pixel aspect ratio: 1/1
          Interlaced: false
          Bitrate: 107884
          Max bitrate: 107884

##  集成

### PulseAudio

[PulseAudio](<../zh-cn/PulseAudio.html> "PulseAudio") 由 [gst-plugins-good](<https://archlinux.org/packages/?name=gst-plugins-good>)包 插件包提供. 

###  KDE / Phonon integration

请查看 [Phonon](</wzh/index.php?title=Phonon&action=edit&redlink=1> "Phonon（页面不存在）"). 

###  硬件加速

见[硬件视频加速](<../zh-cn/%E7%A1%AC%E4%BB%B6%E8%A7%86%E9%A2%91%E5%8A%A0%E9%80%9F.html> "硬件视频加速"). 

GStreamer 将自动检测并使用正确的 API [[1]](<https://gstreamer.freedesktop.org/documentation/tutorials/playback/hardware-accelerated-video-decoding.html>)。根据系统[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")： 

  * [gst-plugin-va](<https://archlinux.org/packages/?name=gst-plugin-va>)包 以支持 [VA-API](<../zh-cn/%E7%A1%AC%E4%BB%B6%E8%A7%86%E9%A2%91%E5%8A%A0%E9%80%9F.html> "VA-API") 。
  * [gst-plugins-bad](<https://archlinux.org/packages/?name=gst-plugins-bad>)包 和 [nvidia-utils](<https://archlinux.org/packages/?name=nvidia-utils>)包 以支持 NVDECODE/NVENCODE 。

如果安装包后新元素没有显示出来，您可能需要删除并重建插件注册表。通常，只需执行以下命令： 
    
    $ rm ~/.cache/gstreamer-1.0/registry.*.bin
    
然后 GStreamer 会在下次调用时重建注册表，通常只需几秒钟。 

####  检验 VA-API

要检验 VA-API ： 
    
    $ gst-inspect-1.0 va
    
    Plugin Details:
      Name                     va
      Description              VA-API codecs plugin
      Filename                 /usr/lib/gstreamer-1.0/libgstva.so
      Version                  _version_
      License                  LGPL
      Source module            gst-plugins-bad
      Documentation            <https://gstreamer.freedesktop.org/documentation/va/>
      Source release date      _date_
      Binary package           Arch Linux gst-plugins-bad _version_
      Origin URL               <https://archlinux.org/>
    
      vaav1dec: VA-API AV1 Decoder
      vacompositor: VA-API Video Compositor
      vadeinterlace: VA-API Deinterlacer
      vah264dec: VA-API H.264 Decoder
      vah264enc: VA-API H.264 Encoder
      vah264lpenc: VA-API H.264 Low Power Encoder
      vah265dec: VA-API H.265 Decoder
      vah265enc: VA-API H.265 Encoder
      vah265lpenc: VA-API H.265 Low Power Encoder
      vajpegdec: VA-API JPEG Decoder
      vampeg2dec: VA-API Mpeg2 Decoder
      vapostproc: VA-API Video Postprocessor
      vavp8dec: VA-API VP8 Decoder
      vavp9dec: VA-API VP9 Decoder
    
      14 features:
      +-- 14 elements

###  检验 NVDECODE/NVENCODE
    
    $ gst-inspect-1.0 nvcodec
    
    Plugin Details:
      Name                     nvcodec
      Description              GStreamer NVCODEC plugin
      Filename                 /usr/lib/gstreamer-1.0/libgstnvcodec.so
      Version                  _version_
      License                  LGPL
      Source module            gst-plugins-bad
      Source release date      _date_
      Binary package           GStreamer Bad Plugins (Arch Linux)
      Origin URL               https://archlinux.org/
    
      cudadownload: CUDA downloader
      cudaupload: CUDA uploader
      nvautogpuh264enc: NVENC H.264 Video Encoder Auto GPU select Mode
      nvautogpuh265enc: NVENC H.265 Video Encoder Auto GPU select Mode
      nvav1dec: NVDEC AV1 Decoder
      nvcudah264enc: NVENC H.264 Video Encoder CUDA Mode
      nvcudah265enc: NVENC H.265 Video Encoder CUDA Mode
      nvh264dec: NVDEC h264 Video Decoder
      nvh264enc: NVENC H.264 Video Encoder
      nvh264sldec: NVDEC H.264 Stateless Decoder
      nvh265dec: NVDEC h265 Video Decoder
      nvh265enc: NVENC HEVC Video Encoder
      nvh265sldec: NVDEC H.265 Stateless Decoder
      nvjpegdec: NVDEC jpeg Video Decoder
      nvmpeg2videodec: NVDEC mpeg2video Video Decoder
      nvmpeg4videodec: NVDEC mpeg4video Video Decoder
      nvmpegvideodec: NVDEC mpegvideo Video Decoder
      nvvp8dec: NVDEC vp8 Video Decoder
      nvvp8sldec: NVDEC VP8 Stateless Decoder
      nvvp9dec: NVDEC vp9 Video Decoder
      nvvp9sldec: NVDEC VP9 Stateless Decoder
    
      21 features:
      +-- 21 elements

####  设置解码器优先级

对于一些 [NVIDIA](<../zh-cn/NVIDIA.html> "NVIDIA") 用户，[gst-libav](<https://archlinux.org/packages/?name=gst-libav>)包 可能会将 Libav 解码器的优先级高于 [nvcodec](<https://gstreamer.freedesktop.org/documentation/nvcodec/index.html>) 解码器，这会阻止硬件加速。可以使用 `GST_PLUGIN_FEATURE_RANK` [环境变量](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html> "环境变量")来设置解码器的优先级，从而缓解此问题。有关更多信息，请参阅[文档](<https://gstreamer.freedesktop.org/documentation/gstreamer/running.html#environment-variables>)中的 "GST_PLUGIN_FEATURE_RANK"。例如： 
    
    GST_PLUGIN_FEATURE_RANK=nvmpegvideodec:MAX,nvmpeg2videodec:MAX,nvmpeg4videodec:MAX,nvh264sldec:MAX,nvh264dec:MAX,nvjpegdec:MAX,nvh265sldec:MAX,nvh265dec:MAX,nvvp9dec:MAX
    
硬件不支持 AV1 的用户可能还需要通过将 `avdec_av1 ` 和 `av1dec ` 添加到上述列表中，来禁用 AV1 解码器（例如，在基于 [webkit2gtk](<https://archlinux.org/packages/?name=webkit2gtk>)包 的浏览器中观看 YouTube）。 

##  相关链接

  * [音频系统](<../zh-cn/%E9%9F%B3%E9%A2%91%E7%B3%BB%E7%BB%9F.html> "音频系统")
  * [官方网站](<https://gstreamer.freedesktop.org/>)
