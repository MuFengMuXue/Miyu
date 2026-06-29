# GameMode
**GameMode** is a daemon/lib combo for Linux that allows games to request a set of optimisations be temporarily applied to the host OS and/or a game process.

GameMode was designed primarily as a stop-gap solution to problems with the Intel and AMD CPU powersave or ondemand governors, but is now host to a range of optimisation features and configurations.

Currently GameMode includes support for optimisations including:
* CPU governor
* I/O priority
* Process niceness
* Kernel scheduler (`SCHED_ISO`)
* Screensaver inhibiting
* GPU performance mode (NVIDIA and AMD), GPU overclocking (NVIDIA)
* CPU core pinning or parking
* Custom scripts

GameMode packages are available for Ubuntu, Debian, Solus, Arch, Gentoo, Fedora, OpenSUSE, Mageia and possibly more.

---
## Requesting GameMode

For games/launchers which integrate GameMode support, simply running the game will automatically activate GameMode.

For others, you must manually request GameMode when running the game. This can be done by launching the game through `gamemoderun`:

``` bash
gamemoderun ./game
```
Or edit the Steam launch options:
``` bash
gamemoderun %command%
```

Note: for older versions of GameMode (before 1.3) use this string in place of `gamemoderun`:
```
LD_PRELOAD="$LD_PRELOAD:/usr/\$LIB/libgamemodeauto.so.0"
```
**Please note the backslash here in `\$LIB` is required.**

---
## Configuration

The daemon is configured with a `gamemode.ini` file. [example/gamemode.ini](configuration.md) is an example of what this file would look like, with explanations for all the variables.

Configuration files are loaded and merged from the following directories, from highest to lowest priority:

1. `$PWD`("unsafe" - **`[gpu]` settings take no effect in this file**)
2. `$XDG_CONFIG_HOME` or `$HOME/.config/`("unsafe" - **`[gpu]` settings take no effect in this file**)
3. `/etc/`
4. `/usr/share/gamemode/`

---
## Note for Hybrid GPU users

It's not possible to integrate commands like optirun automatically inside GameMode, since the GameMode request is made once the game has already started. However it is possible to use a hybrid GPU wrapper like optirun by starting the game with `gamemoderun`.

You can do this by setting the environment variable `GAMEMODERUNEXEC` to your wrapper's launch command, so for example `GAMEMODERUNEXEC=optirun`,`GAMEMODERUNEXEC="env DRI_PRIME=1"`, or `GAMEMODERUNEXEC="env __NV_PRIME_RENDER_OFFLOAD=1 __GLX_VENDOR_LIBRARY_NAME=nvidia __VK_LAYER_NV_optimus=NVIDIA_only"`. This environment variable can be set globally (e.g. in /etc/environment), so that the same prefix command does not have to be duplicated everywhere you want to use `gamemoderun`.

GameMode will not be injected to the wrapper.
