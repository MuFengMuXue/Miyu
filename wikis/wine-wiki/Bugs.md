This page is for notes on how to use Bugzilla to report and triage bugs.
There is also some generic information on [writing good bug
reports](https://bugs.winehq.org/page.cgi?id=bug-writing.html).

## When to report a bug

You should report a bug when:

- Wine doesn't run a program the same way as Windows does (e.g. crashes)
  with the default Wine configuration (i.e. no dlls from Windows, or
  `DllOverrides` set).

- You are using the **latest *development* version** of Wine (not
  stable) (See [downloads](Download) for information on how to get the
  latest).

- You tested with a **clean** Wine directory (default location:
  `~/.wine`, z: drive -\> / link exists, no DLL overrides).

- You [installed and
  ran](Wine-User's-Guide#how-to-install-and-run-windows-programs)
  the application using Wine, not on your Windows installation.

- Your system isn't at fault (system hangs/lockups that require a system
  reboot are usually driver problems).

- Your system has all the libraries that Wine needs.

- You haven't modified Wine in any way; i.e. you are using a prepackaged
  binary without any custom patches or modifications or have built from
  the official WineHQ source by doing:

```sh
$ ./configure
$ make
```

- You are **not** using a third party wrapper for Wine (e.g., Crossover,
  PlayOnLinux, PlayOnMac, Wineskin, Q4Wine, etc.) or custom patches.

- You have searched [Bugzilla](https://bugs.winehq.org), and the
  problem hasn't been reported already. Check [Known
  Issues](Known-Issues) as well.

- Also search for the application in the
  [AppDB](https://appdb.winehq.org) and look at the bug links for that
  application, as it could be already reported.

## How to report

Each bug report should cover ***one*** problem. If there are additional
problems with the same application or game, file separate reports for
each. If a similar problem appears with multiple applications or games,
file separate reports for each. No, really. Even though it may look the
same to you, the underlying problem is likely different. If it really is
the same, we'll resolve the report as duplicate afterward.

Go to [Bugzilla](https://bugs.winehq.org), login, and click [Enter bug,
then Wine](https://bugs.winehq.org/enter_bug.cgi?product=Wine).

- Put the name of the application in the **Summary** field, followed by
  a short description of the error, e.g.

  `WinZip 7: crashes when extracting a zip archive`

  Use a summary explaining the bug symptoms and the name *and version* of
  the program that displays them, not what you think the problem is, so
  that:
    - Users can find duplicates
    - The problem can be marked as solved by checking that the symptom
      is gone
    - The bug remains valid even if your analysis is incorrect

- Describe the bug in the **Comments** field, e.g. how to make the crash
  happen:

  `Wine crashes when I click on the Extract button on the toolbar in WinZip 7.01`

  If you have any clues as to what the problem is, write them in here.
  Don't paste too much information in the comments field, just what
  looks relevant. **Do not paste** backtraces or error logs in the
  comments field (**attach** them instead). For bugs related to
  graphics, sound, and hardware devices, be sure to write down what
  hardware and drivers you're using.  [Here is an example of what NOT
  to do](https://bugs.winehq.org/show_bug.cgi?id=7661#c0).

- Set Product to Wine and **specify Wine version** you are using, if
  in doubt run `wine --version`. If you are using wine-staging,
  mention this in the comments.

- Provide a download link to a free version of the program / program
  installer that shows the bug if possible, e.g.
  [`https://download.winzip.com/ngs/winzip175.exe`](https://download.winzip.com/ngs/winzip175.exe)

  The download link should point to the *exact* program version you
  encountered the bug with (to improve reproducibility). Ideally also
  provide a SHA1 checksum of the installation file, along with the
  filename, e.g.

  ```sh
  $ sha1sum winzip175.exe
  885c7e4ea128351e5fe325d98344f27a46222d73  winzip175.exe
  ```

  This makes it easier for other people to try to reproduce the bug
  using the same program version, especially when the original
  download link is broken and it has to be retrieved elsewhere.

- Attach [**complete terminal
  output**](FAQ#how-can-i-get-a-debugging-log-aka-terminal-output)
  to the bug. Please **do not paste** [backtraces](Commands/winedbg)
  or error logs in the comments field, but *attach* them to your bug
  report (use a `.txt` file extension, or set MIME type to
  `text/plain`). If a file is large, compress it first (e.g. with gzip
  or xz). If you have many files to upload (i.e. more than two), please
  use an archive (e.g. tar) rather than uploading them all individually.
  Also, please do not paste to the Wiki, AppDB, or the IRC channel. A
  trace may be temporarily stored at a
  [Pastebin](https://en.wikipedia.org/wiki/Pastebin) so it can be
  referred to on IRC (it should still be attached to the bug report
  itself so everything is archived in one place).

<div id="severity">
</div>

- Set the importance to
  - **Trivial** for a UI glitch that doesn't affect running of a program
  - **Minor** for minor loss of functionality, or other problem where an
    easy workaround is present
  - **Normal** for an application crash or other issue
  - **Major** for major loss of functionality for a wide range of
    applications
  - **Critical** for a critical problem that prevents **all**
    applications from working
  - **Blocker** when development and/or testing work cannot be done

  For the above example, the severity is **Normal**. Severity levels
  above Normal should only be set by experienced users or bugzilla
  admins, and are not even necessary for 99% of issues. Also, after
  making your initial report, please leave changing the bug's severity
  to someone with admin permissions.

- After you have submitted your bug, please add it to the appropriate
  [AppDB](https://appdb.winehq.org) page(s). If there is no entry in the
  [AppDB](https://appdb.winehq.org) for an application, it might be
  helpful to add one (though that is not required for the bug report).

## Do's and Don'ts

### Do:

- :white_check_mark: Specify your distribution and architecture.

- :white_check_mark: Write your bug report in English. While many
  developers speak other languages, English is the language of choice
  for Wine.

- :white_check_mark: Include a download link (if one is available)
  from the software's website.

- :white_check_mark: Select appropriate keywords in your report (a
  list of accepted keywords is
  [here](http://bugs.winehq.org/describekeywords.cgi)).

- :white_check_mark: **Attach** terminal output (instead of pasting it
  in a comment).

- :white_check_mark: Attach small files that clarify the problem
  (e.g. a screenshot for visual bugs, a sample script for scripting
  engines)

- :white_check_mark: Check on your bug every release or two and let us
  know if the bug is still present. If not, mark it fixed.

- :white_check_mark: Attach the bug to the correct application in the
  [AppDB](https://appdb.winehq.org).


### Don't:

- :x: Change the reported version. It should reflect the earliest
  version of Wine that had the bug. Don't update it every time you
  test for the bug.

- :x: Attach large files such as executables unless they are
  explicitly requested (link to a legitimate download page instead)

- :x: Use pirated/cracked software.

- :x: Post links to file-sharing websites to download executables
  instead of the developer's site.

- :x: Ask when the bug will be fixed. If a fix is in progress, it'll
  likely be posted in the bug.

- :x: Close fixed bugs. We'll close it whenever the next release is
  made.

- :x: cc yourself to bugs you have reported (the system will notify
  you of updates regardless) or reply to email notifications of bug
  updates (add your comment using the webpage).

## Bugzilla Policies

Some general policies for WineHQ's
[Bugzilla](https://bugs.winehq.org/describekeywords.cgi):

- Bug reporters are expected to check their bug on newer Wine versions
  periodically (3-6 months) and to update the bug if it's fixed or still
  present. If it's still present, simply a comment saying still in
  wine-x.y.z is enough. If the behavior of the bug has changed in any
  way, please update the bug with that info as well as an updated log.
- The NEEDINFO status should be used for bugs where:
  - the reporter did not provide enough information to act on (missing
    program name, no terminal output, etc.),
  - there has been no comment on the bug within 1 year AND no download
    is available to test (or the download is not enough on its own,
    e.g., a login is required).
- Bugs that are NEEDINFO for one year will be CLOSED ABANDONED.
- Please don't CC yourself on EVERY bug, this spams a lot of people.
  Users who do this are subject to a ban. If you want to watch all
  bugs, [subscribe to
  wine-bugs](https://list.winehq.org/mailman3/postorius/lists/wine-bugs.winehq.org/).
- All Wine developers are entitled to bugzilla triage permissions. If
  you don't have them, contact
  [Austin English](@austin987) or send an email to
  bugs-admin@winehq.org

## See Also

- [Known Issues](Known-Issues)
- [Bug Triage](Bug-Triage)
