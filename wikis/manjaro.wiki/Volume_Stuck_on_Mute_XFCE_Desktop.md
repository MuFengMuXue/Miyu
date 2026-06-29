+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [![Tango-dialog-warning.png](/images/d/d8/Tango-dialog-warning.png)](//wiki.manjaro.org/index.php?title=File:Tango-dialog-warning.png) | **This article or section is out of date.**                                                                                                                                                                                                                                                                                                                                                                                                                 | [![Tango-dialog-warning.png](/images/d/d8/Tango-dialog-warning.png)](//wiki.manjaro.org/index.php?title=File:Tango-dialog-warning.png) |
|                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                          | :::                                                                                                                                                                                                                                                                                                                                                                                                                                 |                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                          | **Reason:** This is page need to be updated. [Oguzkagan](//wiki.manjaro.org/index.php?title=User:Oguzkagan&action=edit&redlink=1 "User:Oguzkagan (page does not exist)") ([talk](//wiki.manjaro.org/index.php?title=User_talk:Oguzkagan "User talk:Oguzkagan")) ([Discuss](//wiki.manjaro.org/index.php?title=Talk:Volume_Stuck_on_Mute_(XFCE_Desktop)&action=edit&redlink=1 "Talk:Volume Stuck on Mute (XFCE Desktop) (page does not exist)")) |                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                          | :::                                                                                                                                                                                                                                                                                                                                                                                                                                                         |                                                                                                                                                                                                                          |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

## Contents

-   [[1] [Overview]](#Overview)
-   [[2] [Solution 1: Removing PulseAudio]](#Solution_1:_Removing_PulseAudio)
-   [[3] [Solution 2: Creating a Sound Configuration File]](#Solution_2:_Creating_a_Sound_Configuration_File)
    -   [[3.1] [Create the Sound Configuration File]](#Create_the_Sound_Configuration_File)
    -   [[3.2] [Edit the Sound Configuration File]](#Edit_the_Sound_Configuration_File)
    -   [[3.3] [Optional: Add a Keyboard Shortcut to Toggle Volume Muting]](#Optional:_Add_a_Keyboard_Shortcut_to_Toggle_Volume_Muting)
-   [[4] [Troubleshooting]](#Troubleshooting)
    -   [[4.1] [Steam]](#Steam)
    -   [[4.2] [Skype]](#Skype)
-   [[5] [Support]](#Support)

# [Overview]

The inability to toggle the volume mute particulary affects users of the XFCE desktop environment. This is due to an incompatability between *xfce4-volumed* - the volume daemon used by this desktop environment- and *PulseAudio*, which is responsible for recording and playback. The result is that once muted, the volume cannot be restored by un-checking the mute button; it is instead necessary to open the *Volume Control Settings* to do so.

The are two solutions available. The first is to remove *PulseAudio* completely, allowing for the *Alsa* sound server to take over instead. The second is to create a sound configuration file. **New users may find the first solution easier to implement**.

\

# [Solution 1: Removing PulseAudio]

The first step is to remove all PulseAudio packages by entering the following command in the terminal:

    sudo pacman -R pavucontrol pulseaudio pulseaudio-alsa

It might be necessary to remove manjaro-pulse and pulseaudio-ctl first. You can do that with the following command:

    sudo pacman -Rns manjaro-pulse
    sudo pacman -Rns pulseaudio-ctl

\
Once completed, the second step is to install *xfce4-mixer*, which is a volume control applet specifically designed for the XFCE desktop environment. The command below has also listed *xfce4-volumed* for re-installation:

    sudo pacman -S xfce4-mixer xfce4-volumed

\
Once installed, close the terminal and reboot your system for the changes to take effect. *Alsa* will automatically take over from the now-deleted *PulseAudio.*

# [Solution 2: Creating a Sound Configuration File]

An alternative solution is to create a configuration file - **asound.conf** - to act as a workaround by altering the default sound configuration settings. In order to work, it is absolutely essential that this file be created within the **etc** folder, which itself also contains a number of other system configuration files.

\

## [Create the Sound Configuration File]

The syntax of the command to create a sound configuration file within the *etc* folder is:

    sudo [text editor] /etc/asound.conf

For example, if you wish to create and edit the file within the terminal using nano (a standard terminal-based text editor) then enter:

    sudo nano /etc/asound.conf

\
Otherwise - if you have installed the full version of Manjaro (i.e. not the NET-Edition) - you may find it easier to use the pre-installed gedit text editor instead. This will create and open the configuration file up as a document, making it easier to read and edit. To use gedit instead, enter:

    gksudo gedit /etc/asound.conf

\

## [Edit the Sound Configuration File]

Once created, a blank screen or document should be presented. Enter (or copy and paste) the following code into this file, **exactly** as it is shown below:

    pcm.pulse
    ctl.pulse
    pcm.!default
    ctl.!default

\
Once you have completed the code, save and close the file by:

-   **nano**: Press CTRL and \'x\' to exit, \'y\' to save, and \<enter\> to finish, or
-   **gedit**: Select the \'save\' option and then close the window.

\
Prior to rebooting for the changes to take effect, it is also possible to optionally add a keyboard shortcut to toggle volume muting.

\

## [Optional: Add a Keyboard Shortcut to Toggle Volume Muting]

[![Soundshortcut.png](/images/0/01/Soundshortcut.png)](//wiki.manjaro.org/index.php?title=File:Soundshortcut.png)

[](//wiki.manjaro.org/index.php?title=File:Soundshortcut.png "Enlarge")

\
To set a keyboard shortcut:

**1.** Open the Menu, select *Settings*, and then *Keyboard*

**2.** Select the *Application Shortcuts* tab

**3.** Select the *+ Add* Button

**4.** Enter the following command, and then select *OK*

    amixer set Master toggle

**5.** When prompted, press the appropriate key or key combination desired to toggle muting

Once complete, close the *Keyboard Settings* window, and reboot the system for the changes to take effect.\

# [Troubleshooting]

## [Steam]

If U using **Steam**. **Don\'t run** `amixer set Master toggle` command. Otherwise the game will not run properly due to an error ALSA audio. It is recommended to restore the default contents of **/etc/asound.conf**.

## [Skype]

If your music or video sound gets muted when answering a call on Skype, open /etc/pulse/default.pa in your favourite editor. Add \# at the beginning of the line that contains **load-module module-role-cork**, so you get **\# load-module module-role-cork**. Save the file and reboot. [\[1\]](https://bbs.archlinux.org/viewtopic.php?id=148424)

# [Support]

Following is a link to this page\'s forum counterpart where you can post any related feedback: [\[2\]](http://forum.manjaro.org/index.php?topic=6451.msg56627#msg56627)