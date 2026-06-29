# Qutebrowser

qutebrowser is a keyboard-focused web browser written in Python and Qt. It uses the chromium web engine.

## Installation
Install the  package.

## Basic usage
Use  to access the command prompt. You can use  to auto-complete.

On first usage of qutebrowser, a Quickstart page appears. It is later accessible via . See the cheatsheet for keyboard shortcuts.

## User configuration
Qutebrowser can be configured via the UI, the command-line or a Python script. See upstream configuration guide.

Configuration done through the UI will automatically be stored in  (don't edit it manually). For manual configuration, user can write a . Both files are located in  or fallback .

## Configuration in qutebrowser
To set a single configuration item, you can simply type  followed by the name of the configuration item and the new value that you would like to set. For example, you could type

 :set auto_save.session true

to open your previous tabs when you reopen qutebrowser.

To open qutebrowser's UI settings page, type

 :set

without further arguments. There, you can edit the different settings in the UI. When you are finished, type  again to store your configuration.

For example, under  you can configure your search engines which are stored as a list of key-value pairs. When you have not changed this setting yet, this should look something like

 {"DEFAULT": "https://duckduckgo.com/?q={}"}

This configures DuckDuckGo as your default search engine while the placeholder {{ic|{}}} will be replaced by your search term. To add a shortcut for quickly searching the Arch Linux wiki, you could use

 {"DEFAULT": "https://duckduckgo.com/?q={}", "wa": "https://wiki.archlinux.org/?search={}"}

Then, as described by the comment in the qutebrowser UI, you can search the Arch Linux wiki by typing . Notice that the arguments required to perform a search vary across search engines. For example, to set up Google, use {{ic|https://www.google.com/search?hl=en&q={}}}. Or to set up Brave Search, use {{ic|https://search.brave.com/search?q={}}}.

If Tor is installed and running on your system and you wish to use DuckDuckGo onion page instead, the setting should be something like

 {"DEFAULT": "https://duckduckgogg42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczad.onion/?q={}", "wa": "https://wiki.archlinux.org/?search={}"}

## Keybindings
You can edit the keybindings directly from the browser with the command  or you can edit them directly from the file. Notice that there are many, many keybinds already in place. If you notice a lag on one of your keybind it is because some other keybind is also starting with the same key.

See the documentation for examples.

## Video playback
You can add an option in your  to open a video in mpv, in the following example pressing  will bring up all the available video links on the page, then simply press the corresponding key combination for the video link you require and it will open it up in mpv:

{{hc|config.py|
...
config.bind('', 'hint links spawn --detach mpv {hint-url}')
...
}}

## Tips and tricks
## Importing quickmarks/bookmarks
Qutebrowser supports importing bookmarks from several formats via the python script . The default output format is qutebrowser's quickmarks format. For a short explanation of the differences between bookmarks and quickmarks see the qutebrowser FAQ.

## From Chromium/Chrome
Run the script mentioned above specifying  as the first argument and the directory containing the bookmarks file as the second argument. For Chromium this is  and  for Chrome. The output of the script can be appended to . Some of the input formats are explained below. Additional information can be found by supplying the  flag to .

 $ python /usr/share/qutebrowser/scripts/importer.py chromium ~/.config/chromium/Default >> ~/.config/qutebrowser/quickmarks

## From Firefox
Export Firefox bookmarks to an an HTML file (see Then, use the script to import.

 $ python /usr/share/qutebrowser/scripts/importer.py bookmarks.html >> ~/.config/qutebrowser/quickmarks

## From bookmarks.html file
The import from a  file requires the package . To import you just supply your  file to  and append the output to .

 $ python /usr/share/qutebrowser/scripts/importer.py ~/.config/chromium/Default >> ~/.config/qutebrowser/quickmarks

## Import as bookmarks instead of quickmarks
You can use any of the above mentioned methods and supply an additional  flag to change the output format of the script to bookmarks. The output should then be appended to .

 $ python /usr/share/qutebrowser/scripts/importer.py -b chromium ~/.config/chromium/Default >> ~/.config/qutebrowser/bookmarks/urls

Note that the flag must be added before the browser specification.

## Automatically enter login information
You can use the [https://github.com/qutebrowser/qutebrowser/blob/master/misc/userscripts/qute-pass qute-pass userscript to automatically enter login information stored in your Pass password-store. You will need a dmenu-compatible application launcher and . Set up a keybinding which executes .

To quote from the script's description:
 The domain of the site has to appear as a segment in the pass path, for example: "github.com/cryzed" or "websites/github.com". How the username and password are determined is freely configurable using the CLI arguments. The login information is inserted by emulating key events using qutebrowser's fake-key command in this manner: which is compatible with almost all login forms.

To further clarify, the pass-structure that is used by default should look something like this:

This means is that each website is a directory in your ~/.password-store folder. Within each website-named directory is where the files are titled username.gpg, username2.pgp, etc. and each file  contains the password associated with each username for the website.  For those of you migrating from Firefox, a [https://github.com/johnabs/firefox_decrypt modified version of firefox_decrypt should migrate things in this format.

The userscript provides many options to accomodate most workflows and special circumstances (such as only wanting to insert the password or the regular method of inserting the username and password not working).

## Turn on spell checking
First, download the appropriate dictionary using the  script that comes bundled with qutebrowser.

For example, for English (US):

 $ /usr/share/qutebrowser/scripts/dictcli.py install en-US

The script has other features too, which can be shown by using .

Then set the following in qutebrowser:

 :set spellcheck.languages === Minimize fingerprinting ===

Websites may be able to identify you based on combining information on screen size, user-agent, HTTP_ACCEPT headers, and more. See [https://panopticlick.eff.org/ for more information and to test the uniqueness of your browser. Below are a few steps that can be taken to make your qutebrowser installation more "generic".

Additionally see Firefox/Privacy#Configuration for more ideas.

## Set a common user-agent
Several user agents are available as options when using . Another, possibly more generic user-agent is:

 Mozilla/5.0 (Windows NT 10.0; rv:68.0) Gecko/20100101 Firefox/68.0

## Set a common HTTP_ACCEPT header
The following is a common HTTP_ACCEPT header (Firefox default). Simply type the following commands at the prompt

 set content.headers.accept_language en-US,en;q=0.5
 set content.headers.custom '{"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"}'

## Disable reading from canvas
 set content.canvas_reading false

## Disable WebGL
Set  to  to disable WebGL.

## Disable websites
Create  and enter websites you want to block in each line;  for example. This will keep the built-in adblock list while adding the websites in. Restart qutebrowser, and run .

## Enable Brave browser adblocker
Install the  package and enable the adblocker within qutebrowser:

 :set content.blocking.method both

## Open some links in mpv
To open some specific links in mpv (like YouTube, reddit, etc) instead of loading the webpage. This can be used to bypass ads, tracking, etc. You can of course replace mpv by the video player of your choice.

 :bind M hint links spawn mpv {hint-url}

## Enable darktheme everywhere
 :set colors.webpage.darkmode.enabled true

## Disable javascript
 :set content.javascript.enabled false

## Route the traffic through tor
This requires Tor to be enabled and running. Note this is only using the tor proxy but does not provide you any protection from fingerprinting you might have on tor browser.

 :set content.proxy socks://localhost:9050/

## Change the context menu theme
To change the context menu theme, find the relevant section of your  and set the appropriate settings. For example:

## Integrate with KeePassXC
Qutebrowser ships with qute-keepassxc for integration with KeePassXC.

To integrate with KeePassXC:

# Enable KeepassXC-Browser extensions in your KeepassXC config.From KeePassXC go to Tools->Settings->Browser Integration, and check "Enable browser integration".
# Make sure to have a working private-public-key-pair in your GPG keyring.Find your secret keys with . The key must be trusted, e.g. it should contain "in the "uid" field.If it is not trusted, you can trust it with , then ,  (ultimate trust) and confirm.Finally, copy the key id.
# Install the package
# Adapt your qutebrowser config.You can e.g. add the following lines to your . Remember to replace `ABC1234` with your actual GPG key id.

To manage multiple accounts you also need rofi installed.

## Troubleshooting
## Unreadable tooltips
Depending on your Qt theme, tooltips might be hard to read. In order to fix this, create a Qt Style Sheet file. For example:
{{hc|head=~/.local/share/qutebrowser/fix-tooltips.qss|output=
QToolTip {
	background-color: palette(highlight);
	border: 2px solid palette(highlight);
	color: palette(text);
}}}

Then load the style sheet when launching qutebrowser:

 qutebrowser --qt-arg stylesheet ~/.local/share/qutebrowser/fix-tooltips.qss

See the [https://github.com/qutebrowser/qutebrowser/issues/4520 bug report for details.

The bug report offers another method using  that does not require arguments at launch:

# In qutebrowser,
# In , set style: gtk2, standard dialogs: gtk2, palette: default
# Change to Style Sheets tab, and create a new file (I called it  but it should not matter)
# Put the following contents inside: {{bc|QToolTip{
	background: QLinearGradient(x1: 0, y1: 0, x2: 0, y2: 0, stop: 0 palette(window), stop: 1 palette(alternate-window));
	border-radius: 3px;
	border: 1px solid #000000;
	padding: 1px;
	color: palette(text);
}}}
# Click Save then Ok
# Make sure to check the box next to this new file so that it will be applied to the theme
# Click Apply
