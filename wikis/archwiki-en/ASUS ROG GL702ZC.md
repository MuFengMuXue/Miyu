# ASUS ROG GL702ZC

This page is about the Laptop ROG Strix AMD laptop. Runs pretty good out of the box, with some minor issues.

## Backlight
Backlight with  will not work, see Backlight#light.

## Fans
 do not detect any interfaces for fan control. However, fan control through NBFC works well; and there is a profile for this laptop. Enabling and starting the service files, and applying the configurations are sufficient.

## Troubleshooting
## Secure Boot
The BIOS has an utility to load your own BIOS keys; however loading my own keys in the BIOS using the firmware interface did not work.

## Fans turn 100% and computer becomes unresponsive after long idle time
Have not found a fix for this, but reporting this issue nonetheless. This might also indicate a hardware failure: certain power control circuitry can fail and require an RMA for a mainboard replacement.

## Crashes with MCE
The system will sometimes crash (check the Phoronix thread). The problem seems to be the AMD processor. There is no suggested fix other than RMA; you can check if you are affected by running ryzen kill script. My personal experience is that I have two cores that cause these errors; and I had not have it happen much after configuring fans using .

To further investigate, check out Machine-check exception

## Bluetooth and network issues
The Wi-Fi card is of model . Older kernel versions do not have the bluetooth module for this card (>4.19). Also, on 5.2; the rtl cards Wi-Fi modules were merged into ; which was not working for a while. (See my BBS thread here) Currently, Wi-Fi works with the stable kernel; but is noticeably slower than the previous kernel module.
