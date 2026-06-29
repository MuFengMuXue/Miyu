[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Zellij&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://github.com/zellij-org/zellij)

[[]][Package information](https://packages.gentoo.org/packages/app-misc/zellij)

**Zellij** is a terminal workspace with batteries included written in Rust.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [General]](#General)
    -   [[3.2] [Managing Tabs]](#Managing_Tabs)
    -   [[3.3] [Managing Panes]](#Managing_Panes)
    -   [[3.4] [Scroll and Copy Mode]](#Scroll_and_Copy_Mode)
    -   [[3.5] [Session control]](#Session_control)
        -   [[3.5.1] [Start session]](#Start_session)
        -   [[3.5.2] [Attach/Detach]](#Attach.2FDetach)
-   [[4] [Removal]](#Removal)
    -   [[4.1] [Unmerge]](#Unmerge)
-   [[5] [See alse]](#See_alse)

## [Installation]

### [USE flags]

### [USE flags for] [app-misc/zellij](https://packages.gentoo.org/packages/app-misc/zellij) [[]] [A terminal workspace with batteries included]

  ----------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`debug`](https://packages.gentoo.org/useflags/debug)                   Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`man`](https://packages.gentoo.org/useflags/man)                       Build and install man pages
  [`system-sqlite`](https://packages.gentoo.org/useflags/system-sqlite)   Use the system-wide dev-db/sqlite instead of the bundled one
  ----------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-16 09:52] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask app-misc/zellij`

## [Configuration]

The default configuration can be created by issuing:

`user `[`$`]`mkdir ~/.config/zellij `

`user `[`$`]`zellij setup --dump-config > ~/.config/zellij `

## [Usage]

#### [General]

-   [Ctrl]+[p] = Enters Pane mode (to create and manage panes).
-   [Ctrl]+[t] = Enters Tab mode (to create and manage tabs).
-   [Ctrl]+[s] = Enters Scroll mode (to navigate the scrollback buffer).
-   [Ctrl]+[o] = Enters Session mode (to detach from the current session).
-   [Ctrl]+[q] = Quits Zellij and all its sessions.
-   [Alt]+[n] = Creates a new pane (without needing to enter Pane mode).
-   [Alt]+[arrows] = Moves focus between panes.

#### [Managing Tabs]

After pressing [Ctrl]+[t]:

-   [n] = Creates a new tab.
-   [\]] or [l] = Goes to the next tab.
-   [\[] or [h] = Goes to the previous tab.
-   [1-9] = Selects tab 1 through 9.
-   [r] = Renames the current tab.
-   [x] = Closes the current tab.
-   [s] = Synchronizes all panes in the current tab (input in one pane is replicated to all others).

#### [Managing Panes]

After pressing [Ctrl]+[p]:

-   [d] = Creates a new pane below the current one.
-   [n] = Creates a new pane to the right of the current one.
-   [arrows] or [h], [j], [k], [l] = Selects the next pane in the specified direction.
-   [x] = Closes the current pane.
-   [f] = Toggles the current pane to fullscreen mode.
-   [w] = Creates a new pane in floating mode.
-   [c] = Renames the current pane.
-   [p] = Change focus.

#### [Scroll and Copy Mode]

After pressing [Ctrl]+[s]:

-   [k] or [Up Arrow] = Scrolls one line up.
-   [j] or [Down Arrow] = Scrolls one line down.
-   [e] = Edits the scrollback buffer in the system\'s default text editor (defined by the [\$EDITOR] environment variable).

** Note**\
Copying text is generally done by selecting it with the mouse. The selected text is copied to the system clipboard.

### [Session control]

#### [Start session]

To start a new Zellij session with a default name, run:

`user `[`$`]`zellij`

To give the session a specific name on startup, use the [\--session] argument:

`user `[`$`]`zellij --session portage`

#### [][Attach/Detach]

It is possible to detach from a Zellij session, leaving it running in the background. To do this, enter Session mode with [Ctrl]+[o] and press [d]. To view all running sessions, use the command:

`user `[`$`]`zellij list-sessions`

To re-attach to a running session, use the [attach] command (or its shorthand [a]):

`user `[`$`]`zellij attach portage`

## [Removal]

### [Unmerge]

`root `[`#`]`emerge --ask --depclean --verbose app-misc/zellij`

## [See alse]

-   [Tmux](https://wiki.gentoo.org/wiki/Tmux "Tmux") --- a program that enables a number of terminals (or windows), each running a separate program, to be created, accessed, and controlled from a single screen or terminal window.