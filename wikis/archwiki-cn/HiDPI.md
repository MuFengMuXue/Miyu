[![](../File:Tango-preferences-desktop-locale-modified.png)](<../File:Tango-preferences-desktop-locale-modified.png>)**这篇文章或章节的[翻译](<../Project:%E8%B4%A1%E7%8C%AE.html#Translating> "Project:Contributing")质量不佳。**

**原因：** Not in sync with the English page, some sections are untranslated.（在 [Talk:HiDPI#](<../zh-cn/Talk:HiDPI.html>) 中讨论）

**翻译状态：**

  * 本文（或部分内容）译自 [HiDPI](<https://wiki.archlinux.org/title/HiDPI> "arch:HiDPI")，最近一次同步于 2018-09-04，若英文版本有所[更改](<https://wiki.archlinux.org/title/HiDPI?diff=0&oldid=532530>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/HiDPI_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [Font configuration](<../zh-cn/Font_configuration.html> "Font configuration")

HiDPI（High Dots Per Inch）显示器，指的是在较小尺寸下却拥有较高分辨率的显示器。Apple 将其称作“[视网膜屏幕](<https://en.wikipedia.org/wiki/Retina_Display> "wikipedia:Retina Display")”，这项技术主要存在于高端笔记本电脑和显示器中。 

并非所有的软件都在高分辨率屏幕下工作良好。此页列出了一些常见的调整方法，让您更好的使用 HiDPI 显示器。 

##  桌面环境

### GNOME

可在**设置** > **设备** > **显示** > **缩放** 中设置合理的数值。也可以使用 gsettings 进行设置： 
    
    $ gsettings set org.gnome.settings-daemon.plugins.xsettings overrides "[{'Gdk/WindowScalingFactor', <2>}]"
    $ gsettings set org.gnome.desktop.interface scaling-factor 2
    
**注意：**`scaling-factor`仅能设置为整数。1 = 100%，2 = 200%，依此类推。非整数倍缩放请见下。

####  非整数倍缩放

在某些设备（例如小平板电脑）上使用 `scaling-factor`设置整数倍缩放的效果可能并不理想。wayland 和 Xorg 均支持非整数倍缩放，但步骤不同： 

##### Wayland

启用实验性的非整数倍缩放功能： 
    
    $ gsettings set org.gnome.mutter experimental-features "['scale-monitor-framebuffer']"
    
之后再次打开**设置** > **设备** > **显示** 。如果没有立即生效，请尝试重启。 

**注意：** 使用 Xwayland 的旧程序，因为渲染方法不同，在非 100% 缩放下都可能出现字体模糊的问题。

如要为所有用户启用，需创建如下三个文件： 
    
    /etc/dconf/profile/user
    
    user-db:user
    system-db:local
    
    /etc/dconf/db/local.d/00-hidpi
    
    [org/gnome/mutter]
    experimental-features=['scale-monitor-framebuffer']
    
    /etc/dconf/db/locks/hidpi
    
    /org/gnome/mutter/experimental-features
    
运行`dconf update`并重启系统。这将永久锁定选项。 

##### Xorg

您可以同时使用 `scaling-factor` 和 [xrandr](<../zh-cn/Xrandr.html> "Xrandr") 来实现任意的非整数倍缩放。这可以使 TTF 字体被正确缩放，防止出现单独使用 `xrandr` 时出现的模糊现象。您可以使用 `gsettings` 来指定放大系数，并用 [xrandr](<../zh-cn/Xrandr.html> "Xrandr") 指定缩小系数。 

首先使将缩放设为“UI看起来太大”的最小值。通常 2 已经足够大，如果不够大就继续尝试 3 以及更大的数。之后使用 [xrandr](<../zh-cn/Xrandr.html> "Xrandr") 设置缩小系数。首先获取相关的输出名称，下面的例子将使用 `eDP1` 。先试着将缩小系数设为1.25，如果 UI 看起来仍然太大，则增大缩放系数。反之则缩小缩放系数。 
    
    $ xrandr --output eDP1 --scale 1.25x1.25
    
**注意：** 如果你的鼠标光标移动范围和屏幕显示并不匹配，你可能需要同时使用 `--panning`。参阅[#Side display](<#Side_display>)。

可考虑使用[autorandr](<https://archlinux.org/packages/?name=autorandr>)包让设置在重启时保持不变。参考[这个网页](<https://askubuntu.com/questions/754231/how-do-i-save-my-new-resolution-setting-with-xrandr/1130337>)获取更多信息。 

[![](../File:Tango-view-refresh-red.png)](<../File:Tango-view-refresh-red.png>)**本文或本节内容已经过时。**

**原因：** 需要GNOME用户验证是否仍然需要重新编译。 (在[Talk:HiDPI](<../zh-cn/Talk:HiDPI.html>)讨论)

在GNOME设置守护进程中的xsettings插件中，DPI设置是硬编码的。这将忽略Xorg的设置。这里有一篇[重编译 Gnome Settings Daemon](<http://blog.drtebi.com/2012/12/changing-dpi-setting-on-gnome-34.html>)[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2022-09-18 ⓘ]的博客文章。在文档中还介绍了另一种方法来设置 xsettings 的DPI： 

你可以使用dconf编辑器转到这个键值： 
    
    /org/gnome/settings-daemon/plugins/xsettings/overrides
    
加入这个条目： 
    
    'Xft/DPI': <153600>
    
来自 README.xsettings 

注意必须使用这种方式指定（使用<>）。 

上述DPI数值的单位是1024分之一英寸。 

####  字体缩放

可以另外设置字体缩放。在 Gnome Tweak 中的**字体** > **缩放** ，或者也可使用 gsettings。字体缩放倍率不需要是整数。 
    
    $ gsettings set org.gnome.desktop.interface text-scaling-factor 1.5
    
####  Xorg 下的 GTK+ 和 Gnome 外壳元素

在老版本的 Gnome 中（3.35 以前），Gnome 外壳 UI 元素中的字体缩放可能需要以单独编辑界面 CSS 文件的方式单独设置。文件是 `/usr/share/themes/你的主题/gnome-shell/gnome-shell.css`。单独设置其中所有的”font-size“属性，使其与缩放后的 UI 大小一致。设置完后，切换到另一个主题，再切换回来。 

如果需要更改窗口标题栏的字体大小，可以使用 dconf 编辑器。（`org > gnome > desktop > wm > preferences :: titlebar-font`）这同时需要关闭`title-bar-uses-system-fonts`选项。 或者也可使用 gsettings： 
    
    $ gsettings set org.gnome.desktop.wm.preferences titlebar-font 'Cantarell Bold 22' ## 具体内容依需求更改
    $ gsettings set org.gnome.desktop.wm.preferences titlebar-uses-system-font false
    
### KDE

您可以使用KDE的设置来微调字体、图标和部件缩放，这些改动会同时影响 Qt 和 GTK+ 程序。 

要调整整体缩放： 

  1. **系统设置** →**显卡与显示器** →**显示器配置** →**缩放率**
  2. 将滑块调整至适合的位置
  3. 重新启动以使设置生效

要仅调整字体缩放： 

  1. **系统设置** →**外观** →**字体**
  2. 勾选**“固定字体DPI”** 并调整DPI的值。调整之后重新启动应用程序即可生效。要在整个桌面上生效，您需要注销之后重新登录。

要仅调整图标缩放： 

  1. **系统设置** →**外观** →**图标** →**配置图标大小**
  2. 为每一项选择合适的图标大小，更改将会立即生效。

####  非整数倍缩放下的Bug

当您使用非整数倍的缩放比例时，这可能导致一些 Qt 应用程序的字体渲染出现问题（例如 okular）。 

有一个办法可以绕过这个问题： 

  1. 将缩放比例设为1
  2. 用上面的方法调整字体和图标缩放（这会影响所有的应用程序，且不会导致字体问题）
  3. 重新启动KDE
  4. 如果需要缩放 GTK 程序，设置环境变量`GDK_SCALE/GDK_DPI_SCALE`（参见下文）。

####  托盘图标不缩放

在 Xorg 环境下，托盘图标不会跟随整体缩放。Plasma 默认会忽略 Qt 设置。要让 Plasma 使用 Qt 设置，要么使用 Wayland，要么将 `PLASMA_USE_QT_SCALING` 设为1；但对于多台不同 DPI 显示器混用的环境，这会让 UI 显示变得更糟糕。也可以将底栏高度设置为原来的两倍以缩放底栏和底栏内的应用程序图标，此时右键菜单内的图标等其他元素将不会缩放。 

### Xfce

打开**设置管理器** →**外观** →**字体** ，修改 DPI 的值。在 HiDPI 显示器上，通常可以设为180或者192。要获得更精确的数字，可以使用`xdpyinfo | grep resolution`，使用输出DPI两倍的值。 

要增大托盘图标，右键点击托盘的空白处，选择属性，将最大图标大小设置为32,48或者64。 

### Cinnamon

应当开箱即用。 

### Enlightenment

对于E18，首先打开设置面板，在**外观** →**缩放** 中，你可以调整缩放倍数。在MBPr 15 上，你可以选择1.2。 

## X Server

某些程序使用 X Server 所提供的 DPI 值。比如 i3 （[来源](<https://github.com/i3/i3/blob/next/libi3/dpi.c>)） 和 Chromium（[来源](<https://code.google.com/p/chromium/codesearch#chromium/src/ui/views/widget/desktop_aura/desktop_screen_x11.cc>)）。 

[![](../File:Tango-inaccurate.png)](<../File:Tango-inaccurate.png>)**本文或本章节的事实准确性存在争议。**

**原因：** Xorg always sets dpi to 96. See [this](<https://bugs.freedesktop.org/show_bug.cgi?id=23705>), [this](<https://bugs.freedesktop.org/show_bug.cgi?id=41115>) and finally [this](<https://pastebin.com/vtzyBK6e>).（在 [Talk:HiDPI](<../zh-cn/Talk:HiDPI.html>) 中讨论）

要验证 X Server 是否正确检测到了您的显示器的DPI，使用 [xorg-xdpyinfo](<https://archlinux.org/packages/?name=xorg-xdpyinfo>)包 中的 `xdpyinfo` 工具。 
    
    $ xdpyinfo | grep -B 2 resolution
    screen #0:
      dimensions:    3200x1800 pixels (423x238 millimeters)
      resolution:    192x192 dots per inch
    
这个例子中 X Server 检测到的屏幕尺寸并不准确（423mm x 328mm,实际上Dell XPS 9530的屏幕尺寸是346mm x 194mm），但报告的 DPI 是96的整数倍。通常这往往比正确的DPI更好，可以保证字体渲染正确。 

如果 `xdpyinfo` 显示的DPI不正确，参阅[Xorg#Display size and DPI](<../zh-cn/Xorg.html#Display_size_and_DPI> "Xorg")了解如何修复。 

## X Resources

如果你没有使用一个桌面环境，比如 KDE，Xfce，或是没有一个为您操作 Xorg 设置的程序，你可以通过在 [Xresources](</wzh/index.php?title=Xresources&action=edit&redlink=1> "Xresources（页面不存在）") 中的 `Xft.dpi` 变量手动修改DPI设置。 
    
    ~/.Xresources
    
    Xft.dpi: 180
    Xft.autohint: 0
    Xft.lcdfilter:  lcddefault
    Xft.hintstyle:  hintfull
    Xft.hinting: 1
    Xft.antialias: 1
    Xft.rgba: rgb
    
确保设置在X启动时已经被载入。例如在`~/.xinitrc`中使用`xrdb -merge ~/.Xresources`。有关详细信息，请参阅 [Xresources](</wzh/index.php?title=Xresources&action=edit&redlink=1> "Xresources（页面不存在）")。 

通常这会让大多数地方的字体大小正确，但这并不会影响图标大小。 

在设置`Xft.dpi`的同时设置 GUI toolkit 缩放（例如`GDK_SCALE`）可能导致某些程序界面元素过大（例如firefox）。 

## GUI toolkits

### Qt 5

自从 Qt 5.6 开始，Qt 5 应用程序可以遵守屏幕DPI。设置环境变量`QT_AUTO_SCREEN_SCALE_FACTOR`以启用这项功能。 
    
    export QT_AUTO_SCREEN_SCALE_FACTOR=1
    
如果自动检测的 DPI 并不理想，你也可以按屏幕(`QT_SCREEN_SCALE_FACTORS`)或全局(`QT_SCALE_FACTOR`)手动设置缩放，有关详细信息，请参阅 [Qt 博客文章](<https://blog.qt.io/blog/2016/01/26/high-dpi-support-in-qt-5-6/>)。 

**注意：**

  * 如果您手动设置了缩放，则需要设置`QT_AUTO_SCREEN_SCALE_FACTOR=0`。否则某些明确启用 HiDPI 支持的程序会被缩放两次。
  * `QT_SCALE_FACTOR`缩放字体，但`QT_SCREEN_SCALE_FACTORS`并不会。
  * 如果您还在**xrdb** 中手动设置过DPI以支持其他toolkits，同时使用`QT_SCALE_FACTORS`会使字体过大。
  * 如果您有多个不同DPI的屏幕，即 [#Side display](<#Side_display>)，您可能需要设置`QT_SCREEN_SCALE_FACTORS="2;2"`。

还可以采取其他方式，例如固定DPI:
    
    $ QT_FONT_DPI=96 clementine

一个启动WPS表格的实例：
    
    $ QT_SCREEN_SCALE_FACTORS=1 QT_FONT_DPI=192 QT_IM_MODULE=fcitx /usr/bin/et %F

###  GDK 3 (GTK+ 3)

要将UI缩放为两倍大小： 
    
    export GDK_SCALE=2
    
并同时不影响字体： 
    
    export GDK_DPI_SCALE=0.5
    
###  GTK+ 2

GTK+ 2本身并不支持缩放UI。但您可以使用 [themix-full-git](<https://aur.archlinux.org/packages/themix-full-git/>)AUR 创建预缩放过的主题。 

###  Elementary (EFL)

要将缩放倍数设为1.5： 
    
     export ELM_SCALE=1.5
    
更多信息请查看 <https://phab.enlightenment.org/w/elementary/>

##  引导程序

### GRUB

####  降低帧缓冲分辨率

参见[GRUB/Tips and tricks#Setting the framebuffer resolution](<../zh-cn/GRUB/Tips_and_tricks.html#Setting_the_framebuffer_resolution> "GRUB/Tips and tricks")。 

####  改变GRUB字体大小

在`/usr/share/fonts/`中找一个你喜欢的字体。 

使用GRUB工具转换： 
    
    # grub-mkfont -s 30 -o /boot/grubfont.pf2 /usr/share/fonts/_FontFamily/FontName.ttf_
    
**注意：**`-s 30`是字体大小。

编辑`/etc/default/grub`来设置字体。参见[GRUB/Tips and tricks#Background image and bitmap fonts](<../zh-cn/GRUB/Tips_and_tricks.html#Background_image_and_bitmap_fonts> "GRUB/Tips and tricks"): 
    
    GRUB_FONT="/boot/grubfont.pf2"
    
使用`grub-mkconfig -o /boot/grub/grub.cfg`重新生成 GRUB 配置。 

##  应用程序

###  浏览器

#### Firefox

Firefox 应当使用 [#GDK 3 (GTK+ 3)](<#GDK_3_\(GTK+_3\)>) 的设置。但是，建议的 `GDK_SCALE` 可能会使 Firefox 界面的缩放并不一致，并且不能使用小数.你可以使用`GDK_DPI_SCALE`来代替。 

要覆盖这些设置，请打开 Firefox 的高级选项页面（`about:config`）并将 `layout.css.devPixelsPerPx` 设置为 `2`（或是其它需要的数值），但这个选项也可能导致 Firefox 界面的缩放不一致。如果 Firefox 没有缩放字体，您可能需要创建 `userChrome.css` 并添加适当的样式。有关 `userChrome.css`，请访问[mozillaZine](<http://kb.mozillazine.org/index.php?title=UserChrome.css>)。 
    
    ~/.mozilla/firefox/_< profile>_/chrome/userChrome.css
    
    @namespace url("<https://www.mozilla.org/keymaster/gatekeeper/there.is.only.xul>");
    
    /* #tabbrowser-tabs, #navigator-toolbox, menuitem, menu, ... */
    * {
        font-size: 15px !important;
    }
    
    /* exception for badge on adblocker */
    .toolbarbutton-badge {
        font-size: 8px !important;
    }
    
**警告：** 下面的扩展不支持 Firefox Quantum （57版本及以上）。

如果你将 HiDPI 显示器与另一台显示器一起使用，你可以使用 [AutoHiDPI](<https://github.com/ertug/autohidpi>) 来自动调整。另外，从 Firefox 49 以来，它会自动根据您的屏幕分辨率调整缩放，从而更容易处理多个屏幕的情况。 

####  Chromium / Google Chrome

Chromium 应当使用[#GDK 3 (GTK+ 3)](<#GDK_3_\(GTK+_3\)>)设置。 

要覆盖这一选项，请使用`--force-device-scale-factor` flags。这将缩放所有内容。例如：`chromium --force-device-scale-factor=2`。 

当此选项设为1时将会采用正常缩放，此选项也可以使用小数。要永久应用此更改，对于Chromium，可以将其添加到`~/.config/chromium-flags.conf`： 
    
    ~/.config/chromium-flags.conf
    
    --force-device-scale-factor=2

对于Chrome，使用 `~/.config/chrome-flags.conf`。 

如果你将 HiDPI 显示器与另一台显示器一起使用，你可以使用 [reszoom](<https://chrome.google.com/webstore/detail/resolution-zoom/enjjhajnmggdgofagbokhmifgnaophmh>) 扩展。这个扩展将会根据所在屏幕自动调整缩放。 

#### Opera

Opera 应当使用 [#GDK 3 (GTK+ 3)](<#GDK_3_\(GTK+_3\)>) 设置。 

要覆盖这一选项，请使用 `--alt-high-dpi-setting=X` 命令行选项。其中 X 是所需的 DPI。例如，使用 `--alt-high-dpi-setting=144` Opera 将认为 DPI 是 144。在较新版本中，Opera 将使用字体DPI（在 KDE 中可以强制设置字体 DPI）。 

### Thunderbird

参见[#Firefox](<#Firefox>)。要访问 `about:config`，打开**首选项** →**高级** →**配置编辑器** 。 

###  Wine程序

运行 
    
    $ winecfg
    
并且更改**显示** 选项卡中的 DPI。这仅影响字体大小。 

### Skype

Skype for Linux ([skypeforlinux-stable-bin](<https://aur.archlinux.org/packages/skypeforlinux-stable-bin/>)AUR) 使用 [#GDK 3 (GTK+ 3)](<#GDK_3_\(GTK+_3\)>)。 

### Spotify

您可以简单的使用 `Ctrl++` 和 `Ctrl+-` 来调整缩放。使用 `Ctrl+0` 来恢复默认缩放。缩放设置保存在`~/.config/spotify/Users/YOUR-SPOTIFY-USER-NAME/prefs`，您可能需要自行创建该设置文件： 
    
    ~/.config/spotify/Users/YOUR-SPOTIFY-USER-NAME/prefs
    
    app.browser.zoom-level=100
    
Spotify 也可以使用自定义的缩放启动。这个系数和`~/.config/spotify/Users/YOUR-SPOTIFY-USER-NAME/prefs`中的系数相乘的积是实际的缩放倍数。 
    
    $ spotify --force-device-scale-factor=1.5
    
###  Zathura 文档查看器

文档缩放应当开箱即用。 

UI缩放可以在[配置文件](<https://pwmt.org/projects/zathura/documentation/>)中设置 （注意 "font" 是一个[girara option](<https://pwmt.org/projects/girara/options/>))： 
    
    set font "monospace normal 20"
    
### Sublime Text 4

Sublime Text 4 完整支持显示缩放。在**首选项** →**设置** 中添加 `"ui_scale": 2.0` 。 

### IntelliJ IDEA

IntelliJ IDEA 15 及以上应有对 HiDPI 的支持，[[1]](<https://blog.jetbrains.com/idea/2015/07/intellij-idea-15-eap-comes-with-true-hidpi-support-for-windows-and-linux/>) 如果这不能工作最简便的解决办法可能是覆盖默认的字体设置： 

    _File - > Settings -> Behaviour & Appearance -> Appearance_

[14版本](<https://youtrack.jetbrains.com/issue/IDEA-114944>)中将 `-Dhidpi=true` 添加到 `$HOME/.IdeaC14/` 或 `/usr/share/intelligj-idea-ultimate-edition/bin/` 的方法应该不再需要了。 

### NetBeans

NetBeans 可以在启动时用`--fontsize`选项设置字体大小。要要使此设置永久生效，编辑`/usr/share/netbeans/etc/netbeans.conf`，添加`--fontsize`到`netbeans_default_options`。[[2]](<https://web.archive.org/web/20210117211145/http://wiki.netbeans.org/FaqFontSize>)

编辑器字体大小可以在 Tools → Option → Fonts & Color 中设置。 

输出窗口的字体大小可以在Tools → Options → Miscelaneous → Output中控制。 

### Gimp 2.8

使用 HiDPI主题，或是更改现有主题的 `gtkrc`。(Change all occurrences of the size `button` to `dialog`，例如`GimpToolPalette::tool-icon-size`。） 

另外也有 [gimp-hidpi](<https://github.com/jedireza/gimp-hidpi>)。 

### Steam

####  官方 HiDPI支持

  * 从2018年1月25日开始，测试版本已经支持HiDPI并能自动启用。
  * **Steam** →**设置** →**界面** →**勾选** **"按照显示器大小放大图标和文本（需要重启）"**
  * 如果自动检测并不能正确工作，使用`GDK_SCALE=2`来指定缩放级别。
  * 如果以上不工作,使用`steam -forcedesktopscaling 2`或者设置`STEAM_FORCE_DESKTOPUI_SCALING=2.0`。[[3]](<https://github.com/ValveSoftware/steam-for-linux/issues/9209#issuecomment-1594505259>)在2023年6月UI大改动之后,该参数还支持分数缩放级别,例如`1.25`。

####  非官方

使用 [HiDPI-Steam-Skin](<https://github.com/MoriTanosuke/HiDPI-Steam-Skin>) 可以增大字体大小，虽然并不完美，但至少能用。 

**注意：** 皮肤的 README 列出了皮肤应当放置的位置。正确的位置下面应该有一个叫 `skins_readme.txt`的文件。

[MetroSkin Unofficial Patch](<https://steamcommunity.com/groups/metroskin/discussions/0/517142253861033946/>) 也可以使用。 

###  Java 程序

可以通过设置 `sun.java2d.uiScale` 来缩放使用 AWT/Swing 框架的 Java 程序。例如： 
    
    java -Dsun.java2d.uiScale=2 -jar some_application.jar
    
从 Java 9 开始，`GDK_SCALE` 也可以缩放 Swing 程序。 

###  Mono 程序

根据 [[4]](<https://bugzilla.xamarin.com/35/35870/bug.html>)，Mono 程序应像 [GTK3](<#GDK_3_\(GTK+_3\)>) 程序一样缩放。 

### MATLAB

[MATLAB](<../zh-cn/MATLAB.html> "MATLAB") 的近期版本(R2017b)可以设置缩放： 
    
    >> s = settings;s.matlab.desktop.DisplayScaleFactor
    >> s.matlab.desktop.DisplayScaleFactor.PersonalValue = 2
    
此设置将在重启 Matlab 后生效。 

### VirtualBox

**注意：** 仅适用于启用了缩放的 KDE。

VirtualBox 按照系统的缩放级别缩放虚拟监视器，从而降低虚拟机的最大分辨率（参见[[5]](<https://www.virtualbox.org/ticket/16604>)）。 

可以单独缩小 VirtualBox 来绕过这个问题： 
    
    $ QT_SCALE_FACTOR=0.5 VirtualBox --startvm vm-name
    
### Zoom

可以指定`QT_SCALE_FACTOR`来启动 Zoom： 
    
    $ QT_SCALE_FACTOR=2 zoom
    
###  不支持的程序

[run_scaled-git](<https://aur.archlinux.org/packages/run_scaled-git/>)AUR 可以缩放应用程序（内部使用[xpra](<https://archlinux.org/packages/?name=xpra>)包）。 

另一个办法是使每个程序在各自的 VNC 桌面上运行。要缩放 VNC 查看器，使用[vncdesk-git](<https://aur.archlinux.org/packages/vncdesk-git/>)AUR。你可以为每个程序设置单独的桌面，使用简单的命令启动客户端和服务端，例如`vncdesk 2`。 

[x11vnc](<../zh-cn/X11vnc.html> "X11vnc") 有一个实验性的选项 `-appshare`，可以为每个窗口单独打开一个 VNC 查看器。也许我们可以在上面做些文章。 

##  多显示器

HIDPI 将会对整个桌面生效，所以如果你同时使用普通显示器，那么在普通显示器上显示元素会变得很大。但是 [Wayland](<../zh-cn/Wayland.html> "Wayland") 已经支持为每个显示器设置单独的缩放。 

###  侧边显示器

[![](../File:Tango-view-refresh-red.png)](<../File:Tango-view-refresh-red.png>)**本文或本节内容已经过时。**

**原因：** The bug with the mouse unable to reach the whole screen should be [fixed in xorg 1.20](<https://bugs.freedesktop.org/show_bug.cgi?id=39949#c80>). (在[Talk:HiDPI](<../zh-cn/Talk:HiDPI.html>)讨论)

有一个解决方案是使用 [xrandr](<../zh-cn/Xrandr.html> "Xrandr") 提供的缩放选项。比如你希望把一个非 HIDPI 的显示器（假设连接在 DP1）放置在内部 HIDPI 显示器（假设连接在 eDP 1）的右侧，你可以运行如下命令： 
    
    xrandr --output eDP-1 --auto --output DP-1 --auto --scale 2x2 --right-of eDP-1
    
当外部的显示器拓展到内部显示器上方的时候，你可能会看到外部显示器显示了一些内部显示器的内容，这种情况下你可以手动指定显示器的位置或者[使用这个脚本](<https://gist.github.com/wvengen/178642bbc8236c1bdb67>). 

你可能会遇到鼠标没办法移动到整个屏幕范围的问题，这是一个[已知的问题](<https://bugs.freedesktop.org/show_bug.cgi?id=39949>)，你可以通过应用 `xserver-org` 的补丁来解决（或者尝试使用平移选项 `panning`，但这可能会引发其他问题）。 

这是一个 4K 笔记本电脑外接 1920x1080 显示器在右侧时使用平移语法的示例： 
    
    xrandr --output eDP-1 --auto --output HDMI-1 --auto --panning 3840x2160+3840+0 --scale 2x2 --right-of eDP-1
    
通常来说，如果你的HIDPI显示器分辨率为 AxB 像素，普通显示器分辨率为 CxD，并且你将其缩放比例设置为 ExF，那么将普通显示器放置在HIDPIP显示器右侧的命令行格式如下： 
    
    xrandr --output eDP-1 --auto --output HDMI-1 --auto --panning [C*E]x[D*F]+[A]+0 --scale [E]x[F] --right-of eDP-1
    
如果平移（panning）没有办法解决的话，那么手动设置显示器位置并调整主要显示屏幕可能是更好的选择。 

以下是一个示例语法：一台分辨率为 2560x1440、DPI 为 210 的 WQHD 笔记本内置显示器（`eDP1`），使用原生分辨率放置在一台分辨率为 1920x1080、DPI 为 96 的 FHD 外接显示器（`HDMI`）下方，并将外接显示器缩放以匹配全局 DPI 设置。 
    
    xrandr --output eDP-1 --auto --pos 0x1458 --output HDMI-1 --scale 1.35x1.35 --auto --pos 0x0 --fb 2592x2898
    
总屏幕大小（`--fb`）和位置（`--pos`）需要根据缩放倍数进行计算。 

在本例中： 

  * 笔记本显示器（`eDP1`）没有缩放，使用原生分辨率，因此其尺寸为 2560x1440。
  * 外接显示器（`HDMI`）被缩放，需要将其视为更大的屏幕，其逻辑尺寸为 `(1920*1.35)x(1080*1.35)`。 
    * `eDP1` 的 Y 轴位置为 `1080*1.35=1458`。
    * 总屏幕大小： 
      * X 方向：取 `eDP1` 和 `HDMI` 中较大的宽度，即 `1920*1.35=2592`。
      * Y 方向：两者高度之和，即 `1440 + (1080*1.35)=2898`。

通用命令： 

假设： 

  * 高分辨率显示器（HiDPI）分辨率为 AxB 像素。
  * 普通显示器分辨率为 CxD 像素。
  * 普通显示器的缩放比例为 ExF。
  * 高分辨率显示器放置在普通显示器下方。

命令如下： 
    
    xrandr --output eDP-1 --auto --pos 0x(DxF) --output HDMI-1 --auto --scale [E]x[F] --pos 0x0 --fb [greater between A and (C*E)]x[B+(D*F)]
    
You may adjust the "sharpness" parameter on your monitor settings to adjust the blur level introduced with scaling. 

**注意：** Above solution with `--scale 2x2` does not work on some Nvidia cards. No solution is currently available. [[6]](<https://bbs.archlinux.org/viewtopic.php?pid=1670840>) A potential workaround exists with configuring `ForceFullCompositionPipeline=On` on the `CurrentMetaMode` via `nvidia-settings`. For more info see [[7]](<https://askubuntu.com/a/979551>).

###  多外部监视器

如果你有多于个低于内置的 HiDPI 显示器 DPI 的显示器，那么可能会碰到一些问题。这种情况下您可以想要缩小 HiDPI 显示器的内容，例如： 
    
    xrandr --output eDP1 --scale 0.5x0.5 --output DP2 --right-of eDP1 --output HDMI1 --right-of DP2
    
另外，当您缩小内置 HIDPI 显示器中的内容时，内置显示器的字体可能会变得有些模糊。但这与扩大外置显示器内容时带来的模糊并不相同。您可以对比之后选择自己想要的方案。 

###  镜像

如果你只想使用镜像的话，可以按照如下操作： 

A×B是你 HiDPI 显示器的原生分辨率，CxD 是你的另一个显示器的原生分辨率。 
    
    xrandr --output HDMI --scale [A/C]x[B/D]
    
一个 QHD 的例子(3200/1920 = 1.66 and 1800/1200 = 1.5)： 
    
    xrandr --output HDMI --scale 1.66x1.5
    
UHD和1080p的例子 (3840/1920=2 2160/1080=2)： 
    
    xrandr --output HDMI --scale 2x2
    
您可以调整显示器上的清晰度选项以减少模糊感。 

##  Linux 控制台

默认的 [Linux 控制台](<https://en.wikipedia.org/wiki/Linux_console> "w:Linux console")在 HiDPI 显示器上太小了。[kbd](<https://archlinux.org/packages/?name=kbd>)包中最大的字体是`latarcyrheb-sun32`，其他软件包中包含一些更大的字体，例如[terminus-font](<https://archlinux.org/packages/?name=terminus-font>)包中的`ter-132n`和`ter-132b`（粗体）。参阅[Linux console#Fonts](<../zh-cn/Linux_console.html#Fonts> "Linux console")获取配置详情。 

在改变字体之后，当您切换到其他控制台时，屏幕上的内容可能无法读取。要修复这一问题，你可以设置[force specific mode](<../zh-cn/Kernel_mode_setting.html#Forcing_modes_and_EDID> "Kernel mode setting")，例如`video=2560x1600@60`（设为您显示器的原生分辨率）并重新启动。 

##  另请参阅

  * [Ultra HD 4K Linux Graphics Card Testing](<https://www.phoronix.com/scan.php?page=article&item=linux_uhd4k_gpus>) (Nov 2013)
  * [Understanding pixel density](<https://www.eizo.com/library/basics/pixel_density_4k/>)
