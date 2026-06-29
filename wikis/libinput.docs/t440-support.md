# Lenovo \*40 series touchpad support

The Lenovo \*40 series emulates trackstick buttons on the top part of the touchpads.

## Overview

The Lenovo \*40 series introduced a new type of touchpad. Previously, all laptops had a separate set of physical buttons for the [trackstick](http://en.wikipedia.org/wiki/Pointing_stick). This series removed these buttons, relying on a software emulation of the top section of the touchpad. This is visually marked on the trackpad itself, and clicks can be triggered by pressing the touchpad down with a finger in the respective area:

<figure class="align-center">
<img src="top-software-buttons.svg" alt="top-software-buttons.svg" />
<figcaption>Left, right and middle-button click with top software button areas</figcaption>
</figure>

This page only covers the top software buttons, the bottom button behavior is covered in `Clickpad software buttons`.

Clickpads with a top button area are marked with the [INPUT_PROP_TOPBUTTONPAD](https://www.kernel.org/doc/Documentation/input/event-codes.txt) property.

## Size of the buttons

The size of the buttons matches the visual markings on this touchpad. The width of the left and right buttons is approximately 42% of the touchpad's width, the middle button is centered and assigned 16% of the touchpad width.

The line of the buttons is 5mm from the top edge of the touchpad, measurements of button presses showed that the size of the buttons needs to be approximately 10mm high to work reliable (especially when using the thumb to press the button).

## Button behavior

Movement in the top button area does not generate pointer movement. These buttons are not replacement buttons for the bottom button area but have their own behavior. Semantically attached to the trackstick device, libinput re-routes events from these buttons to appear through the trackstick device.

The top button areas work even if the touchpad is disabled but will be disabled when the trackstick device is disabled. If the finger starts inside the top area and moves outside the button area the finger is treated as dead and must be lifted to generate future buttons. Likewise, movement into the top button area does not trigger button events, a click has to start inside this area to take effect.

## Kernel support

The firmware on the first generation of touchpads providing top software buttons is buggy and announces wrong ranges. [Kernel patches](https://lkml.org/lkml/2014/3/7/722) are required; these fixes are available in kernels 3.14.1, 3.15 and later but each touchpad needs a separate fix.

The October 2014 refresh of these laptops do not have this firmware bug anymore and should work without per-device patches, though [this kernel commit](http://git.kernel.org/cgit/linux/kernel/git/torvalds/linux.git/commit/?id=02e07492cdfae9c86e3bd21c0beec88dbcc1e9e8) is required.

For a complete list of supported touchpads check [the kernel source](http://git.kernel.org/cgit/linux/kernel/git/torvalds/linux.git/tree/drivers/input/mouse/synaptics.c) (search for "topbuttonpad_pnp_ids").
