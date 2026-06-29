# Discord

Discord is a proprietary, cross-platform, all-in-one voice and text chat application. Many open-source communities have official Discord servers as well. Discord can be used through a web browser or through the desktop application, which is made with Electron.

## Installation
Install the  package.

Alternatively, install the  package, which enables using the system-provided  for increased security and potentially better performance.

## Development builds
Discord also has alternative packages for users that want to test features that are currently in development:

*  — public test build, which includes more or less robust beta features that are close to reaching stable channels.
*  — alpha build, which includes features in early development.

## Vendor packages
Discord also provides native Arch Linux packages from their official website:

* Stable — https://discord.com/api/download/stable?platform=linux&format=pkg.tar.zst
* PTB — https://discord.com/api/download/ptb?platform=linux&format=pkg.tar.zst
* Canary — https://discord.com/api/download/canary?platform=linux&format=pkg.tar.zst

## Third-party clients
*
*
*
*
*
*
*
*
*

## Command-line clients
There are numerous CLI-based third party clients on the AUR (and non-packaged ones on Github), although most are deprecated or broken.

*

## Chat client plugins
*
*
*

## Custom CSS & plugins
*
*
*
*

## Overlay
For Linux clients, Discord does not support in-game overlay.  is an open-source GTK application that provides these functions. Discover works on X11 or wlroots environments. This is not compatible with third-party clients, due to relying on advanced RPC.

## Utilities
*

## Tips and tricks
## GNOME top bar icon
If you would like to have the icon on the top bar of GNOME, install the AppIndicator and KStatusNotifierItem Support extension and .

## Discord asks for an update not yet available in the repository
Discord will refuse to launch if there is an update available, and the following message will be shown "Must be your lucky day, there's a new update!". If the updated version is not yet available in the official repos, you can build and install the updated package using the Arch build system.

To disable the update check, add the line  to . If the file does not exist, create it and add the following:

{{hc|~/.config/discord/settings.json|
{
  "SKIP_HOST_UPDATE": true
}
}}

Note that if the file exists, you will need to add an extra comma after the  object due to JSON requirements, i.e.:
{{bc|1=
{
  "IS_MAXIMIZED": true,
  "IS_MINIMIZED": false,
  "WINDOW_BOUNDS": {
    "x": 2240,
    "y": 219,
    "width": 1280,
    "height": 720
  },
  "SKIP_HOST_UPDATE": true
}
}}

In case the above method still asks for an update a quick temporary alternative is to extract the new  file into e.g. , change the name of the newly extracted , and symlink it into your  folder, preferably also changing the Name inside the new  file in order to differentiate it from your system discord client.

## Start Discord minimized
Discord can be started minimized through the  argument.

## Microphone noise suppression
Discord now has noise suppression built in, with both a standard option and an AI-powered option provided by Krisp. You can also provide your own noise suppression on PipeWire by following PipeWire#Noise suppression for voice.

## Screen sharing with audio
Discord now natively supports audio streaming with Wayland on Linux, support was added in version 0.0.76.

## Web RPC extensions
There are extensions available to show selected web activity in your Discord rich presence:
*  with appropriate browser extension.
*  with PreWrap or Mal-sync browser extensions.

## Enabling developer tools
Devtools are disabled by default on Discord for safety reasons. To re-enable them, add this to :

   "DANGEROUS_ENABLE_DEVTOOLS_ONLY_ENABLE_IF_YOU_KNOW_WHAT_YOURE_DOING": true

## Enabling text-to-speech
By default, text-to-speech is disabled in the Discord client. However, it can be enabled using the  flag. This utilizes the  daemon to output the speech.

## Native Wayland rendering
Discord and other Electron apps by default use X11 and run through Xwayland on Wayland sessions. However, this can be changed. See Wayland#Electron.

## Troubleshooting
## General app lag
Check if hardware video acceleration is properly enabled. This can fix lag when scrolling through servers (guilds) and also problems related to screen-sharing.

## Crackling during voice calls
If using PulseAudio, try switching to PipeWire. Alternatively, try the steps outlined in PulseAudio/Troubleshooting#Troubleshooting buffer underruns (glitches, skips, crackling).

## Enabling rich presence on Flatpak
When using the Flatpak version of Discord, Rich Presence will not work out of the box. To make it work, it is necessary to create a symlink from  to . To create the symlink for the current user session, run:

 $ ln -sf $XDG_RUNTIME_DIR/{app/com.discordapp.Discord,}/discord-ipc-0

To automatically create the symlink, systemd-tmpfiles can be used by adding the following line to a file with the .conf extension in :

 L %t/discord-ipc-0 - - - - app/com.discordapp.Discord/discord-ipc-0

## Discord becomes unresponsive during long calls
If Discord becomes unresponsive during long calls, launching it with the  command-line argument may help.

## Discord freezes after getting pinged or messaged
If a message that would trigger a notification (pings, direct messages, servers with notifications ON etc.) causes the client to freeze, the client is failing to find a notification server. To fix it without installing a notification server, disable Enable Desktop Notifications in the Notifications settings page.

## Notification sounds do not work with PipeWire
See PipeWire#No notification sounds from Discord.

## Emojis are not rendered correctly
If you encounter rendering issues regarding emojis (such as them being rendered as rectangles), your system is missing emoji font packages. See Fonts#Emoji and symbols.

## Clicking a link does not open the web browser
If clicking a link does not open a tab in your default web browser, install the  optional dependency.

## Blurry Discord icon in KDE Plasma system tray
You can attempt to fix this issue by installing  to replace , which is known to cause this issue.

## Discord spams systemd journal
You may find that Discord creates a lot of messages in your journal in a format like:

 (device_info_linux.cc:45): NumberOfDevices

To disable the logging that causes this pollution: go to App Settings, select "Voice & Video", at the bottom select "Debugging" and disable "Debug Logging".

## No voice chat in a pure-ALSA environment
Discord’s desktop application relies on PulseAudio for voice chat and does not run on ALSA directly. Using apulse as a workaround is, in this case, deprecated. If you want to use Discord’s voice chat without PulseAudio or Pipewire, access Discord’s web client through a Chromium-based web browser. Alternatively, as a Chromium-based wrapper, Webcord works in pure-ALSA environments. See also Chromium#No audio available without sound server.

If you choose this route and are unable to unmute, i.e., to get permission to access your microphone, set it as default capture device in . Also, in Discord, go to User Settings > Voice & Video > Input Device, and make sure Default is selected.

## Notification badge is missing
Discord can display a badge showing the number of unread mentions on the taskbar icon. If the badge is not displayed, verify that the  package is installed, as it is required for this feature to work.

Discord hardcodes the desktop entry , which breaks unread badge notifications on other Discord release channel builds such as  or .

To workaround this, create a copy of the desktop entry of your Discord build () and name it . For example, if you are using :

You can also create a dummy desktop entry file to replace the one provided by Discord, to avoid duplicated desktop entries showing up in your desktop environment.

## Black screen on Wayland on NVIDIA proprietary driver
Discord on Wayland requires VA-API support, which the NVIDIA proprietary driver does not have. A translation layer such as  can be used to get VA-API support.

## Microphone volume keeps lowering when Discord is active using Wireplumber
This can be fixed by adding a PipeWire quirk to Discord.

{{hc|~/.config/pipewire/pipewire-pulse.conf.d/99-stop-microphone-auto-adjust.conf|2=
pulse.rules = [
  {
    matches = [
            { application.process.binary = "Discord" }
    ]
    actions = { quirks = [
      block-source-volume
      block-sink-volume
    ]}
  }
]
}}

Then restart the ,  and  user units.
