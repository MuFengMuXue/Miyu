<small>
&nbsp;[:flag_cn: 简体中文](zh_CN/Fedora)
</small>

-----

**Note:** the Fedora 40 and later packages are built with "new WoW64"
architecture. Unlike the "old WoW64," these packages do not require a
separate install of the 32-bit wine-common package or any 32 bit
dependencies. These packages can run 32 bit programs from a 64 bit wineprefix, but cannot create or use a 32 bit wineprefix. 

## Installing WineHQ packages

Add the repository:

*Fedora 44:*

```
sudo dnf config-manager addrepo --from-repofile=https://dl.winehq.org/wine-builds/fedora/44/winehq.repo
```

*Fedora 43:*

```
sudo dnf config-manager addrepo --from-repofile=https://dl.winehq.org/wine-builds/fedora/43/winehq.repo
```

*Fedora 42:*

```
sudo dnf config-manager addrepo --from-repofile=https://dl.winehq.org/wine-builds/fedora/42/winehq.repo
```

Install **one of the following packages**:

|                    |                              |
|--------------------|------------------------------|
| Stable branch      | `sudo dnf install winehq-stable`  |
| Development branch | `sudo dnf install winehq-devel`   |
| Staging branch     | `sudo dnf install winehq-staging` |

## Build Dependencies

See [Building Wine](Building-Wine#satisfying-build-dependencies)
and srpm files at ```dl.winehq.org/wine-builds/fedora/<Fedora Ver>/src/wine-<devel|stable|staging>-<Wine Ver>.1.src.rpm```

You'll need to install the GNU make toolchain

```sh
$ sudo dnf groupinstall "C Development Tools and Libraries"
$ sudo dnf groupinstall "Development Tools"
```

Also, you may need some packages from
[rpmfusion](https://www.rpmfusion.org)

## Compiling

Thanks to Fedora's multilib arrangement, once you have the dependencies,
building either a plain 32-bit or WoW64 version of Wine should be
straight-forward. The appropriate sections on [Building
Wine](Building-Wine) should list all the steps.

### Plain 32-bit wine on 64 bit system

```sh
$ PKG_CONFIG_PATH=/usr/lib/pkgconfig CC="ccache gcc -m32" ./configure
$ make
```

## A Bit of History

Fedora has a unique history among GNU/Linux distributions that partly
explains its goals and relationship to other distros. It initially began
as a minor distro, Fedora Linux, that would test and package extra
software on top of the venerable RedHat distro (now technically Red Hat
Enterprise Linux). Around the same time though, Red Hat Inc. decided to
focus on very stable releases with long-term support for enterprises.

At first, the company tried directly managing a more fluid branch geared
towards desktops, but many non-subscribing PC users began switching to
Fedora Linux. At that point, Red Hat made the farsighted decision to
cooperate with the Fedora Linux community on experimental work, and the
Fedora project was born. The resulting distribution was originally
called "Fedora Core" before being renamed simply "Fedora" after a few
years.

Today, Fedora is the work of a worldwide community of volunteers, but
Red Hat Inc. still contributes a great deal to the project through both
collaboration and financial support. In a bit of a role-reversal, Fedora
is also now effectively upstream of its parent distro; RedHat (and its
child distros) will periodically branch off a new Fedora release, then
after much more testing and bug-fixing, provide a new release to their
more stability-minded users.

## See Also

- [WineHQ Fedora package build scripts and
  logs](https://build.opensuse.org/project/show/Emulators:Wine:Fedora)
- The [Fedora Wiki's page for Wine](https://fedoraproject.org/wiki/Wine)
- [Building Wine](Building-Wine)
- [Packaging](Packaging)
