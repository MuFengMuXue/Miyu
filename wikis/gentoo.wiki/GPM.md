Other languages:

-   [Deutsch](https://wiki.gentoo.org/wiki/GPM/de "GPM (81% translated)")
-   [English]
-   [español](https://wiki.gentoo.org/wiki/GPM/es "GPM (56% translated)")
-   [français](https://wiki.gentoo.org/wiki/GPM/fr "GPM (81% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/GPM/hu "GPM (81% translated)")
-   [русский](https://wiki.gentoo.org/wiki/GPM/ru "GPM (100% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/GPM/zh-cn "GPM (81% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/GPM/ja "GPM (100% translated)")
-   [한국어](https://wiki.gentoo.org/wiki/GPM/ko "GPM (56% translated)")

*Not to be confused with [GDM](https://wiki.gentoo.org/wiki/GNOME/gdm "GNOME/gdm").*

This guide shows you how to set up and use **GPM** (the General Purpose Mouse server) from within a command line interface. This is especially useful for new Gentoo installations or for systems that cannot or do not use an [Xorg](https://wiki.gentoo.org/wiki/Xorg "Xorg") server.

## Contents

-   [[1] [Kernel]](#Kernel)
-   [[2] [Getting GPM]](#Getting_GPM)
-   [[3] [Configuring GPM]](#Configuring_GPM)
-   [[4] [Running GPM]](#Running_GPM)
    -   [[4.1] [OpenRC]](#OpenRC)
    -   [[4.2] [systemd]](#systemd)
-   [[5] [Working with GPM]](#Working_with_GPM)
    -   [[5.1] [Copying and pasting]](#Copying_and_pasting)
    -   [[5.2] [Text-mode browsing and GPM]](#Text-mode_browsing_and_GPM)

## [Kernel]

[KERNEL] **Kernel configuration**

    Device Drivers  --->
      Input device support ---> [CONFIG_INPUT]
        <*/M> Mouse interface   [CONFIG_INPUT_MOUSEDEV]

## [Getting GPM]

If you\'ve just installed Gentoo, you almost certainly don\'t have your mouse set up to work within a command line interface (CLI) yet. Or perhaps you can\'t use or don\'t need an X server, yet you still need to use a mouse. The solution is simple: [[[sys-libs/gpm]](https://packages.gentoo.org/packages/sys-libs/gpm)[]], the General Purpose Mouse server.

First, you will need to get GPM:

`root `[`#`]`emerge --ask sys-libs/gpm`

You might have noticed a few messages during the compilation that warned about configuring the server. You must do this before starting GPM.

## [Configuring GPM]

Before you can use GPM, you will need to uncomment the lines corresponding to the location and protocol of your mouse. You do this by editing the GPM configuration file:

`root `[`#`]`nano /etc/conf.d/gpm`

In the next example, we have a USB mouse on [/dev/input/mouse0]. So, we uncomment [/dev/input/mice], as this is the cumulative device for all mice on the system, and the appropriate protocol. Try using [/dev/input/mice] before [/dev/psaux], as the latter is deprecated and can be disabled in more recent kernels. If [/dev/input/mice] fails, then fall back to other devices. Here is the example [/etc/conf.d/gpm]:

[CODE] **Example GPM config**

    ## (Please uncomment the type of mouse you have and the appropriate MOUSEDEV entry)

    #MOUSE=ps2
    MOUSE=imps2
    #MOUSEDEV=/dev/psaux
    MOUSEDEV=/dev/input/mice

If you have a wheelmouse, you will want to use the imps2 protocol, so uncomment that line. If imps2 and ps2 both fail to work for you, please refer to the GPM info page ([info gpm]) for other protocols to try. Also, if you want to be able to click on hyperlinks in terminals to navigate to a website, it is a good idea to follow the suggestion in the [/etc/conf.d/gpm] file:

[CODE] **Other options**

    ## (Please uncomment this line if you want GPM to understand charsets
    ##  used in URLs and names with ~ or : in them, etc.
    ##  This is a good idea to turn on!)

    APPEND="-l \"a-zA-Z0-9_.:~/\300-\326\330-\366\370-\377\""

The rest of the conf.d file contains other suggestions for your mouse server; uncomment the various options according to your needs. See [man gpm] for more information.

## [Running GPM]

Now that your mouse server is installed and configured, it\'s time to start using it:

### [OpenRC]

`root `[`#`]`/etc/init.d/gpm start`

You should see a block cursor appear. Remember that only root can run the GPM init script. However, to avoid having to [su] and run the script every single time you begin a new session, why not set GPM to begin every time you turn on your computer?

`root `[`#`]`rc-update add gpm default`

Now, whenever you start your computer, you\'ll be greeted by the console cursor by the time you get to the login prompt. The mouse server will continue to run even if you\'re not logged in as root.

### [systemd]

`root `[`#`]`systemctl enable gpm --now`

This will enable the service, and then start it.

## [Working with GPM]

### [Copying and pasting]

Copying and pasting large blocks of text with a working mouse server is very easy. Simply highlight the text with the left mouse button (it will stay highlighted when you release the button), switch to a different terminal if you wish, position the cursor, and press the middle mouse button to paste the text where you placed the cursor. Note that you can copy and paste without ever leaving the terminal you started. This makes posting the output of error messages to the [Gentoo Forums](https://forums.gentoo.org/) extremely simple.

### [Text-mode browsing and GPM]

If you have a message on one screen and a text-mode web browser on the other, you can copy the error message by highlighting it, then change to the other terminal, left-click the appropriate text entry box to select it, and then press the middle mouse button. Your error message can now be posted to the forums.

Though discussion of text-only browsers is somewhat beyond the scope of this guide, inevitably users will need to find a compatible console browser. Though [[[www-client/lynx]](https://packages.gentoo.org/packages/www-client/lynx)[]] is most likely the oldest and well established browser, its interface has poor mouse support and recognition. Instead, try using [[[www-client/links]](https://packages.gentoo.org/packages/www-client/links)[]] which has excellent mouse integration.

`root `[`#`]`emerge --ask www-client/links`

This concludes the guide to using a mouse within the console. Happy mousing!

Authorship information[]

This page is based on a document formerly found on [gentoo.org](https://www.gentoo.org/).\
The following people contributed to the original document: ****\
\
*[Editors: please do **not** add yourself here. Contributions are recorded on each article\'s associated history page, this list is only present to preserve authorship information, as wiki history does not allow for any external attribution.]*