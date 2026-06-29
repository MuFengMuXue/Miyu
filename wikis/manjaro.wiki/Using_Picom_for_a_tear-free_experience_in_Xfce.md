This page contains [[changes](//wiki.manjaro.org/index.php?title=Using_Picom_for_a_tear-free_experience_in_Xfce&diff=53530)] which are not marked for translation.

## Contents

-   [[1] [Installing picom]](#Installing_picom)
-   [[2] [Configuring picom]](#Configuring_picom)
-   [[3] [Disabling xfwm4 compositor and enabling picom]](#Disabling_xfwm4_compositor_and_enabling_picom)
-   [[4] [Links]](#Links)

People who are experiencing screen tearing in Xfce can try out the following method.

Compton has been replaced by Picom

# [Installing picom]

Picom - is an X compositor which supports xrender and glx (opengl) backends.

To install it from the command line:

[user \$ ][ sudo pacman -S picom [COPY TO CLIPBOARD]]

\

# [Configuring picom]

Picom is configured by editing *\~/.config/picom/picom.conf*.

The following are some commonly used options:

\~/.config/picom/picom.conf

    backend = "glx";
    glx-no-stencil = true;
    vsync = true;
    unredir-if-possible = true;

    # Shadow
    shadow = true; # Enabled client-side shadows on windows.
    shadow-radius = 7; # The blur radius for shadows. (default 12)
    shadow-offset-x = -7; # The left offset for shadows. (default -15)
    shadow-offset-y = -7; # The top offset for shadows. (default -15)
    shadow-exclude = [
      "n:e:Notification",
      "n:e:Docky",
      "g:e:Synapse",
      "g:e:Conky",
      "n:w:*Firefox*",
      "n:w:*Chromium*",
      "n:w:*dockbarx*",
      "class_g ?= 'Cairo-dock'",
      "class_g ?= 'Xfce4-notifyd'",
      "class_g ?= 'Xfce4-power-manager'",
      "class_g ?= 'Notify-osd'",
      "_GTK_FRAME_EXTENTS@:c"
    ];

    # Opacity
    detect-client-opacity = true;

    # Window type settings
    wintypes:
    ;
      dnd = ;
      tooltip = ;
     };

# [Disabling xfwm4 compositor and enabling picom]

The following command can be used to turn off xfwm4\'s compositing feature:

[user \$ ][ xfconf-query -c xfwm4 -p /general/use_compositing -s false [COPY TO CLIPBOARD]]

\

Create a new file *\~/.config/autostart/picom.desktop* with content

\~/.config/autostart/picom.desktop

     [Desktop Entry]
     Encoding=UTF-8
     Version=0.9.4
     Type=Application
     Name=Picom
     Comment=X11 compositor
     Exec=compton -b
     OnlyShowIn=XFCE;
     StartupNotify=false
     Terminal=false
     Hidden=false

Now one could logout and login again to see if picom has been activated.

To check if picom is working following command can be used:

[user \$ ][ pgrep -l picom [COPY TO CLIPBOARD]]

\

# [Links]

-   [https://wiki.archlinux.org/title/Picom](https://wiki.archlinux.org/title/Picom)
-   [https://github.com/yshui/picom](https://github.com/yshui/picom)