The FlightGear flight simulator project is an open-source, multi-platform, cooperative flight simulator development project.

## Contents

-   [[1] [Installation]](#Installation)
-   [[2] [Command line usage]](#Command_line_usage)
-   [[3] [Additional aircraft]](#Additional_aircraft)
    -   [[3.1] [Additional scenery]](#Additional_scenery)
        -   [[3.1.1] [Terrasync]](#Terrasync)
-   [[4] [Scripting command line options]](#Scripting_command_line_options)
-   [[5] [Known Problems]](#Known_Problems)
    -   [[5.1] [Poor Frame Rates Compared to Win32 Build\'s Frame Rates]](#Poor_Frame_Rates_Compared_to_Win32_Build.27s_Frame_Rates)
-   [[6] [See Also]](#See_Also)
-   [[7] [External Resources]](#External_Resources)

## [Installation]

`root `[`#`]`emerge flightgear`

## [Command line usage]

Although the simulation can be started via a menu in the the [desktop environment (DE)](https://wiki.gentoo.org/wiki/Desktop_environment "Desktop environment") or [window manager (WM)](https://wiki.gentoo.org/wiki/Window_manager "Window manager"), it can be preferable to start FlightGear via the command line as there is more control over the simulation configuration.

`user `[`$`]`fgfs`

Show help messages:

`user `[`$`]`fgfs --help --verbose | less`

Start FlightGear via the launcher, which allows choosing various options (including the specific aircraft to fly):

`user `[`$`]`fgfs --launcher`

Show a listing of available aircraft:

`user `[`$`]`fgfs --show-aircraft`

Example command line incantation (which is used within the Win32 build) for adding geometry (use the desired screen resolution) and time of day options:

`user `[`$`]`fgfs --fg-root=/usr/share/games/flightgear --fg-scenery=/usr/share/games/flightgear/Scenery --aircraft=c172p-canvas --control=joystick --disable-random-objects --prop:/sim/rendering/random-vegetation=false --disable-ai-models --disable-ai-traffic --disable-real-weather-fetch --enable-clouds3d --enable-fullscreen --prop:/sim/frame-rate-throttle-hz=60 --geometry=1680x1050 --bpp=32 --timeofday=noon`

## [Additional aircraft]

Users can download additional (unsupported) aircraft models. Once downloaded, extract the tarballs and use the following option:

`user `[`$`]`fgfs --fg-aircraft="$/.fgfs/my-extracted-aircraft-2.12.0`

### [Additional scenery]

Users can download additional scenery or utilize terrasync.

Take note, there is currently no [/usr/share/games/flightgear/Scenery] folder as noted by the previous incantation.

Download the tarball scenery, extract into a local folder, and use the following option:

`user `[`$`]`fgfs --fg-scenery="$/.fgfs/my-extracted-scenery-2.12.0/:/usr/share/games/flightgear/Scenery:$/.fgfs/my-terrasync"-2.12.0`

#### [Terrasync]

To enable Terrasync, use the following while remembering to add the folder to the `--fg-scenery` list of folders, as specified above. (Unknown if specifying the additional Terrasync folder within fg-scenery is necessary.)

`user `[`$`]`mkdir $/.fgfs/my-terrasync-2.12.0`

`user `[`$`]`fgfs --enable-terrasync --terrasync-dir=$/.fgfs/my-terrasync-2.12.0 --fg-scenery=$/.fgfs/my-terrasync"-2.12.0`

## [Scripting command line options]

Eventually it becomes more desirable to automate much of these commands per scenario. It is nice to already have script files for different scenarios, named such as [fgfs.sh], [fgfs-mp.sh], and [fgfs-debug.sh] to respectively start in single player, multiplayer or debug modes.

For example, to start a FlightGear multiplayer session:

[FILE] **`$/bin/fgfs-mp.sh`**

    #!/bin/bash
    # Airports
    # KPDX Portland Intl
    # KLAX Los Angeles Intl
    # PFAI Fairbanks Int
    # KSFO San Fransisco, CA

    # Aircraft
    # 777-300
    # c172p-canvas
    # CitationX

    /usr/games/bin/fgfs \
        --aircraft=c172p-canvas \
        --browser-app=/usr/bin/seamonkey \
        --callsign=BIGBIRD \
        --control=joystick \
        --disable-terrasync \
        --enable-game-mode \
        --enable-real-weather-fetch \
        --fg-root=/usr/share/games/flightgear \
        --multiplay=out,10,mpserver16.flightgear.org,5000 \
        --prop:/sim/rendering/multithreading-mode=AutomaticSelection \
        --prop:/sim/rendering/shaders/quality-level=0 \
        --prop:/sim/rendering/texture-compression=off \
        --log-level=alert \
        --units-feet

Make the file executable and run it whenever. To modify your options, do so by editing the commented script file!

`user `[`$`]`chmod u+x $/bin/fgfs-mp.sh`

`user `[`$`]`./bin/fgfs-mp`

(Omit the \"./\" if \"\$/bin\" is already within the \$PATH.)

## [Known Problems]

### [][Poor Frame Rates Compared to Win32 Build\'s Frame Rates]

The default \"c172p\" aircraft model seems to cause significant frame rate loss. Choosing another aircraft model such as the \"c172p-canvas\" alleviates this problem.

`user `[`$`]`fgfs --aircraft=c172p-canvas`

## [See Also]

[Track IR](https://wiki.gentoo.org/wiki/Track_IR "Track IR")

## [External Resources]