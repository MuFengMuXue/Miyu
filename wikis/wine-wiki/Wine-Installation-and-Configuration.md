<small>
&nbsp;[:flag_fr: Français](fr/Wine-Installation-and-Configuration)
</small>

-----

## Installing Wine

Before you install Wine, make sure that there is no previous Wine
installation on your system, either from a package or from source. If
you haven't yet installed Wine, you should be fine. Many Linux
distributions come with an included Wine package, but due to Wine's
rapid development rate these are usually old and often broken versions.
It is best to uninstall your distribution's included package versions
and update to the latest Wine version available here.

Links to binary packages for Wine for some of the major distros can be
found at the [WineHQ downloads page](Download). In addition, full
source code is available for both the current Wine development tree
and every Wine release [here](Download#wine-source-downloads). For
help with installing from a package or from source, please consult the
[Getting Wine](Wine-User's-Guide#getting-wine) chapter of the User's
guide.

## How to help get applications working in Wine

If you want to help get an application working in Wine, the first thing
you should do is register yourself in the
[AppDB](https://appdb.winehq.org/) and fill out a test report, so others
know what works/doesn't work. Also, be sure to vote for your favorite
application so developers know where to concentrate their efforts.

If the application that you want working is not listed in the
[AppDB](https://appdb.winehq.org/) there is an easy to use form available
for you to add it. If the application is in the database, but lacks a
maintainer, you should consider volunteering. If you are familiar with
Wine, own a legal copy of the application, and have a desire to test it,
help get or keep it working, and help other users, please apply by
clicking the link in the application's page. Each application should
have a supermaintainer, and, if different versions of the application
are substantially different (such as in Adobe Creative Suite), each
subversion should have a maintainer.

If you are the developer or publisher of the application, you obviously
have a very big incentive to help get your application working under
Wine. Fortunately, there are many options available to you other than
reporting bugs and hoping someone will fix them. By far the easiest way
is to file a bug at [Bugzilla](https://bugs.winehq.org/), along with a
small testcase to add to the Wine [test
suite](Conformance-Tests). Another options is to send copies
of your software to Wine developers and hope they'll take an interest in
getting it working. An alternative option, perhaps more effective,
albeit expensive, is to pay Wine developers for their work on your
application, either directly through a negotiated contract or indirectly
by posting a bounty. CodeWeavers, a major Wine developer, offers a
special section for pledges at [their compatibility
center](https://www.codeweavers.com/compatibility/) website. The most
direct method, however, is to help develop Wine itself and contribute
code directly, which is exactly what Corel did for WordPerfect several
years ago. In any case, making a post on the Wine developers [email
list](Forums) can go a long way.

## If your application doesn't work

If your application experiences problems in a particular area, or fails
to even run at all, there are a number of steps you can take to help us.
The most important thing is to find out where exactly the application is
failing. To diagnose application problems, the first step is to run the
program from the console using Wine, rather than from a GUI shortcut.
This will allow Wine to output error messages to the console, the
understanding of which are key to solving the problem and getting the
application to work.

An application may not work because Wine doesn't yet fully implement
one of the DLL files the application is trying to use. If you
encounter a DLL not found error, or see a lot of "FIXME:" messages
while running the application in Wine, this is likely the case. When
this occurs, you can try using native (non-Wine) DLL files in place of
Wine's builtin ones.  Check the AppDB page for the program. There may
be special configuration options or instructions for installing native
DLL files there that you can try to get the application working. For
further configuration help, please see the [Running
Wine](Wine-User's-Guide#running-wine) section of the User Guide.

If the application still doesn't work, it's probably due to a bug or
deficiency in Wine and we'd like to hear about it. Please see the
[reporting bugs](Bugs) page for instructions on how to best
report bugs with applications. Alternatively, if you're a programmer,
we'd really like it if you tried to help us directly; please check out
the primary [Developers](Developers) page and the [Developer
Hints](Developer-Hints) if you're interested.

## If your application does work, but with some difficulty

Sometimes, applications run under Wine but don't function quite as
smoothly as they do in windows. They may have display errors, a feature
may be broken, or they may run unusually slow. These applications should
receive a lower rating from their maintainers ("bronze" or "garbage") in
the Application's Database, depending on the degree of difficulty
encountered.

If you have found a way to make an application work that is more
complicated than simply installing it, please share that information by
posting on the application's page in the database. If you are the
maintainer for the application, please post the instructions in a
"howto" which will appear inside green bars at the top of the
application's page.

## If your application used to work, but has since broken in a new version of Wine

Wine is a large and complex project, composed of many files written by
different authors. Sometimes, an attempt to change a file and expand
support for one application will unexpectedly cause another application
to stop functioning. These changes are known as regressions, and they
are unfortunately sometimes found in the Wine source code because the
author of a patch that causes a regression is unaware of it. Since the
Wine developers can't possibly test every application with every patch,
we have to rely on the community to inform us of when regressions occur
so that the problem can be easily identified and ultimately fixed.
Without community involvement, regressions can go unfixed for
potentially very long periods of time.

If your application has experienced a regression, please try and provide
us with as much information as you can about when and how it broke. This
allows us to isolate the exact thing we screwed up in the code and
provide a fix. Please provide as much as you know about which version of
Wine worked, and which version didn't, including the version number and
how you installed it (from source, binary packages, etc.) Finally,
please post these things in a bug.

If possible, you should also try to isolate the exact patch which broke
your application. This takes quite a bit of time, but minimal effort and
computer skills, and it is the best way to get your application working
again. When it comes to fixing regressions, the only thing more helpful
to the Wine developers than knowing exactly which patch caused a
regression is receiving a fix for the patch itself. For help with
isolating problem patches, please see the documentation on [Regression
Testing](Regression-Testing).
