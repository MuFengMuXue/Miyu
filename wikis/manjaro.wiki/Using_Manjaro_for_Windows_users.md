[![](/images/thumb/e/ed/Page_Under_Construction.jpg/300px-Page_Under_Construction.jpg)](//wiki.manjaro.org/index.php?title=File:Page_Under_Construction.jpg)

[](//wiki.manjaro.org/index.php?title=File:Page_Under_Construction.jpg "Enlarge")

Page under construction

## Contents

-   [[1] [Windows has drives, Linux has a hierarchical file system]](#Windows_has_drives.2C_Linux_has_a_hierarchical_file_system)
-   [[2] [Linux has multiple GUIs]](#Linux_has_multiple_GUIs)
-   [[3] [Linux has multiple file systems]](#Linux_has_multiple_file_systems)
-   [[4] [Linux has multiple kernels]](#Linux_has_multiple_kernels)
-   [[5] [Linux doesn't have a registry!]](#Linux_doesn.E2.80.99t_have_a_registry.21)
-   [[6] [What's the difference between BIOS and UEFI?]](#What.E2.80.99s_the_difference_between_BIOS_and_UEFI.3F)
-   [[7] [The terminal is your best friend!]](#The_terminal_is_your_best_friend.21)
-   [[8] [This is how you install software in Linux]](#This_is_how_you_install_software_in_Linux)
-   [[9] [The Community side of Linux]](#The_Community_side_of_Linux)
    -   [[9.1] [Linux is a self-help OS]](#Linux_is_a_self-help_OS)
    -   [[9.2] [You\'re part of a community now!]](#You.27re_part_of_a_community_now.21)
    -   [[9.3] [What is this \'Upstream\' and \'Downstream\" business?]](#What_is_this_.27Upstream.27_and_.27Downstream.22_business.3F)
-   [[10] [Other tips and tricks]](#Other_tips_and_tricks)
-   [[11] [See Also]](#See_Also)

Remember when you installed your very first Windows, added bells and whistles and then couldn't see the wood for the trees any more and had to re-install??? Well, *you're in the same situation now:* **You're a N00b again! Embrace it!** 😇

I know right now you're thinking: *Why is this so much more difficult than Windows?* Whereas in 6 months time, you'll be like: *Why can\'t I make Windows jump through fiery hoops like I do with Linux???*

## [][Windows has drives, Linux has a hierarchical file system]

So Windows has drives:

-   The C:-drive generally contains Windows and sometimes data
-   The D:-drive (if present) contains data and hardly ever contains Windows itself.
-   The maximum number of drives is 26 (A-Z)
-   All drives that contain a known file system are always [mounted](//wiki.manjaro.org/index.php?title=Mounted "Mounted") automatically.

On the other hand, Linux has *one huge file system:*

-   with an unlimited number of partitions (not disks, not drives!) ¹
-   you can mount any partition of a disk anywhere in the file system! (Repeating that you cannot mount a disk, only a partition under Linux!)
-   you can find the official documentation on the Linux File System Hierarchy Standard (FHS) in HTML / PDF / Text format here: [FHS](https://refspecs.linuxfoundation.org/FHS_3.0/index.html) **Homework assignment #1: read that!** 😁
-   No, really: read it!
-   OK, you didn\'t read it; here\'s the [FHS summary](//wiki.manjaro.org/index.php?title=FHS_summary "FHS summary") 😜

\

**Note**

------------------------------------------------------------------------

Partitions are not automatically mounted in Linux!

*Huh? That sounds dumb! Why doesn\'t Linux mount partitions automatically???* That\'s because the Manjaro installer will *manually* mount only the absolute minimum number of partitions to get your system up and running! I.E. It will manually mount:

-   / (always)
-   /home (if you created such a partition)
-   /boot/efi (If you have an UEFI system instead of a BIOS system)

*and it will leave any other partitions alone to ensure you don't mess them up!* I.E. If you have a dual-boot system, Manjaro will not mount your Windows D: drive automatically!

If you want to have any other partitions available at every boot, you should read about [fstab](//wiki.manjaro.org/index.php?title=Fstab "Fstab").

## [Linux has multiple GUIs]

Windows has *only one* Graphical User Interface ([GUI](https://en.wikipedia.org/wiki/Graphical_user_interface)) depending on its version whereas, Linux has different Desktop Environments (DE) :

-   XFCE: Lightweight, simple, best for beginning users
-   KDE: lots of bells and whistles, good for recent and powerful hardware *and people who like to tinker!* 🛠️
-   Gnome: Simple, the default for lots of distributions
-   Cinnamon: ~~Gnome like it should be~~ Beefed-up Gnome with more bells and whistles.
-   LXDE: comparatively low resource requirements. This makes it especially suitable for use on ~~older~~ resource-constrained computers.
-   I3: Great for power users that need non-overlapping titling windows.

And all of the above come with their own:

-   File Manager
-   System Settings (Known to you as \"Control Panel\")
-   Partition Manager (except XFCE: they need one of the others to be installed)

**Note**

------------------------------------------------------------------------

The above is less important on modern computers and has become more a matter of taste than functionality

**What you should remember is that mixing and matching DE\'s is not wise!** More specifically:

-   Don\'t install the Gnome Editor (\`gedit\`) on KDE but use \`kate\` instead because \`gedit\` will pull in a ton of libraries (and functionality) of Gnome which will bloat your system.
-   Don\'t install 2 DEs for one user:
-   You *can* have different DEs on a single computer
-   Each user can have their own DE
-   **Having 2 DEs for one user is a recipe for disaster as one single configuration file might be used by 2 DEs for wildly different functionality** and untangling this Gordian knot will be so complex that a reinstall is always easier.

**Remember:** *You\'re a N00b again! You\'re going to re-install* **at least once!** (Unless you\'re smarter than the authors of this article\... 😁)

## [Linux has multiple file systems]

Windows has one file system: NTFS (and if you include the DOS FAT file system it has two. \*\*²\*\*)

\
Linux has:

-   [EXT2](https://en.wikipedia.org/wiki/Ext2), [EXT3](https://en.wikipedia.org/wiki/Ext3), [EXT4](https://en.wikipedia.org/wiki/Ext4): If you\'re unsure, take EXT4 as that is the newest member of that family and the most used Linux File System (FS) on desktops.
-   [BtrFS](https://en.wikipedia.org/wiki/Btrfs): \"Better FS\" is good for servers or if you have a beefy computer and want FS resilience
-   [ReiserFS](http://en.wikipedia.org/wiki/ReiserFS)
-   [ZFS](http://en.wikipedia.org/wiki/ZFS)
-   *And even more than you\'ll ever need*
-   *And guess what?* Linux can also read and write to [NTFS](https://en.wikipedia.org/wiki/NTFS) 👍 although it cannot do CHKDSKs, defrag such volumes nor can it change its permissions 👎 , so \*before\* you finally wipe Windows from your machine,*please, please, please* first convert any NTFS volumes to EXT4 or any other Linux FS you\'re comfortable with!

\

**Note**

------------------------------------------------------------------------

And remember to \`mount\` (see above) file systems before you access them, because your file manager \*might\* automount them read-only for you (which is not always what you want/need)😊

## [Linux has multiple kernels]

Windows has different versions and each version has its own kernel. So basically Windows has one kernel for Windows 8, one for Windows 10 another for Windows 11, \... (One of the authors of this wiki distinctly remember saying about Windows Version 1.0: *Huh, what a piece of crap, that\'ll go nowhere! Let me buy SideKick instead!* and history proved him wrong\...) 😁

Linux can have multiple [kernel](https://en.wikipedia.org/wiki/Kernel_(operating_system))s and please remember that:

-   LTS = Long Term Support = ultra-stable
-   Stable = Stable *Development* Kernel
-   RC = Release *Candidate* = ***Unstable*** development kernel
-   Keep an eye out on the End Of Life (EOL) dates for LTS kernels [here](https://www.kernel.org/category/releases.html) and for non-LTS kernels [here](https://www.kernel.org)

It\'s always a good idea to have *at least one* Long Term Support (LTS) kernel installed

It\'s always a good idea to have *at least one* **fall-back kernel** installed. E.G. In the case of 5.10 LTS, that would be 5.4 LTS; in the case of 5.14 Stable, that would be 5.10 LTS; \...

It\'s **only** a good idea to have a non-LTS kernel installed if:

-   you have very new hardware and none of the LTS kernels work for you. [\"What should I be aware of if I\'m not on an LTS kernel?\"](//wiki.manjaro.org/index.php?title=%22What_should_I_be_aware_of_if_I%27m_not_on_an_LTS_kernel%3F%22 ""What should I be aware of if I'm not on an LTS kernel?"")
-   you\'re a developer and want to test your applications with the latest *but not necessarily greatest* kernels out there.
-   the whole point of having Manjaro is to test out new things like new kernels and filing bugs with the developers that don\'t have your technical knowledge.
-   to install different kernels, use the \`kernel\` [GUI](https://en.wikipedia.org/wiki/Graphical_user_interface) program or the \`mhwd-kernel\` [CLI](https://en.wikipedia.org/wiki/Command-line_interface) program.
-   E.G. to install the latest LTS kernel at the time of this writing execute:

<!-- -->

    mhwd-kernel --install linux510

\

**Note**

------------------------------------------------------------------------

To compare this to Windows would be to say that if Windows were Linux it would allow you to run the Windows 11 shell on the Windows XP kernel or the other way around or any other bizarre combination \*you as the administrator\* wanted!👏

## [][Linux doesn't have a registry!]

OK, OK: the Gnome DE (Desktop Environment, see above) has something called \"the dconf database\" which is similar to but different from the registry, mostly used for the DE itself whereas most applications will still use config files. (see below) All other DEs have config files, \'just like all Windows versions prior to Windows 95\':

-   system config files are located in \`/etc\`
-   user config files are in \`\~/.config\`:
-   \`\~\` is an abbreviation for \"your home directory\"
-   \`.config\` is a *hidden* directory: (I.E. Any directory starting with a \`.\` is hidden and you probably have to press [Ctrl]+[H] in your DE\'s File Manager to see these.)
-   Application config files *can reside somewhere else* though that happens rarely..

## [][What's the difference between BIOS and UEFI?]

All that good stuff is explained in our [BIOS_and_UEFI](//wiki.manjaro.org/index.php?title=BIOS_and_UEFI "BIOS and UEFI") section.

## [][The terminal is your best friend!]

## [This is how you install software in Linux]

## [The Community side of Linux]

### [Linux is a self-help OS]

### [][You\'re part of a community now!]

### [][What is this \'Upstream\' and \'Downstream\" business?]

## [Other tips and tricks]

[user \$ ][ 1.example command should be here [COPY TO CLIPBOARD]]

\

[user \$ ][ 2.example command should be here [COPY TO CLIPBOARD]]

\

\

\

[\$] [command]\

    result

\

# [See Also]

[FHS](https://refspecs.linuxfoundation.org/FHS_3.0/index.html) The Official documentation by the Linux Foundation (Yeah: where Linus Torvalds lives) 😊