# 3D Mouse

From Wikipedia:3d mouse#3D mice:
:Also known as bats, flying mice, or wands, these devices generally function through ultrasound and provide at least three degrees of freedom. Probably the best known example would be 3DConnexion/Logitech's SpaceMouse from the early 1990s.

For more information: https://web.archive.org/web/20200731022623/https://www.3dconnexion.com/products/spacemouse.html#panel-whatis

The proprietary drivers have not been updated since 2014 and require potentially unsafe hacks to make them work.

## Installation
There is an open source driver for 3Dconnexion devices maintained by the spacenav project.
From the short list of softwares that supports spacenavd we can cite:

* Blender
* Freecad
* OpenSCAD

For it to work three things must be fulfilled:

# The device must be recognized by the kernel as input device
# The spacenavd daemon must be running
# The application must be compiled with spacenav support. ( should be)

The first requirement should be fulfilled automatically after plugging in the device.
It can be checked by looking if the device is listed in :

For the second point install  and . For testing it is a good idea to start the daemon on foreground mode. The output should look similar to this:

If it works you can simply shut down the daemon by hitting  and run it using the following service to start the daemon (should come with spacenavd).

Now everything is up and running and every supported application should be able to use the 3D Mouse.

## Troubleshooting
If you get an device input access error such as:

 failed to open device: Permission denied

Follow udev#Allowing regular users to use devices to allow the user access to the input device.
