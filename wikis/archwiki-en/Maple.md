# Maple

From the official website:

:Maple is a high-level language and interactive environment for numerical computation, visualization, and programming. Using Maple, you can analyze data, develop algorithms, and create models and applications. The language, tools, and built-in math functions enable you to explore multiple approaches and reach a solution faster than with spreadsheets or traditional programming languages, such as C/C++ or Java.

Maple is proprietary software produced by Maplesoft and requires a license to obtain, install, and activate. Arch is not officially supported, but the installer provided by Maplesoft may work in some cases.

## Installation
Maplesoft provides an installer script that may work on some Arch Linux installations. Version 18 is supported by , later versions use the year as a version: e.g. . Make sure that you have a working Java installation before beginning.

After purchasing your license, download the appropriate Maple release package and unpack it in a location of your choosing. Open a terminal, change to the directory in which you unpacked the files, and run the installer script as a normal user. Installing the program's files inside of a user's home directory is the default option, and allows for easy removal of all components at a later time.

Once the package is installed, you will need to provide a license activation code. This should have been included in your installation archive.

## Troubleshooting
## Blank main window with tiling window managers
See Java#Gray window, applications not resizing with WM, menus immediately closing.

## 3D plots failing
Maple ships with its own C++ runtime, which seems to cause issues with 3D rendering (plot3d, implicitplot3d, ...).

Linking the system's  instead seems to fix the problem (replace  with your version):

 maple20nn/bin.X86_64_LINUX/system

and link  and  to your system's version:

 libstdc++.so.6 -> /usr/lib64/libstdc++.so.6
 libstdc++.so.6.0.20 -> /usr/lib64/libstdc++.so.6.0.22

Another problem with 3D plots, when using Intel graphics, unrelated to the libstdc++: if the method described above does nothing, you should run the following command before launching Maple:

 export MESA_LOADER_DRIVER_OVERRIDE=i965

You can modify the .desktop file, so that this command is ran automatically when Maple is launched.

## Offline activation
If activation by license key does not work, you may try Offline Activation.

Enter your license key in the Purchase Code field, and select either Host ID or Disk Serial Number as the hardware activation method.

To obtain your Host ID, run the following command:

 $ ip address show | grep link/ether | awk '{ print $2; }' | sed 's/://g'

and use one of the resulting IDs.

Enter your e-mail address (or use a disposable one), then copy the contents into .

This should activate Maple on next startup.

## Offline use
Your Maple license is bound to your MAC address (they call it host ID).

For NetworkManager 1.2.0 and newer, MAC address randomization while not connected to a network is enabled by default, which interferes with Maple's ability to verify the license.

To fix this, add the following to NetworkManager.conf and restart NetworkManager.

 device
 wifi.scan-rand-mac-address=no

## Error trying to write your license file
When installed via the AUR script  mentioned on this page, the activation application (e.g ) mentioned in the post-install hook must be run as root or you will receive the error:

 There was an error while trying to write your license file. Please ensure you have the proper permission to write to the license directory and try your request again.

As it is a GUI application, you may need to follow the instructions from Privilege elevation for graphical applications for the activation application to open.
