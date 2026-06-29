# Bubblewrap/Examples

## dhcpcd
Create a simple dhcpcd sandbox:
* Determine available kernel namespaces
 $ ls /proc/self/ns
 cgroup  ipc  mnt  net  pid  uts

* Bind as read-write the entire host  directory to  in the sandbox
* Mount a new devtmpfs filesystem to  in the sandbox
* Create new IPC and control group namespaces
* Create a new UTS namespace and set  as the hostname

 # /usr/bin/bwrap --bind / / --dev /dev --unshare-ipc --unshare-cgroup --unshare-uts --hostname dhcpcd /usr/bin/dhcpcd -q -b

## Unbound
Create a more granular and complex Unbound sandbox:
* Bind as read-only the system  directory to  in the sandbox
* Create a symbolic link from the system  directory to  in the sandbox
* Bind as read-only the system  directory to  in the sandbox
* Create empty  and  directories within the sandbox
* Mount a new devtmpfs filesystem to  in the sandbox
* Create new IPC and PID and control group namespaces
* Create a new UTS namespace and set  as the hostname

 # /usr/bin/bwrap --ro-bind /usr /usr --symlink usr/lib /lib64 --ro-bind /etc /etc --dir /var --dir /run --dev /dev --unshare-ipc --unshare-pid --unshare-cgroup --unshare-uts --hostname unbound /usr/bin/unbound -d

## MuPDF
The power and flexibility of bwrap is best revealed when used to create an environment within a shell wrapper:

* Bind as read-only the host  directory to  in the sandbox
* Bind as read-only the host  directory to  in the sandbox
* Create a symbolic link from the system  directory to  in the sandbox
* Create a tmpfs filesystem overlaying  in the sandbox
** This effectively blacklists the contents of  from appearing in the sandbox
* Create a new tmpfs filesystem as the  directory in the sandbox
* Bind as read-only an  file and Documents directory into the sandbox
** This effectively whitelists the  file and Documents directory with recursion
* Create a new tmpfs filesystem as the  directory in the sandbox
* Whitelist the X11 socket by binding it into the sandbox as read-only
* Clone and create private containers for all namespaces supported by the running kernel
** If the kernel does not support non-privileged user namespaces, skip its creation and continue
* Do not place network components into a private namespace
** This allows for network access to follow URI hyperlinks

 #!/bin/sh
 #~/bwrap/mupdf.sh
 (exec bwrap \
 --ro-bind /usr/bin /usr/bin \
 --ro-bind /usr/lib /usr/lib \
 --symlink usr/lib /lib64 \
 --tmpfs /usr/lib/gcc \
 --tmpfs $HOME \
 --ro-bind $HOME/.Xauthority $HOME/.Xauthority \
 --ro-bind $HOME/Documents $HOME/Documents \
 --tmpfs /tmp \
 --ro-bind /tmp/.X11-unix/X0 /tmp/.X11-unix/X0 \
  --unshare-all \
 --share-net \
 /usr/bin/mupdf "$@")

 $ bwrap \
 --ro-bind /usr/bin /usr/bin \
 --ro-bind /usr/lib /usr/lib \
 --symlink usr/lib /lib64 \
 --tmpfs /usr/lib/gcc \
 --tmpfs $HOME \
 --ro-bind $HOME/.Xauthority $HOME/.Xauthority \
 --ro-bind $HOME/Documents $HOME/Documents \
 --tmpfs /tmp \
 --ro-bind /tmp/.X11-unix/X0 /tmp/.X11-unix/X0 \
 --unshare-all \
 --share-net \
  /usr/bin/sh
 bash-4.4$ ls -AF
 .Xauthority  Documents/

Perhaps the most important rule to consider when building a bubblewrapped filesystem is that commands are executed in the order they appear. From the MuPDF example above:

