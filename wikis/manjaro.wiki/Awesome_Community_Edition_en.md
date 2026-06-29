[Translate this page](//wiki.manjaro.org/index.php?title=Special:Translate&group=page-Awesome+Community+Edition&language=en&action=page&filter= "Special:Translate")

Other languages:

[English](//wiki.manjaro.org/index.php?title=Awesome_Community_Edition "Awesome Community Edition (100% translated)") • ‎[Türkçe](//wiki.manjaro.org/index.php?title=Awesome_Community_Edition/tr "Harika Topluluk Sürümü (19% translated)") • ‎[русский](//wiki.manjaro.org/index.php?title=Awesome_Community_Edition/ru "Редакция сообщества Awesome (100% translated)") • ‎[فارسی](//wiki.manjaro.org/index.php?title=Awesome_Community_Edition/fa "ویرایش اجتماع کاربری Awesome (62% translated)")

## Contents

-   [[1] [Getting started]](#Getting_started)
-   [[2] [Known issues]](#Known_issues)
    -   [[2.1] [Screen resolution does not resize with VirtualBox]](#Screen_resolution_does_not_resize_with_VirtualBox)
-   [[3] [Differences between Manjaro Xfce and Manjaro Awesome]](#Differences_between_Manjaro_Xfce_and_Manjaro_Awesome)
-   [[4] [Maintainer]](#Maintainer)
-   [[5] [Acknowledgments]](#Acknowledgments)

This community edition is tailored to power users. Default configurations are such that the tools are friendly to newcomers.

## [Getting started]

[Download the ISO here](https://manjaro.org/downloads/community/awesome/) and install:

-   On the LiveCD, the password is \"manjaro\".
-   The installer can be found on the menu on top left -\> \"System Tools\" -\> \"Install Manjaro Linux\".
-   There\'s a [caveat when installing in VirtualBox](#Known_issues).

If you\'re new to Awesome, a [short tutorial can be found here](https://scaron.info/blog/getting-started-with-awesome.html).

## [Known issues]

### [Screen resolution does not resize with VirtualBox]

There\'s an issue with the video driver support for VirtualBox. In the virtual machine settings, under \"Display\", change the graphics controller to \"VBoxVGA\" *before installing*. If you do it after, this will result in a black screen.

## [Differences between Manjaro Xfce and Manjaro Awesome]

Replaced applications:

-   xfwm4 → awesome
-   bash → zsh
-   lightdm-gtk-greeter → lightdm-slick-greeter
-   xfce4-terminal → lxterminal
-   qpdfview → zathura
-   viewnior → ristretto

## [Maintainer]

Frank Kusters. I can be reached on the [Manjaro forum](https://forum.manjaro.org/u/frankk/).

## [Acknowledgments]

Hat tip goes to Matti Hyttinen and Thanos Apostolou as previous maintainers.