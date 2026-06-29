**Resources**

[[]][Home](https://helix-editor.com/)

[[]][Official documentation](https://docs.helix-editor.com/)

[[]][Package information](https://packages.gentoo.org/packages/app-editors/helix)

[[]][https://x-editor/helix GitHub](https://github.com/heli:)

**Helix** is a \'Post-Modern\' modal [text editor](https://wiki.gentoo.org/wiki/Text_editor "Text editor") based on [Neovim](https://wiki.gentoo.org/wiki/Neovim "Neovim") and [Kakoune](https://wiki.gentoo.org/wiki/Kakoune "Kakoune") that is written in [Rust](https://wiki.gentoo.org/wiki/Rust "Rust"). Helix comes with a built-in language server, multiple selections, and smart syntax highlighting.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
-   [[3] [Usage]](#Usage)
-   [[4] [Themes]](#Themes)
-   [[5] [Language support]](#Language_support)
-   [[6] [See Also]](#See_Also)

## [Installation]

### [USE flags]

### [USE flags for] [app-editors/helix](https://packages.gentoo.org/packages/app-editors/helix) [[]] [A post-modern text editor]

  ------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+grammar`](https://packages.gentoo.org/useflags/+grammar)   Build and install grammar language files
  [`debug`](https://packages.gentoo.org/useflags/debug)         Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  ------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-03-14 18:46] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask app-editors/helix`

## [Configuration]

Helix uses the [TOML](https://en.wikipedia.org/wiki/TOML "wikipedia:TOML") format for configuration, making the configuration much easier and cleaner than comparable text editors. The configuration is stored at [\~/.config/helix/config.toml].

The runtime directory is installed into [/usr/share/helix/runtime], and needs to be linked to the configuration of the user accounts running helix:

`user `[`$`]`ln -s /usr/share/helix/runtime ~/.config/helix/runtime`

## [Usage]

Helix can be started with [hx]:

`user `[`$`]`hx`

** Tip**\
Use **hx \--tutor** for an interactive introduction to Helix.

## [Themes]

Helix already has a large amount of themes built-in. Setting the theme can be done during a session with `:theme catppucin_latte` or inside the configuration file:

[FILE] **`~/.config/helix/config.toml`**

    theme = "catppuccin_frappe"

## [Language support]

Helix support languages through LSP with [several LSP already pre-configured](//docs.helix-editor.com/lang-support.html).

The server for the corresponding language can be installed by placing the executable in `PATH`. For example, [marksman] for markdown will allow the user to jump between headings. This package is not available yet on Gentoo but a binary can be found [on Github](https://github.com/artempyanykh/marksman/releases).

Configuration can be done in [languages.toml]. For example, setting [texlab](https://github.com/latex-lsp/texlab) with [tectonic](//tectonic-typesetting.github.io/en-US/index.html) (both not yet packaged by Gentoo but easily installed):

[FILE] **`~/.config/helix/languages.toml`**

    [language-server]
    texlab =  } } , onSave  = true } }

}

Using a LSP in [LaTeX](https://wiki.gentoo.org/wiki/LaTeX "LaTeX") allows for example to have a completion upon the bibliography with the [\\cite command.

## [See Also]

-   [Vim](https://wiki.gentoo.org/wiki/Vim "Vim") --- a [vi](https://wiki.gentoo.org/wiki/Vi "Vi")-like [text editor](https://wiki.gentoo.org/wiki/Text_editor "Text editor"), originally descended from the [Stevie](https://en.wikipedia.org/wiki/Stevie_(text_editor) "wikipedia:Stevie (text editor)") vi clone.
-   [Neovim](https://wiki.gentoo.org/wiki/Neovim "Neovim") --- a [vi](https://wiki.gentoo.org/wiki/Vi "Vi")-like [text editor](https://wiki.gentoo.org/wiki/Text_editor "Text editor") designed around a relatively small but extendable core that aims to be a versatile and powerful text editor
-   [Kakoune](https://wiki.gentoo.org/wiki/Kakoune "Kakoune") --- a modern, actively developed [editor](https://wiki.gentoo.org/wiki/Text_editor "Text editor") for the [command line](https://wiki.gentoo.org/wiki/Shell "Shell"), inspired by [vi](https://wiki.gentoo.org/wiki/Vi "Vi").