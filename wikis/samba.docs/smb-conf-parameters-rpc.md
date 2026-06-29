# smb.conf Parameters / rpc

### `rpc server dynamic port range`

Section: rpc; Context: G; Type: string; Default: `49152-65535`

This parameter tells the RPC server which port range it is allowed to use to create a listening socket for LSA, SAM, Netlogon and others without wellknown tcp ports. The first value is the lowest number of the port range and the second the highest. This applies to RPC servers in all server roles.

### `rpc start on demand helpers`

Section: rpc; Context: G; Type: boolean; Default: `yes`

This global parameter determines if samba-dcerpcd should be started on demand to service named pipe (np) DCE-RPC requests from smbd or winbindd . This is the normal case where no startup scripts have been modified to start samba-dcerpcd as a daemon. If samba-dcerpcd is started as a daemon or via a system service manager such as systemd, this parameter MUST be set to "no", otherwise samba-dcerpcd will fail to start.
