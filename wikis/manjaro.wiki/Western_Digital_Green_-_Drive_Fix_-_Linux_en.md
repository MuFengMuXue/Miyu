[Translate this page](//wiki.manjaro.org/index.php?title=Special:Translate&group=page-Western+Digital+Green+-+Drive+Fix+-+Linux&language=en&action=page&filter= "Special:Translate")

Other languages:

[English](//wiki.manjaro.org/index.php?title=Western_Digital_Green_-_Drive_Fix_-_Linux "Western Digital Green - Drive Fix - Linux (100% translated)") • ‎[Türkçe](//wiki.manjaro.org/index.php?title=Western_Digital_Green_-_Drive_Fix_-_Linux/tr "Western Digital Green - Sürücü Düzeltme - Linux (5% translated)") • ‎[русский](//wiki.manjaro.org/index.php?title=Western_Digital_Green_-_Drive_Fix_-_Linux/ru "Western Digital Green - починка диска - Linux (100% translated)")

## Contents

-   [[1] [Here\'s the story]](#Here.27s_the_story)
-   [[2] [How to check/evaluate your WD Green Drive]](#How_to_check.2Fevaluate_your_WD_Green_Drive)
-   [[3] [This is how we solve the problem]](#This_is_how_we_solve_the_problem)
    -   [[3.1] [Modify the timer]](#Modify_the_timer)
    -   [[3.2] [Power off and verify]](#Power_off_and_verify)
    -   [[3.3] [Optional step]](#Optional_step)
-   [[4] [Support]](#Support)

# [][Here\'s the story]

I have recently discovered (a bit too late) that Western Digital Green hard drives have a serious issue when used in Linux as a main drive or a NAS drive. The problem can also occur in certain situations in windows too. The problem is due to a feature called **intellipark**. Which parks the heads on the drive after 8secs of drive inactivity.

Many Linux installations write to the file system a few times a minute in the background (eg. writing logs). As a result, there may be 100 or more load cycles per hour, and the load cycle rating may be exceeded in less than a year. This problem also makes the drives very unresponsive and makes your system feel slow as the heads need to be unparked when you try and load something.

My friend has killed two 1TB Green drives on his XBMC media box in 4years. The 500GB drive in my partners machine is in deep trouble as the **load_cycle** count is at **1991353** after a **power_on_hours** of **29549hrs**. Compare that to my WD Black 1TB which has a **load_cycle** count of **721** after **13579hrs**.

Now Western Digitals specsheet says that the drives are good for 300,000 Load/unload cycles, so this is a pretty big deal. [\[1\]](http://www.wdc.com/wdproducts/library/SpecSheet/ENG/2879-771438.pdf)

# [][How to check/evaluate your WD Green Drive]

If you have a Western Digital Green drive, please check your **SMART** information before it\'s too late. To do this you will need to install the package called **smartmontools** with pamac, octopi, or pacman:

[user \$ ][ sudo pacman -S smartmontools [COPY TO CLIPBOARD]]

\

Now check like this changing **sda** to whatever your Green drive is.\
(Use lsblk in terminal or gparted or i-nex or something to work out which drive it is.):

[user \$ ][ sudo smartctl -A /dev/sda [COPY TO CLIPBOARD]]

\

    193 Load_Cycle_Count        0x0032   253   253
    000    Old_age   Always       -       1991353

If the Load cycle count exceeds a few thousand, you\'re affected by the idle3 timer problem.

Here is how the output should look when this isn\'t a problem:

[user \$ ][ sudo smartctl -A /dev/sdb [COPY TO CLIPBOARD]]

\

    193 Load_Cycle_Count        0x0032   200   200
    000    Old_age   Always       -       721

\

# [This is how we solve the problem]

Ok so you have the problem and want to fix it. Western digital have made a DOS utility to fix it if you ask them for it. Or can find it. Its called wdidle3.exe

But we aren\'t going to use that. Instead we are going to use a Linux unofficial alternative called **idle3-tools**. It is already packaged in Manjaro so no need to compile it. but here is the source [\[2\]](http://idle3-tools.sourceforge.net)

Install **idle3-tools** with pamac or octopi or like this in the terminal:

[user \$ ][ sudo pacman -S idle3-tools [COPY TO CLIPBOARD]]

\

Now check what your drives timer is currently set as. (replace sda if needed with your own drive.):

[user \$ ][ sudo idle3ctl -g /dev/sda [COPY TO CLIPBOARD]]

\

It will likely say it\'s set to 80 \[8sec\]

## [Modify the timer]

In-depth instructions and source of the tool can be found [here](http://idle3-tools.sourceforge.net%7C).

The advisable approach is to simply set the timer to the linux default of 30 seconds (replace sda if needed with your own drive):

[user \$ ][ sudo idle3ctl -s 129 /dev/sda [COPY TO CLIPBOARD]]

\

**Disable the timer (not recommended)**

To just let the system power management handle the drive disable the timer (replace sda if needed with your own drive):

[user \$ ][ sudo idle3ctl -d /dev/sda [COPY TO CLIPBOARD]]

\

## [Power off and verify]

Next step is to shutdown and power off your computer. Rebooting isn\'t enough! You need to power off, so the drive will turn on with the new settings.

Now verify the status:

[user \$ ][ sudo idle3ctl -g /dev/sda [COPY TO CLIPBOARD]]

\

## [Optional step]

Remove idle3-tools and smartmontools with octopi or pamac or in a terminal:

[user \$ ][ sudo pacman -R idle3-tools smartmontools [COPY TO CLIPBOARD]]

\

\
That\'s it! All done. You can now enjoy the reliability and speed from the WD Green drive that you expected to have when you bought it.

\

# [Support]

Following is a link to this page\'s forum counterpart where you can post any related feedback: [\[3\]](https://classicforum.manjaro.org/index.php?topic=17890.0)