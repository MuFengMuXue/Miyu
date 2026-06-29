This is a basic guide to write tests for Gentoo Eclasses.

## Contents

-   [[1] [Testing framework]](#Testing_framework)
    -   [[1.1] [Sourcing]](#Sourcing)
    -   [[1.2] [Overview of helpers]](#Overview_of_helpers)
-   [[2] [External resources]](#External_resources)

## [Testing framework]

In order to test eclasses, you need to source the [eclass/tests/tests-common.sh] file in the [Gentoo ebuild repository](https://wiki.gentoo.org/wiki/Gentoo_ebuild_repository "Gentoo ebuild repository"). It sets up a testing environment, provides replacements for commonly used functions and adds helpers for running tests.

Tests are bash scripts that can be located in any directory, although in this guide [eclass/tests] will be assumed.

### [Sourcing]

In the [::gentoo] repo, it\'s as simple as:

[CODE]

    source tests-common.sh || exit

** Important**\
Always exit if sourcing failed, otherwise terrible things like [[[bug #833342]](https://bugs.gentoo.org/show_bug.cgi?id=833342)[]] could happen!

In other repositories, use [portageq](https://wiki.gentoo.org/wiki/Portageq "Portageq") to locate the file:

[CODE]

    GENTOO_REPO=$(portageq get_repo_path / gentoo) || exit
    source "$"/eclass/tests/tests-common.sh || exit
    TESTS_ECLASS_SEARCH_PATHS+=( "$"/eclass )

Note the `TESTS_ECLASS_SEARCH_PATHS` variable. Without it you won\'t be able to [inherit] Gentoo eclasses.

### [Overview of helpers]

+--------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------+
| Function                                                                                                                 | Description                                                                                                                  | Example use                                                           |
+--------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------+
| [tbegin] `message` | [ebegin] wrapper for a test case. | ::::: gw-box                                                          |
|                                                                                                                          |                                                                                                                              | ::: box-caption                                                       |
|                                                                                                                          |                                                                                                                              | [CODE]  |
|                                                                                                                          |                                                                                                                              | :::                                                                   |
|                                                                                                                          |                                                                                                                              |                                                                       |
|                                                                                                                          |                                                                                                                              | :::  |
|                                                                                                                          |                                                                                                                              |     tbegin "dependency strings"                                       |
|                                                                                                                          |                                                                                                                              | :::                                                                   |
|                                                                                                                          |                                                                                                                              | :::::                                                                 |
+--------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------+
| [t] `cmd`          | Run `cmd` and set the suite\'s exit status to non-zero if it failed.                                              | ::::: gw-box                                                          |
|                                                                                                                          |                                                                                                                              | ::: box-caption                                                       |
|                                                                                                                          |                                                                                                                              | [CODE]  |
|                                                                                                                          |                                                                                                                              | :::                                                                   |
|                                                                                                                          |                                                                                                                              |                                                                       |
|                                                                                                                          |                                                                                                                              | :::  |
|                                                                                                                          |                                                                                                                              |     t test "$" == "app-foo/bar"                              |
|                                                                                                                          |                                                                                                                              | :::                                                                   |
|                                                                                                                          |                                                                                                                              | :::::                                                                 |
+--------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------+
| [tend] `status`    | [eend] wrapper for a test case.   | ::::: gw-box                                                          |
|                                                                                                                          |                                                                                                                              | ::: box-caption                                                       |
|                                                                                                                          |                                                                                                                              | [CODE]  |
|                                                                                                                          |                                                                                                                              | :::                                                                   |
|                                                                                                                          |                                                                                                                              |                                                                       |
|                                                                                                                          |                                                                                                                              | :::  |
|                                                                                                                          |                                                                                                                              |     tend $?                                                           |
|                                                                                                                          |                                                                                                                              | :::                                                                   |
|                                                                                                                          |                                                                                                                              | :::::                                                                 |
+--------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------+
| [texit]                       | Clean up and set the suite\'s exit status. Call it at the end of your test suite.                                            | ::::: gw-box                                                          |
|                                                                                                                          |                                                                                                                              | ::: box-caption                                                       |
|                                                                                                                          |                                                                                                                              | [CODE]  |
|                                                                                                                          |                                                                                                                              | :::                                                                   |
|                                                                                                                          |                                                                                                                              |                                                                       |
|                                                                                                                          |                                                                                                                              | :::  |
|                                                                                                                          |                                                                                                                              |     texit                                                             |
|                                                                                                                          |                                                                                                                              | :::                                                                   |
|                                                                                                                          |                                                                                                                              | :::::                                                                 |
+--------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------+

## [External resources]

-   [Eclass Writing Guide](https://devmanual.gentoo.org/eclass-writing/index.html)