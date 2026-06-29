Interested in compiling wine from source? Want to submit some patches, run a bisection, or maybe just install a patch to make your favorite game work? You've come to the right place.

## Preliminaries

Before you compile a single line of code, there are a few things you need in order to build wine successfully.

### Getting the Wine Source

You can download the Wine source code as a tarball from several places (including the [Wine Download server](https://dl.winehq.org/wine/source/)), but if you plan to do any actual testing or developing, you'll want to use [git](https://git-scm.com/). For more information and some useful hints, see [Git Wine Tutorial](Git-Wine-Tutorial) and the [Source Code](Source-Code) wiki page.

To grab the source code to wine itself, just enter the following command, replacing the directory path at the end with whatever folder you want to download the source tree into:

```sh
$ git clone https://gitlab.winehq.org/wine/wine.git ~/wine-dirs/wine-source
```

### Satisfying Build Dependencies

Once you have the source code, it's time to grab all of the necessary build tools and libraries. If you have a unix with package management, probably the quickest way to find _most_ of the software you need is to use whatever "build dependency" command your package manager offers.

Unfortunately, that by itself probably won't get everything. Dependencies for features you want may be marked as optional or not even packaged in your distro's repository. Wine is still evolving as a project too and might switch over to different libraries between versions, something that especially comes into play if you use a stable distro with spaced out releases.

Some of the platforms and Linux distributions have their own page, which may include more tips about dependencies and compiling:

- [Debian/Ubuntu](Debian-Ubuntu)
- [CentOS/RHEL](CentOS-RHEL)
- [FreeBSD](FreeBSD)
- [MacOS](MacOS-Building)
- [OpenSUSE](OpenSUSE)

While Wine has many dependencies on external libraries, not all of them are actually necessary to build Wine, or indeed to run whatever program you're interested in running. The following table details Wine's build dependencies and what they are used for.

| Library name | Debian | Fedora | Arch | Function | Notes |
|--------------|--------|--------|------|----------|-------|
| Generally necessary |  |  |  |  |  |
| 32-bit toolchain | gcc-multilib | glibc-devel.i686 | lib32-glibc | Needed for 32-bit builds |  |
| MinGW cross-compiler | gcc-mingw-w64 | mingw32-gcc, mingw64-gcc | mingw-w64-gcc | PE format DLLs |  |
| ALSA | libasound2-dev | alsa-lib-devel | alsa-lib | Sound backend | At least one is necessary for sound. |
| BlueZ | bluez | bluez | bluez | Bluetooth driver | Required with libdbus for Bluetooth support. |
| PulseAudio | libpulse-dev | pulseaudio-libs-devel | libpulse |  |  |
| libdbus | libdbus-1-dev | dbus-libs | dbus | Dynamic device detection (specifically, mass storage) | Removable drives may be incorrectly detected otherwise. |
| libfontconfig | libfontconfig-dev | fontconfig-devel | fontconfig | Host font enumeration | Install if you want host fonts to be detected. |
| libfreetype | libfreetype-dev | freetype-devel | freetype2 | FreeType font reading |  |
| libgnutls | libgnutls28-dev | gnutls-devel | gnutls | Cryptography |  |
| libinotify | N/A | N/A | N/A | File change notification | Only necessary for some platforms (Linux does not need this.) |
| OpenGL | libgl-dev | mesa-libGL-devel | mesa | Hardware-accelerated/3D graphics |  |
| libunwind | libunwind-dev | libunwind-devel | libunwind | Exception unwinding | Necessary for x86_64 and arm64, but not used on other platforms. |
| libX11 | libx11-dev | libX11-devel | libx11 | Window management | Used by the X11 driver. |
| XComposite | libxcomposite-dev | libXcomposite-devel | libxcomposite | Window drawing |  |
| XCursor | libxcursor-dev | libXcursor-devel | libxcursor | Cursor management |  |
| XFixes | libxfixes-dev | libXfixes-devel | libxfixes | Clipboard management |  |
| XInput 2 | libxi-dev | libXi-devel | libxi | Keyboard and mouse |  |
| XRandR | libxrandr-dev | libXrandr-devel | libxrandr | Display device management |  |
| XRender | libxrender-dev | libXrender-devel | libxrender | Window drawing |  |
| XShape, XShm | libxext-dev | libXext-devel | libxext | Window drawing |  |
| wayland-scanner | libwayland-bin | wayland-devel | wayland | Wayland protocol parsing | Only used by the Wayland driver as a build-time dependency. |
| Wayland Client | libwayland-dev | wayland-devel | wayland | Window management | Only used by the Wayland driver. |
| libEGL | libegl-dev | libglvnd-devel | libglvnd | OpenGL window support |  |
| Wayland EGL | libwayland-dev | wayland-devel | wayland | OpenGL window support |  |
| libxkbcommon | libxkbcommon-dev | libxkbcommon-devel | libxkbcommon | Keyboard support |  |
| libxkbregistry | libxkbregistry-dev | libxkbcommon-devel | libxkbcommon | Keyboard support |  |
| Needed for many applications |  |  |  |  |  |
| GStreamer 1.0 | libgstreamer1.0-dev, libgstreamer-plugins-base1.0-dev | gstreamer1-devel, gstreamer1-plugins-base-devel | gstreamer, gst-plugins-base-libs | Multimedia playback | Generally necessary for games or applications that play back audio or video files. |
| libSDL2 | libsdl2-dev | SDL2-devel | sdl2 | HID joystick support | Generally necessary for joystick or other HID support. Only one library is necessary, but they may exhibit different behaviour. |
| libudev | libudev-dev | systemd-devel | systemd |  |  |
| Vulkan | libvulkan-dev | vulkan-headers, vulkan-loader-devel | vulkan-icd-loader, vulkan-headers | Hardware-accelerated/3D graphics | Necessary for some games; only supported by some video cards. |
| Rare or domain-specific |  |  |  |  |  |
| libcapi20 | libcapi20-dev | (none) | (none) | ISDN/telephony | Install only if you're using ISDN software. |
| libcups | libcups2-dev | cups-devel | libcups | Printing | Install only if you need printer support. |
| libgphoto2 | libgphoto2-dev | libgphoto2-devel | libgphoto2 | Scanner/still image | Install only if you're using scanner/still image software. |
| libsane | libsane-dev | sane-backends-devel | sane |  |  |
| Kerberos | libkrb5-dev | krb5-devel | krb5 | Kerberos authentication | Install only if you're connecting via Kerberos. |
| libnetapi | samba-dev | samba-devel | smbclient | Networking | Rarely needed. |
| OpenCL | ocl-icd-opencl-dev | ocl-icd-devel | ocl-icd | Parallel computing / GPGPU | Install if you're using parallel computing or GPGPU software. |
| libpcap | libpcap-dev | libpcap-devel | libpcap | Packet capture | Install if you are using applications that require packet capture. (This replaces native wpcap.dll shipped by applications.) |
| libusb 1.0 | libusb-1.0-0-dev | libusbx-devel | libusb | USB device support | Install only if you're using an application that accesses a USB device directly. (Note that many applications using USB devices do so through HID.) See also [Hardware](Hardware). |
| libv4l2 | libv4l-dev | libv4l-devel | v4l-utils | Video capture | Install only if you're capturing video. |
| Never necessary |  |  |  |  |  |
| XFree86-VM | libxxf86vm-dev | libXxf86vm-devel | libxxf86vm | Display management | Obsolete; use XRandR instead. |
| Xinerama | libxinerama-dev | libXinerama-devel | libxinerama | Display management | Obsolete; use XRandR instead. |
| libhal | (none) | (none) | (none) | Dynamic device detection | Obsolete; use libdbus instead. |

If you're missing a library or program wine needs to build, the configure script should output a message specifically telling you what you still need to install. Ideally one run through would list all the missing software, but at least for now, the script terminates at the first check it fails. If you persist through the cycle (tedious, I know) of configure, install missing software, repeat, the script should finish and display a success message.

By the way, some features of wine (legacy, experimental, etc.) aren't enabled by default but can still be built into wine with the right libraries. On a successful run, the configure script should list all disabled features and which libraries enable them. To include those features, simply install the relevant libraries, then run the configure script one more time.

### Runtime Dependencies

If you actually want to run wine after you build it, you'll also need to install runtime dependencies too. The simplest way to do this for most systems is to install the wine release provided by your distro, along with all of its dependencies. Of course, if you use a very old distro, this might not work without forcing an upgrade for many of the dependencies.

Once you do have all dependencies installed, as long as you give your custom wine build its own wine-prefix, you should be able to run it (from inside the build directory) alongside the official repo version without conflicts.

If you would rather uninstall your distro's version of wine, you have a few options for what to do after uninstalling it:

- Just leave the dependencies alone. The main problem with this is your package manager might mark them as unnecessary, orphaned, autoremovable, etc.
- Mark the dependencies as manually installed through your package manager. This approach only causes problems if you want to entirely remove wine and its dependencies from your system later; a command such as autoremove won't uninstall packages marked as manually installed.
- Package your custom version of wine for installation. This definitely involves the most work, but should keep your package database consistent.

## Compiling

### New WoW64 Build

Most likely you want a "new WoW64" build, which can run both 32-bit and 64-bit Windows applications on 64-bit Linux without any 32-bit Linux libraries. Things should be very simple. Once all the build requirements are installed, go to the wine source directory and run:

```sh
$ ./configure --enable-archs=i386,x86_64
$ make -j`nproc`
```

[Installing wine](#installing-from-source) to /usr is optional. You can run wine entirely from within the build directory without installation:

```sh
$ ./wine <some-exe>
```

### 32-bit-only Build

If you want to build Wine on a **_32-bit_** system and run it on the same system, simply run the configure script without arguments, for example:

```sh
$ ./configure
$ make -j`nproc`
```

### 64-bit-only Build

If you're on a 64-bit system, all you need to do to build a 64-bit wine is pass `--enable-win64` to the configure script:

```sh
$ ../wine-source/configure --enable-win64
$ make -j`nproc`
```

The problem is that by itself, that build will only run applications compiled for 64-bit Windows. Since the vast majority of Windows applications have 32-bit installers even if the application itself is 64-bit, you very likely want to follow the [new WoW64](#new-wow64-build) instructions above or [old WoW64](#old-wow64-build) instructions below.

If you want to explicitly leave out an optional feature, even if you have its dependencies installed, the configure script has many options (`--without-PACKAGE`) to disable certain libraries. There are also some options to force including libraries that normally aren't by default (`--with-PACKAGE`). A second class of options can be used to disable or enable general features in wine (`--disable-FEATURE` and `--enable-FEATURE`).

If you plan on cross-compiling to a completely different architecture (not just 32-bit wine on a 64-bit system), you'll definitely want the `--with-wine-tools=` option. When you type it, just add the relative path to the _tools_ subdirectory of a wine build **compiled for your host system.** Unless you include this option (or a copy of the tools are cached where the build scripts can see them), the configure script will abort with an error if you also pass a cross-compiling option.

The configure script has a help flag (`-h`) that lists all relevant options and environment variables, along with a short description. The script also recognizes tab-completion so for a simple list of supported options, just type two hyphens after the `configure` command and hit tab a couple times.

If for any reason you need to pass flags to the compiler while building wine, you can set them with the CFLAGS environment variable during configuration.

### General Compiling Hints

You're perfectly free to build and install wine from within the source directory, _but_ using a separate build directory has many advantages. It keeps the source code uncluttered, makes testing distinct builds easier, allows for much cleaner cross-compilation, simplifies chroots or linux containers, etc.

Just getting started with building software on unix? You might have heard of `make clean`. The wine makefiles also include this rule, which will automatically clean out all the intermediate object files from the build directory. However, those same object files are how `make` knows what steps it can skip if you change the source code and recompile. So if you don't want to recompile all of wine from scratch after every patch, don't disturb the object files.

Maybe you've got one of those (so radically winning) solid-state drives, and you're wondering if compiling on your solid-state drive helps at all. A cruise around the internet shows mixed opinions. If you do see improvements, they'll likely be insignificant and mostly come from faster read times on the source files (processing power is the main bottleneck for compilers). At the same time, while it's not as much an issue as it used to be, solid-state drives are capable of a fixed number of write operations before wearing out. If you _really_ want to, there are ways to have your compiler read the source code from SSD, write the temporary build files into a directory on hard-disk (or even RAM), and even move the finished program back onto the SSD (see how cool separate build directories are?)

Instead of looking for a SSD to speedup your compile times, consider installing [ccache](https://ccache.samba.org/) if you'll be building from source repeatedly. Even with `make`, it adds more sophisticated caching that can be shared across directories. For a small time penalty during your first build, it can cut compile times significantly. Unless you're using another wrapper to your compiler (which makes things more complicated), you only need to set the CC environment variable to call your compiler from ccache, which can also be done specifically for your wine build when calling the configure script. For example, if you're using GCC:

```sh
$ ../wine-source/configure CC="ccache gcc" i386_CC="ccache i686-w64-mingw32-gcc" #your usual configure options
```

Be sure to replace `i386_CC="ccache i686-w64-mingw32-gcc"` with `x86_64_CC="ccache x86_64-w64-mingw32-gcc"` for 64-bit builds. If you have a multi-core processor, the `make` command has a [couple of flags](https://www.gnu.org/software/make/manual/html_node/Parallel.html) you might like.

- The `-j` flag tells `make` to try running independent recipes on different cores with maximum parallelism; an alternate form `-jN` will start up to _N_ recipes in parallel:

  `make -j5`
- Another option is the `-l F.F` flag, which only starts more recipes in parallel so long as the average system load doesn't exceed the floating-point number _F.F_.
- These features don't work for all projects, but they're designed to fail gracefully and revert to serial building when that happens.
- If you don't want to use your computer for anything else while building, a common rule-of-thumb is to set _N_ in `-jN` to (_the number of cores on your system + 1_) (the idea behind the extra job is to keep all cores running even when one pauses for IO requests).
- The parallelism in `make` usually shows diminishing marginal speed-up so if you want to work on your computer while building, don't hesitate to save yourself a few cores.
- Using configure cache using passing -C can speed up reconfigure. However, you may need to call configure without this flag when a new dependent library needs to be found.

  `../wine-source/configure -C ... #your usual configure options`

Furthermore, you can look into [distributing the build](https://gitlab.winehq.org/wine/wine/-/wikis/Distributed-build-with-icecream) by offloading part of it to under-utilised computers in your network.

### New WOW64 mode example with ccache - and tests disabled to compile faster

```sh
$ ../wine-source/configure CC="ccache gcc" i386_CC="ccache i686-w64-mingw32-gcc" x86_64_CC="ccache x86_64-w64-mingw32-gcc" --enable-archs=i386,x86_64 --disable-tests 
```

## Cross-Compiling

So compiling on the target 32-bit system is easy enough, but what if you're on a 64-bit system, or you're targeting a different architecture from your host system? Well... things get a little messier. The general idea is that you'll need to cross-compile wine for the target system, and the core problem is keeping multiple versions of the same libraries from colliding. Each architecture's version of a library needs to be kept separate from the others. Luckily, there are several techniques for doing this.

### Multi-Arch and Multi-lib

If your first thought about cross-compilation is something like, "Why can't I just install libraries for another architecture through my package manager, then build with those?" then you aren't alone. Many unix distributions have adjusted how packages are installed to allow for precisely that, but there are a few different approaches.

A distribution with [Multiarch](Multiarch) compatibility can have several versions of a library, sorted by _architecture_, installed on the same system. All the tools and software provided by the distribution should also be able to correctly determine which version to use, based on context or explicit parameters from the user.

There's also a more limited form of this capability called "multi-lib," which only distinguishes between [_ABIs_](https://en.wikipedia.org/wiki/Application_binary_interface) for a single architecture (_i686_ libraries on _amd64_ are perhaps the most prominent). A common approach to multi-lib is to have separate library directories for different versions (e.g. _/usr/lib32_ for _i686_ libraries on an _amd64_ system), then pass parameters to a multi-lib savvy compiler (such as GCC or Clang) at build time.

While most up-to-date distros have multi-lib capabilities, multi-arch is a work in progress, and most distros outside the Debian Linux family don't seem to consider it a priority. If your distro can handle your specific case though, multi-lib/multi-arch could be the quickest and cleanest way to cross-compile.

If you've installed the necessary libraries, wine's configure script should handle any multi-lib compiler flags for you.

For [Developers](Developers) on Debian-based distros, check out the [Multiarch](Multiarch) page for a list of wine dependencies that still aren't multi-arch compatible. Every package you can make multi-arch compatible helps Wine, Debian, its offspring (and probably other distros in time).

### Containers

If the host system can't keep track of different library versions itself, the next option is to cordon off part of the system and keep conflicting files and processes there. Over the past decade or so, kernel and filesystem-based containers have proven to be a very effective way of doing that.

This technique (also known as OS-level virtualization) strongly isolates sessions in different parts of the filesystem, while conserving resources by sharing kernel-space files and processes. While they can't contain completely different platforms, you can even theoretically run different distros in separate containers as long as they're all compatible with the same kernel (this usually takes a little tweaking though). Another major advantage of containers is that they're relatively simple to setup and use, with much fewer moving parts than a full virtual machine.

For example, to install LXC (Linux containers) on a Debian-based system and create a 32-bit container:

1. Install the lxc package first
2. Create a container from an i386 Ubuntu template, with your existing username and password and your home directory bind-mounted
3. Then start the container

On the command line, this will look something like:

```sh
$ sudo apt-get install lxc
$ sudo lxc-create -t ubuntu -n my32bitbox -- --bindhome $LOGNAME -a i386
$ sudo lxc-start -n my32bitbox
```

- If your container has the same user-space as the host, you can also copy over the apt configuration from the host (before starting the container). Otherwise, you'll probably need to manually edit those files inside the container:

  ```sh
  $ sudo cp -R /etc/apt /var/lib/lxc/my32bitbox/rootfs/etc
  ```
- Also, if a login prompt doesn't automatically appear when you start the container, just start a second terminal, then attach to the container and login with your normal credentials:

  ```sh
  $ sudo lxc-attach -n my32bitbox
  login
  ```

From there, all you need to do is grab the development software (e.g. git) and build dependencies, just like you did to build on the host system. Once you've set everything up, just compile wine while still inside the container.

Perhaps the main disadvantage of containers is that they typically require a whole new image of user-space for each container. As long as you have a typical computer and stable access to broadband internet, getting a system image shouldn't pose a problem though. One other issue with containers that may come up, particularly if you're just on a PC or laptop, is the way that low-level processes are handled by the host. It might take some work to setup things like wi-fi, which can be a real pain if you need to install packages.

**Popular Container Software:**

- [LXC](https://linuxcontainers.org/lxc/introduction/) (Linux Containers)
- Solaris/OpenIndiana [Zones](https://wiki.openindiana.org/oi/7.1+Zones)
- [FreeBSD Jails](https://www.freebsd.org/doc/handbook/jails.html)
- [Docker](https://www.docker.com/)

#### Distrobox
Consider setting up a development environment using `distrobox` and evaluating how it works for your needs. It's a container-based solution that provides tight integration with the host (filesystem, networking, windowing for GUI/graphical applications, etc.) out of the box. [This guide](https://gitlab.winehq.org/wine/wine/-/wikis/Distrobox-development-environment) is tailored to Wine development and explains how you can get a development environment set up within 10 minutes, with all build dependencies met and able to a [WoW64](#shared-wow64) build.

### Chroot

A [chroot](https://en.wikipedia.org/wiki/Chroot) (from "change root") is the classic way of handling this problem. In fact, the virtual containers described in the last section are essentially just evolved forms of chroot. A chroot uses a minimal yet complete environment that is isolated within a subtree of the filesystem. When the chroot is activated, a session begins that is sandboxed inside the chroot part of the file system. With the exception of mounting directories outside the chroot or processes with root permissions, the session can neither see nor access the wider host system.

Chroots are sort of low-level, and like most low-level things, can be a double-edged sword... extremely flexible, but sometimes not the easiest to use. That's where a program (like [schroot](https://wiki.debian.org/Schroot)) that helps manage and configure all of the chroots on your system can really come in handy. Besides allowing chroot access as a normal user and simple configuration files, schroot automatically bind-mounts certain directories on the host environment for you (including $HOME by default... very convenient).

On an Ubuntu system, you can use schroot and debootstrap to install a chroot for building 32-bit wine like so...

1. Install the schroot and debootstrap packages
2. Create a schroot config file
3. Make a chroot folder and install a bare-bones version of Ubuntu in it
4. Setup the chroot's APT repository and enter the chroot
5. Install some basic packages that debootstrap skips

On the command line, step 1 will look like:

```sh
$ sudo apt-get install schroot debootstrap
$ sudo nano (or other editor) /etc/schroot/chroot.d/ubuntu_i386.conf
```

Your schroot config file in step 2 should look something like this (substituting your username on the host system, preferred chroot directory, etc.):

```
[ubuntu_i386]
description=Ubuntu Release 32-Bit
personality=linux32
directory=/srv/chroot/ubuntu_i386
root-users=your_usernamec
type=directory
users=your_username
```

Steps 3 - 5 continue on the command line:

```sh
$ sudo mkdir -p /srv/chroot/ubuntu_i386
$ sudo debootstrap --variant=buildd --arch=i386 oracular (or other release) /srv/chroot/ubuntu_i386 http://archive.ubuntu.com/ubuntu/
```

```sh
$ sudo cp /etc/apt/sources.list.d/ubuntu.sources /srv/chroot/ubuntu_i386/etc/apt/sources.list.d
$ schroot -c ubuntu_i386 -u root
```

```sh
$ apt-get update
$ apt-get install ubuntu-minimal
$ sudo apt-get install software-properties-common
```

After that, just like in a container, download the necessary libraries and tools, then follow the same instructions you would to build wine on the host system.

Although there's a bit of a learning curve, chroots are a powerful technique to learn (and not just for cross-compiling). They're also lighter than virtual machines or containers because only parts of the filesystem are isolated; the chroot session can share everything else, including the kernel instance, with the host session.

However, chroots do have a couple more disadvantages. In many cases, a significant system image needs to be loaded into the chroot directory so you'll have to acquire a distro image just like you would with a container. While it's not much of an issue for cross-compiling trusted code, chroots aren't nearly as secure as other methods of sandboxing either.

### Virtual Machines

As long as you have an image of your target platform, with all the build tools and libraries, you should be able to compile wine within your favorite virtual machine. You can control many virtual machines at a higher-level than containers or chroots, plus this route also leaves you with an instance of the target environment to test in, even if it's a totally different platform from your host system.

However, keep in mind that virtualization can be imperfect and introduce new bugs. If nothing interferes in the build process though, the primary downside to a virtual machine will be the performance penalty during compilation (and execution if you test wine within the virtual machine). You'll also have to account for the inconvenience of getting an image of the distro you want.

Even if you can build and run wine in a VM, please **don't** report bugs you find unless you also see them on a native platform. Without data from a native system, we just have to assume by default that the bug is introduced by the VM. Building and running wine can be a very effective way to debug the VM software itself though.

**Popular Platform Virtualization Software:**

- [KVM](https://www.linux-kvm.org/page/Main_Page)/[QEMU](https://wiki.qemu.org/Main_Page)
- [Xen](https://www.xenproject.org/)
- [VirtualBox](https://www.virtualbox.org/)
- [VMware](https://www.vmware.com/) (proprietary)

## Old WoW64 Build

When Windows began targeting 64-bit architectures, Microsoft decided to include a compatibility layer to support their massive universe of 32-bit applications. This kind of subcomponent, nicknamed [WoW64](https://en.wikipedia.org/wiki/WoW64) (for Windows on Windows 64-bit), is also implemented in Wine to solve the exact same problem.

**64-bit Wine built without 32-bit support will not be able to run ANY 32-bit applications, which most Windows binaries are. Even many 64-bit programs still include 32-bit components!**

The good news is that once you have the dependencies in place to compile both 32 and 64-bit Wine, you've already done the hard part. If you have all your dependencies through multi-lib or (on some happy day in the future) you've co-installed all the dependencies through multi-arch, you only need to follow two simple steps:

1. Compile the 64-bit version of Wine **first** with the `--enable-win64` configure flag, in a separate build directory of course ;)
2. When you build the 32-bit version next (again in a fresh build directory), point `configure` to the 64-bit build directory by using `--with-wine64=` and the relative path

On the command line:

```sh
$ cd ~/wine-dirs/wine64-build/
$ ../wine-source/configure --enable-win64
$ make
```

```sh
$ cd ~/wine-dirs/wine32-build/
$ PKG_CONFIG_PATH=/path/to/pkgconfig ../wine-source/configure --with-wine64=../wine64-build
$ make
```

PKG_CONFIG_PATH should point to the location of the 32 bit pkgconfig files, probably `/usr/lib` or `/usr/lib32` or `/usr/lib/i386-linux-gnu`. Without it, the configure script will pick up the 64 bit files and disable gstreamer support in the 32 bit build.

When you make the 32-bit version of Wine, the build process should inject whatever libraries the 64-bit version needs to handle 32-bit programs. After that, just run wine from the 64-bit build to have WoW64 features.

If you're using GCC, you need at least v4.4 to compile 64-bit wine because \_\__builtin_ms_va_list_ support was missing from earlier versions. For the same reason, you need at least v3.7.1 of Clang.

If you need to use a **container** or **chroot**, there are a couple of complications you have to watch out for. Ultimately, they should just require you to spend a little more time compiling. The main difference is that after you compile 64-bit wine, you'll need to compile the 32-bit version **twice**, each time with different configurations:

1. Enter your 32-bit chroot or container (see above about setting a [chroot](#chroot) or [container](#containers) up)
2. Do a completely normal 32-bit build of wine
3. Do a second 32-bit build, still in the chroot, with both your 64-bit build and the tools from your first 32-bit build

On the command line:

```sh
$ schroot -c chroot_i386 -u yourusername ... or
$ sudo lxc-start -n my32bitbox
```

```sh
$ cd ~/wine-dirs/wine32-tools
$ ../wine-source/configure
$ make
```

```sh
$ cd ~/wine-dirs/wine32-combo
$ ../wine-source/configure --with-wine64=../wine64-build --with-wine-tools=../wine32-tools
$ make
```

In theory, the `--with-wine64` option should work alone by telling `make` to use the pre-compiled tools from the 64-bit build. One of the necessary tools though is a script called `makedep`, which when built with 64-bit wine, needs to access the _amd64_ libraries on the system. But in order to have the 32-bit libraries in the chroot for an i386 build, these have to be **outside** the chroot. The first build of 32-bit wine lets the second build still refer to the 64-bit one, while overriding the (failed) use of the 64-bit tools.

Also, try to keep your 64-bit and 32-bit build directories close together, in a directory you can easily bind mount from your chroot. If you try to build the 32-bit version within a container or chroot that doesn't include the 64-bit build directory, then the `--with-wine64=` option won't be able to see the necessary files.

One last catch is that if you do choose to install your WoW64 build, you should run `make install` in the 32-bit build tree **first**, then in the 64-bit one.

If you run the 32-bit part of your tandem, WoW64 build (without installing), it should theoretically work just like stand-alone 32-bit wine.

## Installing from Source

After compiling Wine from source with one of the above methods, you can install it with:

```sh
# make install
```

This step is purely at your discretion; you can run wine entirely from within the build directory without installation. If you do install wine through make, just be sure that you don't have a version of wine already installed. Overlapping installations shouldn't break your system, but they might seriously tangle up your libraries and package management.

## Packaging Wine

**See **[**Packaging**](Packaging)** for details about assembling the package after building.**

If you're building Wine in order to package it and share in a repo, the build process should follow the same steps for the most part. Your main consideration should be ensuring your build environment has good library hygiene and a complete set of dependencies in order to not introduce new bugs for the end-user.

If you're interested in helping with packaging wine, the current packager for your distro probably has a lot of useful information beyond what you can find here upstream. Many of the major distros have also developed their own packaging tools to streamline the process and ensure code quality.

### Hard vs. Soft Dependencies

In addition to all the critical headers that Wine needs just to run, several optional subcomponents have soft dependencies. Since many end-users might want to install these features, you should have the appropriate libraries installed at compile-time, even if you don't normally use those features of Wine yourself.

To the furthest extent possible, your wine package should be configured to "recommend" (install by default but not require) these soft dependency packages on a user's system.

### 64-bit Packages

If you plan on packaging WoW64-capable wine for a 64-bit OS (a plain 64-bit build of wine is too limited for most users to justify packaging), the main consideration is that your 64-bit package will need to include some files from a 32-bit build.

The most direct method is to follow the instructions above for a [new WoW64 build](#new-wow64-build) or [old WoW64 build](#old-wow64-build); this should load the required 32-bit files into the 64-bit build. If for some reason you can't do the shared build, you should still be able to compile 32-bit and 64-bit wine separately, then copy the necessary files from the 32-bit build directory. See the [Packaging](Packaging) page for an exact list.

### Other Packages

While you're looking into packaging Wine itself, why not consider some of the other programs from the Wine project? They're not part of the main Windows API, but the features they provide are central to enough Windows programs that the project has made them an equal priority.

**Other Packages:**

- [wine-gecko](Gecko) ([WineHQ source tarballs here](https://dl.winehq.org/wine/wine-gecko/))
- [wine-mono](Wine-Mono) ([WineHQ source tarballs here](https://dl.winehq.org/wine/wine-mono/))
- vkd3d ([WineHQ source tarballs here](https://dl.winehq.org/vkd3d/source/))

## Developer Tools

Some developer tools may need to be folded into wine at build time to use them. Here are some basic points to keep in mind.

### Debuggers

Wine includes its own unique debugger ([winedbg](Commands/winedbg)) and debug symbols by default when built from source. If you would rather use a different debugger from wine's built-in one, you can also do that (the [Wine Developer's Guide](Wine-Developer's-Guide/Debugging-Wine#other-debuggers) has more info).

### Compiler Optimizations & Call-Stacks

To use more powerful tools, the main change to how you actually build wine is that you'll want to disable some compiler optimizations, mainly ones that eliminate operations from the call-stack. This does create a performance hit at run-time, but provides memory checkers with a fuller picture of what's actually happening.

If you're using GCC \>= v4.8 or Clang \>= v4.0, you can instruct the compiler to optimize debugging data, not speed or size, by just passing the `-Og` flag:

```sh
$ ../wine-source/configure CFLAGS="-Og" CROSSCFLAGS="-Og"
```

If you're using an older compiler, or you want to pick specific flags for whatever reason, these are the main ones you'll need to debug more effectively:

|  |  |
|--|--|
| `-g` | Emits debug symbols (default when building wine) |
| `-O1` | Enables only more conservative optimizations |
| `-fno-inline` | Disables inlining functions (preserves call-stack) |
| `-fno-omit-frame-pointer` | Function frame pointers are always retained |
| `-fno-optimize-sibling-calls` | Disables tail-recursion elimination |

### Memory & Address Checkers

Another class of tools that can work at build time are memory checkers for C/C++. Some of these (like [AddressSanitizer](https://code.google.com/p/address-sanitizer/)) are implemented as features of the compiler, while others (such as [Valgrind](https://www.valgrind.org/)) are separate suites. Most of these tools shouldn't require any configuration, only that they're installed on your system before compiling.

If Valgrind is installed on the system, the build process should automatically include Valgrind annotations in wine. If you want to double-check this, just grep for the Valgrind variables in _include/config.h_ after configuring your build directory:

`grep VALGRIND include/config.h`

That should return two lines switching on flags for Valgrind:

```
#define HAVE_VALGRIND_MEMCHECK_H 1
#define HAVE_VALGRIND_VALGRIND_H 1
```

If grep doesn't give you these lines, then the configure script failed to find Valgrind for some reason.

Valgrind can use those annotations to determine when Windows apps running on Wine try to access freed heap blocks. Even if wine didn't build with the Valgrind symbols though, you can still run Valgrind with wine to find other memory errors, such as accesses to uninitialized memory.

For more information about actually using Valgrind and helpful patches to the wine source, see [Wine and Valgrind](Wine-and-Valgrind).

Bernhard Übelacker maintains [a Wine branch](https://gitlab.winehq.org/bernhardu/wine/-/branches?state=all&sort=updated_desc&search=asan-pe) that is compatible with AddressSanitizer. There are lengthy instructions on how to compile and use it in the branch's README-ASan.md file.

## See Also

- [Developers](Developers)
- [Packaging](Packaging)
- [Building on macOS](Macos-Building)
- [Building Biarch Wine On Ubuntu](Building-Biarch-Wine-On-Ubuntu)
- [Building Wine Gecko](Gecko#building-wine-gecko)
- [Winelib](Winelib)
- [Compatibility](Compatibility)