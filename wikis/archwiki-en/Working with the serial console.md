# Working with the serial console

An Arch Linux machine can be configured for connections via the serial console port, which enables administration of a machine even if it has no keyboard, mouse, monitor, or network attached to it.

Installation of Arch Linux is possible via the serial console as well.

A basic environment for this scenario is two machines connected using a serial cable (9-pin connector cable).
The administering machine can be any Unix/Linux or Windows machine with a terminal emulator program (PuTTY or Minicom, for example).

The configuration instructions below will enable boot loader menu selection, boot messages, and terminal forwarding to the serial console.

## Configure console access on the target machine
## Boot loader
## GRUB
When using GRUB with a generated , edit  and enable serial input and output support:

Next add the  variable and set the options for the serial connection. For COM1 () with baud rate of 115200 bit/s:

Read GRUB's manual on Using GRUB via a serial line and the serial command for detailed explanation of the available options.

## GRUB first stage serial console
When GRUB is installed to an encrypted /boot/ partition - GRUB first stage (core.img) will show  password prompt only on platform console and will not show anything in serial console even if all serial console configuration steps were done properly.

This happens because the  has special behavior for  and will create early config placed in  but  ignores serial console configuration from  for GRUB first stage.

The  file gets overwritten each time  is launched.

To get the GRUB cryptodisk password prompt on the serial console a few extra configuration steps are required:

1. Run the following command to generate  and see the correct  parameters for your system:

EFI platforms:

 # grub-install --verbose 2>&1 | grep grub-mkimage
BIOS platorms:
 # grub-install --verbose /dev/YOUR_BOOT_DISK 2>&1 | grep grub-mkimage

You can reboot the system to check if it boots properly, but you should save the output of the commahd above - it will be hecessary at step 4.

2. Copy  to

3. Add the following lines at the beginning of  (change those lines according to desired configuration as described above):

 serial --unit=0 --speed=115200
 terminal_input serial console
 terminal_output serial console

4. Edit  parameters from step 1 (the  output):

Replace  to
Remove paramters with empty arguments (like  and ) and add  and  modules to the end of the  parameters list.

5. Run  with these parameters.

6. On BIOS platforms like  (for EFI platforms just skip this step) run the following command to install new  to your system:

 # grub-bios-setup -d /boot/grub/i386-pc/ /dev/YOUR_BOOT_DISK

In order to revert those changes - just reinstall GRUB using  command.

## GRUB Legacy
Edit the GRUB Legacy configuration file  and add these lines to the general area of the configuration:

 serial --unit=0 --speed=9600
 terminal --timeout=5 serial console

## rEFInd
rEFInd supports serial console only in text mode. Edit  and uncomment .

## Syslinux
To enable serial console in Syslinux, edit  and add  as the first directive in the configuration file.

For COM1 () with baud rate of 115200 bit/s:

 SERIAL 0 115200

