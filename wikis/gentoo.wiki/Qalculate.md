[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Qalculate&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://qalculate.github.io)

[[]][GitHub](https://github.com/Qalculate/libqalculate)

[[]][Package information](https://packages.gentoo.org/packages/sci-libs/libqalculate)

**Qalculate** is a multi-purpose cross-platform desktop calculator that features a large library of customizable functions, unit calculations and conversion, physical constants, symbolic calculations (including integrals and equations), arbitrary precision, uncertainty propagation, interval arithmetic, plotting, and a user-friendly interface.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
    -   [[1.3] [GUI applications]](#GUI_applications)
        -   [[1.3.1] [Qalculate-gtk]](#Qalculate-gtk)
        -   [[1.3.2] [Qalculate-qt]](#Qalculate-qt)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Basic calculations]](#Basic_calculations)
    -   [[2.2] [Interactive mode]](#Interactive_mode)
    -   [[2.3] [Using the previous result]](#Using_the_previous_result)
    -   [[2.4] [Performing currency conversions]](#Performing_currency_conversions)
-   [[3] [See also]](#See_also)

## [Installation]

### [USE flags]

### [USE flags for] [sci-libs/libqalculate](https://packages.gentoo.org/packages/sci-libs/libqalculate) [[]] [A modern multi-purpose calculator library]

  --------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`+curl`](https://packages.gentoo.org/useflags/+curl)           Add support for client-side URL transfer library
  [`+hardened`](https://packages.gentoo.org/useflags/+hardened)   Disable unsafe functions like \'command\' and variables like \'uptime\'.
  [`gnuplot`](https://packages.gentoo.org/useflags/gnuplot)       Enable support for gnuplot (data and function plotting)
  [`icu`](https://packages.gentoo.org/useflags/icu)               Enable ICU (Internationalization Components for Unicode) support, using dev-libs/icu
  [`readline`](https://packages.gentoo.org/useflags/readline)     Enable support for libreadline, a GNU line-editing library that almost everyone wants
  [`test`](https://packages.gentoo.org/useflags/test)             Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  --------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-04-03 19:49] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask sci-libs/libqalculate`

### [GUI applications]

#### [Qalculate-gtk]

`root `[`#`]`emerge --ask sci-calculators/qalculate-gtk`

#### [Qalculate-qt]

`root `[`#`]`emerge --ask sci-calculators/qalculate-qt`

## [Usage]

### [Basic calculations]

To perform basic calculations with qalculate, use it like a regular calculator:

`user `[`$`]`qalc 1 + 1`

    1 + 1 = 2

### [Interactive mode]

To enter qalculate\'s interactive mode, run [qalc]:

`user `[`$`]`qalc`

    >

And start performing calculations:

`user `[`$`]`qalc`

    > 1 + 1

      1 + 1 = 2

    >

### [Using the previous result]

To use the previous result in a new calculation, use the `ans` keyword:

`user `[`$`]`qalc`

    > 1 + 1

      1 + 1 = 2

    > ans + 2

      ans + 2 = 4

    >

### [Performing currency conversions]

Add `curl` to [[[sci-libs/libqalculate]](https://packages.gentoo.org/packages/sci-libs/libqalculate)[]]\'s USE flags:

[FILE] **`/etc/portage/package.use/libqalculate`**

    sci-libs/libqalculate curl

To convert between currencies:

`user `[`$`]`qalc`

    > 1 usd to aud

      1 USD ≈ AUD 1.519918094

## [See also]

\* [bc](https://wiki.gentoo.org/wiki/Bc "Bc") --- arbitrary-precision fixed-point mathematical scripting language