# Niri

Niri is a scrollable tiling Wayland compositor. Unlike Sway or Hyprland, Niri arranges the windows in an infinite horizontal desktop, where you can scroll to the left or to the right (although more advanced layouts are possible). It is similar to GNOME's PaperWM and KDE's Karousel.

## Installation
Niri can be installed with the  package. Additionally, to have a better experience, you may want to install:

* : default application launcher in Niri
* : notifications
* waybar: a Wayland bar
* , : to be able to do screen sharing
* alacritty: default terminal in Niri
* : background image
* , : to lock the screen on idle status
* : to run X11 apps
* : to manage and auto-mount USB drives
*  or : complete desktop shell
* : configuration GUI

## Starting
Niri comes with a desktop entry that can be sourced by display managers; selecting it will run  which handles exporting environment variables to systemd.

Additionally you can start Niri from a getty by executing:

 $ niri-session -l

This can be paired with auto login to have a seamless boot experience.

## Configuration
Niri reads the configuration from . It is a KDL file, divided by sections. The default configuration, created on the first run, documents the default options with comments. However, options introduced with updates will not be documented in the user's configuration; you may check Niri's official documentation instead.

Niri automatically applies the configuration when it is saved. The live reload of invalid configuration will not crash Niri; instead, the last working state is preserved, and the user is notified of the configuration error.  can be invoked to validate the configuration outside of a Niri session.

## Keymap
To configure the keymap, edit the  section.

For example, if you want to have a "US Int Alt Gr" layout with  acting as  key:

{{hc|~/.config/niri/config.kdl|
input {
    keyboard {
        xkb {
            layout "us"
            variant "altgr-intl"
            options "ctrl:nocaps"
        }
    }
    ...
}
}}

## Outputs
First run  to get an overview of the outputs recognized by Niri. Then you can apply configs to each monitor. For example to set the HDMI monitor to 2560x1440 60Hz with a 1.2 scaling, and turning off the laptop monitor, set the following:

{{hc|~/.config/niri/config.kdl|
output "HDMI-A-1" {
    mode "2560x1440@60.000"
    scale 1.2
}

output "eDP-1" {
    off
}
}}

## Bindings
The binds section allows to set up the different key combinations that have effect on Niri. Many bindings are already set in the default configuration generated on first launch. These are all remappable.

Please note that Niri does not load any default bindings. If a binding is not specified in the configuration, it will not be active. "Defaults" are simply bindings that are present in the automatically generated configuration. Therefore, take care when removing the bindings. It is recommended to instead comment out unused bindings.

Bindings are defined using the modifiers keys appended with a  sign and the action between brackets. The special action 'spawn' will launch a program. For example, you will find the following bindings that spawn alacritty and  on  and  respectively.  is usually the  key if running standalone, but it is  if it is running inside of another compositor.

{{hc|~/.config/niri/config.kdl|
binds {
    ...
    Mod+T { spawn "alacritty"; }
    Mod+D { spawn "fuzzel"; }
    ...
}
}}

Note that all space-separated arguments to processes started by  must be enclosed in quotes:

{{hc|~/.config/niri/config.kdl|
binds {
    ...
    Mod+Ctrl+semicolon {
        spawn "swaylock" "-c" "121212" "-e" "-f" "-F"
    }
    ...
}
}}

## WASD-like navigation
It is possible to configure Niri workspaces and bindings so that jumping through windows follows a navigation similar to WASD as in games.

{{hc|~/.config/niri/config.kdl|
binds {
    ...
    Mod+A { focus-column-left; }
    Mod+S { focus-window-or-workspace-down; }
    Mod+W { focus-window-or-workspace-up; }
    Mod+D { focus-column-right; }
    ...
}
}}

Be aware that this config will probably need other bindings to be remapped as well. Also, some people may prefer to have the WASD navigation on the right-hand side, or have a more Vim-like navigation.

## Autostart
Niri allows some programs to be started alongside with Niri.
For example, some of the programs mentioned beforehand like ,  and / can be configured:

Note that these processes are tied to the Niri session, and they will be killed when Niri exits or is suspended. To make a process persist, you may set it to a background task by providing the  argument.

## XWayland
Niri does not provide XWayland support for running X11 applications. Instead, it recommends using an external tool:  is listed in the optional dependencies. After installation, no configuration is required.

## Multi GPU Configuration
In laptop (or PC) setups with both integrated graphics and a dedicated GPU, Niri may default to using the dedicated GPU for both the compositor and starting other applications, causing unnecessary battery drain.

To set what GPU Niri should use, first check which render devices are available on your system:

Then, use the PCI address to identify the correct device you want to use for Niri in :

If the first PCI address is the wrong card, try the next one.

Finally add to Niri's configuration and specify the correct render device based on the PCI address you identified:
{{hc|
~/.config/niri/config.kdl|
debug {
    render-drm-device "/dev/dri/renderD128"
}
}}

Reboot your computer. You can now check if one of the rendering devices is correctly in a low power state using:
