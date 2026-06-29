**Resources**

[[]][Home](https://flameshot.org/)

[[]][Official documentation](https://flameshot.org/docs/overview/overview/)

[[]][Package information](https://packages.gentoo.org/packages/media-gfx/flameshot)

[[]][GitHub](https://github.com/flameshot-org/flameshot)

**Flameshot** is a powerful, simple to use screenshot software that includes in-place editing capabilities, support of various shortcuts, and multiple other configuration options.

It is written in C++, can be used via a CLI or GUI, and has multiple interactive editing options of screenshots and custom output destination (save, upload, copy to clipboard, open with other software).

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [GUI]](#GUI)
    -   [[2.2] [Command line interface]](#Command_line_interface)
    -   [[2.3] [Configuration file]](#Configuration_file)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Arguments]](#Arguments)
    -   [[3.2] [Keyboard shortcuts]](#Keyboard_shortcuts)
    -   [[3.3] [Shortcuts for taking screenshots]](#Shortcuts_for_taking_screenshots)
-   [[4] [Troubleshooting]](#Troubleshooting)
    -   [[4.1] [Flameshot does not start and / or GUI does not open on a minimal window manager]](#Flameshot_does_not_start_and_.2F_or_GUI_does_not_open_on_a_minimal_window_manager)
    -   [[4.2] [Flameshot does not start on a Wayland Compositor]](#Flameshot_does_not_start_on_a_Wayland_Compositor)
    -   [[4.3] [GNOME Wayland and Plasma Wayland]](#GNOME_Wayland_and_Plasma_Wayland)
    -   [[4.4] [No tray icon on GNOME]](#No_tray_icon_on_GNOME)
    -   [[4.5] [Other]](#Other)
-   [[5] [External resources]](#External_resources)
-   [[6] [References]](#References)

## [Installation]

### [Emerge]

Emerge [[[media-gfx/flameshot]](https://packages.gentoo.org/packages/media-gfx/flameshot)[]]:

`root `[`#`]`emerge --ask media-gfx/flameshot`

Note: there are currently no specific USE flags for the package.

## [Configuration]

Flameshot can be configured by using the GUI, the CLI, or by modifying the configuration file.

Without configuration, Flameshot will run with the default settings.

### [GUI]

To configure with GUI, the following command can be used:

`user `[`$`]`flameshot config`

If changes are made for the first time in the GUI settings, they will also be applied to the configuration file in [\~/.config/flameshot/flameshot.ini].

In order for changes to be written to the configuration file, modifications to that specific option must be made. Otherwise, if the default option is unchanged, there will be nothing written into the configuration file.

### [Command line interface]

The following syntax can be used for configurations with CLI:

`user `[`$`]`flameshot config [config-options]`

The available options for CLI configuration can be found by referring to the help pages or the [man pages](https://wiki.gentoo.org/wiki/Man_page "Man page"):

`user `[`$`]`flameshot config --help`

`user `[`$`]`man flameshot`

Checking for mistakes or issues related to the configuration file can be done with the `--check` option:

`user `[`$`]`flameshot config --check`

### [Configuration file]

Some of the settings, can also be done by editing the configuration file. On Linux the configuration file can be found in [\~/.config/flameshot/flameshot.ini].

The configuration file could look like this, please note that this is only an example with only a small set of available configurations and every time a change is made to a setting through the GUI, the new value will be written here:

[FILE] **`~/.config/flameshot/flameshot.ini`**

    [General]
    allowMultipleGuiInstances=true
    contrastOpacity=188
    copyPathAfterSave=true
    disabledTrayIcon=true
    savePath=the/configured/path/to/save/screenshots
    showDesktopNotification=false
    showStartupLaunchMessage=true
    uiColor=#960090

It is also possible to make changes to the configuration file directly, which will be immediately applied. This makes it possible, to modify Flameshot settings through the use of scripts and automate the process of screenshots taking. For more, see usage section.

Furthermore, please note that it is possible to use the same configuration file for Windows systems (and reverse).

To accomplish this the `savePath` variable in the [flameshot.ini] have to be adjusted to the new correct save path to meet the DOS / UNIX directory structure.

Additionally the [flameshot.ini] has to be moved to [%appdata%\\flameshot\\flameshot.ini].

## [Usage]

When executed without parameters, the [flameshot] command will start a running instance of the program in the background without taking any actions. If the system has tray icon support, a flameshot tray icon for further interaction and information will appear.

### [Arguments]

Some key arguments for taking screenshots are:

Capture with GUI tool:

`user `[`$`]`flameshot gui`

The GUI tool provides the possibility to edit the taken screenshot in-place, to copy it with Ctrl+C directly to clipboard, adding text, correction of the capturing area, resizing, and a lot more of intuitive usable features.

Capture full screen:

`user `[`$`]`flameshot full`

Capture specific screen:

`user `[`$`]`flameshot screen -n <screen number integer>`

Further arguments are available:

`-p` to specify a custom save path

`user `[`$`]`flameshot gui -p ~/myStuff/captures`

`-d` to define a delay in milliseconds

`user `[`$`]`flameshot gui -d 2000`

`-c` to copy directly to clipboard

`user `[`$`]`flameshot full -c -p ~/myStuff/captures`

For more arguments and additional information please refer to the documentation, the [README.md](https://github.com/flameshot-org/flameshot) and the man pages.

### [Keyboard shortcuts]

This is a a list from the original [README.md]^[\[1\]](#cite_note-1)^ of available shortcuts in GUI mode:

  --------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------
  Keys                                                                        Description
  [P]                                                                   Set the Pencil as paint tool
  [D]                                                                   Set the Line as paint tool
  [A]                                                                   Set the Arrow as paint tool
  [S]                                                                   Set Selection as paint tool
  [R]                                                                   Set the Rectangle as paint tool
  [C]                                                                   Set the Circle as paint tool
  [M]                                                                   Set the Marker as paint tool
  [T]                                                                   Add text to the capture
  [B]                                                                   Set Pixelate as the paint tool
  [←], [↓], [↑], [→]                                  Move selection 1px
  [Shift] + [←], [↓], [↑], [→]                  Resize selection 1px
  [Ctrl] + [Shift] + [←], [↓], [↑], [→]   Symmetrically resize selection 2px
  [Esc]                                                                 Quit capture
  [Ctrl] + [M]                                                    Move the selection area
  [Ctrl] + [C]                                                    Copy to clipboard
  [Ctrl] + [S]                                                    Save selection as a file
  [Ctrl] + [Z]                                                    Undo the last modification
  [Ctrl] + [Shift] + [Z]                                    Redo the next modification
  [Ctrl] + [Q]                                                    Leave the capture screen
  [Ctrl] + [O]                                                    Choose an app to open the capture
  [Ctrl] + [Return]                                               Commit text in text area
  [Return]                                                              Upload the selection to Imgur
  [Spacebar]                                                            Toggle visibility of sidebar with options of the selected tool, color picker for the drawing color and history menu
  Right Click                                                                 Show the color wheel
  Mouse Wheel                                                                 Change the tool\'s thickness
  [Print screen]                                                        Capture Screen
  [Shift] + [Print]                                               Screenshot History
  [Ctrl] + drawing *line*, *arrow* or *marker*                          Drawing only horizontally, vertically or diagonally
  [Ctrl] + drawing *rectangle* or *circle*                              Keeping aspect ratio
  --------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------

[Shift] + drag a handler of the selection area: mirror redimension in the opposite handler.

### [Shortcuts for taking screenshots]

If shortcuts for screenshots are desired, they must be manually enabled. This is done by setting one or more of the desired command-line options from the Usage section as commands for specific key combinations on the system. (For example [flameshot gui])

Since these settings can be achieved in different ways across different desktop environments, window managers, and system settings it is recommended to check the related [Gentoo Desktop Environment Wiki Section](https://wiki.gentoo.org/wiki/Desktop_environment "Desktop environment") of the installed desktop environment or the [Window Manager Section](https://wiki.gentoo.org/wiki/Window_manager "Window manager") if using a minimal Window manager system or to refer to the documentation of the used interface, to find out how to set up custom shortcuts.

For KDE Plasma and XFCE there is a description in the [README on github](https://github.com/flameshot-org/flameshot#global), how to achieve this.

## [Troubleshooting]

### [][Flameshot does not start and / or GUI does not open on a minimal window manager]

Flameshot works the best with dbus, so make the session dbus aware. Refer to [Window Manager](https://wiki.gentoo.org/wiki/Window_manager "Window manager"). For example for i3:

[FILE] **`~/.xinitrc`**

    exec dbus-launch --exit-with-session i3

### [Flameshot does not start on a Wayland Compositor]

Flameshot requires some packages to be installed in order to work properly with Wayland compositors.

`root `[`#`]`emerge --ask sys-apps/xdg-desktop-portal gui-apps/grim sys-apps/xdg-desktop-portal-gtk`

-   The [[[sys-apps/xdg-desktop-portal]](https://packages.gentoo.org/packages/sys-apps/xdg-desktop-portal)[]] is required for desktop integration with backend implementations.
-   Flameshot uses [[[gui-apps/grim]](https://packages.gentoo.org/packages/gui-apps/grim)[]] to grab images from a Wayland compositor.
-   You will probably need [[[sys-apps/xdg-desktop-portal-gtk]](https://packages.gentoo.org/packages/sys-apps/xdg-desktop-portal-gtk)[]] for the Access Dialog to ask for screenshot permission. If there is no portal that supports the Access interface, Flameshot will just wait without showing any output or errors.

Additionally, you will also need to make sure that you have installed one or more backends implementations that are appropriate for your environment (e.g. [[[gui-libs/xdg-desktop-portal-wlr]](https://packages.gentoo.org/packages/gui-libs/xdg-desktop-portal-wlr)[]]). For more details, check out [XDG/xdg-desktop-portal](https://wiki.gentoo.org/wiki/XDG/xdg-desktop-portal "XDG/xdg-desktop-portal").

### [GNOME Wayland and Plasma Wayland]

The Support on GNOME Wayland and Plasma Wayland is still Experimental.

### [No tray icon on GNOME]

The [[[gnome-extra/gnome-shell-extension-appindicator]](https://packages.gentoo.org/packages/gnome-extra/gnome-shell-extension-appindicator)[]] extension is necessary to see the system tray icon.

### [Other]

See [Flameshot Troubleshooting](https://flameshot.org/docs/guide/troubleshooting/) section

## [External resources]

-   [Flameshot Github](https://github.com/flameshot-org/flameshot)
-   [Official Flameshot Documentation](https://flameshot.org/docs/)
-   [Troubleshooting Flameshot Website](https://flameshot.org/docs/guide/troubleshooting/)

## [References]

1.  [[[↑](#cite_ref-1)] [[https://github.com/flameshot-org/flameshot](https://github.com/flameshot-org/flameshot)]]