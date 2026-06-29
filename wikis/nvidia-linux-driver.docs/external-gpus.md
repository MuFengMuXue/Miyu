## Chapter 37. Configuring External and Removable GPUs

This driver release supports the use of external GPUs, or eGPUs, such as those commonly connected via Thunderbolt. However, system stability when an eGPU is unplugged while in use (also known as "hot-unplug") is not guaranteed. This includes situations where the eGPU is being used to display the X11 desktop.

External GPUs are often used in short-running compute scenarios, which better tolerate the eGPU being hot-unplugged. In such cases, a different GPU may be used to display the X11 desktop.

To prevent system instability from hot-unplugging an eGPU while being used to display the X11 desktop, the NVIDIA X driver does not configure X screens on external GPUs by default.

This behavior may also apply to GPUs attached to internal PCIe slots with hot-unplug support, such as in some enterprise systems.

To override this behavior in xorg.conf, see [`Option "AllowExternalGpus" "boolean"`](xconfigoptions.html#AllowExternalGpus). Then, external GPUs may be configured with X as one would any other secondary GPU, by specifying the BusID in the Device section in xorg.conf. See the xorg.conf man page for more information on the BusID option, and [“What is the format of a PCI Bus ID?”](faq.html#busid) for information on how to determine the BusID.
