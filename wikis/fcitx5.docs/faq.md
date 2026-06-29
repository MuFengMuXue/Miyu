# Faq

When you want to complain about input method cannot work correctly, please read this first.

Since 4.2.7, fcitx provides a command called fcitx-diagnose, it will try to detect some common problem and give some advice.

[Hall of Shame for Linux IME Support](Special:MyLanguage/Hall_of_Shame_for_Linux_IME_Support "wikilink")

## When use Ctrl + Space, Fcitx cannot be triggered on

Check the application you want to type into.

### Wayland

See [Using Fcitx 5 on Wayland](Special:MyLanguage/Using_Fcitx_5_on_Wayland "wikilink").

### Only one specific app has problem?

- The most possible reason for this is Ctrl+Space occupied by some hotkey, please change to another trigger key and try again. This usually happens in some editor, since many ide use Ctrl+Space as default key binding for Completion.

### All Gtk Apps have problem?

- Please open a traditional Gtk App (traditional Gtk App means, it cannot be Firefox, Libreoffice, which only use Gtk as a UI style). Gedit is a good choice. Right click at the input box, there will be a menu named "Input Method", please make sure there is "Fcitx" in it and being choosed.


- If there is "Fcitx", but it still not works. Please try to restart Fcitx, if it will works at this time, please check your DBus settings, or make Fcitx start later. You can read [Configure (Other)](Special:MyLanguage/Configure_(Other) "wikilink") if you're using a custom startup script.


- If there is Fcitx but not being choosed by default, and please select it and you can immediately try again in this app. If not works, please read the entry above. For permanent fix (To use Fcitx by default), please read Configure part in [Install And Configure](Special:MyLanguage/Install_And_Configure "wikilink").


- If there is no Fcitx, you should check your install first. Usually, the package name contains fcitx and gtk. If you [compile fcitx from source](Special:MyLanguage/Compile_from_source "wikilink"), please make sure you have enable GTK{2,3}\_IM_MODULE option. If you're sure about this, please read [Input method related environment variables](Special:MyLanguage/Input_method_related_environment_variables "wikilink") for how to update some cached file for gtk.


