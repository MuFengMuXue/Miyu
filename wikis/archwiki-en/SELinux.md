# SELinux

Security-Enhanced Linux (SELinux) is a Linux feature that provides a variety of security policies, including U.S. Department of Defense style Mandatory Access Control (MAC), through the use of Linux Security Modules (LSM) in the Linux kernel. It is not a Linux distribution, but rather a set of modifications that can be applied to Unix-like operating systems, such as Linux and BSD.

Running SELinux under a Linux distribution requires three things: An SELinux enabled kernel, SELinux Userspace tools and libraries, and SELinux Policies (mostly based on the Reference Policy). Some common Linux programs will also need to be patched/compiled with SELinux features.

## Current status in Arch Linux
SELinux is not officially supported (see The status of unofficial support is:

{| class="wikitable"
! Name !! Status !! Available at
|-
| SELinux enabled kernel || Implemented for all officially supported kernels || Available in official repositories since [https://gitlab.archlinux.org/archlinux/packaging/packages/linux/-/commit/3a29867f8266250b10aa9fa8368abc4306fa9c4b 4.18.8.
|-
| SELinux Userspace tools and libraries || Implemented in AUR: https://aur.archlinux.org/packages/?O=0&K=selinux || Work is done at https://github.com/archlinuxhardened/selinux
|-
| SELinux Policy || Work in progress, using Reference Policy as upstream || Upstream: https://github.com/SELinuxProject/refpolicy (since release 20170805 the policy has integrated support for systemd and single-/usr/bin directory)
|}

Summary of changes in AUR as compared to official core packages:

{| class="wikitable"
! Name !! Status and comments
|-
| linux, linux-lts, linux-zen, linux-hardened || Need to set the lsm= kernel parameter
|-
| coreutils || Need a rebuild with  flag to link with libselinux
|-
| cronie || Need a rebuild with  flag
|-
| dbus || Need a rebuild with  and  flags
|-
| findutils || Need a rebuild with libselinux installed to enable SELinux-specific options
|-
| iproute2 || Need a rebuild with  flag
|-
| logrotate || Need a rebuild with  flag
|-
| openssh || Need a rebuild with  flag
|-
| pam || Need a rebuild with  flag for Linux-PAM ; Need a patch for pam_unix2, which only removes a function already implemented in a recent versions of libselinux
|-
| pambase || Configuration changes to add pam_selinux.so to
|-
| psmisc || Need a rebuild with  flag
|-
| shadow || Need a rebuild with  flags
|-
| sudo || Need a rebuild with  flag
|-
| systemd || Need a rebuild with  and  flags
|-
| util-linux || Need a rebuild with  flag
|-
| uutils-coreutils || Need a rebuild with  make flag to link with libselinux
|-
|}

All of the other SELinux-related packages may be included without changes nor risks.

## Concepts: Mandatory Access Controls
Before you enable SELinux, it is worth understanding what it does. Simply and succinctly, SELinux enforces Mandatory Access Controls (MACs) on Linux. In contrast to SELinux, the traditional user/group/rwx permissions are a form of Discretionary Access Control (DAC). MACs are different from DACs because security policy and its execution are completely separated.

An example would be the use of the sudo command. When DACs are enforced, sudo allows temporary privilege escalation to root, giving the process so spawned unrestricted systemwide access. However, when using MACs, if the security administrator deems the process to have access only to a certain set of files, then no matter what the kind of privilege escalation used, unless the security policy itself is changed, the process will remain constrained to simply that set of files. So if sudo is tried on a machine with SELinux running in order for a process to gain access to files its policy does not allow, it will fail.

Another set of examples are the traditional (-rwxr-xr-x) type permissions given to files. When under DAC, these are user-modifiable. However, under MAC, a security administrator can choose to freeze the permissions of a certain file by which it would become impossible for any user to change these permissions until the policy regarding that file is changed.

As you may imagine, this is particularly useful for processes which have the potential to be compromised, i.e. web servers and the like. If DACs are used, then there is a particularly good chance of havoc being wreaked by a compromised program which has access to privilege escalation.

For further information, visit Wikipedia:Mandatory access control.

## Installing SELinux
## Package description
All SELinux related packages belong to the selinux group in the AUR. Before you manually install any of these, read #Installation to see recommended options for a comprehensive installation.

## SELinux aware system utilities
;
:Modified coreutils package compiled with SELinux support enabled. It replaces the  package.
;
:Fedora fork of Vixie cron with SELinux enabled. It replaces the  package.
;
:An SELinux aware version of D-Bus. It replaces the  package.
;
:Patched findutils package compiled with SELinux support to make searching of files with specified security context possible. It replaces the  package.
;
:iproute2 package compiled with SELinux support; for example, it adds the  option to . It replaces the  package.
;
:Logrotate package compiled with SELinux support. It replaces the  package.
;
:OpenSSH package compiled with SELinux support to set security context for user sessions. It replaces the  package.
; and
:PAM package with pam_selinux.so. and the underlying base package. They replace the  and  packages respectively.
;
:Psmisc package compiled with SELinux support; for example, it adds the  option to . It replaces the  package.
;
:Shadow package compiled with SELinux support; contains a modified  file to set correct security context for user after login. It replaces the  package.
;
:Modified sudo package compiled with SELinux support which sets the security context correctly. It replaces the  package.
;
:An SELinux aware version of systemd. It replaces the  package.
;
:Modified util-linux package compiled with SELinux support enabled. It replaces the  package.

## SELinux userspace utilities
;
:Tools to build SELinux policy
;
:Daemon which is used by libselinux to translate MCS labels
;
:Library for security-aware applications. Python bindings needed for semanage and setools now included.
;
:Library for policy management. Python bindings needed for semanage and setools now included.
;
:Library for binary policy manipulation.
;
:SELinux core utils such as newrole, setfiles, etc.
;
:Daemon which maintains the label of some files
;
:Compiler for SELinux policies written in CIL (Common Intermediate Language)
;
:DBus service which allows managing SELinux configuration
;
:SELinux GUI tools (system-config-selinux)
;
:SELinux python tools and libraries (semanage, sepolgen, sepolicy, etc.)
;
:Sandboxing tool for SELinux
;
:Tools to handle SELinux modules when building a policy

## SELinux policy packages
;
:Reference policy sources
;
:Reference policy git master (https://github.com/SELinuxProject/refpolicy) built with configuration specific for Arch Linux
;
:Precompiled modular Reference policy with headers and documentation but without sources. Development Arch Linux Refpolicy patches included, which fixes issues related to path labeling and systemd support. These patches are also sent to Reference Policy maintainers and their inclusion in  is mainly a way to perform updates between Refpolicy releases.

## Other SELinux tools
;
:CLI and GUI tools to manage SELinux
;
:pacman hook to label files accordingly to SELinux policy when installing and updating packages

## Installation
There are three methods to install the requisite SELinux packages.

## Via binary package on GitHub
All packages are available from the selinux unofficial repository. the base package can be replaced with base-selinux during the  stage of system installation.

## Via build script from GitHub
This repository also contains a script named  which builds and installs (or updates) all packages in the needed order. Here is an example of a way this script can be used in a user shell to install all packages (with downloading the GPG keys which are used to verify the source tarballs of the package):

 $ git clone https://github.com/archlinuxhardened/selinux.git
 $ cd selinux
 $ ./recv_gpg_keys.sh
 $ ./build_and_install_all.sh

Of course, it is possible to modify the content of  before running it, for example if you already have SELinux support in your kernel.

## Via AUR
* First, install SELinux userspace tools and libraries, in this order (because of the dependencies): , , , , , , , ,  (which depends on ),  and .
* Then install  and  and make sure you can login again after the installation completed, because files in  got removed and created when  got replaced with .
* Next you can recompile some core packages by installing: , , , , , , ,
* Next, backup your  file if you are not using its drop-in files. Install  and restore your  (it is overridden when this package is installed as a replacement of ).
* Next come util-linux and systemd. Because of a cyclic makedepends between these two packages which will not be fixed (), you need to build the source package , install , build and install  (with ) and rebuild and install .
* Next, install .
* Next, install  in order to run restorecon every time pacman installs a package.

After all these steps, you can install a SELinux kernel (like ) and a policy (like  or ).

## Enable SELinux LSM
To enable SELinux as default security model on every boot, set the following kernel parameter:

 lsm=landlock,lockdown,yama,integrity,selinux,bpf

## Custom kernel
When compiling the kernel, it is required to set at least the following options:

 CONFIG_SECURITY_SELINUX=y
 CONFIG_AUDIT=y

To enable the SELinux Linux security model by default and omit the need to set kernel parameters, additionally set the  option and specify  as the first "major" module in the list:

 CONFIG_LSM="landlock,lockdown,yama,integrity,selinux,bpf"

## Checking PAM
A correctly set-up PAM is important to get the proper security context after login. Check for the presence of the following lines in :

## Installing a policy
Policies are the mainstay of SELinux. They are what govern its behaviour. The only policy currently available in the AUR is the Reference Policy. In order to install it, you should use the source files, which may be got from the package  or by downloading the latest release on https://github.com/SELinuxProject/refpolicy/wiki/DownloadRelease#current-release. When using the AUR package, navigate to  and run the following commands:

 # make bare
 # make conf
 # make install

to install the reference policy as it is. Those who know how to write SELinux policies can tweak them to their heart's content before running the commands written above. The command takes a while to do its job and taxes one core of your system completely, so do not worry. Just sit back and let the command run for as long as it takes.

To load the reference policy run:

 # make load

Then, make the file  with the following contents (Only works if you used the defaults as mentioned above. If you decided to change the name of the policy, you need to tweak the file):

Now, you may reboot. After rebooting, run:

 # restorecon -r /

to label your filesystem.

Now, make a file  with the contents:

{{hc|requiredmod.te|2=
module requiredmod 1.0;

require {
        type devpts_t;
        type kernel_t;
        type device_t;
        type var_run_t;
        type udev_t;
        type hugetlbfs_t;
        type udev_tbl_t;
        type tmpfs_t;
        class sock_file write;
        class unix_stream_socket { read write ioctl };
        class capability2 block_suspend;
        class dir { write add_name };
        class filesystem associate;
}

#============= devpts_t ==============
allow devpts_t device_t:filesystem associate;

#============= hugetlbfs_t ==============
allow hugetlbfs_t device_t:filesystem associate;

#============= kernel_t ==============
allow kernel_t self:capability2 block_suspend;

#============= tmpfs_t ==============
allow tmpfs_t device_t:filesystem associate;

#============= udev_t ==============
allow udev_t kernel_t:unix_stream_socket { read write ioctl };
allow udev_t udev_tbl_t:dir { write add_name };
allow udev_t var_run_t:sock_file write;
}}

and run the following commands:

This is required to remove a few messages from  which are a nuisance to deal with in the reference policy. This is an ugly hack and it should be made very clear that the policy so installed simply patches the reference policy in order to hide the effects of incorrect labelling.

## Testing in a Vagrant virtual machine
It is possible to use Vagrant to provision a virtual Arch Linux machine with SELinux configured. This is a convenient way to test an Arch Linux system running SELinux without modifying a current system. Here are commands which can be used to achieve this:

 $ git clone https://github.com/archlinuxhardened/selinux.git
 $ cd selinux/_vagrant
 $ vagrant up
 $ vagrant ssh

## Post-installation steps
You can check that SELinux is working with . You should get something like:

To maintain correct context, you can enable .

To switch to enforcing mode without rebooting, you can use:

 # echo 1 > /sys/fs/selinux/enforce

## Swapfiles
If you have a swap file instead of a swap partition, issue the following commands in order to set the appropriate security context:

 # semanage fcontext -a -t swapfile_t "/path/to/swapfile"
 # restorecon /path/to/swapfile

## Working with SELinux
SELinux defines security using a different mechanism than traditional Unix access controls. The best way to understand it is by example. For example, the SELinux security context of the apache homepage looks like the following:

The first three and the last columns should be familiar to any (Arch) Linux user. The fourth column is new and has the format:

 user:role:typeTo explain:

#User: The SELinux user identity. This can be associated to one or more roles that the SELinux user is allowed to use.
#Role: The SELinux role. This can be associated to one or more types the SELinux user is allowed to access.
#Type: When a type is associated with a process, it defines what processes (or domains) the SELinux user (the subject) can access. When a type is associated with an object, it defines what access permissions the SELinux user has to that object.
#Level: This optional field can also be know as a range and is only present if the policy supports MCS or MLS.

This is important in case you wish to understand how to build your own policies, for these are the basic building blocks of SELinux. However, for most purposes, there is no need to, for the reference policy is sufficiently mature. However, if you are a power user or someone with very specific needs, then it might be ideal for you to learn how to make your own SELinux policies.

[https://web.archive.org/web/20210310014356/http://www.fosteringlinux.com/tag/selinux/ This is a great series of articles for someone seeking to understand how to work with SELinux.

## Troubleshooting
The place to look for SELinux errors is the systemd journal. In order to see SELinux messages related to the label  (for example), you would need to run:

 # journalctl _SELINUX_CONTEXT=system_u:system_r:policykit_t:s0

## Useful tools
There are some tools/commands that can greatly help with SELinux.

;restorecon: Restores the context of a file/directory (or recursively with ) based on any policy rules
;chcon: Change the context on a specific file

## Reporting issues
Please report issues on GitHub: https://github.com/archlinuxhardened/selinux/issues
