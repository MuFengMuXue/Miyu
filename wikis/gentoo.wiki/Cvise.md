[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=C-Vise&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Package information](https://packages.gentoo.org/packages/dev-util/cvise)

[[]][GitHub](https://github.com/marxin/cvise)

**C-Vise** is a super-parallel Python port of the C-Reduce. The port is fully compatible to the C-Reduce and uses the same efficient LLVM-based C/C++ reduction tool named clang_delta.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Reducing the official example]](#Reducing_the_official_example)
-   [[3] [See also]](#See_also)

## [Installation]

### [USE flags]

### [USE flags for] [dev-util/cvise](https://packages.gentoo.org/packages/dev-util/cvise) [[]] [Super-parallel Python port of the C-Reduce]

  ----------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`test`](https://packages.gentoo.org/useflags/test)   Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  ----------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-04-14 12:38] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

To install [[[dev-util/cvise]](https://packages.gentoo.org/packages/dev-util/cvise)[]]:

`root `[`#`]`emerge --ask dev-util/cvise`

## [Usage]

### [Reducing the official example]

**C-vise\'**s official example is:

[FILE] **`pr94534.c`**

    template<typename T>
    class Demo
     payload;
      friend decltype(payload);
    };

    int main()


The issue with this example is it compiles on Clang but not GCC, so to figure out why, a reduction script has to be made.

** Important**\
C-Vise\'s return values might be considered the inverse of \"normal\" values, 0 means the file is interesting (i.e. failure to compile) and 1 means the file is not interesting (i.e. it successfully compiles).

To make a script to reduce, a simple shell file should suffice:

[FILE] **`reduce.sh`**

    #!/bin/sh

    g++ pr94534.C -c 2>&1 | grep 'instantiate_class_template_1' && clang++ -c pr94534.C

And finally the reduction may be run:

`user `[`$`]`cvise reduce.sh pr94534.c`

    INFO ===< 30356 >===
    INFO running 16 interestingness tests in parallel
    INFO INITIAL PASSES
    INFO ===< IncludesPass >===
    ...
    template <typename> class a ;
    void c()

## [See also]

-   [GCC_ICE_reporting_guide](https://wiki.gentoo.org/wiki/GCC_ICE_reporting_guide "GCC ICE reporting guide") --- guide to debugging **GCC Internal Compiler Errors** (ICEs)