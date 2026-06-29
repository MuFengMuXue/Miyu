Welcome to the Git Wine tutorial! This page describes how to manage Wine
code and patches with [Git](https://git-scm.com/). Git is a fast version
control system, originally written for use with large repositories, such
as the Linux Kernel source. The Git Wine tree gives you fast access to
the entire Wine tree and its history, and allows you to maintain a local
tree or patch series and merge it easily with WineHQ.

## Tutorials and guides

- This Wiki page.
- The Wiki page on [Regression Testing](Regression-Testing)
  (which is aimed at non-programmers).
- The official [Git
  tutorial](https://www.kernel.org/pub/software/scm/git/docs/gittutorial.html),
  and the official [Git
  manual](https://www.kernel.org/pub/software/scm/git/docs/git.html).
- [Pro Git](https://git-scm.com/book/en/v2), a free e-book by Scott
  Chacon and Ben Straub.
- A very comprehensive guide to advanced git usage ("branch wizardry and
  git grandmastery") called [Git
  Magic](https://www-cs-students.stanford.edu/~blynn/gitmagic/index.html)
  available; despite the name it also addresses [Basic
  Trickery](https://www-cs-students.stanford.edu/~blynn/gitmagic/ch02.html)
  for the beginner's needs.
- LWN's article on [Branching and merging with
  git](https://lwn.net/Articles/210045/) (Nov 2006 - which is a bit old,
  but detailed).
- [Git for Computer
  Scientists](https://eagain.net/articles/git-for-computer-scientists/),
  a "quick introduction to git internals for people who are not scared
  by words like Directed Acyclic Graph" (Jul 2009).
- [The Git
  Parable](https://tom.preston-werner.com/2009/05/19/the-git-parable.html)
  "will take you on a journey through the creation of a Git-like system
  from the ground up" (May 2009).

**Note:** To get documentation on a Git command, use `git help` or
`man`. For example, the following two commands are equivalent:

```sh
$ git help format-patch
```
```sh
$ man git-format-patch
```

## Set up your Git repository

The first step to using Git with Wine is to set up a local Git
repository.

### Downloading and installing Git

It's recommended to install Git via your distribution's package manager.
If you want to install from source, you can download the latest version
of Git from <https://www.kernel.org/pub/software/scm/git/> . It installs
into ~/bin by default. See [the Pro Git
book](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git#Installing-from-Source)
for build instructions.

### Cloning the Wine Git repository

Wine uses Gitlab as a development platform. You can browse the WineHQ
Gitlab instance at <https://gitlab.winehq.org>. To download the main
Wine repository:

```sh
$ git clone https://gitlab.winehq.org/wine/wine.git
$ cd wine
```

There is a GitHub mirror
[here](https://github.com/wine-mirror/wine.git); note that this is
controlled by GitHub and not by Wine. Also a Gitee mirror
[here](https://gitee.com/winehq/wine). This may be used to get around
an uncooperative firewall, and may also provide faster download speeds
anyway (although it is slightly slower to update).

### Creating a fork on Gitlab

If you plan on sharing or submitting any patches, you should create your
own fork on the WineHQ Gitlab.

To do this, first [create an
account](https://gitlab.winehq.org/users/sign_up). You'll need to
validate your email address, and then file a [User Verification
issue](https://gitlab.winehq.org/winehq/winehq/issues/new?issuable_template=User%20verification)
to request the necessary permissions to create a fork.

Note: Wine uses a **real name** [policy](#real-name-policy) on
committed patches. Please also use your real name when creating your
Gitlab account, so that it can be matched to your commits.

You'll then need to add an ssh key to your [user
profile](https://gitlab.winehq.org/-/profile/keys). Once you have done
that, you can fork the main tree by clicking the **fork** button of
the [main tree](https://gitlab.winehq.org/wine/wine), and download
your fork with:

```sh
$ git clone git@gitlab.winehq.org:your_gitlab_username/wine.git
```

It is advantageous to add the main tree as an upstream repository. To do
this, use the following command:

```sh
$ git remote add upstream https://gitlab.winehq.org/wine/wine.git
```

You can then refresh your fork with the upstream changes with:

```sh
$ git pull --rebase upstream master
```

### Real-name policy

We request that all contributors use their real name in their Gitlab
profile, and in their git commit information.

This doesn't need to be your legal name (we are not checking
passports), but it should be the preferred/chosen name that you use in
everyday life.

If this is an issue for you, please request an exception to the policy
when filing the User Verification issue (you can mark the issue
confidential), or privately contact @julliard to discuss it.

### Further configuration

You should set your name and email address using:

```sh
$ git config --global user.name "Your Name"
$ git config --global user.email "me@example.com"
```

A useful feature of Git is its ability to color the output of various
commands (diff, status, branch, etc). To enable colors in all commands
that support it, when running them from a terminal:

```sh
$ git config --global color.ui auto
```

Particularly useful is the colored output of the [git
diff](https://www.kernel.org/pub/software/scm/git/docs/git-diff.html)
command, as it also highlights trailing whitespace in patches.

## Glossary

See also the official [Git
glossary](https://www.kernel.org/pub/software/scm/git/docs/gitglossary.html).

- A **commit** (or changeset, or revision) is a snapshot of a codebase.
  Each commit has a name -- its **commit id** -- which is a SHA1 hash.
  Commits can have other names (tags, etc). See the ["Specifying
  revisions" section of the git rev-parse
  page](https://www.kernel.org/pub/software/scm/git/docs/git-rev-parse.html#_specifying_revisions)
  for details on how refer to commits. The verb **to commit** means to
  create a commit.
- A **diff** is a file describing the differences between two sets of
  files. They are created with the command [git
  diff](https://www.kernel.org/pub/software/scm/git/docs/git-diff.html).
  If you have code in the "before" state, you can **apply** the patch
  (with [git
  apply](https://www.kernel.org/pub/software/scm/git/docs/git-apply.html))
  and you end up with code in the "after" state.
- A **patch** is a file that includes authorship information, a
  description, and a diff. They are created with [git
  format-patch](https://www.kernel.org/pub/software/scm/git/docs/git-format-patch.html)
  and committed with [git
  am](https://www.kernel.org/pub/software/scm/git/docs/git-am.html).
  This similar to applying a patch, but it also creates a commit that
  preserves the original description and authorship information.
- The **HEAD** (or **tip**) of a branch is the most recent commit. On
  its own, HEAD means the tip of the current branch.
- **master** is the main branch. SVN/CVS calls this "trunk".
- The **parent** of a commit is the one before it in the history.
  (Commits can technically have more than one parent, but the Wine repo
  avoids using this feature, preferring a linear history.) Given a
  commit `abcde`, its parent is referred to as `abcde^`, and its
  great-grandparent is referred to as `abcde^^^` or `abcde~3`.
- A **repository** (or **repo**) is a database storing the source code
  of every available version of a program, and the author of every
  change.
- A **tree** is a git technical term meaning "directory" (sort of), and
  sometimes means the whole codebase of a project ("the Wine tree").
- The **working copy** or **working tree** refers to the files and
  directories on your file system, the ones you can see and change with
  the file manager. The [git
  status](https://www.kernel.org/pub/software/scm/git/docs/git-status.html)
  command will refer to changes to these files as "Changed but not
  updated".

## Managing your changes - the simple way

### Committing a change into your local tree

After editing the checked out tree, you can use [git
status](https://www.kernel.org/pub/software/scm/git/docs/git-status.html)
to see which files have changed:

```sh
$ git status
```

Or you can examine the difference by using [git
diff](https://www.kernel.org/pub/software/scm/git/docs/git-diff.html):

```sh
$ git diff
```

To then commit *all* changed files to your local tree, use the [git
commit](https://www.kernel.org/pub/software/scm/git/docs/git-commit.html)
command with the -a option:

```sh
$ git commit -a
```

If you only wish to commit some files, use:

```sh
$ git commit <file1> <file2>
```

or:

```sh
$ git add <file1> <file2>...
$ git commit
```

**Commit early, commit often**: Your local Git tree is yours. You should
feel free to commit patches frequently, as it's not until you mail them
in that they have a chance of being committed upstream.

### Seeing where you are and what you've done

You can get a list of all the commits in the tree using [git
whatchanged](https://www.kernel.org/pub/software/scm/git/docs/git-whatchanged.html)
or [git
log](https://www.kernel.org/pub/software/scm/git/docs/git-log.html):

```
git whatchanged     # list of commits, which shows what files were altered
git log             # list of commits
git log --decorate  # list of commits, with the last upstream commit marked
git log --stat      # list of commits, with diffstats
git log --stat -p   # list of commits, with diffstats and patches
```

You can get a list of files that you have changed but have not yet
committed using [git
status](https://www.kernel.org/pub/software/scm/git/docs/git-status.html):

```sh
$ git status          # list of uncommitted changes
```

There's a nice tool to view your Git repository named
[gitk](https://www.kernel.org/pub/software/scm/git/docs/gitk.html),
written in tcl/tk. AJ suggests using something like `gitk wine-1.0..` to
make it go faster (please note that the trailing `..` is important).
gitk visualizes both committed and uncommitted changes.

[qgit](https://sourceforge.net/projects/qgit/) also provides similar
functionality, but in a Qt based interface. It appears to be faster than
gitk and has additional features such as an annotation facility to
identify which change introduced each line of a file.

If you prefer using your terminal, ["git lol" and "git
lola"](https://lwn.net/Articles/390701/) are useful aliases you can add
to your ~/.gitconfig file:

    [alias]
        lol = log --graph --decorate --pretty=oneline --abbrev-commit
        lola = log --graph --decorate --pretty=oneline --abbrev-commit --all

If you have a webserver running, git instaweb allows you to view your
local tree in your web browser.

### Reverting changes in your working copy

If you have edited some files, but decided you don't like the changes
you've made and want to undo **all** the changes that you've made to
your working copy, you can use [git
checkout](https://www.kernel.org/pub/software/scm/git/docs/git-checkout.html):

```
git checkout -f             # revert everything
git checkout file-name      # revert one file
```

Alternatively, use [git
reset](https://www.kernel.org/pub/software/scm/git/docs/git-reset.html):

```
git reset --hard HEAD       # revert everything
```

### Undoing commits

If you want to undo your most recent commit, you can use the [git
reset](https://www.kernel.org/pub/software/scm/git/docs/git-reset.html)
command:

```
git reset HEAD^          # undo commit, but keep changes to working files
git reset --hard HEAD^   # undo commit, and reset working files as well
git reset --hard HEAD~5  # undo 5 commits
git reset --hard origin  # scrap all changes and start all over again
```

### Editing commits

To edit the most recent commit:

```sh
$ vi file.c                        # edit the file
$ git commit --amend file.c        # redo the commit
```

To edit earlier commits (or reorder or delete them) use the -i (aka
--interactive) option to [git
rebase](https://www.kernel.org/pub/software/scm/git/docs/git-rebase.html).
So if you are interested in altering the 5 most recent commits use:

```sh
$ git rebase -i HEAD~5
```

This will open your editor, with a list of commits prefixed with
**pick**. To delete a commit, just remove its line. To reorder them,
just rearrange the lines. To edit commits, change **pick** to **edit**.

Be sure to follow the instructions carefully when doing `git rebase -i`.
Specifically, when you are editing a commit (that you explicitly
requested to edit) and are satisfied with the changes, you must use:

```sh
$ git add <file1> <file2>...
$ git commit --amend
$ git rebase --continue
```

However, when `git rebase -i` asks you to edit a commit that you have
not requested to edit (e.g. there is a conflict), you must use:

```sh
$ git add file1 file2...
$ git rebase --continue
```

This is quite important - not following this carefully will result in
merged patches.

### Editing commits the hard way

Instructions for those who don't want to use `git rebase -i`:

If the commit is not the most recent one, but say 5th from the top then
you can:

```sh
$ git checkout -b tmp HEAD~5              # rewind to the commit in question
$ vi file.c                               # edit the file
$ git commit --amend file.c               # redo the commit without deleting the commit
$ git rebase --onto tmp master~5 master   # replay the later changes
$ git branch -D tmp                       # clean up the temporary branch
```

Where there are a number of files to amend you are probably better off
using:

```sh
$ git checkout -b tmp HEAD~5              # rewind to the commit in question
$ git reset HEAD^                         # delete the commit at the now current point
$ vi file1.c                              # edit
$ vi file2.c                              #      the files
$ git commit -a -c ORIG_HEAD              # redo the commit incorporating all changed files
$ git rebase --onto tmp master~5 master   # replay the later changes
$ git branch -D tmp                       # clean up the temporary branch
```

Where the commit is not the most recent one, but say 5th from the top
and you wish to insert a new commit, then you can:

```sh
$ git checkout -b tmp HEAD~5              # rewind to the commit in question
$ vi new_file.c                           # create the new file
$ git commit -m "New commit of file new_file.c" new-file.c # create a new commit or a series of commits
$ git rebase --onto tmp master~5 master   # replay the later changes
$ git branch -D tmp                       # clean up the temporary branch
```

Likewise if you want to delete a commit that is not the most recent one,
then you can:

```sh
$ git checkout -b tmp HEAD~5              # rewind to the commit in question
$ git reset HEAD^                         # delete the commit at the now current point
$ git checkout path/file1 path/file2 etc  # delete the changed files
$ git rebase --onto tmp master~5 master   # replay the later changes
$ git branch -D tmp                       # clean up the temporary branch
```

and the commit is gone. You need to checkout all the changed files
though and the rebase may throw some errors for you to resolve as it
applies later commits.

### Splitting up a commit

Patches are often rejected because they are too big. To remedy this
situation, you often don't have to touch your working copy at all.
Instead, you can interactively select which chunks from your last commit
belong in a separate commit:

```sh
$ git reset -p HEAD^  # undo some changes from the last commit (in the staging area, not the working copy)
$ git commit --amend  # remove the changes from the commit
$ git commit -a       # add them to a new commit
```

`git reset -p` will show you each chunk and ask you to respond "yes"
(undo the change) or "no" (keep the change).

If you are splitting the commit into more than two commits, use
`git add -p `<file> and `git commit` instead of `git commit -a`. This
will allow you to stage only the chunks that should belong in the next
commit.

### Removing trailing whitespace

Thank you to Mike Kaplinskiy for this very helpful hint:

```sh
$ git rebase --whitespace=fix origin/master
```

"It fixes whitespace on all the commits that you've made. I think it's
pretty good about merge conflicts due to whitespace as well. I don't
know of a way of doing this at commit time though."

This is essential for submitting your patches to the Wine project.
Please see this post for more information:
<https://www.winehq.org/pipermail/wine-devel/2010-July/084870.html>

Trailing whitespace is highlighted in the output of the [git
diff](https://www.kernel.org/pub/software/scm/git/docs/git-diff.html)
command when colored output is enabled (more about this in the [Further
configuration](#further-configuration) section).

### Keeping up to date with WineHQ

Now that you have a copy of the Wine Git repository, you will
periodically need to receive new commits from the original repository.
You do this using:

```sh
$ git pull --rebase
```

This is equivalent to:

```sh
$ git fetch
$ git rebase origin
```

[git
fetch](https://www.kernel.org/pub/software/scm/git/docs/git-fetch.html)
retrieves new files from the WineHQ Git repository; this should always
be a safe operation as it does not change your local file system.

[git
rebase](https://www.kernel.org/pub/software/scm/git/docs/git-rebase.html)
origin reapplies any local commits you have made onto the latest WineHQ
branch. (Technically, it creates a new branch on 'origin', reapplies all
the patches in your current HEAD to the new branch, then changes HEAD to
the new branch.) Patches already applied upstream will not be reapplied.

A common mistake is to use `git fetch` by itself. It will only download
updates but will not apply them. Another common problem is trying to
rebase while having uncommitted changes. One way to fix this is to:

```sh
$ git stash           # save changes
$ git rebase origin   # rebase
$ git stash pop       # apply saved changes
```

When you send patches, inevitably, some of your patches will be
rejected, while others will be accepted. If you have written a series of
patches, but only some of those are rejected, it can be annoying to
reorder them, fix one or two problems and resubmit. The main git tools
that you can use to help solve this problem are [git
rebase](https://www.kernel.org/pub/software/scm/git/docs/git-rebase.html)
and [git
cherry-pick](https://www.kernel.org/pub/software/scm/git/docs/git-cherry-pick.html).
See
[here](https://www.kernel.org/pub/software/scm/git/docs/howto/rebase-from-internal-branch.txt)
for a discussion on the Git mailing list about rebasing on local
branches.

### Resolving merge conflicts

When rebasing, sometimes upstream changes prevent your patches from
applying. If there is a conflict, you will see something like this:

    Applying <patchname>
    error: patch failed: <file>:<line>
    error: <file>: patch does not apply
    Using index info to reconstruct a base tree...
    Falling back to patching base and 3-way merge...
    Auto-merged <file>
    CONFLICT (content): Merge conflict in <file>
    Failed to merge in the changes.
    Patch failed at <msgnum>.
    When you have resolved this problem run "git rebase --continue".
    If you would prefer to skip this patch, instead run "git rebase --skip".
    To restore the original branch and stop rebasing run "git rebase --abort".

There are two choices now: resolve the conflict or skip the patch. The
file in question will contain conflict markers where the patch failed:

    <<<<<<<
    [code that caused patch not to be applied]
    =======
    [what would have been here if the patch had been applied]
    >>>>>>>

To resolve the conflict you have to manually merge the code between the
conflict markers, leaving the file in a compilable state. After that,
run

```sh
$ git add <file>
$ git rebase --continue
```

to remove the merge-conflict state and continue with the operation.

Patches can be skipped as follows:

```sh
$ git reset --hard  # removes the patch
$ git rebase --skip
```

### Submitting a merge request

After checking in your local changes (in multiple small commits), you
can submit a merge request on Gitlab to get your changes upstream. This
requires you to be working on a Gitlab fork. First push your changes to
your fork:

```sh
$ git push origin master:my-awesome-fix
```

You should make up a temporary branch name for your changes. That branch
will be deleted once the merge request is merged, so it's better to
avoid using the master branch directly.

The above command will print the link that you need to visit to complete
the creation of the merge request.

Read the Gitlab documentation for more details:
<https://docs.gitlab.com/ee/user/project/merge_requests/creating_merge_requests.html>

For more experienced users, it's possible to create a merge request
directly from git push, with a command like:

```sh
$ git push -o merge_request.create origin master:my-awesome-fix
```

See <https://docs.gitlab.com/ee/user/project/push_options.html> for
details.

### Updating a merge request

Once your merge request is reviewed, you may be asked to make some
improvements to it. Once you have revised your commits, you can update
the merge request by force-pushing to the branch:

```sh
$ git push --force origin master:my-awesome-fix
```

If the main tree has changed in the meantime, you may want to pull the
upstream commits first. You can do this with:

```sh
$ git pull --rebase upstream master
```

## Managing branches

[Git
branches](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging)
can be useful if you are working on a lot of bugs at the same time.
However, they are completely optional and overkill if you are only
working on one thing.

### Creating a branch

To create a branch, use [git
checkout](https://www.kernel.org/pub/software/scm/git/docs/git-checkout.html)
with the -b option. For example:

```sh
$ git checkout -b new-branch HEAD~5
```

This winds back the working directory to HEAD~5, and forks the history
there, creating the branch **new-branch**. The new branch becomes the
current branch.

### Navigating branches

Use [git
branch](https://www.kernel.org/pub/software/scm/git/docs/git-branch.html)
to list all branches.

```
git branch              # local branches only
git branch -a           # both local and remote branches
```

To change branches, use git checkout:

```sh
$ git checkout master     # change to branch master
```

### Merging and rebasing branches

Git allows you to merge branches together; this is not done in the
WineHQ repository, so it is easier to just rebase/cherry-pick instead.

### Deleting branches

```sh
$ git branch -D new-branch
```

## Other useful operations

### Picking patches from another branch

You can cherry pick (apply) a patch from another branch into your
current branch using:

```sh
$ git cherry-pick <commit-id>
```

This will create a new commit, but with authorship information from the
original patch.

### Getting rid of timestamp changes

Git considers a file changed if its date is different from that in the
Git index file. "git diff-index HEAD" may show files have changed if you
have edited them and reverted the changes (or even just touched the
file). You can remove this difference using:

```sh
$ git reset
```

### Regression testing

Regression testing is really easy with Git. It's done with the help of
[git
bisect](https://www.kernel.org/pub/software/scm/git/docs/git-bisect.html)
that does all the magic. So all that's left to do is to compile and
test. Even non-developers can do it. *See [Regression
Testing](Regression-Testing) for instructions.*

### Committer statistics

To see a list of committers in the last 5 years, sorted by number of
commits:

```sh
$ git shortlog -s -n --since="(5years)"
```

### Finding who changed what

```
git log /path/           # log of changes to files in /path/
git log /path/file       # log of changes to /path/file
git blame /path/file     # show per-line authorship info
git blame -w /path/file  # ditto, but ignoring whitespace changes
```

### Useful morsels

Output all your patches in the directory **out**:

```sh
$ git format-patch -o out upstream/master
```

Save all your patches as one big file (for your own easy
reference/viewing):

```sh
$ git log upstream/master..origin -p > /path/to/file 2>&1
```

Count the number of patches in your repository but not in upstream Wine
(useful for keeping track of any disappearing patches):

```sh
$ git rev-list upstream/master..origin | wc -l
```

Perform an interactive rebase of your commits using [git
rebase](https://www.kernel.org/pub/software/scm/git/docs/git-rebase.html):

```sh
$ git rebase -i upstream/master
```

Automatically fix whitespace errors in all local patches:

```sh
$ git rebase --whitespace=fix upstream/master
```

## Patch stack

[Stacked Git](https://gna.org/projects/stgit) is similar to
[Quilt](https://savannah.nongnu.org/projects/quilt), just on top of Git.
It manages a stack of applied and unapplied patches on top of a Git
branch. Patches can be pushed on the applied stack or popped off the
applied stack onto the unapplied stack. The topmost applied patch can be
edited and the stack can be rebased onto an updated branch. This makes
keeping around and refining local changesets (changeset-\>patch) until
they are applied upstream much easier. The history of changes to a patch
are also kept in Git.

## Annoyances

It can be quite hard to get a real understanding of the underlying
concepts of Git, and if you are a git newb you are almost certain to run
into in a situation where things break and you have no idea how to get
out of the mess. At this point: don't panic! You might be tempted to
just trash your repository and manually remerge your patches, but it is
very probable you will run into the same situation again so you'd be
better off making sure you have understood how Git works. Look through
the [list of tutorials](#tutorials-and-guides) at the top of
this page.

## Other Git repositories

See the [Source Code](Source-Code) page for a list of other
Wine-related git repositories.
