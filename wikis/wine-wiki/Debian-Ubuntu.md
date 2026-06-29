---
title: Debian/Ubuntu
---
<small> </small>[<small>:flag_nl: Nederlands</small>](nl/Debian-Ubuntu)<small>  </small>[<small>:flag_cn: 简体中文</small>](zh_CN/Debian-Ubuntu)

---

Although Debian and Ubuntu offer their own Wine packages, they are often several versions behind. To make installing the latest version of Wine as easy as possible, WineHQ has its own Debian/Ubuntu repository. Should a newer version of Wine cause problems, it is also possible to install an older version of your choice.

The WineHQ repository only offers packages for AMD64 and i386. If you need the ARM version, you can use the Debian/Ubuntu packages.

## Preparation

WineHQ uses the distribution name to add the repository. If you don't know the name or are using a distribution derived from Debian or Ubuntu, it can be found using:

```sh
cat /etc/os-release
```

Look for the line with either `UBUNTU_CODENAME` or `VERSION_CODENAME`. If both are present, use the name after `UBUNTU_CODENAME`.

## WineHQ repository

**Download and add the repository key:**

```sh
sudo mkdir -pm755 /etc/apt/keyrings
wget -O - https://dl.winehq.org/wine-builds/winehq.key | sudo gpg --dearmor -o /etc/apt/keyrings/winehq-archive.key -
```

**Add the repository:**

