This page contains [[changes](https://wiki.gentoo.org/index.php?title=Labwc&diff=1435633)] which are not marked for translation.

**Resources**

[[]][Home](https://github.com/labwc/labwc)

**Labwc** is a stacking [wlroots](https://wiki.gentoo.org/wiki/Wlroots "Wlroots")-based [Wayland compositor](https://wiki.gentoo.org/wiki/Wayland_compositor "Wayland compositor"), inspired by [Openbox](https://wiki.gentoo.org/wiki/Openbox "Openbox").

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
-   [[2] [Starting]](#Starting)
-   [[3] [Configuration files]](#Configuration_files)
    -   [[3.1] [autostart]](#autostart)
    -   [[3.2] [environment]](#environment)
    -   [[3.3] [menu.xml]](#menu.xml)
    -   [[3.4] [rc.xml]](#rc.xml)
        -   [[3.4.1] [Example content]](#Example_content)
    -   [[3.5] [shutdown]](#shutdown)
    -   [[3.6] [Menu generators]](#Menu_generators)
    -   [[3.7] [Themes]](#Themes)

## [Installation]

`root `[`#`]`emerge --ask gui-wm/labwc`

### [USE flags]

### [USE flags for] [gui-wm/labwc](https://packages.gentoo.org/packages/gui-wm/labwc) [[]] [Openbox alternative for wayland]

  ------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`X`](https://packages.gentoo.org/useflags/X)           Add support for X11
  [`icons`](https://packages.gentoo.org/useflags/icons)   Add support for window icons. Icons will only be displayed with USE=svg enabled
  [`nls`](https://packages.gentoo.org/useflags/nls)       Add Native Language Support (using gettext - GNU locale utilities)
  [`svg`](https://packages.gentoo.org/useflags/svg)       Add support for SVG (Scalable Vector Graphics)
  [`test`](https://packages.gentoo.org/useflags/test)     Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  ------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-04-19 17:07] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

## [Starting]

Labwc can be started via a terminal or a [display manager](https://wiki.gentoo.org/wiki/Display_manager "Display manager").

To start it from a terminal:

`user `[`$`]`dbus-run-session labwc`

For [display managers](https://wiki.gentoo.org/wiki/Display_manager "Display manager") that utilise [.desktop] files, a [labwc.desktop] file is installed in [/usr/share/wayland-sessions].

For login managers like [greetd](https://wiki.gentoo.org/wiki/Greetd "Greetd"), a suitable startup script can be produced and the relevant entry added to [/etc/greetd/environments/].

## [Configuration files]

The configuration of Labwc aligns with [Openbox](https://wiki.gentoo.org/wiki/Openbox "Openbox") in order to avoid reinventing configuration and theme syntaxes; the Openbox 3.6 specification is used. This does not mean that Labwc is an Openbox clone, but rather that configuration files will look and feel familiar.

There are five configuration files:

-   [[autostart]](#autostart)
-   [[environment]](#environment)
-   [[menu.xml]](#menu.xml)
-   [[rc.xml]](#rc.xml)
-   [[shutdown]](#shutdown)

[\~/.config/labwc/] is used to store the user-specific custom version of these files, though it needs to be created and populated.

For example:

`user `[`$`]`mkdir -p ~/.config/labwc/ `

`user `[`$`]`bzcat /usr/share/doc/labwc-$(labwc -v | cut -d " " -f 2)/labwc/rc.xml.all.bz2 > ~/.config/labwc/rc.xml `

`user `[`$`]`bzcat /usr/share/doc/labwc-$(labwc -v | cut -d " " -f 2)/labwc/menu.xml.bz2 > ~/.config/labwc/menu.xml `

`user `[`$`]`vim ~/.config/labwc/autostart`

### [autostart]

The [autostart] script is the place to execute specific commands and programs when Labwc starts. It makes no difference if Labwc is started via a terminal or a display manager; [autostart] will be executed either way.

[FILE] **`~/.config/labwc/autostart`Labwc autostart example**

    # start pipewire sound service
    gentoo-pipewire-launcher restart &

    # ensure relevant portals are launched
    /usr/libexec/xdg-desktop-portal-gtk -r &
    /usr/libexec/xdg-document-portal -r &
    /usr/libexec/flatpak-portal --no-idle-exit -r &
    sh -c 'sleep 5;exec /usr/libexec/xdg-desktop-portal -r' &
    sh -c 'sleep 5;exec /usr/libexec/xdg-desktop-portal-wlr -r' &

    # set a wallpaper
    swaybg  -i ~/Pictures/wallpaper-WoT.jpg -m fill &

    # additional Wayland helpers
    mako &
    waybar &

    # any other useful commands
    xhost +SI:localuser:$(id -un) &
    xhost +SI:localuser:root &
    discord --enable-features=UseOzonePlatform --ozone-platform=wayland &
    thunar --daemon &
    flatpak run com.valvesoftware.Steam -console -silent &

### [environment]

The [environment] script is the place to export global variables and configure the Labwc environment.

[FILE] **`~/.config/labwc/environment`Labwc environment example**

    XKB_DEFAULT_LAYOUT=gb

    QT_WAYLAND_DISABLE_WINDOWDECORATION=1
    QT_AUTO_SCREEN_SCALE_FACTOR=1
    QT_QPA_PLATFORMTHEME=qt5ct
    QT_QPA_PLATFORM="wayland;xcb"

    _JAVA_AWT_WM_NONREPARENTING=1
    NO_AT_BRIDGE=1
    GTK_USE_PORTAL=0

    CLUTTER_BACKEND=wayland
    SDL_VIDEODRIVER="wayland,x11"
    SDL_AUDIODRIVER=pipewire

### [menu.xml]

The [menu.xml] file defines the right-click Labwc menus. By default the right-click menu is predefined with some common applications, so unless the applications are installed on the system most of the default links on the menu will not be operational.

The default [menu.xml] is:

[FILE] **`~/.config/labwc/menu.xml`Labwc menu.xml example**

    <?xml version="1.0" ?>

    <openbox_menu>
    <menu id="root-menu" label="">
      <item label="Web browser"><action name="Execute" command="firefox" /></item>
      <item label="Terminal"><action name="Execute" command="alacritty" /></item>
      <item label="Reconfigure"><action name="Reconfigure" /></item>
      <item label="Exit"><action name="Exit" /></item>
    </menu>
    </openbox_menu>

Refer to [#Menu generators](#Menu_generators) for ideas on how to automatically create [menu.xml] files.

### [rc.xml]

The [rc.xml] file defines Labwc behavior, keyboard bindings, and mouse bindings.

The following is a list of special key \'modifiers\':

  ----- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Key   Description
  S     [Shift] key
  C     [Ctrl] key
  A     [Alt] key
  W     Super (windows) key
  M     Meta key
  H     Hyper key
  ----- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

To make a key binding, combine modifiers and a key. They are separated with the `-` (dash) sign.

** Important**\
Case matters! **S** (uppercase) equates to [Shift]-[s], while **s** (lowercase) equates to simply [s].

#### [Example content]

The [rc.xml] file is split into multiple sections with each offering configuration over the respective section

-   `CORE` - General window management options
-   `PLACEMENT` - How new windows should be placed
-   `WINDOW SWITCHER` - Define window switcher behavior
-   `RESISTANCE` - How resistance to movement windows are with regards other windows and screen edge
-   `FOCUS` - Window focus with respect to mouse cursor
-   `WINDOW SNAPPING` - Snapping behavior
-   `REGIONS` - Define snapping regions
-   `WORKSPACES` - Naming and numbering of virtual workspaces
-   `THEME` - Specific themes as well as other customization, corner radius, drop shadow \...
-   `MARGIN` - Edge margin reserving
-   `RESIZE` - Popup resize indicator control
-   `KEYBOARD` - Keyboard control and configuration
-   `MOUSE` - Mouse control and configuration
-   `TOUCH` - Touchpad control and configuration
-   `TABLE` - Tablet control and configuration
-   `LIBINPUT` - Additional input control and configuration
-   `WINDOW RULES` - Per window based behavior overrides
-   `MENU` - Right-click menu controls
-   `MAGNIFIER` - Onscreen magnifier control

[FILE] **`~/.config/labwc/rc.xml`Labwc rc.xml example**

    <?xml version="1.0"?>

    <labwc_config>

      <core>
        <gap>10</gap>
        <decoration>server</decoration>
        <windowSwitcher show="yes" preview="yes" outlines="no" />
       </core>

      <focus>
        <followMouse>yes</followMouse>
        <raiseOnFocus>no</raiseOnFocus>
      </focus>

      <resistance>
        <screenEdgeStrength>20</screenEdgeStrength>
      </resistance>

      <theme>
        <name>Arc-Clone</name>
        <cornerRadius>10</cornerRadius>
        <font><name>sans</name><size>10</size></font>
        <dropShadows>yes</dropShadows>
      </theme>


      automatic</policy>
    </placement>

    <desktops number="4" />

    <keyboard>
        <keybind key="A-Tab"> <action name="NextWindow" /> </keybind>
        <keybind key="W-Return"> <action name="Execute" command="foot" /> </keybind>
        <keybind key="Print"> <action name="Execute"> <command>sh -c 'grim -t jpeg ~/screenshots/$(date +%Y-%m-%d_%H-%m-%s).jpg'</command> </action> </keybind>
        <keybind key="W-Print"> <action name="Execute"> <command>sh -c 'grim -t jpeg -g "$(slurp)"  ~/screenshots/$(date +%Y-%m-%d_%H-%m-%s).jpg'</command> </action> </keybind>

        <keybind key="W-1"> <action name="GoToDesktop" to="1" /> </keybind>
        <keybind key="W-2"> <action name="GoToDesktop" to="2" /> </keybind>
        <keybind key="W-3"> <action name="GoToDesktop" to="3" /> </keybind>
        <keybind key="W-4"> <action name="GoToDesktop" to="4" /> </keybind>

        <keybind key="W-S-1"> <action name="SendToDesktop" to="1" /> </keybind>
        <keybind key="W-S-2"> <action name="SendToDesktop" to="2" /> </keybind>
        <keybind key="W-S-3"> <action name="SendToDesktop" to="3" /> </keybind>
        <keybind key="W-S-4"> <action name="SendToDesktop" to="4" /> </keybind>

        <keybind key="XF86_AudioLowerVolume"> <action name="Execute" command="wpctl set-volume  @DEFAULT_AUDIO_SINK@ 5%-"/> </keybind>
        <keybind key="XF86_AudioRaiseVolume"> <action name="Execute" command="wpctl set-volume  @DEFAULT_AUDIO_SINK@ 5%+"/> </keybind>
        <keybind key="XF86_AudioMute"> <action name="Execute" command="wpctl set-mute @DEFAULT_AUDIO_SINK@ toggle "/> </keybind>
    </keyboard>

    </labwc_config>

All options can be viewed either at [https://labwc.github.io/labwc-config.5.html](https://labwc.github.io/labwc-config.5.html) or [https://github.com/labwc/labwc/blob/master/docs/rc.xml.all](https://github.com/labwc/labwc/blob/master/docs/rc.xml.all)

### [shutdown]

The [shutdown] file is executed as a shell script when Labwc is preparing to terminate itself. All environment variables, including `WAYLAND_DISPLAY` and `DISPLAY`, will be available to the script. However, because the script runs asynchronously with other termination tasks, the [shutdown] file should not assume that the display will be usable. This file is useful to perform any custom operations necessary to finalize a Labwc session.

### [Menu generators]

Several menu generators exist to automatically create a [menu.xml] file with system applications:

-   [labwc-menu-generator](https://github.com/labwc/labwc-menu-generator): Independent of Desktop Environments and associated menu-packages. Very easy to build and use. Written in C.

<!-- -->

-   [labwc-menu-gnome3](https://github.com/labwc/labwc-menu-gnome3): Depends on GTK and a menu package such as GNOME, MATE or Cinnamon. Written in C.

<!-- -->

-   [obmenu-generator](https://trizenx.blogspot.com/2012/02/obmenu-generator.html): Popular with Openbox communities. Written in Perl.

<!-- -->

-   [openbox-menu](http://fabrice.thiroux.free.fr/openbox-menu_en.html): [XDG](https://wiki.gentoo.org/wiki/XDG "XDG") menu spec compliant, using [LXDE](https://wiki.gentoo.org/wiki/LXDE "LXDE")\'s library and menu package. Used to be packaged by Debian, but isn't anymore. Written in C.

<!-- -->

-   [arch-xdg-menu](https://arch.p5n.pp.ru/~sergej/dl/2018/): Arch Linux's xdg-menu package based on SuSE 2003 implementation. Written in Perl.

<!-- -->

-   [obamenu](https://github.com/onuronsekiz/obamenu): Designed for pipemenus, but could easily be modified to produce a root menu. Written in Python 3.

### [Themes]

Since the configuration re-uses the syntax of [Openbox](https://wiki.gentoo.org/wiki/Openbox "Openbox"), existing Openbox themes are usable. A good collection of Openbox themes can be found at [https://github.com/addy-dclxvi/openbox-theme-collections](https://github.com/addy-dclxvi/openbox-theme-collections).

The themes should be copied to [\~/.local/share/themes/\<theme-name\>/openbox-3/] and can be set via the [rc.xml] file under the `THEME` section.