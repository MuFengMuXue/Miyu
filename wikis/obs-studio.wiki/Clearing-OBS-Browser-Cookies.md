Much like a standard browser, the browser sources and docks in OBS store information for things like logins and website settings in cookies.

In some cases it may be necessary to clear your cookies in OBS due to changes to the underlying browser systems, or due to compatibility with third party plugins after an update.

Follow the steps below for your operating system to clear OBS browser cookies.

# Windows

**Clearing Browser Source Cookies**

1. Exit OBS (make sure OBS is not running)
2. Delete the folder `%appdata%\obs-studio\plugin_config\obs-browser\obs_profile_cookies`
3. Start OBS
4. Settings -> Stream -> Disconnect Account -> Connect Account

**Clearing Browser Dock Cookies**

1. Exit OBS (make sure OBS is not running)
2. Delete the file `%appdata%\obs-studio\plugin_config\obs-browser\Cookies`
3. Start OBS
4. Settings -> Stream -> Disconnect Account -> Connect Account

# macOS

1. Exit OBS (make sure OBS is not running)
2. Delete the folder `~/Library/Application Support/obs-studio/plugin_config/obs-browser/obs_profile_cookies`
3. Start OBS
4. Settings -> Stream -> Disconnect Account -> Connect Account

# Linux

1. Exit OBS (make sure OBS is not running)
2. Delete the folder `~/.config/obs-studio/plugin_config/obs-browser/obs_profile_cookies`
3. Start OBS
4. Settings -> Stream -> Disconnect Account -> Connect Account

*Please note that the location of OBS browser cookies on Linux could differ depending on your distro and whether or not you are using an official release. OBS is available officially as an Ubuntu PPA and via Flathub.*