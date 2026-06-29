+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [![Tango-dialog-warning.png](/images/d/d8/Tango-dialog-warning.png)](//wiki.manjaro.org/index.php?title=File:Tango-dialog-warning.png) | **This article or section is out of date.**                                                                                                                                                                                                                                                                                                                                                                     | [![Tango-dialog-warning.png](/images/d/d8/Tango-dialog-warning.png)](//wiki.manjaro.org/index.php?title=File:Tango-dialog-warning.png) |
|                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                                                                 |                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                          | :::                                                                                                                                                                                                                                                                                                                                                                                     |                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                          | **Reason:** This is page need to be updated. [Oguzkagan](//wiki.manjaro.org/index.php?title=User:Oguzkagan&action=edit&redlink=1 "User:Oguzkagan (page does not exist)") ([talk](//wiki.manjaro.org/index.php?title=User_talk:Oguzkagan "User talk:Oguzkagan")) ([Discuss](//wiki.manjaro.org/index.php?title=Talk:Simple_fix_for_screen_tearing_-_nVidia "Talk:Simple fix for screen tearing - nVidia")) |                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                          | :::                                                                                                                                                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                          |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

This fix is known to work with the nVidia non-Free driver package on Xfce & Openbox. It should work on any GTK based DE/WM & possibly others. This page will be updated in that regard as feedback comes in.

    21-Mar-2015 - Fully re-written due to new information coming in:

## [Possible side effects]

-   It is likely that whenever your mouse touches the top border of your screen it will dissapear (only whilst touching that border).

<!-- -->

-   It is looking like there have been improvements made to the nVidia proprietary driver package that have removed the problem that this fix had in its earlier days, in that it **no longer** slows down 3D graphics = games.

<!-- -->

-   Possible problem with some docks. It is not a problem with the Openbox dock or Tint2. (Will add information to this if it comes along.)

\

## [Here is the relatively simple procedure]

**1.** Open **/etc/X11/mhwd.d/nvidia.conf** in your favourite text editor with root permission.

**2.** Under Section **Device** add the following line

    Option "metamodes" "nvidia-auto-select +0+0 "

**3.** Save the modified file using the **Save As** option in your text editor, as **/etc/X11/xorg.conf.d/95-mhwd.conf**

**4.** Again, as root, delete the **/etc/X11/xorg.conf.d/@90-mhwd.conf** file, or **90-mhwd.conf** file (whichever you have).

**5.** Log out/in.

\
That\'s it.

    Making the new 95-mhwd.conf file as prescribed in the above method,
    means that nVidia won't overwrite it in the future with one of their
    future closed source driver upgrades.

\

## [Support]

Following is a link to this page\'s forum counterpart where you can post any related feedback: [\[1\]](https://forum.manjaro.org/index.php?topic=21358.0;topicseen)