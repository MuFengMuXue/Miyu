**Resources**

[[]][Home](https://github.com/busyloop/lolcat)

**Lolcat** is a funny terminal colorizer written in [Ruby](https://wiki.gentoo.org/wiki/Ruby "Ruby").

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Emerge]](#Emerge)
    -   [[1.2] [Tweaking]](#Tweaking)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Examples]](#Examples)
-   [[3] [External resources]](#External_resources)

## [Installation]

[Accept](https://wiki.gentoo.org/wiki/ACCEPT_KEYWORDS "ACCEPT KEYWORDS") the unstable keyword.

[FILE] **`/etc/portage/package.accept_keywords`**

    games-misc/lolcat ~amd64

### [Emerge]

Install [[[games-misc/lolcat]](https://packages.gentoo.org/packages/games-misc/lolcat)[]]:

`root `[`#`]`emerge --ask games-misc/lolcat`

### [Tweaking]

It is funny to add this to your [\~/.bashrc], if you wish to lolcat all the time:

[FILE] **`~/.bashrc`**

    alias cat="lolcat"

** Warning**\
Adding this to ~~other people\'s~~ your .bashrc however might cause unexpected side effects, use with caution!

## [Usage]

There are many use cases; Here are a few ways to take advantage of it:

`user `[`$`]`find /usr/portage -type f -exec lolcat '' \; `

`user `[`$`]`find /var/cache/man -type f -exec lolcat '' \; `

`user `[`$`]`fortune | cowsay | lolcat `

`user `[`$`]`tcpdump | lolcat `

`user `[`$`]`emerge --info | lolcat `

`user `[`$`]`cat /dev/urandom | base64 -w $COLUMNS | lolcat `

** Note**\
All emerge commands can be lolcatted. Use wisely.

You can have a nice fortune every time you open a shell with a random cow:

[FILE] **`~/.bashrc`**

    cow_mode[1]="-b"
    cow_mode[2]="-d"
    cow_mode[3]="" # default
    cow_mode[4]="-g"
    cow_mode[5]="-p"
    cow_mode[6]="-s"
    cow_mode[7]="-t"
    cow_mode[8]="-w"
    cow_mode[9]="-y"

    rng=$(( $RANDOM % 9 + 1))

    IFS=' '
    cowfiles=(`cowsay -l | sed 1d | paste -sd " "`)
    num_files=$
    cowfile=$

    fortune | cowsay -W 35 $ -f $cowfile | lolcat

### [Examples]

-   [YouTube video](https://www.youtube.com/watch?v=8uEFZ37D4xY)

## [External resources]

-   [[[games-misc/fortune-mod]](https://packages.gentoo.org/packages/games-misc/fortune-mod)[]]
-   [[[games-misc/cowsay]](https://packages.gentoo.org/packages/games-misc/cowsay)[]]
-   [debian community demanding lolcat](https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=646877)