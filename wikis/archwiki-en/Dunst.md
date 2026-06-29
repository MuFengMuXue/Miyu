# Dunst

Dunst is a lightweight replacement for the notification-daemons provided by most desktop environments.

## Installation
Install the  package.

An example configuration file is included at . Copy this file to  and edit it accordingly.

Launch  and make sure your window manager or desktop environment starts it on startup/login.

## Appearance
Text in notifications can be styled. Some examples are bold, italics, strikethrough and underline. For a complete reference see Pango markup. Pango can be stripped from notifications if  is set to .

The formatting of the notification can be specified. Options are as follows:
 %a  appname
 %s  summary
 %b  body
 %i  iconname (including its path)
 %I  iconname (without its path)
 %p  progress value if set ([  0%] to or nothing

These can be used in conjunction with HTML markup. For example the  can be set to  for a bolded notification summary, a newline and the body unformatted.

## Icon sets
Icons are set in the option  of the  section of the configuration file. Status, devices and legacy icons are needed. By default, Dunst looks for the  icons. For example, to use  (gnome-icon-theme's successor), instead:

 icon_path = /usr/share/icons/Adwaita/16x16/status/:/usr/share/icons/Adwaita/16x16/devices/:/usr/share/icons/Adwaita/16x16/legacy/

Instead of specifying the path to the icon folder, it is possible to specify the icon theme directly, also in the  section of the configuration file. In this case, you also need to set  to enable search in the subfolders of the theme main folder.

Example:

 icon_theme = Papirus
 enable_recursive_icon_lookup = true

## Shortcuts
Dunst can be controlled with dunstctl. You can update your keyboard shortcuts to call dunstctl.

For example, to close all notifications:
 $ dunstctl close-all

To show history:
 $ dunstctl history-pop

## Rules
You can create rules in your dunstrc file which match certain notifications and then perform an action on it such as executing a script.

## Filtering
To create a new rule, create a new section with a custom name in your configuration file.
In that section you can now use the attributes appname, summary, body, icon, category, match_transient and msg_urgency to match the notification.
Globbing is supported. See Scripting for an example.
Start dunst with the  option to find out useful information about a notification to write proper rules.

## Modifying
When a notification is matched you can perform certain actions on it like modifying the format string, which is especially
useful if you want to completely ignore certain notifications.
In that case simply add the line  to your rule.

Another useful feature is if you want to keep certain notifications out of your history for example if you use dunst
as a Volume indicator.
To achieve this simply add  to your rule.

## Scripting
Dunst can be configured to run scripts based on certain notification content. Here is an example using Dunst to run a script when someone from  signs on:

 [signed_on
    appname = Pidgin
    summary = "*signed on*"
    urgency = low
    script = do_something.sh

The specified script will be passed the following parameters in that order: appname, summary, body, icon, urgency.

## Disable dunst temporarily
To disable dunst temporarily there are two options.

;Use
:You can use  to disable/reenable or toggle pausing notifications. Use  to check if dunst is currently running or paused.

;Use
:Use  to disable and  to reenable

Once paused dunst will hold back all notifications.
After enabling dunst again all held back notifications will be displayed.

## Dunstify
Dunstify is an alternative to the notify-send command
which is completely compatible to notify-send and can be used alongside it, but offers some more features.

Additionally to the options available in notify-send, dunstify offers some more features like IDs and actions.

## Replacing notifications
You can assign an ID to a notification by calling dunstify with the  option, where  must be an integer.
If a notification with that ID already exists it will be replaced with the new one.
You may also close a notification with .

However, for most use cases, implementing tags is preferred over micromanaging IDs because the latter option has many hidden pitfalls Replacing IDs may be considered for debugging and for very complex notification senders instead of common practice [https://github.com/dunst-project/dunst/issues/672#issuecomment-554530659.

Notifications with the same tag ("test" in this example) are replaced without having to care for IDs.

 $ dunstify -h string:x-dunst-stack-tag:test Test -A 'tested,default'
 $ dunstify -h string:x-dunst-stack-tag:test Testing

## Actions
You can define actions which can be invoked directly from the notification by specifying one or more  parameters.
For instance:

 $ dunstify --action="replyAction,reply" "Message received"

The user can then access the specified actions via Dunst's context menu. The call to dunstify will block until either the notification disappears or an action is selected. In the former case dunstify will return 1 if the notification timed out and 2 if it was dismissed manually In the latter case it returns the action which was selected by the Dunst context menu.

In addition to invoking actions with the context menu, you may also define how mouse events invoke actions [https://github.com/dunst-project/dunst/blob/3f3082efb3724dcd369de78dc94d41190d089acf/dunstrc#L237. This allows Dunst to be used interactively, as was suggested in When a notification has only one action, or when an action is named "default", that action may be invoked by middle-clicking the notification (by default or when  defines ).

{{bc|
reply_action () {}
forward_action () {}
handle_dismiss () {}

ACTION=$(dunstify --action="default,Reply" --action="forwardAction,Forward" "Message Received")

case "$ACTION" in
"default")
    reply_action
    ;;
"forwardAction")
    forward_action
    ;;
"2")
    handle_dismiss
    ;;
esac
}}

## Tips and tricks
## Using dunstify as volume/brightness level indicator
You can use the replace id feature to implement a simple volume or brightness indicator notification like in this picture [https://i.postimg.cc/j2CDkS1H/screen1712.png.

To realize that volume indicator place the following script somewhere on your .

{{bc|
#!/bin/bash
# changeVolume

# Arbitrary but unique message tag
msgTag="myvolume"

# Change the volume using alsa(might differ if you use PulseAudio)
amixer -c 0 set Master "$@" > /dev/null

# Query amixer for the current volume and whether or not the speaker is muted
volume="$(amixer -c 0 get Master | tail -1 | awk '{print $4}' | sed 's/mute="$(amixer -c 0 get Master | tail -1 | awk '{print $6}' | sed 's/[^a-z*//g')"
if | "$mute" == "off" ; then
    # Show the sound muted notification
    dunstify -a "changeVolume" -u low -i audio-volume-muted -h string:x-dunst-stack-tag:$msgTag "Volume muted"
else
    # Show the volume notification
    dunstify -a "changeVolume" -u low -i audio-volume-high -h string:x-dunst-stack-tag:$msgTag \
    -h int:value:"$volume" "Volume: ${volume}%"
fi

# Play the volume changed sound
canberra-gtk-play -i audio-volume-change -d "changeVolume"
}}

Now simply bind  etc. to some hotkey and you are done. You might also want to make dunst ignore these type of notifications in its history. See #Modifying.

## Overwrite previous notification
For some notifications (for example sound or brightness), you might want to overwrite the previous notification. You can either use the Dunst method in #Replacing notifications or refer to Desktop notifications#Replace previous notification for a more general example.

## Troubleshooting
## Dunst fails to start via systemd
When using dunst without a Display Manager, the  environment variable might not be correctly set.To fix this, add the following to your :
 systemctl --user import-environment DISPLAY

## Non-matching font sizes (Emojis much larger than text)
This is caused by  not rescaling bitmap fonts. This is usually only noticed with certain emoji fonts (e.g. )

To solve, simply run:
 # ln -s /etc/fonts/conf.avail/10-scale-bitmap-fonts.conf /etc/fonts/conf.d/

and restart Dunst.

## Notifications from some applications do not obey timeout rules
The symptoms for this issue is having configured the timeouts for all urgency levels to be 30 seconds, but notifications from certain applications, such as Discord, Mattermost, and GitLab, disappearing very quickly (typically after only 3 seconds).

You can find more details about this in upstream's [https://github.com/dunst-project/dunst/issues/276 issue #276.

This occurs because the notifications are being closed forcefully. To address this, a special parameter called  has been introduced. You can enable this parameter to disregard the  message sent via D-Bus. Enabling it ensures that the timeout defined in the dunst configuration is respected. By default, this parameter is set to false.
