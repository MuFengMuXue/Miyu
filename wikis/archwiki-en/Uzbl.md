# Uzbl

Uzbl is a lightweight browser based on uzbl-core. Uzbl adheres to the UNIX philosophy of "Write programs that do one thing and do it well". The uzbl-browser package includes uzbl-core, uzbl-browser and uzbl-event-manager. Most users will want to use uzbl-browser or uzbl-tabbed as they provide the fullest set of tools for browsing. Uzbl-browser allows for a single page per window (with as many windows as you want), while uzbl-tabbed provides a wrapper for uzbl-browser and implements basic tabs with multiple pages per window.

## Installation
Install the  or  package.

Thanks to , uzbl can make use of NPAPI plugins: installing  or  will enable their use in uzbl-browser and uzbl-tabbed.

## Commands
One of the biggest advantages of using Uzbl is that nearly everything can be controlled by the keyboard. This is preferable to the traditional mouse/keyboard combo because less moving around of the hands is needed. Vim users will find Uzbl much easier to pick-up, especially as the default bindings loosely resemble Vim keystrokes. For instance, following a link requires the user to type , and then the keystrokes in the box that appears next to each link on the page. Shortening the command to just  in the configuration file allows for even faster navigation.

Below are basic, default commands that can be used with uzbl-browser and uzbl-tabbed. These commands can all be found in  (which is usually located in ). The default settings work well, but many users like to edit them to suit their preferences and in fact, it is encouraged to change this file to suit your needs. More help with editing the configuration file can be found on the Uzbl readme.

## Navigation
{| class="wikitable"
! Command
! Doing what
|-
| o || enter url
|-
| O || edit url
|-
| b || back
|-
| m || forward
|-
| S || stop
|-
| r || reload
|-
| R || reload ignoring cache
|-
| fl || spawn numbers next to each hyperlink. Type the number after typing fl to follow the link.
|-
| gh || go home
|}

## Page Movement
{| class="wikitable"
! Command
! Doing what
|-
| j || scroll up
|-
| k || scroll down
|-
| h || scroll left
|-
| l || scroll right
|-
| PgUp || scroll page up
|-
| ctrl+b || scroll page up
|-
| PgDn || scroll page down
|-
| ctrl+f || scroll page down
|-
| Home || vertical beginning of the page
|-
| > || vertical end of the page
|-
| Space || vertical end of the page
|-
| ^ || horizontal beginning of the page
|-
| $ || horizontal end of the page
|-
| / || find in page
|-
| ? || find backwards in page
|-
| n || repeat find forward
|-
| N || repeat find backwards
|}

## Zooming
{| class="wikitable"
! Command
! Doing what
|-
| + || zoom_in
|-
| - || zoom_out
|-
| T || toggle_zoom_type
|-
| 1 || set zoom_level = 1
|-
| 2 || set zoom_level = 2
|}

## Searching
{| class="wikitable"
! Command
! Doing what
|-
| ddg || search term in DuckDuckGo
|-
| gg || search term in Google
|-
| \wiki || search term in Wikipedia
|}

## Inserting Text
{| class="wikitable"
! Command
! Doing what
|-
| i || toggle_insert_mode   (Esc works to go back to command mode much like vim)
|-
| fi || go to the first input field and enter insert mode
|}

## Bookmarks and History
{| class="wikitable"
! Command
! Doing what
|-
| M || insert bookmark (bookmarks are saved in ~/.local/share/uzbl/bookmarks
|-
| U || load url from history via dmenu
|-
| u || load url from bookmarks via dmenu
|}

## Tabs (when using uzbl-tabbed)
{| class="wikitable"
! Command
! Doing what
|-
| go || load uri in new tab
|-
| gt || go to next tab
|-
| gT || go to previous tab
|-
| gn || open new tab
|-
| gi+n || goto 'n' tab
|-
| gC || close current tab
|}

## Other
{| class="wikitable"
! Command
! Doing what
|-
| t || show/hide status bar
|-
| w || open new window
|-
| ZZ || exit
|-
| : || enter command
|-
| Esc || back to normal mode
|-
| ctrl+[ || back to normal mode
|}

## Tips and tricks
## Caching
Due to its lightweight nature, uzbl does NOT contain caching functionality. You can install Squid to speed up page loading.

## Troubleshooting
## Parcellite
Parcellite can cause problems at the time of selecting text under uzbl - just disable it.

## TLS certificates
Per https://bbs.archlinux.org/viewtopic.php?id=185014, adjust the configuration file:
