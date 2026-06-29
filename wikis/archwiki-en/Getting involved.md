# Getting involved

In evolutionary biology, cooperation describes interactions where an individual pays a small cost to yield a larger benefit to one or more others. If this contribution is reciprocated, everyone involved can benefit tremendously. This principle also applies to proactive members of the Arch community wanting to get involved and contribute to their favorite Linux distribution. Their participation benefits not only the community member and their fellow Archers, but all users of free and open source software.

This article describes how both new and experienced Arch users can contribute to the community. Note that this is not an exhaustive list. Before contributing, please get accustomed with the Code of conduct.

## Community
## Post on the forums
One of the easiest ways to get involved is participating in the Arch Linux Forums, which allows getting to know the community and help new users.

## Improve this wiki
ArchWiki is a collaboratively maintained Arch Linux documentation. All users are encouraged to contribute.

## Join the chatroom
You can help other users solve problems on the Arch IRC channels. It is of vital importance however, that you read the channel rules before participating. Further channels are available for specific topics.

## Join the mailing lists
Join the discussion on one or more of the public mailing lists. Make sure to stay on topic as provided in the list description.

## Artwork
Feel free to share wallpapers, splash screens, color palettes, widgets, themes, etc. with the community on the art subforum.

See also Arch Linux Art and Artwork.

## Packages
## Report installed packages
pkgstats provides a systemd timer that sends a list of the packages installed on your system, along with the architecture and the mirrors you use, to the Arch Linux developers in order to help them prioritize their efforts and make the distribution even better. The information is sent anonymously and cannot be used to identify you. You can view the collected data at the Statistics page. More information is available in this forum thread.

## Fix and report bugs
Reporting and fixing bugs for Arch packages on GitLab is one of the possible ways to help the community.

However, ineffective use can be counter-productive. Please read the Bug reporting guidelines and General guidelines#Packaging merge requests.

## Inform about security issues
New vulnerabilities are found all the time. Help the Arch Security Team keep track of new vulnerabilities.

## Help test packages
Packages on the testing repositories need to be tried out and signed off before they are promoted to the main repositories. Help the Arch Testing Team test new packages.

## Request features
Request features for Arch packages on GitLab. Before doing so, read Bug reporting guidelines#Bug or feature?, to make sure it is a valid feature request, and General guidelines#Packaging merge requests.

Request features for AUR packages on the corresponding AUR package pages.

## Create and adopt AUR packages
The Arch User Repository contains community-made package scripts, allowing users to easily install software not part of the official repositories. Popular packages get included into the extra repository.

## Becoming a Package Maintainer
If you want to help maintain the AUR and packages in the extra repository, you can apply to become a Package Maintainer. See Package Maintainers#How do I become a Package Maintainer? for details.

## Hosting a mirror
If you wish to contribute to a worldwide spread mirror network and help deliver package updates to users, you can set up a mirror server and apply by following the DeveloperWiki:NewMirrors guidelines.

## Help porting Arch Linux to other architectures
While Arch Linux only supports x86_64 as underlying processor architecture, the acceptance of RFC0032: Arch Linux Ports has opened the possibility for other architectures to eventually become supported. If this is something you want to help out with, take a look at the related projects on GitLab, Arch Linux Ports web page, and join the #archlinux-ports IRC channel and the arch-ports mailing list to participate in discussions.

## Events
There are regular events open to the community for bugfixing, cleanup, and other activities.

* AUR Cleanup Day
* Bug Day

## Software projects
The Arch Linux distribution comprises of many components and each of the projects can be contributed to individually.

Discussion around the various projects (unless noted otherwise) takes place on the arch-projects mailing list and in the #archlinux-projects IRC channel on the Libera Chat network.

