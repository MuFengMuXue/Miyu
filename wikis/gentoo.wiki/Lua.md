[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Lua&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](http://www.lua.org/)

[[]][Package information](https://packages.gentoo.org/packages/dev-lang/lua)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Lua_(programming_language) "wikipedia:Lua (programming language)")

[[]][[#lua](ircs://irc.libera.chat/#lua)] ([[webchat](https://web.libera.chat/#lua)])

[[]][[#lua-support](ircs://irc.libera.chat/#lua-support)] ([[webchat](https://web.libera.chat/#lua-support)])

**Lua** is a powerful light-weight programming language designed for extending applications. It can be embedded into various application as scripting language.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Enabling different Lua versions]](#Enabling_different_Lua_versions)
-   [[3] [See also]](#See_also)

## [Installation]

### [USE flags]

### [USE flags for] [dev-lang/lua](https://packages.gentoo.org/packages/dev-lang/lua) [[]] [A powerful light-weight programming language designed for extending applications]

  ------------------------------------------------------------------- ---------------------------------------------------------------------------------------
  [`+deprecated`](https://packages.gentoo.org/useflags/+deprecated)   make deprecated data structures/routines available
  [`readline`](https://packages.gentoo.org/useflags/readline)         Enable support for libreadline, a GNU line-editing library that almost everyone wants
  ------------------------------------------------------------------- ---------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-23 10:23] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask dev-lang/lua`

## [Configuration]

### [Enabling different Lua versions]

The [[[app-eselect/eselect-lua]](https://packages.gentoo.org/packages/app-eselect/eselect-lua)[]] package provides an [eselect](https://wiki.gentoo.org/wiki/Eselect "Eselect") module to switch between different Lua slots. Once this package has been installed, list available Lua versions by running:

`user `[`$`]`eselect lua list`

To enable the version designated by number n in the list, use `lua set`:

`user `[`$`]`eselect lua set n`

## [See also]

-   [Lua/Porting notes](https://wiki.gentoo.org/wiki/Lua/Porting_notes "Lua/Porting notes")