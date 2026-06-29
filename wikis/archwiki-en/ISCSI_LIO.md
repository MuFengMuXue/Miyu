# ISCSI/LIO

LIO (LinuxIO) is the in-kernel iSCSI target (since Linux 2.6.38).

## Installation
The iSCSI target fabric is included since Linux 3.1.

The important kernel modules are target_core_mod and iscsi_target_mod, which should be in the kernel and loaded automatically.

It is highly recommended to use the free branch versions of the packages: ,  and .

Start/enable the , included in , to load necessary modules, mount the configfs and load previously saved iSCSI target configuration.

## targetcli
Run  as root to see some information about the running configuration.

You can use targetcli to create the whole configuration, see .

The configuration shell creates most names and numbers for you automatically, but you can also provide your own settings.
At any point in the shell you can type  in order to see what commands you can issue here.

After starting the target (see above) you enter the configuration shell with
In this shell you include a block device (here: ) to use with

 /> cd backstores/block
 /backstores/block> create md_block0 /dev/disk/by-id/md-name-nas:iscsi

You then create an iSCSI Qualified Name (IQN) and a target portal group (TPG) with:

 ...> cd /iscsi
 /iscsi> create

In order to tell LIO that your block device should get used as backstore for the target you issue

 .../tpg1> cd luns
 .../tpg1/luns> create /backstores/block/md_block0

Then you need to create a portal, making a daemon listen for incoming connections:

 .../luns/lun0> cd ../../portals
 .../portals> create

Targetcli will tell you the IP and port where LIO is listening for incoming connections (defaults to 0.0.0.0 (all)).
You will need at least the IP for the clients. The port should be the standard port 3260.

In order for a client/initiator to connect you need to include the IQN of the initiator in the target configuration:

 ...> cd ../../acls
 .../acls> create iqn.2005-03.org.open-iscsi:SERIAL

Instead of  you use the IQN of an initiator.
It can normally be found in .
You have to do this for every initiator that needs to connect.
Targetcli will automatically map the created LUN to the newly created ACL.

The last thing you have to do in targetcli when everything works is saving the configuration with:

 ...> cd /
 /> saveconfig

The will the configuration in .
You can now safely start and stop  without losing your configuration.

## Authentication
Authentication per CHAP is enabled per default for your targets.
You can either setup passwords or disable this authentication.

## Disable authentication
Navigate targetcli to your target (i.e. /iscsi/iqn.../tpg1) and:

 .../tpg1> set attribute authentication=0

## Set credentials
Navigate to a certain ACL of your target (i.e. /iscsi/iqn.../tpg1/acls/iqn.../) and

 ...> get auth

will show you the current authentication credentials.

 ...> set auth userid=
 ...> set auth password=
 ...> set auth mutual_userid=  (optional)
 ...> set auth mutual_password=  (optional)

The first two fields are the username and password of the target. The initiator will use this to log into the target. The last two fields (prefixed with "mutual_") are the username and password of the initiators (note that all initiators will have the same username and password). These two are optional parameters and it ensures that initiators will only accept connections from permitted targets.

## Tips and tricks
* With  you can list the current open sessions.
