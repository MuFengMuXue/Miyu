#  custom-device interface

The `custom-device` interface permits access to a device of a specific class and model without requiring the creation of an interface for that device alone. It’s intended to be used with [Ubuntu Core](https://snapcraft.io/docs/reference/glossary/) and its scope and specification are defined as part of the [gadget snap](https://snapcraft.io/docs/reference/development/yaml-schemas/the-gadget-snap/) for the deployed Ubuntu Core image.

To permit access, the application snaps define a custom-device plug and the [gadget snap](https://documentation.ubuntu.com/core/reference/gadget-snap-format/) defines a custom-device slot, where both the plug and the slot have the identically-named `custom-device` attribute.

Under specific and appropriate circumstances, it is possible to define the slot directly from the consuming application itself, together with the plug, which is an acceptable approach for applications that will be widely distributed but support very specific hardware.

Using the custom-device requires [Store approval and permissions](https://snapcraft.io/docs/reference/administration/process-for-aliases-auto-connections-and-tracks/), both to allow the presence of the slot, and to set up elements such as the slot self-connecting exactly to the plug on the app. The more specific the tagging information provided by the slot, the easier it will be to allow for this.

The slot-side of the interface is used to derive which _udev_ rules are provided to the plug-side of the connection:

```yaml
slots:
  dual-sd:
    interface: custom-device
    custom-device: my-dual-sd-device
    devices:
      - /dev/DualSD
```

To prevent connection to arbitrary custom-device slots, the plug and slot must share the same custom-device attributes:

```yaml
plugs:
  dual-sd:
    interface: custom-device
    custom-device: my-dual-sd-device
apps:
  app:
    plugs: [dual-sd]
```

When the slot and plug are connected, a udev rule is automatically generated and tagged for the plug side for each device path in the `devices` and `read-devices` attributes, such as:

```
KERNEL=="DualSD",
```

Note that here, the default udev `KERNEL` rule is the full device path following the leading `/dev/`. Depending on the device drivers, some devices expect the `KERNEL` rule to be only the basename of the device path, even if that device is in a subdirectory of `/dev/`. For this reason, when `udev-tagging` attributes are not given for a device which is in a subdirectory of `/dev/`, default `KERNEL` rules are generated for both the basename and for the full device path following the leading `/dev/`.

If the `udev-tagging` attribute is used, this default udev rule is replaced with more specific rules, as described below. When a device name in the `kernel` attribute does not match the device path listed in the `devices` section, such as if the `KERNEL` udev attribute is different than the `/dev/...` path, an optional `for-device` attribute can be added to establish a correspondence, such that both udev matching rules and the AppArmor profile is generated correctly.

Requires snapd version *2.55+*, while `udev-tagging.for-device` attribute support requires snapd version *2.66+*.

---

## Developer details

**[Auto-connect](https://snapcraft.io/docs/explanation/interfaces/interface-auto-connection/)**: no

**[Super-privileged](https://snapcraft.io/docs/explanation/interfaces/super-privileged-interfaces/)**: yes

**Attributes**:
* `custom-device` (optional) (plug, slot): A label for the custom device.

 The label must be identical across the plug and slot connections.
If omitted, the label defaults to either local slot name or local plug name.
* `devices` (slot): paths to device nodes.

    Example: `devices: [/dev/input/event[0-9], /dev/input/mice]`

* `files` (optional) (slot):
  * `read` (slot): list of files and/or directories for read-only access by the device.

      Example:  `read: [ /dev/input/by-id/* ]`
  * `write` (slot): list of files and/or directories for read/write access by the device.

      Example: `write: [ /etc/file-write, /etc/dir-write ]`
* `read-devices` (optional) (slot): paths to device nodes for read-only access.
    Example: `read-devices: [ /dev/js* ]`
* `udev-tagging` (optional): used to tailor the generated udev rules. Can be one of the following:
  * `kernel`: (mandatory): maps to the string used as the udev `KERNEL==` filter rule.
  * `subsystem`: corresponds to the `SUBSYSTEM==` filters in a udev rule.
  * `environment`: a map of expected environment variables for the udev rule to match with `ENV{...}=="..."`
  * `attributes`: a map of attributes used with `ATTR{...}=="..."`
  * `for-device`: indicates which device the `udev-tagging` snippet refers to

### Code examples

A truncated example showing how the subsystem and attributes can be used:

 ```yaml
    udev-tagging:
      - kernel: hiddev0
        subsystem: usb
        attributes:
          idVendor: "0x03f0" # HP
      - kernel: hiddev1
        subsystem: usb
        attributes:
          idVendor: "0x03fc" # ECS
 ```

An example slot declaration showing the how the kernel environment settings can be used with a custom joystick interface:

```yaml
slots:
  hwdev:
    interface: custom-device
    custom-device: custom-joystick
    devices:
      - /dev/input/js{[0-9],[12][0-9],3[01]}
      - /dev/input/event[0-9]*
    files:
      read:
        - /run/udev/data/c13:{6[5-9],[7-9][0-9],[1-9][0-9][0-9]*}
        - /run/udev/data/c13:{[0-9],[12][0-9],3[01]}
        - /sys/devices/**/input[0-9]*/capabilities/*
    udev-tagging:
      - kernel: input/event[0-9]*
        subsystem: input
        environment:
          ID_INPUT_JOYSTICK: "1"
```

The above example will generate the following udev tags:

```
spec.TagDevice(`KERNEL=="js{[0-9],[12][0-9],3[01]}"`)
spec.TagDevice(`KERNEL=="input/js{[0-9],[12][0-9],3[01]}"`)
spec.TagDevice(`SUBSYSTEM=="input", KERNEL=="input/event[0-9]*", ENV{ID_INPUT_JOYSTICK}=="1"`)
```

The following example shows the `udev-tagging` syntax:

```yaml
   slots:
      v4l:
        interface: custom-device
        devices:
          - /dev/video[0-9]
        files:
          read:
            - /sys/bus/usb/devices
            - /sys/class/video4linux
            - /sys/kernel/debug/sleep_time
          write:
            - /proc/sys/vm/stat_interval
        udev-tagging:
          - kernel: video[0-9]
            subsystem: v4l
            environment:
              var1: foo
              var2: bar
            attributes:
              attr1: one
              attr2: two
```

An additional example, showing how to match udev rules with a device which appears at a different path under `/dev/..`:

```yaml
   slots:
      msr:
        interface: custom-device
        devices:
          - /dev/cpu/[0-9]*/msr
        udev-tagging:
          - kernel: msr[0-9]*
            subsystem: msr
            for-device: /dev/cpu/[0-9]*/msr
```

The above example generates a udev rule to match `KERNEL=="msr[0-9]*", SUBSYSTEM=="msr"` and an AppArmor rule allowing read/write access through `/dev/cpu/[0-9]*/msr`.

The test code can be found in the snapd repository: [https://github.com/canonical/snapd/blob/master/interfaces/builtin/custom_device_test.go](https://github.com/canonical/snapd/blob/master/interfaces/builtin/custom_device_test.go)

The source code for the interface is in the snapd repository:
[https://github.com/canonical/snapd/blob/master/interfaces/builtin/custom_device.go](https://github.com/canonical/snapd/blob/master/interfaces/builtin/custom_device.go)
