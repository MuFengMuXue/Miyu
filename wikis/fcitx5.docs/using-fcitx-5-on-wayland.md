# Using Fcitx 5 On Wayland

[Wayland](https://wayland.freedesktop.org/) is the next generation of display server protocol. While the initial release of the protocol is in 2008, the support of input method is not really ideal.

Also, using input method on Wayland-based compositor may require different setup to make it work, and certain features of fcitx that works under X11 are not yet supported by Wayland.

This page will try to cover all the current information with some underlying details, and [Setup Fcitx 5](Special:MyLanguage/Setup_Fcitx_5 "wikilink") is still generally useful.

## Applications

### TL;DR Do we still need XMODIFIERS, GTK_IM_MODULE and QT_IM_MODULE?

#### XMODIFIERS

For XMODIFIERS, yes, we do. X11 application running under X11 and XWayland has nearly no difference.

#### GTK_IM_MODULE

In an ideal setup, you should use fcitx im module Gtk application running under X11, and Gtk's text-input-v3 for wayland. The way of doing this is:

1\. Do NOT set GTK_IM_MODULE environment variable.

2\. For Gtk2, Add following content to \$HOME/.gtkrc-2.0

gtk-im-module="fcitx" 3. For Gtk 3, add following content to \$HOME/.config/gtk-3.0/settings.ini

\[Settings\] gtk-im-module=fcitx

4\. For Gtk 4, add following content to \$HOME/.config/gtk-4.0/settings.ini

\[Settings\] gtk-im-module=fcitx

5\. If you are using GNOME 3+, also run following command.

gsettings set org.gnome.settings-daemon.plugins.xsettings overrides "{'Gtk/IMModule':\<'fcitx'\>}"

For GTK_IM_MODULE, as for now, the modern Gtk 3/4 application should be able to use text-input-v3 which is supported almost by every compositor, except weston. There are a few different options in terms of setting the value of GTK_IM_MODULE. When it is unset, the Gtk built-in Wayland im module will be used for Gtk3 and Gtk4. While you can also enforce it by doing GTK_IM_MODULE=wayland, remember it will be also picked up by Gtk2. Setting GTK_IM_MODULE=fcitx can still work, and it is necessary if your compositor does not support Wayland input method frontend.

It is possible to force a certain im module with Gtk configuration file, so without GTK_IM_MODULE set, it will still be able to use different im module.

Per Gtk implementation (still valid for 3.24.41), the order of preferences is:

- X11
  - GTK_IM_MODULE in the environment
  - Value of Gtk/IMModule from XSettings
  - Value from configuration file
  - A locale based automatic selection
- Wayland
  - GTK_IM_MODULE in the environment
  - "wayland"

#### QT_IM_MODULE

For QT_IM_MODULE, as for now QT \< 6.7 can only use its own text-input-v{2,4}, which is only supported by KWin. Which means, under KDE you should unset it, but under other desktop, you will need to set it to QT_IM_MODULE=fcitx. Also the proprietary Qt applications in the wild complicates the situation. Some do not work on Wayland, some do not bundle/provide Qt wayland. Most of them do not bundle fcitx im module because fcitx is only a third party application to Qt, but I also noticed some do bundle but not bundle all the required libraries. While fcitx 5 support ibus protocol, some of those applications do not even bundle ibus im module. There are a few different environment variables you can try for those proprietary Qt applications (WPS, Anki, DaVinci Resolve, Mathematica, etc...).

QT_IM_MODULE=fcitx \# For those who bundle qt im module, e.g. WPS, Anki, you should find a .so file with fcitx in the file name QT_IM_MODULE=ibus \# For those who bundle ibus im module shipped with Qt, you should find libibusplatforminputcontextplugin.so in the package. QT_QPA_PLATFORM=xcb QT_IM_MODULE=ibus \# Enforce it to run on X11/XWayland and use ibus im module

In Qt 6.7, there is a new environment variable called "QT_IM_MODULES", which allows you so specify a fallback order on im modules. You can set it to

QT_IM_MODULES="wayland;fcitx;ibus"

So it will be able pick up the most usable one even for application that bundles no fcitx/wayland. Remember, you may still need to set( or unset) QT_IM_MODULE (not "QT_IM_MODULES") in order to handle Qt 4/5 applications.

Qt 6.7 also brings text-input-v3 support, and there are some important fixes for text-input-v3 in the Qt 6.8 series ([related bugs](https://bugreports.qt.io/issues/?jql=text%20~%20%22text%20input%20v3%22)). If you are using a compositor that only supports text-input-v3, it should be OK to use text-input-v3 with Qt 6.8.2 or later.

### Legacy X11 application that runs under XWayland

In a word, XWayland support for input method is as good as normal X11 display server. As long as you set the same environment variable, using Xwayland should not be a issue. This category includes:

- Xlib-based (and also other toolkit based on Xlib, e.g. tk, SDL1, etc), e.g. xterm, rxvt. Make sure XMODIFIERS is set correctly.
- Gtk2-based applications, similar to Xlib, but can use fcitx im module. Set GTK_IM_MODULE to fcitx will give it best experience.
- SDL2-based applications that doesn't default to wayland. Set SDL_IM_MODULE to fcitx
- electron, chromium, these are still default to X11, similar to Gtk2 case.
- For Qt4 applcation, Qt 4 can only use X11. You will need to QT_IM_MODULE to fcitx. Same for Qt5+ that uses XCB (can be override with QT_QPA_PLATFORM=xcb).

### Gtk3 / Gtk4

Gtk3 and Gtk4 support text-input-v3 natively. At the same time, it's also possible to use fcitx im module under wayland. So, either GTK_IM_MODULE=wayland or GTK_IM_MODULE=fcitx works. There are some difference to it. text-input-v3

### Qt5 / Qt6

See [\#QT_IM_MODULE](#QT_IM_MODULE "wikilink").

If your Qt application natively runs under Wayland, you can either unset QT_IM_MODULE to make it use text-input-v2, or set QT_IM_MODULE=fcitx to make it use fcitx im module.

text-input-v2 is not upstreamed to wayland-protocols, that is probably why only kwin support it. This means in non-kwin environment, you will need to use QT_IM_MODULE=fcitx to make the Qt applications work.

On Qt6, you may also use QT_IM_MODULE= (empty) or QT_IM_MODULE=wayland if your Qt vesion contains this <https://codereview.qt-project.org/c/qt/qtwayland/+/416862>.

### Native wayland application (winit)

Most likely text-input-v3 is being used.

### Chromium / Electron

TL;DR version, if you use XWayland to run Chromium or Electron application, just install Gtk im module and GTK_IM_MODULE=fcitx the same way like X11.

If you choose to run it natively under Wayland, for chromium you will need to use

1.  If your compositor supports text-input-v1 protocol. Check the compositor section below.

`chromium --enable-features=UseOzonePlatform --ozone-platform=wayland --enable-wayland-ime`

1.  If your compositor & chromium supports text-input-v3 protocol, you may also use

`chromium --enable-features=UseOzonePlatform --ozone-platform=wayland --enable-wayland-ime --wayland-text-input-version=3`

1.  However, due to a different understanding in text-input-v3 protocol, it has some issue when using with KWin.

`# Prefer text-input-v1 if you're using kwin.`
`chromium --enable-features=UseOzonePlatform --ozone-platform=wayland --enable-wayland-ime --wayland-text-input-version=1`

Or

1.  You will get wrong position for the input method popup window, unless you use GNOME shell + kimpanel extension.

`chromium --enable-features=UseOzonePlatform --ozone-platform=wayland --gtk-version=4`

For electron, only the first option is avaiable (electron does NOT support to run internal chromium with gtk4), e.g. for vscode

1.  If your compositor supports text-input-v1 protocol. Check the compositor section below.

`code --enable-features=UseOzonePlatform --ozone-platform=wayland --enable-wayland-ime`

By default it should run under Xwayland (As of 2023/02/25 on Archlinux/Chromium 110.0.5481.177), but some user also reports it is using wayland even the "Preferred Ozone Platform" is "Default". So to check whether it's really run with wayland, you can use xeyes or xwininfo. With xeyes, if it's an X11 window, the "eyes" will move with mouse, otherwise it's wayland. With xwininfo, if the mouse cursor changed to "+" shape, and click the window shows the window information, then it is a X11 window.

You may force it to run with Wayland, or X11 with the flag `--ozone-platform=wayland` and `--ozone-platform=x11`. You may persistent this by changing the option "Preferred Ozone Platform" in <chrome://flags>. It has four values, "Default", "X11", "Wayland", "Auto".

It's possible to make it use GTK_IM_MODULE if it runs with Gtk4 (only supported by chromium/chrome at this time, not electron) by passing `--gtk-version=4`.

It's also possible to make it use text-input-v1 by passing `--enable-wayland-ime` in addition to the flag above.

The Chromium support for text-input-v1 is not very stable and you may hit some random crash. E.g. in the past, version 112 has a crash bug: <https://bugs.chromium.org/p/chromium/issues/detail?id=1431532> , which is fixed in version 115. In the bug comment, Chromium developer claims this text-input-v1 is only supposed to be used internally and not well supported, so use this at your own risk though it's currently the only out of box option.

You should only use one of `--enable-wayland-ime` or `--gtk-version=4`, depending on you want to use text-input-v1, or gtk4 im module. text-input-v1 works for kwin 5.27 and weston. Gtk4 im module works on all environment, but only GNOME with Kimpanel extension can display the popup window in the correct position.

## Support in Wayland Compositor

Even if you are using only native wayland applications, Xwayland is recommended to be enabled for following reason. If client side input panel in im module does not work, fcitx will fallback to a X11 window, instead of a wayland window. The reason for this is because wayland window can not be placed freely on the screen. On the contrary, even if im module can only pass a coordinate relative to the application window to fcitx, which make the coordinate position doesn't make much sense, if your application window size is "maximized", the coordinate may just be "right" if treated as the global coordinate. This makes X11 window a better option than a randomly placed wayland window.

### KDE Plasma

Best setup:

- KDE Plasma 5.27 or later
- Environment variables:
  - Set `XMODIFIERS=@im=fcitx` for XWayland application
  - Start fcitx5 by go to "System settings" -\> "Virtual keyboard" -\> Select Fcitx 5
  - Do not set `GTK_IM_MODULE` & `QT_IM_MODULE` & `SDL_IM_MODULE` . You could unset `GTK_IM_MODULE` & `QT_IM_MODULE` by runing `im-config` and then selecting `do not set any IM from im-config and use desktop default"`
  - Run chromium/electron application with `--enable-features=UseOzonePlatform --ozone-platform=wayland --enable-wayland-ime`
- Caveats:
  - Certain Gtk/Qt application that only works under X11 may still need to set `GTK_IM_MODULE` or `QT_IM_MODULE` for them individually.
  - If you set `GTK_IM_MODULE/QT_IM_MODULE` globally, you will hit this issue [Candidate window is blinking under wayland with Fcitx 5](Special:MyLanguage/FAQ#Candidate_window_is_blinking_under_wayland_with_Fcitx_5 "wikilink")

Support Information:

- App/Compositor supports text-input-v2 and text-input-v3.
- Comopositor/Application uses zwp_input_method_v1.
- 5.27 additionally supports text-input-v1.
- 5.24 usable zwp_input_method_v1 with fcitx5. Pre-5.24 there are lots of problems, always use fcitx im module instead.
- Use "Virtual keyboard" KCM to launch fcitx5. This is required to use text-input protocol. If you launch fcitx this way, make sure you do not use "restart" in the tray menu, since the socket passed from KWin can not be reused with the newly restarted fcitx.

### GNOME

Best setup:

- Environment variables:
  - Set `XMODIFIERS=@im=fcitx` for XWayland application
  - Set `QT_IM_MODULE=fcitx` for Qt, since Qt5 would use XWayland by default.
  - If you don't use Qt \>=6.7,\<6.8.2, set `QT_IM_MODULES="wayland;fcitx"` for Qt 6.8.2+
  - Run chrome with XWayland and `GTK_IM_MODULE=fcitx`

Support information:

- Application/Compositor uses text-input-v3
- Compositor/Input Method uses ibus dbus protocol, so ibus frontend is required to be used.
- Adding Fcitx 5 to autostart, it will replace any existing ibus-daemon upon start up so it will work out of box.
- Popup candidate window is not able to be displayed over gnome-shell UI. Only solution is to use [Kimpanel](Special:MyLanguage/Kimpanel "wikilink"), [link to extension](https://extensions.gnome.org/extension/261/kimpanel/).
- Qt \< 6.8.2 need to use QT_IM_MODULE=fcitx since mutter doesn't support text-input-v2.

### Sway

Best setup:

- sway 1.10 or later
- Environment variables:
  - Set `XMODIFIERS=@im=fcitx` for XWayland application
  - Set `QT_IM_MODULE=fcitx` for Qt5
  - If you don't use Qt \>=6.7,\<6.8.2, set `QT_IM_MODULES="wayland;fcitx"` for Qt 6.8.2+

Support Information:

- Application/Compositor uses text-input-v3
- Comopositor/Application uses zwp_input_method_v2. You will need sway 1.10+ (which includes [this pull request](https://github.com/swaywm/sway/pull/7226)) to make it show the popup candidate window for text-input-v3 client.
- fcitx im module also works.
- Qt \< 6.8.2 need to use QT_IM_MODULE=fcitx since sway doesn't suppport text-input-v2.

### Weston

- Application/Compositor uses text-input-v1
- Comopositor/Application uses zwp_input_method_v1.
- Since it has no text-input-v3, which is more commonly used, im module is the only solution for Gtk/Qt, need to set GTK_IM_MODULE=fcitx and QT_IM_MODULE=fcitx.
- Add following content to \$HOME/.config/weston.ini to make it launch fcitx 5. (xwayland part is recommended to make fcitx work best, even if it's wayland)


    [core]
    xwayland=true


    [input-method]
    path=/usr/bin/fcitx5

### Other compositors

Please check their upstream for more information. For wlroots based compositors, it is possible that they also support in the same way as Sway does, or zwp_input_method could also be unsupported.

## Known Issues

### Fcitx managed XKB layout

Unlike X11, there is no generic way to set XKB layout to compositor, which means it can only be implemented for every individual desktop. Right now, Fcitx managed layout only works for KDE Plasma and GNOME.

As for other desktop, in order to make this "semi" work you'll need to ensure following:

- The XKB layout of the input method group should be the same as the actual xkb layout you configured for the compositor. Fcitx will "think" the layout is the same and bypass the key conversion logic.
- If you need other layout for text typing (e.g. Arabic), just add them to the Fcitx. As long as the key is forwarded to fcitx, it should work.

### Popup candidate window

Wayland does not have a global coordinate system for regular client, so for native wayland client, it is impossible for Fcitx to place a wayland surface at a certain position. In order for popup window to be placed at the correct position, there are following cases:

- Xwayland have no problem and it should work as good as X11.
- If zwp_input_method protocol can be used, it has a surface role to allow compositor to place the popup window for input method. This only works if client uses text-input protocol.
- For GNOME, kimpanel extension can read window coordinate since it's running inside compositor. As long as im module can report relative coordinate, kimpanel extension can display the popup window at the correct position. As similar approach for Plasma kimpanel is planned, but not yet implemented.
- For Gtk/Qt, fcitx's im module implement a way to render the popup with in the client process. This has some limitation because implemenation of xdg_popup in Gtk3/Qt5 doesn't support reposition the window. So show/hide trick is used to mitigate this, but it may cause window blinking. Fcitx tries not to move window if possible. You may also disable popup animation if you're using KWin to help reduce the blinking.

### Per-window input method state

When zwp_input_method is used, essentially there is only one input context visible to fcitx, and fcitx cannot distinguish what application is being used. Which means the input method "active"/"inactivate" state is now "global".

Now fcitx supports two protocol to figure out the focused window and the corresponding application name, including wlr-foreign-toplevel-management (used by wlroots based compositor) and plasma-window-management (used by kwin).
