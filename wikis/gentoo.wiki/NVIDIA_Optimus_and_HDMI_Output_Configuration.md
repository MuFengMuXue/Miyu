**[] Deprecated article**\
\

This article is **deprecated (obsolete)**. Contents are [no longer relevant], and are intended for historical reference only!

\
TLDR: **Do not use this article!**

Until now, HDMI doesn\'t work with Optimus hybrid graphics chipsets under Linux for most laptops, even if you use [Bumblebee](https://wiki.gentoo.org/wiki/NVIDIA/Bumblebee "NVIDIA/Bumblebee"). For our happiness there is a way to get HDMI to work: by using a separate session.

Using the instructions below, you\'ll get an LXDE session (you can use Xfce or others, but the instructions below are for LXDE) to show up on the external monitor (which is connected via HDMI). In this session, all the applications you launch use your laptop\'s NVIDIA graphics card, so you can play games, watch movies, etc. The LXDE session runs in the same time as your regular session, so on your laptop\'s screen you get your regular (main) session. Also, the mouse and keyboard are shared between the two sessions / monitors.

However, nothing is so good\... There are some things to consider when using this:

-   The sound won\'t work (if you know a way to get it to work, please let us know in the comments!) through HDMI so you\'ll only get sound through your laptop\'s speakers
-   You can\'t move a window from your current desktop to the monitor connected via HDMI. The only way to run applications on the device connected via HDMI is to either run it from its session menu, or by using \"export DISPLAY=:8.0\" (see the end of the post for more info on this). The mouse is however, shared between the two desktops.
-   When loading the extra session, you may get double indicators / tray icons on your current (main) session. There is a way around this though (see the \"tips\" section at the end of the post)

## Contents

-   [[1] [Get HDMI to work with laptops using the Optimus technology under Gentoo using Bumblebee and Synergy]](#Get_HDMI_to_work_with_laptops_using_the_Optimus_technology_under_Gentoo_using_Bumblebee_and_Synergy)
-   [[2] [Tips]](#Tips)
    -   [[2.1] [Launching applications]](#Launching_applications)
    -   [[2.2] [Configuring the Nvidia graphics card]](#Configuring_the_Nvidia_graphics_card)
    -   [[2.3] [Fixing mouse problem]](#Fixing_mouse_problem)
    -   [[2.4] [Example of a working xorg.nvdia.conf file]](#Example_of_a_working_xorg.nvdia.conf_file)
    -   [[2.5] [Error libGL error: failed to load driver: swrast]](#Error_libGL_error:_failed_to_load_driver:_swrast)
-   [[3] [External resources]](#External_resources)

## [Get HDMI to work with laptops using the Optimus technology under Gentoo using Bumblebee and Synergy]

The first step is to make sure [[[x11-misc/bumblebee]](https://packages.gentoo.org/packages/x11-misc/bumblebee)[]] is installed:

`root `[`#`]`emerge --ask bumblebee`

For further information about Bumblebee Project, visit [The Bumblebee Project](https://github.com/Bumblebee-Project) page or the [Gentoo Wiki Bumblebee Page](https://wiki.gentoo.org/wiki/NVIDIA/Bumblebee "NVIDIA/Bumblebee").

I\'m not sure if you can run two sessions using the same [window manager](https://wiki.gentoo.org/wiki/Category:Window_manager "Category:Window manager") without them interfering anyway, so you\'ll need to use a different [desktop environment](https://wiki.gentoo.org/wiki/Category:Desktop_environment "Category:Desktop environment") / session. I\'ve used LXDE so using the instructions below, you\'ll get an LXDE session on the monitor connected via HDMI.

To get the mouse and keyboard working on the external monitor connected via HDMI we\'ll use Synergy, a tool that lets you share the mouse and keyboard between multiple computers.

`root `[`#`]`emerge --ask synergy lxde-meta`

To be able to use Synergy, you\'ll need to create a configuration file. Copy the file to your home folder and rename it to [.synergy.conf] (notice the dot in front of the filename - that makes the file become hidden).

[FILE] **`/etc/synergy.conf`**

    section: screens
    gentoo:
    hdmi:
    end

    section: aliases
    end

    section: links
    gentoo:
    right = hdmi
    hdmi:
    left = gentoo
    end

    section: options
    end

The file I\'ve provided above should be enough, but if you want to change it, you can read about the Synergy configuration file [here](http://synergy2.sourceforge.net/configuration.html).

To start LXDE on the external monitor connected via HDMI, you can use a script bellow.

[FILE] **`~/hdmi`**

    #! /bin/bash

    export DISPLAY=:1.0
    optirun startlxde &
    sleep 5
    synergys -f -a 127.0.0.1 --display :0 -n gentoo &
    sleep 5
    synergyc -f -n hdmi --display :1 127.0.0.1 &
    sleep 5
    export DISPLAY=:0.0

Copy the \"hdmi\" script to your home folder and make it executable using the following command:

`user `[`$`]`chmod +x ~/hdmi`

Now, to run the script, use the following command:

`user `[`$`]`./hdmi`

LXDE should now start on the external monitor connected via HDMI. Give it some time (around 10 seconds) and moving your mouse to the left of your screen should make it show up on the HDMI device.

The script uses some \"sleep\" commands which add a delay to make sure the commands have enough time to get executed before running the next command.

## [Tips]

### [Launching applications]

To launch an application on the monitor connected via HDMI, you can use the LXDE menu on the external monitor or use the following command on your main session:

`user `[`$`]`export DISPLAY=:1.0 APPLICATION`

where \"APPLICATION\" is the executable name for the app you want to launch.

Optionally, you can also run \"export DISPLAY=:1.0\" in a terminal window on your main session, and then all the applications you launch from that terminal window should show up on the external monitor.

### [Configuring the Nvidia graphics card]

Using the above instructions to launch applications on the external monitor, you can launch \"nvidia-settings\" (if you\'re using the proprietary Nvidia graphics drivers):

`user `[`$`]`export DISPLAY=:1.0 nvidia-settings`

Launching this on your laptop session displays an error message saying that you\'re not using Nvidia drivers, but launching in on the HDMI-connected device (which uses Bumblebee with \"optirun\"), you can configure various Nvidia settings: the screen resolution, etc.

### [Fixing mouse problem]

When synergyc and synergys are running, you should notice a strange effect. When moving your mouse, you should see it moving on both screens, witch is quiet annoying and we need to fix this. I have found a solution after googled and I will share it here also. First of all we need to install the X.Org void driver:

`root `[`#`]`emerge --ask xf86-input-void`

The void driver simply does nothing. We need it, as synergy gives us mouse and keyboard, and there is no way to configure them in [xorg.conf](https://wiki.gentoo.org/wiki/Xorg.conf "Xorg.conf"). AutoEnableDevices makes X to add any further mouses and keyboards, it finds, to the server. We don\'t want them, so we disable it.

A working xorg.nvidia.conf file is presented in the following section, and you should use it as an example.

### [Example of a working xorg.nvdia.conf file]

[FILE] **`/etc/bumblebee/xorg.nvidia.conf`**

    Section "ServerLayout"
        Identifier "Layout0"
        Screen     "Screen0"
        InputDevice  "Keyboard1" "CoreKeyboard"
        InputDevice  "Mouse1" "CorePointer"
        Option "AutoAddDevices" "false"
    EndSection

    Section "Files"
        ModulePath "/usr/lib/nvidia-current/xorg,/usr/lib/xorg/modules"
    EndSection

    Section "Extensions"
        Option         "Composite" "Enable"
    EndSection

    Section "Device"
        Identifier "Device0"
        Driver "nvidia"
        VendorName "NVIDIA Corporation"
        BusID "01:00:0"
        Option "NoLogo" "true"
        Option "ConnectedMonitor" "DFP-0"
        Option "RenderAccel" "true"
        Option "AllowGLXWithComposite" "true"
    EndSection

    Section "Module"
        Load           "glx"
    EndSection

    Section "Monitor"
        Identifier    "Monitor0"
    EndSection

    Section "InputDevice"
        Identifier      "Keyboard1"
        Driver          "void"
        Option          "CoreKeyboard"
    EndSection

    Section "InputDevice"
        Identifier      "Mouse1"
        Driver          "void"
        Option          "CorePointer"
    EndSection

    Section "Screen"
        Identifier "Screen0"
        Monitor "Monitor0"
        Device "Device0"
        Defaultdepth 24
    # depending on your monitor, I didnt need the following section
    #    SubSection "Display"
    #   Depth 24
    #   Modes "1920x1080"
    #   Modes "1600x1200"
    #    EndSubSection
    EndSection

### [Error libGL error: failed to load driver: swrast]

[] The information in this section is probably **outdated**. You can help the Gentoo community by verifying and [updating this section](https://wiki.gentoo.org/index.php?title=NVIDIA_Optimus_and_HDMI_Output_Configuration&action=edit).

If you are seeing this error when starting glxgears:

    $ glxgears
    libGL error: failed to load driver: swrast
    libGL error: failed to load driver: swrast
    libGL error: failed to load driver: swrast
    primus: fatal: failed to acquire direct rendering context for display thread

Make sure that you have nvidia set in eselect list:

    $ sudo eselect opengl list
    Available OpenGL implementations:
      [1]   nvidia
      [2]   xorg-x11 *
    $ sudo eselect opengl set 1
    Switching to nvidia OpenGL interface... done

## [External resources]

-   [http://www.webupd8.org/2012/08/get-hdmi-working-with-nvidia-optimus-on.html](http://www.webupd8.org/2012/08/get-hdmi-working-with-nvidia-optimus-on.html)
-   [http://itviking.net/blog/m11xr3-bumblebee-and-the-dual-screen-setup](http://itviking.net/blog/m11xr3-bumblebee-and-the-dual-screen-setup)
-   [http://www.linuxquestions.org/questions/linux-desktop-74/multiple-x-servers-multiple-graphics-adapters-single-seat-kind-of-tutorial-864646/](http://www.linuxquestions.org/questions/linux-desktop-74/multiple-x-servers-multiple-graphics-adapters-single-seat-kind-of-tutorial-864646/)
-   [http://itviking.net/blog/m11xr3-bumblebee-and-the-dual-screen-setup](http://itviking.net/blog/m11xr3-bumblebee-and-the-dual-screen-setup)