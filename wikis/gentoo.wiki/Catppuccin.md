[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Catppuccin&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][GitHub](https://github.com/catppuccin/gtk)

[[]][x11-themes/catppuccin-gtk](https://github.com/gentoo/guru/tree/master/x11-themes/catppuccin-gtk)

**catppuccin** is a soothing pastel theme.

## [Installation]

### [Emerge]

Catppuccin is in the **GURU** repository.

First, enable the repository:

`root `[`#`]`eselect repository enable guru`

Sync the repository:

`root `[`#`]`emerge --sync guru`

Finally, emerge **catppuccin-gtk**:

`root `[`#`]`emerge --ask x11-themes/catppuccin-gtk`

A temporary workaround for now due to problems with 1.0.3 is to emerge **=catppuccin-gtk-0.7.5**.

For icons, emerge **tela-icon-theme**:

`root `[`#`]`emerge --ask x11-themes/tela-icon-theme`

## [Kvantum]

For a qt theme, install **catppuccin-kvantum**.

`root `[`#`]`emerge --ask x11-themes/catppuccin-kvantum`

Then, edit your **.profile**:

[FILE] **`~/.profile`**

    export QT_STYLE_OVERRIDE=kvantum