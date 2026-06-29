# Gobi Broadband Modems

From Wikipedia:
: Qualcomm Gobi is a family of embedded mobile broadband modem products by Qualcomm.

## Device identification
Install  and then examine the output of

 $ lsusb

which will show the vendor and product IDs of the device.

For example, on a HP un2430 modem:

 Bus 001 Device 005: ID 03f0:371d Hewlett-Packard

The device is detected by the qcserial module, if not, you are going to have to recompile the qcserial module with your added product and vendor id.

Alternatively you can add the Product and Vendor ID by writing them into the  file (best both at the same time because most Gobi modules switch the Product ID when the Firmware is loaded).
For example on a Gobi2K with the Vendor ID  and the Product IDs  (waiting for Firmware) and  (firmware loaded)

 # echo "04da 250e" > /sys/bus/usb-serial/drivers/qcserial/new_id
 # echo "04da 250f" > /sys/bus/usb-serial/drivers/qcserial/new_id

note that this has to be repeated when you reload the qcserial module or reboot/shutdown.

## gobi_loader
From the developer GitHub page:
: gobi_loader is a firmware loader for Qualcomm Gobi USB chipsets. These devices appear in an uninitialized state when power is applied and require firmware to be loaded before they can be used as modems. gobi_loader adds a udev rule that will trigger loading of the firmware and make the modem usable.

Install  and .

After installation, you should enter your product and vendor id in the

Then a simple reload of the qcserial module:

 # rmmod qcserial
 # modprobe qcserial

## Manage Connection in Network Manager
ModemManager is required for network manager to detect any mobile broadband devices.

This needs to be started/enabled. As soon as they are started the Mobile Broadband option will be available from the Network Manager Applet.

Make sure  and  are installed.

To use this quite old modem, you need to blacklist qmi_wwan and cdc_wdm modules from loading into Linux kernel. Else, if these modules are loaded, ModemManager recognizes this modem as something new with QMI interface, and then complains about too small versions of some QMI services. [https://gitlab.freedesktop.org/mobile-broadband/ModemManager/issues/69 Source

## Connection
## wvdial
See main article: wvdial

The general procedure is to switch the device into modem mode, make sure the  device(s) are recognized by the qcserial kernel module, and then to run wvdial to dial, connect and start pppd.

Install . The configuration file  will in general depend on which device you have and which mobile network you are connecting to. A single  can be defined with named sections to be usable with several USB modems and networks, should you need them.

Run:

 # wvdialconf

which will attempt to write  correctly. You will need to add the user, password and Access Point Name (APN). You can obtain these from your network provider, from other users via published , or by logging the USB tty traffic under another operating system (e.g. Sysinternals' Portmon).

An example of  looks like this:

To simplify the procedure, one can take the SIM card out and disable the PIN so  is not needed before connecting to the internet.

Often there will be several devices (at , ,  for example). If in doubt about which to use, try each of them in turn. Once the configuration files are prepared, the internet connection is established by running

 $ wvdial section

The final wvdial command should start pppd and the obtained IP address should be visible in the terminal output. At that point the internet connection should be live, which can be easily checked with a web browser or by pinging an external IP address.
