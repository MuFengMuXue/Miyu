# WeeChat

WeeChat is a highly extendable and feature rich IRC client.

## Installation
Install the  package.

## Usage
WeeChat provides two executables:

* , the curses interface;
* , the headless version.

Read the quick start guide. For details consult the user's guide.

## Configuration
By default WeeChat stores its configuration files in XDG directories. Editing these files directly is not recommended because WeeChat may write them at any time.Instead you should use the [https://weechat.org/files/doc/devel/weechat_user.en.html#command_weechat_set /set command. You can get a list of all configurable options by running  in the WeeChat buffer window. Since there are nearly 600 default configurable options, you can search through them with a wildcard syntax:  or  as an example. You can get help on each option with the  command:

 /help irc.server.libera.autoconnect

## Connecting to a server
You can connect to a IRC server by adding it and then using :

 /server add libera irc.libera.chat/6697
 /connect libera

See the WeeChat documentation and  for more information.

## Configuring TLS
Many IRC servers, including Libera.Chat where the Arch IRC channels are, support TLS.

If you are making a server with , add the TLS port (usually 6697) and  to the end of the line. For example:

 /server add libera irc.libera.chat/6697 -tls

## Tips and tricks
## Upgrading
WeeChat can be upgraded without disconnecting from the IRC servers (plaintext connections only):

 /upgrade

This will load the new WeeChat binary and reload the current configuration.

## Aliases
Aliases can be created to simplify commonly executed commands. A nice example is Wraithan's smart filter alias:

First, we need to enable smart filters:

 /set irc.look.smart_filter "on"

Next, we will create the "sfilter" alias:

 /alias add sfilter filter add irc_smart_$server_$channel irc.$server.$channel irc_smart_filter *

We can now type

 /sfilter

in any buffer, and the smart filter will only be enabled for that buffer.

The following alias will remove a previously enabled smart filter in the current buffer. Add the alias:

 /alias add rmsfilter filter del irc_smart_$server_$channel

and execute it by

 /rmsfilter

## Exec command
A plugin called "exec" is available, with the command . It will execute external command and can display output to the current buffer with the  option or locally (default).

## Key bindings
See .

Example that adds basic irssi style window scrolling:

 /key bind meta-p /window page_up
 /key bind meta-n /window page_down

If you are using vimode plugin, most of the default bindings will not work will have vim like alternatives. Check bindings

## SSH connection lost when idle
If you are connecting to your WeeChat through a remote shell using SSH, for example running it in GNU Screen or tmux you might experience getting disconnected after a while when idle. There are multiple factors in play why this might happen, but the easiest way to change this is to force the connection to be kept alive by appending this to your SSH-configuration on the remote shell.

This has nothing to do with WeeChat itself, but losing connection when idle will not happen with its alternative irssi by default, and thus is a common situation for those converting to WeeChat.

Or have a look at Mosh.

## Emojis
Emojis are part of Unicode set. Requirements for emojis:

* terminal emulator must support Unicode and emojis subset.
* font used in terminal emulator must support emojis subset.

Incomplete list of terminals with emojis support:

* alacritty
* foot
* kitty
* rxvt-unicode
*

## Mouse support
A terminal emulator will pass through mouse scroll events and weechat will scroll-in areas

* chat area
* nicklist bar

## Mouse in tmux
When running in tmux turn on mouse support in :

 set -g mouse on

## Matrix
The  script allows you to connect to Matrix servers. Install it, then:

# run  inside Weechat,
# configure weechat-matrix, and
# use the  command inside a Matrix buffer to join Matrix channels, e.g. .

To load the script automatically during WeeChat startup, run:

 $ mkdir -p ~/.local/share/weechat/python/autoload
 $ ln -s /usr/share/weechat/python/weechat-matrix.py -t ~/.local/share/weechat/python/autoload

## Slack
There is a native client for slack: wee-slack

## Desktop notifications
To receive desktop notifications for mentions or private messages, the  script by Petr Zemek can be installed.

The script uses libnotify and is known to work with both KDE and Gnome.

Another alternative with the built-in  plugin is to set a value for .

 /set trigger.trigger.beep.command "/print -beep;/exec -bg notify-send -i '/usr/share/icons/hicolor/32x32/apps/weechat.png' 'IRC Notification' "${tg_tag_nick}: ${tg_message_nocolor}""

## Mobile device notifications
To receive notifications for mentions or private messages to an Android mobile device, you can use the IrssiNotifier port to WeeChat from the official website. This script requires a Google Account, and a registration step with the service provider to obtain an API key. Then, install the plugin

 $ cd ~/.local/share/weechat/python
 $ curl -O https://www.weechat.org/files/scripts/irssinotifier.py
 $ ln -s ../irssinotifier.py autoload/

and intialize the API token and end-to-end encryption password in WeeChat

 /set plugins.var.python.irssinotifier.api_token your-api-token-from-website
 /set plugins.var.python.irssinotifier.encryption_password your-password-same-as-in-android-app
 /save

An alternative that does not require a Google Account is a Ruby script for NotifyMyAndroid.com from GitHub, with a similar installation procedure to the above, but into .

## WeeChat relay with a systemd user service
To use your WeeChat instance as a WeeChat relay for other WeeChat clients (not to be confused with the IRC relay feature) you can use the WeeChat relay plugin and either a systemd user service, if you only want headless operation, or a combination of a systemd user service and tmux to maintain full command line functionality.

Either method involves creating a service file in the directory

## tmux method
Due to the incompatibilities between how systemd manages jobs and the client-server behavior of tmux you will want to use the  option to separate your default tmux sessions from the WeeChat one being managed by systemd. If this is the first tmux session started using the default socket then stopping and restarting the WeeChat user service will kill all the sessions connected to the default tmux socket. If the WeeChat tmux session is started after another default tmux session then the WeeChat session will die once systemd moves onto the next service unit. Sequestering the WeeChat tmux server to its own socket forces the expected behaviors when invoking systemctl. This does however mean that you will not see the WeeChat session when using tmux without using  to select the correct socket.

Once the service is in place, all you need to do is start/enable the user unit and run .

From there you can connect to the tmux session in order to configure the weechat relay plugin:

 $ tmux -L weechat attach

From there you can configure the WeeChat relay plugin with the desired settings on the console: https://www.weechat.org/files/doc/stable/weechat_user.en.html#relay

If you want to hide tmux status bar, you can append this option to :
 \; set-option status off

For displaying 256 colors with the session it may be needed to append this to tmux configuration file:
 set -g default-terminal tmux-256color

## Headless method
A key difference with this method is that you will either need to start WeeChat normally, configure the relay plugin, stop WeeChat, and then start the service or edit your  file manually while WeeChat is not running and then start your service. Either way you will need to configure your relay settings before starting your systemd WeeChat service: https://www.weechat.org/files/doc/stable/weechat_user.en.html#relay.

Once the service is in place, all you need to do is start/enable the user unit and run .

Note that we do not need an  defined because systemd will automatically track the PID and send the appropriate shutdown signal to the daemon.

Once the user unit is in place, enable it. When you are ready to start your headless relay, start the user unit.

## Troubleshooting
## Errors loading plugins
You may see output like the following in the main window after starting weechat:

The default configuration for weechat attempts to load all plugins found in  which in this case includes ruby, lua, aspell and tcl. These packages are not required by the weechat package and may not be installed on your machine. There are two options if these errors bother you:

# Install , ,  and/or .
# Or, run  which will prevent loading those plugins with a bang (!) prefix.

## Problem loading multiline.pl
This problem happens with  version >= 5.31.1

The script  depends on the  module. However, since  version v5.31.1  has been removed.

To fix the problem, install .

## Guides
* Official WeeChat quick start guide - a good place to start
* FiXato's guide to WeeChat - A Weechat Contributers Guide
* My always up-to-date WeeChat configuration - r3m (weechat-dev)
