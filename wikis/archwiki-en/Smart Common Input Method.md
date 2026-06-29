# Smart Common Input Method

SCIM is an input method framework developed by Su Zhe (or James Su) around 2001, similar to IBus or Uim.

Its stated goals are to:
* Act as an unified front-end for current available input method libraries. Currently bindings to uim and m17n library are available.
* Act as a language engine of IIIMF input method framework.
* Provide as many native IMEngines as possible.
* Support as many input method protocols/interfaces as possible.
* Support as many operating systems as possible.

## Installation
Install the  package.

## Input method engines
Currently the SCIM project has a wide range of input methods (some may need other libraries), covering more than 30 languages, including (Simplified/Traditional) Chinese, Japanese, Korean and many European languages. These are some of the examples (more can be found here):

*  - Chinese
*  - Chinese Smart PinYin .
*  - Chinese WuBi or other tables based
*  - Korean

uim can be used as an engine for SCIM by using .

## Configuration
Configuring SCIM correctly requires the following three steps:
# Exporting some environment variables that specify the used input method.
# Modifying locale related files.
# Finally, starting SCIM.

## A simple scenario
If you just need SCIM to work urgently in any desktop environment or window manager, put these lines into your xprofile and then reboot:

These lines can be added to other files that are run at startup, such as: , ,  or  (when using Openbox).

This is a very basic example for configuring XIM (X Input Method) to work with SCIM. XIM is not recommended because it has quite some limitations.

## Note for GTK
If you use GNOME, edit  by adding follow content at the end:

If your  or  is en_US.UTF-8, change  to .

After making those changes, be sure to reboot. You can find out what input method modules are available on your system by executing .

If SCIM does not work with GTK applications after these changes, check that the GTK_IM_MODULE_FILE environment variable is set to .

You can use another file (in this example ) that contains the necessary information about input methods modules by adding these lines in the file you selected in the section above.
 gtk-query-immodules-2.0 > ~/.immodules
 export GTK_IM_MODULE_FILE=~/.immodules

## Locale-related files
If your keyboard locale is not  (or ), you have to modify the first line of  (or  to apply these settings to all users) according to the following example:

 /SupportedUnicodeLocales = en_US.UTF-8,de_CH.UTF-8

and replace your  with your locale.

If you do not know which locales you have active at the moment, you can check it:

 locale -a

(alternatively you can look at ).

## Further troubleshooting with locales
If after you have install SCIM and the necessary input tables, SCIM still does not work, then you need to set the  environmental variable in  to the locale you plan to use. Simply create an entry for LC_CTYPE such as:
 LC_CTYPE="zh_CN.UTF-8"              # if you want to type simplified chinese

Finally you need to generate the locale using the  command.

## Executing SCIM
SCIM can be run by just executing the  command, although it is common to start SCIM as a daemon:
 scim -d

You can put the above command in a script file and execute it automatically. Usual places are  (after environment variables and before DE/WM),  (after environment variables) or  (after environment variables and possibly after some sleep command).

## Note for GNOME
In case you use GNOME as your desktop environment, the command above does not seem to work as expected. Instead, you have to execute the following:

  scim -f x11 -c simple -d

If you want SCIM to start automatically at startup, go to System > Preferences > Session and create a new command with the line above.

## Note for KDE
In case you use KDE as a desktop environment, the command above does not seem to work as expected. Instead, you have to execute the following:
  scim -f socket -c socket -d

## Troubleshooting
## LWJGL (Lightweight Java Game Library) losing keyboard focus
Turn off SCIM or restart it after the program using LWJGL has started.=== Chrome/Chromium does not take input ===

Edit the .xinitrc or .xsession file.

This is a rather sloppy workaround. Also, even with this workaround, Korean users may find scim unusable with Chrome/Chromium, as the preedit string disappears when the space bar or other modifier keys are pressed at the end of a word.
