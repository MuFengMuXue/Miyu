## Before installing

**Note**: these instructions are community-maintained and are not supported by the Sway project.

This document will guide you through installing Sway on Debian 10 (Buster).

## Nightly builds

There exists a [Debian repository](https://apt.quantum2.xyz/sway-utils/) that includes Debian 10-compatible `sway` package which is rebuilt nightly. Run following commands in order to install Sway from the repository:

```
curl -L https://quantum2.xyz/apt.key | sudo apt-key add -
echo 'deb [arch=amd64] https://apt.quantum2.xyz/sway-utils/ buster main' | sudo tee /etc/apt/sources.list.d/sway-utils.list
sudo apt update
sudo apt install sway
```

Note that as these packages track master, they may be less stable than the latest official Sway release.

## Sway 1.4 installation from source
proceed with the manual steps below for installing sway 1.4.

Make sure you have activated the `contrib` and `non-free` apt repositories.
```
sudo sed -i -e 's/main$/main contrib non-free/g' /etc/apt/sources.list
```

Update apt cache:

```
sudo apt update
```

Make sure you have meson (>= 0.53.1)
Depends ninja-build (>= 1.6) and python3
if the meson version is satisfied skip next part (go to **install 1.4 continued**)

### Debian stable steps
The stable debian apt source list uses a 0.49.2 version of meson.

**get newer version of meson**
listed here there is 3 ways of doing that

1. A **safe and easy** method is to download the deb directly from packages.debian.org and use `sudo apt install /path/to/package/name.deb` or **gdebi** to try and install it. If there’s dependency issues with the stable libraries, it will refuse to do so.

2. **Debian specifically advises against the following method** Add the debian sid mirror to your apt/sources.list [discouraged](https://wiki.debian.org/DebianUnstable)
example: `deb http://ftp.de.debian.org/debian sid main`
Then again update the apt cache: `sudo apt update` and install newest meson `sudo apt install meson`
then you can go and remove the sid mirror from your apt/sources.list and avoid 1000+ upgradable apt packages in sid compared to buster (if you do not remove the sid mirror after installing meson and you run a `sudo apt update && sudo apt upgrade` you may render your system unstable)

Please note that acquiring newer software in this manner is [discouraged](https://wiki.debian.org/DebianUnstable). _Attempting to mix packages between Debian repositories can create unstable situations_. If you wish to use newer software, it is *best* to install packages from [backports](https://backports.debian.org/Instructions/). Unfortunately as of now the backports only have meson (0.52.1)
In general, mixing stable and upstream Debian repos will lead to dependency problems down the road. Later many packages can end up being uninstallable. Debian specifically advises against this method.

3. The **very best** method, though it’s the most work, is to backport the newer package from the source code against the stable libraries. This does take some skill for some packages, but absolutely will not break anything.
[Build a Package from Source](http://forums.debian.net/viewtopic.php?f=16&t=38976)

Nevertheless whatever way you choose and you now have meson (>= 0.53.1). Continue with the following steps.

### install 1.4 continued

Create a directory to organize sources:

```
mkdir ~/sway-src
```

### Install wlroots

First we'll install [wlroots](https://github.com/swaywm/wlroots) 0.10 with almost all extra dependencies (for now meson have been removed from this install line, it will return as soon as the debian stable (buster) apt meson package have been updated to >=0.53.1):
````
sudo apt install build-essential cmake libwayland-dev wayland-protocols \
 libegl1-mesa-dev libgles2-mesa-dev libdrm-dev libgbm-dev libinput-dev \
 libxkbcommon-dev libudev-dev libpixman-1-dev libsystemd-dev libcap-dev \
 libxcb1-dev libxcb-composite0-dev libxcb-xfixes0-dev libxcb-xinput-dev \
 libxcb-image0-dev libxcb-render-util0-dev libx11-xcb-dev libxcb-icccm4-dev \
 freerdp2-dev libwinpr2-dev libpng-dev libavutil-dev libavcodec-dev \
 libavformat-dev universal-ctags

sudo apt install libelogind-dev libxcb-util0-dev

cd ~/sway-src
git clone https://github.com/swaywm/wlroots.git
cd wlroots
git checkout 0.10.0
meson build
sudo ninja -C build install
````

### Install json-c

Debian's json-c version is too old, we need to manually build a newer version:

```
sudo apt install autoconf libtool

cd ~/sway-src
git clone https://github.com/json-c/json-c.git
cd json-c
git checkout json-c-0.13.1-20180305
sh autogen.sh
./configure --enable-threading --prefix=/usr/local
CPUCOUNT=$(nproc)
make -j$CPUCOUNT
sudo make install
sudo ldconfig
```

### Install scdoc (optional)

scdoc is needed for manual pages generation, which I recommend, but Debian's (stable) scdoc version is also too old, we need to manually build a newer version (or get it via [backports](https://packages.debian.org/buster-backports/scdoc)):

```
cd ~/sway-src
git clone https://git.sr.ht/~sircmpwn/scdoc
cd scdoc
git checkout 1.10.1
make PREFIX=/usr/local -j$CPUCOUNT
sudo make PREFIX=/usr/local install
```

### Install sway

Next we'll install sway 1.4:
````
sudo apt install libpcre3-dev libcairo2-dev libpango1.0-dev libgdk-pixbuf2.0-dev xwayland

cd ~/sway-src
git clone https://github.com/swaywm/sway.git
cd sway
git checkout 1.4
meson build
sudo ninja -C build install
````

### Install swaybg

We need to install swaybg, or else the default configuration won't work:
```
cd ~/sway-src
git clone https://github.com/swaywm/swaybg.git
cd swaybg
git checkout 1.0 
meson build
sudo ninja -C build install
```

### Using `sway`

If you already have another desktop environment installed, you may be unable to boot to `sway` without messing with your display manager. To prevent your display manager from starting up on boot you can disable it via Systemd:
````
sudo systemctl disable gdm3.service
````
`gdm3` is used as an example here, your display manager may differ.

Alternatively, you may prefer to switch the target environment to use by default from `graphical.target` to `multi-user.target`. More information on how Systemd targets work is described in [this article](https://www.digitalocean.com/community/tutorials/systemd-essentials-working-with-services-units-and-the-journal).

The simple instructions are to first check to see that you are actually using `graphical.target` with the command `systemctl get-default`.

If you are, check to make sure that no critical services will be disabled when changing to `multi-user target`:
````
$ systemctl list-dependencies graphical.target
graphical.target
● ├─accounts-daemon.service
...
● └─multi-user.target
●   ├─anacron.service
...
●   ├─basic.target
●   │ ├─-.mount
...
````
Only items that are children `multi-user.target` will remain active. If there are any essential services that are direct children of `graphical.target` or children of another target that depends on it, you can move their .service file from their appropriate `/lib/systemd/system/<target_name>.target.wants` to the `/lib/systemd/system/multi-user.wants` directory.

You can then change to use the multi-user target:
````
systemctl set-default multi-user.target
````

By changing to the multi-user.target, you will be prompted to log in at a tty. After logging in you can run `sway` to start up your new window manager. If you would like to have sway start automatically on a specific tty, you can configure your `.bash_profile` file to do so:

````
if [[ -z $DISPLAY ]] && [[ $(tty) = /dev/tty1 ]]; then
  exec sway
fi
````

If you are on a single-user system and are used to having your account auto-login, you can configure `getty` to log you into the same tty that you have set to automatically execute sway. See the [Arch Wiki](https://wiki.archlinux.org/index.php/Getty#Automatic_login_to_virtual_console) on this topic. Note that this should only be done if you have some other layer of security such as a password-protected filesystem which is decrypted on boot.