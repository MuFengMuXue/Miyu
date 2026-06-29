[] This article has been flagged for not conforming to the [wiki guidelines](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Guidelines "Gentoo Wiki:Guidelines"). Please [help Gentoo out](https://wiki.gentoo.org/wiki/Help_improve_Gentoo_by_getting_involved_with_documentation!#Make_articles_conform_to_the_guidelines "Help improve Gentoo by getting involved with documentation!") by starting fixing things.

[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Gpib&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

## Contents

-   [[1] [Linux Gpib Howto in Gentoo]](#Linux_Gpib_Howto_in_Gentoo)
-   [[2] [Installing linux-gpib]](#Installing_linux-gpib)
-   [[3] [Configuring linux-gpib]](#Configuring_linux-gpib)
-   [[4] [Example Python]](#Example_Python)

###### [Linux Gpib Howto in Gentoo]

linux-gpib with python flags is using python 2.7

##### [Installing linux-gpib]

First set use flags in [/etc/portage/package.use]:

`user `[`$`]`sudo vim /etc/portage/package.use`

Add line for python bindings and Documentation:

[FILE] **`/etc/portage/package.use`**

    sci-libs/linux-gpib python doc

Other possible Flags *pcmcia static debug guile perl php tcl firmware*. If you want to use *pcmia* you need to have a 2.7 kernel. But *pcmia* is normally just used in old computers so it doesn\'t matter.

Install it with:

`root `[`#`]`emerge --ask sci-libs/linux-gpib`

Add your user to gpib group

`root `[`#`]`gpasswd -a user gpib`

##### [Configuring linux-gpib]

To configure Linux GPIB you need first to create a config file at [/etc/gpib.conf]:

`root `[`#`]`vim /etc/gpib.conf`

Just an example which is for NI USB- HS Adapter is:

\

[FILE] **`/etc/gpib.conf`**

    interface

\
You can lookup the board_type at [Linux-gpib-Website](http://linux-gpib.sourceforge.net/doc_html/x259.html).

\
There is an example config file with more parameters on [GPIB-Linux Website](http://linux-gpib.sourceforge.net/doc_html/r23.html).

After you wrote your own config file, you have to plug in your GPIB Device and either first chgrp the gpib Devices in [/dev/] and make them write and readable:

`root `[`#`]`chgrp gpib /dev/gpib* `

`root `[`#`]`chmod g+wr /dev/gpib* `

or do all things as root.

After doing that you should be able to call with root

`root `[`#`]`/usr/sbin/gpib_config -m 0`

0 is the device you plugged in.

##### [Example Python]

Be carefull linux-gpib cames with python2.7 bindings so first start python2.7

`user `[`$`]`python2.7`

This example is tested with a HP8720D

To import gpib:

`>>>``import gpib`

To get a device of a board named in [/etc/gpib.conf] joe:

`>>>``con=gpib.dev(0,16)`

0 is the GPIB BOARD and 16 the Adress of the Listener

To write a command:

`>>>``gpib.write(con,'STAR2400MHZ;')`

or more universal

`>>>``gpib.write(con,'*IDN?')`

To read the result:

`>>>``gpib.read(con,1000)`

1000 is the Number of byte that are read