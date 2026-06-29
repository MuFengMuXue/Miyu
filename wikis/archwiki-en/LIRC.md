# LIRC

From the official website:
:LIRC (Linux Infrared Remote Control) is a package that decodes and sends infra-red signals of many (but not all) commonly used remote controls.

This article covers setup and usage of LIRC with serial or USB infrared devices.

LIRC is a daemon that can translate key presses on a supported remote into program specific commands. In this context, the term, "program specific" means that a key press can do different things depending on which program is running and taking commands from LIRC.

# A button on the remote is pressed causing it to transmit an IR or RF signal.
# The signal is received by the receiver connected to the Linux computer.
# The kernel (via the correct module) use presents pulse data from the remote on a device like , ,  or .
#  uses the information from  to convert the pulse data into button press information.
# Programs that use LIRC translate the button press info from  into user-defined actions according to  or to program-specific mappings.

## Installation
Install the  package.

## Configuration
## Receiver and transmitter configuration
The driver and/or the device for the LIRC service may need to be specified in order to run properly. Look for messages like these in the journalctl output if the service abruptly stops while running LIRC-dependent programs such as irrecord:

 Driver `devinput' not found or not loadable (wrong or missing -U/--plugindir?).
 readlink() failed for "auto": No such file or directory

Set these in the configuration file and then restart the service.

## Serial port
Modern kernel has serial_ir module, which supersedes older lirc_serial driver. It supports even DIY receivers and transmitters, connected to the motherboard's serial port. Install  and run:

 # setserial /dev/ttyS0 uart none
 # modprobe serial_ir

After loading serial_ir module, device  will be created by kernel. If not, check the journal for any relevant errors. An LIRC configuration example for serial device:

## Sound card
Sound card with connected external DIY circuits can be used to receive and transmit IR codes.

audio_alsa driver included in , but supports only reception.

Unmute microphone input with  and set enough gain. You can check waveform and gain with . There should be distinguishable square pulses: not flatlined, nor overloaded. Also good demodulated pulses easily perceptible by ear. Note that LIRC and  reads positive pulses in right audio channel. Negative pulses will not work.

audio driver included in  and supports both reception and transmission. Note, that default latency around 0.02 can cause "Warning: Output underflow" and corrupted transmission - receiver will not respond to it. Try a higher value like 0.05.

Increase sound card output loudness, otherwise LED signal will be weak and range is low. LED flash can be detected with smartphone camera, as it sensitive to infrared wavelengths.

## Remote configuration
Directory  contains system-wide configuration files for remotes. Each *.conf file corresponds to one device and describes its protocol, scancodes and keycodes. It allows LIRC receive and send signals for specific hardware. These files are not included in  package and should be found somewhere or created by user.

## Searching for remote configuration
Plenty of configuration files can be found in the LIRC remotes database. Follow the url or use  to search the database.

An example using  to find a configuration file for a "Streamzap" remote:

Once identified, copy the needed .conf to  to allow the daemon to initialize support for it.

 # cp streamzap.lircd.conf /etc/lirc/lircd.conf.d/

## Creating remote configuration
Remote control configurations can be created using , which guides users trough the process. If using a detected remote, invoke it like so:

 # irrecord --device=/dev/lirc0 MyRemote

The program will instruct user to begin hitting keys on the remote in an attempt to learn it, ultimately mapping out every button and its corresponding scancode. When finished, save the resulting file to  and proceed. Consider sharing configuration file with others.

## Application-specific actions
Bind keycodes to application-specific actions by placing their respective configuration files in  which should be created manually if desired, see .  This only works for LIRC-aware applications, like MPlayer, VLC, MythTV and  (Kodi also supports LIRC but does so in a non-standard way, see Kodi#Using a remote control).

Define these application-specific configurations in separate files and include them in lircrc, like:

 include "~/.config/lircrc/mplayer"
 include "~/.config/lircrc/mythtv"
 include "~/.config/lircrc/vlc"

## Running as a regular user
By default, lircd runs as root.  For increased stability and security, upstream recommends running it as a regular user.  See Appendix 14 at this link.

## User the AUR package for lirc-user-service
 is offered which does everything automatically.

## Testing
Start/enable .

## Receiving commands
Run , point remote to the receiver and press some buttons. Received codes will be printed to stdout.

If  gives no output:

* Run mode2 or xmode2 to see if LIRC actually read something from IR sensor, if no - check the hardware
* If mode2 receives pulse data, check the configuration files in  for errors

## Transmitting commands
List registered remotes (configuration files):

List available codes for the specific device:

Choose discovered device  and send command :

 $ irsend SEND_ONCE LG_6710CMAP01A KEY_POWER

## Troubleshooting
## Remote functions as a keyboard
## When using Xorg
Xorg detects some remotes, such as the Streamzap USB PC Remote, as a Human Interface Device (HID) which means some or all of the keys will show up as key strokes as if entered from the physical keyboard. This behavior will present problems if LIRC is to be used to manage the device.

To disable, create the following file and restart X:

Do not forget to alter the  property according to one shown in  from output of

 $ grep -e IR /proc/bus/input/devices

For example  for

## Not using Xorg
Blacklist the offending modules by creating  to suppress this behavior. An example is provided for the Streamzap remote.
 install ir_sharp_decoder /bin/false
 install ir_xmp_decoder /bin/false
 install ir_rc5_decoder /bin/false
 install ir_nec_decoder /bin/false
 install ir_sony_decoder /bin/false
 install ir_mce_kbd_decoder /bin/false
 install ir_jvc_decoder /bin/false
 install ir_rc6_decoder /bin/false
 install ir_sanyo_decoder /bin/false

## Changing default configuration
Users not getting any output from  may have the default configuration in  incorrectly setup (or might have been overwritten by an update).

First, check if  is present:

 $ mode2 --driver default --device /dev/lirc0

Watch the output while pressing buttons on the remote. If output is present, edit  changing the  driver and device appropriately.

If no output is presented, the task becomes locating the correct driver/device combination. First check what combination lirc detected by default. Run  from the  package. and check the output. It will look similar to this:

  Found /sys/class/rc/rc0/ (/dev/input/event5) with:
        Driver ite-cir, table rc-rc6-mce
        Supported protocols: unknown other lirc rc-5 jvc sony nec sanyo mce-kbd rc-6 sharp xmp
        Enabled protocols: lirc
        Extra capabilities:

In this case, LIRC automatically detected  as the IR device, which uses the  driver. Check if this combination is working by running:

 $ mode2 --driver devinput --device /dev/input/event5

Now try pressing buttons on the remote. If there is no output, try different driver and device combinations.  Once a working combination has been identified, change driver and device in  appropriately.

## Example
An example configuration for a MCE RC6 compatible receiver:
