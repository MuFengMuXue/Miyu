This Known Problems page tries to make it more clear towards our end-users which wide spread problems are currently going on in Gentoo Linux, especially with packages coming from the Portage tree. For each problem we know about, we will attempt to document why the problem is happening, which temporary fixes are available and what we are waiting for for it to be resolved; that way users can continue without waiting for certain things to happen. This isn\'t meant to replace news items, but rather list problems that aren\'t important enough to be distributed as a news item. This is a community-driven documentation effort, so it may miss things; feel free to contribute.

## Contents

-   [[1] [automake 1.13 causes aclocal to fail because AM_CONFIG_HEADER macro is obsolete]](#automake_1.13_causes_aclocal_to_fail_because_AM_CONFIG_HEADER_macro_is_obsolete)
    -   [[1.1] [Symptoms]](#Symptoms)
    -   [[1.2] [Cause]](#Cause)
    -   [[1.3] [Temporary Fixes]](#Temporary_Fixes)
    -   [[1.4] [Resolution]](#Resolution)

## [[] automake 1.13 causes aclocal to fail because AM_CONFIG_HEADER macro is obsolete]

### [Symptoms]

Merging [some packages](http://bpaste.net/show/94342/) may lead to a failure of running aclocal:

[Output]

\

     * Failed Running aclocal !
     *
     * Include in your bugreport the contents of:
     *
     *   /var/tmp/portage/app-misc/failing-package-1.2.3/temp/aclocal.out

Upon then inspecting the aclocal.out file you will find the error:

[Output]

\

    error: 'AM_CONFIG_HEADER': this macro is obsolete

### [Cause]

As documented at [changes in automake release](https://autotools.io/forwardporting/automake.html) the `AM_CONFIG_HEADER` macro has deprecated in automake 1.13 and has been replaced by `AC_CONFIG_HEADERS`. This version was in the tree for some time, but it only got recently unmasked and allowed to be used in an eclass. (The previous statement dates from April 2013.)

### [Temporary Fixes]

-   Emerge the failing packages again by appending `WANT_AUTOMAKE="1.12"` in front, this will cause them to use the previous version:

`root `[`#`]`WANT_AUTOMAKE="1.12" emerge --oneshot app-misc/failing-package`

-   Alternatively, you can temporarily mask the new automake and unmerge it if too many packages are failing because of it; don\'t forget to unmask it later.

`root `[`#`]`echo "sys-devel/automake:1.13" >> /etc/portage/package.mask `

`root `[`#`]`emerge -C sys-devel/automake:1.13`

### [Resolution]

When such a failing package occurs, people should file a bug for that package (make sure none exists already) and block [[[bug #451744]](https://bugs.gentoo.org/show_bug.cgi?id=451744)[]]; that way, maintainers can deal with the problem such that eventually all packages are fixed and then we can upgrade to the version 1.13 of automake. Make sure to provide enough details (emerge \--info) and attach the relevant files.