# Mouse polling rate

If you have invested in a high resolution mouse, adjusting the USB polling rate is a common trick to utilize the added precision it brings. The polling rate (or report rate) determines how often the mouse sends information to your computer.

## Polling rate and polling interval
The polling rate of a device is measured in Hertz (Hz) and is determined by the polling interval. The polling interval is measured in milliseconds (ms) or microseconds and equates to lag time.

The default polling interval is 10ms. However, USB controllers round the interval down to the nearest power of two. Thus, an interval setting of 10ms will actually use 8ms, 7ms will use 4ms, etc.

If the polling rate is 125 Hz, the mouse position will be updated every 8 milliseconds. In situations where lag is critical — for example games — some users decrease the interval to as little as possible. However, this puts more load on the CPU, so care should be taken when adjusting this value.

For the USB 2.0 High Speed and USB 3.0+ devices are able to poll in intervals smaller that 1 millisecond - in such case kernel will report polling interval in microseconds.

The following table shows the relation between polling rate Hertz and the corresponding interval milliseconds (rate = 1000 / interval) and microseconds (rate = 1000000 / interval):

{| class="wikitable"
! Hz
|8000||4000||2000||1000||500||250||125
|-
! ms
|0.125||0.25||0.5||1||2||4||8
|-
! us
|125||250||500||1000||2000||4000||8000
|}

## Measure polling rate
## Measure polling rate via libinput
In case  is used on the host, one can use the  while running as root or otherwise having access to the  pseudo file system, and observe that events happen periodically. For example, for a 500 Hz mouse polling rate one can see maximum difference between two consecutive events being  seconds, for 1000 Hz updates each millisecond (so  seconds), and for the polling rates higher, the reported events may occur at the same millisecond.

 # libinput debug-events

For 500 Hz:

 event22  POINTER_MOTION          +10.918s	  1.22/  1.22 ( +1.00/ +1.00)
 event22  POINTER_MOTION          +10.920s	  0.00/  1.22 ( +0.00/ +1.00)
 event22  POINTER_MOTION          +10.922s	  0.00/  1.12 ( +0.00/ +1.00)
 event22  POINTER_MOTION          +10.924s	  1.25/  1.25 ( +1.00/ +1.00)

For 1000 Hz:

 event18  POINTER_MOTION          +0.235s	 -1.87/ -1.87 ( -1.00/ -1.00)
 event18  POINTER_MOTION          +0.236s	 -1.87/  0.00 ( -1.00/ +0.00)
 event18  POINTER_MOTION          +0.237s	 -1.66/  0.00 ( -1.00/ +0.00)
 event18  POINTER_MOTION          +0.238s	 -1.66/  0.00 ( -1.00/ +0.00)

For 2000 Hz:

 event22  POINTER_MOTION          +14.114s	 -2.00/  0.00 ( -1.00/ +0.00)
 event22  POINTER_MOTION          +14.114s	 -2.00/  0.00 ( -1.00/ +0.00)
 event22  POINTER_MOTION          +14.115s	  0.00/ -2.00 ( +0.00/ -1.00)
 event22  POINTER_MOTION          +14.115s	 -2.00/  0.00 ( -1.00/ +0.00)

## Measure polling rate via evhz
The  tool can display the actual mouse refresh rate.

You can install it from  and execute as root:

 # evhz

Now move the mouse continuously in large circles until the displayed  stabilizes then press  to exit.

If the  value does not stabilize and switches between two values, then the attempted polling rate is faster than the device is capable of; see #USB device speed.

## Measure polling rate via Wine+DirectX
Alternatively, Windows tools such as DirectX mouserate checker can be run using Wine. Or use a website based checker like the one provided by CPS-Check.

## Display polling interval
Device information including polling interval can be found in debugfs if it is mounted and you have root access.

First, find the vendor and product IDs of your device with:

Then run the following as root with those IDs to display the debug information for that device:

