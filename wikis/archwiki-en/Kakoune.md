# Kakoune

Kakoune is a modal text editor. It is inspired by Vim and similar alternatives, but tries to improve the text editing workflow as well as fit better to the Unix philosophy. Besides modal editing, two other main concepts are selection based editing, and multi-cursor editing. It has an interactive help system, and supports many languages. Kakoune inspired editors like Helix.

## Installation
Install the  package.

## Usage
 opens the documentation of .

It has an interactive help system, which means e.g. pressing   shows a dialog with possible keys and destinations, or it displays a help dialog with the description of the highlighted completion candidate in  mode.

## Configuration
Kakoune reads configuration from .

The main configuration file is , and custom colorschemes can be stored in the  directory.

Every  file is loaded from  at startup. If this directory exists in , Kakoune does not load the system wide  dir (located at ), so it has to be linked there. For example:

 $ ln -s /usr/share/kak/autoload $XDG_CONFIG_HOME/kak/autoload/default
