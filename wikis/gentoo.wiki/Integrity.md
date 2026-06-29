Integrity is a [Gentoo Hardened](https://wiki.gentoo.org/wiki/Hardened_Gentoo "Hardened Gentoo") subproject aiming for the integration of off-line system integrity technologies within Gentoo.

This project will support the Linux IMA/EVM technology within Gentoo Linux, which perform integrity checks during boot. The primary focus is to prevent tampering of files, settings and images: when this occurs, the boot-up of the system detects the tampering and refuses to load further (or report this to the administrator). The project will support the necessary kernel patches, utilities and documentation. The goal is to make off-line integrity checks, compliance checks and reporting available to the wider public.

Next to the integrity subsystem within Linux (IMA/EVM), this project will also support the various trusted computing technologies (such as TPM support) through well-documented guides and tools.

## Contents

-   [[1] [Integrity resources]](#Integrity_resources)
    -   [[1.1] [About IMA and EVM]](#About_IMA_and_EVM)
    -   [[1.2] [Intrusion Detection Systems]](#Intrusion_Detection_Systems)
-   [[2] [Limitations]](#Limitations)
-   [[3] [See also]](#See_also)

## [Integrity resources]

### [About IMA and EVM]

-   [Introduction and Concepts](https://wiki.gentoo.org/wiki/Integrity/Concepts "Integrity/Concepts") gives a high-level introduction to system integrity and some of the involved technologies

### [Intrusion Detection Systems]

-   [AIDE](https://wiki.gentoo.org/wiki/AIDE "AIDE") is the *Advanced Intrusion Detection Environment* and is a simple yet powerful method for online or offline integrity scanning.

## [Limitations]

Online tampering detection support is a later goal. Other integrity-related technologies, compliance checks and reporting technologies will also be supported sometime in the future. Also see [qcheck](https://wiki.gentoo.org/wiki/Q_applets#Verifying_package_integrity_.28qcheck.29 "Q applets") for portage related on-line integrity checking.

## [See also]

-   [System Integrity subproject page](https://wiki.gentoo.org/wiki/Project:Integrity "Project:Integrity")
-   [Integrity Measurement Architecture](https://wiki.gentoo.org/wiki/Integrity_Measurement_Architecture "Integrity Measurement Architecture") --- is responsible for calculating the hashes of files and programs before they are loaded