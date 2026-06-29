**Resources**

[[![Gentoo peach graphic](/images/thumb/a/ad/Gentoo-logo-peach.svg/25px-Gentoo-logo-peach.svg.png)](https://wiki.gentoo.org/wiki/Project:Portage "Project:Portage")][Project](https://wiki.gentoo.org/wiki/Project:Portage "Project:Portage")

**portageq** is a tool to quickly query Portage information. It comes pre-installed as part of Portage and is primarily used by Gentoo developers in order to determine Portage configuration information.

## Contents

-   [[1] [Usage]](#Usage)
    -   [[1.1] [Invocation]](#Invocation)
    -   [[1.2] [Querying environment variables]](#Querying_environment_variables)
    -   [[1.3] [Query repository information]](#Query_repository_information)
    -   [[1.4] [Query package metadata]](#Query_package_metadata)
-   [[2] [See also]](#See_also)

## [Usage]

### [Invocation]

`user `[`$`]`portageq --help`

    >>> Portage information query tool
    >>> 2.2.20.1
    >>> Usage: portageq <command> [<option> ...]

    Available commands:
       all_best_visible <eroot>
          Returns all best_visible packages (without .ebuild).
       available_eclasses <eroot> <repo_id>+
          Returns space-separated list of available eclasses for specified repository.
       best_version <eroot> <category/package>
          Returns highest installed matching category/package-version (without .ebuild).
       best_visible <eroot> [pkgtype] <atom>
          Returns category/package-version (without .ebuild).
          The pkgtype argument defaults to "ebuild" if unspecified,
          otherwise it must be one of ebuild, binary, or installed.
       colormap Display the color.map as environment variables.
       config_protect Returns the CONFIG_PROTECT paths.
       config_protect_mask Returns the CONFIG_PROTECT_MASK paths.
       contents <eroot> <category/package>
          List the files that are installed for a given package, with
          one file listed on each line. All file names will begin with
          <eroot>.
       distdir Returns the DISTDIR path.
       eclass_path <eroot> <repo_id> <eclass>+
          Returns the path to specified eclass for specified repository.
       envvar <variable>+
          Returns a specific environment variable as exists prior to ebuild.sh.
          Similar to: emerge --verbose --info | egrep '^<variable>='
       expand_virtual <eroot> <atom>
          Returns a \n separated list of atoms expanded from a
          given virtual atom (GLEP 37 virtuals only),
          excluding blocker atoms. Satisfied
          virtual atoms are not included in the output, since
          they are expanded to real atoms which are displayed.
          Unsatisfied virtual atoms are displayed without
          any expansion. The "match" command can be used to
          resolve the returned atoms to specific installed
          packages.
       filter_protected <eroot>
          Read filenames from stdin and write them to stdout if they are protected.
          All filenames are delimited by \n and must begin with <eroot>.
       gentoo_mirrors Returns the mirrors set to use in the portage configuration.
       get_repo_path <eroot> <repo_id>+
          Returns the path to the repo named argv[1], argv[0] = $EROOT
       get_repos <eroot>
          Returns all repos with names (repo_name file) argv[0] = $EROOT
       has_version <eroot> <category/package>
          Return code 0 if it's available, 1 otherwise.
       is_protected <eroot> <filename>
          Given a single filename, return code 0 if it's protected, 1 otherwise.
          The filename must begin with <eroot>.
       license_path <eroot> <repo_id> <license>+
          Returns the path to specified license for specified repository.
       list_preserved_libs <eroot>
          Print a list of libraries preserved during a package update in the form
          package: path. Returns 1 if no preserved libraries could be found,
          0 otherwise.
       mass_best_version <eroot> [<category/package>]+
          Returns category/package-version (without .ebuild).
       mass_best_visible <eroot> [<type>] [<category/package>]+
          Returns category/package-version (without .ebuild).
          The pkgtype argument defaults to "ebuild" if unspecified,
          otherwise it must be one of ebuild, binary, or installed.
       master_repos <eroot> <repo_id>+
          This is an alias for the master_repositories command.
       master_repositories <eroot> <repo_id>+
          Returns space-separated list of master repositories for specified repository.
       match <eroot> <atom>
          Returns a \n separated list of category/package-version.
          When given an empty string, all installed packages will
          be listed.
       metadata <eroot>  <category/package> [<key>]+
          Returns metadata values for the specified package.
          Available keys: DEFINED_PHASES,DEPEND,DESCRIPTION,EAPI,HDEPEND,HOMEPAGE,INHERITED,IUSE,KEYWORDS,LICENSE,PDEPEND,PROPERTIES,PROVIDE,RDEPEND,REQUIRED_USE,RESTRICT,SLOT,SRC_URI
       owners <eroot> [<filename>]+
          Given a list of files, print the packages that own the files and which
          files belong to each package. Files owned by a package are listed on
          the lines below it, indented by a single tab character (\t). All file
          paths must either start with <eroot> or be a basename alone.
          Returns 1 if no owners could be found, and 0 otherwise.
       pkgdir Returns the PKGDIR path.
       portdir Returns the PORTDIR path.
          Deprecated in favor of get_repo_path command.
       portdir_overlay Returns the PORTDIR_OVERLAY path.
          Deprecated in favor of get_repos & get_repo_path or repos_config commands.
       pquery [options] [atom]+
          Emulates a subset of Pkgcore's pquery tool.
       repos_config <eroot>
          This is an alias for the repositories_configuration command.
       repositories_configuration <eroot>
          Returns the configuration of repositories.
       vdb_path Returns the path used for the var(installed) package database for the
          set environment/configuration options.

    Pkgcore pquery compatible options:

    usage: portageq pquery [options] [atom ...]

    Repository matching options:
      --no-filters          no visibility filters (ACCEPT_KEYWORDS, package
                            masking, etc)
      --repo REPO           repository to use (all repositories are used by
                            default)

    Package matching options:
      --herd HERD           exact match on a herd
      --maintainer-email MAINTAINER_EMAIL
                            comma-separated list of maintainer email regexes to
                            search for

    Output formatting:
      -n, --no-version      collapse multiple matching versions together

### [Querying environment variables]

Probably the only question users will have as they read through the help output above is the definition of *eroot*. eroot simply means the repository filesystem path (directory) and can be obtained by:

`user `[`$`]`portageq envvar EROOT`

    /

Queryable [Portage](https://wiki.gentoo.org/wiki/Portage "Portage") specific environmental variables are listed in [[/var/db/repos/gentoo/profiles](https://wiki.gentoo.org/wiki//var/db/repos/gentoo/profiles "/var/db/repos/gentoo/profiles")/info_vars]. The queryable user environment\'s [environment variables](https://wiki.gentoo.org/wiki/Handbook:AMD64/Working/EnvVar#Environment_variables "Handbook:AMD64/Working/EnvVar") can be shown using the [env] command.

Return the `CONFIG_PROTECT` variable value (should be a filesystem path):

`user `[`$`]`portageq config_protect`

Return the `DISTDIR` variable value (should be a filesystem path):

`user `[`$`]`portageq distdir`

    /var/cache/distfiles

Return the `PKGDIR` variable value (should be a filesystem path):

`user `[`$`]`portageq pkgdir`

    /var/cache/binpkgs

### [Query repository information]

To see a detailed list of repositories as configured in [repos.conf](https://wiki.gentoo.org/wiki//etc/portage/repos.conf "/etc/portage/repos.conf"), without any formatting:

`user `[`$`]`portageq repos_config /`

To see a list of repositories sorted by priority (highest first):

`user `[`$`]`portageq get_repos /`

### [Query package metadata]

To get a specific piece of metadata about an atom (i.e. package name including version):

`user `[`$`]`portageq metadata / ebuild sys-devel/gcc-13.2.1_p20231216 HOMEPAGE`

The general syntax for the `metadata` subcommand is:

    metadata <eroot>  <category/package> [<key>]+

where:

-   `` is one of `ebuild`, `porttree`, `binary`, `bintree`, `installed` or `vartree`;

and

-   `<key>` is one or more of `BDEPEND`, `DEFINED_PHASES`, `DEPEND`, `DESCRIPTION`, `EAPI`, `HOMEPAGE`, `IDEPEND`, `INHERIT`, `INHERITED`, `IUSE`, `KEYWORDS`, `LICENSE`, `PDEPEND`, `PROPERTIES`, `RDEPEND`, `REQUIRED_USE`, `RESTRICT`, `SLOT` and `SRC_URI`.

## [See also]

-   [Elogv](https://wiki.gentoo.org/wiki/Elogv "Elogv") --- a curses-based tool that parses the contents of [elogs](https://wiki.gentoo.org/wiki/Portage_log "Portage log") created by Portage.
-   [Egencache](https://wiki.gentoo.org/wiki/Egencache "Egencache") --- a tool that (re)builds metadata information for the Portage package database.
-   [Environment variables](https://wiki.gentoo.org/wiki/Handbook:AMD64/Working/EnvVar "Handbook:AMD64/Working/EnvVar") (AMD64 handbook)