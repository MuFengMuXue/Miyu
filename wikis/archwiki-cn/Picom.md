**翻译状态：**

  * 本文（或部分内容）译自 [Picom](<https://wiki.archlinux.org/title/Picom> "arch:Picom")，最近一次同步于 2024-09-12，若英文版本有所[更改](<https://wiki.archlinux.org/title/Picom?diff=0&oldid=788010>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Picom_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[picom](<https://github.com/yshui/picom>) 是一个独立的 [Xorg](<../zh-cn/Xorg.html> "Xorg") [合成器](<../zh-cn/Xorg.html#%E5%90%88%E6%88%90> "Xorg")，适合与没有合成功能的[窗口管理器](<../zh-cn/%E7%AA%97%E5%8F%A3%E7%AE%A1%E7%90%86%E5%99%A8.html> "窗口管理器")一起使用。picom 是 [compton](<https://github.com/chjj/compton/>) 的一个分支，而 compton 是 [xcompmgr](<../zh-cn/Xcompmgr.html> "Xcompmgr") 分支 [xcompmgr-dana](<https://web.archive.org/web/20150429182855/http://oliwer.net/xcompmgr-dana/>) 的一个分支。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [picom](<https://archlinux.org/packages/?name=picom>)包 软件包或开发者版本 [picom-git](<https://aur.archlinux.org/packages/picom-git/>)AUR。 

##  配置

默认的配置位于 `/etc/xdg/picom.conf` 中，若要修改，请先将其复制到 `~/.config/picom/picom.conf` 或 `~/.config/picom.conf`。 

若要让 picom 使用其他的自定义配置文件，请使用如下的命令： 
    
    $ picom --config _path/to/_ picom.conf
    
详情请参阅 [picom(1) § CONFIGURATION FILES](<https://man.archlinux.org/man/picom.1#CONFIGURATION_FILES>)。 

###  为某些窗口禁用阴影效果

可按需使用 `shadow-exclude` 选项以禁用窗口阴影。有关已禁用的窗口，参见[这个链接](<https://github.com/yshui/picom/blob/b66e5fd422820460f030db853109e4d50bb3549d/picom.sample.conf#L46>)。 

若要禁用菜单的阴影效果，请将以下内容添加至 `picom.conf` 中的 `wintypes`： 
    
    # menu        = { shadow = false; };
    dropdown_menu = { shadow = false; };
    popup_menu    = { shadow = false; };
    utility       = { shadow = false; };
    
EWMH 标准中定义了其他可用的 `WINDOW_TYPE` 值：`unknown`、`desktop`、`dock`、`toolbar`、`menu`、`utility`、`splash`、`dialog`、`normal`、`dropdown_menu`、`popup_menu`、`tooltip`、`notification`、`combo` 以及 `dnd`。 

###  不透明度

若要为聚焦和非聚焦的窗口（如终端模拟器）设置不透明度（实际上是透明度），将以下内容添加至 `picom.conf`： 
    
    opacity-rule = [
      "90:class_g = 'URxvt' && focused",
      "60:class_g = 'URxvt' && !focused"
    ];
    
另见 [#选项卡式窗口（阴影和透明度）](<#%E9%80%89%E9%A1%B9%E5%8D%A1%E5%BC%8F%E7%AA%97%E5%8F%A3%EF%BC%88%E9%98%B4%E5%BD%B1%E5%92%8C%E9%80%8F%E6%98%8E%E5%BA%A6%EF%BC%89>). 

##  使用

可在会话期间的任意时间点手动启用或禁用 picom，或作为会话的一个后台进程自动启动。有一些可选参数用于调整 picom 所提供的合成效果。这些效果包括： 

  * `-b`：作为会话的一个后台进程运行（例如，随窗口管理器 [Openbox](<../zh-cn/Openbox.html> "Openbox") 启动）
  * `-c`：启用阴影效果
  * `--config`：使用指定的配置文件

**注意：**`-C`（禁用面板和停靠栏的阴影效果）和 `-G`（禁用应用程序窗口和拖放对象的阴影效果）参数已弃用，类似功能请参考 [#为某些窗口禁用阴影效果](<#%E4%B8%BA%E6%9F%90%E4%BA%9B%E7%AA%97%E5%8F%A3%E7%A6%81%E7%94%A8%E9%98%B4%E5%BD%B1%E6%95%88%E6%9E%9C>)。

更多可用选项，包括设置需要管理的时机和显示效果，菜单、窗口边框和不活跃应用程序的菜单的不透明度，参见 [picom(1)](<https://man.archlinux.org/man/picom.1>)。 

**注意：** 其他[合成管理器](<../zh-cn/Xorg.html#%E5%90%88%E6%88%90> "Xorg")应当在 _picom_ 运行之前启动。

要在会话期间手动启用默认的合成效果，请使用以下命令： 
    
    $ picom &
    
要作为会话的后台进程自动启动 picom，可以使用 `-b` 参数（有可能导致显示画面冻结）： 
    
    $ picom -b
    
以下是使用需要传值的额外参数的例子： 
    
    $ picom -cfF -o 0.38 -O 200 -I 200 -t 0 -l 0 -r 3 -D2 -m 0.88
    
##  多显示器

若在没有 xinerama（意味着以多个屏幕启动 X 服务）的情况下使用了[多显示器](<../zh-cn/%E5%A4%9A%E6%98%BE%E7%A4%BA%E5%99%A8.html> "多显示器")的配置，picom 默认只会在一个屏幕上运行。可以使用 `DISPLAY` 环境变量令其在所有屏幕上运行。例如，在 X 上标识符为 0 的屏幕后台运行 picom： 
    
     DISPLAY=":0" picom -b
    
上述命令在所有显示器上都应该生效。若无效，请尝试旧方法，指定每一个显示器： 
    
    seq 0 3 | xargs -l1 -I@ picom -b -d :0.@
    
##  灰度

可以使用[着色器](<https://learnopengl.com/Getting-started/Shaders>)将窗口颜色转换为灰度。 

根据 [picom(1)](<https://man.archlinux.org/man/picom.1>)，从 [picom 的源码](<https://github.com/yshui/picom/blob/next/compton-default-fshader-win.glsl>)中编辑默认的着色器。 
    
    _/path/to/shader/file.glsl_
    
    #version 330
    
    in vec2 texcoord;
    uniform sampler2D tex;
    uniform float opacity;
    
    vec4 default_post_processing(vec4 c);
    
    vec4 window_shader() {
    	vec2 texsize = textureSize(tex, 0);
    	vec4 color = texture2D(tex, texcoord / texsize, 0);
    
    	color = vec4(vec3(0.2126 * color.r + 0.7152 * color.g + 0.0722 * color.b) * opacity, color.a * opacity);
    
    	return default_post_processing(color);
    }

将编辑好的文件路径引入着色器后启动 picom。或许还需要 `glx` 后端。 
    
    $ picom --backend glx --window-shader-fg /path/to/shader/file.glsl
    
##  故障排除

近期的 picom 版本在 DRI2 加速上存在一些问题，表现为使用 DRI2 时出现严重的画面闪烁（[picom bug](<https://github.com/yshui/picom/issues/47>)、[mesa bug](<https://bugs.freedesktop.org/show_bug.cgi?id=108651>)）。此问题已经过反馈和修复，但仍可能会影响某些用户。DRI3 则不受该问题的影响。 

使用合成效果可能会导致一些问题，例如在与其他应用程序一起使用时，错误的配置会引起显示故障。 

### Conky

若要禁用 [Conky](<../zh-cn/Conky.html> "Conky") 窗口的环绕阴影，请将以下内容添加至 `~/.conkyrc`： 
    
    own_window_class conky
    
若使用模糊特效时，上述方法无效，请在 `~/.conkyrc` 中尝试如下配置： 
    
    own_window_type= 'desktop'
    
###  dwm 和 dmenu

picom 所有能自动排除窗口管理器元素的功能都无法检测到 [dwm](<../zh-cn/Dwm.html> "Dwm") 的状态栏。无论是 dwm 的状态栏还是 [dmenu](<../zh-cn/Dmenu.html> "Dmenu") 都没有固定的窗口 id。若要将其从不活跃窗口透明化中排除，要么在源码中加入一个窗口类，要么使用不那么精确的属性将其排除。下面的示例将 dwm 的状态栏置于顶部，这样就可以实现与位置排除无关的分辨率： 
    
    $ picom <任意的其他参数> --focus-exclude "x = 0 && y = 0 && override_redirect = true"
    
或者在使用的配置文件中配置如下内容： 
    
    focus-exclude = "x = 0 && y = 0 && override_redirect = true";
    
对于大多数窗口来说，覆盖重定向属性的值似乎都是 false，在排除规则中使用此属性可以防止在左上角绘制的其他窗口被排除在外（例如，当 dwm 状态栏被隐藏时，x0 y0 将与 dwm 主堆栈（master stack）中的任何内容相匹配）。 

### Firefox

参见 [#为某些窗口禁用阴影效果](<#%E4%B8%BA%E6%9F%90%E4%BA%9B%E7%AA%97%E5%8F%A3%E7%A6%81%E7%94%A8%E9%98%B4%E5%BD%B1%E6%95%88%E6%9E%9C>)。 

要禁用[火狐浏览器](<../zh-cn/Firefox.html> "火狐")元素的阴影效果，将以下内容添加至 `picom.conf` 中的 shadow-exclude： 
    
    "class_g = 'firefox' && argb",
    
详情请参考[这个链接](<https://github.com/chjj/compton/issues/201#issuecomment-45288510>)。 

### slock

使用 [slock](<../zh-cn/Slock.html> "Slock") 时，开启不活跃窗口透明化效果（以 `-i` 参数启动）可能会导致麻烦的问题。一种解决方法是将透明度修改为 `0.2`。例如，以 picom 参数运行命令： 
    
    $ picom <任意的其他参数> -i 0.2
    
或者在使用的配置文件中配置如下内容： 
    
    inactive-dim = 0.2;
    
另一种方式是，通过 slock 的窗口 id 将其排除在外，或排除所有无名称的窗口。 

**注意：** 某些程序在每次运行新实例时都会改变 id，但 slock 的 id 是固定的。有相关知识的用户会去确认 slock 的 id 是否真的是固定不变的，至此，请谨慎使用排除方法。

使用如下的选项排除所有无名称的窗口： 
    
    $ picom <其他参数> --focus-exclude "! name~=''"
    
运行以下命令以找出 slock 的窗口 id： 
    
    $ xwininfo & slock
    
在 slock 退出前快速点击屏幕上的任意位置，然后输入密码解锁。应该可以看到输出中的窗口 id： 
    
    xwininfo: Window id: 0x1800001 (has no name)
    
提取该 id 并在 picom 中将其排除： 
    
    $ picom <任意的其他参数> --focus-exclude 'id = 0x1800001'
    
或者在使用的配置文件中配置如下内容： 
    
    focus-exclude = "id = 0x1800001";
    
###  画面闪烁（Flicker）

以默认的 `picom.conf` 应用于最大化窗口（无面板的会话中）会引发此问题，可以通过以下选项解决： 
    
    unredir-if-possible = false;
    
详情请参见[这个链接](<https://github.com/chjj/compton/issues/402>)。 

###  全屏撕裂

若仅在全屏播放视频时观察到屏幕撕裂，请参考 [#画面闪烁（Flicker）](<#%E7%94%BB%E9%9D%A2%E9%97%AA%E7%83%81%EF%BC%88Flicker%EF%BC%89>)。 

###  使用 xft 字体时显示延迟

若在使用了 Xft 字体的应用程序（例如 [xterm](</wzh/index.php?title=Xterm&action=edit&redlink=1> "Xterm（页面不存在）")（英语：[xterm](<https://wiki.archlinux.org/title/xterm> "en:xterm")） 和 [urxvt](<../zh-cn/Rxvt-unicode.html> "Urxvt")）中遇到严重的显示延迟，请尝试以下选项： 
    
    --xrender-sync --xrender-sync-fence
    
或使用 xrender 后端。 

详情请参见[这个链接](<https://github.com/chjj/compton/issues/152>)。 

###  选项卡式窗口（阴影和透明度）

以选项卡式显示的透明化窗口，其后方的选项卡式窗口由于透明度的原因依然可见。每个选项卡式窗口都会绘制自己的阴影，这会导致多重阴影。 

可将以下内容添加至已有的[阴影效果排除列表](<https://github.com/yshui/picom/blob/248bffede73e520a4929dd7751667d29d4169d59/picom.sample.conf#L175-L181>)中以解决多重阴影的问题： 
    
    "_NET_WM_STATE@:32a *= '_NET_WM_STATE_HIDDEN'"
    
将下面的内容添加至 `picom.conf` 中可禁用绘制后方选项卡式窗口： 
    
    opacity-rule = [
      "95:class_g = 'URxvt' && !_NET_WM_STATE@:32a",
      "0:_NET_WM_STATE@[0]:32a *= '_NET_WM_STATE_HIDDEN'",
      "0:_NET_WM_STATE@[1]:32a *= '_NET_WM_STATE_HIDDEN'",
      "0:_NET_WM_STATE@[2]:32a *= '_NET_WM_STATE_HIDDEN'",
      "0:_NET_WM_STATE@[3]:32a *= '_NET_WM_STATE_HIDDEN'",
      "0:_NET_WM_STATE@[4]:32a *= '_NET_WM_STATE_HIDDEN'"
    ];
    
注意，`URxvt` 是终端的 Xorg 类名。若使用不同的终端，请更改该类名。运行命令 `xprop WM_CLASS` 并点击一个窗口以查询该窗口的类名称。 

详情请参见[这个链接](<https://www.reddit.com/r/unixporn/comments/330zxl/webmi3_no_more_overlaying_shadows_and_windows_in/>)。 

**警告：** 使用 i3 并以 kitty 作为终端时，上述操作（截至 2020-08-31）会在重新加载 i3 时冻结所有选项卡式的 kitty 实例（参见[这个链接](<https://github.com/kovidgoyal/kitty/issues/1681>)），可能的解决方案可在一个类似的[问题](<../zh-cn/Intel_graphics.html#DRI3_issues> "Intel graphics")中找到。

###  Xsetroot 无法更改背景颜色

目前，picom 不兼容 `xsetroot` 的 `-solid` 选项，一种解决方法是使用 [hsetroot](<https://archlinux.org/packages/?name=hsetroot>)包 更改背景颜色： 
    
    $ hsetroot -solid '#000000'
    
详情请参见[这个链接](<https://github.com/chjj/compton/issues/162>)。 

###  使用 NVIDIA 专有驱动时遇屏幕撕裂

请在 `picom.conf` 中尝试以下设置： 
    
    vsync = true;
    
###  使用 NVIDIA 专有驱动和 FullCompositionPipeline 时有显示延迟

请尝试以如下参数运行 picom： 
    
    --backend xrender
    
或在 `picom.conf` 中添加如下的配置项： 
    
    backend = "xrender";
    
详情请参见[这个链接](<https://github.com/chjj/compton/issues/208>)。 

另一个降低延迟的方法是在 nvidia 的 OpenGL 设置中禁用“允许翻转”（disable "allow flipping"，参见[这个链接](<https://github.com/yshui/picom/issues/620#issuecomment-869666038>)）。也可以用命令行实现同样的效果： 
    
    $ nvidia-settings -a 'AllowFlipping=0'
    
要在重启后加载设置（参见[自动启动](<../zh-cn/%E8%87%AA%E5%8A%A8%E5%90%AF%E5%8A%A8.html> "自动启动")），请运行： 
    
    $ nvidia-settings --load-config-only
    
###  使用 NVIDIA 专有驱动时 Xorg 会泄漏 GPU 的内存

参见 [#使用 NVIDIA 专有驱动和 FullCompositionPipeline 时有显示延迟](<#%E4%BD%BF%E7%94%A8_NVIDIA_%E4%B8%93%E6%9C%89%E9%A9%B1%E5%8A%A8%E5%92%8C_FullCompositionPipeline_%E6%97%B6%E6%9C%89%E6%98%BE%E7%A4%BA%E5%BB%B6%E8%BF%9F>)。 

###  设备挂起后 slock 相关问题

若使用 systemd 服务在挂起或休眠时触发 slock，设备屏幕可能在恢复后的几秒中内没有锁定。禁用窗口淡入淡出效果以防止此问题发生： 
    
    $ picom --no-fading-openclose
    
###  屏幕共享

将以下内容添加至 `shadow-exclude` 可防止出现屏幕共享上的阴影覆盖和 [Zoom Meetings](</wzh/index.php?title=Zoom_Meetings&action=edit&redlink=1> "Zoom Meetings（页面不存在）")（英语：[Zoom Meetings](<https://wiki.archlinux.org/title/Zoom_Meetings> "en:Zoom Meetings")） 弹出窗口的阴影效果： 
    
    shadow-exclude = [
      "name = 'cpt_frame_xcb_window'",
      "class_g ?= 'zoom'",
    ];
    
按照如下内容将 [Zoom Meetings](</wzh/index.php?title=Zoom_Meetings&action=edit&redlink=1> "Zoom Meetings（页面不存在）")（英语：[Zoom Meetings](<https://wiki.archlinux.org/title/Zoom_Meetings> "en:Zoom Meetings")） 添加至 `blur-background-exclude` 中可禁用屏幕共享时的模糊效果。 
    
    blur-background-exclude = [
      "class_g ?= 'zoom'",
    ];
    
对于 Microsoft Teams，分享内容的红色外边框是以一个几乎完全透明的窗口实现的。启用模糊效果将导致该功能无法使用，应按照如下方式禁用模糊效果： 
    
    shadow-exclude = [
      "name = 'rect-overlay'",
    ];
    
    blur-background-exclude = [
      "name = 'rect-overlay'",
    ];
    
###  切换工作区时禁用窗口的淡入淡出效果

添加 `--fade-in-step=1 --fade-out-step=1 --fade-delta=0` 标识可以在切换至新的工作区时禁用窗口的淡入淡出效果。参见[这个链接](<https://github.com/yshui/picom/issues/354#issuecomment-835809210>)。 

##  另见

  * [在 XFCE 或 LXDE 上使用 Compton 作为无撕裂的窗口合成器](<https://ubuntuforums.org/showthread.php?t=2144468&p=12644745#post12644745>)
