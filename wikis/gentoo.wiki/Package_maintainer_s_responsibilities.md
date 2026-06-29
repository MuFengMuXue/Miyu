This page aids developers in getting familiar with the tasks and responsibilities of a package maintainer in Gentoo. It may be found useful for community members who are curious about stepping up as a maintainer, returning from a long hiatus, or those who are simply looking for tips.

Not everything listed in here need to be incorporated to a workflow, but following these steps should keep the Gentoo repository in a clean working state, keep your activity up, and ease maintainer tasks.

General responsibilities as a maintainer consist of:

1.  keeping ebuilds up-to-date with upstream releases,
2.  responding to and fixing assigned bugs,
3.  handling possible stabilization of packages in time.

It is also important to keep up with the Python, Ruby, PHP, etc. ecosystems in Gentoo.

*Rationale: If a package has existing stable keywords you **must** request stabilization of a newer version within a reasonable time frame (usually at least 30 days, but see the [stabilization section in devmanual](https://devmanual.gentoo.org/keywording/workflow/index.html#moving-from-arch-to-arch)), provided there are no regressions compared to the last stable version. This prevents stable users from being stuck on old versions of the package with no justification.*

*Rationale: It is also important to add the latest e.g. Python versions which a package supports as soon as possible to avoid conflicts for users when the default Python target in the Gentoo profiles changes. See* [Daily / Occasional pkgcheck scans](https://wiki.gentoo.org/wiki/Package_maintainer%27s_responsibilities#Daily_.2F_Occasional_pkgcheck_scans "Package maintainer's responsibilities") *for a tip to quickly check for a `PYTHON_COMPAT` update in packages.*

## Contents

-   [[1] [Bugzilla]](#Bugzilla)
-   [[2] [Ebuilds and git workflow]](#Ebuilds_and_git_workflow)
    -   [[2.1] [GitHub pull requests]](#GitHub_pull_requests)
-   [[3] [External tools]](#External_tools)
    -   [[3.1] [Package updates, and bugs]](#Package_updates.2C_and_bugs)
    -   [[3.2] [CI issues with packages]](#CI_issues_with_packages)
    -   [[3.3] [Daily / Occasional pkgcheck scans]](#Daily_.2F_Occasional_pkgcheck_scans)
-   [[4] [External resources]](#External_resources)

## [Bugzilla]

[Gentoo\'s Bugzilla](https://bugs.gentoo.org/) is still the main communication channel to reach you with your package state. When a bug report gets assigned to a developer, the first thing you should attempt to do is to confirm and replicate it with the information attached to the bug. You should then either mark the bug as \"CONFIRMED\", or provide a comment that you can\'t.

Keep an eye out for CI/tinderbox-style bugs too, which are found by testing the latest ebuilds (by commit) and random packages, respectively. They reveal breakages on different systems, mostly missing dependencies, and make you face issues you perhaps hadn\'t thought of before.

When you make a commit to Gentoo\'s git tree, please remember to reference or close a single bug, or multiple bugs, by using *Bug:* or *Closes:* tag in your git commit message\'s footer area. [See an example, and more documentation](https://devmanual.gentoo.org/ebuild-maintenance/git/index.html#git-commit-message-format).

[Stabilization can be done by a maintainer who is also a developer, and owns relevant hardware](https://devmanual.gentoo.org/keywording/workflow/index.html#stabilization-rules). It can also be [requested through Bugzilla](https://devmanual.gentoo.org/keywording/workflow/index.html#moving-from-arch-to-arch) for arch teams to handle, even for your own packages.

It is recommended to set up your mail client\'s filtering properly. Separating Bugzilla mail from generic alias mail, mailing lists, GitHub etc, helps to create an organized workflow and time usage.

A simple alias separation, for example, is done by simple filters:

    # example project, Bugzilla mail
    To-contains: example@gentoo.org
    From-is: bugzilla-daemon@gentoo.org

    # example project, alias mail
    To-contains: example@gentoo.org
    From-isn't: bugzilla-daemon@gentoo.org

And a separate personal Bugzilla email such as:

    # Personal Bugzilla mail
    To-is: developer@gentoo.org
    From-is: bugzilla-daemon@gentoo.org

You can separate mailing list e-mails similarly, etc. See [Project:Infrastructure/Developer_E-Mail/Sieve_Example](https://wiki.gentoo.org/wiki/Project:Infrastructure/Developer_E-Mail/Sieve_Example "Project:Infrastructure/Developer E-Mail/Sieve Example") for an example.

Any GitHub pull requests linked to your bugs are shown in the \"See also\" field. See the [Github pull requests](https://wiki.gentoo.org/wiki/Package_maintainer%27s_responsibilities#GitHub_pull_requests "Package maintainer's responsibilities") section below.

Check bugs assigned to you by searching `assignee:developer@gentoo.org`. You can also see them in [Bugzilla\'s front page](https://bugs.gentoo.org/) after logging in, \"Open bugs assigned to me\". And also in [Package_maintainer\'s_responsibilities#Package_updates.2C_and_bugs](https://wiki.gentoo.org/wiki/Package_maintainer%27s_responsibilities#Package_updates.2C_and_bugs "Package maintainer's responsibilities").

## [Ebuilds and git workflow]

See the devmanual\'s [Git for Gentoo Developers page](https://devmanual.gentoo.org/ebuild-maintenance/git/index.html) for git configuration help.

When writing and pushing ebuilds to Gentoo\'s ebuild repository (and why not to any overlay as well) QA tools should be utilized whenever possible. [pkgcheck] is the best choice for developers, however some developers use custom scripts. It can be installed from gentoo:: with:

`root `[`#`]`emerge --ask dev-util/pkgdev`

Make sure you don\'t blindly copy-paste an old ebuild and try to push that. Always take a look and try to spot the obvious outdated parts - such as old EAPI, [unguarded external tool calls](https://devmanual.gentoo.org/ebuild-writing/error-handling/index.html#the-die-function), new Python compatibility update, [etc](https://devmanual.gentoo.org/ebuild-writing/common-mistakes/index.html).

** Note**\
EAPI availability is usually dictated by the state of eclasses being used.

After ebuilds or [metadata.xml] files have been modified, run [pkgcheck scan] in the package directory to perform QA checks.

[pkgcheck] will not catch every issue. So watch out for [common mistakes](https://devmanual.gentoo.org/ebuild-writing/common-mistakes/index.html) when writing ebuilds. In general, familiarize yourself with the Quality Assurance\'s [Policy guide](https://projects.gentoo.org/qa/policy-guide/) and if writing Python ebuilds, the Python project\'s [Python guide](https://dev.gentoo.org/~mgorny/python-guide/).

When committing changes, [pkgdev commit -s] (from the [[[dev-util/pkgdev]](https://packages.gentoo.org/packages/dev-util/pkgdev)[]] package) can be used. It will properly sign-off the commits with accordance to Gentoo\'s [GLEP 76 requirements](https://www.gentoo.org/glep/glep-0076.html#certificate-of-origin). This tool will also append the correct, GLEP 66 compliant [summary](https://devmanual.gentoo.org/ebuild-maintenance/git/index.html#git-commit-message-format).

Commits also need to be PGP-signed, so keep encryption keys [up-to-date](https://wiki.gentoo.org/wiki/Project:Infrastructure/Generating_GLEP_63_based_OpenPGP_keys#Invalid_expiration_date "Project:Infrastructure/Generating GLEP 63 based OpenPGP keys") and [available](https://wiki.gentoo.org/wiki/Project:Infrastructure/Generating_GLEP_63_based_OpenPGP_keys#Submit_your_new_key_to_the_keyserver "Project:Infrastructure/Generating GLEP 63 based OpenPGP keys") in Gentoo\'s infra.

After committing, use [pkgcheck scan \--commits] for a final check before issuing [git pull && git push] or [git pull && pkgdev push]. Of course, [git log -p] before pushing does not hurt either. [git status] will help confirm no other files have been accidentally modified, or uncommitted work (like a [.patch] file) before pushing. Those unfamiliar with git can review [\"A better ebuild workflow with pure git and pkgcheck\"](https://blogs.gentoo.org/mgorny/2019/12/12/a-better-ebuild-workflow-with-pure-git-and-pkgcheck/) blog entry for a short guide.

Gentoo\'s [CI system](https://qa-reports.gentoo.org/output/gentoo-ci/output.html) runs pkgcheck, so familiarizing one\'s self with pkgcheck and its warnings is encouraged. If you add a new warning to the tree, you will get an e-mail from \"repomirrorci@g.o\" with the warning, and this could most likely have been prevented by running [pkgcheck scan \--commits] before pushing the changes. A new CI error will prevent metadata being generated to Gentoo\'s sync-repositories, and therefore deny users the latest updates until the CI error is fixed. Note the difference in severity between warnings and errors.

By default [pkgcheck] enables a lot of checks. Some of them are more useful than the others. pkgcheck can be configured via the [\~/.config/pkgcheck/pkgcheck.conf] file. For example, a sane configuration could look like this:

[FILE] **`~/.config/pkgcheck/pkgcheck.conf`pkgcheck configuration example**

    # ~/.config/pkgcheck/pkgcheck.conf
    #
    # -ImlateCheck = PotentialStable, all of these checks are just noise.
    [DEFAULT]
    checks = -ImlateCheck,-RedundantVersionCheck,-UnstableOnlyCheck

Refer to the [official pkgcheck documentation](https://pkgcore.GitHub.io/pkgcheck/man/pkgcheck.html) for all options and edit as needed.

It is also possible enable the desired checks from the command line each time pkgcheck is called however, this will become repetitive and tedious, e.g., [pkgcheck scan -c StableRequestCheck]. More on that below.

When unsure of the meaning or how to fix a warning, be sure to ask fellow developer for assistance. If in doubt about who to ask, head to the [[#gentoo-dev](ircs://irc.libera.chat/#gentoo-dev)] ([[webchat](https://web.libera.chat/#gentoo-dev)]), [[#gentoo-qa](ircs://irc.libera.chat/#gentoo-qa)] ([[webchat](https://web.libera.chat/#gentoo-qa)]), or [[#gentoo-dev-help](ircs://irc.libera.chat/#gentoo-dev-help)] ([[webchat](https://web.libera.chat/#gentoo-dev-help)]) (for non-developers too) IRC channels. if something is not fully clear, be sure to ask before pushing.

### [GitHub pull requests]

Some developers may find themselves in a position where users provide contributions to their ebuilds via GitHub pull requests. As GitHub is a popular platform, Gentoo is seeing many contributions pushed there. That being said, using GitHub is not mandatory and Bugzilla is still the main channel for reporting enhancements to the Gentoo ebuild repository.

**Joining the Gentoo GitHub organization:** To join the Gentoo GitHub organization, make sure the `gentooGitHubUser` LDAP attribute has been set in infrastructures [dev.gentoo.org\'s LDAP record](https://wiki.gentoo.org/wiki/Project:Infrastructure/LDAP_Guide#Optional_custom_attributes "Project:Infrastructure/LDAP Guide"). Join [[#gentoo-infra](ircs://irc.libera.chat/#gentoo-infra)] ([[webchat](https://web.libera.chat/#gentoo-infra)]) on the Libera IRC network to ask for a manual re-sync, and you will be added to the Gentoo organization in GitHub. You should be automatically added to teams you\'re part of. Remember to once again update your mail filters so you can organize incoming mail from GitHub better.

**The CI check in GitHub:** GitHub pull requests feature a powerful CI check to ensure the commits won\'t break repository\'s integrity. As said, a new CI error will prevent metadata being generated thus denying users the latest updates, until the CI error is fixed. Every pull request gets tested, and you\'ll see **\@gentoo-repo-qa-bot** commenting whether the pull requests passes or fails the CI check with a *Pull request CI report* comment. Pay attention to this report, as it shows very clearly where and why the PR fails, if it fails. You can utilize this CI check even for your own commits if you\'re afraid it\'s going to break something - e.g. when doing [profile/] updates. Just open a [pull request of your own](https://wiki.gentoo.org/wiki/Gentoo_GitHub#How_to_make_a_pull_request "Gentoo GitHub") against our [gentoo/gentoo GitHub mirror](https://github.com/gentoo/gentoo).

**Reviewing pull requests:** GitHub\'s Web UI provides an easy interface to review individual commits, or all changes at once. Make sure you thoroughly read through all parts of the contribution and hold it to the same standards as your own work, i.e., latest EAPI, updated Python compatibility, missing `|| dies` etc. And again, [pkgcheck] does not catch everything a human does (and vice versa).

Alternatively, [[[dev-util/github-cli]](https://packages.gentoo.org/packages/dev-util/github-cli)[]] can be used to work with pull requests.

**Testing pull requests:** All contributions should be tested. Even though the ebuild looks fine, unpredictable issues may be encountered, like changed `SRC_URI`, missing `DEPEND`, etc.

You can easily and quickly do the basic testing by merging it to a local repository, then running [emerge] against affected package(s). More thorough testing can be done via different chroots, containers, and virtual machines, but setting them up for a one-time run might be a bit much. [[[dev-util/ebuildtester]](https://packages.gentoo.org/packages/dev-util/ebuildtester)[]] is a great tool for situations like that. For continuous involvement with GitHub contributions, it is recommended to set up a more [permanent test environment](https://wiki.gentoo.org/wiki/Test_environment "Test environment"). See also [Package testing](https://wiki.gentoo.org/wiki/Package_testing "Package testing").

**Merging pull requests:** Since the [gentoo/gentoo GitHub repository](https://github.com/gentoo/gentoo) is just a mirror, we can\'t actually merge these **in** GitHub. So we merge the raw [.patch] files to our own git.gentoo.org repository.

[curl \| git -am -sS] can be used, but there are also tools to help you merge GitHub pull requests, and/or Bugzilla [.patch] files. See [[[app-portage/pram]](https://packages.gentoo.org/packages/app-portage/pram)[]] or [[[dev-perl/Gentoo-App-Pram]](https://packages.gentoo.org/packages/dev-perl/Gentoo-App-Pram)[]] for more information. At this point you can also fix any malformed commit summaries, messages etc. that do not adhere to Gentoo\'s GLEPS [66](https://www.gentoo.org/glep/glep-0066.html) and [76](https://www.gentoo.org/glep/glep-0076.html) requirements. If the author has added their sign-off to their contribution, per GLEP-76 their copyrighted work **can not** be modified. So perform the additional fixes and updates in a separate commit. Make sure to review the contribution so that broken ebuilds are not pushed and then fixing them afterwards, since it\'s also a learning experience for the contributor.

## [External tools]

If you are in doubt whether there is \"anything for you to do\" with your packages, use these external tools / resources to check state of your packages. And if these tools still report you have nothing to do, extend the checks to the projects you\'re involved with 😉

### [][Package updates, and bugs]

[packages.gentoo.org](https://packages.gentoo.org/) provides a [Repology](https://repology.org/) integration, which shows which of your packages don\'t have the latest versions available in Gentoo\'s package repository. You can find it under the \"Outdated\" tab of your maintainer page, `https://packages.gentoo.org/maintainer/developer@gentoo.org`. You can also find open bugs assigned to you from this page behind the \"Bugs\" tab.

[Repology](https://repology.org/) itself provides an RSS feed to follow per maintainer, so if you search for \"Maintainer: developer@gentoo.org\", and get to `https://repology.org/maintainer/developer%40gentoo.org` page, you can find HTML and RSS feeds on the rightmost pane. These will announce when a package maintained by you gets a new version flagged in Repology.

** Note**\
If the package is unique to Gentoo, Repology obviously can\'t know about updates happening outside Gentoo.

### [CI issues with packages]

Our [QA reports](https://qa-reports.gentoo.org/) page reports all currently available CI issues within the main repository. You can filter this CI report page by appending `;maintainer=my@e.mail` matching the address listed in [metadata.xml] file. For example, `https://qa-reports.gentoo.org/output/gentoo-ci/output.html;maintainer=developer@gentoo.org` would show all CI issues for packages assigned to `developer@gentoo.org`. This works with projects and proxied maintainers alike.

More verbose checks can be obtained by adding [output.verbose.html] to the URL. `https://qa-reports.gentoo.org/output/gentoo-ci/output.verbose.html;maintainer=developer@gentoo.org`

** Note**\
For Gentoo developers, the developer tag is enough, i.e.,`;maintainer=developer`

### [][Daily / Occasional pkgcheck scans]

[pkgcheck] provides a tool to quickly check the overall state of your packages. To check for pending stabilizations, you can use something like can be ran in the root of the git tree.

`user `[`$`]`git grep -l developer@gentoo.org '**/metadata.xml' | cut -d/ -f1-2 | xargs pkgcheck --color true scan -c StableRequestCheck`

To see packages with identical `KEYWORDS`, which means some older versions can be cleaned from the tree, use:

`user `[`$`]`git grep -l developer@gentoo.org '**/metadata.xml' | cut -d/ -f1-2 | xargs pkgcheck --color true scan -c RedundantVersionCheck`

Finally, to combine these checks, run:

`user `[`$`]`git grep -l developer@gentoo.org '**/metadata.xml' | cut -d/ -f1-2 | xargs pkgcheck --color true scan -c RedundantVersionCheck,StableRequestCheck`

These two above checks are also shown in your maintainer page on [packages.gentoo.org](https://packages.gentoo.org/).

One more: check available `PYTHON_COMPAT` updates to packages with:

`user `[`$`]`git grep -l developer@gentoo.org '**/metadata.xml' | cut -d/ -f1-2 | xargs pkgcheck --color true scan -k PythonCompatUpdate`

\

## [External resources]

-   [A better ebuild workflow with pure git and pkgcheck](https://blogs.gentoo.org/mgorny/2019/12/12/a-better-ebuild-workflow-with-pure-git-and-pkgcheck/)
-   [Generating GLEP 63 based OpenPGPkeys](https://wiki.gentoo.org/wiki/Project:Infrastructure/Generating_GLEP_63_based_OpenPGP_keys "Project:Infrastructure/Generating GLEP 63 based OpenPGP keys")
-   [Gentoo GitHub - How to make a pull request](https://wiki.gentoo.org/wiki/Gentoo_GitHub#How_to_make_a_pull_request "Gentoo GitHub")
-   [Gentoo Python\'s guide](https://dev.gentoo.org/~mgorny/python-guide/)
-   [Gentoo QA\'s Policy Guide](https://projects.gentoo.org/qa/policy-guide/)
-   [Package testing](https://wiki.gentoo.org/wiki/Package_testing "Package testing")
-   [QA reports](https://qa-reports.gentoo.org/)
-   [Repology](https://repology.org)
-   [Test environment](https://wiki.gentoo.org/wiki/Test_environment "Test environment")
-   [Ultimate guide to EAPI-7](https://mgorny.pl/articles/the-ultimate-guide-to-eapi-7.html)
-   [Ultimate guide to EAPI-8](https://mgorny.pl/articles/the-ultimate-guide-to-eapi-8.html)