* A tmpfs system is created followed by the bind mounting of an  file and a Documents directory:
 --tmpfs $HOME \
 --ro-bind $HOME/.Xauthority $HOME/.Xauthority \
 --ro-bind $HOME/Documents $HOME/Documents \

 bash-4.4$ ls -a
 .  ..  .Xauthority  Documents

* A tmpfs filesystem is created after the bind mounting of  and overlays it so that only the Documents directory is visible within the sandbox:

 --ro-bind $HOME/.Xauthority $HOME/.Xauthority \
 --tmpfs $HOME \
 --ro-bind $HOME/Documents $HOME/Documents \

 bash-4.4$ ls -a
 .  ..  Documents

## p7zip
Applications which have not yet been patched against known vulnerabilities constitute prime candidates for bubblewrapping:

* Bind as read-only the host  executable path to the sandbox
* Create a symbolic link from the system  directory to  in the sandbox
* Blacklist the sandboxed contents of  and  with tmpfs overlays
* Mount a new devtmpfs filesystem to  in the sandbox
* Bind as read-write the host  directory to the  directory in the sandbox
** 7za will only run in the host  directory and/or its subdirectories when called from the shell wrapper
* Create new cgroup/IPC/network/PID/UTS namespaces for the application and its processes
** If the kernel does not support non-privileged user namespaces, skip its creation and continue
** Creation of a new network namespace prevents the sandbox from obtaining network access
* Add a custom or an arbitrary hostname to the sandbox such as
* Unset the  environment variable to hide the location of the X11 connection cookie
** 7za does not need to connect to an X11 display server to function properly
* Start a new terminal session to prevent keyboard input from escaping the sandbox

 #!/bin/sh
 #~/bwrap/pz7ip.sh
 (exec bwrap \
 --ro-bind /usr/bin/7za /usr/bin/7za \
 --symlink usr/lib /lib64 \
 --tmpfs /usr/lib/modules \
 --tmpfs /usr/lib/systemd \
 --dev /dev \
 --bind /sandbox /sandbox \
 --unshare-all \
 --hostname p7zip \
 --unsetenv XAUTHORITY \
 --new-session \
 /usr/bin/7za "$@")

 bwrap \
 --ro-bind /usr/bin/7za /usr/bin/7za \
 --ro-bind /usr/bin/ls /usr/bin/ls \
 --ro-bind /usr/bin/sh /usr/bin/sh \
 --symlink usr/lib /lib64 \
 --tmpfs /usr/lib/modules \
 --tmpfs /usr/lib/systemd \
 --dev /dev \
 --bind /sandbox /sandbox \
 --unshare-all \
 --hostname p7zip \
 --unsetenv XAUTHORITY \
 --new-session \
 /usr/bin/sh
 bash: no job control in this shell
 bash-4.4$ ls -AF
 dev/  lib64@  usr/
 bash-4.4$ ls -l /usr/lib/modules
 total 0
 bash-4.4$ ls -l /usr/lib/systemd
 total 0
 bash-4.4$ ls -AF /dev
 console  full  null  ptmx@  pts/  random  shm/  stderr@  stdin@  stdout@  tty  urandom  zero
 bash-4.4$ ls -A /usr/bin
 7za  ls  sh

## Firefox
Network facing applications with large surface attack areas are also ideal candidates to be bubblewrapped:

