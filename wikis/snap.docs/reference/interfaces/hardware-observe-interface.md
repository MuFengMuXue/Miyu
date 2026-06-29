#  hardware-observe interface

The `hardware-observe` interface allows for getting hardware information from the system.

`hardware-observe` grants read-only access to many files and directories, primarily in `/sys` and `/proc`. Additionally, it provides access to many utility files and binaries such as `lspci`, `lsusb`, and `hwinfo`.

`hardware-observe` is a more general and broad interface. If more specific hardware access is required, such as for GPIO or I2C devices, See the [gpio](https://snapcraft.io/docs/gpio-interface) and [i2c](https://snapcraft.io/docs/i2c-interface) interfaces.

---

## Developer details

**[Auto-connect](https://snapcraft.io/docs/explanation/interfaces/interface-auto-connection/)**: no

### Path access

`hardware-observe` grants **read** access to the following paths:

* **For tools like `hwinfo --short` to get hardware information**:

`/proc/ioports`

`/proc/dma`

`/proc/tty/driver/{,*}`

`/proc/sys/dev/cdrom/info`

* **For tools like `lshw -quiet` to get hardware information**:

`/proc/devices`

`/proc/ide/{,**}`

`/proc/scsi/{,**}`

`/proc/device-tree/{,**}`

`/sys/kernel/debug/usb/devices`

`/proc/sys/abi/{,*}`

* **For tools like `lspci -A linux-sysfs` to get information on files in `/sys`**:

`/sys/{block,bus,class,devices,firmware}/{,**}`

* **For tools like `lspci -A linux-proc` to get information on `/proc`**:

`/bus/pci/{,**}`
`/{,usr/}lib/modprobe.d/{,*}`

* **For tools like `lspci -k` to get information on loaded modules**:

Examples: `/etc/modprobe.d/{,*}`,

* **For tools like `lsusb` to get USB information**:

`/var/lib/usbutils/usb.ids`

`/dev/`

`/dev/bus/usb/{,**/}`

`/etc/udev/udev.conf`

*Note:* lsusb and its database have to be shipped in the snap if not on classic

* **For tools like `sensors` to get sensor information**:

`/etc/sensors3.conf`

`/etc/sensors.d/{,*}`

* **For tools like `udevadm` to get device information**:

`/run/udev/data/**`

* **For  hugepage and transparent_hugepage statuses (but not the pages themselves)**:

`/sys/kernel/mm/{hugepages,transparent_hugepage}/{,**}`

* **For information on available input devices**:

`/proc/bus/input/devices`

* **For power information**:

`/sys/power/{,**}`

`/run/udev/data/+power_supply:*`

* **For interrupts**:

`/proc/interrupts`

* **For  loaded kernel module information**:

`/proc/modules`

* **For VM information**:

`/proc/cpuinfo`

`/proc/sysinfo`

`/proc/xen/capabilities`

`/proc/1/sched`

`/sys/hypervisor/properties/features`

`/sys/hypervisor/type`

* **For container information**:

`/run/systemd/container`

### Binary access

`hardware-observe` grants executable access to the following binaries:
* **For tools provided by `util-linux`**:

`/{,usr/}bin/lsblk`

`/{,usr/}bin/lscpu`

`/{,usr/}bin/lsmem`

* **For tools like `lsusb`**:

`/{,usr/}bin/lsusb`

* **For tools like `systemd-detect-virt`**:

`/{,usr/}bin/systemd-detect-virt`

### Capability access

`hardware-observe` grants the following *capabilities*:

* **For tools like `lscpu` and `lspci -A` to inspect specific PCI access methods**:

`capability sys_rawio`

`capability sys_admin`

### Socket access

`hardware-observe` grants the following *socket access:*

* **For udevadm to read netlink**:

`network netlink raw`

The test code for the interface is in the snapd repository: [https://github.com/canonical/snapd/blob/master/interfaces/builtin/hardware_observe_test.go](https://github.com/canonical/snapd/blob/master/interfaces/builtin/hardware_observe_test.go)

The source code for the interface is in the snapd repository: [https://github.com/canonical/snapd/blob/master/interfaces/builtin/hardware_observe.go](https://github.com/canonical/snapd/blob/master/interfaces/builtin/hardware_observe.go)
