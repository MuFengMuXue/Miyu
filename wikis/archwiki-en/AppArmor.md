# AppArmor

AppArmor is a Mandatory Access Control (MAC) system, implemented upon the Linux Security Modules (LSM).

AppArmor, like most other LSMs, supplements rather than replaces the default Discretionary Access Control (DAC). As such, it is impossible to grant a process more privileges than it had in the first place.

Ubuntu and a number of other distributions use it by default. RHEL (and its variants) and SUSE use SELinux, which requires good userspace integration to work properly. SELinux attaches labels to all files, processes and objects and is therefore very flexible. However, configuring SELinux is considered to be very complicated and requires a supported filesystem. AppArmor on the other hand works using file paths and its configuration can be easily adapted.

AppArmor proactively protects the operating system and applications from external and internal threats and even zero-day attacks by enforcing a specific rule set on a per application basis. Security policies completely define what system resources individual applications can access, and with what privileges. Access is denied by default if no profile says otherwise. A few default policies are included with AppArmor and using a combination of advanced static analysis and learning-based tools, AppArmor policies for even very complex applications can be deployed successfully in a matter of hours.

Every breach of policy triggers a message in the system log, and AppArmor can be configured to notify users with real-time violation warnings popping up on the desktop.

## Installation
AppArmor is available in all officially supported kernels.

Install  for userspace tools and libraries to control AppArmor. To load all AppArmor profiles on startup, enable .

To enable AppArmor as the default security model on every boot, set the following kernel parameter:

 lsm=landlock,lockdown,yama,integrity,apparmor,bpf

## Custom kernel
When compiling the kernel, it is required to set at least the following options:

 CONFIG_SECURITY_APPARMOR=y
 CONFIG_AUDIT=y

To enable the AppArmor Linux security model by default and omit the need to set kernel parameters, additionally set the  option and specify  as the first "major" module in the list:

 CONFIG_LSM="landlock,lockdown,yama,integrity,apparmor,bpf"

## Usage
## Display current status
To test if AppArmor has been correctly enabled:

To display the current loaded status use :

In complain mode, policy violations of profiles are allowed but are logged. Complain mode is used for testing new profiles. Note that deny rules of profiles are enforced/blocked even in complain mode.

In enforce mode, policy violations of profiles are blocked and logged.

## Parsing profiles
To load (enforce or complain), unload, reload, cache and stat profiles use . The default action () is to load a new profile in enforce mode, loading it in complain mode is possible using the  switch, in order to overwrite an existing profile use the  option and to remove a profile use . Each action may also apply to multiple profiles. Refer to  man page for more information.

## Disabling loading
Disable AppArmor by unloading all profiles for the current session:

 # aa-teardown

To prevent AppArmor profiles from loading at the next boot disable . To prevent the kernel from loading AppArmor, append  to the kernel parameters, or remove the  kernel parameter that was added when setting up AppArmor.

## Configuration
## Auditing and generating profiles
To create new profiles the Audit framework should be running. This is because Arch Linux adopted systemd and does not do kernel logging to file by default. AppArmor can grab kernel audit logs from the userspace auditd daemon, allowing you to build a profile.

New AppArmor profiles can be created by utilizing  or . The profile is first created in complain mode: in this mode policy violations are only reported but not enforced. The rules are interactively created by the  tool available in  package. Finally the profile should be set into enforce mode with . In this mode the policy defined by the rules in the respecting profile are enforced. If necessary, additional rules can be added by repeatedly executing , or the profile can be set back to complain mode with . Detailed guide about using those tools is available at AppArmor wiki - Profiling with tools.

Note that  also offers deny rules which are actually not strictly necessary as according to the basic AppArmor logic everything is forbidden which is not explicitly allowed by a rule. However, deny rules serve two purposes:

# deny rules take precedence over allow rules. They are often used in many abstractions located in  in order to block any access to important folders/files. This ensures that inadvertently created allow rules do not make a profile too permissive.
# deny rules silence logging and make subsequent runs of aa-logprof less noisy. It is important to keep in mind that deny rules are enforced also in complain mode - hence, if an application does not work properly even in complain mode it should be checked if a deny rule in the profile or in one of the included abstractions is the culprit.

