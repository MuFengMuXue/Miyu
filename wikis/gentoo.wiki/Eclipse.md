**[] Archived article**\
\

This article is **archived (obsolete)**. Contents are surely incorrect for current usage, and are intended for historical reference only. *Page archived as of **2025-03-17**.*

\
TLDR: **Do not use this article!**

\

**Resources**

[[]][Home](https://eclipse.org/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Eclipse_(software) "wikipedia:Eclipse (software)")

**Eclipse** is a software development platform including front ends for typically Java development software tools, however a C/C++ front end can also be optionally installed and is called CDT. The installation of CDT is further discussed below.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Overlay]](#Overlay)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Invocation]](#Invocation)
    -   [[2.2] [Install CDT]](#Install_CDT)
-   [[3] [Configuration]](#Configuration)
    -   [[3.1] [Install Update Repository]](#Install_Update_Repository)
    -   [[3.2] [Install CDT Repository]](#Install_CDT_Repository)
-   [[4] [Troubleshooting]](#Troubleshooting)
    -   [[4.1] [\"bundle org.eclipse.rse.ui \... could not be found\" or \"missing remote debug launcher\"]](#.22bundle_org.eclipse.rse.ui_..._could_not_be_found.22_or_.22missing_remote_debug_launcher.22)
    -   [[4.2] [Random crashes happening in native code (C \[libgobject-2.0.so.0+0x1b0b8\] g_object_get_qdata+0x18)]](#Random_crashes_happening_in_native_code_.28C_.5Blibgobject-2.0.so.0.2B0x1b0b8.5D_g_object_get_qdata.2B0x18.29)
-   [[5] [See also]](#See_also)

## [Installation]

### [Overlay]

Use [eselect repository] from [[[app-eselect/eselect-repository]](https://packages.gentoo.org/packages/app-eselect/eselect-repository)[]] to add the [eclipse ebuild repository](https://gitweb.gentoo.org/repo/proj/eclipse.git):

`root `[`#`]`eselect repository enable eclipse`

`root `[`#`]`emerge --sync eclipse`

If needed, see article on [regenerating the Eix cache](https://wiki.gentoo.org/wiki/Eix#Managing_the_cache "Eix"), for those using Eix.

### [Emerge]

Install the Eclipse SDK:

`root `[`#`]`emerge --ask dev-util/eclipse-sdk-bin`

## [Usage]

### [Invocation]

The package is slotted for major Eclipse releases, to be able to have multiple versions installed at the same time.

To run it, simply type the following replacing with the version number installed:

`user `[`$`]`/usr/bin/eclipse-bin-4.6`

In a desktop environment, the different versions should show up automatically in the list of installed applications.

### [Install CDT]

CDT adds C/C++ tools to Eclipse SDK.

Need to first find the latest code name for the latest release of CDT. Go to the following page and take note of the latest code named release. (ie. kepler, indigo, juno, \...)

[http://www.eclipse.org/cdt/downloads.php](http://www.eclipse.org/cdt/downloads.php)

## [Configuration]

### [Install Update Repository]

Go to \"Help \> Install New Software\" and add the following repository after clicking add, and after finding and replacing \"kepler\" with the latest code named repository.

-   Kepler Updates
-   [http://download.eclipse.org/releases/kepler](http://download.eclipse.org/releases/kepler)

This general repository is needed prior trying to add the CDT repository, as the CDT repository depends on other packages outside of the CDT repository and which were not installed by default.

### [Install CDT Repository]

Go to \"Help \> Install New Software\" and click \'add\', adding the following after also replacing the code name with the latest code named repository.

-   CDT 8.2.1 for Eclipse Kepler
-   [http://download.eclipse.org/tools/cdt/releases/kepler](http://download.eclipse.org/tools/cdt/releases/kepler)

Once this repository is entered, go ahead and select it and select all or some of the packages and click next. Eclipse may need to restart afterwards.

## [Troubleshooting]

### [][\"bundle org.eclipse.rse.ui \... could not be found\" or \"missing remote debug launcher\"]

Install the general Update Software repository mentioned above prior to installing CDT in order to satisfy these dependencies. Eclipse SDK should then automatically pull them in.

### [][Random crashes happening in native code (C \[libgobject-2.0.so.0+0x1b0b8\] g_object_get_qdata+0x18)]

See also [[[bug #430432]](https://bugs.gentoo.org/show_bug.cgi?id=430432)[]].

Workaround: Set the gtk+-2 theme to default. This can be limited to eclipse-sdk:

`user `[`$`]`GTK2_RC_FILES=/usr/share/themes/Default/gtk-2.0/gtkrc eclipse-sdk`

## [See also]

[PyCharm Community Edition](https://wiki.gentoo.org/wiki/PyCharm_Community_Edition "PyCharm Community Edition") - A free and open source IDE for Python.