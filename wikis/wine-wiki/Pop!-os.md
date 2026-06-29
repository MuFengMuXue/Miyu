# Building Wine in Pop!_OS

While Pop!_OS, like Ubuntu, has support for multi-arch libraries, some
i386 packages that are required to build a 32-bit version of Wine may
conflict with pre-installed system packages, so you won't be able to
install them.

For this reason, in this tutorial we will use LXD to create a 64-bit
Ubuntu LXC container were we will install the required packages, build
Wine with WoW64 support, and then use it to our host system.

We start by creating a working directory:

```sh
$ mkdir $HOME/wine-dir
$ cd $HOME/wine-dir
```

## Setting up an LXC container

This Section is based on the [official Pop!_OS documentation on
containers](https://support.system76.com/articles/containers/).

We use LXD to create the Ubuntu container.

Install LXD through snap:

```sh
$ sudo apt install snapd
$ snap install lxd
```

Add your current user to the lxd group so that it has the correct
permissions to use the application:

```sh
$ sudo usermod -aG lxd $USER
$ reboot # to apply permissions.
```

Initialize LXD:

```sh
$ lxd init
```

If you don't want containers to automatically start on boot:

```sh
$ lxc profile set default boot.autostart false
```

Launch an Ubuntu container:

```sh
$ lxc launch ubuntu:20.04 wine-container
```

Start the container:

```sh
$ lxc list
$ lxc start wine-container
```

and update:

```sh
$ lxc exec wine-container -- apt update
```

To enter container, use the following command:

```sh
$ lxc exec wine-container -- /bin/bash
```

In order to share files between the host and the container, we have two
options:

- \(a\) Setup a shared host directory inside the LXC container in
  read-write mode.
- \(b\) Pull and push directories every time we need to.

Option (a) is probably the most comfortable in the long run, if you need
to compile wine many times, but it requires special permissions and a
longer setup.

We will use Option (a) in this tutorial. For Option (b) see [Pushing
and pulling files from the container without a shared
directory](#pushing-and-pulling-files-from-the-container-without-a-shared-directory).

## Setup a shared host directory inside the LXC container

This Section is based on a [tutorial from
nixCraft](https://www.cyberciti.biz/faq/how-to-add-or-mount-directory-in-lxd-linux-container/).

### Allow remaping the user ID in the host

First, we need to know our user id in the host, for that purpose we can
use the `id` command:

```sh
$ id
```

This is an example output:

```
uid=1000(alice) gid=1000(alice) groups=1000(alice),4(adm),27(sudo),121(lpadmin),999(lxd)
```

We see that our user (alice in this example) has user id (uid) 1000, and
group id (gid) 1000.

Now, we need to give permission to the root user (and thus, the LXD
daemon) to remap the user id and the group id.

We do that by adding new lines to the `/etc/subuid` and `/etc/subgid`
files, respectively:

```sh
$ echo "root:1000:1" | sudo tee -a /etc/subuid
$ echo "root:1000:1" | sudo tee -a /etc/subgid
```

where we need to replace the `1000` with our uid in the first line, and
to replace the `1000` with our gid in the second line.

### Remap user ID inside the container

The next step is to remap the user ID inside the container, so we need
to enter it, with the aforementioned command:

```sh
$ lxc exec wine-container -- /bin/bash
```

After entering the container, we need to know if our user is already
present inside:

```
# grep '^alice' /etc/passwd
```

If no line appears, we need to create it:

```
# adduser alice
```

We now need the uid and gid our user inside the container:

```
# id alice
```

This is an example output:

```
uid=1001(alice) gid=1001(alice) groups=1001(alice)
```

in this case the uid and the gid are 1001.

Now we go back to the host, and map both the uid and gid from our user
in the host to our user in the container:

```sh
$ lxc config set wine-container raw.idmap "both 1000 1001"
```

where we replace the 1000 and 1001 accordingly.

And we restart the container:

```sh
$ lxc restart wine-container
```

Finally, we can mount the directory:

```sh
$ lxc config device add wine-container wine-dir disk source=$HOME/wine-dir path=/root/wine-dir
```

## Download the wine source code

We clone the wine repo inside the wine-dir directory, in the host
system:

```sh
$ cd $HOME/wine-dir
$ git clone https://gitlab.winehq.org/wine/wine.git wine-source
```

We can then select a specific branch or tag:

```sh
$ cd wine-source
$ git checkout stable
```

## Install wine dependencies in the container

We need access to the source code repositories inside the container, so
we enter the container again:

```sh
$ lxc exec wine-container -- /bin/bash
```

Uncomment all `deb-src` lines after uncommented `dev` lines in
`/etc/apt/sources.list` using `nano` or `vim`:

```
# nano /etc/apt/sources.list
```

Also, add the i386 arch, and **update**:

```
# dpkg --add-architecture i386
# apt update
```

Install both x86-64 and i386 wine dependencies

```
# apt-cache depends wine # Just lists distro's wine package dependencies.
# apt build-dep wine64
# apt build-dep wine32:i386
# apt install gcc-multilib g++-multilib
# apt install libx11-dev:i386 libfreetype-dev:i386 libgnutls28-dev:i386 ocl-icd-opencl-dev:i386 libvulkan-dev:i386
# apt install gcc-mingw-w64
```

In case you need more, check the [Building
Wine](Building-Wine#satisfying-build-dependencies) page.

This is a list of packages that works at the time of writing:

```
# apt install libgl-dev libpulse-dev libdbus-1-dev libfontconfig-dev libxrender-dev gettext libxcursor-dev libxi-dev libxrandr-dev libxfixes-dev libxinerama-dev libxcomposite-dev libosmesa6-dev libpcap-dev libsane-dev libusb-1.0-0-dev libv4l-dev libgphoto2-dev libgphoto2-dev libudev-dev libsdl2-dev libcapi20-dev libkrb5-dev libopenal-dev libldap-dev libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev libgstreamer-plugins-good1.0-dev libpng-dev libjpeg-dev libtiff-dev
```

and their i386 versions:

```
# apt install libgl-dev:i386 libpulse-dev:i386 libdbus-1-dev:i386 libfontconfig-dev:i386 libxrender-dev:i386 gettext:i386 libxcursor-dev:i386 libxi-dev:i386 libxrandr-dev:i386 libxfixes-dev:i386 libxinerama-dev:i386 libxcomposite-dev:i386 libosmesa6-dev:i386 libpcap-dev:i386 libsane-dev:i386 libusb-1.0-0-dev:i386 libv4l-dev:i386 libgphoto2-dev:i386 libgphoto2-dev:i386 libudev-dev:i386 libsdl2-dev:i386 libcapi20-dev:i386 libkrb5-dev:i386 libopenal-dev:i386 libldap-dev:i386 libgstreamer1.0-dev:i386 libgstreamer-plugins-base1.0-dev:i386 libgstreamer-plugins-good1.0-dev:i386 libpng-dev:i386 libjpeg-dev:i386 libtiff-dev:i386
```

We can also install ccache to lower our build times in case we need to
build Wine many times:

```
# apt install ccache
```

And other packages that you may want, such as `valgrind:i386`.

## Building 64-bit wine

Let's start by building a 64-bit version of Wine inside the container.

```
# cd /root/wine-dir
# mkdir wine64
# cd wine64
# ../wine-source/configure --enable-win64 CC="ccache gcc" CROSSCC="ccache x86_64-w64-mingw32-gcc"
```

Where the CROSSCC option allows cross compiling modules as PE.

If you don't use ccache, remove `ccache` in both arguments.

Read the configure script output. If you need more libraries, install
them as in the previous step, otherwise continue.

Run:

```
# make -j8 # or as many CPU threads you have available.
```

## Building 32-bit wine-tools

Now we need to build a 32-bit version of Wine and inject it into our
64-bit Wine build to turn it into a WoW64 Wine, so that it supports
32-bit Windows applications, since most of them indeed are 32-bit.

Before we build a 32-bit wine, we need the 32-bit wine-tools, so we make
a provisional 32-bit version of Wine:

```
# cd /root/wine-dir
# mkdir wine32-tools
# cd wine32-tools
# ../wine-source/configure CC="ccache gcc" CROSSCC="ccache i686-w64-mingw32-gcc"
# make -j8 # or as many CPU threads you have available.
```

If you don't use ccache, remove `ccache` from the options.

## Building 32-bit wine

```
# cd /root/wine-dir
# mkdir wine32
# cd wine32
```

Configure and make:

```
# ../wine-source/configure --with-wine64=../wine64 --with-wine-tools=../wine32-tools CC="ccache gcc" CROSSCC="ccache i686-w64-mingw32-gcc"
# make -j8 # or as many threads you have available.
```

Again, if you don't use ccache, remove `ccache` from the options.

## Fixing symbolic links

Some links may have absolute paths for within the container. These need
to be fixed.

We can inspect all the symbolic links:

```sh
$ cd $HOME/wine-dir
$ find wine32 wine64 wine32-tools -type l -ls
```

In particular the offending ones:

```sh
$ find wine32 wine64 wine32-tools -type l -ls | grep '-> /root/'
```

At the moment of writing, there are two links that need to be changed,
the ones that the 64-bit build uses to refer to the 32-bit build:

```
wine64/loader/wine -> /root/wine-dir/wine32/loader/wine
wine64/loader/wine-preloader -> /root/wine-dir/wine32/loader/wine-preloader
```

We change them inside the container:

```
# cd /root/wine-dir
# rm wine64/loader/wine wine64/loader/wine-preloader
# ln -s ../../wine32/loader/wine wine64/loader/wine
# ln -s ../../wine32/loader/wine-preloader wine64/loader/wine-preloader
```

## Install runtime dependencies in the host system

Wine requires access to some dynamic system libraries to run.

As mentioned in the [Building
Wine](Building-Wine#runtime-dependencies) section of the Building Wine
page, the easiest way to achieve this is to install the wine package
provided by the distribution in the host system:

```sh
$ apt install wine
```

Keep in mind that the `wine` command will execute the version of wine
that this package installs, and not the one you build.

You may also want to install optional runtime dependencies such as:

```sh
$ apt install corefonts
```

## Run wine

You should be able to run wine from your build now, remember to use it
with a prefix.

```sh
$ PREFIX=$HOME/wine-dir/wine-prefix $HOME/wine-dir/wine64/wine --version
```

We can stop the container now

```sh
$ lxc stop wine-container
```

## Pushing and pulling files from the container without a shared directory

If you don't want to set up a shared directory between the host and the
container, an alternative is to use the `lxc file push` and
`lxc file pull` commands to send and retireve files from the container.

The syntax is:

```sh
$ lxc file push -r <host-src-directory> wine-container/root/<container-dst-directory>
$ lxc file pull -r wine-container/root/<container-dst-directory> <host-dst-directory>
```

Keep in mind that symbolic links end up invalid in the host system after
pulling, because `lxc file pull` makes their paths absolute and
respective to the container filesystem. Check the symbolic links using:

```sh
$ find <pulled-directory> -type l -ls
```

We can fix them running the following `link_fixer.sh` script in the same
folder we pulled the directory.

```sh
#!/bin/bash

PULLED_DIRECTORIES="$@"

find $PULLED_DIRECTORIES -type l | while read symlink; do
    if [ ! -e "$symlink" ]; then
        old_path=$(readlink "$symlink")
        # Remove the '/root/' prefix and change it with the current path ${PWD}
        new_path=${old_path/\/root\//${PWD}\/}
        new_path=$(realpath --relative-to="$(dirname "$symlink")" "$new_path")
        ( set -x; ln -f -s "$new_path" "$symlink")
    fi
done
```

```sh
$ bash link_fixer.sh <host-dst-directory>
```
