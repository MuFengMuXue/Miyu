# Chromium

Chromium is an open-source graphical web browser based on the Blink rendering engine. It is the basis for the proprietary Google Chrome browser.

See this page for an explanation of the differences between Chromium and Google Chrome.

See List of applications/Internet#Blink-based for other browsers based on Chromium.

## Installation
Install the  package, which tracks the  releases.

## Configuration
## Default applications
To set Chromium as the default browser and to change which applications Chromium launches when opening downloaded files, see default applications.

## Certificates
Chromium uses Network Security Services for certificate management. Certificates can be managed in .

The "Local certificates" tab manages server certificates. Certificates added in the "Custom" section are per-profile, and stored in the  SQLite database in the profile directory. Certificates in the "Linux" section are read from the NSS Shared DB at , and cannot be modified in this UI. To add to NSS Shared DB, use another tool such as certutil. See #SSL certificates for usage examples.

The "Your certificates" tab manages client certificates. Certificates added here are stored in the NSS Shared DB.

## Making flags persistent
You can put your flags in a  file under  (or under  if you have configured that environment variable) or  for global.

No special syntax is used; flags are defined as if they were written in a terminal.

* The arguments are split on whitespace and shell quoting rules apply, but no further parsing is performed.
* In case of improper quoting anywhere in the file, a fatal error is raised.
* Flags can be placed in separate lines for readability, but this is not required.
* Lines starting with a hash symbol (#) are skipped. (This is only supported by the Chromium launcher script and will not work when using Google Chrome.)

Below is an example  file that defines the flags :

## Force GPU acceleration
Since at least Chromium 110, GPU acceleration is enabled by default for most systems. You may have to append the following flags to persistent configuration if your system configuration is matched by the block list:

## Hardware video acceleration
If you have confirmed working VA-API support by checking the output of  (see Hardware video acceleration#Verifying VA-API), since Chromium 143 hardware acceleration via VA-API should work out of box. On older Chromium versions you might first try the following flag alone:

Otherwise, continue reading.

To enable accelerated encoding in Chromium:
* Append the  feature, e.g. . See and [https://issues.chromium.org/issues/40225939#comment54 for details.

To enable VA-API support:

* Install the correct VA-API driver for your video card and verify VA-API has been enabled and working correctly, see Hardware video acceleration. For proprietary NVIDIA support, you must install  and append the  feature in addition to the features above.
* Set the option . This is enough when using ANGLE GL renderer and .
* When using ANGLE, Chromium forces the older i965 driver and fails when  is used. As a workaround, configure VA-API manually. See for details.
* To use the system GL renderer on Xorg or Wayland, use . Setting this option might no longer be needed when using Chrome 112 and may break GPU acceleration when using AMD GPUs.
* If VA-API still does not work, try the  or flag
* If VA-API still does not work on X11 and old GPUs, set the  environment variable [https://www.phoronix.com/news/VA-API-libva-2.18.

## Vulkan
When using Vulkan, the following flags are required and might also be sufficient on Chromium 126 and Mesa 24.1:

without any of the additional flags mentioned above.

## Tips and tricks
To check if it is working play a video which is using a codec supported by your VA-API driver (vainfo tells you which codecs are supported, but Chromium will only support VP9 and h264):

* Open the DevTools by pressing  or on the Inspect button of the context (right-click) menu
* Add the Media inspection tab: Hamburger menu > More tools > Media
* In the newly opened Media tab, look at the hardware decoder state of the video decoder

Test on a large enough video. Starting with version 86, Chromium on desktop will only accelerate videos larger than 720p.

To reduce CPU usage while watching YouTube where VP8/VP9 hardware decoding is not available use the h264ify, enhanced-h264ify or Not yet, AV1extension.

On some systems (especially on Xwayland) you might need to #Force GPU acceleration. Only  is enough for our purposes.

You might need to disable the Skia renderer, as it is currently not compatible with video decode acceleration:

## KDE integration
For integration into Plasma, you can:

* install  on your system, and [https://chromewebstore.google.com/detail/plasma-integration/cimiefiiaegbelhefglklhhakcgmhkai Plasma Integration in your browser (see KDE Plasma Browser Integration for more details)
* install  to allow Chromium to use native KDE open/save dialogs
* configure Chromium to use KWallet

## PDF viewer plugin
Chromium and Google Chrome are bundled with the Chromium PDF Viewer plugin. If you do not want to use this plugin, check Download PDFs in .

## Running on Xwayland
If you are using NVIDIA's proprietary driver, running Chromium on Xwayland may cause the GPU process to occasionally crash. To prevent the GPU process from crashing, add the following flags:

 --use-angle=vulkan --use-cmd-decoder=passthrough

## Native Wayland support
Chromium 140 supports Wayland by default.
For old versions, you can use

 --ozone-platform-hint=auto

or

 --ozone-platform=wayland

See #Making flags persistent for a permanent configuration. The flag is also available via browser flags menu.

This will select wayland Ozone backend when in wayland session, so you can use a single desktop entry if you switch between X11 and Wayland often.

Additionally, if you are having trouble with input methods you may also want to force newer GTK:

 --gtk-version=4

If a / key stops working, adding this workaround might fix it:

 --disable-gtk-ime

If you are using Fcitx5 and not work properly when using the above flags, try using the  flag instead of . --enable-wayland-ime --wayland-text-input-version=3

## Touchpad gestures for navigation
To enable two finger swipe to go back and forward through your history, use the following flags:

 --ozone-platform-hint=auto --enable-features=TouchpadOverscrollHistoryNavigation

## Force device scale factor
To force a scale factor on native Wayland, use the following flags [https://chromium.googlesource.com/chromium/src/+/756e64489c84c22998470beddb1facab5e78e1fa:

 --force-device-scale-factor=1.33 --gtk-version=4 --enable-features=WaylandPerSurfaceScale,WaylandUiScale

## Tips and tricks
The following tips and tricks should work for both Chromium and Chrome unless explicitly stated.

## Browsing experience
## chrome:// URLs
A number of tweaks can be accessed via Chrome URLs. See chrome://chrome-urls for a complete list.

* chrome://flags - access experimental features such as WebGL and rendering webpages with GPU, etc.
* chrome://extensions - view, enable and disable the currently used Chromium extensions.
* chrome://gpu - status of different GPU options.
* chrome://sandbox - indicate sandbox status.
* chrome://version - display version and switches used to invoke the active .

An automatically updated, complete listing of Chromium switches (command line parameters) is available at https://peter.sh/experiments/chromium-command-line-switches/.

## Chromium task manager
Shift+ESC can be used to bring up the browser task manager wherein memory, CPU, and network usage can be viewed.

## Chromium overrides/overwrites Preferences file
If you enabled syncing with a Google Account, then Chromium will override any direct edits to the Preferences file found under . To work around this, start Chromium with the  switch:
 $ chromium --disable-sync-preferences

If Chromium is started in the background when you login in to your desktop environment, make sure the command your desktop environment uses is:
 $ chromium --disable-sync-preferences --no-startup-window

## Search engines
Make sites like wiki.archlinux.org and wikipedia.org easily searchable by first executing a search on those pages, then going to Settings > Search and click the Manage search engines.. button. From there, "Edit" the Wikipedia entry and change its keyword to w (or some other shortcut you prefer). Now searching Wikipedia for "Arch Linux" from the address bar is done simply by entering "w arch linux".

## Tmpfs
## Cache in tmpfs
To limit Chromium from writing its cache to a physical disk, one can define an alternative location via the  flag:

 $ chromium --disk-cache-dir="$XDG_RUNTIME_DIR/chromium-cache"

Cache should be considered temporary and will not be saved after a reboot or hard lock. Another option is to setup the space in :

Alternatively create a symbolic link to . Make sure to delete Chromium's cache folder before you run the command:

 $ ln -s /tmp /home/username/.cache/chromium

## Profile in tmpfs
Relocate the browser profile to a tmpfs filesystem, including , or  for improvements in application response as the entire profile is now stored in RAM.

Use an active profile management tool such as  for maximal reliability and ease of use. It symlinks or bind mounts and syncs the browser profile directories to RAM. For more, see Profile-sync-daemon.

## Launch a new browser instance
When you launch the browser, it first checks if another instance using the same data directory is already running. If there is one, the new window is associated with the old instance. If you want to launch an independent instance of the browser, you must specify separate directory using the  parameter:

 $ chromium --user-data-dir=/path/to/some/directory

## Directly open *.torrent files and magnet links with a torrent client
By default, Chromium downloads  files directly and you need to click the notification from the bottom-left corner of the screen in order for the file to be opened with your default torrent client. This can be avoided with the following method:

* Download a  file.
* Right-click the notification displayed at the bottom-left corner of the screen.
* Check the "Always Open Files of This Type" checkbox.

See xdg-open to change the default assocation.

## Touch Scrolling on touchscreen devices
You may need to specify which touch device to use. Find your touchscreen device with  then launch Chromium with the  parameter, where "x" is the id of your device.

## Reduce memory usage
By default, Chromium uses a separate OS process for each instance of a visited web site. However, you can specify command-line switches when starting Chromium to modify this behaviour.

For example, to share one process for all instances of a website:

 $ chromium --process-per-site

To use a single process model:

 $ chromium --single-process

In addition, you can suspend or store inactive Tabs with extensions such as [https://chrome.google.com/webstore/detail/tab-suspender/fiabciakcmgepblmdkmemdbbkilneeeh?hl=en Tab Suspender and OneTab.

## User Agent
The User Agent can be arbitrarily modified at the start of Chromium's base instance via its  parameter.

## Forcing specific GPU
In multi-GPU systems, Chromium automatically detects which GPU should be used for rendering (discrete or integrated). This works 99% of the time, except when it does not - if an unavailable GPU is picked (for example, discrete graphics on VFIO GPU passthrough-enabled systems),  will complain about not being able to initialize the GPU process.

On this page below Driver Information there will be multiple GPUs shown (GPU0, GPU1, ...). There is no user-friendly way to switch between them.  However we can read their PCI addresses then compel Chromium to select the GPU at a specific PCI address via command-line argument:

Then we can identify which is which:

Then to launch Chromium:
 $ chromium --render-node-override=/dev/dri/by-path/pci-0000:01:00.0-render
or
 $ chromium --render-node-override=/dev/dri/by-path/pci-0000:03:00.0-render

Unfortunately the simpler  or  specifiers are unstable and subject to change based on driver/kernel module load order.

## Import bookmarks from Firefox
To ease the transition, you can import bookmarks from Firefox into Chromium.

Navigate Chromium to

If Firefox is already installed on your computer, you can directly import bookmarks as well as many other things from Firefox.

Make sure Mozilla Firefox is selected. Optionally, you can uncheck some unwanted items here. Click the Import and then Done. You are done with it.

If you import bookmarks from another PC, you have to export bookmarks from Firefox first.

 Import and Backup > Export Bookmarks To HTML in Firefox.

The procedure is pretty much the same. You need to go to . However, this time, in the From drop-down menu, select Bookmarks HTML File and click the Choose File button and upload the desired bookmark file.

## Enabling autoscroll with middle mouse button
The autoscroll is still an experimental feature It is intended to be disabled by default if Chromium or Chromium-based browsers are not a development build and is running on a Linux environment. [https://issues.chromium.org/issues/40811836

To enable this feature, launch your browser with the  flag. In case you want to make the option persistent, see #Making flags persistent.

## U2F authentication
Install  library. This provides the udev rules required to enable access to the U2F key as a user.
U2F keys are by default only accessible by root, and without these rules Chromium will give an error.

## Theming
You can make Chromium use your current GTK theme for browser menus and controls. Simply press Use GTK in .

## Dark mode
Since Chromium 114, XDG Desktop Portal is used to automatically determine the user's preferred appearance (issue), thereby dissociating dark mode enablement from the user's GTK theme. This preference will be applied to prefers-color-scheme in CSS, JavaScript, Settings and Dev-Tools.

The way to change the preferred appearance depends on your XDG Desktop Portal backend. For instance, many desktop environments have a switch in their appearance settings. Or when using e.g. , set the preferred mode to ,  or  with:

 $ dconf write /org/gnome/desktop/interface/color-scheme \'prefer-dark\'

You can query the current preferred appearance using  in  (documentation):

 $ dbus-send --session --print-reply=literal --dest=org.freedesktop.portal.Desktop /org/freedesktop/portal/desktop org.freedesktop.portal.Settings.Read string:org.freedesktop.appearance string:color-scheme | tr -s ' ' | cut -d ' ' -f 5

* 0: No preference
* 1: Prefer dark appearance
* 2: Prefer light appearance

## Pre Chromium 114
To enable dark mode and enable the dark theme (normally used for incognito mode) append the following flag to persistent configuration:

## Enable Side Panel
The Side Panel can be enabled through . You can enable or disable Side panel, and change options such as Side panel border and Side panel drag and drop.

## Profile maintenance
Chromium uses SQLite databases to manage history and the like.  Sqlite databases become fragmented over time and empty spaces appear all around. But, since there are no managing processes checking and optimizing the database, these factors eventually result in a performance hit. A good way to improve startup and some other bookmarks- and history-related tasks is to defragment and trim unused space from these databases.

 and  do just this.

## Security
## Disable JIT
At the cost of reduced performance, you can disable just-in-time compilation of JavaScript to native code, which is responsible for roughly half of the security vulnerabilities in the JS engine, using the flag .

## WebRTC
WebRTC is a communication protocol that relies on JavaScript that can leak one's actual IP address and hardware hash from behind a VPN. While some software may prevent the leaking scripts from running, it is probably a good idea to block this protocol directly as well, just to be safe. As of October 2016, there is no way to disable WebRTC on Chromium on desktop, there are extensions available to disable local IP address leak, one is this extension.

One can test WebRTC via https://browserleaks.com/webrtc.

## SSL certificates
See #Certificates for general information.

## Adding CAcert certificates for self-signed certificates
Grab the CAcerts and create an , if one does not already exist.  To do this, first install the  package, then complete these steps:

 $ mkdir -p $HOME/.pki/nssdb
 $ cd $HOME/.pki/nssdb
 $ certutil -N -d sql:.

 $ curl -k -o "cacert-root.crt" "http://www.cacert.org/certs/root.crt"
 $ curl -k -o "cacert-class3.crt" "http://www.cacert.org/certs/class3.crt"
 $ certutil -d sql:$HOME/.pki/nssdb -A -t TC -n "CAcert.org" -i cacert-root.crt
 $ certutil -d sql:$HOME/.pki/nssdb -A -t TC -n "CAcert.org Class 3" -i cacert-class3.crt

Now users may manually import a self-signed certificate.

## Example 1: Using a shell script to isolate the certificate from TomatoUSB
Below is a simple script that will extract and add a certificate to the user's :

 #!/bin/sh
 #
 # usage:  import-cert.sh remote.host.name #
 REMHOST=$1
 REMPORT=${2:-443}
 exec 6>&1
 exec > $REMHOST
 echo | openssl s_client -connect ${REMHOST}:${REMPORT} 2>&1 |sed -ne '/-BEGIN CERTIFICATE-/,/-END CERTIFICATE-/p'
 certutil -d sql:$HOME/.pki/nssdb -A -t "P,," -n "$REMHOST" -i $REMHOST
 exec 1>&6 6>&-

Syntax is advertised in the commented lines.

References:
*https://web.archive.org/web/20180718193807/https://blog.avirtualhome.com/adding-ssl-certificates-to-google-chrome-linux-ubuntu
*https://chromium.googlesource.com/chromium/src/+/master/docs/linux/cert_management.md

## Example 2: Using Firefox to isolate the certificate from TomatoUSB
The  browser can be used to save the certificate to a file for manual import into the database.

Using firefox:
#Browse to the target URL.
#Upon seeing the "This Connection is Untrusted" warning screen, click: I understand the Risks > Add Exception...
#Click: View > Details > Export and save the certificate to a temporary location ( in this example).

Now import the certificate for use in Chromium:
 $ certutil -d sql:$HOME/.pki/nssdb -A -t TC -n "easy" -i /tmp/easy.pem

Reference:
*https://sahissam.blogspot.com/2012/06/new-ssl-certificates-for-tomatousb-and.html

## Canvas Fingerprinting
Canvas fingerprinting is a technique that allows websites to identify users by detecting differences when rendering to an HTML5 canvas. This information can be made inaccessible by using the  flag.

To confirm this is working run [https://panopticlick.eff.org this test and make sure "hash of canvas fingerprint" is reported as undetermined in the full results.

## Privacy extensions
See Browser extensions#Privacy.

## Do Not Track
To enable Do Not Track, visit , scroll down to Advanced and under Privacy and security, check Send a "Do Not Track" request with your browsing traffic.

## Force a password store
Chromium uses a password store to store your passwords and the Chromium Safe Storage key, which is used to encrypt cookie values. By default Chromium auto-detects which password store to use, which can lead to you apparently losing your passwords and cookies when switching to another desktop environment or window manager.

You can force Chromium to use a specific password store by launching it with the  flag with one of following the values [https://chromium.googlesource.com/chromium/src/+/master/docs/linux/password_storage.md:

* , uses Gnome Keyring via libsecret.
* , uses KDE Wallet 5
* , uses KDE Wallet 6
* , saves the passwords and the cookies' encryption key as plain text in the file
* , the default auto-detect behavior

For example, to force Chromium to use Gnome Keyring in another desktop or WM use , see #Making flags persistent for making it permanent.

When using a password store of another desktop environment you probably also want to unlock it automatically. See GNOME/Keyring#Using the keyring and KDE Wallet#Unlock KDE Wallet automatically on login.

## Enable hybrid post-quantum key exchange
Chromium supports the hybrid post-quantum key exchange X25519Kyber768 for TLS 1.3 since version 155 This feature is disabled by default, but can be enabled using the  flag.

## Open any website as a native application
You can open any website in a tabless window intended for [https://developer.chrome.com/blog/getting-started-pwa/ Progressive Web Apps:

 $ chromium --app=https://archlinux.org/

You need to use a correct full URL. This could be combined with  to split configs. Local html file is also used at native application with .

## Force offline
You can force offline state by  for security when you use local html file from Chromium.

## Faster downloading
Chromium has  flag for parallel downloading without extensions.

## Re-enable Manifest V2 (MV2) extension compatibility
As of Chromium version 148, manifest V2 support can be re-enabled to use popular extensions such as the original (non-Lite) uBlock Origin extension.

To do so, launch Chromium with the following flags:

 $ chromium --enable-features=AllowLegacyMV2Extensions --disable-features=ExtensionsManifestV3Only,ExtensionManifestV2Unsupported,ExtensionManifestV2Disabled

See also #Making flags persistent.

## Troubleshooting
## Fonts
## Tab font size is too large
Chromium will use the GTK settings as described in GTK#Configuration. When configured, Chromium will use the  setting for tabs (which may mismatch window font size). To override these settings, use .

Since Chrome Refresh 2023 became default, GNOME users with Cantarell font may notice some characters (like lowercase g) cut off in the tab title. See the issue on chromium.org.

Until the issue resolved, a workaround is to replace Cantarell with another font using a configuration based on Font configuration#Set default or fallback fonts, e.g.

This configuration will apply only if process name  matches. You can use  for Google Chrome.

## WebGL
There is the possibility that your graphics card has been blacklisted by Chromium. See #Force GPU acceleration.

If you are using Chromium with Bumblebee, WebGL might crash due to GPU sandboxing. In this case, you can disable GPU sandboxing with .

Visit  for debugging information about WebGL support.

Chromium can save incorrect data about your GPU in your user profile (e.g. if you use switch between an Nvidia card using Optimus and Intel, it will show the Nvidia card in  even when you are not using it or primusrun/optirun). Running using a different user directory, e.g,  may solve this issue. For a persistent solution you can reset the GPU information by deleting .

## Incorrect HiDPI rendering
Chromium will automatically scale for a HiDPI display, however, this may cause an incorrectly rendered GUI.

The flag  may be used to overrule the automatic scaling factor.

## Incorrect window size and mouse position on Wayland fractional scaling
When native Wayland support is enabled, Chromium will automatically scale based on the configured scale of each monitor.

There is a longstanding bug in chromium, which affects electron apps as well, with scaling under wayland when the desktop scale is less than 100% on some compositors (e.g. KDE). Windows will shrink themselves on every interaction and mouse positioning is scaled by the desktop scale percentage. The flag  can be used to disable this behavior.

The flag  was removed in Chromium v146, but the flag  disables the broken behavior.

## Password prompt on every start with GNOME Keyring
See GNOME/Keyring#Passwords are not remembered.

## Everything is syncing except for password
If synchronization is not working for password only (you can check it on ) delete profile login data:

 $ rm ~/.config/chromium/Default/Login\ Data*

See Google Chrome Help forum for details.

## Losing cookies and passwords when switching between desktop environments
If you see the message  in the terminal when you start Chromium, it might try to use the wrong password storage backend. This might happen when you switch between Desktop Environments.

See #Force a password store.

## Hang on startup when Google Sync enabled
Try launching Chrome with  or another appropriate password store.

See #Force a password store.

## Chromium asks to be set as the default browser every time it starts
If you are using KDE and have once set Firefox as the default browser (by clicking the button inside Firefox), you might find Chromium asks to be set as the default browser every time it starts, even if you click the "set as default" button.

Chromium checks for this status by running . If the output is "no", it is not considering itself to be the default browser. The script  checks for the following MIME associations and expect all of them to be :

To fix it, go to System settings > Applications > Default applications > Web browser and choose Chromium. Then, set the MIME association for :

 $ xdg-mime default chromium.desktop text/html

Finally, update the MIME database:

 $ update-mime-database ~/.local/share/mime

## "This browser or app may not be secure" error logging in to Google
As of 2020.04.20 if you run chromium with  flag for web development, you cannot log in to your Google account. Temporarily disable this flag to login and then you can enable it back.

## Chromium rendering at 60 FPS despite using a display with a higher refresh rate
See the general issue which may contain some additional workarounds and a sister issue about mixed refresh rates.

## Mixed refresh rates
When using displays with mixed refresh rates(for example 60Hz and 144Hz), Chromium might render for the lower Hz display.

There is a suitable workaround for this issue, append the following flags to persistent configuration:

This should make Chromium run at 144 FPS when used on a 144Hz display, assuming your compositor is also refreshing at 144 FPS.
Keep in mind it might be a little choppy due to , but it is way better than being stuck at 60 FPS.

## Running on the Wayland backend
There seem to be Wayland compositor-specific problems that trigger this issue.
Notably, Plasma 5 seems to only ever render on 60Hz no matter the setup, but Plasma 6(rc1, at the time of writing) makes Chromium work flawlessly on high refresh rates.

A workaround may be to switch to the XWayland backend if all else fails.

## Chromium slow scroll speed
Mouse whell scrolling in chromium and electron based applications may be too slow for daily usage. Here are some solutions.

Libinput#Mouse wheel scrolling speed scaling injects  function in libinput and provides an interface to change scale factor. This is not an application level injection, so an addition script for application specific scale factor tuning is needed. Note that scroll on chromium's small height developer tools may be too fast when scale factor is big enough.

IMWheel increases scroll distance by replaying X wheel button event for multiple times. However, chromium assumes the real scroll and the replayed ones as two events. There is a small but noticeable delay between them, so one mouse wheel scroll leads to twice page jumps. Also, touchpad scroll needs additional care.

Linux Scroll Speed Fix and SmoothScroll are two chromium extensions with support for scroll distance modification. Upon wheel scroll in a web page, the closest scrollable ancestor of current focused node will be found, then a scroll method with given pixel distance will be called on it, even if it has been scrolled to bottom. So once you scroll into a text editor or any scrollable element, you can never scroll out of it, except moving mouse. Also, extension based methods can not be used outside chromium.

## Videos load but do not play
This may be a PulseAudio issue. See the suggested fix in PulseAudio/Troubleshooting#Browsers (firefox) load videos but do no play.

## Passwords are not saved due to a corrupted database
The stored password database can become corrupted and in need of getting rebuilt. Doing so will destroy all data therein/lose stored passwords.

Launch chromium from a terminal and look for output like:
 Password decryption failed, encryption_result is 2

Exit chromium and then delete these three database files:

Launching chromium again should re-create them.

## Cursor is not correct on KDE Wayland
See KDE#Plasma cursor sometimes shown incorrectly.

## Chromium window is transparent under Wayland
Due to a [https://issues.chromium.org/issues/329678163 bug, chromium 124 must be started with the explicit command line flag .

## Wayland hardware acceleration buffer handle is null errors
Due to a bug, you may see the below in your log when launching from terminal, especially with hardware acceleration enabled on Wayland:

Workaround for now is adding this flag:

## No audio available without sound server
Chromium does not support Advanced Linux Sound Architecture#Addressing hardware directly.
Set output devices  and  as seen in the page and use  flags.

## Gnome "Global Shortcuts" menu appears on startup
Due to extensions which define global shortcuts (such as obsidian web clipper), the gnome "Global Shortcuts" appears at startup. This is described in https://github.com/brave/brave-browser/issues/44886 and can be fixed by adding this flag:

## Compose key does not work: Typing special characters with keyboard not possible
Due to a bug the "Compose" key does not work in recent versions of chromium. This becomes apparent when user tries to type in special characters such as `@` or umlauts anywhere in the browser. The special key combinations utilizing the compose key (for example `ALT GR`) work in all applications except chromium. This issue is most likely related to gtk and cannot be resolved by switching between Wayland and X11. It is described at https://issues.chromium.org/issues/327158031 and can be fixed by adding this flag:

## Chromium does not fully maximize on Wayland
You have to enable Use system title bar and borders via the chrome://settings/appearance menu.

## Chromium has no sound but sound output device is present
For WirePlumber users, resetting WirePlumber state may help.

## File picker does not open when trying to save or download
This is a problem with XDG Desktop Portal, restarting the user unit may help.

## Forcing a specific GPU has no effect on Wayland
Sometimes, #Forcing specific GPU may not work on Wayland, with an error message like so:

As of March 10th 2026, the only workaround that works is disabling the unwanted GPU in the firmware (which is not ideal, and even impossible on some systems). It might be possible to achieve the same result by blacklisting the appropriate kernel modules, but users might still find this approach undesirable.

Another possibility would be to go back to Xorg or use Xwayland More information can be read in [https://forum.vivaldi.net/topic/99688/vivaldi-crashes-at-startup-when-using-wayland, and [https://issues.chromium.org/issues/40766635.
