Sometimes updates to Wine, designed to fix bugs or introduce new
features, cause unexpected new problems, called regressions. Since most
users only update at new releases, hundreds of patches may be committed
before someone notices the regression. This is where regression testing
comes in.

By using the [Git source control program](https://git-scm.com/) and its
[bisect command](https://git-scm.com/docs/git-bisect) specifically,
debuggers can partially (or even fully in some cases) automate a binary
search over Wine's revision history for the exact patch that causes the
regression. For a more general article on using git and Wine together,
see [Git Wine Tutorial](Git-Wine-Tutorial); this article is
focused on regression testing.

## Before you start

### A cheap alternative?

The Wine codebase is not small and takes some time to build so if you
can pin down the problem patch by other means, you could save
significant time and effort. One possibility is that the failure has
been caught by Wine's suite of automatic [conformance
tests](Conformance-Tests). If you have some idea of which components
in Wine are failing, you can skim the automated test results for
recent builds of Wine at <https://test.winehq.org/data>.

For instance, bug #28415 was narrowed down by looking at
<https://test.winehq.org/data/tests/winmm:midi.html>. That's not often
going to be possible, but when it is, it's easier than running a real
regression test.

### Getting the source

To begin, first make sure git is installed on your system and you are
using version 1.4.1 or newer (should only be an issue with very
old/stable distros):

```sh
$ git --version
```

If git is not installed, download and install it using your
distribution's package manager. For example, to install git in Ubuntu
use:

```sh
$ sudo apt-get install git
```

To save lots of time during the regression testing, you might want to
consider installing [ccache](http://ccache.samba.org/), which can cache
some compilation steps to avoid redundant work. You can probably find
ccache using your distro's package manager. For example, on Ubuntu,
simply use:

```sh
$ sudo apt-get install ccache
```

With git and ccache installed, you should be able to
[clone](http://git-scm.com/docs/git-clone) the Wine source code to a
directory of your choice ("wine-git" is used in this page's examples)
with the following command:

```sh
$ git clone https://gitlab.winehq.org/wine/wine.git wine-git/
$ cd wine-git
```

The Wine source tree is large (hundreds of megabytes) so downloading
and initializing the repository will take some time. Now that you have
a bleeding-edge copy of the source code, we can begin testing.

### Compiling Wine

Follow the instructions at [Building Wine](Building-Wine). Just to check that the regression hasn't already been fixed in a very recent patch, you will probably want to compile the latest Wine first. This also seeds ccache and ensures that you have all the proper build dependencies. First, run the configure script inside your Wine repository with the appropriate options:

```sh
$ ./configure CC="ccache gcc" i386_CC="ccache i686-w64-mingw32-gcc" x86_64_CC="ccache x86_64-w64-mingw32-gcc" --enable-archs=i386,x86_64 --disable-tests
```

Reassigning the CC variable enables ccache by default every time you recompile, and the --disable-tests option will also save the time that would be used to compile Wine's test suite (which shouldn't be necessary for testing regressions). The [Wine TestBot](Wine-TestBot) system is usually used to check the test suite itself for regressions.

Unless you've compiled Wine before, configure will probably return some errors due to missing dependencies. With some distros, you can use the package manager to quickly install all dependencies. For example, on Debian-based distros, you can use:

```sh
$ sudo apt-get build-dep wine
```

After installing dependencies, run the `./configure` command again, and repeat this process until you receive no errors.

After a successful run of configure, the makefile in your repository should be set up properly, and you can build Wine by simply entering `make -j$(nproc)`. Compilation will take some time, depending on the speed of your hardware. Some computers take as few as 3 minutes, while some may take hours, though 20 to 40 minutes seems about average. Running `make install` after compiling is **not recommended**. Not only will it cause conflicts in your system as you test different versions of Wine over the course of the bisection, but it will interfere with any stable version of Wine you already have installed.

Once Wine finishes compiling, you'll want to test for the bug. To be
safe, test with a clean .wine directory, which can be done by either
backing up the existing wine directory or switching to a new wineprefix
(if using a different wineprefix, remember that the wine directory
resets to default once you end the terminal session):

```sh
$ mv ~/.wine ~/.wine-backup
```

or

```sh
$ export WINEPREFIX="$HOME/.wine-test"
```

**Note:** Some bugs can be suppressed simply by giving a program a fresh
.wine directory of its own.

Now, install your application from scratch, and make sure that you're
running the git version of Wine by invoking it with a full path:

```sh
$ wine-git/wine program_install.exe
```

instead of just

```sh
$ wine program_install.exe
```

Finally run your installed program (again making sure to invoke the
built-from-source version of Wine):

```sh
$ ./wine 'C:\Program Files\Program Name\program.exe'
```

Hopefully, your bug has been already fixed, in which case you can use
the git version to run your program until the next release. If not, you
will have to run the bisection to pin down the cause of the regression.

### Regressions between wine-staging versions

Because wine-staging is a set of constantly rebased patches applied on
top of upstream, it can't be bisected in the same way as upstream wine.
For instructions on bisecting between wine-staging versions, see
[Regressions between Staging versions](https://gitlab.winehq.org/wine/wine-staging/-/wikis/home#regressions-between-staging-versions).
The basic process will probably be similar to the instructions on this
page, but the details may differ.

## Running the bisection

### Preliminary notes

If you don't remember which version of Wine you were using when the
program last worked, you can try finding it by installing archived
binary packages of Wine (e.g. from
<https://wine.budgetdedicated.com/archive/index.html>). Eliminating as
many early versions of Wine from the bisection as possible allows
testing a smaller set of revisions. It can also help you avoid building
very old versions of Wine, which are a headache to compile due to major
changes in Wine's design and dependencies.

Also, you don't need an internet connection while doing the regression
test. The bisection will run entirely within your local git repository.

### Walkthrough

Suppose that you have a bug that was introduced when upgrading from Wine
0.9.36 to Wine 0.9.37 (these numbers are release tags; for a list of
release tags in use, see
[here](https://gitlab.winehq.org/wine/wine/-/tags)). The following
command will set up git to test for your bug between these releases:

```sh
$ git bisect start
$ git bisect good wine-0.9.36
$ git bisect bad wine-0.9.37
```

Sometimes, however, you may know exactly which component the bad patch
was in, if so, you can tell git. Omitting the tag parameters from the
`bad` and `good` commands respectively tells git that the most
recent version is broken (very likely) and that even the earliest
revision should be tested (not recommended, see notes above). For
example, to tell git that the problem is in the wined3d dll component,
and the problem wasn't present in Wine 0.9.38 but is in the current
version, use:

```sh
$ git bisect start -- dlls/wined3d
$ git bisect good wine-0.9.38
$ git bisect bad
```

Git will then tell you the number of commits that will be tested in the
interval. Don't worry if it seems large, it won't take that many tests
:-). Git will revert the source to the version between the two
end-points (`good` and `bad`). For example, if you have 100 commits
to test, it will position the source at the 50th commit. At this point
you will recompile the Wine source code with `make`. While it
shouldn't always be necessary to rerun `./configure` too, if you want to
be safe (which might be good if you're testing over a large interval),
you can run both in one command:

```sh
$ ./configure --verbose && make
```

If the version you are testing fails to compile (or cannot be tested for
some other reason), enter:

```sh
$ git bisect skip
```

Then try running `make` again. Repeat this as many times as necessary
until Wine successfully compiles. This can particularly cause problems
with old versions of Wine because of changes to freetype ([this mailing
list
discussion](https://www.winehq.org/pipermail/wine-patches/2008-September/060764.html)
explains why and includes a patch).

Once you've successfully recompiled Wine, run your program and test for
your bug. If the bug is still present, you know that the problems
started somewhere among the older 50 patches, not in the newer 50. To
tell that to git, issue the command:

```sh
$ git bisect bad
```

If the bug wasn't present, you know that the regression was caused by
one of newer 50 patches. To tell that to git, issue the command:

```sh
$ git bisect good
```

These commands tell git to ignore the half of the interval that does not
need testing, then reposition the source code at the midpoint of the
remaining patches. At this point, you simply need to continue repeating
the process, recompiling Wine, testing for the bug, then notifying git
whether the bug was present or not. After a few tests, git will
eventually identify the bad patch, and output something like this:

```
a460a2df43aa8eae10b1db028c6020829b009c54 is first bad commit
commit a460a2df43aa8eae10b1db028c6020829b009c54
Author: Stefan Doesinger <stefandoesinger@gmx.at>
Date:   Sat Jun 9 14:27:41 2007 +0200
wined3d: Store the gl information in a per adapter structure and initialize it only once.
:040000 040000 d8ae35832fcdbca8de07acae73b9e21564ced413
1720cc38fb598110071c9ee4f21f8f61b6f764c3 M      dlls
```

**If you do not see a message telling you the hash of the first bad
commit, but something like this instead:**

```
Bisecting: 0 revisions left to test after this
```

**you are not done yet**. This message means you have pinpointed a
specific patch but still need to test if it is the last good or first
bad commit so compile and test one more time.

If all you get are "good" tests (the bug fails to show), git's final
output may have a line reading "Release x.x.xx" and look like this:

```
b821e839bb33ac8f56939cc582010ecf4d9c25d4 is first bad commit
commit b821e839bb33ac8f56939cc582010ecf4d9c25d4
Author: Alexandre Julliard <julliard@winehq.org>
Date:   Fri Mar 21 16:41:33 2008 +0100
    Release 0.9.58.
:100644 100644 9123c03a3138b05cb8ebb5271f554bb76510cd09 3b88d88dcdfc8e148f8e7e0858bf0ca62c0bdff3 M  ANNOUNCE
:100644 100644 900c8932cb5aad58e928a5c3192ab95967dc0664 e001d501bec609c31c5a91ab185a06ef1662f4c8 M  ChangeLog
:100644 100644 5614cdd9b3c6af6d44027f067fcc423e49c49c91 36e035642c055736e2f833210f5db334a6706486 M  VERSION
:100755 100755 a516335cb3e4c67298f285adbdb2ede09da133be 51a9fd0b9741b28a588e2dd3bb57ae2be8805af2 M  configure
```

This probably means the regression actually occurs outside of the
interval you've given. This particular output is just a version tag,
meaning that no real code was changed (and cannot have made your problem
appear). You will need to reset your bisection (see below) and use that
"Release x.x.xx" as your first `good` bisect (wine-x.x.xx).

### Contact the developer

Once you have identified which patch is causing the regression, post the
information to any bug reports in [bugzilla](https://bugs.winehq.org)
(enter a new report if one hasn't already been filed). Also, be sure to
**CC the author of the patch** when you post to the bug report. This
will allow the developers to fix the problem much quicker.

### Resetting the bisect

Once you've finished with a test, you may want to check something else
or simply use the latest git version. If you try to start a new
bisection before resetting, git-bisect will fail with "won't bisect on
seeked tree." Also, the bisection process causes git to leave your
branches so to reset your git repository and return to the default
branch, use:

```sh
$ git bisect reset
$ git checkout master
```

## Working with developers

### Reverting the patch

If the bisect identifies a patch that a developer believes is harmless,
you may be asked to check your result by reverting that patch. First,
reset your bisect if you haven't already, then use the revert command
with the SHA1 ID of the bad patch. The `-n` flag avoids committing the
reversion:

```sh
$ git revert -n b821e839bb33ac8f56939cc582010ecf4d9c25d4
```

Rebuild Wine and test your program again. When you're done testing, be
sure to reset your tree to the latest Wine commit:

```sh
$ git reset --hard HEAD
```

### Patching your git tree

Now suppose a developer posts a new patch that they want you to test.
Though this may seem overwhelming, it's quite simple. Simply download
the patch (likely from Bugzilla, or possibly from e-mail) and copy it to
the top-level directory of your git repository. Then run:

```sh
$ git apply patch_name.diff
```

This will patch the source code and if successful, should output a
confirmation listing the directories that have been message.

See, wasn't that hard! Now if you're going to be testing any other
programs, you don't want your tree cluttered with patches you were
testing for another program. To undo **all** patches to your git tree,
run:

```sh
$ git reset --hard origin
```

This will reset all commits you've made, but this shouldn't be an issue
if you're only testing and not developing patches of your own.

### Updating your git tree

Let's assume that some time has passed, and a bug you've been following
is now reported to work in the latest source version of Wine. If you
want to test this, you need to update your git repository and compile
the new version. Updating consists of two steps, first downloading any
new patches, then syncing your local repository to point to the latest
revision:

```sh
$ git fetch
$ git rebase origin
```

Once that's done, just compile Wine again and test. If there was a fix
for your bug in one of the new patches, your program should now work!

## Other ideas

### Automating the bisection

If the regression is something easily scripted (e.g. a broken compile, a
program that crashes without any user interaction, etc.), you can use a
script to automate git-bisect. For instance, if 'winetricks dotnet11'
crashes for you in 1.1.44, but not 1.1.43, you would setup the bisection
interval like normal, but then run a script:

```sh
$ git bisect start
$ git bisect good wine-1.1.43
$ git bisect bad wine-1.1.44
$ git bisect run ./foo.sh
```

The script foo.sh should look something like:

```sh
#!/bin/sh
./configure --disable-tests || exit 125
make || exit 125
rm -rf $HOME/.wine || exit 125
WINE=$HOME/wine-git/wine winetricks -q dotnet11
```

The key point is that git decides what to do at each step based on error
codes. The script should exit with a non-zero status for a failure, and
with zero for success. If Wine fails, it will pass the error code for
you, but all other steps in the script should exit with 125 on failure.
Error code 125 tells git to skip a patch instead of registering it as
"bad."

### Testing a broken compile

If the regression you're testing for is a broken compilation, it should
be easy to automate the bisection as shown above. One major difference
is that you should not pass error code 125 if make fails (because you
want to mark compiler failures, not skip them):

```sh
#!/bin/sh
./configure --disable-tests || exit 125
make
```

### Disabling optimization to speed up compilation

When compiling Wine, a large portion of the build time is spent
optimizing code. Unless you're testing for performance issues, this
becomes unnecessary when running a bisection. You might be able to speed
up compilation substantially by skipping optimization. This can be done
by passing a few flags to \`configure\` on the command line, like so:

```sh
$ CC="ccache gcc" CFLAGS="-g -O0" ./configure --verbose
```

### Disabling tests to speed up compilation

When building a plain vanilla version of Wine from source, compiling the
test suite also takes up a good deal of time. While these tests are
invaluable for development, they are not needed for regression testing
(we already know something broke, so conformance is irrelevant).

Alexandre Julliard committed a
[patch](35078f4b57523d4afe00d01da9afb9cbe2c37dba)
that allows one to disable building the test suite when regression
testing. For Wine 1.1.9 and above, you can simply pass the
`--disable-tests` flag to configure:

```sh
$ ./configure --disable-tests
```

If your last known "good" version is older, a small hack is needed. This
patch works for versions of Wine up to around 1.1.3:

```diff
diff --git a/dlls/Makefile.in b/dlls/Makefile.in
index d7b0976..2b4b779 100644
 --- a/dlls/Makefile.in
+++ b/dlls/Makefile.in
@@ -332,7 +332,7 @@ SUBDIRS = \
        winequartz.drv \
        winex11.drv
-BUILDSUBDIRS   = $(BASEDIRS) $(EXTRADIRS) $(TESTSUBDIRS)
+BUILDSUBDIRS   = $(BASEDIRS) $(EXTRADIRS)
 INSTALLSUBDIRS = $(BASEDIRS) $(EXTRADIRS) $(IMPLIBSUBDIRS)
 DOCSUBDIRS     = $(BASEDIRS) $(EXTRADIRS)
diff --git a/programs/Makefile.in b/programs/Makefile.in
index 3c128e1..72dbdb8 100644
--- a/programs/Makefile.in
+++ b/programs/Makefile.in
@@ -41,7 +41,6 @@ SUBDIRS = \
        winemenubuilder \
        winemine \
        winepath \
-       winetest \
        winevdm \
        winhelp \
        winver \
--
1.4.4.2
```

If you're testing Wine versions between 1.1.3 and 1.1.9, use this patch
instead:

```diff
diff --git a/dlls/Makefile.in b/dlls/Makefile.in
index 6680673..e998a38 100644
--- a/dlls/Makefile.in
+++ b/dlls/Makefile.in
@@ -9,9 +9,8 @@ INSTALLDIRS = $(DESTDIR)$(dlldir)
 DLLSUBDIRS     = @ALL_DLL_DIRS@
 IMPLIBSUBDIRS  = @ALL_IMPLIB_DIRS@
-TESTSUBDIRS    = @ALL_TEST_DIRS@
-SUBDIRS        = $(DLLSUBDIRS) $(IMPLIBSUBDIRS) $(TESTSUBDIRS)
-BUILDSUBDIRS   = $(DLLSUBDIRS) $(TESTSUBDIRS)
+SUBDIRS        = $(DLLSUBDIRS) $(IMPLIBSUBDIRS)
+BUILDSUBDIRS   = $(DLLSUBDIRS)
 INSTALLSUBDIRS = $(DLLSUBDIRS) $(IMPLIBSUBDIRS)
 DOCSUBDIRS     = $(DLLSUBDIRS)
@@ -445,8 +444,6 @@ CROSS_IMPLIBS = \
        wsock32/libwsock32.a \
        wtsapi32/libwtsapi32.a
-$(TESTSUBDIRS:%=%/__crosstest__): $(CROSS_IMPLIBS)
-
 implib: $(IMPORT_LIBS)
 .PHONY: implib
diff --git a/programs/Makefile.in b/programs/Makefile.in
index 7bd60b2..e5edef4 100644
--- a/programs/Makefile.in
+++ b/programs/Makefile.in
@@ -38,7 +38,3 @@ install install-lib:: install-progs$(DLLEXT) $(INSTALLDIRS)
 uninstall::
        -cd $(DESTDIR)$(bindir) && $(RM) wineapploader $(INSTALLPROGS)
        -rmdir $(DESTDIR)$(dlldir)
-
-# Rules for testing
-
-check test:: $(SUBDIRS:%=%/__test__)
diff --git a/programs/winetest/Makefile.in b/programs/winetest/Makefile.in
index d153c04..3dd7bcd 100644
--- a/programs/winetest/Makefile.in
+++ b/programs/winetest/Makefile.in
@@ -21,10 +21,6 @@ SVG_SRCS = winetest.svg
 @MAKE_PROG_RULES@
-ALL_TEST_DIRS = @ALL_TEST_DIRS@
-
-TESTBINS = $(ALL_TEST_DIRS:%/tests=%_test.exe)
-
 @ALL_WINETEST_DEPENDS@
 # Special rules
--
1.5.3.6
```

However, care must be taken when using these patches. Git doesn't like
you editing the tree in the middle of a bisection. So to disable tests
while bisecting old versions of Wine, use this little trick everytime
you recompile Wine in the bisection:

```sh
$ git apply disable_test_patch.diff && CC="ccache gcc" ./configure && make depend && make && git apply -R < disable_test_patch.diff
```

Test your app and use the git-bisect `good` and `bad` commands as
usual. The alternate recompilation command applies one of the patches
above (be sure to download the proper one and invoke it with the name
you saved it under), compiles Wine, then reverses the patch, leaving git
none the wiser.

## Troubleshooting

If you are having problems with regression testing, you might want to
try double-checking the [git documentation](https://git-scm.com/docs/)
first of all. Another possibility is asking for help on the
[\#winehackers](irc://irc.libera.chat:6697/#winehackers) channel on
[IRC](IRC). If you are particularly having trouble compiling or
running an older version of Wine, odds are the instructions in
[Reverse Regression Testing](Reverse-Regression-Testing) will be able
to help you.

## See Also

- You can see a list of regressions that haven't been bisected and how
  many regressions different developers have pinpointed
  [here](https://source.winehq.org/regressions).
- [Reverse Regression Testing](Reverse-Regression-Testing)
