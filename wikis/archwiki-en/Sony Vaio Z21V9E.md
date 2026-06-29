# Sony Vaio Z21V9E

## Installation
The only real hurdle with getting Arch Linux installed is the RAID configuration. There are several alternatives with various advantages and disadvantages. The easiest is to just leave the raid enabled as per factory settings and treat the resulting partition as a single drive.

As you can see the system contains two separate drives which have been used to create a single RAID partition, raid0. When preparing your storage drive during installation, you would then treat that raid0 partition as the drive to install on.

Alternatively, just disable the IRST and treat the two SSD drives separately.
