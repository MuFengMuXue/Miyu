This article explains package categories [acct-user](https://packages.gentoo.org/categories/acct-user) and [acct-group](https://packages.gentoo.org/categories/acct-group) from the Gentoo ebuild repository.

## Contents

-   [[1] [Summary]](#Summary)
-   [[2] [Details]](#Details)
    -   [[2.1] [Category acct-user]](#Category_acct-user)
    -   [[2.2] [Category acct-group]](#Category_acct-group)
-   [[3] [See also]](#See_also)
-   [[4] [External resources]](#External_resources)

## [Summary]

Some packages pull in other packages with names of the form [acct-user/\*] and [acct-group/\*] as dependencies. This is normal, they are similar to packages in category [virtual](https://packages.gentoo.org/categories/virtual), install no files, are used to manage the operating system\'s user and group account databases, and, in most cases, users don\'t need to take any specific action.

## [Details]

Packages in categories [acct-user] and [acct-group], as well as the [eclasses](https://wiki.gentoo.org/wiki/Eclass "Eclass") of the same name, are used to implement the policy set by Gentoo Linux Enhancement Proposal ([GLEP](https://www.gentoo.org/glep)) 81: *\"[User and group management via dedicated packages](https://www.gentoo.org/glep/glep-0081.html)\"*, in May 2019.

These are not \'real\' packages, in the sense that they do not install files; instead, they are used to perform updates to the operating system\'s user and group account databases in a systematic and ordered manner, using existing package manager mechanisms specified in the [Package Manager Specification](https://wiki.gentoo.org/wiki/Package_Manager_Specification "Package Manager Specification"). This avoids requiring a new [EAPI](https://wiki.gentoo.org/wiki/EAPI "EAPI") or changes in the package manager\'s code.

Some packages need particular accounts to exist in the user or group databases, e.g. for a file\'s owner and/or group, or for a long-running process\' (*daemon*) effective user and/or group. Traditionally, account databases management was done ad-hoc by every ebuild that needed it. However, GLEP 81 mentions that:

-   Some packages might share the same user or group, so the problem of doing so reliably among different packages should be addressed.
-   Sharing users and groups reliably among different packages, and different Gentoo systems, requires consistent user IDs (UIDs) and group IDs (GIDs).
-   No systematic way of tracking which packages need specific users or groups existed, and that complicates determining which ones are obsolete.

For more information about the motivation of and rationale for GLEP 81, please [consult it](#External_resources).

Each [acct-user/\*] and [acct-group/\*] package corresponds to a single user or group account, respectively, and has that account\'s name. It logically represents the ownership of the corresponding user or group, and technically implements its creation if it doesn\'t currently exist in the corresponding account database. Packages that need a specific account use package dependency specifications to pull the required user/group packages, e.g. in the value of the `RDEPEND` variable, to specify that the account is needed at runtime or at install time. This allows the package manager to link packages with the specific accounts they need.

For example, package [[[acct-user/mysql]](https://packages.gentoo.org/packages/acct-user/mysql)[]] corresponds to the user account with name [mysql], needed e.g. by packages [[[dev-db/mariadb]](https://packages.gentoo.org/packages/dev-db/mariadb)[]], [[[dev-db/mysql]](https://packages.gentoo.org/packages/dev-db/mysql)[]] and [[[dev-db/percona-server]](https://packages.gentoo.org/packages/dev-db/percona-server)[]] when the `server` [USE flag](https://wiki.gentoo.org/wiki/USE_flag "USE flag") is set, and package [[[acct-group/input]](https://packages.gentoo.org/packages/acct-group/input)[]] corresponds to the group account with name [input], needed e.g. by packages [[[sys-fs/eudev]](https://packages.gentoo.org/packages/sys-fs/eudev)[]], [[[sys-fs/udev]](https://packages.gentoo.org/packages/sys-fs/udev)[]] and [[[sys-apps/systemd]](https://packages.gentoo.org/packages/sys-apps/systemd)[]].

All [acct-user/\*] and [acct-group/\*] packages in Gentoo\'s ebuild repository define a preferred, fixed UID and GID, respectively, that is unique within the repository. [acct-user/\*] and [acct-group/\*] packages can also exist in [alternative ebuild repositories](https://wiki.gentoo.org/wiki/Ebuild_repository "Ebuild repository"), and can specify that the UID and GID, respectively, be dynamically allocated.

Installing an [acct-user/\*] and [acct-group/\*] package pulled as a dependency when the corresponding account exists does not modify the account databases, it only registers the dependency with the package manager.

### [Category acct-user]

Ebuilds for packages in category [acct-user] conform to [EAPI](https://wiki.gentoo.org/wiki/EAPI "EAPI") 7, and generally inherit the [acct-user] [eclass](https://wiki.gentoo.org/wiki/Eclass "Eclass") (i.e. contain an `inherit acct-user` command), and consist of variable assignments. They contain at least:

-   An assignment to variable `ACCT_USER_ID`, specifying the preferred user ID. It can be set to `-1` in [alternative ebuild repositories](https://wiki.gentoo.org/wiki/Ebuild_repository "Ebuild repository") to dynamically allocate the UID.
-   An assignment to variable `ACCT_USER_GROUPS`. This is a [Bash](https://wiki.gentoo.org/wiki/Bash "Bash") array with at least one element, the group ID of the user\'s primary group. If the array contains more that one element, every element after the first one specifies the group ID of a user\'s supplementary group. It is possible to add further supplementary groups during the installation of the ebuild with the space-separated list variable *ACCT_USER\_\<UPPERCASE_USERNAME\>\_GROUPS_ADD* in *make.conf.*
-   An invocation of the `acct-user_add_deps()` function in global scope, after the assignment to `ACCT_USER_GROUPS`. This creates a runtime dependency on the [acct-group/\*] packages that correspond to the accounts specified in `ACCT_USER_GROUPS`, by adding them to the value of the `RDEPEND` variable.

Additionally, the ebuild can contain assignments to the following variables:

-   `ACCT_USER_HOME`: The pathname of the user\'s home directory.
-   `ACCT_USER_HOME_OWNER`: The owner and group of the user\'s home directory, using the [chown] command\'s *user:group* syntax.
-   `ACCT_USER_HOME_PERMS`: The permissions of the user\'s home directory, using any syntax accepted by the [chmod] command.
-   `ACCT_USER_SHELL`: The user\'s shell, as the pathname of the shell\'s executable.
-   `ACCT_USER_ENFORCE_ID`: If set to a non-empty value, package installation will fail if the account already exists with a different UID, or if the UID specified by `ACCT_USER_ID` is taken by a different account. Otherwise, if the preferred UID specified by `ACCT_USER_ID` cannot be used, a different one is dynamically allocated.

If these variables are not set in the ebuild, default values are provided by the [acct-user] eclass, as well as default values for the `DESCRIPTION`, `SLOT` and `KEYWORDS` variables.

The [acct-user] eclass exports default definitions (`EXPORT_FUNCTIONS`) of the `pkg_pretend()`, `src_install()`, `pkg_preinst()`, `pkg_postinst()` and `pkg_prerm()` phase functions:

-   The exported `pkg_pretend()` verifies, if `ACCT_USER_ENFORCE_ID` is set by the ebuild to a non-empty value, that the specified UID is free and can be used by the account.
-   The exported `src_install()` creates the home directory using the [keepdir] command if it doesn\'t exist, and if `ACCT_USER_HOME` is specified in the ebuild and not set to [/dev/null].
-   The exported `pkg_preinst()` actually creates the account by calling function `enewuser()` from the [user] eclass, if it didn\'t exist before package installation, and sets the home directory\'s owner, group and permissions according to `ACCT_USER_HOME_OWNER` and `ACCT_USER_HOME_PERMS`, using the [fowners] and [fperms] commands, if `ACCT_USER_HOME` is specified in the ebuild and not set to [/dev/null].
-   The exported `pkg_postinst()` unlocks the account if it existed before package installation, and sets the account\'s home directory, shell, groups and comment in the account database, according to `ACCT_USER_HOME`, `ACCT_USER_SHELL`, `ACCT_USER_GROUPS` and `DESCRIPTION`, respectively, using functions from the [user] eclass.
-   The exported `pkg_prerm()` locks the account if the package is uninstalled by the package manager. Following GLEP 81, account locking is performed on package removal, rather that removing the account altogether, to guarantee that no files with stale ownership are left (e.g. on unmounted filesystems), and that the same UID is not reused for another account.

For further technical details, check the [acct-user.eclass] file in the [eclass] subdirectory of [[/var/db/repos/gentoo]](https://wiki.gentoo.org/wiki//var/db/repos/gentoo "/var/db/repos/gentoo").

### [Category acct-group]

Ebuilds for packages in category [acct-group] conform to [EAPI](https://wiki.gentoo.org/wiki/EAPI "EAPI") 7, and generally inherit the [acct-group] [eclass](https://wiki.gentoo.org/wiki/Eclass "Eclass") (i.e. contain an `inherit acct-group` command), and consist of variable assignments. They contain at least an assignment to variable `ACCT_GROUP_ID`, specifying the preferred group ID. It can be set to `-1` in [alternative ebuild repositories](https://wiki.gentoo.org/wiki/Ebuild_repository "Ebuild repository") to dynamically allocate the GID. Additionally, the ebuild can contain an assignment to the `ACCT_GROUP_ENFORCE_ID` variable: if set to a non-empty value, package installation will fail if the account already exists with a different GID, or if the GID specified by `ACCT_GROUP_ID` is taken by a different account. Otherwise, if the preferred GID specified by `ACCT_GROUP_ID` cannot be used, a different one is dynamically allocated.

The [acct-group] eclass provides default values for the `DESCRIPTION`, `SLOT` and `KEYWORDS` variables, if they are not set in the ebuild, and exports default definitions (`EXPORT_FUNCTIONS`) of the `pkg_pretend()` and `pkg_preinst()` phase functions:

-   The exported `pkg_pretend()` verifies, if `ACCT_GROUP_ENFORCE_ID` is set by the ebuild to a non-empty value, that the specified GID is free and can be used by the account.
-   The exported `pkg_preinst()` actually creates the account by calling function `enewgroup()` from the [user] eclass, if it didn\'t exist before package installation.

For further technical details, check the [acct-group.eclass] file in the [eclass] subdirectory of [[/var/db/repos/gentoo]](https://wiki.gentoo.org/wiki//var/db/repos/gentoo "/var/db/repos/gentoo").

## [See also]

-   [Practical guide to the GLEP 81 migration](https://wiki.gentoo.org/wiki/Practical_guide_to_the_GLEP_81_migration "Practical guide to the GLEP 81 migration")
-   [Project:Quality Assurance/UID GID Assignment](https://wiki.gentoo.org/wiki/Project:Quality_Assurance/UID_GID_Assignment "Project:Quality Assurance/UID GID Assignment") --- a list of existing fixed UID/GID assignments in Gentoo.

## [External resources]

-   [GLEP 81](https://www.gentoo.org/glep/glep-0081.html)