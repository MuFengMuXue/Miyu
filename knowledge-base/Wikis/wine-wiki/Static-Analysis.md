[Static analysis](https://en.wikipedia.org/wiki/Static_code_analysis) is
a technique for finding bugs just by looking at source code without
actually running it. That's great because it can find bugs that are
really hard to trigger.

## Current Tools

### Coverity

[Coverity](https://coverity.com) is a static analysis service that offers
free, periodic scans to many open source apps, including Wine. You can
see a result summary for the most recent scan at [Wine's Coverity
page](https://scan.coverity.com/projects/wine).

To see detailed results, after setting up an account (you can also just
login with an existing Github account), you need to be granted access
rights as a member of the project. Our official contacts are [Paul
Vriens](https://www.winehq.org/pipermail/wine-devel/2007-March/055416.html)
and [Jan
Zerebecki](https://www.winehq.org/pipermail/wine-devel/2007-March/055428.html)
so you'll want to email them to request privileges.

When posting patches to fix bugs found by Coverity, please include
**(Coverity)** in the subject line. If you're interested, you can see
a [list of Coverity-related patches in
Wine](https://gitlab.winehq.org/wine/wine/-/commits/master?search=coverity).

### PVS-Studio

[PVS-Studio](https://www.viva64.com/) is a commercial static analysis
tool, and the developing company kindly runs [scans on open source
projects](https://www.viva64.com/en/a/0084/) from time to time. For those
interested in purchasing the tool, it integrates into Visual Studio and
has a deeper knowledge of the Windows API.

While this has the benefit of finding unique defects in Wine, there are
also a ton of "intended behaviour" cases, especially in the Wine tests.
Nevertheless, quite a few [Wine
commits](https://gitlab.winehq.org/wine/wine/-/commits/master?search=PVS-Studio)
can be credited to PVS-Studio. If you submit a patch to fix a bug found
by PVS-Studio, be sure to include **(PVS-Studio)** in the subject line.

Here are some other reports done by PVS-Studio for Wine code:

- The [second analysis](https://www.viva64.com/en/b/0352/) from October
  2015, which also includes fixes since the first run.
- The [first analysis](https://www.viva64.com/en/b/0272/) in August 2014.
- Bugs reported by PVS-Studio [in WineHQ's
  Bugzilla](https://bugs.winehq.org/buglist.cgi?list_id=250262&product=Wine&query_format=advanced&short_desc=PVS-Studio&short_desc_type=allwordssubstr).

Besides these scans, PVS-Studio has provided some of the developers
(Michael Stefaniuc and Nikolay Sivov) with the raw data from these
analyses, as well as temporary licenses for PVS-Studio. The data can be
shared freely with Wine developers, though as XML it is hard to read but
beautiful to process.

### Coccinelle

[Coccinelle](https://coccinelle.lip6.fr) is an open source static
analysis tool developed jointly by several French research institutes.
Students at Aalborg University say [they found a number of bugs with
it](https://www.winehq.org/pipermail/wine-devel/2008-May/065508.html) in
2008; both Paul Vriens and Michael Stefaniuc have been using it since
2009 too.

When posting patches to fix bugs found by Coccinelle, don't forget to
include **(Coccinelle)** in the subject line. You can see a list of all
[Coccinelle-motivated patches in Wine's git
history](https://gitlab.winehq.org/wine/wine/-/commits/master?search=coccinelle)
Michael Stefaniuc has also shared [some Wine-oriented Coccinelle
scripts](https://people.redhat.com/mstefani/wine/coccinelle/) you might
find interesting.

### Clang Static Analyzer

[Clang](https://clang.llvm.org/) (the C-language front end to the [LLVM
compiler](https://www.llvm.org/)) includes a new static analysis tool
currently named the [Clang Static
Analyzer](https://clang-analyzer.llvm.org/). Henri Verbeet was the first
to submit patches fixing errors detected by the Clang Static Analyzer,
the [first one coming in October
2008](https://winehq.org/pipermail/wine-patches/2008-October/062650.html).

When posting patches to fix bugs found by Clang, please include
**(Clang)** in the subject line; as with the other tools, you can see
all [Clang-related patches in our git
history](https://gitlab.winehq.org/wine/wine/-/commits/master?search=clang).

## Old / Unused Tools

### Flawfinder

The same students from Aalborg University mentioned above also tried out
[Flawfinder](https://www.dwheeler.com/flawfinder/), another open-source
static analysis tool. Instead of trying to rigorously determine faulty
code logic, Flawfinder only scans the source code for C constructs that
commonly expose security flaws. Think of it as a version of `grep`
that's already been house-trained.

There [was a
discussion](https://www.winehq.org/pipermail/wine-devel/2008-August/068714.html)
about adding Flawfinder to Wine's patch-watcher at one point, but
Flawfinder returned [too many false
positives](https://www.winehq.org/pipermail/wine-devel/2008-September/068814.html)
to be much use.

### Smatch

[Smatch](https://repo.or.cz/w/smatch.git) is an open-source static
analysis tool based on sparse, the checker used by the Linux kernel. A
while back, Michael Stefaniuc adapted an existing script for Smatch Mark
1 (which was based not on sparse, but a modified version of GCC) to find
code paths with missing `LeaveCriticalSection` statements.

Scripts to find other useful things like GDI object leaks might not be
too hard to write; Michael even created a [page with more
info](https://people.redhat.com/mstefani/wine/smatch/) on using Smatch to
test Wine. However, he began experimenting with Coccinelle in Jan 2010
because it seemed to make prototyping much easier.

If you're interested in possibly using Smatch to debug Wine, the
official Smatch documentation (which is a bit scanty) is included in the
Smatch source. If you do fix any bugs found with it, don't forget to add
**(Smatch)** to the subject line of your patch. You can also see all
Smatch-related patches in the [Wine git
tree](https://gitlab.winehq.org/wine/wine/-/commits/master?search=smatch).

## See Also

- [Code Coverage](Code-Coverage) is a complementary technique
  for checking possible execution paths
- [Wine and Valgrind](Wine-and-Valgrind) has info on using
  the Valgrind suite to debug Wine at runtime
- [Debugging Hints](Debugging-Hints) lists some issues that
  regularly pop up when hacking on Wine
