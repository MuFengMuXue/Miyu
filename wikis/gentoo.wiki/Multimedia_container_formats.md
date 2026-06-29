[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Multimedia_container_formats&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Wikipedia](https://en.wikipedia.org/wiki/Container_format#Multimedia_container_formats "wikipedia:Container format")

For a computer novice or any person unfamiliar with the technical details of multimedia production, transmission, and *even* consumption, understanding how to view certain media can be quite a challenge. This article adds clarity and insight for end-users (generally on desktop profiles) on how enable Gentoo to display multimedia.

## Contents

-   [[1] [Introduction]](#Introduction)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Discovery]](#Discovery)
-   [[3] [See also]](#See_also)

## [Introduction]

Under the surface, multimedia (video, audio, or both) is generally shipped in a [container format](https://en.wikipedia.org/wiki/Container_format_(computing) "wikipedia:Container format (computing)"). These container formats have various names and can hold various multimedia content (codecs).

The three most relevant multimedia formats on Gentoo are (links to Wikipedia for each entry):

1.  [Audio file formats](https://en.wikipedia.org/wiki/Audio_file_format "wikipedia:Audio file format")
2.  [Image file formats](https://en.wikipedia.org/wiki/Image_file_format "wikipedia:Image file format")
3.  [Video file formats](https://en.wikipedia.org/wiki/Video_file_format "wikipedia:Video file format")

For example, in 2017 Apple started using the [High Efficiency Image File Format (HEIF)](https://en.wikipedia.org/wiki/High_Efficiency_Image_File_Format "wikipedia:High Efficiency Image File Format") to store photos (digital images) that were saved using a [.heic] file extension. This same format can also be enabled for photo storage on Android. Without the proper USE flags enabled and supporting libraries (packages) installed, viewing HEIF coded files ([.heic] files) will not be possible on Gentoo.

## [Configuration]

Depending on the container format desired, a search can be performed in order to determine what packages and USE flags correspond to the container format and the codecs.

### [Discovery]

For example, supposing a system administrator desired to enable HEIF support so that photos taken on an iPhone or Android device could be viewed while using the [GNOME](https://wiki.gentoo.org/wiki/GNOME "GNOME") desktop environment. The system administrator could [use packages.gentoo.org to perform a heif USE flag search](https://packages.gentoo.org/useflags/search?q=heif) to see if any `heif` or `heic` USE flags are available for any packages.

Alternatively a system administrator could also search the local system using the [quse] command (included with [[[app-portage/portage-utils]](https://packages.gentoo.org/packages/app-portage/portage-utils)[]]):

`user `[`$`]`euse heif`

Ah! A search on both packages.g.o and the local system revealed that an `heif` USE flag is supported by some packages, and the `heic` USE flag does not exist.

To ease support, the `heif` USE flag can be added for all installed packages (globally) via a [make.conf] addition:

[FILE] **`/etc/portage/make.conf`**

    USE="heif"

In order for the package manager to recognize this change for already installed packages, a [world set](https://wiki.gentoo.org/wiki/World_set_(Portage) "World set (Portage)") rebuild is necessary:

`root `[`#`]`emerge --update --deep --changed-use @world`

## [See also]

-   [HEIF](https://wiki.gentoo.org/wiki/HEIF "HEIF") --- provides configuration information to add HEIF container format support to [desktop environments](https://wiki.gentoo.org/wiki/Desktop_environment "Desktop environment") supporting its integration.