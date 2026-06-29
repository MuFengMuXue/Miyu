This page contains ideas for fixes and improvements to the design and
structure of WineHQ. This includes all of the sub-sites such as Bugzilla
and the wiki.

For a list of actual writing tasks, see [Writers](Writers).

## Across All Sites

- Fixing some [open bugs for
  WineHQ](https://bugs.winehq.org/buglist.cgi?bug_status=UNCONFIRMED&bug_status=NEW&bug_status=ASSIGNED&bug_status=STAGED&bug_status=REOPENED&bug_status=RESOLVED&product=WineHQ.org&query_format=advanced)
  always helps

- Move static web pages to the wiki.
- Ensure compliance to the latest (x)html spec.
- Update legacy PHP code to modern standards (PHP7)

## WineHQ Itself

- Some sort of picture would look snazzy in the upper right of the About
  page

### Test and Status Pages

- We dropped all of the old manually updated status reports, but it
  would be pretty cool (and helpful) if we could have more automated
  ones
  - Could we sick one or two of the [Wine TestBot
    VMs](Wine-TestBot-VMs), or do a rotation between distro
    images, to report build errors?
  - Maybe another one could rotate through [Static
    Analysis](Static-Analysis) tools and our own scripts to
    check [Code Hygiene](Code-Hygiene)?
  - The existing [Conformance Tests](Conformance-Tests)
    provide one good measure of runtime errors
  - We could also mine Bugzilla and use open bugs as a second estimate
    of logic errors
  - Use a scripted version of `git shortlog` by DLL to report current
    workers? (could be useful for new developers wondering who to
    contact about specific features)
- We could bring it all together into a fancy report page
  - Highlight the DLLs with the most failed/missing tests and bugs as
    priority DLLs?
  - We could possibly use an existing library for graphs & such (like
    D3.js?)

## AppDB Improvements

- A good place to start would be to fix some of the many [open bugs for
  the
  AppDB](https://bugs.winehq.org/buglist.cgi?bug_status=UNCONFIRMED&bug_status=NEW&bug_status=ASSIGNED&bug_status=STAGED&bug_status=REOPENED&bug_status=RESOLVED&list_id=298398&product=WineHQ%20Apps%20Database&query_format=advanced)
- Also check the [AppDB ToDo List](https://gitlab.winehq.org/winehq/appdb/-/wikis/ToDo-List).

## Bugzilla

Our official policy is **to not accept patches to upstream code** like
Bugzilla; you can still help us (and other Bugzilla users) if you try
[introducing your improvements
upstream](https://www.bugzilla.org/contribute/). Improvements to any
templates or code we overlay ourselves (like in *template/* for
instance) are always welcome though..

- A good place to start is by fixing some of the [open bugs for
  Bugzilla](https://bugs.winehq.org/buglist.cgi?bug_status=UNCONFIRMED&bug_status=NEW&bug_status=ASSIGNED&bug_status=STAGED&bug_status=REOPENED&bug_status=RESOLVED&list_id=298403&product=WineHQ%20Bugzilla&query_format=advanced).
- Open up more to allow for more thorough triage?
- Some improvements to the interface?
  - I think Bugzilla has provided ajax capabilities for a while; we may
    just need to tweak our templates and config to use them.

## Forums

Our official policy is **to not accept patches to upstream code** like
phpBB. If you [contribute those improvements
upstream](https://www.phpbb.com/get-involved/) though, they should work
their way to us when we update. Improvements to any templates or code we
overlay ourselves are always welcome though.

- Enable some kind of bot to crawl for useful info? (ambitious perhaps)
  - Store it in structured form?
