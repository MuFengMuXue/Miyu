[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Fastfetch&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Package information](https://packages.gentoo.org/packages/app-misc/fastfetch)

[[]][GitHub](https://github.com/fastfetch-cli/fastfetch)

**Fastfetch** is a neofetch-like tool for fetching system information and displaying them in a pretty way. It is written mainly in C, with performance and customizability in mind.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Files]](#Files)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Invocation]](#Invocation)
-   [[4] [See also]](#See_also)

## [Installation]

### [USE flags]

### [USE flags for] [app-misc/fastfetch](https://packages.gentoo.org/packages/app-misc/fastfetch) [[]] [Fast neofetch-like system information tool]

  ------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`X`](https://packages.gentoo.org/useflags/X)                       Add support for X11
  [`chafa`](https://packages.gentoo.org/useflags/chafa)               Enables text/graphics renderer with media-gfx/chafa
  [`dbus`](https://packages.gentoo.org/useflags/dbus)                 Enable dbus support for anything that needs it (gpsd, gnomemeeting, etc)
  [`ddcutil`](https://packages.gentoo.org/useflags/ddcutil)           Use app-misc/ddcutil to query monitor settings
  [`drm`](https://packages.gentoo.org/useflags/drm)                   Enables support for X.org\'s x11-libs/libdrm
  [`efl`](https://packages.gentoo.org/useflags/efl)                   Enables Enlightenment support using dev-libs/efl
  [`elf`](https://packages.gentoo.org/useflags/elf)                   Use libelf to extract strings from binaries
  [`gnome`](https://packages.gentoo.org/useflags/gnome)               Add GNOME support
  [`imagemagick`](https://packages.gentoo.org/useflags/imagemagick)   Enable optional support for the ImageMagick or GraphicsMagick image converter
  [`opencl`](https://packages.gentoo.org/useflags/opencl)             Enable OpenCL support (computation on GPU)
  [`opengl`](https://packages.gentoo.org/useflags/opengl)             Add support for OpenGL (3D graphics)
  [`pulseaudio`](https://packages.gentoo.org/useflags/pulseaudio)     Add sound server support via media-libs/libpulse (may be PulseAudio or PipeWire)
  [`sqlite`](https://packages.gentoo.org/useflags/sqlite)             Add support for sqlite - embedded sql database
  [`test`](https://packages.gentoo.org/useflags/test)                 Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`vulkan`](https://packages.gentoo.org/useflags/vulkan)             Enables reading GPU via media-libs/vulkan-loader
  [`wayland`](https://packages.gentoo.org/useflags/wayland)           Enable dev-libs/wayland backend
  [`xcb`](https://packages.gentoo.org/useflags/xcb)                   Support the X C-language Binding, a replacement for Xlib
  [`xrandr`](https://packages.gentoo.org/useflags/xrandr)             Enables support for Xrandr
  ------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-14 15:43] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask app-misc/fastfetch`

## [Configuration]

### [Files]

** Important**\
Fastfetch\'s config language uses JSONC, not JSON! Make sure the file extension is **.jsonc**.

The simplest fastfetch `config.jsonc` looks like:

[FILE] **`~/.config/fastfetch/config.jsonc`**

    // ~/.config/fastfetch/config.jsonc


## [Usage]

You can see your system configuration by running:

`user `[`$`]`fastfetch`

### [Invocation]

`user `[`$`]`fastfetch --help`

    Fastfetch is a neofetch-like tool for fetching system information and displaying them in a pretty way

    Usage: fastfetch <?options>

    Informative options:
      -h, --help <?command>                      Show this message, or help for a specific command
      -v, --version                              Show the full version of fastfetch
          --version-raw                          Show the raw version string (major.minor.patch)
          --list-config-paths                    List search paths of config files
          --list-data-paths                      List search paths of presets and logos
          --list-logos                           List available logos
          --list-modules                         List available modules
          --list-presets                         List presets fastfetch knows about
          --list-features                        List the supported features fastfetch was compiled with
          --print-logos                          Print available logos
          --print-structure                      Print the default structure

    Config options:
      -c, --config <config>                      Specify the config file or preset to be loaded
          --gen-config <?path>                   Generate a config file to specified path with options specified in the command line (if any)
          --gen-config-force <?path>             Generate a config file to specified path. Overwrite the existing one

    pseudo options:
          --thread <?bool>                       Use separate threads to send HTTP requests
          --escape-bedrock <?bool>               On Bedrock Linux, whether to escape the bedrock jail
          --wmi-timeout <num>                    Set the timeout (ms) for WMI queries
          --processing-timeout <num>             Set the timeout (ms) when waiting for child processes
          --ds-force-drm <?bool>                 Set if only DRM should be used to detect displays

    Logo options:
      -l, --logo <logo>                          Set the logo source
          --logo-type <enum>                     Set the type of the logo given in "--logo"
          --logo-width <num>                     Set the width of the logo (in characters), if it is an image
          --logo-height <num>                    Set the height of the logo (in characters), if it is an image
          --logo-preserve-aspect-ratio <?bool>   Set if the logo should fill the specified width and height as much as possible without stretching
          --logo-color-[1-9] <color>             Overwrite a color in the logo
          --logo-padding <num>                   Set the padding on the left and the right of the logo
          --logo-padding-left <num>              Set the padding on the left of the logo
          --logo-padding-right <num>             Set the padding on the right of the logo
          --logo-padding-top <num>               Set the padding on the top of the logo
          --logo-print-remaining <?bool>         Whether to print the remaining logo, if it has more lines than modules to display
          --logo-separate <?bool>                If true, print modules at bottom of the logo
          --logo-recache <?bool>                 If true, regenerate image logo cache
          --file                           Short for --logo-type file --logo
          --file-raw                       Short for --logo-type file-raw --logo
          --data <data>                          Short for --logo-type data --logo <data>
          --data-raw <data>                      Short for --logo-type data-raw --logo <data>
          --raw                            Short for --logo-type raw --logo
          --sixel                          Short for --logo-type sixel --logo
          --kitty                          Short for --logo-type kitty --logo
          --kitty-direct                   Short for --logo-type kitty-direct --logo
          --iterm                          Short for --logo-type iterm --logo
          --chafa                          Short for --logo-type chafa --logo
          --chafa-fg-only <?bool>                Produce character-cell output using foreground colors only
          --chafa-symbols <str>                  Specify character symbols to employ in final output
          --chafa-canvas-mode <enum>             Determine how colors are used in the output
          --chafa-color-space <enum>             Set color space used for quantization
          --chafa-dither-mode <enum>             Set output dither mode (No effect with 24-bit color)

    Display options:
      -s, --structure <structure>                Set the structure of the fetch
          --stat <?bool>                         Show time usage (in ms) for individual modules
          --pipe <?bool>                         Disable logo and all escape sequences
          --color-keys <color>                   Set the color of the keys
          --color-title <color>                  Set the color of the title
          --color <color>                        Set the color of both the keys and title
          --key-width <num>                      Align the width of keys to <num> characters
          --bright-color <?bool>                 Set if the keys, title and ASCII logo should be printed in bright color
          --separator <str>                      Set the separator between key and value
          --set <key=value>                      Hard set the value of a key
          --set-keyless <key=value>              Hard set the value of a key, but don't print the key or the separator
          --show-errors <?bool>                  Print occurring errors
          --disable-linewrap <?bool>             Whether to disable line wrap during the run
          --hide-cursor <?bool>                  Whether to hide the cursor during the run
          --binary-prefix <enum>                 Set the binary prefix to used
          --percent-type <num>                   Set the percentage output type
          --percent-ndigits <num>                Set the number of digits to keep after the decimal point when formatting percentage numbers
          --bar-char-elapsed <str>               Set the character to use in elapsed part of percentage bars
          --bar-char-total <str>                 Set the character to use in total part of percentage bars
          --bar-width <num>                      Set the width of percentage bars, in number of characters
          --bar-border <?bool>                   Whether to show a border around percentage bars
          --no-buffer <?bool>                    Set if the stdout application buffer should be disabled
          --size-ndigits <num>                   Set the number of digits to keep after the decimal point when formatting sizes
          --size-max-prefix <enum>               Set the largest binary prefix to use when formatting sizes
          --temperature-unit <enum>              Set the unit of the temperature

    Library path options:
          --lib-pci                        Pciutils. Used for GPU output
          --lib-vulkan                     Vulkan module & fallback for GPU output
          --lib-wayland                    Better display performance and output in wayland sessions
          --lib-xcb-randr                  X11 sessions for better display detection and faster WM detection
          --lib-xcb                        X11 sessions for better display detection and faster WM detection
          --lib-xrandr                     X11 sessions for better display detection and faster WM detection
          --lib-x11                        X11 sessions for better display detection and faster WM detection
          --lib-drm                        Used for fast resolution and refresh rate detection
          --lib-gio                        Needed for values that are only stored GSettings
          --lib-dconf                      Needed for values that are only stored in DConf + Fallback for GSettings
          --lib-dbus                       Bluetooth, Player & Media detection
          --lib-xfconf                     Needed for XFWM theme and XFCE Terminal font
          --lib-sqlite3                    Needed for pkg & rpm package count
          --lib-rpm                        Slower fallback for rpm package count
          --lib-imagemagick                Images in terminal using sixel or kitty graphics protocol
          --lib-z                          Libz. Faster image output when using kitty graphics protocol
          --lib-chafa                      Image output as ascii art
          --lib-egl                        Needed by the OpenGL module for gl context creation
          --lib-glx                        Needed by the OpenGL module for gl context creation
          --lib-osmesa                     Needed by the OpenGL module for gl context creation
          --lib-opencl                     OpenCL module
          --lib-pulse                      Pulseaudio. Used for Sound detection
          --lib-nm                         NetworkManager. Used for Wifi detection
          --lib-freetype                   Used for Termux font detection
          --lib-ddcutil                    Used for brightness detection of external displays

    Module specific options:
          --title-fqdn <?bool>                   Set if the title should use fully qualified domain name
          --title-color-user <color>             Set color of the user name (left part)
          --title-color-at <color>               Set color of the @ symbol (middle part)
          --title-color-host <color>             Set color of the host name (right part)
          --chassis-use-wmi <?bool>              Set if WMI query should be used on Windows
          --separator-string <str>               Set the string printed by the separator module
          --os-file                        Set the additional file path which containing OS information
          --disk-folders                   A colon (semicolon on Windows) separated list of folder paths for the disk output
          --disk-show-regular <?bool>            Set if regular volume should be printed
          --disk-show-external <?bool>           Set if external volume should be printed
          --disk-show-hidden <?bool>             Set if hidden volumes should be printed
          --disk-show-subvolumes <?bool>         Set if subvolumes should be printed
          --disk-show-readonly <?bool>           Set if read only volumes should be printed
          --disk-show-unknown <?bool>            Set if unknown (unable to detect sizes) volumes should be printed
          --disk-use-available <?bool>           Use f_bavail (lpFreeBytesAvailableToCaller for Windows) instead of f_bfree to calculate used bytes
          --diskio-name-prefix <str>             Show disks with given name prefix only
          --bluetooth-show-disconnected <?bool>  Set if disconnected bluetooth devices should be printed
          --packages-winget <?bool>              Set if winget package count should be detected
          --display-compact-type <enum>          Set if all displays should be printed in one line
          --display-precise-refresh-rate <?bool> Set if decimal refresh rates should not be rounded into integers when printing
          --brightness-ddcci-sleep <num>         Set the sleep times (in ms) when sending DDC/CI requests
          --sound-type <enum>                    Set what type of sound devices should be printed
          --battery-dir                    The directory where the battery folders are
          --battery-use-setup-api <?bool>        Set if "SetupAPI" should be used on Windows to detect battery info
          --cpu-temp <?bool>                     Detect and display CPU temperature if supported
          --cpu-freq-ndigits <num>               Set the number of digits to keep after the decimal point when printing CPU frequency
          --cpuusage-separate <?bool>            Display CPU usage per CPU logical core, instead of an average result
          --de-slow-version-detection <?bool>    Set if DE version should be detected with slow operations
          --gpu-temp <?bool>                     Detect and display GPU temperature if supported
          --gpu-use-nvml <?bool>                 Use nvml (NVIDIA Management Library) to detect more detailed GPU information
          --gpu-force-vulkan <?bool>             Force using vulkan to detect GPUs
          --gpu-hide-type <enum>                 Specify the type of GPUs should not be printed
          --battery-temp <?bool>                 Detect and display Battery temperature if supported
          --localip-show-ipv4 <?bool>            Show IPv4 addresses in local ip module
          --localip-show-ipv6 <?bool>            Show IPv6 addresses in local ip module
          --localip-show-mac <?bool>             Show mac addresses in local ip module
          --localip-show-loop <?bool>            Show loop back addresses (127.0.0.1) in local ip module
          --localip-name-prefix <str>            Show interfaces with given interface name prefix only
          --localip-default-route-only <?bool>   Show the interface that is used for default routing only
          --localip-compact <?bool>              Show all IPs in one line
          --netio-name-prefix <str>              Show interfaces with given name prefix only
          --netio-default-route-only <?bool>     Show the interfac that is used for default routing only
          --publicip-timeout <num>               Time in milliseconds to wait for the public ip server to respond
          --publicip-url <str>                   The URL of public IP detection server to be used
          --weather-location <str>               Set the location to be used
          --weather-timeout <num>                Time in milliseconds to wait for the weather server to respond
          --weather-output-format <str>          The output weather format to be used
          --wm-detect-plugin <?bool>             Set if window manager plugin should be detected on supported platforms
          --player-name <str>                    The name of the player to use for module Media and Player
          --opengl-library <enum>                Set the OpenGL context creation library to use
          --command-shell <str>                  Set the shell program to execute the command text
          --command-key <str>                    Set the module key to display
          --command-text <str>                   Set the command text to be executed
          --colors-symbol <enum>                 Set the symbol to be printed by Colors module
          --colors-padding-left <num>            Set the number of white spaces to print before the symbol

    General module options:
          --<module>-format <format>             Set the format string to use for each specific module
                                                 To see how a format string works, use "fastfetch -h format".
                                                 To see help about a specific format string, use "fastfetch -h <module>-format"
          --<module>-key <key>                   Set the key to use for each specific module.
                                                 For modules which print multiple lines, the string is parsed
                                                 as a format string with the index as first character
          --<module>-key-color <color>           Override the global "--color-keys" option for each specific module
          --<module>-key-width <num>             Override the global "--key-width" option for each specific module

    Parsing is not case sensitive. E.g. "--lib-PCI" is equal to "--Lib-Pci"
    If a value starts with a ?, it is optional. An optional boolean value defaults to true if not specified.
    More detailed help messages for each options can be printed with "-h <option_without_dash_prefix>"
    All options can be made permanent with command "fastfetch <options> --gen-config"

## [See also]

-   [neofetch](https://wiki.gentoo.org/wiki/Neofetch "Neofetch") --- a command-line system information tool that displays information about the operating system, software, and hardware in an aesthetic and visually pleasing way.