[Translate this page](//wiki.manjaro.org/index.php?title=Special:Translate&group=page-Reactivating+the+Backlight&language=en&action=page&filter= "Special:Translate")

Other languages:

[English](//wiki.manjaro.org/index.php?title=Reactivating_the_Backlight "Reactivating the Backlight (100% translated)") • ‎[Türkçe](//wiki.manjaro.org/index.php?title=Reactivating_the_Backlight/tr "Arka Işığı Yeniden Etkinleştirme (100% translated)") • ‎[français](//wiki.manjaro.org/index.php?title=Reactivating_the_Backlight/fr "Réactivation du rétro-éclairage (100% translated)") • ‎[русский](//wiki.manjaro.org/index.php?title=Reactivating_the_Backlight/ru "Повторное включение подсветки (100% translated)") • ‎[فارسی](//wiki.manjaro.org/index.php?title=Reactivating_the_Backlight/fa "بازفعال‌سازی روشنایی پس‌زمینه (100% translated)") • ‎[中文（中国大陆）‎](//wiki.manjaro.org/index.php?title=Reactivating_the_Backlight/zh-cn "重新激活背光 (100% translated)")

## Contents

-   [[1] [Overview]](#Overview)
-   [[2] [Reactivating the Screen Backlight]](#Reactivating_the_Screen_Backlight)

## [Overview]

Some users - particularly those using laptops - are encountering a problem where the screen brightness is too dim upon replacing Microsoft Windows with a Linux distribution as their main operating system. This is because some unscrupulous hardware manufacturers have coded the BIOS to automatically disable the screen backlight if Windows is not detected running on the system. Fortunately, it is possible to fix this problem by entering a single command in the terminal.

## [Reactivating the Screen Backlight]

This problem can be easily fixed by ensuring that the GRUB bootloader re-activates the backlight. To do this, first open up your terminal, and enter the following command:

[user \$ ][ sudo sed \"s/\\(GRUB_CMDLINE_LINUX=\\)\\\"\\\"/\\1\\\"acpi_osi=Linux acpi_backlight=vendor\\\"/\" /etc/default/grub -i [COPY TO CLIPBOARD]]

\

You will also have to enter your password to continue. Now enter the second and final command:

[user \$ ][ sudo update-grub [COPY TO CLIPBOARD]]

\

Once complete, close the terminal and re-boot your system for the changes to take permanent effect.