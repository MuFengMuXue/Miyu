## Wine patch submission guidelines

In order to review code better and use established lines of
communication, the Wine project accepts code in the form of merge
requests on the [WineHQ Gitlab](https://gitlab.winehq.org). The process
may seem a little complicated at first, but it will probably become very
natural after just one or two submissions.

### Can I submit patches?

Not everyone can contribute code to Wine, primarily because doing so
would violate the [Clean Room Guidelines](Clean-Room-Guidelines). If
you have studied the Microsoft Windows source code, even if you aren't
under a [non-disclosure
agreement](https://en.wikipedia.org/wiki/Non-disclosure_agreement),
your patches probably won't be accepted. This is to ensure that the
Wine project does not violate any copyrights belonging to
Microsoft. Some more notes related to this can be found in the
[Developer FAQ](Developer-FAQ).

### Check your Git setup

It is important to make sure the author and email settings for your Git
repo are configured correctly.

```sh
$ git config --global user.name "Your Name"
$ git config --global user.email "me@example.com"
```

The [Git Wine Tutorial](Git-Wine-Tutorial) has more details,
but the key point is to **use your real name**. This isn't just for
developers to show a stronger commitment and establish trust, but also
helps discourage irresponsible programmers from submitting unacceptable
code (such as disassembled Microsoft components).

You will need a [Gitlab profile](https://gitlab.winehq.org/-/profile)
which must also use your real name. Please be precise; having the names
match exactly really helps identify commits.

If you haven't validated your account yet, you'll need to file a [User Verification issue](https://gitlab.winehq.org/winehq/winehq/issues/new?issuable_template=User%20verification); see the [WineHQ Gitlab policies](https://gitlab.winehq.org/winehq/winehq/-/wikis/home) for more details. Once you have, your next step is to [fork a personal copy of Wine](https://gitlab.winehq.org/wine/wine/-/forks/new) and then clone that repository to your local system.

You can then work in that local tree in any branch you choose, and when
you are ready, you push your work to your personal copy of Wine and
request that your work be merged into Wine with a merge request.

Finally, there's always a chance that someone has recently changed the
same code you are working on. To make sure your code hasn't been
superseded, be sure to update your Git repo before submitting your merge
request.

```sh
$ git pull --rebase
```

If you prefer to manage your work in separate branches, remember that
the above command will only update your **current branch** and all of
your branches need to be up-to-date. Keeping your "master" branch in
sync with WineHQ's repository and creating branches (and rebasing them
on "master") for your own changes might be a good idea. Again, the
[Git Wine Tutorial](Git-Wine-Tutorial) page goes into much more detail
on using Git to manage your work.

## Making your changes

### Code guidelines

There are two main guides for writing good C code for Wine: **[Some
notes about
style](Wine-Developer's-Guide/Coding-Practice#some-notes-about-style)**
and **[Writing portable
code](Wine-Developer's-Guide/Coding-Practice#writing-portable-code)**.
When changing existing code, try to follow the style of the old code,
but be sure to follow best practices when writing new code. Note that
copying and pasting old code is considered adding new code!

As a general rule, only the simplest code possible is accepted into
Wine. Spend some time looking over your changes and think about whether
there is a more concise or straightforward way to do what you want.

### Patch guidelines

In order to make your patches as easy to check as possible, try to keep
them **small, clear, and atomic**:

- Only include closely related changes in one commit
- When adding [conformance tests](Conformance-Tests) for an fix, try to put the tests in a separate commit, ordered before the fix, with `todo_wine` annotations that are removed by the fix. This makes it easy to see what is fixed. Don't do this if the tests would crash or hang, or otherwise if todo_wine can't trivially be added. This is also not really necessary for new features, or extremely simple fixes where it's very clear what's being fixed.
- Limit a commit to changing a single file or component unless that
  would break something somewhere else
- Don't implement extra things that no one uses. To quote Wine's chief
  maintainer: "We don't add a dll unless some app wants it, we don't add
  a function unless some app calls it, we don't add a version resource
  unless some app checks it, etc." [^1]
- Limit each merge request to only a few commits (no more than 5 is a
  good guideline)

[^1]: https://gitlab.winehq.org/wine/wine/-/merge_requests/2045#note_22578

These rules make the merge request easier to review, and also make it
easier to [find regressions](Regression-Testing), and help
prevent new bugs from slipping through.

You can also look at the [accepted merge
requests](https://gitlab.winehq.org/wine/wine/-/merge_requests?scope=all&state=merged)
to see the requests that have been submitted and committed recently. Try
to imitate the style of the successful merge requests.

Related parts of the Wine project, such as the website, may have
slightly looser requirements on patches, but it is still important to
keep patches clear and simple, bundle related changes together, and not
break anything.

### Testing for problems

Be sure to run the conformance tests on an unchanged branch of Wine (or
before you make any changes) to see where your system is OK. Then run
the tests again after you make your changes to verify that they don't
break anything new. If you've added or modified any of the conformance
tests, be sure to check that they work properly by using the `make test`
command, then submitting the resulting executable to the [Wine Test
Bot](https://testbot.winehq.org/).

Also, make note of any significant compiler warnings that come up when
building your modified version of Wine and fix the underlying cause
before submitting your patch.

### The commit message

In the **first line** of the commit message, write the name of the
component you changed, followed by a colon, one sentence in the
imperative mood that will appear in the release notes, and a period. Be
brief: the first line should ideally not be more than 72 characters in
length.

After the first line, you may add **explanatory paragraphs** that tell
what the patch accomplishes. Describe your changes in the imperative
mood, as if you are giving orders to the codebase to change its
behavior, e.g. `Make xyzzy do frotz.` instead of
`This patch makes xyzzy do frotz.` or `Changed xyzzy to do frotz.` Try
to make sure your explanation can be understood without external
resources. Instead of giving a URL to a mailing list archive, summarize
the relevant points of the discussion. Describe *how* the patch works
and *why* it is needed, but do not repeat what the diff already shows.
Wrap all paragraph lines to 72 characters.

If your patch is related to a bug, it's recommended to include a
**Wine-Bug line** with a URL to Bugzilla (see the example below). Do not
include the bug number in the first line.

You can include any **extra information** that you do *not* want
included in the commit log in the Description field when creating the
merge request on the website.

A complete example:

    gdiplus: Avoid calling GdipFillPath() with an empty path.

    There is no point filling an empty path, and an empty path will cause
    SelectClipPath() used in brush_fill_path() to return an error.

    Wine-Bug: https://bugs.winehq.org/show_bug.cgi?id=987654

## Submitting your changes

### Quality check

It never hurts to check through your changes one last time:

- Look at each line of the patch, make sure there are no unintentional
  or unrelated changes
- Did your fix pass all related tests? If it wasn't covered by a test,
  have you written a test of your own?

### Sending the merge request

The [Git Wine Tutorial](Git-Wine-Tutorial) includes more
details about sending merge requests. In general you should push your
changes to a temporary branch in your fork on Gitlab:

```sh
$ git push origin master:my-awesome-fix
```

and then go to the link that is displayed to finish the creation of the
merge request.

### Managing your submission

After you've submitted your merge request, a reviewer will be assigned
to it, if someone is responsible for that area of code. You can also
assign a reviewer yourself if you know who the right person is. If a
reviewer gives some feedback or a critique, carefully think about what
they say and fix your patch before resubmitting. If others point out a
few flaws in your patch, it's safe to assume that they missed some too
so try to check the whole patch and fix other flaws before resubmitting.

When updating your changes, don't simply push the fixes as a new commit
on top of your merge request. You need to actually modify and recreate
the existing commits to make it look as if you got everything right on
the first try. You can then update your merge request by force pushing
to its branch:

```sh
$ git push --force origin master:my-awesome-fix
```

If your merge request remains in the queue for several weeks without
being committed and without feedback, improving it (perhaps by adding
more tests) and resubmitting it (after rebasing to the current tip) may
help. You can also ask for suggestions on the [IRC
channel](IRC) or the [wine-devel mailing
list](https://www.winehq.org/pipermail/wine-devel/). If you have patches
rejected multiple times, don't be discouraged. You might consider
finding a mentor willing to pre-review your changes before you submit
them (see
<https://www.winehq.org/pipermail/wine-devel/2010-August/086207.html>
for a discussion of this)

### Reviewing merge requests

If you are asked to review a merge request, and find things that need to
be improved, you should add a comment to the merge request from the
Gitlab UI. If you prefer to use email, you can reply to the Gitlab
notification (if you are subscribed to these), or to the mails that were
sent to the [wine-gitlab mailing
list](https://list.winehq.org/mailman3/hyperkitty/list/wine-gitlab@winehq.org/)
(if you are following that).

You can also fix things up yourself and force-push updated commits to
the original branch. At the moment this requires the submitter to
explicitly give you access (we are hoping to lift that restriction).

If you think that the merge request is good to go in, you should mark it
approved in Gitlab. As a rule, a merge request won't be committed until
all reviewers have approved it. If you have been assigned as a reviewer
but feel that you cannot meaningfully review the changes, feel free to
unassign yourself, and maybe re-assign it to someone more knowledgeable
in that area.

### Responding to review

Sometimes, this is a trivial process. A reviewer points out an error in
your patch which you missed, or some way in which the code style differs
from the norm in Wine. In this case all you need to do is fix up that
part of the patch and resend.

Sometimes review is less trivial, and may result in extended discussion.
Here are some things to keep in mind to keep a good relationship with
your reviewers:

- **Assume positive intent.** You will be interacting with contributors
  from many cultures, most of whom are not native English speakers.
  Sometimes communication can come off as curt or impolite without
  meaning to.
- Reviewers may phrase suggestions as questions, but on the other hand,
  questions don't always mean that you need to change your code. On the
  *other* hand, if a question is asked once, it might be asked again, in
  the future, by a newcomer trying to understand the code (or by someone
  who's forgotten it).
- Try to understand the reviewer's perspective. Often you will spend a
  long time working on a code, polishing it to perfection, rewriting it
  multiple times. When you submit that patch, you are the world's expert
  on that code, and it can be frustrating to receive feedback asking
  that it be done differently, or questioning your decisions. Try to
  understand where that feedback is coming from.
- Being the world's expert on a piece of code is a double-edged sword.
  You will not always be as familiar with that code as you are
  now. Often a reviewer will see parts of code as complex and
  difficult to understand that you understand perfectly. This can be
  an asset: the code should be comprehensible to you, not just now,
  but in the future as well, and it should also be comprehensible to
  anyone who's starting to work on that component.
- You may be the expert on the code which you are submitting, but that
  doesn't always translate to understanding the way it interacts with
  other code. A maintainer's job is to understand these interactions.
- People make mistakes, and have blind spots. That applies to both you
  and the reviewer. If the reviewer makes a mistake, or asks a
  question the answer to which seems obvious to you, try to be
  charitable. On the other hand, if a reviewer asks for some change
  and this change seems disadvantageous to you, it's fine to explain
  why—maybe there's something they missed.
- Perhaps most importantly, try to avoid being argumentative. People
  do not enjoy reviewing patches when they feel like they are having
  an argument with the submitter, and this can lead to discussions and
  patches being ignored, sometimes even preemptively.

This is not the same thing as "don't argue". Part of not being
argumentative is being open-minded to suggestions, and willing to change
your patch according to the maintainer's preferences. A more important
part of it, though, is understanding and acknowledging why the
suggestion was made, and explaining why it's not the best approach. Work
\*with\* the maintainer, not against them. Verbally acknowledging the
tradeoffs that lead you to choose a certain approach over that suggested
by the maintainer, or acknowledging why their suggested approach would
be preferable even if it's not actually possible, can do a lot to keep
review enjoyable for both parties. Even phrasing like "unfortunately we
can't do it that way, because X" can go a long way.

## Special situations

### Submitting patches written by somebody else

Occasionally, the author of a useful patch stops working on it, and
somebody else has to pick it up and continue. In this case, commit the
author's original patch file to your local branch (`git am`), making
sure that the Author: field of the commit is set to the original author,
and submit a merge request. You'll be asked to approve the merge request
to show that you have checked the original author's work.

### Coauthored patches

If someone else has made a significant contribution to the patch, first
try to split up the patch so that each patch has only one author. If
that is impractical, explain in the commit message who you collaborated
with on the patch, but keep yourself as the author.

### Multiple outstanding merge requests

Wine's chief maintainer, Alexandre Julliard, says you should concentrate
on one thing and get it in before trying others. He may ignore some of
your merge requests if he feels you have too many balls in the air.

### Introducing new dependencies

Sometimes new Wine functionality requires adding new build dependencies
on Linux libraries. When that happens:

- Your merge request must still compile and not break Wine or the Wine
  tests even if the libraries are missing from the build environment.
- You are not required to send a patch to update the GitLab CI
  environment.
- Sending a patch to update the build environment is helpful though. If
  doing so it must be sent in a separate merge request with no other
  change. Also note that the GitLab CI environment will only be updated,
  manually, after that merge request is merged. This is to ensure that
  all merge requests go through a well known and verified environment.

------
