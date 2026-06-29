# Keyboard shortcuts

This article provides a list of (not commonly known) default keyboard shortcuts and provides information about user customization.

## Standard shortcuts
## Kernel (SysRq)
There are several low level shortcuts that are implemented in the kernel via the SysRq key which can be used for debugging and recovering from an unresponsive system. Whenever possible, it is recommended that you use these shortcuts instead of doing a hard shutdown (holding down the power button to completely power off the system).

See Wikipedia:Magic SysRq key for more details.

## Enabling
systemd has the SysRq permissions bitmask set to 0x10 by default, which does not allow process signalling or rebooting, among other things. To allow full use of the  key on your system, add  to your sysctl configuration. Values greater than 1 can be used to selectively enable SysRq functions; see the Linux kernel documentation for details. If you want to make sure it will be enabled even before the partitions are mounted and in the initramfs, then add  to your kernel parameters.

Note that changing the setting through these methods will cause the changes to persist across reboots. If you want to try changing the SysRq settings for just your current session, you can run either  or .

To avoid security risks involved in fully enabling the  function, users may turn on a subset of features, as described in the following section. If unrestricted use of  is enabled, it allows killing processes and forcing reboots, which does not increase risk to desktop and laptop users. But it also can be used to dump the contents of the CPU registers, which could theoretically reveal sensitive information. Unless you go out of your way, that requires physical access to the system.

## Rebooting
A common idiom to remember this is "Reboot Even If System Utterly Broken" (also referred to as "REISUB"). Alternatively, think of it as "BUSIER"  backwards.

{| class="wikitable"
! Keyboard Shortcut
! Description
! Code to Enable
! Other Functions Enabled
|-
|  Unraw
| Switch keyboard mode for the current virtual console from the raw mode to ASCII mode (also known as XLATE mode) |
|  SAK
|-
|  Terminate
| Send SIGTERM to all processes, allowing them to terminate gracefully.
| rowspan=2
| rowspan=2 |  OOM kill   Thaw
|-
|  Kill
| Send SIGKILL to all processes, forcing them to terminate immediately.
|-
|  Sync
| Flush data to disk.
|
|
|-
|  Unmount
| Unmount and remount all filesystems read-only.
|
|
|-
|  Reboot
| Reboot
|
|
|}

For example, to selectively enable just the reboot function, set  to 128. The whole set of REISUB functions can be enabled by setting it to 244, although this also enables the additional functions, such as those listed in the last column of the table. For further documentation, see the [https://docs.kernel.org/admin-guide/sysrq.html SysRq key documentation and the kernel source file .

If you have an unresponsive system and want to perform the entire REISUB sequence, do the following:

* Press and hold .
* Press and release  (or  if your keyboard doesn't have ).
* Press and release each of the letters in the mnemonic in order, waiting about 1 second in between each press.

## Killing a memory-hogging process
 can be used to invoke the OOM (out-of-memory) killer without causing a kernel panic if nothing can be killed. The OOM killer uses a set of heuristics to pick whichever relatively non-vital process is using the most memory and kill it. This is very useful to kill a process that is softlocking your system by causing excessive thrashing, such as a runaway browser script, and can alleviate the need for a reboot in many cases. Note that the OOM killer can target a wide variety of processes despite its well-meaning heuristics and can be somewhat unpredictable, so be careful about calling it casually.

## Remote usage
 is a daemon for remotely using  functionality. It appears to be currently unmaintained. ==== Troubleshooting ====

* If a SysRq action produces output, it is sent to the kernel ring buffer where the systemd journal will pick it up. When nothing prevents the output to be displayed on the Linux console, it will be there too. Not having a response on the console does not prove the SysRq command was not processed successfully. If that is the case, run  to monitor the output as it arrives to the kernel ring buffer.
* If you are using a display manager and after  you are presented with the login screen (or full desktop if autologin is enabled), it is most likely caused by  directive in the relevant service file. If necessary, edit the unit, however this should not prevent the "REISUB" sequence from working.
* If all the above combinations work except , try using the opposite  key.
* On laptops that use  key to differentiate  from , it may not actually be necessary to use the  key (i.e.,  could work).
* On Lenovo laptops (outside of their Legion lineup)  is often configured as . To use it press and hold  then press , release  and  still holding  followed by the keys above.
* You may need to press  along with , or [https://unix.stackexchange.com/a/403843. The full key shortcut would be  or .
* Some keyboards, like Logitech K835, use  to produce .

## Xorg and Wayland
{| class="wikitable"
! Keyboard Shortcut
! Description
! Notes
|-
| , , , ...
| Switch to n-th virtual console
| If it does not work, try .
|-
|
| Paste text from the PRIMARY buffer
| By default, Qt maps  to CLIPBOARD instead of the PRIMARY buffer (see e.g. and  is mapped to the PRIMARY buffer.
|-
|}

## Customization
The below tools bind keys to higher-level actions. For tools that only bind keys to other keys, see Input remap utilities.

## Readline
Readline is a commonly used library for line-editing; it is used for example by Bash, FTP, and many more (see the details of  package under "Required By" for more examples). It has Emacs-like and vi-like editing modes which can be customized with escape sequences. Default key bindings are listed in  and the [https://tiswww.cwru.edu/php/chet/readline/rluserman.html Info documentation.

## Xorg
See Xorg/Keyboard configuration#Frequently used XKB options for some common shortcuts, that are disabled by default.

When we are in a graphical environment we may want to execute a command when certain key combination is pressed (i.e. bind a command to a keysym). There are multiple ways to do that:

* The most portable way using low level tools, such as acpid. Not all keys are supported, but configuration in uniform way is possible for keyboard keys, power adapter connection and even headphone jack (un)plugging events. It is also difficult to run programs inside X session correctly.
* The universal way using Xorg utilities (e.g. xbindkeys) and eventually your desktop environment or window manager tools.
* The quicker way using a third-party program to do everything in GUI, such as the Gnome Control Center.

## sxhkd
A simple X hotkey daemon with a powerful and compact configuration syntax. See sxhkd for details.

## actkbd
From actkbd home page:
: is a simple daemon that binds actions to keyboard events. It recognises key combinations and can handle press, repeat and release events. Currently it only supports the linux-2.6 evdev interface. It uses a plain-text configuration file which contains all the bindings.

A sample configuration and guide is available here.

## xbindkeys
xbindkeys allows advanced mapping of keysyms to actions independently of the Desktop Environment.

## Key binding for X-selection-paste
Users who prefer to work with the keyboard rather than the mouse may benefit from a key binding to the paste operation of the middle mouse button. This is especially useful in a keyboard-centered environment. A workflow example is:

# In Firefox, select a string you want to web-search for (with the mouse).
# Hit  to enter the "search engine" field.
# Hit  to paste the buffer, instead of moving the mouse pointer to the field and middle-click to paste.

The method suggested here uses the following three packages::

*  to give access to the x-selection-buffer content.
* Xbindkeys to bind a key-stroke to an action.
*  to pass the buffer string to the application by emulating keyboard input.

This example binds the x-selection-paste operation to the  key:

The  code prefixes a 100 ms pause to inserting the selection buffer (see the xvkbd home page).

The key codes for keys other than  can be determined using .

References:

* Pasting X selection (not clipboard) contents with keyboard
* xvkbd home page
