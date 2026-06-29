# ELinks

ELinks is an advanced and well-established feature-rich text mode web (HTTP/FTP/...) browser. ELinks can render both frames and tables, is highly customizable and can be extended via Lua or Guile scripts. It features tabs and some support for CSS.

## Installation
Install the  package.

## Usage
See .

## Navigation
Navigating the web with a text browser is more or less the same as a graphical browser, just without the 'distractions'. Once you have started elinks, you can press  and type in the web page you would like to request. Then you can navigate the page using arrow keys to navigate by line, the space bar to navigate by page, or the  and  keys to navigate by link.

## Configuration
ELinks provides to two menus, accessible through ELinks, to customize options and keybinds respectively.

It is recommended to use these tools as opposed to hand-editing the configuration files (which are placed in ). It is both much easier and safer this way.

By default, the  key opens the option manager and the  key the keybind-manager.

## Tips and tricks
## JavaScript (sort of) support
ELinks has an experimental feature called ECMAScript which is a form of JavaScript. Currently, the repo package does not build with this, but a simple modification to the PKGBUILD can provide it.

# Add  and something that provides xxd such as  to the depends array.
# Add the following to the arch-meson bit in the package function: -D spidermonkey=true \
#

Once built, it must be enabled in elinks either by navigating to the options section or directly modifying  to contain:
set ecmascript.enable = 1

ECMAScript is not perfect and may not provide full JavaScript functionality.

## Defining URL-handlers
ELinks is capable of using external programs for various tasks,

Defining URL-handlers through the option menu can be a little confusing at first, but once you get it, it is fine.

To do this, go into the option manager and navigate to MIME. All the submenus have Info pages to help you.

This is one of the few cases where it might be easier just to edit the configuration file.

For example, to get ELinks to automatically launch your image-viewer when you click on a JPEG file, you can add the following to your  file,

## Tor usage
ELinks does not support using a SOCKS proxy directly. Alternatives are to either invoke ELinks through , or install the privoxy package for forwarding to Tor's SOCKS proxy, first by adding the following line to your :

 forward-socks5 / localhost:9050 .

Restart , then enter the following lines to your :

 set protocol.http.proxy.host = "127.0.0.1:8118"
 set protocol.https.proxy.host = "127.0.0.1:8118"

## Passing URL's to external commands
You can define commands which ELinks will pass the current URL to.

To do this, go into the options menu, navigate under Document, then to URI-passing. Then press  to add a new command name. Then navigate to the new command name and press  to edit. Type in the name of command, enter and save.

Assuming the command "tab-external-command" is mapped to KEY, whenever you press KEY, a menu containing your commands will appear. Select the one you want, and ELinks passes the current URL to that command.

## Saving link to the X clipboard
 echo -n %c | xclip -i

## Passing YouTube-links through external player
For strictly YouTube-links,  has built-in support. Just use the following:

 mpv %c

For a more general approach that can handle many 'tube' sites, you will need . Then add the following command,

 youtube-dl -o - %c | mplayer -

## Troubleshooting
## ELinks froze and I cannot start it without it freezing again
By default, every time you start ELinks you are connecting to an existing instance. Thus, if that instance freezes, all current and future instances will freeze as well.

You can prevent ELinks from connecting to an existing instance by starting it like so:

 $ elinks -no-connect

If this happens a lot, you might consider making this your default startup by making an alias in your shell:

 alias elinks="elinks -no-connect"
