These instructions will allow you to run a regression test between
recent versions of Wine and very old ones (which often have trouble
compiling and/or running on modern systems). Only basic knowledge of
Linux is needed, as this guide should be very straightforward. If you
don't know a command, Google and the man pages are your friend :smiley:.

Sometimes old programs don't compile on new systems. Sometimes old
programs compile but don't work on new systems. But what if you know
that the old version of the program worked better than new one for a
particular task? This is called a regression. The fastest way to find
the cause of the regression is to do [regression
testing](Regression-Testing). But the usual regression
testing procedure will fail to work in some cases: you cannot compile
(or run) and test older versions!

This guide is based on real-world examples, so below you will find only
compile-time problems. But reverse regression testing also allows you to
find and solve run-time problems as well. For example, [on Ubuntu 7.04
versions of Wine before around 0.9.24 compile successfully but crash on
startup with segmentation
fault](https://www.winehq.org/pipermail/wine-devel/2007-June/057650.html).
This of course prevents some people from doing regression tests. But
using the instructions in this guide everyone should be able to solve
such problems by doing reverse regression test(s).

Let's examine a real-world example. We want to run a regression test
between wine-0.9 and wine-0.9.40. But we cannot compile wine-0.9 on a
modern system! Does that means we cannot do the regression test? No, we
can. But we need to do a reverse regression test first . What does
"reverse" mean? It means that if wine compiles or runs successfully -
this is a "bad" revision. If it doesn't compile or fail to run - this is
a "good" revision.

## Step 0 (optional)

This is a preliminary optional step. The system used by the author of
this howto was Debian Etch at the time of writing (if you are using
something else you may face with additional problems but you should be
able to solve all of them by following instructions in this howto). We
know that 0.9 doesn't compile on it. Let's try to compile other old
revisions - maybe they will work? For example:

```sh
$ git reset wine-0.9.10
$ git checkout -f
```

Then try to compile:

```sh
$ ./configure --verbose && make depend && make
```

Great! Now we know that wine-0.9.10 can be successfully compiled on
Debian Etch. So we now know that wine-0.9.10 compiles fine on Debian
Etch but wine-0.9 doesn't. This helps us pinpoint where we need to start
the reverse regression testing, and ultimately reducing the testing that
has to be done.

## Step 1

First, we need to start git-bisect:

```sh
$ git bisect start
```

Then we need to tell GIT that our current version (0.9.10) compiles:

```sh
$ git bisect bad wine-0.9.10
```

Then we need to choose the version that we cannot compile:

```sh
$ git bisect good wine-0.9
```

## Step 2

Now try to compile:

```sh
$ ./configure --verbose && make depend && make
```

If at the end of compilation you see:

```
Wine build complete.
```

Then the current revision compiles cleanly and you need to tell git
this:

```sh
$ make distclean; git checkout -f && git bisect bad
```

Clean up commands `make distclean` and `git checkout -f` are for sanity
(without them fatal errors may occur). If you get a fatal error when
trying to run git-bisect see troubleshooting section at the end of this
guide. If you don't see "Wine build complete." then compilation was
stopped because of errors. In this case you need to execute:

```sh
$ make distclean; git checkout -f && git bisect good
```

Be sure to note the error that occurs before compiling the next version.
If multiple compile errors may appear, you will need to run _separate_
reverse regression tests for each.

## Step 3

Go to step 2. Repeat this until you find which patch is causing wine not
to compile (make sure to remember its SHA id) and execute:

```sh
$ git bisect reset
```

## Examples

When trying to compile 0.9 first compilation error in my case was:

```sh
$ gcc -m32 -c -I. -I. -I../../include -I../../include  -DINCLUDEDIR="\"/usr/local/include/wine\"" -Wall ...
lex.yy.o lex.yy.c
lex.yy.c:2610: error: expected ';', ',' or ')' before numeric constant
make.bin[2]: *** [lex.yy.o] Error 1
make.bin[2]: *** Waiting for unfinished jobs....
```

First compile error may be different on **your** system of course. It is
irrelevant what error(s) exactly you get but it is important to make
sure to do reverse regression test against one particular error only and
ignore all other possible errors (if any). If you followed above steps
carefully and your system is similar to mine you will find that this
error is caused by lack of commit
**69dcbaaf93a65820a28fe2485b6d15a90f423899** in 0.9 (if your system is
different your result may be different too - that's OK). Using qgit it
is easy to find this patch. Select it in the tree, press Ctrl+P to open
separate window with patch content. Now press right mouse button and
choose "Select All". Then press Ctrl+C to copy whole patch. With your
favorite editor create file
[0.9-wrc-parser.diff](https://www.winehq.org/pipermail/wine-users/attachments/20071107/f0dad1e8/attachment-0007.diff)
and paste the patch into. Now go to step 0 and search for a cause of
next problem. When you face with "expected ';', ',' or ')' before
numeric constant" error again at step 2 execute:

```sh
$ patch -p1 < 0.9-wrc-parser.diff
$ ./configure --verbose && make depend && make
```

And try to compile again. If you receive another error, go back to step
2. Each iteration of reverse regression testing will give us yet another
patch. At the end we will have all patches necessary to compile the
ancient wine-0.9 on your modern system.

Sometimes patches won't apply to old revisions. Usually this isn't a big
problem. For example, I have incorporated following patches to a file
[0.9-gdi-freetype.diff](https://www.winehq.org/pipermail/wine-users/attachments/20071107/f0dad1e8/attachment-0006.diff):
**603d21cbc4fc8b915248cd3a6f90b02f721980c4**,
**0458a5e38dcf7d03a0eedd1e63922c1eb4e37cb9**. But we cannot apply this
fix to 0.9 directly. How do we solve this problem? Execute this to
choose wine-0.9 revision first:

```sh
$ git reset wine-0.9
$ git checkout -f
```

Then try to apply the patch:

```sh
$ patch -p1 < 0.9-gdi-freetype.diff
```

Fortunately, just 1 out of 6 hunks failed to apply. We now have
freetype.c.rej. Open it. As you can see it is very easy to fix this by
editing freetype.c accordingly. Save the result to
[0.9-gdi-freetype-old.diff](https://www.winehq.org/pipermail/wine-users/attachments/20071107/f0dad1e8/attachment-0004.diff)
by executing:

```sh
$ git diff > 0.9-gdi-freetype-old.diff
```

At the end of the whole process I have four patches:
[0.9-kernel-time.diff](https://www.winehq.org/pipermail/wine-users/attachments/20071107/f0dad1e8/attachment-0005.diff),
[0.9-gdi-freetype.diff](https://www.winehq.org/pipermail/wine-users/attachments/20071107/f0dad1e8/attachment-0006.diff),
[0.9-gdi-freetype-old.diff](https://www.winehq.org/pipermail/wine-users/attachments/20071107/f0dad1e8/attachment-0004.diff)
and
[0.9-wrc-parser.diff](https://www.winehq.org/pipermail/wine-users/attachments/20071107/f0dad1e8/attachment-0007.diff).
As you remember, our original goal was to do regression test between
0.9.40 and 0.9. So what now? Just proceed with regression test as usual.
When you get compile error just apply the corresponding patches and try
to compile again. It may be confusing to have multiple versions of
patches to fix similar errors
([0.9-gdi-freetype.diff](https://www.winehq.org/pipermail/wine-users/attachments/20071107/f0dad1e8/attachment-0006.diff)
and
[0.9-gdi-freetype-old.diff](https://www.winehq.org/pipermail/wine-users/attachments/20071107/f0dad1e8/attachment-0004.diff)
in this case). But actually it isn't too hard to guess what you need.
For example if you about 0.9.5 revision you need 0.9-gdi-freetype.diff",
if you about 0.9 revision you need
[0.9-gdi-freetype-old.diff](https://www.winehq.org/pipermail/wine-users/attachments/20071107/f0dad1e8/attachment-0004.diff).
Of course it is possible to apply wrong version of patch by mistake - in
this case just execute:

```sh
$ git checkout -f
```

And then apply the correct patch(es).

## Alternative method

If you need to compile very old Wine version **sometimes** it is
possible to use a faster alternative to reverse regression testing: fix
the code yourself. But this can be faster **only** if you know
**exactly** what's wrong, how to fix it and there are few lines to
change. For example, this is exactly how I created the patch
[0.9-kernel-time.diff](https://www.winehq.org/pipermail/wine-users/attachments/20071107/f0dad1e8/attachment-0005.diff):
by fixing the code manually (I just replaced old function
TIME_ClockTimeToFileTime with newer version of it taken from recent
time.c). However, if you don't know exact cause or there too many lines
to change reverse regression testing is the best and fastest option.

## Troubleshooting

If you get error like this:

```
fatal: Untracked working tree file 'dlls/advapi32/tests/.gitignore'
would be overwritten by merge.
```

Then try to run these commands:

```sh
$ git clean -d
$ git checkout -f
```

Above commands may also help in other cases. Please note that these two
commands will erase all untracked files in Wine source directory and
revert all non-committed changes to source files. This is typical and a
very useful clean up procedure so it is good practice to avoid
non-autogenerated untracked files in the directory with git-tree.
