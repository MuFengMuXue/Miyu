# Autostart

## Distribution specific tool

Distribution may provides some specific tool for autostart Fcitx and usually also set up environment variable together.

### im-config (Debian/Debian-based/Ubuntu)

This is a tool used by debian or debian based distribution. Just run `im-config` from command line after login to your graphics interface and it should pop up a wizard, just select fcitx5 from it.

### imsettings (Fedora)

A program that is similar to im-config, and it also provides a GUI to select the input method framework to be used. Under default installation, imsettings should be installed by default, if not, you may install that. imsettings can setup the environment variable and also launch the input method correspondingly. It also provides a graphical frontend [im-chooser](https://pkgs.org/search/?q=im-chooser) to change the configuration. What you need to do is simply execute `im-chooser`, log-out and log-in again.

[Video instruction for Fedora 36 KDE](https://www.youtube.com/watch?v=FwqTtGEN4vQ). This instruction should work for other non-GNOME XDG-compliance desktop.

### fcitx5-autostart (Fedora)

This is a [fedora package](https://pkgs.org/search/?q=fcitx5-autostart) that bundles a /etc/profile.d script for setting up environment variables and also XDG autostart file for autostart.

## XDG Autostart

Certain distribution may not provide such a file. If not, you can simply copy `/usr/share/applications/org.fcitx.Fcitx5.desktop` to `$HOME/.config/autostart`

mkdir -p \$HOME/.config/autostart && cp /usr/share/applications/org.fcitx.Fcitx5.desktop \$HOME/.config/autostart

## KWin Wayland 5.24+

You do not have to do this if you use only Gtk/Qt/Xwayland application. If you want to use wayland native applications supporting text-input-v3, you will need to let KWin start input method as a special client.

Simply open systemsettings, go to the "Virtual Keyboard" section, change the input method from "None" to "Fcitx 5".

## Non-XDG compliant Window Manager/Wayland Compoistor

In those case may not support XDG Autostart, please check your Window Manager manual about how to automatically launch a program upon start.

### Weston

Weston is a reference wayland compositor implementation, which is not a common setup for normal user.

If you want to use the westons zwp_input_method_v1 implementation, you will need to have following content in your \$HOME/.config/weston.ini (Update the path accordingly for if it is not /usr/bin/fcitx5).

\[input-method\] path=/usr/bin/fcitx5

There are certain issues if you try to use weston in a nested mode for debugging and fcitx5, if you already have a running fcitx5 in the same session.

If you just run weston under X11 for debugging purpose, easiest way is to simply quit fcitx5 before start weston.

Also be aware, there is a bug that weston does not set DISPLAY correctly input method on the first run. You may need to kill fcitx5 once to make it get the right DISPLAY or use OpenX11Connection dbus call to let fcitx to connect.

# Environment variables

Due to the transition phase in a lot of different places, there is no perfect solution that works for every one. Please choose your own solution based on your environment. Basically what you want to do is to set following environment variables for your desktop session.

``
`XMODIFIERS=@im=fcitx`
`GTK_IM_MODULE=fcitx`
`QT_IM_MODULE=fcitx`

Though it looks like valid shell script, please \*NOTE\* that the snippet above is just to demonstrate what these value gonna be. Please check the section below for concrete syntax for different methods.

## Login shell profile

If you are using Bash as your login shell, `$HOME/.bash_profile` is the best user-level thing you can rely on. It is widely supported by different DMs and will also work if you start graphics from TTY.

- Supported by mainstream Display manager, including GDM/SDDM/LightDM
- TTY login

If you are not using bash, you may want to double check if your shell profile can be used as a place to set environment variables, especially you are using some uncommon login shells.

The snippet that you need to add to `$HOME/.bash_profile` would be

``
`export XMODIFIERS=@im=fcitx`
`export GTK_IM_MODULE=fcitx`
`export QT_IM_MODULE=fcitx`

Some may argue that `$HOME/.profile` is a shell agnostic solution, which is wrong. While GDM always source this file, SDDM/Bash would not source this file if `$HOME/.bash_profile` presents. This makes `$HOME/.bash_profile` a better solution because bash is quite widely used. But check your login shell before proceeding, some distribution may not use bash as default shell.

Here is an [video](https://youtu.be/8XDmLr6wb4M) on how to manual setup environment variable on Archlinux

## /etc/profile

Best option if you does not care about modifying a file with root. This file is generally supported by all distribution. The code snippet that you need to append to the end of `/etc/profile` is same as [login shell](Special:myLanguage/Setup_Fcitx_5#Login_in_shell_profile "wikilink").

## \$HOME/.xprofile

An old perfect option if you are using X11 and display manager. But there is no counterpart for Wayland, so it is not ideal if you want to set environment variable for Wayland. The code that you want to add is same as [login shell](Special:myLanguage/Setup_Fcitx_5#Login_in_shell_profile "wikilink").

## environment.d

This is a new configuration that introduced by system.d, but not widely used supported by desktop environment or display manager. It is basically the environment configuration for systemd user unit. Currently, it is only supported by GDM or Plasma 5.22+. As GDM, it means any session that login with GDM will work. As for Plasma, it means it works for Plasma regardless what DM you are using.

This configuration is applied upon your first user session login and persist afterwards unless you manually stop the systemd user. So after you modifies this configuration, the easiest way to make it effective is to reboot your system.

The syntax is similar to shell, but no `export` is required. For example, you can create a file `$HOME/.config/environment.d/im.conf` with following content:

``
`XMODIFIERS=@im=fcitx`
`GTK_IM_MODULE=fcitx`
`QT_IM_MODULE=fcitx`

## pam_env.so

This is an obsolete solution for following reasons:

- pam deprecate user level configuration `$HOME/.pam_environment` since 1.5.0.
- Some distribution does not enable pam_env in their pam configuration.

If you know it works for your system, you can put following snippet to your `$HOME/.pam_environment`.

`XMODIFIERS DEFAULT=\@im=fcitx`
`GTK_IM_MODULE DEFAULT=fcitx`
`QT_IM_MODULE DEFAULT=fcitx.`

Please **NOTE** that the syntax is different from shell script.

## \$HOME/.config/plasma-workspace/env/\*.sh

A env script location that only works for Plasma desktop, you need to create your own .sh file, e.g. `$HOME/.config/plasma-workspace/env/im.sh` and put the code snippet same as [login shell](Special:myLanguage/Setup_Fcitx_5#Login_in_shell_profile "wikilink").

## Other less common setup

There are some other variable that might be useful certain applications.

### SDL_IM_MODULE

Set the value to fcitx. Only SDL2 requires this. SDL1 uses XIM.

### GLFW_IM_MODULE

This is a variable only used by [kitty](https://github.com/kovidgoyal/kitty/). You need to set it to \`GLFW_IM_MODULE=ibus\`.

### Binary Qt application

Due to Qt 5 does not support XIM, and it only bundles ibus im module, you may want to set \`QT_IM_MODULE=ibus\` for Qt application that does not use your system Qt library. (It may still not work because certain Qt application does not even bundle any im module).

# DBus

On most distribution that ships with systemd, this should no longer be an issue. But if you are using some so called "systemd" free distribution, you may need to start DBus yourself and set the relevant environment variables. Usually, this can be done by adding a line in like this in your start up script. E.g. \$HOME/.xprofile if you are using X11. Also you need to make sure this syntax works for your login shell.

`` eval `dbus-launch --sh-syntax --exit-with-session` ``

# Configure Fcitx 5

See [Configtool (Fcitx 5)](Special:myLanguage/Configtool_(Fcitx_5) "wikilink").
