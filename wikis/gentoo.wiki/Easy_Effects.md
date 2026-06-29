[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Easy_Effects&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://wwmm.github.io/easyeffects/)

[[]][Package information](https://packages.gentoo.org/packages/media-sound/easyeffects)

[[]][GitHub](https://github.com/wwmm/easyeffects)

**Easy Effects** is a limiter, compressor, convolver, equalizer, auto volume, and many other plugins, for [PipeWire](https://wiki.gentoo.org/wiki/PipeWire "PipeWire") applications.

Easy Effects was:

> formerly known as PulseEffects, but \... was renamed to Easy Effects after it started to use GTK4 and GStreamer usage was replaced by native PipeWire filters. And eventually the whole application was ported from GTK4 to a combination of Qt, QML and KDE/Kirigami frameworks.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)

## [Installation]

### [USE flags]

### [USE flags for] [media-sound/easyeffects](https://packages.gentoo.org/packages/media-sound/easyeffects) [[]] [Limiter, auto volume and many other plugins for PipeWire applications]

  --------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+doc`](https://packages.gentoo.org/useflags/+doc)             Install packages needed to display built-in user documentation
  [`calf`](https://packages.gentoo.org/useflags/calf)             Enable use of media-plugins/calf for adding various FX
  [`debug`](https://packages.gentoo.org/useflags/debug)           Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`mda-lv2`](https://packages.gentoo.org/useflags/mda-lv2)       Enable use of media-plugins/mda-lv2 for the loudness FX
  [`webengine`](https://packages.gentoo.org/useflags/webengine)   Read documentation inside the application with dev-qt/qtwebengine
  [`zamaudio`](https://packages.gentoo.org/useflags/zamaudio)     Enable use of media-plugins/zam-plugins for the maximizer FX
  --------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-11-27 22:54] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask media-sound/easyeffects`

## [Usage]

To start Easy Effects and launch its GUI:

`user `[`$`]`easyeffects`

To start Easy Effects without launching the GUI, use:

`user `[`$`]`easyeffects -w`

or

`user `[`$`]`easyeffects --hide-window`

To list available presets:

`user `[`$`]`easyeffects -p`

To load a preset at startup:

`user `[`$`]`easyeffects -l `*``*

where \"\\" should be replaced by the name of the preset.

The `-p` and `-l` options have long forms, `--presets` and `--load-preset`, respectively.