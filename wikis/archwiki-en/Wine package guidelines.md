# Wine package guidelines

Many Windows programs may still be useful in Linux and so we may want to have a package for them. The differences between the two operating systems make this task a little complex. In this guideline we will talk about Win32 binaries, since projects where source is available usually are ported to Linux.

## Things to check outright
* License: does the license allow the program to be repackaged?
* Installer: is it possible to install the program silently? Even better, does an installer-less version exist?
* Portability and cleanness: is the program portable? It is clean?

Here we mean a program is portable if it never writes in the registry or outside its directory; we mean a program is clean if it never writes in its directory, but it may write its settings in the user folder. A program can be also both (e.g., it never writes settings) or neither (e.g., it writes in its directory, it writes around, it writes in the registry...)

## License
Usually licenses are in a text file in the install directory. If you cannot find it, try following the screens during installation. If nothing is said about repackaging, go on. The author does not care. Otherwise the license usually does not allow removing files or does not allow repackaging at all. In the former case just be careful that the makepkg process does not lose any file, you may delete unneeded files (e.g., uninstallers) in the  phase; in the latter case all the installing process must be done in the  phase. The  phase will only be for copying the install files.

## Installer
It is much easier to work with compressed files like  than with Windows installers. If you have no choice, since the author insists on distributing its program with an installer, search the Internet for if it is possible to silently install the software. MSFN is usually a good place to search. If you cannot find a way, try to open the installer with different unpacking utilities; it may work.

## Portability and cleanness
A portable program does not need its own Wine emulated file system, so check in Portable Freeware if the program you are packaging is portable.

## The guideline in short
The idea behind packaging a Windows program is to use the program's files as mere data that Wine will interpret, just like JVM and Java bytecode.

So we will install the program in  and the program will write all what it needs  in .  Everything will be prepared by a small script saved in  that will create the folder, prepare it if needed, and finally start the program.

In the next sections we will talk about every step.

This way every user will have their own settings and their decisions will not bother other users.

## Installing
If the program has no installer, the installation is a mere decompression of a file; unpack it to , making sure that the permissions are correct. These commands will do:

 $ find "$pkgdir"/usr/share -type f -exec chmod 644 "{}" \;
 $ find "$pkgdir"/usr/share -type d -exec chmod 755 "{}" \;

If the program cannot be installed the easy way, you need to create a Wine environment:

 $ install -m755 -d "$srcdir"/tmp "$srcdir"/tmp/env "$srcdir"/tmp/local
 $ export WINEPREFIX="$srcdir"/tmp/env
 $ export XDG_DATA_HOME="$srcdir"/tmp/local
 $ wine "$srcdir"/installer.exe /silentoptions

We have not discussed portability yet, but if your program does not need the registry keys it modified, you can just copy the directory from the:

 "$srcdir"/tmp/env/drive_c/Program\ Files/programname

Otherwise you need to copy all the registry files too and eventually the files the program installed around. The  will contains menu icons and desktop files, you may want to copy them in the package. If there does not exist a way to install the program silently... Maybe you can make a  file and upload it somewhere? If nothing automated is possible, force the user to follow the installer and hope they do not mess up the installation, write some checks before blindly copying a folder that may not exist (e.g. the user pressed 'Cancel').

## The /usr/bin script
This script prepares the settings folder and starts the program. If your program is portable, it will look like this:

 #!/bin/bash
 unset WINEPREFIX
 if [ ! -d "$HOME"/.programname ] ; then
    mkdir -p "$HOME"/.programname
    #prepare the environment here
 fi
 WINEDEBUG=-all wine "$HOME"/.programname/programname "$@"

If it is clean, it will look like this:

 #!/bin/bash
 export WINEPREFIX="$HOME"/.programname/wine
 if [ ! -d "$HOME"/.programname ] ; then
    mkdir -p "$HOME"/.programname/wine
    wineboot -u
    #copy the registry file if needed
 fi
 WINEDEBUG=-all wine /usr/share/programname "$@"

As you can see, in the second case there is no environment preparation. In fact a clean application will be started directly from  since it will not need to write in its folder, so its settings will be written somewhere in the emulated file system.

If the application is neither clean neither portable the two ideas must be combined.

If the application does not write settings at all, skip the  and start it from .

