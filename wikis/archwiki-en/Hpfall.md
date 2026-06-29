# Hpfall

hpfall is a simple daemon providing HDD shock protection for HP laptops supporting the feature officially called "HP Mobile Data Protection System 3D" or "HP 3D DriveGuard".

## Installation
Install .

## Configuration
You need to set your hard drive in the configuration file:

Start and enable

## Testing
After rebooting with new kernel, check if  was initialized correctly through the journal.

## Testing Shock protection
Find your HDD's unload_heads file:

Go to its directory and run:

Lift your laptop into free space and simulate a free fall while holding it firmly with your hands (~10 cm should be enough).
If the disk protection works, you should hear your HDD making "click" sound and see one of your laptop's LEDs flashing. The watch value's background should also permanently turn black.
