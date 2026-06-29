# Compile kernel module

Sometimes you may wish to compile Linux's Kernel module without recompiling the whole kernel.

## Build environment
Firstly you will need to install build dependencies such as a compiler () and .

Next you will need to get the source code for the kernel version the module is intended to run on. You may try using newer kernel sources but most likely the compiled module will not load.

In case the intended kernel version is the installed kernel, find its version with

 $ uname -r

There are two main options to acquire the required source. Each option has slightly different usage methods and directory structure.

## Traditional compilation
See Kernel/Traditional compilation#Download the kernel source. If you fetch latest source using Git you will need to checkout needed version using tag (eg. v4.1).

## Arch Build System
For a general overview on Arch Build System read ABS. See Kernel/Arch build system for acquiring the kernel source, as well as the directory structure, and other details.

## Source configuration
When you have the source code, enter its directory. For the #Arch Build System case, that directory would be  down from where the PKGBUILD is.

The output from  is beneficial here. Start by cleaning with

 $ make mrproper

An appropriate  file is now required. If none is nearby, perhaps from a saved , and the intended kernel version is the running kernel, you can use its configuration file:

 $ zcat /proc/config.gz > .config

Next ensure the  file is adjusted for the kernel version. If you are using kernel sources for the exact current version then it should not ask anything. But for another version than the current kernel you might be asked about some options. In any case, for the #Arch Build System option, you might want to examine the  function.

If the module you want to compile have some compilation options such as debug build, or it was not compiled before, you can also, possibly must, adjust the kernel configuration. You can do this with one of the many configuration targets mentioned by make help.

 $ make oldconfig

## Module compilation
In order to compile and load our module cleanly, we must find the value of the EXTRAVERSION component of the current kernel version number so we can match the version number exactly in our kernel source. EXTRAVERSION is a variable set in the kernel top-level Makefile, but the Makefile in a vanilla kernel source will have EXTRAVERSION empty; it is set only as part of the Arch kernel build process. If relevant, the value of the current kernel's EXTRAVERSION can be found by looking at the output of the  command. In general, the kernel version is the concatenation of three components. Namely, the numeric version, the EXTRAVERSION, and the LOCALVERSION. The numeric version itself is a concatenation of three numbers. If built by a PKGBUILD file, the LOCALVERSION will be taken from the  variable, prefixed by a hyphen. And the EXTRAVERSION will be the suffix of the  variable, where the period character to the right of the third numeric number of the numeric version is replaced by a hyphen. For example, with the linux package , the LOCALVERSION is . The EXTRAVERSION is . The output of  will be  in that example.

Once the EXTRAVERSION value is known, we prepare the source for module compilation:
 $ make EXTRAVERSION= modules_prepare
Example:
 $ make EXTRAVERSION=-arch1 modules_prepare

Alternatively, if you are happy to load modules with modprobe using the  option to ignore mismatches in the kernel version number, you can simply run:
 $ make modules_prepare

Finally, compile wanted module by specifying its directory name. You can find the module location, thus also its directory name, with modinfo or find.

 $ make M=fs/btrfs

As a last resort, if nothing else has worked, you can

 $ make modules

Which will build all the modules from the kernel configuration.

## out-of-tree module compilation
get the official source code of the current running linux kernel as described in Kernel/Arch build system:

 $ cd && mkdir build
 $ pkgctl repo clone linux

then point to the checked out source when compiling the module:

 $ cd build/mymod
 $ make -C ~/build/linux/src/archlinux-linux M=$PWD modules

## Module installation
Now after successful compilation you just need to gzip and copy it over for your current kernel.

If you are replacing some existing module you will need to overwrite it (and remember that reinstalling  will replace it with default module)

 $ zstd fs/btrfs/btrfs.ko
 # cp -f fs/btrfs/btrfs.ko.zst /usr/lib/modules/$(uname -r)/kernel/fs/btrfs/

Or alternatively, you can place the updated module in the updates folder (create it if it does not already exist).

 $ cp fs/btrfs/btrfs.ko.zst /usr/lib/modules/$(uname -r)/updates

However if you are adding a new module you can just copy it to extramodules (note, this is just example as btrfs will not get loaded from here)

 # cp fs/btrfs/btrfs.ko.zst /usr/lib/modules/$(uname -r)/extramodules/

You need to rebuild the module dependency tree with "depmod" to use installed modules.

If you are compiling a module for early boot (e.g. updated module) which is copied to Initramfs then you must remember to regenerate it with (otherwise your compiled module will not be loaded).

 # mkinitcpio -p linux

## possible errors
If EXTRAVERSION is not set correctly the following errors may occur
 # insmod mymod.ko
 insmod: ERROR: could not insert module mymod.ko: Invalid module format
 # modprobe mymod
 modprobe: ERROR: could not insert 'mymod': Exec format error
adding force-vermagic makes it ignore the version mismatch
 modprobe mymod --force-vermagic
