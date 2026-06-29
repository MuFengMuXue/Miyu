[Translate this page](//wiki.manjaro.org/index.php?title=Special:Translate&group=page-Enable+Touchpad+Horizontal+and+Vertical+Scrolling&language=en&action=page&filter= "Special:Translate")

Other languages:

[English](//wiki.manjaro.org/index.php?title=Enable_Touchpad_Horizontal_and_Vertical_Scrolling "Enable Touchpad Horizontal and Vertical Scrolling (100% translated)") • ‎[Türkçe](//wiki.manjaro.org/index.php?title=Enable_Touchpad_Horizontal_and_Vertical_Scrolling/tr "Dokunmatik Yüzeyde Yatay ve Dikey Kaydırmayı Etkinleştir (21% translated)") • ‎[русский](//wiki.manjaro.org/index.php?title=Enable_Touchpad_Horizontal_and_Vertical_Scrolling/ru "Включение горизонтальной и вертикальной прокрутки тачпада (100% translated)")

## Contents

-   [[1] [Open the Synaptics Configuration File]](#Open_the_Synaptics_Configuration_File)
-   [[2] [Enable Click on Tap, Vertical and Horizontal Scrolling]](#Enable_Click_on_Tap.2C_Vertical_and_Horizontal_Scrolling)

In order to enable the *click on tap* and *vertical and horizonal scrolling* functions for your touchpad, it will be necessary first open your terminal in order to open and then edit the **synaptics configuration file**.

# [Open the Synaptics Configuration File]

The syntax the command to edit the synaptic configuration file is:

    sudo [text editor] /etc/X11/xorg.conf.d/50-synaptics.conf

\
To use nano (the default text-based terminal editor) enter the command:

    sudo nano /etc/X11/xorg.conf.d/50-synaptics.conf

\
Otherwise, you may find it easier to read and edit the file by using gedit, which will open the configuration file as if it were a document. To use gedit instead, enter the command:

    sudo gedit /etc/X11/xorg.conf.d/50-synaptics.conf

# [][Enable Click on Tap, Vertical and Horizontal Scrolling]

Once the synaptic configuration file has been opened, replace the content of this file with the following:

    Section "InputClass"
        Identifier "touchpad catchall"
        Driver "synaptics"
        MatchIsTouchpad "on"
        Option "TapButton1" "1"
        Option "VertEdgeScroll" "1"
        Option "HorizEdgeScroll" "1"
    EndSection

\
Once your amendments have been completed save your changes and close the configuration file by:

-   **nano**: Press CTRL and \'x\' to exit, \'y\' to save, and \<enter\> to finish, or
-   **gedit**: Select the \'save\' option and then close the window.