The serial parameters are hardcoded to 8 bits, no parity and 1 stop bit.Read [https://wiki.syslinux.org/wiki/index.php?title=Config#SERIAL Syslinux Wiki:Config#SERIAL for the directive's options.

## Kernel
Kernel's output can be sent to serial console by setting the  kernel parameter. The last specified  will be set as .

 console=tty0 console=ttyS0,115200

See https://docs.kernel.org/admin-guide/serial-console.html.

## getty
At boot,  will start a getty instance for each console specified in the kernel command line.

If you have not configured  in kernel command line start . For  (COM1) that would be . Enable the service to start it at boot.

Unless specified otherwise in the kernel command line, getty will be expecting 38400 bit/s baud rate, 8 data bits, no parity and one stop bit-times.

## Making Connections
## Connect using a terminal emulator program
Perform these steps on the machine used to connect the remote console.

## cu
 tool  can be used to "Call Up" another system and act as a serial console:

 $ cu --line /dev/ttyS0

## dterm
 is a tiny serial communication program. If you invoke it without parameters, it will connect to  at 9600 baud by default. The following example connect to  at 115200 baud, with 8 data bits, no parity bit and 1 stop bit-times:

 $ dterm 115200 8 n 1

See its README for more examples.

## Minicom
 can be obtained from the official repositories. Start Minicom in setup mode:

 $ minicom -s

Using the textual navigation menu, change the serial port settings to the following:

 Serial Device: /dev/ttyS0
 Bps/Par/Bits: 9600 8N1

Press Enter to exit the menus (pressing Esc will not save changes).
Remove the modem Init and Reset strings, as we are not connecting to a modem. To do this, under the Modem and Dialing menu, delete the Init and Reset strings. Optionally save the configuration by choosing save setup as dfl from the main menu.
Restart minicom with the serial cable connected to the target machine.
The special keys for navigating Minicom can be found in the help menu which is opened by pressing  (i.e., exit session is ).

## picocom
 is a tiny dumb-terminal emulation program that is very like minicom, but instead of mini, it is pico. The following example connect to  at 9600 bps:

 $ picocom -b 9600 /dev/ttyS0

See its manual for detailed usage.

## Screen
GNU Screen is able to connect to a serial port. It will connect at 9600 baud by default:

 $ screen /dev/ttyS0

A different baud rate (e.g. 115200) may be specified on the command line.

 $ screen /dev/ttyS0 115200

To end the session, press  followed by . Alternatively, press , type  and confirm it by pressing .

## Serialclient
Serialclientis a CLI client for serial connection written in ruby. Install  package, then install it with the following:

 # gem install serialclient

Then, you can use like this:

 $ serialclient -p /dev/ttyS0

## tinyserial
 is a  replacement for accessing serial ports on Linux inspired by FreeBSD 'tip'.

 $ com /dev/ttyS0 9600

## tio
 is a simple serial device tool which features a straightforward command-line and configuration file interface to easily connect to serial TTY devices for basic I/O operations. It has less focus on classic terminal/modem features and more focus on the needs of embedded developers and hackers. tio was originally created to replace screen for connecting to serial devices when used in combination with tmux.

 $ tio /dev/ttyUSB0

## socat
 is a command line based utility that establishes two bidirectional byte streams and transfers data between them.

 $ socat - /dev/ttyACM0,raw,echo=0,b115200

## microcom
microcom Copy bytes from stdin to TTY and from TTY to stdout, its part of

 $ busybox microcom -s 115200 /dev/ttyACM0

## Graphical front-ends
*
*
*
*

## Windows clients
On Windows machines, connect to the serial port using programs like [https://www.chiark.greenend.org.uk/~sgtatham/putty/download.html PuTTY or Terminalbpp.

## Installing Arch Linux using the serial console
# Connect to the target machine using the method described above.
# Boot the target machine using the Arch Linux installation medium.
# When the boot loader appears, select Boot Arch Linux () and press  to edit
# Append  and press .
# Now systemd should detect  and spawn a serial getty on it. Log in as  and start the installation as usual.

## Debugging an unresponsive machine using a serial console
Even though https://lists.archlinux.org/archives/list/arch-general@lists.archlinux.org/message/R3B32YF5EBKZCYF3TGKG6WTDONQ6RFS4/ has only raw and terse instructions, it presents the full scene. It is important to note that here, the machine under test got unresponsive in a  reproducible manner. And that it happened during normal operation. So it could be accessed normally before it needed debugging. However, in general, the serial console is also useful for debugging boot issues. Perhaps by configuring the boot loader by hand at machine startup time. Also note the mentioned netconsole within the P.S paragraph of the external link from this section.

## Tips and tricks
## On-demand serial-getty for ttyUSB
Debugging a system by attaching a USB serial adapter requires starting  which may not be possible if the system cannot be interacted with in normal ways. A solution is to write an udev rule that starts the service when a USB serial adapter is plugged in.

To allow using the USB serial adapter the other way around too, the udev rule can be limited to trigger only on a specific USB port. To do that, plug in the adapter and find out its used USB port identifier. E.g. for  run:

 $ udevadm info --query=property --property=ID_PATH --value --name=/dev/ttyUSB0

Create a udev rule with the following contents using the value obtained with the previous command:

{{hc|/etc/udev/rules.d/99-usb_serial-getty.rules|2=
ACTION=="add", SUBSYSTEM=="tty", ENV{ID_BUS}=="usb", ENV{ID_PATH}=="your_ID_PATH_value", TAG+="systemd", ENV{SYSTEMD_WANTS}+="serial-getty@$kernel.service"
}}

Re-plug the USB serial adapter and the appropriate  will get started automatically. Verify it by checking the unit status with systemctl. The service will get automatically stopped when the USB device is unplugged.

## Troubleshooting
## Ctrl+c and Minicom
If you are having trouble sending a  command through minicom you need to switch off hardware flow control in the device settings (), which then enables the break.

## RS-232 barcode scanners (garbled output)
Some barcode scanners connect via RS-232 using USB-to-serial adapters (e.g. FTDI) and appear as  devices. These scanners output barcode data as a byte stream and do not use the SANE scanning stack.

If scanned barcodes produce unreadable characters (such as the Unicode replacement character ), this is commonly caused by a mismatch in serial framing parameters rather than an incorrect baud rate.

Many scanners default to 7 data bits with even parity (7E1), while Linux tools often default to 8 data bits with no parity (8N1). To test and correct this, explicitly configure the serial port:

## Resizing a terminal
Unlike ssh, serial connections do not have a mechanism to transfer something like  when a terminal is resized. This can cause weird problems with some full-screen programs (e.g. ) when you resize your terminal emulator's window.

Resizing the terminal via  is a workaround:

 $ stty rows lines cols columns

However, this requires you to manually input the proper geometry. The following methods should be simpler.

1. There is a lesser-known utility called , shipped with , that can solve this problem. Invoke it without parameters after you resize the terminal emulator's window:

 $ resize

2. If you do not want to install xterm, it is possible to do the same work via a shell function. Put the following function into your bash/zshrc and invoke it without parameters after resizing the terminal emulator's window:

{{bc|rsz() {
	if  -t 0 && $# -eq 0 ;then
		local IFS='[;' escape geometry x y
		echo -ne '\e7\e[r\e[999;999H\e[6n\e8'
		read -t 5 -sd R escape geometry || {
			echo unsupported terminal emulator. >&2
			return 1
		}
		x="${geometry##*;}" y="${geometry%%;*}"
		if  ${COLUMNS} -eq "${x}" && ${LINES} -eq "${y}" ;then
			echo "${TERM} ${x}x${y}"
		elif  "$x" -gt 0 && "$y" -gt 0 ;then
			echo "${COLUMNS}x${LINES} -> ${x}x${y}"
			stty cols ${x} rows ${y}
		else
			echo unsupported terminal emulator. >&2
			return 1
		fi
	else
		echo 'Usage: rsz'
	fi
}}}

## Extra hardware serial ports
The generic 8250 serial driver exposes 32 hardware serial ports, as set in the Arch kernel configuration. This means by default serial ports are created numbered from  to . On most systems many of these ports will be non-functional.

The number can be reduced by setting the kernel parameter . E.g.:

 8250.nr_uarts=5

This value must be set as a kernel boot parameter not a module option, as the  driver is compiled into the kernel image.
