# Hard Drive Active Protection System

Hard Drive Active Protection System (HDAPS) protects your hard drive from sudden shocks (such as dropping or banging your laptop on a desk). It does this by parking the disk heads, so that shocks do not cause them to crash into the drive's platters. Hopefully, this will prevent catastrophic failure.

## Shock detection
Your hardware needs to support some kind of shock detection.  This is usually in the form of an accelerometer built into your laptop's motherboard.  If you have the hardware, you also need a way to communicate what the hardware is detecting to your operating system.  This section describes drivers to communicate the accelerometer's state to the OS so it can detect and protect against shocks.

## tp_smapi
tp_smapi is a set of drivers for many ThinkPad laptops.  It is highly recommended if you have a supported ThinkPad, even if you do not plan to use HDAPS.  Among a plethora of other useful things, tp_smapi represents the accelerometer output as joystick devices .

Install . After a reboot, this will activate most of the drivers, represented through the  filesystem.

The kernel provides its own HDAPS drivers. The  package installs  to /lib/modules/$(uname -r)/updates, which will let it supersede the built-in module.  Thus, you can simply add  to your  array.

## Invert module parameter
For some ThinkPads, the invert module parameter is needed in order to handle the X and Y rotation axes correctly. In that case, you can add the option in :

 options hdaps invert=1

 is an example value used for a ThinkPad T410. The invert option takes the following values:

* invert=1 invert both X and Y axes;
* invert=2 invert the X axes (uninvert if already both axes inverted)
* invert=4 swap X and Y (takes place before inverting)

Note that options can be summed. For instance, invert=5 swaps the axes and inverts them. The maximum value of invert is obviously 7. If you do not know which option is correct for you, just try them out with hdaps-gl or some other GUI (see below). Alternatively, you can determine the exact value for your thinkpad model from this table under the column labelled "HDAPS axis orientation".

As an alternative to reloading the  module, the  value can also be written directly to .

## Shock protection
Now that your hardware is reporting its shock detection to the OS, we need to do something with this data. This section describes software utilities to transform the sensor output into shock protection.

## hdapsd
hdapsd monitors the output of the HDAPS joystick devices to determine if a shock is about to occur, then tells the kernel to park the disk heads.

You should check your "Load cycle count" in SMART when setting up hdaps, if it is too sensitive the head would park too often and load cycle count would rise too rapidly.

Install . You can start hdapsd with , however you do not need to enable it.

The package installs udev rules. Udev will start one hdapsd instance for each rotational, non-removable disk it finds.
For more information, see the hdapsd github page.

It may be desirable to tweak the parameters used by hdaspd. Edit  and add e.g  to the parameters.

## GUI Utilities
Utilities exist to monitor hdapsd's status so you know what is going on while you are using your laptop. These are entirely optional.
