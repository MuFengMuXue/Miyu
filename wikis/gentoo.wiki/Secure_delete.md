**Resources**

[[]][Package information](https://packages.gentoo.org/packages/sys-apps/coreutils)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Data_erasure "wikipedia:Data erasure")

Once data has been stored on a disk, it may not be straightforward to remove that data, being sure that it cannot be read again. Securely wiping memory can differ depending on the memory type, as well as how it is interfaced with. The main obstacle in securely erasing a drive is [Data Remanence](https://en.wikipedia.org/wiki/Data_remanence "wikipedia:Data remanence"), or residual data remaining on the drive.

## Contents

-   [[1] [Introduction]](#Introduction)
    -   [[1.1] [Secure against whom or what]](#Secure_against_whom_or_what)
    -   [[1.2] [Crypto shredding]](#Crypto_shredding)
    -   [[1.3] [Wiping woes]](#Wiping_woes)
        -   [[1.3.1] [Advanced data recovery]](#Advanced_data_recovery)
        -   [[1.3.2] [Inaccessible memory regions]](#Inaccessible_memory_regions)
        -   [[1.3.3] [Write once read many (WORM) memory]](#Write_once_read_many_.28WORM.29_memory)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [USE flags]](#USE_flags)
    -   [[2.2] [Emerge]](#Emerge)
-   [[3] [Methods of destruction]](#Methods_of_destruction)
    -   [[3.1] [Crypto shredding]](#Crypto_shredding_2)
    -   [[3.2] [Erasing]](#Erasing)
        -   [[3.2.1] [Generic methods]](#Generic_methods)
        -   [[3.2.2] [SATA]](#SATA)
        -   [[3.2.3] [NVMe]](#NVMe)
-   [[4] [References]](#References)

## [Introduction]

Erasing portions of storage is often unnecessary, this is because it is simpler faster to just unlink data instead of wiping it. Wiping data requires the region of memory to be totally overwritten, and this can be a very slow process.

### [Secure against whom or what]

Like all combat areas, being it defending your system from the internet or copy protection, data erasure is another. Start with the premise that nothing is perfect.

The methods discussed here are probably adequate to defend against an attacker armed with the same tools you have. To defend against a well equipped, well funded determined attacker, media destruction is the only sure way.

### [Crypto shredding]

Planning in advance, and never writing plaintext data on a drive can help in preventing data recovery, especially recovery using inaccessible data regions. If only encrypted data has been written to a disk, through the use of [Full Disk Encryption](https://wiki.gentoo.org/wiki/Full_Disk_Encryption "Full Disk Encryption"), or other methods, deleting the key is typically enough to prevent data recovery.

An analogy to this approach is locking something into a container and throwing away the key.

### [Wiping woes]

Or, why wiping storage is not always simple.

#### [Advanced data recovery]

Even if an entire drive is overwritten with 0s, that does not guarantee that data cannot be recovered, especially if transparent compression is being used. Doing multiple overwrite passes with random data is typically required to be reasonably certain that data cannot be recovered. Wiping using random data is typically slower, and also requires good entropy sources for any amount of speed.

** Note**\
A single pass with random data is typically enough to stop recovery, especially on modern, high-capacity drives, but doesn\'t affect inaccessible memory regions.

#### [Inaccessible memory regions]

Modern hard drives often come with more available storage than the controller allows usage of. This allows the drive to reallocate data when it detects that memory is degrading. This over-provision is especially relevant to SSDs, which can physically only write each section of memory a limited amount of times before it fails. Depending on the drive, software methods used to overwrite all memory may have no way to touch this now deallocated memory.

#### [][Write once read many (WORM) memory]

Data written to any form of WORM memory, such as CD-Rs cannot be overwritten or erased, so the storage must be destroyed to prevent data recovery.

## [Installation]

### [USE flags]

### [USE flags for] [sys-apps/hdparm](https://packages.gentoo.org/packages/sys-apps/hdparm) [[]] [Utility to change hard drive performance parameters]

  --------------------------------------------------------- -----------------------------------------------------------------------------------------------------
  [`static`](https://packages.gentoo.org/useflags/static)   !!do not set this during bootstrap!! Causes binaries to be statically linked instead of dynamically
  --------------------------------------------------------- -----------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-12-19 09:51] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [USE flags for] [sys-apps/nvme-cli](https://packages.gentoo.org/packages/sys-apps/nvme-cli) [[]] [NVM-Express user space tooling for Linux]

  ------------------------------------------------------- -------------------------------------------------------
  [`+json`](https://packages.gentoo.org/useflags/+json)   Support JSON output via dev-libs/json-c
  [`pdc`](https://packages.gentoo.org/useflags/pdc)       Set default Persistent Discovery Controllers behavior
  ------------------------------------------------------- -------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-12-12 04:13] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask sys-apps/hdparm`

`root `[`#`]`emerge --ask sys-apps/nvme-cli`

## [Methods of destruction]

### [Crypto shredding]

If data recovery is ever a concern for a storage device, encryption should be the first line of defense. In the event the device is obtained before it could be wiped, the data should already be useless, unless the keys were stored with the device, making decryption easy.

If a device is encrypted using LUKS, wiping the headers is enough to render the data useless, so long as backups do not exist.

If [/dev/sda1] is LUKS encrypted, all keys can be removed from the header with:

`root `[`#`]`cryptsetup erase /dev/sda1`

** Tip**\
LUKS keys can be checked using

`root `[`#`]`cryptsetup luksDump /dev/sda1`

With no keys installed, there is no way the partition can be decrypted. To totally remove the LUKS header:

`root `[`#`]`wipefs --all /dev/sda`

** Important**\
This process doesn\'t actually remove any of the data that was written to the drive, it simply removes the metadata used for accessing it, making it irrecoverable with modern technology.

### [Erasing]

#### [Generic methods]

** Important**\
**shred** can only overwrite regions which the storage controller allows writing to, potentially leaving some recoverable data. Wear leveling on SSD\'s can also result in data being left behind until that cell is reused.

**shred** is part of *GNU coreutils* and should be preinstalled on most Gentoo based systems.

**shred** can be used to erase [/dev/sda] using one pass of pseudorandom data sourced from [/dev/urandom]:

`root `[`#`]`shred --verbose --random-source /dev/urandom --iterations 1 /dev/sda`

#### [SATA]

** Important**\
An ATA secure erase command should be executed over a proper SATA interface, not a USB interface, this is because the command is executed by the firmware, taking the drive offline while it executes. The USB controller may try to \"help\" by resetting the device, interrupting the erase.^[\[1\]](#cite_note-1)^

**hdparm** can be used to execute an [ATA Secure Erase command](https://tinyapps.org/docs/wipe_drives_hdparm.html). A Secure Erase command should handle wiping inaccessible regions.

In order to execute a SATA Secure Erase, a password must be set for the device, this password will be removed during the erase process:

`root `[`#`]`hdparm --security-set-pass NULL /dev/sda`

    security_password: ""

    /dev/sda:
     Issuing SECURITY_SET_PASS command, password="", user=user, mode=high

With the password set, the drive can be erased using:

`root `[`#`]`hdparm --security-erase NULL /dev/sda`

    security_password: ""

    /dev/sda:
     Issuing SECURITY_ERASE command, password="", user=user

#### [NVMe]

A firmware secure erase can be executed on a [NVMe](https://wiki.gentoo.org/wiki/NVMe "NVMe") drive using the [[[sys-apps/nvme-cli]](https://packages.gentoo.org/packages/sys-apps/nvme-cli)[]]-provided utility:

`root `[`#`]`nvme format --ses 1 /dev/nvmeXnY`

** Tip**\
Using various Lenovo laptops, such as [ThinkPad T480](https://wiki.gentoo.org/wiki/Lenovo_Thinkpad_T480 "Lenovo Thinkpad T480"), the formatting operation fails with *NVMe Status: Invalid Format: The LBA Format specified is not supported*. Lenovo provides an ISO of [ThinkPad Drive Erase Utility](https://support.lenovo.com/gb/en/downloads/ds019026) which can be launched from a bootable USB device. Note, the ISO image requires a transformation using [[[app-cdr/geteltorito]](https://packages.gentoo.org/packages/app-cdr/geteltorito)[]].^[\[2\]](#cite_note-2)^

## [[] References]

1.  [[[↑](#cite_ref-1)] [[https://web.archive.org/web/20180711170859/http://www.tomshardware.co.uk/answers/id-1984547/secure-erase-external-usb-hard-drive.html](https://web.archive.org/web/20180711170859/http://www.tomshardware.co.uk/answers/id-1984547/secure-erase-external-usb-hard-drive.html)]]
2.  [[[↑](#cite_ref-2)] [[make a bootable image on a removable Flash drive of Lenovo\'s SSD firmware update tool](https://askubuntu.com/questions/859202/make-a-bootable-image-on-a-removable-flash-drive-of-lenovos-ssd-firmware-update), askubuntu.com]]