* Transmission included in the sandbox to launch with magnet and torrent links
* Example wrap supports audio (PulseAudio) and printing (CUPS/Avahi) under GNOME (Wayland)
** Paths in  should reflect the  variable
* Full paths are used to allow for keyboard bindings in environments which do not support variable expansion.
* WebRenderer and hardware (accelerated) compositing support included

 bwrap \
 --symlink usr/lib /lib \
 --symlink usr/lib64 /lib64 \
 --symlink usr/bin /bin \
 --symlink usr/bin /sbin \
 --ro-bind /usr/lib /usr/lib \
 --ro-bind /usr/lib64 /usr/lib64 \
 --ro-bind /usr/bin /usr/bin \
 --ro-bind /usr/lib/firefox /usr/lib/firefox \
 --ro-bind /usr/share/applications /usr/share/applications \
 --ro-bind /usr/share/gtk-3.0 /usr/share/gtk-3.0 \
 --ro-bind /usr/share/fontconfig /usr/share/fontconfig \
 --ro-bind /usr/share/icu /usr/share/icu \
 --ro-bind /usr/share/drirc.d /usr/share/drirc.d \
 --ro-bind /usr/share/fonts /usr/share/fonts \
 --ro-bind /usr/share/glib-2.0 /usr/share/glib-2.0 \
 --ro-bind /usr/share/glvnd /usr/share/glvnd \
 --ro-bind /usr/share/icons /usr/share/icons \
 --ro-bind /usr/share/libdrm /usr/share/libdrm \
 --ro-bind /usr/share/mime /usr/share/mime \
 --ro-bind /usr/share/X11/xkb /usr/share/X11/xkb \
 --ro-bind /usr/share/icons /usr/share/icons \
 --ro-bind /usr/share/mime /usr/share/mime \
 --ro-bind /etc/fonts /etc/fonts \
 --ro-bind /etc/resolv.conf /etc/resolv.conf \
 --ro-bind /usr/share/ca-certificates /usr/share/ca-certificates \
 --ro-bind /etc/ssl /etc/ssl \
 --ro-bind /etc/ca-certificates /etc/ca-certificates \
 --dir "$XDG_RUNTIME_DIR" \
 --ro-bind "$XDG_RUNTIME_DIR/pulse" "$XDG_RUNTIME_DIR/pulse" \
 --ro-bind "$XDG_RUNTIME_DIR/wayland-1" "$XDG_RUNTIME_DIR/wayland-1" \
 --dev /dev \
 --dev-bind /dev/dri /dev/dri \
 --ro-bind /sys/dev/char /sys/dev/char \
 --ro-bind /sys/devices/pci0000:00 /sys/devices/pci0000:00 \
 --proc /proc \
 --tmpfs /tmp \
 --bind /home/example/.mozilla /home/example/.mozilla \
 --bind /home/example/.config/transmission /home/example/.config/transmission \
 --bind /home/example/Downloads /home/example/Downloads \
 --setenv HOME /home/example \
 --setenv GTK_THEME Adwaita:dark \
 --setenv MOZ_ENABLE_WAYLAND 1 \
 --setenv PATH /usr/bin \
 --hostname RESTRICTED \
 --unshare-all \
 --share-net \
 --die-with-parent \
 --new-session \
 /usr/bin/firefox

## Enhancing privacy
* Further restrictions can be made by removing specific entries
** Remove the following entry to remove audio support:

 --ro-bind "$XDG_RUNTIME_DIR/pulse" "$XDG_RUNTIME_DIR/pulse" \

*  represents an arbitrary location defined by the user to hold desired profile information
** This allows for the use of a sanitized profile copied into  via a script/cron job or manually e.g.

 $ cp -pR ~/.mozilla /sandbox/

The location can be a network share, a USB mount, or a local filesystem or ramfs/tmpfs location

* Set  to obscure the actual
* Set new user ID and group ID values

 bwrap \
 ....
 --bind /sandbox/.mozilla /home/r/.mozilla \
 --bind /sandbox/Downloads /home/r/Downloads \
 ...
 --setenv HOME /home/r \
 ...
 --uid 200 --gid 400 \
 ...
 /usr/bin/firefox --no-remote --private-window

## Chromium
A simple chromium sandbox on wayland and with pipewire:

* PipeWire:
** If you are not using pipewire, feel free to remove this line
*  mounts your chromium configuration directory in the sandbox as readable and writable
*  mounts your ~/Downloads directory in the sandbox as readable and writable
* This example can be further improved for more isolation.

