Other languages:

[English] • ‎[español](//wiki.manjaro.org/index.php?title=Set_all_Java_apps_to_use_GTK%2B_font_%26_theme_settings/es "Configure todas las aplicaciones Java para usar la configuración de fuente y tema GTK+ (100% translated)") • ‎[français](//wiki.manjaro.org/index.php?title=Set_all_Java_apps_to_use_GTK%2B_font_%26_theme_settings/fr "Configurer toutes les applications Java pour qu'elles utilisent les polices et les thèmes GTK (100% translated)") • ‎[русский](//wiki.manjaro.org/index.php?title=Set_all_Java_apps_to_use_GTK%2B_font_%26_theme_settings/ru "Настройка всех Java-приложений на использование шрифтов и тем GTK+ (100% translated)") • ‎[فارسی](//wiki.manjaro.org/index.php?title=Set_all_Java_apps_to_use_GTK%2B_font_%26_theme_settings/fa "تنظیم همهٔ برنامه‌های جاوا برای استفاده از قلم و زمینهٔ +GTK (83% translated)")

## Contents

-   [[1] [Introduction]](#Introduction)
-   [[2] [How do you do it?]](#How_do_you_do_it.3F)
-   [[3] [See Also]](#See_Also)

### [Introduction]

This fix makes your Java apps use your GTK+ theme (colours & such) & your chosen font settings. Here is how it looks like:

\

[![](/images/thumb/c/ca/Java_default_look.png/400px-Java_default_look.png)](//wiki.manjaro.org/index.php?title=File:Java_default_look.png)

[](//wiki.manjaro.org/index.php?title=File:Java_default_look.png "Enlarge")

Before the fix

[![](/images/thumb/9/98/Java_GTK_look.png/400px-Java_GTK_look.png)](//wiki.manjaro.org/index.php?title=File:Java_GTK_look.png)

[](//wiki.manjaro.org/index.php?title=File:Java_GTK_look.png "Enlarge")

After the fix

### [][How do you do it?]

Set the variable **\_JAVA_OPTIONS** by running this command in a terminal:

    export _JAVA_OPTIONS="-Dawt.useSystemAAFontSettings=on -Dswing.aatext=true -Dswing.defaultlaf=com.sun.java.swing.plaf.gtk.GTKLookAndFeel -Dswing.crossplatformlaf=com.sun.java.swing.plaf.gtk.GTKLookAndFeel $"

First test to see if the outcome is what you expect by running your Java app from the same terminal window.

If the result looks good to you, let us make the changes permanent:

Append the above definition of the **\_JAVA_OPTIONS** variable to **\~/.profile** (for your user only) or **/etc/profile.d/90-java_ops.sh** (system-wide). In both cases, if the file does not exist, create it.

### [ ]

[![Chmsee-icon.png](/images/thumb/8/81/Chmsee-icon.png/36px-Chmsee-icon.png)](//wiki.manjaro.org/index.php?title=File:Chmsee-icon.png)

See Also

-   [How can I get a java apps to use the GTK+ theme?(askubuntu)](http://askubuntu.com/questions/21886/how-can-i-get-a-java-apps-to-use-the-gtk-theme)