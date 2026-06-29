# Firefox/Tweaks

This page contains advanced Firefox configuration options and performance tweaks.

## Performance
Improving Firefox's performance is divided into parameters that can be inputted while running Firefox or otherwise modifying its configuration as intended by the developers, and advanced procedures that involve foreign programs or scripts.

This section contains advanced Firefox options for performance tweaking. For additional information see these MozillaZine articles.

## Change Performance settings
Firefox automatically uses settings based on the computer's hardware specifications Adjusting these settings can be done in Preferences or by changing the  value to  and  to  manually in .

However you may want to manually adjust this setting to increase performance even further or decrease memory usage on low-end devices.

In this case the Content process limit for the current user has been increased to 4:

## WebRender
WebRender is a high-performance, GPU-accelerated 2D rendering engine written in Rust. It is the compositor that powers Firefox and the Servo browser engine project. As of Firefox 93, it is enabled by default for all users and uses hardware rendering by default if the hardware it is running on [https://searchfox.org/mozilla-central/rev/2b3f6e5bf3ed0f13a08d0efbafeca57df6616ffa/gfx/webrender_bindings/WebRenderAPI.cpp#141 supports at least OpenGL 3.0 or OpenGL ES 3.0 (as of 2021-04) and meets minimum driver requirements. If your system does not meet these requirements it will fallback to software rendering using Software WebRender.

You can force GPU-accelerated WebRender for all tasks by setting  preference to  in .

If you are experiencing rendering issues with up-to-date drivers on your machine, you can force-enable Software WebRender by setting the  preference to .

## Turn off the disk cache
Every object loaded (html page, jpeg image, css stylesheet, gif banner) is saved in the Firefox cache for future use without the need to download it again. It is estimated that only a fraction of these objects will be reused, usually about 30%. This is because of very short object expiration time, updates or simply user behavior (loading new pages instead of returning to the ones already visited). The Firefox cache is divided into memory and disk cache and the latter results in frequent disk writes: newly loaded objects are written to memory and older objects are removed.

An alternative approach is to use  settings:

* Set  to
* Verify that  is set to , more information about this option can be found in the browser.cache.memory Mozilla article
* Add the entry  and set it to the amount of KB you want to spare, or to  for automatic cache size selection (skipping this step has the same effect as setting the value to )
** The "automatic" size selection is based on a decade-old table that only contains settings for systems at or below 8GB of system memory.  The following formula very closely approximates this table, and can be used to set the Firefox cache more dynamically:  , where  is in GB and the result is in KB.

This method has some drawbacks:

* The content of currently browsed webpages is lost if the browser crashes or after a reboot, this can be avoided using anything-sync-daemon or any similar periodically-syncing script so that cache gets copied over to the drive on a regular basis
* The settings need to be configured for each user individually

## Move disk cache to RAM
An alternative is to move the "disk" cache to a RAM disk, giving you a solution in between the two above. The cache will now be preserved between Firefox runs (including Firefox crash recovery), but will be discarded upon reboot (including OS crash).

To do this, go to  and set  to , where  is your user's ID which can be obtained by running .

Open  to verify the new disk cache location.

## Longer interval between session information record
Firefox stores the current session status (opened urls, cookies, history and form data) to the disk on a regular basis. It is used to recover a previous session in case of crash.
The default setting is to save the session every 15 seconds, resulting in frequent disk access.

To increase the save interval to 10 minutes (600000 milliseconds) for example, change in  the setting of  to

To disable completely this feature, change  to .

## Defragment the profile's SQLite databases
Firefox keeps bookmarks, history, passwords in SQLite databases. SQLite databases become fragmented over time and empty spaces appear all around. But, since there are no managing processes checking and optimizing the database, these factors eventually result in a performance hit. A good way to improve start-up and some other bookmarks and history related tasks is to defragment and trim unused space from these databases.

You can use  to do this, while Firefox is not running:

{| class="wikitable"
|+ profile-cleaner usage example:
! SQLite database || Size Before || Size After || % change
|-
|urlclassifier3.sqlite|| 37 M || 30 M || 19 %
|-
|places.sqlite || 16 M || 2.4 M || 85 %
|-
|}

Firefox provides a tool to defragment and optimize the places database, which is the source of most slowdowns and profile corruptions. To access this tool, open the  page, search for  and click the  button.

## Cache the entire profile into RAM via tmpfs
If the system has memory to spare,  can be used to cache the entire profile directory, which might result in increased Firefox responsiveness.

## Force-enable hardware video decoding
Although  is enabled by default, one may need to force-enable hardware video decoding by setting  to .

## Automatically unload inactive tabs
To only unload tabs that are at least 1 hour inactive, set the following in :

*  must be set to
*  to
*  to

## Appearance
## Fonts
See the main article: Font configuration

## Configure the DPI value
Modifying the following value can help improve the way fonts looks in Firefox if the system's DPI is below 96.  Firefox, by default, uses 96 and only uses the system's DPI if it is a higher value. To force the system's DPI regardless of its value, type  into the address bar and set  to 0.

Note that the above method only affects the Firefox user interface's DPI settings. Web page contents still use a DPI value of 96, which may look ugly or, in the case of high-resolution displays, may be rendered too small to read. A solution is to change  to system's DPI divided by 96. For example, if your system's DPI is 144, then the value to add is 144/96 = 1.5. Changing  to 1.5 makes web page contents use a DPI of 144, which looks much better.

If this results in fonts that are undesirably large in releases after Firefox 103, change  to zero. Then, type  into the  search bar, select the circle next to 'number,' click the plus button to add the setting key, and edit its value to 100 times your  value. For example, if that was set to 1.25,  should be set to 125.

See also HiDPI#Firefox for information about HiDPI displays and  for calculating the DPI.

## Default font settings from Microsoft Windows
Below are the default font preferences when Firefox is installed in Microsoft Windows. Many web sites use the Microsoft fonts.

## General user interface CSS settings
Firefox's user interface can be modified by editing the  and  files in  (profile_dir is of the form hash.name, where the hash is an 8 character, seemingly random string and the profile name is usually default). You can find out the exact name by typing  in the URL bar, and searching for the  field under the  section as described in the [https://support.mozilla.org/en-US/kb/profiles-where-firefox-stores-user-data#w_how-do-i-find-my-profile Firefox documentation.

This section only deals with the  file which modifies Firefox's user interface, and not web pages.

## Change the interface font
The setting effectively overrides the global GTK font preferences, and does not affect webpages, only the user interface itself:

{{hc|~/.mozilla/firefox/profile/chrome/userChrome.css|
* {
    font-family: "FONT_NAME";
}
}}

## Hide button icons
Enables text-only buttons:
{{hc|~/.mozilla/firefox/profile/chrome/userChrome.css|
.button-box .button-icon {
    display: none;
}
}}

## Hiding various tab buttons
These settings hide the arrows that appear to the horizontal edges of the tab bar, the button that toggles the "all tabs" drop-down list, and the plus sign button that creates a new tab.

{{hc|~/.mozilla/firefox/profile/chrome/userChrome.css|
/* Tab bar */

toolbarbutton#scrollbutton-up, toolbarbutton#scrollbutton-down {
    /* Hide tab scroll buttons */
    display: none;
}

.browser-toolbar > * #alltabs-button {
    /* Hide tab drop-down list */
    display: none;
}

.browser-toolbar > * #new-tab-button {
    /* Hide new-tab button */
    display: none;
}
}}

