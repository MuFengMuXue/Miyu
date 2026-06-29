# Unofficial user repositories

This article lists binary repositories freely created and shared by the community, often providing pre-built versions of PKGBUILDs found in the Arch User Repository (AUR).

In order to use these repositories, add them to , as explained in pacman#Repositories and mirrors. If a repository is signed, you must obtain and locally sign the associated key, as explained in pacman/Package signing#Adding unofficial keys.

Many of the unofficial Arch Linux repositories are indexed on https://archlinux.pkgs.org — it provides repositories browser and packages search.

If you want to create your own custom repository, follow pacman/Tips and tricks#Custom local repository.

If you have your own repository, please add it to this page so that all the other users will know where to find your packages. Keep the following rules when adding new repositories:

* Keep the lists in alphabetical order.
* Include some information about the maintainer—at least a (nick)name and some form of contact information (website, email address, user page on ArchWiki or the forums, etc.).
* Include some short description—e.g., the category of packages provided in the repository.
* If there is a page—either on ArchWiki or external—containing more information about the repository, include a link to it.
* If the repository is of the signed variety, please include a key-id, possibly using it as the anchor for a link to its keyserver; if the key is not on a keyserver, include a link to the key file.
* If possible, avoid using comments in code blocks: the formatted description is much more readable. Users who want some comments in their  can easily create it on their own.

Some repositories may also have packages for architectures besides x86_64. The  variable will be set automatically by pacman.

## Signed
## ada
* Maintainer: Rod Kay
* Description: Arch Ada Repository—all packages relating to the Ada and SPARK programming languages.
* Key-ID: 0xED55AF75B0330A2A3BAA9986B6120CD888A0DFD2

## alerque
* Maintainer: Caleb Maclennan
* Description: Typesetting, publishing, and font development related tools such as SILE, CaSILE, Fontship, and their related dependencies including many fonts, Lua rocks, and Python modules. Also Asterisk, most of the AUR packages I (co-)maintain, and many of the AUR builds I use personally.
* Git repository: https://github.com/alerque/aur
* Key-ID: 63CC496475267693

## ALHP
* Maintainer: Giovanni Harting
* Description: ALHP—stands for whatever you want it—provides official repositories compiled for specific x86-64 microarchitecture level with additional optimizations1:

:{| class="wikitable"
|-
! !! C and C++ !! Fortran !! Go !! Rust
|-
| CPU microarchitecture
|
:
:

, 2:
: 3
|
:
:
|

|
:
:
|-
| Link-time optimization(LTO)
|
:
: -falign-functions=32
|
|
|

:
:
|-
| Other
|
:
:
:

, :
: 4
|
:
:
|
|
:
:
:
:
|}

:# See the current compilation flags in https://somegit.dev/ALHP/ALHP.GO/src/branch/main/flags.yaml and https://alhp.dev/makepkg/.See also makepkg#Optimization.
:# You have to use Dynamic Kernel Module Support (DKMS) packages instead of directly linked kernel modules—e.g. users of ,  and ArchZFS are affected.
:# Setting  for the kernel compilation would not yield any significant results.
:# Setting  for the kernel compilation is questionable.

: See also Blacklisted packages.

