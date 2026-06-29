There is no longer a maintained Stable branch starting with 10.0.\
See the Wine Stable presentation from the [[WineConf-2025]].

Wine Stable's mantra is to not break currently running applications.
Regressions are a priority to fix and new regressions should not be
added.  Thus a patch that fixes ten applications but breaks one
application is a bad patch for Stable.

## Scope of this Page

These rules were valid for:

- Wine stable versions 1.8.x to 9.0.x
- Stable maintainer: ~~[Michael Stefaniuc](@mstefani)~~

## Acceptable Patches for Wine Stable

Rules for patches going into Wine Stable:

- It must be first accepted in the Development version (in exceptional
  cases it can come via Staging).
- It must be tested (in 1-2 released Development or Staging versions).
- It should be small.
- It must fix a real bug in a real application.
- Stubs must get an application to run (not to just crash later) and
  need a longer testing period in the wild.
- It must fix a build issue, especially on distributions using Wine
  Stable.
- Translation updates are in scope too.

## Submitting Patches for Wine Stable

To mark a patch for inclusion into Stable you can choose between the
following methods:

- Set the ["Target Milestone" to
  6.0.x](https://bugs.winehq.org/buglist.cgi?bug_status=RESOLVED&bug_status=CLOSED&product=Wine&query_format=advanced&resolution=FIXED&target_milestone=6.0.x)
  for a bug in bugzilla.
- Or send the Stable maintainer an email with a list of commit IDs to
  cherry pick.
- Add the Wine-Bug tag to the patch when submitting it to wine-devel.

## Accepted / Queued Patches

Here is the list of [accepted and queued
patches](https://people.redhat.com/mstefani/wine/stable/) for Wine
Stable.

Or in raw format in git on <https://github.com/mstefani/wine-stable>

Branches:

- **stable:** Accepted patches that will be in the next wine-6.0.x
- **queue:** Queued patches for stable

  **Warning:** This branch is always **rebased** on top of stable

Additional information is kept with git notes in **stable-notes**.
Github doesn't shows any notes so those need to be accessed via git:

```sh
$ git pull <stable-remote> refs/notes/stable-notes
$ export GIT_NOTES_REF=refs/notes/stable-notes
$ git log
$ git show
```
