\"Optfeature\" in short is a concept for optional features. Some programs are able to dynamically load a library and add functionality, while not breaking the main program if the optional library is missing. Some python scripts etc are essentially capable of doing the same. Optfeature can also be used to advertise additional programs to complete a full software suite, e.g. with [gui-wm/sway](https://packages.gentoo.org/packages/gui-wm/sway) one may have a better experience after also installing [gui-apps/swaybg](https://packages.gentoo.org/packages/gui-apps/swaybg), [gui-apps/swaylock](https://packages.gentoo.org/packages/gui-apps/swaylock), and so on. These additional programs aren\'t linked to sway and sway can work without them.

Optfeature is not to be mixed with [\"automagic dependencies\"](https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Automagic_dependencies "Project:Quality Assurance/Automagic dependencies").

## Contents

-   [[1] [Usage]](#Usage)
    -   [[1.1] [In ebuilds]](#In_ebuilds)
    -   [[1.2] [In your system, as a user]](#In_your_system.2C_as_a_user)
-   [[2] [See also]](#See_also)

## [Usage]

### [In ebuilds]

    inherit optfeature
    ...
    ...
    pkg_postinst()

See the [eclass documentation](https://devmanual.gentoo.org/eclass-reference/optfeature.eclass/index.html).

** Important**\
`PYTHON_USEDEP` should not be used in optfeature package definitions.

### [][In your system, as a user]

Optional features can simply be **emerge**d and they will take effect. However bloating [/var/lib/portage/world] file may later make it harder to identify and remember why some entries are there. Another way is to use [portage sets](https://wiki.gentoo.org/wiki//etc/portage/sets "/etc/portage/sets") dedicated to optfeature. These set files allow commenting, to identify why an entry has been added.

[FILE] **`/etc/portage/sets/optfeature`**

    # Archive support for file-roller,
    app-arch/p7zip
    app-arch/unrar

    # Diagnosis support for htop,
    sys-process/iotop
    sys-process/lsof

    # Encrypted chat support for Thunderbird,
    net-libs/libotr

Add **\@optfeature** to your [/var/lib/portage/world_sets] file, or issue

`root `[`#`]`emerge -av @optfeature`

## [See also]

-   [https://www.gentoo.org/glep/glep-0062.html](https://www.gentoo.org/glep/glep-0062.html) - Optional runtime dependencies via runtime-switchable USE flags (deferred due to inactivity)