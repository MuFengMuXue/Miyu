# Google Earth

From the project web page:

:Google Earth allows you to travel the world through a virtual globe and view satellite imagery, maps, terrain, 3D buildings, and much more. With Google Earth's rich, geographical content, you are able to experience a more realistic view of the world. You can fly to your favorite place, search for businesses and even navigate through directions.

## Installation
Install the  package.

## Troubleshooting
## Crash on startup
Google Earth can crash on startup for numerous reasons. Here are some of the most common ones.

## Startup tips are enabled
While startup tips can be useful, they are also known to cause crashes. To disable them, change or add the line below to the :

## No new line at the end of drirc
This can cause a crash with -dri drivers:

 $ echo >> ~/.drirc

## Corrupt settings
In case the cache is corrupt and needs recreation, remove it:

 $ rm -r ~/.googleearth/Cache/

If that did not work, try removing the whole settings directory:

 $ rm -r ~/.googleearth/

## Another crash happened while handling crash!
You may try removing the following:

 $ rm -f ~/.googleearth/Cache/cookies ~/.googleearth/instance-running-lock

## Wayland
Google Earth does not seem to support Wayland yet, forcing X11 helps in this situation. Launch using:

 $ QT_QPA_PLATFORM=xcb google-earth-pro

## Panoramio photos not working
There have been numerous reports [https://productforums.google.com/forum/#!msg/earth/_h4t6SpY_II/6O_DTry49pgJ on this in the [https://productforums.google.com/forum/#!categories/earth/linux Google Earth forums with varying solutions.

## Graphical corruption
Either refer to the #Corrupt settings section above or disable texture compression in Tools > Options... > 3D View > Compress.

## Earth shows nothing but yellow borders
Taken from the changelog of 7.0.3 this issue has improved to some extent but overall it is still there:

 Imagery now displays for Linux users running specific families of Intel GPUs.

## Excessive memory use
Memory use can be controlled by limiting the maximum cache size in Tools > Options... > Cache, or by lowering the graphics settings in the 3D View tab.
