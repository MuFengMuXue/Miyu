[Translate this page](//wiki.manjaro.org/index.php?title=Special:Translate&group=page-Kernel+Fails+to+Load+%28pata+acpi+error%29&language=en&action=page&filter= "Special:Translate")

Other languages:

[English](//wiki.manjaro.org/index.php?title=Kernel_Fails_to_Load_(pata_acpi_error) "Kernel Fails to Load (pata acpi error) (100% translated)") • ‎[русский](//wiki.manjaro.org/index.php?title=Kernel_Fails_to_Load_(pata_acpi_error)/ru "Ядро не загружается (ошибка pata acpi) (100% translated)")

## Contents

-   [[1] [Overview]](#Overview)
-   [[2] [Opening the Default GRUB File]](#Opening_the_Default_GRUB_File)
-   [[3] [Editing the Default GRUB File]](#Editing_the_Default_GRUB_File)
-   [[4] [Updating the GRUB]](#Updating_the_GRUB)

# [Overview]

**Tip**

------------------------------------------------------------------------

**Parallel ATA** (**[PATA](http://en.wikipedia.org/wiki/Parallel_ATA)**) is an interface standard to connect storage devices, and the **Advanced Configuration and Power Interface** (**[ACPI](http://en.wikipedia.org/wiki/Acpi)**) is used for device configuration and power management.

\
This problem may affect particular computer systems using the **[JMicron PATA Controller chipset](http://en.wikipedia.org/wiki/JMicron)**, which is used to control and access storage devices, such as Solid State Drives (**[SSD](http://en.wikipedia.org/wiki/Solid-state_drive)**). More specifically, it may be due to the **PATA ACPI driver** being loaded by the GRUB (**GR**and **U**nified **B**ootloader), which has consequently resulted in a conflict with the *JMicron* chipset. Should this indeed be the case, then an error message similar - or identical - to the example provided below should be displayed upon attempting to boot the affected kernel version(s):

    ERROR: device 'UUID=......' not found. Skipping FSCK'
    ERROR: Unable to find root device 'UUID=......'
    You are being dropped to the recovery shell
    Type 'exit' to try and continue booting
    sh: can't access tty: job control turned off'
    [...]
    mount: can't find UUID='.....'
    You are now being dropped into the emergency shell.

\
If so, then the solution is to simply stop the *PATA ACPI* driver from being loaded in the first place. This is a simple task, undertaken by amending a single line in the **default grub** file.

\

# [Opening the Default GRUB File]

**Warning**

------------------------------------------------------------------------

**DO NOT edit the *grub.cfg* file**. This is not the same as the *grub* file, which does not have an extension at the end of its name.

\
The syntax of the command to open the grub file is:

[user \$ ][ sudo \[text editor\] /etc/default/grub [COPY TO CLIPBOARD]]

\

\
For example, if you wish to edit the file within the terminal using nano (a standard terminal-based text editor) then enter:

[user \$ ][ sudo nano /etc/default/grub [COPY TO CLIPBOARD]]

\

\
If you have installed the full version of Manjaro, not the NET-Edition, you may find it easier to use the pre-installed *gedit* text editor instead. This will open the file up as a document, making it easier to read and edit. To use *gedit* instead, enter:

[user \$ ][ sudo gedit /etc/default/grub [COPY TO CLIPBOARD]]

\

# [Editing the Default GRUB File]

Once the *default grub* file has been opened, it will be necessary to amend the **GRUB_CMDLINE_LINUX=\"\"** command, which is itself located near the top of the file. An example has been provided below, with the appropriate line **highlighted in green** below for illustrative purposes:

    GRUB_DEFAULT=saved
    GRUB_TIMEOUT=5
    GRUB_DISTRIBUTOR="Manjaro"
    GRUB_CMDLINE_LINUX_DEFAULT="GRUB_CMDLINE_LINUX_DEFAULT= resume=/dev/disk/by-uuid/<some-guid>"
    GRUB_CMDLINE_LINUX=""

\
To prevent the *PATA ACPI* driver from being loaded, **modprobe.blacklist=pata_acpi** must be added in between the otherwise empty speech marks. An example of the necessary amendment has been provided below, which has again been **highlighted in green** for illustrative purposes:

    GRUB_DEFAULT=saved
    GRUB_TIMEOUT=5
    GRUB_DISTRIBUTOR="Manjaro"
    GRUB_CMDLINE_LINUX_DEFAULT="GRUB_CMDLINE_LINUX_DEFAULT= resume=/dev/disk/by-uuid/<some-guid>"
    GRUB_CMDLINE_LINUX="modprobe.blacklist=pata_acpi"

\
Once you have completed the amendments, save the change and close the file by:

-   **nano**: Press CTRL and \'x\' to exit, \'y\' to save, and \<enter\> to finish, or
-   **gedit**: Select the \'save\' option and then close the window.

\
Now all that is necessary is to **update the GRUB** before rebooting.

\

# [Updating the GRUB]

To update the GRUB, ensure that the terminal is open, and enter the folliwing command:

[user \$ ][ sudo update-grub [COPY TO CLIPBOARD]]

\

\
Once complete, reboot your system for the change to take effect.