# Chrome OS devices/Crostini

Crostini is Google's umbrella term for making Linux application support easy to use and integrating well with Chrome OS.

This article describes how to install Arch Linux on a Chromebook in a container (via Crostini), without needing to enable developer mode, allowing apps to run alongside other Chrome/Android apps.

Highlights:

* Officially supported, do not need to enable developer mode - leaves Chrome OS secure, no need to flash a BIOS etc.
* Better battery life - battery life of Chrome with the functionality of Linux.
* Audio (in/out) & OpenGL are supported, but USB devices are only partially supported and development is still in progress.

## Introduction
## Enabling Linux support
Look for Linux under Settings and enable it. This installs a Debian Linux container that we will then replace with an Arch Linux container.

:Settings > Linux > Enable

Crostini is still rolling out to Chromebooks. If you do not see an option to enable Linux, you may need to switch to the beta or developer channel, if it has not rolled out to the stable channel for your laptop yet. This can be done via Settings > About Chrome OS > Channel > Dev/Beta.

## Replacing the default Debian Linux container with Arch Linux
The below instructions were initially based on https://www.reddit.com/r/Crostini/wiki/howto/run-arch-linux?v=2d4c6b4c-bbb0-11e8-8f2f-0e740b2a8a8c.

## Optional: Delete the Debian container
If you have no use for Debian anymore, you can save some storage space by destroying and recreating the Termina VM (this will let you skip renaming / deleting existing container later). Beware this will also delete any other containers you may have under Termina.

Open the crosh terminal in Chrome ().

 vmc destroy termina
 vmc start termina
## Create the container
Open a new crosh terminal in Chrome (). Enter termina using:
 vsh termina
Now you need to replace the default  remote:
 lxc remote remove images
 lxc remote add images https://images.lxd.canonical.com/ --protocol=simplestreams

Then create the Arch Linux container:
 lxc launch images:archlinux arch --config security.privileged=true
Open a shell in Termina and check if the Arch Linux container is present (it may a few minutes to show on the list):

 lxc list

If the container is not started, start it:

 lxc start arch

Note: As of October 2025 Canonical no longer provides Arch Linux container images for  only . If you are on x86_64, see #Requested architecture isn't supported by this host.

Launch a bash shell in the container:

 lxc exec arch -- bash

## Set up the user
The container creates a default user on install based on the email used to sign in to Chrome OS. The username can be seen with the following command:

 grep 1000:1000 /etc/passwd|cut -d':' -f1

Optionally you can rename user/group, by default named by your GMail id:

 # pkill -9 -u old-username
 # groupmod -n new-username old-username
 # usermod -d /home/new-username -l new-username -m -c new-username old-username

A password needs setting for the user:

 # passwd username

You may additionally want to install sudo and add the user to the wheel group. Use after installation:

 # visudo

Uncomment the following line to allow the wheel group to use sudo:

 # %wheel ALL=(ALL) ALL

Add your user to the wheel group:

 # usermod -aG wheel username

Leave the container:

 # exit

## Set up the container for use in Chrome OS
Login to the container using regular user account you just configured:

 lxc console arch

Verify networking in the container. The command

 $ ip -4 a show dev eth0

should return a non-empty output with the container's assigned IP address. If it is not empty, you can proceed, otherwise you are facing the issue described in #No network in container - follow the instructions listed there to address the issue.

Install the Crostini container tools, Wayland for GUI application support and Xwayland for X11 application support:

Install the  package. Additionally install  and  to be able to use GUI tools.

Start/enable the following user units:

{| class="wikitable"
! Template instance !! Purpose
|-
|  || Wayland
|-
|  || X11
|-
|  || Wayland (low density)
|-
|  || X11 (low density)
|}

Make sure these user services are running successfully by checking their unit statuses. Now, when apps are installed in Arch Linux, they will automatically appear in the Chrome OS launcher. Exit from the container shell back to the Termina shell by pressing  .

## Replace the default Debian container with Arch Linux
The default Debian container is named penguin. Renaming the "arch" container created above to it will cause Chrome OS to launch Linux apps from the arch container. Stop the Arch Linux container:

 lxc stop --force arch

Stop the Debian container and rename it to "debian" (this step can be skipped if you have already removed the Debian container):

 lxc stop --force penguin
 lxc rename penguin debian

Rename the Arch container to "penguin" and start it:

 lxc rename arch penguin
 lxc start penguin

Restart the Linux subsystem to apply the changes. After restart, verify that no failed system or user units are listed.

The following command should report the IP address assigned for container:

 ip -4 a show dev eth0

