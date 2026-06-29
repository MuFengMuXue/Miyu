# DSDT

DSDT (Differentiated System Description Table) is a part of the ACPI specification. It supplies information about supported power events in a given system. ACPI tables are provided in firmware from the manufacturer. A common Linux problem is missing ACPI functionality, such as: fans not running, screens not turning off when the lid is closed, etc.  This can stem from DSDTs made with Windows specifically in mind, which can be patched after installation. The goal of this article is to analyze and rebuild a faulty DSDT, so that the kernel can override the default one.

Basically a DSDT table is the code run on ACPI (Power Management) events.

## Before you start
It is possible that the hardware manufacturer has released an updated firmware which fixes ACPI related problems.  Installing an updated firmware is often preferred over this method because it would avoid duplication of effort.

This process does tamper with some fairly fundamental code on your installation. You will want to be absolutely sure of the changes you make. You might also wish to clone your disk beforehand.

Even before attempting to fix your DSDT yourself, you can attempt a couple of different shortcuts:

## Tell the kernel to report a version of Windows
Use the variable  as a kernel parameter. For example:
 acpi_os_name="Microsoft Windows NT"

To add a recognized OS interface, use the variable .
 acpi_osi="Linux"

To use only one OS interface, add . This tells the firmware that there is only one supported operating system, so this is often the recommended solution.
 acpi_osi=! acpi_osi="Windows 2022"

To remove an interface, use an exclamation point in the beginning of the string.
 acpi_osi="!Windows 2012"

Other strings to test:
* "Microsoft Windows XP"
* "Microsoft Windows 2000"
* "Microsoft Windows 2000.1"
* "Microsoft Windows ME: Millennium Edition"
* "Microsoft WindowsME: Millennium Edition"
* "Windows 2001"
* "Windows 2006"
* "Windows 2009"
* "Windows 2012"
* "Windows 2015"
* "Windows 2020"

Out of curiosity, you can follow the steps below to extract your DSDT and search the .dsl file.  Just grep for "Windows" and see what pops up.

## Find a fixed DSDT
A DSDT file is originally written in ACPI Source language (an .asl/.dsl file). Using a compiler this can produce an 'ACPI Machine Language' file (.aml) or a hex table (.hex). To incorporate the file in your Arch install, you will need to get hold of a compiled .aml file — whether this means compiling it yourself or trusting some stranger on the Internet is at your discretion.  If you do download a file from the world wide web, it will most likely be a compressed .asl file.  So you will need to unzip it and compile it. The upside to this is that you will not have to research specific code fixes yourself.

Arch users with the same laptop as you are: a minority of a minority of a minority. Try browsing other distributions/Linux forums for talk about the same model. It is likely they have the same problems and either because there is a lot of them, or because they are tech savvy — someone there has produced a working DSDT and may even provide a precompiled version (again, use at your own risk).
Search engines are your best tools. Try keeping it short: 'model name' + 'dsdt' will probably produce results.

## Recompiling it yourself
Your best resources in this endeavor are going to be ACPI Spec homepage, and Linux ACPI Project which supercedes the activity that occurred at acpi.sourceforge.net.
In a nutshell, you can use Intel's ASL compiler to turn your systems DSDT table into source code, locate/fix the errors, and recompile.

You will need to install  to modify code.

What compiled the original code?
Check if your system's DSDT was compiled using Intel or Microsoft compiler:

In case Microsoft's compiler had been used, abbreviation INTL would instead be MSFT.
In the example, there were 5 errors on decompiling/recompiling the DSDT. Two of them were easy to fix after a bit of googling and delving into the ACPI specification. Three of them were due to different versions of compiler used and are, as later discovered, handled by the ACPICA at boot-time. The ACPICA component of the kernel can handle most of the trivial errors you get while compiling the DSDT. So do not fret yourself over compile errors if your system is working the way it should.

Extract the binary ACPI tables:

Disassemble the ACPI tables to a .dsl file:

Attempt to create a hex AML table (in C) from the .dsl file:

Examine any errors outputted from creating the hex AML table and fix them. For example:

Amend the file at line 6727 where the error occurred:

{{bc|
(_PLD, Package(1) {Buffer (0x10)
{
    ...
}})
}}

Increase the OEM version. Otherwise, the kernel will not apply the modified ACPI table. For example, before increasing the OEM version:

After increasing the OEM version:

Create the hex AML table again after fixing all errors and increasing the OEM version:

You might want to try the option  for C include file to insert into kernel source. If no errors and no warnings are raised, you should be good to go.

## Using modified code
There are at least two ways to use a custom DSDT:

* creating a uncompressed CPIO archive that is loaded by the kernel very early during boot,
* compiling it into the kernel.

## Using mkinitcpio's acpi_override hook
mkinitcpio provides an  hook which takes all .aml files found in  and  and places them in an early uncompressed CPIO archive inside . This avoids the need to manually create a separate CPIO archive or to change the boot loader configuration since mkinitcpio packs the uncompressed CPIO archive together with the main initramfs image into one file.

First, create the  directory and copy all needed .aml files to it. E.g.:

 # mkdir /etc/initcpio/acpi_override
 # cp dsdt.aml /etc/initcpio/acpi_override/

Add  to the  array in :

Finally, regenerate the initramfs and reboot.

## Using a CPIO archive
This method has the advantage that you do not need to recompile your kernel, and updating the kernel will not make it necessary to repeat these steps.

This method requires the  kernel configuration to be enabled (true for the  package). See for details.

First, create the following folder structure:

 $ mkdir -p kernel/firmware/acpi

Copy the fixed ACPI tables into the just created  folder, for example:

 $ cp dsdt.aml ssdt1.aml kernel/firmware/acpi

Within the same folder where the newly created  folder resides, run:

 $ find kernel | cpio -H newc --create > acpi_override

This creates the CPIO archive containing the fixed ACPI tables. Copy the archive to the  directory.

 # cp acpi_override /boot

Lastly, configure the boot loader to load your CPIO archive, like the examples in Microcode#Microcode in a separate initramfs file.

Now all that is left to do is to reboot and to verify the result.

## Compiling into the kernel
You will want to be familiar with compiling your own kernel.  The most straightforward way is with the "traditional" approach.
After compiling DSDT, iasl produce two files:  and .

Using :
* Disable "Select only drivers that do not need compile-time external firmware". Located in "Device Drivers -> Generic Driver Options".
* Enable "Include Custom DSDT" and specify the absolute path of your fixed DSDT file (, not ). Located in "Power management and ACPI options -> ACPI (Advanced Configuration and Power Interface) Support".

## Using the AML with GRUB
If you use GRUB you can use an even easier method. Copy the above created .aml file to your boot partition:

 # cp dsdt_patch.aml /boot

Then add the following line to your GRUB config:

 acpi /dsdt_patch.aml

You can e.g. add this to , don't forget to generate your GRUB config afterwards.

## Using the AML with dracut
If you use Dracut, you can simply copy the above created .aml file to a defined location. An according configuration file
 must be created:
 acpi_override="yes"
 acpi_table_dir="/usr/local/lib/firmware/acpi"

## Verify successful override
Look for messages that confirm the override, for example:
