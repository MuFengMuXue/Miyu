Other languages:

[English] • ‎[русский](//wiki.manjaro.org/index.php?title=Configure_NVIDIA_(non-free)_settings_and_load_them_on_Startup/ru "Настройка параметров NVIDIA (несвободные) и загрузка их при запуске (100% translated)")

## Contents

-   [[1] [Introduction]](#Introduction)
-   [[2] [Install NVIDIA Drivers]](#Install_NVIDIA_Drivers)
-   [[3] [Configure The Resolution/Refresh Rate]](#Configure_The_Resolution.2FRefresh_Rate)
-   [[4] [Configure X Screen settings (OpenGL Settings, Antialiasing, X Server XVideo)]](#Configure_X_Screen_settings_.28OpenGL_Settings.2C_Antialiasing.2C_X_Server_XVideo.29)
-   [[5] [Troubleshooting: X-Server Failed to Start and Install]](#Troubleshooting:_X-Server_Failed_to_Start_and_Install)
-   [[6] [Bumblebee and Steam]](#Bumblebee_and_Steam)
-   [[7] [Feedback and Support]](#Feedback_and_Support)

# [Introduction]

**Note**

------------------------------------------------------------------------

This tutorial is meant for users who are using the NVIDIA Proprietary (non-free) drivers.

\
You can check what drivers you have installed by entering the following command into your terminal:

    inxi -G

# [Install NVIDIA Drivers]

If you have the Nouveau driver you can install the proprietary NVIDIA driver by using the [Manjaro Hardware Detection (MHWD)](//wiki.manjaro.org/index.php?title=Configure_Graphics_Cards "Configure Graphics Cards") utility. To do so, enter the following command into your terminal:

    sudo mhwd -a pci nonfree 0300

\
Once Complete, reboot your system to complete the process. You can then confirm that the driver has been installed and is working by entering the following command into your terminal:

    mhwd -li

\

# [][Configure The Resolution/Refresh Rate]

**Warning**

------------------------------------------------------------------------

The method provided does not currently work for the Cinnamon Edition. As soon as a solution is found, then this article will be updated.

\
**1.** Open your terminal and enter the following command:

    sudo nvidia-settings

\
**2.** Change resolution and refresh rate in \'X Server Display Configuration\' tab.

**3.** Hit the \'Save to X Configuration File\' button and save to **/etc/X11/mhwd.d/nvidia.conf**

**4.** Now enter the following command into the terminal to complete the process:

    sudo mhwd-gpu --setmod nvidia --setxorg /etc/X11/mhwd.d/nvidia.conf

# [][Configure X Screen settings (OpenGL Settings, Antialiasing, X Server XVideo)]

**1.** Open your terminal and enter the following command:

    nvidia-settings

\
**2.** Change settings in X Server XVideo Settings, OpenGL and Antialiasing, in the \'X Screen\' tab.

**3.** Click on \'nvidia-settings configuration\' tab and click on the \'Save Current Configuration\' button.

**4.** Save the .nvidia-settings-rc to the default location specified (**/home/\[your account name\]**)

**5.** Edit the .xinitrc file with your preferred text editor. For example, run this in your terminal:

    gedit ~/.xinitrc

\
**6.** Once opened, add the following line into the configuration file, before the last line that starts with \'exec\' :

    nvidia-settings --load-config-only
    exec $(get_session)

**7.** Save and exit.

# [Troubleshooting: X-Server Failed to Start and Install]

Where there has been an error during the installation process, upon rebooting you may see the following error message: **modprobe: ERROR: could not insert nvidia : No such a device**

\
If this happens:

**1.** Remove the NVIDIA driver by entering the following command into your terminal:

    sudo mhwd -r pci video-nvidia

\
**2.** Reboot your computer

\
**3.** Enter the following into your terminal:

    sudo gedit /etc/mkinitcpio.conf

\
**4.** delete the word **nouveau** from the following line:

    MODULES=" nouveau"

\
It should now look like this (i.e. keep the speech marks (\"\")):

    MODULES=""

\
**5.** Save and close the file.

\
**6.** It is now necessary to reconfigure your existing kernel to take into account this change. The syntax of the necessary command to enter into your terminal is:

    sudo mkinitcpio -p [linux kernel version]

\
For example, if you are currently using Kernel 3.10, you would enter the following:

    sudo mkinitcpio -p linux310

\
For kernel 3.11, you would enter the following:

    sudo mkinitcpio -p linux311

\
And so on.

**7.** Now re-install the NVIDIA driver by entering the following command into your terminal:

    sudo mhwd -a pci nonfree 0300

\
**8.** Reboot your system. Now it should work ;)

# [Bumblebee and Steam]

**Warning**

------------------------------------------------------------------------

These instructions are outdated. Until they are reviewed for validity, please do not follow them blindly. Especially consider that there are also legacy nvidia drivers for older cards, like nvidia390xx and nvidia340xx. If you are not sure, please look for a tutorial or ask for assistance at the [forum](https://forum.manjaro.org).

\

Properly using and configuring Bumblebee with Steam is much easier than it seems at first.

**1.** Install bumblebee for nonfree nvidia. Please run in terminal command in proper order:

    sudo pacman -S virtualgl lib32-virtualgl lib32-primus primus

    sudo mhwd -f -i pci video-hybrid-intel-nvidia-bumblebee

    sudo systemctl enable bumblebeed

**2.** Reboot system:

    sudo reboot

**3.** Next run:

    optirun -b none nvidia-settings -c :8

**4.** Verify it is working

    primusrun glxspheres64

and

    glxspheres64

so you can see the difference.

**5a.** To have all games with Steam run using the NVidia card. Run Steam with command:

    primusrun steam

**5b.** Alternatively, you can run specific games by:

Select a game - that you want to run using your discrete Nvidia card - from the Library page of the Steam client, right-click, and select Properties. Click the SET LAUNCH OPTIONS\... button and specify primusrun %command% for the command line. Save your changes.This method allows you to pick when the discrete NVidia GPU should be used on a per-game basis.

# [Feedback and Support]

If you have any problems, improvements or see any errors in this tutorial, please post in this Manjaro forum thread: [\[1\]](http://forum.manjaro.org/index.php?topic=4489.0)