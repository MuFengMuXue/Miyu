**翻译状态：**

  * 本文（或部分内容）译自 [Streaming to twitch.tv](<https://wiki.archlinux.org/title/Streaming_to_twitch.tv> "arch:Streaming to twitch.tv")，最近一次同步于 2022-11-18，若英文版本有所[更改](<https://wiki.archlinux.org/title/Streaming_to_twitch.tv?diff=0&oldid=757367>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Streaming_to_twitch.tv_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

Twitch.tv 是一个流行的 [RTMP](<https://en.wikipedia.org/wiki/Real_Time_Messaging_Protocol> "wikipedia:Real Time Messaging Protocol") 的流媒体服务。因此，本页面为 Twitch.tv 提供流媒体服务的解决方案列表。使用案例可能包括流媒体游戏、Linux 桌面等。 

##  Twitch 广播要求

根据 [Twitch.tv 支持页面](<https://help.twitch.tv/s/article/broadcast-guidelines?language=en_US>): 

视频要求
    
  * 编解码器：H.264 (x264)
  * 模式：严格恒定比特率
  * 关键帧间隔：2 秒

音频要求
    
  * 编解码器：AAC-LC，立体声或单声道
  * 最大比特率：160 kbps
  * 采样频率：任意

**注意：** 已取消支持 MP3 编解码器

其他要求
    
  * 页面未列出对 [Y'UV420p 像素格式](<https://en.wikipedia.org/wiki/YUV#Y.27UV420p_.28and_Y.27V12_or_YV12.29_to_RGB888_conversion> "wikipedia:YUV")的要求，因为对 Y'UV444 的支持还不广泛。

##  图形用户界面解决方案

  * [ Open Broadcaster Software](<../zh-cn/Open_Broadcaster_Software.html> "Open Broadcaster Software")（[obs-studio](<https://archlinux.org/packages/?name=obs-studio>)包）是一款流行的流媒体程序。Alpha Linux 构建的安装包（[obs-studio-git](<https://aur.archlinux.org/packages/obs-studio-git/>)AUR）也可用于编译和测试。
  * Castawesome（[castawesome](<https://aur.archlinux.org/packages/castawesome/>)AUR）是一款用于 ffmpeg 流媒体的 Gtk3 前端，内置 Twitch.tv 支持。
  * SimpleScreenRecorder（[lib32-simplescreenrecorder](<https://archlinux.org/packages/?name=lib32-simplescreenrecorder>)包）可对 Twitch 串流（直播）进行配置： 
    * 容器需设置为 FLV
    * RTMP URL 需要放在‘另存为’栏中
    * 确保没有选中“文件分段”
    * 视频编解码器设置为 libx264（不是 H.264）
    * 设定合理的比特率，如 2000 kbps
    * 在自定义选项栏中，输入`preset=fast,minrate=2000,maxrate=2000,bufsize=2000,keyint=60`

**注意：** “minrate”、“maxrate”和“bufsize”的值应等于比特率。

##  命令行界面解决方案

  * [FFmpeg](<#FFmpeg>) ([ffmpeg](<https://archlinux.org/packages/?name=ffmpeg>)包) 
    * PyLivestream ([pylivestream-git](<https://aur.archlinux.org/packages/pylivestream-git/>)AUR)
  * [GStreamer](<../zh-cn/GStreamer.html> "GStreamer") ([gstreamer](<https://archlinux.org/packages/?name=gstreamer>)包) 
    * [gst-live](<https://github.com/joanrieu/gst-live>)

### FFmpeg

下面的解决方案利用了 [FFmpeg](<../zh-cn/FFmpeg.html> "FFmpeg") 来实现向 Twitch.tv 串流（直播）。 

####  shell 脚本方法

使用 FFmpeg 实现的向 Twitch.tv 串流（直播）的 shell 脚本。它支持对桌面和 OpenGL 元素进行串流。可通过运行 `stream-to-twitch path/to/stream_key` 在 shell 中调用，密钥则使用 [pass](<../zh-cn/Pass.html> "Pass") 安全存储。脚本内容如下： 
    
    /usr/local/sbin/stream-to-twitch
    
    #!/usr/bin/env sh
    #
    # Stream screen and audio (speakers and microphone) to Twitch.tv using FFmpeg.
    #
    # Usage: stream-to-twitch path/to/key
    
    set -euo pipefail
    
    #######################################
    # Stream to Twitch.tv.
    # Globals:
    #   None.
    # Arguments:
    #   Stream key. A string.
    # Returns:
    #   None.
    #######################################
    stream_to_twitch() {
        res_input="1920x1080" # input resolution
        res_output="1280x720" # output resolution
        fps="30" # target FPS
        gop="60" # i-frame interval, should be double of fps
        gop_min="30" # min i-frame interval, should be equal to fps
        probesize="42M" # https://stackoverflow.com/a/57904380
        threads="2" # max 6
        cbr="1000k" # constant bitrate (should be between 1000k–3000k)
        quality="ultrafast" # one of the many FFmpeg presets
        audio_input_speakers="0" # speakers' sink id
        audio_input_mic="default" # microphone's sink id
        audio_rate="44100"
        stream_server="live-prg" # see https://stream.twitch.tv/ingests for list
        stream_key="${1}" # key will be passed as an agument from the command line
        loglevel="warning" # supress unecessary information from printing
    
        ffmpeg \
            -loglevel "${loglevel}" \
            -f x11grab -s "${res_input}" -r ${fps} -probesize ${probesize} -i :0.0 \
            -f pulse -i "${audio_input_speakers}" \
            -f pulse -i "${audio_input_mic}" \
            -filter_complex "[2]highpass=f=200,lowpass=f=3000[hl]; [1][hl]amix=inputs=2[a]" \
            -map 0:v -map [a] \
            -f flv -ac 2 -ar ${audio_rate} \
            -vcodec libx264 -g ${gop} -keyint_min ${gop_min} -b:v ${cbr} \
            -minrate ${cbr} -maxrate ${cbr} -pix_fmt yuv420p \
            -s ${res_output} -preset "${quality}" -tune film -acodec aac \
            -threads ${threads} -strict normal \
            -bufsize ${cbr} \
            "rtmp://${stream_server}.twitch.tv/app/${stream_key}"
    }
    
    # Get stream key securely stored with the password manager "pass"
    # and pass the key to the script to start the stream.
    stream_to_twitch "$(pass "${1}")"
    
**提示：** 如果使用 PulseAudio，请运行 `pactl list sinks short` 寻找输入音频流。也可使用混音器（例如 [pulsemixer](<https://archlinux.org/packages/?name=pulsemixer>)包 或 [pavucontrol](<https://archlinux.org/packages/?name=pavucontrol>)包）在脚本运行时编辑音源。

**注意：** 根据你的网络上传速度，你可能需要修改 FFmpeg 的参数。请使用参数明细作为参考。

**FFmpeg 参数明细** 参数 | 描述   
---|---  
`ffmpeg` | 转换器   
`-loglevel "${LOGLEVEL}"` | -loglevel 设置日志输出级别   
`-f x11grab` | -f 强制从 x11grab 输入   
`-s $RES_INPUT` | -s 从输入源设置一个指定的图像尺寸，由变量 $RES_INPUT 提供   
`-r $FPS` | -r 设置帧率为 $FPS   
`-probesize "${PROBESIZE}"` | -probesize 设置要分析的数据大小，以获得流信息   
`-i :0.0` | -i 获取显示（器）输入，在这里，是从 x11 的 :0.0 显示（器）获取。可以调整，例如：-i :0.0+500,100 是指在屏幕位置 500/100 处开始获取   
`-f pulse` | 强制从 PulseAudio 输入   
`-i "${AUDIO_INPUT_SPEAKERS`"} | 选择扬声器的 sink ID   
`-i "${AUDIO_INPUT_MIC`"} | 选择麦克风的 sink ID   
`-filter_complex ...` | 将过滤器应用到麦克风，以减少噪音并合并音频流   
`-map 0:v` | 映射视频流   
`-map [a]` | 映射音频流   
`-f flv` | 强制格式为 FLV   
`-ac 2` | 设置声道为 2   
`-ar "${AUDIO_RATE}"` | -ar 设置音频比特率   
`-vcodec libx264` | 设置视频编解码器为 libx264   
`-b:v "$CBR"` | -b:v 指定要改变到的视频比特率。比特率的值由 $CBR 决定   
`-pix_fmt yuv420p` | 设置像素格式为 Y'UV420p。否则默认使用 Y'UV444，这与 Twitch 不兼容   
`-s $RES_OUTPUT` | -s 为输出设置一个指定的图像尺寸，由变量 $RES_OUTPUT 提供   
`-preset "{$QUALITY}"` | 设置预设的压缩质量和速度   
`-acodec aac` | 设置音频编解码器以使用 AAC   
`-threads 0` | 设置启动的 CPU 线程，为 0 则根据 CPU 核心数自动启动线程 
