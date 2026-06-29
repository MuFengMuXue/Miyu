# Telegram

Telegram is a cloud-based cross-platform instant messaging service with optional end-to-end encryption. Account creation requires a phone number.

## Installation
You can use one of following methods in order to use Telegram:

## Graphical clients
*
*
*
*
*
*

## Web-based clients
Two official browser-agnostic clients exist: Telegram WebK and Telegram WebA, while the Telegram Chrome app for Chromium-based browser is also available. There are also third-party clients:

*
*

## Chat client plugins
Some multi-purpose chat clients provide a plugin for Telegram:

*

## Command-line clients
*
*
*
*
*

## Tips and tricks
## File chooser style
See Qt#Configuration of Qt 5/6 applications under environments other than KDE Plasma

## Wayland support
See GNOME/Troubleshooting#Cursor size or theme issues on Wayland.

See Wayland#Qt for generic instructions.

## xdg-open scheme handler
If you want to use xdg-open for  links and receive an error not finding a handler for , run:

 $ xdg-mime default org.telegram.desktop.desktop application/x-xdg-protocol-tg
 $ xdg-mime default org.telegram.desktop.desktop x-scheme-handler/tg

## Real-time priority
If you get the following error:

Install , add yourself to the  group and reboot. See Realtime process management#Configuring PAM for details.

## HiDPI scaling
If you have Qt scaling enabled on your system, and the scaling factor is not an integer, you may encounter problems like pixelated images and icons. you may need to disable high-DPI scaling for Telegram separately.

Unset  environment variable as follows:

You may need to perform Desktop entries#Update database of desktop entries afterwards.

Also consider disabling Default interface scale in Settings and enabling Enable precise High DPI scaling in Settings -> Advanced -> Experimental settings to avoid incorrect scaling when launch by  (e.g. opening  link).

## Audio backend
As Telegram makes use of OpenAL, it is possible to configure the audio settings by editing its config files, i.e. , or the environment variables listed here.

In case sound is not working due to an invalid audio backend being used, it can be overwritten by setting the environment variable  or the  property in the  section of the OpenAL config. The drivers value  for example would try pulseaudio first and then fallback to the default driver list.

## Fcitx support for Qt 6 Telegram
Telegram-desktop is built against Qt 6 since 3.4.2-2. Users upgrading from an older version might notice Fcitx stop working for this application. To make it work again, install . If using Fcitx5, install .

## Changing the default file browser
Telegram Desktop uses the File Manager DBus Interface to open the file browser. The spec does not allow to choose the preferred one, ensure you have only one file browser installed.

Do not confuse file browsers with file dialogs which are parts of toolkits and is covered by #File chooser style.
