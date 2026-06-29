**D**igital **r**ights **m**anagement (**DRM**) is a system to prevent piracy of copyrighted material. It is not possible to access DRM protected content with only open source software. DRM is highly controversial which does not matter for this article.

## Contents

-   [[1] [Firefox]](#Firefox)
-   [[2] [Chromium and Google Chrome]](#Chromium_and_Google_Chrome)
-   [[3] [Browsers installed with Flatpak]](#Browsers_installed_with_Flatpak)
-   [[4] [Troubleshooting]](#Troubleshooting)
    -   [[4.1] [Disney+ not working]](#Disney.2B_not_working)
    -   [[4.2] [LibreWolf not downloading DRM plugins]](#LibreWolf_not_downloading_DRM_plugins)
    -   [[4.3] [Netflix]](#Netflix)
-   [[5] [See also]](#See_also)

## [Firefox]

The default USE flags for [Firefox](https://wiki.gentoo.org/wiki/Firefox "Firefox") allow DRM-protected content to be played. When changing the defaults USE flags, both `eme-free` and `gmp-autoupdate` USE flags affect Firefox\'s ability to play DRM-protected content.

For [[[www-client/firefox]](https://packages.gentoo.org/packages/www-client/firefox)[]], the `eme-free` USE flag must be disabled, otherwise Firefox will be compiled with no DRM capability. And the `gmp-autoupdate` USE flag must be enabled in order to allow Firefox to download the Widevine plugin at runtime, which is needed to play DRM content.

When using the [[[www-client/firefox-bin]](https://packages.gentoo.org/packages/www-client/firefox-bin)[]] package, no `eme-free` USE flag exists and therefore does not need to be disabled. The `gmp-autoupdate` USE flag still needs to be enabled.

Now emerge Firefox:

`root `[`#`]`emerge --ask www-client/firefox`

For Firefox to download the plugins required to decrypt DRM content, go to: [Settings] → [General] → [Digital Rights Management (DRM) Content] and tick [Play DRM-controlled content]. When a video player which plays DRM content is opened, Firefox will start downloading the required plugins. This process might take a few minutes. Refresh the page to check if the plugins were successfully downloaded.

## [Chromium and Google Chrome]

See [[[bug #547630]](https://bugs.gentoo.org/show_bug.cgi?id=547630)[]].

Enable the `widevine` USE flag for [[[www-client/chromium]](https://packages.gentoo.org/packages/www-client/chromium)[]], as well as [[[www-plugins/chrome-binary-plugins]](https://packages.gentoo.org/packages/www-plugins/chrome-binary-plugins)[]] in [/etc/portage/package.use]. This can be done by adding these lines to the file:

[FILE] **`/etc/portage/package.use`**

    www-plugins/chrome-binary-plugins widevine
    www-client/chromium widevine

Next emerge the packages:

`root `[`#`]`emerge --ask www-plugins/chrome-binary-plugins www-client/chromium`

If Google Chrome is used instead of Chromium, replace `www-client/chromium` with `www-client/google-chrome` in [/etc/portage/package.use] and emerge [[[www-client/google-chrome]](https://packages.gentoo.org/packages/www-client/google-chrome)[]] instead of [[[www-client/chromium]](https://packages.gentoo.org/packages/www-client/chromium)[]]:

`root `[`#`]`emerge --ask www-client/google-chrome`

## [Browsers installed with Flatpak]

Any browser that is installed through Flatpak and that supports DRM decryption should not require any extra steps related to Gentoo to play DRM content.

## [Troubleshooting]

### [][Disney+ not working]

There have been multiple incidents where it was not possible to stream anything from Disney+ on Linux because of a new DRM.^[\[1\]](#cite_note-1)[\[2\]](#cite_note-2)^ This issue can be bypassed by switching the browser\'s user agent so that it imitates Microsoft Windows. There are browser extensions for browsers using Blink (e. g. Chromium) and Gecko (e. g. Firefox) as their browser engine.^[\[3\]](#cite_note-3)^ It is also possible to change the browser\'s user agent to anything in Firefox and browsers based on Firefox. This is not advised as it can lead to fingerprinting.

### [LibreWolf not downloading DRM plugins]

For older versions of [LibreWolf](https://wiki.gentoo.org/wiki/LibreWolf "LibreWolf") are extra steps required to get the DRM plugins downloading.^[\[4\]](#cite_note-4)^ A few lines need to be commented out. If LibreWolf was installed using Portage, edit [/usr/lib/librewolf/librewolf.cfg]. If LibreWolf was installed using Flatpak, edit [\~/.local/share/flatpak/app/io.gitlab.librewolf-community/current/active/files/lib/librewolf/librewolf.cfg].

[FILE] **`/usr/lib/librewolf/librewolf.cfg`**

    /** [SECTION] DRM */
    /** defaultPref("media.eme.enabled", false); // master switch for drm content
      * defaultPref("media.gmp-manager.url", "data:text/plain,"); // prevent checks for plugin updates when drm is disabled
      * // disable the widevine and the openh264 plugins
      * defaultPref("media.gmp-provider.enabled", false);
      * defaultPref("media.gmp-gmpopenh264.enabled", false);
      */

### [Netflix]

In Netflix settings navigate to: [Your Account] → [Your Profile] → [Playback Settings], ensure that \"[Prefer HTML5 player instead of Silverlight]\" is checked (it should be by default; just verify).

## [See also]

-   [Streaming DRM protected content/Pipelight](https://wiki.gentoo.org/wiki/Streaming_DRM_protected_content/Pipelight "Streaming DRM protected content/Pipelight")

1.  [[[↑](#cite_ref-1)] [[https://itsfoss.com/disney-plus-linux/](https://itsfoss.com/disney-plus-linux/)]]
2.  [[[↑](#cite_ref-2)] [[https://www.reddit.com/r/linuxquestions/comments/yfjeaz/disney_no_longer_working_on_linux/](https://www.reddit.com/r/linuxquestions/comments/yfjeaz/disney_no_longer_working_on_linux/)]]
3.  [[[↑](#cite_ref-3)] [[https://add0n.com/useragent-switcher.html](https://add0n.com/useragent-switcher.html)]]
4.  [[[↑](#cite_ref-4)] [[https://www.youtube.com/watch?v=bJsdnBxDKI8](https://www.youtube.com/watch?v=bJsdnBxDKI8)]]