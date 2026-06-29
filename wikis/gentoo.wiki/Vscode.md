\

[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Vscode&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://visualstudio.microsoft.com)

[[]][Package information](https://packages.gentoo.org/packages/app-editors/vscode)

[[]][GitHub](https://github.com/microsoft/vscode)

**VS Code** or **Visual Studio Code** is a lightweight but powerful source code editor which runs on the desktop, and is available for Windows, macOS, and Linux.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Before Installation]](#Before_Installation)
    -   [[1.3] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Invocation]](#Invocation)
-   [[3] [Tips]](#Tips)
    -   [[3.1] [Disable Telemetry]](#Disable_Telemetry)
-   [[4] [Troubleshooting]](#Troubleshooting)
    -   [[4.1] [Login with GitHub doesn\'t work]](#Login_with_GitHub_doesn.27t_work)
    -   [[4.2] [Very high CPU usage]](#Very_high_CPU_usage)
-   [[5] [See also]](#See_also)

## [Installation]

### [USE flags]

### [USE flags for] [app-editors/vscode](https://packages.gentoo.org/packages/app-editors/vscode) [[]] [Multiplatform Visual Studio Code from Microsoft]

  ------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------
  [`egl`](https://packages.gentoo.org/useflags/egl)             Use EGL platform, enables smooth rendering in high refresh rate monitors on X11/Xwayland
  [`kerberos`](https://packages.gentoo.org/useflags/kerberos)   Add kerberos support
  [`wayland`](https://packages.gentoo.org/useflags/wayland)     Run in wayland mode under wayland sessions, xwayland otherwise. This flag doesn\'t affect x11 sessions.
  [`webkit`](https://packages.gentoo.org/useflags/webkit)       Enable extensions that require WebKit (e.g., Microsoft authentication).
  ------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-22 04:24] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Before Installation]

** Warning**\
Microsoft Visual Studio Code uses telemetry (record some aspects of usage, machine, etc., and send this data back to Microsoft). Understand this before accepting the EULA and unmasking the package, otherwise install the free/libre version [[[app-editors/vscodium]](https://packages.gentoo.org/packages/app-editors/vscodium)[]].

In order to install VS Code the user needs to accept the *Microsoft-vscode* license agreement. A copy of the license can be found at [/var/db/repos/gentoo/licenses/Microsoft-vscode]. Read with:

`user `[`$`]`less /var/db/repos/gentoo/licenses/Microsoft-vscode`

And to agree:

`root `[`#`]`echo "app-editors/vscode Microsoft-vscode" >> /etc/portage/package.license`

To prefer the free/libre version of VS Code, install VSCodium with the package [[[app-editors/vscodium]](https://packages.gentoo.org/packages/app-editors/vscodium)[]], which completely removes telemetry. To learn the differences, [read the upstream documentation](https://github.com/VSCodium/vscodium/blob/master/docs/index.md#extensions-marketplace).

** Note**\
VSCodium has no telemetry but has a limited number of extensions because of the VS Code Marketplace [Terms of Use](https://aka.ms/vsmarketplace-ToU). For this reason it uses [open-vsx.org](https://open-vsx.org), an open source registry for VS Code extensions.

### [Emerge]

Emerge Microsoft\'s release with:

`root `[`#`]`emerge --ask app-editors/vscode`

Or emerge the free/libre release with:

`root `[`#`]`emerge --ask app-editors/vscodium`

## [Usage]

Depending on the version installed, run VS Code with:

`user `[`$`]`vscode`

Or:

`user `[`$`]`vscodium`

### [Invocation]

`user `[`$`]`vscode --help`

    Visual Studio Code _Version_here_

    Usage: code [options][paths...]

    To read from stdin, append '-' (e.g. 'ps aux | grep code | code -')

    Options
      -d --diff <file> <file>           Compare two files with each other.
      -a --add <folder>                 Add folder(s) to the last active window.
      -g --goto <file:line[:character]> Open a file at the path on the specified
                                        line and character position.
      -n --new-window                   Force to open a new window.
      -r --reuse-window                 Force to open a file or folder in an
                                        already opened window.
      -w --wait                         Wait for the files to be closed before
                                        returning.
      --locale <locale>                 The locale to use (e.g. en-US or zh-TW).
      --user-data-dir <dir>             Specifies the directory that user data is
                                        kept in. Can be used to open multiple
                                        distinct instances of Code.
      -h --help                         Print usage.

    Extensions Management
      --extensions-dir <dir>
          Set the root path for extensions.
      --list-extensions
          List the installed extensions.
      --show-versions
          Show versions of installed extensions, when using --list-extensions.
      --category <category>
          Filters installed extensions by provided category, when using --list-extensions.
      --install-extension <extension-id[@version] | path-to-vsix>
          Installs or updates the extension. The identifier of an extension is always `$.$`. Use `--force` argument to update to latest version. To install a
    specific version provide `@$`. For example: 'vscode.csharp@1.2.3'.
      --pre-release
          Installs the pre-release version of the extension, when using --install-extension
      --uninstall-extension <extension-id>
          Uninstalls an extension.
      --enable-proposed-api <extension-id>
          Enables proposed API features for extensions. Can receive one or more extension IDs to enable individually.

    Troubleshooting
      -v --version                       Print version.
      --verbose                          Print verbose output (implies --wait).
      --log <level>                      Log level to use. Default is 'info'.
                                         Allowed values are 'critical', 'error',
                                         'warn', 'info', 'debug', 'trace', 'off'.
      -s --status                        Print process usage and diagnostics
                                         information.
      --prof-startup                     Run CPU profiler during startup.
      --disable-extensions               Disable all installed extensions.
      --disable-extension <extension-id> Disable an extension.
      --sync <on> <off>                  Turn sync on or off.
      --inspect-extensions         Allow debugging and profiling of
                                         extensions. Check the developer tools for
                                         the connection URI.
      --inspect-brk-extensions     Allow debugging and profiling of
                                         extensions with the extension host being
                                         paused after start. Check the developer
                                         tools for the connection URI.
      --disable-gpu                      Disable GPU hardware acceleration.
      --max-memory <memory>              Max memory size for a window (in Mbytes).
      --telemetry                        Shows all telemetry events which VS code
                                         collects.

## [Tips]

### [Disable Telemetry]

See [information on how to change or completely disable](https://code.visualstudio.com/docs/getstarted/telemetry#_disable-telemetry-reporting) telemetry on VS Code. Read the full page to understand telemetry, data protection, and privacy.

## [Troubleshooting]

### [][Login with GitHub doesn\'t work]

Writing login information to the keychain failed with error: *Object does not exist at path \"/org/freedesktop/secrets/collection/login\"*. On [systemd](https://wiki.gentoo.org/wiki/Systemd "Systemd") systems: add this line to the WM init file:[\[1\]](https://code.visualstudio.com/docs/editor/settings-sync#_linux)

`user `[`$`]`source /etc/X11/xinit/xinitrc.d/50-systemd-user.sh`

On [OpenRC](https://wiki.gentoo.org/wiki/OpenRC "OpenRC") systems, run this program before starting VSCode or add it to WM init file:[\[2\]](https://forums.gentoo.org/viewtopic-t-1149647-start-0-postdays-0-postorder-asc-highlight-.html)

`user `[`$`]`dbus-update-activation-environment --all`

### [Very high CPU usage]

VS Code could spawn a process called [rg] and cause huge stress for the CPU. A workaround can be done by setting the \"search.followSymlinks\" option to false in the options panel, following issue [https://github.com/microsoft/vscode/issues/98594#issuecomment-643871783](https://github.com/microsoft/vscode/issues/98594#issuecomment-643871783).

## [See also]

-   [Text editor](https://wiki.gentoo.org/wiki/Text_editor "Text editor") --- a program to create and edit text files.