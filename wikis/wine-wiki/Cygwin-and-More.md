Here at the Wine project, we're trying to help Windows applications talk to unix systems. At the same time, other great projects have been working on making sure the conversation goes both ways. User-space packages like [Cygwin](https://www.cygwin.com/) and cross-compilers like [mingw-w64](https://mingw-w64.org/doku.php) allow unix applications to talk to Windows systems and reach a wider audience. On this page, we discuss how you can use these complementary projects to test and improve Wine.

## Disclaimers

**If you only want to use or debug normal apps on Wine, or even do normal development, these are not the pages you're looking for (\*does Jedi hand wave\*)**

The ideas here are ordered from least to most experimental, but even the first tests involving Cygwin are geared towards developers interested in pure experimentation. **None** of these ideas are stable or simple enough for regular use (and they likely never will be).

**For the foreseeable future, any questions about "how to get/setup/install Wine on Windows" or "Wine through bash on Windows 10" on the forums, mailing lists, or IRC may result in ostracism, shunning, the evil eye, and/or being grumpily ignored.**

Well not really; we do try to be friendly. However, we want to emphasize that there is **no such feature as "Wine on Windows"** since there has been a lot of confusion about it in the past. That was just a pithy name for the most experimental projects on this page, but when users mistake this for a real feature and ask about it on the forum for instance, it only creates confusion and distracts volunteers from answering other questions. If someone does ask, please politely correct them with a clear explanation or a link to these disclaimers.

We can certainly appreciate where the demand for such a feature comes from, but remember that [Wine isn't an emulator](FAQ#is-wine-an-emulator-there-seems-to-be-disagreement) anyways. Even if our developers can someday perfect the truly gnarly alchemy required to make the ideas here work, a "Wine on Windows" setup would have to run in tandem with something like Cygwin or WSL. Essentially, Wine would be converting WinAPI calls from your program to unix-isms, which would then need to be converted _back_ to WinAPI calls (plus WSL doesn't even support 32-bit binaries to begin with). That's definitely not a recipe for a reliable, responsive experience.

