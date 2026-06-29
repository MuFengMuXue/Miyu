# Razer peripherals

Razer Inc makes gaming-focused computer hardware and other consumer electronics. There are currently no official drivers for any Razer peripherals in Linux.

Projects like razercfg, OpenRazer can be used to enable Razer support.

There is also the OpenRGB project which aims to have manufacturer agnostic lighting configurations.

## OpenRGB
See OpenRGB.

## razercfg
## Compatibility
A list of compatible devices can be found here.

## Installation
Install the  package.

Enable and start the  service.

## Configuration
The file  can be
used to specify various razerd options and initial hardware configuration settings. An example config file is included as  in the package.

If no configuration file is available, razerd will work with default settings.

## Using the Razer Configuration Tool
There are two tools provided, one CLI: razercfg and a Qt-based GUI: qrazercfg.

With either tool you can set 5 profiles, change the DPI, change mouse frequency, enable and disable the scroll and logo lights and configure the buttons.

If settings change on reboot, edit the configuration file directly and test after a reload of the service is done. For example:

## OpenRazer
## Compatibility
A list of compatible devices can be found here.

## Installation
Install the  package. Add your current user to the user group  before logging out and back in.

If customizing and configuring devices is not the priority, one can install just the  package instead.

## How to use
## CLI
The  can be used to configure devices via the terminal.
## GUI
The recommended way is to use a graphical front-end for interfacing with the drivers.

* : A Qt-based (Python) front-end with effect editor
* : A Qt-based front-end with custom editor
* : A GTK-based front-end
* Snake: A front-end able to bind mouse buttons + keyboard

## Troubleshooting
Visit the Troubleshooting page in the OpenRazer wiki.

## Razer keyboards
There are currently two Python scripts available to enable the extra M1 - M5 macro keys, that certain Razers have, under Linux:
Note that this does not allow to assign any content to Macro keys, it merely will enable the sending of keycodes. For Razers without M1 -M5 extra keys there is no point using this tool.

## Blackwidow Control
## Features
* confirmed to work with regular BlackWidow, BlackWidow 2013 and BlackWidow Ultimate Stealth 2014
* should also work with BlackWidow Ultimate, BlackWidow Ultimate 2013 and BlackWidow 2014
* does not work with BlackWidow (Ultimate) 2016 yet
* uses Python 3
* allows to control the status of the LED
* contains a file with udev rule so macro keys will be enabled automatically when the keyboard is plugged in

## How to Use
Install . After install, run:

 # blackwidowcontrol -i

Then use the shortcut utility of your Desktop Environment to map the keys, i.e. to actually use the macro keys for something useful. For example, the "KDE global shortcuts" GUI (find it in system settings) can assign macros to a key on any keyboard, not just Razers.

## Blackwidow macro scripts
## Features
* Works with BlackWidow Ultimate and Stealth 2013 (unknown whether it works with other versions or keyboard models)
* adding the "021e" ID for Ornata Chroma makes the Game-mode feature (white "G" LED) work on Ornata Chroma as well.
* Uses Python 2
* Bundles scripts to create and execute macros

## Troubleshooting
## Mouse randomly stops working
If your razer mouse stops working after some time, however, led flashes or lights up, but reboot and re-plugging does not help, try the following commands.

Unload  and  modules:

 # rmmod ehci_pci
 # rmmod ehci_hcd

Disconnect the mouse, wait a few seconds and run the following commands to load modules back:

 # modprobe ehci_hcd
 # modprobe ehci_pci

Connect the mouse and it should be working.

## CAPS Lock makes Razer Blade Stealth crash
The crash is caused by keyboard built-in driver.

## If using Xorg
Get the keyboard description:

 $ xinput list | grep "Set 2 keyboard"

And create the file below, here we assume the above command returned "AT Raw Set 2 keyboard".

## If using Xwayland
CAPS Lock will now be identified as another CTRL key.

Source: https://github.com/rolandguelle/razer-blade-stealth-linux/blob/master/ubuntu-18-04.md#13-caps-lock-crash
