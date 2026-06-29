# Citrix

Citrix Workspace App (previously known as Citrix Receiver and ICA Client) is the client component of XenDesktop (desktop virtualization software) and XenApp (application virtualization software), developed by Citrix Systems.

## Components
The Citrix client for Linux is made up of several different components that support different functionalities

## Wfica
## Storebrowse
## USB device sharing daemon
## Browser Extension
## Citrix "Light" (HTML5)
The Citrix web portal offers a selection between the client installed by the  and  packages or a "light" version, which is an in-browser HTML5 client.

When the non-light version is selected, launching an app or desktop will download an  file which will presumably be opened by xdg-open via mimetype association, launching wfica with that file as a parameter.

When attempting to change between light and non-light clients, the web portal runs a "detection" process that consists of attempting to open a  URL in hopes that it launches #Wfica with some (undocumented?) parameters that cause it to reach out to the server and confirm it's existence. An example url:

Base64 decoding the last part of the path (without the trailing ) yields some parameters:

## MIME Associations
*  - ini-style files that wfica uses to launch and connect to remote applications and desktops.
*  XML file describing a Citrix Store. Launched with  to add the described Store to the local client. Example content:

*  URL schema associated with Citrix web portal's discovery of local clients

## Installation
Install the  package. It includes the  file, so Arch knows how to open ica files.

## TLS/SSL Certificates
Because ICAClient uses SSL you may need a security certificate to connect to the server, check with the server administrator. If there is a certificate download and place it in .

You may then receive the error .

There may be several reasons for this:

; You do not have the root Certificate Authority (CA) certificates.
: These are already installed on most systems, they are part of the core package , but they are not where ICAClient looks for them. Since versions 13.1, Citrix needs the certificates in separate files. You need to run the following commands as root:
{{bc|1=
# cd /opt/Citrix/ICAClient/keystore/cacerts/
# cp /etc/ca-certificates/extracted/tls-ca-bundle.pem .
# awk 'BEGIN {c=0;} /BEGIN CERT/{c++} { print > "cert." c ".pem"}'  /usr/lib/libX11.so.6 (0x00007fe4401d9000)
        }}
As you can see, the nsgcepa executable (which is the main executable of nsepa) has been linked to a libcurl.so.4 that contains the "CURL_OPENSSL_3" symbol. I think this is a patched version from Ubuntu and I could not find an Arch package providing it, not even . Unfortunately you have to find an appropriate lib for yourself. I found one in the Steam runtime under .

* Troubleshooting-Step 1. Create a directory for patched library files and copy libcurl.so.4 into it. Also copy dependencies.

* Troubleshooting-Step 2. In order to use these libs instead of your system's libs, we have to fiddle with the way nsgcepa is being called. There is a .desktop file provided in the nsepa package for that: . Change the Exec line to:

* Troubleshooting-Step 3. The .desktop file had already been copied to where the system expects it to be: . Overwrite it with your new one.

Now go to you company's Citrix URL again. The EPA should run. If it does not, you should check if the protocol handler for "nsgcepa://" works: If it answers "gio: nsgcepa://something.com: The specified location is not supported" or "klauncher said: Unknown protocol 'nsgcepa'" you need to add the protocol handler manually:
If the EPA still fails you should ask your company's Citrix Netscaler admins if they have disabled Linux logins completely. It seems like there is no corresponding error message for that case, instead the error message is the same as if you do not have installed the EPA plugin at all.

## Tips and tricks
## Remember Sign out/Disconnect preference
If clicking 'Disconnect' always asks you wether to disconnect or sign out, add  in  anywhere in the  section. Then only 'Disconnect' is available, and the choice can be remembered. See https://docs.citrix.com/en-us/citrix-workspace-app-for-linux/session-experience.html#enable-sustainability-feature

## Create .desktop entries for Subscribed Desktops and Applications
The #Storebrowse component can generate .desktop files for Desktops and Applications that have been "subscribed to" (starred in the interface).

 $ storebrowse https://mystore.example.com --subscribed --details 0x100000

The same command can be used to remove them by passing a slightly different value to :

 $ storebrowse https://mystore.example.com --subscribed --details 0x200000

