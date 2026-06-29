**Resources**

[[]][Home](https://github.com/NateBrune/silk-guardian/)

Silk Guardian is a Linux kernel module kill switch that upon detecting changes to USB ports, wipes the RAM, securely deletes user specified files, and then shuts down the system.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Software]](#Software)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Kernel module]](#Kernel_module)
-   [[3] [Usage]](#Usage)
-   [[4] [Removal]](#Removal)
-   [[5] [See also]](#See_also)
-   [[6] [External resources]](#External_resources)

## [Installation]

### [Software]

Silk Guardian needs to be built manually since it can only be configured by modifying the source code prior to being built.

Install the required dependencies:

`root `[`#`]`emerge --ask --noreplace dev-vcs/git`

Clone the Silk Guardian [Git](https://wiki.gentoo.org/wiki/Git "Git") repository:

`root `[`#`]`git clone https://github.com/NateBrune/silk-guardian.git /usr/local/src/silk-guardian`

Silk Guardian activation can be prevented by adding known USB devices to a whitelist. The whitelist format is `,`, where `<vendor-id>` and `` are 4 digit hexadecimal numbers returned by [lsusb]. For example, to whitelist a Logitech G105 keyboard, add its vendor ID (`046d`) and product ID (`c248`) to the `whitelist_table` array in [config.h]:

[FILE] **`/usr/local/src/silk-guardian/config.h`**

    static const struct usb_device_id whitelist_table[] = ,
    };

When activated, Silk Guardian will securely delete user specified files with [shred]. This feature is particularly useful when sensitive files are stored on the system. For example, to securely delete the user Larry\'s SSH and GnuPG private keys, add the following to the `remove_files` array in [config.h]:

[FILE] **`/usr/local/src/silk-guardian/config.h`**

    static char *remove_files[] = ;

Build and install Silk Guardian:

`root `[`#`]`cd /usr/local/src/silk-guardian `

`root `[`#`]`make && make install `

** Note**\
The Silk Guardian kernel module will need to be built and installed every time a new kernel is installed.

## [Configuration]

### [Kernel module]

The Silk Guardian kernel module can be loaded manually by the [modprobe] command:

`root `[`#`]`modprobe silk`

To manually remove the Silk Guardian kernel module:

`root `[`#`]`modprobe -r silk`

The Silk Guardian kernel module can also be loaded automatically at boot:

[FILE] **`/etc/modules-load.d/silk-guardian.conf`**

    silk

## [Usage]

-   Silk Guardian can be activated when an unknown USB device is plugged into the system. This could be useful in stopping a malicious USB device from installing malware or a backdoor onto the system.

<!-- -->

-   Silk Guardian can be activated by unplugging a known USB device from the system that has not been whitelisted. In this case, the known USB device needs to be plugged into the system prior to loading the Silk Guardian kernel module. This is useful when the system needs to be quickly secured, especially when [disk encryption](https://wiki.gentoo.org/wiki/Dm-crypt "Dm-crypt") is utilized.

## [Removal]

To uninstall Silk Guardian:

`root `[`#`]`modprobe -r silk `

`root `[`#`]`rm -i /lib/modules/$(uname -r)/extra/silk.ko `

`root `[`#`]`depmod -a `

## [See also]

-   [Allow only known usb devices](https://wiki.gentoo.org/wiki/Allow_only_known_usb_devices "Allow only known usb devices") --- describes how to protect a GNU/Linux system against rogue USB devices via a white listing policy.

## [External resources]

-   [USBGuard](https://usbguard.github.io/) - A software framework that protects against rogue USB devices.