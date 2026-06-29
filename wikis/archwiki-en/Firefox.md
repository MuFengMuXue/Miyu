# Firefox

Firefox is a popular open-source graphical web browser developed by Mozilla.

## Installation
Install the  package.

Other alternatives include:

*
*
*
*
* On top of the different Mozilla build channels, a number of forks exist with more or less special features—see List of applications/Internet#Gecko-based.

A number of language packs are available for Firefox, other than the standard English. Language packs are usually named as  (where  can be any language code, such as de, ja, fr, etc.). For a list of available language packs, see firefox-i18n for , firefox-developer-edition-i18n for  and firefox-nightly- for .

## Add-ons
Firefox is well known for its large library of add-ons which can be used to add new features or modify the behavior of existing features. Firefox's "Add-ons Manager" is used to manage installed add-ons or find new ones.

For instructions on how to install add-ons and a list of add-ons, see Browser extensions.

## Adding search engines
Search engines may be added to Firefox by creating bookmarks:

* Press the star on the address bar or .
* Right click on the bookmark you have created, then press Edit Bookmark...
* Complete the URL field with search URLs. Complete the place of the query with . Complete the Keyword field with user-defined characters. Like this:

 URL:
 https://duckduckgo.com/html/?q=%s
 Keyword:
 d

Searches are performed by pre-pending the search term with the keyword of the specified search engine:  will query DuckDuckGo using the search term

Search engines may also be added to Firefox through add-on extensions; see this page for a list of available search tools and engines.

A very extensive list of search engines can be found at the Mycroft Project.

## firefox-extension-arch-search
Install the  package to add Arch-specific searches (AUR, wiki, forum, packages, etc) to the Firefox search toolbar.

## Configuration
Firefox exposes a number of configuration options. To examine them, enter in the Firefox address bar:

 about:config

Once set, these affect the user's current profile, and may be synchronized across all devices via Firefox Sync. Please note that only a subset of the  entries are synchronized by this method, and the exact subset may be found by searching for  in . Additional preferences and third party preferences may be synchronized by creating new boolean entries prepending the value with services.sync.prefs.sync. To synchronize the whitelist for the extension NoScript:

 services.sync.prefs.sync.capability.policy.maonoscript.sites

The boolean  must be set to  to synchronize the remainder of NoScript's preferences via Firefox Sync.

## Settings storage
Firefox stores the configuration for a profile via a  in the profile folder, usually .

Firefox also allows configuration for a profile via a  file: user.js kept also in the profile folder. A  configuration supersedes a . The  configuration is only parsed at start-up of a profile. Hence, you can test changes via  and modify  at runtime accordingly. For a useful starting point, see e.g custom user.js which is targeted at privacy/security conscious users.

One drawback of the above approach is that it is not applied system-wide. Furthermore, this is not useful as a "pre-configuration", since the profile directory is created after first launch of the browser. You can, however, let firefox create a new profile and, after closing it again, copy the contents of an already created profile folder into it.

Sometimes, it may be desired to lock certain settings, a feature useful in widespread deployments of customized Firefox. In order to create a system-wide configuration, follow the steps outlined in Customizing Firefox Using AutoConfig:

1. Create :

 pref("general.config.filename", "firefox.cfg");
 pref("general.config.obscure_value", 0);

2. Create  (this stores the actual configuration):

 //
 //...your settings...
 // e.g to disable Pocket, uncomment the following lines
 // lockPref("extensions.pocket.enabled", false);
 // lockPref("browser.newtabpage.activity-stream.feeds.section.topstories", false);

Please note that the first line must contain exactly . The syntax of the file is similar to that of .

## Multimedia playback
Firefox uses FFmpeg for playing multimedia inside HTML5  and  elements. Use https://cconcolato.github.io/media-mime-support/ to test video or https://hpr.dogphilosophy.net/test/ to test audio, to determine which formats are actually supported.

Firefox uses PulseAudio for audio playback and capture. If PulseAudio is not installed, Firefox uses ALSA instead. Note that by default, Firefox blocks all media with sound from playing automatically ==== HTML5 DRM/Widevine ====

