[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=MCUXpresso&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://www.nxp.com/design/software/development-software/mcuxpresso-software-and-tools-/mcuxpresso-integrated-development-environment-ide:MCUXpresso-IDE)

This page describes the installation of **MCUXpresso** from NXP, which is a integrated development environment for some NXP microcontrollers.

** Tip**\
This already contains the \"Config Tools\", so there is no need for installing them separately.

## Contents

-   [[1] [Installation]](#Installation)
-   [[2] [Requirements]](#Requirements)
    -   [[2.1] [Installing MCUXpresso on Debian]](#Installing_MCUXpresso_on_Debian)
    -   [[2.2] [Extract relevant files on Debian]](#Extract_relevant_files_on_Debian)
    -   [[2.3] [Install relevant files on Gentoo]](#Install_relevant_files_on_Gentoo)
-   [[3] [Usage]](#Usage)

## [Installation]

** Warning**\
This software may cause unwanted damage to the system as it is not contained in an ebuild

NXP does not provide a tarball of MCUXpresso for Gentoo, but some kind of packed script for Debian and alikes. A circumvention is necessary to get the files necessary for the actual installtion on Gentoo via a installation on a debian-alike system.

## [Requirements]

A Debian (or debian-alike distribution) system at your disposal, can also be virtual. For simplification, this installation or PC will be called \"Debian\" in the further text.

### [Installing MCUXpresso on Debian]

1\. Download the .deb.bin file from the software supplier ([https://www.nxp.com/design/software/development-software/mcuxpresso-software-and-tools-/mcuxpresso-integrated-development-environment-ide:MCUXpresso-IDE](https://www.nxp.com/design/software/development-software/mcuxpresso-software-and-tools-/mcuxpresso-integrated-development-environment-ide:MCUXpresso-IDE))

2\. Make the file executable

`user `[`$`]`chmod u+x mcuxpresso.deb.bin`

3\. Start the installation as root and have it guide you through

`root `[`#`]`./mcuxpresso.deb.bin`

Now the installation on Debian is complete.

**Alternative**: launch the following command and extract the mcuxpresso\*.deb file. Then extract the data.tar.gz file to find the files we for installation below. This allows to skip \"Extract relevant files on Debian\" but needs you to copy the files to /usr and /lib.

`root `[`#`]`./mcuxpresso.deb.bin --keep`

### [Extract relevant files on Debian]

1\. Collect the relevant files

`root `[`#`]`tar -czf mcuxpressodump.tar.gz /usr/lib/udev/rules.d/56-pemicro.rules /usr/lib/udev/rules.d/60-dfu-util.rules /usr/lib/udev/rules.d/85-mcuxpresso.rules /usr/local/mcuxpressoide-11.2.1_4149 /usr/share/applications/com.nxp.mcuxpressoide.desktop`

2\. Copy the files to your Gentoo installation

### [Install relevant files on Gentoo]

Now switch to your Gentoo installation.

**Hint: JLink will not be contained in the files copied, therefore, if you need it, please install it separately now. It is available as a tarball from the supplier\'s webpage.**

1\. Extract the files to the relevant paths

`root `[`#`]`tar -xzf mcuxpressodump.tar.gz`

2\. Set everything up

`root `[`#`]`# Set the permissions `

`root `[`#`]`chmod 777 /usr/local/mcuxpressoide-11.2.1_4149 -R `

`root `[`#`]`# Create soft link for consistency with a debian installation `

`root `[`#`]`ln -s /usr/local/mcuxpressoide-11.2.1_4149 /usr/local/mcuxpressoide `

`root `[`#`]`# Create soft link for launching from commandline / rofi / dmenu etc. `

`root `[`#`]`ln -s /usr/local/mcuxpressoide/ide/mcuxpressoide /usr/bin/mcuxpressoide`

## [Usage]

Use the desktop launcher or the command line:

`user `[`$`]`/usr/bin/mcuxpressoide`