# Rxvt-unicode/Tips and tricks

## Improved Kuake-like behavior in Openbox
This was originally posted on the forum by Xyne and it relies on the  package.

## Scriptlets
Save this scriptlet from the  man page somewhere on your system as  (e.g., in ):

and save this one as :

Make both files executable.

Make sure that you change  to the actual path to the  scriptlet that you saved above. We will be using  to launch both regular instances of  and the kuake-like instance.

## urxvtq with tabbing
To activate tab support, you can either replace the fifth line of your :

 /path/to/urxvtc -name urxvtq -geometry 80x28

with:

 /path/to/urxvtc -name urxvtq -pe tabbed -geometry 80x28

or replace this line of your  file:

 URxvt.perl-ext-common: default,matcher

with

 URxvt.perl-ext-common: default,matcher,tabbed

## Tab control
{| class="wikitable"
! Key !! Description
|-
| Shift+Left || Switch to the tab left of the current one
|-
| Shift+Right || Switch to the tab right of the current one
|-
| Shift+Down || Create a new tab
|}

You can also use your mouse to switch the tabs by clicking the wished one and create a new tab by clicking on .

To close a tab just enter  like you would to normally close a terminal.

## Openbox configuration
Now add the following lines to the  section of :

and add these lines to the  section:

Here too you need to change the  lines to point to the scripts that you saved above. Save the file and then reconfigure Openbox. You should now be able to launch regular instances of urxvt with , and toggle the kuake-like console with  (the grave key also known as the backtick).

## Further configuration
The advantage of this configuration over the urxvt kuake Perl script is that Openbox provides more keybinding options such as modifier keys. The kuake script hijacks an entire physical key regardless of any modifier combination. Review the [https://openbox.org/help/Bindings Openbox bindings documentation for the full range or possibilities.

The Openbox per-app settings can be used to further configure the behavior of the kuake-like console (e.g. screen position, layer, etc.). You may need to change the "geometry" parameter in the  scriptlet to adjust the height of the console.

## Related scripts
* hbekel has posted a generalized version of the  here which can be used to toggle any application using .
* http://www.jukie.net/~bart/blog/20070503013555 - A script for opening URLs with your keyboard instead of mouse with urxvt.

## Improving performance
* Avoid the use of Xft fonts. If Xft fonts must be used, append  to the setting value.* Build rxvt-unicode with disabled support for unnecessary features,  and  in particular.[http://pod.tst.eu/http://cvs.schmorp.de/rxvt-unicode/doc/rxvt.7.pod#Rxvt_unicode_uses_gobs_of_memory_how
* Limit the number of  (option ) in the scrollback buffer to reduce memory usage. ** Use tmux for scrollback buffer and set saveLines to 0
* Disable perl
* Consider running  as a daemon accepting connections from  clients.

## Daemon-client
## Xinitrc
See the Examples section in . This is the preferred option.

## systemd
System service:

Pass the username when starting the service:

 urxvtd@username.service

For a systemd/User service, place the following unit files in :

## Advanced tab management
Install the  package, then add the  value to the  X resource in your :

 URxvt.perl-ext-common: ...,tabbedex,...

By default, the "[NEW" button (which is rarely used and usable only with the mouse) is disabled with tabbedex. You can reenable this feature by setting the  to true.

 URxvt.tabbedex.new-button: true

Tabs can be named with  ( to confirm,  to cancel).

The tabs bar is hidden when only one tab is present. If you want to always show the tabs bar:

 URxvt.tabbedex.autohide: false

To prevent the last tab from closing Urxvt, enable the following resource:

 URxvt.tabbedex.reopen-on-close: yes

To start a new tab or cycle through tabs, use the following user commands: . Example of mappings:

 URxvt.keysym.Control-t: perl:tabbedex:new_tab
 URxvt.keysym.Control-Tab: perl:tabbedex:next_tab
 URxvt.keysym.Control-Shift-Tab: perl:tabbedex:prev_tab

To define your own key bindings to rename a tab or move a tab to the right or to the left, use the following commands:  and . Example of mappings:

 URxvt.keysym.Control-Shift-Left: perl:tabbedex:move_tab_left
 URxvt.keysym.Control-Shift-Right: perl:tabbedex:move_tab_right
 URxvt.keysym.Control-Shift-R: perl:tabbedex:rename_tab

## Transparency
## True transparency
To use true transparency, you need to be using a window manager that supports compositing or a separate compositor.

From the command-line:

 $ urxvt -depth 32 -bg rgba:3f00/3f00/3f00/dddd

Using the configuration file:

or

where '95' is the opacity level in percentage and '#000000' is the background color.

To use a color i.e. #302351 with the rgba:rrrr/gggg/bbbb/aaaa syntax it would be rgba:3000/2300/5100/ee00. "ee00" (the alpha value) to make it nicely transparent.

## Native transparency
If there is no need for true transparency, or if compositing uses too many resources on your system, you can get transparency working in the following way:

Using the URxvt*background setting exemplified above instead of URxvt*shading will also work.

## Set icon
By default URxvt does not feature a taskbar icon. However, this can be easily changed by adding the following line to  and pointing to the desired icon:

 URxvt.iconFile:    /usr/share/icons/Clarity/scalable/apps/terminal.svg

## Use urxvt as application launcher
urxvt can be used as a lightweight alternative to application launchers such as . Run urxvt with the following configuration to imitate look and behaviour of an application launcher or assign the command to a custom alias:

 $ urxvt -geometry 80x3 -name 'bashrun' -e sh -c "/bin/bash -i -t"

## Xterm escape sequences
It is possible for rxvt-unicode to mimic the Xterm escape sequences. These can be found for arbitrary key combinations by running  inside xterm, then bound in urxvt using keysyms.

Take this word by word movement binding as an example:

For more information, see  and the keysym section of the  man page.

## Bidirectional support
It is possible to add bidirectional support for languages like Hebrew, Farsi or Arabic using the bidi extension.

## Bell Command
It is possible to execute a shell command when the terminal rings the bell. The pre-packed  extension needs to be enabled first in the  file:

  URxvt.perl-ext-common: ...,bell-command,...

The following example will use ALSA's  command to play a  file:

  URxvt.bell-command: aplay /path/to/a/file.wav

The following example will use libcanberra's  command to play the bell sound of your current sound theme:

  URxvt.bell-command: canberra-gtk-play -i bell

And the next setting will pop a visual notification:

  URxvt.bell-command: notify-send "rxvt-unicode: bell!"

## Xterm-like colors
urxvt uses the same colors as Xterm, except one. Add  to  to change this.

## Launch rxvt-unicode with current working directory of another window
There are three possibilities to launch rxvt-unicode "from here": some sort of shell script, Perl extension, and xcwd.

## xcwd
Install  or , see the README for more information.

i3 sample setup:
