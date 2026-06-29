# ASUS KCMA-D8

This page describes the steps necessary to get most out of the ASUS KCMA-D8 hardware. It assumes that you have already successfully installed Arch Linux.

## BIOS
The manufacturers BIOS is outdated, has no NVMe drivers and is closed source. To remedy this, we can install a precompiled open source coreboot distribution, coreboot-15h.

The stock BIOS prevents you from flashing it with a non-OEM BIOS, so the first flash must be done via hardware. The easiest way to install coreboot-15h for the first time is with a Raspberry Pi, connecting the bios chip to the GPIO as seen here. Install flashrom on the Pi with , download and extract the latest  image from the KCMA-D8 page, and then follow the how to use flashprog instructions to backup and flash the BIOS (replacing  with ). Make sure to clear the CMOS before booting with the new BIOS. Setting  in the command flags is recommended to improve stability and reliability.

Once coreboot-15h has been installed, it can be updated from within the operating system by installing  and following these instructions (replacing  with ).

The stock BIOS chip is 2MiB, and can be upgraded to a 16MiB one such as the  or the  with a . This will allow more space for larger payloads in the future, but isn't strictly necessary.

Libreboot will be implementing coreboot-15h soon, and this will be an alternative up-to-date coreboot distribution.

## Sensors
After running , it loads the incorrect kernel driver . This can be remediated by replacing  with  in lm_sensors configuration file:

The enumerated hwmon symlinks located in  may vary in order after a power cycle, because the kernel modules do not load in a consistent order every boot. Something as simple as plugging in a game controller could cause the order to change. Creating/editing  in such a manner should create a defined order for the modules to load in, which should make the hwmon paths stay where they are and not change order upon reboot:

This method may not always work consistently, and a more reliable method should be documented and implemented.

## Fan control
Fan control in this motherboard is quite unusual. There is 8 PWM fan control channels, however only 2 channels are used for controlling the fan speed of all 8 fan headers. One must use a combination of 4 pin fans (recommended for CPU), and 3 pin fans (recommended for case). One speed can be set for all of the 4 pin fans, and another speed can be set for all of the 3 pin fans. After running ,  refuses to start. This is because fancontrol cannot associate more than 2 fans with PWM speed. Manually configure  so that  only has two inputs per device, and restart . Here is an example configuration:

## Gaming Boost Clocks
Gaming on the KCMA-D8 is quite attainable with a pair of Opteron 4332 HE / 4386 CPU's and some 1333-1600MHz RAM. However, there are a few things you can do to improve the experience. For example, the 4386's all core max turbo is 3.1GHz, however they can boost to 3.8GHz on 2 cores 4 threads (2 modules) when the other 2 cores 4 threads (2 modules) are not as busy. Since these CPU's have plenty of threads, we can simply disable half of the cores/modules and get a massive single threaded boost. The recommended way to do this is with .

Keep in mind that inter-CPU communication introduces latency that isn't usually desirable for games, so restricting all of the game threads and memory to run on NUMA node 0 is often desirable. See  for setting NUMA affinity.

## IPMI Module
This motherboard supports an ASMB4 IPMI Module. The manufacturers ROM for the IPMI module is massively insecure and has incompatibilities with coreboot. See 15h.org's AST2050 page for their compatible open source BMC firmware replacement.