## Vertical/tree tabs
To place the tab bar in a sidebar/tree, use one of the following:

* Native vertical tabs (since Firefox 140.0)
* Tree Style Tab
* Sidebery
* Tabby

Firefox addons cannot hide the native tab bar through its extension APIs - to do so, follow the setup/advanced instructions for your addon.

## Hide title bar and window border
To replace the title bar with the tab bar, set  to  in .

Or go to "More tools", then "Customize toolbar" and then at the bottom-left corner find checkbox named "Title Bar". Uncheck it. If the checkbox is missing, make sure the  environment variable is correctly set and/or the  environment variable is set to "client".

## Auto-hide Bookmarks Toolbar
{{hc|~/.mozilla/firefox/profile/chrome/userChrome.css|
#PersonalToolbar {
    visibility: collapse !important;
}

#navigator-toolbox:hover > #PersonalToolbar {
    visibility: visible !important;
}
}}

## Remove sidebar width restrictions
{{hc|~/.mozilla/firefox/profile/chrome/userChrome.css|
/* remove maximum/minimum  width restriction of sidebar */
#sidebar {
    max-width: none !important;
    min-width: 0px !important;
}
}}

## Unreadable input fields with dark GTK themes
When using a dark GTK theme, one might encounter Internet pages with unreadable input and text fields (e.g. text input field with white text on white background, or black text on dark background). This can happen because the site only sets either background or text color, and Firefox takes the other one from the theme. To prevent Firefox from using theme's colors and dark themes in web pages respectively confirm  and  are set to  in .

