# Comparison of tiling compositors

This article provides an unbiased comparison of the most popular tiling Wayland compositors (as opposed to floating window managers).

## Comparison table
{| class="wikitable sortable" style="text-align: center;"
! Window Manager
! Written in
! Configured with
! Management style
! System tray support
! On-the-fly reload
! Information bars
! Default layouts
! Pixel usage
! External control
! Library
! Multiple (n) monitor behavior
! Maintenance
|-
! Cagebreak
| C || Text || Manual || || || || || || ||libx, wlroots || ||
|-
! cwc
| C || C, Lua || Dynamic ||   || || || || || || wlroots || ||
|-
! dwl
| C || C (recompile) || Dynamic || Optional patch || Optional patch || Optional patch || master, monocle || 1px border || Optional patch || wlroots || n regions, 9 workspaces fixed to each region ||
|-
! Hyprland
| C++ || Lua || Dynamic, Scrolling || None || Yes (automatic) || None || dwindle (default), master, scrolling || Configurable titles and borders || hyprctl || Aquamarine || Configurable ||
|-
! MangoWM
| C || Text || Dynamic, Scrolling || None || Yes || None || || Variable borders, no titles || mmsg || wlroots || n regions, 9 workspaces fixed to each region ||  ||
|-
! miracle-wm
| C++ || YAML || Manual || None || Yes || || || Configurable titles and borders || swaymsg || Mir || Configurable ||
|-
! niri
| Rust || [https://kdl.dev KDL || Scrolling || None || Yes || None || || || niri msg || Smithay || Per-monitor dynamic workspaces ||
|-
! Qtile
| Python || Python || Dynamic || Built-in, via freedesktop StatusNotifierItem || Built-in preview(?)|| Built-in || Several built-in options || || || wlroots || ||
|-
! River Classic
| Zig|| Bash (default), any language|| Dynamic|| Yes|| Yes|| || || || riverctl|| wlroots|| ||
|-
! Sway
| C || Text || Dynamic(?) || Yes || Yes || Built-in (swaybar) || || || swaymsg || wlroots || ||
|-
! Velox
| C || Text || Dynamic ||  || || Built-in || || || || swc || ||
|-
|}