Widevine is a digital rights management tool that Netflix, Amazon Prime Video, and others use to protect their video content. It can be enabled in Settings > General > Digital Rights Management (DRM) Content. If you visit a Widevine-enabled page when this setting is disabled, Firefox will display a prompt below the address bar asking for permission to install DRM. Approve this and then wait for the "Downloading" bar to disappear; now, you are able to watch videos from Widevine protected sites.

Firefox can only play 720p video (or lower) with Widevine, due to not using [https://bugzilla.mozilla.org/show_bug.cgi?id=1700815 hardware DRM playback. It is also required that the private mode browsing is disabled, for the window and in the Settings.

## "Open With" extension
# Install Open With add-on.
# Go to Add-ons > Open With > Preferences.
# Proceed with instructions to install a file in your system and test the installation.
# Click Add browser.
# In the dialog, write a name for this menu entry and command to start a video streaming capable player (e.g. ).
## Optionally, add needed arguments to the player (e.g. you may want  for mpv).
# Right click on links or visit pages containing videos. Select newly created entry from Open With's menu and if the site is supported, the player will open as expected.

The same procedure can be used to associate video downloaders such as youtube-dl.

## Hardware video acceleration
Hardware video acceleration via VA-API is available under Wayland and Xorg [https://bugzilla.mozilla.org/show_bug.cgi?id=1619523 To enable VA-API in Firefox:

# Ensure that your video card is correctly configured for VA-API as described in Hardware video acceleration.
# Ensure WebRender is enabled by navigating to  and verifying the Compositing value is "WebRender". It is enabled by default in GNOME and other desktop environments [https://mastransky.wordpress.com/2021/01/10/firefox-were-finally-getting-hw-acceleration-on-linux/.
#* Ensure you are not running "Software WebRender" as that will not work as of August 2021 #* If necessary, Hardware WebRender can be force enabled by setting  to  in .
# VA-API is enabled by default for Intel GPUs [https://bugzilla.mozilla.org/show_bug.cgi?id=1777430 since Firefox 115, and for AMD GPUs since Firefox 136. For other GPUs, set  to  in .
# Optionally, to save power on multi-GPU systems (e.g. Ryzen 7000 series with IGP and GPU) and/or take advantage of more video codecs supported by a IGP/GPU: run Firefox with  environment variable set to the preferred rendering device. (Available devices can be listed with ).

VA-API usage can be verified by checking Firefox's VA-API logs. Run Firefox with the  environment variable and check in the log output that VA-API is enabled and used (search for the "VA-API" string) when playing a video for example. Pay attention to these logs as they might indicate that only one of the two possible compositors described before (WebRender or OpenGL) works with VA-API on your particular setup.

## Spell checking
Firefox can use system-wide installed Hunspell dictionaries as well as dictionaries installed through its own extension system.

To enable spell checking for a specific language, right click on any text field and check the Check Spelling box. To select a language for spell checking, you have to right click again and select your language from the Languages sub-menu.

If your default language choice does not stick, see #Firefox does not remember default spell check language.

## System-wide Hunspell dictionaries
Install Hunspell and its dictionaries for the languages you require.

## Dictionaries as extensions
To get more languages, right click on any text field, click Add Dictionaries... and select the dictionary you want to install from the [https://addons.mozilla.org/firefox/language-tools/ Dictionaries and Language Packs list.

## XDG Desktop Portal integration
Starting with version 64, Firefox can optionally use XDG Desktop Portals to handle various desktop features, such as opening a file picker, or handling MIME types. Using Desktop Portals allows you to, for example, customize which program is invoked to display a dialog when you select files to upload on a webpage or when picking a download location using Save as.... See XDG Desktop Portal#List of backends and interfaces for a list of available backend options.

Firefox has a number of independent settings for specifying whether each feature should be handled with a Desktop Portal request or whether to use the default GTK feature.

Each setting can have the following values:
*  – Never
*  – Always
*  – Auto (typically depends on whether Firefox is run from within Flatpak or whether the  environment is set)

The settings are:
*  – Whether to use XDG portal for the file picker
*  – Whether to use XDG portal for the mime handler
*  – Whether to try to use XDG portal for settings/look-and-feel information
*  – Whether to use XDG portal for geolocation
*  – Whether to use XDG portal for opening to a file

## KDE integration
* To apply KDE styles to GTK applications, including Firefox, see KDE#GTK application appearance.
* To use the KDE file picker in Firefox 64 or newer, install  and , then set  to  in .
* Extensions/add-ons may provide additional integration, such as:
** Browser integration in Plasma: requires  and the Plasma Integration add-on.
::

## GNOME integration
In order to use the GNOME file picker, you will need to install  and change  from  to  in .

## Listen (text to speech)
Firefox can perform Text to Speech synthesis for web pages.

## Setup
TTS must be setup for the Listen icon to appear in the Reader view.  Firefox uses Speech dispatcher which requires a speech synthesis engine. The currently recommended speech synthesis engine is Festival.

## Usage
See the illustrated steps on Mozilla's website.

The Listen icon (a headphones icon) will only appear if you have performed all the configuration above, Speech Dispatcher is working, and you have started Firefox after you started the Festival server (you cannot start Firefox then Festival).

Furthermore, sometimes a Festival server process may linger after you have tried to kill it, but will terminate after you shut down Firefox.

For common issues, see #Web Speech API has no voices and #Narrate/Listen icon missing in Reader Mode.

## Using the festival-us voices
The voices in the package  provide better quality audio than those in  but they do not work in Firefox. They do not appear in the list of available voices in Firefox and when you open Reader view you will see error messages like this in the terminal output from the Festival server:

To fix this you need to edit the following files:

*
*
*

For each of these files you need to add some code to the second last line of code of each file, eg for  add code before this line:

The code you need to add to  is below.  You will need to change the voice name, gender, dialect and description as appropriate for the other two files.

## Tips and tricks
For general enhancements, see Firefox/Tweaks, and for privacy related enhancements, see Firefox/Privacy.

## Dark themes
Firefox should respect your GTK theme settings and your OS-wide dark appearance settings (as in the Appearance section of GNOME's settings or KDE system settings). If the latter does not work, make sure to have a suitable  package installed.

Starting with Firefox 68, you can make all the Firefox interfaces and even other websites respect dark themes, irrespective of the system GTK theme and Firefox theme. To do this, set  to  in  As of Firefox 100, further control of the dark theme of web pages that opt-in (using the CSS media query [https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-color-scheme prefers-color-scheme) and Firefox's own in-content pages is possible with . Setting this to  will follow the browser theme, setting this to  will follow the system wide dark-mode preference ( as above, which defaults to  if the user has not changed the dark-mode preference or if a system does not support a system-wide dark-mode preference), while  and  will always force light-mode and dark-mode respectively. This setting can also be accessed through the user settings of Firefox under General > Language and Appearance > Website appearance.

## Frame rate
If Firefox is unable to automatically detect the right value, it will default to 60 fps. To manually correct this, set  to the refresh rate of your monitor (e.g. 144 for 144 Hz).

## Memory limit
To prevent pages from abusing memory (and possible OOM), we can use Firejail with the  option.

## New tabs position
To control where new tabs appears (relative or absolute), use  and . See for more information.

## Screenshot of webpage
You can Take a Screenshot by either using the screenshots button that can be added to the toolbar from the customize screen in the Hamburger menu at More tools > Customize toolbar, by pressing  or by right-clicking on the webpage. See [https://support.mozilla.org/en-US/kb/firefox-screenshots Firefox screenshots for more information, including on the telemetry data collection.

You can also use the screenshot button in the developer tools, which can be added through the developer tools Settings menu, under the Available Toolbox Buttons section. The settings for the developer tools are accessible through the three horizontal dots located at the top right of the developer tools pane.

## Xwayland
Starting with version 121, Firefox defaults to Wayland instead of XWayland and does not require any configuration.

You can force Xwayland mode via an environment variable.

 $ MOZ_ENABLE_WAYLAND=0 firefox

To make this permanent, see Environment variables#Graphical environment and start Firefox via the desktop launcher like you normally would.

To verify that it worked, look for Window Protocol in . The presence of  means you are running Firefox under Xorg display server, while  means your system is running Wayland but executing Firefox as legacy X11 application.

## Window manager rules
You can change how your window manager groups Firefox windows using CLI options.

## Xorg
Under Xorg, windows are grouped by their  string. Set a custom value using Firefox's  option, then update the  field in the desktop entry to the same value.

## Wayland
Under Wayland, windows are grouped by their  attribute. To set a custom value, use Firefox's  option instead;  appears to have no effect.

On some desktop environments (e.g. KDE; others untested), you also have to make sure that the desktop entry has the same file stem as your custom  value if you are pinning Firefox to the task manager. This way the launched instance of Firefox will be grouped with the pinned entry.

## Profiles
To start new Firefox instances, multiple profiles are required. To create a new profile:

 $ firefox -P

You can use profiles together with #Window manager rules to group windows of each profile separately.

[https://ffprofile.com/ Firefox Profilemaker can be used to create a Firefox profile with the defaults you like.

## Touchscreen gestures and pixel-perfect trackpad scrolling
See Firefox/Tweaks#Pixel-perfect trackpad scrolling, Firefox/Tweaks#Enable touchscreen gestures and Firefox/Tweaks#Smooth scrolling.

## Multiple home pages
To have multiple tabs opened when starting Firefox, open a new window and then open the sites you want to have as "home tabs".

Now go to Settings > Home and under Homepage and new windows click the Use Current Pages button.

Alternatively, go directly to Settings > Home and now under Homepage and new windows set the first field to Custom URLs.. and enter the pages you want as new home pages in the following format:

 https://url1.com|https://url2.com|https://url3.com

## View two pages side by side in the PDF viewer
To display two pages at once with the integrated PDF viewer, set  to  in .

## Kiosk mode
Firefox supports kiosk mode that shows pages in full screen without browser chrome, context menus, and other features useful for typical desktop browsing. These can be seen on ATMs or information panels where users are not expected to interact with the rest of the system.

To use kiosk mode, start Firefox with:

 $ firefox --kiosk url

The startup page can be configured in the settings or supplied as a command-line parameter.

If you need printing, you can prevent Firefox from showing paper size configuration dialogs with:

 $ firefox --kiosk --kiosk-printing url

## Compact mode
Starting with Firefox version 89, the compact mode density option was removed from the Customize panel but you can still use compact density. To do this, set  to  in .

The UI can be scaled down even further, see Firefox/Tweaks#Configure the DPI value but use values between 0 and 1 instead.

## GNOME search provider
Firefox includes a search provider for GNOME Shell which exposes Firefox bookmarks and history to GNOME Shell search while Firefox is running. However, this provider is disabled by default; to enable it go to  and set  to .

## Custom date and time format in Library window
The date and time format used in the Library window (the window showing bookmarks, history and downloads, accessible via  and ) can be customized by setting , , and  in  or .  For example, to get a format similar to RFC:3339 ("2022-12-31 22:49"), set the three preferences to , , and {{ic|{1} {0} }}, respectively.

Setting the  environment variable to  only worked in old Firefox versions (perhaps 57 and earlier).  Mozilla's [https://bugzilla.mozilla.org/show_bug.cgi?id=1426907 bug report 1426907 contains further information.

## Disable the Ctrl+q keybinding for shutting down Firefox
Create and set the option  to  in .

## Enable hybrid post-quantum key exchange
Firefox supports X25519Kyber768, a hybrid post-quantum key exchange for TLS 1.3. Since Firefox 132.0, it is enabled by default. To test that it is working you can visit this Cloudflare Research test page, which will tell you whether you are using a PQ-safe key exchange.

## Disable cursor blinking
By default, Firefox enables cursor blinking. To stop the cursor from blinking, set  to  in  === Share NSS DB with Chromium ===

By default, Chromium reads the NSS Shared DB at . Firefox puts the NSS DB in the profile directory,  and .

To make Firefox use the NSS Shared DB, add , , and change  [https://blog.xelnor.net/firefox-systemcerts/. For example, bold below indicates the changes. You should leave the surrounding options intact if they differ from the below example.
{{hc|~/.mozilla/YOUR_PROFILE_DIRECTORY/pkcs11.txt|
library=libnsssysinit.so
name=NSS Internal PKCS #11 Module
parameters=configdir='sql:/home/YOUR_USER/.pki/nssdb' certPrefix= keyPrefix= secmod='secmod.db' flags= updatedir= updateCertPrefix= updateKeyPrefix= updateid= updateTokenDescription=''
NSS=Flags=moduleDBOnly,internal,critical trustOrder=75 cipherOrder=100 slotParams=(1={slotFlags=askpw=any timeout=30})
}}

You may wish to copy the database files from your Firefox profile directory to , if you have custom certificates in them.

## Troubleshooting
## Troubleshoot Mode
The command line switch  starts Firefox in [https://support.mozilla.org/en-US/kb/diagnose-firefox-issues-using-troubleshoot-mode Troubleshoot Mode, which disables extensions, themes, hardware acceleration, the JIT and some other features for this session.

This mode can also be enabled by pressing on the hamburger menu while Firefox is open, clicking Help, selecting Troubleshoot Mode and confirming this on the modal dialog that appears. Please note this will require a browser restart.

This mode was previously named Safe Mode until Firefox 88.

## Firefox refresh
Some issues experienced by users in Firefox may be caused by profile issues, such as corruption.

If you have ruled out other causes, it may be worth trying a new Firefox profile for testing purposes to see if this will resolve your issue. More information on how to create a new profile and switch between profiles can be found on the Firefox support page.

If this resolves your issue, you should switch back to your original profile and consider refreshing your Firefox.

Refreshing your profile will retain all browsing and download history, bookmarks, web form auto-fill data, cookies, personal dictionary and passwords, and will transfer them to a brand new profile without extensions, themes, extension data and preferences, among other data. A backup of your old profile will also be retained.

To refresh your profile, navigate to , press Refresh Firefox and confirm this on the modal dialog that appears.  can also be accessed by pressing the Hamburger menu, selecting Help and then clicking More troubleshooting information.

More information on refreshing your Firefox, including further details about what is transferred to the new profile, can be found on the Firefox support page.

## Hardware video acceleration issues
If you are having issues with hardware video acceleration in Firefox, e.g. in case of freezes or graphical corruption, start Firefox in Troubleshoot Mode for testing purposes to confirm that this is the issue. If this step resolves the issue, merely set  to  in  to disable hardware video acceleration, and restart Firefox.

## Extension X does not work on some Mozilla owned domains
By default, extensions will not affect pages designated by . If this is not desired, this field can be cleared (special pages such as  will not be affected). Then create and set  to true.

## Firefox startup takes very long
If Firefox takes much longer to start up than other browsers, it may be due to lacking configuration of the localhost in . See Network configuration#Local network hostname resolution on how to set it up.

Misbehaving Firefox extensions, or too many extensions, may be another source of slow startup. This can be confirmed through the use of Troubleshoot Mode, which will disable extensions on restart.

A further cause of slow start-up may be a profile issue, such as corruption. For more troubleshooting steps around your Firefox profile, see #Firefox refresh.

## Font troubleshooting
See Font configuration.

Firefox has a setting which determines how many replacements it will allow from Fontconfig. To allow it to use all your replacement rules, change  to  (the highest possible value).

Firefox ships with the Twemoji Mozilla font. To use the system emoji font, set  to  in . Additionally, to prevent the Mozilla font interfering with your system emoji font, change  to  or remove  (see also pacman#Skip files from being installed to system).

## Setting an email client
Inside the browser,  links by default are opened by a web application such as Gmail or Yahoo Mail. To set an external email program, go to Settings > General > Applications and modify the action corresponding to the  content type; the file path will need to be designated (e.g.  for Kmail).

Outside the browser,  links are handled by the  mime type, which can be easily configured with xdg-mime. See Default applications for details and alternatives.

## File association
See Default applications.

## Firefox keeps creating ~/Desktop even when this is not desired
Firefox uses  as the default place for download and upload files. To change it to another folder, set the  option as explained in XDG user directories.

## My downloads directory is full of files I do not remember saving
In Firefox version 98, the behavior of opening files in external programs was silently changed. Instead of downloading them into  and giving that file location to the child process, Firefox now downloads the file as if you had chosen to save it, and then gives the child process the location of the file in your downloads directory. As a result, your downloads will be littered with files you only ever intended to open for viewing. This happens both when you select a program to use to open the file in a dialog and for file types you have configured to automatically open in a specific program. Notably this also happens for some file types that are opened internally in Firefox (such as PDF documents if the in-browser PDF.js viewer is enabled).

Due to an oversight, the dialog prompting you for what to do with the file still describes the old choices (either open or save) while it is in reality always going to save the file. Since this behavior could realistically pose a security and privacy risk to certain users who expect the files to not be saved to disk, you might want to disable the new behavior.

To do this, create and set  to  in .

Alternatively, to prevent Firefox from automatically saving PDFs into the downloads directory while opening them in the in-browser viewer, set  to  in .

## Additional settings to consider
* :  (only ask whether to save or cancel in the file saving dialog, never ask to open with another program)
* :  (same as Settings > General > Files and Applications > What should Firefox do with other files? > Ask whether to open or save files).
* Set all known file types in Settings > General > Files and Applications to Always ask, with the possible exception of the ones set to be opened by Firefox itself.

## Locate and change Firefox Cache storage location
Create  in  and set it's string value to the desired location, for example to  or

## Changes to userChrome.css and userContent.css are ignored
Set  to  in

## Middle-click behavior
To autoscroll on middle-click (default for Windows browsers), you have two ways to enable this feature:

* Go to Settings > General, look for the Browsing section and enable Use autoscrolling option.

* Alternatively, set  to  in .

To disable pasting from the clipboard (PRIMARY selection) when the middle mouse button is clicked, set  to  in .

To load the contents of the clipboard as a URL when the middle mouse button is clicked,  to  in . This was the default behaviour prior to Firefox 57.

## Backspace does not work as the 'Back' button
According to MozillaZine, the  key was mapped based on which platform the browser was running on. As a compromise, this preference was created to allow the  key to either go back/forward, scroll up/down a page, or do nothing.

To make  go back one page in the tab's history and  go forward, set  to  in .

To have the  key scroll up one page and  scroll down one page, set  to . Setting this property to any other value will leave the key unmapped (Arch Linux defaults to ; in other words, it is unmapped by default).

## Firefox does not remember login information
It may be due to a corrupted  file in Firefox's profile folder. In order to fix this, just rename or remove  while Firefox is not running.

Open a terminal of choice and type the following:

 $ rm -f ~/.mozilla/firefox/.default/cookies.sqlite

The profile id is a random 8 character string.

Restart Firefox and see if it solved the problem.

If it did not work, check if there exists a  file that you could use to manually restore the cookies.

## Cannot enter/leave fullscreen
If Firefox detects an EWMH/ICCCM compliant window manager, it will try to send a WM_STATE message to the root window to request Firefox be made to enter (or leave) full-screen mode (as defined by the window manager). Window managers are allowed to ignore it, but if they do, Firefox will assume the request got denied and propagate it to the end user which results in nothing happening. This may result in not being able to full screen a video. A general workaround is to set the  to  in .

Related bug reports: Bugzilla 1189622.

## Scrollbar is not hidden/disabled when YouTube is fullscreen
This can be fixed using a uBlock Origin filter. To add a filter, click the uBlock Origin extension icon > Three cogwheels (Open the dashboard) > My Filters. Then, add the following to the text field:

 www.youtube.com##ytd-app:style(overflow: hidden !important;)

After applying the changes and reloading the YouTube window, the filter will take effect. Note that you have to have cosmetic filtering enabled for this to work (the middle icon with the eye).

## JavaScript context menu does not appear on some sites
You can try setting  to  in .

## Firefox does not remember default spell check language
The default spell checking language can be set as follows:

# Type  in the address bar.
# Set  to your language of choice, for instance .
# Notice that the for dictionaries installed as a Firefox plugin the notation is , and for  dictionaries the notation is .

When you only have system wide dictionaries installed with , Firefox might not remember your default dictionary language settings. This can be fixed by having at least one dictionary installed as a Firefox plugin. Notice that now you will also have a tab Dictionaries in Add-ons. You may have to change the order of preferred language for displaying pages in  to make the spell check default to the language of the addon dictionary.

Related questions on the StackExchange platform: [https://stackoverflow.com/questions/21542515/change-default-language-on-firefox/29446353, Related bug reports: [https://bugzilla.mozilla.org/show_bug.cgi?id=776028 Bugzilla 776028, Ubuntu bug 1026869

## Firefox does not find system-wide Hunspell spell checking dictionaries
Ensure that the setting  exists and is set to the path of the system's Hunspell dictionaries: .

## Some MathML symbols are missing
You need some Math fonts, namely Latin Modern Math and STIX (see this MDN page: to display MathML correctly.

In Arch Linux, these fonts are provided by , but they are not available to fontconfig by default. See TeX Live#Making fonts available to Fontconfig for details. You can also try other Math fonts. In case you encounter this bug [https://bugzilla.mozilla.org/show_bug.cgi?id=1208776, installing  can help.

## Videos load but do not play
This may be a PulseAudio issue. See the suggested fix in PulseAudio/Troubleshooting#Browsers (firefox) load videos but do no play.

## Tearing when scrolling
Try disabling smooth scrolling in Settings > General > Browsing. Note that the pages will scroll jerkily. Furthermore, in  setting  to different values (i.e. 0 or 1) can also improve scrolling smoothness.

## Firefox WebRTC module cannot detect a microphone
WebRTC applications for instance Firefox WebRTC getUserMedia test page say that microphone cannot be found. Issue is reproducible for both ALSA or PulseAudio setup. Firefox debug logs show the following error:

You can try setting  property to  at  Firefox page and restart Firefox.

This can also help if you are using the PulseAudio module-echo-cancel and Firefox does not recognise the virtual echo canceling source.

## WebRTC sharing indicator displays an XML parsing error
After agreeing to share a microphone or web camera, you may then see a window with a tan background and a red border in the top left corner on your primary window, displaying the following error message:

 XML Parsing Error: no root element found
 Location: chrome://browser/content/webrtcLegacyIndicator.xhtml
 Line Number: 1, Column 1:
 ^

If this is the case for you, performing the following steps should resolve the issue:

# Navigate to .
# Click on the Clear Startup Cache button and agree to restart the browser.

See Mozilla's bug report for more information.

## Google meet
When using screen sharing in Google Meet, you might notice choppy visuals and overall laggy video. A possible fix is to change your browser’s user agent to Google Chrome. You can do this with the User agent switcher extension.

## Cannot login with my Chinese account
Firefox provides a local service for Chinese users, with a local account totally different from the international one. Firefox installed with the  package uses the international account system by default, to change into the Chinese local service, you should install the add-on manager on this page, then you can login with your Chinese account now.

## No audio on certain videos when using JACK and PulseAudio
If you are using JACK in combination with PulseAudio and cannot hear any sound on some videos, it could be because those videos have mono audio. This happens if your JACK setup uses more than just stereo, but you use normal headphones. To fix this, you simply have to connect the  port from the PulseAudio JACK Sink to both  and  ports of the system output.

You can also do this automatically using a script:

Keep in mind that the names for the sink and the ports might be different for you. You can check what your JACK setup looks like with a Patchbay like Catia from .

## Geolocation does not work
Google limits the use of its location service, which causes the following error when geolocation is enabled on a website: . Region-locked services such as Hulu may display a similar error indicating that your location could not be determined even though you have allowed location services for the site.

See  for more details.

One work around is to navigate to  and change the  setting  to a static data value such as:

 data:application/json,{"location": {"lat": 41.8818, "lng": -87.6232}, "accuracy": 27000.0}

Doing so will provide static coordinates for the geolocation service (in this example , ). The coordinates should be modified to reflect the desired location. This will allow services such as Hulu to function properly, but will not automatically update location information when it changes.

## Right mouse button instantly clicks the first option in window managers
This problem has been observed in i3, bspwm and xmonad.

To fix it, navigate to  and change  to .

See === Firefox window does not repaint after disabling or enabling compositing ===

Unset the environment variable .

Related bug report: [https://bugzilla.mozilla.org/show_bug.cgi?id=1711039 Bugzilla 1711039.

## Firefox continuously asks to be set as default browser upon launch
There are a couple things you can try: if you are using a desktop environment, check if Firefox is set as the default browser in your system settings. If it is not, then set it, otherwise you can run the following  command, provided by the xdg-utils package, to query which browser is set as default on your system:

 $ xdg-settings get default-web-browser

If no value is returned or it is not Firefox, then run this command to set it:

 $ xdg-settings set default-web-browser firefox.desktop

If Firefox still asks to be set as the default browser, then it may be quieted if it is set to handle http and https URL schemes. To do so, run these  commands:

 $ xdg-mime default firefox.desktop x-scheme-handler/http
 $ xdg-mime default firefox.desktop x-scheme-handler/https

If those do not work either, check if you have set the environment variable  (all values trigger the bug), in which case, unset it. Related bug report: Bugzilla 1516290. If that does not work or you did not set it, navigate Firefox to , check if the variable  is set to  and, if so, set it to .

If you wish to disable default browser check entirely, navigate Firefox to  and set  to .

## Video stuttering
If you experience video stuttering and you notice that Firefox is only hitting one core at 100% when watching videos (especially higher resolution videos), this might help you.

Go into  and search for  and change  from 1 to a higher number. An ad hoc method to find a good number is to increase it one at a time until you get good results, but 4 seems to be a good value.

## Bengali font broken in some pages
In most cases, installing the  and making Noto Sans Bengali as defaults in Fonts and Colors settings solves it. However, in some social media sites, Bengali fonts may still be broken. In those cases, Mozilla provides a detailed guide on how to see all the fonts gets loaded in a page. By using Page Inspector, find out all the fonts that are being loaded on that particular page. Removing fonts other than Noto Sans from the system will resolve the issue permanently.

There will be some fonts that have been installed as dependency of other package. For example,  installs  as dependency, which loads itself in some Firefox pages automatically and breaks Bengali fonts on those pages. To solve this issue, use the following rule in your font configuration:

## Web Speech API has no voices
Firefox uses for text to speech (tts) speechd. You can use the command  to test if it reads the text or  to get a list of the voices. If there are no voices, too, you can install some with the package . If they do not work out of the box, you maybe have to configure them. You can use the  command or edit the config file . There should be the following lines active (without # in front of it):

 AddModule "espeak-ng"                "sd_espeak-ng" "espeak-ng.conf"
 DefaultModule espeak-ng

## Narrate/Listen icon missing in Reader Mode
## Enable Speech Synthesis
Per https://developer.mozilla.org/en-US/docs/Web/API/Web_Speech_API/Using_the_Web_Speech_API, speech synthesis must be enabled (it is enabled by default). To enable, set  to  in .

## Disable Fingerprinting Protection
Per https://support.mozilla.org/en-US/kb/firefox-protection-against-fingerprinting,
Fingerprinting Protection disables the WebSpeech API. If you enabled this option, you will need to disable it for the narrator to work. To disable fingerprinting protection, set  to  in .

## Disable filter voices
If you do not see the narrator icon, try setting  to  in .

This can be used to check whether  works at all. If it helps, you may miss voices for the language of the article opened in reader mode (check ). If you have voices for the reader article language installed, there may be some incorrect settings or defaults related to  configuration.

## File dialogs do not open when downloading files
If no file chooser is shown when downloading files, even with the option "Always ask where to save files" enabled in Firefox's settings, then you might not have both  and a suitable implementation. Desktop environments usually provide an implementation, but if you are using a standalone window manager such as i3, then you may need to manually install one. Install  and for example .

## Notifications are not floating in tiling window managers or Wayland compositors
If you are using a tiling window manager or a Wayland compositor, and the HTML notifications appear as normal Firefox windows instead of floating pop-ups, you need to install  and make sure you have a working Desktop notifications server, such as .

## DNIe certificate is not picked up after renewal from the card reader
After renewing the certificate in the card (Spanish DNIe) Firefox continues to use the previous certificate, allows to login but won't authenticate the users on any service. You need to clear the card cache

 $ pkcs15-tool --clear-cache
