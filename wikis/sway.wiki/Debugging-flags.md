Sway has some debugging options available via the `-D` command-line flag.

- `-D noatomic`: disables atomic transactions
- `-D txn-wait`: forces all atomic transactions to time out
- `-D txn-timings`: logs addition information about transaction timings
- `-D txn-timeout=<ms>`: overrides the default atomic transaction timeout
- `-D legacy-wl-drm`: enables the legacy `wl_drm` protocol extension (Sway 1.10 and later)

Also see `enable_debug_flag()`.

On Sway ≤ 1.9, the following flags are also supported:

- `-D damage=highlight`: paints regions that haven't been updated in yellow (replaced by `WLR_SCENE_DEBUG_DAMAGE=highlight` on Sway 1.10)
- `-D damage=rerender`: disables damage tracking by forcing the whole output to be repainted each frame (replaced by `WLR_SCENE_DEBUG_DAMAGE=rerender` on Sway 1.10)
- `-D noscanout`: disables direct scan-out (replaced by `WLR_SCENE_DISABLE_DIRECT_SCANOUT=1` on Sway 1.10)