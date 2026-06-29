This article explains, how the GLEP 81 migration works and which special cases have to be considered.

## Contents

-   [[1] [Summary]](#Summary)
-   [[2] [Details]](#Details)
-   [[3] [Migration]](#Migration)
-   [[4] [Override acct packages]](#Override_acct_packages)
    -   [[4.1] [Override acct-user changes]](#Override_acct-user_changes)
        -   [[4.1.1] [System-wide]](#System-wide)
        -   [[4.1.2] [Per package]](#Per_package)
    -   [[4.2] [Override user groups]](#Override_user_groups)
        -   [[4.2.1] [System-wide]](#System-wide_2)
        -   [[4.2.2] [Per package]](#Per_package_2)
            -   [[4.2.2.1] [Example]](#Example)
    -   [[4.3] [Override others]](#Override_others)
-   [[5] [See also]](#See_also)

## [Summary]

In the past, user and group management was managed through various ebuilds, which were inheriting `user.eclass`. This means that there was no central user and group management, as instead each ebuild added users and groups in its own way. In order to provide central management for user and groups, [GLEP 81](https://www.gentoo.org/glep/glep-0081.html) was born.

## [Details]

[GLEP 81](https://www.gentoo.org/glep/glep-0081.html) describes how user and group management will be done in future. In practice this means, that ebuilds using a user/group will no longer create users or groups, but instead, all users and groups are managed through centralized ebuilds. Those centralized ebuilds will be provided by the categories `acct-group` for groups and `acct-user` for users. See [Categories_acct-group_and_acct-user](https://wiki.gentoo.org/wiki/Categories_acct-group_and_acct-user "Categories acct-group and acct-user") for more details in the technical implementation.

All ebuilds for `acct-group` and `acct-user` categories define which settings a group and an user will possess. Each ebuild which was previously inheriting `user.eclass` will depend on acct-\* packages in the \*DEPEND variable(s) after GLEP 81 migration.

Typical defined settings are:

-   UID and GID
-   Path to user home directory
-   Owner of user home directory
-   Permissions of home directory
-   An optional defined shell

This makes it possible to split all user and groups from the main ebuilds and provide separate updates to it. Each ebuild name in `acct-group` and `acct-user` categories represents the same name, which will be used for the added user and group to the local system.

In addition, all acct-\* packages are using fixed UID and GID. This provides the benefit, as all users and groups will always use across multiple systems the same UID and GID. A list as *source of truth* is provided in Git via [uid-gid.txt](https://gitweb.gentoo.org/data/api.git/tree/files/uid-gid.txt)

## [Migration]

Once a package has been migrated to [GLEP 81](https://www.gentoo.org/glep/glep-0081.html), it will be automatically installed by a normal [emerge -a -uvDU \@world] system update. This can be seen if [emerge] pulls in the corresponding acct-\* packages.

** Warning**\
Currently, once acct-\* packages are installed, all local user and group changes for this pulled in user and group will be completely lost, as `acct-*.eclass` will by default revert those changes.

## [Override acct packages]

As, by default, all local user and group changes will be reverted by acct-\* packages, there are three options to preserve those changes:

1.  Disable any changes to the user, which will be modified by `acct-user`. This can be set global or per package. This is discouraged because of possible inconsistencies that will be created in the system. If you must do this, do it locally per-package, not globally.
2.  Override assigned groups for the specified user. This is preferred to 1.
3.  Fork/copy the relevant `acct-*` ebuilds into an [ebuild repository configured with portage](https://wiki.gentoo.org/wiki/Creating_an_ebuild_repository "Creating an ebuild repository"), and customise them there.

### [Override acct-user changes]

To deactivate changes to users which have been already created, an environment variable `ACCT_USER_NO_MODIFY=1` must be defined.

#### [System-wide]

For a system-wide setting, the setting `ACCT_USER_NO_MODIFY=1` must be defined in [/etc/portage/make.conf]

** Warning**\
This approach is not recommended, as this will disable entirely all changes by `acct-user` packages and could lead to unforeseen problems. If possible, this should be configured per package.

#### [Per package]

The better approach is to disable `acct-user` changes per-package. This can be achieved by using the [/etc/portage/package.env] mechanism for **acct-user** packages. See the wiki article [[/etc/portage/package.env](https://wiki.gentoo.org/wiki//etc/portage/package.env "/etc/portage/package.env")] for how to create a per package configuration.

In this per package configuration, `ACCT_USER_NO_MODIFY=1` must be defined.

### [Override user groups]

If the local system has assigned various other groups to the user, which are not covered by the `acct-user` package, this would be by default removed from the local system.

In order to preserve such assignments, it\'s necessary to provide a custom configuration which will ensure that such group assignments will be preserved.

A special environment variable is available for this purpose, called `ACCT_USER_<UPPERCASE_USERNAME>_GROUPS`. Replace `<UPPERCASE_USERNAME>` with the local system user, which will be installed or updated by the `acct-user` package. This variable contains a space-separated list.

Alternatively, additional groups can be added to the ebuild\'s default groups by listing them in the environment variable `ACCT_USER_<UPPERCASE_USERNAME>_GROUPS_ADD`. Again, the value is a space-separated list.

#### [System-wide]

For a system-wide setting, the setting `ACCT_USER_<UPPERCASE_USERNAME>_GROUPS` or `ACCT_USER_<UPPERCASE_USERNAME>_GROUPS_ADD` must be defined in `/etc/portage/make.conf`

#### [Per package]

The better approach is to disable `acct-user` changes on a per-package basis. This can be achieved by using the `package.env` mechanism for **acct-user** packages. See the wiki article [[/etc/portage/package.env](https://wiki.gentoo.org/wiki//etc/portage/package.env "/etc/portage/package.env")] for how to create a per-package configuration.

In this per package configuration, `ACCT_USER_<UPPERCASE_USERNAME>_GROUPS` or `ACCT_USER_<UPPERCASE_USERNAME>_GROUPS_ADD` must be defined.

##### [Example]

Let\'s assume, you have currently installed [[[www-servers/apache]](https://packages.gentoo.org/packages/www-servers/apache)[]], which is still based on `user.eclass` and with the newest updated, a GLEP 81 migrated version will be pulled in. This means, that [emerge] would install [[[acct-user/apache]](https://packages.gentoo.org/packages/acct-user/apache)[]] and [[[acct-group/apache]](https://packages.gentoo.org/packages/acct-group/apache)[]]. If you didn\'t made any changes to the `apache` user, like assigning to different groups, you don\'t have to configure anything. But in this example, let\'s assume, you have assigned the `apache` user to additional groups named `foo` and `baz`.

In order to ensure, that this changes are not override by `acct-user`, as stated before, you would need to define `ACCT_USER_<UPPERCASE_USERNAME>_GROUPS_ADD`. In practice, an environment variable called `ACCT_USER_APACHE_GROUPS_ADD` must be definied with the value `foo baz`, to ensure that the user `apache` is added to the secondary groups `foo` and `baz`, in addition to the primary group `apache` defined by the ebuild.

**System-wide**: Add `ACCT_USER_APACHE_GROUPS_ADD="foo baz"` in [/etc/portage/make.conf].

**Per package**: Add `ACCT_USER_APACHE_GROUPS_ADD="foo baz"` in per package configuration.

### [Override others]

Please follow the pattern described above.

Similar variables exist for UID, comment, shell, and home:

-   `ACCT_USER_APACHE_ID`
-   `ACCT_USER_APACHE_COMMENT`
-   `ACCT_USER_APACHE_SHELL`
-   `ACCT_USER_APACHE_HOME`
-   `ACCT_USER_APACHE_HOME_OWNER`
-   `ACCT_USER_APACHE_HOME_PERMS`
-   `ACCT_USER_APACHE_GROUPS`

## [See also]

-   [Categories acct-group and acct-user](https://wiki.gentoo.org/wiki/Categories_acct-group_and_acct-user "Categories acct-group and acct-user") --- explains package categories [acct-user](https://packages.gentoo.org/categories/acct-user) and [acct-group](https://packages.gentoo.org/categories/acct-group) from the Gentoo ebuild repository.