# ThinkPad mobile Internet

Many Lenovo ThinkPads come with a mobile broadband modem. By inserting a SIM card into the modem, it is possible to use a cellular network to connect to the internet.

## ModemManager-handled devices
Newer Quectel modems (for example, the Quectel EM120R-GL on X13 Gen2, X1C Gen9, T14 Gen 2 AMD) can be set by ModemManager and managed with NetworkManager.

Install , then start and enable .

## FCC unlock a Quectel modem
On some devices the modem will be in an fcc-lock state.

You need to find the modem device: known devices are  and .
Alternatively, search the kernel log for  or .

A locked modem can be confirmed with the following command:

You can then unlock the modem:

 # mbimcli -p -d device -v --quectel-set-radio-state=on

Then you can enable the modem:

 $ mmcli --modem 0 --enable

Alternatively:
The  package provides a service to automatically perform the FCC unlock for the Fibocom L860R+, Fibocom FM350 5G, Quectel RM520N-GL, Quectel EM160R-GL, Quectel EM061K, Quectel EM05-CN modems based on the official Lenovo tool.

## Configuring ModemManager-handled devices
This can be set via CLI or GUI.

You can use NetworkManager's nm-connection-editor to add a new Mobile Broadband connection and follow the prompts to configure your connection.

Or as an example on KDE Plasma:

* In System Settings > Connections click the plus sign in the lower right corner to create a new link
* Select Mobile Broadband > Create
* Set up mobile broadband connection > any GSM device
* Country > country_code
* Provider > provider_name
* Select your plan > My plan is not listed
* APN > apn.number

## QMI protocol modems
## Requirements
The broadband modems in older ThinkPads use the QMI modem protocol — see "an introduction to libqmi" by a ModemManager developer for more information. These modems will show up as  on the filesystem.

It is not possible to initialize a QMI modem for use on Linux. Use Windows to activate the modem using Lenovo's activation app (or web search for "Lenovo mobile broadband" for the correct app for your modem). The modem will not work until it has been correctly initialized using the app.

## Procedure
Install the  package, which provides the  and  programs. Also install  for the helper script, which uses the  command.

Said helper script for  is available on GitHub. Save the script to somewhere in your , then review the script and make it executable. The values of some of the variables might need to be changed, especially  which can be found via  (device name start with ).

Load the kernel modules  and :

 # modprobe qmi_wwan
 # modprobe qcserial

Also read the README on the GitHub page of the QMI helper for any further prerequisites. In particular, you may need to set the APN provided by your cellular internet provider in .

Finally, running  should start the cellular internet connection.

## Gobi modems
This method is an alternative for some QMI modems.

First of all you need to make sure what model your modem is. Open your ThinkPad's backplate and look for an IC or FCC ID. For this example we are going to use GOBI2000 (IC: 2723A-GOBI2000, FCC ID: J9CGOBI2000-L)

Enable your modem device from you BIOS I/O settings.

Download the driver installer executable from https://support.lenovo.com/us/en/downloads/ds001302 and extract it with Wine. It will unpack the drivers to . The unpacker will prompt you to install the drivers automatically after unpacking, but if you need the installer again it is  in previously mentioned folder. The installer will in turn unpack the firmware images to .

Now refer to the reference information on what firmware you want/need. Generally you are good to go with the Generic UMTS and Default Firmware (Forlders 6 an UMTS).

Install . Now copy the 3 previous firmware files to  (if the folder does not exist, create it). Insert your sim card to the port found under your battery pack and restart. Your modem should now show up in your network manager.

See: https://www.thinkwiki.org/wiki/Qualcomm_Gobi_2000

## Getting around BIOS-level whitelist restrictions
In newer ThinkPad models, it is normally impossible to swap the LTE modem for a supported one due to BIOS-level restrictions ("whitelists" of allowed M.2 expansion cards) implemented in all modern Lenovo laptops. However, a method has been found to configure any Sierra Wireless EM73xx/EM74xx modem to "evade" the whitelist checks, so these modems can be used normally.

