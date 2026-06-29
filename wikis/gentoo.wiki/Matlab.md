This guide explains how to install and run MathWorks Matlab on Gentoo.

\

## Contents

-   [[1] [Downloading Matlab Installer]](#Downloading_Matlab_Installer)
-   [[2] [Mounting the installation media]](#Mounting_the_installation_media)
    -   [[2.1] [ISO file]](#ISO_file)
    -   [[2.2] [Optical disk]](#Optical_disk)
-   [[3] [Mounting the installation media]](#Mounting_the_installation_media_2)
-   [[4] [Installing]](#Installing)
-   [[5] [Troubleshooting]](#Troubleshooting)
    -   [[5.1] [Blank window while using xmonad/awesome/dwm]](#Blank_window_while_using_xmonad.2Fawesome.2Fdwm)
    -   [[5.2] [Install gui not show up]](#Install_gui_not_show_up)
    -   [[5.3] [\'TS_ABNORM​AL_TERMINA​TION\' when running installer]](#.27TS_ABNORM.E2.80.8BAL_TERMINA.E2.80.8BTION.27_when_running_installer)
    -   [[5.4] [Warning \`GLIBCXX_3.4.29\' not found]](#Warning_.60GLIBCXX_3.4.29.27_not_found)
    -   [[5.5] [Installer not launching on openrc systems]](#Installer_not_launching_on_openrc_systems)
    -   [[5.6] [Failed to load module \"canberra-gtk-module\"]](#Failed_to_load_module_.22canberra-gtk-module.22)
    -   [[5.7] [Failed to load module \"appmenu-gtk-module\"]](#Failed_to_load_module_.22appmenu-gtk-module.22)
    -   [[5.8] [Failed to begin installer \"libexpat.so.1: file too short\"]](#Failed_to_begin_installer_.22libexpat.so.1:_file_too_short.22)
    -   [[5.9] [ERROR 5201 when trying to run matlab]](#ERROR_5201_when_trying_to_run_matlab)
-   [[6] [Desktop entry]](#Desktop_entry)
    -   [[6.1] [MATLAB startup options]](#MATLAB_startup_options)
    -   [[6.2] [Example desktop entry]](#Example_desktop_entry)
-   [[7] [See also]](#See_also)
-   [[8] [External resources]](#External_resources)

## [Downloading Matlab Installer]

Before the MATLAB program can be installed, a full copy of the program must be acquired; license holders can access the program via the [MathWorks website](https://www.mathworks.com) or on a DVD. A file installation key is also needed.

\

## [Mounting the installation media]

### [ISO file]

`root `[`#`]`modprobe loop `

`root `[`#`]`mkdir -p /mnt/iso `

`root `[`#`]`mount -o loop matlab.iso /mnt/iso `

`root `[`#`]`cd /mnt/iso `

### [Optical disk]

`root `[`#`]`mkdir -p /mnt/cdrom `

`root `[`#`]`mount -t iso9660 -o ro /dev/cdrom /mnt/cdrom `

`root `[`#`]`cd /mnt/cdrom `

\

## [Mounting the installation media]

## [Installing]

`root `[`#`]`./install `

## [Troubleshooting]

### [][Blank window while using xmonad/awesome/dwm]

Set the WM name to \"LG3D\"

e.g. xmonad:

[FILE] **`~/.xmonad/xmonad.hs`**

    main =
        xmonad $ defaultConfig

### [Install gui not show up]

This may happen on R2023b. Try

`root `[`#`]`LD_PRELOAD=/usr/lib/gcc/x86_64-pc-linux-gnu/$/libstdc++.so ./install`

If matlab\'s gui not show up as well, you can also try to use

`user `[`$`]`LD_PRELOAD=/usr/lib/gcc/x86_64-pc-linux-gnu/$/libstdc++.so matlab`

### [][\'TS_ABNORM​AL_TERMINA​TION\' when running installer]

The above solution also works for this error at R2024b version.

However an alternative solution is running the installer as root: [Explanation](https://www.mathworks.com/matlabcentral/answers/2108841-why-do-i-get-error-ts_abnormal_termination-when-i-try-to-launch-the-matlab-r2024a-installer-on-lin)

`user `[`$`]`xhost +SI:localuser:root`

`user `[`$`]`sudo ./install`

`user `[`$`]`xhost -SI:localuser:root`

### [][Warning \`GLIBCXX_3.4.29\' not found]

This warning vanishes after linking the current library. For example:

`root `[`#`]`ln -sf /usr/lib/gcc/x86_64-pc-linux-gnu/12.2.0/libstdc++.so.6.0.30 /usr/local/MATLAB/R2022a/bin/glnxa64/libstdc++.so.6`

### [Installer not launching on openrc systems]

Matlab versions from 2021a include a new installer that assumes systemd is present. The resulting error is:

`root `[`#`]`./install `

terminate called after throwing an instance of \'std::runtime_error\'

     what():  Failed to launch web window with error: Unable to launch the MATLABWindow application. The exit code was: 127

\[1\] 342 IOT instruction ../../install

This can be caused by more than one assumed library being missing, but in particular if you are running openrc as your init system it will fail because of a missing libsystemd.so.0. This can be verified by launching the MATLABWindow application directly:

`root `[`#`]`./path/to/matlabInstallFiles/bin/glnxa64/MATLABWindow ./MATLABWindow: error while loading shared libraries: libsystemd.so.0: cannot open shared object file: No such file or directory`

If this is indeed the library causing the fault it can be solved by symlinking /lib64/libelogind.so.0 to the install\'s glnxa64 path as libsystemd.so.0, as elogind provides all the methods needed by the install:

`root `[`#`]`ln -s /lib64/libelogind.so.0 /path/to/matlabInstallFiles/bin/glnxa64/libsystemd.so.0 `

`root `[`#`]`/path/to/matlabInstallFiles/install `

### [][Failed to load module \"canberra-gtk-module\"]

This warning vanishes after linking the libcanberra module. For example:

`root `[`#`]`ln -s /usr/lib64/gtk-2.0/modules/libcanberra-gtk-module.so /usr/local/MATLAB/R2023a/bin/glnxa64/libcanberra-gtk-module.so`

### [][Failed to load module \"appmenu-gtk-module\"]

This warning vanishes after linking the libappmenu-gtk module. For example:

`root `[`#`]`ln -s /usr/lib64/gtk-2.0/modules/libappmenu-gtk-module.so /usr/local/MATLAB/R2023a/bin/glnxa64/libcanberra-gtk-module.so`

### [][Failed to begin installer \"libexpat.so.1: file too short\"]

`root `[`#`]`unzip -X -K matlab_R2024a_glnxa64`

\

### [ERROR 5201 when trying to run matlab]

`user `[`$`]`./matlab`\
`Unable to access services required to run MATLAB (error 5201).`

[More info](https://in.mathworks.com/matlabcentral/answers/1815395-why-do-i-receive-error-5201-unable-to-access-services-required-to-run-matlab) Current workaround that works for R2024b and R2024a confirmed is: The second line may be not needed depending on your install. (replace user with your user)

`root `[`#`]`patchelf --clear-execstack /home/user/.MathWorks/ServiceHost/-mw_shared_installs/v2025.2.2.1/bin/glnxa64/libmwfoundation_crash_handling.so`

`root `[`#`]`patchelf --clear-execstack /home/user/.MathWorks/ServiceHost/-mw_shared_installs/v2025.2.2.1/bin/glnxa64/mathworksservicehost/rcf/matlabconnector/serviceprocess/rcf/service/libmwmshrcfservice.so`

\

## [Desktop entry]

Optionally create a desktop entry. The MIME type of MATLAB files is `text/x-matlab`.

MATLAB can be started with several useful flags:

### [MATLAB startup options]

-   `-h`, `-help` --- Show all startup arguments and exit.
-   `-n` --- Display final environment variables and diagnostic startup information. MATLAB does not run.
-   `-e` --- Display all environment variables and their values. MATLAB does not run.
-   `v=variant` --- Start MATLAB from `bin/glnxa64/variant` instead of the default `bin/glnxa64`.
-   `-c licensefile` --- Use the specified license file or server (e.g., `port@host`). Ignores `LM_LICENSE_FILE` and `MLM_LICENSE_FILE`.
-   `-display Xdisplay` --- Send X commands to a specific X display (Linux only).
-   `-nodisplay` --- Disable all X display output. No desktop is started, but Java is still initialized unless `-nojvm` is also used.
-   `-noFigureWindows` --- Prevent creation of figure windows (useful for headless execution).
-   `-nosplash` --- Suppress the MATLAB splash screen.
-   `-softwareopengl` --- Force software OpenGL (common workaround for GPU/driver issues).
-   `-nosoftwareopengl` --- Disables automatic fallback to software OpenGL (Linux only).
-   `-debug` --- Provide additional debugging information, especially for X-related issues (Linux only).
-   `-desktop` --- Allow MATLAB desktop to start without a controlling terminal (required for launching from a desktop entry).
-   `-nodesktop` --- Do not start the desktop; run in terminal mode (Java still loads).
-   `-singleCompThread` --- Restrict MATLAB to a single computational thread.
-   `-nojvm` --- Completely disable the Java Virtual Machine. No desktop and reduced functionality.
-   `-jdb` `[port]` --- Enable remote Java debugging (default port: 4444).
-   `-batch` `MATLAB_command` --- Run MATLAB command(s) non-interactively with no desktop; exit with command status. Cannot be combined with `-r`.
-   `-r` `MATLAB_command` --- Run MATLAB command at startup. Cannot be combined with `-batch`.
-   `-sd folder` --- Set the startup folder. Cannot be combined with `-useStartupFolderPref`.
-   `-useStartupFolderPref` --- Use the "Initial working folder" preference as the startup folder. Cannot be combined with `-sd`.
-   `-logfile file` --- Mirror all command-window output (including crash reports) to a file.
-   `-Ddebugger` `[options]` --- Start MATLAB under a debugger.
-   `-nouserjavapath` --- Ignore `javaclasspath.txt` and `javalibrarypath.txt` overrides.

\
In order for icons to appear correctly StartupWMClass needs to be set in the desktop entry. To find it out start MATLAB, run:

`user `[`$`]` xprop | grep WM_CLASS `

and select the MATLAB window.

\

### [Example desktop entry]

Place the file at:

    /usr/share/applications/matlab.desktop

[FILE] **`/usr/share/applications/matlab.desktop`**

    [Desktop Entry]
    Type=Application
    MimeType=text/x-matlab
    Terminal=false
    Exec=/usr/local/MATLAB/R20xyz/bin/matlab -desktop -useStartupFolderPref -softwareopengl
    Name=MATLAB
    Icon=matlab
    Categories=Development;Math;Science;
    Comment=Scientific computing environment
    StartupNotify=true
    StartupWMClass=matlab

\

## [See also]

-   [GNU Octave](https://wiki.gentoo.org/wiki/GNU_Octave "GNU Octave") --- a free and open-source computing environment and high-level interactive programming language, that is primarily intended for numerical computations.

## [External resources]