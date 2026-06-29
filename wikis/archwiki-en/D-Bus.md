# D-Bus

D-Bus is a message bus system that provides an easy way for inter-process communication. It consists of a daemon, which can be run both system-wide and for each user session, and a set of libraries to allow applications to use D-Bus.

 is pulled and installed as a dependency of  and user session bus is started automatically for each user.

## Implementations
Arch provides two D-Bus message broker implementations. Initially, the user will be asked to choose a desired dbus-units provider during installation of  package. Only one implementation can be installed at a time.

## dbus-broker
dbus-broker is currently the default implementation for Arch [https://rfc.archlinux.page/0025-dbus-broker-default/. It is a drop-in replacement for the reference implementation, which aims "to provide high performance and reliability, while keeping compatibility to the D-Bus reference implementation".

Select  when asked for dbus-units provider, or install it explicitly.

## Reference implementation
The reference implementation is still officially supported by Arch.

Select  when asked for dbus-units provider, or install it explicitly.

## Tips and tricks
## Override dbus service
This is useful when specifying a particular service among other services providing the same well-known bus name. See KeePass#Autostart and KDE Wallet#Automatic D-Bus activation for example.

D-Bus services can be masked by setting  in service files of . For example, to mask gvfsd,

If the service is already launched, the override will not work. The existing service's process must be killed, or launched earlier.

## Debugging
*
*
*
*

You can also use  from systemd.
