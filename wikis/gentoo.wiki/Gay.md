[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Gay&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][GitHub](https://github.com/ms-jpq/gay)

**gay** is a way to colour your text / terminal to be more gay.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Invocation]](#Invocation)
    -   [[2.2] [Piping]](#Piping)

## [Installation]

### [Emerge]

[[[games-misc/gay::guru]](https://github.com/gentoo-mirror/guru/tree/master/games-misc/gay)[]] is available in the [GURU](https://wiki.gentoo.org/wiki/GURU "GURU") repository.

First, enable the repository:

`root `[`#`]`eselect repository enable guru`

Sync the repository:

`root `[`#`]`emerge --sync guru`

Finally, emerge **gay**.

`root `[`#`]`emerge --ask games-misc/gay`

## [Usage]

### [Invocation]

`user `[`$`]`gay -h`

    usage: gay [-h] [--encoding ENCODING] [-f] [-l] [-g] [-b] [-t] [-a] [-p] [-n]
               [--gq] [--mlm] [--aro] [--poly] [--db] [--dg] [--ag] [--bg] [--gf]
               [--abro] [--nt] [--tri] [-u] [-c ] [-i ] [--period PERIOD]
               [--tabs TABS]

    options:
      -h, --help            show this help message and exit
      --encoding ENCODING

      -f, --flag

      -l, --les, --lesbian, --wlw
      -g, --gay
      -b, --bi, --bisexual
      -t, --trans, --transgender
      -a, --ace, --asexual
      -p, --pan, --pansexual
      -n, --nb, --non-binary
      --gq, --gender-queer
      --mlm
      --aro, --aromantic
      --poly, --polysexual
      --db, --demiboy
      --dg, --demigirl
      --ag, --agender
      --bg, --bigender
      --gf, --genderfluid
      --abro, --abrosexual
      --nt, --neut, --neutrois
      --tri, --trigender

      -u, --unbuffered
      -c , --colour
      -i , --interpolation
      --period PERIOD
      --tabs TABS, --tab-width TABS

### [Piping]

Gay is similar to **lolcat**. To use it:

`user `[`$`]`echo Larry the Cow beckons you to explore the Gentoo Wiki! | gay`