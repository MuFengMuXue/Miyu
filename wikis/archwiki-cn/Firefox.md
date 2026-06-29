**翻译状态：**

  * 本文（或部分内容）译自 [Firefox](<https://wiki.archlinux.org/title/Firefox> "arch:Firefox")，最近一次同步于 2025-01-04，若英文版本有所[更改](<https://wiki.archlinux.org/title/Firefox?diff=0&oldid=824469>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Firefox_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [Firefox/微调](<../zh-cn/Firefox/%E5%BE%AE%E8%B0%83.html> "Firefox/微调")
  * [Firefox/在 RAM 中存储配置](<../zh-cn/Firefox/%E5%9C%A8_RAM_%E4%B8%AD%E5%AD%98%E5%82%A8%E9%85%8D%E7%BD%AE.html> "Firefox/在 RAM 中存储配置")
  * [Firefox/隐私](<../zh-cn/Firefox/%E9%9A%90%E7%A7%81.html> "Firefox/隐私")
  * [浏览器扩展](<../zh-cn/%E6%B5%8F%E8%A7%88%E5%99%A8%E6%89%A9%E5%B1%95.html> "浏览器扩展")
  * [Chromium](<../zh-cn/Chromium.html> "Chromium")
  * [Opera](<../zh-cn/Opera.html> "Opera")

[Firefox](<https://www.mozilla.org/firefox>)（中文常称为“火狐浏览器”）是一个来自 [Mozilla](<https://www.mozilla.org>) 的流行开源图形化网页浏览器。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [firefox](<https://archlinux.org/packages/?name=firefox>)包。 

其他替代方案包括： 

  * **Firefox Developer Edition** — 开发者版本

     <https://www.mozilla.org/firefox/developer/> || [firefox-developer-edition](<https://archlinux.org/packages/?name=firefox-developer-edition>)包

  * **Firefox Extended Support Release** — 长期支持版本

     <https://www.mozilla.org/firefox/organizations/> || [firefox-esr](<https://aur.archlinux.org/packages/firefox-esr/>)AUR

  * **Firefox Beta** — 前沿版本

     <https://www.mozilla.org/firefox/channel/desktop/#beta> || [firefox-beta-bin](<https://aur.archlinux.org/packages/firefox-beta-bin/>)AUR

  * **Firefox Nightly** — 用于测试的夜间构建（[实验特性](<https://developer.mozilla.org/Firefox/Experimental_features>)）

     <https://www.mozilla.org/firefox/channel/desktop/#nightly> || [firefox-nightly](<https://aur.archlinux.org/packages/firefox-nightly/>)AUR

  * **Firefox KDE** — 集成了 OpenSUSE 补丁的 Firefox 版本，提供比简单的 Firefox 插件更好的 [#KDE 集成](<#KDE_%E9%9B%86%E6%88%90>)

     <https://build.opensuse.org/package/show/mozilla:Factory/MozillaFirefox> || [firefox-kde-opensuse](<https://aur.archlinux.org/packages/firefox-kde-opensuse/>)AUR

  * 除了不同的 Mozilla 构建通道外，还有许多包含更多或更少特殊功能的分支；请参见[应用程序列表/互联网#基于 Gecko](<../zh-cn/%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F%E5%88%97%E8%A1%A8/%E4%BA%92%E8%81%94%E7%BD%91.html#%E5%9F%BA%E4%BA%8E_Gecko> "应用程序列表/互联网")。

Firefox 提供了许多语言包，除了标准的英语。语言包通常命名为 `firefox-i18n-_语言代码_`（其中 `_语言代码_` 可以是任何语言代码，如 **zh-cn** 、**zh-tw** 、**ja** 等）。可以安装中文语言包 [firefox-i18n-zh-cn](<https://archlinux.org/packages/?name=firefox-i18n-zh-cn>)包（简体）或 [firefox-i18n-zh-tw](<https://archlinux.org/packages/?name=firefox-i18n-zh-tw>)包（繁体），使其通过 pacman 更新。查询 [firefox-i18n](<https://archlinux.org/packages/extra/any/firefox-i18n/>)、[firefox-developer-edition-i18n](<https://archlinux.org/packages/extra/any/firefox-developer-edition-i18n/>) 或 [firefox-nightly-](<https://aur.archlinux.org/packages/?K=firefox-nightly->) 可以分别得到 [firefox](<https://archlinux.org/packages/?name=firefox>)包、[firefox-developer-edition](<https://archlinux.org/packages/?name=firefox-developer-edition>)包 或 [firefox-nightly](<https://aur.archlinux.org/packages/firefox-nightly/>)AUR 可用语言包的列表。 

**注意：** 由于频繁的字符串更改可能导致崩溃， _-nightly_ 和 _-developer-edition_ 中禁用了语言包。要强制更改 UI 语言，您可能需要在 `about:config` 中设置 `intl.locale.requested` [[1]](<https://www.reddit.com/r/firefox/comments/lx3dp9/how_to_change_interface_language/gpovlsp/?context=8&depth=9>)。要在设置页面显示语言设置，请在 `about:config` 中将 `intl.multilingual.enabled` 设置为 `true`。

##  扩展

Firefox 因其庞大的扩展库而闻名，这些扩展可用于添加新功能或修改现有功能的行为。Firefox 的“附加组件管理器”可用于管理已安装的扩展或查找新扩展。 

有关如何安装扩展和扩展列表的说明，请参见[浏览器扩展](<../zh-cn/%E6%B5%8F%E8%A7%88%E5%99%A8%E6%89%A9%E5%B1%95.html> "浏览器扩展")。 

###  添加搜索引擎

可以通过创建书签将搜索引擎添加到 Firefox： 

  * 按下地址栏上的星标或 `Ctrl+d`。
  * 右键单击您创建的书签，然后按“编辑书签⋯(I)”。
  * 在“网址(U)”字段中输入搜索 URL。将查询位置填入 `%s`。在“关键词(K)”字段中填写用户定义的文本。如下所示：

    网址(U)
     <https://duckduckgo.com/html/?q=%s>
    关键词(K)
     d
    
**注意：** 旧版本使用“位置”而不是“网址”。

搜索通过将搜索词与指定搜索引擎的关键字一起前缀进行：`d archwiki` 将使用搜索词 `archwiki` 查询 DuckDuckGo。 

也可以通过插件扩展将搜索引擎添加到 Firefox；请参见[此页面](<https://addons.mozilla.org/firefox/search-tools/>)获取可用的搜索工具和引擎列表。 

可以在 [Mycroft Project](<https://mycroftproject.com/>) 找到一个非常广泛的搜索引擎列表。 

#### firefox-extension-arch-search

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [firefox-extension-arch-search](<https://aur.archlinux.org/packages/firefox-extension-arch-search/>)AUR 包，以将 Arch 特定的搜索（漏洞追踪器、AUR、wiki、论坛与包）添加到 Firefox 搜索工具栏。 

##  配置

Firefox 提供多种配置选项。要查看这些选项，在 Firefox 地址栏输入： 
    
    about:config
    
设置完成后，这些选项会影响用户的当前配置文件，并可能通过 [Firefox 浏览器同步](<https://www.mozilla.org/zh-CN/firefox/features/sync/>)同步到所有设备。需要注意的是，`about:config` 条目中只有一部分会被同步，可通过在 `about:config` 中搜索 `services.sync.prefs` 找到确切的同步条目。通过创建新布尔条目并在值前添加 [services.sync.prefs.sync](<https://support.mozilla.org/en-US/kb/sync-custom-preferences>)，可以同步更多的偏好项或第三方偏好项。要同步 [NoScript](<https://addons.mozilla.org/firefox/addon/noscript/>) 扩展的白名单： 
    
    services.sync.prefs.sync.capability.policy.maonoscript.sites
    
必须将布尔值 `noscript.sync.enabled` 设置为 `true`，才能通过 Firefox 浏览器同步同步 NoScript 的其余偏好项。 

**提示：** 有关如何正确设置 `about:config` 选项的完整指南，请参阅 [Firefox 的配置编辑器](<https://support.mozilla.org/zh-CN/kb/about-config-editor-firefox>)。

###  设置存储

Firefox 通过配置文件夹中的 `prefs.js` 文件存储配置，通常位于 `~/.mozilla/firefox/_xxxxxxxx_.default/`。 

Firefox 还允许通过配置文件夹中的 `user.js` 文件进行配置：[user.js](<https://kb.mozillazine.org/User.js_file>)。`user.js` 配置会覆盖 `prefs.js`。`user.js` 配置仅在启动配置文件时解析。因此，可以通过 `about:config` 测试更改，并在运行时相应修改 `user.js`。例如，针对隐私/安全用户的实用起点，请参阅[定制 user.js](<https://github.com/pyllyukko/user.js>)。 

上述方法的一个缺点是，它不能应用于整个系统。此外，作为“预配置”也不适用，因为配置文件目录是在首次启动浏览器后创建的。但是，可以让 Firefox 创建一个新配置文件，并在关闭后，将已创建配置文件夹的内容[复制到](<https://support.mozilla.org/zh-CN/kb/%E5%A4%87%E4%BB%BD%E4%BD%A0%E7%9A%84%E4%BF%A1%E6%81%AF#w_hui-fu-yi-ge-yong-hu-pei-zhi-wen-jian-bei-fen>)新配置文件中。 

有时，可能需要锁定某些设置，这对于大规模部署定制 Firefox 很有用。要创建系统范围的配置，请按照[用 AutoConfig 定制 Firefox](<https://support.mozilla.org/zh-CN/kb/autoconfigfirefox>) 中的步骤操作： 

1\. 创建 `/usr/lib/firefox/defaults/pref/autoconfig.js`： 
    
    pref("general.config.filename", "firefox.cfg");
    pref("general.config.obscure_value", 0);
    
2\. 创建 `/usr/lib/firefox/firefox.cfg`（此文件存储实际配置）： 
    
    //
    //...你的设置...
    // 例如，要禁用 Pocket，请取消注释以下行
    // lockPref("extensions.pocket.enabled", false);
    // lockPref("browser.newtabpage.activity-stream.feeds.section.topstories", false);
    
请注意，第一行必须只是 `//`。该文件的语法类似于 `user.js`。 

###  多媒体播放

Firefox 使用 [FFmpeg](<../zh-cn/FFmpeg.html> "FFmpeg") 播放 HTML5 `<audio>` 和 `<video>` 元素中的多媒体。可以使用 <https://cconcolato.github.io/media-mime-support/> 测试视频，或 <https://hpr.dogphilosophy.net/test/> 测试音频，以确定实际支持的格式。 

Firefox 使用 [PulseAudio](<../zh-cn/PulseAudio.html> "PulseAudio") 播放和录制音频。如果未安装 PulseAudio，Firefox 将改用 [ALSA](<../zh-cn/ALSA.html> "ALSA")。请注意，默认情况下，Firefox 会阻止自动播放所有带声音的媒体。[[2]](<https://support.mozilla.org/en-US/kb/block-autoplay>)

**提示：** 如果未配置音频，Firefox 可能无法播放视频。如果你打算使用 [PipeWire](<../zh-cn/PipeWire.html> "PipeWire") 和 [WirePlumber](<../zh-cn/WirePlumber.html> "WirePlumber")，请确保它们正常运行并安装必要的 [pipewire-pulse](<https://archlinux.org/packages/?name=pipewire-pulse>)包 兼容层。

####  HTML5 DRM/Widevine

Widevine 是一种数字版权管理工具，Netflix、Amazon Prime Video 等服务用它来保护视频内容。可以在 _设置 > 常规 > 数字版权管理（DRM）内容_中启用。如果在该设置被禁用时访问支持 Widevine 的页面，Firefox 会在地址栏下方显示提示，请求安装 DRM 的权限。批准后等待“下载”进度条消失，您便可以观看受 Widevine 保护的网站上的视频。 

由于没有使用[硬件 DRM 播放](<https://bugzilla.mozilla.org/show_bug.cgi?id=1700815>)，Firefox 在使用 Widevine 时仅支持播放 720p 或以下分辨率的视频。此外，需要确保未启用隐私模式浏览（窗口及设置中均需关闭）。 

####  “Open With”扩展

  1. 安装 [Open With](<https://addons.mozilla.org/firefox/addon/open-with/>) 插件。
  2. 转到 _扩展 > Open With > 首选项_。
  3. 按照说明安装系统文件并测试安装。
  4. 点击 _添加浏览器_ 。
  5. 在对话框中，为菜单项输入一个名称，并输入用于启动支持视频流播放的播放器的命令（例如 `/usr/bin/mpv`）。 
     1. 可选地，添加播放器需要的参数（例如，您可能需要为 [mpv](<../zh-cn/Mpv.html> "Mpv") 添加 `--force-window --ytdl`）。
  6. 右键点击链接或访问包含视频的页面。从 Open With 菜单中选择新创建的条目，如果站点受支持，播放器将如预期启动。

同样的方法可以用于关联视频下载工具，例如 _youtube-dl_ 。 

####  硬件视频加速

[硬件视频加速](<../zh-cn/%E7%A1%AC%E4%BB%B6%E8%A7%86%E9%A2%91%E5%8A%A0%E9%80%9F.html> "硬件视频加速")通过 VA-API 在 [Wayland](<../zh-cn/Wayland.html> "Wayland") [[3]](<https://mastransky.wordpress.com/2020/06/03/firefox-on-fedora-finally-gets-va-api-on-wayland/>) 和 [Xorg](<../zh-cn/Xorg.html> "Xorg") [[4]](<https://bugzilla.mozilla.org/show_bug.cgi?id=1619523>) [[5]](<https://www.phoronix.com/scan.php?page=news_item&px=Firefox-80-VA-API-X11>) 下可用。 

要在 Firefox 中启用 VA-API： 

  1. 确保视频卡已按[硬件视频加速](<../zh-cn/%E7%A1%AC%E4%BB%B6%E8%A7%86%E9%A2%91%E5%8A%A0%E9%80%9F.html> "硬件视频加速")中的说明正确配置为支持 VA-API。
  2. 确保 WebRender 已启用。导航到 `about:support` 并确认 _合成_ 值为“WebRender”。在 GNOME 和其他桌面环境中默认启用 [[6]](<https://mastransky.wordpress.com/2021/01/10/firefox-were-finally-getting-hw-acceleration-on-linux/>)。 
     * 确保未运行“软件 WebRender”，因为截至 2021 年 8 月，这将不起作用 [[7]](<https://bugzilla.mozilla.org/show_bug.cgi?id=1723540#c1>)。
     * 如果需要，可在 `about:config` 中设置 `gfx.webrender.all` 为 `true` 强制启用硬件 WebRender。
  3. 如果使用 Firefox 115 或更新版本，[Intel](<../zh-cn/Intel_%E5%9B%BE%E5%BD%A2%E5%A4%84%E7%90%86%E5%99%A8.html> "Intel") GPU 默认启用 VA-API [[8]](<https://bugzilla.mozilla.org/show_bug.cgi?id=1777430>)。对于其他 GPU，请在 `about:config` 中将 `media.ffmpeg.vaapi.enabled` 设置为 `true`。
  4. 可选地，为节省多 GPU 系统（例如 Ryzen 7000 系列 IGP 和 GPU）上的功耗或利用 IGP/GPU 支持的更多视频编解码器：运行 Firefox 时设置 `MOZ_DRM_DEVICE` 环境变量为首选渲染设备。（可用设备可通过 `stat /dev/dri/*` 列出）。

**注意：**

  * 如果在 `about:support` 中硬件视频加速被错误代码 `FEATURE_HARDWARE_VIDEO_DECODING_DISABLE` 或 `FEATURE_FAILURE_VIDEO_DECODING_TEST_FAILED` 阻止，可以通过将 `media.hardware-video-decoding.force-enabled=true` 强制启用。有关更多信息，请参阅 [[9]](<https://bbs.archlinux.org/viewtopic.php?id=281398>)。或者，可以安装 [firefox-vaapi](<https://aur.archlinux.org/packages/firefox-vaapi/>)AUR。
  * 虽然 NVIDIA 的专有驱动程序不支持 VA-API，但较新版本支持 DMA-BUF。使用 [libva-nvidia-driver](<https://archlinux.org/packages/?name=libva-nvidia-driver>)包 可通过 [CUDA](<../zh-cn/GPGPU.html#CUDA> "CUDA") 启用 NVIDIA 上的硬件视频解码。文档请参见 [GitHub 项目](<https://github.com/elFarto/nvidia-vaapi-driver/#firefox>)。
  * 目前，Firefox 的 VA-API 实现可解码 H.264/AVC、VP8 & VP9、AV1 编码视频。AV1 支持需要 Firefox 98+ [[10]](<https://bugzilla.mozilla.org/show_bug.cgi?id=1745225>)。
  * 多 GPU 系统应能根据此[已解决的问题](<https://bugzilla.mozilla.org/show_bug.cgi?id=1588904#c36>)自动选择适合的 GPU 以支持 VA-API。
  * [AMDGPU](<../zh-cn/AMDGPU.html> "AMDGPU") 用户在使用 [linux-hardened](<https://archlinux.org/packages/?name=linux-hardened>)包 时，可能需要在重新构建 _linux-hardened_ 内核时启用 `CONFIG_CHECKPOINT_RESTORE=y`，以满足 [mesa](<https://archlinux.org/packages/?name=mesa>)包 的 [依赖需求](<https://gitweb.gentoo.org/repo/gentoo.git/tree/media-libs/mesa/mesa-9999.ebuild>)。此问题可能已因[此修复](<https://bugzilla.mozilla.org/show_bug.cgi?id=1624743>)而不再需要。
  * Wayland 有时会干扰硬件视频解码。如果视频在切换到全屏时短暂闪烁，可能需要在 `about:config` 中设置 `widget.wayland.opaque-region.enabled=false`。
  * 如果您使用 [nvidia-open](<https://archlinux.org/packages/?name=nvidia-open>)包 或 [nvidia-open-dkms](<https://archlinux.org/packages/?name=nvidia-open-dkms>)包，`nvidia-smi` 可能显示 Firefox 的 VRAM 使用量为 0MB。这是正常现象，可忽略。如果需要修复，可以切换驱动到 [nvidia](<https://archlinux.org/packages/?name=nvidia>)包 或 [nvidia-dkms](<https://archlinux.org/packages/?name=nvidia-dkms>)包。

可以通过检查 Firefox 的 VA-API 日志验证 VA-API 是否被使用。在运行 Firefox 时设置环境变量 `MOZ_LOG="FFmpegVideo:5"`，并在日志输出中搜索“VA-API”字符串来确认播放视频时 VA-API 是否被启用和使用。请注意这些日志，它们可能会指出两种可能的组合器之一（WebRender 或 OpenGL）在您的特定设置下可与 VA-API 配合使用。 

**提示：** 在 YouTube 上启用硬件解码，视频编解码器必须被硬件支持。您可以通过[硬件视频加速#检验 VA-API](<../zh-cn/%E7%A1%AC%E4%BB%B6%E8%A7%86%E9%A2%91%E5%8A%A0%E9%80%9F.html#%E6%A3%80%E9%AA%8C_VA-API> "硬件视频加速") 检查 GPU 支持的配置文件，并通过 [h264ify](<https://addons.mozilla.org/firefox/addon/h264ify/>)、[enhanced-h264ify](<https://addons.mozilla.org/firefox/addon/enhanced-h264ify/>) 或 [refined-h264ify](<https://addons.mozilla.org/firefox/addon/refined-h264ify/>) 扩展插件（如果 YouTube 提供选择）控制使用的编解码器。

###  拼写检查

Firefox 可以使用系统范围安装的 [Hunspell](<../zh-cn/%E8%AF%AD%E8%A8%80%E6%A3%80%E6%9F%A5.html> "Hunspell") 字典以及通过其扩展系统安装的字典。 

要为特定语言启用拼写检查，右键单击任何文本框并选中**检查拼写** 框。要选择拼写检查语言，需再次右键单击并从**语言** 子菜单中选择您的语言。 

如果默认语言选择无法保存，请参阅[#Firefox 无法记住默认拼写检查语言](<#Firefox_%E6%97%A0%E6%B3%95%E8%AE%B0%E4%BD%8F%E9%BB%98%E8%AE%A4%E6%8B%BC%E5%86%99%E6%A3%80%E6%9F%A5%E8%AF%AD%E8%A8%80>)。 

####  系统范围的 Hunspell 字典

安装 [Hunspell](<../zh-cn/%E8%AF%AD%E8%A8%80%E6%A3%80%E6%9F%A5.html> "Hunspell") 及其需要语言的字典。 

####  通过附加组件添加字典

要获取更多语言，右键单击任何文本框，点击**添加字典⋯(A)** ，然后从[字典和语言包](<https://addons.mozilla.org/firefox/language-tools/>)列表中选择您想安装的字典。 

**提示：** 对于俄语，此扩展包名为 [firefox-spell-ru](<https://archlinux.org/packages/?name=firefox-spell-ru>)包。

###  XDG 桌面门户集成

从版本 64 开始，Firefox 可以选择使用 [XDG 桌面门户](<../zh-cn/XDG_%E6%A1%8C%E9%9D%A2%E9%97%A8%E6%88%B7.html> "XDG 桌面门户")来处理各种桌面功能，例如打开文件选择器或处理 [MIME 类型](<../zh-cn/%E9%BB%98%E8%AE%A4%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F.html> "默认应用程序")。使用桌面门户可以让您自定义程序，例如当您在网页上选择要上传的文件或使用**另存为⋯** 时选择下载位置。有关可用后端选项的列表，请参阅 [XDG 桌面门户#一些后端以及其支持情况](<../zh-cn/XDG_%E6%A1%8C%E9%9D%A2%E9%97%A8%E6%88%B7.html#%E4%B8%80%E4%BA%9B%E5%90%8E%E7%AB%AF%E4%BB%A5%E5%8F%8A%E5%85%B6%E6%94%AF%E6%8C%81%E6%83%85%E5%86%B5> "XDG 桌面门户")。 

Firefox 对每个功能都有独立的设置，可指定是通过桌面门户请求处理，还是使用默认 GTK 功能。 

每个设置可以有以下值： 

  * `0`——永不
  * `1`——始终
  * `2`——自动（通常取决于是否在 [Flatpak](<../zh-cn/Flatpak.html> "Flatpak") 中运行 Firefox 或是否设置了 `GDK_DEBUG=portals` 环境变量）

这些设置包括： 

  * `widget.use-xdg-desktop-portal.file-picker`——是否使用 XDG 门户打开文件选择器
  * `widget.use-xdg-desktop-portal.mime-handler`——是否使用 XDG 门户处理 MIME 类型
  * `widget.use-xdg-desktop-portal.settings`——是否尝试使用 XDG 门户获取设置/外观信息
  * `widget.use-xdg-desktop-portal.location`——是否使用 XDG 门户进行地理位置服务
  * `widget.use-xdg-desktop-portal.open-uri`——是否使用 XDG 门户打开文件

###  KDE 集成

  * 要为包括 Firefox 在内的 GTK 应用程序应用 KDE 样式，请参阅 [KDE#GTK 应用程序外观](<../zh-cn/KDE.html#GTK_%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F%E5%A4%96%E8%A7%82> "KDE")。
  * 要在 Firefox 64 或更新版本中使用 KDE 文件选择器，安装 [xdg-desktop-portal](<https://archlinux.org/packages/?name=xdg-desktop-portal>)包 和 [xdg-desktop-portal-kde](<https://archlinux.org/packages/?name=xdg-desktop-portal-kde>)包，然后在 `about:config` 中将 `widget.use-xdg-desktop-portal.file-picker` 设置为 `1`。
  * 要集成 KDE MIME 类型系统、代理和文件对话框，可使用来自 AUR 的 [firefox-kde-opensuse](<https://aur.archlinux.org/packages/firefox-kde-opensuse/>)AUR 版本，该版本应用了 OpenSUSE 补丁。或者，也可以通过将 MIME 数据库 `~/.config/mimeapps.list` 创建符号链接到已弃用的 `~/.local/share/applications/mimeapps.list` 来实现 MIME 类型集成。参见 [XDG MIME 应用程序#mimeapps.list](<../zh-cn/XDG_MIME_%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F.html#mimeapps.list> "XDG MIME 应用程序")。
  * 扩展/附加组件可以提供额外的集成，例如： 
    * 在 [Plasma](<../zh-cn/KDE.html> "Plasma") 中的浏览器集成：需要安装 [plasma-browser-integration](<https://archlinux.org/packages/?name=plasma-browser-integration>)包 和 [Plasma Integration](<https://addons.mozilla.org/firefox/addon/plasma-integration/>) 附加组件。

**提示：** 为了避免媒体播放器小部件或托盘图标中的重复条目，将 `media.hardwaremediakeys.enabled` 设置为 `false`。此设置会禁用来自 Firefox 的媒体条目，仅使用 Plasma Integration 附加组件提供的条目。

###  GNOME 集成

要使用 GNOME 文件选择器，需要安装 [xdg-desktop-portal-gnome](<https://archlinux.org/packages/?name=xdg-desktop-portal-gnome>)包 并在 `about:config` 中将 `widget.use-xdg-desktop-portal.file-picker` 从 `2` 更改为 `1`

###  大声朗读（文本转语音）

Firefox 可以为网页执行文本转语音（TTS）。 

####  设置

要使**大声朗读** 图标出现在阅读器视图中，需配置 TTS。Firefox 使用 [Speech Dispatcher](</wzh/index.php?title=Speech_Dispatcher&action=edit&redlink=1> "Speech Dispatcher（页面不存在）")（英语：[Speech Dispatcher](<https://wiki.archlinux.org/title/Speech_Dispatcher> "en:Speech Dispatcher")），而 Speech Dispatcher 需要语音合成引擎。目前推荐的语音合成引擎是 [Festival](</wzh/index.php?title=Festival&action=edit&redlink=1> "Festival（页面不存在）")（英语：[Festival](<https://wiki.archlinux.org/title/Festival> "en:Festival")）。 

####  使用

请参阅 Mozilla 网站上的[图示步骤](<https://support.mozilla.org/zh-CN/kb/firefox%E9%98%85%E8%AF%BB%E6%A8%A1%E5%BC%8F%E8%AE%A9%E7%BD%91%E9%A1%B5%E6%9B%B4%E6%B8%85%E7%88%BD>)。 

只有在完成所有配置、Speech Dispatcher 正常运行且在 Festival 服务器启动后才启动 Firefox 时，**大声朗读** 图标（耳机图标）才会出现（不能先启动 Firefox 然后再启动 Festival）。 

此外，有时 Festival 服务器进程可能会在尝试终止后仍然滞留，但在关闭 Firefox 后会终止。 

常见问题请参阅 [#Web Speech API 没有语音](<#Web_Speech_API_%E6%B2%A1%E6%9C%89%E8%AF%AD%E9%9F%B3>)和 [#Narrate/Listen 图标在阅读模式中缺失](<#Narrate/Listen_%E5%9B%BE%E6%A0%87%E5%9C%A8%E9%98%85%E8%AF%BB%E6%A8%A1%E5%BC%8F%E4%B8%AD%E7%BC%BA%E5%A4%B1>)。 

####  使用 festival-us 语音

[festival-us](<https://archlinux.org/packages/?name=festival-us>)包 包中的语音提供比 [festival-english](<https://archlinux.org/packages/?name=festival-english>)包 更好的音质，但它们在 Firefox 中无法使用。这些语音不会出现在 Firefox 可用语音列表中，并且当你打开阅读模式时，你将在 Festival 服务器的终端输出中看到类似这样的错误消息： 
    
     SIOD: unknown voice cmu_us_awb_cg 

要解决这个问题，你需要编辑以下文件： 

  * `/usr/share/festival/voices/us/cmu_us_awb_cg/festvox/cmu_us_awb_cg.scm`
  * `/usr/share/festival/voices/us/cmu_us_rms_cg/festvox/cmu_us_rms_cg.scm`
  * `/usr/share/festival/voices/us/cmu_us_slt_cg/festvox/cmu_us_slt_cg.scm`

对于每个文件，你需要在倒数第二行的代码前面添加一些代码，例如，对于 `cmu_us_awb_cg.scm`，你需要在此行前面添加代码： 
    
    (provide 'cmu_us_awb_cg)

你需要为 `cmu_us_awb_cg.scm` 添加的代码如下。你还需要根据其他两个文件的语音名称、性别、方言和描述进行相应的修改。 
    
    (proclaim_voice
     'cmu_us_awb_cg
     '((language english)
       (gender male)
       (dialect scottish)
       (description "This voice is Scottish")))
    
**注意：** 为了避免每次 [festival-us](<https://archlinux.org/packages/?name=festival-us>)包 升级后重新进行这些修改，请参阅 [pacman#在升级时跳过文件](<../zh-cn/Pacman.html#%E5%9C%A8%E5%8D%87%E7%BA%A7%E6%97%B6%E8%B7%B3%E8%BF%87%E6%96%87%E4%BB%B6> "Pacman")。

##  提示和技巧

有关一般增强功能，请参阅 [Firefox/微调](<../zh-cn/Firefox/%E5%BE%AE%E8%B0%83.html> "Firefox/微调")，有关隐私相关的增强功能，请参阅 [Firefox/隐私](<../zh-cn/Firefox/%E9%9A%90%E7%A7%81.html> "Firefox/隐私")。 

###  黑暗主题

Firefox 应该会遵循你的 GTK 主题设置和操作系统全局的黑暗外观设置（例如 GNOME 设置中的外观部分或 KDE 系统设置）。如果后者不起作用，请确保安装了合适的 [xdg-desktop-portal](<https://archlinux.org/packages/?name=xdg-desktop-portal>)包 包。 

从 Firefox 68 开始，你可以让所有 Firefox 界面甚至其他网站都遵循黑暗主题，而不管系统的 GTK 主题和 Firefox 主题是什么。要做到这一点，可以在 `about:config` 中将 `ui.systemUsesDarkTheme` 设置为 `1` [[11]](<https://bugzilla.mozilla.org/show_bug.cgi?id=1488384#c23>)。 

从 Firefox 100 开始，你可以进一步控制支持黑暗主题的网站（通过 CSS 媒体查询 [prefers-color-scheme](<https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-color-scheme>)）和 Firefox 自身的内嵌页面。通过设置 `layout.css.prefers-color-scheme.content-override`，设置为 `3` 将跟随浏览器主题，设置为 `2` 将跟随系统的黑暗模式首选项（如上所述的 `ui.systemUsesDarkTheme`，如果用户没有更改黑暗模式首选项或系统不支持系统级的黑暗模式首选项，则默认为 `0`），而 `1` 和 `0` 分别将强制开启浅色模式和深色模式。这个设置也可以通过 Firefox 的用户设置访问，在**常规 > 语言和外观 > 网站外观**下。 

###  帧率

如果 Firefox 无法自动检测正确的值，它将默认为 60 fps。要手动调整，设置 `layout.frame_rate` 为你的显示器的刷新率（例如 144 表示 144 Hz）。 

###  内存限制

为了防止页面滥用内存（以及可能的 [OOM](<https://en.wikipedia.org/wiki/Out_of_memory> "wikipedia:Out of memory")），我们可以使用 [Firejail](<../zh-cn/Firejail.html> "Firejail") 和 `rlimit-as` 选项。 

###  新标签页位置

要控制新标签页的打开位置（相对位置或绝对位置），使用 `browser.tabs.insertAfterCurrent` 和 `browser.tabs.insertRelatedAfterCurrent`。更多信息请参阅 [[12]](<https://support.mozilla.org/en/questions/1229062>)。 

###  网页截图

你可以通过使用截图按钮来“截取屏幕”，该按钮可以从汉堡菜单的自定义屏幕中添加到工具栏，路径为**更多工具 > 自定义工具栏**，或通过按 `Ctrl+Shift+s`，或者通过右键单击网页。更多信息请参见 [Firefox 截图](<https://support.mozilla.org/zh-CN/kb/firefox%20%E6%88%AA%E5%9B%BE>)（包括关于遥测数据收集的描述）。 

还可以使用开发者工具中的截图按钮，可以通过开发者工具的**设置** 菜单中的**可用工具栏按钮** 部分添加。开发者工具的设置可以通过位于开发者工具窗格右上角的三个水平点来访问。 

### Xwayland

从 Firefox 121 版本开始，Firefox 默认使用 [Wayland](<../zh-cn/Wayland.html> "Wayland")，而不是 XWayland，并且不需要任何配置。 

你可以通过设置[环境变量](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html> "环境变量")强制启用 [Xwayland](<../zh-cn/Wayland.html#Xwayland> "Xwayland") 模式。 
    
    $ MOZ_ENABLE_WAYLAND=0 firefox
    
为了使这个设置永久生效，请参阅[环境变量#图形环境](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html#%E5%9B%BE%E5%BD%A2%E7%8E%AF%E5%A2%83> "环境变量")并像平常一样通过桌面启动器启动 Firefox。 

验证是否成功，你可以在 `about:support` 中查找 _Window Protocol_ 。如果显示 `x11`，说明你正在通过 [Xorg](<../zh-cn/Xorg.html> "Xorg") 显示服务器运行 Firefox，而如果显示 `xwayland`，说明你的系统正在运行 Wayland，但将 Firefox 作为传统的 X11 应用程序运行。 

###  窗口管理器规则

为了能够将不同的配置应用于 Firefox 窗口，使用 Firefox 的 `--class` 选项修改 WM_CLASS 字符串。在 Wayland 下，Firefox 使用 `--name` 选项。然后你可以在窗口管理器中通过设置的字符串引用不同的 Firefox 窗口。 

###  配置文件

要启动多个 Firefox 实例，需要多个配置文件。创建新配置文件的方法是： 
    
    $ firefox [--new-instance] -P
    
在启动 Firefox 时，可以为未使用的配置文件指定类： 
    
    $ firefox [--new-instance] -P _profile_name_ --class=_class_name_
    
[Firefox Profilemaker](<https://ffprofile.com/>) 可以用来创建一个符合你偏好的 Firefox 配置文件。 

###  屏幕触摸手势和精确的触控板滚动

[![](../File:Merge-arrows-2.png)](<../File:Merge-arrows-2.png>)**本文或本章节可能需要合并到[Firefox/微调#启用屏幕触摸手势](<../zh-cn/Firefox/%E5%BE%AE%E8%B0%83.html#%E5%90%AF%E7%94%A8%E5%B1%8F%E5%B9%95%E8%A7%A6%E6%91%B8%E6%89%8B%E5%8A%BF> "Firefox/微调")。**

**附注：** 同样的解决方案。（在 [Talk:Firefox](<../zh-cn/Talk:Firefox.html>) 中讨论）

要启用触摸手势（如滚动和捏合缩放）和一对一触控板滚动（如 GTK3 应用程序 Nautilus 中的体验），在启动 Firefox 前设置 `MOZ_USE_XINPUT2=1` [环境变量](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html> "环境变量")。在 Wayland 上不需要进行任何配置。 

由于一个 [bug](<https://bugzilla.mozilla.org/show_bug.cgi?id=1568722>)，Wayland 上的动感滚动感觉较为松散，你可以在 `about:config` 中关闭 `apz.gtk.kinetic_scroll.enabled` 来禁用该功能。需要注意的是，这样会使得滚动到长页面的开始和结束变得更加困难。 

###  多个主页

要在启动 Firefox 时打开多个标签页，打开一个新窗口，然后打开你想要作为“主页标签”的网站。 

然后转到**设置 > 主页**，在**主页和新窗口** 下点击**使用当前页面** 按钮。 

或者，直接转到 _设置 > 主页_，在 _主页和新窗口_ 下，将第一个字段设置为 _自定义 URL.._ ，并以如下格式输入你希望作为新主页的页面： 
    
    https://url1.com|https://url2.com|https://url3.com
    
###  在 PDF 查看器中并排查看两个页面

要在集成的 PDF 查看器中同时显示两个页面，请在 `about:config` 中将 `pdfjs.spreadModeOnLoad` 设置为 `1`。 

###  资讯站模式 (Kiosk mode)

Firefox 支持资讯站模式，该模式以全屏显示页面，去除浏览器的界面元素（如浏览器框架、右键菜单等）以及其他通常用于桌面浏览的功能。这种模式通常应用于用户不需要与设备上系统的其他部分进行交互的场所(如ATM、信息面板等)。 

要使用 Kiosk 模式，可以通过以下命令启动 Firefox： 
    
    $ firefox --kiosk _url_
    
启动页面可以通过设置配置或作为命令行参数提供。 

如果需要打印，可以通过以下方式阻止 Firefox 显示纸张尺寸配置对话框： 
    
    $ firefox --kiosk --kiosk-printing _url_
    
###  紧凑模式

从 Firefox 89 版本开始，紧凑模式密度选项已从自定义面板中移除 [[13]](<https://support.mozilla.org/en-US/kb/compact-mode-workaround-firefox>)，但你仍然可以使用紧凑密度。要做到这一点，可以在 `about:config` 中将 `browser.uidensity` 设置为 `1`。 

用户界面还可以进一步缩放，参见 [Firefox/微调#配置 DPI 值](<../zh-cn/Firefox/%E5%BE%AE%E8%B0%83.html#%E9%85%8D%E7%BD%AE_DPI_%E5%80%BC> "Firefox/微调")，但请使用介于 0 和 1 之间的值。 

###  GNOME 搜索提供者

Firefox 包含一个 GNOME Shell 的搜索提供者，在 Firefox 运行时，它会将 Firefox 的书签和历史记录暴露给 GNOME Shell 搜索。然而，该提供者默认是禁用的；要启用它，请转到 `about:config` 并将 `browser.gnome-search-provider.enabled` 设置为 `true`。 

###  自定义我的足迹窗口中的日期和时间格式

在“我的足迹”窗口（显示书签、历史记录和下载的窗口，可以通过 `Ctrl+Shift+o` 和 `Ctrl+Shift+h` 访问）中使用的日期和时间格式，可以通过在 `user.js` 或 `about:config` 中设置 `intl.date_time.pattern_override.date_short`、`intl.date_time.pattern_override.time_short` 和 `intl.date_time.pattern_override.connector_short` 来自定义。例如，要获得类似 [RFC:3339](<https://tools.ietf.org/html/rfc3339> "rfc:3339") 格式（"2022-12-31 22:49"），可以将这三个首选项设置为 `yyyy-MM-dd`、`HH:mm` 和 `{1} {0} `。 

将 `LC_TIME` 环境变量设置为 `en_DK.UTF-8` 仅在旧版 Firefox（可能是 57 及更早版本）中有效。有关更多信息，请参见 Mozilla 的 [bug 报告 1426907](<https://bugzilla.mozilla.org/show_bug.cgi?id=1426907>)。 

###  禁用 Ctrl+q 快捷键关闭 Firefox

在 `about:config` 中创建并设置选项 `browser.quitShortcut.disabled` 为 `true`。 

###  启用后量子混合密钥交换

Firefox 支持 [X25519Kyber768](<https://www.ietf.org/archive/id/draft-tls-westerbaan-xyber768d00-02.html>)，这是一种用于 TLS 1.3 的后量子混合密钥交换。从 Firefox 132.0 开始，该功能默认启用。要测试是否启用，可以访问[这个 Cloudflare Research 测试页面](<https://pq.cloudflareresearch.com>)，它将告诉你是否正在使用 PQ 安全的密钥交换。 

##  故障排除

###  排障模式

命令行选项 `-safe-mode` 可以启动 Firefox 的[排障模式](<https://support.mozilla.org/zh-CN/kb/%E5%AE%89%E5%85%A8%E6%A8%A1%E5%BC%8F>)，该模式将禁用扩展、主题、硬件加速、JIT 和其他一些功能。 

你也可以通过打开 Firefox 后，点击汉堡菜单，选择**帮助** ，点击**排障模式⋯(M)** ，然后在弹出的对话框中确认启用此模式。请注意，这将要求重启浏览器。 

该模式在 Firefox 88 之前被称为“安全模式”。 

###  翻新 Firefox

一些 Firefox 用户遇到的问题可能是由配置文件问题引起的，例如损坏。 

如果排除了其他原因，尝试创建一个新的 Firefox 配置文件来进行测试，看是否能解决问题。如果你需要有关如何创建新配置文件以及如何在配置文件之间切换的信息，可以访问[Firefox 支持页面](<https://support.mozilla.org/zh-CN/kb/%E7%AE%A1%E7%90%86%E7%94%A8%E6%88%B7%E9%85%8D%E7%BD%AE%E6%96%87%E4%BB%B6>)。 

如果新配置文件解决了问题，你可以切换回原始配置文件，并考虑翻新 Firefox。 

翻新配置文件时，浏览历史、下载历史、书签、网页表单自动填充数据、Cookies、个人词典和密码将会保留，并且会转移到一个全新的配置文件中，新的配置文件不会包含扩展、主题、扩展数据和首选项等数据。旧配置文件的备份也会被保留。 

要翻新配置文件，请转到 `about:support`，点击**翻新 Firefox⋯** 并在弹出的对话框中确认此操作。你也可以通过点击汉堡菜单，选择**帮助** 然后点击**更多排障信息(T)** 来访问 `about:support`。 

有关刷新 Firefox 的更多信息，包括转移到新配置文件中的内容，请参阅 [Firefox 支持页面](<https://support.mozilla.org/en-US/kb/refresh-firefox-reset-add-ons-and-settings>)。 

###  硬件视频加速问题

如果你在 Firefox 中遇到硬件视频加速问题，例如卡顿或图形损坏，可以启动 Firefox 的[排障模式](<#%E6%8E%92%E9%9A%9C%E6%A8%A1%E5%BC%8F>)来确认是否是这个问题。如果这个步骤解决了问题，可以通过在 `about:config` 中将 `media.ffmpeg.vaapi.enabled` 设置为 `false` 来禁用硬件视频加速，然后重启 Firefox。 

###  扩展无法在某些 Mozilla 拥有的域名上工作

默认情况下，扩展不会影响由 `extensions.webextensions.restrictedDomains` 指定的页面。如果不希望这样，可以清除该字段（特殊页面如 `about:*` 不会受到影响）。然后创建并将 `privacy.resistFingerprinting.block_mozAddonManager` 设置为 true。 

###  Firefox 启动时间过长

如果 Firefox 启动时间远长于其他浏览器，可能是因为在 `/etc/hosts` 中没有配置 localhost。请参阅[网络配置#局域网主机名解析](<../zh-cn/%E7%BD%91%E7%BB%9C%E9%85%8D%E7%BD%AE.html#%E5%B1%80%E5%9F%9F%E7%BD%91%E4%B8%BB%E6%9C%BA%E5%90%8D%E8%A7%A3%E6%9E%90> "网络配置")了解如何进行配置。 

行为不正常的 Firefox 扩展，或者扩展过多，可能是启动缓慢的另一个原因。可以通过[排障模式](<#%E6%8E%92%E9%9A%9C%E6%A8%A1%E5%BC%8F>)来确认这一点，该模式将在重启时禁用扩展。 

启动缓慢的另一个原因可能是配置文件问题，例如损坏。有关 Firefox 配置文件故障排除的更多步骤，请参阅[#翻新 Firefox](<#%E7%BF%BB%E6%96%B0_Firefox>)。 

###  字体故障排除

请参阅[字体配置](<../zh-cn/%E5%AD%97%E4%BD%93%E9%85%8D%E7%BD%AE.html> "字体配置")。 

Firefox 有一个设置，决定它允许多少字体替换来自 Fontconfig。如果你希望它使用所有的替换规则，可以将 `gfx.font_rendering.fontconfig.max_generic_substitutions` 设置为 `127`（最大值）。 

Firefox 附带了 _Twemoji Mozilla_ 字体。要使用系统的 emoji 字体，请在 `about:config` 中将 `font.name-list.emoji` 设置为 `emoji`。此外，要防止 Mozilla 字体干扰你的系统 emoji 字体，可以将 `gfx.font_rendering.opentype_svg.enabled` 设置为 `false`，或删除 `/usr/lib/firefox/fonts/TwemojiMozilla.ttf`（参见 [pacman#在安装时跳过文件](<../zh-cn/Pacman.html#%E5%9C%A8%E5%AE%89%E8%A3%85%E6%97%B6%E8%B7%B3%E8%BF%87%E6%96%87%E4%BB%B6> "Pacman")）。 

###  设置电子邮件客户端

在浏览器内，`mailto` 链接默认由 Web 应用程序（如 Gmail 或 Yahoo Mail）打开。要设置外部电子邮件程序，请转到**设置 > 常规 > 应用程序**，并修改对应 `mailto` 内容类型的“操作”；需要指定文件路径（例如，`/usr/bin/kmail` 用于 Kmail）。 

在浏览器外，`mailto` 链接由 `x-scheme-handler/mailto` MIME 类型处理，可以通过 [xdg-mime](<../zh-cn/XDG_MIME_%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F.html> "Xdg-mime") 轻松配置。详细信息和替代方法，请参见[默认应用程序](<../zh-cn/%E9%BB%98%E8%AE%A4%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F.html> "默认应用程序")。 

###  文件关联

参见[默认应用程序](<../zh-cn/%E9%BB%98%E8%AE%A4%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F.html> "默认应用程序")。 

###  Firefox 即使不需要也会创建 ~/Desktop

Firefox 使用 `~/Desktop` 作为下载和上传文件的默认位置。要将其更改为其他文件夹，请按照 [XDG 用户目录](<../zh-cn/XDG_%E7%94%A8%E6%88%B7%E7%9B%AE%E5%BD%95.html> "XDG 用户目录")中的说明设置 `XDG_DESKTOP_DIR` 选项。 

###  下载目录充满了不记得保存过的文件

在 Firefox 98 版本中，打开文件至外部程序的行为被悄然更改。原本 Firefox 会将文件下载到 `/tmp` 并将其位置提供给子进程，而现在它会像选择“保存”一样下载文件，然后将文件的位置提供给子进程。结果，您的下载目录可能充满了仅供查看的文件。这种情况发生在您从对话框中选择程序打开文件时，以及对于配置为自动用特定程序打开的文件类型。值得注意的是，对于某些文件类型（如启用了浏览器内 **PDF.js** 查看器的 PDF 文档）也会发生这种情况。 

由于疏忽，对话框中的选项仍然描述旧行为（选择“打开”或“保存”），但实际上会始终保存文件。这种行为可能对期望文件不会保存到磁盘的用户构成安全和隐私风险，建议您禁用此新行为。 

为此，请在 `about:config` 中创建并设置 `browser.download.start_downloads_in_tmp_dir` 为 `true`。 

或者，为了防止 Firefox 在打开 PDF 文件时自动将其保存到下载目录，请在 `about:config` 中设置 `browser.download.open_pdf_attachments_inline` 为 `true`。 

**注意：** 虽然选项的名称似乎表明它只会将文件暂时缓存到 `/tmp` 中然后移动到其他位置，但 Mozilla 已[确认](<https://www.mozilla.org/en-US/firefox/102.0a1/releasenotes/>)这实际上会恢复旧行为： 

    现在有一个企业策略（`StartDownloadsInTempDirectory`）和一个 `about:config` 参数（`browser.download.start_downloads_in_tmp_dir`），可以让 Firefox 再次将下载文件放置到操作系统临时文件夹中的子文件夹中，而不是下载目录中。通过“Firefox 应如何处理此文件”对话框打开或自动用辅助程序打开的文件会保留在该文件夹中。保存的文件（如之前提到的非打开文件）仍然会保存在 Firefox 的下载目录中。

####  其他设置

  * `browser.download.forbid_open_with`：`true` （在文件保存对话框中仅询问是保存还是取消，从不询问是否用其他程序打开）
  * `browser.download.always_ask_before_handling_new_types`：`true` （同于“设置 > 常规 > 文件和应用程序 > Firefox 应如何处理其他文件？> 询问是否打开或保存文件”）。
  * 在“设置 > 常规 > 文件和应用程序”中，将所有已知文件类型设置为“总是询问”，可能的例外是设置为由 Firefox 自身打开的文件类型。

###  对 userChrome.css 和 userContent.css 的更改被忽略

在 `about:config` 中将 `toolkit.legacyUserProfileCustomizations.stylesheets` 设置为 `true`。 

###  中键单击行为

要启用中键单击自动滚动（Windows 浏览器的默认设置），可以通过以下两种方式： 

  * 转到“设置 > 常规”，在“浏览”部分启用“使用自动滚动”选项。
  * 或者，在 `about:config` 中设置 `general.autoScroll` 为 `true`。

要禁用中键单击时从剪贴板粘贴内容（[PRIMARY 选区](<../zh-cn/%E5%89%AA%E8%B4%B4%E6%9D%BF.html#%E9%80%89%E5%8C%BA> "剪贴板")），请在 `about:config` 中将 `middlemouse.paste` 设置为 `false`。 

要在中键单击时将剪贴板内容作为 URL 加载，请将 `middlemouse.contentLoadURL` 设置为 `true`。这是 Firefox 57 之前的默认行为。 

###  Backspace 键无法用作“后退”按钮

根据 [MozillaZine](<https://kb.mozillazine.org/Browser.backspace_action>) 的说法，`Backspace` 键的行为取决于浏览器运行的平台。为达成妥协，此偏好被创建，以允许 `Backspace` 键用于“后退/前进”、上下滚动页面，或不执行任何操作。 

要使 `Backspace` 键返回选项卡历史记录的上一页，并让 `Shift+Backspace` 前进一页，请在 `about:config` 中将 `browser.backspace_action` 设置为 `0`。 

要使 `Backspace` 键向上滚动一页，并让 `Shift+Backspace` 向下滚动一页，请将 `browser.backspace_action` 设置为 `1`。将此属性设置为任何其他值将使该键无映射功能（Arch Linux 默认为 `2`，即默认情况下无映射）。 

###  Firefox 未记住登录信息

这可能是由于 [Firefox 用户配置文件](<https://support.mozilla.org/zh-CN/kb/%E7%94%A8%E6%88%B7%E9%85%8D%E7%BD%AE%E6%96%87%E4%BB%B6%E2%80%94%E2%80%94Firefox%20%E4%BF%9D%E5%AD%98%E4%B9%A6%E7%AD%BE%E3%80%81%E5%AF%86%E7%A0%81%E5%92%8C%E5%85%B6%E4%BB%96%E7%94%A8%E6%88%B7%E6%95%B0%E6%8D%AE%E7%9A%84%E6%96%87%E4%BB%B6>)文件夹中的 `cookies.sqlite` 文件损坏造成的。为了解决此问题，请在 Firefox 未运行时重命名或删除 `cookies.sqlite`。 

打开终端并输入以下命令： 
    
    $ rm -f ~/.mozilla/firefox/<profile id>.default/cookies.sqlite
    
配置文件 ID 是一个随机的 8 字符字符串。 

重新启动 Firefox 并检查问题是否解决。 

如果不起作用，请检查是否存在 `cookies.sqlite.bak` 文件，您可以用来手动恢复 Cookie。 

###  无法进入/退出全屏

如果 Firefox 检测到 [EWMH/ICCCM](<https://specifications.freedesktop.org/wm-spec/latest/>) 兼容的窗口管理器，它会尝试向根窗口发送 WM_STATE 消息，要求进入（或退出）全屏模式（由窗口管理器定义）。窗口管理器可以忽略此请求，但如果忽略，Firefox 会认为请求被拒绝，并将此结果传递给用户，这会导致什么都没有发生。一个常见的解决方法是在 `about:config` 中将 `full-screen-api.ignore-widgets` 设置为 `true`。 

相关错误报告：[Bugzilla 1189622](<https://bugzilla.mozilla.org/show_bug.cgi?id=1189622>)。 

###  全屏模式下 YouTube 的滚动条未隐藏/禁用

[![](../File:Tango-inaccurate.png)](<../File:Tango-inaccurate.png>)**本文或本章节的事实准确性存在争议。**

**原因：** 这不应该发生。添加 uBlock Origin 过滤器是一种权宜之计，可能是由于 bug 或其他扩展干扰引起的。（在 [Talk:Firefox](<../zh-cn/Talk:Firefox.html>) 中讨论）

此问题可以通过 [uBlock Origin](<https://ublockorigin.com/>) 过滤器修复。要添加过滤器，点击“uBlock Origin 扩展图标 > 三个齿轮（打开控制面板）> 我的过滤器”。然后，将以下内容添加到文本框中： 
    
    www.youtube.com##ytd-app:style(overflow: hidden !important;)
    
应用更改并重新加载 YouTube 窗口后，过滤器将生效。注意，您需要启用美化过滤功能（中间带眼睛的图标）才能使其生效。 

###  某些网站上的 JavaScript 右键菜单无法显示

您可以尝试在 `about:config` 中将 `dom.w3c_touch_events.enabled` 设置为 `0`。 

###  Firefox 无法记住默认拼写检查语言

默认拼写检查语言的设置方式如下： 

  1. 在地址栏中输入 `about:config`。
  2. 将 `spellchecker.dictionary` 设置为所选语言，例如 `en_GB`。
  3. 请注意，对于作为 Firefox 插件安装的字典，标记形式为 `en-GB`；而对于 [hunspell](<https://archlinux.org/packages/?name=hunspell>)包 字典，标记形式为 `en_GB`。

如果您仅安装了系统范围的 [hunspell](<https://archlinux.org/packages/?name=hunspell>)包 字典，Firefox 可能不会记住您的默认字典语言设置。解决方法是至少安装一个[字典](<https://addons.mozilla.org/firefox/language-tools/>)作为 Firefox 插件。注意，现在您会在“附加组件”中看到“字典”选项卡。您可能需要更改 `about:preferences#general` 中“首选网页显示语言”的顺序，使拼写检查默认为插件字典的语言。 

相关问题（**StackExchange** 平台）：[[14]](<https://stackoverflow.com/questions/26936792/change-firefox-spell-check-default-language/29446115>)，[[15]](<https://stackoverflow.com/questions/21542515/change-default-language-on-firefox/29446353>)，[<https://askubuntu.com/questions/184300/how-can-i-change-firefox>

相关漏洞报告：[Bugzilla 776028](<https://bugzilla.mozilla.org/show_bug.cgi?id=776028>), [Ubuntu bug 1026869](<https://bugs.launchpad.net/ubuntu/+source/firefox/+bug/1026869>)

###  Firefox 无法找到系统范围内的 Hunspell 拼写检查词典

确保设置 `spellchecker.dictionary_path` 存在，并且其值设置为系统 Hunspell 词典的路径：`/usr/share/hunspell`。 

###  某些 MathML 符号丢失

您需要一些数学字体，如 Latin Modern Math 和 STIX（参见此 MDN 页面：[[16]](<https://developer.mozilla.org/en-US/docs/Mozilla/MathML_Project/Fonts#Linux>)），以正确显示 MathML。 

在 Arch Linux 中，这些字体由 [texlive-fontsextra](<https://archlinux.org/packages/?name=texlive-fontsextra>)包 提供，但默认情况下它们无法被 fontconfig 使用。详情参见 [TeX Live#Making fonts available to Fontconfig](<../zh-cn/TeX_Live.html#Making_fonts_available_to_Fontconfig> "TeX Live")。也可以尝试其他[数学字体](<../zh-cn/%E5%AD%97%E4%BD%93.html#Math> "Fonts")。如果遇到此问题 [[17]](<https://bugzilla.mozilla.org/show_bug.cgi?id=1208776>)，安装 [otf-latinmodern-math](<https://archlinux.org/packages/?name=otf-latinmodern-math>)包 可能会有所帮助。 

###  视频加载但无法播放

这可能是 PulseAudio 的问题。请参见[PulseAudio/问题解决#浏览器（Firefox） 视频加载但无法播放](</wzh/index.php?title=PulseAudio/%E9%97%AE%E9%A2%98%E8%A7%A3%E5%86%B3&action=edit&redlink=1> "PulseAudio/问题解决（页面不存在）")（英语：[PulseAudio/Troubleshooting#Browsers (firefox) load videos but do no play](<https://wiki.archlinux.org/title/PulseAudio/Troubleshooting#Browsers_\(firefox\)_load_videos_but_do_no_play> "en:PulseAudio/Troubleshooting")）中的建议解决方案。 

###  滚动时出现画面撕裂

尝试在“设置 > 常规 > 浏览”中禁用平滑滚动。请注意，页面滚动可能会变得不平滑。 

###  Firefox WebRTC 模块无法检测到麦克风

WebRTC 应用（例如 [Firefox WebRTC getUserMedia 测试页面](<https://mozilla.github.io/webrtc-landing/gum_test.html>)）提示无法找到麦克风。问题在 ALSA 或 PulseAudio 设置下均可重现。Firefox 调试日志显示以下错误： 
    
    $ NSPR_LOG_MODULES=MediaManager:5,GetUserMedia:5 firefox
    
    ...
    [Unnamed thread 0x7fd7c0654340]: D/GetUserMedia  VoEHardware:GetRecordingDeviceName: Failed 1

您可以尝试在 `about:config` 页面中将 `media.navigator.audio.full_duplex` 属性设置为 `false`，然后重启 Firefox。 

如果您使用 PulseAudio 的 [module-echo-cancel](<../zh-cn/PulseAudio.html#Microphone_echo/noise_cancellation> "PulseAudio") 并且 Firefox 无法识别虚拟回声消除源，这也可能有所帮助。 

###  WebRTC 共享指示器显示 XML 解析错误

在同意共享麦克风或摄像头后，您可能会在主窗口的左上角看到一个带棕色背景和红色边框的窗口，显示以下错误信息： 
    
    XML Parsing Error: no root element found
    Location: chrome://browser/content/webrtcLegacyIndicator.xhtml
    Line Number: 1, Column 1:
    ^
    
如果您遇到此问题，可以通过以下步骤解决： 

  1. 访问 `about:support`。
  2. 单击“清除启动缓存”按钮，并同意重启浏览器。

详情请参见 [Mozilla 的错误报告](<https://bugzilla.mozilla.org/show_bug.cgi?id=1639821>)。 

###  无法使用我的中国账号登录

Firefox 为中国用户提供了本地服务，与国际版完全不同。使用 [firefox](<https://archlinux.org/packages/?name=firefox>)包 软件包安装的 Firefox 默认使用国际账户系统，若要切换至中国本地服务，您需要在[此页面](<http://mozilla.com.cn/thread-343905-1-1.html>)安装插件管理器，随后即可使用中国账号登录。 

###  使用 JACK 和 PulseAudio 时某些视频无声

如果您在使用 JACK 和 PulseAudio 时，某些视频没有声音，这可能是因为这些视频使用单声道音频。如果您的 JACK 设置使用超过立体声的配置但您使用普通耳机，则可能会出现这种情况。要修复此问题，只需将 PulseAudio JACK Sink 的 `front-center` 端口连接到系统输出的 `playback_1` 和 `playback_2` 端口。 

您还可以使用脚本自动完成此操作： 
    
    jack-mono.sh
    
    #!/bin/sh
    jack_connect "PulseAudio JACK Sink:front-center" "system:playback_1"
    jack_connect "PulseAudio JACK Sink:front-center" "system:playback_2"

请注意，接收器和端口的名称可能因您的配置而异。您可以使用 [cadence](<https://aur.archlinux.org/packages/cadence/>)AUR 中的 Catia 之类的 Patchbay 查看您的 JACK 设置。 

###  地理定位无法工作

最近，Google 限制了其定位服务在 Arch Linux 上的使用，这会导致网站启用地理定位时出现以下错误：`Geolocation error: Unknown error acquiring position`。诸如 [Hulu](<https://www.hulu.com/>) 之类的区域限制服务可能也会显示类似错误，即使您已允许网站使用位置服务。 

为避免这些问题，您可以切换为 [Mozilla 定位服务](<https://location.services.mozilla.com/>)。在 `about:config` 中将 `geo.provider.network.url` 设置为： 
    
    https://location.services.mozilla.com/v1/geolocate?key=%MOZILLA_API_KEY%
    
详情请参见 [FS#65241](<https://bugs.archlinux.org/task/65241>)。 

###  右键单击在窗口管理器中瞬间选择了第一个选项

此问题在 [i3](<../zh-cn/I3.html> "I3")、[bspwm](<../zh-cn/Bspwm.html> "Bspwm") 和 [xmonad](<../zh-cn/Xmonad.html> "Xmonad") 中都曾被观察到。 

要修复此问题，访问 `about:config` 并将 `ui.context_menus.after_mouseup` 设置为 `true`。 

参见 [[18]](<https://www.reddit.com/r/i3wm/comments/88k0yt/right_mouse_btn_instantly_clicks_first_option_in/>)。 

###  禁用或启用合成后 Firefox 窗口不重绘

取消设置环境变量 `MOZ_X11_EGL`。 

相关错误报告：[Bugzilla 1711039](<https://bugzilla.mozilla.org/show_bug.cgi?id=1711039>)。 

###  每次启动时 Firefox 都请求设为默认浏览器

可以尝试以下方法：如果您使用[桌面环境](<../zh-cn/%E6%A1%8C%E9%9D%A2%E7%8E%AF%E5%A2%83.html> "桌面环境")，检查 Firefox 是否已在系统设置中被设为默认浏览器。如果未设置，请设置为默认浏览器；否则，运行以下 [xdg-settings(1)](<https://man.archlinux.org/man/xdg-settings.1>) 命令（由 [xdg-utils](<../zh-cn/Xdg-utils.html> "Xdg-utils") 软件包提供）查询系统默认浏览器： 
    
    $ xdg-settings get default-web-browser
    
如果未返回值或默认浏览器不是 Firefox，请运行以下命令设置： 
    
    $ xdg-settings set default-web-browser firefox.desktop
    
如果 Firefox 仍提示设为默认浏览器，您可以通过设置处理 _http_ 和 _https_ URL 协议来解决。运行以下 [xdg-mime(1)](<https://man.archlinux.org/man/xdg-mime.1>) 命令： 
    
    $ xdg-mime default firefox.desktop x-scheme-handler/http
    $ xdg-mime default firefox.desktop x-scheme-handler/https
    
如果仍然无效，请检查是否设置了环境变量 `GTK_USE_PORTAL`（所有值都会触发此问题），如果是，请取消设置。如果问题仍未解决或您未设置此变量，请访问 Firefox 的 `about:config`，检查变量 `widget.use-xdg-desktop-portal` 是否设置为 `true`，如果是，请设置为 `false`。 

如果您希望完全禁用默认浏览器检查，请访问 Firefox 的 `about:config`，将 `browser.shell.checkDefaultBrowser` 设置为 `false`。 

###  视频卡顿

如果您发现视频播放卡顿，并且注意到 Firefox 在观看视频（尤其是高分辨率视频）时仅占用一个核心达到 100%，以下方法可能对您有所帮助。 

访问 `about:config`，搜索 `dom.ipc.processCount`，并将 `dom.ipc.processCount.file` 从 1 改为更高的值。一种临时方法是每次增加一个值，直到效果满意，但 4 通常是一个不错的选择。 

###  孟加拉字体在某些页面损坏

在大多数情况下，安装 [noto-fonts](<https://archlinux.org/packages/?name=noto-fonts>)包 并将 **Noto Sans Bengali** 设置为**字体** 设置中的默认字体即可解决问题。然而，在一些社交媒体网站中，孟加拉字体可能仍然会损坏。在这些情况下，Mozilla 提供了详细的指南，帮助查看页面中加载了哪些字体。使用[页面检查器](<https://developer.mozilla.org/en-US/docs/Tools/Page_Inspector/How_to/Open_the_Inspector>)，查找[所有加载的字体](<https://developer.mozilla.org/en-US/docs/Tools/Page_Inspector/How_to/Edit_fonts#all_fonts_on_page>)。通过从系统中删除除 **Noto Sans** 外的其他字体，可以永久解决该问题。 

某些字体是作为其他软件包的依赖项安装的。例如，[chromium](<https://archlinux.org/packages/?name=chromium>)包 会将 [ttf-liberation](<https://archlinux.org/packages/?name=ttf-liberation>)包 安装为依赖项，后者会在一些 Firefox 页面中自动加载，并破坏这些页面上的孟加拉字体。为了解决这个问题，可以在[字体配置](<../zh-cn/%E5%AD%97%E4%BD%93%E9%85%8D%E7%BD%AE.html> "字体配置")中使用以下规则： 
    
    $XDG_CONFIG_HOME/fontconfig/fonts.conf
    
    <match target="pattern">
     <test qual="any" name="family"><string>Liberation</string></test>
     <edit mode="assign" name="family" binding="same"><string>Noto Sans Bengali</string></edit>
    </match>

###  语音接口没有语音

Firefox 使用 speechd 进行文本转语音（tts）。你可以使用命令 `spd-say "some test sentence"` 测试是否能朗读文本，或者使用 `spd-say -L` 获取语音列表。如果没有语音，你可以通过安装 [espeak-ng](<https://archlinux.org/packages/?name=espeak-ng>)包 包来获得一些语音。如果它们无法直接使用，可能需要进行配置。你可以使用 `spd-conf` 命令或编辑配置文件 `.config/speech-dispatcher/speechd.conf`。配置文件中应包含以下行（前面没有 #）： 
    
    AddModule "espeak-ng"                "sd_espeak-ng" "espeak-ng.conf"
    DefaultModule espeak-ng
    
###  阅读模式中缺少大声朗读图标

####  启用语音合成

根据 [[19]](<https://developer.mozilla.org/zh-CN/docs/Web/API/Web_Speech_API/Using_the_Web_Speech_API>)，语音合成必须启用（默认情况下已启用）。要启用它，请在 `about:config` 中将 `media.webspeech.synth.enabled` 设置为 `true`。 

####  禁用指纹识别保护

根据 [[20]](<https://support.mozilla.org/zh-CN/kb/Firefox%20%E9%92%88%E5%AF%B9%E6%8C%87%E7%BA%B9%E6%94%B6%E9%9B%86%E7%9A%84%E4%BF%9D%E6%8A%A4>)，指纹识别保护会禁用 WebSpeech API。如果启用了此选项，你需要禁用它才能使朗读器正常工作。要禁用指纹识别保护，请在 `about:config` 中将 `privacy.resistFingerprinting` 设置为 `false`。 

####  禁用过滤语音

如果看不到朗读图标，请尝试在 `about:config` 中将 `narrate.filter-voices` 设置为 `false`。 

这可以用来检查 `speech-dispatcher` 是否工作。如果有效，可能是由于打开阅读模式的文章语言没有安装对应的语音（检查 `spd-say -L`）。如果已经安装了文章语言的语音，可能存在与 `speech-dispatcher` 配置相关的不正确设置或默认值。 

###  下载文件时文件对话框无法打开

如果在下载文件时没有显示文件选择器，即使在 Firefox 设置中启用了“始终询问保存位置”选项，也可能是你没有同时安装 [xdg-desktop-portal](<https://archlinux.org/packages/?name=xdg-desktop-portal>)包 和合适的实现。桌面环境通常提供实现，但如果你使用的是独立的窗口管理器，如 [i3](<../zh-cn/I3.html> "I3")，则可能需要手动安装。[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [xdg-desktop-portal](<https://archlinux.org/packages/?name=xdg-desktop-portal>)包，例如 [xdg-desktop-portal-gtk](<https://archlinux.org/packages/?name=xdg-desktop-portal-gtk>)包。 

###  在平铺式窗口管理器或 Wayland 混成器中通知不浮动

如果你使用的是平铺式[窗口管理器](<../zh-cn/%E7%AA%97%E5%8F%A3%E7%AE%A1%E7%90%86%E5%99%A8.html#%E5%B9%B3%E9%93%BA%E7%AA%97%E5%8F%A3%E7%AE%A1%E7%90%86%E5%99%A8> "窗口管理器")或 [Wayland 混成器](<../zh-cn/Wayland.html#%E5%B9%B3%E9%93%BA%E5%BC%8F> "Wayland")，并且 HTML 通知显示为正常的 Firefox 窗口而不是浮动弹出窗口，则需要[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [libnotify](<https://archlinux.org/packages/?name=libnotify>)包 并确保你有一个正常工作的[桌面通知程序](<../zh-cn/%E6%A1%8C%E9%9D%A2%E9%80%9A%E7%9F%A5%E7%A8%8B%E5%BA%8F.html> "桌面通知程序")服务器，例如 [mako](<https://archlinux.org/packages/?name=mako>)包。 

##  参见

  * [官方网站](<https://www.mozilla.org/firefox/>)
  * [Mozilla 基金会](<https://www.mozilla.org/>)
  * [MozillaWiki:Firefox](<https://wiki.mozilla.org/Firefox> "mozillawiki:Firefox")
  * [zhwp:Mozilla Firefox](<https://zh.wikipedia.org/wiki/Mozilla_Firefox> "zhwp:Mozilla Firefox")
  * [Firefox 附加组件](<https://addons.mozilla.org/>)
  * [Firefox 主题](<https://addons.mozilla.org/firefox/themes/>)
  * [Mozilla 的 FTP](<https://ftp.mozilla.org/pub/firefox/releases/>)
  * [mozillaZine](<https://forums.mozillazine.org/>) 非官方论坛
