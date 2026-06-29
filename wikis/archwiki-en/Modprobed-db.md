# Modprobed-db

modprobed-db is a utility that populates a list of all the kernel modules that have been loaded on a system while running. This list can then be used to disable all the unused modules when building your own kernel and significantly reduce the compilation time.

## Installation
Install the  package.

# Run  to create  if it does not already exist.
# Run  to create the  database file and populate it with the currently loaded modules.

Optionally: add modules in the ignore array that you do *not* want counted, for example modules that get built or that are provided by another package.
Some common ones are included by default:

## Usage
## Populating the database
Once the initial database has been created, use  to show the current database modules and  to update the database with the currently loaded kernel modules.

## Recommendations
It is recommended to "use" the official Arch kernel, with  installed, for a good amount of time to allow the database to grow based on usage and capture everything the system needs before building a kernel without the unneeded modules). Here are some suggested actions to allow appropriate modules to load and get cataloged:

* Mount every kind of filesystem that will be used.
* Insert every kind of removable media that will be used (USB, DVD, CD, etc.).
** This includes the mounting of ISO image files if applicable, which uses the loop and isofs modules.
* Use every device on the machine (network interfaces, input devices, webcams, mobile devices, etc.).
* Use every desired application, as some depend on kernel modules. For example:
** IP blocking/filtering software such as  require the iptables kernel module.
** Encryption software such as  requires cryptography kernel modules. Be sure to mount some encrypted containers so they will actually be loaded.
** Certain QEMU configurations require kernel modules.
** lm-sensors requires kernel modules for reading hardware sensors.
* Try re-running modprobed-db while running different Linux-kernels; they may include modules not enabled in the other kernels.

These suggested actions are to be made in parallel with periodically updating the database with  to capture any newly loaded kernel module.

## Automatic periodic database updates
Calls to  can be automated with one of the following methods:

## Cron
The most convenient method to use modprobed-db is to simply add a crontab entry invoking  at some regular interval.

Example running the script once every hour:

 $ crontab -e
 0 */1 * * *   /usr/bin/modprobed-db store &> /dev/null

## systemd
Instead of cron, enable/start the  user unit. It will run modprobed-db in store mode once per 6 hours, and at boot and on shutdown.

Like any service and timer, the status of the  user unit can be queried.

## Manually editing the database
Using the #Automatic periodic database updates or manually running  is not entirely foolproof:

* Some modules get loaded then unloaded between two periodic database updates and may not be captured.
* Some modules are used during boot and are not captured by  (e.g. ), they need to be manually added to the  file.

Thankfully, the  database file is a simple text file that contains one kernel module name per line: it can be manually edited to add/remove a module. It is then recommended to run  after a manual edit so the modules get automatically reordered.

## Recommended modules
These modules are recommended to be added to the  database file as they are broadly used:

* , , : to support common file systems and the EFI system partition
* , : to support mounting the EFI system partition. This is required on , on other kernels they may be built-in.
* : to mount a file as a file system
* : to mount ISO files
* : for network filesystems like Samba
* : for mounting the UEFI#UEFI variables file system
* : to support USB storage devices
* : to support USB input devices

For a ready-made database of commonplace modules, linux-tkg maintains one for each (recent) kernel version: === Building a kernel with modprobed-db ===

After the database has been adequately populated, it can be read directly by [https://git.kernel.org/pub/scm/linux/kernel/git/stable/linux.git/tree/README?id=refs/tags/v4.3.3#n205 make localmodconfig.

## Traditional compilation
 naturally intervenes in a traditional compilation workflow during the configuration step with the default Arch .config file.

## Using the official Arch kernel PKGBUILD
The official Arch kernel  can be modified as shown to do this automatically:

{{hc|PKGBUILD.patch|output=
--- a/PKGBUILD
+++ b/PKGBUILD
@@ -154,6 +154,8 @@ prepare() {
   make olddefconfig
   diff -u ../config .config  :

+  make LSMOD=$HOME/.config/modprobed.db localmodconfig  version
   echo "Prepared $pkgbase version $(<version)"
 }
}}

## Using linux-tkg
linux-tkg offers a user-friendly kernel build script that also includes extra patches oriented towards improving desktop/gaming performance. In its configuration file, it supports user-provided 's database files, but also offers its own "diet" database files: contains the most common modules while still producing a lighter kernel.

## Benefits of modprobed-db with "make localmodconfig" in custom kernels
# Significantly reduced compilation time
# Unneeded modules are not built, the saved disk space is negligible for desktop computers as it is a relatively small gain (few hundred megabytes).

Comparisons using kernel version 5.13.1, where a Kernel/Traditional compilation is made with the default Arch configuration.

{| class="wikitable"
! Machine CPU !! # of threads !! Compiler !! make localmodconfig !! # of Modules !! Total Compilation Time !! Kernel Compilation Time !! Modules Compilation Time
|-
| Ryzen 5950X @ 4.55 GHz || 32 || GCC 11.1.0 || No || 5442 || 5m 12s || 58s || 4m 14s
|-
| Ryzen 5950X @ 4.55 GHz || 32 || GCC 11.1.0 || Yes || 227 || 1m 32s || 57s || 35s
|-
| Ryzen 5950X @ 4.55 GHz || 32 || Clang 12.0.1 || No || 5442 || 9m 5s || 1m 13s || 7m 52s
|-
| Ryzen 5950X @ 4.55 GHz || 32 || Clang 12.0.1 || Yes || 227 || 2m 13s || 1m 13s || 1m
|}

The main results of the benchmark is that 80% of the build time of a "full" kernel is spent on modules. Given that only a fraction of those modules are needed by any given machine, the build time can be reduced by ~70%. The results will vary from one machine to another but should be similar.

The number of modules can be determined by the following:

 $ cd /lib/modules/15.13.1-your-custom-kernel
 $ find -name '*.ko*' | wc -l

The kernel build time is obtained with:

 $ time make -jx bzImage # Replace "x" with the wanted number of threads

then the modules build time is obtained with:

 $ time make -jx modules # Replace "x" with the wanted number of threads
