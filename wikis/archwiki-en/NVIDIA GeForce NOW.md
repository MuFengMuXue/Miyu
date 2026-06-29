# NVIDIA GeForce NOW

GeForce NOW is a cloud gaming services that lets users play video games in the browser (including on Arch Linux) and on dedicated apps available on other platforms.

Unlike other cloud gaming platforms, GeForce NOW connects to video game digital distribution services such as Steam and the Epic game store, where  games have to be bought separately from the GeForce NOW subscription. Given the nature of Cloud Gaming, you will not need to install the client from these services on your computer.

It is available either as an official Flatpak package from NVIDIA, or can be used without installation in a Chromium-based web browser.

## Flatpak version
To install the Flatpak package, start by adding NVIDIA remote to your system:

 # flatpak remote-add --if-not-exists GeForceNOW https://international.download.nvidia.com/GFNLinux/flatpak/geforcenow.flatpakrepo

Then proceed to install the package:

 # flatpak install GeForceNOW com.nvidia.geforcenow

## Browser version
## Usage
GeForce NOW supports Chromium-based browsers out of the box, it should work for most people on Chromium.

## Non-qwerty keyboard layout
As of October 2021, the setting to change keyboard layout may not be visible when accessing GeForce NOW on Linux.

In some cases, the following steps allow to access this setting by making Chromium appear to run on Windows.

## Edit indexDB
The values for the keyboard layout are saved in the indexDB, in the database "gfnclient" in the objectstore "sharedStore". You can use a webextension like https://chrome.google.com/webstore/detail/indexeddbedit/npjecebdjnmlolggnoajngnlodhgpfac, to edit this values. Simply install the extension, reload play.geforcenow.com. Now open Dev-Tools (F12) and find the database with the objcetstore. Here you can add a key for "keyboardLayout" with the proper value for your language. German example:

 {
    "key": "keyboardLayout",
    "value": {
      "name": "Deutsch",
      "code": "de-DE"
    }
  },

After saving, reload the page and you are done.

As an alternative, a user-proivded extension exists, with all the currently pre-defined layouts from the GFN page. Since this extension is not in the Chrome Webstore, you must sideload it as unpacked extension.

## Launch Chromium with disabled User-Agent Client Hint
User-Agent Client Hint is a new feature on Chromium-based browser designed to improve over User-Agent strings. Unfortunately, because it is new, there is not yet an extension that let users change it.
To disable this feature, launch Chrome or Chromium this way :

 $ chromium --disable-features=UserAgentClientHint

## Change your User-Agent string to make your OS appears as Windows
Multiple extensions exist to switch the User-Agent string, they can be installed using the Chrome Webstore.
While Google provides one of these, it seems to not reliably alter the User-Agent string, notably on GeForce NOW.
User-Agent Switcher and Manager is another extension with this feature. The Firefox version being recommended by Mozilla, it seems trustworthy enough.

This later extension provides a list of common User-Agent strings to choose from. Selecting the first "Chrome on Windows" one will work.
If you are using another extension, a User-Agent string such as this one will work :
 Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.7113.93 Safari/537.36

## Access the keyboard layout setting
With these steps applied, the keyboard layout settings will be available in the main settings panel, below the Network settings.