We will assume the model to be  here.

## Settings for Sierra Wireless EM7455
## General description
Use  AT command to disable the modem's USB fast enumeration feature. The modem will take a significantly longer time to appear on the USB bus and the firmware will "miss" the modem at boot time.

Alternatively, use  to selectively enable USB fast enumeration for warm boots only. The modem will reappear faster on S3 resume but still evade the whitelist checks on regular boots and reboots (the mechanism of this effect is not fully clear to the author).

This comes with a downside: because the firmware does not "see" the modem, it will not export the WWAN rfkill but instead it will unconditionally assert the  pin of the M.2 slot, forcing the modem into "airplane mode".
Use  AT command to configure the modem to ignore this pin.

## Step-by-step
Boot the laptop with the stock modem in place and WWAN card access enabled in BIOS setup.

Suspend the laptop (make sure it is configured to use S3).

Hot-swap the stock Fibocom modem with the Sierra Wireless one, then resume. Whitelists are not consulted at S3 resume.

Check that the modem is present on the USB bus:

Remember the VID (vendor ID) of the modem ( in this example).

Stop  if it is running.

Optionally, update the modem firmware with the  tool:

 # cd /path/to/extracted/firmware
 # qmi-firmware-update -d 1199 -u *.cwe *.nvu

Change the modem's USB composition to enable AT command ports:

 # qmicli -d /dev/cdc-wdm1 --dms-swi-set-usb-composition=8

Power-cycle the modem as advised by :

 # qmicli -d /dev/cdc-wdm1 --dms-set-operating-mode=offline
 # qmicli -d /dev/cdc-wdm1 --dms-set-operating-mode=reset

Wait for the modem to reappear, then verify:

Verify that the three serial ports ,  and  are now available (assuming you do not have any other USB-serial converters plugged in):

Attach to  with a serial terminal emulator of your choice (e. g. ):

 # screen /dev/ttyUSB2 115200

Enter the AT commands (note that you do not need to type , the replies are included here as part of a session transcript):

Enable command echo (if echo is initially disabled, you will not see this command as you type it):

 ATE1
 OK

Unlock engineering commands:

 AT!ENTERCND="A710"
 OK

Check customization options (these are the author's options):

 AT!CUSTOM?
 !CUSTOM:
              GPSENABLE          0x01
              GPSSEL             0x01
              IPV6ENABLE         0x01
              SIMLPM             0x01
              SINGLEAPNSWITCH    0x01

 OK

Configure USB fast enumeration (swap  for  if you want to play it safe):

 AT!CUSTOM="FASTENUMEN",2
 OK

Verify, it should now show the  option alongside others:

 AT!CUSTOM?
 !CUSTOM:
              GPSENABLE          0x01
              GPSSEL             0x01
              IPV6ENABLE         0x01
              SIMLPM             0x01
              FASTENUMEN         0x02
              SINGLEAPNSWITCH    0x01

 OK

Configure the modem to ignore W_DISABLE:

 AT!PCOFFEN=2
 OK

Verify:

 AT!PCOFFEN?
 2

 OK

Reset the modem:

 AT!RESET
 OK

the terminal will disconnect after a while.

Wait for the modem to reappear, then verify configuration by rebooting / powering down / hard resetting the laptop.

## Remarks
For more information (including the original thought process that led to this discovery), see these lenovo threads and this reddit thread.

You may also apply other useful configuration options described here.

## Troubleshooting
Ensure that you have initialized the modem on Windows.

## WWAN/LTE GUI
Install NetworkManager and  to make your life easier finding the correct APN for your SIM card.

## Invalid Transition
If you get an error  when running , it is likely you have not yet removed the fcc-lock on the modem.  See the example commands in #FCC unlock a Quectel modem.
