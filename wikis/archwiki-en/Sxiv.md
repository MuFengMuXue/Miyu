# Sxiv

sxiv, Simple X Image Viewer is a lightweight and scriptable image viewer written in C.

## Installation
Install one of the following packages:

* , a fork of the now-unmaintained sxiv with the purpose of being a (mostly) drop-in replacement for sxiv, maintaining its interface and adding simple, sensible features.
* , the original package. Unmaintained.

## Usage
## Assigning keyboard shortcuts
sxiv supports external key events. First you have to press  to send the next key to the external key-handler. The external key-handler requires an executable file  and passes the key combination pressed via argument as well the names of the currently marked images as stdin (or, if none are marked, the currently selected image). An example key-handler is shipped, when installing sxiv: . The example is a great start to customize shortcuts.

 $ mkdir -p ~/.config/sxiv/exec/
 $ cp /usr/share/sxiv/exec/key-handler ~/.config/sxiv/exec/key-handler

Be sure to mark the script as executable.

In the following example, we will add the bindings  to execute ,  to copy the current images' names to the clipboard with , and  to set the current wallpaper with nitrogen. Obviously, some commands may only make sense with a single image as an argument, so you may want to revise this to handle cases when those are passed more than one.

Create  folder if it does not exist:

 $ mkdir ~/.trash

## Tips and tricks
## Browse through images in directory after opening a single file
sxivs developer was requested a few times to make his program browse all images in a directory of the filename given as argument (see and [https://github.com/muennich/sxiv/issues/105). There are some forks that features the desired behaviour: doronbehar's, qsmodo's and sammoth's.

Alternatively, you can use the official version of  and place this script in  and call it like this:

 $ scriptname a_single_image.jpg

As indicated in the comments of the script, it may be used to have this behavior when opening images from within ranger.

This shell script from starts  in
thumbnail mode if and only if the passed file argument is a folder:

{{hc|~/bin/sxiv.sh|
#!/bin/sh

    if command -v sxiv >/dev/null 2>&1; then
      if [ -d "${@: -1}"  || [ -h "${@: -1}" ]; then
        sxiv -t "$@"
      else
        sxiv    "$@"
      fi
    elif command -v feh >/dev/null 2>&1; then
      feh "$@"
    else
      echo "Please install SXIV or FEH!"
    fi
}}

## Showing the image size in the status bar
Place the following executable script in  and make sure that you have the  package installed:

{{hc|~/.config/sxiv/exec/image-info|
#!/bin/sh

# Example for ~/.config/sxiv/exec/image-info
# Called by sxiv(1) whenever an image gets loaded,
# with the name of the image file as its first argument.
# The output is displayed in sxiv's status bar.

s=" | " # field separator

filename=$(basename "$1")
filesize=$(du -Hh "$1" | cut -f 1)

# The 'stands for the first frame of a multi-frame file, e.g. gif.
geometry=$(identify -format '%wx%h' "$1[0")

tags=$(exiv2 -q pr -pi "$1" | awk '$1~"Keywords" { printf("%s,", $4); }')
tags=${tags%,}

echo "${filesize}${s}${geometry}${tags:+$s}${tags}${s}${filename}"
}}
