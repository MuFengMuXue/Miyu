Wine implements its own version of Internet Explorer. The implementation
is based on a custom version of [Mozilla's Gecko Layout
Engine](https://en.wikipedia.org/wiki/Gecko_(layout_engine)).

### Installing

When your application tries to display a site, Wine loads and uses its
custom implementation of Gecko. Wine tries to find Gecko installation in
following order:

- If Wine Gecko is already installed in the prefix, that installation
  will be used.
- Wine 5.0-rc1 and newer will try to load Gecko from UNIX-style
  installation without installing it into the prefix. It will look for
  `wine-gecko-$(VERSION)-$(ARC)` subdirectory of standard local lookup
  (see below).
- Wine will try to find Wine Gecko MSI installer on local machine (see
  below). If it can find it, it will install it into the prefix and use
  it.
- If the file can't be found on your computer, Wine will download it for
  you. The downloaded .msi is saved to `~/.cache/wine`. If the download
  fails, you can download the appropriate version (see table below)
  yourself from <https://dl.winehq.org/wine/wine-gecko/>.

Whenever Wine tries to find local installation, it will look in
following directories:

- In most cases, the file(s) should be placed in `/usr/share/wine/gecko`.
- If you installed Wine in some \$prefix rather than /usr,
  `$prefix/share/wine/gecko/` before `/usr/share/wine/gecko`, followed by
  `/opt/wine/gecko`. (e.g. if you installed it from source, then place the
  files in `/usr/local/share/wine/gecko`).
- If you're running Wine from build tree, Wine will try to find files in
  `$build_dir/../gecko directory`.
- Local cache, usually `~/.cache/wine`.

For 64 bit (WoW64) Wine, both the x86 and x86_64 packages are required.

Wine will currently not be able to use such Gecko installation if it
can't map it to DOS drive (for example if z: drive is removed).

| Wine                      | Gecko (32 bit)                                                                                                                                                                                                     | Gecko (64 bit)                                                                                                                                                                                                                 |
|---------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| wine-0.9.47 - wine-1.1.11 | wine_gecko-0.1.0.cab                                                                                                                                                                                               |                                                                                                                                                                                                                                |
| wine-1.1.12 - wine-1.1.14 | wine_gecko-0.9.0.cab                                                                                                                                                                                               |                                                                                                                                                                                                                                |
| wine-1.1.15 - wine-1.1.26 | wine_gecko-0.9.1.cab                                                                                                                                                                                               |                                                                                                                                                                                                                                |
| wine-1.1.27 - wine-1.3.1  | wine_gecko-1.0.0-x86.cab                                                                                                                                                                                           |                                                                                                                                                                                                                                |
| wine-1.3.2 - wine-1.3.15  | wine_gecko-1.1.0-x86.cab                                                                                                                                                                                           | wine_gecko-1.1.0-x86_64.cab                                                                                                                                                                                                    |
| wine-1.3.16 - wine-1.3.26 | wine_gecko-1.2.0-x86.msi                                                                                                                                                                                           | wine_gecko-1.2.0-x86_64.msi                                                                                                                                                                                                    |
| wine-1.3.27 - wine-1.3.32 | wine_gecko-1.3-x86.msi                                                                                                                                                                                             | wine_gecko-1.3-x86_64.msi                                                                                                                                                                                                      |
| wine-1.3.33 - wine-1.4    | wine_gecko-1.4-x86.msi                                                                                                                                                                                             | wine_gecko-1.4-x86_64.msi                                                                                                                                                                                                      |
| wine-1.5.0 - wine-1.5.6   | wine_gecko-1.5-x86.msi                                                                                                                                                                                             | wine_gecko-1.5-x86_64.msi                                                                                                                                                                                                      |
| wine-1.5.7 - wine-1.5.9   | wine_gecko-1.6-x86.msi                                                                                                                                                                                             | wine_gecko-1.6-x86_64.msi                                                                                                                                                                                                      |
| wine-1.5.10 - wine-1.5.14 | wine_gecko-1.7-x86.msi                                                                                                                                                                                             | wine_gecko-1.7-x86_64.msi                                                                                                                                                                                                      |
| wine-1.5.15 - wine-1.5.21 | wine_gecko-1.8-x86.msi                                                                                                                                                                                             | wine_gecko-1.8-x86_64.msi                                                                                                                                                                                                      |
| wine-1.5.22 - wine-1.5.30 | wine_gecko-1.9-x86.msi                                                                                                                                                                                             | wine_gecko-1.9-x86_64.msi                                                                                                                                                                                                      |
| wine-1.5.31 - wine-1.7.2  | wine_gecko-2.21-x86.msi                                                                                                                                                                                            | wine_gecko-2.21-x86_64.msi                                                                                                                                                                                                     |
| wine-1.7.3 - wine-1.7.30  | wine_gecko-2.24-x86.msi                                                                                                                                                                                            | wine_gecko-2.24-x86_64.msi                                                                                                                                                                                                     |
| wine-1.7.31 - wine-1.7.37 | wine_gecko-2.34-x86.msi                                                                                                                                                                                            | wine_gecko-2.34-x86_64.msi                                                                                                                                                                                                     |
| wine-1.7.38 - wine-1.7.49 | wine_gecko-2.36-x86.msi                                                                                                                                                                                            | wine_gecko-2.36-x86_64.msi                                                                                                                                                                                                     |
| wine-1.7.50 - wine-1.9.2  | [wine_gecko-2.40-x86.msi](https://dl.winehq.org/wine/wine-gecko/2.40/wine_gecko-2.40-x86.msi)                                                                                                                      | [wine_gecko-2.40-x86_64.msi](https://dl.winehq.org/wine/wine-gecko/2.40/wine_gecko-2.40-x86_64.msi)                                                                                                                            |
| wine-1.9.3 - wine-1.9.12  | [wine_gecko-2.44-x86.msi](https://dl.winehq.org/wine/wine-gecko/2.44/wine_gecko-2.44-x86.msi)                                                                                                                      | [wine_gecko-2.44-x86_64.msi](https://dl.winehq.org/wine/wine-gecko/2.44/wine_gecko-2.44-x86_64.msi)                                                                                                                            |
| wine-1.9.13 - wine-3.21   | [wine_gecko-2.47-x86.msi](https://dl.winehq.org/wine/wine-gecko/2.47/wine_gecko-2.47-x86.msi)                                                                                                                      | [wine_gecko-2.47-x86_64.msi](https://dl.winehq.org/wine/wine-gecko/2.47/wine_gecko-2.47-x86_64.msi)                                                                                                                            |
| wine-5.0-rc1 - wine-5.22  | [wine-gecko-2.47.1-x86.msi](https://dl.winehq.org/wine/wine-gecko/2.47.1/wine-gecko-2.47.1-x86.msi)<br>[wine-gecko-2.47.1-x86.tar.bz2](https://dl.winehq.org/wine/wine-gecko/2.47.1/wine-gecko-2.47.1-x86.tar.bz2) | [wine-gecko-2.47.1-x86_64.msi](https://dl.winehq.org/wine/wine-gecko/2.47.1/wine-gecko-2.47.1-x86_64.msi)<br>[wine-gecko-2.47.1-x86_64.tar.bz2](https://dl.winehq.org/wine/wine-gecko/2.47.1/wine-gecko-2.47.1-x86_64.tar.bz2) |
| wine-6.0-rc1 - wine-7.12  | [wine-gecko-2.47.2-x86.msi](https://dl.winehq.org/wine/wine-gecko/2.47.2/wine-gecko-2.47.2-x86.msi)<br>[wine-gecko-2.47.2-x86.tar.xz](https://dl.winehq.org/wine/wine-gecko/2.47.2/wine-gecko-2.47.2-x86.tar.xz)   | [wine-gecko-2.47.2-x86_64.msi](https://dl.winehq.org/wine/wine-gecko/2.47.2/wine-gecko-2.47.2-x86_64.msi)<br>[wine-gecko-2.47.2-x86_64.tar.xz](https://dl.winehq.org/wine/wine-gecko/2.47.2/wine-gecko-2.47.2-x86_64.tar.xz)   |
| wine-7.13 - wine-8.5      | [wine-gecko-2.47.3-x86.msi](https://dl.winehq.org/wine/wine-gecko/2.47.3/wine-gecko-2.47.3-x86.msi)<br>[wine-gecko-2.47.3-x86.tar.xz](https://dl.winehq.org/wine/wine-gecko/2.47.3/wine-gecko-2.47.3-x86.tar.xz)   | [wine-gecko-2.47.3-x86_64.msi](https://dl.winehq.org/wine/wine-gecko/2.47.3/wine-gecko-2.47.3-x86_64.msi)<br>[wine-gecko-2.47.3-x86_64.tar.xz](https://dl.winehq.org/wine/wine-gecko/2.47.3/wine-gecko-2.47.3-x86_64.tar.xz)   |
| wine-8.6 - current        | [wine-gecko-2.47.4-x86.msi](https://dl.winehq.org/wine/wine-gecko/2.47.4/wine-gecko-2.47.4-x86.msi)<br>[wine-gecko-2.47.4-x86.tar.xz](https://dl.winehq.org/wine/wine-gecko/2.47.4/wine-gecko-2.47.4-x86.tar.xz)   | [wine-gecko-2.47.4-x86_64.msi](https://dl.winehq.org/wine/wine-gecko/2.47.4/wine-gecko-2.47.4-x86_64.msi)<br>[wine-gecko-2.47.4-x86_64.tar.xz](https://dl.winehq.org/wine/wine-gecko/2.47.4/wine-gecko-2.47.4-x86_64.tar.xz)   |

### Debug info

If Gecko is crashing on you, you can download a debug build from
<https://dl.winehq.org/wine/wine-gecko/> to get more verbose logs.
Download the -unstripped.tar.bz2 file for the version you are using (on
a 64 bit system, download both the x86 and x86_64 tarballs), unpack the
files, and replace the files in
`$WINEPREFIX/drive_c/windows/system32/gecko/version` and (on 64 bit)
`$WINEPREFIX/drive_c/windows/sysWoW64/gecko/version` with the
extracted files.

### Building Wine Gecko

The following describe how the Wine Gecko package is built.

NOTE: If you're unsure if you want to build it yourself, the answer is
no. There is no reason to build it yourself unless you're going to work
on Mozilla code. If you need Gecko to run an app in Wine, follow the
instructions above. Wine Gecko source is hosted in Git on
[GitLab](https://gitlab.winehq.org/wine/wine-gecko).

Wine Gecko is maintained by Jacek Caban. If you need help, feel free to
contact him.

#### Mingw-w64

It is
[encouraged](https://developer.mozilla.org/en-US/docs/Cross_Compile_Mozilla_for_Mingw32)
to use [mingw-w64](https://www.mingw-w64.org) for cross-compiling. A
fairly recent version of mingw-w64 should be enough.

##### Building

The exact instruction about building the package are hosted in
[wine/README](https://gitlab.winehq.org/wine/wine-gecko/-/blob/master/wine/README)
in Wine Gecko source directory.

##### Binary Packages

Some Distro are maintaining mingw-w64 in their repo, like
[Fedora](https://apps.fedoraproject.org/packages/mingw-headers). You can
install the dependencies with commands like

```
# yum-builddep mingw32-wine-gecko
```

#### Troubleshooting

##### 'pthread_t' does not name a type

Try to remove media/libstagefright/ports/win32/include/pthread.h. This
should be fixed in version 2.47.1.

##### mingw-w64 too old

For example:

- ['ILocation' was not
  declared](https://sourceforge.net/p/mingw-w64/mingw-w64/ci/7268caece9b4cb33ff698306e51140b11d7656b0/#diff-3).
- ['EXTERN_C' does not name a
  type](https://sourceforge.net/p/mingw-w64/mingw-w64/ci/6c56d0b0eb5be9fbeb552ba070a2304b842a5102/)

The mingw-w64 package on your distro may be too old to include this
patch [(for example, it will take some time to backport these patch to
stable branches like
v4.x)](https://lists.fedoraproject.org/pipermail/mingw/2015-April/009047.html).
If you faced this trouble, please consider compile mingw-w64 by
yourself (as
[README](https://gitlab.winehq.org/wine/wine-gecko/-/blob/master/wine/README)
said)

### See also

- [Gecko version needed by current Wine
  git](https://gitlab.winehq.org/wine/wine/-/blob/master/dlls/appwiz.cpl/addons.c#L48)
