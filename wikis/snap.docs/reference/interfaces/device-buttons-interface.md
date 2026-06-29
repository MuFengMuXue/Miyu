#  device-buttons interface

`device-buttons` allows read and write access to device buttons exposed as input events. Such buttons can be defined using `gpio-keys` inside the device tree bindings. Consult kernel documentation on [gpio-keys](https://www.kernel.org/doc/Documentation/devicetree/bindings/input/gpio-keys.txt) for more details.

The interface can access `/dev/input/event*` devices that are udev marked with `ID_INPUT_KEY=1` but are not keyboards (`ID_INPUT_KEYBOARD!=1`).

**Auto-connect**: no

Requires snapd version _2.37+_.
