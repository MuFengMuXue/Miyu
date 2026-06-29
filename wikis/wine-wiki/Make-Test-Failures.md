## Build and run Winetest to upload fresh results

See [Conformance Tests](Conformance-Tests) for information on running
the test suite.

## Known Good Window Managers

Message-sequence tests usually fail because of window manager bugs.
Alexandre has been working with window manager developers to get these
fixed. At the moment, known good window managers are:

- metacity 2.23.8 or later (see
  <https://bugs.winehq.org/show_bug.cgi?id=9916#c69> for how to build and
  run that)
- fvwm 2.5.26. (Alexandre says: "fvwm 2.4.20 may also work on 32-bit,
  the bug I fixed was for 64-bit platforms".)
- KDE in Gutsy seems to be ok, too, though Alexandre hasn't blessed it

So - if you are seeing message sequence failures, check to see if
switching to one of the above window manager versions helps.

## Known Good Graphics Cards

The only graphics cards known to pass all d3d9 tests are Nvidia GeForce
6 and higher. (Note: a few TODO's are expected, that's ok.) For
instance, here are lspci strings of cards that have passed the tests:

- nVidia Corporation G70 \[GeForce 7600 GT\] (rev a1)
- nVidia Corporation G80 \[GeForce 8800 GTX\] (rev a2)
- nVidia Corporation NV40 \[GeForce 6800\] (rev a1)
- nVidia Corporation NV41GL \[Quadro FX 1400\] (rev a2)
- nVidia Corporation GeForce 9800 GTX+ (rev a2)

ATI cards are known to fail the tests due to bugs like

- <https://ati.cchtml.com/show_bug.cgi?id=1031>
- <https://ati.cchtml.com/show_bug.cgi?id=1030>

ATI is willing to fix bugs that affect games badly, but aren't eager to
fix conformance test failures that don't correspond to a bug in a
popular game.

## Flaky tests

[patchwatcher](https://code.google.com/p/winezeug/source/browse/trunk/patchwatcher/patchwatcher.sh#63)
ignores failures in the a number of tests because they seem to fail
intermittantly. The blacklist as of 27 Aug 2008 is:

- comctl32:tooltips.c
- d3d9:device.c
- d3d9:visual.c
- ddraw:visual.c
- kernel32:thread.c
- urlmon:protocol.c
- urlmon:url.c
- user32:msg.c
- user32:input.c
- user32:monitor.c
- wininet:http.c

More flaky tests:

- ole32:marshal.c - random timeout, crash or success
- ole32:clipboard.c - even after fix in 1.1.31
- oleaut32:tmarshal.c and likely some more ole\* tests
- winmm:wave - sometimes `waveOutGetPosition(0): returned 10787 samples
  (10787 bytes), should be 22050 (22050 bytes)`, followed by
  `SMPTE/MIDI/TICKS test failed`

Some tests fail with WINEDEBUG set. A few of these are a WONTFIX:

- crypt32:sip.c - +relay - "+relay adds a wrapper around functions, so
  it's normal that addresses no longer match." - [Alexandre Julliard](@julliard)
- rpcrt4:cstub.c - +relay - "Functions pointers are changed by +relay,
  same issue as bug 17517." - [Alexandre Julliard](@julliard)
- user32:class.c - +relay - "Functions pointers are changed by +relay,
  same issue as bug 17517." - [Alexandre Julliard](@julliard)

## Known bugs

We currently have a couple general bugs related to "make test" failures
on Wine:

- ~~bug #9916~~: "make test" usually fails
- ~~bug #12074~~: The conformance tests fail on Windows
- bug #7915: Wine tests fail on Mac OS X
- ~~bug #7645~~: Wine tests fail under FreeBSD and other problems

As well as several specific failures:

- ~~bug #10221~~: d3d9: visual.c:8694: Test failed: TSSARGTEMP test returned color 0x00ff0000,
  expected 0x00FFFF00
- bug #19183: d3d9: visual flakey test failures
- ~~bug #12730~~: gdi32: some tests fail when X is run in 16 bit mode,
  but not 32 bit fails
- ~~bug #12768~~: gdi32: metafile.ok fails in a virtual desktop
- ~~bug #12925~~: d3d8: Visual test fails
- ~~bug #17416~~: urlmon: url sometimes fails wit 2 errors

and several platform-specific failures (hmm, maybe we went a bit
overboard with bug reports here):

- bug #12840: kernel32: change.ok test fails in PC-BSD but not Linux
- bug #12854: ntdll: change.ok test fails in PC-BSD and OS X but not Linux
- ~~bug #12858~~: winmm: wave.ok test fails in PC-BSD but not Linux
- bug #12891: ntdll: exception.ok test fails in PC-BSD, Solaris and OS X but not Linux
- ~~bug #12894~~: kernel32: thread test fails in PC-BSD but not Linux
- ~~bug #12896~~: kernel32: pipe.ok hangs in PC-BSD but not Linux
- ~~bug #13230~~: msi: msi.ok fails in Opensolaris
- ~~bug #15538~~: gdi32: path.ok test succeeds in todo block in PC-BSD and OS X

## Automated test reports

See also [Conformance Tests](Conformance-Tests) for how to look at or
contribute to the automated test result reporting system.

When you run the 'dotests' script, your results should show up at
<https://test.winehq.org> within a few seconds.

You can use the perl script <https://kegel.com/wine/skipgood.txt> to
ignore tests which pass everywhere. Its output for wine-1.0-rc2 as of
May 24 is at <https://kegel.com/wine/failing-1.0-rc2.html> . The skipgood
script above now also tallies tests by how many people they fail for;
see below.

## Most Common Failures on XP

As of 2011/08/24, the tests that fail the most on machines running XP
are:

```
gdi32:font urlmon:protocol urlmon:url user32:cursoricon ws2_32:sock
```

## Most Common Failures on Wine

As of 1.0-rc2, here are the tests that fail on some Wine systems, and
how many people they fail for:

```
14 user32:msg
12 user32:win
9 user32:input
6 dsound:ds3d dsound:ds3d8 kernel32:path user32:monitor
5 kernel32:process msi:install msi:package riched20:editor
4 comctl32:listview ddraw:visual dinput:device gdi32:font gdi32:metafile kernel32:profile kernel32:sync kernel32:virtual snmpapi:util urlmon:protocol user32:class wininet:internet
3 comctl32:monthcal ddraw:d3d kernel32:volume msi:msi setupapi:devinst shell32:shlfolder user32:menu userenv:userenv
2 advapi32:registry advapi32:security advapi32:service comctl32:tooltips d3d8:visual d3d9:visual ddraw:dsurface dsound:dsound kernel32:version msvcrt:time ntdll:exception psapi:psapi_main qedit:mediadet
1 advpack:advpack advpack:install ...[many deleted]... wininet:http winmm:wave winspool.drv:info
```

Whew, that's a lot of data. I looked at all the ones that failed for
five or more people:

- user32:msg, user32:win, and user32:input are probably people running
  non-blessed window managers; Alexandre's position is that we can
  ignore these, since upstream gnome's WM is fixed.

- dsound:ds3d is mostly "ds3d.c:891: Test failed: The primary volume
  changed from -27 to -960" (worrisome, random) plus "ds3d.c:896: Test
  failed: The primary pan changed from -5594 to -5595" (rounding
  error, just add slop of 1?). dsound:ds3d8 is the same.

- kernel32:path is mostly
  "path.c:899:TMP=c:\windows\temp"..."path.c:1178: Test failed:
  expected buf\[0\] upper case letter got c", probably people whose
  ~/.wine is old and has a windir that starts with a lowercase drive
  letter?! Has that changed recently?

- msi:install is mostly "install.c:4414: Test failed: File installed".

- msi:package is mostly "package.c:1661: Test failed: wrong return val
  (0)"

- riched20:editor has several failures.

- d3d9:visual failures are all from people not running an approved
  graphics card, and can be ignored (though maybe we should tell users
  we only support nvidia Geforce 6 and higher for 3d graphics...)

Here are some older notes from a previous build:

- kernel32:process is mostly "process.c:1237: Test failed: Wrong
  cursor position"

- ddraw:visual has two kinds of errors. The most common is
  "visual.c:2045: Test failed: Got color 00dcdde6, expected
  0000ff00". Less common is mstefani's failure, "visual.c:481: Test
  failed: Untransformed vertex with linear vertex fog has color
  00ff0000". \[fixme: file bugs?\]

- urlmon:protocol has three or so failure modes; most common is
  "protocol.c:1597: Test failed: Read failed: 8000000a (0 bytes)".
  \[fixme: file bug?\]

- gdi32:font has several failure modes, not sure what's going on
  there.  \[fixme: file bug?\]
