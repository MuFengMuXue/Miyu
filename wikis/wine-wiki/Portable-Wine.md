In the past, installing Wine to a portable distribution could be a
lengthy struggle, fraught with peril, frustration, and chroots. But that
gloomy age is gone now! Thanks to the widespread and mature live-system
machinery developed by many distros, it shouldn't be hard to have your
own portable installation of Wine.

## Installing the Base Distro

The main thing you'll need is a properly formatted (FAT32) USB flash
drive. To be sure you also have enough space, you'll probably want...

- At least 3 to 4 GB for the base distro, though some only require a few
  hundred MB
- 1 GB or more for Wine itself and any dependencies
- Another GB if you plan to keep and compile from source on the drive
- Anywhere from just a few to hundreds of GB for your programs and data,
  depending entirely on your needs

The next ingredient is the ISO image of whatever distro you want to run
Wine on. If you don't have one in mind, two well-known Linux distros
that historically focused on portability are
[KNOPPIX](https://www.knopper.net/knoppix/index-en.html) and
[Puppy](https://puppylinux.org/main/Overview%20and%20Getting%20Started.htm),
but most major distros including [Fedora](Fedora) and
[Ubuntu](Debian-Ubuntu) now offer live-USB versions.

Another distro you might find interesting is [Zorin
OS](https://zorinos.com/), which tries to make Linux as familiar to
Windows users as possible and consequently includes a version of Wine
right out of the box.

You can always just go to your preferred distro's website and download
an ISO image, but another option definitely worth considering is the
[UNetbootin](https://unetbootin.github.io/) tool. Not only can this
create your live-USB install from a pre-downloaded ISO, or download the
ISO itself, but it makes configuring other settings for your live-USB
simple, and can be used entirely from within Windows.

Mac computers have a picky boot-loader and will not accept the file
structure typically used on live-USBs. As a result, even though
UNetbootin runs on Mac OS X, it can't create a live-USB image bootable
on OS X.

This doesn't mean you can't create a portable installation for running
on Macs; the tool [Mac Linux USB
Loader](https://sevenbits.github.io/Mac-Linux-USB-Loader/) supposedly
can, but we haven't tested this software before. If that doesn't work,
you may just need to follow special instructions for manually creating
your live-USB (Ubuntu's [live-USB for OS
X](https://www.ubuntu.com/download/desktop/create-a-usb-stick-on-mac-osx)
instructions are a good example)

Whether you choose a live-USB creator or to follow your distro's
specific instructions manually, just **be sure to enable *persistence***
when you install the distro to your USB. This setting will allow your
live-USB to record any changes to settings and files when you log off,
which is exactly what you need to install Wine and your programs to the
drive.

## Installing Wine and Programs

Once you have a persistent live-USB ready and working, installing Wine
itself shouldn't be too hard at all. If you're ok with the version
packaged by the distro itself, you should be able to install Wine
through the package manager. We also package recent development and
staging versions of Wine for a few distros; you can find out more at our
[Downloads page](Download).

If you want the cutting-edge, as long as your USB drive and host
computer's RAM have enough space, downloading [Wine from
Git](Git-Wine-Tutorial) and [Building Wine](Building-Wine) from source
should also work essentially the same.

Just don't forget to always reboot or shutdown, then unplug your
live-USB properly so that data isn't corrupted.

## Other Possible Ideas

This section is for noting other approaches that have definite
disadvantages, but may actually be useful for some users. If you do come
across a situation where one of these methods is preferable, feel free
to move its entry to a new section with detailed instructions.

- If you really want or need to, remastering your distro's ISO image
  with Wine and your programs already installed, then writing it to your
  USB is possible. In fact, this used to be the required approach for
  portable Wine. Compared to a persistent live install though, this
  method results in an installation that is both more difficult to setup
  and less convenient to update.

<!-- -->

- Another thing a remastered ISO image would allow for is theoretically
  putting your Wine install and distro on a DVD, rather than a USB.
  However, with the ubiquity of USB ports, using a DVD would have
  essentially no advantages over a flash drive (except the lower cost of
  the disk) but many disadvantages (longer boot times and even a
  rewritable DVD would have limited capacity for updates, which would be
  *very* inconvenient)

<!-- -->

- Installing Wine and your prefixes and programs to a flash drive,
  without any underlying distro, is entirely possible. Besides being
  inherently less portable (it would only work on unix hosts with all
  necessary dependencies), you would need to configure each host system
  to properly access the files.
  - Actually, if you're just interested in unix host systems, this might
    not be too hard. One could keep a script on the flash drive to do
    any necessary configuration.
  - Would symlinking even be necessary, or could directories just be
    appended to the session's PATH variables?

<!-- -->

- One last possibility is to still have a live-USB distribution, but
  rather than installing Wine through the OS with persistence, keep Wine
  outside the OS file-system on the flash drive. This method should
  still be wholly portable, but the OS would need to be configured to
  find all the files (preferably on mount without user input)
  - This method does arguably keep the base OS image more stable, with
    Wine in a distinct overlay. Would that be a significant advantage
    though?
  - If the Wine files can be kept in a different partition altogether,
    one could also use file-systems other than FAT for them.

## See Also

- [Buildroot](Buildroot)
