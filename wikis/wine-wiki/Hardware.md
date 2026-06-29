Wine includes some limited support for direct hardware access, including
running native Windows drivers. This comes with several restrictions,
but we still have been able to successfully access some native devices.

## Restrictions

- Wine runs in user space, and therefore *cannot* access any hardware
  that the kernel does not expose a user-space interface for. Depending
  on operating system this can be prohibitive, although Linux exposes
  interfaces for many common protocols, including PCI, USB, serial and
  parallel ports.

- Wine *cannot* drive hardware that is currently being driven by the
  host operating system. This means, for instance, that we cannot drive
  keyboard and mouse devices, or GPU or network drivers, without
  disabling them on the host side, and hence making them unusable for
  applications not being run through Wine.

- We are unlikely to implement support for common classes of devices
  which are usually accessed through a higher-level API, including but
  not limited to: GPU, network, mass storage, keyboard and mouse, audio,
  camera. If such devices are unsupported or poorly supported, effort
  should be spent on bringing up support for the host system instead.
  Efforts to support direct hardware access in Wine are mostly about
  domain-specific (and often obsolete) hardware, which it would be
  difficult and not particularly worthwhile to reverse-engineer host
  drivers for.
  - Although part of the problem here is accessing hardware which is
    usually also being driven by the host system (as in the above
    restriction), another part is about hooking up access via high-level
    Win32 APIs. For example, we implement Win32 sockets directly on top
    of POSIX sockets; implementing the infrastructure required to run NT
    network drivers, and hooking up Win32 sockets to these, would be a
    massive undertaking, and due to the design of kernel drivers in Wine
    it would likely have negative performance impact. In many cases the
    kernel interface is also undocumented, adding to the difficulty.
  - Note however that some devices have special configuration only
    available through a Win32 driver, and we may be able to support that
    special configuration while neglecting to implement support for the
    device's "normal" usage. For example, the SteelSeries USB mouse
    driver offers the ability to modify the mouse's LED settings as well
    as simply driving the mouse, and in this case Wine is able to pass
    through the LED settings while still being unable to drive the mouse
    normally. Note that other restrictions still apply; e.g. settings
    cannot be changed while the mouse is being used by the host
    operating system.

- Hardware that is being driven through wine can *only* be accessed
  through Windows programs, and cannot be accessed from host programs
  outside of Wine. E.g. in some cases it is possible to use Wine to run
  HID drivers, but those HID devices will only appear to Windows
  programs run through Wine, and not to other programs on the host
  operating system.

- Some native NT drivers require kernel interfaces that we *cannot*
  support. (One notable example of this is the ability to access user
  space memory via `METHOD_NEITHER` ioctls that contain pointers.)

- As of the time of this writing (April 2022), support for direct
  hardware access has received limited testing and limited attention.
  Only a small number of protocols have been hooked up to any degree.
  Many interfaces are also missing. It's worth mentioning also that
  there are plenty of bugs affecting driver installation. If an
  application doesn't work, and you believe it should be able to
  work—considering the above restrictions—please [report a
  bug](https://bugs.winehq.org/).

## USB

As of Wine 5.7, Wine includes support for USB kernel drivers. This
requires a functional libusb 1.0 on the host, including at compile time.
As of the time of writing (Wine 7.6), user space access via winusb.dll
is not yet implemented.

Depending on operating system and configuration, you may need to ensure
that Wine has permission to access the device in question.

On Linux, this means read/write access. This can be done via a udev
rules file. Refer to the `udev(7)` manual page for full documentation.
For quick testing, though, the following file, placed as
/etc/udev/rules.d/99-usb.rules will grant full read/write access to the
specified device to **all** (world) users:

    SUBSYSTEM=="usb", ATTR{idVendor}=="1234", ATTR{idProduct}=="abcd", MODE="0666"

Safer is to set up a separate group and use the `GROUP="mygroup"`
directive, and then restrict the mode to 0664.

You may need to make sure that your rules apply last, after those
shipped by the distribution, hence using a high number such as 99 will
help.

Replace `1234` and `abcd` with the actual hexadecimal ID of the device.
This can be found using `lsusb`.

## Serial and parallel ports

Wine includes support for serial and parallel I/O via user space.
Support for kernel drivers is not implemented.

## HID

HID support has been added to Wine. It is now used as a backend for
every game controller device and all the relevant APIs to access them
from the Windows side. It is implemented over the host's libSDL or
evdev, although pass-through of host HID devices is also possible when
they are accessible through hidraw.

### Relevant Debug Channels

- `+hid`: Traces all HID stack events
- `+rawinput`: Traces for the RawInput frontend
- `+dinput`: Traces for the DInput frontend
- `+xinput`: Traces for the XInput frontend
- `+input`: Traces for the Windows.Gaming.input frontend

### Pass-through of specific HID devices

Some devices, such as the Sony DualShock and Sony DualSense are using a
proprietary protocol that is the only way to access features such as LED
control or advanced haptics. This protocol is supported by several
Windows applications, and the only way to make it accessible to them is
to setup the HID stack in pass-through mode directly to the host HID
device, through hidraw.

On Linux, by default, no hidraw devices are not accessible to normal
users. You will need to either add rw permission to the `/dev/hidraw`<X>
device that you want to have accessible in Wine, or better, add a new
udev rule to automatically allow access on matching devices when they
are added.

Several distributions already provide packages that contain the
necessary udev rules for these devices. Most of them are related to
Steam, and on Debian the package is named `steam-devices`. Installing
this package (you don't even need to install Steam) should be enough to
have the udev rules installed and no manual setup will then be
necessary. For manual configuration, the relevant udev rules to copy can
be found in that package sources
[1](https://github.com/ValveSoftware/steam-devices/blob/master/60-steam-input.rules).

### Tools to use with device testing

- hid_test.exe: Wine tests written around direct HID access, in the wine
  tree dlls/hid/tests.
- hclient.exe: This is distributed by Microsoft in the DDK (and various
  free download sites if you are so inclined). This tool will enumerate
  devices and allow for all various levels of control and exploration.
- hid.exe: (https://www.codeweavers.com/xfer/aric/HID/ access-key:
  sLcm7EZ7) A quick sample application for testing HID joysticks and
  gamepads with source.
- HID descriptor parser: (https://eleccelerator.com/usbdescreqparser/) a
  web page to parse descriptor byte strings. Useful for debugging
  devices.

### Devices that have been tested

| Device                                     | Platform(s)  | Status                                     |
|--------------------------------------------|--------------|--------------------------------------------|
| Logitech Rumblepad 2                       | Linux / OS/X | Working                                    |
| Xbox360 Controller                         | OS/X         | Working (with 3rd party drivers installed) |
| Steam Controller                           | ---          | Not working                                |
| MY-POWER / CSL (low budget ps3 controller) | Linux        | Working                                    |
| Playstation 4 Controller (DS4)             | OS/X         | Working                                    |

### Hid Talks given by [Aric Stewart](@aricstewart) at WineConfs

- [WineConf 2016](/media/Hid-wineconf2016.pdf)
- [WineConf 2015](/media/Hid-wineconf2015.pdf)