* Git repository: https://somegit.dev/ALHP/ALHP.GO
* Keyring:
* Mirrors:
* debuginfod: https://debuginfod.alhp.dev

 Include = /etc/pacman.d/alhp-mirrorlist

 [extra-x86-64-v''N''
 Include = /etc/pacman.d/alhp-mirrorlist

 Include = /etc/pacman.d/alhp-mirrorlist

## andontie-aur
* Maintainer: Holly M.
* Description: A repository containing the most popular AUR packages, as well as some I use all the time. New packages can be requested on the upstream website.
* Upstream page: https://aur.andontie.net
* Key-ID: [https://keyserver.ubuntu.com/pks/lookup?search=72BF227DD76AE5BF&fingerprint=on&op=index 72BF227DD76AE5BF

## arcanisrepo
* Maintainer: arcanis
* Description: AUR packages (including some VCS packages), mostly development and scientific tools. Updated daily.
* Upstream page: https://repo.arcanis.me/arcanisrepo/x86_64/index.html
* Key-ID: 0xBD2AC8C5E989490C

## arch4edu
* Maintainers: Jingbei Li (petronny), and others
* Description: Community repository for Arch Linux and Arch Linux ARM that strives to provide the latest versions of most software used by college students.
* Git repository: https://github.com/arch4edu/arch4edu, also for packaging issues, out-of-date notifications, package requests, and related questions.
* Key-ID: 7931B6D628C8D3BA
* Mirrors: https://github.com/arch4edu/mirrorlist/blob/master/mirrorlist.arch4edu

## archlinuxcn
* Maintainers: phoenixlzx, Felix Yan (felixonmars, dev), lilydjwg, farseerfc, and others
* Description: Packages by the Chinese Arch Linux community, all signed. Be aware that non-x86_64 packages are not fully maintained and tested. Create an issue if you find some problems.
* Git repository: https://github.com/archlinuxcn/repo, also for packaging issues, out-of-date notifications, package requests, and related questions.
* Key-ID: Once the repository is added, archlinuxcn-keyring package must be installed before any other, so you do not get errors about PGP signatures. archlinuxcn-keyring package itself is signed by a developer.
* Mirrors: https://github.com/archlinuxcn/mirrorlist-repo, or install archlinuxcn-mirrorlist-git from the repository and use the  mirror list.
* debuginfod: https://repo.archlinuxcn.org

## ArchZFS
* Maintainers: Jan Houben (minextu), Luchesar Iliev (kerberizer), and others
* Description: Packages for ZFS on Arch Linux.
* Upstream wiki: https://github.com/archzfs/archzfs/wiki
* Key-ID: 3A9917BF0DED5C13F69AC68FABEC0A1208037BE9

## artafinde
* Maintainer: Leonidas Spyropoulos
* Description: Personal repository with AUR and custom packages.
* Key-ID: Not needed, as key is in archlinux keyring.

## avr
* Maintainer: Vianney Bouchaud
* Description: Some of the AUR builds I use personally, packages mainly related to kubernetes that I used to build for my own use as well as some of my own software that I also package.
* Upstream page: https://bouchaud.org/packages/avr
* Git repository: https://github.com/vbouchaud/aur
* Key-ID: 157B08346330029C

## bioarchlinux
* Maintainer: BioArchLinux Team
* Description: Biological Software Repository for Arch Linux, incrudes R cran binary packages.
* Upstream page: https://github.com/BioArchLinux/Packages
* Setup: https://wiki.bioarchlinux.org/index.php?title=Usage
* Citation: https://doi.org/10.1093/bioinformatics/btaf106
* Key-ID: B1F96021DB62254D

## blackeagle-pre-community
* Maintainer: Ike Devolder
* Description: Testing of the by me maintained packages before moving to extra repository.
* Key-ID: Not required, as maintainer is a Package Maintainer.

## build.kilabit.info
* Maintainer: shulhan
* Upstream page: https://build.kilabit.info
* Package list: https://build.kilabit.info/karajo/app/
* Key-ID: 4A5360B500C9C4F0

## chaotic-aur
* Maintainer: dr460nf1r3, PedroHLC, LordKitsuna, Librewish, SolarAquarion, thotypous (former TU), and RustemB (in memoriam).
* Description: Auto builds AUR packages the maintainers use, update them hourly (a few are updated daily). It has several mirrors worldwide. Its main builder is hosted at the Federal University of Sao Carlos, Brazil. It's x86_64 only.
* Upstream page: https://aur.chaotic.cx
* Key-ID: FBA220DFC880C036, with some subkeys. To help, keyring and mirror list are available at the repository's homepage.

## coderkun-aur
* Maintainer: coderkun
* Description: AUR packages with random software. Supporting package deltas and package and database signing.
* Upstream page: https://www.suruatoel.xyz/arch
* Key-ID: 39E27199A6BEE374
* Keyfile: https://www.suruatoel.xyz/coderkun.key

## condorcore
* Maintainer: MrHacker
* Description: Wazuh-SIEM packages that I co-maintain and AUR. signed from the database.
* Upstream page: https://aur.condorbs.net
* Key-ID: 3CA0B9DF1BE7CE09
* Keyfile:GPG
* Keyring: https://aur.centauricorex.net/x86_64/condorcore-keyring-20231117-1-any.pkg.tar.zst

## desolve
* Maintainer: desolve
* Description: Collection of some extra stuff, binary R cran.
* Git repository for other AUR packages: https://github.com/dvdesolve/pkgbuilds
* Key-ID: DD3BF75DCD96541AC723B7CD6A4CD3276CA8EBBD

## devkitpro
* Maintainer: wintermute
* Description: Provides Homebrew toolchains for the Nintendo Wii, Gamecube, DS, GBA, Gamepark gp32, and Nintendo Switch.
* Upstream page: https://devkitpro.org/wiki/devkitPro_pacman
* Key-ID: F7FD5492264BB9D0
* Keyring: https://pkg.devkitpro.org/devkitpro-keyring.pkg.tar.xz

## g14
* Maintainer: Luke Jones
* Description: A custom repository for ASUS Linux, it contains prebuilt binaries for all of the software they offer.
* Upstream page: https://asus-linux.org/
* Package list: https://arch.asus-linux.org/
* Key-ID: 8F654886F17D497FEFE3DB448B15A6B0E9A3FA35

## grawlinson
* Maintainer: George Rawlinson
* Description: AUR packages maintained by the user as well as some experimental packages.
* Git repository: https://git.little.kiwi/grawlinson/arch-pkgs
* Package list: https://mirror.little.kiwi
* Key-ID: 9D120F4AAF400B8313A87EF2369552B2069123EE
* Keyfile: https://mirror.little.kiwi/grawlinson.asc

## herecura
* Maintainer: Ike Devolder
* Description: Additional packages not found in the Community repository.
* Git repository: https://gitlab.com/herecura/packages
* Key-ID: Not required, as maintainer is a Package Maintainer.

## ivasilev
* Maintainer: Ianis G. Vasilev
* Description: A variety of packages, mostly my own software and AUR builds.
* Upstream page: https://ivasilev.net/pacman
* Key-ID: 17DAB671

## jk-aur
* Maintainer: JustKidding
* Description: Packages from the AUR I maintain and co-maintain.
* Upstream page: https://github.com/jstkdng/aur
* Key-ID: 7627D0F8F60FBA35371A29E1AA6B2752759F9361

## kawaii
* Maintainer: Leonid Pilyugin
* Description: Kawaii modified packages from AUR and myself.
* Upstream page: https://github.com/LeonidPilyugin/kawaii-repo
* Key-ID: A308BDBE10D7C9C168AA2E055F2E4806FFE6B2CD

## lahwaacz
* Maintainer: Jakub Klinkovský
* Description: Personal repository with AUR packages.
* Key-ID: Not needed, as key is in the  package.

## linux-lts66
* Maintainer: bemxio
* Description: A repository for the  kernel packages, including  and .
* Git repository: https://github.com/bemxio/linux-lts66-repo
* Key-ID: D6BA2CBC66075B2B

## linux-nitrous
* Maintainer: Simao Gomes Viana (superboringdev or xdevs23)
* Description: Prebuilt packages of the linux-nitrous kernel.
* Git repository: https://gitlab.com/xdevs23/linux-nitrous, also for packaging issues and questions.
* Key-ID: 3FFA4C23 (keyserver.ubuntu.com) | 3FFA4C23 (pgp.mit.edu) | 3FFA4C23 (pgp.net.nz)

## liquorix
* Maintainer: Steven Barrett (damentz)
* Description: Automated builds of , , and .
* Upstream page: https://liquorix.net
* Git repository: https://github.com/damentz/liquorix-package, https://aur.archlinux.org/cgit/aur.git/log/?h=linux-lqx
* Key-ID:  9AE4078033F8024D (keys.openpgp.org)

## manuelschneid3r_Arch
* Maintainer: Manuelschneid3r
* Description: Albert launcher packages by the developer of Albert.
* Key-ID: https://software.opensuse.org/download/package.iframe?project=home:manuelschneid3r&package=albert

## miffe
* Maintainer: miffe (AUR profile)
* Description: AUR packages maintained by miffe, e.g. linux-mainline.
* Key-ID: 313F5ABD

## mxmeinhold
* Maintainer: mxmeinhold
* Description: Packages I maintain in the AUR, currently just factorio-headless.
* Key-ID: B77D730E8D444707FA93320D72E05836F8252405
* Keyfile: https://gpg.mxmeinhold.com

## orhun
* Maintainer: Orhun Parmaksiz
* Description: Personal repository with AUR and custom packages.
* Key-ID: Not needed, as the maintainer is a Package Maintainer.

## oscloud
* Maintainer: bionade24
* Description: Various command-line tools and other packages from the AUR.
* CI/CD status: https://abs-cd.oscloud.info
* Key-ID: FF363C5F81664E2B

## ownstuff
* Maintainer: Martchus
* Description: A lot of packages from the AUR and the referenced upstream page, e.g. a great number packages for mingw-w64 and Android cross compilation, nvidia-580xx packages (including compiled modules for  and ), fonts, Perl modules, tools like ,  and .
* Upstream page: https://github.com/Martchus/PKGBUILDs (sources beside the AUR) and https://martchus.dyn.f3l.de/buildservice/#package-search-section (package browser/search)
* Key-ID: B9E36A7275FC61B464B67907E06FE8F53CDC6A4C

## pkgbuilder
* Maintainer: Chris Warrick
* Description: A repository for PKGBUILDer, a Python AUR helper.
* Upstream page: https://github.com/Kwpolska/pkgbuilder
* Key-ID: 5EAAEA16

## post-factum kernels
* Maintainer: Oleksandr Natalenko aka post-factum
* Description: pf-kernel packages by its developer, post-factum.
* Upstream page: https://pfkernel.natalenko.name
* Key-ID: 95C357D2AF5DA89D
* Keyfile: https://download.opensuse.org/repositories/home:/post-factum:/kernels/Arch/x86_64/home_post-factum_kernels_Arch.key

## pro-audio-legacy
* Maintainer: David Runge
* Description: Legacy tooling for Professional audio (e.g. ), mainly useful for old setups or CI.
* Key-ID: Not needed, as maintainer is a developer/TU.

## proaudio
* Maintainer: OSAMC members (SpotlightKid, cbix, daniel.appelt et al.)
* Description: Professional audio packages not (yet) in the official repos, built for x86_64 and aarch64.
* Upstream page: https://arch.osamc.de/
* Git repository: https://github.com/osam-cologne/archlinux-proaudio (PRs welcome)
* Key-ID: 762AE5DB2B38786364BD81C4B9141BCC62D38EE5
* Keyfile: https://arch.osamc.de/proaudio/osamc.gpg

## QOwnNotes
* Maintainer: Patrizio Bekerle (pbek), QOwnNotes author
* Description: QOwnNotes is an open-source notepad and todo list manager with markdown support and ownCloud integration.
* Key-ID: F2205FB121DF142B31450865A3BA514562A835DB
* Keyfile: https://download.opensuse.org/repositories/home:/pbek:/QOwnNotes/Arch_Extra/x86_64/home_pbek_QOwnNotes_Arch_Extra.key

## quarry
* Maintainer: anatolik
* Description: Arch binary repository for Rubygems packages. See forum announcement for more information.
* Git repository: https://github.com/anatol/quarry
* Key-ID: Not needed, as the maintainer is a developer.

## repo.mksscryertower.quest
* Maintainer: Klimenko Maxim Sergievich
* Description: Collection of AUR packages that I personally use: Crowdsec, libraries and etc.
* Key-ID: CF26478FD667CD54

## rne
* Maintainer: Richard Neumann
* Description: Collection of AUR packages that I personally use.
* Key-ID: 4CA8D523BD386AF7

## seblu
* Maintainer: Sébastien Luttringer
* Description: All seblu useful pre-built packages, some homemade (linux-seblu-meta, zfs-dkms, spotify, masterpdfeditor, etc.).
* Key-ID: 8DBD63B82072D77A

## seiichiro
* Maintainer: Stefan Brand (seiichiro0185)
* Description: AUR-packages I use frequently.
* Key-ID: 805517CC

## sergej-repo
* Maintainer: Sergej Pupykin
* Description: nextcloud, prosody, and some other stuff.
* Key-ID: Not required, as the maintainer is a Package Maintainer.

## sublime-text
* Maintainer: Sublime Text developer
* Description: Sublime Text editor packages from developer's repository.
* Upstream page: https://www.sublimetext.com/docs/3/linux_repositories.html#pacman
* Key-ID: 8A8F901A

## supermario
* Maintainer: Mario Finelli (supermario)
* Description: AUR packages that I use or maintain.
* Git repository: https://github.com/mfinelli/pkgs, https://github.com/mfinelli/aur-packages
* Key-ID: C3CD75B002978A8468CA7B1F6C3ADDDE36FDA306
* Keyfile: https://finelli.pub/36FDA306.asc

## taur
* Maintainer: toufic ar. (toufy)
* Description: Weekly builds of AUR packages (mostly for development) that I use.
* Upstream page: https://aur.toufy.me
* Git repository: https://git.toufy.me/taur
* Key-ID: BBA33017E29E74FB

## trinity
* Maintainer: Trinity Desktop Environment Developers
* Description: Trinity Desktop Environment.
* Key-ID: D6D6FAA25E9A3E4ECD9FBDBEC93AF1698685AD8B

## xyne-x86_64
* Maintainer: Xyne
* Description: A repository for Xyne's own projects.
* Upstream page: https://xyne.dev/projects/

* Key-ID: Not required, as maintainer is a TU.

## Unsigned
## alucryd
* Maintainer: Maxime Gauduin
* Description: Various packages Maxime Gauduin maintains (or not) in the AUR, in particular the multilib repository is for various packages needed to run Steam without its runtime environment.

## arch-mact2
* Maintainer: Noa Himesaka
* Description: Kernel and utilities for use on Macs with T2 security chip.
* Upstream page: https://mirror.funami.tech/arch-mact2

## archlinuxgr
* Maintainer:
* Description: many interesting packages provided by the Hellenic (Greek) Arch Linux community

## archlinux-phalcon
* Maintainer: Michal Sotolar
* Description: Phalcon Framework PHP 5.6 - 7.x extension builds
* Upstream page: https://archlinux-phalcon.gitlab.io

## archlinux-php
* Maintainer: Michal Sotolar
* Description: PHP 5.6 - 7.x old stable builds coexistable with mainline version
* Upstream page: https://archlinux-php.gitlab.io

## dx37essentials
* Maintainer: DragonX256
* Description: Personal repository. Contains packages from AUR, which I using every day.
* Git repo: https://gitlab.com/DX37/dx37essentials
* Upstream page: https://dx3756.ru/dx37essentials

## ffy00 (python)
* Maintainer: Filipe Laíns
* Description: Provides several different Python versions (eg. 3.5, 3.6, 3.7). All active Python releases should be available here.
* Git repo: https://github.com/FFY00/arch-python-repo
* Upstream page: https://github.com/FFY00/arch-python-repo

## heftig
* Maintainer: Jan Alexander Steffens
* Description: Includes firefox-nightly,  and crawl-git
* Upstream page: https://bbs.archlinux.org/viewtopic.php?id=117157

## kicad-nightly
* Maintainer: Rafael Silva
* Description: Prebuilt nightly packages for KiCad
* Git repo: https://gitlab.com/kicad/packaging/kicad-arch/kicad-arch-builder
* Upstream page: https://www.kicad.org/help/nightlies-and-rcs/

## mesa-git
* Maintainer: Laurent Carlier
* Description: Mesa git builds for the testing repositories

## principia
* Maintainer: ROllerozxa
* Description: Binary builds of the  and  packages.
* Upstream page: https://arch.principia-web.se

## rayr
* Maintainer: Rayr
* Description: Prebuilt packages of my AUR packages, as an Arch repo.
* Upstream page: https://github.com/Rayrsn/ArchRepo

## selinux
* Maintainer: Nicolas Iooss (nicolas  iooss  m4x  org)
* Description: Provide binary packages for SELinux.
* Upstream Page: https://github.com/archlinuxhardened/selinux

## stx4
* Maintainer: StarterX4
* Description: Any – some fonts and fakepkgs; x86_64 – archival yet might useful packages (like PacmanXG4), and some AUR soft I use* Upstream Page: https://github.com/StarterX4/StarterX4.github.io

## vdr4arch
* Maintainers: [https://aur.archlinux.org/account/CReimer CReimer, M-Reimer
* Description: A set of VDR packages for Arch Linux
* Upstream page: https://github.com/VDR4Arch/vdr4arch