The values for the  flag can be found in the [https://docs.citrix.com/en-us/citrix-workspace-app-for-linux/storebrowse#details Storebrowse documentation

## Troubleshooting
* If you have issues opening a Citrix connection under Firefox you may need to set the Citrix Receiver plugin to 'Always Activate' under the Firefox Add-ons Manager plugin settings.
* If Firefox downloads the .ica file instead of opening Citrix, go to Settings > General > Files and Applications and choose 'Ask whether to open or save files' under Applications.
*  may be required to correctly interpret the .ica file mimeinfo and open it as per the setup in .
* If you have cursor alignment issues under Citrix and you have multiple displays connected to your machine you may need to disable all but one when using Citrix.
* If you have sticky Control Ctrl key issues after logging to session you may resolve it using this guide
* On i3, Citrix might go full screen and grab all keyboard input. A workaround is to disable full screen mode. See https://bbs.archlinux.org/viewtopic.php?id=242398.

* If  does not work in a remote Citrix session on GNOME Wayland, these two settings will enable key passthrough.

 $ gsettings set org.gnome.mutter.wayland xwayland-grab-access-rules "'Wfica'"
 $ gsettings set org.gnome.mutter.wayland xwayland-allow-grabs true

* If ICAClient is flooding the journal with error messages, a simple fix is to disable all logging in Citrix Workspace Preferences.
* If your timezone inside the VDI is reset to UTC when starting session from Firefox, you might need to go to  and set . This feature spoofs the browser's timezone to UTC which is then redirected to the Citrix session.

Note: at the time of writing the  setting cannot be used to exclude your company's self-service portal because it's still under testing and not fully working. This might not be the case in the future anymore.

## Chromium/Google Chrome
If you have problems launching Citrix applications with Chromium, just go to  and disable "Citrix Receiver for Linux".

## Log file fills disk when using Smartcard
At time of writing (Jan 2026), the Smartcard component is configured to log traces by default, writing many lines to  per second about polling the Smartcard, eventually filling up the disk. This log level is not controlled by Citrix's normal logging settings.

Instead, you have to change this in  by setting the  key to :

## Microsoft Teams audio redirection troubleshooting
Citrix VDIs have a special Teams client "Optimized for Citrix." This client redirects audio and video to be rendered on the client via webrtp.

Logs for this redirection are written to  with no apparent way to change their location.

## Audio devices detected by Windows, but not by MS Teams
Check whether the HdxRtcEngine process is running on your client machine:

If not, the process might have crashed. Look for any libraries that are not installed or loaded from the wrong path:

In most cases you might be missing some of them. In particular  might be installed in a different path from the one Citrix is trying to load it from. In such case execute the following to fix that:

Another thing that might be crashing the  process is an incompatible version (at the time of writing) of . Downgrading to version 3.18-2 from the Arch Linux Archive may fix the issue:

Note: you don't actually need to start the  service, but only have a compatible  installed.

## Calls started from Firefox interrupted after a few minutes or audio dropping out
It might be related to resource limits set by Firefox and inherited by the Citrix processes. You can check that by running  while a session is running. If the soft or hard limits show anything different than unlimited (default on most systems) you might have to run  to fix that. Note that limits are reset when you close and reopen a session so you'll have to set them every time.

Alternatively you can just start your session from  or other Chromium based browsers.

## Echo Cancellation
If Microsoft Teams configures auto gain control and noise suppression options, Citrix-redirected Microsoft Teams honors the values as configured. Otherwise, these options are enabled by default. However, starting from Citrix Workspace app 2104, the echo cancellation option is disabled by default. This can cause issues with other participants hearing themselves echoed into the call which can't be reproduced with the "test call" feature.

You can re-enable echo cancellation, gain control, and noise suppression on the client side. Despite no other files for the software living there,  is still the correct directory in which to create the config file.

{{hc|$ vim /var/.config/citrix/hdx_rtc_engine/config.json|
{
  "EnableAEC":1,
  "EnableAGC":1,
  "EnableNS":1
}
}}

To ensure the change took effect, check the :

Note that the values are correct, 1 for on, 0 for off
