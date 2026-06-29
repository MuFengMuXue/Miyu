[TABLE]

## Functions

|  |  |
|----|----|
| \#define | [OSTREE_CHECK_VERSION](reference__ostree-ostree-version.md#OSTREE-CHECK-VERSION:CAPS "OSTREE_CHECK_VERSION()")() |

## Types and Values

|  |  |
|----|----|
| \#define | [OSTREE_YEAR_VERSION](reference__ostree-ostree-version.md#OSTREE-YEAR-VERSION:CAPS "OSTREE_YEAR_VERSION") |
| \#define | [OSTREE_RELEASE_VERSION](reference__ostree-ostree-version.md#OSTREE-RELEASE-VERSION:CAPS "OSTREE_RELEASE_VERSION") |
| \#define | [OSTREE_VERSION](reference__ostree-ostree-version.md#OSTREE-VERSION:CAPS "OSTREE_VERSION") |
| \#define | [OSTREE_VERSION_S](reference__ostree-ostree-version.md#OSTREE-VERSION-S:CAPS "OSTREE_VERSION_S") |
| \#define | [OSTREE_VERSION_HEX](reference__ostree-ostree-version.md#OSTREE-VERSION-HEX:CAPS "OSTREE_VERSION_HEX") |

## Description

ostree provides macros to check the version of the library at compile-time

## Functions

### OSTREE_CHECK_VERSION()

``` programlisting
#define             OSTREE_CHECK_VERSION(year,release)
```

Compile-time version checking. Evaluates to `TRUE` if the version of ostree is equal or greater than the required one.

#### Parameters

|         |                          |     |
|---------|--------------------------|-----|
| year    | required year version    |     |
| release | required release version |     |

Since: 2017.4

## Types and Values

### OSTREE_YEAR_VERSION

``` programlisting
#define OSTREE_YEAR_VERSION (2026)
```

ostree year version component (e.g. 2017 if [`OSTREE_VERSION`](reference__ostree-ostree-version.md#OSTREE-VERSION:CAPS "OSTREE_VERSION") is 2017.2)

Since: 2017.4

------------------------------------------------------------------------

### OSTREE_RELEASE_VERSION

``` programlisting
#define OSTREE_RELEASE_VERSION (2)
```

ostree release version component (e.g. 2 if [`OSTREE_VERSION`](reference__ostree-ostree-version.md#OSTREE-VERSION:CAPS "OSTREE_VERSION") is 2017.2)

Since: 2017.4

------------------------------------------------------------------------

### OSTREE_VERSION

``` programlisting
#define OSTREE_VERSION (2026.2)
```

ostree version.

Since: 2017.4

------------------------------------------------------------------------

### OSTREE_VERSION_S

``` programlisting
#define OSTREE_VERSION_S "2026.2"
```

ostree version, encoded as a string, useful for printing and concatenation.

Since: 2017.4

------------------------------------------------------------------------

### OSTREE_VERSION_HEX

``` programlisting
#define             OSTREE_VERSION_HEX
```

ostree version, encoded as an hexadecimal number, useful for integer comparisons.

Since: 2017.4

------------------------------------------------------------------------
