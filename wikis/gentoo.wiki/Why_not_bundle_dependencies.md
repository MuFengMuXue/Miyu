The intent of this page is to collect information on dependency bundling and static linking as a reference to refer upstream developers, instead of explaining the same thing repeatedly by e-mail.

Contributions to this page are welcome.

## Contents

-   [[1] [When is code bundled?]](#When_is_code_bundled.3F)
-   [[2] [Temptations]](#Temptations)
    -   [[2.1] [Comforting non-Linux users]](#Comforting_non-Linux_users)
    -   [[2.2] [Easing up adoption despite odd dependencies]](#Easing_up_adoption_despite_odd_dependencies)
    -   [[2.3] [Dependencies with unstable APIs]](#Dependencies_with_unstable_APIs)
    -   [[2.4] [Private forks]](#Private_forks)
-   [[3] [Problems]](#Problems)
    -   [[3.1] [Security implications]](#Security_implications)
    -   [[3.2] [Waste of hardware resources]](#Waste_of_hardware_resources)
    -   [[3.3] [Waste of development time downstream]](#Waste_of_development_time_downstream)
    -   [[3.4] [Potential for symbol collisions]](#Potential_for_symbol_collisions)
-   [[4] [Downstream consequences]](#Downstream_consequences)
    -   [[4.1] [Analysis]](#Analysis)
        -   [[4.1.1] [Separating forks from copies]](#Separating_forks_from_copies)
        -   [[4.1.2] [Determining versions]](#Determining_versions)
    -   [[4.2] [Patching]](#Patching)
-   [[5] [What to do upstream]](#What_to_do_upstream)
-   [[6] [See also]](#See_also)
-   [[7] [External resources]](#External_resources)

## [][When is code bundled?]

Say you develop and distribute a piece of software: a game, a library, anything.

Now, the code is considered bundled if any of the following conditions occur:

1.  Statically linking against a system library.
2.  Shipping and using your own copy of a library.
3.  Including and (unconditionally) using snippets of code copied from a library.

In other words, code bundling occurs whenever a program or library ends up containing code that does not belong to it.

## [Temptations]

There are reasons why bundling dependencies and using static linking happens occurs; there are certain benefits to it. So why is it tempting to do such a thing?

### [Comforting non-Linux users]

Especially in Windows, shipping dependencies *can* be a favor to users to save end users having to manually install dependencies or additional libraries. Without a package manager there is no real-solution to that on Windows anyway. It is tempting when using bundled code on Windows to also bundle on GNU/Linux too. It feels consistent and fits together nicely in the mind of the software author.

### [Easing up adoption despite odd dependencies]

If a software package *P* has some dependency *D* that is not yet packaged for major distributions, *D* makes it harder for *P* to get in, as packaging *P* forces the new maintainer to package *D* him/herself or to wait for someone else to package it for him/her.

Bundling *D* hides the dependency on *D* in a way: if the packager is not paying close attention *P* may even get in despite and with the bundled dependency. (It is, however, only a matter of time until someone noticed the bundling.)

### [Dependencies with unstable APIs]

If a program uses a library with a very unstable interface that often changes between minor versions, you are practically unable to produce packages which will work with each new release of that library.

Consider *ffmpeg* as a good example. Programs using it have to suffer major code changes and even rewrites due to changes in the library, and supporting more than a few successive versions is at least painful. Bundling an internal copy of ffmpeg with a particular release allows the developers to choose a single version which is known to be compatible.

Often, this problem is encountered if the developers of the library do not account for the difficulties which developers of programs using it will face.

In other cases, the particular package may be using private interfaces of the library which are not intended to be used by other packages --- and thus they are not guaranteed to be \'stable\' between releases.

### [Private forks]

If *P* uses a library *D*, the developers of *P* may wish to make some changes to *D*, for example to add a new feature, modify the API, or change the default behavior. If the developers of *D* for whatever reason are opposed to these changes, the developers of *P* may want to fork *D*. But publishing and properly maintaining a fork takes time and effort, so the developers of *P* could be tempted to take the easy road, bundle their patched version of *D* with *P*, and maybe occasionally update it for upstream *D* changes.

## [Problems]

So why is bundling dependencies and static linking bad after all?

### [Security implications]

Let\'s consider you\'re a developer of *foo* and your *foo* uses *libbar*. Now, a very important security flaw has been found in *libbar* (say, remote privilege escalation). The problem is large enough that devs of *libbar* release fixed version right away, and distributions package it quickly to decrease the possibility of break-in to users\' systems to minimum.

If a particular distribution has efficient security upgrade system, the patched library can get there in less than 24 hours. But that would be of no use to *foo* users which will still use the earlier vulnerable library.

Now, depending on how bad things are:

-   if *foo* statically linked against *libbar*, then the users would either have to rebuild *foo* themselves to make it use the fixed library or distribution developers would have to make a new package for *foo* and make sure it gets to user systems along with *libbar* (assuming they are aware that the package is statically linked);

<!-- -->

-   if *foo* bundled local copy of *libbar*, then they would have to wait till you discover the vulnerability, update *libbar* sources, release the new version and distributions package the new version.

In the meantime, users probably even won\'t know they are running vulnerable application just because they won\'t know there\'s a vulnerable library statically linked into the executables.

Examples:

-   [CVE-2016-3074](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2016-3074) has to be [fixed in PHP](https://bugs.php.net/bug.php?id=71912) (where it is bundled) after it is [fixed in libgd](https://github.com/libgd/libgd/commit/2bb97f407c1145c850416a3bfbcc8cf124e68a19) (upstream).

### [Waste of hardware resources]

Say a media player is bundling library libvorbis. If libvorbis is also installed system-wide this means that two copies of libvorbis

1.  occupy twice as much space on disk
2.  occupy (up to) twice as much RAM (of the page cache)

### [Waste of development time downstream]

Due to the [consequences](#Downstream_consequences) of bundled dependencies, many hours of downstream developer time are wasted that could have been put to more useful work.

### [Potential for symbol collisions]

If a program *P* uses a system-installed library *A* and also uses another library *B* which bundles library *A*, there is a potential for symbol collisions.

This means that *P* might use an interface, such as *my_function()* and that the *my_function()* symbol would be present in both *A* and the version of *A* bundled inside of library *B*.

If the system-installed copy of *A* and the copy of *A* compiled into library *B* are from different releases of library *A*, then the operation of the interface *my_function()* might behave differently in each copy of *A*.

Since the program *P* was compiled against the system-installed copy of *A* and for various other reasons, if *P* ends up using the *my_function()* interface from the version of *A* bundled in library *B* instead of the interface in the system-installed copy.

This can potentially result in crashes or strange unpredictable behavior.

This sort of problem can be prevented if library *B* uses symbol visibility tricks when it links against library *A*, which would cause library *B* not to export library *A\'*s interfaces.

Examples:

-   libmagic bundled with PHP ([Gentoo bug 471682](https://bugs.gentoo.org/show_bug.cgi?id=471682), [PHP bug 66095](https://bugs.php.net/bug.php?id=66095))

## [Downstream consequences]

When a bundled dependency is discovered downstream this has a number of bad consequences.

### [Analysis]

So there is a copy of libvorbis bundled with that media player. Which version is it? Has it been modified?

#### [Separating forks from copies]

Before the bundled dependency can be replaced by the system-widely installed one, we need to know if it has been modified: we have to know if it\'s a fork. If it is a fork it may or may not be replaced without breaking something. That\'s something to find out: more time wasted. If the code says which version it is we at least know what to run `diff` against; but that is not always the case.

#### [Determining versions]

If a bundled dependency doesn\'t tell its version we may have to find out ourselves. Mailing upstream could work, comparing against a number of tarball contents may work too. Lots of opportunities to waste time.

### [Patching]

Once it is clear that a bundled dependency can be ripped out, a patch is written, applied and tested (more waste of time). If upstream is willing to co-operate the patch may be dropped later. If not the patch will need porting to each now version downstream.

## [What to do upstream]

\(A\) Remove bundled dependency

\(B\) Keep bundled dependency, make usage *completely optional*

## [See also]

-   [Fedora Packaging --- Bundled Libraries](https://fedoraproject.org/wiki/Bundled_Libraries?rd=Packaging:Bundled_Libraries)
-   [[[Gentoo bug tracking packages that bundle dependencies]](https://bugs.gentoo.org/buglist.cgi?quicksearch=bundled-libs&order=bug_id%20DESC)[]]
-   [Diego Elio Pettenò: Bundling libraries for despair and insecurity (2009-01-02)](https://flameeyes.blog/2009/01/02/bundling-libraries-for-despair-and-insecurity/)

## [External resources]

-   [Michał Górny: The modern packager's security nightmare](https://blogs.gentoo.org/mgorny/2021/02/19/the-modern-packagers-security-nightmare/)