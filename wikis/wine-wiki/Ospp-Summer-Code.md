[Summer 2021 of Open Source Promotion Plan
(OSPP)](https://summer.iscas.ac.cn/help/en/) is jointly organized by
[Institute of Software Chinese Academy of Sciences
(ISCAS)](https://english.is.cas.cn/au/) and [openEuler
community](https://openeuler.org/en/). OSPP Summer is very similar to
Google Summer of Code (GSoC) and [Outreachy](Outreachy).

OSPP opens to all projects with OSI-approved licenses, and worldwide
students. When students finish their projects, both students and mentors
will be paid. OSPP committee will process international wire transfers
if needed.

## Student Guide

### LEGAL REQUIREMENTS

You must state that you will follow these minimal legal requirements :

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

For more information, please read the
[Developer-FAQ](Developer-FAQ#copyright-issues) and the
[Clean_Room_Guidelines](Clean-Room-Guidelines)

### How to Apply

1.  Check [Student
    Eligibility](https://summer.iscas.ac.cn/help/en/student/#student-eligibility)
    and register your account at OSPP Portal.
2.  Introduce yourself (Brief!) and discuss your ideas at
    1.  [wine-devel mailing
        list](https://list.winehq.org/mailman3/postorius/lists/wine-devel.winehq.org/)
    2.  Or \#winehackers IRC channel on irc.libera.chat
    3.  You could also send your ideas to your mentor directly
    4.  Note: This is a **necessary** step!
3.  Update your draft proposal
4.  Submit your final proposal on [OSPP Summer
    portal](https://summer.iscas.ac.cn/help/en/student/#2-submit-the-project-application)
    before the deadline

### Suggestions

- Have a look at [the developers page on the wiki](Developers) and
  grab Wine's [source code](Source-Code), try to get acquainted with
  it
- Look at [Previous Summers Of Code](Previous-Summers-of-Code) for
  previously accepted proposals / their results
- It's encouraged to propose more than one idea. But only one proposal
  will be accepted per applicant.
- **HIGHLY RECOMMEND** applicants submit a patch to Wine (see
  [Submitting Patches](Submitting-Patches)). It can be a stub dll or
  adding a test case. We want you be comfortable with Wine's Git
  Workflow.

## Differences With GSoC

- [OSPP is providing three different
  levels](https://summer.iscas.ac.cn/help/en/community/#how-to-set-project-difficulty-in-community),
  with different awards. That might make it easier to find
  projects/students. If an idea is interesting but too easy for GSoC, it
  might be suitable for OSPP summer with medium/low difficulty.

- [OSPP explicitly lists documentation work as possible
  tasks](https://summer.iscas.ac.cn/help/en/#what-kind-of-projects-are-supported).
  This adds a few (but not many) opportunities for easy, yet useful
  projects.

## Projects

**NOTE: Please check [OSPP Summer 2021
Portal](https://summer.iscas.ac.cn/#/org/orgdetail/wine?lang=en) for
list of committee-approved projects**

### Your own idea

Possible mentors: We'll provide you with the appropriate mentor

- If you have an idea, please post it on [Wine Developers mailing
  list](https://www.winehq.org/pipermail/wine-devel) so we can help you
  with your idea. Showing initiative and willing to discuss your idea
  **greatly improves** your chances of getting accepted.
- As long as you work hard and interact with the community and your
  mentor in a positive and constructive way you don't have to worry
  about not meeting all your goals.
- Don't be afraid that you don't have a perfect idea - take advantage of
  the time before the proposal deadline.

------------------------------------------------------------------------

### Various vkd3d-shader enhancements

Possible mentors: Henri Verbeet

The vkd3d-shader library is used by vkd3d and Wine to translate between
different shader formats.

- Introduce a shader model 4+ assembler. Shader model 4+ shaders are
  typically written in HLSL, but when writing vkd3d tests it would
  sometimes be convenient to have more control over the generated
  bytecode, for example by explicitly selecting specific instructions to
  use. Note that for a shader model 4+ shader to be functional, it
  requires not only the shader code itself, but also input/output
  signatures, and patch constant signature in case of tessellation
  shaders. These would need to be able to be specified as well.
- Port wined3d's GLSL (OpenGL Shading Language) generator to
  vkd3d-shader. The ability to translate Direct3D shaders to GLSL is
  useful outside of wined3d as well. Porting the GLSL generator to
  vkd3d-shader would make it much easier to use for projects other than
  Wine, including vkd3d-compiler for offline compilation. In combination
  with a HLSL compiler, this would allow translation of HLSL to GLSL.
- Introduce a MSL (Metal Shader Language) generator to vkd3d-shader. For
  much of the same reasons that adding a GLSL generator would be useful,
  adding a MSL generator would be useful for usage in combination with
  Apple's Metal API. This project would be a little harder than the GLSL
  project above, because there's no existing MSL generator in Wine to
  port. Still, wined3d's GLSL generator could perhaps be used for
  inspiration.
- Add a Direct3D shader model 6 (DXIL) parser/disassembler. Direct3D
  shader model 6 shaders use a bytecode format (DXIL) that's different
  from previous versions. We would like to support shader model 6
  shaders in vkd3d, and being able to parse them would be the first
  step.
- Documentation improvements. We have some API documentation, and some
  example code in the form of the "gears" and "triangle" demos, but it
  would be nice to also have some "tutorial" style documentation to help
  people get started.
- Make vkd3d-shader compiler messages and vkd3d-compiler output
  translatable.
- Convert existing Direct3D 12 tests to the shader_runner framework.
  Much like Vulkan, Direct3D 12 is an API that requires many things
  which would be done implicitly by other APIs to be done explicitly by
  the user of the API. That has its advantages, but one of the
  consequences is that many of the d3d12 tests ended up being more
  verbose than equivalent d3d11 tests. The shader_runner framework in
  vkd3d is similar in concept to Piglit's shader_runner, and allows
  tests to be written in a more declarative and much more concise style,
  at the expense of some flexibility. Where possible, we would like to
  convert our existing d3d12 tests to shader_runner tests. Note that
  until vkd3d-shader's HLSL compiler is sufficiently complete, shaders
  would need to be specified in binary form, like they currently are in
  the existing tests.
- Support more shader_runner target APIs. Because shader_runner tests
  are largely unaware of the underlying API used to implement them, it
  would be possible to run the same tests on multiple different APIs
  with relatively little effort. Support for Vulkan, or OpenGL with the
  ARB_gl_spirv extension would allow testing vkd3d-shader shader
  translation independently of the rest of vkd3d. In the future, that
  could also apply to HLSL input, and GLSL or MSL output formats.

------------------------------------------------------------------------

### Implement keyboard shortcut support for Datetime Picker Control

Possible mentors: We'll provide you with the appropriate mentor

The idea is to add support of all/some of the keyboard shortcuts
mentioned in this
[MSDN](https://docs.microsoft.com/en-us/windows/win32/controls/month-calendar-controls#selecting-a-day)
page, so that we can select a day by the keyboard.

[Wine bug 50511](#50511) will also benefit from this work.

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

### Multi-monitor display settings support on Mac

Possible mentors: Zhiyi Zhang

- Currently, Wine supports enumerating multiple
  monitors(EnumDisplayMonitors) but cannot change their display settings
  on Mac(EnumDisplaySettings, ChangeDisplaySettings). On Mac, only the
  primary display settings can be changed. Multi-monitor display setting
  handlers are implemented in winex11.drv so we can do a similar thing
  in winemac.drv.
- End goal would be to allow changing the display setting on
  multi-monitor Mac systems and passing all the tests in
  dlls/user32/tests/monitor.c

------------------------------------------------------------------------

### Implement XRandR display settings handler with transforms

Possible mentors: Zhiyi Zhang

- On Wayland and some setups with Nvidia proprietary drivers, XRandR
  reports only one
  resolution (https://bugs.winehq.org/show_bug.cgi?id=34348#c34). In this
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

------------------------------------------------------------------------

### Brain Storming

Please feel free to drop immature ideas here. It's okay if you post an
idea here while you're not participating as a student/mentor. It may be
the start of some high-quality discussion

## Coordinator

Zhenbo Li
IRC: @zhenbo:matrix.org
Email: litimetal -at- gmail dot com

Austin English
IRC Nick: austin987
Contact: austinenglish -at - gmail dot com

Name: André Hentschel
IRC: Andre_H
Email: nerv -at- dawncrow -dot- de
