# Bluetooth mouse

This article describes configuration & troubleshooting steps specific to Bluetooth mice. The information here builds on the main Bluetooth article, and assumes the user has already followed any installation, configuration, or troubleshooting from that article.

## Configuration
## Apple Magic Mouse scroll speed
If the scroll speed is too slow, you can try

 # modprobe -r hid_magicmouse
 # modprobe hid_magicmouse scroll_acceleration=1 scroll_speed=55

Scroll speed can be set from 0 to 63.

If the speed suits you, you can make the change permanent in

## Apple Magic Mouse middle click
If you find the middle click to be too finicky, you can disable it

 # modprobe -r hid_magicmouse
 # modprobe hid_magicmouse emulate_3button=0

If this setting suits you, you can make the change permanent in

## Mouse pairing and dual boot
When dual booting Windows and Linux, you may find yourself having to re-pair your Bluetooth mouse again and again. This will happen every time you switch OS, because when you pair your device, your Bluetooth service generates a unique set of pairing keys. And the core reason is that the set of pairing keys cannot be shared between the two OS.

First, your computer stores the Bluetooth device's mac address and pairing key. Second, your Bluetooth device stores your computer's mac address and the matching key. This usually works fine, but the mac address for your Bluetooth port will be the same on both Linux and Windows (it is set on the hardware level). However, when you re-pair the device in Windows or Linux, it generates a new key. That key overwrites the previously stored key on the Bluetooth device. Windows overwrites the Linux key and vice versa.

To fix the problem, see Bluetooth#Dual boot pairing.

if using a Bluetooth LE device use this python script, slightly edited to adapt for arch, originally discussed on == Troubleshooting ==

## Mouse lag
If you experience mouse lag you can try to increase the polling rate. See Mouse polling rate for more information.

You can try to set the minimum/maximum latency for the mouse in BlueZ [https://bbs.archlinux.org/viewtopic.php?pid=1860951#p1860951:

Add or modify the following section in  (adapt the path accordingly):

 MinInterval=6
 MaxInterval=9
 Latency=44
 Timeout=216

Also, you can use  (in ) to change latency parameters of the device:

 # HANDLE="$(hcitool con | grep '' | awk '{print $5}')"  # get the device handle
 # hcitool lecup --handle $HANDLE --latency 0 --min 6 --max 8

Note that this method is only effective for the current connection. If the mouse gets disconnected, you will need to execute again.

Alternatively, you can change the default latency settings via debugfs. See {{ic|/sys/kernel/debug/bluetooth/hci0/conn_{latency,{min,max}_interval} }}.

This example will solve the lag problems, but you must un pair and pair the mouse:

 # echo 0 > /sys/kernel/debug/bluetooth/hci0/conn_latency
 # echo 6 > /sys/kernel/debug/bluetooth/hci0/conn_min_interval
 # echo 7 > /sys/kernel/debug/bluetooth/hci0/conn_max_interval

## Problems with the USB dongle
If you have trouble with your USB dongle, you may also want to try:

 # modprobe -v rfcomm

At this point, you should get an hci0 device with:

 # hcitool dev

Sometimes the device is not active right away. Try starting the interface with:

 # hciconfig hci0 up

and searching for devices as shown above.

## Mouse always disconnects
If the mouse stops working but works again after restarting bluetooth, or the mouse seemingly keeps "falling asleep" after a couple of seconds of inactivity (which is the case for at least some models of Dell XPS 13 [https://web.archive.org/web/20220118101210/https://fueledonbacon.com/popos-bluetooth-autosuspend-problem/), you may need to disable USB autosuspend for the selected device.

The issue may also lie in the device timeout and HID settings. See #Thinkpad Bluetooth Laser Mouse problems.

If you are using a Logitech device, this issue may be resolved by following the procedure in #Problems with the Logitech BLE mouse (M557, M590, M720, anywhere mouse 2, etc).

## Thinkpad Bluetooth Laser Mouse problems
If you are experiencing that your Thinkpad Bluetooth Laser Mouse rapidly connects and then (after a few milliseconds) disconnects again every few seconds (when you move the mouse or press a button), try pairing it with the code  instead pairing without a code.

If the above is unhelpful, the issue may be in the device timeout settings. Edit/create the file  and apply the following changes:

 # Configuration file for the input service

 # This section contains options which are not specific to any
 # particular interface
 # Set idle timeout (in seconds) before the connection will be disconnect and
 # the input device is removed.
 # Defaults: 0 (disabled)
 IdleTimeout=0

 # Enable HID protocol handling in userspace input profile
 # Defaults to true (Use UHID instead of kernel HIDP)
 UserspaceHID=true

These changes will prevent device timeout in order to remain connected. The second setting enables userspace HID handling for Bluetooth devices. However, both should be set this way by default. Restart  to test changes. You also may need a reboot and to re-pair the device.

## Kensington Expert Wireless Trackball problems
The Kensington Expert Wireless Trackball has default polling rates in the 200ms range, which make it laggy. To fix that, add or modify the  section in  (adapt the path according to your mouse bluetooth address) as shown above, especially lower the latency to a small number or even .

## Problems with the Logitech BLE mouse (M557, M590, M720, anywhere mouse 2, etc)
In some case, the mouse is paired but not moving when used. The device add to be trusted and unblocked.
First of all open a terminal and run

# Power off the bluetooth:
# Power on the bluetooth, then enable the pairing method on the mouse if needed:
# List the available bluetooth devices, you have to copy the mouse device ID XX:XX:XX:XX:XX:XX:
# Unpair the device if already paired:
# Put device in pairing mode (typically by long pressing a button). It will be detected by scan and displayed. Mind that the device ID may have changed (slightly), so copy the device ID shown by the scan.
# Trust the device:
# Pair the mouse with the computer:
# Connect the computer with the mouse:
# Unblock the device control:
# Power the bluetooth off and on.

If the mouse does not work directly, just power off and power on the mouse.

In some cases, it may also be necessary to load the  kernel module.
