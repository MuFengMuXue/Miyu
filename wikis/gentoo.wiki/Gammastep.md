[[]][GitLab](https://gitlab.com/chinstrap/gammastep)

Gammastep is an actively maintained fork of Redshift, with new features like native Wayland support via the wlroots protocol.

Gammastep is an automatic color temperature adjustment to help reduce monitor eye strain induced by working in low-light conditions. Depending on the location (longitude and latitude) of the user\'s computer system, Gammastep will change the color of the screen from the default bluish color to a orange/reddish color during evening hours, and then back again to bluish tint during daylight hours.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Files]](#Files)
    -   [[2.2] [Saving location information]](#Saving_location_information)
-   [[3] [Service]](#Service)
    -   [[3.1] [OpenRC]](#OpenRC)
    -   [[3.2] [systemd]](#systemd)
-   [[4] [Usage]](#Usage)
    -   [[4.1] [Invocation]](#Invocation)

## [Installation]

### [USE flags]

### [USE flags for] [x11-misc/gammastep](https://packages.gentoo.org/packages/x11-misc/gammastep) [[]] [A screen color temperature adjusting software]

  --------------------------------------------------------------------- ------------------------------------------------------------------------------------
  [`appindicator`](https://packages.gentoo.org/useflags/appindicator)   Build in support for notifications using the libindicate or libappindicator plugin
  [`geoclue`](https://packages.gentoo.org/useflags/geoclue)             Control dependency on app-misc/geoclue
  [`gtk`](https://packages.gentoo.org/useflags/gtk)                     Add support for x11-libs/gtk+ (The GIMP Toolkit)
  [`nls`](https://packages.gentoo.org/useflags/nls)                     Add Native Language Support (using gettext - GNU locale utilities)
  [`wayland`](https://packages.gentoo.org/useflags/wayland)             Enable dev-libs/wayland backend
  --------------------------------------------------------------------- ------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-01-04 18:33] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

After setting necessary USE flags, install Gammastep:

`root `[`#`]`emerge --ask x11-misc/gammastep`

## [Configuration]

### [Files]

A configuration file should be created at [\$/gammastep/config.ini]. If [XDG_CONFIG_HOME] is unset, the default of [\~/.config] is used.

An example configuration file can be found at [/etc/gammastep/config.ini.example].

In order for Gammastep to start, it will require longitude and latitude information inside the configuration file.

`user `[`$`]`gammastep -l manual:help`

### [Saving location information]

Gammastep can be quickly established in working order by adding correct location information into the configuration file. Latitude/Longitude values can be found searching for the closest city or region at [Wikipedia](https://www.wikipedia.org) or with a map service such as [OpenStreetMap](https://www.openstreetmap.org/).

When using OpenStreetMap, simply search for the location. When it appears on the map tiles click the [Export] button (should be near the top left). The center of the displayed tiles will be the exact Lat/Lon location. The Lat value is the second number from the end displayed in the URL. The Lon value is the last number on the end.

## [Service]

### [OpenRC]

Gammastep does not currently include an OpenRC init script.

### [systemd]

`user `[`$`]`systemctl --user enable gammastep.service `

`user `[`$`]`systemctl --user start gammastep.service `

## [Usage]

### [Invocation]

`user `[`$`]`gammastep -h`

    Usage: gammastep -l LAT:LON -t DAY:NIGHT [OPTIONS...]

    Set color temperature of display according to time of day.

      -h        Display this help message
      -v        Increase logging verbosity
      -q        Decrease logging verbosity
      -V        Show program version

      -b DAY:NIGHT  Screen brightness to apply (between 0.1 and 1.0)
      -c FILE   Load settings from specified configuration file
      -g R:G:B  Additional gamma correction to apply
      -l LAT:LON    Your current location
      -l PROVIDER   Select provider for automatic location updates
            (Type `list' to see available providers)
      -m METHOD Method to use to set color temperature
            (Type `list' to see available methods)
      -o        One shot mode (do not continuously adjust color temperature)
      -O TEMP   One shot manual mode (set color temperature)
      -p        Print mode (only print parameters and exit)
      -P        Reset existing gamma ramps before applying new color effect
      -x        Reset mode (remove adjustment from screen)
      -r        Disable fading between color temperatures
      -t DAY:NIGHT  Color temperature to set at daytime/night

    The neutral temperature is 6500K. Using this value will not change the color
    temperature of the display. Setting the color temperature to a value higher
    than this results in more blue light, and setting a lower value will result in
    more red light.

    Default values:

      Daytime temperature: 6500K
      Night temperature: 4500K

    Please report bugs to <https://gitlab.freedesktop.org/CameronNemo/gammastep/issues>