Other languages:

[English] • ‎[Türkçe](//wiki.manjaro.org/index.php?title=Did_X.server_recognise_your_monitor_correctly%3F/tr "X.server monitörünüzü doğru bir şekilde tanıdı mı? (13% translated)") • ‎[русский](//wiki.manjaro.org/index.php?title=Did_X.server_recognise_your_monitor_correctly%3F/ru "Правильно ли X.server распознал монитор? (100% translated)")

## Contents

-   [[1] [A Quick Test to Validate these X.server Settings:]](#A_Quick_Test_to_Validate_these_X.server_Settings:)
    -   [[1.1] [The Test:]](#The_Test:)
    -   [[1.2] [What if the X.server got it wrong?]](#What_if_the_X.server_got_it_wrong.3F)
    -   [[1.3] [Getting Your Monitor\'s Specifications:]](#Getting_Your_Monitor.27s_Specifications:)
    -   [[1.4] [What do I do with the Specifications:]](#What_do_I_do_with_the_Specifications:)
    -   [[1.5] [What if I can\'t find the Manufacturer\'s Specifations?]](#What_if_I_can.27t_find_the_Manufacturer.27s_Specifations.3F)

# [A Quick Test to Validate these X.server Settings:]

It is certainly worthwhile checking that the X.server has recognised your monitor correctly. If the X.server can\'t recognise your monitor or incorrectly recognises your monitor your display will not be optimal.

\

## [The Test:]

Enter the following command in the Terminal:

\

[user \$ ][ xdpyinfo [COPY TO CLIPBOARD]]

\

\
These are the results from my machine; fortunately they are correct:

\

\

[\$] [xdpyinfo]\

    screen #0:
    dimensions:    1920x1200 pixels (524x321 millimeters)
    resolution:    93x95 dots per inch

\
**Note:** If you are running more than one monitor, this test will most likely provide results that are created by combining the monitors that you have connected to your machine & treating them as though they are one monitor!

So you may need to do some arithmetic, OR, of course you could just connect one monitor at a time for the test. ;)

\

## [][What if the X.server got it wrong?]

If the X.server can\'t work out what your screen size is it will set your DPI at the default of 75 x 75. If so, you will need to manually create a file like so:

[user \$ ][ touch /etc/X11/xorg.conf.d/90-monitor.conf [COPY TO CLIPBOARD]]

\

to which you must add the pertinent details *(see below)*.

\

## [][Getting Your Monitor\'s Specifications:]

Probably the easiest way to get the required details is from the technical specifications supplied in the monitor\'s manual.

If you don\'t have the manual, you can search for the specifications of your monitor online; most maker\'s have a section on their sites for archived manuals.

There are also other sites out there that carry such information.

\

## [What do I do with the Specifications:]

Enter the following into the Terminal to call your favourite text editor as root & create an initially empty file with the right path & name:

[user \$ ][ sudo \$EDITOR /etc/X11/xorg.conf.d/90-monitor.conf [COPY TO CLIPBOARD]]

\

Then copy the following into your editor\'s blank page:

\
**/etc/X11/xorg.conf.d/90-monitor.conf**

    Section "Monitor"
        Identifier             "Monitor0"
        DisplaySize             286 179    # In millimeters
    EndSection

\
You **MUST** replace the **DisplaySize** numbers with the ones for your monitor.

After you have done that, save the file & reboot. The next time X starts the X.server will have calculated your DPI values from the numbers that you put in the **DisplaySize** line above.

To test that the X.server has done what it has supposed to do & also that there were no typo\'s, run the test from the start of this wiki again.

\

## [][What if I can\'t find the Manufacturer\'s Specifations?]

You can measure your monitor & input the numbers that way, though your measurements will most likely be different than manufacturer\'s.

If you can\'t find the manufacturer\'s specifications on the web, have a look at this page as you still have options available to you: [\[1\]](https://wiki.archlinux.org/title/Xorg#Display_size_and_DPI)