{| class="wikitable sortable"
! Project !! Description !! Languages !! Maintainers !! Additional links
|-
! alpm
| Project that works on specifications, Rust libraries and tools for Arch Linux Package Management
| Rust
| dvzrv, orhun, nukesor
| bugs, documentation, IRC irc.oftc.net#alpm
|-
! alpm.rs
| Rust bindings for libalpm
| Rust
| Morganamilo
| bugs
|-
! arch-boxes
| Virtual machine images
| Bash
| klausenbusk
| bugs, IRC #archlinux-releng, arch-releng mailing list
|-
! arch-install-scripts
| Useful scripts for installing Arch Linux
| Bash
| Foxboron
| bugs
|-
! arch-rebuild-order
| A CLI tool to determine the rebuild order of provided package(s)
| Rust
| jelle
| bugs
|-
! arch-release-promotion
| Promotion and synchronization of existing releases of a project in Arch Linux's GitLab instance
| Python
| dvzrv
| bugs
|-
! arch-repro-status
| CLI tool for querying the reproducibility status of the Arch Linux packages
| Rust
| orhun
| bugs
|-
! arch-security-tracker
| The security.archlinux.org CVE tracking platform and aids in publishing advisories
| Python (Flask)
| anthraxx
| bugs, IRC #archlinux-security, Advisory mailing list
|-
! arch-signoff
| Sign off Arch Linux test packages
| Python
| Jelle
| bugs
|-
! archinstall
| Arch Linux official installer
| Python
| Torxed
| bugs, Discord, documentation
|-
! archivetools
| A turnkey solution to snapshot Arch Linux packages repositories, ISOs images and bootstrap tarballs
| Bash
|
| bugs
|-
! archiso
| Scripts and configuration for building live media
| bash
| dvzrv, nl6720
| bugs, IRC #archlinux-releng, arch-releng mailing list
|-
! archlinux-common-style
|  Arch Linux common CSS styles
| SCSS, HTML, JavaScript
| anthraxx, jelle
| bugs
|-
! archlinux-docker
| Docker images
| Bash
| hashworks, sangy
| bugs, docker hub, IRC #archlinux-releng, arch-releng mailing list
|-
! archlinux-keyring
| Arch Linux PGP keyring handling
| Python
| anthraxx, dvzrv
| bugs
|-
! archlinux-repro
| Tools to rebuild Arch Linux packages
| Python
| Foxboron, Jelle, Coderobe
| bugs
|-
! archlinux-wsl
| WSL images
| Bash
| Antiz, mark
| bugs, Arch Wiki, IRC #archlinux-releng, arch-releng mailing list
|-
! archmanweb
| The man.archlinux.org website
| Python (Django)
| Lahwaacz
| bugs
|-
! archweb
| The archlinux.org website
| Python (Django)
| jelle
| bugs
|-
! aurweb
| The page and system for aur.archlinux.org
| Python, HTML, MySQL
| artafinde, lfleischer
| bugs, IRC #archlinux-aurweb, aur-dev mailing list
|-
! bugbuddy
| Helper daemon that watches the incoming bug reports for Arch Linux and makes sure that the right people are assigned to them
| Rust
| anthraxx, gromit
| bugs
|-
! bumpbuddy
| A daemon watching for new upstream releases for our packages
| Bash
| Antiz, gromit, klausenbusk
| bugs
|-
! buildbtw
| A service for assisting Arch Linux staff with building new versions of packages
| Rust
| anthraxx, sven, raffomania
| bugs, IRC #archlinux-buildbtw
|-
! dbscripts
| Scripts to release and manage packages into the repositories
| Bash
| Foxboron
| bugs
|-
! devtools
| Packaging tools for developers and packagers
| Bash
| Anthraxx, Foxboron, jelle, gromit
| bugs
|-
! gitlab-exporter
| GitLab metrics exporter
| Rust
| Artafinde, orhun
| bugs
|-
! gluebuddy
| A secure helper daemon that watches several aspects of the Arch Linux infrastructure and makes sure that certain conditions are met
| Rust
| anthraxx, jelle
| bugs
|-
! infrastructure
| Arch Linux infrastructure
| Ansible, Bash, Python, Packer, Terraform, Zsh
| anthraxx, foutrelis, freswa, heftig, jelle, klausenbusk, svenstaro, artafinde, gromit, Antiz
| bugs, IRC #archlinux-devops, arch-devops mailing list
|-
! keycloak-archlinux-theme
| Keycloak Arch Linux theme
| Java
| Artafinde
| bugs
|-
! mkinitcpio
| Initramfs generator
| Ash, Bash
| Foxboron
| bugs
|-
! mkinitcpio-archiso
| Mkinitcpio integration for archiso
| Ash, Bash
| dvzrv, nl6720
| bugs, IRC #archlinux-releng, arch-releng mailing list
|-
! namcap
| Tool for checking binary packages and source PKGBUILDs for common packaging errors
| Python
| alerque, dvzrv, FFY00, kgizdov
| bugs
|-
! netctl
| Profile based systemd network management
| Bash
| jwitteveen
| bugs
|-
! neoasknot
| Contribution landing page for Arch Linux
| JavaScript, Svelte
| polyzen
| bugs, whatcanidofor.archlinux.org
|-
! pacman
| Package Manager
| Bash, C
| Allan, agregory
| bugs, IRC #archlinux-pacman, pacman-dev mailing list
|-
! pacman-contrib
| Contribution scripts to pacman
| Bash, C, Perl
| Demize, Polyzen
| bugs, IRC #pacman-contrib, pacman-contrib mailing list
|-
! pkgstats-cli
| pkgstats client
| Go
| pierres
| bugs, pkgstats.archlinux.de
|-
! pkgstats.archlinux.de
| Arch Linux package statistics website
| JavaScript, PHP, Vue
| pierres
| bugs, pkgstats.archlinux.de
|-
! pyalpm
| alpm Python bindings
| Python, C
| Jelle
| bugs
|-
! pytest-pacman
| Pytest plugin for generating repository sync databases
| Python
| Jelle
| bugs
|-
! rebuilderd-website
| Website for reproducible.archlinux.org
| JavaScript
| Jelle
| bugs, reproducible-builds.org, Debian wiki, IRC #archlinux-reproducible
|-
! releng
| Automation of release artifacts (installation medium, PXE boot)
| Bash, Python
| dvzrv
| bugs, IRC #archlinux-releng, arch-releng mailing list
|-
! repod
| Tooling to maintain binary package repositories for Linux distributions using the pacman package manager
| Python
| dvzrv
| bugs, documentation
|-
! signstar
| A secure enclave signing solution and tooling around it
| Rust
| dvzrv
| bugs, documentation, IRC #archlinux-signstar
|-
! voa
| A project to provide Rust libraries, command line tools to interact with the File Hierarchy for the Verification of OS Artifacts (VOA).
| Rust
| dvzrv, heiko
| bugs, IRC irc.oftc.net#alpm
|}