## Troubleshooting
## Arch container fails to start
The container is present but the state is stopped:
 $ lxc list
 +---------+---------+------+------+-----------+-----------+
 |  NAME   |  STATE  | IPV4 | IPV6 |   TYPE    | SNAPSHOTS |
 +---------+---------+------+------+-----------+-----------+
 |  arch   | STOPPED |      |      | CONTAINER | 0         |
 +---------+---------+------+------+-----------+-----------+

Attempts to start the container via  do not start the container.

Cause:
systemd version 258 requires cgroup v2, which Crostini does not currently support.

 Detected cgroup v1 hierarchy at /sys/fs/cgroup/, which is no longer supported by current version of systemd.
 Please instruct your initrd to mount cgroup v2 (unified) hierarchy,
 possibly by removing any stale kernel command line options, such as:
  systemd.legacy_systemd_cgroup_controller=1
  systemd.unified_cgroup_hierarchy=0
 Detected unsupported legacy cgroup hierarchy, refusing execution.
 Exiting PID 1...
 Error: write /dev/pts/ptmx: file already closed

There is no workaround at present apart from downgrading  in the container to version 257.

## Requested architecture isn't supported by this host
 lxc launch images:archlinux archlinux --config security.privileged=true
 Creating archlinux
 Error: Failed instance creation: Failed creating instance record: Requested architecture isn't supported by this host

Canonical no longer provides Arch Linux container images for . You can see which architectures are supported with the following command:
 lxc image list images: | grep archlinux | grep CONTAINER

## Arch container fails to start after update to Chrome OS 81
Most of custom containers stopped working with Chrome OS 81 update. The root cause is a LXC version update, as a result, the container fails to start with following error:

 lxc penguin 20200411193357.312 WARN     initutils - initutils.c:setproctitle:324 - Invalid argument - Failed to set cmdline
 lxc penguin 20200411193357.395 WARN     conf - conf.c:lxc_map_ids:2919 - newuidmap is lacking necessary privileges
 lxc penguin 20200411193357.395 WARN     conf - conf.c:lxc_map_ids:2925 - newgidmap is lacking necessary privileges
 lxc penguin 20200411193357.400 WARN     conf - conf.c:lxc_map_ids:2919 - newuidmap is lacking necessary privileges
 lxc penguin 20200411193357.400 WARN     conf - conf.c:lxc_map_ids:2925 - newgidmap is lacking necessary privileges
 lxc penguin 20200411193357.477 ERROR    conf - conf.c:run_buffer:335 - Script exited with status 32
 lxc penguin 20200411193357.477 ERROR    conf - conf.c:lxc_setup:3589 - Failed to run mount hooks
 lxc penguin 20200411193357.477 ERROR    start - start.c:do_start:1263 - Failed to setup container "penguin"
 lxc penguin 20200411193357.478 ERROR    sync - sync.c:__sync_wait:62 - An error occurred in another process (expected sequence number 5)
 lxc penguin 20200411193357.478 WARN     network - network.c:lxc_delete_network_priv:2561 - Failed to rename interface with index 17 from "eth0" to its initial name "veth421fa9d1"
 lxc penguin 20200411193357.478 ERROR    lxccontainer - lxccontainer.c:wait_on_daemonized_start:842 - Received container state "ABORTING" instead of "RUNNING"
 lxc penguin 20200411193357.479 ERROR    start - start.c:__lxc_start:1939 - Failed to spawn container "penguin"
 lxc penguin 20200411193357.701 WARN     conf - conf.c:lxc_map_ids:2919 - newuidmap is lacking necessary privileges
 lxc penguin 20200411193357.701 WARN     conf - conf.c:lxc_map_ids:2925 - newgidmap is lacking necessary privileges
 lxc 20200411193357.706 WARN             commands - commands.c:lxc_cmd_rsp_recv:132 - Connection reset by peer - Failed to receive response for command "get_state"
 lxc 20200411193357.707 WARN             commands - commands.c:lxc_cmd_rsp_recv:132 - Connection reset by peer - Failed to receive response for command "get_state"

Solution

Navigate to crosh and execute the following commands:

 vmc start termina
 vsh termina
 lxc file delete penguin/var/lib/lxc
 lxc file delete penguin/var/lib/lxcfs

Restart Linux subsystem and container started should start normally.

## No network in container
As was reported by multiple sources, systemd-networkd and systemd-resolved services in systemd-244.1 are not working properly for unprivileged LXC containers, which ends up in missing network connectivity inside the Crostini container. Users may see only IPv6 address but no IPv4 address for the  container (for example, using  command).

One possible solution is stated here: LXD#No IPv4 with systemd-networkd.

