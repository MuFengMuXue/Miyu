# Oolite

Oolite is a space trading / simulation game based on the well-known Elite game from the 80's.

## Installation
Install the  package.

## Troubleshooting
Oolite uses shaders extensively which may not work well with all drivers, especially the gallium OSS drivers.

By default Oolite starts with full shaders, if it hangs on the title screen follow these 3 steps:

## Testing for shader problem
Run Oolite from terminal with this command:

 $ LIBGL_ALWAYS_INDIRECT=1 oolite

If Oolite works, the problem is with the shaders. In case this does not help, you have a different problem. Post about this on the Arch Linux forums or register a bug.

## Verify which setting works
Edit  and look for these lines at the bottom:

 shader-mode
 	3

Try changing the value of this key to 2 and 1 and test if Oolite runs normally (whithout setting ).

## Feedback
For the value of shader-mode that works, please post  on the Oolite forum, along with the highest shader-mode value that works for you.

This info will be used to determine the correct default shader setting for Oolite for your card/driver combination. This will then become part of the Oolite graphics configuration data in a later version.