If you're having troubles with Windows' compatibility mode, have you considered using a dual-boot install of unix alongside Windows, or if you feel ready, switching to unix entirely? Then you can run Wine as it's designed to be, which is really just one among thousands of benefits to entering the paradise of unix. If you're still resisting the switch to unix for some reason though, you may have some luck investigating [ReactOS](https://www.reactos.org/).

**Of course, if you are interested in hacking on these projects, blaspheming against all that is holy, and don't mind losing your sanity in their recursive jungles, continue reading... _if you dare!!!_**

For those that do want to tease out and fix the issues that emerge from these projects, we wish you luck. You can always ask reasonable, focused questions on [wine-devel](mailto:wine-devel@list.winehq.org) or #winehackers, and report [Bugs](Bugs) on Bugzilla. We only ask that before discussing any problems, you **first try to make progress and analyze bugs on your own as much as possible**, with the help of the docs of course. This is purely so these experiments don't steal much oxygen from higher-priority work.

## Cygwin in Wine

Before we plunge into the truly wild and wooly, installing and running the Cygwin suite within Wine is a relatively well-behaved process. Even as early as around Wine v1.0, Dan Kegel reported that much of the Cygwin suite installed and ran successfully.

As of 2026, Cygwin doesn't quite run correctly on Wine. However, some components of Cygwin do indeed work, and progress has been made with a few significant bugs being fixed. The current status in the AppDB can be found [here](https://appdb.winehq.org/objectManager.php?sClass=application&iId=633). There is a fork of Wine that contains fixes that get things like Mintty working at https://gitlab.winehq.org/bernhardu/wine/-/tree/msys2-cygwin_wip?ref_type=heads.

Cygwin is a set of libraries and tools compiled for Windows that provides a POSIX API. It's less a compatibility-layer like Wine and more like a miniature distribution that overlays Windows. As a result, unix apps must still be recompiled for Windows to run in Cygwin.

By using Cygwin in Wine, we can do more than uncover bugs with Cygwin itself; we can theoretically rebuild many unix binaries, scripts, etc. into tiny unit tests for Wine. Since the Cygwin sources are completely open too, it should be easier to diagnose the cause of a specific problem. Just remember the Cygwin executables must be run from a Windows/Wine console, not a unix command-line (if you want to start Cygwin's shell, launch the _cygwin.bat_ script from the same console).

For more details, our Bugzilla has a quick [list of bugs provoked by cygwin](https://bugs.winehq.org/buglist.cgi?no_redirect=0&quicksearch=cygwin).

For a less self-referential take on the "let's run an _entire suite_ on Wine" approach to testing, see [Guest Unit Tests](Guest-Unit-Tests)

## Role Reversal

And here's where things start getting interesting. Running Cygwin on Wine is a good test for Wine while still offering a little mischief, yet it doesn't really offer new, profound (and Faustian) possibilities. What if we switched things around though and tried to run Wine on Cygwin? Or cross-compile the Wine DLLs to plug into Windows? Or test on a hybrid system like coLinux? Or... you get the idea.

### Wine on Cygwin

**This has not been tested in a while; consequently, problem or requirement lists may be especially outdated. If you've tested this more recently, please update any results.**

So to get started, you'll need to install Cygwin on your Windows system. You could theoretically install it to a Wine prefix running on a unix machine (or even within another Cygwin install within ... ad infinitum), but let's stick to one heresy at a time.

You'll want _at least_ the following modules from Cygwin's _setup.exe_:

- audio/libgsm-devel
- devel/bison
- devel/ccache (for [Regression Testing](Regression-Testing))
- devel/flex
- devel/gcc
- devel/gettext-devel
- devel/gnutls-devel
- devel/libjpeg-devel
- devel/liblcms2-devel
- devel/libncurses-devel
- devel/libpng-devel
- devel/make
- devel/openldap-devel
- devel/patch
- devel/pkg-config
- graphics/libtiff-devel
- libs/libtiff-devel
- libs/libxml2-devel
- libs/libxslt-devel
- system/libdbus1-devel
- utils/patchutils
- X11/libfontconfig-devel
- X11/libX11-devel

After that you'll want to get Wine's [Source Code](Source-Code), either as a tarball or [or from git](Git-Wine-Tutorial). Then in the source directory, follow the instructions for [Building Wine](Building-Wine) as you normally would.

Once you've finished, Wine will almost certainly fail as a whole. However, you should still be able to check-off some individual DLLs and executables as mostly working. A few issues that have shown up in the past and deserve attention are:

- _configure_ may fail to detect many packages _even if_ you've installed them; there doesn't seem to be an open or closed bug-report about this though
- 16-bit components had severe compilation problems so Wine now builds with `--disable-16bit` by default. Getting those to compile might be a "fun" problem; see bug #17930 for more info

### Cross-compiling with mingw-w64

Besdies Cygwin, another possibility is to cross-compile Wine's DLLs into Windows' Portable Executable format, then see how they behave on a Windows system. One advantage of this method is that you can run the cross-compiler from the comfort of your native unix environment; we will focus on the mingw-w64 cross-compiler for these instructions.

While the original MinGW project still has some active developers, it has been largely outpaced by the younger mingw-w64 fork.

On many distributions, you should be able to find a package for mingw-w64. We recommend installing it through your package-manager if it all possible, though you can always download a [source tarball](https://sourceforge.net/projects/mingw-w64/files/mingw-w64/mingw-w64-release/), or pull straight [from git](https://sourceforge.net/p/mingw-w64/mingw-w64/ci/master/tree/), if your distro doesn't offer one or you want the newest changes.

Once mingw-w64 is installed and you've run _configure_ in your Wine build directory, you can cross-compile various parts of Wine, based on your needs.

#### A Shortcut for Unit Tests

One particularly handy recipe is to cross-compile just Wine's tests so you can run them on a Windows machine. With mingw-w64 installed, you can just run from the top of your build tree:

```
make crosstest
```

This skips all of Wine's DLLs and programs, cross-compiling only the tests. It's great for when you've written new [Conformance Tests](Conformance-Tests) and want to check them on a Windows machine before [Submitting Patches](Submitting-Patches), especially since you don't need to go through any extra preparations.

#### Preparing to Cross-Compile

If you're interested in cross-compiling more than just Wine's conformance tests, however, you will need to do some extra configuration in your build directories first.

Configurations will persist for a build directory unless you re-run _configure_ in it with different parameters. As a result, if you plan to regularly alternate between building for unix and cross-compiling to Windows, you really should have two separate build directories, one configured for each.

The first step is to determine which setting to pass to the `--host` flag in your cross-compiled build directory. Some of the options appear to be redundant, but the main points are that you pick one that specifies using **mingw** and that it targets the proper architecture.

Although they haven't been tested recently, here are some that should work based on Wine's _configure_ script:

|  |  |
|--|--|
| **i686-mingw32msvc-gcc** | Target x86 arch, MS Visual C headers, [GCC](Gcc) backend |
| **i686-mingw32-gcc** | Target x86 arch, mingw-w64 headers, GCC backend |
| **i686-w64-mingw32-clang** | Target x86 arch, mingw-w64 headers, [Clang](Clang) backend |
| **amd64-mingw32msvc-gcc** | Target [AMD64](AMD64) arch, MS Visual C headers, GCC backend |
| **amd64-w64-mingw32-gcc** | Target AMD64 arch, mingw-w64 headers, GCC backend |
| **amd64-w64-mingw32-clang** | Target AMD64 arch, mingw-w64 headers, Clang backend |
| **armv7-w64-mingw32-gcc** | Target [ARM](ARM) arch, mingw-w64 headers, GCC backend |
| **armv7-w64-mingw32-clang** | Target ARM arch, mingw-w64 headers, Clang backend |

As of Mar 2016, the flags still use the name _mingw32_, but this should not be an issue so long as you have mingw-w64 installed.

Next, after creating _two_ separate directories to build Wine in, one native and the other for cross-compiling, you need to make the native, Wine build-tools:

```sh
$ cd build-native
$ ../wine-source/configure
$ make __tooldeps__
$ cd ..
```

Now you can configure your other build directory for cross-compilation. Just be sure to unset the `CC` environment variable before running _configure_. This ensures that your normal compiler doesn't accidentally override mingw-w64:

```sh
$ unset CC
$ cd build-mingw
$ ../wine-source/configure --host=i686-mingw32msvc-gcc --with-wine-tools=../build-native --without-freetype --without-x
```

#### Individual Subsystems

In properly prepared build directories, you can easily cross-compile an individual Wine DLL too:

```sh
$ cd build-mingw/dlls/<dll>
$ make <dll>.dll
```

Cross compiling an import library for DLLs or static libraries is also simple:

```sh
$ cd build-mingw/dlls/<dll>
$ make lib<dll>.a
```

After compiling these dlls, you should be able to use them in Windows just by placing them in the same directory as whatever program you want to run.

While it is possible to install DLLs system-wide by overwriting the native Microsoft ones and removing backups from the _dllcache_, this is **very risky and we strongly discourage it**. If you do decide to try it, at least back up copies of all DLLs involved; archiving a full image of your system that can be easily restored would be even better.

If you want to specifically cross-compile the Wine Direct3D DLLs, at least in the past (we haven't tested this in a while), you would need to pass the `-DUSE_WIN32_OPENGL` custom flag to the compiler. This would instruct the files to load OpenGL functions from Windows' native _opengl32.dll_

An interesting test can be to cross-compile a Wine DLL with mingw-w64, then build the same one in Cygwin. After that, you can test each of them on a Windows system. Since mingw-w64 and Cygwin cooperate regularly, the results should be similar, but if one version works better than the other, consider reporting a bug to whichever project give an error. This may not help Wine directly, but we do work alongside both projects on several issues; if it helps the ecosystem, it helps us too.

#### The Whole Shebang

At this point, if you want to cross-compile as much of Wine as possible, most of the actual work should be done if you configured your build directory correctly. Just enter your cross-compilation build directory and do `make -k`:

```sh
$ cd build-mingw
$ make -k
```

The reason for the `-k` flag is that some of Wine's DLLs are only for a unix environment. Since `make` won't be able to run through the whole build tree anyway, this allows you to still build whatever you can in one go.

## Even More Options

What?! You say your soul still doesn't feel polluted enough from strange and unnatural works, which were never meant to be?! Ok then.

Since perhaps the main benefit of these tests are improving Wine's [Compatibility](Compatibility) and robustness, other Windows-like setups could be worth testing too. The overlay and cross-compiler approaches discussed above are hands-down the most heavily tested. Both of these projects are alive and well too, which can make a big difference when trying to pick apart a knotty issue.

However, there are a few other possibilities that haven't been tested much, but could be worth it... in the name of science, of course. We've included sections for any software that we have tested somewhat, but here are a couple setups we've only heard whispers of...

- [UWIN](https://github.com/att/uwin) (similar approach to Cygwin, from AT&T Labs)
- [Parity](https://github.com/mduft/parity) (a wrapper for the MS Visual C/C++ compiler; adds GCC-like commands and Interix features)
- [LBW](https://github.com/davidgiven/LBW) (essentially Wine in reverse, a Linux ELF binary loader for Windows Interix)

### Psst... Even Microsoft Does UNIX... Sort of

From the earliest days of Windows NT through Windows 8.0 (but not 8.1 or 10), Microsoft has actually packaged shims and user-space software that allows running many unix programs on a Windows system. Initially called Services For Unix (SFU) through Windows XP, it was restructured and renamed to Subsystem for Unix-based Applications (SUA) starting with Windows Vista / Server 2003. Another name you may hear for this software is Interix, which is technically the standard POSIX tools and system-call translators that form the heart of SUA (you might even say Interix is Cygwin's doppelgänger). However, Interix actually used the subsystem feature of the NT kernel to run outside Win32, unlike Cygwin.

Microsoft officially deprecated Interix beginning with Windows 8 before retracting it altogether for Windows 8.1 and 10. Apparently still fascinated by the idea though, Microsoft released the Windows Subsystem for Linux (WSL), sometimes called "bash on Windows," for Windows 10 beginning with the "Anniversary" update (summer 2016). Like Interix, WSL uses Windows features to partly isolate unix processes from Windows kernel-level ones, but whereas Interix sought to implement POSIX binaries as Windows executables, WSL is meant to run Linux-native ELF binaries by providing a virtual Linux API, enabled by a translation layer on top of the Windows kernel... so essentially like Wine in reverse (we should probably be flattered).

#### Trying to Build Wine on WSL

If you're interested in actually trying to build Wine on top of WSL, at this time (spring 2018), nobody seems to have even tried. Who says people don't have common sense? It would probably be even more difficult than with SUA, requiring many workarounds for POSIX binaries and Linux features that WSL doesn't implement well, if at all. On top of that, WSL **only** supports 64-bit binaries so you would be restricted to building Wine64... and don't forget, if you want graphics, you'll have to install and debug an X11 server all on your own!

Of course, if you decide to try anyway, you're encouraged to add some notes and observations here.

#### Trying (and Failing) to Build Wine on SUA?

With Windows XP and Server 2003 no longer even receiving minimal, extended support, we will focus on SUA, which is still available for premium versions of Windows Vista / Server 2008 through Windows 8.0 / Server 2012 R1.

Even though SUA is still provided for some versions of Windows, it has barely been maintained and contains many outdated binaries. In some cases, you may need to build and install newer versions of even basic tools. In fact, general opinion on the internet seems to be that recent versions of Cygwin are now far easier to get working than the neglected SUA system.

If you're on a Windows system that provides SUA, you can enable the core of the subsystem just like other built-in Windows components:

1. Open the _Control Panel_
2. Select the _Add/Uninstall a Program_ applet
3. Go to the _Turn Windows features on or off_ option
4. Check the box for "Subsystem for UNIX-based Applications"

However, to get the actual user-space tools, which make up the bulk of Interix, you'll also need to download and install the separate SUA SDK and utilities. As of April 2016, the following links were all still valid:

- For [Windows Vista / Server 2008 R1](https://www.microsoft.com/en-us/download/details.aspx?id=23754) (\~475 MB)
- For [Windows 7 / Server 2008 R2](https://www.microsoft.com/en-us/download/details.aspx?id=2391) (\~250 MB)
- For [Windows 8.0 / Server 2012 R1](https://www.microsoft.com/en-us/download/details.aspx?id=35512) (\~250 MB)

If you _really_ want to put yourself through it, you can then try compiling Wine with SUA (as usual, we make no guarantees this won't do something horrible to your system or your sanity). This also hasn't been tested in a long time, but once have SUA and any necessary replacement binaries together, compiling Wine from source shouldn't be too out of the ordinary. In the past, you would need to download a source tarball of Wine, but now with Git even ported to Windows, this probably isn't necessary.

In the past, Wine's _configure_ script also had trouble detecting the **freetype** libraries on Interix, even if they had been built properly from source and installed. Another issue that could pop up is poor X11 support, unless that is, you've built and installed a full X11 system. Since you'll probably have your hands full even without graphics support, you may want to ignore that for now. Finally, old documentation by Microsoft on [build configuration in Interix](https://technet.microsoft.com/en-us/library/bb463199.aspx) suggests passing the `-D_ALL_SOURCE` flag to the compiler for better results

Putting it all together, your best bet may be a configuration that looks sort of like this:

```sh
$ CFLAGS="-D_ALL_SOURCE" CXXFLAGS="-D_ALL_SOURCE" ./configure --without-freetype --without-x
```

### The Cooperative Linux Kernel

One last experiment would be to attempt building and testing wine through some variation on [Cooperative Linux](https://colinux.org/) (aka coLinux). This system is neither a compatibility layer nor OS, but a Linux kernel modified to run in a privileged mode concurrently and with deference to a host Windows NT kernel. The modifications include virtual devices drivers that pass particularly low-level calls through to the host kernel.

While coLinux by itself only provides the unique kernel, without most of the libraries and features Wine would need, there were multiple distributions developed on top of the coLinux kernel. These distributions, such as the Ubuntu-based [andLinux](https://www.andlinux.org/), provide a comprehensive collection of software but still integrate with the host Windows system as much as possible.

In theory, this approach to contorting Wine could be simpler than some of the earlier ones discussed. However, there are still several issues that could come up:

- coLinux and the distributions that use it are still incomplete and have been dormant for years now.
  - Whether the original developers plan to revive the projects themselves isn't clear, but anyone interested in using them might have to effectively revive the project anyways.
- At least in the past, coLinux couldn't access physical memory or the Windows filesystem on demand, features Wine would require.
- coLinux needs administrator access for installation and must run in a privileged mode.
  - This isn't necessarily a problem or an issue; it's not a benefit though and could cause complications in odd or dangerous situations.
- coLinux is currently a Win32-only kernel mode driver and will not work on Win64.

## The Audience Applauds

> The whole concept of "tricking" windows into being useful is just such a deviant thrill. - _Thomas Stover, on reading an early revision of this page_

> I am torn between "That is disgusting beyond words" and "I salute your awesome perversity". - [_Eric S. Raymond_](https://esr.ibiblio.org/?p=904#comment-233972)

> The _real_ reason, of course, is that it's obviously evil and wrong and therefore fun for hack value. - _David Gerard, who did much of the early work on this idea_

> It's straight out of Goethe! - _Kyle Auble, on revising the page for the new wiki_

## See Also

- [Building Wine](Building-Wine)
- [Compatibility](Compatibility)
- [Developer FAQ](Developer-FAQ)
- As mentioned above, for those interested in a practical alternative that isn't Windows but doesn't follow unix paradigms, consider checking out [ReactOS](https://www.reactos.org/)