- If you are using Ubuntu and upgrade to 12.04 recently, or something werid happens to your system (Due to packager careless, or buggy package manager which can not do upgrade in correct order, for example, [pacman](https://bugs.archlinux.org/task/32764)), you might notice that gtk.immodules related files doesn't generate correctly during upgrade. Try uninstall , or coressponding package on your system and re-install them to trigger the file generate. Then recheck the input method menu to see whether it have "Fcitx" in the menu or not.

### All Qt Apps have problem?

- Run qtconfig (might have different name on your distribution, it might be qtconfig-qt4), and go to the third tab, make sure fcitx is in the "Default Input Method" combo-box. If not, please check your install.
- Above solution can also applies if you want use XIM, but still we highly recommend you to use im module. See Also [Input method related environment variables](Special:MyLanguage/Input_method_related_environment_variables "wikilink").

#### Telegram desktop

Some distribution enables Qt6 for telegram desktop. Just make sure you have the Qt6 im module (For fcitx4, it's fcitx-qt6 on archlinux).

### Chromium or any other chromium based browser (E.g. Microsoft Edge)

For Chromium running under X11, if you are using startx to start your graphical user interface, you may hit [an issue](https://gitlab.freedesktop.org/xorg/app/xinit/-/issues/9) in startx that unset the DBUS_SESSION_BUS_ADDRESS, which prevent chromium based browser from using dbus correctly. To mitigate this, you may:

1\. either export DBUS_SESSION_BUS_ADDRESS by yourself in your \$HOME/.xinitrc (or simply change to use \$HOME/.xsession if you are using debian based system).

2\. or use a display manager like sddm, gdm, lightdm instead of startx.

For Chromium that runs natively under wayland, the only native wayland input method protocol it supports is text-input-v1, which is only supported by weston. Alternatively, it can also use Gtk4's im module, you can use following flag (---enable-features=UseOzonePlatform --ozone-platform=wayland --gtk-version=4) to make it use Gtk im module, but it doesn't fully work in terms of popup window position unless you are using kimpanel + GNOME.

### Is it Java, Xterm, wine, or some other non-Gtk/Qt Application?

There are also some very rare case, that you're using a embedded linux or mini-linux distro, in which you must use XIM, the X server might missing some locale file. The file is usually needed to be under /usr/share/X11/locale/.

And When you must use XIM, please make sure, your locale **must NOT** be C or POSIX and need to be a valid locale (no matter which language), and need to be generated if you are using glibc (locale-gen). When you are using im module, there is no such limitation.

### Is it a Qt application that bundles its own Qt library?

Bundled Qt library usually uses theirs own plugin directory, which is different from system's Qt. And commonly, they are also using Qt different on system Qt, which will also make it incompatible if you simply copy the system fcitx-qt files. But anyway, you can start to check whether it loads your copied files with following environment variable. Depending on how the XIM application is written, it may need to find specific font to make it work. On Archlinux xorg-mkfontscale is required to generate correct font dir files. After install it, you'll need to restart X Server to make it work.

QT_DEBUG_PLUGINS=1 QT_LOGGING_RULES="\*.debug=true"

And try to resolve all incompatible errors. Usually, ubuntu's fcitx-frontend-qt5 and libfcitxqt5-1 are good source for fcitx-qt5 build against specific qt version. For example, DraftSight 2017S0 [1](https://groups.google.com/forum/#!topic/fcitx/9e4TI39_4sk) may work with xenial's fcitx-qt5.

### Emacs

Try

LC_CTYPE=zh_CN.UTF-8 emacs

Don't forget to check your locale -a contains that. See also [Input method related environment variables](Special:MyLanguage/Input_method_related_environment_variables "wikilink").

Emacs will use \`-\*-\*-\*-r-normal--<some font size>-\*-\*-\*-\*-\*-\*-\*' as basefont(in src/xfns.c), if you do not have one matched, the code for input method won't run. Install some font package may help (For required fonts xorg-fonts-misc might be the right package but you can also try other xorg-fonts-\* package.).

### Non Gtk/Qt Wayland Application (Alacritty, kitty, etc)

It is possible that the application you use does not support input method at all, because they need to have relevant code to implement it. Even if they do, it is highly possible that compositor does not have the support for input method. Only GNOME Shell and KWin has full text-input-v3 support. As of 2022/05/07, sway still does not have full zwp_input_method_v2 support to support input surface. For KWin, you will need Plasma 5.24+ and Fcitx 5.0.14+ and make KWin to start Fcitx 5. You will need to go to Virtual Keyboard KCM and select Fcitx 5 in the KCM.

## Candidate window is blinking under wayland with Fcitx 5

This is mainly due to the whole poor state of wayland input method. The existing wayland input method protocol is not widely supported by compositor. Even though fcitx 5 support those protocols, the poor support in application and compositor make them not usable. Not to mention certain design flaw within the protocol.

In order to make input method some what usable with **CURRENTLY** available and widely adopted techniques, Fcitx 5 implements a mechanism called "Client Side Input Panel", which basically asks client application to render the input window. This is done through dbus and IM Module for Gtk/Qt. The implementation requires using a underlying wayland protocol xdg_popup to show the window. Unfortunately, only new version of xdg_popup protocol supports **moving** a visible popup window, and this part is **NOT** implemented in Gtk3 and Qt5. What makes it even worse is that Gtk3 and Qt5 both comes to their end of life, which means it is not possible to get this new protocol support in Gtk3/Qt5. The issue is that input method requires to display a window that resizes and moves extremely frequently. To mitigate this issue, Fcitx 5 IM Module implement a hack that when we need to move the window, it will hide the window first and then show the window. Unfortunately, this would cause certain-level of blinking. It might looks bad in certain hardware and compositor combination.

Here is some possible workaround for this.

1\. Use kimpanel under GNOME shell, which will make the candidate window to be rendered with a totally different mechanism, which won't cause any blinking.

2\. Disable Fade-in and Fade-Out effect under KWin. KWin seems to tolerate such blink much better than certain compositor.

## Problem in Firefox and Google Docs

You might want to toggle preedit off temporarily, which is Ctrl+Alt+P.

## Cannot use Fcitx in flash

Please read [Hall of Shame for Linux IME Support](Special:MyLanguage/Hall_of_Shame_for_Linux_IME_Support "wikilink"), and use im module.

## Cannot type English after updating to fcitx newer than 4.2.4

Make sure you have add "[Keyboard](Special:myLanguage/Keyboard "wikilink")" to the input method list. You can use [Configuration tool](Special:myLanguage/Integrate_with_Desktop#Configuration_tool "wikilink").

And you may want to move "Keyboard" to the first one.

## Unexpected keyboard layout change

Use [Configuration tool](Special:myLanguage/Integrate_with_Desktop#Configuration_tool "wikilink"), to bind specific keyboard layout to the specific input method.

## xmodmap settings being overwritten

Fcitx now control keyboard layout and when switch layout, xmodmap setting will be overwritten. So fcitx-xkb provides an option to specify the xmodmap script and let fcitx loads it for you whenever keyboard layout changes. Or disable fcitx-xkb addon is also a solution for you, or if your requirement is simply, for example, switching Caps Lock and Esc, which is provided by xkb option, you can just set it with your desktop keyboard configuration tool (Gnome and KDE all support such configuration).

For more detailed explanation, xmodmap is a very low level tool, that doesn't aware keyboard layout. For X11, keyboard layout is built on a set of profile, when such profile is loaded, anything you changed with xmodmap will be overwritten, this isn't specific to fcitx, but all tool that support keyboard layout configuration. Xkb option is a set of profile that can do some pre-defined change over keyboard layout, including many thing that people usually do with xmodmap, for example, defining where dead key is, switching Caps Lock and Esc, and so on. Unless you have special requirements, xkb layout and xkb option is recommended.

Since 4.2.7, Fcitx will try to load \$HOME/.Xmodmap if it exists.

## Configure user interface, font, vertical list

Use [Configuration tool](Special:myLanguage/Integrate_with_Desktop#Configuration_tool "wikilink"), Addon Configuration -\> Classic UI.

If you are using [fcitx-configtool](Special:myLanguage/Configtool "wikilink") newer than 0.4.5 or [kcm-fcitx](Special:myLanguage/Kcm "wikilink") newer 0.4.1, you can directly configure those from the first level tab.

## Possible issue for GNOME 3.6

[Note for GNOME Later than 3.6](Note_for_GNOME_Later_than_3.6 "wikilink")

## [Classic UI](Special:MyLanguage/ClassicUI "wikilink") is not transparent

- This problem might NOT exist any more since 4.2.6 with a different approach for detect composite manager.
- Restart Fcitx first, if it's ok then, it might be a bug in your Window manager. Gnome-Shell, xcompmgr is known to have this bug. You can try to set the delay start to walkaround this problem.
- If restart Fcitx doesn't solve this problem, you should check whether your window manager supports composite or it's enabled or not.

### Kwin

Enable desktop effects.

### Metacity before GNOME3

gconftool-2 -s --type bool /apps/metacity/general/compositing_manager true

### Xfce

Xfwm support composite, but need to be enabled by hand.

### Compiz

0.9 series compiz can disable composite. You can use ccsm to configure it.

### Other window manager

You can use xcompmgr, cairo-compmgr as composite manager for them.

## Minecraft

Original Minecraft under linux doesn't support input method, what make it worse is, XIM will conflict with its key event processing, one way to work around is, set a wrong environment variable on purpose for minecraft, then start up it. You can use following script to do that

    #!/bin/sh
    # set a wrong one
    export XMODIFIERS="@im=null"
    # start minecraft, this might change depends on you're mod, but simply its what you ARE using to start minecraft.
    java -Xmx1024M -Xms512M -cp minecraft.jar net.minecraft.LauncherFrame

This way can be also used, if you don't want fcitx to work on some application which is using XIM.

There is a mod can be used to support input under Linux, called [NihongoMOD](http://forum.minecraftuser.jp/viewtopic.php?t=6279), 1.2.2 with minecraft 1.5.2 can work with Fcitx without upper hack.

## Root application under normal user X

Root application under X normal user session is always broken (in general, not specific to fcitx), due to the fact that dbus is a user session only process. The only way to type in root application with normal fcitx is to use XIM, set GTK_IM_MODULE=xim and QT_IM_MODULE=xim before you start your application.

## Cursor Following problem

There is a common misunderstanding that it's input method's fault that input window could not follow the cursor, which is simply wrong. This is how cursor following works: Application send the position to Input method, then input method move the input window. So if application do not send the position, the position would be wrong. This behavior is controlled by application, but not input method. So if you meet any problem, please ask application to fix it, don't ask input method to do anything. Actually, input method could do nothing with this.

Although there is some walkaround for specific problem, bug is still in application, not in input method.

- Opera, enable on the spot for [XIM](Special:MyLanguage/XIM "wikilink").
- Firefox, enable preedit.
- Java program that uses swing or awt. There is a historical OpenJDK bug. But jetbrains patches there own JDK with the fix. <https://youtrack.jetbrains.com/issue/JBR-2460/Wrong-position-of-input-window-and-no-input-preview-with-fcitx-and-ubuntu-13.04> You may want to try jetbrains jdk instead. Confirmed that 21.0.5b631.19 can work properly.

## Colored Emoji

The issue itself is usually not relevant to Fcitx itself, but the library used to render text. When using X11, or using native wayland input method protocol, the text is rendered by pango, which is the same as Gtk. You can also check if Gtk application is fine with such emoji character. A common issue is that, the embedded bitmap font is disabled by fontconfig, which is required to display color emoji.

As for Wayland that uses "Client side input panel" feature, the text is rendered natively by the toolkit. If it is a Qt application, which you may hit some Qt bugs: <https://bugreports.qt.io/browse/QTBUG-80434> , <https://bugreports.qt.io/browse/QTBUG-85744> , which does not have a resolution yet.

[Category:How-to](Category:How-to "wikilink")