The task of preparing the environment may differ greatly between applications, but follow these rules of thumb:
If the program:

* just needs to read a file, symlink it.
* needs to write in a file, copy it.
* does not use a file, ignore it.

Of course the minimum is just starting .

Usually the environment will be made by symlinking between the  directory and the  files. But since some Windows programs are very fickle about their paths, you may need to symlink directly in the  directory.

Of course those are just ideas to integrate Win32 applications in the Linux environment, do not forget your intelligence and gumption.

As example, μTorrent is by default a clean application, but with a easy step can be used as a portable one. Since it is a single file and it is pretty small creating its wine environment (about 5MB) it is probably an overkill. It is better to symlink the executable, create the empty settings.dat in order to use it portable in the  directory. With the added advantage that just visiting the  directory, a user can see a copy of the  files they downloaded.

## UnionFsFuse
You can consider using the UnionFsFuse program available as . UnionFsFuse allows to keep the base directory in  and put a copy of the files the application needed to write inside
almost automatically.

Using UnionFsFuse means an additional dependency and it requires the fuse module that not all users might load. Yet, it might be worthwhile if the application would need lots of symlinking or if it is unclear exactly what it needs to be written. Just ensure to mount and unmount the UnionFs correctly.

## One example
To see examples of AUR packages that depends on wine, see https://aur.archlinux.org/rpc/v5/search/wine?by=depends

We will make a package for eMule. According to Portable Freeware, eMule is not completely portable since it writes some (useless) keys in the registry.

On the other hand, it is not clean either since it writes its configuration files and puts its downloads in its installation folder.

Luckily there is an installer-less version available.

So we make our PKGBUILD; the only dependency is . The  should be added.

{{bc|
# Maintainer: You
pkgname=emule
pkgver=0.49b
pkgrel=1
pkgdesc="One of the biggest and most reliable peer-to-peer file sharing
clients around the world."
arch=('x86_64')
url="https://www.emule-project.net"
license=('GPL')
depends=()
depends=(wine)
makedepends=(unzip)
source=(emule https://sourceforge.net/projects/emule/files/eMule/$pkgver/eMule$pkgver.zip)
noextract=()
options=(!strip)

build() {
  rm -f src/eMule"$pkgver"/license* #It is GPL

  install -d -m755 pkg/usr/share/emule
  cp -ra src/eMule"$pkgver"/* pkg/usr/share/emule
  find pkg/usr/share/emule -type d -exec chmod 755 "{}" \;
  find pkg/usr/share/emule -type f -exec chmod 644 "{}" \;

  install -d -m755 pkg/usr/bin
  install -m755 emule pkg/usr/bin
}
}}

Now we make our emule file, which according to , will be copied and made executable in .

 #!/bin/bash
 export WINEARCH=win32 WINEPREFIX="$HOME/.emule/wine"

 if [ ! -d "$HOME"/.emule ] ; then
   mkdir -p "$HOME"/.emule/wine || exit 1
   #Each user will have its config, we copy the default file since emule
   #needs to write here.
   cp -r /usr/share/emule/config "$HOME"/.emule || exit 1
   #We symlink the files emule needs to read to work
   ln -s /usr/share/emule/emule.exe "$HOME"/.emule/emule || exit 1
   ln -s -T /usr/share/emule/lang "$HOME"/.emule/lang || exit 1
   ln -s -T /usr/share/emule/webserver "$HOME"/.emule/webserver || exit 1
 fi

 wine "$HOME"/.emule/emule "$@"

If you want to be more precise, you may add a message in the  file telling the user that they should disable search history since wine messes up that menu. You may even provide a default configuration file with the best settings.  And that's it... run , check the package folder to be sure, and install.

## Gecko and Mono
Unless you know for sure, that software require browser of .NET runtime (packages  and ), default wine installation prompts for Gecko/Mono are undesirable.

To disable HTML rendering, bytecode support and the dialogs, you need to use a dlloverride in your script.
For Gecko:

 export WINEDLLOVERRIDES="mshtml="

For Mono:

 export WINEDLLOVERRIDES="mscoree="

For both:

 export WINEDLLOVERRIDES="mscoree,mshtml="

You can also disable them via : just set mscoree/mshtml to Disable.
