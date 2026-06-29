#  usb-gadget interface

The `usb-gadget` interface permits snaps to access the [USB Gadget API](https://www.kernel.org/doc/html/v4.17/driver-api/usb/gadget.html) using [configfs](https://www.kernel.org/doc/Documentation/filesystems/configfs/configfs.txt).

USB gadget is a feature of the Linux kernel that allows USB connected devices to identify as USB peripherals, such as USB keyboards or storage devices. They are unrelated to [Ubuntu Core gadget snaps](https://documentation.ubuntu.com/core/reference/gadget-snap-format/).

The usb-gadget interface requires snapd version _2.71+_. Prior to snapd 2.72,  function filesystem devices need `mount-control` and `system-files` interfaces to provide the necessary permissions.

## Developer details

**Auto-connect**: no

The USB Gadget API, through configfs, can be loaded through libcomposite which then provides `/sys/kernel/config/usb_gadget/` . This can then be used to create and discover new USB gadgets. This interface allows snaps to read and write to those paths.

USB gadgets using the [function filesystem](https://www.kernel.org/doc/Documentation/usb/functionfs.txt) can use a definition based on the following:

```
  usb-gadget:
    interface: usb-gadget
    ffs-mounts:
      - name: ffs-dev0
        where: /dev/ffs-dev0
        persistent: {true,false}
```

### Code examples

The test code can be found in the snapd repository:
https://github.com/canonical/snapd/blob/master/interfaces/builtin/usb_gadget_test.go

The source code for the interface is in the snapd repository:

https://github.com/canonical/snapd/blob/master/interfaces/builtin/usb_gadget.go
