# Kernel module

Kernel modules are pieces of code that can be loaded and unloaded into the kernel upon demand. They extend the functionality of the kernel without the need to reboot the system.

To create a kernel module, you can read The Linux Kernel Module Programming Guide. A module can be configured as built-in or loadable. To dynamically load or remove a module, it has to be configured as a loadable module in the kernel configuration (the line related to the module will therefore display the letter ).

To rebuild a kernel module automatically when a new kernel is installed, see Dynamic Kernel Module Support (DKMS).

## Obtaining information
Usually modules depend on the kernel release and are stored in the  directory.

To show what kernel modules are currently loaded:

 $ lsmod

To show information about a module:

 $ modinfo module_name

To list the options that are set for a loaded module use  from :

 $ systool -v -m module_name

To display the comprehensive configuration of all the modules:

 $ modprobe -c | less

To display the configuration of a particular module:

 $ modprobe -c | grep module_name

List the dependencies of a module (or alias), including the module itself:

 $ modprobe --show-depends module_name

## Automatic module loading
Today, all necessary modules loading is handled automatically by udev, so if you do not need to use any out-of-tree kernel modules, there is no need to put modules that should be loaded at boot in any configuration file. However, there are cases where you might want to load an extra module during the boot process, or blacklist another one for your computer to function properly.

## Early module loading
Early module loading depends on the initramfs generator used:

* Booster#Early module loading
* Dracut#Early kernel module loading
* Mkinitcpio#MODULES

## systemd
Kernel modules can be explicitly listed in files under  for systemd to load them during boot. Each configuration file is named in the style of . Configuration files simply contain a list of kernel modules names to load, separated by newlines. Empty lines and lines whose first non-whitespace character is  or  are ignored.

See  for more details.

## Manual module handling
Kernel modules are handled by tools provided by the  package, which is installed as a dependency of a kernel package. You can use these tools manually. To load a module:

 # modprobe module_name

To load a module by a file name—i.e. one that is not installed in the  directory—use any of:

 # insmod file_name module_options
 # modprobe file_name

To unload—remove—a module, use any of:

 # rmmod module_name
 # modprobe -r module_name
 # modprobe --remove module_name

## Setting module options
To pass a parameter to a kernel module, you can pass them manually with modprobe or assure certain parameters are always applied using a modprobe configuration file or by using the kernel command line. If the module is built into the kernel, the kernel command line must be used and other methods will not work.

## Using modprobe
The basic way to pass parameters to a module is using the modprobe command. Parameters are specified on command line using simple  assignments:

 # modprobe module_name parameter_name=parameter_value

## Using modprobe.d
Configuration files in the  directory can be used to pass module settings to udev, which will use modprobe to manage the loading of the modules during system boot. Files in this directory can have any name, given that they end with the .conf extension. The file name matters, see . To show the effective configuration:

 $ systemd-analyze cat-config modprobe.d

The syntax is:

Multiple module parameters are separated by spaces, in turn a parameter can receive a list of values which is separated by commas:

For example:

## Using kernel command line
You can also pass options to the module using the kernel command line. This is the only working option for modules built into the kernel. For all common boot loaders, the following syntax is correct:

 module_name.parameter_name=parameter_value

For example:

 thinkpad_acpi.fan_control=1

Simply add this to the appropriate line in your boot loader configuration, as described in Kernel parameters#Boot loader configuration.

## Aliasing
Aliases are alternate names for a module. For example:  means you can use  instead of . You can also use shell-style wildcards, so  means that  has the same effect. Create an alias:

Aliases can be internal—contained in the module itself. Internal aliases are usually used for #Automatic module loading when it is needed by an application, e.g. when the kernel detects a new device. To see the module internal aliases:

 $ modinfo --field=alias module_name

To see both configured and internal aliases:

 $ modprobe --showconfig | grep '\<module_name$'

## Blacklisting
Blacklisting, in the context of kernel modules, is a mechanism to prevent the kernel module from loading. This could be useful if, for example, the associated hardware is not needed, or if loading that module causes problems: for instance there may be two kernel modules that try to control the same piece of hardware, and loading them together would result in a conflict.

Some modules are loaded as part of the initramfs.  will print out all automatically detected modules: to prevent the initramfs from loading some of those modules, blacklist them in a .conf file under  and it shall be added in by the  hook during image generation. Running  will list all modules pulled in by the various hooks (e.g.  hook,  hook, etc.). Remember to add that .conf file to the  array in  if you do not have the  hook in your  array (e.g. you have deviated from the default configuration), and once you have blacklisted the modules regenerate the initramfs, and reboot afterwards.

## Using modprobe.d
## alias
Disable an alias by overriding. For example, to prevent Bluetooth module autoloading (assuming a module named  does not exist):

## blacklist
To disable all internal aliases for a given module use the  keyword. For example, to prevent the  module from loading on boot to avoid sounds through the PC speaker:

## install
There is a workaround for the behaviour described in the #alias and #blacklist notes. The  configuration command instructs modprobe to run a custom command instead of inserting the module in the kernel as normal, so you can simulate the successful module loading with:

You can force the module to always fail loading with : this will effectively prevent the module—and any other that depends on it—from loading by any means, and a log error message may be produced.

## Using kernel command line
You can also blacklist modules from the boot loader boot entry configuration.

Simply add  to your kernel command line, as described in Kernel parameters#Boot loader configuration.

Another use case for a command line option is to disable hardware-specific components of a module without disabling the module entirely. For example, disabling a microphone while retaining other sound out options. See BBS#303475 for a few examples.

## Troubleshooting
## Module does not load
In case a specific module does not load and the boot log (accessible by running  as root) says that the module is blacklisted, but the directory  does not show a corresponding entry, check another modprobe source directory at  for blacklisting entries.

A module will not be loaded if the "vermagic" string contained within the kernel module does not match the value of the currently running kernel. If it is known that the module is compatible with the current running kernel the "vermagic" check can be ignored with .