## Steam
Steam requires access to the D-Bus system in order to function properly.

The following script uses xdg-dbus-proxy to expose restricted host bus access to the sandbox. This proxy will terminate once bwrap exits.

{{hc|steam.py|2=
#!/usr/bin/env python3
from glob import glob
import os
from pathlib import Path
import subprocess

HOME = Path.home()
XDG_RUNTIME_DIR = Path(os.getenv("XDG_RUNTIME_DIR", "/tmp"))
XDG_CACHE_HOME = Path(os.getenv("XDG_CACHE_HOME", HOME / ".cache"))
XDG_DATA_HOME = Path(os.getenv("XDG_DATA_HOME", HOME / ".local/share"))
DBUS_PROXY_PATH = XDG_RUNTIME_DIR / "bus-proxy"
DBUS_PROXY_PATH.mkdir(exist_ok=True, parents=True)

#
STEAM_HOME = XDG_DATA_HOME / "steam_home"
STEAM_HOME.mkdir(exist_ok=True, parents=True)

# xdg-dbus-proxy
r, w = os.pipe()
session_bus_proxy = DBUS_PROXY_PATH / str(os.getpid())
system_bus_proxy = DBUS_PROXY_PATH / f"{os.getpid()}-system"
subprocess.Popen([
    "/usr/bin/xdg-dbus-proxy",
    f"--fd={w}",
    # session bus
    os.environstr(session_bus_proxy),
    "--filter",
    "--own=com.steampowered.*",
    "--talk=org.freedesktop.portal.*",
    "--talk=org.gnome.SettingsDaemon.MediaKeys",
    "--talk=org.kde.StatusNotifierWatcher",
    "--talk=org.freedesktop.ScreenSaver",
    "--talk=org.freedesktop.PowerManagement",
    "--talk=org.freedesktop.Notifications",
    # systrem bus
    "unix:path=/run/dbus/system_bus_socket",
    str(system_bus_proxy),
    "--filter",
    "--talk=org.freedesktop.UPower",
    "--talk=org.freedesktop.UDisks2",  # used by wine
, pass_fds=# wait xdg-dbus-proxy to start
os.read(r, 1)
os.set_inheritable(r, True)

# bwrap
argv: list[str = [
    "bwrap",
    "--bind", str(STEAM_HOME), str(HOME),
    "--proc", "/proc",
    "--dev", "/dev",
    "--dir", "/tmp",
    "--unshare-cgroup-try",
    "--unshare-pid",
    "--unshare-user-try",
    "--unshare-uts",
    "--die-with-parent",
    "--sync-fd", str(r), # ensures dbus proxy stops when the bwrap bwrap quits
    "--bind", str(system_bus_proxy), "/run/dbus/system_bus_socket",
    "--bind", str(session_bus_proxy), str(XDG_RUNTIME_DIR / "bus"),
]
def rw(*paths): argv.extend(for path in paths for i in ("--bind-try", str(path), str(path)))
def ro(*paths): argv.extend(for path in paths for i in ("--ro-bind-try", str(path), str(path)))
def dev(*paths): argv.extend(for path in paths for i in ("--dev-bind-try", str(path), str(path)))
def link(*links): argv.extend(for link in links for i in ("--symlink", str(link[0), str(linkrw(
    "/usr",
    "/etc",
    "/opt",
    "/run/systemd/resolve/",
    # WARNING: Forwarding the X11 is insecure and might lead to sandbox escapes
    "/tmp/.X11-unix",
    "/tmp/.ICE-unix",
    *glob(str(XDG_RUNTIME_DIR / "wayland*")),
    # audio
    "/var/lib/alsa/",
    *glob(str(XDG_RUNTIME_DIR / "pulse*")),
    *glob(str(XDG_RUNTIME_DIR / "pipewire*")),
    # shader cache
    XDG_CACHE_HOME / "mesa_shader_cache",
    XDG_CACHE_HOME / "mesa_shader_cache_db",
    XDG_CACHE_HOME / "nv",
    XDG_CACHE_HOME / "nvidia",
    XDG_CACHE_HOME / "radv_builtin_shaders",
    XDG_CACHE_HOME / "radv_builtin_shaders64",
    # steam
    XDG_DATA_HOME / "Steam",
)
link(
    ("/usr/bin", "/bin"),
    ("/usr/bin", "/sbin"),
    ("/usr/lib", "/lib"),
    ("/usr/lib64", "/lib64"),
    ("/run", "/var/run"),
)
dev(
    "/dev/dri",
    "/dev/input",
    "/dev/hugepages",
    *glob("/dev/nvidia*"),
    "/dev/snd",
    "/dev/fuse",
    "/sys/block/",
    "/sys/bus/",
    "/sys/class/",
    "/sys/dev/",
    "/sys/devices/",
    "/sys/module/",
)
os.execvp("bwrap", argv + ["--sync-fd", str(r), "/usr/lib/steam/steam")
}}
* This script mounts  as . You can modify the  variable to use a different location
* Use the  or  functions to grant read/write or read-only access, respectively, to a host path. For example, .

## NPM, Node Version Manager (NVM), Maven Java
In order to be able to run npm in a project root you can use the following command.

It works in combination with Angular, Cypress and Maven Java. X11 and wayland are on top included because Cypress starts a GUI based on electron.

It allows full file access to the current directory where it is run from. Assuming you execute  in the current project root where npm needs to write to , , etc. Also access to global npm install directory and nvm is allowed (). Furthermore X11 with cypress is also able to run and even wayland apps.

{{bc|1=
bwrap_arguments=(
    # no zombies
    --die-with-parent

    # network required for dependencies
    --unshare-all
    --share-net

    # create environment for a properly running shell
    --tmpfs /
    --tmpfs /run
    --dir /tmp
    --dev /dev
    --proc /proc
    --ro-bind /bin /bin
    --ro-bind /sbin /sbin
    --ro-bind /usr /usr
    --ro-bind /etc /etc
    --ro-bind /lib /lib
    --ro-bind /lib64 /lib64
    --ro-bind /sys /sys
    --ro-bind /var /var

    # systemd-resolve for dns
    --ro-bind /run/systemd/resolve /run/systemd/resolve

    # git is used by npm to init repos, config necessary for email username
    --ro-bind $XDG_CONFIG_HOME/git/config $XDG_CONFIG_HOME/git/config

    # zsh has to look everywhere cool
    --ro-bind $XDG_CONFIG_HOME/zsh/.zshrc $XDG_CONFIG_HOME/zsh/.zshrc
    --ro-bind $XDG_CONFIG_HOME/zsh/.zshenv $XDG_CONFIG_HOME/zsh/.zshenv
    --ro-bind $HOME/.zshenv $HOME/.zshenv

    # Maven
    --ro-bind /opt/maven /opt/maven
    --ro-bind $HOME/.m2 $HOME/.m2

    # NPM
    --bind "$XDG_DATA_HOME/npm" "$XDG_DATA_HOME/npm"

    # cache is needed by many programs like npm, cypress, nvm, maven
    --bind "$XDG_CACHE_HOME" "$XDG_CACHE_HOME"

    # x11, needed for cypress
    --ro-bind "$XAUTHORITY" "$XAUTHORITY"

    # wayland, might be useful
    --ro-bind "$XDG_RUNTIME_DIR/$WAYLAND_DISPLAY" "$XDG_RUNTIME_DIR/$WAYLAND_DISPLAY"

    # current dir is assumed to be project dir and full access is allowed
    --bind "$(pwd)" "$(pwd)"
)

# run bwrap with the arguments specified above and with the command provided by the user: zsh, npm install, etc
$ bwrap "${bwrap_arguments@}" "$@"
}}
