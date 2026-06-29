# Clevo P650RS

The P650RS is a device by the Taiwanese OEM manufacturer Clevo. It is also sold
as Sager NP8153-S and many other names. The hardware is configurable and
includes an Intel Skylake Core i7, NVIDIA 1070M graphics, USB-C connectors, a
fingerprint reader, mini DisplayPort as well as HDMI connections, and more.

## Graphics
The Clevo is available in switchable, and non-switchable configurations. In
configurations with both integrated and discrete GPUs, the BIOS includes an
an option () to disable the integrated card, rendering it the
same as the dedicated GPU model.

## Discrete only
Given this laptop has a mux, it does not require PRIME configuration to make use
of the dedicated graphics card in full even though it should be possible.
Installation should follow NVIDIA after setting and booting with
 BIOS option.

Using the NVIDIA proprietary driver (testing with 375.20) the backlight may not
come back on after the display has gone to sleep. A workaround is to drop to
console (e.g. Ctrl-Alt-F2) and then back to X.

## Switchable / Optimus
Xorg may not work out of the box with a  error.

Xorg selects the dGPU when in fact it is the integrated one that has the control
of the screen. This is probably an issue only fixable with a BIOS update
(testing against v1.05.03, it will not work).

To overcome this a xorg configuration file needs to be created telling xorg the
correct address and driver combination. This can be done by creating (or adding
the line with  in:
{{hc|/etc/X11/xorg.conf.d/20-intel.conf|
Section "Device"
        Identifier "Intel Graphics"
        Driver     "intel"
        BusID      "PCI:x:x:x"    # 20W on idle though.

## Keyboard Backlight
For the white keyboard backlight, no special actions are required. However the RGB-backlit keyboard will not work out of the box.

To enable the Keyboard, the installation of the  package is required.

The colors of the three sections can be controlled, after loading the kernel module, the special keys on the keyboard (, , , ) should work.

## Wi-Fi
Wi-Fi seems to work well and coexist nicely with Bluetooth. Consider enabling antenna aggregation to take the most out of the hardware: iwlwifi.

When using the  package, the  combination to toggle air plane mode also works.

## Webcam
As with the Clevo W840SU the webcam must be activated with
before it will show up in the device list. This survives a reboot.
