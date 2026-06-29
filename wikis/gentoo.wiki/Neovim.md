**Resources**

[[]][Home](https://neovim.io)

[[]][Official documentation](https://neovim.io/doc/general/)

[[]][Package information](https://packages.gentoo.org/packages/app-editors/neovim)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Neovim "wikipedia:Neovim")

[[]][GitHub](https://github.com/neovim/neovim)

[[]][[#neovim](ircs://irc.libera.chat/#neovim)] ([[webchat](https://web.libera.chat/#neovim)])

[![Ohloh Logo](/images/thumb/c/c1/Ohloh-logo.png/30px-Ohloh-logo.png)][Open Hub](https://www.openhub.net/p/neovim)

**Neovim** is a [vi](https://wiki.gentoo.org/wiki/Vi "Vi")-like [text editor](https://wiki.gentoo.org/wiki/Text_editor "Text editor") designed around a relatively small but extendable core that aims to be a versatile and powerful text editor, with the expected learning-curve vs power tradeoff of vi-like modal editors.

Commonly used in a text [terminal](https://wiki.gentoo.org/wiki/Terminal_emulator "Terminal emulator"), several Neovim [GUIs](https://neovim.io/doc/user/gui/) are available, and it can also be embedded in other applications (in [Vscode](https://wiki.gentoo.org/wiki/Vscode "Vscode")^[\[1\]](#cite_note-1)^ or [Firefox](https://wiki.gentoo.org/wiki/Firefox "Firefox")^[\[2\]](#cite_note-2)^, for example).

Though by default Neovim is purely and deliberately a text editor, it\'s heavy focus on extensibility^[\[3\]](#cite_note-3)^ intends it to be adaptable to wider and more diverse use-cases. This has allowed use as a [pager](https://wiki.gentoo.org/wiki/Pager "Pager") ^[\[4\]](#cite_note-4)^, and as a full-fledged [IDE](https://wiki.gentoo.org/wiki/Category:IDE "Category:IDE") ^[\[5\]](#cite_note-5)^, for example.

Based on [Vim](https://wiki.gentoo.org/wiki/Vim "Vim"), the two projects have different goals, despite having evolved from the same codebase. For example, Neovim integrates a [Lua](https://wiki.gentoo.org/wiki/Lua "Lua") interface (while still supporting Vimscript), whereas Vim created Vim9script (which is not planned to be adopted by Neovim^[\[6\]](#cite_note-6)^). Vim provides the graphical [Gvim](https://wiki.gentoo.org/wiki/Vim#Gvim "Vim"), while Neovim is designed to have third-party [GUIs](https://neovim.io/#guis).

The core functionality of Neovim remains compatible with Vim (to the point that most Vimscript Vim plugins still work in Neovim). There are however some major differences between the projects^[\[7\]](#cite_note-7)^, for example Neovim has chosen to remove certain features that were present in Vim^[\[8\]](#cite_note-8)^, Lua plugins can only work on Neovim, Vim9script plugins can only work in Vim, etc.

Neovim includes a native [LSP](https://neovim.io/doc/user/lsp/) framework, and has experimental native support for [tree-sitter](https://neovim.io/doc/user/treesitter/). It uses an asynchronous architecture, [built around the libuv library](https://neovim.io/doc/user/luvref/), to help provide a low-latency user experience.

** See also**\
The [Vim](https://wiki.gentoo.org/wiki/Vim "Vim") article provides general information on vi-like editors. See the [Vim guide](https://wiki.gentoo.org/wiki/Vim/Guide "Vim/Guide") for an introductory tutorial on vi-like editor usage. See the [text editor](https://wiki.gentoo.org/wiki/Text_editor "Text editor") article for general information on installing and configuring text editors in Gentoo.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
    -   [[1.3] [Additional software]](#Additional_software)
        -   [[1.3.1] [Plugins]](#Plugins)
        -   [[1.3.2] [Plugin managers]](#Plugin_managers)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Environment variables]](#Environment_variables)
    -   [[2.2] [Files]](#Files)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Invocation]](#Invocation)
    -   [[3.2] [Tutorial]](#Tutorial)
-   [[4] [Removal]](#Removal)
    -   [[4.1] [Unmerge]](#Unmerge)
-   [[5] [Troubleshooting]](#Troubleshooting)
    -   [[5.1] [I\'m trapped in neovim!]](#I.27m_trapped_in_neovim.21)
    -   [[5.2] [No colors when running through a terminal multiplexer such as screen or tmux]](#No_colors_when_running_through_a_terminal_multiplexer_such_as_screen_or_tmux)
    -   [[5.3] [No syntax highlighting on Gentoo configuration files]](#No_syntax_highlighting_on_Gentoo_configuration_files)
        -   [[5.3.1] [Workaround]](#Workaround)
        -   [[5.3.2] [Install gentoo-syntax with lazy.nvim]](#Install_gentoo-syntax_with_lazy.nvim)
-   [[6] [Want to contribute]](#Want_to_contribute)
-   [[7] [See also]](#See_also)
-   [[8] [References]](#References)

## [Installation]

### [USE flags]

### [USE flags for] [app-editors/neovim](https://packages.gentoo.org/packages/app-editors/neovim) [[]] [Vim-fork focused on extensibility and agility]

  ----------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`+nvimpager`](https://packages.gentoo.org/useflags/+nvimpager)   Install nvimpager symlink to less.sh macro
  [`test`](https://packages.gentoo.org/useflags/test)               Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  ----------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-03 17:17] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask app-editors/neovim`

** Note**\
After installation, it may be desirable to [set the \"vi\" command to link to neovim](https://wiki.gentoo.org/wiki/Vi#.2Fusr.2Fbin.2Fvi_symlink "Vi"). The system default text editor may also be [set to use neovim.](https://wiki.gentoo.org/wiki/Text_editor#Setting_system_default "Text editor")

### [Additional software]

#### [Plugins]

Plugins extend the editor\'s functionality and are entirely optional. [Many plugins](https://github.com/rockerBOO/awesome-neovim) for neovim may be found across the Internet, however much can be accomplished with \"plain\" neovim and sometimes being mindful not to get dragged down a configuration rabbit hole can help to stay productive (perhaps like Gentoo itself).

Note that [vim plugins](https://github.com/mhinz/vim-galore/blob/master/PLUGINS.md) are usually compatible with neovim.

Plugins may be [installed manually](https://neovim.io/doc/user/usr_05.html#05.5), though a plugin manager can make working with plugins much easier.

#### [Plugin managers]

Several plugin managers are available for neovim, including an experimental built-in plugin manager, [vim.pack](https://neovim.io/doc/user/pack/#vim.pack), since version 0.12 (which is awaiting stabilization in Gentoo, as of 2026-05).

Users have a choice of [plugin managers](https://github.com/rockerBOO/awesome-neovim?tab=readme-ov-file#plugin-manager) to fit their needs, or preferences: most will offer basic core-features such as automatic plugin download and installation, automatic plugin updates, or plugin configuration facilities. Some provide fuller, or different, sets of features, and some focus on aspects such as ease of use, speed, or minimalism.

Some examples of plugin managers are [vim-plug](https://github.com/junegunn/vim-plug), [mini-deps](https://github.com/nvim-mini/mini.nvim/blob/main/readmes/mini-deps.md), [pathogen](https://github.com/tpope/vim-pathogen), or [lazy.nvim](https://lazy.folke.io/) (not to be confused with [LazyVim](https://www.lazyvim.org/), which is a whole preconfigured neovim setup).

## [Configuration]

### [Environment variables]

Important environment variables include:

-   `NVIM_APPNAME` - Allows starting neovim with an alternative configuration, for example for testing or if maintaining several separate neovim configurations is required. Run [:help \$NVIM_APPNAME] in neovim for more information.
-   `VIMRUNTIME` - Used to locate runtime files (documentation, syntax highlighting, etc.).
-   `VIMINIT` - Ex commands to be executed at startup. Run [:help VIMINIT] in neovim for more information.

A full list of environment variables can be found under the environment section of [man 1 nvim].

### [Files]

Neovim honors XDG base directories.^[\[9\]](#cite_note-9)^ Therefore the configuration directories are defined by `XDG_CONFIG_HOME` (defaults to [\~/.config]) or `XDG_CONFIG_DIRS` (defaults to [/etc/xdg]) variables.

-   [\$XDG_CONFIG_HOME/nvim] - User-local Neovim configuration directory
-   [\$XDG_CONFIG_HOME/nvim/init.vim] - User-local Neovim configuration file
-   [\$XDG_CONFIG_HOME/nvim/init.lua] - User-local Neovim Lua configuration file
-   [\$XDG_CONFIG_DIRS/nvim/sysinit.vim] - System-global Neovim configuration file

For example, customize Neovim for a specific user by editing the:

[FILE] **`$XDG_CONFIG_HOME/nvim/init.vim`**

    set number
    " sets the number on left-hand side
    set relativenumber
    " sets relative number on left-hand side
    set tabstop=4
    set shiftwidth=4
    set expandtab
    " sets the tab to be 4 spaces

The above configuration may alternatively be achieved with Neovim\'s init.lua:

[FILE] **`$XDG_CONFIG_HOME/nvim/init.lua`**

    local options =

    -- Prepends vim.opt to all of the options defined above; using a loop.
    for k, v in pairs (options) do
        vim.opt[k] = v
    end

This particular example activates line numbers on the left-hand side of the editor, sets relative numbers, and changes the tab width.

For a full list of options, type

`:help options`

while in vim normal mode.

## [Usage]

### [Invocation]

`user `[`$`]`nvim --help`

    Usage:
      nvim [options] [file ...]      Edit file(s)
      nvim [options] -t <tag>        Edit file where tag is defined
      nvim [options] -q [errorfile]  Edit file with first error

    Options:
      --                    Only file names after this
      +                     Start at end of file
      --cmd <cmd>           Execute <cmd> before any config
      +<cmd>, -c <cmd>      Execute <cmd> after config and first file

      -b                    Binary mode
      -d                    Diff mode
      -e, -E                Ex mode
      -es, -Es              Silent (batch) mode
      -h, --help            Print this help message
      -i <shada>            Use this shada file
      -m                    Modifications (writing files) not allowed
      -M                    Modifications in text not allowed
      -n                    No swap file, use memory only
      -o[N]                 Open N windows (default: one per file)
      -O[N]                 Open N vertical windows (default: one per file)
      -p[N]                 Open N tab pages (default: one per file)
      -r, -L                List swap files
      -r <file>             Recover edit state for this file
      -R                    Read-only mode
      -S <session>          Source <session> after loading the first file
      -s <scriptin>         Read Normal mode commands from <scriptin>
      -u <config>           Use this config file
      -v, --version         Print version information
      -V[N][file]           Verbose [level][file]

      --api-info            Write msgpack-encoded API metadata to stdout
      --embed               Use stdin/stdout as a msgpack-rpc channel
      --headless            Don't start a user interface
      --listen <address>    Serve RPC API from this address
      --noplugin            Don't load plugins
      --startuptime <file>  Write startup timing messages to <file>

    See ":help startup-options" for all options.

### [Tutorial]

Neovim has a built-in interactive tutorial that aims to teach basic nvim usage.

The tutor can be stared from within nvim by pressing [:] in normal mode then entering the command [Tutor] [Enter] (the command is case-sensitive).

If nvim is not yet running, the tutor may alternatively be started from a [shell](https://wiki.gentoo.org/wiki/Shell "Shell") when launching nvim:

`user `[`$`]`nvim +Tutor`

** Note**\
If using [LazyVim](https://www.lazyvim.org/), the tutorial plugin is disabled by default, in order to improve loading times. Before use it must be re-enabled by editing the [lazy.lua](https://www.lazyvim.org/configuration/lazy.nvim) configuration file.

## [Removal]

### [Unmerge]

`root `[`#`]`emerge --ask --depclean --verbose app-editors/neovim`

## [Troubleshooting]

### [][I\'m trapped in neovim!]

** See also**\
As Vim and Neovim share the same basic commands, see the [corresponding section in the Vim article](https://wiki.gentoo.org/wiki/Vim#I.27m_trapped_in_vim.21 "Vim") on how to exit vi-like editors.

### [No colors when running through a terminal multiplexer such as [screen] or [tmux]]

`user `[`$`]`export TERM=screen-256color`

`user `[`$`]`screen`

See: [https://github.com/neovim/neovim/wiki/FAQ#home-or-some-other-special-key-doesnt-work](https://github.com/neovim/neovim/wiki/FAQ#home-or-some-other-special-key-doesnt-work)

### [No syntax highlighting on Gentoo configuration files]

[   Note to editors] []

This section needs work, if anyone with more advanced knowledge of neovim or [[[app-vim/gentoo-syntax]](https://packages.gentoo.org/packages/app-vim/gentoo-syntax)[]] could help. Perhaps the plugin could be installed \"natively\" with neovim rather than using lazy.nvim\...

Unfortunately, [[[app-vim/gentoo-syntax]](https://packages.gentoo.org/packages/app-vim/gentoo-syntax)[]] has no native support for Neovim yet. Thus, Gentoo configuration files (e.g. most files under [/etc/portage]) don\'t have specialized syntax highlighting and the editor doesn\'t initialize the buffer for new Gentoo files (e.g. new ebuilds, new init scripts) with a skeleton.

#### [Workaround]

Since Neovim is compatible with Vim configuration, the [/usr/share/vim/vimfiles] directory, where the system wide installed Vim plugins reside, can be added to the Neovim runtime path in [\$XDG_CONFIG_HOME/nvim/init.vim]:

[FILE] **`$XDG_CONFIG_HOME/nvim/init.vim`**

    set rtp+=/usr/share/vim/vimfiles

To do the same if using Lua configuration, edit [\$XDG_CONFIG_HOME/nvim/init.lua]:

[FILE] **`$XDG_CONFIG_HOME/nvim/init.lua`**

    vim.opt.rtp:append('/usr/share/vim/vimfiles')

If you\'re using Lazy as your plugin manager, the previous won\'t work since Lazy will reset the runtime path by default. You can instead do the following:

[FILE] **`$XDG_CONFIG_HOME/nvim/init.vim`**

    require("lazy").setup(,
        }
      }
    })

However, this is just a workaround with the side effect that all other plugins which are installed for Vim system wide are now enabled in Neovim as well.

#### [Install gentoo-syntax with lazy.nvim]

Installing the [[[app-vim/gentoo-syntax]](https://packages.gentoo.org/packages/app-vim/gentoo-syntax)[]] package with portage will make the plugin available for [vim](https://wiki.gentoo.org/wiki/Vim "Vim"), but not currently for neovim. It appears to be possible to install the *gentoo-syntax* vim plugin in neovim with the lazy.nvim plugin manager however. If using the lazy.nvim package manager, this may be an alternative for the previous workaround.

Create a file to install *gentoo-syntax*, just like installing any other plugin with lazy.nvim (the [\$XDG_CONFIG_HOME] directory is often [\~/.config/]):

[FILE] **`$XDG_CONFIG_HOME/nvim/lua/plugins/gentoo.lua`**

    return ,
    }

Then run an installation or sync with lazy.nvim as usual.

## [Want to contribute]

Neovim is a community fork of Vim. Contribute here: [Github: Neovim](https://github.com/neovim/neovim)

## [See also]

-   [Knowledge Base:Edit a configuration file](https://wiki.gentoo.org/wiki/Knowledge_Base:Edit_a_configuration_file "Knowledge Base:Edit a configuration file")
-   [Text editor](https://wiki.gentoo.org/wiki/Text_editor "Text editor") --- a program to create and edit text files.
-   [Vi](https://wiki.gentoo.org/wiki/Vi "Vi") --- a powerful *modal* [text-based editor](https://wiki.gentoo.org/wiki/Text_editor "Text editor") with a long history in the Unix(like) operating system.
-   [Vim](https://wiki.gentoo.org/wiki/Vim "Vim") --- a [vi](https://wiki.gentoo.org/wiki/Vi "Vi")-like [text editor](https://wiki.gentoo.org/wiki/Text_editor "Text editor"), originally descended from the [Stevie](https://en.wikipedia.org/wiki/Stevie_(text_editor) "wikipedia:Stevie (text editor)") vi clone.
-   [Vim/Guide](https://wiki.gentoo.org/wiki/Vim/Guide "Vim/Guide") --- explain basic usage for users new to [vi-like](https://en.wikipedia.org/wiki/vi "wikipedia:vi") text editors in general, and vim in particular.

## [References]

1.  [[[↑](#cite_ref-1)] [[https://github.com/vscode-neovim/vscode-neovim](https://github.com/vscode-neovim/vscode-neovim)]]
2.  [[[↑](#cite_ref-2)] [[https://github.com/glacambre/firenvim](https://github.com/glacambre/firenvim)]]
3.  [[[↑](#cite_ref-3)] [This design choice yields [plugins](https://neovim.io/doc/user/usr_05/#plugin), [remote-plugins](https://neovim.io/doc/user/remote_plugin/) (for interfacing with a wide-range of programming languages), it\'s [API-centric](https://neovim.io/doc/user/api/) architecture, embedding facilities (through it\'s [RPC interface](https://neovim.io/doc/user/api/#RPC) or the libnvim library), amongst other features.]]
4.  [[[↑](#cite_ref-4)] [[https://github.com/lucc/nvimpager](https://github.com/lucc/nvimpager)]]
5.  [[[↑](#cite_ref-5)] [[https://neovim.io/charter/](https://neovim.io/charter/)]]
6.  [[[↑](#cite_ref-6)] [[https://neovim.io/charter/](https://neovim.io/charter/)]]
7.  [[[↑](#cite_ref-7)] [[https://neovim.io/doc/user/vim_diff/](https://neovim.io/doc/user/vim_diff/)]]
8.  [[[↑](#cite_ref-8)] [[https://neovim.io/doc/user/vim_diff/#\_removed-legacy-features](https://neovim.io/doc/user/vim_diff/#_removed-legacy-features)]]
9.  [[[↑](#cite_ref-9)] [[XDG base directory specification support #3470](https://github.com/neovim/neovim/pull/3470) , GitHub. Retrieved on December 31, 2021]]