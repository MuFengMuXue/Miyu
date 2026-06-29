# Tp-battery-mode

tp-battery-mode is a module to easily switch your Thinkpad's battery charging mode to prolong battery lifetime using .

## Installation
Install the  package.

## Features
Your Thinkpad's default behavior is to start charging its battery as soon as it drops below 100% capacity and stop charging once it is at 100% capacity. Switching your battery charging mode changes these start & stop threshold. tp-battery-mode's default values can be found in

 START_THRESHOLD=85
 STOP_THRESHOLD=90

These values mean that your battery will start charging once the capacity drops below 85% and stop charging once it has reached 90% capacity. This should prolong your battery's lifespan while still giving you ample charge for portable needs.

## Prolong Battery Lifetime
Switching to these new charging thresholds is as simple as enabling and starting

You can tailor the start/stop thresholds to fit your needs by modifying . If you modify these values, you will need to restart the tp-battery-mode service otherwise the changes will not be reflected until you reboot.

## Reverting to default charging behavior
Sometimes you might want to charge your battery all the way to 100% If you wish to revert to the default Thinkpad charging behavior, you just need to stop

If you wish to revert to the default Thinkpad charging behavior completely, you will also need to disable
