# ImageMagick

According to Wikipedia:

:ImageMagick is a free and open-source software suite for displaying, converting, and editing raster image and vector image files. It can read and write over 200 image file formats.

## Installation
Install the  package. Alternatively install  for GraphicsMagick, a fork of ImageMagick, emphasizing stability of the API and command-line interface.

## Usage
See , or  for GraphicsMagick.

## Common operations
## Convert between image formats
The basic usage of this facility is to specify the existing, and desired, image formats as the filename extension. For example, to get the .jpg representation of a given .png image, use:

 $ magick image.png image.jpg

## Append
Combining multiple pictures into one:

 $ magick -append input.pngs output.png

## Crop, chop
To crop part of multiple images and convert them to another format:

 $ mogrify -crop WIDTHxHEIGHT+X+Y -format jpg *.png

Where WIDTH and HEIGHT is the cropped output image size, and X and Y is the offset from the input image size.

One can also  to cut of a single edge from an image, using gravity to select that edge. Which is easier as less numbers, or trial and error, is involved.

 $ magick frame_red.gif -gravity South -chop 0x10 chop_bottom.gif

## Limit the storage size
To achieve reasonable quality for a given storage size:

 $ magick image.jpg -define jpeg:extent=3000KB image_small.jpg

Hopefully, this will shorten the transmission time. Note that , as in

 $ magick image.jpg -quality 85% image_small.jpg

is harder to use when the correlation between quality and storage size is not clear.

## Rotate
To rotate an image by 90&deg; clock wise:

 $ magick image.jpg -rotate 90 image_rotated.jpg

Note rotation not by multiply of 90&deg; necessarily enlarges the size of the minimal rectangular surrounding the image when data loss is not acceptable, and one of the edges of the minimal rectangular should stay in parallel to the earth surface. To get convinced, imagine, or draw, a minimal rectangular surrounding a vertical line, when the line is rotated by, say, 45&deg;.

## Built in GUI
, which is installed by default, can serve as a GUI for many of the tools. Use it to display, or edit, an image or image sequence on any X server. For editing, it has a reasonably competent, but not the full ImageMagic capabilities. With

 $ display -resize 25% *images_in_directory*.jpg

A new window will open.  is meant to show the whole image, without using the entire screen area, which will be the case for a large image. An image that is larger for the screen will automatically get a pan window. The new window will be showing only the 1st image specified in the command line invocation of display, or a default image. Quit by simultaneously pressing the ctrl and q keys, or just the q key. When there is more then a single image, traversing the images back and forth can be done with the backspace and space keyboard keys. Hitting the backspace key at the first image, or the space key at the last image, will quit display. Unless the X server is configured intentionally otherwise, pressing the left mouse button will bring up a menu to work with. Press  for an overview which includes a description of the effect of the mouse buttons, a list of the available menu entries, and a rather long list of keyboard shortcuts. URLs for the other help text for actions the GUI provides are at and [https://github.com/ImageMagick/ImageMagick/blob/main/MagickCore/display.c#L968-L1305

## Screenshot taking
An easy way to take a screenshot of your current system is using the  command:

 $ import -window root screenshot.jpg

Running  without the  option allows selecting a window or an arbitrary region interactively. With  you can specify a delay in which you can, for example, lower some windows.

## Screenshot of multiple X screens
If you run twinview or dualhead, simply take the screenshot twice and use  to paste them together:

{{bc|
$ import -window root -display :0.0 -screen /tmp/0.png
$ import -window root -display :0.1 -screen /tmp/1.png
$ convert +append /tmp/0.png /tmp/1.png screenshot.png
$ rm /tmp/{0,1}.png
}}

## Screenshot of individual Xinerama heads
Xinerama-based multi-head setups have only one virtual screen. If the physical screens are different in height, you will find dead space in the screenshot. In this case, you may want to take screenshot of each physical screen individually. As long as Xinerama information is available from the X server, the following will work:

{{bc|
#!/bin/sh
xdpyinfo -ext XINERAMA | sed '/^  head #/!d;s///' |
while IFS=' :x@,' read i w h x y; do
        import -window root -crop ${w}x$h+$x+$y head_$i.png
done
}}

## Screenshot of the active/focused window
The following script takes a screenshot of the currently focused window. It works with EWMH/NetWM compatible X Window Managers. To avoid overwriting previous screenshots, the current date is used as the filename.

{{bc|
#!/bin/sh
activeWinLine=$(xprop -root | grep "_NET_ACTIVE_WINDOW(WINDOW)")
activeWinId=${activeWinLine:40}
import -window "$activeWinId" /tmp/$(date +%F_%H%M%S_%N).png
}}

Alternatively, the following should work regardless of EWMH support:

 $ import -window "$(xdotool getwindowfocus -f)" /tmp/$(date +%F_%H%M%S_%N).png

## Encryption of image data
To encrypt:

 $ echo pass_phrase | magick image.jpg -encipher - -depth 8 png24:image.png

This can be decrypted by:

 $ echo pass_phrase | magick image.png -decipher - image.jpg

It is highly advised to read the discussion at Encrypting Images for all sorts of issues, and suggestions, for such commands.

Metadata of image formats that have the  tag can be used to test for encryption. However, it could be removed or spoofed by an EXIF editing program.

 $ identify -verbose image.png

In general, testing if a raster image was encrypted can be done by checking the distribution of the pixel components. If it exceeds a certain threshold, the data could be considered random and a possible candidate for encryption. However, an example for false positives are images created with the  Diamond-square algorithm.

## Create a PDF from images
See PDF, PS and DjVu#Create a PDF from images. For some background, a stackexchange thread.
