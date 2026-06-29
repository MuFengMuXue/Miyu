# KeePass

KeePass is an encrypted password database format. It is an alternative to online password managers and is supported on all major platforms.

There are two versions of the format: KeePass 1.x (Classic) and KeePass 2.x

## Installation
There are three major implementations of KeePass available in the official repositories:

*
*
*

Other lesser-known alternatives can be found in the AUR:

*
*
*
*
*
*

## Integration
Many plugins and extensions are available for integrating KeePass to other software. KeePassX and KeePassXC do not have a plugin interface, but KeePassXC has various integrations built-in.

## Plugin installation in KeePass
KeePass is by default installed at . Copy  to a plugins sub-directory under the KeePass installation directory as demonstrated below:

## Browser integration
## keepassxc-browser for KeePassXC
keepassxc-browser is the browser extension of KeePassXC’s built-in browser integration using native-messaging and transport encryption using libsodium. It was developed to replace KeePassHTTP, as KeePassHTTP’s protocol has fundamental security problems.

The developers provide the browser extension on

* Firefox Add-ons (for Firefox and Tor Browser) and
* in the chrome web store (for Chromium, Google Chrome, Vivaldi and Brave).

Support for Firefox and Chromium forks is available. For , open KeePassXC, go to Tools > Settings > Browser Integration > Advanced > Config Location:, and add .

The source code and an explanation how it works can be found on GitHub, the KeePassXC developers provide a configuration guide on their website.

## KeePassRPC and Kee
Kee (GitHub repo) is a browser extension for Firefox and Chromium which integrates KeePass through KeePassRPC, a KeePass plugin from the same developers.

The KeePass plugin is available from GitHub or from the AUR ().

The browser extension can be found on GitHub, Firefox Add-ons and the chrome web store.

## Via autotype feature
An alternative to having a direct channel between browser and KeePass(XC) is using the autotype feature.

To enable the autotype feature on Wayland, force KeePass(XC) to fallback to X11. Edit  and change the value of  to . Alternatively, set the  environment variable before launching KeePassXC. However, native Wayland applications will not work with autotype. For example, autotype works when running Firefox without Wayland, but not with.

There are browser extensions which support this way by putting the page URL into the window name:

* KeePass Helper or TitleURL for Firefox
* URL in title for Chromium

## Yubikey
YubiKey can be integrated with KeePass thanks to contributors of KeePass plugins. KeepassXC provides built-in support for Yubikey Challenge-Response without plugins.

## Configuration with KeePass
For an explanation of the configuration options, see https://keepass.info/help/kb/yubikey.html.

# StaticPassword
#:Configure one of Yubikey slots to store static password. You can make the password as strong as 65 characters (64 characters with leading "!"). This password can then be used as master password for your KeePass database.
# One-time passwords (OATH-HOTP)
## Download plugin from KeePass website: https://keepass.info/plugins.html#otpkeyprov
## Setup the Yubikey OATH-HOTP slot (program the same, if a backup Yubikey is used)
## In advanced mode untick OATH Token Identifier
## In KeePass additional option will show up under Key file / provider called One-Time Passwords (OATH HOTP)
## Copy secret, key length (6 or 8), and counter you set
## You may need to setup Look-ahead count option to something greater than 0, please see this thread for more information
## See this video for more help
#Challenge-Response (HMAC-SHA1)
## Get the plugin from AUR:
## In KeePass additional option will show up under Key file / provider called Yubikey challenge-response
## Plugin assumes slot 2 is used

## SSH agent
KeePassXC offers SSH agent support, a similar feature is also available for KeePass using the KeeAgent plugin.

The feature allows to store SSH keys in KeePass databases, KeePassXC/KeeAgent acts as OpenSSH Client and dynamically adds and removes the key to the Agent.

The feature in KeePassXC is documented in its FAQ. First configure SSH agent to start on login and make sure the  variable is set. Then logout and log back in. Now, in KeePassXC settings, enable SSH agent integration. The  value exposed in the UI should correspond to what you configured earlier.

## Secret Service
KeePassXC contains a Freedesktop.org Secret Service integration. It will allow external applications to use KeePassXC as an encrypted database (a.k.a. as a vault, wallet, or keyring) to store user credentials (e.g., messaging applications, games).

It can be enabled by going into the settings (under the Tools menu), and selecting which group(s) you want to share (for each database, open Database > Database Settings..., then go to the Secret Service Integration tab).

KeePassXC will refuse to enable its integration if it detects that another program (such as GNOME/Keyring) is already providing that service. You should first stop that program (for example, by stopping  user unit for ). Note that you will likely want to disable the program permanently, otherwise KeePassXC's integration will fail on the next reboot (for example, by disabling the  of a systemd/User for ).

An application that requests access to the database will connect to KeePassXC through D-Bus, where KeePassXC will be "seen" just as GNOME libsecret by the application. The database that will be exposed can be stored anywhere on the disk, just like any other KeePassXC database, and the master password of this database will be the one to type when applications will want to retrieve a credential in the future.

## Autostart
KeePassXC will not be automatically started when an application requests secrets, which may cause them to break. A D-Bus auto-start file can be created:

{{hc|${XDG_DATA_HOME:-$HOME/.local/share}/dbus-1/services/org.freedesktop.secrets.service|2=
Service
Name=org.freedesktop.secrets
Exec=/usr/bin/keepassxc
}}

## Tips and tricks
## Disable your clipboard manager
If you are an avid user of clipboard managers, you may need to disable your clipboard manager before you launch Keepass and then re-start your clipboard manager afterwards.

KeePassXC implementations has the option to auto-clear the clipboard manager after an amount of time, enough to paste copied items.

## Dark theme
To enable the dark theme for KeePass, install . After installation, the plugin will get compiled upon starting KeePass. It can then be activated via Tools > Dark Theme, or by pressing .

## Synchronization
Without using specialized plugin, a KeePass database is well-suited to be synchronized through Syncthing. On conflicts, some applications provides a way to resolve them, such as the Merge from database feature of KeePassXC.

## Troubleshooting
## User interface scaling issues with KeePassXC 2.6
If the user interface elements are not scaled properly, see HiDPI#Qt 5 and upstream bug report.

## Greyed-out options
Some options like Start minimized and locked may appear greyed-out. According to a discussion on SourceForge, since version 2.31, KeePass has disabled two options because of their broken behaviors on Mono.

To force these features to be enabled, launch KeePass with the  argument.

## Wrongly scaled tray icons
In some desktop environments, the tray icon of KeePass may appear too big or too small due to Mono's bug, according to a bug report on SourceForge.

Keebuntu contains three plugins to provide desktop integration:

* : For Cinnamon and MATE;
* : For Plasma and GNOME with ;
* keepass2-plugin-launcher: For the  dock.

After installing one of these plugins, it is sometimes necessary to hide the original tray icon to prevent duplicate icons in the system tray.

## Secret Service Integration
First, check that the group under which your passwords are stored is exposed; the Tools > Settings menu contains a list of groups enabled for each database. If a database isn't exposing the proper group, select its tab, open Database > Database Settings..., then select the group in the Secret Service Integration tab).

Note that merging a database can cause it to stop exposing any groups.

## Graphical glitches with KeePassXC, Plasma6 and Wayland
If you are experiencing graphical glitches, install the  and  packages. KeePassXC (as of version v2.7.7) still uses Qt5.
