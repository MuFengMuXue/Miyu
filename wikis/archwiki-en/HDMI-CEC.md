# HDMI-CEC

High-Definition Multimedia Interface - Consumer Electronics Control is an additional low-speed (50 B/s) bus in the HDMI connection that a "network" of HDMI devices can use to communicate with each other. It allows HDMI devices to notify each other that they should be turning on or off, that the TV has switched input or that a remote control button is being pressed, among other things. In PC setups it is usually encountered in an HTPC (home-theater PC) setup.

For a variety of reasons almost no PC GPU has hardware support for CEC. Video game consoles and set-top boxes usually have to include an external chipset to drive the CEC pin. While there are devices with native CEC support (such as the VideoCore GPU found on a Raspberry Pi), most hardware configurations need additional hardware.

## Features
The main purpose of CEC is to grant a television insight and control over the state of the devices plugged into it. As such, it is split into a dozen of "features" that each target specific use cases, and which devices can opt to support or not based on their role as initiator/follower, their capabilities, as well as user configuration.

The standardized features are:

;One Touch Play: Lets a device signal that it wishes to immediately become the active source, which can automatically turn on the TV
;Routing Control: Allows the TV to control HDMI switches and lets devices check what source is currently active
;Remote Control Passthrough: Lets devices send remote control signals to each other, usually from the TV to the active source
;Deck Control: To control a movie/music player and query its playback status
;Standby/System Standby: Lets a device request that another specific device be turned off, or broadcast that all devices on the system should now turn off.
;Power Status: Lets devices be probed to see if they are in standby mode or turned on, or if they are in the process of turning on.
;System Audio Control: Grants control of an AV receiver connected over the TV's Audio Return Channel, allowing the volume to be changed and the receiver to be turned on or off.
;Tuner Control: Lets any device step through the list of TV channels known to a tuner device and query information on the active channel, like the channel number for analog TV or DVB/ATSC/ARIB transport stream information for digital TV
;One Touch Record: Enables a recorder to query what channel the TV is currently showing so that said recorder can tune to the same channel and begin recording, or know that it should record itself or a downstream device if it already is the currently active HDMI source
;Timer Programming: Allows a TV to configure a timer on a recorder to start recording a given source at a specific time
;OSD display: Allows a device to print a message on the TV, between 1 and 13 ASCII characters long
;Dynamic Auto Lipsync: Allows a TV to broadcast changes in presentation latency to the audio sink, which a source that has its own speakers (like a PC) can use for latency compensation with the image

For a device like a PC, the most useful one among these is going to be Remote Control Passthrough. System Standby may be useful for HTPCs, but would be of questionable use on more general-purpose machines, which are not usually expected to go to sleep when the screen turns off. Routing Control could be used to wake up the system when the TV attempts to display that input, provided the connected PC has a way to listen to CEC traffic while suspended. System Audio Control would be convenient for some HDMI sound outputs, but does not currently work as a mean of volume control with either PipeWire or PulseAudio.

## Hardware setup
The Linux Kernel already has a built-in subsystem to automatically respond to queries and handle CEC events, but the hardware may need to be configured first in order to work.

## Native CEC
Native CEC is mostly encountered in ARM devices. In x86 world the easiest option is tunneling over DisplayPort, otherwise only some Chrome OS devices and SECO UDOO single-board computers offer CEC.

## Tunneling over DisplayPort
The DisplayPort 1.3 standard (introduced in 2014) allows DisplayPort-to-HDMI adapters to use the auxiliary channel to forward CEC signals both ways. This is the sort of feature that adapters do not usually support unless mentioned, and is not commonly found, but it can counter-intuitively be cheaper and easier to use CEC tunneling over DisplayPort than a USB-CEC adapter. The kernel documentation page for the CEC submodule has a list of adapters which have been confirmed to work.

The list is not exhaustive, however, and it is often more useful to know the name of the chipset being used by the adapter than the model of the adapter itself. For instance, the Framework HDMI module card is not explicitly advertised as supporting HDMI-CEC, but the Parade PS186 chipset inside of it does, and the card itself is detected by cec-ctl and works as expected. On the other hand, the Synaptics "Spyder" VMM7100 which is used by several DisplayPort-to-HDMI-2.1 adapters like the Club3D CAC-1088, only does signal processing and seemingly does not support CEC-over-AUX. This is unlike the Club3D CAC-1080, a very similar HDMI 2.0 adapter based on the Megachips MCDP2900 chipset, which *does* support CEC.

## CEC adapter
## PulseEight USB adapter
The PulseEight USB-CEC adapter works by passively extending all the pins of the HDMI connector on from the "PC side" connector to the "TV side" connector, save for the CEC pin, which is intercepted. The data going through that pin is instead exposed over a USB serial interface to let a PC control and monitor CEC traffic. The serial device needs to have its line discipline (a flag to signal to the kernel that a TTY is of a specific known type and requires a driver to work) configured manually before the kernel takes over and acknowledges it as a CEC adapter. This cannot be done automatically due to limitations around serial device APIs, so it is currently best achieved with a udev rule paired with a systemd unit (as udev rules cannot launch long-running or forking processes) to run  when the device is plugged.

