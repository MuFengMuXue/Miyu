# Gamescope (Linux-specific)

# what is 'gamescope'?
Gamescope is something only Linux has.
It is a microcompositor from Valve that is used on the Steam Deck. Its goal is to provide an isolated compositor that is tailored towards gaming and supports many gaming-centric features such as:

1.    Spoofing resolutions.
2.    Upscaling using **AMD FidelityFX™** Super Resolution or **NVIDIA Image Scaling** (gain fps).
3.    Limit framerates / support tearing / use **open-VR** on all you installed through heroic
4.    ProtonGE: bundeled **FSR / FSHack is gone? simply use Gamescope.**

# Gamescope inside of Heroic-App
## (specific per game/app)
There is a plan to have a Gamescope setting in Heroic, while that is implemented, you can still use it with Heroic following the steps bellow:
1. Install [Gamescope](https://github.com/Plagman/gamescope) in your system.
2. In Heroic, open the game settings and go to the **Other** tab.
3. On the Advanced Options (Environment Variables), put the Gamescope command line you want to use followed by two dashes in the end, for instance: `gamescope -w 1920 -h 1080 -W 3440 -H 1440 -b --`.
4. If you have other variables, make sure you add it add the end of the input like: `DXVK_HUD=full gamescope ... --`
5. For now, enabling `mangohud` or `gamemode` might make gamescope not work, so try with those options enabled first.

# 'gamescoped' Heroic
(*all* apps / games started through hgl also started through gamescope (including FSR-/hotkey-/etc.-capabilities))
(*no window borders anymore*)

0. Install [Gamescope](https://github.com/Plagman/gamescope) in your system.

## 'gamescoped' Heroic - as seperate app
1. edit '$HOME/.local/share/applications/Heroic-Deck.desktop'

[Desktop Entry]
`Categories=App-Starter;`
`Comment=An Open Source alternative to the Epic Games launcher`
`Exec=env GDK_BACKEND=wayland gamescope -w 1920 -h 1080 -f -Y -R --RT --force-grab-cursor --prefer-vk-device --adaptive-sync --sharpness 15 -- /opt/Heroic/heroic --ozone-platform=x11 --enable-features=UseOzonePlatform,WaylandWindowDecorations`
`GenericName=gs_hgl`
`Icon=heroic`
`MimeType=`
`Name=_Heroic_Games`
`Path=`
`StartupNotify=false`
`StartupWMClass=Heroic`
`Terminal=false`
`TerminalOptions=`
`Type=Application`
`X-KDE-SubstituteUID=false`
`X-KDE-Username=`

* { Hint 1: 'Exec-'line, '/opt/Heroic/heroic' is Debian/Ubuntu-specific, should be streamlined to your distro }
* { Hint 2: 'Exec-'line, for better compatability (f.e. if you want to start other electron-based apps through hgl) you could append '--use-angle=vulkan'}

2. 'Heroic-Deck' should be there as new app, look into $HOME/.local/share/applications/ to start it manually

## 'gamescoped' Heroic - as 'login-session'
use Heroic as streamlined gaming-ui or as a beamer- or smartphone-ui with capability of installing native linux-apps by simply 'login' to heroic after you powered on (through sddm, gdm etc., possibly password-free, f.e. through editing sddm-config)

1. edit '/usr/share/wayland-sessions/Heroic-Deck.desktop'
`Exec=/usr/lib/x86_64-linux-gnu/libexec/plasma-dbus-run-session-if-needed kwin_wayland --drm /usr/share/bin/heroicdeck`
`Name=Heroic-Deck 1080p (Wayland)`
`Name[de]=Heroic-Deck 1080p (Wayland)`
`Comment[de]=Heroic-Deck`
`X-KDE-PluginInfo-Version=5.27.3`

* { Hint: 'Exec-'line, --drm could be accompanied / replaced by --xwayland --drm --x11-display }

2. edit '/usr/share/bin/heroicdeck'
`#!/bin/bash`
`/usr/lib/x86_64-linux-gnu/libexec/org_kde_powerdevil &`
`qdbus  local.org_kde_powerdevil /org/kde/Solid/PowerManagement/Actions/PowerProfile setProfile performance`
`#older hardware: use lower base-resolution (f.e. 1920x1080 here) for more fps`
`#kscreen-doctor output.DP-#.mode.#`
`#kscreen-doctor output.DP-#.scale.#`
`env GDK_BACKEND=wayland gamescope -w 1920 -h 1080 -f -Y -R --RT --force-grab-cursor --prefer-vk-device  --adaptive-sync --sharpness 15 -- /opt/Heroic/heroic --ozone-platform=x11 --enable-features=UseOzonePlatform,WaylandWindowDecorations `

* { Hint 1: 'env'-line, if you want 720p for fps reasons, use `'-w 1280 -h 720'` (or something else)}
* { Hint 2: 'env'-line, for better compatability (f.e. if you want to start other electron-based apps through hgl) you could append `'--use-angle=vulkan'`}
* { Hint 3: 'env'-line, '--force-grab-cursor' / --prefer-vk-device needs a relatively new gamescope binary, '--force-grab-cursor' is needed if you 1. use ozone though wayland 2. use antimicrox 3. want to control a hgl-started electron-based-app through antimicrox}

### gamescoped hgl & gamemode (& NICE-capability)
for using gamescope properly with gamemode (and a NICE-capable kernel), just simply
`'sudo setcap 'CAP_SYS_NICE=eip' /usr/games/gamescope'`

### gamescoped hgl & firejail
just put in your firejail-code into the line, f.e. (simplified)
`gamescope -f -- firejail --noprofile --/opt/Heroic/heroic`
* { Hint: Heroic and apps started through it sometimes need a lot of 'caps', you have to manually sort them out if you want to set `--caps` for firejail (benefit: not all steam needs are needed here) }
