# Firejail

Firejail is an easy to use Setuid sandbox program that reduces the risk of security breaches by restricting the running environment of untrusted applications using Linux namespaces, seccomp-bpf and Linux capabilities.

## Installation
Install the  package. A GUI application for use with Firejail is also available, .

## Configuration
Most users will not require any custom configuration and can proceed to #Usage.

Firejail uses profiles to set the security protections for each of the applications executed inside of it - you can find the default profiles in . Should you require custom profiles for applications not included, or wish to modify the defaults, you may place new rules or copies of the defaults in the  directory. You may have multiple custom profile files for a single application, and you may share the same profile file among several applications.

If firejail does not have a profile for a particular application, it uses its restrictive system-wide default profile. This can result in the application not functioning as desired, without first creating a custom and less restrictive profile.

Refer to .

## Usage
To execute an application using firejail's default protections for that application (the default profile), execute the following:

 $ firejail program_name

One-time additions to the default profile can be added as command line options (see ). For example, to execute okular with seccomp protection, execute the following:

 $ firejail --seccomp okular

You may define multiple non-default profiles for a single program. Once you create your profile file, you can use it by executing:

 $ firejail --profile=/absolute/path/to/profile program_name

## Using Firejail by default
To use Firejail by default for all applications for which it has profiles, run the firecfg tool with sudo:

 $ sudo firecfg

This creates symbolic links in  pointing to  for  programs for which Firejail has default or self-created profiles. Note that  only symlinks the programs listed in . Certain CLI programs are absent, such as: tar, curl, and git. These need to be symlinked manually. See Profiles not in firecfg #2507 for why they are not included. firecfg additionally adds the current user to Firejail user access database and checks the  files if they contain the full path to the respective executable, removes the full path and copies them to . This ensures that the symlinks in  will be used, which prevents Firejail getting bypassed. If sudo is not installed on your system, you should execute:

 # firecfg

as root and

 $ firecfg --fix

as user in order to fix the .desktop files.

There may be cases for which you need to manually modify the  line of the .desktop file in  to explicitly call Firejail.

To manually map individual applications, execute:

 # ln -s /usr/bin/firejail /usr/local/bin/application

## Use with hardened_malloc
 is a hardened implementation of glibc's  allocator, originally written for Android but extended for use on the desktop. While not integrated into glibc yet, it can be used selectively with . The proper way to launch an application within firejail using hardened_malloc is demonstrated below. To make it permanent, you would need to create your own entry in  for the desired application.

 $ firejail --env=LD_PRELOAD='/usr/lib/libhardened_malloc.so' /usr/bin/firefox

Alternatively, add the following to a custom profile:

 env LD_PRELOAD=/usr/lib/libhardened_malloc.so

Profiles that have private-lib will need the following in custom profiles:

 private-lib /lib/libhardened_malloc.so

The various environment variables and settings that can be used to tune hardened_malloc can be found on its github page.

## Enable AppArmor support
Since 0.9.60-1, Firejail has supported more direct integration with AppArmor through a generic AppArmor profile. During installation, the profile, , is placed in  directory, and needs to be loaded into the kernel by running the following command as root:

 # apparmor_parser -r /etc/apparmor.d/firejail-default

See .

Local customizations of the apparmor profile are supported by editing the file

AppArmor is already enabled for a large number of Firejail profiles. There are several ways to enable AppArmor confinement on top of a Firejail security profile:

* Pass the  flag to Firejail in the command line, e.g.
* Use a custom profile and add the  command.
* Enable Apparmor globally in  and disable as needed through the use of  in .

Note that enabling AppArmor by above methods always means that  is used. If you rather want to use a specific AppArmor profile for an application, you have to use the above mentioned  command. However, that is not recommended, as using both Firejail and AppArmor for the same applications often creates problems.

## Verifying Firejail is being used
 $ firejail --list

A more comprehensive output is produced by

 $ firejail --tree

## Creating custom profiles
## Whitelists and blacklists
Blacklists deny access to a specific file or directory. All other files and directories, which are not added to the blacklist, are not changed.

* Deny access to a directory or file:
* Ignore a  line that comes after:

The order in which they appear in a profile is important: noblacklist directives must be added above blacklist directives.