The WineHQ packages for **Ubuntu 25.10** and later and **Debian Testing** (wine versions 10.18 and up) are WoW64. Therefore, the 32-bit packages are no longer necessary. The new WoW64 can run 32-bit programs from a 64-bit [wineprefix](https://gitlab.winehq.org/wine/wine/-/wikis/FAQ#wineprefixes), but it cannot use 32-bit wineprefixes. If you have any 32-bit wineprefixes from a previous installation, you will need to _reinstall_ your 32-bit applications to a 64-bit wineprefix. Older versions of Ubuntu and Debian require the 32-bit architecture to be enabled.

If your distribution name is not on the list, older [packages may be available](#my-debianubuntu-version-is-not-listed) on the download server.

Only add the repository that corresponds to your distribution.

---

### Resolute

**Ubuntu 26.04**

_Add the sources file:_

```sh
sudo wget -NP /etc/apt/sources.list.d/ https://dl.winehq.org/wine-builds/ubuntu/dists/resolute/winehq-resolute.sources
```

---

### Questing

**Ubuntu 25.10**

_Add the sources file:_

```sh
sudo wget -NP /etc/apt/sources.list.d/ https://dl.winehq.org/wine-builds/ubuntu/dists/questing/winehq-questing.sources
```

---

### Plucky

**Ubuntu 25.04**

_Enable the 32-bit repository:_

```sh
sudo dpkg --add-architecture i386
```

_Add the sources file:_

```sh
sudo wget -NP /etc/apt/sources.list.d/ https://dl.winehq.org/wine-builds/ubuntu/dists/plucky/winehq-plucky.sources
```

---

### Noble

**Ubuntu 24.04 & Linux Mint 22**

_Enable the 32-bit repository:_

```sh
sudo dpkg --add-architecture i386
```

_Add the sources file:_

```sh
sudo wget -NP /etc/apt/sources.list.d/ https://dl.winehq.org/wine-builds/ubuntu/dists/noble/winehq-noble.sources
```

---

### Jammy

**Ubuntu 22.04 & Linux Mint 21.x**

_Enable the 32-bit repository:_

```sh
sudo dpkg --add-architecture i386
```

_Add the sources file:_

```sh
sudo wget -NP /etc/apt/sources.list.d/ https://dl.winehq.org/wine-builds/ubuntu/dists/jammy/winehq-jammy.sources
```

---

### Forky

**Debian Testing**

_Add the sources file:_

```sh
sudo wget -NP /etc/apt/sources.list.d/ https://dl.winehq.org/wine-builds/debian/dists/forky/winehq-forky.sources
```

---

### Trixie

**Debian 13**

_Enable the 32-bit repository:_

```sh
sudo dpkg --add-architecture i386
```

_Add the sources file:_

```sh
sudo wget -NP /etc/apt/sources.list.d/ https://dl.winehq.org/wine-builds/debian/dists/trixie/winehq-trixie.sources
```

---

### Bookworm

**Debian 12**

_Enable the 32-bit repository:_

```sh
sudo dpkg --add-architecture i386
```

_Add the sources file:_

```sh
sudo wget -NP /etc/apt/sources.list.d/ https://dl.winehq.org/wine-builds/debian/dists/bookworm/winehq-bookworm.sources
```

---

---

## Update

Update the package information:

```sh
sudo apt update
```

## Install Wine

Install **one** of the following packages:

<table>
<tr>
<th>Wine branch</th>
<th>Command</th>
</tr>
<tr>
<td>Stable branch</td>
<td>

<pre>sudo apt install --install-recommends winehq-stable</pre></td>
</tr>
<tr>
<td>Development branch</td>
<td>

<pre>sudo apt install --install-recommends winehq-devel</pre></td>
</tr>
<tr>
<td>Staging branch</td>
<td>

<pre>sudo apt install --install-recommends winehq-staging</pre></td>
</tr>
</table>

The [User's Guide](Wine-User%27s-Guide#wine-from-winehq) explains the differences between the branches.

---

## Help

Sometimes there are problems installing Wine. If your problem is not listed, search the [forum](https://forums.winehq.org/WineHQ) or if you can't find an answer ask your question.

### Ubuntu 25.10 and later/ Debian Testing

The WineHQ packages are WoW64. This means that the 32-bit packages are unnecessary. The new WoW64 wine-devel package is set to conflict with and replace wine-devel-i386 and wine-devel-amd64, which are no longer separate packages. Upgrading users should get a message about the replacement and asked if they want to continue. If updating an older Wine version does not work, uninstall the old packages first.

```sh
sudo apt remove winehq-devel wine-devel wine-devel-amd64 wine-devel-i386:i386
```

### Missing dependencies

Read the [FAQ](FAQ#How_do_I_solve_dependency_errors_when_trying_to_install_Wine.3F) about dependency errors and tips for troubleshooting dependency issues. The most common issues are:

#### Third-party repositories

WineHQ packages are created and tested on a clean installation. Using PPAs or third-party repositories may prevent the installation of Wine. Often the problem is that these repositories are not multiarch. The required 32 and 64-bit packages are missing or cannot be installed side by side. The _deb.sury.org_ repository is known for causing problems.

Downgrade the problematic dependency packages to the official version.

#### KDE Neon

Ubuntu 22.04 KDE Neon users report problems with the _libpoppler-glib8_ dependency. The solution is to downgrade this package to the official Ubuntu version. `sudo apt install libpoppler-glib8:{i386,amd64}=22.02.0-2ubuntu0.3`

#### Backports

Another cause may be the use of backports. A newer 64-bit version of a library is already installed, but the 32-bit version isn't. These packages are given a lower priority so they will not be installed automatically. The solution is to manually install the missing 32-bit package from backports.

#### FAudio

Older versions of Wine (prior to version 6.21) have FAudio as a dependency. These packages are missing on Ubuntu 18.04. These can be downloaded from the [Open Build Service](https://download.opensuse.org/repositories/Emulators:/Wine:/Debian/xUbuntu_18.04/). For Debian 10, these packages are available in backports.

### Winehq key problems

- **The WineHQ repository key was changed on 2018-12-19**

  If you downloaded and added the key before that time, you will need to download and add the new key and run `sudo apt update` to accept the repository changes.
- **Apt-key is now deprecated**

  Previously, _apt-key_ was used to add the Wine key. If you get this warning, remove the Wine key with:

  ```sh
  sudo apt-key del "D43F 6401 4536 9C51 D786 DDEA 76F1 A20F F987 672F"
  ```

  And remove the the line about the WineHQ repository from _/etc/apt/sources.list(.d/\*)_.

### Mirror sync in progress?

If you get an error message when trying to install a package from WineHQ that includes the line `Mirror sync in progress?` that is most likely the problem. There are many packages to sync, and it can take a long time to complete.

Wait a few hours, and try again. If the problem persists for more than a day, file a bug.

### My Debian/Ubuntu version is not listed

When a Debian/Ubuntu version is no longer supported, no new Wine packages are built. And the repository will no longer appear in the list above. Since no new versions are built, it is not necessary to add the WineHQ repository. Just download and install [the four WineHQ deb packages](#notes).

Please note that these packages are no longer maintained and are no longer supported.

## Notes

- Menu items are not created for Wine's builtin programs (winecfg, etc.). If you upgrade the Wine distro packages that had added them, they will be removed. You can recreate them yourself using your menu editor.
- The Wine files are installed in `/opt/wine-<branch>/`
- WineHQ does not offer _wine-gecko_ or _wine-mono_ packages. When creating a new [wineprefix](FAQ#Wineprefixes), you will be asked if you want to download those components. For best compatibility, it is recommended to click _Yes_ here. If the download doesn't work for you, please follow the instructions on the [Gecko](Gecko) and [Mono](Wine-Mono) wiki pages to install them manually.
- Beginning with Wine 5.7, the WineHQ packages have an optional debconf setting to enable CAP_NET_RAW to allow applications that need to send and receive raw IP packets to do so. This is disabled by default because it carries a potential security risk, and the vast majority of applications do not need that capability. Users of applications that do need it can enable CAP_NET_RAW after installing Wine by running `dpkg-reconfigure wine-<branch>-amd64 wine-<branch> wine-<branch>-i386` and answering _yes_ to the three questions.
- Binfmt_misc registration is not added. Consult your distro's documentation for update-binfmts (`man update-binfmts`) if you wish to do this manually.
- A complete Wine installation on a 64-bit system consists of four packages. The Debian Testing / Ubuntu 25.10 packages are WoW64. These distributions only have the `winehq-<branch>` and `wine-<branch>` packages.
  - `winehq-<branch>` This package ensures that the _wine_ command is available system-wide.
  - `wine-<branch>` This package has the following two packages as dependencies and provides a working Wine installation.
  - `wine-<branch>-amd64` The 64-bit part of Wine.
  - `wine-<branch>-i386` The 32-bit part of Wine.

  By splitting a Wine over different packages, it is possible to install different branches side by side.

  For example: Use Wine _stable_ as the default Wine version and install Wine _staging_ to test other programs.

  Install Wine stable:

  `sudo apt install --install-recommends winehq-stable`

  Install Wine staging:

  `sudo apt install --install-recommends wine-staging` (Note the missing _hq_ after _wine_)

  Run a program with Wine _stable_:

  `wine program.exe`

  Run a program with Wine _staging_:

  `WINEPREFIX=~/wine-staging /opt/wine-staging/bin/wine program.exe`

  (It is recommended to give each Wine branch its own wineprefix.)
- There are several versions of Wine on the repository. The latest version is installed by default. Usually, the latest version is recommended. However, it may happen that an older version is desired. Use `apt policy winehq-<branch>` to list the different available versions.

  Install an older version of your choice with

  ```sh
  sudo apt install winehq-<branch>=<version>
  ```

  For example:

  ```sh
  sudo apt install winehq-staging=7.12~bookworm-1
  ```

  When the Wine packages are downgraded, all four Wine packages must be downgraded.

  ```sh
  sudo apt install winehq-staging=7.12~bookworm-1 wine-staging=7.12~bookworm-1 wine-staging-amd64=7.12~bookworm-1 wine-staging-i386=7.12~bookworm-1
  ```

## Installing without Internet

To install Wine on a machine without internet access, you must have access to a second machine (or VM) with an internet connection to download the WineHQ .deb package and its dependencies.

On the machine with internet, add the WineHQ repository and run apt update as described above.

Next, cache just the packages necessary for installing Wine, without extracting them:

```sh
sudo apt-get clean
sudo apt-get --download-only install winehq-<branch>
sudo apt-get --download-only dist-upgrade
```

Copy all of the .deb files in /var/cache/apt/archives to a USB stick:

```sh
cp -R /var/cache/apt/archives/ /media/usb-drive/deb-pkgs/
```

Finally, on the machine without internet, install all of the packages from the flash drive:

```sh
cd /media/usb-drive/deb-pkgs sudo dpkg -i *.deb
```

## Building from Source

- Beginning with 4.0-rc2, the WineHQ repository includes the .dsc, .diff.gz, and .orig.tar.gz files generated by the Open Build Service(OBS). These source packages can be found on `https://dl.winehq.org/wine-builds/<debian|ubuntu>/dists/<version>/main/source/<matching filename>`
- The latest version of Debian and Ubuntu are multiarch. It is possible to install all 64 and 32 bit dependencies side by side. This allows Wine to be built using the steps listed under [Shared WoW64](Building-Wine#shared-wow64).
- On older versions of Debian/Ubuntu the multiarch implementation could be incomplete. You can't simply install 32-bit and 64-bit libraries alongside each other. If you're on a 64-bit system, you'll have to create an isolated environment for installing and building with 32-bit dependencies. See [Building Wine](Building-Wine) for instructions on how to build in a chroot or container.

## See Also

- [WineHQ Debian/Ubuntu package build scripts and logs](https://build.opensuse.org/project/show/Emulators:Wine:Debian)
- The [Debian Wiki's page for Wine.](https://wiki.debian.org/Wine)
- [Packaging](Packaging)