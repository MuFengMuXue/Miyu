**Orange Pi PC**

[][![An Orange Pi PC](/images/thumb/d/d1/Orangepipc-gentoo.jpg/265px-Orangepipc-gentoo.jpg)](https://wiki.gentoo.org/wiki/File:Orangepipc-gentoo.jpg "An Orange Pi PC")

**Resources**

[[]][Home](http://www.orangepi.org)

[[]][GitHub](https://github.com/orangepi-xunlong)

[[]][[#orangepi](ircs://irc.libera.chat/#orangepi)] ([[webchat](https://web.libera.chat/#orangepi)])

[[]][linux-sunxi wiki](http://linux-sunxi.org/Xunlong_Orange_Pi_PC)

The **Orange Pi PC** is an inexpensive development board from the Orange Pi family. It has a quad-core ARM SoC (Allwinner H3, ARMv7) with 1 GB RAM and uses a microSD(HC) card for storage.

## [Hardware]

### [Component status]

  ------------------------------ ------------- --------------------------------------------------------------------
  Device                         Works         Notes
  CPU: Allwinner H3              Works
  Video: Mali 400MP2             Not tested
  Audio                          Not tested
  Ethernet: 10/100M              Works
  USB Controller (Host)          Works
  USB Controller (OTG)           Not tested
  Camera: CSI Camera interface   Not tested
  SD card reader                 Works
  Hardware monitoring            Partial       Two sensors are detected, but do not provide any sensible readings
  GPIO                           Not tested
  LED control                    Not tested
  IR (Infrared) input            Not tested
  ------------------------------ ------------- --------------------------------------------------------------------

## [Installation]

For installation the u-boot environment and kernel must be built and then written to the microSD card.

Alternatively, an existing bootable Linux image can be used. See the [Quick Start](https://wiki.gentoo.org/wiki/Orange_Pi_PC/Quick_Start "Orange Pi PC/Quick Start") guide.