Otherwise, if the previous modification did not solve the issue, it is possible to launch Firefox with a light GTK theme by adding a new string in  named  and setting it to a light theme like  or .

## Override input field color with CSS
The extension Text Contrast for Dark Themes sets the other color as needed to maintain contrast.

Alternatively set the standard colors explicitly for all web pages in  or using the stylus add-on.
The style sheet is usually located in your profile folder (visit  for the path) in , if not you can create it there.

The following sets input fields to standard black text / white background; both can be overridden by the displayed site, so that colors are seen as intended:

{{bc|1=
input:not(.urlbar-input):not(.textbox-input):not(.form-control):not(textarea, select {
    -moz-appearance: none !important;
    background-color: white;
    color: black;
}

#downloads-indicator-counter {
    color: white;
}
}}

## Change the GTK theme
To force Firefox to use a light theme (e.g. Adwaita) for both web content and UI, see GTK#Themes.

## Change the GTK theme for content process only
To force Firefox to use a light theme (e.g. Adwaita) for web content only:

# Open  in the address bar.
# Create a new  string type entry ( > New > String).
# Set the value to the light theme to use for rendering purposes (e.g. ).
# Restart Firefox.

## Web content CSS settings
This section deals with the  file in which you can add custom CSS rules for web content. Changes to this file will take effect once the browser is restarted.

This file can be used for making small fixes or to apply personal styles to frequently visited websites. Custom stylesheets for popular websites are available from sources such as [https://userstyles.org/ userstyles.org. You can install an add-on such as superUserContent to manage themes. This add-on creates the directory  and applies changes to the CSS files therein when the page is refreshed.

## Import other CSS files
## Block certain parts of a domain
{{hc|~/.mozilla/firefox/profile/chrome/userContent.css|
@-moz-document domain(example.com) {
    div#header {
        background-image: none !important;
    }
}
}}

## Add after links to PDF files
{{hc|~/.mozilla/firefox/profile/chrome/userContent.css|
/* add '[pdf' next to links to PDF files */
a{
    font-size: smaller;
    content: " [pdf";
}
}}

## Mouse and keyboard
## Mouse wheel scroll speed
To modify the default values (i.e. speed-up) of the mouse wheel scroll speed, go to  and search for . This will show the available options, modifying the following:

* Set  to .
* Set  to the desired number ( to  are common values).

Alternatively, to use system values (as how scrolling works in Chromium), set  to .

Mozilla's recommendation for increasing the mousewheel scroll speed is to:

* Set  between  and  (default: )

## Pixel-perfect trackpad scrolling
To enable one-to-one trackpad scrolling (as can be witnessed with GTK3 applications like Nautilus), set the  environment variable before starting Firefox.

If scrolling is undesirably jerky, try enabling Firefox's Use smooth scrolling option under Preferences > General > Browsing.

## Enable touchscreen gestures
On Wayland, touchscreen gestures are enabled by default.

On X11, make sure  is either set to 1 (enabled) or 2 (default, auto-detect), and set the  environment variable.

On some devices, it may be necessary to disable xinput's touchscreen gestures by running the following:

 $ xsetwacom --set device Gesture off

## Mouse click on URL bar's behavior
In older versions of Firefox it was possible to tweak the behavior of the address bar in , but this has been removed in March 2020.

In order to for example disable the behavior that selects the contents of the address bar on first click, or to allow to double click the URL to select it in full, see user contributed scripts such as https://github.com/SebastianSimon/firefox-omni-tweaks

## Smooth scrolling
In order to get smooth physics-based scrolling in Firefox, the  configurations can be changed to emulate a snappier behaviour like in other web browsers. For a quicker configuration, append the following to  (requires restart):

 user_pref("general.smoothScroll.lines.durationMaxMS", 125);
 user_pref("general.smoothScroll.lines.durationMinMS", 125);
 user_pref("general.smoothScroll.mouseWheel.durationMaxMS", 200);
 user_pref("general.smoothScroll.mouseWheel.durationMinMS", 100);
 user_pref("general.smoothScroll.msdPhysics.enabled", true);
 user_pref("general.smoothScroll.other.durationMaxMS", 125);
 user_pref("general.smoothScroll.other.durationMinMS", 125);
 user_pref("general.smoothScroll.pages.durationMaxMS", 125);
 user_pref("general.smoothScroll.pages.durationMinMS", 125);

