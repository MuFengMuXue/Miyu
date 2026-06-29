## Wine and the Google Summer of Code

This page collects some tips for students who want to work on Wine
during the Summer of Code, and provides a few ideas for projects.

- Do you:
  - Know [C](https://kegel.com/academy/tutorials.html)?
  - Perhaps have done some Win32 low-level Windows programming already
    (below MFC)?
  - Have an idea to improve Wine and make it more useful and popular?
  - Perhaps improve a specific application to run under Wine? (it
    however needs to be predictable ahead in scope for Summer of Code)
  - If so, please introduce yourself on the [wine-devel mailing
    list](https://list.winehq.org/mailman3/postorius/lists/wine-devel.winehq.org/) or the
    [\#winehackers IRC channel at
    libera.chat](irc://irc.libera.chat:6697/#winehackers), and apply for
    a [Google Summer of Code scholarship](https://code.google.com/soc)!
- Hint/reminders:
  - Have a look at [the developers page on the
    wiki](Developers) and grab Wine's [source
    code](Source-Code), try to get acquainted with it
  - Look at [Previous Summers Of
    Code](Previous-Summers-of-Code) for previously accepted
    proposals / their results
  - Do not forget: we can only support one proposal per application. You
    can file multiple applications if you want to propose more than one
    idea.
  - Copying proposals verbatim will get your proposal deleted without
    even looking at it twice. You have to make your own proposal. See
    also [PostgreSQL's Summer Of Code
    Advice](https://www.postgresql.org/developer/summerofcodeadvice)
  - Read [How can I prepare for
    GSoC](https://www.quora.com/How-can-I-prepare-for-GSoC-2015) for some
    general rules.
  - Read [How Not To Apply For Summer Of
    Code](https://blog.gerv.net/2006/05/how_not_to_apply_for_summer_of/)
    to save your time and save our time.
- Note: Applicants **MUST** have submitted a patch or testcase to
  wine-devel (see [Submitting Patches](Submitting-Patches))
  to be considered for acceptance.

To apply, go to the [Google Summer of Code home
page](https://developers.google.com/open-source/gsoc/).

------------------------------------------------------------------------

## Important notes!

- Applicants **MUST** have submitted a patch or testcase to wine-devel
  (see [Submitting Patches](Submitting-Patches)) to be
  considered for acceptance.
- Please first send a draft proposal and discuss it with us, don't send
  the final one directly.
- We cannot accept [ReactOS](https://www.reactos.org) proposals, so
  please only make proposals that will benefit Wine.

To apply, go to the [Google Summer of Code home
page](https://developers.google.com/open-source/gsoc/).

------------------------------------------------------------------------

## Beware of Legal Requirements

You must state that you will follow these minimal legal requirements
during the SoC (and have done so in the past):

- **You are not allowed to read or reuse Windows source code (leaked
  source / Windows Research Kernel\* / ...)**

(**\*** we are following the
[SFLC](https://en.wikipedia.org/wiki/Software_Freedom_Law_Center)'s
advice)

- **You are not allowed to reverse engineer Windows files by
  disassembling or decompiling them**
- **You are not allowed to analyze Windows files with the trace
  functions of Wine**
- **People who work or have worked for Microsoft should probably not
  participate**

------------------------------------------------------------------------

## Other Outreach Programs

In addition to Google Summer of Code Wine also participates in:

- [Outreachy](https://www.outreachy.org/) is a program similar to GSoC
  organized by the Software Freedom Conservancy. The goal of Outreachy
  is to provide encouragement, experience, and networking opportunities
  for minorities that are underrepresented in tech. Unlike GSoC, it is
  not limited to students; you can read the Wine Wiki's
  [Outreachy](Outreachy) page for more information.

------------------------------------------------------------------------

## Ideas

### Your own idea

Possible mentors: We'll provide you with the appropriate mentor

- If you have an idea, please post it on [Wine Developers mailing
  list](https://www.winehq.org/pipermail/wine-devel) so we can help you
  with your idea and find out if it's realistic or not. Showing
  initiative and willing to discuss your idea greatly improves your
  chances of getting accepted. Even more so than taking one of the ideas
  below.
- As long as you work hard and interact with the community and your
  mentor in a positive and constructive way you don't have to worry
  about not meeting all your goals.

------------------------------------------------------------------------

### Fix Tests on Your Windows Machine

Possible mentors: Depends on the libraries you pick

Wine has an extensive testsuite that is used to document how the Windows
API works and check Wine's conformance to the native Windows behaviour.
The Wine testbot automatically runs tests when patches are submitted to
check if a patch breaks anything.

Unfortunately no Windows machine passes all the tests:
<https://test.winehq.org/data/> . A few tests are failing reliably and
others fail randomly. This can have a number of reasons. Either the test
is too strict, Windows' behaviour changed from version to version, the
test does not take the influence on some settings into account (e.g.
system language), etc.

A possible GSoC project is to pick a set of libraries of a certain
domain you are familiar with (e.g. 3D graphics, XML parsing, networking,
etc), where tests are failing on one or more of your machines and try to
fix them. However, we don't simply want to remove failing tests, but try
to understand why they are not behaving as expected. So be prepared for
long debug sessions to find out the differences between your Windows
installation and one that passes the tests.

Some of the details we expect you to provide in your proposal are DLLs
you plan to look at and the current test failures you see in them. Hack
away any crashes that prevent any later tests from running to get the
full picture. Test how the same tests behave on Linux inside Wine.

------------------------------------------------------------------------

### Upstream changes from winevdm

Possible mentors: Stefan Dösinger

Wine supports running old Windows 3.x (Win16) programs on 64 bit Linux
hosts. The winevdm project (https://github.com/otya128/winevdm) ported
this ability to Windows. They are using Wine's 16 bit thunks and combine
it with a CPU emulator to get around kernel limitations that prevent 16
bit applications from working natively on 64 bit Windows.

The winevdm project has made quite a few changes to the thunks over time
and extended them. This project proposal is about upstreaming those
changes to Wine. Find some applications that work in winevdm but not
Wine, isolate the changes necessary to make them work (the winevdm git
log is your friend) and submit them in small patches to wine-devel.

Your GSoC application should identify one or more Win16 applications
together with a likely set of changes that will get the application
running. It doesn't have to be a complete set of patches - that will be
the main part of your project - but we want to see that you are able to
find your way around the source tree.

------------------------------------------------------------------------

### Implement XRandR display settings handler with transforms

Possible mentors: Zhiyi Zhang

- On Wayland and some setups with Nvidia proprietary drivers, XRandR
  reports only one
  resolution(https://bugs.winehq.org/show_bug.cgi?id=34348#c34). In this
  case, the proper solution is to use XRandR transforms to simulate
  display resolution changes so that Wine can support multiple display
  resolutions even if the host only report the native resolution.
- End goal would be to allow changing the display setting on Wayland and
  passing all the tests in dlls/user32/tests/monitor.c

------------------------------------------------------------------------

### DirectShow DVD support

Possible mentors: Zebediah Figura

- DirectShow is a general multimedia streaming framework, built around
  creating graphs of individual "filters" which consume and produce
  data. Windows ships a number of built-in filters.
- Several interfaces related to DVD support (DVD Navigator filter, DVD
  filter graph) are stubs or unimplemented. The work would consist of
  providing an implementation of these interfaces.
- End goal would be to allow a native application to play DVDs.

------------------------------------------------------------------------

### AVFoundation video capture support

Possible mentors: Zebediah Figura, Gijs Vermeulen
Requirements: Mac OS development

- Yet another DirectShow project: implement video capture on Mac.
- Currently the only video capture backend is Video4Linux (i.e. v4l2).
  The work would consist of writing another backend using AVFoundation.
- End goal would be to allow a native application to capture video.

------------------------------------------------------------------------

### DirectShow audio capture

Possible mentors: Zebediah Figura

- Yet another DirectShow project: implement audio capture.
- The work would consist of implementing the CLSID_AudioRecord object,
  which is currently only stubs.
- Audio capture should probably be done through WinMM APIs (i.e.
  waveIn\*).
- End goal would be to allow a native application to capture audio.

------------------------------------------------------------------------

### Implement robocopy.exe

Possible mentors: Zebediah Figura

- A complex copying program needed by some installers: bug #43653
- Work would consist of implementing the basic functionality of the
  program, including flags needed by the relevant programs.

------------------------------------------------------------------------

### Evaluate performance of hqemu in Hangover

Possible mentors: Stefan Dösinger

Hangover (https://github.com/AndreRH/hangover) is a proof of concept of
integrating a CPU emulator - in this case qemu - with Wine to run x86
Windows applications on non-x86 host CPUs without running a full Linux
userspace stack inside the emulator. While its design is not suitable
for upstream integration, it is useful for performance evaluation.

hqemu (https://csl.iis.sinica.edu.tw/hqemu/) is a modification of qemu to
generate more efficient translated code with the help of LLVM.

This project proposal is about merging together the hqemu modifications
and hangover qemu modifications to evaluate the combined performance.
Hangover ideally keeps the amount of code that needs to be emulated
small and hqemu speeds up the emulation. If combined, they might either
synergize well, or the faster emulation makes hangover's high level
thunks moot.

To work on this you will need an arm64 Linux machine. Hangover is
notoriously difficult to build. Please try to build and run both
Hangover and hqemu separately before submitting your application. Try to
get an idea of the modifications each project makes to qemu and how to
reconcile them.