Alternatively, another solution is to completely disable systemd-networkd/systemd-resolved and perform network configuration by dhclient service instead. First, install , then, as the root user, run:

 dhcpcd eth0
 systemctl disable systemd-networkd
 systemctl disable systemd-resolved
 unlink /etc/resolv.conf
 touch /etc/resolv.conf
 systemctl enable dhclient@eth0
 systemctl start dhclient@eth0

NetworkManager and dhcpcd also can be used to address the issue if you prefer them over the  solution.

## Permission denied with ping
If you get

 ping: socket: permission denied

when trying to ping from a user other than , you need to set the capability flag on the  file to fix it.

 # setcap cap_net_raw+ep /usr/bin/ping

This should solve the problem. See .

## App not opening in chrome OS (infinite spinner)
I found that launching a console (lxc console penguin) session prevents apps from launching in Chrome OS. Launching results in an infinite spinner. In that case, I have to stop and start the container to get the Chrome OS launcher working

 lxc stop penguin
 lxc start penguin

Instead of using an lxc console session, I use a regular Linux terminal GUI launched from Chrome OS that prevents this issue.

## Audio playback/input
Crostini support audio playback starting Chrome OS 74. With  installed both ALSA and PulseAudio playback should work after PulseAudio configuration. Audio input is  supported starting Chrome OS 79.

Enter the following command in the container (in case you did not):

 $ cp -rT /etc/skel/.config/pulse ~/.config/pulse

It is also possible to use PipeWire instead of PulseAudio. Put the following file into :

{{hc|1=/etc/pipewire/pipewire.conf.d/crostini-audio.conf|2=
context.objects = [
    { factory = adapter
        args = {
            factory.name           = api.alsa.pcm.sink
            node.name              = "Virtio Soundcard Sink"
            media.class            = "Audio/Sink"
            api.alsa.path          = "hw:0,0"
            audio.channels         = 2
            audio.position         = "FL,FR"
        }
    }
    { factory = adapter
        args = {
            factory.name           = api.alsa.pcm.source
            node.name              = "Virtio Soundcard Source"
            media.class            = "Audio/Source"
            api.alsa.path          = "hw:0,0"
            audio.channels         = 2
            audio.position         = "FL,FR"
        }
    }

}}

## Video playback
mpv can play videos using software rendering without any addition configuration, however this is CPU consuming and laggy experience for modern video codecs like H265. For hardware accelerated playback GPU acceleration is required. Take into account, that GPU acceleration for Crostini is based on VirGL, so no real GPU device pass-though is performed and hardware-specific APIs like VA-API or VPDAU are not available. However OpenGL acceleration can be used, i.e. this is example of  which enabled accelerated video and audio playback on Google Pixelbook starting Chrome OS 77:

 vo=gpu
 ao=alsa

## GPU acceleration
On Google Pixelbook GPU acceleration works with Arch out-of-the-box starting Chrome OS 77. Also no flags need to be enabled on recent released of Chrome OS:

{{hc|$ glxinfo -B|name of display: :0
display: :0  screen: 0
direct rendering: Yes
Extended renderer info (GLX_MESA_query_renderer):
    Vendor: Red Hat (0x1af4)
    Device: virgl (0x1010)
    Version: 19.1.4
--> Accelerated: yes  ~/.local/share/keyrings/default

## Fullscreen video, games and mouse capture
Currently Crostini has limited support for mouse capture starting with Chrome OS 79. You must enable the flag chrome://flags/#exo-pointer-lock to get mouse capture. The closed issue relating to mouse capture is https://bugs.chromium.org/p/chromium/issues/detail?id=927521.

## "Linux Files" is empty on host
If you find the "Linux Files" directory on host is always empty and see the following logs in the guest Arch Linux, then you might be affected.

 Feb 24 21:18:23 penguin garcon[183: sftp: accepted connection from vsock:2:3162708311
 Feb 24 21:18:23 penguin garcon[183: Failed to execute requested program in child process: No such file or directory
 Feb 24 21:18:23 penguin garcon[183: sftp: failed to spawn child process: No child processes (10)

Since 2022-06, garcon launches the sftp server with , while the  package installs the binary at . A workaround is linking the path expected by garcon to the installed one:

 # mkdir /usr/lib/openssh/
 # ln -s /usr/lib/ssh/sftp-server /usr/lib/openssh/sftp-server

## Firefox laggy clicking, scrolling & videos
If firefox is exhibiting extremely laggy behavior when clicking on the address bar, scrolling, selecting text etc, and or playing lagged or choppy videos, running firefox with MOZ_ENABLE_WAYLAND=1 may resolve this. Inside firefox, about:support should show "Window Protocol" as wayland after this.

 MOZ_ENABLE_WAYLAND=1 firefox
