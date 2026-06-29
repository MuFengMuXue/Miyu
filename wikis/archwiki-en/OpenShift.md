# OpenShift

OpenShift is a Kubernetes distribution from Red Hat. It is a complex piece of software that bundles different pieces (monitoring, console-gui, authentication) together. The aim is to support containers in a productive environment with (paid) support by Red Hat.

## Installation
## Server
OKD is an open source alternative which can be used free of charge, see the upstream documentation.

To just try it out, it is possible to use a pre-configured instance at https://learn.openshift.com. Alternatively, install it in a non-production environment (see below).

## OpenShift v4
Red Hat OpenShift Local can be used to install an OpenShift v4 cluster.

The installation is described in the Getting Started Guide (please check for correct version).
The installation asks for sudo rights (maybe not needed?) and will install an openshift cluster using kvm/libvirt.
Since Arch Linux is not natively supported by the setup procedure, make sure you have the prerequisites installed: , ,  and  or systemd-resolved.
It will add the current user to the libvirt group.
One also needs a secret from cloud.redhat.com (account is needed) that can be obtained in the Red Hat Cloud Console.

The basic steps for installing crc on your computer:

 #untar downloaded archive
 tar -xJf crc-linux-amd64.tar.xz
 #create a bin link so that future versions only need relinking, no new path
 ln -s crc-linux--amd64 bin
 #add bin folder to PATH and restart your terminal so that PATH is updated (or source config file)
 ...
 #create base install of crc takes some minutes (will ask for secret)
 crc setup
 #start openshift cluster
 crc start
 #get credentials of openshift instance
 crc console --credentials
 #open console in webbrowser
 crc console

## Client
 - Provides the  command.

## Tips and tricks
## Troubleshoot network traffic of a container
In Kubernetes, each shares its network layer with other containers in the same pod. You can install a container with tcpdump in the same pod, and then use  to connect to the container and monitor the traffic.

See Using sidecars to analyze and debug network traffic in OpenShift for more details.

## Troubleshoot VM stuck
If the CRC VM stuck in booting check the libvirt logs at . When you see the following error you have to downgrade  to version 202411-1.

See CRC VM stuck in booting state and Fedora Wiki Edk2Security

 !!!! X64 Exception Type - 0E(#PF - Page-Fault)  CPU Apic ID - 00000000 !!!!
 ExceptionData - 0000000000000003  I:0 R:0 U:0 W:1 P:1 PK:0 SS:0 SGX:0
 RIP  - 0000000076BFFCF0, CS  - 0000000000000038, RFLAGS - 0000000000210006
 RAX  - 0000000076C1B000, RCX - 0000000076C1B000, RDX - 0000000000024000
 RBX  - 000000007E25E4C0, RSP - 000000007FE5AEB8, RBP - 000000007EA6BF98
 RSI  - 0000000000000000, RDI - 0000000076C1B000
 R8   - 0000000076C3F000, R9  - 000000007BCC96FD, R10 - 000000007DCDA058
 R11  - 0000000000000077, R12 - 000000007F9EC018, R13 - 000000007E31F000
 R14  - 000000007E25D728, R15 - 000000007E25D730
 DS   - 0000000000000030, ES  - 0000000000000030, FS  - 0000000000000030
 GS   - 0000000000000030, SS  - 0000000000000030
 CR0  - 0000000080010033, CR2 - 0000000076C1B000, CR3 - 000000007FC01000
 CR4  - 0000000000000668, CR8 - 0000000000000000
 DR0  - 0000000000000000, DR1 - 0000000000000000, DR2 - 0000000000000000
 DR3  - 0000000000000000, DR6 - 00000000FFFF0FF0, DR7 - 0000000000000400
 GDTR - 000000007F9D8000 0000000000000057, LDTR - 0000000000000000
 IDTR - 000000007F48F018 0000000000000FFF,   TR - 0000000000000048
 FXSAVE_STATE - 000000007F9D7460
 !!!! Find image based on IP(0x76BFFCF0) (No PDB)  (ImageBase=0000000000DF59E8, EntryPoint=0000000000DF61E7) !!!!