Alternatively profiles may be also created manually, see guide available at AppArmor wiki - Profiling by hand.

In addition to the default profiles in , there are more predefined profiles in . Note that those are not necessarily deemed production-ready, so manual intervention or usage of  may be required.

Another set of AppArmor profiles can be found in the apparmor.d project, however, as of writing, the project is not currently stable.

## Understanding profiles
Profiles are human readable text files residing under  describing how binaries should be treated when executed. A basic profile looks similar to this:

{{hc|/etc/apparmor.d/usr.bin.test|
#include

profile test /usr/lib/test/test_binary {
    #include

    # Main libraries and plugins
    /usr/share/TEST/** r,
    /usr/lib/TEST/** rm,

    # Configuration files and logs
    @{HOME}/.config/ r,
    @{HOME}/.config/TEST/** rw,
}
}}

Strings preceded by a  symbol are variables defined by abstractions (), tunables () or by the profile itself.  includes other profile-files directly. Paths followed by a set of characters are access permissions. Pattern matching is done using AppArmor's globbing syntax.

Most common use cases are covered by the following statements:

*  — read: read data
*  — write: create, delete, write to a file and extend it
*  — memory map executable: memory map a file executable
*  — execute: execute file; needs to be preceded by a qualifier

Remember that these permissions do not allow binaries to exceed the permissions dictated by the Discretionary Access Control (DAC).

This is merely a short overview, for a more detailed guide be sure to have a look at the  man page and documentation.

## Tips and tricks
## Get desktop notification on DENIED actions
The notification daemon displays desktop notifications whenever AppArmor denies a program access. To automatically start aa-notify daemon on login, follow the steps below:

Install the Audit framework and enable and start the userspace Linux Audit daemon. Allow your desktop user to read audit logs in  by adding it to  user group:

 # groupadd -r audit
 # gpasswd -a user audit

Add  group to :

Install ,  and .

Create a desktop launcher with the following content:

Reboot and check if the  process is running:

 $ pgrep -ax aa-notify

For more information, see .

## Speed-up AppArmor start by caching profiles
Since AppArmor has to translate the configured profiles into a binary format, it may significantly increase the boot time. You can check the current AppArmor startup time with:

 $ systemd-analyze blame | grep apparmor

To enable caching AppArmor profiles, uncomment:

To change the default cache location add:

Reboot and check AppArmor startup time again to see the improvement:

 $ systemd-analyze blame | grep apparmor

## Troubleshooting
## Failing to start Samba SMB/CIFS server
See Samba#Permission issues on AppArmor.

## Login impossible after upgrading to AppArmor v4
In rare cases, after upgrading to AppArmor version 4, it becomes impossible to log into any system account.

The system journal might contain errors like these:

This might be caused by  and/or  not being readable by the  user (i.e. the permission bits of those files might be entirely unset). Thus, a possible solution would be to:

# Reboot, and disable AppArmor either by editing the appropriate boot loader entry during boot or by using fallback boot entry, which doesn't have AppArmor enabled.
# Log in as , and set the correct file permissions:
# Reboot once again.

## Differences between Linux distributions
Information you find is often about AppArmor on Ubuntu, which can be confusing, since Ubuntu carries a lot of kernel patches regarding AppArmor. Other distributions may also carry their own kernel patches, while Arch Linux uses a close-to-mainline kernel.

For example,  documented  rules years prior to their support in the mainline kernel in 6.17 Support also varies by D-Bus implementation: the  package is built without AppArmor support, necessary for applying dbus AppArmor rules.

AppArmor-specific kernel patches applied by Ubuntu can be found at (replace  with the codename of the Ubuntu version you are interested in):

 https://git.launchpad.net/~ubuntu-kernel/ubuntu/+source/linux/+git/jammy/log/?qt=grep&q=UBUNTU%3A+SAUCE%3A+apparmor

The ABI versions supported by the userland tools can be found in . The ABI supported by the currently running kernel can be shown with:

 $ aa-features-abi --extract

or

 $ ls /sys/kernel/security/apparmor/features/