## Donate money
You can find out how to help sustaining server costs on the official Arch Linux donate page.

## Unofficial projects
Arch's community maintains many projects. Feel free to include yours!

## Groups
Arch-specific groups that you can engage in.

; Arch Linux Subreddit: Place for Reddit users to discuss Arch related issues.
; International communities: Local communities and meet-up places for users.
; Telegram group: Place for Telegram users to discuss Arch related issues.
; Matrix room (in Arch Linux space): Place for Matrix users to discuss Arch related issues.
; Discord server: Place for Discord users to discuss Arch related issues.
; Archcord - Discord server: An alternative Discord server providing users with choice, effective moderation and a warm community. Archcord also has a Fluxer available now at https://fluxer.gg/arch

## Software
Community-developed software that focuses on Arch Linux.

; Community Contributions
: Forum for Arch-related projects.

; Arch Linux topic @GitHub
: GitHub repositories for Arch-related projects.

## Becoming an Arch Developer
The main motivation for your work on Arch should be helping the whole community, and not simply trying to become an Arch developer by any means.

Usually, new developers are picked by the existing developers as the workload increases. Sometimes they post a position and you can apply to fill it, but more often, they just invite somebody they know would be good at it and would fit in well with the rest of the team. Having a portfolio of Arch contributions is the best way to make it on the team.

Here is a list of things that you may do in order to gain some "popularity" towards Arch's developers:

* Establish a reputation as being helpful by offering assistance whenever possible.
* Answer questions on the forum, IRC, and mailing lists.
* Join the Package Maintainers to gain packaging experience to show your skills.
* Submit packages to the AUR.
* Join one of the offshoot projects that may be incorporated into Arch mainstream someday, or start your own.
* Work on pacman, makepkg or other project (on GitLab) and submit patches to the bug tracker.
* Traverse the bug tracker and fix existing bugs.
* Find and submit new bugs.
* Fix wiki errors, add new pages, clean up existing pages and make sure the procedures are up-to-date.
* Submit translations.
