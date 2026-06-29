[Translate this page](//wiki.manjaro.org/index.php?title=Special:Translate&group=page-Set+all+Qt+app%27s+to+use+GTK%2B+font+%26+theme+settings&language=en&action=page&filter= "Special:Translate")

Other languages:

[English](//wiki.manjaro.org/index.php?title=Set_all_Qt_app%27s_to_use_GTK%2B_font_%26_theme_settings "Set all Qt app's to use GTK+ font & theme settings (100% translated)") • ‎[Türkçe](//wiki.manjaro.org/index.php?title=Set_all_Qt_app%27s_to_use_GTK%2B_font_%26_theme_settings/tr "Tüm Qt uygulamalarını GTK+ yazı tipi ve tema ayarlarını kullanacak şekilde ayarlayın (92% translated)") • ‎[español](//wiki.manjaro.org/index.php?title=Set_all_Qt_app%27s_to_use_GTK%2B_font_%26_theme_settings/es "Configure todas las aplicaciones Qt para usar la configuración de fuente y tema GTK+ (92% translated)") • ‎[русский](//wiki.manjaro.org/index.php?title=Set_all_Qt_app%27s_to_use_GTK%2B_font_%26_theme_settings/ru "Настройка всех приложений Qt на использование шрифтов и тем GTK+ (100% translated)") • ‎[فارسی](//wiki.manjaro.org/index.php?title=Set_all_Qt_app%27s_to_use_GTK%2B_font_%26_theme_settings/fa "تنظیم همهٔ برنامه‌های کیوت برای استفاده از قلم و زمینهٔ +GTK (92% translated)")

## Contents

-   [[1] [Overview]](#Overview)
-   [[2] [Using qt5ct]](#Using_qt5ct)
-   [[3] [See Also]](#See_Also)

### [Overview]

When using a [Desktop Environment](//wiki.manjaro.org/index.php?title=Desktop_Environments "Desktop Environments") or Window Manager that doesn\'t allow for the settings of QT themes, you can set QT to use your GTK themes instead.

### [ ]

Using qt5ct

**note**

------------------------------------------------------------------------

In some Manjaro editions, this is already done for you by default

\
Install `qt5ct` using your favorite package manager or the command:

[user \$ ][ pamac install qt5ct [COPY TO CLIPBOARD]]

\

\
Set environment variables in `~/.profile` by adding or updating the following lines:

\~/.profile

    export QT_QPA_PLATFORMTHEME="qt5ct"

\
Run the application **QT5 Configuration Manager** from the menu or run the command `qt5ct`.

\

Logout and login again to make the change effective

### [ ]

[![Chmsee-icon.png](/images/thumb/8/81/Chmsee-icon.png/36px-Chmsee-icon.png)](//wiki.manjaro.org/index.php?title=File:Chmsee-icon.png)

See Also

-   [Arch Wiki](https://wiki.archlinux.org/index.php/Uniform_Look_for_Qt_and_GTK_Applications)