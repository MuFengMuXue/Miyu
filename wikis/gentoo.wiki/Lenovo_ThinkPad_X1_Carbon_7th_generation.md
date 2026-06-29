**Resources**

[[]][Official Support Page (Whiskey Lake)](https://pcsupport.lenovo.com/us/en/products/laptops-and-netbooks/thinkpad-x-series-laptops/thinkpad-x1-carbon-7th-gen-type-20qd-20qe)

[[]][Official Support Page (Comet Lake)](https://pcsupport.lenovo.com/us/en/products/laptops-and-netbooks/thinkpad-x-series-laptops/thinkpad-x1-carbon-7th-gen-type-20r1-20r2)

[[]][Specifications](https://psref.lenovo.com/syspool/Sys/PDF/ThinkPad/ThinkPad_X1_Carbon_7th_Gen/ThinkPad_X1_Carbon_7th_Gen_Spec.pdf)

[[]][Specifications (by region)](https://psref.lenovo.com/Product/ThinkPad/ThinkPad_X1_Carbon_7th_Gen)

[[]][Hardware Maintenance Manual](https://download.lenovo.com/pccbbs/mobiles_pdf/tp_x1yoga_x1carbon_hmm_en.pdf)

[[]][User Guide](https://download.lenovo.com/pccbbs/mobiles_pdf/x1yoga_x1carbon_ug_v2_en.pdf)

[[]][BIOS Setup](https://download.lenovo.com/pccbbs/mobiles_pdf/lenovo_bios_setup_linux_wmi_sysfs_1.2.pdf)

[[]][ThinkPad X1 series](https://en.wikipedia.org/wiki/ThinkPad_X1_series "wikipedia:ThinkPad X1 series")

These are my notes on getting Gentoo fully functional on the Lenovo X1 Carbon, 7th generation.

## Contents

-   [[1] [Kernel]](#Kernel)
    -   [[1.1] [Storage]](#Storage)
    -   [[1.2] [Touchpad]](#Touchpad)
-   [[2] [External resources]](#External_resources)

## [Kernel]

### [Storage]

[KERNEL]

    Device Drivers --->
       NVME Support --->
         <*> NVM Express block device

### [Touchpad]

Enable the following options to get the touchpad working:

[KERNEL]

    Processor type and features --->
       [*] Intel Low Power Subsystem Support
     Device Drivers --->
       Input device support --->
         [*] Mice --->
           <*> Synaptics I2C Touchpad support
         <*> Synaptics RMI4 bus support
         <*>   RMI4 I2C Support
         <*>   RMI4 SMB Support
         [*]   RMI4 Function 03 (PS2 Guest)
         [*]   RMI4 Function 11 (2D pointing)
         [*]   RMI4 Function 30 (GPIO LED)
         [*]   RMI4 Function 34 (Device reflash)
         [*]   RMI4 Function 54 (Analog diagnostics)
         -*-   RMI4 Function 55 (Sensor tuning)
       I2C Support --->
         -*- I2C support
            I2C Hardware Bus support --->
              <*> Intel 82801 (ICH/PCH)
              <*> SMBus Control Method Interface
              <*> Synopsys DesignWare Platform
              <*> Synopsys DesignWare PCI
       -*- Pin controllers --->
         <*> Intel Canon Lake PCH pinctrl and GPIO driver
       Multifunction device drivers --->
         <*> Intel Low Power Subsystem support in ACPI mode
         <*> Intel Low Power Subsystem support in PCI mode
       HID support
         -*- HID support
         <*> Generic HID driver
             Special HID drivers --->
               <*> Lenovo / ThinkPad devices
               <*> HID Multitouch panels
       [*] DMA Engine support --->
         <*> Intel integrated DMA 64-bit support
         -*- Synopsys DesignWare AHB DMA PCI driver
       [*] X86 Platform Specific Device Drivers --->
         <*> ThinkPad ACPI Laptop Extras
         <*> WMI
         <*>   WMI embedded Binary MOF driver

## [External resources]

-   [https://wiki.archlinux.org/title/Lenovo_ThinkPad_X1_Carbon\_(Gen_7)](https://wiki.archlinux.org/title/Lenovo_ThinkPad_X1_Carbon_(Gen_7))