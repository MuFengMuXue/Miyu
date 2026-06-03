For some time now, [unit
testing](https://en.wikipedia.org/wiki/Unit_testing) has proven to be a
valuable quality-assurance method. The technique allows a computer to
grind through all of the possible code that a change might destabilize
with subtle side-effects. This approach not only preserves much higher
code-quality but also spares developers from many tedious hours (and
migraines) spend on debugging.

Wine has had its own suite of [Conformance
Tests](Conformance-Tests) since ca. 2003 to keep bugs from
sneaking into the source tree. Since the tests can also be run on
Windows, this has been a great black-box method to collect data on how
wine's behavior still differs from Windows'. This is especially true of
bugs-become-features and other undocumented parts of the API that
real-world programs rely on.

That said, we can only develop so many tests ourselves, but fortunately
there are even more ways to let the machines do some debugging for us.
Since the goal is for wine to interact with Windows API programs
indistinguishably from Windows, we can use high-quality, mature test
suites from other projects to spot deviations. You can think of this as
very similar to how chemists use [standard
reagents](https://en.wikipedia.org/wiki/Primary_standard#In_chemistry)
for precise results, even if they don't have direct access to the tools
that set the standard.

## Basic Tips

If you have a test-suite already designed to run on Windows, then you
should be able to just execute it in Wine and watch the sparks fly. Just
be sure to also run the test suite on at least one or two Windows
machines for comparison, especially if it's not a particularly mature
test-suite. Errors that appear on both may still be valid problems in
wine, but the deviations should have priority.

One particularly nice class of test-suites to try are ones developed for
programming languages. Many are totally open-source, made to be
cross-platform, and easy to run. For example, if you've installed a
recent Windows release of Python3 to your wine prefix, you can try
running the default test suite with one line:

`wine 'c:\path\to\python.exe' -m test`

The one trade-off with language test-suites is that the interpreter /
compiler involved inevitably adds another layer between the actual test
and wine. This can make it a little harder to interpret failed test
results sometimes.

By contrast, project unit-tests written in C or C++ may not always be
packaged as nicely, but they should run well on wine. Furthermore, by
eliminating any intervening software and staying closer to bare metal,
these tests will often point directly to the issue in wine, making them
a great tool for digging up bugs.

Say you've found something with a foreign test-suite and want to report
a bug on our Bugzilla. To make tracking bugs easier, consider appending
the project's short name in parentheses at the end of your report title.
For example, "(Apache)", "(Firefox)", or "(Ruby)"

## Projects with Buildbots

"Success story" pages by build-and-test systems, aka "continuous
integration" (CI), are one great way to find test-suites. One can
typically follow links to the project's actual test-rig instance, with
details about the project's current status vis-a-vis different
configurations, including Windows. Every project that's been doing fine
on Windows for a while is a prime candidate for testing against wine.

Many of the projects may not necessarily be built on Windows, but here
are grocery-list pages for some different CI suites:

- [Buildbot](https://buildbot.net/trac/wiki/SuccessStories)
- [Jenkins](https://wiki.jenkins-ci.org/pages/viewpage.action?pageId=58001258)
  has a list of open-source projects midway down the page

Of course, if you've stumbled across another project with a test-suite
that performs solidly on Windows, you're always free to use it.

A major reason we prefer test-suites from projects using CI is that
there's a higher risk of flaky tests otherwise. It's often only after a
project starts running their tests continuously that the flawed and
chaotic unit tests are exposed and fixed. Don't be discouraged from
trying an interesting test-suite, even if the project doesn't test
continuously. Just keep in mind that such test results will be viewed as
less reliable by default.

## Windows-oriented Gizmos

There are a few other interesting tools out there that may not count as
full test-suites, but could still serve a useful function for testing
wine's compatibility with Windows.

The first is a small app called [Control
Spy](https://msdn.microsoft.com/en-us/library/windows/desktop/bb773165%28v=vs.85%29.aspx),
designed and provided by Microsoft itself for debugging Windows control
objects. In the past, this tool helped us uncover a few bugs.

At one point, there was a [debate on Bugzilla](#239) about whether
using Control Spy v2 to test wine violates Microsoft's EULA. If you
are interested in using Control Spy to debug wine, you should
definitely **ask the wine-devel mailing list first** and wait for an
ok.

Another handy program, which can also open up new horizons for testing
on wine, is [AutoHotkey](https://www.autohotkey.com). Besides automating
many everyday tasks on Windows (and wine), with a little ingenuity, you
can whip up your own bespoke automated tests. At one point in fact,
Austin English was developing a script framework called Appinstall; it
would use AutoHotkey to automatically test installation and more for a
wide range of programs. This project has been dormant for a while, but
may be revived in the future (see [Winezeug](Winezeug) for
more info).

Finally, while there haven't been any updates for newer versions of
Windows, [Francois Gouget](@fgouget) had the inspired
and sneaky idea to re-purpose the code snippets from programming books
into a simple test-suite of sorts. You can read more about his method
and observations [on his
web-page](https://fgouget.free.fr/wine/booktesting-en.shtml).

## See Also

- [Debugging Hints](Debugging-Hints)
- [Wine TestBot](Wine-TestBot)
- [Static Analysis](Static-Analysis)
- [Wine and Valgrind](Wine-and-Valgrind)
- [Cygwin and More](Cygwin-and-More)