Additionally the mouse wheel scroll settings have to be changed to react in a smooth way as well:

 user_pref("mousewheel.min_line_scroll_amount", 30);
 user_pref("mousewheel.system_scroll_override_on_root_content.enabled", true);
 user_pref("mousewheel.system_scroll_override_on_root_content.horizontal.factor", 175);
 user_pref("mousewheel.system_scroll_override_on_root_content.vertical.factor", 175);
 user_pref("toolkit.scrollbox.horizontalScrollDistance", 6);
 user_pref("toolkit.scrollbox.verticalScrollDistance", 2);

If you have troubles on machines with varying performance, try modifying the  until it feels snappy enough.

For a more advanced configuration which modifies the mass-spring-damper parameters, see AveYo's natural smooth scrolling configuration.

## Jerky or choppy scrolling
Scrolling in Firefox can feel "jerky" or "choppy". A post on MozillaZine gives settings that work on Gentoo, but reportedly work on Arch Linux as well:

# Set   to 40
# Set   and  to false
# Set   to something really large such as 2100000000 but no more than 2140000000.  Above that number Firefox will not accept your entry and complain with the error code:  "The text you entered is not a number."
# Set   to at least 512K

Now scrolling should flow smoothly.

## Set backspace's behavior
See Firefox#Backspace does not work as the 'Back' button.

## Disable middle mouse button clipboard paste
See Firefox#Middle-click behavior.

## Emacs key bindings
To have Emacs/Readline-like key bindings active in text fields, see GTK#Emacs key bindings.

## Miscellaneous
## Remove full screen warning
Warning about video displayed in full screen mode (… is now fullscreen) can be disabled by setting  to  in .

## Change the order of search engines in the Firefox Search Bar
To change the order search engines are displayed in:

* Open the drop-down list of search engines and click Manage Search Engines... entry.
* Highlight the engine you want to move and use Move Up or Move Down to move it. Alternatively, you can use drag-and-drop.

## "I'm Feeling Lucky" mode
Some search engines have a "feeling lucky" feature. For example, Google has "I'm Feeling Lucky".

To activate them, search for  in  and modify its value (if any) to the URL of the search engine.

For Google, set it to:

## Secure DNS with DNSSEC validator
You can enable DNSSEC support for safer browsing.

## Secure DNS with DNS over HTTPS
See Domain name resolution#Application-level DNS.

## Adding magnet protocol association
In  set  to . In case it does not exist, it needs to be created, right click on a free area and select New > Boolean, input  and set it to .

The next time you open a magnet link, you will be prompted with a Launch Application dialogue. From there simply select your chosen BitTorrent client. This technique can also be used with other protocols: .

## Prevent accidental closing
There are different approaches to handle this:

This behavior can be disabled with  property set to  in

An alternative is to add a rule in your window manager configuration file. For example in Openbox add:

      false

in the '''' section of your  file.

The Disable Ctrl-Q and Cmd-Q extension can be installed to prevent unwanted closing of the browser.

## Run Firefox inside an nspawn container
See systemd-nspawn#Run Firefox.

## Disable WebRTC audio post processing
If you are using the PulseAudio PulseAudio#Microphone echo/noise cancellation, you probably do not want Firefox to do additional audio post processing.

To disable audio post processing, change the value of the following preferences to :

*  (Acoustic Echo Cancellation)
*  (Automatic Gain Control)
*  (Noise suppression)
*  (High-pass filter)

## Fido U2F authentication
Firefox supports the Fido U2F authentication protocol. Install  for the required udev rules.

## Force-enable WebGL
On some platforms WebGL may be disabled even when the user desires to use it. To force-enable WebGL set  to , to also force-enable WebGL anti-aliasing, set  to .

If you get an error similar to this:

then you can try the solution explained in Firefox bug 1480755 Set  to

## Prevent the download panel from opening automatically
As of Firefox 98, the download panel (with ongoing/recent downloads) always opens whenever a download starts.

You can disable this behavior by setting the  preference to  in .
