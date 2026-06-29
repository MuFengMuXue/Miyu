**[] Deprecated article**\
\

This article is **deprecated (obsolete)**. Contents are [no longer relevant], and are intended for historical reference only!

\
TLDR: **Do not use this article!**

**Resources**

[[]][Home](http://pipelight.net/cms/)

Recently it has become possible to watch Netflix on Linux and FreeBSD via [Wine](https://wiki.gentoo.org/wiki/Wine "Wine") with good performance.

## Contents

-   [[1] [Prequisites]](#Prequisites)
    -   [[1.1] [xattr]](#xattr)
        -   [[1.1.1] [Checking for support]](#Checking_for_support)
        -   [[1.1.2] [Adding support]](#Adding_support)
-   [[2] [Installation]](#Installation)
-   [[3] [Initialization]](#Initialization)
    -   [[3.1] [Microsoft core fonts (optional)]](#Microsoft_core_fonts_.28optional.29)
    -   [[3.2] [Netflix]](#Netflix)
-   [[4] [Troubleshooting]](#Troubleshooting)
    -   [[4.1] [Audio]](#Audio)
-   [[5] [External resources]](#External_resources)

## [Prequisites]

### [xattr]

File system extended attributes are used to keep the precious DRM working, so you'll potentially need to add support in your kernel as well as having your file system mounted explicitly with the option.

#### [Checking for support]

`user `[`$`]`touch ~/.xattr_test && setfattr -n 'user.testAttr' -v 'attribute value' ~/.xattr_test &> /dev/null; getfattr ~/.xattr_test 2>&1 | grep -q user.testAttr && echo 'It works!' || echo 'No workie!'; rm ~/.xattr_test &> /dev/null`

#### [Adding support]

In recent kernel versions there doesn't appear to be an option for ext4 extended attributes, presumably meaning they're always on already.

[KERNEL]

    File systems  --->
       Ext3 journalling file system support
          [*] Ext3 extended attributes
       The Extended 4 (ext4) filesystem
          [*] Ext4 extended attributes

See [Kernel/Upgrade](https://wiki.gentoo.org/wiki/Kernel/Upgrade "Kernel/Upgrade") for in-depth kernel rebuild instructions.

[FILE] **`/etc/fstab`**

    # <fs>         <mountpoint>  <type>        <opts>        <dump/pass>
    /dev/sda3       /       ext4        user_xattr  0 1

If you were only missing the option in [/etc/fstab]:

`root `[`#`]`mount / -o remount`

## [Installation]

Initially, pipelight is only keyworded on **[\~amd64]**. Stable users will need to keyword it. Otherwise, it is a simple emerge command:

`root `[`#`]`emerge --ask www-plugins/pipelight`

## [Initialization]

After the installation just initialize the plugin(s) you want to use. To use Netflix you have to enable Silverlight.

`user `[`$`]`pipelight-plugin --enable silverlight`

Press [Y] to accept the plugin license. Then run Firefox (or your chosen web browser) from the Terminal to check if the plugin will run, i.e. for firefox-bin:

`user `[`$`]`firefox-bin`

Watch the startup in the terminal for any errors. The plugin installation either starts immediately, or when visiting about:plugins in your webbrowser. If there are some errors please check again that you really installed Wine and Pipelight according to this page, if not then proceed with the following steps.

### [][Microsoft core fonts (optional)]

For Wine-Compholio \< 1.7.14 this step was required such that Silverlight works properly (see this [FAQ entry](https://answers.launchpad.net/pipelight/+faq/2441)). With Wine-Compholio 1.7.14 or greater the patchset already includes a [Arial replacement font](https://github.com/compholio/wine-compholio-daily/tree/master/patches/10-Missing_Fonts), which seems to be sufficient for the Silverlight plugin.

To install the Microsoft core fonts for Wine, you can use winetricks; just emerge it:home directory):

`root `[`#`]`emerge --ask winetricks`

Then run it, specifying the Wine prefix used for Pipelight:

`user `[`$`]`WINEPREFIX=$HOME/.wine-pipelight winetricks`

Then select \"[Select the default wineprefix]\" -\> \"[Install a font]\" -\> \"[corefonts]\" and click \"[Okay]\".

### [Netflix]

Install an extension listed at [http://answers.launchpad.net/pipelight/+faq/2351](http://answers.launchpad.net/pipelight/+faq/2351) such as [https://addons.mozilla.org/en-US/firefox/addon/user-agent-switcher/](https://addons.mozilla.org/en-US/firefox/addon/user-agent-switcher/) and configure a Windows UA string, such as this one:[\*](http://answers.launchpad.net/pipelight/+faq/2351)

    Mozilla/5.0 (Windows NT 6.1; WOW64; rv:15.0) Gecko/20120427 Firefox/15.0a1

Enjoy improved Netflix.

## [Troubleshooting]

-   Try different UA strings
-   (Re)Move [\~/.wine-pipelight]
-   (Re)Move [pluginreg.dat] from [\~/.mozilla]. Find it by running:

[find \~/.mozilla/ -name \'pluginreg.dat\']

-   Check paths and other variables in [\~/.config/pipelight-silverlight5.1] (or if nonexistent, [/usr/share/pipelight/configs/pipelight-silverlight5.1])

`root `[`#`]`eselect opengl list`

`root `[`#`]`eselect opengl set #`

### [Audio]

If you use Pulseaudio but find that wine32 is trying to load 64-bit pulseaudio drivers, consider the solution found in this [here](https://forums.gentoo.org/viewtopic-p-7060060.html)

## [External resources]

-   [[[Bug 481596 - use Silverlight apps in browser using Wine]](https://bugs.gentoo.org/show_bug.cgi?id=481596)[]]
-   [FDS-Team](http://fds-team.de/cms/articles/2013-08/pipelight-using-silverlight-in-linux-browsers.html)
-   [Gentoo Forums :: View topic - HOWTO: Install Netflix on Gentoo](https://forums.gentoo.org/viewtopic-t-951092.html)