The  is the polling interval; this device has requested 10ms (and actually reports every 8ms as explained in #Polling rate and polling interval). The  is the device speed explained in #USB device speed. For information about the other fields, see the kernel documentation.

If debugfs or root access are not available, the polling interval can be shown with:

## USB device speed
USB devices are designed to operate at a certain bitrate. Many pointing devices are "Low Speed" 1.5Mbit/s devices. The speed of a device can be shown as explained in #Display polling interval.

"Low Speed" devices may not be capable of polling at intervals less than 8ms.

All USB hubs should be capable of at least "Full Speed" 12Mbit/s. The speed of the hub that the device is attached to can be shown with the following command with the same  as the device:

The  of the hub is independent of the device and does not affect the polling rate of the device.

## Set polling interval
To configure the polling rate, use the  option of the  kernel module. The default value is 0 which means the module uses the interval requested by the device(s).

The current value of the option can be verified with:

To change the configuration, add the following kernel module parameter:

 options usbhid mousepoll=4

This example requests a polling rate of 250Hz. Similarly, you may use jspoll or kbpoll to change the polling rate of gamepads/joysticks or keyboards.

To change the polling interval without rebooting:

 # modprobe -r usbhid && modprobe usbhid mousepoll=4

You may have to unplug the mouse and plug it back in for the change to take effect.

## Known issues
## Polling at half of requested rate
There is a kernel bug that for certain configurations prevents devices from reaching 1000 Hz (1ms) polling rate. See the BBS and Bug.

A work-around that may help is to connect the device to a port using a different driver.

## Polling rate not changing
The USB 3 driver  may be ignoring the   setting. See the linux-usb mailing list message and Bug.

The  module should respect the interval requested by the device, so check the documentation for the device for a hardware or firmware setting.

A work-around that may help is to connect the device to a port using a different driver.

Another work-around is to disable xHCI. There might be a BIOS setting for this or you can do so by blacklisting the  module. However, either way will cause any USB 3 ports to act as USB 2 as the kernel will use the  module instead.

As an alternative, one can install a kernel module . The module identifies a mouse with its vendor and product ID (VID:PID) values to overclock it even with XHCI hubs, without losing USB 3 functionality. The polling rate of the usb_oc module can be configured with a runtime option e.g. a .conf file in :

 options usb_oc interrupt_interval_override=045e:0040:2

The example above would set an interval of 2ms, or 500Hz, for the device with VID:PID of 045e:0040. More information is available in the project's README.

## Polling rate resulting in lag with wine
Having a mouse with a high poll rate has been reported to cause lag in older versions of Wine; see Wine bug 46976. In January 2026, the bug was closed as having been fixed in Wine version 11.0-rc5. This issue should be able to be fixed by updating Wine, adjusting your mouse's polling rate with the mentions described previously, or using a mouse with a lower polling rate. Note that it is not possible to change the polling rate of the mouse using the methods within this wiki (the "usbhid" method) if your computer only has a USB3 xHCI Controller.

## Polling rates higher than 1000 Hz
Make sure the device is connected to a USB slot supporting at least USB 2.0 High Speed. Polling rates higher than 1 kHz are only supported starting with USB 2.0 High Speed. This will allow the device "to be polled" at a higher rate.

Note that the device itself also needs to support the High Speed to begin with: if this mode cannot be negotiated, then higher polling rates cannot be used either. Many devices operate in the slower Full Speed mode known from USB 1.1, sometimes despite using USB 2.0 protocol themselves. This can be checked with the command  and looking at the top of the output for Negotiated speed.

## Logitech mice with onboard memory
Certain Logitech mice can store the polling rate among other parameters in their built-in onboard memory. If onboard memory is enabled, it can be configured with . This may not work if onboard memory has been disabled. The Logitech G HUB software for Windows and MacOS tends to disable onboard memory to allow for more advanced customisations handled by the software itself. If the onboard memory is disabled, the mouse will default to a 125 Hz polling rate and ignore the   setting.
