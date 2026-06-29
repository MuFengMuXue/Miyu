**Resources**

[[]][Home](https://github.com/hyprwm/hyprpaper/)

[[]][GitHub](https://github.com/hyprwm/hyprpaper)

[[]][Official documentation](https://github.com/hyprwm/hyprpaper#readme)

**hyprpaper** is a blazing fast [Wayland](https://wiki.gentoo.org/wiki/Wayland "Wayland") wallpaper utility with IPC controls.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Alternatives]](#Alternatives)
-   [[3] [See also]](#See_also)
-   [[4] [References]](#References)

## [Installation]

### [USE flags]

Currently this package has no use flags.

### [Emerge]

It is available in the [GURU](https://wiki.gentoo.org/wiki/Project:GURU/Information_for_End_Users "Project:GURU/Information for End Users") repository^[\[1\]](#cite_note-1)^. After enabling that repo, run

`root `[`#`]`emerge --ask gui-apps/hyprpaper`

## [Configuration]

For a simple wallpaper that loads when Hyprland starts, place `exec-once=hyprpaper` into the Hyprland config file. Then create `~/.config/hypr/hyprpaper.conf` with the following lines:

[FILE] **`~/.config/hypr/hyprpaper.conf`**

    wallpaper

Replace eDP-1 to denote the monitor being used. This preloads wallpaper.jpg and sets it as the default wallpaper. Refer to the official documentation link above for more advanced configuration options. Use of \~ in the wallpaper file paths may cause issues, so it is safer to default to spelling out the full path.

** Note**\
For paths that contain spaces, no quotes `"` or escaping `\` needed, for example: `path = /path/to/my bg.jpg`

### [Alternatives]

See [https://wiki.hypr.land/Useful-Utilities/Wallpapers/](https://wiki.hypr.land/Useful-Utilities/Wallpapers/) for other Hyprland wallpaper utility options.

## [See also]

-   [Hyprland](https://wiki.gentoo.org/wiki/Hyprland "Hyprland") --- an open-source [Wayland compositor](https://wiki.gentoo.org/wiki/Wayland_compositor "Wayland compositor") written in C++.
-   [List of software for Wayland](https://wiki.gentoo.org/wiki/List_of_software_for_Wayland "List of software for Wayland") --- various desktop related packages for Wayland

## [References]

1.  [[[↑](#cite_ref-1)] [[https://gpo.zugaina.org/gui-apps/hyprpaper](https://gpo.zugaina.org/gui-apps/hyprpaper)]]