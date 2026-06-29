[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=BLAS_and_LAPACK_Providers&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://netlib.org/blas/index.html)

[[]][Home](https://netlib.org/lapack/index.html)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Basic_Linear_Algebra_Subprograms "wikipedia:Basic Linear Algebra Subprograms")

[BLAS, CBLAS](https://netlib.org/blas/index.html), [LAPACK, LAPACKE, ScaLAPACK](https://netlib.org/lapack/index.html), etc. are standards for linear algebra libraries defined by NetLib.\
Any package implementing the *api* for **BLAS** and installing the library **libblas.so** would be a provider for **BLAS**, similarly for **libcblas.so**, **liblapack.so**, etc.

## Contents

-   [[1] [Overview]](#Overview)
-   [[2] [Potential Hazards]](#Potential_Hazards)
-   [[3] [Providers]](#Providers)
-   [[4] [GPU limitations]](#GPU_limitations)
-   [[5] [Runtime switching]](#Runtime_switching)
-   [[6] [See also]](#See_also)

## [Overview]

Gentoo provides *virtual* packages for ensuring that an implementation is present, [[[virtual/blas]](https://packages.gentoo.org/packages/virtual/blas)[]], [[[virtual/cblas]](https://packages.gentoo.org/packages/virtual/cblas)[]], [[[virtual/lapack]](https://packages.gentoo.org/packages/virtual/lapack)[]], [[[virtual/lapacke]](https://packages.gentoo.org/packages/virtual/lapacke)[]].

This ensures that during runtime one of the providers for the request virtual is going to be present.

## [Potential Hazards]

Most providers for these packages also provide their own extensions in addition to the standard library *api* demanded by NetLib.

This can create problems if a package links to **libcblas.so** but uses extra functions, let us say, defined by Intel MKL libraries, because it expects that the **libcblas.so** is the one that is provided by [[[sci-libs/mkl-rt]](https://packages.gentoo.org/packages/sci-libs/mkl-rt)[]].

This is incorrect behaviour and the packages in Gentoo should be amended so that they link with the respective named libraries instead of the standard *libblas.so*/*liblapack.so*/\...

## [Providers]

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------- ----------- ------------- --------------
  Package                                                                                                                                                                                                                                                                                                                                                                     **BLAS**   **CBLAS**   **LACPACK**   **LACPACKE**
  [[[sci-libs/lapack]](https://packages.gentoo.org/packages/sci-libs/lapack)[]]         Yes        Yes         Yes           Yes
  [[[sci-libs/openblas]](https://packages.gentoo.org/packages/sci-libs/openblas)[]]   Yes        Yes         Yes           No
  [[[sci-libs/mkl-rt]](https://packages.gentoo.org/packages/sci-libs/mkl-rt)[]]         Yes        Yes         Yes           Yes
  [[[sci-libs/blis]](https://packages.gentoo.org/packages/sci-libs/blis)[]]               Yes        Yes         No            No
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------- ----------- ------------- --------------

## [GPU limitations]

Using a GPU to do BLAS calculations might seem *very* tempting but unfortunately real life is not so simple.

BLAS has been divided into 3 levels;

-   **level 1** - *vector only* : operations which only deal with vectors and scalars
-   **level 2** - *matrix-vector* : operations between vectors and matrices
-   **level 3** - *matrix-matrix* : operations between two matrices

\
For **level 1, 2**, the cost of copying elements from CPU memory to GPU memory offsets the benefit gained from doing GPU based calculations.

There is a lot of benefit for doing **level 3** operations in the GPU as the copying cost is tiny compared to matrix multiplications.

In an ideal world, level 1 and 2 would be implemented in the library *libcpublas.so* and level 3 would be in *libgpublas.so*, which would simplify choosing the appropriate implementations for the desired functions.

## [Runtime switching]

Gentoo provides a way to mix and match these packages by using *eselect* packages to change the library during runtime.

This is part of the [Blas-lapack-switch](https://wiki.gentoo.org/wiki/Blas-lapack-switch "Blas-lapack-switch") project, which added this functionality to all provider packages.

## [See also]

-   [Blas-lapack-switch](https://wiki.gentoo.org/wiki/Blas-lapack-switch "Blas-lapack-switch")