[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Btop&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Package information](https://packages.gentoo.org/packages/sys-process/btop)

[[]][GitHub](https://github.com/aristocratos/btop)

**btop** is a resource monitor that shows usage and stats for processor, memory, disks, network and processes. It is the third iteration of [bpytop](https://wiki.gentoo.org/wiki/Bpytop "Bpytop") and [bashtop](https://wiki.gentoo.org/wiki/Bashtop "Bashtop").

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Invocation]](#Invocation)
-   [[3] [GPU monitoring]](#GPU_monitoring)
    -   [[3.1] [Intel GPU]](#Intel_GPU)
    -   [[3.2] [AMD GPU]](#AMD_GPU)
    -   [[3.3] [NVIDIA GPU]](#NVIDIA_GPU)
-   [[4] [See also]](#See_also)

## [Installation]

### [Emerge]

`root `[`#`]`emerge --ask sys-process/btop`

## [Usage]

To start btop, you can run

`user `[`$`]`btop`

### [Invocation]

`user `[`$`]`btop --help`

    usage: btop [-h] [-v] [-/+t] [-p <id>] [--utf-force] [--debug]

    optional arguments:
      -h, --help            show this help message and exit
      -v, --version         show version info and exit
      -lc, --low-color      disable truecolor, converts 24-bit colors to 256-color
      -t, --tty_on          force (ON) tty mode, max 16 colors and tty friendly graph symbols
      +t, --tty_off         force (OFF) tty mode
      -p, --preset <id>     start with preset, integer value between 0-9
      --utf-force           force start even if no UTF-8 locale was detected
      --debug               start in DEBUG mode: shows microsecond timer for information collect
                            and screen draw functions and sets loglevel to DEBUG

## [GPU monitoring]

### [Intel GPU]

To monitor an Intel GPU without requiring elevated privileges, grant [btop] the required [CAP_PERFMON] capability using [setcap].

`root `[`#`]`` setcap cap_perfmon=+ep `readlink -f "$(command -v btop)"`  ``

### [AMD GPU]

For monitoring an AMD GPU using btop, install the ROCm SMI library.

`user `[`$`]`emerge --ask dev-util/rocm-smi `

Once ROCm SMI is installed, btop can monitor GPU usage, VRAM usage, clocks, and temperature.

### [NVIDIA GPU]

NVIDIA GPU monitoring should work out of the box with [btop] as long as the official NVIDIA drivers are installed (both closed and open kernel modules). No extra configuration is required.

## [See also]

-   [htop](https://wiki.gentoo.org/wiki/Htop "Htop") --- a cross-platform interactive process viewer. It is a text-mode application (for console or X terminals) and requires ncurses.
-   [Recommended tools](https://wiki.gentoo.org/wiki/Recommended_tools "Recommended tools") --- lists system-administration related tools recommended for use in a **[shell](https://wiki.gentoo.org/wiki/Shell "Shell") environment** ([terminal/console](https://wiki.gentoo.org/wiki/Terminal_emulator "Terminal emulator"))