This serial interface appears as device node , and the inputattach utility is needed to set the line discipline and let the kernel drivers take over to create the  device that will be needed later. This requires the  package.

{{Note|{{ic|ATTRS{product} }}'s value must match the  field and {{ic|ATTRS{manufacturer} }}'s value must match the  field  in  output for the Pulse-Eight Adapter's device otherwise the rule below will never trigger. For some adapters the  field is not  but . }}

{{hc|/etc/udev/rules.d/pulse8-cec-autoattach.rules|2=
SUBSYSTEM=="tty" ACTION=="add" ATTRS{manufacturer}=="Pulse-Eight" ATTRS{product}=="CEC Adapter" TAG+="systemd" ENV{SYSTEMD_WANTS}="pulse8-cec-attach@$devnode.service"
}}

However, USB device connections are usually reset when the system wakes up from sleep (a step known as reset-resume) , meaning the serial connection will be lost if the computer is ever suspended, on top of serial connections usually hanging up on resume anyway. This means the above rule has to be triggered again somehow.

Unfortunately, the  driver in charge of the  object that the above rule reacts to does not raise any uevent about the connection being reset and the line discipline being lost, and the rule cannot be hooked on the USB device directly. Instead, the most reliable way to get the used rule above to trigger again at the right time is to delete and recreate the  object by forcing the USB device to be reconfigured when it resets.

{{hc|/etc/udev/rules.d/pulse8-cec-autoattach.rules|2=
# Make sure that power/persist is and stays off,
# in case CONFIG_USB_DEFAULT_PERSIST enables it by default
SUBSYSTEM=="usb" ATTR{manufacturer}=="Pulse-Eight" ATTR{product}=="CEC Adapter" ATTR{power/persist}="0"

SUBSYSTEM=="tty" ACTION=="add" ATTRS{manufacturer}=="Pulse-Eight" ATTRS{product}=="CEC Adapter" TAG+="systemd" ENV{SYSTEMD_WANTS}="pulse8-cec-attach@$devnode.service"

# Force device to be reconfigured when reset after suspend, otherwise the ttyACM link is lost but udev will not notice.
# A usb_dev_uevent with DEVNUM=000 is a sign that the device is being reset before enumeration.
# Re-configuring causes ttyACM to be removed and re-added instead.
SUBSYSTEM=="usb" ACTION=="change" ATTR{manufacturer}=="Pulse-Eight" ATTR{product}=="CEC Adapter" ENV{DEVNUM}=="000" ATTR{bConfigurationValue}=="1" ATTR{bConfigurationValue}="1"
}}

This essentially acts as if the USB adapter had been unplugged and re-plugged immediately upon coming out of sleep, ensuring the  rule from before gets to run again. This ensures that the systemd service will be restarted as soon as the device is back to a usable state.

## Software setup
Now that the CEC subsystem has something to bind on and that  has been created, it is now possible to configure the PC so other CEC devices know about it. When using the command-line, CEC devices are normally controlled via , which is part of .

## Informing a USB adapter of its physical address
One thing to be aware of is that the CEC pin alone does not have enough information on its own to send a valid CEC message. A CEC adapter that only monitors pin 13 (CEC) cannot know its "physical address", which is a 16 bit value representing its position in the "tree" of HDMI devices in terms of port number.

The adapter needs to be aware of this physical address in order to complete the logical address allocation procedure, which is detailed in the next section. The physical address is communicated over pin 16 (DDC/EDID), so configuring the CEC subsystem includes specifying which display output port is supposed to be associated with that CEC object, in order for the physical address to be extracted from the display's EDID.

One way to find the name of the active connectors is to use  (which also works on Wayland):

Once the correct port has been identified (for example ), then the sysfs port name can be found by using  (such as ). In this case, the corresponding display's EDID data would be kept at .

The physical address can be previewed like this:

Given how CEC configuration must be performed every time the  device node is re-created, this is best handled with another udev rule that fires when the  object appears.

{{hc|/etc/udev/rules.d/cec-configure-autostart.rules|2=
SUBSYSTEM=="cec" KERNEL=="cec0" ACTION=="add" TAG+="systemd" ENV{SYSTEMD_WANTS}="cec0-configure@card1-HDMI-A-1.service"
}}

See the next section for more details.

## Obtaining a logical address
Because the bandwidth is so limited, instead of a 16 bit physical address, the CEC protocol uses a shorter 4 bit logical address to mark the origin and destination of each message.  Without a logical address, a device can only receive and send broadcast messages. This identifies devices as "Tuner #3" or "Playback Device #1", with a finite number of each. These roles are intended to relate to the CEC features mentioned earlier, namely:

;Tuner (4 max): Should support the "Tuner Control" feature.
;Recorder (2 max): Only type that can use "One Touch Record"; TVs are supposed to ignore related messages coming from other addresses
;Playback device (3 max): General purpose video source. Computers and video game consoles are considered "Playback devices"
;Backup (2 max): Can be used if address allocation fails because too many devices of one type are present

The remaining 4 addresses are reserved for the TV itself, the Audio System, a vague "Specific use device" (possibly a second TV) and the default broadcast/unregistered address. HDMI switches are "transparent" and don't have their own addresses.

Unlike the last times, the required call to cec-ctl is short-lived enough to work directly as part of a udev rule. If you have already created a systemd unit for physical address configuration earlier, this rule would be redundant and can be ignored.

The above udev rule (and previous systemd unit) uses  to configure a Playback device. It is, however, generally OK to set the device class to Tuner () or Recorder (), whether because there are no more unused playback addresses, or simply to have the PC stand out in the list on TVs that visually set apart each device class in their input menus. The rule also uses   to configure the advertised source name to be used in TV menus. As the example name implies, it is limited to 14 ASCII characters only.

## Input-handling daemons
*
*

## Userspace tools
User access to  devices can be granted by enrolling users into the  user group. The basic tool for controlling CEC devices is  from . A similar one is  from , for which there are also Python bindings available in .

## Uses for CEC
## Remote control pass through
With the  object now configured, the Linux CEC subsystem should also have created a matching object in , which acts as an input device that converts UI Command Code signals into the equivalent keypresses.

* The "Power" signal, which is not usually on the remote itself but can be sent via menus, is mapped by default to bring up the "Close session" confirmation screen in KDE, and to immediately suspend the system in GNOME, just like the suspend button on a keyboard.
** For waking up afterwards, see #Wake-on-CEC
* The arrow buttons are mapped to the arrow navigation keys and will work everywhere.
* The "Back" and "Select" navigation buttons are not mapped to the "Escape" and "Enter" keys, but to the "OK" and "EXIT" media buttons, which are only recognized by some media players.
* "Play", "Pause" and "Stop" work the same as media keys and are recognized everywhere, possibly even when the player is not focused depending on DE configuration.
** "Rewind", "Fast-forward", "Next track" and "Previous track" are usually ignored, but VLC and Totem acknowledge them
* "Dot" in the number buttons cluster is recognized as the numpad "." key
* Various other keys like "Menu", "Setup", "Audio" and "Record" do nothing by default but can be assigned as valid keyboard shortcuts by most applications.
* The 4 coloured function buttons, the number buttons and the channel +/- buttons, among others, are not picked up as keyboard or media keys by applications, though the evdev key events they raise could still be used by applications that specifically check for them.
* Volume control is usually intercepted by the TV instead of passed on to the source, but is handled as normal volume keys in cases where it is passed through.

## Wake-on-CEC
HDMI devices are usually notified by the television when they become the active source, using the Routing Control feature. This can be used to wake up suspended devices, although this runs into a problem when it comes to computers. Since CEC support is achieved through the Linux kernel or a userspace library, and not handled by the motherboard itself, there is nothing listening to CEC traffic while the computer is suspended.

One of the benefits of the Pulse-Eight adapter, compared to DisplayPort-to-HDMI adapters, is that it can remain powered and active even while its host system is in standby. Once it has been informed of its physical and logical address, if it detects that its USB host is gone, it will continue to operate in "autonomous mode" so long as it remains powered. While in this state, it will keep doing the following:

* Reply to system information inquiries (on-screen name, logical address, current power status, etc.)
* Respond to any "Power" remote signals or  messages with itself as the destination by sending a power switch event to the PC to wake it up

The Pulse-Eight USB adapter can do that because it registers as a USB keyboard alongside its serial interface. DisplayPort-to-HDMI adapters (including USB-C adapters which use the DisplayPort alt mode) do not have this kind of side-channel, and as a result cannot wake the host like this.

Devices with native CEC support, like the Raspberry Pi, don't usually have a suspend mode. While the Pi itself can be powered down, it will not listen to the CEC pin while in this state, and requires external circuitry to be powered on in this way.

## CEC traffic monitoring
An interesting thing that can be done with a device that supports CEC is to just tap the CEC line to see what other devices are saying. Since the CEC line is physically interconnected between all devices (even those that do not support CEC), all messages sent by any device are visible by all other devices, no matter their position. In order to log these messages with , all that is needed is to run the following:

 # cec-ctl -d0 --monitor-all --ignore=all,poll

One specific message that can usually be left out is the polling message. The logical address allocation procedure doesn't define any mean of releasing said addresses, so the expected way of verifying whether an address has become available is to periodically poll it by sending a message with a source and destination address, but no payload, similar to how ping works. If the message is not acknowledged, then it is understood that the device at this logical address "no longer needs/uses it", and will be assumed to no longer exist. Most televisions will therefore poll their downstream devices rather frequently to check their status, and using  (to ignore all poll messages regardless of provenance) or  (to only ignore poll messages from the TV) can help reduce noise in the logs.
