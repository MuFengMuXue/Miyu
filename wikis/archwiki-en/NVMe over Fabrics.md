# NVMe over Fabrics

NVMe over Fabrics (NVMe-oF) allows sending NVMe commands over Ethernet or Fibre Channel. This can be used for remote access to block devices similar to iSCSI. An NVMe-oF host can access devices exposed by an NVMe-oF controller. This is not limited to NVMe devices, you can also expose block devices such as ZFS zvols.

## Host configuration
To access a block device exposed by a remote NVMe-oF controller, install the  package.

First, make sure the necessary kernel module is loaded:

 # modprobe nvme-fabrics

Now you can use the CLI to connect to the device:

 # nvme connect --transport=tcp --traddr=192.168.0.5 --trsvcid=4420 --nqn=nqn.2024-08.com.example:my-disk

; --transport=tcp: Specifies the transport protocol. TCP is the most simple to set up.
; --traddr=192.168.0.5: The address of the NVMe-oF target, i.e. the server that exposes the block device.
; --trsvcid=4420: The port the target is listening on. 4420 is the recommended port (IANA assignment).
; --nqn=nqn.2024-08.com.examplemy-disk: The NVMe Qualified Name (NQN) of the device to connect to. The device must be configured on the controller.

After running this command, the device will be available as a normal NVMe block device, e.g. under  with partitions under . It is recommended to refer to these devices by UUID, however.

## Controller configuration
Install the  package.

First, make sure the necessary kernel module is loaded:

 # modprobe nvmet

Controller configuration happens through a file system located at . nvmetcli provides a convenient interface to modify that file system. It also provides a way to load and save the settings.  will save the current state to , and  will load from that location. You can enable the  unit to load the configuration from that file automatically.

Inside , you can navigate using  and show the config tree using . There are three top-level directories.

; : contains the NQNs of hosts that are referenced in other parts of the tree, e.g. for access control. You can add an NQN here and then make the client use that NQN using the  parameter.
; : configures the protocols used to access the devices, e.g. a TCP port.
; : configures the individual accessible devices.

## Adding a device
First you'll want to create a device to expose:

 /> cd subsystems
 /subsystems> create nqn.2024-08.com.example:my-device
 /subsystems> cd nqn.2024-08.com.example:my-device
 /subsystems/n...ple:my-device>

Configure access for the device:

 /subsystems/n...ple:my-device> set attr allow_any_host=1

Configure a namespace for the device and set the backing block device:

 /subsystems/n...ple:my-device> cd namespaces
 /subsystems/n...ce/namespaces> create 1
 /subsystems/n...ce/namespaces> cd 1
 /subsystems/n.../namespaces/1> set device path=/dev/path/to/block/device
 /subsystems/n.../namespaces/1> enable

## Configuring the port
Next, create a port. Navigate back to the top using .

 /> cd ports
 /ports> create 1
 /ports> cd 1
 /ports/1> set addr trtype=tcp traddr=192.168.0.5 trsvcid=4420 adrfam=ipv4

; trtype: The transport protocol
; traddr: The listener address
; trsvcid: The listener TCP port ("service ID")

Add the device you created above to the network port:

 /ports/1> cd subsystems
 /ports/1/subsystems> create nqn.2024-08.com.example:my-device

That's it! Now the device is accessible to the host using the above instructions. To make this permanent, give the  command and ensure  is enabled/started.

## Authentication using DHCHAP
It is prudent to not allow just any device access to the exposed block device. To authenticate the host, NVMe-oF offers a DHCHAP handshake using a secret shared between host and controller. Unfortunately, as of writing, nvmetcli does not support this out of the box, so you have to modify the config FS manually. The host  command does support DHCHAP.

First, use  to limit access to the device to only a single host, identified by NQN.

 /> cd hosts
 /hosts> create nqn.2024-08.com.example.host
 /hosts> cd /subsystems/nqn.2024-08.com.example:my-device
 /subsystems/n...ple:my-device> set attr allow_any_host=0
 /subsystems/n...ple:my-device> cd allowed_hosts
 /subsystems/n...allowed_hosts> create nqn.2024-08.com.example.host

The NVMe controller now knows that only the host with the NQN  may access the device. You can test this (without DHCHAP, for now) using . With the wrong NQN, the connection should fail, with the right NQN, it should succeed.

The next step is to configure DHCHAP. First you need to generate a secret like so:

 $ nvme gen-dhchap-key --nqn=nqn.2024-08.com.example.host
 DHHC-1:00:znDcb37R200FNlZkIOkv37idpu/notvalid!!si1VQ09KhKv2g:

Because nvmetcli does not support DHCHAP, you must configure it manually:

 # echo 'DHHC-1:00:znDcb37R200FNlZkIOkv37idpu/notvalid!!si1VQ09KhKv2g:' > /sys/kernel/config/nvmet/hosts/nqn.2024-08.com.example.host/dhchap_key

Now, you can connect using the DHCHAP secret:

 # nvme connect --transport=tcp --traddr=192.168.0.5 --trsvcid=4420 --nqn=nqn.2024-08.com.example:my-disk --hostnqn=nqn.2024-08.com.example.host --dhchap-secret="DHHC-1:00:znDcb37R200FNlZkIOkv37idpu/notvalid!!si1VQ09KhKv2g:"

## Booting from NVMe-oF
It is possible to connect to an NVMe-oF device during the boot process inside initramfs and use the device for the root file system. The procedure is very similar to that for iSCSI. Only the NVMe-specific parts are listed here for now.

The  hook is different for NVMe-oF. The install script adds different modules, and adds the  binary instead of :

{{hc|1=/etc/initcpio/install/nvme-of|
2=build () {
	map add_module nvme-fabrics nvme-tcp nvme-keyring
	add_checked_modules "/drivers/net"
	add_binary nvme
	add_runscript
}
help () {
	cat
 dump_stack_lvl+0x4d/0x70
 warn_alloc+0x165/0x1e0
 ? __alloc_pages_direct_compact+0x163/0x390
 __alloc_pages_slowpath.constprop.0+0xce9/0xde0
 __alloc_pages+0x320/0x340
 ? nvmet_tcp_install_queue+0x50/0x140 ...
 __kmalloc_large_node+0x71/0x130
 __kmalloc+0xc4/0x130
 nvmet_tcp_install_queue+0x50/0x140 ...
 nvmet_install_queue+0xa6/0x1f0 ...
 nvmet_execute_io_connect+0xd1/0x1a0 ...
 nvmet_tcp_io_work+0x811/0x880 ...
 process_one_work+0x180/0x350
 worker_thread+0x315/0x450
 ? __pfx_worker_thread+0x10/0x10
 kthread+0xe8/0x120
 ? __pfx_kthread+0x10/0x10
 ret_from_fork+0x34/0x50
 ? __pfx_kthread+0x10/0x10
 ret_from_fork_asm+0x1b/0x30

}}

If the stack traces match, you are running into a linux-nvme bug. To serve a new TCP connection, the NVMe target / controller allocates a relatively large contiguous buffer in kernel space. If kernel memory is full (or fragmented), such a large contiguous region may not be available. This used to cause a kernel crash that was fixed in recent kernels, but as of February 2025 this still prevents new TCP connections to the controller. A patch for that is pending but stuck in review.

To work around this issue, you can use the following command to free up kernel memory on the controller prior to connection:

 # echo 3 > /proc/sys/vm/drop_caches

Another option that seems to work is to create and delete a large file in tmpfs:

 # dd if=/dev/urandom of=/tmp/random-buffer bs=1M count=4096 status=progress; rm -f /tmp/random-buffer

If that does not help, a reboot might be necessary.
