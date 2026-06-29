Or for those who like to be buzzword compliant, the Wine Testing Cloud
Service. The Wine Testbot is a collection of (thoroughly vetted) virtual
machines we have running at WineHQ, and now with an approved account,
you too can submit your tests to run on several Windows environments.

## Getting Started

If you're interested in using the TestBot service, the first thing
you'll want to do is register; you can begin by clicking the "Register"
link [at the TestBot page](https://testbot.winehq.org). Once your
account is approved (you'll be notified via email), you can login.

When logged on, the navigation sidebar will include the option to submit
a job, allowing you to upload tests in one of two formats:

- A Windows '.exe' (possibly cross-compiled on unix)
- A unified diff patch in the style of `git diff` (the TestBot will
  compile it for you)

You can also select which Windows releases (we have both 32 and 64-bit
versions) you want to run your tests on.

We trust our developers to use this service appropriately so **don't**
abuse the privilege by trying anything questionable. In addition to
automatic safety measures, we have access to all of the images' logs and
consoles.

After your job has been submitted, you can check on its status from the
TestBot homepage; you can also see more detailed progress info by
clicking on the job ID. When the job completes, the results will be
published on the TestBot page. Just to be safe, there are some failsafes
built into the system; a major one is a 5-minute timeout (the
[Conformance Tests](Conformance-Tests) have a similar policy)
so try to design considerate, reasonable tests.

TestBot results are not private and can be seen by anyone visiting the
TestBot page.

Even if you don't ever register with the TestBot service, you'll be
interacting with it in the form of Marvin. This bot automatically scans
all submissions to the wine-patches mailing list for changes to
[Conformance Tests](Conformance-Tests) first. Then it
rebuilds the changed tests and runs them on all Windows images to
guarantee the changes don't break anything. Marvin should mail back the
results of those tests to the submitter, and if it determines there are
any new failures (vs. the current version of `winetest.exe` from
WineHQ), it will email both the submitter and the wine-devel mailing
list.

Marvin only handles complete series of patches. If you submit a series,
Marvin will queue your first patches until it has received the full
series, then combine them into a single patch to test all at once.

## How It Works

Only patches that contain changes to tests are run so the TestBot checks
for changes to files of the form *dlls/<dllname>/tests/\** . This is
intended to cover the vast majority of cases but is not 100% failproof
(for example, changes to *include* files may not trigger the tests
depending on that header). Before each test run, the selected VMs are
also reset to a clean snapshot to ensure good build hygiene.

For each Windows release, we have a "basic" VM that runs the most
up-to-date, popular version of that release. However, we also try to
provide VMs that test other variations of your release. For example, the
basic XP image uses XP Professional SP3, but we have other images for
SP2, Media Center Edition, etc. Of course, we still cannot exhaust every
possible configuration of Windows, but these extra datapoints still help
immensely.

Because the TestBot is completely virtual, we recommend also running
your test (using a custom build of Wine's unit-test suite) on at least
one physical Windows machine, even if everything checks out with the
TestBot.

## Questions

If you have any questions or suggestions for the TestBot maintainers,
you can contact them through the web-interface. You can also report
issues on the WineHQ Bugzilla; just remember to select **Wine-TestBot**
as the product when you write up your report.

The TestBot source code is licensed as LGPL and is available from the
**tools** repository of WineHQ's git tree. You can [browse the source
online](https://gitlab.winehq.org/winehq/tools/-/tree/HEAD/testbot) or
clone it to your system with git:

```sh
$ git clone https://gitlab.winehq.org/winehq/tools.git
```

## Some History

We have Ge van Geldorp (peace be upon him) to thank for laying the
groundwork of the TestBot service. After several discussions about
testing at WineConf 2009, [he took it upon
himself](https://www.winehq.org/pipermail/wine-devel/2009-November/080131.html)
to setup and manage the first servers and their VMs, not to mention
writing the web-interface and Marvin, our friendly patch-checking bot.
Even the first edition of this page was his work.

After his passing, the service was migrated to new machines at
CodeWeavers, and since then, we have been updating the VMs to provide
modern Windows environments and doing further testing to ensure the
TestBot results are valid.

## See also

- [Wine TestBot VMs](Wine-TestBot-VMs) has details on how the
  VMs are configured

- [Daily results for Wine's test suite](https://test.winehq.org/data)
  (download link for `winetest.exe` at the bottom of the page)
