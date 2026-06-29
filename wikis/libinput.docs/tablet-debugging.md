# Debugging tablet issues

## Required tablet capabilities

To handle a tablet correctly, libinput requires a set of capabilities on the device. When these capabilities are missing, libinput ignores the device and prints an error to the log. This error messages reads

    missing tablet capabilities: xy pen btn-stylus resolution. Ignoring this device.

or in older versions of libinput simply:

    libinput bug: device does not meet tablet criteria. Ignoring this device.

When a tablet is rejected, it is usually possible to verify the issue with the `libinput record` tool.

- **xy** indicates that the tablet is missing the `ABS_X` and/or `ABS_Y` axis. This indicates that the device is mislabelled and the udev tag `ID_INPUT_TABLET` is applied to a device that is not a tablet. A bug should be filed against [systemd](http://github.com/systemd/systemd).
- **pen** or **btn-stylus** indicates that the tablet does not have the `BTN_TOOL_PEN` or `BTN_STYLUS` bit set. libinput requires either or both of them to be present. This indicates a bug in the kernel driver or the HID descriptors of the device.
