# Llpp

llpp is a lightweight, fast and featureful PDF, EPUB, XPS and CBZ viewer based on MuPDF.

## Installation
Install the  package.

## Usage
llpp uses keyboard shortcuts and the mouse to navigate through a document.  By default, pressing  or  will bring up a help page where all other key bindings are described.

Check out the following page for the full help text.

## Configuration
llpp uses a configuration file to store settings:  or . This file stores the following:

# Application defaults.
# File-by-file user preferences (e.g. the last page viewed).

## Per-document options
Pressing  will enter information mode, where you can examine and modify display settings for the current document.

Alternately, pressing  (where  is one of the tunable options shown in the help screen) allows you to set a single setting directly.

## UI Font
One can set the font used by llpp by indicating the size and filename in the configuration. For example:

   ...

## Custom key bindings
It is possible to configure key bindings. For example, to disable  exiting llpp, add the  element in between the  tags as follows:

More examples can be found in llpps example file keys.txt. For vi-like key bindings, see this example.

## Save annotations to PDF
You can annotate a PDF file by right clicking while holding . To allow saving of annotations, add

 savepath-command='echo %s'

to your . After annotating the file, save the changes by pressing . This s the current PDF file path to the  option.

## Opening links in web browser
By default, llpp will not open links in the default browser. The  option in  is responsible for handling this action. To open links in your default web browser, set it to:

 uri-launcher='xdg-open "%s"'

## Tips and tricks
## Reload file
A document can be reloaded in three ways:

* Pressing the  key
* Sending a HUP signal to the llpp process

 $ killall -SIGHUP llpp

* Using the "remote" interface (see below)

## Multiple columns
For side-by-side 2-page viewing, press  (or set  to  in info mode).

If the page offset is wrong (left-hand page showing on the right-hand side), set columns to .

A unique feature of llpp is being able to split a single page down the middle by setting columns to . Use  to split a 3-column document.

## Remote interface
The following commands will setup the remote interface and use it to reload the file "image.pdf".

 $ mkfifo /tmp/llpp.remote
 $ llpp -remote /tmp/llpp.remote image.pdf & disown
 $ sleep 1
 $ echo reload >/tmp/llpp.remote

There are eight remote commands:

*  - reload
*  - quit
*  - goto
*  - goto
*  - goto other document
*  - goto named destination within the other document
*  - draw a rectangle
*  - raise and switch to llpp's window

## Inverse search using Synctex and Vim/Emacs
To use the synctex capability of llpp, add the line below to your  under the  tag:

     ...

where  is the script below

 #!/bin/bash
 pdf_file=$1
 page=$(($2 + 1)) # The page number star at zero in llpp
 x=$3
 y=$4

 # for vim
 synctex edit -o "$page:$x:$y:$pdf_file" \
        -x "gvim --servername synctex --remote-wait-silent +%{line} '%{input}'"

 # for emacs
 # synctex edit -o "$page:$x:$y:$pdf_file" -x "emacsclient +%{line} '%{input}'"

Make sure  is an executable script and add it to your  environment variable. To use the  command you will need  package from the official Arch repositories.
