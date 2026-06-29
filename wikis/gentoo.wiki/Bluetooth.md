This page contains [[changes](https://wiki.gentoo.org/index.php?title=Bluetooth&oldid=1291133&diff=1424772)] which are not marked for translation.

Other languages:

-   [Deutsch](https://wiki.gentoo.org/wiki/Bluetooth/de "Bluetooth (92% translated)")
-   [English]
-   [français](https://wiki.gentoo.org/wiki/Bluetooth/fr "Bluetooth (60% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/Bluetooth/hu "Bluetooth (100% translated)")
-   [polski](https://wiki.gentoo.org/wiki/Bluetooth/pl "Bluetooth (36% translated)")
-   [தமிழ்](https://wiki.gentoo.org/wiki/Bluetooth/ta "ஊடலை (60% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/Bluetooth/zh-cn "蓝牙 (51% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Bluetooth/ja "Bluetooth (100% translated)")

**Resources**

[[]][Wikipedia](https://en.wikipedia.org/wiki/Bluetooth "wikipedia:Bluetooth")

This article describes the configuration and usage of Bluetooth controllers and devices.

## Contents

-   [[1] [Prerequisites]](#Prerequisites)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Kernel]](#Kernel)
    -   [[2.2] [Firmware]](#Firmware)
    -   [[2.3] [USE flags]](#USE_flags)
    -   [[2.4] [Emerge]](#Emerge)
-   [[3] [Configuration]](#Configuration)
    -   [[3.1] [Permissions]](#Permissions)
    -   [[3.2] [Services]](#Services)
        -   [[3.2.1] [OpenRC]](#OpenRC)
        -   [[3.2.2] [systemd]](#systemd)
    -   [[3.3] [Enabling experimental mode]](#Enabling_experimental_mode)
-   [[4] [Usage]](#Usage)
    -   [[4.1] [Battery level]](#Battery_level)
    -   [[4.2] [Controller setup]](#Controller_setup)
    -   [[4.3] [Device pairing]](#Device_pairing)
    -   [[4.4] [hciconfig]](#hciconfig)
-   [[5] [Wake from suspend]](#Wake_from_suspend)
-   [[6] [Disable Bluetooth]](#Disable_Bluetooth)
    -   [[6.1] [Using udev to disable Bluetooth]](#Using_udev_to_disable_Bluetooth)
    -   [[6.2] [Using OpenRC to disable Bluetooth]](#Using_OpenRC_to_disable_Bluetooth)
    -   [[6.3] [Disable Bluetooth at kernel level]](#Disable_Bluetooth_at_kernel_level)
-   [[7] [Utilities]](#Utilities)
-   [[8] [Troubleshooting]](#Troubleshooting)
    -   [[8.1] [TLP and laptop_mode]](#TLP_and_laptop_mode)
    -   [[8.2] [XBOX ONE controller pairing]](#XBOX_ONE_controller_pairing)
    -   [[8.3] [Notebook has a Synopsys DesignWare Controller]](#Notebook_has_a_Synopsys_DesignWare_Controller)
    -   [[8.4] [Resolving firmware problems]](#Resolving_firmware_problems)
-   [[9] [See also]](#See_also)
-   [[10] [References]](#References)

## [[] Prerequisites]

This article assumes that [udev](https://wiki.gentoo.org/wiki/Udev "Udev") and [USB](https://wiki.gentoo.org/wiki/USB "USB") have been previously configured.

## [[] Installation]

### [[] Kernel]

In most cases enabling [RFCOMM](https://en.wikipedia.org/wiki/List_of_Bluetooth_protocols#Radio_frequency_communication_.28RFCOMM.29 "wikipedia:List of Bluetooth protocols") (`CONFIG_BT_RFCOMM`), [HIDP](https://en.wikipedia.org/wiki/List_of_Bluetooth_profiles#Human_Interface_Device_Profile_.28HID.29 "wikipedia:List of Bluetooth profiles") (`CONFIG_BT_HIDP`), [HCI](https://en.wikipedia.org/wiki/List_of_Bluetooth_protocols#Host_Controller_Interface_.28HCI.29 "wikipedia:List of Bluetooth protocols") USB (`CONFIG_BT_HCIBTUSB`) and/or HCI UART (`CONFIG_BT_HCIUART`) should be sufficient. The User-space I/O driver for HID input devices (`CONFIG_UHID`) should be enabled for Bluetooth keyboards and mice. `CONFIG_INPUT_UINPUT` is used also in some rare devices (^[\[1\]](#cite_note-1)^).

[KERNEL] **Enabling Bluetooth support**

      Networking support Search for <code>CONFIG_NET</code> to find this item. --->
       [*] Bluetooth subsystem support Search for <code>CONFIG_BT</code> to find this item. --->
         [*]  Bluetooth Classic (BR/EDR) features Search for <code>CONFIG_BT_BREDR</code> to find this item.
         <*>    RFCOMM protocol support Search for <code>CONFIG_BT_RFCOMM</code> to find this item.
         [ ]      RFCOMM TTY support Search for <code>CONFIG_BT_RFCOMM_TTY</code> to find this item.
         < >    BNEP protocol support Search for <code>CONFIG_BT_BNEP</code> to find this item.
         [ ]      Multicast filter support Search for <code>CONFIG_BT_BNEP_MC_FILTER</code> to find this item.
         [ ]      Protocol filter support Search for <code>CONFIG_BT_BNEP_PROTO_FILTER</code> to find this item.
         <*>    HIDP protocol support Search for <code>CONFIG_BT_HIDP</code> to find this item.
         [*]  Bluetooth Low Energy (LE) features Search for <code>CONFIG_BT_LE</code> to find this item.
              Bluetooth device drivers --->
                <M> HCI USB driver Search for <code>CONFIG_BT_HCIBTUSB</code> to find this item.
                [*]   Enable USB autosuspend for Bluetooth USB devices by default Search for <code>CONFIG_BT_HCIBTUSB_AUTOSUSPEND</code> to find this item.
                <M> HCI UART driver Search for <code>CONFIG_BT_HCIUART</code> to find this item.
         <*> RF switch subsystem support Search for <code>CONFIG_RFKILL</code> to find this item. --->
     Device Drivers --->
       Input device support  --->
         [*] Miscellaneous devices Search for <code>CONFIG_INPUT_MISC</code> to find this item. --->
           [*] User level driver support Search for <code>CONFIG_INPUT_UINPUT</code> to find this item.
       [*] HID bus support Search for <code>CONFIG_HID_SUPPORT</code> to find this item. --->
           [*] User-space I/O driver support for HID subsystem Search for <code>CONFIG_UHID</code> to find this item.

** Important**\
Kernel may fail to initialize RFCOMM/BNEP being compiled as built-in. System log for bluetooth service in this case will mention the lack of RFCOMM/BNEP support. And this in turn for example may break HSP/HFP headset profile initialization. So if dmesg says nothing about RFCOMM, better recompile as a module.

### [[] Firmware]

Most Bluetooth controllers need [firmware](https://wiki.gentoo.org/wiki/Linux_firmware "Linux firmware") to function. If the controller is supported by Linux, [dmesg] will usually indicate if firmware is needed. The [[[sys-kernel/linux-firmware]](https://packages.gentoo.org/packages/sys-kernel/linux-firmware)[]] package should provide the needed firmware, although some devices may need firmware that is available in another package or obtainable only from the manufacturer.

`root `[`#`]`emerge --ask --noreplace sys-kernel/linux-firmware`

### [[] USE flags]

[BlueZ](http://www.bluez.org/) is an implementation of the Bluetooth protocol stack for Linux, and it is provided by the [[[net-wireless/bluez]](https://packages.gentoo.org/packages/net-wireless/bluez)[]] package.

### [USE flags for] [net-wireless/bluez](https://packages.gentoo.org/packages/net-wireless/bluez) [[]] [Bluetooth Tools and System Daemons for Linux]

  ----------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+mesh`](https://packages.gentoo.org/useflags/+mesh)                   Add support for Bluetooth Mesh control application and advertising bearer.
  [`+obex`](https://packages.gentoo.org/useflags/+obex)                   Enable OBEX transfer support
  [`+readline`](https://packages.gentoo.org/useflags/+readline)           Enable support for libreadline, a GNU line-editing library that almost everyone wants
  [`+udev`](https://packages.gentoo.org/useflags/+udev)                   Enable virtual/udev integration (device discovery, power and storage device support, etc)
  [`btpclient`](https://packages.gentoo.org/useflags/btpclient)           Enable BTP client
  [`cups`](https://packages.gentoo.org/useflags/cups)                     Add support for CUPS (Common Unix Printing System)
  [`debug`](https://packages.gentoo.org/useflags/debug)                   Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`deprecated`](https://packages.gentoo.org/useflags/deprecated)         Build deprecated plugins
  [`doc`](https://packages.gentoo.org/useflags/doc)                       Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`experimental`](https://packages.gentoo.org/useflags/experimental)     Build experimental plugins
  [`extra-tools`](https://packages.gentoo.org/useflags/extra-tools)       Install tools that upstream doesn\'t install on purpose by default. All this tools shouldn\'t be used. Then, please notify upstream about you still need them to let them know the situation.
  [`man`](https://packages.gentoo.org/useflags/man)                       Build and install man pages
  [`midi`](https://packages.gentoo.org/useflags/midi)                     Enable MIDI support
  [`selinux`](https://packages.gentoo.org/useflags/selinux)               !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`systemd`](https://packages.gentoo.org/useflags/systemd)               Enable use of systemd-specific libraries and features like socket activation or session tracking
  [`test`](https://packages.gentoo.org/useflags/test)                     Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`test-programs`](https://packages.gentoo.org/useflags/test-programs)   Install tools for testing of various Bluetooth functions
  ----------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-26 02:33] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

Bluetooth support can be enabled system-wide by setting the `USE` variable to `bluetooth`:

[FILE] **`/etc/portage/make.conf`**

    USE="bluetooth"

Alternatively, support can be enabled individually on important packages, for example, PulseAudio and PipeWire sound servers.

### [[] Emerge]

The system needs to be updated if the `USE` variable was set to `bluetooth`:

`root `[`#`]`emerge --ask --changed-use --deep @world`

Install BlueZ:

`root `[`#`]`emerge --ask --noreplace net-wireless/bluez`

## [[] Configuration]

### [[] Permissions]

Permissions for Bluetooth devices is handled automatically by D-Bus, and access is granted to all users by default.

### [[] Services]

#### [[] OpenRC]

Start bluetooth:

`root `[`#`]`rc-service bluetooth start`

Start bluetooth at boot:

`root `[`#`]`rc-update add bluetooth default`

#### [[] systemd]

Start bluetooth:

`root `[`#`]`systemctl start bluetooth`

Start bluetooth at boot:

`root `[`#`]`systemctl enable bluetooth`

### [[] Enabling experimental mode]

** Note**\
The `experimental` USE flag needs to be enabled in [[[net-wireless/bluez]](https://packages.gentoo.org/packages/net-wireless/bluez)[]].

** Warning**\
Using [bluez]\'s experimental mode may prevent some bluetooth microphones from connecting automatically.^[\[2\]](#cite_note-2)^

Enable experimental mode:

[FILE] **`/etc/bluetooth/main.conf`**

    [General]

    Experimental=true

Restart bluetooth to apply the configuration changes:

`root `[`#`]`rc-service bluetooth restart`

## [[] Usage]

### [[] Battery level]

[Bluez] has a feature to report a device\'s battery level to upower. Upower should know the battery level of every device which supports sending its own battery level.

`user `[`$`]`upower --dump`

will dump all information of connected devices including battery details.

The [D-Bus](https://wiki.gentoo.org/wiki/D-Bus "D-Bus") property can also be fetched directly via

`user `[`$`]`dbus-send --system --print-reply --dest=org.freedesktop.UPower /org/freedesktop/UPower/devices/<device> org.freedesktop.DBus.Properties.Get string:"org.freedesktop.UPower.Device" string:"Percentage"`

or^[\[3\]](#cite_note-3)^

`user `[`$`]`dbus-send --system --print-reply --dest=org.bluez /org/bluez/<hci>/<device> org.freedesktop.DBus.Properties.Get string:"org.bluez.Battery1" string:"Percentage"`

Alternatively

`user `[`$`]`bluetoothctl info`

will show the battery percentage of connected devices.

### [[] Controller setup]

If, after following the steps described in the \"[Installation](#Installation)\" and \"[Configuration](#Configuration)\" sections above, Bluetooth doesn\'t appear to be working, or an attempt to enable the controller results in a message such as:

\

    Can't init device hci0: Operation not possible due to RF-kill

query the state of the Bluetooth radio transmitter with [[[rfkill(8)]](https://man.archlinux.org/man/rfkill.8.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]:

`root `[`#`]`rfkill list bluetooth`

    0: hci0: Bluetooth
            Soft blocked: no
            Hard blocked: no

[rfkill] is provided by [util-linux](https://wiki.gentoo.org/wiki/Util-linux "Util-linux").

** Note**\
If Bluetooth is blocked or disabled in the BIOS/UEFI, [rfkill] may incorrectly list the controller as `Hard blocked: no`.

Unblock the controller if [rfkill] indicates (with `Soft blocked: yes`) that the controller is blocked:

`root `[`#`]`rfkill unblock bluetooth`

If [rfkill] indicates (with `Hard blocked: yes`) that the controller is blocked, unblock the controller by physical switch or keyboard function key.

Bluetooth controllers can be enabled automatically by setting `AutoEnable=true` in [/etc/bluetooth/main.conf]:

[FILE] **`/etc/bluetooth/main.conf`**

    [Policy]
    AutoEnable=true

In some instances Bluetooth controllers may have been soft-blocked by power management tools in udev. Make sure `state` is set to `1` in the corresponding rule file, or remove the following line entirely:

[FILE] **`/etc/udev/rules.d/10-local-powersave.rules`**

    SUBSYSTEM=="rfkill", ATTR=="bluetooth", ATTR="1"

### [[] Device pairing]

Bluetooth devices need to be paired with a Bluetooth controller before they can be used. This is done by entering a PIN (or other code) on both devices via an interaction agent. Certain devices such as headsets do not allow entering an arbitrary PIN. These devices use a static PIN, which is usually 0000, 1111, 1234 or 9999. There are also devices (e.g. [Sony BD Remote Control](https://en.wikipedia.org/wiki/PlayStation_3_accessories#Blu-ray_Disc_Remote_Control "wikipedia:PlayStation 3 accessories")) that do not require PIN entry, and attempting to enter a PIN when prompted will result in failure. Pairing can be skipped with such devices.

This article only covers device pairing with [bluetoothctl], which is a command-line interaction agent provided by the [[[net-wireless/bluez]](https://packages.gentoo.org/packages/net-wireless/bluez)[]] package. If a graphical desktop environment is being used, device paring can be done with a graphical interaction agent. For [KDE](https://wiki.gentoo.org/wiki/KDE "KDE") use [[[kde-plasma/bluedevil]](https://packages.gentoo.org/packages/kde-plasma/bluedevil)[]], for [GNOME](https://wiki.gentoo.org/wiki/GNOME "GNOME") use [[[net-wireless/gnome-bluetooth]](https://packages.gentoo.org/packages/net-wireless/gnome-bluetooth)[]], and for GTK use [[[net-wireless/blueman]](https://packages.gentoo.org/packages/net-wireless/blueman)[]].

** Note**\
[bluetoothctl] commands can be run not only via an interactive session, but also directly from the command line. For example, to run a command available in the top level of an interactive session, provide the command as an argument to [bluetoothctl], e.g.:

`user `[`$`]`bluetoothctl list`

To provide a command in a submenu of an interactive session, prepend the command with the name of the submenu followed by `.`, e.g.:

`user `[`$`]`bluetoothctl scan.auto-connect off`

Start a [bluetoothctl] interactive session:

`user `[`$`]`bluetoothctl`

List the available controllers:

`[bluetooth]#``list`

Display information about a controller:

`[bluetooth]#``show `*`controller_mac_address`*

Set the default controller:

`[bluetooth]#``select `*`controller_mac_address`*

Power on the controller:

`[bluetooth]#``power on`

Enable the agent and set it as default:

`[bluetooth]#``agent on `

`[bluetooth]#``default-agent `

Set the controller as discoverable (temporarily for 3 minutes) and pairable:

`[bluetooth]#``discoverable on `

`[bluetooth]#``pairable on `

Scan for devices:

`[bluetooth]#``scan on`

Put the device into pairing mode. This generally involves pressing a button or a combinations of buttons, usually for several seconds.

Discover the device MAC address:

`[bluetooth]#``devices`

Pair with the device:

`[bluetooth]#``pair `*`device_mac_address`*

Enter the [PIN] if prompted:

`[agent]``PIN code: ####`

In case the pin is not prompted but needed, this command may need to be added before pairing with the device (see [this post](https://stackoverflow.com/questions/34709583/bluetoothctl-set-passkey)):

`[bluetooth]#``agent NoInputNoOutput`

Allow the service authorization if requested:

`[agent]``Authorize service `*`service_uuid`*` (yes/no): yes`

Trust the device:

`[bluetooth]#``trust `*`device_mac_address`*

Connect to the device:

`[bluetooth]#``connect `*`device_mac_address`*

Display information about the device:

`[bluetooth]#``info `*`device_mac_address`*

The device is now paired:

`[bluetooth]#``quit`

### [[] hciconfig]

** Warning**\
[hciconfig] is deprecated, and [bluetoothctl], [described above](#Device_pairing), should be used instead. [hciconfig] and other utilities are only available if [[[net-wireless/bluez]](https://packages.gentoo.org/packages/net-wireless/bluez)[]] is installed with the `deprecated` USE flag enabled.

For information on [hciconfig] usage, refer to the [Bluetooth/hciconfig](https://wiki.gentoo.org/wiki/Bluetooth/hciconfig "Bluetooth/hciconfig") page.

## [[] Wake from suspend]

To enable Bluetooth devices to wake the system from suspend, the USB device corresponding to the controller first needs to be configured to allow triggering wakeup. This can be done with a [udev](https://wiki.gentoo.org/wiki/Udev "Udev") rule.

To configure this for a specific controller, first find the `idVendor` and `idProduct` pair. Get the USB device syspath hosting the Bluetooth interface:

`user `[`$`]`find /sys/bus/usb/devices/*/* -mindepth 1 -maxdepth 1 -name bluetooth | xargs dirname | xargs dirname`

    /sys/bus/usb/devices/3-10

This will produce multiple paths if multiple Bluetooth controllers are present. Details of each device can be viewed with `udevadm info /sys/bus/usb/devices/3-10`.

Get the current state and the ID pair:

`user `[`$`]`cat /sys/bus/usb/devices/3-10/}`

    disabled  # The current value of the power/wakeup attribute
    8087      # idVendor
    0026      # idProduct

Then create the following udev rule, replacing the `idVendor` and `idProduct` values with those from above.

[FILE] **`/etc/udev/rules.d/10-bluetooth-wake.rules`**

    SUBSYSTEM=="usb", ATTRS=="8087", ATTRS=="0026", ACTION=="add", ATTR="enabled"

Conversely, a udev rule can be created to match and configure all Bluetooth controller devices:

[FILE] **`/etc/udev/rules.d/10-bluetooth-wake.rules`**

    SUBSYSTEM=="usb", ATTR=="e0", ATTR=="01", ACTION=="add", ATTR="enabled"

Test that the new rule applies to the USB device:

`user `[`$`]`udevadm test /sys/bus/usb/devices/3-10 2>&1 | grep wakeup`

    3-10: /etc/udev/rules.d/10-bluetooth-wake.rules:2 Running in test mode, skipping writing ATTR="enabled".

If successful, trigger the new udev rules:

`root `[`#`]`udevadm trigger --action=add --sysname-match 3-10`

Each paired Bluetooth device which should be allowed to trigger wake needs to be configured so:

`user `[`$`]`bluetoothctl wake 90:9C:4A:02:F1:C0 on`

For testing on systemd systems, `systemctl suspend` will trigger an immediate suspend. The Bluetooth device should then trigger the system to wake up.

## [[] Disable Bluetooth]

To disable Bluetooth at runtime, run the following command:

`root `[`#`]`rfkill block bluetooth`

To disable Bluetooth automatically on every boot, choose one of the following options:

### [[] Using udev to disable Bluetooth]

When using UDEV, just install the following rule which will disable Bluetooth:

[FILE] **`/etc/udev/rules.d/80-disable-bluetooth.rules`**

    SUBSYSTEM=="rfkill", ATTR=="bluetooth", ATTR="0"

### [[] Using OpenRC to disable Bluetooth]

When using [[[sys-apps/openrc]](https://packages.gentoo.org/packages/sys-apps/openrc)[]], install the following script for *local* service and ensure it is executable:

[FILE] **`/etc/local.d/disable-bluetooth.start`**

    #!/bin/sh
    rfkill block bluetooth

`root `[`#`]`chmod o+x /etc/local.d/disable-bluetooth.start`

### [[] Disable Bluetooth at kernel level]

When the kernel has modular Bluetooth support, disable loading of Bluetooth modules:

[FILE] **`/etc/modprobe.d/blacklist-bluetooth.conf`**

    blacklist bnep
    blacklist bluetooth
    blacklist btusb

## [[] Utilities]

[btmon], provided by [[[net-wireless/bluez]](https://packages.gentoo.org/packages/net-wireless/bluez)[]], provides access to the Bluetooth subsystem monitor infrastructure for reading HCI traces. Refer to the output of `btmon --help` for usage details.

The [[[net-wireless/bluez-tools]](https://packages.gentoo.org/packages/net-wireless/bluez-tools)[]] package provides a number of utilities, including [[[bt-obex(1)]](https://man.archlinux.org/man/bt-obex.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")], for Bluetooth file transfers, and [[[bt-network(1)]](https://man.archlinux.org/man/bt-network.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")], a Bluetooth network manager.

## [[] Troubleshooting]

### [[] TLP and laptop_mode]

If [laptop-mode-tools](https://wiki.gentoo.org/wiki/Power_management/Guide "Power management/Guide") is installed or TLP make sure they\'re not disabling Bluetooth to save power.

### [[] XBOX ONE controller pairing]

It\'s a known issue that XBOX ONE wireless controllers will refuse to pair out of the box on most linux systems. To solve this issue ERTM needs to be disabled.

To disable it manually:

`root `[`#`]`echo 'Y' > /sys/module/bluetooth/parameters/disable_ertm`

This will disable ERTM only until the system is rebooted. To disable it permanently, install the xpadneo kernel module.

`root `[`#`]`emerge --ask games-util/xpadneo`

In most cases, this will automatically solve the issue. If it doesn\'t, add this line into xpadneo config manually:

[FILE] **`/etc/modprobe.d/xpadneo.conf`**

    options bluetooth disable_ertm=Y

### [[] Notebook has a Synopsys DesignWare Controller]

Bluetooth support for this controller needs also these options in kernel config^[\[4\]](#cite_note-4)^:

[KERNEL]

    Device Drivers  --->
        Character devices  --->
            Serial drivers  --->
                [*] 8250/16550 and compatible serial support
                [*] Support for Synopsys DesignWare 8250 quirks

### [Resolving firmware problems]

It happens that the firmware of bluetooth adapters enters a state where it is unable to pair with a certain (or all) bluetooth devices. Resetting the adapter might solve such problems.

In the case of a laptop with a built-in bluetooth adapter this might be achieved by:

-   Enter the laptop\'s firmware settings (BIOS) and disable the built-in adapter
-   Save settings and restart the laptop
-   Enter the firmware settings a second time and enable the bluetooth adapter again
-   Save and restart
-   Now try to pair the device again

## [[] See also]

-   [Bluetooth headset](https://wiki.gentoo.org/wiki/Bluetooth_headset "Bluetooth headset") --- describes the configuration of Bluetooth [headsets](https://en.wikipedia.org/wiki/Headset_(audio) "wikipedia:Headset (audio)") within Gentoo Linux.
-   [Bluetooth input devices](https://wiki.gentoo.org/wiki/Bluetooth_input_devices "Bluetooth input devices") --- describes the setup of [Bluetooth] input devices, for example a bluetooth mouse, on a Linux system.
-   [Bluetooth Network Aggregation Point](https://wiki.gentoo.org/wiki/Bluetooth_Network_Aggregation_Point "Bluetooth Network Aggregation Point") --- covers the setup of a Bluetooth Network Aggregation Point (NAP) on Gentoo Linux.
-   [Broadcom Bluetooth](https://wiki.gentoo.org/wiki/Broadcom_Bluetooth "Broadcom Bluetooth") --- details setup for Broadcom Bluetooth 4.x devices mostly based on BCM20702, BCM4354, and BCM4356 chipsets.

## [[] References]

1.  [[[↑](#cite_ref-1)] [[Gentoo Forums thread](https://forums.gentoo.org/viewtopic-t-1169502-highlight-.html)]]
2.  [[[↑](#cite_ref-2)] [[https://github.com/bluez/bluez/issues/236](https://github.com/bluez/bluez/issues/236)]]
3.  [[[↑](#cite_ref-3)] [[https://github.com/bluez/bluez/blob/c24f0b487ca3d4e0ca315114a889dad4d2c3bb26/doc/org.bluez.Battery.rst](https://github.com/bluez/bluez/blob/c24f0b487ca3d4e0ca315114a889dad4d2c3bb26/doc/org.bluez.Battery.rst)]]
4.  [[[↑](#cite_ref-4)] [[Gentoo Forums thread](https://forums.gentoo.org/viewtopic-t-1161073.html)]]