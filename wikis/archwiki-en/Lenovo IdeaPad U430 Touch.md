# Lenovo IdeaPad U430 Touch

## Installation
To install Arch, turn your device completely off (shutdown Windows). Now press the little switch on the left side of the device near the Ethernet port. You are now able to enter the BIOS and disable Secure Boot. After that, save your settings and shutdown the machine once more. After pressing the small button again, you may enter the boot menu and choose your USB installation medium.

You are probably greeted now by complete darkness, press  a few times to brighten up your screen.

## Graphics
Graphics work well out of the box after installing . Bumblebee works very well too, if you want to use the integrated NVIDIA card. Be sure to also install  and .

If you do not want to use Optimus, consider disabling it in the BIOS, there is an option for this.

## Track-pad
Copy and edit  until it fits your needs. Here is an example:

## Hot-keys
Work perfectly. There is a setting in the BIOS to switch the function keys, so that they () work as intended.

## Power management
There is a noticeable drop in battery run-time compared to Windows 8, but there are tools to improve from about 3h to almost 6h.

First, if you are using it, make sure Bumblebee and most important bbswitch are properly set up. If not, it may happen that your NVIDIA card runs at all times! If that's the case your device will get a lot hotter and louder than in normal operation.

Check if your card is on or off with

For general power management and if you do not want to tweak every setting yourself, install and enable TLP.

DO NOT install laptop-mode, cpupower, or any other power-management tools in addition to tlp. cpupower may even break p-state (powersaving) of your Haswell CPU, modern CPUs know how to handle themselves.
