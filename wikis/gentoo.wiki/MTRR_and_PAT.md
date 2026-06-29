## Contents

-   [[1] [MTRR(Memory Type Range Register) and PAT (Page Attribute Table)]](#MTRR.28Memory_Type_Range_Register.29_and_PAT_.28Page_Attribute_Table.29)
-   [[2] [MTRR]](#MTRR)
-   [[3] [Enable MTRR and Reg clean-up]](#Enable_MTRR_and_Reg_clean-up)
-   [[4] [PAT Newer systems]](#PAT_Newer_systems)
-   [[5] [Testing and Debugging]](#Testing_and_Debugging)

## [][MTRR(Memory Type Range Register) and PAT (Page Attribute Table)]

The MTRR and PAT are some of the same but are different in how they deal with memory. PAT is designed to replace the old method of MTRR but is only available on newer generation hardware as the CPU is required to support PAT. The Memory Type Range Register as it\'s name suggests registers the available memory in a ordered way for applications and drivers to access it. The MTRR can then set specific range of memory to different attributes such as cached, write-back, write-through and so on to increase performance of particular tasks on a computer.

PAT on the other hand uses the similar registers to MTRR but then creates a table which allocates memory inside the registered locations set by MTRR. MTRR and PAT therefore go hand in hand and it has been said that in the future MTRR will be replaced by PAT so enabling PAT in the kernel will handle the small task of ranging the memory into a register and create the allocation tables rather than be seen as two entities.

## [MTRR]

This feature had been placed in processors due to memory sizes becoming bigger and bigger. There had to be a way that the memory could be allocated, addressed and used more effectively.

A main feature of the MTRR is to map locations of PCI or AGP memory components in your system so that software and drivers could access them quickly and efficiently, much like partitioning ones hard disk to better manage the free space.

To check if your processor(s) have this feature you can type:

`root `[`#`]` cat /proc/cpuinfo | grep mtrr `

This will show if your CPU is capable of utilising range registers. If your processor does support it then you can:

`root `[`#`]` cat /proc/mtrr `

and view the output of the registers and how they have been allocated and set. For those that have either a PCI(e) or AGP graphics card installed you should view the registered memory lines showing as write-back enabled. If not then you may not have the Reg-Cleanup setup in your kernel or you have the newer PAT supported hardware.

## [Enable MTRR and Reg clean-up]

Kernel setup for MTRR and reg clean-up is simple in the kernel config and compile process.

`root `[`#`]` cd /usr/src/linux `

The enter the kernel menu configurator:

`root `[`#`]` make menuconfig `

[KERNEL]

    Processor type and features  --->
        [*] MTRR (Memory Type Range Register) support
         [*]   MTRR cleanup support
         (1)     MTRR cleanup enable value (0-1)
         (1)     MTRR cleanup spare reg num (0-7)

To understand the memory cleanup spare reg num we need to look at the output from the cat /proc/mtrr command above, the displayed list will show the registered range allocated for your graphics card and start with the Reg(number). It is usually Reg01 but your maybe different depending on your hardware. This reg number can be entered into the MTRR cleanup spare reg num in the kernel so that it can be setup and controlled by the graphics driver and configured to operate in a optimised fast write-back mode. It is called cleanup as the graphics driver can clean any data stored in that range and write data to it for it\'s own use.

Once this has been changed and or enabled you can proceed to building your kernel and installing it.

`root `[`#`]` mount /boot `

`root `[`#`]` make && make modules_install && make install `

## [PAT Newer systems]

Check to see if your system supports PAT.

`root `[`#`]` cat /proc/cpuinfo | grep pat `

If you have this feature on your system then enable it in the kernel. Currently it is part of the MTRR and you need enable MTRR to enable PAT as PAT uses the setup of the MTRR to range the memory into registers before creating a PA Table. If your system in 64Bit then you most certainly have PAT support.

\

[KERNEL]

    Processor type and features  --->
        [*] MTRR (Memory Type Range Register) support
         [*]   MTRR cleanup support
         (1)     MTRR cleanup enable value (0-1)
         (1)     MTRR cleanup spare reg num (0-7)
        [*]   x86 PAT support

Of course once set build and install your newly configured kernel:

`root `[`#`]` mount /boot `

`root `[`#`]` make && make modules_install && make install `

## [Testing and Debugging]

There are many ways we can use to peek into the memory type range registers and PA Table. We can cat the proc filesystems relevant folders to see what is going on.

The first thing that needs to be enabled in your Kernel to be able to view the MTRR/PAT is the Debug File System. Sounds like an option you would want to use for debuging a filesystem but it is far more than that. We enable this by enabling the option in the kernel

[KERNEL]

    Kernel hacking
        [*] Debug filesystem

Build and install the newly configured kernel and we should now have access to the MTRR and PAT in the /proc folder.

\

`root `[`#`]` mount /boot `

`root `[`#`]` make && make modules_install && make install `

We can view the relevant data we wish to see by mounting the debug filesystem and catonating the contents.

`root `[`#`]` mount -t debugfs debugfs /sys/kernel/debug `

And the view its contents:

`root `[`#`]` cat /sys/kernel/debug/x86/pat_memtype_list `

You should now be able to see the entire table the PAT has allocated and registered inside the reg cleaned up register. It should contain all the write-back, write-cached, write-through memory regions including that of your graphics card etc.

\
Further reading can be found in the Linux Kernel doccumentation here:

Kernel documentation of PAT [PAT Page Attribute table Kernel](https://www.kernel.org/doc/Documentation/x86/pat.txt)

Kernel documentation of MTRR [MTRR Memory Type Range Register Kernel](https://www.kernel.org/doc/Documentation/x86/mtrr.txt)