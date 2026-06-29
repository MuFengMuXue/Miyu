# W3m

w3m is a text-based web browser as well as a pager like more or less. With w3m you can browse web pages through a Terminal emulator window. Moreover, w3m can be used as a text formatting tool which typesets HTML into plain text.

## Installation
Install the  package.

## Usage
See .

## Configuration
w3m can either be configured using the in-browser settings menu or by directly modifying its configuration files.

Some of the more advanced options are not available using the settings menu, so it is recommended editing the configuration files themselves.

By default all configuration files reside in .

/etc/w3m/config isn't exposed so o (= Option Setting Panel), tab until in an unselected setting (eg a ( )YES), Enter to select that, tab down to an and Enter on that to leave the panel. You will now have ~/.w3m/config.

## Tips and tricks
## Vim keybinds
Replace  with a [https://gist.githubusercontent.com/Lovebird-Connoisseur/a11b9dbc5c056d705d1f0e1053de35af/raw/92b30d2ca4cf67b5816146f86f5d920b4bdfc492/keymap custom configuration.

## URL hints
w3m supports qutebrowser-like link navigation, simply navigate to your config file and change the following line from  to .

And add  and  to .

## Using kitty image protocol
Users of the kitty terminal emulator may chose to use its own graphics protocol.

To do so simply change the following line in :

 inline_img_protocol 0

to:

 inline_img_protocol 4

## Using Iterm2 image protocol
Users of the wezterm terminal emulator may chose to use the Iterm2 graphics protocol which WezTerm supports.

To do so simply change the following line in :

 inline_img_protocol 0

to:

 inline_img_protocol 3

## Searching
You can set  to 1, to allow searches to jump to the top after they have hit the bottom of all matches within a page.

You can set  to 1 to enable case insensitive searching.

## Custom search engines
You can map keys to launch a CGI script that will capture your input and pass it onto a custom search engine, to do so first create a keybind inside  to launch your script:

 keymap s COMMAND "SET_OPTION dictcommand=file:///cgi-bin/omnibar_google.cgi ; DICT_WORD"

And place omnibar_google.cgi inside your  directory and giving it execute permission.

While the above script will return a Google result, you can use these kinds of scripts to search StackOverflow, GitHub, DuckDuckGo, Reddit and a bunch of other websites.

You can view similar scripts on GitHub.

## Reader mode
Some webpages do not work well with w3m, be it because they use a lot of javascript or CSS to display most of their content. Very often you will have to scroll multiple pages just to get to the start of an article.

This can be mitigated by first passing the webpages through a reader mode program such as .

To do so add the following to :

 keymap R COMMAND "READ_SHELL 'rdrview $W3M_URL -H 2> /dev/null 1> /tmp/readable.html' ; LOAD /tmp/readable.html"

## Redirect URLs
 file is used to set some preferences depending on the website, such as: referrer and user agent.

It can also be used to redirect to lighter (both in terms of layout and bandwidth), more privacy respecting alternatives to websites.

In addition to this it can also be used to run certain CGI scripts.

## Restore closed windows
Default w3m cannot reopen closed tabs, this can be added by binding the close tab button to echo the current URL of the tab to be closed to a text file, and binding another key to restore the latest URL added to the file, using a CGI script.

Inside  add:

 keymap d COMMAND "EXTERN 'echo %s >> ~/.w3m/RestoreTab.txt' ; CLOSE_TAB"
 keymap u COMMAND TAB_GOTO file:/cgi-bin/restore_tab.cgi

Then place the following file inside  and make it executable.

restore_tab.cgi

## Opening magnet links
magnet.cgi can be used to make w3m auto open magnet links using Transmission.

## Fingerprinting
## Using tor
You can use  to route w3m traffic through .

 $ torify w3m -v

## User agent and headers
By default w3m uses its own user agent, meaning w3m users stand out amongst other users.

Fingerprint can be reduced by using a more generic user agent, language and http_accept header.

## Disable cookies
To disable cookies set  to 0 in .

## Disable cache
To disable cache set  to 1 in .

## Troubleshooting
## Images flickering/causing lag
Unfortunately, sometimes w3m lags when trying to scroll past an image, to the point where the browser can become unresponsive for multiple seconds.

A solution to this is outright disabling images, but this breaks some websites (for example, hacker news relies on GIFs for comment indentation).

A more elegant solution would be to make a keybind to toggle images on or off, to do so add the following line to :

 keymap i COMMAND "SET_OPTION display_image=toggle ; RESHAPE"
