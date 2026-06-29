[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Halloy&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][GitHub](https://github.com/squidowl/halloy)

**Halloy** is an open-source IRC client written in Rust, with the iced GUI library. It aims to provide a simple and fast client for Mac, Windows, and Linux platforms.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Config]](#Config)

## [Installation]

### [USE flags]

Halloy supports the following USE flags:

opengl vulkan wayland X debug

### [Emerge]

Halloy is available on the [Project:GURU](https://wiki.gentoo.org/wiki/Project:GURU "Project:GURU") repository.

Instructions for enabling this repository can be found here: [Project:GURU/Information_for_End_Users](https://wiki.gentoo.org/wiki/Project:GURU/Information_for_End_Users "Project:GURU/Information for End Users")

After enabling the repository, emerge Halloy.

`root `[`#`]`emerge --ask net-irc/halloy`

## [Usage]

### [Config]

Halloy uses toml configuration files to manage connections and settings. An example configuration file:

[FILE] **`~/.config/halloy/config.toml`**

    # Halloy config template.
    #
    # For a complete list of available options,
    # please visit https://halloy.squidowl.org/configuration/index.html

    #[servers.liberachat]
    #nickname = "larry"
    #server = "irc.libera.chat"
    #port = 6697
    #use_tls = true
    #channels = ["#halloy","#gentoo"]