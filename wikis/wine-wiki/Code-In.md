Wine may join the next [Google Code-In](https://codein.withgoogle.com/),
so this page is for collecting potential tasks.

## Code: Tasks related to writing or refactoring code

### Add one more REG.exe option: [Bug 19533](#19533) (split this into the single options)

According to #19533
Wine misses the reg.exe option "COPY".
Have a look at the source at: https://gitlab.winehq.org/wine/wine/-/tree/HEAD/programs/reg
and send a patch which adds this option

According to #19533
Wine misses the reg.exe option "SAVE".
Have a look at the source at: https://gitlab.winehq.org/wine/wine/-/tree/HEAD/programs/reg
and send a patch which adds this option

According to #19533
Wine misses the reg.exe option "RESTORE".
Have a look at the source at: https://gitlab.winehq.org/wine/wine/-/tree/HEAD/programs/reg
and send a patch which adds this option

According to #19533
Wine misses the reg.exe option "LOAD".
Have a look at the source at: https://gitlab.winehq.org/wine/wine/-/tree/HEAD/programs/reg
and send a patch which adds this option

According to #19533
Wine misses the reg.exe option "UNLOAD".
Have a look at the source at: https://gitlab.winehq.org/wine/wine/-/tree/HEAD/programs/reg
and send a patch which adds this option

According to #19533
Wine misses the reg.exe option "COMPARE".
Have a look at the source at: https://gitlab.winehq.org/wine/wine/-/tree/HEAD/programs/reg
and send a patch which adds this option

According to #19533
Wine misses the reg.exe option "EXPORT".
Have a look at the source at: https://gitlab.winehq.org/wine/wine/-/tree/HEAD/programs/reg
and send a patch which adds this option

### Fix a WineHQ Website/Bugzilla/AppDB bug

WineHQ is our development infrastructure with a web presentation, bug tracker, application compatiblity database and more.
Still there are bugs and we want you to fix one of them.
You can find the code in one of the projects here: https://gitlab.winehq.org/winehq/
And a list of bugs here: https://bugs.winehq.org/buglist.cgi?bug_status=UNCONFIRMED&bug_status=NEW&bug_status=ASSIGNED&bug_status=STAGED&bug_status=REOPENED&product=WineHQ%20Apps%20Database&product=WineHQ%20Bugzilla&product=WineHQ.org

## Documentation/Training: Tasks related to creating/editing documents and helping others learn more

### Document the install procedure for Wine on Linux Mint at [our download page](Download/) (see discussion/talk page)

### Do a Video about compiling Wine on a Linux machine

Compile Wine on your Linux machine, at best with as much dependencies as possible.
Take a Video of it with e.g. SimpleScreenRecorder or Kazam and share it online on a popular video-sharing website

## Outreach/Research: Tasks related to community management, outreach/marketing or studying problems and recommending solutions

### Make a social network post about your best running application in Wine

Try your favorite applications in Wine and post about the best running one on a social network with a screenshot showing that it runs in Wine.

### Do an updated slideshow possibly based on [one from Dan Kegel](https://kegel.com/wine/cebit2009/talk.pdf)

### Do a Video about running an Application in Wine

Run a application in recent Wine version, pick one where you think others could be interested in especially this Windows application.
Take a Video of it with e.g. SimpleScreenRecorder or Kazam and share it online on a popular video-sharing website

### Add a new Application to the AppDB

Have a look for applications you use which are not yet listed in the Wine AppDB at https://appdb.winehq.org/
Run one of those applications in a recent Wine version and add the application entry with your test results to the AppDB

### Add a new Testreport to an existing Application in the AppDB

Have a look for applications you use which are listed in the Wine AppDB at https://appdb.winehq.org/
Run one of those applications in a recent Wine version and add your test results to the AppDB

### Make a list of suggestions how Wine could be presented on [OpenHatch](https://openhatch.org)

## Quality Assurance: Tasks related to testing and ensuring code is of high quality

### Run a git bisect on a regression on the lower part of <https://source.winehq.org/regressions>

At WineHQ our regressions are tracked at https://source.winehq.org/regressions
At top are regressions which are already tracked down to a specific commit
and on the bottom there regressions which need a git bisect to track down the commit which caused it.
There are [instructions](Regression-Testing) on how to do that.

### Test old Wine bug in current Wine Version

Wine has lots of bug reports which get older and older without receiving an update,
one needs to download that application and test it in the latest version of Wine.
Here you can find bug reports not touched for a year which have a download link:
https://bugs.winehq.org/buglist.cgi?cmdtype=dorem&list_id=542286&namedcmd=1y%20old%20%2B%20download&remaction=run&sharer_id=4672

## User Interface: Tasks related to user experience research or user interface design and interaction

None yet.

## Old task we don't want to use anymore

Those tasks don't provide much benefit for Wine, but cause a lot of work
for maintainers. The new focus of Code-In for Wine should be outreaching
to get new Users by showing them what Wine could do and potential new
developers by letting them code

### Run [winetest](Conformance-Tests) on a Linux machine

Wine builds a set of unit tests that check the behavior of a large portion of the Windows API.
You can get it here at the bottom: https://test.winehq.org/data/
You can run it according to: [Conformance Tests](Conformance-Tests#running-winetest-in-wine)

### Run [winetest](Conformance-Tests) on a BSD machine

Wine builds a set of unit tests that check the behavior of a large portion of the Windows API.
You can get it here at the bottom: https://test.winehq.org/data/
You can run it according to: [Conformance Tests](Conformance-Tests#running-winetest-in-wine)

### Run [winetest](Conformance-Tests) on a Mac OS X machine

Wine builds a set of unit tests that check the behavior of a large portion of the Windows API.
You can get it here at the bottom: https://test.winehq.org/data/
You can run it according to: [Conformance Tests](Conformance-Tests#running-winetest-in-wine)

### Run [winetest](Conformance-Tests) on a Windows machine

Wine builds a set of unit tests that check the behavior of a large portion of the Windows API.
You can get it here at the bottom: https://test.winehq.org/data/
You can run it according to: [Conformance Tests](Conformance-Tests#running-winetest-on-windows)
