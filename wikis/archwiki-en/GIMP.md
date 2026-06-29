# GIMP

GIMP is a powerful raster image editing program, and commonly used for photo retouching, image composition, and general graphic design work. It can be used as a simple paint program, an expert quality photo retouching program, an online batch processing system, a mass production image renderer, an image format converter, etc.

## Installation
Install the  package.

## Tips and tricks
## Captions
To caption an image follow these steps after inputting the desired text:

# Click Layer and Text to Path
# Click Select and From Path
# Click Select and Invert
# Click Edit and Stroke Path

## Create a circle
To draw a circle in GIMP follow these steps:

# Select the Ellipse tool and hold
# Click Edit and Fill with Color
# Click Select and Shrink
# Press

## Photoshop behaviour
Since GIMP is highly configurable, it is possible to change the keybinds, and even the UI, to be more familiar to those who are used to the raster image editing program Photoshop.

Specifically the GimpPs theme aims to make GIMP behave more like Photoshop, which you can install on top of GIMP.

Alternately, if you just want the keybinds, the relevant lines are included in the theme's  file, which you can then add to your local .

There is also the PhotoGIMP project, aiming to do to the same.

## Plugins
GIMP has an extensive plugin system, as well as a Scheme interpreter which can be used to write Script-Fu scripts.

Most plugins are distributed via the official repositories (for example, ) and the AUR; some, but not all, are listed as optional dependencies of the  package.

## Manual installation
If not distributed via the repositories, plugins can be compiled and installed using the  executable.

To install a plugin from source:

To install a pre-compiled plugin:

To install a Script-Fu script:

Further options may be found in the  message.

## Packaging
Plugin packages should add their files to a directory with their name within .

## Troubleshooting
## Green text
Add the following to  if you see a green tint around letters with antialiasing enabled:

## Hide Noto
Add the following to  if you have  installed and would like to remove them from GIMP's fonts list:

See  and Font configuration#Whitelisting and blacklisting fonts for more information.

## PDF files
GIMP requires the  library to open PDF files or it will report that they are unrecognised.

Since GIMP rasterizes PDF files right from the start, it will not exploit intrinsic PDF capabilities while editing them. Other programs (like LibreOffice Draw) can be used to better edit PDF files.

## Global menu in KDE Plasma under Wayland
If you don't see the global menu in GIMP, make sure you have installed the packages from KDE#Plasma 6 Global Menu not working with some applications. If the problem still persists, use environment variable to launch GIMP: .
