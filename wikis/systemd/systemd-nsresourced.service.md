## Name

systemd-nsresourced.service, systemd-nsresourced — User Namespace Resource Delegation Service

## Synopsis

`systemd-nsresourced.service`

`/usr/lib/systemd/systemd-nsresourced`

## Description

**systemd-nsresourced** is a system service that permits transient delegation of a UID/GID range to a user namespace (see user_namespaces(7)) allocated by a client, via a Varlink IPC API.

Unprivileged clients may allocate a user namespace, and then request a UID/GID range to be assigned to it via this service. The user namespace may then be used to run containers and other sandboxes, and/or apply it to an id-mapped mount.

Allocations of UIDs/GIDs this way are transient: when a user namespace goes away, its UID/GID range is returned to the pool of available ranges. In order to ensure that clients cannot gain persistency in their transient UID/GID range a BPF-LSM based policy is enforced that ensures that user namespaces set up this way can only write to file systems they allocate themselves or that are explicitly allowlisted via **systemd-nsresourced**.

**systemd-nsresourced** automatically ensures that any registered UID ranges show up in the system's NSS database via the User/Group Record Lookup API via Varlink.

Currently, only UID/GID ranges consisting of either exactly 1 or exactly 65536 UIDs/GIDs can be registered with this service. Moreover, UIDs and GIDs are always allocated together, and symmetrically.

The allocation API supports *delegated ranges*: additional UID/GID ranges that are mapped 1:1 into the user namespace rather than being translated to a target UID/GID. These delegated ranges enable nested user namespace scenarios where a container needs to create child user namespaces with their own transient UID ranges. Normally, the kernel restricts which UIDs can be mapped into a user namespace to those that are also mapped in the parent. Delegated ranges solve this by pre-allocating additional ranges that are visible inside the user namespace and can be used by nested `AllocateUserRange()` calls. Up to 16 delegated ranges can be requested per user namespace, each of size 65536. The ranges are allocated from the container UID ranges as per Users, Groups, UIDs and GIDs on systemd Systems.

The allocation API also supports *identity mappings*: instead of allocating a transient UID/GID range, the user namespace can be configured to map the caller's UID/GID to root (UID 0) inside the namespace, or to itself. Identity mappings can be combined with delegated ranges to enter a privileged user namespace from which the container can be set up after which the container can run in one of the delegated ranges. Identity mapped users are not subject to BPF-LSM write restrictions unlike the transient ranges.

Additionally, the allocation API supports mapping the *foreign UID range* into the user namespace. When this option is enabled, the foreign UID range is mapped 1:1 into the user namespace, allowing processes inside to access and manipulate files owned by the foreign UID range.

The service provides API calls to allowlist mounts (referenced via their mount file descriptors as per Linux `fsmount()` API), to pass ownership of a cgroup subtree to the user namespace and to delegate a virtual Ethernet device pair to the user namespace. When used in combination this is sufficient to implement fully unprivileged container environments, as implemented by systemd-nspawn(1), fully unprivileged `RootImage=` (see systemd.exec(5)) or fully unprivileged disk image tools such as systemd-dissect(1).

This service provides one Varlink service: `io.systemd.NamespaceResource` allows registering user namespaces, and assign mounts, cgroups and network interfaces to it.

## See Also

systemd(1), systemd-mountfsd.service(8), systemd-nspawn(1), systemd.exec(5), systemd-dissect(1), user_namespaces(7)
