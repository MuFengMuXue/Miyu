Over the years, Wine contributor Dan Kegel built up a veritable
steamer-trunk of interesting scripts for testing, tweaking, and
otherwise teaching Wine and WineHQ to do all kinds of tricks (even the
early versions of [Winetricks](Winetricks)). For those
interested in sorting through all his tools, keep on reading.

This page is not intended to be permanent. The goal is to keep hints and
major notes here while doing some code archaeology on the Winezeug repo,
a project that probably has at most a time-horizon of a few years (and
much shorter if someone prioritizes it).

## Getting Winezeug

Winezeug was originally hosted on Google Code, but when Google began
unwinding their code hosting service, it was automatically exported to
Github. As of this writing, winezeug was last updated a year and a half
ago by Austin English and there's no sign that Dan's repo will be
actively maintained.

Still if you're interested in downloading it as Dan left it on Google
Code, you can clone it through git:

```
git clone https://github.com/dankegel/winezeug.git
```

However, there are still occasional changes to Winezeug, and the repo
hosted alongside winetricks appears to be upstream:

```
git clone https://github.com/Winetricks/winezeug
```

Kyle Auble has also forked Dan's repo on his Bitbucket account and
plans to dig through it from time to time, pushing any changes back to
Bitbucket:

```
git clone https://bitbucket.org/kauble/winezeug-archaeology-v2.git
```

## Preliminary Observations

From a very cursory glance, the code in the repo seems to fall into
several categories:

- Random simple tests and cruft (the easy stuff to clear out)
- Helper / Installer scripts, including early versions of winetricks and
  related tools
- Some basic prototypes of an approach to prefix management
- A couple of web-scrapers to mine the AppDB and report on popular
  titles (according to gamerankings.com)
- Shims for using different testing tools on Wine
- A collection of examples for trying out the Cmake build tool
- Alternative versions of a possible testbot

When the repo was exported to Github from Google Code, the few wiki
pages were loaded into a distinct *wiki* branch of the repo. However,
only the ConvergedFrontends file was not entirely obsolete or superseded
by the winetricks wiki, and it has now been merged into the [Bottling
Standards](Bottling-Standards) page on this wiki.

## Potentially Valuable Parts

### AppDB Mashup / Gamerankings Scraper

These are some shell scripts for scraping records from the Gamerankings
website, linking them to AppDB entries, then displaying some tables.
Even if the scripts themselves don't really have fragments worth
polishing, the idea itself is interesting; maybe the could be
reimplemented as a fun AppDB enhancement.

### Appinstall

Austin English developed a wrapper script called Appinstall that would
configure the [AutoHotkey](https://www.autohotkey.com/) automation tool
in a wine prefix, then use it to test installing various Windows
programs. This is one of the ideas in Winezeug aimed at what a still
active problem: how can we get more digestible test data from actual
programs in the wild.

Because of that, there's a good chance Appinstall won't be entirely
unwound but rather revived in a new repo. In addition to the operational
files being cleaned up, the docs will also get cleaned up, fleshed out,
and merged with notes from the old wiki. After a little more inspection,
winetricks already supports AutoHotKey as a verb, and it may be possible
to keep the Appinstall scripts in their own repo, as a sort of extension
to [wt-daily](Conformance-Tests#getting-wt-daily).

### BuildBot & Patchwatcher

For now, this info makes sense here. Once these parts of winezeug have
been thoroughly digested though, the paragraphs below (with updates)
probably belong more on some part of the [Wine TestBot](Wine-TestBot)
page.

[BuildBot](https://buildbot.net/) is a mature, open-source continuous
integration (build-and-test) service written in Python. It can be
operated as a distributed installation, with a master server
automatically pushing jobs out to slave servers. Dan Kegel and Jeremy
White setup a BuildBot farm at WineHQ several years ago for feasiblity
tests, before we settled on our current
[Wine TestBot](Wine-TestBot). It would monitor the
wine-patches mailing list, automatically sending errors to Dan, who
would personally filter out the false positives, then email the
submitter and wine-devel about any legitimate errors.

Prior to the BuildBot test instance, Wine relied on Patchwatcher, a
custom testbot whipped up by Dan to automatically check submitted
patches against Wine [Conformance Tests](Conformance-Tests).
After all these bespoke scripts became too much of a hassle to maintain
though, the wine team decided to try other options, including existing
projects like BuildBot or [Jenkins](https://jenkins-ci.org/).

Our current Wine TestBot gets the job done fine, but if we ever decide
to transition to BuildBot, the groundwork done by Dan & Jeremy could
give us a nice headstart.

### CMake Sample Projects

Dan worked through a series of simple projects to practice using the
CMake build system. While some of the work consisted of very trivial
steps or wrangling Eclipse workarounds, there was also a lot of useful
info about getting started with CMake. However, most of this is
superseded by existing tutorials; there are a few bits that focus on
targeting multiple platforms and mixing Java with C/C++ (by way of JNI)
that don't seem to be discussed by any other tutorials out there.
Perhaps the authors of the better tutorials would appreciate these
samples to work into their own documents, but if there's no interest,
there's no need to keep these.

### Miscellanous

There are a few scripts that don't really fit into one category. Some
help with getting build dependencies, others run [Guest Unit
Tests](Guest-Unit-Tests) or scan the code for certain errors;
there's even occasionally a new script for the repo. We need a little
more digging to see what's worth keeping of the old scripts though.

### Valgrind Tools

Winezeug contains a grab-bag of useful scripts, config files, and even a
couple patches for applying valgrind to wine. Sorting through what's
still relvant and what's obsolete may take a little time.

### Winetricks-y Things

There are a few scripts that were part of very early winetricks
versions, but have since fallen by the wayside. For the most part,
they're just obsolete, but a couple add features (like anonymous usage
data) that don't seem to be in winetricks currently. They may be worth
putting back together and merging back into winetricks proper.

### Yagmark

Another interesting idea directed more at diagnosing performance issues
in wine (and feeding our ego by comparing them to Windows) was yagmark.
Dan developed this set of scripts to automatically install and configure
several graphics benchmarks in a prefix, then run them before processing
the results.

This is still a cool idea for sure, and considering many wine users run
graphics-intensive games, performance testing is still something where
we could use more precision and systemization. However, since winetricks
has several verbs to download graphics benchmarks, it seems most of this
program can be set aside, though a way to collate and report results
might be good to work on.
