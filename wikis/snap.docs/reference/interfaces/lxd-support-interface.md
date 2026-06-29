#  lxd-support interface

`lxd-support` enables operating as the LXD service. This interface can currently only be established with the upstream LXD project.

## Developer details

**[Auto-connect](https://snapcraft.io/docs/explanation/interfaces/interface-auto-connection/)**: no

**[Super-privileged](https://snapcraft.io/docs/explanation/interfaces/super-privileged-interfaces/)**: yes

**Transitional**: yes

**Attributes**:

 * **enable-unconfined-mode** (plug, optional):  indicates that snapd should make use of the AppArmor `unconfined` profile mode (if this is supported by the system) when generating the associated AppArmor profiles for the snap which plugs this interface.
