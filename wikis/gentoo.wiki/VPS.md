[]  As of **March 13th, 2017**, the information in this article is probably **outdated**. You can help the Gentoo community by verifying and [updating this article](https://wiki.gentoo.org/index.php?title=VPS&action=edit).

Basic virtualization concepts are explained in this overview article.

## Contents

-   [[1] [Concepts]](#Concepts)
    -   [[1.1] [Methodology]](#Methodology)
    -   [[1.2] [Virtual machines]](#Virtual_machines)
    -   [[1.3] [Para-virtualized machines]](#Para-virtualized_machines)
    -   [[1.4] [OS-level virtualization]](#OS-level_virtualization)
    -   [[1.5] [Conclusion]](#Conclusion)
-   [[2] [Usage scenarios]](#Usage_scenarios)
    -   [[2.1] [Improved security]](#Improved_security)
    -   [[2.2] [Server consolidation]](#Server_consolidation)
    -   [[2.3] [Development and testing]](#Development_and_testing)

## [Concepts]

### [Methodology]

Virtualization is a framework or methodology of dividing the resources of a computer into multiple execution environments. Virtualization techniques create multiple isolated partitions (Virtual Machines (VM) or Virtual Private Servers (VPS)) on a single physical server. There are several kinds of virtualization techniques which provide similar features but differ in the degree of abstraction and the methods used for virtualization.

### [Virtual machines]

Virtual Machines emulate some real or fictional hardware, which in turn requires real resources from the Host (the machine running the VMs). This approach, used by most System Emulators, allows the emulator to run an arbitrary Guest Operating System without modifications because OS isn\'t aware that it's not running on real hardware. The main issue with this approach is that some CPU instructions require additional privileges and may not be executed in user space thus requiring a Virtual Machines Monitor (VMM) to analyze executed code and make it safe on-the-fly. Hardware Emulation approach is used by VMware products and Microsoft Virtual Server.

### [Para-virtualized machines]

This technique also requires a VMM, but most of its work is performed in the Guest OS code, which in turn is modified to support this VMM and avoid unnecessary use of privileged instructions. The paravirtualization technique also enables running different OSs on a single server, but requires them to be ported. The paravirtualization approach is used by Xen, UML.

### [OS-level virtualization]

Most applications running on a server can easily share a machine with others, if they could be isolated and secured. Further, in most situations, different operating systems are not required on the same server, merely multiple instances of a single Operating System. OS Virtualization systems have been designed to provide the required isolation and security to run multiple applications or copies of the same (or similar i.e different Linuxes) OS on the same server. OpenVZ, Linux-VServer are examples of OS virtualization.

### [Conclusion]

The three techniques differ in complexity of implementation, breadth of OS support, performance in comparison with standalone server, and level of access to common resources. For example, VMs have wide scope of usage, but poor performance. Para-VMs have better performance, but can support fewer OSs because of need to port original OSes.

Virtualization on the OS Level provides the best performance and scalability compared to other approaches. Performance of such systems can differ only about 1-3% from standalone server. They are also much simpler to administer as all of the Virtual servers can be accessed and administered from the host. Generally, such systems are best choice for server consolidation of same OS workloads.

## [Usage scenarios]

### [Improved security]

Consider a Linux server used to serve mail, web site, and DNS. There are at least three different applications listening to and handling network requests, and any of them can contain security holes. Using Virtualization, a server can be divided into three VPSs, one for each application. Thus, if the DNS server is compromised, the other applications will still be left intact due to complete isolation between VPSs.

### [Server consolidation]

Having a separate physical server for each application is generally a good approach, it increases availability and improves security. However, separate servers lead to increased costs of hardware and collocation, and modern hardware is often underutilized in this scenario.

With Virtualization, you can enjoy the benefits of dedicated server without such drawbacks. Create a VPS for each application and use the existing hardware more efficiently. This approach can be deployed totally transparently to your users.

### [Development and testing]

Developers often need access to several different Linux distributions to develop an application. Testing also needs to be performed on various software configurations. Therefore, testing and development groups often require a lot of hardware. Alternatively, using Virtualization developers and QAs can create multiple partitions with different Linux distributions and configurations residing on one physical server. Each VPS can have its own set of packages, system libraries, configuration files.

\

Authorship information[]

This page is based on a document formerly found on [gentoo.org](https://www.gentoo.org/).\
The following people contributed to the original document: **Benedikt Boehm (author), OpenVZ.org (by courtesy) on June 19, 2006**\
\
*[Editors: please do **not** add yourself here. Contributions are recorded on each article\'s associated history page, this list is only present to preserve authorship information, as wiki history does not allow for any external attribution.]*