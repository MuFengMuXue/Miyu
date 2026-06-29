**Resources**

[[![Gentoo peach graphic](/images/thumb/a/ad/Gentoo-logo-peach.svg/25px-Gentoo-logo-peach.svg.png)](https://wiki.gentoo.org/wiki/Project:Portage "Project:Portage")][Project](https://wiki.gentoo.org/wiki/Project:Portage "Project:Portage")

[egencache] is a tool that (re)builds metadata information for the Portage package database. By default the metadata corresponds to the Gentoo ebuild repository. It is built into Portage and therefore comes installed on every Gentoo system.

Metadata for the Portage package database comes included in Gentoo repository snapshots and, in most circumstances, can be re-downloaded by running an [emerge \--sync]. It will *not* be downloaded when using git as the Portage sync method, which is more easily possible using [repos.conf](https://wiki.gentoo.org/wiki//etc/portage/repos.conf "/etc/portage/repos.conf").

## Contents

-   [[1] [Installation]](#Installation)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Invocation]](#Invocation)
    -   [[2.2] [Rebuilding the metadata cache]](#Rebuilding_the_metadata_cache)
-   [[3] [See also]](#See_also)

## [Installation]

Every Gentoo system should have [egencache] installed. Run a quick test by issuing the the `--help` option as seen in the [usage section](#Usage) below.

If usage instructions are not displayed to the terminal there is certainly a problem. It is possible to (re)install Portage by following the Portage [installation instructions](https://wiki.gentoo.org/wiki/Portage#Installation "Portage").

## [Usage]

### [Invocation]

Use the `-h`/`--help` option to see the capabilities of [egencache]:

`user `[`$`]`egencache --help`

    usage: egencache [options] <action> ... [atom] ...

    optional arguments:
      -h, --help            show this help message and exit

    Actions:
      --update              update metadata/md5-cache/ (generate as necessary)
      --update-use-local-desc
                            update the use.local.desc file from metadata.xml
      --update-changelogs   update the ChangeLog files from SCM logs
      --update-pkg-desc-index
                            update package description index
      --update-manifests    update manifests

    Common options:
      --repo REPO           name of repo to operate on
      --config-root PORTAGE_CONFIGROOT
                            location of portage config files
      --gpg-dir GPG_DIR     override the PORTAGE_GPG_DIR variable
      --gpg-key GPG_KEY     override the PORTAGE_GPG_KEY variable
      --portdir PORTDIR     override the PORTDIR variable (deprecated in favor of
                            --repositories-configuration)
      --portdir-overlay PORTDIR_OVERLAY
                            override the PORTDIR_OVERLAY variable (deprecated in
                            favor of --repositories-configuration)
      --repositories-configuration REPOSITORIES_CONFIGURATION
                            override configuration of repositories (in format of
                            repos.conf)
      --sign-manifests <y|n>
                            manually override layout.conf sign-manifests setting
      --strict-manifests <y|n>
                            manually override "strict" FEATURES setting
      --thin-manifests <y|n>
                            manually override layout.conf thin-manifests setting
      --tolerant            exit successfully if only minor errors occurred
      --ignore-default-opts
                            do not use the EGENCACHE_DEFAULT_OPTS environment
                            variable
      --write-timestamp     write metadata/timestamp.chk as required for rsync
                            repositories

    --update options:
      --cache-dir CACHE_DIR
                            location of the metadata cache
      -j JOBS, --jobs JOBS  max ebuild processes to spawn
      --load-average LOAD_AVERAGE
                            max load allowed when spawning multiple jobs
      --rsync               enable rsync stat collision workaround for bug 139134
                            (use with --update)

    --update-use-local-desc options:
      --preserve-comments   preserve the comments from the existing use.local.desc
                            file
      --use-local-desc-output ULD_OUTPUT
                            output file for use.local.desc data (or '-' for
                            stdout)

### [Rebuilding the metadata cache]

In order to rebuild the metadata cache on a system issue the following command:

`root `[`#`]`egencache --jobs=9 --update --repo gentoo`

Adjust the number of jobs to be appropriate to each system. The \"safe\" metric to use with jobs will depend on the processor and system load; if there is no load on the system use the metric of one job per processor thread plus one. In a quad core processor that has two threads per core the equation would result in `9` being set for jobs (2\*4+1). In the example above `9` jobs are used as the example.

** Note**\
Rebuilding the checksum cache can take quite some time. If running the [egencache] command hangs for a while just wait it out.

## [See also]

-   [Elogv](https://wiki.gentoo.org/wiki/Elogv "Elogv") --- a curses-based tool that parses the contents of [elogs](https://wiki.gentoo.org/wiki/Portage_log "Portage log") created by Portage.
-   [Useful Portage tools](https://wiki.gentoo.org/wiki/Useful_Portage_tools "Useful Portage tools") --- provides a list of Gentoo-specific system management tools, notably for [Portage](https://wiki.gentoo.org/wiki/Portage "Portage"), available in the [ebuild repository](https://wiki.gentoo.org/wiki/Ebuild_repository "Ebuild repository").