[] This article has been flagged by [cronolio](https://wiki.gentoo.org/wiki/User:Cronolio "User:Cronolio") ([talk](https://wiki.gentoo.org/wiki/User_talk:Cronolio "User talk:Cronolio") \| [contribs](https://wiki.gentoo.org/wiki/Special:Contributions/cronolio "Special:Contributions/cronolio")) for not conforming to the [wiki guidelines](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Guidelines "Gentoo Wiki:Guidelines"). Please [help Gentoo out](https://wiki.gentoo.org/wiki/Help_improve_Gentoo_by_getting_involved_with_documentation!#Make_articles_conform_to_the_guidelines "Help improve Gentoo by getting involved with documentation!") by starting fixing things.

**Resources**

[[![Gentoo peach graphic](/images/thumb/a/ad/Gentoo-logo-peach.svg/25px-Gentoo-logo-peach.svg.png)](https://wiki.gentoo.org/wiki/Project:Science "Project:Science")][Project](https://wiki.gentoo.org/wiki/Project:Science "Project:Science")

The *BLAS/LAPACK Switching Mechanism* is a method to change the BLAS/LAPACK libraries during runtime, without the need to recompile software depending on these libraries.

## Contents

-   [[1] [Overview]](#Overview)
    -   [[1.1] [Importance]](#Importance)
-   [[2] [User guide]](#User_guide)
    -   [[2.1] [Disabling the feature]](#Disabling_the_feature)
    -   [[2.2] [Enabling the feature]](#Enabling_the_feature)
    -   [[2.3] [Recommendations]](#Recommendations)
-   [[3] [Developer guide]](#Developer_guide)
    -   [[3.1] [Providers]](#Providers)
    -   [[3.2] [Reverse dependencies]](#Reverse_dependencies)
-   [[4] [Implementation details]](#Implementation_details)
-   [[5] [Frequently asked questions]](#Frequently_asked_questions)
-   [[6] [Reference]](#Reference)
-   [[7] [Maintainers]](#Maintainers)
-   [[8] [See also]](#See_also)

## [Overview]

The switching mechanism, using [eselect] is based on an [ld.so] feature to allow library search paths to be modified during runtime, which allows a program to load different libraries than the ones it was compiled with.\
This produces a similar result to Debian\'s update-alternatives and in certain aspects is easier to use and manage.

### [Importance]

The classical numerical linear algebra libraries, BLAS and LAPACK, play an important role in the scientific computing field. Various demands, like speed, scalability and memory usage among others, on these libraries pose non-trivial challenges on system management and running code.\
By leveraging this mechanism, which enables the user to switch BLAS and LAPACK libraries smoothly and painlessly, the problems can be properly addressed.

## [User guide]

### [Disabling the feature]

This feature is **disabled** by default, which means users who don't care about it should simply ignore the `eselect-ldso` `USE` flag and not be bothered with the extra choices.

### [Enabling the feature]

Enable the mechanism in the default portage config file:

[FILE] **`/etc/portage/make.conf`**

    USE="$ eselect-ldso"

And update the tree accordingly

`root `[`#`]`emerge --ask --verbose --newuse "@world"`

This will not change the tree if there are no packages which depend on [[[virtual/blas]](https://packages.gentoo.org/packages/virtual/blas)[]], [[[virtual/cblas]](https://packages.gentoo.org/packages/virtual/cblas)[]] or [[[virtual/lapack]](https://packages.gentoo.org/packages/virtual/lapack)[]].\
If later, a package is installed that needs these libraries, such as [[[dev-python/numpy]](https://packages.gentoo.org/packages/dev-python/numpy)[]], [[[dev-python/scipy]](https://packages.gentoo.org/packages/dev-python/scipy)[]], [[[dev-lang/julia]](https://packages.gentoo.org/packages/dev-lang/julia)[]] or any of the other [large list of packages](https://qa-reports.gentoo.org/output/genrdeps/rindex/virtual/blas), this mechanism will be enabled and installed.

To install the mechanism manually, install the following packages

`root `[`#`]`emerge --ask --verbose --newuse "virtual/blas" "virtual/lapack"`

After finishing the installation, to check the status of BLAS/LAPACK selections:

`root `[`#`]`eselect blas list`

    Available BLAS/CBLAS (lib64) candidates:
      [1]   reference *

`root `[`#`]`eselect lapack list`

    Available LAPACK (lib64) candidates:
      [1]   reference *

This means all binaries linked against [libblas.so.3] or [libcblas.so.3] will use the reference BLAS implementation; those linked against [liblapack.so.3] will use the reference LAPACK implementation.

The reference implementation is very slow, and for some users (e.g. scientific computing users) this is unacceptable.\
In Gentoo's main repository, there are several [optimized BLAS/LAPACK implementations available](https://wiki.gentoo.org/index.php?title=BLAS_and_LAPACK_Providers).\
They will be automatically registered in the mechanism as long as the `eselect-ldso USE` flag is enabled during installation.\
For example:

`root `[`#`]`emerge --ask --verbose "sci-libs/blis" "sci-libs/openblas"`

** Note**\
Without the `eselect-ldso` flag, these packages won't be registered in the mechanism and won't install the extra libraries.

After installation with the feature enabled, the BLAS/LAPACK implementation can be switched using [eselect]:

`root `[`#`]`eselect blas set openblas`

`root `[`#`]`eselect lapack set openblas`

Directly run your program again and see if it's running faster.\
No re-compilation is required thanks to this mechanism.\

### [Recommendations]

The most recommended choice is `blas=openblas lapack=openblas`.\
If non-free software is acceptable, `blas=mkl-rt lapack=mkl-rt` is also a possibility.

Advanced users can explore the possible combinations but note that mixing and matching BLAS/LAPACK providers is discouraged as it can *and will* lead to unexpected behaviors during runtime.

** Important**\
Don't use `pthread` and `openmp` at the same time since it will incur significant performance drop due to excessive thread creation.\
This can happen when some libraries linked against an application use OpenMP threading, while some others use pthread.

** Important**\
Please don't use GNU OpenMP ([libgomp.so]) and Intels ([libiomp.so]) at the same time as the symbol clash between them can lead to silent computation error.\
This can happen when MKL uses Intel/LLVM OpenMP while some other libraries linked against the same application use GNU OpenMP.

## [Developer guide]

** Important**\
The promises made here are not mandated by Netlib specifications and should not be relied on. The may be changed in future updates.\

Packages must not rely on the [libblas.so.3/libblas.so] to contain the BLAS symbols but should only assume that linking to [-lblas] will ensure symbol resolution during runtime.\

If you wish to ensure that symbols are present, they should done by linking to provider libraries, such as [libopenblas.so], [libblis.so], [libmkl_rt.so] or any other provider library.

### [Providers]

For any BLAS/LAPACK implementation, providing extra shared object with proper SONAMEs is necessary.\
For example, do not use [libopenblas.so.0] (SONAME=[libopenblas.so.0]) as the BLAS/CBLAS provider by simply symlinking it into [libblas.so and [libcblas.so because any program to be linked against BLAS (`-lblas`) or CBLAS (`-lcblas`) will be eventually linked against [libopenblas.so.0] (verify this with [readelf -d foobar]), which will clearly break the runtime switching mechanism. The current solution is to patch upstream build systems and build customized shared objects with proper SONAMEs.

To package a BLAS/LAPACK provider with the runtime switching feature enabled, the maintainer should pay attention to the following points:

-   Patch upstream build systems and provide extra shared objects in a private library directory. Specifically, a new BLAS/CBLAS implementation, say \"myblas\", should install 4 files to the [/usr/lib64/blas/\<myblas\>/] directory:
    1.  [libblas.so.3] (ELF shared object, providing the fortran BLAS ABI, SONAME=[libblas.so.3])
    2.  [libblas.so] (symlink pointing to [libblas.so.3]);
    3.  [libcblas.so.3] (ELF shared object, providing the C BLAS ABI, SONAME=[libcblas.so.3])
    4.  [libcblas.so] (symlink pointing to [libcblas.so.3]).
-   Similarly, a new LAPACK implementation, say \"mylapack\" should install 2 files to the [/usr/lib64/lapack/\<mylapack\>] directory:
    1.  [liblapack.so.3] (ELF shared object, providing the fortran LAPACK ABI, SONAME=[liblapack.so.3]);
    2.  [liblapack.so] (symlink pointing to [liblapack.so]).
-   Register an alternative with [eselect blas add \...] during postinst.
-   Remove an alternative with [eselect blas validate] during postrm.
-   Guard the code associated with all the above points with the `eselect-ldso` USE flag.

For real example please see the latest ebuild files for [[[sci-libs/lapack]](https://packages.gentoo.org/packages/sci-libs/lapack)[]], [[[sci-libs/blis]](https://packages.gentoo.org/packages/sci-libs/blis)[]], or [[[sci-libs/openblas]](https://packages.gentoo.org/packages/sci-libs/openblas)[]].

### [Reverse dependencies]

If a package needs to be linked against the reference (aka. netlib) BLAS and LAPACK, it should declare virtual packages dependency, i.e. `virtual/` instead of a specific implementation. In this case the package must assume a standard (reference) API and ABI from the virtual package. Otherwise, please write a specific implementation in the dependency list and avoid linking against `-lblas` or `-llapack`.

## [Implementation details]

** Important**\
The promises made here are not mandated by Netlib specifications and should not be relied on. The may be changed in future updates.\

Packages must not rely on the [libblas.so.3/libblas.so] to contain the BLAS symbols but should only assume that linking to [-lblas] will ensure symbol resolution during runtime.\

If you wish to ensure that symbols are present, they should done by linking to provider libraries, such as [libopenblas.so], [libblis.so], [libmkl_rt.so] or any other provider library.

The core part of the implementation involves `>=sci-libs/lapack-3.8.0`, `>=eselect-blas-0.2` and `>=eselect-lapack-0.2`, where the former one controls both (fortran) BLAS and CBLAS alternatives at the same time.

The [[[sci-libs/lapack]](https://packages.gentoo.org/packages/sci-libs/lapack)[]] is the code base of the reference (or standard) BLAS, CBLAS, LAPACK, and LAPACKE. BLAS and LAPACK are a set of stable Fortran API / ABI. CBLAS and LAPACKE are thin wrappers around BLAS and LAPACK respectively, providing the C API / ABI. In our BLAS/LAPACK runtime switching mechanism, every candidate must provide every API / ABI that the reference implementation provides. Taking advantage of the API/ABI stability, we can change the backend libraries (e.g. [libblas.so.3]) without recompiling applications as long as the new one provides a compatible set of ABI.

The users could easily switch the libraries by adjusting the `LD_LIBRARY_PATH` environment variables as a temporary solution. For system level library switching, two custom eselect modules ([eselect-blas], [eselect-lapack]) are provided. They manipulates configuration files under the [/etc/ld.so.conf.d/] directory, hinting [ld.so] on the places to find the BLAS/LAPACK libraries.

As a side effect, this solution depends on the [ld.so.conf] support from the system C standard library. Besides, it is recommended to read the code if you need even more details.

Code: [[[app-eselect/eselect-blas]](https://packages.gentoo.org/packages/app-eselect/eselect-blas)[]] [[[app-eselect/eselect-lapack]](https://packages.gentoo.org/packages/app-eselect/eselect-lapack)[]] [[[sci-libs/lapack]](https://packages.gentoo.org/packages/sci-libs/lapack)[]] [[[sci-libs/blis]](https://packages.gentoo.org/packages/sci-libs/blis)[]] [[[sci-libs/openblas]](https://packages.gentoo.org/packages/sci-libs/openblas)[]] [[[sci-libs/mkl-rt]](https://packages.gentoo.org/packages/sci-libs/mkl-rt)[]]

## [Frequently asked questions]

**Q: I disabled this feature when installing a bunch of packages, but now I regret and want to enable the runtime switching feature. How to accomplish this?**

A: Simply reinstall the virtual packages and your favorite BLAS/LAPACK providers with the `eselect-ldso` flag toggled. The whole dependency tree doesn't need to be rebuilt as a rebuild is expected to make no difference.

**Q: Some BLAS/LAPACK implementations support 64-bit array indexing, which provides functions such as `sasum(int64_t N, float* X, int64_t INCX)`. How does this mechanism deal with such feature?**

A: The "BLAS64" or "BLAS-ILP64" ABI is different from the "BLAS32" or "BLAS-LP64" ABI. Mixing them together will lead to unpredictable results, hence the "BLAS64" feature is not integrated into the mechanism. Currently we only provide this feature in the [[[sci-libs/openblas]](https://packages.gentoo.org/packages/sci-libs/openblas)[]] package for Julia's use. Besides, the generic switching mechanism for BLAS64/LAPACK64 is still being experimented in Debian. When the demand on "BLAS64" is common enough or the experiment in Debian was successful, we could start to provide it in Gentoo.

**Q: How to add a customized implementation into this mechanism?**

A: Taking MKL as an example. We first install MKL to [/path/to/mkl], and symlink [/path/to/mkl/libmkl_rt.so] to [/path/to/mkl/libblas.so. Then register it with [eselect blas add lib64 /path/to/mkl/ mkl]. Note that building programs when MKL is selected is discouraged. The reason could be found in the developer guide part.

A real example about adding and setting Intel MKL as the backend library:

`user `[`$`]`pip install mkl --user `

`user `[`$`]`cd ~/.local/lib/ `

`user `[`$`]`ln -s libmkl_rt.so libblas.so.3 `

`user `[`$`]`ln -s libmkl_rt.so libblas.so `

`user `[`$`]`ln -s libmkl_rt.so libcblas.so.3 `

`user `[`$`]`ln -s libmkl_rt.so libcblas.so `

`user `[`$`]`ln -s libmkl_rt.so liblapack.so.3 `

`user `[`$`]`ln -s libmkl_rt.so liblapack.so `

`root `[`#`]`eselect blas add lib64 $(pwd) mkl `

`root `[`#`]`eselect lapack add lib64 $(pwd) mkl `

`root `[`#`]`eselect blas set mkl `

`root `[`#`]`eselect lapack set mkl`

To remove the MKL candidate, or any other customized library, just remove the corresponding files under [/etc/env.d/blas/] and [/etc/env.d/lapack/] directories, then select some other candidates. Note, the [[[sci-libs/mkl-rt]](https://packages.gentoo.org/packages/sci-libs/mkl-rt)[]] package can do all the above steps for you.

## [Reference]

1.  [GSoC Project Link](https://summerofcode.withgoogle.com/projects/#6268942782300160)
2.  \[gentoo-science\] GSoC Proposal: Improvements to the BLAS / LAPACK and their reverse-dependencies [https://archives.gentoo.org/gentoo-science/message/4d0186acdce6df538a2740e0f1146ae6](https://archives.gentoo.org/gentoo-science/message/4d0186acdce6df538a2740e0f1146ae6)
3.  \[gentoo-dev\] RFC: BLAS and LAPACK runtime switching [https://archives.gentoo.org/gentoo-dev/message/d917547f7a9e1226fca63632a1e02026](https://archives.gentoo.org/gentoo-dev/message/d917547f7a9e1226fca63632a1e02026)
4.  \[gentoo-dev\] \[PATCH 0/2\] RFC: Introducing ldso switching to BLAS/LAPACK [https://archives.gentoo.org/gentoo-dev/message/95beba3dc1c0f684ce1ec82d51988fc8](https://archives.gentoo.org/gentoo-dev/message/95beba3dc1c0f684ce1ec82d51988fc8)
5.  \[gentoo-science\] On BLAS and LAPACK int64 ABI [https://archives.gentoo.org/gentoo-science/message/8e3b9567297de5a1809feb28c62be633](https://archives.gentoo.org/gentoo-science/message/8e3b9567297de5a1809feb28c62be633)
6.  Hasan ÇALIŞIR (Gentoo Proxy Maintainer) wrote an "openblas" script for similar switching purpose. However the implementation is neither generic nor simple enough. See [https://github.com/gentoo/gentoo/pull/11700/files](https://github.com/gentoo/gentoo/pull/11700/files)
7.  Zongyu Zhang [fixed a bug in numpy ebuild](https://github.com/gentoo/gentoo/commit/f5c71a4aa9615c8c14caa8e7076519ab2a4b9824#diff-e86a27d02ab70b6118a6b04d18ff075e) so that numpy could make use of the switching mechanism correctly.
8.  Some positive user feedbacks: [https://github.com/gentoo/sci/issues/805#issuecomment-510469206](https://github.com/gentoo/sci/issues/805#issuecomment-510469206) [https://github.com/gentoo/sci/issues/805#issuecomment-512097570](https://github.com/gentoo/sci/issues/805#issuecomment-512097570)

Related pull requests:

1.  [https://github.com/gentoo/gentoo/pull/12316](https://github.com/gentoo/gentoo/pull/12316)
2.  [https://github.com/gentoo/gentoo/pull/12318](https://github.com/gentoo/gentoo/pull/12318)
3.  [https://github.com/gentoo/gentoo/pull/12319](https://github.com/gentoo/gentoo/pull/12319)
4.  [https://github.com/gentoo/gentoo/pull/12322](https://github.com/gentoo/gentoo/pull/12322)
5.  [https://github.com/gentoo/gentoo/pull/12323](https://github.com/gentoo/gentoo/pull/12323)
6.  [https://github.com/gentoo/gentoo/pull/12356](https://github.com/gentoo/gentoo/pull/12356)
7.  [https://github.com/gentoo/gentoo/pull/12357](https://github.com/gentoo/gentoo/pull/12357)
8.  [https://github.com/gentoo/gentoo/pull/12358](https://github.com/gentoo/gentoo/pull/12358)
9.  [https://github.com/gentoo/gentoo/pull/12381](https://github.com/gentoo/gentoo/pull/12381)
10. [https://github.com/gentoo/gentoo/pull/12382](https://github.com/gentoo/gentoo/pull/12382)
11. [https://github.com/gentoo/gentoo/pull/12405](https://github.com/gentoo/gentoo/pull/12405)
12. [https://github.com/gentoo/gentoo/pull/12409](https://github.com/gentoo/gentoo/pull/12409)
13. [https://github.com/gentoo/gentoo/pull/12420](https://github.com/gentoo/gentoo/pull/12420)
14. [https://github.com/gentoo/gentoo/pull/12422](https://github.com/gentoo/gentoo/pull/12422)
15. [https://github.com/gentoo/gentoo/pull/12423](https://github.com/gentoo/gentoo/pull/12423)
16. [https://github.com/gentoo/gentoo/pull/12475](https://github.com/gentoo/gentoo/pull/12475)
17. [https://github.com/gentoo/gentoo/pull/12742](https://github.com/gentoo/gentoo/pull/12742)

## [Maintainers]

Author: Mo Zhou [lumin@debian.org](mailto:lumin@debian.org) GSoC Mentor: Benda Xu [heroxbd@gentoo.org](mailto:heroxbd@gentoo.org)

## [See also]

-   [Google_Summer_of_Code/2019/Ideas/BLAS_and_LAPACK_runtime_switching](https://wiki.gentoo.org/wiki/Google_Summer_of_Code/2019/Ideas/BLAS_and_LAPACK_runtime_switching "Google Summer of Code/2019/Ideas/BLAS and LAPACK runtime switching")