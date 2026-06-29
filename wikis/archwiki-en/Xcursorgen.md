# Xcursorgen

xcursorgen is a tool that allows for creation of cursor files to be used with Xorg. A cursor can be created from PNG files.

## Installation
Install the  package.

## Usage
By default, the user has to supply two files to xcursorgen:

* a square image file saved as PNG
* a configuration

xcursorgen takes two arguments: the configuration file and an output path.

The configuration file must at least contain the following, space-delimited values:

* image size in pixels
* : the x coordinate of the pointer tip
* : the y coordinate of the pointer tip
* file name

Suppose there is an image file named  of 32x32 pixels. Save this configuration file alongside:

and run:

 $ xcursorgen red.cursor default

This will create the cursor as  which can later on be used with Xorg.
The pointer tip is located in the upper left.

## Animated cursors
Animated cursors are created from multiple image files.
For animated cursors copy the configuration line for each image file and specify a delay in milliseconds for each frame:

## Installing created cursor files
If only some cursors of an already existing cursor theme should be changed, create a custom directory in .
Create this file inside the folder:

Note that the  has to be the same as the directory name.

Next, copy the cursor file created from xcursorgen into a subdirectory , e.g.:

Now, configure your system to use this newly created cursor theme.
Note that most applications have to be restarted to use the new cursor theme.

For more information, refer to Cursor themes#Manually.
