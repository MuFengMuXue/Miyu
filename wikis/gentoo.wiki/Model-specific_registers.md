[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Model-specific_registers&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Official documentation](https://man7.org/linux/man-pages/man4/msr.4.html)

[Model-specific registers](https://en.wikipedia.org/wiki/Model-specific_register) are [processor registers](https://en.wikipedia.org/wiki/Processor_register) in the x86 system architecture that can be used for debugging, monitoring, and toggling of features.

### [Kernel]

To enable access to MSRs in the kernel:

[KERNEL] **menuconfig**

    Processor type and features  --->
        <*> /dev/cpu/*/msr - Model-specific register support

Note that enabling either of the kernel [lockdown](https://wiki.gentoo.org/wiki/Security_Handbook/Kernel_security/Kernel_Lockdown "Security Handbook/Kernel security/Kernel Lockdown") modes requires disabling access to MSRs.

## [External resources]

-   [https://en.wikipedia.org/wiki/Control_register](https://en.wikipedia.org/wiki/Control_register)
-   [https://wiki.osdev.org/Model_Specific_Registers](https://wiki.osdev.org/Model_Specific_Registers)
-   [x86 architecture model specific registers](https://sandpile.org/x86/msr.htm)
-   [Intel® 64 and IA-32 Architectures Software Developer's Manual, Volume 4: Model-Specific Registers](https://software.intel.com/content/www/us/en/develop/download/intel-64-and-ia-32-architectures-software-developers-manual-volume-4-model-specific-registers.html)
-