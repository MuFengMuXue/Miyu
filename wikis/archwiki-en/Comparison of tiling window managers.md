# Comparison of tiling window managers

This article provides an unbiased comparison of the most popular tiling window managers (as opposed to floating window managers).

## Comparison table
The following table lists the most popular tiling window managers alongside notable features, providing readers with a quick overview.

{| class="wikitable sortable" style="text-align: center;"
! Window Manager
! Written in
! Configured with
! Management style
! System tray support
! On-the-fly reload
! Information bars
! Compositing
! Default layouts
! Pixel usage
! External control
! Library
! Multiple (n) monitor behavior
! ICCCM/EWMH compliant
! Maintenance
|-
! Awesome
| C || Lua || Dynamic || Built-in || Yes || Built-in, images and text || External || max, nh-stack (and invert), nv-stack (and invert), free || Variable borders, optional h-tab titles || dbus (if enabled) || XCB || n-tags (workspaces). Per default 9  are enabled. Example || Yes || Active
|-
! bspwm
| C || Anything || Hybrid || None || Yes || Can write internal state to a FIFO || External || v-split, h-split || Variable borders || via  || XCB || Monitors hold Desktops || Yes || Active
|-
! dwm
| C || C (recompile) || Dynamic || Optional Patch || Optional || Built-in, reads from root window name || External || v-stack, max || || via dwmfifo || Xlib || n regions, 9 workspaces fixed to each region || No || Active
|-
! FrankenWM
| C || C (recompile) || Dynamic || None || No || No, outputs information to stdout, which can easily be parsed and displayed by an external monitor or panel (dzen2, conky, etc) || External || v-stack (and invert), h-stack (and invert), dual-v/h-stack, grid, fibonacci (vh-stack), rows, columns, max, free || Variable borders ||  || XCB ||  || No || Active
|-
! herbstluftwm
| C++ || Anything || Manual || None || Yes ||  || External || vertical, horizontal, grid, max, tabbed || 1-pix borders || commands via  || Xlib || n regions, 9 workspaces visible in any region || Yes || Active
|-
! i3
| C || Text || Manual || i3bar || Yes (Layout is preserved) || text piped to i3bar (/ and others can be used) || External || tree, v-split, h-split, stacked, tabbed, max, can be nested infinitely || None, 1-pix or 2-pix, optional titlebars, can hide edge borders || commands via ipc (or i3-msg, which uses ipc) || XCB || n regions || Yes || Active
|-
! LeftWM
| Rust || RON (user settings) / Anything (themes) || Dynamic || None || Yes || Yes, many options through theme system || External || v-stack, columns, rows || Variable based on theme || supports  and sending commands to a named pipe || Xlib || Workspaces and monitors are not tied. Many workspaces for monitor or many monitors for workspace || Yes || Active
|-
! Notion
| C, Lua || Lua, compatible with Ion3 configs || Manual || trayion, stalonetray || Yes || configurable || ? || h-tab, max || Configurable borders and titlebars/tabs || EWMH, arbitrary Lua scripts which have access to the rich internal API || Xlib || n workspaces on each monitor. Supports on-the-fly changes in topology || || Active
|-
! qtile
| Python || Python || Dynamic || Yes || Yes || Yes || External || tree, v-split, h-split, stacked, tabbed, max || No borders, although customizable || Hooks, Server mode || XCB || || || Active
|-
! Ratpoison
| C || Text || Manual || None || Yes || Yes || External || max || || || Xlib || || No || Active
|-
! Snapwm
| C || Reloadable Text || Dynamic || None || Yes || Built-in, reads from root window name || External || nVertical, Fullscreen, nHorizontal, Grid, Center Stacking || Variable borders, no titles || || Xlib || Number of desktops distributed evenly between monitors || || Active
|-
! Spectrwm
| C || Text || Dynamic || None || Yes || Built-in, reads from user script || No || nv-stack, nh-stack, max || 1-pix borders, no titles || || XCB || n regions, 10 workspaces visible in any region || No || Active
|-
! Stumpwm
| Common Lisp || Common Lisp || Manual || StumpTray || Yes || Yes || External || max || || SLIME server ("Swank") || CLX (Xlib-equivalent) || || No || Active
|-
! xmonad
| Haskell || Haskell || Dynamic || None || Yes || No || Yes, with xmonad-contrib and an external manager || nv-stack, nh-stack, max || Variable borders, no titles || via XMonad-Hooks-ServerMode || Xlib || n regions, 9 workspaces visible in any region || Yes / via XMonad-Hooks-EwmhDesktops || Active
|-
|}

## Management style
Dynamic management emphasizes automatic management of window layouts for speed and simplicity. Manual management emphasizes manual adjustment of layout and sizing with potentially more precise control, at the cost of more time spent moving and sizing windows.

## Layouts
A number of common layout types appear in several tiling WMs, although the terminology varies somewhat.
* max: one window shown fullscreen (with or without a status bar, title and borders). Aka: monocle (dwm, monsterwm).
* h-stack: master area in top half, other windows stack up horizontally in the bottom half. The master area may be resizable. May be inverted top-bottom (wmfs). Aka: bottom stack (dwm), bstack(monsterwm).
* v-stack: master area in left half, other windows stack up vertically in the right half. The master area may be resizable. May be inverted left-right (wmfs). Aka: tile (dwm, monsterwm).
* nh-stack: h-stack allowing >=1 windows in master area. Aka: nbstack (dwm)
* nv-stack: v-stack allowing >=1 windows in master area. Aka: ntile (dwm)
* mirror-h: nh-stack with stacks above and below the master area
* mirror-v: nv-stack with stacks to the left and right of the master area
* h-tab: one window shown fullscreen with all window titles shown horizontally (like browser tabs)
* v-tab: one window shown fullscreen with all window titles shown vertically. Aka: stack (wmii).
* h-split: a keybinding splits the current window horizontally creating space for another
* v-split: a keybinding splits the current window vertically creating space for another
* columns: manual layout style which treats windows as belonging to vertical columns
* rows: manual layout style which treats windows as belonging to horizontal rows
* grid: window positions and sizes based on a regular NxM grid. May be automatic (like wmfs, monsterwm) or manual (like Subtle).

## Key bindings
Tiling window managers are usually designed to be used entirely with the keyboard or with keyboard & mouse. This is for speed (reaching for and moving a mouse is slow) and ease of use. Sensible key bindings are crucial to making workflow fast and efficient. Some default sets are better than others, but generally the keys can be rebound as desired by the user.
