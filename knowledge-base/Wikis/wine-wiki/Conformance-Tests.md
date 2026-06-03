Wine builds a set of [unit tests](Guest-Unit-Tests) that
check the behavior of a large portion of the Windows API. The purpose of
these tests is to:

- Document the behavior of the Windows API.
- Make sure the Wine implementation conforms to the Windows behavior.
- Detect and prevent Wine regressions.

To simplify running the tests, a single Windows executable containing
all the tests (named WineTest) is updated daily and can be downloaded
from the bottom of [WineHQ's testing page](https://test.winehq.org/).
This helps collect results from a broader set of Windows, Unix and Mac
environments than the [Wine TestBot](Wine-TestBot) farm can
cover.

Running WineTest requires **no programming skills** whatsoever. Simply
download the executable, answer any prompts that come up, and let the
test suite do the rest. This makes running the test suite one of the
simplest ways that users can help improve Wine.

To ensure that the conformance test suite meets its goals:

- Alexandre will not commit any patch that causes conformance test
  failures on his Wine development machine. This ensures the tests pass
  on at least one Wine environment and prevents regressions (but he
  won't say what his computer specs are to preserve the testing
  environment diversity).
- All [merge requests](https://gitlab.winehq.org/wine/wine/-/merge_requests)
  that modify a test are run on a set of Windows machines using the
  the Wine TestBot. Tests that fail there will not be committed. This
  ensures the correctness of the conformance tests, i.e.  that what
  they describe is indeed the Windows behavior.

## Running the tests manually

Wine developers will want to run specific subsets of the tests whenever
they changed something to make sure they did not introduce regressions.
Everyone else should probably use WineTest instead and thus skip to the
next section.

To run specific conformance tests, go to the corresponding dll's tests
directory and run `make test` or `make testname.ok`. For instance:

```sh
$ cd dlls/advapi32/tests
$ make test
$ make services.ok
```

There is an executable in the tests directory after make, for example
dxgi_test.exe, which you can copy to windows machines to test.

## Writing conformance tests

The goal of Wine's conformance testing is to make sure that the Wine
APIs behave identically to the corresponding Windows APIs. As there are
many versions of Windows, ranging from 3.1 to 7, we need people to write
tests as well as volunteers to run them on Windows. The test suite is
still far from complete, but every little bit helps. Writing a test is
also often the best way to check that a bug is real (and not simply a
symptom of a problem elsewhere), and it shows Alexandre Julliard that
your changes should be accepted.

Besides proving that a patch is correct, writing a test case for a
particular API is a great idea if you have doubts about its
implementation. Don't make the mistake of trusting MSDN too much, which
does contain incorrect information, partly because it's not usually
written by the same people who wrote the code. Even if you don't have
the tools on hand to compile a test EXE, somebody else will. Also,
writing conformance tests doesn't require using or targeting Wine in any
way and can be done entirely on Windows.

The [Wine Developer's Guide](Wine-Developer's-Guide) section
on the [writing of Conformance
Tests](Wine-Developer's-Guide/Writing-Conformance-Tests) is
the definitive doc. [This mailing list
discussion](https://www.winehq.org/pipermail/wine-devel/2008-October/069721.html)
also has some great notes on using
`ok(), todo_wine(), skip(), and broken()` inside the conformance tests.

Once you have written your test case, you should verify that it passes
on the TestBot before submitting it to the project. The service will run
your test on several different versions of Windows so that we know it's
a good test.

See also [Cmd Conformance Tests](Cmd-Conformance-Tests),
which are handled a bit differently.

## Getting WineTest

WineTest is the best and easiest way to run the conformance tests
because it will upload the results to a central location where everyone
can look at the results. You can get the latest version of WineTest at:

- <https://test.winehq.org/builds/winetest-latest.exe> for the 32-bit
  Windows executable.
- <https://test.winehq.org/builds/winetest64-latest.exe> for the 64-bit
  Windows executable.

You can also get older 32-bit versions of the test suite by going to the
[WineTest](https://test.winehq.org/) website, opening a specific build's
page, and clicking on the commit id on that page's header.

If you build Wine yourself you will also find a
[Winelib](Winelib) version of WineTest in the
programs/winetest directory.

## Getting wt-daily

*Wt-daily, the easy way to run Wine's Conformance Tests every day!*

This new script, courtesy of Francois Gouget, will make running
WineTest a breeze. It will pull an unpatched version of Wine from the
[Wine git](Git-Wine-Tutorial) tree to build the tests from scratch and
and run them. The script keeps the tests confined within its own tree
and wineprefix, so it won't interfere with your development
environment (or vice-versa).

For more information, [please see the original post to
wine-devel](https://www.winehq.org/pipermail/wine-devel/2015-September/109318.html).

### Quickstart for wt-daily

Checkout the source:

```sh
$ git clone https://github.com/fgouget/wt-daily.git
$ cd wt-daily
```

Create a config file called **wt-daily.config**. For wt-daily to run,
you must include a tag and your email. It's better if you can include a
meaningful tag and a good description of your system.

The format should be:

```
email="your email address here"
tag="a-tag"
desc="A description of your system for Wine developers"
```

The **email** field must be a valid email so that Wine developers can
contact you if they have questions regarding your test results.

The **tag** field is 20 characters, so making it make sense is
challenging.

The **desc** field is your chance to make it all make more sense. This
is where details about the system belong.

Once those are in place, wt-daily will run. Simply save the file and
then run it:

```sh
$ ./wt-daily
```

### Getting wt-daily to Report

Conformance tests will only accept your results for publishing if you
have less than 50 failures and/or less than 10 skips. If you're close,
skipping a test that doesn't work can supply the rest of your valuable
information to the Wine Community. Figuring out which tests are failing
is key, review the **wt-bot-{yourtag}.log** file located in
**\~/wt-daily/winetest/wine**.

Add a field:

```
exclude="test:specifictest"
```

This should be something like **ddraw:ddraw1**.

### Adding to the wt-daily Experience

Finally, if you're running the tests at a time when you'll be away from
your system, you can set it to suspend or shutdown on completion.

Add a field:

```
shutdown="suspend"
```

## Running WineTest on Windows

Here is how to run the tests once you've followed the instructions
above:

1.  Run the WineTest executable.
2.  Enter a short tag for your test run. This is what will be displayed
    as the heading on the [WineTest](https://test.winehq.org/) website.
3.  Provide your email address. This is needed so developers can contact
    you when investigating why a given test failed.
4.  Wait for the tests to run.
5.  Press OK to upload the data to the test results page.
6.  About 5-10 minutes later your results will be on the page for that
    test run.

Also see the [Make Test Failures](Make-Test-Failures) page
for a (necessarily) out-of-date list of known test failures.

Insert an audio or mixed audio+data CD-ROM or DVD in a drive otherwise
winmm:mcicda and ntdll:cdrom skip some tests.

### Windows firewall

- Starting with Windows XP SP2, the Windows firewall will likely ask
  whether to allow some of the tests to accept incoming network
  connections. There is no need to worry about it, and answering either
  way won't impact the results. The reason is that the firewall always
  authorizes connections originating from the local host which is all we
  need for the Wine tests.

### Windows User Account Control

- If you are running Windows Vista or greater with UAC turned on, you
  will get UAC prompts for some of the tests. The tests are supposed to
  gracefully deal with those but may fail to do so. To sidestep the
  issue you can run WineTest by right-clicking on it and selecting 'Run
  as administrator', or by starting from a shell running as
  administrator.

### DirectX

- Even with a fully updated Windows system you will be missing some
  DirectX libraries, typically d3dcompiler_43 and the d3dx9_\* dlls,
  thus causing some tests to be skipped. To avoid that install the
  [latest version of DirectX](https://www.microsoft.com/download/).

## Running WineTest in Wine

The procedure is the same as on Windows except that:

1.  You would use the wine script to run the 32-bit tests and wine64 to
    run the 64-bit ones.
2.  If you built Wine from source you already have WineTest and can run
    it with `wine ./programs/winetest/winetest.exe.so`
3.  The WineTest website only accepts test results from unpatched Wine
    sources.

If you are running the tests unattended you will likely want to disable
winedbg's 'crash dialog' to avoid long delays whenver a test crashes. To
do so, run something like the command below before starting WineTest.

```sh
$ ./wine regedit.exe - <<__EOF__
[HKEY_CURRENT_USER\Software\Wine\WineDbg]
"ShowCrashDialog"=dword:00000000
__EOF__
```

### Unix notes

- To avoid skipped tests, in particular in gdiplus:font, it is
  recommended to install the following Microsoft fonts: Arial, Courier
  New, Microsoft Sans Serif and Times New Roman. On Debian most of
  them are provided by the ttf-mscorefonts-installer
  package. Alternatively, one should at least install the Liberation
  fonts.

- Message-sequence tests usually fail because of window manager bugs.
  Alexandre has been working with window manager developers to get these
  fixed. At the moment, known good window managers are metacity 2.23.8
  or later, fvwm 2.5.26 (older versions may be fine too on 32-bit
  platforms), probably KDE 3.5.8 or greater too. So if you are seeing
  message sequence failures, check to see if switching to one of the
  above window manager versions helps.

- A missing libjpeg library will cause a number of test failures. So if
  you compiled Wine from source make sure the configure script did not
  complain about it. Also make sure that there is no mismatch between
  the headers and the library you link with, like using the libjpeg62
  headers but linking with libjpeg.so.8. This is particularly important
  if you have both 32-bit and 64-bit versions of this library.

- You need a functional ntlm_auth binary otherwise you will get some
  rpcrt4 test failures. Note that on some systems, ntlm_auth is present
  by default but does not work because there is no smb.conf file.

- Insert an audio or mixed audio+data CD-ROM or DVD in a drive otherwise
  winmm:mcicda and ntdll:cdrom skip some tests.

### Mac OS

- Apple's X11 server is buggy and will result in a lot of test failures,
  especially on Leopard or older. So you should install and use
  [XQuartz](https://xquartz.macosforge.org/trac/wiki) instead.

- Depending on the [MacOS](MacOS) settings, the application
  firewall may ask whether to allow [wineserver](Commands/wineserver)
  or some of the tests to accept incoming network connections. There is
  no need to worry about it, and answering either way won't impact the
  results. The reason is that the firewall always authorizes connections
  originating from the local address which is all we need for the Wine
  tests.
