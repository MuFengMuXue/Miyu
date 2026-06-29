NOTICE: This guide is a little outdated. As of the time of this
writing (2019) most of Wine's dependencies are multiarch-compatible on
Ubuntu, with a few notable exceptions (libgstreamer, mostly). Unless
you really need both versions of one or more multiarch-incompatible
libraries, you can probably just skip all the nonsense with containers
and follow the instructions at [Building
Wine](Building-Wine#shared-wow64).

## Overview

Ubuntu makes building 32-bit Wine hard because the 64-bit system doesn't
come with a full set of 32-bit development libraries. The easiest
workaround is to build 32-bit Wine inside a 32-bit container, but that
breaks --with-wine64, which expects to be able to run 64-bit tools
inside the 32-bit build. The easiest workaround there is to use
--with-wine-tools to point to a plain old 32-bit build of wine. This
guide uses [LXC](https://en.wikipedia.org/wiki/LXC) (chroot is another
option) and should work with any Ubuntu derivative distro, compatible
with 12.04 or later, that supports LXC. The source code and full build
will require about 3.5GiB of storage space. The LXC container will
require about 1.6GiB.

The basic approach is:

- Build 64-bit wine
- Build 32-bit tools in lxc
- Build 32-bit wine in lxc, referring to the 64-bit Wine and 32-bit
  tools built in the previous steps
- Install 32-bit wine
- Install 64-bit wine

Many of the commands require root privileges. Your user account needs to
have access to root via sudo or you need to switch to a user account
that does with:

```sh
$ su -l <username>
```

## Preparation

Ubuntu and derivatives use apt-get for software management. To build
(compile) Wine from source code the build tools and the headers all if
its dependencies need to be installed. The headers are the "\*-dev"
packages which are located in the *source repositories*. The repository
configurations are located in /etc/apt in the sources.list file and as
separate files in the sources.list.d directory. These are text files and
can be viewed with any text editor. A normal repository entry begins
with "deb" while a source repository begins with "deb-src". Normally the
source repositories are not configured by default and have to be added.
This can be performed via the command line and with graphical tools
including software-properties-gtk (a.k.a. "Settings & Updates" or
"Software Sources" in the desktop menu, "Settings \> Repositories" in
Synaptic, "Edit \> Software Sources" in Ubuntu Software Center), Muon,
or Adept. They can also be added via the command line with
add-apt-repository using the "-s" option. After adding the source
repositories, update the package lists using either a graphical package
manager or apt-get in a terminal:

`sudo apt-get update`

Packages can be installed or removed using apt-get, aptitude, or a
graphical package manager. The examples use apt-get since it is
universally available and a terminal is needed for most of the other
commands.

Next you need to remove all existing Wine packages. You will need
wine-mono, wine-gecko, and optionally winetricks for your compiled
version of wine but they may depend on the existing Wine installation
which may force you to remove them. Don't fight it - they can be
installed manually later.

Search for installed Wine packages using the search or filter functions
of your graphical package manager tool. If you are using a terminal then
use *apt-cache* to search by name then use apt-get to remove them:

```
apt-cache madison wine
     wine | 1:1.7.55-0ubuntu1 | `[`https://ppa.launchpad.net/ubuntu-wine/ppa/ubuntu/`](https://ppa.launchpad.net/ubuntu-wine/ppa/ubuntu/)` trusty/main amd64 Packages
     wine | 1:1.6.2-0ubuntu4 | `[`https://mirrors.xmission.com/ubuntu/`](https://mirrors.xmission.com/ubuntu/)` trusty/universe amd64 Packages
  wine1.6 | 1:1.6.2-0ubuntu4 | `[`https://mirrors.xmission.com/ubuntu/`](https://mirrors.xmission.com/ubuntu/)` trusty/universe Sources
  wine1.7 | 1:1.7.55-0ubuntu1 | `[`https://ppa.launchpad.net/ubuntu-wine/ppa/ubuntu/`](https://ppa.launchpad.net/ubuntu-wine/ppa/ubuntu/)` trusty/main Sources
```

```
apt-get remove wine wine1.6 wine1.7
```

You can also use *dpkg-query* to list packages with "wine" in their
names:

```
dpkg-query -l '*wine*'
```

After removing the conflicting packages, install git and the Wine build
dependencies:

```sh
$ sudo apt-get install git
$ sudo apt-get build-dep wine
```

## Obtain Wine Source Code

Create a local git repository of the Wine source code. This can be over
300MiB so it may take a while depending on your Internet connection
speed.

```sh
$ cd $HOME
$ git clone https://gitlab.winehq.org/wine/wine.git
```

## Patching

Patches need to be applied before compiling. For example, if a developer
provided you a patch to test as part of resolving a bug then it needs to
be applied against the source code in ~/wine-git. Typically a patch is
made using the *diff* tool and applied with the *patch* command. A patch
can affect many files. To apply a patch against your local git
repository:

```
$ cd $HOME/wine-git
$ patch -p1 <../fix.patch
```

The *patch* command may respond with a warning:

`Reversed (or previously applied) patch detected!  Assume -R?`

This means the changes from the patch already exists in the source code,
either from being applied previously or the result of the changes being
accepted into the main source tree by the maintainers. Press Enter to
skip applying it again.

## Build 64-bit Wine

The general process for compiling anything is to execute a configuration
script (checks for dependencies and compiler quirks then creates "make"
files), execute *make* to compile the source code, then install the
binaries that the compiler (gcc) created. Compiling can be faster with a
multi-core system by starting several compiler "jobs" simultaneously.
This is controlled by the "-j#" parameter supplied to *make*. The
examples assume four simultaneous jobs (-j4). The *make clean* removes
existing binaries that were from a previous build.

```sh
$ mkdir $HOME/wine64
$ cd $HOME/wine64
$ make clean
$ ../wine-git/configure --enable-win64
$ make -j4
```

If the configure or make steps fail then check the config.log file to
make sure there aren't any missing build dependencies. If you can't
figure it out then ask on the forum or IRC.

## Install LXC

Install LXC:

```sh
$ sudo apt-get install lxc lxctl lxc-templates
```

Next create a 32-bit container named "my32bitbox" using the Ubuntu
template and bind your home directory to the /home directory in the
container.

Since sudo will result in $HOME pointing to /root, $LOGNAME is used to
supply the home directory name. This assumes your home directory name is
the same as your login name. If it is not then just type it manually.

```sh
$ sudo lxc-create -t ubuntu -n my32bitbox -- --bindhome $LOGNAME -a i386
```

Copy the apt configuration from the host to the LXC container to save
time:

```sh
$ sudo cp -R /etc/apt /var/lib/lxc/my32bitbox/rootfs/etc
```

Start the container and log in with your username and password.

```sh
$ sudo lxc-start -n my32bitbox
```

Now you should be inside the container but in your real home directory.
If you are not in the container (the prompt is not
<your username>@my32bitbox), then open a new terminal and attach to it.
Then try to login again.

```sh
$ sudo lxc-attach -n my32bitbox
```

Install the 32-bit dependencies:

```sh
$ sudo apt-get update
$ sudo apt-get install python-software-properties git-core
$ sudo apt-get build-dep wine
```

## Build 32-bit Wine

Build the 32-bit version of the Wine developer tools from within the
LXC. The *make clean* removes existing binaries that were from a
previous build.

```sh
$ mkdir $HOME/wine32-tools
$ cd $HOME/wine32-tools
$ make clean
$ ~/wine-git/configure
$ make -j4
```

Next build the 32-bit version of Wine, pointing to the 64-bit build for
data, and the 32-bit tools build:

```sh
$ mkdir $HOME/wine32
$ cd $HOME/wine32
$ make clean
$ ~/wine-git/configure --with-wine64=$HOME/wine64 --with-wine-tools=$HOME/wine32-tools
$ make -j4
```

Install the 32-bit Wine *in the LXC itself* to force the last little bit
of building:

```sh
$ cd $HOME/wine32
$ sudo make install
```

If successful then shut down the container. Make sure you see the
`<your username>@my32bitbox` prompt then:

```sh
$ sudo shutdown -h now
```

This drops you back out into your real machine.

## Install Wine

Install the newly built Wine into your real machine:

```sh
$ cd $HOME/wine32
$ sudo make install
$ cd $HOME/wine64
$ sudo make install
```

Warning: When you install a locally built version of Wine, the package
management system will not know it exists since it did not come from a
package. Thus it is possible to later break its dependencies or install
a conflicting version of Wine without a warning from the package
management tools. You can prevent this by creating a package or by
blocking conflicting packages with apt-pinning by setting "Pin-Priority:
-1" for the packages.

Next, install [Mono](Wine-Mono), [Gecko](Gecko), and
optionally [winetricks](Winetricks) if you had to remove
their packages because of a dependency on a conflicting Wine package.

And you're done! Use `wine --version` to check the version installed.

## Uninstallation

The uninstall process is similar to the install process:

```sh
$ cd $HOME/wine32
$ sudo make uninstall
$ cd $HOME/wine64
$ sudo make uninstall
```

Then remove any manually installed Mono, Gecko, and winetricks.

## Updating

If you want to update your Wine installation then start by uninstalling
the old binaries. Then remove the old binaries from the build
directories:

```sh
$ cd $HOME/wine32
$ make clean
$ cd $HOME/wine64
$ make clean
```

If your system libraries are later updated, as part of normal
maintenance, be sure to update the 32-bit system in the LXC also.

## Reverting Patches

If you need to remove all changes to your local git repository from
patches you applied:

```sh
$ cd $HOME/wine-git
$ git fetch --all
$ git reset --hard origin/master
```

## See Also

- [Debian/Ubuntu](Debian-Ubuntu)
- [Building Wine](Building-Wine)
- [Mono](Wine-Mono)
- [Gecko](Gecko)
- [Winetricks](Winetricks)
