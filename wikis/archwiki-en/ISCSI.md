# ISCSI

With iSCSI you can access storage over an IP-based network.

The exported storage entity is the target and the importing entity is the initiator.

Since Linux 2.6.38 LIO is the in-kernel iSCSI target.
Before that it was tgt. SCST was another candidate for kernel inclusion.https://lwn.net/Articles/424004/

The current initiator is Open-iSCSI.

It is possible to boot Arch Linux via iSCSI.
