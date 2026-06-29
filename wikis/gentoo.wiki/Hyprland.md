**Resources**

[[]][Home](https://hyprland.org/)

[[]][GitHub](https://github.com/hyprwm/Hyprland)

[[]][Official project wiki](https://wiki.hypr.land/)

[[]][Forum](https://forum.hypr.land/)

[[]][r/hyprland](https://reddit.com/r/hyprland)

**hyprland** is an open-source [Wayland compositor](https://wiki.gentoo.org/wiki/Wayland_compositor "Wayland compositor") written in C++. The rendering backend is GLES 3.2.^[\[1\]](#cite_note-1)^

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Files]](#Files)
    -   [[2.2] [Display configuration]](#Display_configuration)
    -   [[2.3] [Sound volume]](#Sound_volume)
    -   [[2.4] [Other special hotkeys]](#Other_special_hotkeys)
        -   [[2.4.1] [Monitor and keyboard backlights]](#Monitor_and_keyboard_backlights)
        -   [[2.4.2] [Playerctl]](#Playerctl)
    -   [[2.5] [Terminal emulator]](#Terminal_emulator)
-   [[3] [Executing Hyprland]](#Executing_Hyprland)
    -   [[3.1] [On login with tty]](#On_login_with_tty)
-   [[4] [Status bars]](#Status_bars)
-   [[5] [Screenshotting]](#Screenshotting)
-   [[6] [Screen sharing]](#Screen_sharing)
    -   [[6.1] [xdg-desktop-portal-hyprland]](#xdg-desktop-portal-hyprland)
    -   [[6.2] [xdg-desktop-portal-gnome]](#xdg-desktop-portal-gnome)
-   [[7] [Flatpak portals]](#Flatpak_portals)
    -   [[7.1] [xdg-desktop-portals]](#xdg-desktop-portals)
-   [[8] [Polkit authentication]](#Polkit_authentication)
-   [[9] [Removal]](#Removal)
    -   [[9.1] [Unmerge]](#Unmerge)
-   [[10] [Troubleshooting]](#Troubleshooting)
    -   [[10.1] [No Sound on OBS]](#No_Sound_on_OBS)
    -   [[10.2] [Steam cannot re-open without a tray]](#Steam_cannot_re-open_without_a_tray)
-   [[11] [See also]](#See_also)
-   [[12] [References]](#References)

## [Installation]

### [Emerge]

With the fast pace of Hyprland releases, and the dependencies that are required, use of the [hyproverlay](https://codeberg.org/hyproverlay/hyproverlay.git) repository is recommended.

To add the `hyproverlay` overlay, run:

`root `[`#`]`emerge -va app-eselect/eselect-repository `

`root `[`#`]`eselect repository enable hyproverlay `

`root `[`#`]`emaint sync -r hyproverlay `

As third party repositories don\'t have the \"stable\" keyword, use the following to accept all packages in the overlay, to avoid having to add packages one by one:

[FILE] **`/etc/portage/package.accept_keywords/hyproverlay`Accept all testing keywords for hyproverlay**

    */*::hyproverlay

More information on this topic can be found at [/etc/portage/package.accept_keywords](https://wiki.gentoo.org/wiki//etc/portage/package.accept_keywords "/etc/portage/package.accept keywords").

`root `[`#`]`emerge --ask gui-wm/hyprland`

## [Configuration]

To view all available configuration options, run:

`user `[`$`]`man Hyprland`

or visit the Hyprland wiki link in this page\'s InfoBox.

### [Files]

Each user running Hyprland can edit the default configuration file in order to run a customized session. The default config file location is [\~/.config/hypr/hyprland.lua].

### [Display configuration]

Display options can be queried with:

`user `[`$`]`hyprctl monitors`

    Monitor eDP-1 (ID 0):
        2560x1440@165.003006 at 0x0
        description: Chimei Innolux Corporation 0x152A (eDP-1)
        make: Chimei Innolux Corporation
        model: 0x152A
        serial:
        active workspace: 1 (1)
        reserved: 0 35 0 0
        scale: 1.00
        transform: 0
        focused: yes
        dpmsStatus: 1
        vrr: 0

Monitors can be adjusted by modifying [\~/.config/hypr/hyprland.lua]. Once the file is saved, the configuration is reloaded automatically.

[FILE] **`~/.config/hypr/hyprland.lua`auto configuration of monitors**

    hl.monitor()

[FILE] **`~/.config/hypr/hyprland.lua`Configure primary display which is centered**

    hl.monitor()

[FILE] **`~/.config/hypr/hyprland.lua`Configure alternate display which is vertical**

    hl.monitor()

Refer to the \"[Monitors](https://wiki.hypr.land/Configuring/Basics/Monitors/)\" page on the Hyprland wiki for more information.

### [Sound volume]

If [PulseAudio](https://wiki.gentoo.org/wiki/Pulseaudio "Pulseaudio") is being used, the following configuration can be used for changing sound volume:

[FILE] **`~/.config/hypr/hyprland.lua`Set keyboard shortcuts to change sound volume for pulseaudio**

    hl.bind("XF86AudioRaiseVolume", hl.dsp.exec_cmd("pactl set-sink-volume @DEFAULT_SINK@ +5%"))
    hl.bind("XF86AudioLowerVolume", hl.dsp.exec_cmd("pactl set-sink-volume @DEFAULT_SINK@ -5%"))

If [PipeWire](https://wiki.gentoo.org/wiki/PipeWire "PipeWire") is being used, the following configuration can be used for changing sound volume (with [WirePlumber](https://wiki.gentoo.org/wiki/Wireplumber "Wireplumber")):

[FILE] **`~/.config/hypr/hyprland.lua`Set keyboard shortcuts to change sound volume for PipeWire**

    hl.bind("XF86AudioRaiseVolume", hl.dsp.exec_cmd("wpctl set-volume @DEFAULT_AUDIO_SINK@ 5%-"))
    hl.bind("XF86AudioLowerVolume", hl.dsp.exec_cmd("wpctl set-volume @DEFAULT_AUDIO_SINK@ 5%-"))

If [ALSA](https://wiki.gentoo.org/wiki/ALSA "ALSA") is being used, the following configuration can be used for changing sound volume:

[FILE] **`~/.config/hypr/hyprland.lua`Set keyboard shortcuts to change sound volume for ALSA**

    hl.bind("XF86AudioRaiseVolume", hl.dsp.exec_cmd("amixer -Mq set Speaker 5%+"))
    hl.bind("XF86AudioLowerVolume", hl.dsp.exec_cmd("amixer -Mq set Speaker 5%-"))

If [[[media-sound/sndio]](https://packages.gentoo.org/packages/media-sound/sndio)[]] is being used, the following configuration can be used for changing sound volume:

[FILE] **`~/.config/hypr/hyprland.lua`Set keyboard shortcuts to change sound volume for sndio**

    hl.bind("XF86AudioRaiseVolume", hl.dsp.exec_cmd("sndioctl -f snd/default output.level=+0.05"))
    hl.bind("XF86AudioLowerVolume", hl.dsp.exec_cmd("sndioctl -f snd/default output.level=-0.05"))

### [Other special hotkeys]

[FILE] **`~/.config/hypr/hyprland.lua`Set the keyboard shortcuts for muting mic and sound volume for pulseaudio**

    hl.bind("XF86AudioMute", hl.dsp.exec_cmd("pactl set-sink-mute @DEFAULT_SINK@ toggle"))
    hl.bind("XF86AudioMicMute", hl.dsp.exec_cmd("pactl set-source-mute @DEFAULT_SOURCE@ toggle"))

#### [Monitor and keyboard backlights]

The package [[[app-misc/brightnessctl::GURU]](https://repos.gentoo.org/#GURU)[]] is available in [GURU](https://wiki.gentoo.org/wiki/GURU "GURU") and can be used to adjust backlights and brightness.

`root `[`#`]`emerge --ask app-misc/brightnessctl`

Here is an example config for monitor backlight control:

[FILE] **`~/.config/hypr/hyprland.lua`Set keyboard shortcuts for screen brightness support**

    hl.bind("XF86MonBrightnessDown", hl.dsp.exec_cmd("brightnessctl set 5%-"))
    hl.bind("XF86MonBrightnessUp", hl.dsp.exec_cmd("brightnessctl set 5%+"))

Here is an example config for keyboard backlight control:

[FILE] **`~/.config/hypr/hyprland.lua`Set keyboard shortcuts for keyboard brightness support**

    hl.bind("xf86KbdBrightnessUp", hl.dsp.exec_cmd("brightnessctl -d *::kbd_backlight set +33%"))
    hl.bind("xf86KbdBrightnessDown", hl.dsp.exec_cmd("brightnessctl -d *::kbd_backlight set 33%-"))

Other tools to control brightness include [[[sys-power/acpilight]](https://packages.gentoo.org/packages/sys-power/acpilight)[]] and [[[dev-libs/light]](https://packages.gentoo.org/packages/dev-libs/light)[]].

#### [Playerctl]

[[[media-sound/playerctl]](https://packages.gentoo.org/packages/media-sound/playerctl)[]] can be used to control multimedia apps.

`root `[`#`]`emerge --ask media-sound/playerctl`

Here is an example config:

[FILE] **`~/.config/hypr/hyprland.lua`Set keyboard shortcuts for media playback**

    hl.bind("XF86AudioPlay", hl.dsp.exec_cmd("playerctl play-pause"))
    hl.bind("XF86AudioNext", hl.dsp.exec_cmd("playerctl next"))
    hl.bind("XF86AudioPrev", hl.dsp.exec_cmd("playerctl previous"))
    hl.bind("XF86audiostop", hl.dsp.exec_cmd("playerctl stop"))

### [Terminal emulator]

Terminal emulators that support Wayland can be found on the [List of software for Wayland](https://wiki.gentoo.org/wiki/List_of_software_for_Wayland "List of software for Wayland") page. Popular choices include [[[x11-terms/alacritty]](https://packages.gentoo.org/packages/x11-terms/alacritty)[]] or [[[x11-terms/kitty]](https://packages.gentoo.org/packages/x11-terms/kitty)[]], which works natively with Wayland if the `KITTY_ENABLE_WAYLAND` environment variable is set to `1`.

## [Executing Hyprland]

** Note**\
systemd automatically starts a D-Bus user session. systemd users should omit dbus-run-session

** Note**\
Starting with v0.53.0, upstream suggests launching Hyprland with the command:

`user `[`$`]`start-hyprland`

Older versions should continue starting Hyprland with:

`user `[`$`]`Hyprland`

Some [display managers](https://wiki.gentoo.org/wiki/Display_manager "Display manager") may work. Without a display manager, Hyprland can be started from a tty:

`user `[`$`]`dbus-run-session start-hyprland`

#### [On login with tty]

A simple function can be added to a user\'s shell profile file to execute a Hyprland session upon login, which will only be evaluated in login shells:

[FILE] **`~/.bash_profile`Launch Hyprland after logging into a TTY**

    dbus-run-session start-hyprland

If using [Zsh](https://wiki.gentoo.org/wiki/Zsh "Zsh"), this function can be put it in [\~/.zprofile].

## [Status bars]

Refer to the \"[List of software for Wayland](https://wiki.gentoo.org/wiki/List_of_software_for_Wayland#Status_bars "List of software for Wayland")\" page for a list of status bar options.

## [Screenshotting]

While there are a few options to screenshot in Hyprland, there is an official tool, [hyprshot].

First, unmask hyprshot:

[FILE] **`/etc/portage/package.accept_keywords/hyprshot`**

    gui-apps/hyprshot ~amd64

Then emerge:

`root `[`#`]`emerge --ask gui-apps/hyprshot`

and add the following to [hyprland.lua]:

[FILE] **`~/.config/hypr/hyprland.lua`**

    -- Screenshot a window
    hl.bind(mainMod .. " + PRINT", hl.dsp.exec_cmd("hyprshot -m window"))

    -- Screenshot a monitor
    hl.bind("PRINT", hl.dsp.exec_cmd("hyprshot -m output"))

    -- Screenshot a region
    hl.bind(mainMod .. " + SHIFT + PRINT", hl.dsp.exec_cmd("hyprshot -m region"))

## [Screen sharing]

Refer to the \"[hyprland Screen sharing](https://wiki.hyprland.org/Useful-Utilities/Screen-Sharing/)\" page on the Hyprland wiki.

** Note**\
XDPH is not necessary. Hyprland will work with XDPW, but XDPH has more features, like window sharing. XDPH will work on wlroots-based compositors, but is limited to XDPW features (others will be disabled).

### [xdg-desktop-portal-hyprland]

[xdg-desktop-portals](https://wiki.gentoo.org/wiki/Xdg-desktop-portal "Xdg-desktop-portal") are helper programs for desktop environments. They work by managing D-Bus interfaces and exposing them as \'portals\'. On Wayland they are often needed because, unlike X, Wayland does not allow windows to easily talk to each other.

If some programs start up very slowly or screen sharing does not work, a problem with the xdg-desktop-portal is likely the reason.

Hyprland works with [[[gui-libs/xdg-desktop-portal-wlr]](https://packages.gentoo.org/packages/gui-libs/xdg-desktop-portal-wlr)[]], but also lacks screen sharing. Hyprland upstream forked xdg-desktop-portal-wlr into [[[gui-libs/xdg-desktop-portal-hyprland::GURU]](https://repos.gentoo.org/#GURU)[]]:

`root `[`#`]`emerge --ask gui-libs/xdg-desktop-portal-hyprland`

xdg-desktop-portal-hyprland needs to be started after Hyprland starts. This is best done with Hyprland\'s `hl.on("hyprland.start", ...)` function. It\'s also a good idea to tell D-Bus that the current desktop is Hyprland. To do so, add this to the Hyprland config file:

[FILE] **`~/.config/hypr/hyprland.lua`XDPH environment variables**

    hl.env("XDG_CURRENT_DESKTOP", "Hyprland")
    hl.env("XDG_SESSION_TYPE", "wayland")
    hl.env("XDG_SESSION_DESKTOP", "Hyprland")

    hl.on("hyprland.start", hl.exec_cmd("dbus-update-activation-environment --systemd WAYLAND_DISPLAY XDG_CURRENT_DESKTOP"))

[OpenRC](https://wiki.gentoo.org/wiki/OpenRC "OpenRC") users should not worry too much about the `--systemd` flag here. The command will update the systemd \--user environment if possible, but will simply not do that on OpenRC.

** Note**\
systemd will automatically start xdg-desktop-portals via D-Bus. systemd users may omit this step.

If not using systemd, a script should be used to start xdg-desktop-portal-hyprland. Although the script can reside anywhere, for this example, it will be located at [\~/.config/hypr/xdg-portal-hyprland].

[FILE] **`~/.config/hypr/xdg-portal-hyprland`**

    #!/bin/bash
    sleep 1
    killall xdg-desktop-portal-hyprland
    killall xdg-desktop-portal-gnome
    killall xdg-desktop-portal-wlr
    killall xdg-desktop-portal
    logger 'killed all xdg-desktop'
    sleep 1
    /usr/libexec/xdg-desktop-portal-hyprland &
    logger 'xdg-desktop-portal-hyprland started'
    sleep 2
    /usr/libexec/xdg-desktop-portal &
    logger 'xdg-desktop-portal started'

Once that file has been created, add the following to the [hyprland.lua] file:

[FILE] **`~/.config/hypr/hyprland.lua`**

    hl.on("hyprland.start", hl.exec_cmd("~/.config/hypr/xdg-portal-hyprland"))

This will ensure that no other desktop portal is running while using Hyprland, which can cause problems.

### [xdg-desktop-portal-gnome]

** Important**\
Avoiding gnome-shell would be wiser than following the directions in this section, which are not supported by Gentoo.

Even though the other portals\' processes get killed in the script from the earlier point, xdg-desktop-portal-gnome causes problems with Hyprland. Hyprland warns about that at startup when it detects xdg-desktop-portal-gnome on the system.

When using Hyprland, xdg-desktop-portal-gnome should be uninstalled from the system:

`root `[`#`]`emerge --unmerge xdg-desktop-portal-gnome`

GNOME will still work, but it could lack some functionality (like screen sharing).

Because [[[gnome-base/gnome-shell]](https://packages.gentoo.org/packages/gnome-base/gnome-shell)[]] depends on the portal, [[[sys-apps/xdg-desktop-portal-gnome]](https://packages.gentoo.org/packages/sys-apps/xdg-desktop-portal-gnome)[]] will be pulled in with every Portage world set update.

Portage\'s [package.provided](https://wiki.gentoo.org/wiki/Package.provided "Package.provided") feature can be used to prevent pulling in xdg-desktop-portal-gnome.

## [Flatpak portals]

### [xdg-desktop-portals]

[xdg-desktop-portals](https://wiki.gentoo.org/wiki/Xdg-desktop-portal "Xdg-desktop-portal") were originally designed to provide access to system resources within Flatpak sandboxes. Recently, large compositors have influenced many software developers to adopt these portals as standard mechanisms for screenshot and screencast functionalities in Wayland.

To ensure that links within Flatpak applications can be opened, and that Flatpak applications can send notifications, it\'s not enough to simply install the [[[gui-libs/xdg-desktop-portal-hyprland]](https://packages.gentoo.org/packages/gui-libs/xdg-desktop-portal-hyprland)[]] package, a fork of [[[gui-libs/xdg-desktop-portal-wlr]](https://packages.gentoo.org/packages/gui-libs/xdg-desktop-portal-wlr)[]] claiming to support screencast and screenshot functionalities.

For more context, refer to [xdg-desktop-portal-wlr issue #42](https://github.com/emersion/xdg-desktop-portal-wlr/issues/42), which shows that the [[[sys-apps/xdg-desktop-portal-gtk]](https://packages.gentoo.org/packages/sys-apps/xdg-desktop-portal-gtk)[]] package needs to both be installed and started with Hyprland.

** Note**\
systemd will automatically start xdg-desktop-portal along with D-Bus. systemd users may omit this step.

If [\~/.config/hypr/xdg-portal-hyprland] was added, modify it as follows:

[FILE] **`~/.config/hypr/xdg-portal-hyprland`**

    #!/bin/bash
    sleep 1
    killall xdg-desktop-portal-hyprland
    killall xdg-desktop-portal-gtk
    killall xdg-desktop-portal-gnome
    killall xdg-desktop-portal-wlr
    killall xdg-desktop-portal
    logger 'killed all xdg-desktop'
    sleep 1
    /usr/libexec/xdg-desktop-portal-gtk &
    logger 'xdg-desktop-portal-gtk started'
    sleep 1
    /usr/libexec/xdg-desktop-portal-hyprland &
    logger 'xdg-desktop-portal-hyprland started'
    sleep 2
    /usr/libexec/xdg-desktop-portal &
    logger 'xdg-desktop-portal started'

## [Polkit authentication]

In order for processes/apps which do not have privilege to communicate with more privileged processes/apps, unprivileged processes will need the [[[sys-auth/polkit]](https://packages.gentoo.org/packages/sys-auth/polkit)[]] package. For example, this is the case when trying to mount filesystems and drives through the use of a graphical file manager. Along with polkit (PolicyKit), the user will need a \"polkit agent\", which is used to make the user of a session prove that they really are the user or an administrative user. The Hyprland Wiki recommends [hyprpolkitagent], which can be installed from the [GURU](https://wiki.gentoo.org/wiki/GURU "GURU") repository:

`root `[`#`]`emerge --ask sys-auth/hyprpolkitagent`

Hyprpolkitagent can be autostarted by adding the following line to hyprland.conf:

[FILE] **`~/.config/hypr/hyprland.lua`**

    hl.on("hyprland.start", hl.exec_cmd("/usr/libexec/hyprpolkitagent"))

## [Removal]

### [Unmerge]

`root `[`#`]`emerge --ask --depclean --verbose gui-wm/hyprland gui-libs/xdg-desktop-portal-hyprland`

## [Troubleshooting]

### [No Sound on OBS]

[PulseAudio](https://wiki.gentoo.org/wiki/PulseAudio "PulseAudio") may fail to autostart, and OBS will fail to connect to the PulseAudio server. Add the following in [hyprland.lua], after dbus:

[FILE] **`~/.config/hypr/hyprland.lua`**

    hl.on("config.reloaded", hl.exec_cmd("start-pulseaudio-x11"))

### [Steam cannot re-open without a tray]

Running [steam], either from terminal or an application launcher, can only be done once. After closing Steam, it will run in the background and expect a tray. It is recommended to install a system tray, such as [Waybar](https://wiki.gentoo.org/wiki/Waybar "Waybar") with the `tray` USE flag.

## [See also]

-   [Hyprpaper](https://wiki.gentoo.org/wiki/Hyprpaper "Hyprpaper") --- a blazing fast [Wayland](https://wiki.gentoo.org/wiki/Wayland "Wayland") wallpaper utility with IPC controls.
-   [List of software for Wayland](https://wiki.gentoo.org/wiki/List_of_software_for_Wayland "List of software for Wayland") --- various desktop related packages for Wayland

## [References]

1.  [[[↑](#cite_ref-1)] [[https://photon-reddit.com/r/hyprland/comments/141g6b2/what_is_the_default_render_backend_of_hyprland/](https://photon-reddit.com/r/hyprland/comments/141g6b2/what_is_the_default_render_backend_of_hyprland/)]]