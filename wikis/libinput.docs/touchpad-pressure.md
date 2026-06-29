# Touchpad pressure-based touch detection

libinput uses the touchpad pressure values and/or touch size values to detect whether a finger has been placed on the touchpad. This is `kernel_pressure_information` and combines with a libinput-specific hardware database to adjust the thresholds on a per-device basis. libinput uses these thresholds primarily to filter out accidental light touches but the information is also used for some `palm_detection`.

Most devices only support one of either touch pressure or touch size. libinput uses whichever is available but a preference is given to touch size as it provides more specific information. Since most devices only provide one type anyway, this internal preference does not usually matter.

Pressure and touch size thresholds are **not** directly configurable by the user. Instead, libinput provides these thresholds for each device where necessary. See `touchpad_pressure_hwdb` for instructions on how to adjust the pressure ranges and `touchpad_touch_size_hwdb` for instructions on how to adjust the touch size ranges.

## Information provided by the kernel

The kernel sends multiple values to inform userspace about a finger touching the touchpad. The most basic is the `EV_KEY/BTN_TOUCH` boolean event that simply announces physical contact with the touchpad. The decision when this event is sent is usually made by the kernel driver and may depend on device-specific thresholds. These thresholds are transparent to userspace and cannot be modified. On touchpads where pressure or touch size is not available, libinput uses `BTN_TOUCH` to determine when a finger is logically down.

Many contemporary touchpad devices provide an absolute pressure axis in addition to `BTN_TOUCH`. This pressure generally increases as the pressure increases, however few touchpads are capable of detecting true pressure. The pressure value is usually related to the covered area - as the pressure increases a finger flattens and thus covers a larger area. The range provided by the kernel is not mapped to a specific physical range and often requires adjustment. Pressure is sent by the `ABS_PRESSURE` axis for single-touch touchpads or `ABS_MT_PRESSURE` on multi-touch capable touchpads. Some devices can detect multiple fingers but only provide `ABS_PRESSURE`.

Some devices provide additional touch size information through the `ABS_MT_TOUCH_MAJOR/ABS_MT_TOUCH_MINOR` axes and/or the `ABS_MT_WIDTH_MAJOR/ABS_MT_WIDTH_MINOR` axes. These axes specify the size of the touch ellipse. While the kernel documentation specifies how these axes are supposed to be mapped, few devices forward reliable information. libinput uses these values together with a device-specific `device-quirks` entry. In other words, touch size detection does not work unless a device quirk is present for the device.
