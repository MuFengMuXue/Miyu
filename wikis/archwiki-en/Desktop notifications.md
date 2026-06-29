# Desktop notifications

Desktop notifications are small, passive popup dialogs that notify the user of particular events in an asynchronous manner.

## Libnotify
 is a desktop-independent implementation of the Desktop Notifications Specification, which provides  utility and support for GTK and Qt applications. It is already used by many open source applications like Evolution and Pidgin.

## Notification servers
In order to receive notifications sent via libnotify, a notification server is required.

## Built-in
Cinnamon, Deepin, Enlightenment, GNOME, and GNOME Flashback use their own implementations to display notifications, and may not be able to be replaced since their notification servers are started automatically on login to receive notifications from applications via DBus.

On KDE Plasma if you enter the configuration for the System Tray you can disable the built-in notification server under System Services by changing the drop-down next to Notifications to Disabled. You can then add your preferred notification server in the System Settings menu under System / Autostart by adding a new Autostart application. You will need to log out and back in to take effect.

## Standalone
In other desktop environments, a notification server needs to be manually installed and launched using e.g. XDG Autostart.

Alternatively, by making the notification server a D-Bus service, the notification server can be launched automatically on the first call to it. Most notification servers already ship a dbus service under . For some implementations, e.g.  package, it's necessary to create one manually in the user D-Bus services directory ():

Whenever an application sends a notification by sending a signal to , D-Bus activates  if it has not already been activated.

You can also choose one of the following implementations:

*
*
*
*
*
*
*
:You can run it manually using .
*
*
*
*
*
*
*
:You can run it manually using .
:

## Tips and tricks
## Send notifications to another user
 can be used to enter another user's session and send notifications to them, e.g. from a background script running as root:

 # systemd-run --machine=target_user@.host --user notify-send 'Hello world!' 'This is an example notification.'

## Send notifications to all graphical users
This can be extended to send a notification to all graphical users with the following:

Another possibility is to use . The following command will show a notification to all users who run  in their user session:

 $ dbus-send --system / net.nuetzlich.SystemNotifications.Notify 'string:Hello world!' 'string:This is an example notification.'

## Replace previous notification
Notifications can be replaced if their ID is known; if a new notification request specifies the same ID, it will always replace the old notification. Unfortunately notify-send does not report this ID, so alternative tools are required to do this on CLI. One capable CLI-tool is the notify-send.py python script, which provides notify-send syntax with additional ID-reporting and replacing capabilities.

However, with some notification servers (such as Notify-OSD), you can use the  hint with notify-send to achieve the same result.

For example, to get a notification displaying time:

## Include Buttons or listen for close/on-click of the notification
With the notify-send.py script, actions can be used to display buttons or to listen for the default-action of the notification (usually, when the user clicks on it) and the close-action. When the action-icons hint is set to true and the notification daemon supports this, the buttons will display icons instead of text. The script prints the action identifier or "close" to the command line when the corresponding event has occured. To listen for the default action (on-click), one has to use the action-identifier "default".

Example with icons on buttons:

## Multiple notification servers with D-Bus services
As described in the section Standalone, users can create a D-Bus service so that a notification server can be launched automatically. Some implementations already include the D-Bus service files. However, this causes a problem when multiple notification servers are installed and when some of them come with the service files. For example, installing both  and  without explicitly specifying the desired server, D-Bus then chooses one for the users, and the decision is out of users' control. To avoid the situation, you can override the service used by creating an  (see #Standalone) and pointing to the service you want to use, then restarting the session.

## Troubleshooting
## Applications hanging for exactly one minute
If applications hang when attempting to show notifications, it might be because of a notification service falsely advertising its availability through the D-Bus service.

For instance, suppose a user recently installed a KDE component that requires , but the user is still running XFCE. In this case, the KDE notifier will be prioritized, but the user is not running it. The application will hang while waiting for the service, and only after a timeout will it fall back to .

The most noticeable hanging might come from the volume indicator scroll adjustment.

If you are in this situation, you should have two notification handlers:

Of those two, one fails regularly after a 1-minute timeout, as seen in the journal:

Choosing the service you want to use as described in #Multiple notification servers with D-Bus services will fix the problem.
