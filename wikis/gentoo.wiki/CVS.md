[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=CVS&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://savannah.nongnu.org/projects/cvs)

[[]][Package information](https://packages.gentoo.org/packages/dev-vcs/cvs)

[[]][Guide](https://wiki.gentoo.org/wiki/CVS/Tutorial#.2FGuide "CVS/Tutorial")

[[]][Wikipedia](https://en.wikipedia.org/wiki/Concurrent_Versions_System "wikipedia:Concurrent Versions System")

**CVS** (**C**oncurrent **V**ersions **S**ystem) is a [version control system](https://en.wikipedia.org/wiki/Version_control "wikipedia:Version control") that builds on and expands [RCS](https://en.wikipedia.org/wiki/Revision_Control_System "wikipedia:Revision Control System"). CVS enables users to record the history of source files and documents.

** Note**\
CVS tends to be used less nowadays in favor of later generation VCSs, such as [git](https://wiki.gentoo.org/wiki/Git "Git").

** Warning**\
CVS is not recommended for hosting gentoo repositories (overlays), as it is not supported by [eselect repository](https://wiki.gentoo.org/wiki/Eselect/Repository "Eselect/Repository").

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
    -   [[1.3] [Configuration]](#Configuration)
-   [[2] [Usage]](#Usage)
-   [[3] [See also]](#See_also)
-   [[4] [External resources]](#External_resources)

## [Installation]

### [USE flags]

### [USE flags for] [dev-vcs/cvs](https://packages.gentoo.org/packages/dev-vcs/cvs) [[]] [Concurrent Versions System - source code revision control tools]

  ------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------
  [`crypt`](https://packages.gentoo.org/useflags/crypt)         Add support for encryption \-- using mcrypt or gpg where applicable
  [`doc`](https://packages.gentoo.org/useflags/doc)             Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`kerberos`](https://packages.gentoo.org/useflags/kerberos)   Add kerberos support
  [`nls`](https://packages.gentoo.org/useflags/nls)             Add Native Language Support (using gettext - GNU locale utilities)
  [`pam`](https://packages.gentoo.org/useflags/pam)             Add support for PAM (Pluggable Authentication Modules) - DANGEROUS to arbitrarily flip
  [`selinux`](https://packages.gentoo.org/useflags/selinux)     !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`server`](https://packages.gentoo.org/useflags/server)       Enable server support
  ------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-12-19 09:51] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Installing cvs is as easy as running an [emerge] command:

`root `[`#`]`emerge --ask dev-vcs/cvs`

** Note**\
If planning on using CVS for *serving* source code to clients be sure to emerge it with the [[[server]](https://packages.gentoo.org/useflags/server)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] [USE flag](https://wiki.gentoo.org/wiki/USE_flag "USE flag") set.

### [Configuration]

The default configuration file for CVS should be located in a file called [\~/.cvsrc] the user\'s home directory. Currently installing [[[dev-vcs/cvs]](https://packages.gentoo.org/packages/dev-vcs/cvs)[]] through [Portage](https://wiki.gentoo.org/wiki/Portage "Portage") does not create a default configuration file, therefore any specific configuration must be done by the user.

## [Usage]

Checkout a CVS module by using the following command:

`user `[`$`]`cvs checkout <module_name>`

## [See also]

-   The [CVS Tutorial](https://wiki.gentoo.org/wiki/CVS/Tutorial "CVS/Tutorial") article.

## [External resources]

-   The CVS man page locally ([man cvs]) or online at
-   [\[gentoo-dev\] Packages up for grabs: dev-vcs/cvs\* (post CVS project disband)](https://archives.gentoo.org/gentoo-dev/message/8c3e00874040dafa46f77470d6d5e121)