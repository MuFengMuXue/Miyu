# Surf

surf is a simple web browser based on WebKit/GTK. It is able to display websites and follow links. It supports the XEmbed protocol which makes it possible to embed it in another application. Furthermore, one can point surf to another URI by setting its XProperties.

## Installation
Install the  package. Due to the absence of releases since 2021, you may want to try the  package for the development version.

Optionally also install the  package for URL-bar

## Configuration
surf is configured through its  file. A sample  file is included with the source and should be instructive.

As with other packages such as dwm, consider using the Arch Build System (ABS) and maintaining your own PKGBUILD with sources and md5sums for your own configuration and source files.

## Extended usage
## Patches & additional features
There are many user-created patches available from the offical site that greatly extend the functionality of surf. Patches can be applied to both the source  file and the  file:

 $ cd src/surf-version/
 $ patch -p1

          Clean
