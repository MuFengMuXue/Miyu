# Newsraft

Newsraft is a text-based feed reader inspired by Newsboat while seeking to be its lightweight alternative. It supports RSS 2.0 and lower, Atom 1.0, RSS Content Module, Media RSS, DublinCore 1.1 Elements, and JSON Feed.

## Installation
Install the  package.

## Configuration
Configuration of newsraft is optional, used only to change default settings or add functionality. This is accomplished via entries in , including reader and color settings, and key bindings for both built in actions  and shell commands , including options for opening links in designated programs. Multiple commands can be associated with a single binding by separating them with semicolons:

Default key bindings can be disabled if undesired or for repurposing with . Finally, like the feeds file, the # symbol designates comment lines and will be ignored by newsraft.

## Example configuration
A full listing of available actions, settings, and defaults is available in the  manual.

## Usage
Newsraft needs a feeds file created before it can be launched. The default feed file location and name is . Once this is populated with links to feeds, start newsraft with the command:

 $ newsraft

## Managing feeds
The feeds file can contain three types of lines. The first is the feed URL, which can be added with a text editor one feed per line:

Only the URL is strictly necessary. Newsraft will attempt to name the feed based on information provided by the feed. If an alternate name is desired, this can be supplied by adding the title in enclosed double quotes separated from the URL by at least one white space.

Section headers are the next type of line, which start with the @ symbol, at least one white space, and then the section name:

The final type of entry in the feeds file are comments, which start with the # symbol:

Both feed URLs and section headers can set auto update frequency, with individual feed frequencies overriding sectional frequencies. The period is specified by a number minutes enclosed by square brackets:

Specifying  will disable automatic updates and global feed updates can be specified by using the  section header. In the above example, all feeds under  are automatically updated every two hours, except feed2, which is updated every hour, and feed4, which is never automatically updated.

## Basic default commands
While all of these key bindings can be modified via newsraft's config file, here are the basic default key bindings and their commands:

{| class="wikitable"
! Command
! Description
|-
|
| move selection down to next menu item
|-
|
| move selection up to previous menu item
|-
|
| open selected menu item
|-
|
| close selected menu item, return to previous menu.  If currently in top menu, quit newsraft
|-
|
| mark selection read and move to next menu item
|-
|
| mark selection unread and move to next menu item
|-
|
| mark all menu items read
|-
|
| open selection in browser.  If no number precedes 'o', opens first selection
|-
|
| manually update selected feed
|-
|
| manually update all feeds
|}
