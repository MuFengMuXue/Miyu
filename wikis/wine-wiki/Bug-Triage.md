Because there are so many Windows applications out there, and because
very few of them work perfectly, we get a lot of questions from users,
many bug reports that need to be diagnosed, and many bugs to fix. This
makes bug diagnosis and support two closely related activities that are
very important to Wine. We can always use more people willing to respond
to issues that pop up on the [User Forum](https://forum.winehq.org) and
[Bugzilla](https://bugs.winehq.org) and help triage them.

## Initial Responses

When first handling a bug report, email, or forum question, the
following guidelines tend to work well:

- General Wine issues and questions can usually be answered in a direct
  reply, using the same method of the original question
- For application-specific issues, please check first with the program's
  AppDB Maintainers (if there are any) to see if the issue is already
  known (ideally such issues should be listed in that application's
  entry in the [AppDB](https://appdb.winehq.org))
- Other issues require more work to determine whether the problem is
  reproducible and what environments it specifically affects. Forming a
  hypothesis about where the problem may exist is an important skill
  because it usually takes the right debug options to get useful logs
  that will help the developers fix the problem.
- If the problem cannot be quickly resolved on the mailing list or
  forum, create a bug report in bugzilla.

## Triaging Fresh Bugs

Many times, new bug reports are not in a condition that most developers
will be able to work with. That's where triaging comes in. Start by
making sure the bug is not a duplicate of another bug by searching for
the program's name, the error reported, or other salient points. Also
take a look at the [list of most frequently reported
bugs](https://bugs.winehq.org/duplicates.cgi) to make sure it's not a
commonly reported issue. If so, mark it as a duplicate, but if the bug
does appear to be original, fill in missing information if possible. If
there is not enough information in the bug for anyone to act on it, ask
the reporter for the information that is needed and mark the bug
NEEDINFO.

After filling in any missing information, it's a good idea to try to
verify the bug if possible. This should definitely be doable for any
program with the **download** keyword. Download and test for the
problem, making sure to start with a clean wine prefix. If you don't
have access to the program or know how to test it, ask the reporter to
give a step-by-step guide to reproduce the issue. If you can reproduce
the error, you can confirm the bug and begin helping the developers
narrow down the exact cause. If you cannot confirm the bug, be sure to
ask the reporter to retry testing for the bug *in a clean .wine
directory*.

A useful experiment to try after this is seeing if switching in any
native DLLs help fix the bug. Running the program with
`WINEDEBUG=+loaddll wine program.exe` will tell you what DLLs were
loaded. If a one or more native DLLs fix the issue, uploading a log
with a trace of that component will usually help whichever developer
claims the bug. If native DLLs don't help, running the program with
`WINEDEBUG=+relay,+tid,+seh wine program.exe` or `WINEDEBUG=warn+all
wine program.exe` are two more tests that will usually reveal some
clues.

Finally, if the bug is a regression from a previous version, ask the
reporter if they would be comfortable doing [Regression
Testing](Regression-Testing). Don't start without checking if
a clean .wine directory fixes the problem, but if this doesn't help,
suggest the regression test (if you have access to the program and can
confirm the bug, you can try the regression test yourself if you wish).
If the test succeeds, have the reporter note the patch that introduced
the bug and add the author of that patch to the report's CC list.

A few more things you may want to try include:

- Search through the **unconfirmed** and **new** bug reports and get
  them in proper shape for developers. This can include confirming them
  and suggesting debug channels for the reporter to try, among other
  things.
- Subscribe to the [wine-bugs mailing
  list](https://list.winehq.org/mailman3/postorius/lists/wine-bugs.winehq.org/). The
  list is read-only and reports every unassigned bug sent to it.

## Handling Old Bugs

Managing the status of bugs is critical to keeping the bug tracker
uncluttered, which allows developers to prioritize when addressing
problems. Here are a few guidelines about triaging old bugs:

- Mark a bug as **FIXED** if the patch that fixes the bug has been
  committed to git
  - Do **not** close **fixed** bugs (this is done by the maintainer upon
    releases)
- Mark a report as **INVALID** if the bug is:
  - Not due to Wine
  - In the application itself
  - Being run with native DLLs (doesn't apply if the reporter was asked
    to try native DLLs)
  - Uses a third party version of Wine (PlayOnLinux, Wineskin, etc.)
  - Wasn't properly installed in Wine (was copied from or is being run
    from a Windows partition).
- Mark a bug as **CONFIRMED** if a triager or multiple users have
  reproduced it
- Add the keyword **abandoned?** if there has been a request for more
  information/testing but no response for 6 months
  - Some dormant bugs should still **not** be tagged **abandoned?**.
    Bugs that have been around for years and are large scale projects
    should be left alone. On the other hand, bugs that are a year or two
    old, only about an uncommon program, and haven't had any input from
    the reporter can almost definitely be tagged. In between those
    extremes, use your judgment.
- Mark a bug as **NOTOURBUG** if it's not due to a problem in Wine
  (display drivers, kernel, etc).
  - If possible, provide the upstream bug link in the "See also" field
  - Keep an eye on the upstream bug and close the entry in Wine's
    bug-tracker once it's fixed
- If a bug has been marked **NEEDINFO** for a year, it may be **CLOSED
  ABANDONED**.

## Field Suggestions

Here are some hints about how to fill in a bug report's fields so that
the developers have as much useful info as possible:

| Field            | Notes                                                                                                                                                                                                                                                                                                                                            |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Product          | Should usually be Wine, unless the bug really does relate to something like the website or documentation. Staging should only be used for bugs that exist only in wine-staging and not in the development branch. On rare occasions, you may have Wine bugs mislabeled as a WineHQ bug for instance. If you come across one of these, change it. |
| Component        | Reporters will often fill this out wrong. Fix this if you can determine the correct component, but if you're not sure, change it to "unknown."                                                                                                                                                                                                   |
| Hardware         | If not filled in, ask the reporter to do so. It will most likely be a PC, but even then, it could be 32bit (x86) or 64bit (AMD64). Especially since some bugs seem to be specifically affect 64-bit processors, this is important.                                                                                                               |
| OS               | While Linux is most common, ask the reporter to fill it in if it isn't already instead of guessing.                                                                                                                                                                                                                                              |
| Version          | If an older version of Wine (not from Git or the latest binary version), ask the reporter to upgrade and retest. If it is blank, ask the reporter to fill it in. (Logs captured by Wine's GUI crash dialog will include this information, so you may be able to fill in this field based on that.)                                               |
| Priority         | This should always be at P2, and if it isn't, change it back. Only the developers use this on other settings.                                                                                                                                                                                                                                    |
| Severity         | People often mislabel this one, thinking any issue they have is automatically a blocker. Use the [bug severity guide](https://bugs.winehq.org/page.cgi?id=fields.html#bug_severity) to determine the proper severity.                                                                                                                            |
| Target Milestone | Don't worry about this one. The developers will take care of changing it.                                                                                                                                                                                                                                                                        |
| URL              | If the program can be downloaded somewhere, make sure the URL is here. If there isn't a download link, enter the vendor's website, or the AppDB page if one isn't available.                                                                                                                                                                     |
| Whiteboard       | Leave this blank.                                                                                                                                                                                                                                                                                                                                |
| Keywords         | Use the list of valid keywords [here](https://bugs.winehq.org/describekeywords.cgi) to fill this in. The most commonly used are **download**, **installer**, **regression**, and **source**.                                                                                                                                                     |
| Difficulty       | Leave this blank unless you intend to fix this bug yourself and have a good estimate of how long it will take you.                                                                                                                                                                                                                               |
| Depends on       | Leave this blank unless you know for certain that this bug depends on other bugs.                                                                                                                                                                                                                                                                |
| Blocks           | Leave this blank unless you know for certain that this bug blocks some other bug.                                                                                                                                                                                                                                                                |

## Useful Queries

Here are a few queries that you might find especially useful when
looking for bugs to triage:

- [All **unconfirmed** bugs with the **download**
  keyword](https://bugs.winehq.org/buglist.cgi?query_format=advanced&short_desc_type=allwordssubstr&short_desc=&product=Wine&long_desc_type=substring&long_desc=&bug_file_loc_type=allwordssubstr&bug_file_loc=&status_whiteboard_type=allwordssubstr&status_whiteboard=&keywords_type=allwords&keywords=download&bug_status=UNCONFIRMED&emailassigned_to1=1&emailtype1=substring&email1=&emailassigned_to2=1&emailreporter2=1&emailcc2=1&emailtype2=substring&email2=&bugidtype=include&bug_id=&votes=&chfieldfrom=&chfieldto=Now&chfieldvalue=&cmdtype=doit&order=Importance&field0-0-0=Bug+creation&type0-0-0=noop&value0-0-0=)

- [All **open** bugs with a **download** keyword and no activity for
  90
  days](https://bugs.winehq.org/buglist.cgi?query_format=advanced&short_desc_type=allwordssubstr&short_desc=&product=Wine&long_desc_type=substring&long_desc=&bug_file_loc_type=allwordssubstr&bug_file_loc=&status_whiteboard_type=allwordssubstr&status_whiteboard=&keywords_type=allwords&keywords=download&bug_status=UNCONFIRMED&bug_status=NEW&bug_status=ASSIGNED&bug_status=REOPENED&emailassigned_to1=1&emailtype1=substring&email1=&emailassigned_to2=1&emailreporter2=1&emailcc2=1&emailtype2=substring&email2=&bugidtype=include&bug_id=&votes=&chfieldfrom=&chfieldto=Now&chfieldvalue=&cmdtype=doit&order=Reuse+same+sort+as+last+time&field0-0-0=days_elapsed&type0-0-0=greaterthan&value0-0-0=90)
  (This is a good place to check for abandoned or invalid reports)

- [All bugs that have not had any activity for 6
  months](https://bugs.winehq.org/buglist.cgi?query_format=advanced&short_desc_type=allwordssubstr&short_desc=&product=Wine&long_desc_type=substring&long_desc=&bug_file_loc_type=allwordssubstr&bug_file_loc=&status_whiteboard_type=allwordssubstr&status_whiteboard=&keywords_type=allwords&keywords=&bug_status=UNCONFIRMED&bug_status=NEW&bug_status=ASSIGNED&bug_status=REOPENED&emailassigned_to1=1&emailtype1=substring&email1=&emailassigned_to2=1&emailreporter2=1&emailcc2=1&emailtype2=substring&email2=&bugidtype=include&bug_id=&votes=&chfieldfrom=&chfieldto=Now&chfieldvalue=&cmdtype=doit&order=Reuse+same+sort+as+last+time&field0-0-0=days_elapsed&type0-0-0=greaterthan&value0-0-0=180&field0-1-0=keywords&type0-1-0=notsubstring&value0-1-0=abandoned)
  (Many of these can probably be tagged as **abandoned?**, but should
  not be closed yet)

- [All bugs with an **abandoned?** keyword and no activity for 6
  months](https://bugs.winehq.org/buglist.cgi?query_format=advanced&short_desc_type=allwordssubstr&short_desc=&product=Wine&long_desc_type=substring&long_desc=&bug_file_loc_type=allwordssubstr&bug_file_loc=&status_whiteboard_type=allwordssubstr&status_whiteboard=&keywords_type=allwords&keywords=abandoned?&bug_status=UNCONFIRMED&bug_status=NEW&bug_status=ASSIGNED&bug_status=REOPENED&emailassigned_to1=1&emailtype1=substring&email1=&emailassigned_to2=1&emailreporter2=1&emailcc2=1&emailtype2=substring&email2=&bugidtype=include&bug_id=&votes=&chfieldfrom=&chfieldto=Now&chfieldvalue=&cmdtype=doit&order=Reuse+same+sort+as+last+time&field0-0-0=days_elapsed&type0-0-0=greaterthan&value0-0-0=180)
  (Almost all of these can be closed as abandoned without problems)

## FAQ

### Why has my bug been marked as FIXED?

There are two reasons why a bug may be marked as fixed.

1.  A user has tested the application in a newer version of Wine and has
    confirmed that the issue has been fixed.
2.  A patch has been committed to the Wine source tree which will likely
    fix the bug.

If you find that your application still fails in the same way using the
latest version of Wine (which may need to be built from source) then
reopen the bug and state that this is the case. **Do not** reopen the
bug if you experience a new bug or a different problem. If there is a
new problem with your application then you need to file a new bug.
Metabugs will be closed invalid.

### Why has my bug been marked as STAGED?

This means that an experimental fix for the bug has been checked into
the staging branch, but it is not yet ready for inclusion in the
development branch.

### Why has my bug been marked as ABANDONED?

A bug report is marked as abandoned after a long period of inactivity.
You will have been asked to update the current status of the bug, to
test a workaround or to test in a new version of Wine but have not
responded to the request. This inactivity leads to the logical
conclusion that you have lost interest in resolving the issue and it has
been abandoned.

You may choose to update the bug with the information requested. At this
point you can reopen the bug if you wish to do so. Filing a new,
duplicate bug serves no useful purpose.

### Why has my bug been marked as INVALID?

There are a number of reasons why a bug report may be marked as
invalid.  The easiest way to avoid this is to read [Bugs](Bugs)
carefully.

- The bug exists in the application or game (behaves the same way on
  Windows).
- The bug is in your software or your set-up, not in Wine.
- Your wineprefix is not clean.
- You are using a third party or patched version of Wine.
- You have not properly installed the application/game in Wine.
- Your hardware is not suitable. For example: a graphics-intensive game
  may require a powerful graphics card and lots of memory, but your
  system is inadequate.
- The triage team believe that no bug existed, and you have failed to
  provide enough evidence that it does.

### Why has my bug been marked as NOTOURBUG?

A bug is marked as upstream if the bug you are experiencing does not
exist in Wine, but on a package that Wine depends on. A bug needs to be
filed with the package maintainer. See [the list of most duplicated
bugs](https://bugs.winehq.org/duplicates.cgi) and [NOTOURBUG
Bugs](https://bugs.winehq.org/buglist.cgi?query_format=advanced&list_id=120445&bug_status=UNCONFIRMED&bug_status=NEW&bug_status=ASSIGNED&bug_status=REOPENED&bug_status=RESOLVED&bug_status=CLOSED&resolution=NOTOURBUG).
