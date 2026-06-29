# NAME

blkid - command-line utility to locate/print block device attributes

# SYNOPSIS

**blkid** \[ **-ghlLv** \] \[ \[ **-c** *cachefile* \] **-w** *writecachefile* \] \[ **-o** *format* \] \[ **-s** *tag* \] \[ **-t** *NAME*=*value* \] \[ *device ...* \]

# DESCRIPTION

The **blkid** program is the command-line interface to working with **libblkid**(3) library. It can determine the type of content (e.g. file system, swap) a block device holds, and also attributes (tokens, NAME=value pairs) from the content metadata (e.g. LABEL or UUID fields).

**blkid** has two main forms of operation: either searching for a device with a specific NAME=value pair, or displaying NAME=value pairs for one or more devices.

# OPTIONS

**-c*** cachefile*
Read from *cachefile* instead of reading from the default cache file */etc/blkid.tab*. If you want to start with a clean cache (i.e. don't report devices previously scanned but not necessarily available at this time), specify */dev/null*.

**-g**
Perform a garbage collection pass on the blkid cache to remove devices which no longer exist.

**-h**
Display a usage message and exit.

**-l**
Look up one device that matches the search parameter specified using the **-t** option. If there are multiple devices that match the specified search parameter, then the device with the highest priority is returned, and/or the first device found at a given priority. Device types in order of decreasing priority are Device Mapper, EVMS, LVM, MD, and finally regular block devices. If this option is not specified, **blkid** will print all of the devices that match the search parameter.

**-o*** format*
Display **blkid**'s output using the specified format. The *format* parameter may be *full* (the default), *value* (only print the value of the tags), *list* (print the devices in a user-friendly format), or *device* (only print the device name).

**-L**
Print the devices in a user-friendly list format. This is the equivalent of using the option **-o list**.

**-s*** tag*
For each (specified) device, show only the tags that match *tag*. It is possible to specify multiple **-s** options. If no tag is specified, then all tokens are shown for all (specified) devices. In order to just refresh the cache without showing any tokens, use **-s none** with no other options.

**-t*** NAME***=***value*
Search for block devices with tokens named *NAME* that have the value *value*, and display any devices which are found. Common values for *NAME* include **TYPE**, **LABEL**, and **UUID**. If there are no devices specified on the command line, all block devices will be searched; otherwise only the specified devices are searched.

**-v**
Display version number and exit.

**-w*** writecachefile*
Write the device cache to *writecachefile* instead of writing it to the default cache file */etc/blkid.tab*. If you don't want to save the cache to the default file, specify */dev/null.* If not specified it will be the same file as that given by the **-c** option.

*device*
Display tokens from only the specified device. It is possible to give multiple *device* options on the command line. If none is given, all devices which appear in */proc/partitions* are shown, if they are recognized.

# RETURN CODE

If the specified token was found, or if any tags were shown from (specified) devices, 0 is returned. If the specified token was not found, or no (specified) devices could be identified, an exit code of 2 is returned. For usage or other errors, an exit code of 4 is returned.

# AUTHOR

**blkid** was written by Andreas Dilger for libblkid.

# AVAILABILITY

**blkid** is part the e2fsprogs package since version 1.26 and is available from http://e2fsprogs.sourceforge.net.

# SEE ALSO

**libblkid**(3)
