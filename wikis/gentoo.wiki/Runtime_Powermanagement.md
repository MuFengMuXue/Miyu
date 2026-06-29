Linux can power down unused devices and wake them up on demand.

## [Configuration]

Enforce for every device:

[FILE] **`/etc/udev/rules.d/60-runtime-powermanagement.rules`**

    SUBSYSTEM!="pci", GOTO="power_runtime_rules_end"
    ACTION!="add", GOTO="power_runtime_rules_end"

    KERNEL=="????:??:??.?" #, WAIT_FOR_SYSFS="bInterfaceProtocol"
    PROGRAM="/bin/sleep 0.1"

    ATTR=="*", ATTR="auto"

    LABEL="power_runtime_rules_end"

## [See also]

-   [USB Power Saving](https://wiki.gentoo.org/wiki/USB_Power_Saving "USB Power Saving")
-   [Hprofile](https://wiki.gentoo.org/wiki/Hprofile "Hprofile") --- an application that can be used to manage multiple profiles be it hardware or software.