Whitelists block everything under the same "top directory", that is not explicitly whitelisted. This means that if you whitelist for example , this file will be accessible, but for example if there's another file , that will not be accessible. In  Firejail, a "top directory" means, if the whitelisted file's path is for example , then the top directory would be . All other top directories like ,  and so on, haven't changed, so all files there are still accessible, unless a file or directory inside them is also whitelisted.

* Allow access to a directory or file and forbid everything else in the "top directory":
* Ignore a  line that comes after:

The order in which they appear in a profile is important: nowhitelist directives must be added above whitelist directives.

## Profile writing
The basic process is:

# Copy  to  or  and rename it to  where ProfileName should match the name of the executable to be sandboxed
# Change the line  to
# Gradually comment/uncomment the various options while checking at each stage that the application runs inside the new sandbox. Do not change the order of the sections in that template.
# Detailed explanations of the possible options for a Firejail profile can be found in the  man page
# Test the profile for security holes, see #Testing profiles

If you want to create a whitelisted profile (i.e. a profile which contains whitelist directives), you can build a whitelist of permitted locations by executing

 $ firejail --build application

Keep in mind that a whitelisted profile is problematic for applications that need to access random locations (like text editors or file managers).

## Persistent local customisation
The standard profile layout includes the capability to make persistent local customisations through the inclusion of  filesBasically, each officially supported profile contains the lines  and . These *.local files might be located in  or in . Since the order of precedence is determined by which is read first, this makes for a very powerful way of making local customisations.
For example, with reference [https://github.com/netblue30/firejail/issues/1510#issuecomment-326443650 this firejail question, to globally enable Apparmor and disable Internet connectivity, one could simply create/edit  to include the lines

 # enable Apparmor and disable Internet globally
 net none
 apparmor

Then, to allow, for example, "curl" to connect to the internet, yet still maintain its apparmor confinement, one would create/edit  to include the lines.

 # enable internet for curl
 ignore net

Since  is read before ,  overrides , and, as a bonus, the above changes would be persistent across future updates.

## Testing profiles
In order to test and audit a Firejail profile, you may find the following to be useful:

#  Gives a detailed breakdown of the sandbox
#  and  show the blacklisted and whitelisted directories and files for the current profile.
#  gives a list of caps supported by the current Firejail software build. This is useful when building a caps whitelist.
#  for a full list of  options
#  monitors the running process. See  for details
# Executing  tests running sandboxes. See the  man page for details.
#  may also be useful in testing which standard security features are being used

## Firejail with Xorg
On Xorg any program can listen to all keyboard input and record all screens. The purpose of sandboxing X11 is to restrict this behavior, which is especially problematic for complex programs working with potentially malicious input like browsers.

Xephyr and Xpra allow you to sandbox Xorg. Although Xpra provides full clipboard support, it is recommended to use Xephyr due to the very notable and permanent lag with nested X11 sessions.

For a complete setup with (not ideal) clipboard support (clipboard is still always shared), see Sakaki's Gentoo guide, especially the section about the clipboard and automatic rescaling.

Alternatively, if clipboard support is not needed but windows need to be managed, install a standalone window manager such as Openbox.

 can be set in  where  and  are in pixels and based on your screen resolution.

To open the sandbox:

 $ firejail --x11=xephyr --net=device openbox

 is your active network interface, which is needed to ensure that DNS works. Then right click and select your applications to run.

See the Firejail Wordpress site for a simpler guide.

According to the guide:

:The sandbox replaces the regular X11 server with Xpra or Xephyr server. This prevents X11 keyboard loggers and screenshot utilities from accessing the main X11 server.

Note that the statement:

:The only way to disable the abstract socket  is by using a network namespace. If for any reasons you cannot use a network namespace, the abstract socket will still be visible inside the sandbox. Hackers can attach keylogger and screenshot programs to this socket.

is incorrect, xserverrc can be edited to , which disables the abstract sockets of X11 and helps isolate it.

## Sandboxing a browser
Openbox can be configured to start a certain browser at startup.  is the respective profile contained in , and  is the command line used to start the program. For example, to start Chromium in the sandbox:

 $ firejail --x11=xephyr --profile=/etc/firejail/chromium.profile openbox --startup "chromium"

You can control the size of the screen with the parameter:

 --xephyr-screen=400x250

## Tips and tricks
## Hardening Firejail
The security risk of Firejail being a SUID executable can be mitigated by adding the line

 force-nonewprivs yes

to . However, this can break specific applications. On Arch Linux, VirtualBox doesn't start anymore. With the  kernel Wireshark and Chromium-based browsers are also affected.

Further hardening measures include creating a special firejail group with adding the user to that group and changing the file mode for the firejail executable. For details see here.

## Paths containing spaces
If you need to reference, whitelist, or blacklist a directory within a custom profile, such as with , you must do so using the absolute path, without encapsulation or escapes:
 /home/user/.moonchild productions

## Private mode
Firejail also includes a one time private mode, in which no mounts are made in the chroots to your home directory. In doing this, you can execute applications without performing any changes to disk. For example, to execute okular in private mode, do the following:

 $ firejail --seccomp --private okular

## Experimental improved tools
Some of the Firejail developers recognized issues with the tools it ships with and made their own, improved versions of them.

* firecfg.py, an improved version of .
* fjp, a tool to interact with Firejail profiles.
* fireurl, Fixing the firejail URL open issue.
* firejail-handler-http, which helps with opening HTTP(S) links properly when sandboxing applications.
* firejail-handler-extra, like above but handles other protocols.

## Troubleshooting
Firejail can be hard to debug. The symptoms of a misconfigured or otherwise unfitting setup range from random segmentation faults and hangs in the applications to simple error messages.

Some applications are harder to sandbox than others. For example web browsers and Electron applications tend to need more troubleshooting than others since there is much that can go wrong. It is crucial to check the FAQ and open issues first, since debugging can take quite some time.

## Remove Firejail symbolic links
To remove Firejail created symbolic links (e.g. reset to default):

 # firecfg --clean

If you do not want to use Firejail for a specific application (e.g., because you prefer to rather confine it with AppArmor), you have to manually remove the related symbolic link:

 # rm /usr/local/bin/application

As a subsequent execution of firecfg would re-add the removed symlinks, the respective applications should be commented in .

Verify if any leftovers of Desktop entries are still overruled by Firejail.

## PulseAudio
If Firejail causes PulseAudio issues with sandboxed applications the following command may be used:

 $ firecfg --fix-sound

This commands creates a custom  file for the current user with  and possible other workarounds.

## hidepid
If the system uses the hidepid kernel parameter, Firemon can only be run as root. This, among other things, will cause problems with the Firetools GUI incorrectly reporting "Capabilities", "Protocols" and the status of "Seccomp"[https://github.com/netblue30/firejail/issues/1564.

## Proprietary Nvidia drivers
Some users report problems when using Firejail and proprietary graphic drivers from NVIDIA (e.g. [https://github.com/netblue30/firejail/issues/879 or This can often be solved by disabling the  Firejail option in the application's profile file.

## --net options and Linux kernel >=4.20.0
There is a bug on firejail 0.5.96 with linux >= 4.20.0, see [https://github.com/netblue30/firejail/issues/2314 and Example error message:

 $ firejail --noprofile --net=eth0 ls
 Parent pid 8521, child pid 8522
 Error send: arp.c:182 arp_check: Invalid argument
 Error: proc 8521 cannot sync with peer: unexpected EOF
 Peer 8522 unexpectedly exited with status 1

## Warning: Cannot confine the application using AppArmor
For some applications (e.g. Firefox) starting with Firejail may result in warnings like:

 Warning: Cannot confine the application using AppArmor.
 Maybe firejail-default AppArmor profile is not loaded into the kernel.
 As root, run "aa-enforce firejail-default" to load it.

When running the suggested command you might see:

 ERROR: Cache read/write disabled: interface file missing. (Kernel needs AppArmor 2.4 compatibility patch.)

This means that AppArmor is not enabled as a kernel parameter, so you have to set it according to AppArmor#Installation.

## /usr/bin/patch: **** Can't open patch file
This means the  uses  with the  argument so a whitelist for  in  is needed.

Create the override  with the value of your :

 whitelist /path/to/makepkg/sources

Changing the  to use  also works:

 patch -p1 < ../file.patch

## Daemonizing/backgrounded processes hang
There is a [https://github.com/netblue30/firejail/issues/3491 known issue that prevents processes from daemonizing. There is currently no solution to this except not using Firejail to sandbox the affected application. Because it is a bug within Firejail, no configuration can solve this issue. Fortunately the applications mentioned in the issue usually do not have a large attack surface, so the risks of running them without a sandbox are comparatively low.
