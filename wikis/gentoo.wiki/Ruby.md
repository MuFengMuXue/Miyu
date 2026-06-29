**Resources**

[[![Gentoo peach graphic](/images/thumb/a/ad/Gentoo-logo-peach.svg/25px-Gentoo-logo-peach.svg.png)](https://wiki.gentoo.org/wiki/Project:Ruby "Project:Ruby")][Project](https://wiki.gentoo.org/wiki/Project:Ruby "Project:Ruby")

[[]][Home](https://www.ruby-lang.org/en/)

[[]][Package information](https://packages.gentoo.org/packages/dev-lang/ruby)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Ruby_(programming_language) "wikipedia:Ruby (programming language)")

[[]][GitHub](https://github.com/ruby/ruby)

[[]][[#ruby](ircs://irc.libera.chat/#ruby)] ([[webchat](https://web.libera.chat/#ruby)])

[[]][[#rubyonrails](ircs://irc.libera.chat/#rubyonrails)] ([[webchat](https://web.libera.chat/#rubyonrails)])

**Ruby** is an interpreted programming language. An implementation of the Ruby interpreter is required for software like [Rails](https://wiki.gentoo.org/wiki/Rails "Rails"), [passenger](https://wiki.gentoo.org/wiki/Rails#passenger_via_apache "Rails"), and [GitLab](https://wiki.gentoo.org/wiki/GitLab "GitLab").

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
    -   [[1.3] [Adding a new implementation]](#Adding_a_new_implementation)
    -   [[1.4] [Installing a test implementation]](#Installing_a_test_implementation)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [make.conf]](#make.conf)
    -   [[2.2] [Select a Ruby slot with eselect]](#Select_a_Ruby_slot_with_eselect)
-   [[3] [Troubleshooting]](#Troubleshooting)
    -   [[3.1] [Package fails to emerge due to missing Ruby target(s)]](#Package_fails_to_emerge_due_to_missing_Ruby_target.28s.29)
-   [[4] [Removal]](#Removal)
    -   [[4.1] [Removing an old implementation]](#Removing_an_old_implementation)
-   [[5] [See also]](#See_also)
-   [[6] [External resources]](#External_resources)
-   [[7] [References]](#References)

## [Installation]

### [USE flags]

### [USE flags for] [dev-lang/ruby](https://packages.gentoo.org/packages/dev-lang/ruby) [[]] [An object-oriented scripting language]

  ------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+ssl`](https://packages.gentoo.org/useflags/+ssl)                 Add support for SSL/TLS connections (Secure Socket Layer / Transport Layer Security)
  [`berkdb`](https://packages.gentoo.org/useflags/berkdb)             Add support for sys-libs/db (Berkeley DB)
  [`debug`](https://packages.gentoo.org/useflags/debug)               Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`doc`](https://packages.gentoo.org/useflags/doc)                   Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`examples`](https://packages.gentoo.org/useflags/examples)         Install examples, usually source code
  [`gdbm`](https://packages.gentoo.org/useflags/gdbm)                 Add support for sys-libs/gdbm (GNU database libraries)
  [`jemalloc`](https://packages.gentoo.org/useflags/jemalloc)         Use dev-libs/jemalloc for memory management
  [`jit`](https://packages.gentoo.org/useflags/jit)                   Enable just-in-time compilation for improved performance. May prevent use of some PaX memory protection features in Gentoo Hardened.
  [`socks5`](https://packages.gentoo.org/useflags/socks5)             Add support for the socks5 proxy
  [`static-libs`](https://packages.gentoo.org/useflags/static-libs)   Build static versions of dynamic libraries as well
  [`systemtap`](https://packages.gentoo.org/useflags/systemtap)       Enable SystemTap/DTrace tracing
  [`tk`](https://packages.gentoo.org/useflags/tk)                     Add support for Tk GUI toolkit
  [`valgrind`](https://packages.gentoo.org/useflags/valgrind)         Enable annotations for accuracy. May slow down runtime slightly. Safe to use even if not currently using dev-debug/valgrind
  [`xemacs`](https://packages.gentoo.org/useflags/xemacs)             Add support for XEmacs
  ------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-12 23:35] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Emerge the base package:

`root `[`#`]`emerge --ask dev-lang/ruby`

** Note**\
Adding the base package in this way will pull it into the system\'s [\@world set](https://wiki.gentoo.org/wiki/World_set_(Portage) "World set (Portage)"). Those who are not developing Ruby packages or have some clear and explicit reason for directly emerging the package should gather additional information before proceeding.

### [Adding a new implementation]

To add a new implementation, first adjust the Ruby target variable in [/etc/portage/package.use/00Ruby]. For example, if upgrading from Ruby 2.5 to Ruby 2.6, add `ruby26` to the `RUBY_TARGETS` variable:

[FILE] **`/etc/portage/package.use/00Ruby`**

    # 2020-04-05 upgrade from ruby 2.5 to ruby 2.6 -Larry
    # RUBY_TARGETS="ruby25"
    */* RUBY_TARGETS: ruby25 ruby26"

Next perform an upgrade of the Ruby base package:

`root `[`#`]`emerge --ask --oneshot --update dev-lang/ruby`

List then select the newly installed implementation using eselect:

`root `[`#`]`eselect ruby list`

    Available Ruby profiles:
      [1]   ruby25 (with Rubygems) *
      [2]   ruby26 (with Rubygems)

`root `[`#`]`eselect ruby set ruby26`

    Successfully switched to profile:
      ruby26

Finally, update the rest of the packages on the system. This will avoid certain bugs^[\[1\]](#cite_note-1)^ that require the newly emerged Ruby implementation to be selected before upgrading. It will force all packages that depend on and support the Ruby 2.6 base implementation to rebuilt:

`root `[`#`]`emerge --ask --update --deep --newuse @world`

Once all packages depending on the newly installed implementation have been rebuilt, the older implementation can be unmerged (uninstalled). For removal instructions the [Removal section](#Removal) below.

### [Installing a test implementation]

Starting with Ruby 2.2 the [Gentoo Ruby project](https://wiki.gentoo.org/wiki/Project:Ruby "Project:Ruby") is using the stable mask mechanism to keep new Ruby implementations marked as testing until they are ready to be unmasked. For example, to use Ruby 2.7 on an otherwise stable system, apply the following changes:

[FILE] **`/etc/portage/profile/use.stable.mask`Unmasking flags for Ruby 2.7**

    -ruby_targets_ruby27

For further information please see the [similar instructions for Python](https://wiki.gentoo.org/wiki/Project:Python/PYTHON_TARGETS#Unmasking_non-stable_implementation_on_a_stable_system "Project:Python/PYTHON TARGETS").

## [Configuration]

### [make.conf]

Activate a specific Ruby implementations by adding `RUBY_TARGETS="$implementation"` to . Please note: setting the `RUBY_TARGETS` variable may overwrite the implementations set by the systems base profile.

[FILE] **`/etc/portage/package.use/00Ruby`**

    */* RUBY_TARGETS: ruby25 ruby26 ruby27

Multiple Ruby implementations in can be installed in parallel. The `RUBY_TARGETS` variable picks the implementations from `USE_RUBY` (which is set ebuilds depending on Ruby) and (re)compiles packages with support for each selected implementation.

### [Select a Ruby slot with eselect]

Ruby is slotted in Portage, to view which installed version slot the system is currently using, run:

`root `[`#`]`eselect ruby list`

To change the selected slot, issue:

`root `[`#`]`eselect ruby set ruby26`

## [Troubleshooting]

### [][Package fails to emerge due to missing Ruby target(s)]

When a world update fails due to missing a Ruby target, [emerge] will show the following output:

     * You need to select at least one compatible Ruby installation target via RUBY_TARGETS in make.conf.
     * Compatible targets for this package are: ruby26
     * ruby27
     *
     * See https://www.gentoo.org/proj/en/prog_lang/ruby/index.xml#doc_chap3 for more information.
     *
     * ERROR: app-misc/hivex-1.3.20::gentoo failed (prepare phase):
     *   No compatible Ruby target selected.
     *
     * Call stack:
     *     ebuild.sh, line  127:  Called src_prepare
     *   environment, line 3475:  Called ruby-ng_src_prepare
     *   environment, line 3224:  Called _ruby_each_implementation '_ruby_source_copy'
     *   environment, line  939:  Called die
     * The specific snippet of code:
     *           die "No compatible Ruby target selected.";

To fix the issue, add the target(s) displayed above into the `RUBY_TARGETS` variable in Portage\'s [/etc/portage/make.conf] file and re-run previously failed [emerge] command. See the [make.conf section](#make.conf) above.

## [Removal]

### [Removing an old implementation]

To remove an old implementation, in this case Ruby 2.4, first be certain Ruby has been updated (see the [Adding a new implementation section](#Adding_a_new_implementation)). A newer implementation of Ruby will need to be installed *before* an older implementation can be removed. This is to ensure the packages that depend on Ruby will have an interpreter with which to run.

After the new implementation has been selected, remove the old implementation from the `RUBY_TARGETS` variable:

[FILE] **`/etc/portage/package.use/00Ruby`Removing the Ruby 2.4 implementation**

    # RUBY_TARGETS="ruby24 ruby25" # 2020-04-05 removed ruby24 -Larry
    */* RUBY_TARGETS: -ruby24 ruby25

It is safe not to add *and* remove targets to the `RUBY_TARGETS` variable in one step.

Next, ask Portage to rebuild the [\@world set](https://wiki.gentoo.org/wiki/Package_sets#System_defining_sets "Package sets") with the new Ruby target list:

`root `[`#`]`emerge --ask --update --deep --newuse @world`

After the emerge completes, update the slot to the newly installed version (2.5 in this case) using [eselect] as [mentioned above](#Select_a_Ruby_slot_with_eselect).

Finally, as long as no packages are still using the old version, it should be removable by asking Portage to do a dependency clean:

`root `[`#`]`emerge --depclean`

## [See also]

-   [Python](https://wiki.gentoo.org/wiki/Python "Python") --- an extremely popular cross-platform object oriented programming language.
-   [Project:Ruby](https://wiki.gentoo.org/wiki/Project:Ruby "Project:Ruby")
-   [Gem](https://wiki.gentoo.org/wiki/Gem "Gem") --- programs and libraries for the [Ruby] programming language.

## [External resources]

-   [Codecademy\'s Ruby course](https://www.codecademy.com/tracks/ruby)

## [References]

1.  [[[↑](#cite_ref-1)] [[[[bug #628838]](https://bugs.gentoo.org/show_bug.cgi?id=628838)[]]]]