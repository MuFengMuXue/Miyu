# Silent boot

This page is for those who prefer to limit the verbosity of their system to a strict minimum, either for aesthetics or other reasons. Following this guide will remove all text from the bootup process. Video demonstration

## Kernel parameters
Change the kernel parameters using the configuration options of your boot loader, to include the following parameters:

 quiet

If you are still getting messages printed to the console, it may be dmesg sending you what it thinks are important messages. You can change the level at which these messages will be printed by using , where  is any number between 0 and 7, where 0 is the most critical, and 7 is debug levels of printing.

 quiet loglevel=3

Note that this only seems to work if both  and  are used, and they must be in that order (quiet first). The loglevel parameter will only change that which is printed to the console, the levels of dmesg itself will not be affected and will still be available through the journal as well as dmesg. For more information, see kernel parameters.

If you also want to stop systemd from printing its version number when booting, you should also append  to your kernel parameters. If systemd is used in an initramfs, append  instead. See  for details.

If you are using the  hook in the initramfs, you may get systemd messages during initramfs initialization. You can pass  to disable them, or  to only suppress successful messages (so in case of errors you can still see them). Actually,  is already passed to  when  is used, however for some motive sometimes systemd inside initramfs does not get it. Below are the parameters that you need to pass to your kernel to get a completely clean boot with systemd in your initramfs:

 quiet loglevel=3 systemd.show_status=auto rd.udev.log_level=3

Also  to remove the Last login message.

Users of plymouth must use both the  and  kernel parameter, otherwise the  fallback theme is used and shows systemd messages.

## Remove console cursor blinking
The console cursor at boot keeps blinking if you follow these instructions. This can be solved by passing  to the kernel To recover the cursor in the TTY, run:
 # setterm -cursor on >> /etc/issue

## sysctl
To hide any kernel messages from the console, add or modify the  line according to [https://unix.stackexchange.com/a/45525:

## agetty
To hide agetty printed issue and "login:" prompt line from the consolecreate a drop-in snippet for .

{{hc|/etc/systemd/system/getty@tty1.service.d/skip-prompt.conf|2=
[Service
ExecStart=
ExecStart=-/sbin/agetty --skip-login --nonewline --noissue --autologin username --noreset --noclear - ${TERM}
}}

## startx
To hide  messages, you could redirect its output to  in your shell profile file (like  in Bash or  in Zsh):

 if [ -z "$DISPLAY" ] && [ "$XDG_VTNR" = 1 ]; then
   exec startx &>/dev/null
 fi

## fsck
To hide fsck messages during boot, let systemd check the root filesystem. For this, replace udev hook with systemd and remove the fsck hook:

 HOOKS=(base systemd autodetect microcode modconf kms keyboard sd-vconsole block filesystems)

in  and regenerate the initramfs.

See  for more info on the options you can pass to  - you can change how often the service will check (or not) your filesystems.

## Make GRUB silent
To hide GRUB welcome and boot messages, you may install unofficial  package.

After the installation, it is required to reinstall GRUB to necessary partition first.

Then, take an example as , and make necessary changes to .

Below three lines are necessary:

Lastly, regenerate the  file.

## Retaining or disabling the vendor logo from UEFI
Modern UEFI systems display a vendor logo on boot until handing over control to the boot loader—e.g. Lenovo laptops display a bright red Lenovo logo. This vendor logo is typically blanked by the boot loader—if standard GRUB is used—or by the kernel.

To prevent the kernel from blanking the vendor logo, Linux 4.19 introduced a new configuration option  that retains the contents of the framebuffer until text needs to be printed on the framebuffer console. Since version 4.19.arch1, the official Arch Linux kernels are compiled with .

When combined with a low loglevel (to prevent text from being printed), the vendor logo can be retained while the system is initialized. Note that GRUB in the standard configuration blanks the screen; consider booting directly an EFI boot stub and thus leverage deferred takeover.

Video demonstration

The kernel command line should use  or  as mentioned above. Note that if you often receive  messages in the kernel log, you need to use log level 2 to silence these at boot time. Alternatively, if you compile your own kernel, adjust the log level of the message in .

If you use Intel graphics, see also Intel graphics#Fastboot.

Further reading:

* Phoronix: Linux 4.19 Adds Deferred Console Takeover Support For FBDEV - Cleaner Boot Process
* Hans de Goede: Adding deferred fbcon console takeover to the Fedora kernels

## Disabling deferred takeover
If the new behavior leads to issues, you can disable deferred takeover by using the  kernel parameter.
