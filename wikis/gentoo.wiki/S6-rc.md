**Resources**

[[]][Home](https://www.skarnet.org/software/s6-rc/)

[[]][Git repository browser](https://git.skarnet.org/cgi-bin/cgit.cgi/s6-rc)

[[]][GitHub mirror](https://github.com/skarnet/s6-rc)

[[]][Package information](https://packages.gentoo.org/packages/sys-apps/s6-rc)

s6-rc is a service manager for [s6](https://wiki.gentoo.org/wiki/S6 "S6")-based systems, i.e. a suite of programs that can start and stop services, both long-running daemons and one-time initialization scripts, in the proper order according to a dependency tree. It can be used as an init system component, with a role similar to that of [OpenRC](https://wiki.gentoo.org/wiki/OpenRC "OpenRC") for [sysvinit](https://wiki.gentoo.org/wiki/Sysvinit "Sysvinit") + OpenRC systems. A high level overview of s6-rc is available [here](https://www.skarnet.org/software/s6-rc/overview.html). The package\'s documentation is provided in HTML format, and can be read on a text user interface using for example [[[www-client/links]](https://packages.gentoo.org/packages/www-client/links)[]]. However, a man page port of the documentation is available: [[[app-doc/s6-rc-man-pages]](https://packages.gentoo.org/packages/app-doc/s6-rc-man-pages)[]].

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Files]](#Files)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Compiled service databases]](#Compiled_service_databases)
        -   [[3.1.1] [Longrun definitions]](#Longrun_definitions)
        -   [[3.1.2] [Oneshot definitions]](#Oneshot_definitions)
        -   [[3.1.3] [Service bundles]](#Service_bundles)
        -   [[3.1.4] [Extracting information from a compiled database]](#Extracting_information_from_a_compiled_database)
    -   [[3.2] [Initializing s6-rc]](#Initializing_s6-rc)
    -   [[3.3] [Managing services]](#Managing_services)
    -   [[3.4] [Service dependencies]](#Service_dependencies)
    -   [[3.5] [Live updates to the service database]](#Live_updates_to_the_service_database)
    -   [[3.6] [Longrun pipelining]](#Longrun_pipelining)
    -   [[3.7] [s6-rc as an init system component]](#s6-rc_as_an_init_system_component)
-   [[4] [Removal]](#Removal)
    -   [[4.1] [Unmerge]](#Unmerge)
-   [[5] [See also]](#See_also)
-   [[6] [References]](#References)

## [Installation]

### [USE flags]

### [USE flags for] [sys-apps/s6-rc](https://packages.gentoo.org/packages/sys-apps/s6-rc) [[]] [Service manager for the s6 supervision suite]

  ------------------------------------------------------------------- -----------------------------------------------------
  [`system-init`](https://packages.gentoo.org/useflags/system-init)   Installed as a provider of virtual/service-manager.
  ------------------------------------------------------------------- -----------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-04-13 11:26] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask sys-apps/s6-rc`

** Important**\
s6-rc is currently on the testing branch. Users with systems on the stable branch will need to add the package to [/etc/portage/package.accept_keywords] (if using Portage) to be able to install it, and also add [[[dev-libs/skalibs]](https://packages.gentoo.org/packages/dev-libs/skalibs)[]], [[[dev-lang/execline]](https://packages.gentoo.org/packages/dev-lang/execline)[]] and [[[sys-apps/s6]](https://packages.gentoo.org/packages/sys-apps/s6)[]]. While it is generally not advised to mix packages of stable and testing branches, the skarnet.org software stack only depends on the [libc](https://wiki.gentoo.org/wiki/Libc "Libc"), so in this case it should be safe.

## [Configuration]

### [Files]

-   [/run/s6-rc] - Default live state directory.
-   [/etc/s6-rc/compiled] - Default pathname of the compiled service database used by [s6-rc-init] to initialize s6-rc.

## [Usage]

s6-rc manages *services*. A service is usually thought of as being provided by a *server program* that runs as a long-lived process. In this case, the service is *up* while the program is running and ready to provide the service, and *down* otherwise. s6-rc calls this kind of service a *longrun*, and arranges to run the corresponding program as a *supervised process* using [s6](https://wiki.gentoo.org/wiki/S6 "S6") tools.

A service can also be thought of as being provided after some sequence of actions is performed, without involving a long-lived process. For example, making a filesystem available by mounting it, or making a network interface ready for traffic by bringing it up and configuring it with a static address, could also be considered services. In this case the service is up after the corresponding actions are successfully performed. s6-rc calls this kind of service a *oneshot*, and arranges to perform the corresponding actions in a controlled, reproducible environment. This environment is also set up by an s6 supervision tree even though oneshots do not involve supervised processes. For a oneshot, a transition to down state might mean just doing nothing and \'forgetting\' that the corresponding actions were performed, so a subsequent transition to up would simply redo them. Or it might mean performing some sort of inverse procedure, like e.g. unmounting a filesystem or bringing down a network interface.

Services can also *depend* on other services. This generally means that a service can only transition to and remain in up state only as long as all of the services it depends on are also in up state. The dependencies of a service might in turn have dependencies themselves, creating dependency chains. s6-rc supports dependency specifications and arranges to perform service state transitions accordingly. []

### [Compiled service databases]

Performing requested state transitions for a set of services submitted to s6-rc (called *the selection*) requires it to compute a *dependency graph*, and then use it to compute, from the full set of managed services, the complete subset of those that need state transitions (called *the closed selection*), so that the requested operation can be performed while also honoring all dependency specifications. For this purpose, s6-rc stores its managed longruns and oneshots in a *compiled service database*. This database is a directory that contains a set of files and subdirectories with formats optimized for efficient computation of dependency graphs and closed selections. A compiled database is created with the [s6-rc-compile] program. It cannot be modified except by using the [s6-rc-bundle] program (see [live updates to the service database](#s6rcupdate)), and can be placed in a read-only filesystem.

[s6-rc-compile] accepts the (absoulte or relative to its working directory) pathname of the database to create, and a nonempty set of directory pathnames. These directories must contain *service definitions* in a format called [s6-rc-compile]\'s *source format*. A service definition is a subdirectory, or symbolic link to directory, that must contain a regular file named [type]. This file specifies one of the s6-rc\'s supported service types: longrun, oneshot and *bundle* (see [service bundles](#bundles)). The contents of a service definition directory depend on the service\'s type. The name of the directory defines the *service name* that is used by all s6-rc programs to refer to the service. Service names cannot be duplicated and cannot contain a slash (\'/\') or a newline; they can contain spaces and tabs, but using anything other than alphanumerical characters, underscores (\'\_\') and dashes (\'-\') is discouraged.

Currently, [s6-rc-compile] also unconditionally adds two s6-rc support services to each compiled service database: [s6rc-oneshot-runner], a longrun that is used to implement oneshots (see [oneshot definitions](#oneshots)), and [s6rc-fdholder], a longrun that is used to implement pipelines (see [longrun pipelining](#pipelines)). Service names that start with **s6rc-** or **s6-rc-** are reserved, and [s6-rc-compile] fails with an error if it finds one in the submitted service definitions. [s6-rc-compile] also ignores, in any of the supplied directories, files that are not directories or symbolic links to directory, and files with names that start with a dot (\'.\'). For the full description of [s6-rc-compile], please consult the HTML documentation in the package\'s [/usr/share/doc] subdirectory.

The [examples/source] directory in the package\'s [/usr/share/doc] subdirectory contains an example set of service definitions in [s6-rc-compile]\'s source format for a few programs, taken from a working Linux system running Busybox and skarnet.org packages (without private information and without the supporting files elsewhere, like e.g. configuration files in [/etc]).

#### [Longrun definitions]

A longrun definition in [s6-rc-compile]\'s source format is a variation of an [s6 service directory](https://wiki.gentoo.org/wiki/S6#Usage "S6"). It must contain a file named [run], and can contain files named [finish], [notification-fd], [nosetsid], [timeout-finish], and [timeout-kill], with the same meaning and required content as for s6. As of version 0.5.0.0, a longrun definition can also contain [max-death-tally] and [down-signal] files, which s6 added support for in versions 2.7.1.0 and 2.7.2.0, respectively. On the other hand, [down] files are ignored because longruns are managed using s6-rc tools that take care of these files themselves. And [log] subdirectories or symbolic links are ignored too, because their functionality is replaced by pipelines (see [longrun pipelining](#pipelines)).

** Important**\
Support for [max-death-tally] and [down-signal] files in longrun definitions was actually introduced in s6-rc version 0.4.1.0, but a bug prevented it from working. The bug was fixed in version 0.5.0.0

The [type] file of a longrun definition must contain the word **longrun** followed by a newline. A longrun definition can also contain optional, regular files named [dependencies] (see [service dependencies](#dependencies)), [timeout-up] and [timeout-down] (see [managing services](#manage)). If the service is a member of a pipeline, the longrun definition must also contain a regular file named [producer-for] or [consumer-for], and can contain an optional, regular file named [pipeline-name]. And finally, a longrun definition can also contain subdirectories named [data] and [env], for use by the [run] and [finish] files. Their content is ignored by [s6-rc-compile]. [env] is customarily an environment directory used by an [s6-envdir] invocation in [run] or [finish], and [data] is customarily used for other support files. For example, to hold [rules directories or rules files](https://wiki.gentoo.org/wiki/S6/UNIX_domain_super-server#rulesdir "S6/UNIX domain super-server") for tools like [s6-fdholderd] and [s6-ipcserver-access], or to hold [a [check] file](https://wiki.gentoo.org/wiki/S6#s6notifyoncheck "S6") for [s6-notifyoncheck].

Longrun definitions are \'compiled\' by [s6-rc-compile] to actual s6 service directories. The program automatically sets appropriate permissions for files with meaning defined by s6 (e.g. **0755** for [run] and [finish], **0644** for [notification-fd], etc.), so s6-rc service definitions do not need to have them set correctly. It only matters that [s6-rc-compile]\'s effective user is allowed to read them. The compiled s6 service directories are copied to the live state directory and linked from the scan directory of a running [s6-svscan] process by the [s6-rc-init] program (see [initializing s6-rc](#initialization)). The [data] and [env] subdirectories are copied verbatim to the s6 service directory, and [down] files are created or removed in it as needed by s6-rc programs. For the full description of the longrun definition source format, please consult [s6-rc-compile]\'s HTML documentation in the package\'s [/usr/share/doc] subdirectory.

Example definition in source format for a longrun named *test-longrun*:

`user `[`$`]`ls -l test-longrun`

    total 16
    -rw-r--r-- 1 user user 130 Mar 20 12:00 finish
    -rw-r--r-- 1 user user   2 Mar 20 12:00 notification-fd
    -rw-r--r-- 1 user user  94 Mar 20 12:00 run
    -rw-r--r-- 1 user user   8 Mar 20 12:00 type

[FILE] **`test-longrun/type`**

    longrun

[FILE] **`test-longrun/run`**

    #!/bin/execlineb -P
    foreground
    fdmove -c 2 1
    test-daemon --s6=3

[FILE] **`test-longrun/notification-fd`**

    3

[FILE] **`test-longrun/finish`**

    #!/bin/execlineb -S0
    ifelse
       echo test-daemon exited with code $1

This service\'s transition to up state spawns a long-lived process that executes a hypothetical [test-daemon] program. It is assumed that it supports the [s6 readiness notification protocol](https://wiki.gentoo.org/wiki/S6#s6readiness "S6") when passed an `--s6` option. The notification channel\'s file descriptor is **3**, so there is a [notification-fd] file specifying that. The [type] file indicates that this service is a longrun, and the rest of the files are standard s6 service directory files. Messages are printed to [run]\'s and [finish]\'s standard output, so that service events can be tracked. []

#### [Oneshot definitions]

A oneshot definition in [s6-rc-compile]\'s source format is a directory that must contain a regular file named [up], and can optionally contain a regular file named [down]. This files encode the actions that must be performed to transition the service to up and down state, respectively. When s6-rc is asked to start or stop the service, it behaves **as if** it executed an [s6-sudo -e supervision-socket up] or [s6-sudo -e supervision-socket down] command, respectively, where *supervision-socket* would be the UNIX domain socket of an [[s6-sudod](https://wiki.gentoo.org/wiki/S6#s6sudo "S6")] process that runs with the same environment that is set up for longruns, and has been invoked as [s6-sudod execlineb -P]. [execlineb] is the script parser and launcher from the execline package ([[[dev-lang/execline]](https://packages.gentoo.org/packages/dev-lang/execline)[]]). This means that the [up] and [down] files can have [execline syntax](https://www.skarnet.org/software/execline/execlineb.html) (quoted strings, -blocks, backslash sequences, #-coments, etc.), and that it is possible to have them contain full execline scripts. However, because a program name that can be found by `PATH` search, or a program\'s absolute pathname, followed by program arguments, is a valid execline script, it is possible to use shell scripts for the oneshot\'s actions by simply invoking them in the [up] and [down] files.

An absent [down] file is equivalent to an empty [down] file. Because invoking [execlineb] with an empty file does nothing but making it exit with a 0 code, stopping the corresponding service performs no actions other than updating s6-rc\'s notion of the service state. The [type] file of a oneshot definition must contain the word **oneshot** followed by a newline. A oneshot definition can also contain regular files named [dependencies] (see [service dependencies](#dependencies)), [timeout-up] and [timeout-down] (see [managing services](#manage)). For the full description of the oneshot definition source format, please consult [s6-rc-compile]\'s HTML documentation in the package\'s [/usr/share/doc] subdirectory.

Oneshot definitions are \'compiled\' by [s6-rc-compile] to an array of strings, suitable as the \'argv\' argument of a POSIX `execve()` call. [s6-rc-compile] actually performs execlineb-style parsing itself using the execline package\'s library, [libexecline]. At the time of a service state transition, what s6-rc actually does is perform an [s6-sudo] invocation with the `-e` option and the UNIX domain socket of an internal support service named **s6rc-oneshot-runner**. [s6rc-oneshot-runner] spawns a long-lived [s6-sudod] process; when a connection is made by an [s6-sudoc] client to this process\' socket, an s6-rc internal program, [s6-rc-oneshot-run], is executed with the arguments supplied by the client. [s6-rc-oneshot-run] accepts an action name (\'up\' or \'down\') and the numerical encoding of a oneshot, that it uses to retrieve the corresponding compiled array of strings from the service database, and makes the `execve()` call that actually performs the oneshot\'s actions. This ensures that the [s6-sudoc] - [s6-sudod] mechanism is only used to run [s6-rc-oneshot-run], so that only actions explicitly encoded in the database are executed. Because the [s6rc-oneshot-runner] service is an s6-rc longrun, the corresponding [s6-sudod] process is supervised. Therefore, it runs with the environment set up by the s6 supervision tree used for longruns, which is inherited by its [s6-rc-oneshot-run] child process. This ensures that oneshot\'s actions are always performed in this known environment, and using [s6-sudo]\'s `-e` option ensures that it is not accidentally modified by the [s6-sudoc] client\'s environment. [s6-rc-compile] automatically makes [s6rc-oneshot-runner] a direct dependency of every oneshot. For further information about [s6-rc-oneshot-run], please consult the HTML documentation in the package\'s [/usr/share/doc] subdirectory.

Example definition in source format for a oneshot named *test-oneshot*:

`user `[`$`]`ls -l test-oneshot`

    total 12
    -rw-r--r-- 1 user user 118 Mar 20 12:00 down
    -rw-r--r-- 1 user user   8 Mar 20 12:00 type
    -rw-r--r-- 1 user user 119 Mar 20 12:00 up

[FILE] **`test-oneshot/type`**

    oneshot

[FILE] **`test-oneshot/up`**

    foreground
    /home/user/s6-rc-scripts/real-script.sh start

[FILE] **`test-oneshot/down`**

    foreground
    /home/user/s6-rc-scripts/real-script.sh stop

This service\'s transition to up state executes a hypothetical [real-script.sh] shell script, located in [/home/user/s6-rc-scripts], with a **start** argument. Its transition to down state executes the same script, but with a **stop** argument instead. This shows how to use shell scripts, or any external executable file, with s6-rc. Messages are printed before the script\'s invocation so that service events can be tracked. The [type] file indicates that this service is a oneshot. The oneshot\'s actions are actually encoded in [real-script.sh]:

[FILE] **`/home/user/s6-rc-scripts/real-script.sh`**

    #!/bin/sh
    echo real-script.sh invoked with arguments $@
    case "$1" in
       start) echo Performing start actions ;;
       stop) echo Performing stop actions ;;
       *) echo Unrecognized argument ;;
    esac

#### [Service bundles]

A service bundle is just a named group of services, created for administrative purposes. Because a bundle is also created with a service definition directory supplied to [s6-rc-compile], and bundle names can be used in most places that expect a service name, the term *service* is loosely used to also refer to bundles, and the term *atomic service* is used to refer to either longruns or oneshots, but not bundles, when the distinction matters. In particular, bundles can be used to implement runlevel-like functionality if so desired, combined with the [s6-rc -pu change] command (see [service dependencies](#dependencies)). For examples of this, see [live updates to the service database](#s6rcupdate).

A service bundle definition in [s6-rc-compile]\'s source format must contain a regular file named [contents]. The [type] file must contain the word **bundle** followed by a newline. The [contents] file must contain a list of service names, one per line; the bundle will cointain all the corresponding services. Whitespace at the beginning of a line is ignored, but trailing whitespace is not. Lines that start with a hash sign (\'#\') are treated as comments and ignored. Names that refer to other bundles can be used in [contents]; [s6-rc-compile] interprets them as referring to the set of atomic services contained in the named bundle. For the full description of the bundle definition source format, please consult [s6-rc-compile]\'s HTML documentation in the package\'s [/usr/share/doc] subdirectory.

Example definition in source format for a service bundle named *test-bundle*:

`user `[`$`]`ls -l test-bundle`

    total 8
    -rw-r--r-- 1 user user 26 Mar 20 12:00 contents
    -rw-r--r-- 1 user user  7 Mar 20 12:00 type

[FILE] **`test-bundle/type`**

    bundle

[FILE] **`test-bundle/contents`**

    test-longrun
    test-oneshot

This bundle is comprised by atomic services *test-longrun* and *test-oneshot*. The [type] file indicates that this service is not an atomic service, but a bundle. []

#### [Extracting information from a compiled database]

Because the format of an s6-rc compiled service database is not human-readable, the package provides the [s6-rc-db] program for analyzing a compiled database, extracting information from it, and printing it in a user-friendly format. By default, the database read by [s6-rc-db] is the one currently associated with live state directory [/run/s6-rc] (see [initializing s6-rc](#initialization)), unless it is passed an `-l` option followed by the (absolute or relative to the working directory) pathname of a different live state directory, or it is passed a `-c` option followed by the pathname of the database.

[s6-rc-db] accepts a *subcommand* that tells it what to print. Some of these subcommands are:

-   **help**: prints a help message.
-   **list**: lists service names that satisfy some condition specified by the subcommand\'s argument:
    -   **all** (i.e. [s6-rc-db list all]): lists the names of all atomic services and service bundles contained in the database.
    -   **services**: lists the names of all atomic services contained in the database, i.e. the list does no include service bundle names.
    -   **bundles**: lists the names of all service bundles contained in the database.
    -   **longruns**: lists the names of all longruns contained in the database. This includes the s6-rc supporting services automatically added by [s6-rc-compile].
    -   **oneshots**: lists the names of all oneshots contained in the database.
-   **type**: displays the type of the service (\'oneshot\', \'longrun\' or \'bundle\') corresponding to the name supplied as the subcommand\'s argument.
-   **contents**: displays the list of atomic services contained in the service bundle corresponding to the name supplied as the subcommand\'s argument.
-   **atomics**: displays the fully resolved list of atomic services represented by a list of service names supplied as the subcommand\'s arguments. Atomic service names in the list will be displayed in the output as-is, and service bundle names will be replaced in the output by the names of its contained atomic services. Each service name will be listed only once, with no repetitions. This computation of an atomic service list is also performed by the [s6-rc] program, see [managing services](#manage).
-   **script**: displays the actions executed during state transitions of the oneshot corresponding to the name supplied as the subcommand\'s argument. If a `-u` option is passed to [s6-rc-db] (*before* the subcommand name), the output is the string sequence produced by [s6-rc-compile]\'s parsing of the [up] file from the oneshot\'s definition in [s6-rc-compile]\'s source format. If a `-d` option is passed to [s6-rc-db], the output is the string sequence produced by [s6-rc-compile]\'s parsing of the [down] file from the oneshot\'s definition. If there is neither a `-u` option nor a `-d` option, [s6-rc-db] behaves as if the `-u` option had been specified. Each string in the sequence is terminated by a null character, so it is usually necessary to pipe [s6-rc-db]\'s output to something like [xargs -0].

Other [s6-rc-db] subcommands can be used to display dependency information (see [service dependencies](#dependencies)), state transition timeouts (see [managing services](#manage)) and pipeline information (see [longrun pipelining](#pipelines)). For the full description of [s6-rc-db], please consult the HTML documentation in the package\'s [/usr/share/doc] subdirectory.

Example directories *srv-src1* and *srv-src2* containing service definition subdirectories in [s6-rc-compile]\'s source format:

`user `[`$`]`ls -l srv-src*`

    srv-src1:
    total 12
    drwxr-xr-x 2 user user 4096 Mar 20 12:00 test-bundle
    drwxr-xr-x 2 user user 4096 Mar 20 12:00 test-longrun
    drwxr-xr-x 2 user user 4096 Mar 20 12:00 test-oneshot

    srv-src2:
    total 12
    drwxr-xr-x 2 user user 4096 Mar 20 12:00 all-services
    drwxr-xr-x 2 user user 4096 Mar 20 12:00 another-longrun
    drwxr-xr-x 2 user user 4096 Mar 20 12:00 another-oneshot

Directory [srv-src1] contains definitions for the example services described in previous sections. Directory [srv-src2] contains another set of service definitions. *all-services* is a bundle:

[FILE] **`srv-src2/all-services/type`**

    bundle

[FILE] **`srv-src2/all-services/contents`**

    test-bundle
    another-longrun
    another-oneshot

Note that the [contents] file contains names of both atomic services (*another-longrun* and *another-oneshot*) and bundles (*test-bundle*).

An s6-rc compiled service database *test-database1* can be created from [srv-src1] and [srv-src2] by invoking [s6-rc-compile] with their pathnames as arguments:

`user `[`$`]`s6-rc-compile -v 3 -u $(id -u) test-database1 srv-src1 srv-src2`

    s6-rc-compile: info: parsing srv-src1/test-bundle
    s6-rc-compile: info: test-bundle has type bundle
    s6-rc-compile: info: parsing srv-src1/test-longrun
    s6-rc-compile: info: test-longrun has type longrun
    s6-rc-compile: info: parsing srv-src1/test-oneshot
    s6-rc-compile: info: test-oneshot has type oneshot
    s6-rc-compile: info: parsing srv-src2/all-services
    s6-rc-compile: info: all-services has type bundle
    s6-rc-compile: info: parsing srv-src2/another-longrun
    s6-rc-compile: info: another-longrun has type longrun
    s6-rc-compile: info: parsing srv-src2/another-oneshot
    s6-rc-compile: info: another-oneshot has type oneshot
    s6-rc-compile: info: making bundles for pipelines
    s6-rc-compile: info: resolving bundle names
    s6-rc-compile: info: converting bundle array
    s6-rc-compile: info: resolving service names
    s6-rc-compile: info: converting service dependency array
    s6-rc-compile: info: checking database correctness
    s6-rc-compile: info: writing compiled information to test-database1
    s6-rc-compile: info: writing test-database1/n
    s6-rc-compile: info: writing test-database1/resolve.cdb
    s6-rc-compile: info: writing test-database1/db
    s6-rc-compile: info: writing test-database1/servicedirs

The `-u` option is needed so that the [s6-rc] program can be used to manage oneshots by the nonprivileged user that created the database. The `-v 3` option makes the output of [s6-rc-compile] more verbose. The resulting database is a directory:

`user `[`$`]`ls -l test-database1`

    total 16
    -rw-r--r-- 1 user user  646 Mar 20 12:05 db
    -rw-r--r-- 1 user user    0 Mar 20 12:05 lock
    -rw-r--r-- 1 user user   24 Mar 20 12:05 n
    -rw-r--r-- 1 user user 2397 Mar 20 12:05 resolve.cdb
    drwxr-xr-x 6 user user 4096 Mar 20 12:05 servicedirs

The [servicedirs] subdirectory contains the s6 service directories generated for all longruns, including those of automatically included s6-rc supporting services:

`user `[`$`]`ls -l test-database1/servicedirs`

    total 16
    drwxr-xr-x 2 user user 4096 Mar 20 12:05 another-longrun
    drwxr-xr-x 3 user user 4096 Mar 20 12:05 s6rc-fdholder
    drwxr-xr-x 3 user user 4096 Mar 20 12:05 s6rc-oneshot-runner
    drwxr-xr-x 2 user user 4096 Mar 20 12:05 test-longrun

`user `[`$`]`ls -l test-database1/servicedirs/test-longrun`

    total 12
    -rwxr-xr-x 1 user user 130 Mar 20 12:05 finish
    -rw-r--r-- 1 user user   2 Mar 20 12:05 notification-fd
    -rwxr-xr-x 1 user user  94 Mar 20 12:05 run

This shows that the [run] and [finish] files are executable, as expected by [s6-supervise], even if the corresponding ones in the s6-rc service definition were not. Listing all service names in the resulting compiled database:

`user `[`$`]`s6-rc-db -c test-database1 list all | sort`

    all-services
    another-longrun
    another-oneshot
    s6rc-fdholder
    s6rc-oneshot-runner
    test-bundle
    test-longrun
    test-oneshot

This shows that the created database contains the union of the services defined in subdirectories of [srv-src1], and the services defined in subdirectories of [srv-src2]. Listing service names by type:

`user `[`$`]`s6-rc-db -c test-database1 list longruns | sort`

    another-longrun
    s6rc-fdholder
    s6rc-oneshot-runner
    test-longrun

`user `[`$`]`s6-rc-db -c test-database1 list oneshots | sort`

    another-oneshot
    test-oneshot

`user `[`$`]`s6-rc-db -c test-database1 list bundles | sort`

    all-services
    test-bundle

Displaying the type of different services:

`user `[`$`]`s6-rc-db -c test-database1 type all-services`

    bundle

`user `[`$`]`s6-rc-db -c test-database1 type test-longrun`

    longrun

`user `[`$`]`s6-rc-db -c test-database1 type another-oneshot`

    oneshot

Displaying the contents of service bundles:

`user `[`$`]`s6-rc-db -c test-database1 contents test-bundle | sort`

    test-longrun
    test-oneshot

`user `[`$`]`s6-rc-db -c test-database1 contents all-services | sort`

    another-longrun
    another-oneshot
    test-longrun
    test-oneshot

This shows that, because the [contents] file in the definition of bundle [all-services] named the bundle [test-bundle], all atomic services contained in the latter became members of the former. Displaying the string sequence compiled from the [up] and [down] files of a oneshot:

`user `[`$`]`s6-rc-db -uc test-database1 script test-oneshot | xargs -0 printf '"%s"\n'`

    "foreground"
    " echo"
    " Calling /home/user/s6-rc-scripts/real-script.sh..."
    ""
    "/home/user/s6-rc-scripts/real-script.sh"
    "start"

`user `[`$`]`s6-rc-db -dc test-database1 script test-oneshot | xargs -0 printf '"%s"\n'`

    "foreground"
    " echo"
    " Calling /home/user/s6-rc-scripts/real-script.sh..."
    ""
    "/home/user/s6-rc-scripts/real-script.sh"
    "stop"

Notice the result of execlineb-style processing: the quoted strings that were arguments of the [echo] utility become single elements in the compiled sequence of strings even if they contain whitespace, and -blocks become a sequence of arguments that start with a space, terminated by an empty string, [a format recognized by all execline programs](https://www.skarnet.org/software/execline/el_semicolon.html), including [foreground].

Resolving some atomic service sets:

`user `[`$`]`s6-rc-db -c test-database1 atomics another-oneshot test-bundle | sort`

    another-oneshot
    test-longrun
    test-oneshot

This shows that because [another-oneshot] is an atomic service, it is included as-is in the output, and because [test-bundle] is a bundle, it is replaced in the output by the set of atomic services it contains.

`user `[`$`]`s6-rc-db -c test-database1 atomics another-longrun all-services | sort`

    another-longrun
    another-oneshot
    test-longrun
    test-oneshot

This shows that bundle *all-services* is replaced by the set of atomic services it contains, and because that set includes [another-longrun], this service is listed only once. []

### [Initializing s6-rc]

s6-rc must be initialized with a [compiled service database](#database) and an [s6 supervision tree](https://wiki.gentoo.org/wiki/S6#Usage "S6"), that is used to supervise longruns and to provide the environment used for performing oneshots\' actions. The program that performs this initialization is [s6-rc-init].

[s6-rc-init] accepts the absolute pathname of a scan directory, that must have a corresponding [s6-svscan] process already running. The service database is assumed to be [/etc/s6-rc/compiled]. A different (absolute) pathname can be specified with a `-c` option. [s6-rc-init] creates a *live state directory* that associates the s6-rc service database with the s6 supervision tree, and keeps track of service states. The live state directory must be in a read-write filesystem, and defines an s6-rc \'instance\'. The live state directory is [/run/s6-rc] by default; a different (absolute) pathname can be specified with an `-l` option. [/run/s6-rc] is actually a symbolic link to a directory created by [s6-rc-init] in [/run]; this is necessary for the operation of the [s6-rc-update] program (see [live updates to the service database](#s6rcupdate)). Similarly, if the `-l` option is used, [s6-rc-init] it will create both a symbolic link with that pathname, and a subdirectory in the directory containing the symlink.

A compiled database that becomes associated with a live state directory by using [s6-rc-init], [s6-rc-update] or [s6-rc-format-upgrade] is said to *be live*. A database that is not live can be freely moved around in the filesystem, but once it becomes live, it must not move anymore and must not be deleted. A database stops being live if it is deassociated from the live state directory by [s6-rc-update] or [s6-rc-format-upgrade], or if the corresponding s6 supervision torn down (e.g. by [s6-svscanctl -t]).

The s6-rc live state directory also contains a copy of the compiled s6 service directories of all longruns in the service database. [s6-rc-init] creates a symbolic link to each of them in the specified scan directory, so that the corresponding program can be run as a supervised process, and performs the equivalent an [s6-svscanctl -a] command to make [s6-svscan] perform a scan. The initial state of all atomic services after the invocation of [s6-rc-init] is **down**. In the case of longruns, [s6-rc-init] enforces this by creating [down] files in each of their service directories, so that their [s6-supervise] processes do not execute the [run] file. [s6-rc-init] also accepts a `-p` option followed by a prefix, that prepends the specified prefix to the name of every longrun when creating the symlinks in the scan directory. For example, if a longrun\'s name is *name*, [s6-rc-init -p instance-1:] will name the symlink *instance-1:name*. This allows the sharing of a single s6 supervision tree among different \'instances\' of s6-rc, i.e. among s6-rc-managed services associated with different live state directories.

Support services [s6rc-oneshot-runner] and [s6rc-fdholfer] use UNIX domain sockets, and s6 access control tools to decide whether to grant or refuse service to clients that connect to these sockets. By default, they only grant access to *root*, but this can be modified by passing `-u` and `-g` options to [s6-rc-compile], followed by a comma-separated list of numerical user IDs and group IDs, respectively. These options are used to construct [rules directories](https://wiki.gentoo.org/wiki/S6/UNIX_domain_super-server#rulesdir "S6/UNIX domain super-server"): user IDs specified with `-u` are used for the [uid] subdirectory, and group IDs specified with `-g` are used for the [gid] subdirectory. If any of these options are used, root\'s UID or the GID of a group it is a member of must be explicitly specified to grant it access. For further information about [s6-rc-compile], please consult the HTML documentation in the package\'s [/usr/share/doc] subdirectory.

Example s6 scan directory containing a supervised logger with a FIFO, that logs supervision tree messages in a similar way to that of [the catch-all logger of an s6 and s6-rc-based init system](https://wiki.gentoo.org/wiki/S6_and_s6-rc-based_init_system#logger "S6 and s6-rc-based init system"):

`user `[`$`]`ls -ld * .s6-svscan`

    drwxr-xr-x 2 user user 4096 Mar 30 12:00 logger
    drwxr-xr-x 2 user user 4096 Mar 30 12:00 .s6-svscan

`user `[`$`]`ls -l logger`

    total 4
    prw------- 1 user user   0 Mar 30 12:00 fifo
    -rwxr-xr-x 1 user user 144 Mar 30 12:00 run

[FILE] **`logger/run`**

    #!/bin/execlineb -P
    redirfd -w 1 /dev/null
    redirfd -rnb 0 fifo
    foreground
    s6-log t ../../logdir

Starting the supervision tree, assuming that the working directory is the scan directory:

`user `[`$`]`redirfd -wnb 1 logger/fifo s6-svscan &`

    [1] 2460
    Starting logger...

`user `[`$`]`ps xf -o pid,ppid,pgrp,euser,args`

     PID  PPID  PGRP EUSER    COMMAND
    ...
    2130  2123  2130 user     -bash
    2460  2130  2460 user      \_ s6-svscan
    2461  2460  2460 user          \_ s6-supervise logger
    2462  2461  2462 user              \_ s6-log t ../../logdir
    ...

Initializing s6-rc with this supervision tree and the example database *test-database1* from section [\"extracting information from a compiled database\"](#s6rcdb), assuming that it is located in [/home/user]:

`user `[`$`]`s6-rc-init -c /home/user/test-database1 -l /home/user/live "$(pwd)"`

`user `[`$`]`ls -l`

    total 12
    lrwxrwxrwx 1 user user   43 Mar 30 12:10 another-longrun -> /home/user/live/servicedirs/another-longrun
    drwxr-xr-x 4 user user 4096 Mar 30 12:05 logger
    lrwxrwxrwx 1 user user   41 Mar 30 12:10 s6rc-fdholder -> /home/user/live/servicedirs/s6rc-fdholder
    lrwxrwxrwx 1 user user   47 Mar 30 12:10 s6rc-oneshot-runner -> /home/user/live/servicedirs/s6rc-oneshot-runner
    lrwxrwxrwx 1 user user   40 Mar 30 12:10 test-longrun -> /home/user/live/servicedirs/test-longrun

This creates the live state directory in [/home/user], and, as shown, symbolic links in the scan directory.

`user `[`$`]`ls -l ../live`

    lrwxrwxrwx 1 user user 22 Mar 30 12:10 ../live -> live:s6-rc-init:peEEK3

This shows that [/home/user/live] is actually a symbolic link to subdirectory [live:s6-rc-init:peEEK3] of [/home/user]:

`user `[`$`]`ls -l ../live:s6-rc-init:peEEK3`

    total 8
    lrwxrwxrwx 1 user user   25 Mar 30 12:10 compiled -> /home/user/test-database1
    -rw-r--r-- 1 user user    0 Mar 30 12:10 prefix
    lrwxrwxrwx 1 user user   15 Mar 30 12:10 scandir -> /home/user/scan
    drwxr-xr-x 6 user user 4096 Mar 30 12:10 servicedirs
    -rw-r--r-- 1 user user    6 Mar 30 12:10 state

Updated supervision tree:

`user `[`$`]`ps xf -o pid,ppid,pgrp,euser,args`

     PID  PPID  PGRP EUSER    COMMAND
    ...
    2130  2123  2130 user     -bash
    2460  2130  2460 user      \_ s6-svscan
    2461  2460  2460 user          \_ s6-supervise logger
    2462  2461  2462 user          |   \_ s6-log t ../../logdir
    2471  2460  2460 user          \_ s6-supervise test-longrun
    2472  2460  2460 user          \_ s6-supervise s6rc-oneshot-runner
    2473  2460  2460 user          \_ s6-supervise s6rc-fdholder
    2474  2460  2460 user          \_ s6-supervise another-longrun
    ...

This shows that none of the longruns is in up state: only their supervisor is running. Service directory of *test-longrun*:

`user `[`$`]`ls -l ../live/servicedirs/test-longrun`

    total 20
    -rw-r--r-- 1 user user    0 Mar 30 12:10 down
    drwx-ws--T 2 user user 4096 Mar 30 12:10 event
    -rwxr-xr-x 1 user user  130 Mar 30 12:10 finish
    -rw-r--r-- 1 user user    2 Mar 30 12:10 notification-fd
    -rwxr-xr-x 1 user user   94 Mar 30 12:10 run
    drwx------ 2 user user 4096 Mar 30 12:10 supervise

This shows that [s6-rc-init] created a [down] file. Subdirectories [event] and [supervise] are created by the corresponding [s6-supervise] process (process 2471 in this example). From s6\'s point of view, the service is down:

`user `[`$`]`s6-svstat test-longrun`

    down (exitcode 0) 337 seconds, ready 337 seconds

Another example using prefixes:

`user `[`$`]`mv srv-src2/all-services srv-src2/.all-services`

`user `[`$`]`s6-rc-compile -u $(id -u) db-instance-1 srv-src1`

`user `[`$`]`s6-rc-compile -u $(id -u) db-instance-2 srv-src2`

Service definitions in directories [srv-src1] and [srv-src2] are now compiled to separate databases, *db-instance-1* and *db-instance-2*. The definition directory of bundle [all-services] was renamed to start with a dot so that [s6-rc-compile] ingores it. After changing to scan directory [/home/user/scan] and starting a supervision tree again with command [redirfd -wnb 1 logger/fifo s6-svscan &]:

`user `[`$`]`s6-rc-init -c /home/user/db-instance-1 -p instance-1: -l /home/user/live1 /home/user/scan`

`user `[`$`]`s6-rc-init -c /home/user/db-instance-2 -p instance-2: -l /home/user/live2 /home/user/scan`

`user `[`$`]`ls -l *`

    total 24
    lrwxrwxrwx 1 user user   42 Apr 29 12:10 instance-1:s6rc-fdholder -> /home/user/live1/servicedirs/s6rc-fdholder
    lrwxrwxrwx 1 user user   48 Apr 29 12:10 instance-1:s6rc-oneshot-runner -> /home/user/live1/servicedirs/s6rc-oneshot-runner
    lrwxrwxrwx 1 user user   41 Apr 29 12:10 instance-1:test-longrun -> /home/user/live1/servicedirs/test-longrun
    lrwxrwxrwx 1 user user   44 Apr 29 12:11 instance-2:another-longrun -> /home/user/live2/servicedirs/another-longrun
    lrwxrwxrwx 1 user user   42 Apr 29 12:11 instance-2:s6rc-fdholder -> /home/user/live2/servicedirs/s6rc-fdholder
    lrwxrwxrwx 1 user user   48 Apr 29 12:11 instance-2:s6rc-oneshot-runner -> /home/user/live2/servicedirs/s6rc-oneshot-runner
    drwxr-xr-x 4 user user 4096 Apr 29 12:05 logger

This shows that the symbolic links to the s6 service directories have different prefixes depending on which live state directory the corresponding logrun is associated with. Live state directory [/home/user/live1] is associated with compiled service database [db-instance-1], and live state directory [/home/user/live2] is associated with compiled service database [db-instance-2]. Each of these can be thought as a different s6-rc \'instance\', even if they share the same s6 supervision tree and scan directory. The corresponding services are independent:

`user `[`$`]`ls -l ../live*`

    lrwxrwxrwx 1 user user   23 Apr 29 12:10 ../live1 -> live1:s6-rc-init:ISOd2e
    lrwxrwxrwx 1 user user   23 Apr 29 12:11 ../live2 -> live2:s6-rc-init:AtGbln

    '../live1:s6-rc-init:ISOd2e':
    total 12
    lrwxrwxrwx 1 user user   24 Apr 29 12:10 compiled -> /home/user/db-instance-1
    -rw-r--r-- 1 user user   11 Apr 29 12:10 prefix
    lrwxrwxrwx 1 user user   15 Apr 29 12:10 scandir -> /home/user/scan
    drwxr-xr-x 5 user user 4096 Apr 29 12:10 servicedirs
    -rw-r--r-- 1 user user    4 Apr 29 12:10 state

    '../live2:s6-rc-init:AtGbln':
    total 12
    lrwxrwxrwx 1 user user   24 Apr 29 12:11 compiled -> /home/user/db-instance-2
    -rw-r--r-- 1 user user   11 Apr 29 12:11 prefix
    lrwxrwxrwx 1 user user   15 Apr 29 12:11 scandir -> /home/user/scan
    drwxr-xr-x 5 user user 4096 Apr 29 12:11 servicedirs
    -rw-r--r-- 1 user user    4 Apr 29 12:11 state

`user `[`$`]`s6-rc-db -l ../live1 list all | sort`

    s6rc-fdholder
    s6rc-oneshot-runner
    test-bundle
    test-longrun
    test-oneshot

`user `[`$`]`s6-rc-db -l ../live2 list all | sort`

    another-longrun
    another-oneshot
    s6rc-fdholder
    s6rc-oneshot-runner

### [Managing services]

The s6-rc package provides one program, also named [s6-rc], to perform most of the service management tasks after initialization has been done. [s6-rc] accepts a *subcommand* that specifies what to do. The subcommands are:

-   **help**: prints a help message.
-   **list**: displays the fully resolved list of atomic services represented by a list of service names supplied as the subcommand\'s arguments, just like [s6-rc-db atomics] (see [extracting information from a compiled database](#s6rcdb)). This list of atomic services is called *the selection*.
-   **change**: computes the selection in the same way as the `list` subcommand, and performs state transitions for all atomic services in the resulting list. If a `-u` option (\'up\') is passed to [s6-rc] (*before* the subcommand name), the requested action is to start all services in the selection, i.e. transition them to up state. If a `-d` option (\'down\') is passed to [s6-rc], the requested action is to stop all services in the selection, i.e. transition them to down state. If there is neither a `-u` nor a `-d` option, [s6-rc] behaves as if the `-u` option had been supplied. If an `-n` option (\'dry run\') followed by an integral value is passed to [s6-rc], state transitions are simulated instead of actually performed (see later).
-   **diff**: checks the consistency between s6-rc\'s view of the state of all longruns (as recorded in the live state directory), and s6\'s view (as recorded in the [state] file of the service\'s [supervise] control directory). This subcommand should normally report nothing, but directly using some s6 programs with s6-rc-managed longruns can cause state discrepancies. For example, if a longrun is in down state, and an [s6-svc -u] command with its symlink in the scan directory is used instead of an [s6-rc -u change] command with its service name, not only would that run the underlying program (without also starting services that were specified as dependencies), but it would also make s6 view the process\' state as up (as reported by [s6-svstat]), while s6-rc would still view the corresponding service as down. The `diff` subcommand prints a line for each longrun it finds that has a state inconsistency, prepended by a plus sign (\'+\') if s6 considers it to be up, and a minus plus sign (\'-\') if s6 considers it to be down.
-   **listall**: displays the computed closed selection, see [service dependencies](#dependencies)).

Unlike [s6-rc-db], which operates exclusively on a compiled database, [s6-rc] operates on the live state directory. Therefore, it has knowledge of not only the associated database, but also of service states. The live state directory is [/run/s6-rc] by default, but a different one can be used by passing an `-l` option to [s6-rc] with the directory\'s pathname (absoulte or relative to [s6-rc]\'s working directory). [s6-rc-db] can be used both with live and non-live databases, but in the latter case, the database\'s pathname has to be specified with a `-c` option.

Because [s6-rc] is aware of service states, it accepts an `-a` (\'active\') option for both its `list` and `change` subcommands, that adds the current set of atomic services in up state to the initial selection derived from the subcomannd\'s arguments. [s6-rc] also accepts the `-d` option for its `list` subcommand, but the meaning in this case is to *complement* the initial selection derived from the subcomannd\'s arguments (plus the active services if the `-a` option is also present), i.e. the final selection is the set of all atomic services in the live state directory\'s associated database that **are not** in the initial selection. For completeness, [s6-rc] also accepts an explicit `-u` option for its `list` subcommand, that does nothing. For both `list` and `change`, the supplied list of service names can be empty, meaning an (initial) *empty selection*. [s6-rc list] is mostly useful in conjunction with the `-a` or `-d` options.

s6-rc also has a notion of *transition success* and *transition failure*. For a longrun, if its underlying program supports the [s6 readiness notification protocol](https://wiki.gentoo.org/wiki/S6#s6readiness "S6"), transition to up state is considered successful if the supervised process is up and ready before the expiry of a timeout. Otherwise, transition to up is considered successful if the supervised process is up before the expiry of a timeout, i.e. when its supervisor has spawned a [run] child. The [s6-rc -u change] command uses an [s6-svc -uwU] or [s6-svc -uwu] command, respectively, to start the supervised process, so it will wait until it [receives a notification](https://wiki.gentoo.org/wiki/S6#s6notification "S6") of the relevant event from [s6-supervise]. Transition to down state is considered successful if the supervised process is really down before the expiry of a timeout, i.e. if it is down and the [finish] file, if present, was executed and has exited (or got killed by [s6-supervise] because of a [timeout-finish] file). The [s6-rc -d change] command uses an [s6-svc -dwD] command to stop the supervised process, so it will wait until it receives the really down notification from [s6-supervise]. If a transition to up fails, the [s6-rc -u change] command then uses an [s6-svc -d] command to bring the supervised process to a known down state. For a oneshot, transition to up or down state is considered successful if the equivalent of executing the [up] or [down] file from its service definition, respectively, that is performed by the [s6-rc-oneshot-run] program, exits with code 0 before the expiry of a timeout (see [oneshot definitions](#oneshots)). The [s6-rc change] command waits for [s6-rc-oneshot-run] to finish. For the full description of the [s6-rc] program, please consult the HTML documentation in the package\'s [/usr/share/doc] subdirectory.

Supporting service [s6rc-oneshot-runner] uses a rules directory to decide whether to grant or refuse service to clients that connect to its UNIX domain socket. The [s6-rc] program executes a [sudo -e] command with [s6rc-oneshot-runner]\'s socket to start or stop a oneshot, so [s6-rc]\'s effective user must be allowed by this service\'s rules directory. Setup of [s6rc-oneshot-runner]\'s rules directory can be done using [s6-rc-compile]\'s `-u` and `-g` options, see [initializing s6-rc](#initialization).

The timeout for a state transition can be configured by including regular files named [timeout-up] and [timeout-down] in the definition of an atomic service submitted to [s6-rc-compile], that must contain an integral time value in milliseconds. The former specifies the timeout for the transition to up, and the latter, for the transition to down. If any of these files is absent or contains the value **0**, the corresponding timeout is infinite, i.e. the [s6-rc change] command will wait forever for the notification of the relevant event from [s6-supervise] in the case of a longrun, and will wait forever for [s6-rc-oneshot-run] to exit, in the case of a oneshot. For further information about configuration of state transition timeouts, please consult [s6-rc-compile]\'s HTML documentation in the package\'s [/usr/share/doc] subdirectory. The **timeout** subcommand of the [s6-rc-db] program prints the state transition timeouts. The up timeout is printed if a `-u` option is passed to [s6-rc-db], and the down timeout is printed if a `-d` option is passed to [s6-rc-db]. If there is neither a `-u` option nor a `-d` option, [s6-rc-db] behaves as if the `-u` option had been specified. For further information, please consult [s6-rc-db]\'s HTML documentation in the package\'s [/usr/share/doc] subdirectory.

[s6-rc change] calls the internal program [s6-rc-dryrun] instead of [s6-svc] or [s6-sudo] when the `-n` option is specified, which makes [s6-rc] print to standard output what the command would have done without the `-n` option. The option must be followed by integral time value in milliseconds; [s6-rc-dryrun] will sleep for the specified time before exiting, to simulate an [s6-svc] or [s6-sudo] invocation that does not complete immediately. For further information about [s6-rc-dryrun], please consult the HTML documentation in the package\'s [/usr/share/doc] subdirectory.

Example usage of [s6-rc] to print a list of all atomic services in the compiled database that is live, assuming the setup from the first example of section [\"initializing s6-rc\"](#initialization):

`user `[`$`]`s6-rc -dl ../live list | sort`

    another-longrun
    another-oneshot
    s6rc-fdholder
    s6rc-oneshot-runner
    test-longrun
    test-oneshot

This works because no service names are provided, so the initial selection is empty, and then the `-d` option complements the selection. The complement of the empty set is \'the universe\', i.e. the set of all atomic services in the compiled database. So this is the same as using an [s6-rc-db -l ../live list services \| sort] command. Simulating a transition to up for service *test-longrun*:

`user `[`$`]`s6-rc -n 10 -ul ../live change test-longrun`

    s6-rc-dryrun: s6-svc -uwU -T 0 -- ../live/servicedirs/test-longrun

The service is a longrun, so this shows that it would be started with an [s6-svc -u] command. Option `-wU` makes the command wait for an up and ready notification from [s6-supervise]. Actually starting the service:

`user `[`$`]`time s6-rc -ul ../live change test-longrun`

    real 0m10.010s
    user    0m0.002s
    sys 0m0.000s

`user `[`$`]`cat ../logdir/current | s6-tai64nlocal`

    2018-03-30 12:19:25.012770836 test-daemon starting

`user `[`$`]`s6-svstat test-longrun`

    up (pid 2448) 38 seconds, ready 28 seconds

This shows that [s6-rc -u change] waited the approximately 10 seconds that were necessary for [test-daemon] become ready and notify [s6-supervise].

`user `[`$`]`ls -l ../live/servicedirs/test-longrun`

    total 20
    drwx-ws--T 2 user user 4096 Mar 30 12:19 event
    -rwxr-xr-x 1 user user  130 Mar 30 12:10 finish
    -rw-r--r-- 1 user user    2 Mar 30 12:10 notification-fd
    -rwxr-xr-x 1 user user   94 Mar 30 12:10 run
    drwx------ 2 user user 4096 Mar 30 12:19 supervise

This shows that the [down] file created by [s6-rc-init] was removed from [test-longrun]\'s compiled s6 service directory by the [s6-rc -u change] command. Simulating a transition to up for service *test-oneshot*:

`user `[`$`]`s6-rc -n 10 -ul ../live change test-oneshot`

    s6-rc-dryrun: s6-svc -uwU -T 0 -- ../live/servicedirs/s6rc-oneshot-runner
    s6-rc-dryrun: s6-sudo -el0 -t 30000 -T 0 -- ../live/servicedirs/s6rc-oneshot-runner/s up 3  # test-oneshot

The service is a oneshot, so this shows that it would be started with an [s6-sudo -e] command that connects to [s6rc-oneshot-runner]\'s socket ([/home/user/live/servicedirs/s6rc-oneshot-runner/s]), and passes arguments \'up\' and \'3\'. This in turn triggers execution of an [s6-rc-oneshot-run up 3] command. The output of [s6-rc-dryrun] is intended to be human readable, so it shows that numeric identifier **3** corresponds indeed to service [test-oneshot] in the compiled service database. Because [s6rc-oneshot-runner] is a dependency of [test-oneshot] and was in down state, [s6-rc] would start it first (see [service dependencies](#dependencies)), and because [s6rc-oneshot-runner] is a longrun, it would use an [s6-svc -u] command to do that. Actually starting the service:

`user `[`$`]`s6-rc -ul ../live change test-oneshot`

    Calling /home/user/s6-rc-scripts/real-script.sh...
    real-script.sh invoked with arguments start
    Performing start actions

Because the [s6-sudoc] - [s6-sudod] mechanism is used for oneshots, and [s6-sudoc] transmits the file descriptors of its standard input, output and error to [s6-sudod] [via fd-passing](https://wiki.gentoo.org/wiki/S6/File_descriptor_holder "S6/File descriptor holder"), messages from the oneshot\'s executed programs are printed on [s6-rc]\'s standard output, which is the interactive shell\'s controlling terminal in this case. Displaying the list of atomic services in up state:

`user `[`$`]`s6-rc -al ../live list | sort`

    s6rc-oneshot-runner
    test-longrun
    test-oneshot

This works because no service names are provided, so the initial selection is empty, and then the `-a` option adds the set of atomic services in up state to it. It is also shown that [s6rc-oneshot-runner] is also in up state.

Service bundle names can be used with [s6-rc] as a substitute of their contained atomic services:

`user `[`$`]`s6-rc-db -l ../live contents test-bundle | sort`

    test-longrun
    test-oneshot

`user `[`$`]`s6-rc -n 10 -dl ../live change test-bundle`

    s6-rc-dryrun: s6-sudo -el0 -t 30000 -T 0 -- ../live/servicedirs/s6rc-oneshot-runner/s down 3  # test-oneshot
    s6-rc-dryrun: s6-svc -dwD -T 0 -- ../live/servicedirs/test-longrun

This shows that stopping bundle *test-bundle* is the same as individually stopping [test-longrun] and [test-oneshot]. [test-longrun] would be stopped with an [s6-svc -d] command; option `-wD` makes the command wait for a really down notification from [s6-supervise]. [test-oneshot] would be stopped with an [s6-sudo -e] command that connects to [s6rc-oneshot-runner]\'s socket, and passes arguments \'down\' and \'3\'. This in turn triggers execution of an [s6-rc-oneshot-run down 3] command.

`user `[`$`]`s6-rc -dl ../live change test-bundle`

    Calling /home/user/s6-rc-scripts/real-script.sh...
    real-script.sh invoked with arguments stop
    Performing stop actions

`user `[`$`]`s6-svstat test-longrun`

    down (exitcode 0) 17 seconds, ready 17 seconds

`user `[`$`]`cat ../logdir/current | s6-tai64nlocal`

    2018-03-30 12:19:25.012770836 test-daemon starting
    2018-03-30 12:25:50.314271979 test-daemon exited with code 0

This shows that [s6-rc -d change] stopped all atomic services contained in the bundle.

`user `[`$`]`ls -l ../live/servicedirs/test-longrun`

    total 20
    -rw-r--r-- 1 user user    0 Mar 30 12:25 down
    drwx-ws--T 2 user user 4096 Mar 30 12:25 event
    -rwxr-xr-x 1 user user  130 Mar 30 12:10 finish
    -rw-r--r-- 1 user user    2 Mar 30 12:10 notification-fd
    -rwxr-xr-x 1 user user   94 Mar 30 12:10 run
    drwx------ 2 user user 4096 Mar 30 12:25 supervise

This shows that [s6-rc -d change] created a [down] file in this longrun\'s service directory.

`user `[`$`]`s6-rc -ul ../live list all-services | sort`

    another-longrun
    another-oneshot
    test-longrun
    test-oneshot

Here the resulting selection of the [s6-rc list] command is the contents of bundle *all-service*, so that\'s what is shown. This is the same as using an [s6-rc-db -l ../live atomics all-services \| sort] command. Starting all atomic services in this selection:

`user `[`$`]`s6-rc -ul ../live change all-services`

    Calling /home/user/s6-rc-scripts/real-script.sh...
    real-script.sh invoked with arguments start
    Performing start actions

`user `[`$`]`s6-rc -al ../live list | sort`

    another-longrun
    another-oneshot
    s6rc-oneshot-runner
    test-longrun
    test-oneshot

Updated supervision tree:

`user `[`$`]`ps xf -o pid,ppid,pgrp,euser,args`

     PID  PPID  PGRP EUSER    COMMAND
    ...
    2130  2123  2130 user     -bash
    2460  2130  2460 user      \_ s6-svscan
    2461  2460  2460 user          \_ s6-supervise logger
    2462  2461  2462 user          |   \_ s6-log t ../../logdir
    2471  2460  2460 user          \_ s6-supervise test-longrun
    2496  2471  2496 user          |   \_ test-daemon --s6=3
    2472  2460  2460 user          \_ s6-supervise s6rc-oneshot-runner
    2495  2472  2495 user          |   \_ s6-ipcserverd -1 -- s6-ipcserver-access ... -- s6-sudod ... -- /usr/libexec/s6-rc-oneshot-run ...
    2473  2460  2460 user          \_ s6-supervise s6rc-fdholder
    2474  2460  2460 user          \_ s6-supervise another-longrun
    2494  2474  2494 user              \_ test-daemon
    ...

This shows that longrun [another-longrun] just spawns another [test-daemon] process, with readiness notification turned off, and that [s6rc-oneshot-runner] launches an [s6-ipcserverd] process that, in turn, spawns an [s6-sudod] child for each client connection to its corresponding socket. [s6-sudod] executes program [s6-rc-oneshot-run] with the arguments supplied by the client.

`user `[`$`]`s6-svc -d another-longrun`

`user `[`$`]`s6-svstat another-longrun`

    down (exitcode 0) 21 seconds, normally up, ready 21 seconds

Service [another-longrun] is now actually in down state, because the underlying program is no longer running, but s6-rc doesn\'t know about it. This type of inconsistencies can be reported by an [s6-rc diff] command:

`user `[`$`]`s6-rc -l ../live diff`

    -another-longrun

The minus sign (\'-\') confirms that s6 considers it down. A subsequent [s6-rc -d change] command that that contains [another-longrun] in its closed selection (see [service dependencies](#dependencies)) will bring the service state in sync again:

`user `[`$`]`s6-rc -dl ../live change another-longrun`

`user `[`$`]`s6-rc -l ../live diff`

`user `[`$`]`s6-svstat another-longrun`

    down (exitcode 0) 48 seconds, ready 48 seconds

The [s6-rc -d change] command uses an [s6-svc -dwD] command, which is a no operation and returns immediatly because the supervised process is already down, but the service state is now also down in s6-rc\'s view, so the the output of [s6-rc diff] is empty.

Stopping all services in the live compiled database:

`user `[`$`]`s6-rc -dal ../live change`

    Calling /home/user/s6-rc-scripts/real-script.sh...
    real-script.sh invoked with arguments stop
    Performing stop actions

`user `[`$`]`cat ../logdir/current | s6-tai64nlocal`

    2018-03-30 12:19:25.012770836 test-daemon starting
    2018-03-30 12:25:50.314271979 test-daemon exited with code 0
    2018-03-30 12:41:08.974825979 test-daemon starting
    2018-03-30 12:43:25.258589540 test-daemon exited with code 0

This shows all of [test-longrun]\'s state transitions, as reported by messages printed by its [run] and [finish] scripts and logged by the supervised [s6-log] process. Requesting a list of atomic services in up state using [s6-rc -al ../live list] should now return an empty result.

To demonstrate usage of [s6-rc diff] once again, service [test-longrun] can transition to up with an [s6-svc -u] command without s6-rc noticing:

`user `[`$`]`s6-svc -u test-longrun`

`user `[`$`]`s6-svstat test-longrun`

    up (pid 2847) 6 seconds, normally down

`user `[`$`]`s6-rc -l ../live diff`

    +test-longrun

The plus sign (\'+\') confirms that s6 considers it up. Consistency can be restored by using an [s6-rc -ul ../live change test-longrun] command to align s6-rc\'s view of service state with s6\'s, or an [s6-svc -d test-longrun] command to align s6\'s view of service state with s6-rc\'s. []

### [Service dependencies]

s6-rc supports the specification of dependencies between services. Service **A** can be defined to *directly depend* on service **B**, with the following meaning:

-   If s6-rc it is asked to start **A**, then **B** is automatically started first, and if that transition was successful, the requested operation is performed.
-   If s6-rc it is asked to stop **B**, then **A** is automatically stopped first, and if that transition was successful, the requested operation is performed.

Therefore, transition failures (see [managing services](#manage)) might result in not performing the requested operation, leaving the service in the state it was before.

In turn, a service\'s dependencies can have dependencies themselves, forming dependency chains: if service **A** directly depends on service **B**, and **B** directly depends on service **C**, then service **A** is said to *depend* (with no qualification) on both **B** and **C**. The aforementioned procedure for state transitions is performed recursively when there are dependency chains, so asking s6-rc to start A will result in a cascade of transitions to up to honor dependencies: C first, B second, A last. Similarly, asking s6-rc to stop C will result in transitions to down for A, B and C, in that order. This means that dependencies introduce, for the purpose of state transitions, a partial ordering of services. The [s6-rc change] command parallelizes the transitions as much as it can. Independent services are processed in parallel, but ordering constraints introduced by dependencies may result in serial processing for one or more subsets of services.

An atomic service definition in [s6-rc-compile]\'s source format (i.e. not [bundle definitions](#bundles)) can specify direct dependencies by including a regular file named [dependencies], that must contain a list of service names, one per line. Whitespace at the beginning of a line is ignored, but trailing whitespace is not. Lines that start with a hash sign (\'#\') are treated as comments and ignored. [dependencies] files *can* contain service bundle names; s6-rc considers the service being defined to directly depend on every atomic service contained in the specified bundle. For further information about configuration of service dependencies, please consult [s6-rc-compile]\'s HTML documentation in the package\'s [/usr/share/doc] subdirectory.

Because dependencies may cause state transitions for services that are not in the computed selection of an [s6-rc change] command, the [s6-rc] program must also compute a *forward dependency graph* for transitions to up, or a *reverse dependency graph* for transitions to down, and then it must compute the *closed selection*, which is the set of all atomic services in the database that need a state transition. An atomic service is in the command\'s closed selection if:

-   it is in the selection, or
-   a service in the selection depends on it and the requested operation was to start services, or
-   it depends on a service in the selection and the requested operation was to stop services.

The format of a compiled service database allows [s6-rc] to perform these computations efficiently. Dependency correctness, i.e. the absence of dependency cycles in the submitted set of service definitions, is verified by [s6-rc-compile] at the time of database creation.

The [s6-rc-db] program (see [extracting information from a compiled database](#s6rcdb)) has two subcommands that display dependency information:

-   **dependencies**: displays the direct dependencies of the service corresponding to the name supplied as the subcommand\'s argument. If the specified service is a bundle, it displays the union of the direct dependencies of all the atomic services contained in the bundle.
-   **all-dependencies**: displays the fully resolved list of atomic services represented by the list of service names supplied as the subcommand\'s arguments, in the same way as the `atomics` subcommand, plus all services in either the forward or the reverse dependency graph. The forward dependency graph is used if a `-u` option is passed to [s6-rc-db], and the reverse dependency graph is used if a `-d` option is passed to [s6-rc-db]. If there is neither a `-u` option nor a `-d` option, [s6-rc-db] behaves as if the `-u` option had been specified.

Finally, the [s6-rc] program also has a **listall** subcommand that displays the closed selection computed from the service names supplied as arguments. Since this is done with a depencency graph, the result is the same as that of [s6-rc-db all-dependencies], except that the latter can also be used with a compiled database that is not live. The forward dependency graph is used if the `-u` option is passed to [s6-rc], and the reverse dependency graph is used if the `-d` option is passed to [s6-rc]. If a `-p` option (\'prune\') is passed to [s6-rc] combined with the `change` subcommand, if a transition to up was requested, services in the computed closed selection are started and every other service not in down state is stopped. If a transition to down was requested, services in the computed closed selection are stopped and every other service not in up state is started. In both cases, all transitions to down are performed before all transitions to up.

For further information about the [s6-rc] and [s6-rc-db] programs, please consult the HTML documentation in the package\'s [/usr/share/doc] subdirectory.

Example set of service definitions with dependencies:

`user `[`$`]`ls -l srv-src3/*`

    srv-src3/service-A:
    total 24
    drwxr-xr-x 2 user user 4096 Apr 11 12:00 env
    -rw-r--r-- 1 user user   44 Apr 11 12:00 finish
    -rw-r--r-- 1 user user    2 Apr 11 12:00 notification-fd
    -rw-r--r-- 1 user user  161 Apr 11 12:00 run
    -rw-r--r-- 1 user user    6 Apr 11 12:00 timeout-up
    -rw-r--r-- 1 user user    8 Apr 11 12:00 type

    srv-src3/service-B:
    total 20
    -rw-r--r-- 1 user user 10 Apr 11 12:00 dependencies
    -rw-r--r-- 1 user user 44 Apr 11 12:00 finish
    -rw-r--r-- 1 user user  2 Apr 11 12:00 notification-fd
    -rw-r--r-- 1 user user 92 Apr 11 12:00 run
    -rw-r--r-- 1 user user  8 Apr 11 12:00 type

    srv-src3/service-C:
    total 12
    -rw-r--r-- 1 user user  50 Apr 11 12:00 down
    -rw-r--r-- 1 user user   8 Apr 11 12:00 type
    -rw-r--r-- 1 user user 150 Apr 11 12:00 up

    srv-src3/service-D:
    total 16
    -rw-r--r-- 1 user user 20 Apr 11 12:00 dependencies
    -rw-r--r-- 1 user user 44 Apr 11 12:00 finish
    -rw-r--r-- 1 user user 85 Apr 11 12:00 run
    -rw-r--r-- 1 user user  8 Apr 11 12:00 type

    srv-src3/service-E:
    total 20
    drwxr-xr-x 2 user user 4096 Apr 11 12:00 env
    -rw-r--r-- 1 user user  177 Apr 11 12:00 finish
    -rw-r--r-- 1 user user    2 Apr 11 12:00 notification-fd
    -rw-r--r-- 1 user user  158 Apr 11 12:00 run
    -rw-r--r-- 1 user user    8 Apr 11 12:00 type

    srv-src3/service-F:
    total 16
    -rw-r--r-- 1 user user 10 Apr 11 12:00 dependencies
    -rw-r--r-- 1 user user 76 Apr 11 12:00 down
    -rw-r--r-- 1 user user  8 Apr 11 12:00 type
    -rw-r--r-- 1 user user 50 Apr 11 12:00 up

    srv-src3/service-G:
    total 12
    -rw-r--r-- 1 user user 44 Apr 11 12:00 finish
    -rw-r--r-- 1 user user 85 Apr 11 12:00 run
    -rw-r--r-- 1 user user  8 Apr 11 12:00 type

Dependency specifications for these services are set up according to the following diagram:

    A <-- B <--+ D
               |
          C <--+

          E <--  F

                 G

Legend `X <-- Y` means \"Y directly depends on X\". This diagram shows that service D depends on services A, B and C. Service A is a longrun with no dependencies:

[FILE] **`srv-src3/service-A/type`**

    longrun

[FILE] **`srv-src3/service-A/run`**

    #!/bin/execlineb -P
    foreground
    s6-envdir env
    foreground
    fdmove -c 2 1
    test-daemon --s6=3

[FILE] **`srv-src3/service-A/notification-fd`**

    3

[FILE] **`srv-src3/service-A/timeout-up`**

    15000

[FILE] **`srv-src3/service-A/finish`**

    #!/bin/execlineb -P
    echo Service A stopping

The underlying program is a hypothetical [test-daemon] program that supports the [s6 readiness notification protocol](https://wiki.gentoo.org/wiki/S6 "S6") when passed an `--s6` option. The notification channel\'s file descriptor is **3**, so there is a [notification-fd] file specifying that. The time taken by this service to be up and ready is the value of environment variable `LONGRUN_TIME` (**1 second** if unset), plus the actual time [test-daemon] takes to be up and ready. A timeout value of **15 seconds** (15000 milliseconds) is set for this service\'s transition to up. The environment is set by the s6 supervision tree and modified by the contents of environment subdirectory [env], which will be copied verbatim to service A\'s compiled s6 service directory. Both the [run] and [finish] scripts print messages to standard output, so that service events can be tracked.

Service B also runs [test-daemon], and has service A as a direct dependency:

[FILE] **`srv-src3/service-B/type`**

    longrun

[FILE] **`srv-src3/service-B/dependencies`**

    service-A

[FILE] **`srv-src3/service-B/run`**

    #!/bin/execlineb -P
    foreground
    fdmove -c 2 1
    test-daemon --s6=3

[FILE] **`srv-src3/service-B/notification-fd`**

    3

[FILE] **`srv-src3/service-B/finish`**

    #!/bin/execlineb -P
    echo Service B stopping

Service C is a oneshot with no dependencies that prints messages to standard output, so that service events can be tracked, but does nothing else:

[FILE] **`srv-src3/service-C/type`**

    oneshot

[FILE] **`srv-src3/service-C/up`**

    foreground
       s6-tai64n
    }
    s6-envdir -I /home/user/s6-rc-env/service-C
    importas -D 0 E ONESHOT_STATUS
    exit $E

[FILE] **`srv-src3/service-C/down`**

    pipeline -d
    s6-tai64n

The [up] and [down] files contain full execline scripts in this case. The former can have different exit codes depending on environment variable `ONESHOT_STATUS` (**0** if unset). The environment is set by the s6 supervision tree, inherited by [s6-rc-oneshot-run], and modified by the contents of environment directory [/home/user/s6-rc-env/service-C]. Because oneshots don\'t have a corresponding s6 service directory, this envdir must be elsewhere, and specified via an absolute pathname. [s6-tai64n] invocations are used to prepend a timestamp to printed messages.

Service D also runs [test-daemon] with readiness notification turned off, and has two direct dependencies:

[FILE] **`srv-src3/service-D/type`**

    longrun

[FILE] **`srv-src3/service-D/dependencies`**

    service-B
    service-C

This means it has both a longrun (service B) and a oneshot (service C) as dependencies.

[FILE] **`srv-src3/service-D/run`**

    #!/bin/execlineb -P
    foreground
    fdmove -c 2 1
    test-daemon

[FILE] **`srv-src3/service-D/finish`**

    #!/bin/execlineb -P
    echo Service D stopping

Service E is a longrun with no dependencies:

[FILE] **`srv-src3/service-E/type`**

    longrun

[FILE] **`srv-src3/service-E/run`**

    #!/bin/execlineb -P
    foreground
    s6-envdir env
    importas -D no Y LONGRUN_FAIL
    if
    fdmove -c 2 1
    test-daemon --s6=3

[FILE] **`srv-src3/service-E/notification-fd`**

    3

This [run] execline script exits 1 if environment variable `LONGRUN_FAIL` has the value **yes**, and runs [test-daemon] otherwise. The environment is set by the s6 supervision tree and modified by the contents of environment subdirectory [env].

[FILE] **`srv-src3/service-E/finish`**

    #!/bin/execlineb -P
    s6-envdir env
    importas -D no Y LONGRUN_FAIL
    ifte
       exit 125
    }
    test $Y != yes

This [finish] execline script exits **125** if environment variable `LONGRUN_FAIL` has the value **yes**, signalling permanent failure to [s6-supervise].

Service F is a oneshot that only prints messages to standard output, and that has a longrun as its direct dependency:

[FILE] **`srv-src3/service-F/type`**

    oneshot

[FILE] **`srv-src3/service-F/dependencies`**

    service-E

[FILE] **`srv-src3/service-F/up`**

    pipeline -d
    s6-tai64n

[FILE] **`srv-src3/service-F/down`**

    foreground
       s6-tai64n
    }
    sleep 10

And finally, service G is a longrun with no dependencies and no relation with any other service, that also runs [test-daemon] with readiness notification turned off:

[FILE] **`srv-src3/service-G/type`**

    longrun

[FILE] **`srv-src3/service-G/run`**

    #!/bin/execlineb -P
    foreground
    fdmove -c 2 1
    test-daemon

[FILE] **`srv-src3/service-G/finish`**

    #!/bin/execlineb -P
    echo Service G stopping

Creating an s6-rc compiled database with this set of services and using [s6-rc-db] to show direct dependencies:

`user `[`$`]`s6-rc-compile -u $(id -u) test-database2 srv-src3`

`user `[`$`]`for i in A B C D E F G`

    > do echo service-$i:
    > s6-rc-db -c test-database2 dependencies service-$i
    > echo
    > done
    service-A:

    service-B:
    service-A

    service-C:
    s6rc-oneshot-runner

    service-D:
    service-C
    service-B

    service-E:

    service-F:
    service-E
    s6rc-oneshot-runner

    service-G:

Note that for every oneshot the implicit dependency on service [s6rc-oneshot-runner] is also displayed (see [oneshot definitions](#oneshots)). Initializing s6-rc, assuming that there is a supervision tree with [/home/user/scan] as the scan directory and with a logger like in the example from section [\"initializing s6-rc\"](#initialization), that database *test-database2* is in [/home/user], and that the working directory is the scan directory:

`user `[`$`]`s6-rc-init -c /home/user/test-database2 -l /home/user/live /home/user/scan`

`user `[`$`]`s6-rc -ul ../live list service- | sort`

    service-D
    service-F
    service-G

`user `[`$`]`s6-rc -ul ../live listall service- | sort`

    s6rc-oneshot-runner
    service-A
    service-B
    service-C
    service-D
    service-E
    service-F
    service-G

Here [s6-rc]\'s selection is the same as the list of services provided as arguments, because they are all atomic services, and [s6-rc -u listall] shows the resulting closed selection using the forward dependency graph: services D, F and G are included because they are in the selection, services A, B and C are included because they are dependencies of service D, service E is included because it is a dependency of service F, and [s6rc-oneshot-runner] is included because services C and F are oneshots and depend on it. An [s6-rc-db -ul ../live all-dependencies service- \| sort] command would have produced the same output. Simulating the transition of services to up state:

`user `[`$`]`s6-rc -n 10 -ul ../live change service-`

    s6-rc-dryrun: s6-svc -uwu -T 0 -- ../live/servicedirs/service-G
    s6-rc-dryrun: s6-svc -uwU -T 0 -- ../live/servicedirs/service-E
    s6-rc-dryrun: s6-svc -uwU -T 15000 -- ../live/servicedirs/service-A
    s6-rc-dryrun: s6-svc -uwU -T 0 -- ../live/servicedirs/s6rc-oneshot-runner
    s6-rc-dryrun: s6-svc -uwU -T 0 -- ../live/servicedirs/service-B
    s6-rc-dryrun: s6-sudo -el0 -t 30000 -T 0 -- ../live/servicedirs/s6rc-oneshot-runner/s up 8  # service-F
    s6-rc-dryrun: s6-sudo -el0 -t 30000 -T 0 -- ../live/servicedirs/s6rc-oneshot-runner/s up 7  # service-C
    s6-rc-dryrun: s6-svc -uwu -T 0 -- ../live/servicedirs/service-D

Services D and G are longruns that don\'t use readiness notificacion, so [s6-svc]\'s `-wu` option (wait for the up notification) is used instead of `-wU` (wait for the up and ready notification). And because service A\'s definition specified an up timeout of 15 seconds, the corresponding [s6-svc] invocation uses a `-T 15000` option instead of `-T 0` (\"infinite\").

Actually starting the services:

`user `[`$`]`time s6-rc -ul ../live change service- | s6-tai64nlocal`

    2018-04-12 11:39:59.886267000 Service C starting
    2018-04-12 11:40:09.801486747 Service F starting

    real    0m21.194s
    user    0m0.015s
    sys 0m0.010s

`user `[`$`]`cat ../logdir/current | s6-tai64nlocal`

    2018-04-12 11:39:59.683503297 Service G starting
    2018-04-12 11:39:59.685378175 Service E starting
    2018-04-12 11:39:59.686330763 Service A starting
    2018-04-12 11:40:10.784500674 Service B starting
    2018-04-12 11:40:20.793244854 Service D starting

This shows how [s6-rc change] tried to parallelize state transitions as much as it could: services A, C, E and G were started immediately and in parallel, but services B, D and F were not. Service B\'s transition happens approximately 11 seconds after service A\'s, because it is a dependency and that is the time it took service A to become up and ready, and service D\'s transition happens approximately 10 seconds after service B\'s for the same reason. It didn\'t happen later than that because its other dependencies, services A and C, had already successfully transitioned to up. Service F\'s transition happens approximately 10 seconds after service E\'s, because it is a dependency and that is the time it took service E to become up and ready. Service D\'s, F\'s, and G\'s transitions are almost instant, because service F is a oneshot, and services D and G do not wait for readiness, so the whole operation took about 21 seconds, and finished after service D\'s transition to up. Because all state transitions were successful, all services in the selection are now in up state. Stopping all services:

`user `[`$`]`time s6-rc -dal ../live change | s6-tai64nlocal`

    2018-04-12 11:42:37.012906156 Service F stopping
    2018-04-12 11:42:37.022828479 Service C stopping

    real    0m10.019s
    user    0m0.005s
    sys 0m0.006s

`user `[`$`]`cat ../logdir/current | s6-tai64nlocal`

    2018-04-12 11:39:59.683503297 Service G starting
    2018-04-12 11:39:59.685378175 Service E starting
    2018-04-12 11:39:59.686330763 Service A starting
    2018-04-12 11:40:10.784500674 Service B starting
    2018-04-12 11:40:20.793244854 Service D starting
    2018-04-12 11:42:37.014092710 Service G stopping
    2018-04-12 11:42:37.017188595 Service D stopping
    2018-04-12 11:42:37.022690818 Service B stopping
    2018-04-12 11:42:37.029667303 Service A stopping
    2018-04-12 11:42:47.023984194 Service E stopping

This shows that most state transitions were almost instant except service F\'s, because of the [sleep 10] command in its [down] file. Service E\'s transition happens after service F\'s transition completed because it is a dependency, so the whole operation took about 10 seconds and finished after service E\'s transition to down.

Forcing a rotation of the logging directory with an [s6-svc -a logger] command so that the [current] file gets emptied, and redoing the steps with one modification:

`user `[`$`]`echo 10 >service-A/env/LONGRUN_TIME`

`user `[`$`]`time s6-rc -ul ../live change service- | s6-tai64nlocal`

    2018-04-12 11:47:02.955608987 Service C starting
    2018-04-12 11:47:12.969170358 Service F starting
    s6-svlisten1: fatal: timed out
    s6-rc: warning: unable to start service service-A: command exited 99

    real    0m15.025s
    user    0m0.003s
    sys 0m0.005s

`user `[`$`]`cat ../logdir/current | s6-tai64nlocal`

    2018-04-12 11:47:02.943057415 Service G starting
    2018-04-12 11:47:02.948378126 Service E starting
    2018-04-12 11:47:02.948776158 Service A starting
    2018-04-12 11:47:17.962572120 Service A stopping

This shows that the attempt to start service A failed: an extra delay of 10 seconds caused by the setting of environment variable `LONGRUN_TIME` caused the transition to take longer than the maximum 15 seconds configured in its service definiton. And because of that failure, services that depend on service A were not started -in this case, services B and D-. The whole operation took about 15 seconds and finished after service A\'s transition timed out. The final \"Service A stopping\" message in the log is caused by the extra [s6-svc -d] command that [s6-rc -u change] executes for longruns that fail to start.

`user `[`$`]`s6-rc -ual ../live list | sort`

    s6rc-oneshot-runner
    service-C
    service-E
    service-F
    service-G

This shows that after the [s6-rc -u change] command, services A, B and D are not in up state. Stopping all services with an [s6-rc -dal ../live change], forcing another rotation of the logging directory, and redoing the steps with more modifications:

`user `[`$`]`rm service-A/env/LONGRUN_TIME`

`user `[`$`]`echo 7 >/home/user/s6-rc-env/service-C/ONESHOT_STATUS`

`user `[`$`]`time s6-rc -ul ../live change service- | s6-tai64nlocal`

    2018-04-12 11:53:24.643007310 Service C starting
    s6-rc: warning: unable to start service service-C: command exited 7
    2018-04-12 11:53:34.642459632 Service F starting

    real    0m21.031s
    user    0m0.004s
    sys 0m0.005s

`user `[`$`]`cat ../logdir/current | s6-tai64nlocal`

    2018-04-12 11:53:24.632173839 Service E starting
    2018-04-12 11:53:24.637136736 Service G starting
    2018-04-12 11:53:24.637411837 Service A starting
    2018-04-12 11:53:35.650247605 Service B starting

This shows that the attempt to start service C failed: the equivalent of executing the [up] file of its service definition that program [s6-rc-oneshot-run] performs exited with a nonzero code (**7**), caused by the setting of environment variable `ONESHOT_STATUS`. And because service D depends on service C, the former was not started. The whole operation took about 21 seconds and finished after service B\'s transition to up.

`user `[`$`]`s6-rc -al ../live list | sort`

    s6rc-oneshot-runner
    service-A
    service-B
    service-E
    service-F
    service-G

This shows that after the [s6-rc -u change] command, services C and D are not in up state. Stopping all services, forcing another rotation of the logging directory, and redoing the steps with more modifications:

`user `[`$`]`rm /home/user/s6-rc-env/service-C/ONESHOT_STATUS`

`user `[`$`]`echo yes >service-E/env/LONGRUN_FAIL`

`user `[`$`]`time s6-rc -ul ../live change service- | s6-tai64nlocal`

    s6-svlisten1: fatal: ../live/servicedirs/service-E failed permanently: the finish script exited 125
    s6-rc: warning: unable to start service service-E: command exited 1
    2018-04-12 12:08:45.991490743 Service C starting

    real    0m21.238s
    user    0m0.006s
    sys 0m0.011s

`user `[`$`]`cat ../logdir/current | s6-tai64nlocal`

    2018-04-12 12:08:45.689700612 Service G starting
    2018-04-12 12:08:45.720197503 Service E starting
    2018-04-12 12:08:45.740891903 Service A starting
    2018-04-12 12:08:45.880561107 Service E failed permanently
    2018-04-12 12:08:56.846140697 Service B starting
    2018-04-12 12:09:06.853497873 Service D starting

This shows that the attempt to start service E failed: the setting of environment variable `LONGRUN_FAIL` to **yes** caused the [run] script in its s6 service directory to exit immediately, and the [finish] script to exit with code 125, which signals permanent failure to s6. And because service F depends on service E, the former was not started. The whole operation took about 21 seconds and finished after service D\'s transition to up.

`user `[`$`]`s6-rc -al ../live list | sort`

    s6rc-oneshot-runner
    service-A
    service-B
    service-C
    service-D
    service-G

This shows that after the [s6-rc -u change] command, services E and F are not in up state. []

### [Live updates to the service database]

The s6-rc package provides a program, [s6-rc-bundle], that allows adding or removing [service bundles](#bundles) to or from a compiled database, without having to recompile it from source using [s6-rc-compile]. It is also notable in that it can be used even if the database is live, i.e. already associated with an s6 supervision tree and an s6-rc live state directory. [s6-rc-bundle] accepts a subcommand that tells it what to do:

-   **add**: adds a service bundle to the database. It accepts a list of service names: the first one is the name of the bundle, and the others are the contents of the bundle. The effect is the same as that of a bundle definition in [s6-rc-compile]\'s source format that contains those service names in its [contents] file.
-   **delete**: removes a service bundle from the database. It accepts a single argument specifying the name of the bundle.
-   **multiple**: allows removal and addition of several service bundles in one go. It expects its arguments to be in the format execline\'s [execlineb] program [generates when parsing the block syntax](https://skarnet.org/software/execline/el_semicolon.html), so the forward compatible way to use it is in an execline script or [execlineb -c] command: the invocation can be written using a the syntax [s6-rc-bundle multiple  n1  n2  \...], where *d1*, *d2*, \... are service names specifying bundles to delete, *n1*, *n2*, \... are service names specifying bundles to add, *c11*, *c12*, \... are service names specifying the contents of bundle *n1*, *c21*, *c22*, \... are service names specifying the contents of bundle *n2*, and so on. The list *d1 d2 \...* can be empty, resulting in no deletions. Everything after the first -block can be omitted, resulting in no additions.

[s6-rc-bundle] operates on the database associated with live state directory [/run/s6-rc], unless it is passed an `-l` option followed by the (absolute or relative to the working directory) pathname of a different live state directory, or it is passed a `-c` option followed by the pathname of a database. For more information about [s6-rc-bundle], please consult the HTML documentation in the package\'s [/usr/share/doc] subdirectory.

Using [s6-rc-bundle] is the only way to modify a compiled database. Any other modification has to be done on the service definitions in source format that were used to create the database, and then [s6-rc-compile] must be used to make a new database. Because a database that is live cannot be deleted, the s6-rc package provides a tool that allows its *replacement*: the [s6-rc-update] program, an *online service database switcher*. If the replaced database contained a service that is not present in the replacing database, the affected service will be *deleted*: its name will no longer be recognized as valid by tools like the [s6-rc] and [s6-rc-db] programs. Therefore, the replacing database must contain all wanted services, both modified and unmodified ones, and generally means that service definitions in [s6-rc-compile]\'s source format must be kept around.

[s6-rc-update] accepts the replacing database\'s absolute pathname as an argument, and performs the database switch for live state directory [/run/s6-rc], unless it is passed an `-l` option followed by the absolute pathname of a different live state directory. It also ensures consistency of service states: it analyses both the replaced and replacing database\'s contents to determine which services are present in both (based on name), and preserves their corresponding state, except for services that change types (longrun to oneshot and vice-versa, atomic service to bundle and vice-versa) or direct dependencies. In those cases, if the service is in up state at program startup, [s6-rc-update] *restarts* it: it stops it before the database replacement, and then starts it after the database replacement, so if there are new services defined as direct dependencies, [s6-rc-update] will start them too after the database replacement. Deleted services are stopped before the replacement.

[s6-rc-update] also accepts an `-f` option followed by the pathname of a file, the *conversion file*, that can currently be used for two purposes: service renaming and forced restarts. The file must contain a sequence of lines of text, each of which is independently lexed into words as if by the [execlineb] program, so it can contain #-comments, quoted strings, etc. A line of the form `old-service -> new-service` renames service *old-service* to *new-service*. Therefore, all appearances of name *old-service* in service definitions of the replaced database, and all appearances of name *new-service* in service definitions of the replacing database, are understood to refer to the same service for the purpose of computing needed state transitions. Otherwise, they are considered to name unrelated services. A line of the form `service-name restart` makes [s6-rc-update] forcibly restart service *service-name*, and a line of the form `old-service -> new-service restart` makes [s6-rc-update] perform both a rename and a forced restart.

** Note**\
If a renamed service is a longrun that does not end up getting restarted by [s6-rc-update], and the [ps] utility is used after the service database switch, its [s6-supervise] parent will appear in the output with the old service name as agrument, because that is how it was invoked by [s6-svscan]. This is purely cosmetic and has no impact on the service; nevertheless, if the \'correct\' ouput is desired, the file supplied with the `-f` option must also specify a forced restart of the longrun.

[s6-rc-update] performs the computed state transitions using an [s6-rc -d change] command before the database switch, and an [s6-rc -u change] command after the database switch. It also accepts an `-n` (\'dry run\') option that makes it simulate the state transitions without switching the database, printing the [s6-rc] invocations to standard output with the [s6-rc-dryrun] internal program. For the full description of [s6-rc-compile], please consult the HTML documentation in the package\'s [/usr/share/doc] subdirectory.

** Important**\
The absolute pathname specified to [s6-rc-update] with an `-l` option must be that of the symbolic link to directory created by [s6-rc-init], not that of the actual directory.

Finally, s6-rc provides the [s6-rc-format-upgrade] program, that can be used to upgrade the format of a compiled service database that is live and was created with an earlier, incompatible version of [s6-rc-compile]. It is intended to be used after upgrading the s6-rc package to a possibly backwards-incompatible version, without disrupting the live state directory and associated s6 supervision tree (e.g. if s6-rc is used as [an init system component](#initsystem)). It accepts the absolute pathname of a compiled database, and operates on live state directory [/run/s6-rc], unless it is passed an `-l` option followed by the (absolute or relative to the working directory) pathname of a different live state directory. For more information about [s6-rc-format-upgrade], please consult the HTML documentation in the package\'s [/usr/share/doc] subdirectory.

** Important**\
The replacing database submitted to [s6-rc-format-upgrade] must have been created with the [s6-rc-compile] program from the upgraded package, and the exact same service definitions in source format that were originally used to compile the replaced database. So, for example, if database A was created from service definitions *S1*, *S2*, \..., *SN* with [s6-rc-compile] from version 0.3.0.1, and an upgrade is made to version 0.4.0.0, then, after the ugrade, a new database B must be created from *S1*, *S2*, \..., *SN* with [s6-rc-compile], and then [s6-rc-format-upgrade] must be invoked with database B\'s pathname (and that of the live state directory A is currently associated with, using the `-l` option, if it is not [/run/s6-rc]). Please carefully review the details of the upgrade procedure in [s6-rc-format-upgrade]\'s HTML documentation (in the package\'s [/usr/share/doc] subdirectory).

** Warning**\
As of s6-rc version 0.4.0.0, [s6-rc-update] **cannot** be safely used with a live state directory currently associated with a database that was created with the [s6-rc-compile] program from an earlier, backwards-incompatible version of the package.

[s6-rc-format-upgrade] currently handles upgrades from version 0.3.0.1 to version 0.4.0.0, and performs a database switch like [s6-rc-update] does, but without changing any service states (i.e. without executing any [s6-rc change] commands). However, to upgrade to version 0.4.0.0, or any later version compatible with the 0.4.x.x series, without disruption of services in a database that is live, an intermediate upgrade to version 0.3.0.1 is needed^[\[1\]](#cite_note-1)^ using the following procedure:

1.  Upgrade to s6-rc version 0.3.0.1.
2.  Recompile all live service databases using [s6-rc-compile] from their corresponding service definitions in source format.
3.  Perform all live database switches using [s6-rc-update] ([s6-rc-format-upgrade] was introduced in version 0.4.0.0).
4.  Upgrade to s6-rc version 0.4.0.0 or any later, compatible version.
5.  Recompile all live service databases again using [s6-rc-compile].
6.  Perform all database format upgrades using [s6-rc-format-upgrade].

** Note**\
s6-rc packages have four number verions of the form A.B.C.D. For the purpose of deciding whether [s6-rc-format-upgrade] should be used, two versions are considered incompatible if they differ in either the first (A) or second (B) number.

Example usage of [s6-rc-update], assuming the setup from section [\"service dependencies\"](#dependencies), and assuming that the working directory is the scan directory:

`user `[`$`]`ls -l ../live`

    lrwxrwxrwx 1 user user 22 Apr 16 12:14 ../live -> live:s6-rc-init:y0jVfr

`user `[`$`]`ls -l`

    total 8
    drwxr-xr-x 4 user user 4096 Apr 16 12:00 logger
    lrwxrwxrwx 1 user user   41 Apr 16 12:14 s6rc-fdholder -> /home/user/live/servicedirs/s6rc-fdholder
    lrwxrwxrwx 1 user user   47 Apr 16 12:14 s6rc-oneshot-runner -> /home/user/live/servicedirs/s6rc-oneshot-runner
    lrwxrwxrwx 1 user user   37 Apr 16 12:14 service-A -> /home/user/live/servicedirs/service-A
    lrwxrwxrwx 1 user user   37 Apr 16 12:14 service-B -> /home/user/live/servicedirs/service-B
    lrwxrwxrwx 1 user user   37 Apr 16 12:14 service-D -> /home/user/live/servicedirs/service-D
    lrwxrwxrwx 1 user user   37 Apr 16 12:14 service-E -> /home/user/live/servicedirs/service-E
    lrwxrwxrwx 1 user user   37 Apr 16 12:14 service-G -> /home/user/live/servicedirs/service-G

List of services in up state:

`user `[`$`]`s6-rc -ual ../live list | sort`

    s6rc-oneshot-runner
    service-A
    service-B
    service-C
    service-D
    service-E
    service-F
    service-G

The associated service database is going to be replaced by one created from this set of service definitions in [s6-rc-compile]\'s source format:

`user `[`$`]`ls -l srv-src4/*`

    lrwxrwxrwx 1 user user   21 Apr 14 12:00 srv-src4/service-C-renamed -> ../srv-src3/service-C
    lrwxrwxrwx 1 user user   21 Apr 14 12:00 srv-src4/service-F -> ../srv-src3/service-F
    lrwxrwxrwx 1 user user   21 Apr 14 12:00 srv-src4/service-G -> ../srv-src3/service-G

    srv-src4/service-B:
    total 0
    lrwxrwxrwx 1 user user 31 Apr 14 12:00 finish -> ../../srv-src3/service-B/finish
    lrwxrwxrwx 1 user user 40 Apr 14 12:00 notification-fd -> ../../srv-src3/service-B/notification-fd
    lrwxrwxrwx 1 user user 28 Apr 14 12:00 run -> ../../srv-src3/service-B/run
    lrwxrwxrwx 1 user user 29 Apr 14 12:00 type -> ../../srv-src3/service-B/type

    srv-src4/service-D:
    total 4
    -rw-r--r-- 1 user user 28 Apr 14 12:00 dependencies
    lrwxrwxrwx 1 user user 31 Apr 14 12:00 finish -> ../../srv-src3/service-D/finish
    lrwxrwxrwx 1 user user 28 Apr 14 12:00 run -> ../../srv-src3/service-D/run
    lrwxrwxrwx 1 user user 29 Apr 14 12:00 type -> ../../srv-src3/service-D/type

    srv-src4/service-E:
    total 12
    -rw-r--r-- 1 user user 50 Apr 14 12:00 down
    -rw-r--r-- 1 user user  8 Apr 14 12:00 type
    -rw-r--r-- 1 user user 50 Apr 14 12:00 up

This shows that directories containing service definitions are allowed to have symbolic links to files and directories placed elsewhere. The new database is mostly the same as database *test-database2*, except that it contains no service A (so it will be removed after the database switch), renames service C to *service-C-renamed*, and turns service E into a oneshot. So all references to service A must be removed, and all references to service C must use the new name:

[FILE] **`srv-src4/service-D/dependencies`**

    service-B
    service-C-renamed

Service A is gone from [service-D/dependencies], and so is file [service-B/dependencies]. Service E needs a new definition:

[FILE] **`srv-src4/service-E/type`**

    oneshot

[FILE] **`srv-src4/service-E/up`**

    pipeline -d
    s6-tai64n

[FILE] **`srv-src4/service-E/down`**

    pipeline -d
    s6-tai64n

To actually rename service C, a conversion file must be supplied:

[FILE] **`conversion-file1`**

    service-C -> service-C-renamed

Compiling the new database using an [s6-rc-compile -u \$(id -u) test-database3 srv-src4] command, assuming it will be placed in [/home/user] along with the conversion file, and simulating the effect of invoking [s6-rc-update]:

`user `[`$`]`s6-rc-update -n -l /home/user/live -f ../conversion-file1 /home/user/test-database3`

    s6-rc-dryrun: s6-rc -v 1 -t 0 -l /home/user/live -d -- change service-E service-A
    s6-rc-dryrun: s6-rc -v 1 -t 0 -l /home/user/live -u -- change service-F service-E service-D service-B

This shows that [s6-rc-update] would use an [s6-rc -d change] command to stop some services, switch the database, and then use an [s6-rc -u change] command to start some other services, which implies that (possibly updated) dependency specifications would be honored. Actually performing the database switch, after forcing a rotation of the logging directory with an [s6-svc -a logger] command so that the [current] file gets emptied:

`user `[`$`]`time s6-rc-update -l /home/user/live -f ../conversion-file1 /home/user/test-database3 | s6-tai64nlocal`

    2018-04-16 12:17:38.591813680 Service F stopping
    2018-04-16 12:17:48.616989175 Service E starting
    2018-04-16 12:17:48.623626677 Service F starting

    real    0m20.040s
    user    0m0.006s
    sys 0m0.012s

`user `[`$`]`cat ../logdir/current | s6-tai64nlocal`

    2018-04-16 12:17:38.591475904 Service D stopping
    2018-04-16 12:17:38.596463367 Service B stopping
    2018-04-16 12:17:38.603899826 Service A stopping
    2018-04-16 12:17:48.601233571 Service E stopping
    2018-04-16 12:17:48.617483162 Service B starting
    2018-04-16 12:17:58.624084755 Service D starting

This shows that because service E changes type, the original longrun was stopped, and the new oneshot was started. Longruns\' messages appear in the supervision tree\'s logging directory, but because of [s6-sudoc]\'s fd-passing, oneshots\' messages are printed to [s6-rc-update]\'s standard output. Therefore, the \"Service E stopping\" and \"Service E starting\" messages appear in different places. This also shows that because service A was removed, it was stopped first, and because services B and D depended on it and were up before the database switch, both were restarted. Note that transitions to down have to be serial in the order D, B, A, and transitions to up have to be serial in the order B, D. Finally, because service F continues to depend on service E, and the latter had to restart, F was restarted too, again using serial transitions. Service F was stopped first, and service E was stopped about 10 seconds later, because that was the duration of service F\'s transition. Then, after the database switch, their transitions to up were almost instant. The whole operation took about 20 seconds: 10 to stop service F plus 10 to start service B.

The symbolic link to the live state directory was updated:

`user `[`$`]`ls -l ../live`

    lrwxrwxrwx 1 user user 24 Apr 16 12:17 ../live -> live:s6-rc-update:SGBH3e

The output of [ls] previously showed [live:s6-rc-init:y0jVfr]. The s6 scan directory has also updated all symbolic links:

`user `[`$`]`ls -l`

    total 8
    drwxr-xr-x 4 user user 4096 Apr 16 12:00 logger
    lrwxrwxrwx 1 user user   41 Apr 16 12:17 s6rc-fdholder -> /home/user/live/servicedirs/s6rc-fdholder
    lrwxrwxrwx 1 user user   47 Apr 16 12:17 s6rc-oneshot-runner -> /home/user/live/servicedirs/s6rc-oneshot-runner
    lrwxrwxrwx 1 user user   37 Apr 16 12:17 service-B -> /home/user/live/servicedirs/service-B
    lrwxrwxrwx 1 user user   37 Apr 16 12:17 service-D -> /home/user/live/servicedirs/service-D
    lrwxrwxrwx 1 user user   37 Apr 16 12:17 service-G -> /home/user/live/servicedirs/service-G

There is neither a [service-A] symlink, because the corresponding service no longer exists, nor a [service-E] symlink, because the corresponding service is no longer a longrun.

`user `[`$`]`s6-rc -ual ../live list | sort`

    s6rc-oneshot-runner
    service-B
    service-C-renamed
    service-D
    service-E
    service-F
    service-G

This shows that, except for service A, the same set of services are in up state after the database switch, and that the renaming of service C has been performed indeed. Note that the service C has not been restarted; there were no \"Service C starting\" or \"Service C stopping\" messages printed to [s6-rc-update]\'s standard output. Also note that, because service G is both in [test-database2] and [test-database3] and not in any dependency chain that involves modified or restarted services, it is left alone by [s6-rc-update] and remains in up state during the database switch.

One more example with another set of service definitions:

`user `[`$`]`ls -l srv-src5/*`

    lrwxrwxrwx 1 user user   21 Apr 14 12:00 srv-src5/service-B-renamed -> ../srv-src4/service-B
    lrwxrwxrwx 1 user user   21 Apr 14 12:00 srv-src5/service-C-renamed -> ../srv-src3/service-C
    lrwxrwxrwx 1 user user   21 Apr 14 12:00 srv-src5/service-E -> ../srv-src4/service-E
    lrwxrwxrwx 1 user user   21 Apr 14 12:00 srv-src5/service-F -> ../srv-src3/service-F
    lrwxrwxrwx 1 user user   21 Apr 14 12:00 srv-src5/service-G -> ../srv-src3/service-G

    srv-src5/service-D:
    total 4
    -rw-r--r-- 1 user user 46 Apr 14 12:00 dependencies
    lrwxrwxrwx 1 user user 31 Apr 14 12:00 finish -> ../../srv-src3/service-D/finish
    lrwxrwxrwx 1 user user 28 Apr 14 12:00 run -> ../../srv-src3/service-D/run
    lrwxrwxrwx 1 user user 29 Apr 14 12:00 type -> ../../srv-src3/service-D/type

    srv-src5/service-H:
    total 12
    -rw-r--r-- 1 user user 44 Apr 14 12:00 finish
    -rw-r--r-- 1 user user 85 Apr 14 12:00 run
    -rw-r--r-- 1 user user  8 Apr 14 12:00 type

Service B is is going to be renamed, and a new service H is going to be created as a dependency of service D:

[FILE] **`srv-src5/service-D/dependencies`**

    service-B-renamed
    service-C-renamed
    service-H

Service H is a longrun with no dependencies that runs program [test-daemon] with readiness notification turned off:

[FILE] **`srv-src5/service-H/type`**

    longrun

[FILE] **`srv-src5/service-H/run`**

    #!/bin/execlineb -P
    foreground
    fdmove -c 2 1
    test-daemon

[FILE] **`srv-src5/service-H/finish`**

    #!/bin/execlineb -P
    echo Service H stopping

Conversion file for renaming service B that also forces a restart of service G (which is otherwise unmodified):

[FILE] **`conversion-file2`**

    service-B -> service-B-renamed
    service-G restart

Compiling a new database with these service definitions using a [s6-rc-compile -u \$(id -u) test-database4 srv-src5] command, assuming it will also be placed in [/home/user] along with the conversion file, forcing another rotation of the supervision tree\'s logging directory, and then performing the database switch:

`user `[`$`]`time s6-rc-update -l /home/user/live -f ../conversion-file2 /home/user/test-database4`

    real  0m0.127s
    user    0m0.007s
    sys 0m0.007s

`user `[`$`]`cat ../logdir/current | s6-tai64nlocal`

    2018-04-16 12:23:07.375107786 Service G stopping
    2018-04-16 12:23:07.376383751 Service D stopping
    2018-04-16 12:23:07.478780248 Service H starting
    2018-04-16 12:23:07.479606503 Service G starting
    2018-04-16 12:23:07.496890435 Service D starting

This shows that service G was restarted indeed because of the conversion file, but also service D, because it was in up state before the database switch and its dependencies changed after the switch: service H was added as a direct dependency. On the other hand, service B was only renamed, so it didn\'t restart. The whole operation took place almost instantly, because not waiting for readiness notification makes service D\'s, G\'s and H\'s transitions almost instant.

`user `[`$`]`ls -l ../live`

    lrwxrwxrwx 1 user user 24 Apr 16 12:23 ../live -> live:s6-rc-update:5RCX6s

This shows that the live state directory symlink was modified once again; the output of [ls] previously showed [live:s6-rc-update:SGBH3e]

`user `[`$`]`ls -l`

    total 12
    drwxr-xr-x 4 user user 4096 Apr 16 12:00 logger
    lrwxrwxrwx 1 user user   41 Apr 16 12:23 s6rc-fdholder -> /home/user/live/servicedirs/s6rc-fdholder
    lrwxrwxrwx 1 user user   47 Apr 16 12:23 s6rc-oneshot-runner -> /home/user/live/servicedirs/s6rc-oneshot-runner
    lrwxrwxrwx 1 user user   45 Apr 16 12:23 service-B-renamed -> /home/user/live/servicedirs/service-B-renamed
    lrwxrwxrwx 1 user user   37 Apr 16 12:23 service-D -> /home/user/live/servicedirs/service-D
    lrwxrwxrwx 1 user user   37 Apr 16 12:23 service-G -> /home/user/live/servicedirs/service-G
    lrwxrwxrwx 1 user user   37 Apr 16 12:23 service-H -> /home/user/live/servicedirs/service-H

This shows that the symlink for service B in the s6 scan directory was renamed, and that a new symlink was created for service H.

`user `[`$`]`s6-rc -ual ../live list | sort`

    s6rc-oneshot-runner
    service-B-renamed
    service-C-renamed
    service-D
    service-E
    service-F
    service-G
    service-H

This shows again that the same set of services are in up state after the database switch, and that the renaming of service B has been performed indeed. Adding two runlevel-like bundles to the compiled service database while it is live:

`user `[`$`]`s6-rc-db -l ../live list bundles`

`user `[`$`]`execlineb -Pc 's6-rc-bundle -l ../live multiple  runlevel-X  runlevel-Y '`

`user `[`$`]`s6-rc-db -l ../live list bundles | sort`

    runlevel-X
    runlevel-Y

This shows that both bundles were simultaneously added. It is equivalent to using an [s6-rc-bundle -l ../live add runlevel-X service-D] command followed by an [s6-rc-bundle -l ../live add runlevel-Y service-F service-G] command. Forcing another rotation of the supervision tree\'s logging directory, and then using an [s6-rc -pu change] command to emulate a runlevel change:

`user `[`$`]`s6-rc -pul ../live change runlevel-X | s6-tai64nlocal`

    2018-04-16 12:26:08.604157313 Service F stopping
    2018-04-16 12:26:18.632999649 Service E stopping

`user `[`$`]`cat ../logdir/current | s6-tai64nlocal`

    2018-04-16 12:26:08.603648681 Service G stopping

`user `[`$`]`s6-rc -ual ../live list | sort`

    s6rc-oneshot-runner
    service-B-renamed
    service-C-renamed
    service-D
    service-H

This shows that only atomic services that are members of bundle *runlevel-X*, and their dependencies, are now up. Deleting the bundle from the compiled service database:

`user `[`$`]`s6-rc-bundle -l ../live delete runlevel-X`

`user `[`$`]`s6-rc-db -l ../live list bundles`

    runlevel-Y

This shows that only bundle *runlevel-Y* remains. It is equivalent to using an [execlineb -Pc \'s6-rc-bundle -l ../live multiple \'] command. Performing another \'runlevel change\':

`user `[`$`]`s6-rc -pul ../live change runlevel-Y | s6-tai64nlocal`

    2018-04-16 12:29:39.558335051 Service C stopping
    2018-04-16 12:29:39.569330382 Service E starting
    2018-04-16 12:29:39.576582824 Service F starting

`user `[`$`]`cat ../logdir/current | s6-tai64nlocal`

    2018-04-16 12:26:08.603648681 Service G stopping
    2018-04-16 12:29:39.552344150 Service D stopping
    2018-04-16 12:29:39.559029637 Service B stopping
    2018-04-16 12:29:39.561047890 Service H stopping
    2018-04-16 12:29:39.569014150 Service G starting

`user `[`$`]`s6-rc -ual ../live list | sort`

    s6rc-oneshot-runner
    service-E
    service-F
    service-G

This shows that atomic services that were members of (former) bundle *runlevel-X* were stopped, and only atomic services that are members of bundle *runlevel-Y*, and their dependencies, are now up. []

### [Longrun pipelining]

The s6 supervision tools support the [daemontools mechanism](https://wiki.gentoo.org/wiki/Daemontools-encore#logging "Daemontools-encore") that allows connecting the standard output of a supervised process to the standard input of another one with a pipe, normally for logging purposes. This mechanism is used when a subdirectory or symbolic link to directory named [log] is present in a service directory. s6-rc generalizes this idea with *pipelines*: it allows arbirary length chains of longruns that have their standard output connected to the standard input of the next one in the chain with a pipe. Moreover, as of version 0.4.0.0, s6-rc also allows tying the standard input of a longrun with the standard output of two or more other longruns, so that multiple streams of messages from different supervised processes can be collapsed into a single stream. This means that s6-rc pipelines are really *funnels*, but the name \'pipeline\' is retained for compatibility with earlier versions that did not support this feature.

The [s6-rc-compile] program creates pipelines when the definition directories of their member services contain regular files named [producer-for] and [consumer-for]. A [producer-for] file must contain a single service name; the standard output of the service being defined will then be connected to the standard input of the service named in the file as a result. s6-rc requires that the definition directory of the latter also contain a [consumer-for] file that names the former, and [s6-rc-compile] implicitly makes the latter a direct dependency of the former, as if by the presence a [dependencies] file. This ensures that if the pipeline mechanism is used for logging, loggers will be up before starting the \'main\' services. A [consumer-for] file must contain a list of service names. If more that one service is named in a [consumer-for] file, the funnel-style collapsing of message streams will take place. Pipeline consistency, e.g. absence of collisions or cycles, is verified by [s6-rc-compile] at service database creation time, as well as the existence of a [consumer-for] file in the definition of each service named in a [producer-for] file, and a [producer-for] file in the definition of each service named in a [consumer-for] file. To create [a logging chain](https://wiki.gentoo.org/wiki/S6#loggingchain "S6") with s6-rc services, definitions of \'main\' services must contain a [producer-for] file naming their loggers, and the loggers must be created just like any other s6-rc longrun, with definition directories that contain a [consumer-for] file naming (only) their main services.

The definition directory of a service with a [consumer-for] file and no [producer-for] file, named the corresponding pipeline\'s *last consumer*, can also contain an optional, regular file named [pipeline-name], that must contain a single service name; [s6-rc-compile] will then create a service bundle with this name that contains all the services that are members of the pipeline. A [pipeline-name] in the definition directory of a service that is not a pipeline\'s last consumer is ignored. For further information about pipelines, please consult [s6-rc-compile]\'s HTML documentation in the package\'s [/usr/share/doc] subdirectory.

s6-rc implements pipelines using an internal support service named **s6rc-fdholder**. This service spawns a long-lived process that executes the [s6-fdholderd] program, i.e. [the fd-holder daemon from s6](https://wiki.gentoo.org/wiki/S6/File_descriptor_holder#fdholder "S6/File descriptor holder"), and runs an internal s6-rc program, [s6-rc-fdholder-filler], chained from [s6-ipcclient]. [s6-rc-fdholder-filler] is a short-lived [UCSPI IPC client](https://wiki.gentoo.org/wiki/S6/UNIX_domain_super-server#ipcserverd "S6/UNIX domain super-server"), that reads a file containing service names, creates a pipe for each of them using the POSIX `pipe()` call, connects to the socket of an [s6-fdholderd] process, and transfers the file descriptors associated with the reading and writing end of all pipes to the server with a set dump operation, i.e. as if by [s6-fdholder-setdumpc]. The file with service names is created by [s6-rc-compile] in [s6rc-fdholder]\'s s6 service directory. [s6-rc-compile] also automatically makes [s6rc-fdholder] a direct dependency of every longrun that is a member of a pipeline, and creates a wrapper [run] execline script in their compiled s6 service directory. The wrapper script retrieves the file descriptors that correspond to the reading and / or writing ends of the pipes the service needs with [s6-fdholder-retrieve] invocations, and then executes the actual [run] file supplied in its s6-rc definition (currently installed as [run.user] in the compiled s6 service directory). The same happens with the [finish] file, if there is one. For further information about [s6-rc-fdholder-filler], please consult the HTML documentation in the package\'s [/usr/share/doc] subdirectory.

[s6rc-fdholder] uses a rules directory to decide whether to grant or refuse service to clients that connect to its UNIX domain socket. The effective user of all processes in an s6 supervision tree is initially that of [s6-svscan]. The [s6-supervise] process of every longrun that is a member of a pipeline will spawn a child process that executes the wrapper [run] execline script with the [s6-fdholder-retrieve] invocations, so [s6-svscan]\'s effective user must be allowed by [s6rc-fdholder]\'s rules directory. Setup of this rules directory can be done using [s6-rc-compile]\'s `-u` and `-g` options, see [initializing s6-rc](#initialization). If [s6-svscan]\'s effective user is root, the effective user of the [s6-fdholderd] process can be adjusted by passing an `-h` option to [s6-rc-compile] followed by an account\'s username; [s6rc-fdholder]\'s [run] script will then include an [s6-envuidgid] invocation to drop privileges accordingly. For further information about [s6-rc-compile], please consult the HTML documentation in the package\'s [/usr/share/doc] subdirectory.

Finally, the [s6-rc-db] program (see [extracting information from a compiled database](#s6rcdb)) has a **pipeline** subcommand that accepts a service name argument. If the corresponding service is a member of a pipeline, it displays information about it, otherwise, it just prints the supplied name. For further information about [s6-rc-db], please consult the HTML documentation in the package\'s [/usr/share/doc] subdirectory.

Example set of service definitions using pipelines:

`user `[`$`]`ls -l srv-src6/*`

    srv-src6/final-logger:
    total 16
    -rw-r--r-- 1 user user  18 Apr 18 12:00 consumer-for
    -rw-r--r-- 1 user user  20 Apr 18 12:00 pipeline-name
    -rw-r--r-- 1 user user 130 Apr 18 12:00 run
    -rw-r--r-- 1 user user   8 Apr 18 12:00 type

    srv-src6/reader-A:
    total 16
    -rw-r--r-- 1 user user  10 Apr 18 12:00 consumer-for
    -rw-r--r-- 1 user user  13 Apr 18 12:00 producer-for
    -rw-r--r-- 1 user user 115 Apr 18 12:00 run
    -rw-r--r-- 1 user user   8 Apr 18 12:00 type

    srv-src6/reader-B:
    total 16
    -rw-r--r-- 1 user user  10 Apr 18 12:00 consumer-for
    -rw-r--r-- 1 user user  13 Apr 18 12:00 producer-for
    -rw-r--r-- 1 user user 115 Apr 18 12:00 run
    -rw-r--r-- 1 user user   8 Apr 18 12:00 type

    srv-src6/service-A:
    total 12
    -rw-r--r-- 1 user user  9 Apr 18 12:00 producer-for
    -rw-r--r-- 1 user user 32 Apr 18 12:00 run
    -rw-r--r-- 1 user user  8 Apr 18 12:00 type

    srv-src6/service-B:
    total 12
    -rw-r--r-- 1 user user  9 Apr 18 12:00 producer-for
    -rw-r--r-- 1 user user 32 Apr 18 12:00 run
    -rw-r--r-- 1 user user  8 Apr 18 12:00 type

Service A spawns a process that executes a hypothetical [test-daemon] program. It is assumed that this program prints a message of the form \"Message #N\", where *N* is an incrementing number, each time it receives a `SIGHUP` signal.

[FILE] **`srv-src6/service-A/type`**

    longrun

[FILE] **`srv-src6/service-A/run`**

    #!/bin/execlineb -P
    test-daemon

[FILE] **`srv-src6/service-A/producer-for`**

    reader-A

Reader A spawns a process that reads lines of text from its standard input and prints them to its standard output, prepended with the string \"This comes from service A:\":

[FILE] **`srv-src6/reader-A/type`**

    longrun

[FILE] **`srv-src6/reader-A/run`**

    #!/usr/bin/python3
    import sys
    for line in sys.stdin: print ('This comes from service A:', line, end='', flush=True)

[FILE] **`srv-src6/reader-A/consumer-for`**

    service-A

Service A\'s standard ouput will be connected to reader A\'s standard input with a pipe. Service B and reader B constitute a similar pair of services:

[FILE] **`srv-src6/service-B/type`**

    longrun

[FILE] **`srv-src6/service-B/run`**

    #!/bin/execlineb -P
    test-daemon

[FILE] **`srv-src6/service-B/producer-for`**

    reader-B

[FILE] **`srv-src6/reader-B/type`**

    longrun

[FILE] **`srv-src6/reader-B/run`**

    #!/usr/bin/python3
    import sys
    for line in sys.stdin: print ('This comes from service B:', line, end='', flush=True)

[FILE] **`srv-src6/reader-B/consumer-for`**

    service-B

And finally, service *final-reader* spawns an [s6-log] process. Messages read from its standard input are logged in logging directory [/home/user/logdir]:

[FILE] **`srv-src6/final-logger/type`**

    longrun

[FILE] **`srv-src6/final-logger/run`**

    #!/bin/execlineb -P
    redirfd -w 1 /dev/null
    foreground
    s6-log /home/user/logdir

The s6-rc pipeline ties reader A\'s and B\'s standard output with this logger\'s standard input:

[FILE] **`srv-src6/reader-A/producer-for`**

    final-logger

[FILE] **`srv-src6/reader-B/producer-for`**

    final-logger

[FILE] **`srv-src6/final-logger/consumer-for`**

    reader-A
    reader-B

[final-logger] is the pipeline\'s last consumer, so it has a [pipeline-name] file that specifies a name for the pipeline:

[FILE] **`srv-src6/final-logger/pipeline-name`**

    service-AB-pipeline

A diagram that represents this pipeline:

    service A --> reader A -->+
                              |
    service B --> reader B -->+
                              |
                              +--> final-logger

After creating a database with these service definitions using a [s6-rc-compile -u \$(id -u) test-database5 srv-src6] command:

`user `[`$`]`s6-rc-db -c test-database5 list all | sort`

    final-logger
    reader-A
    reader-B
    s6rc-fdholder
    s6rc-oneshot-runner
    service-A
    service-AB-pipeline
    service-B

`user `[`$`]`s6-rc-db -c test-database5 type service-AB-pipeline`

    bundle

This shows that the database contains an actual service named *service-AB-pipeline*, and that it is a bundle. [s6-rc-compile] must be invoked with an `-u` option so that the nonprivileged effective user of each longrun\'s process is allowed to retrieve the file descriptors associated with this pipeline from the fd-holder.

`user `[`$`]`s6-rc-db -c test-database5 contents service-AB-pipeline | sort`

    final-logger
    reader-A
    reader-B
    service-A
    service-B

This shows that the bundle contains all services associated this pipeline.

`user `[`$`]`for i in - final-logger`

    > do echo $i:
    > s6-rc-db -c test-database5 dependencies $i
    > echo
    > done
    service-A:
    reader-A
    s6rc-fdholder

    service-B:
    reader-B
    s6rc-fdholder

    reader-A:
    final-logger
    s6rc-fdholder

    reader-B:
    final-logger
    s6rc-fdholder

    final-logger:
    s6rc-fdholder

This shows that [s6-rc-compile] made [s6rc-fdholder] a direct dependency of all members of the pipeline and made each service associated with the writing end of a pipe a dependency of the service associated with the corresponding reading end.

Starting all the services after launching an s6 supervision tree and initializing s6-rc, assuming that the working directory is the scan directory and that [../live] is the relative pathname of the live state directory:

`user `[`$`]`s6-rc -ul ../live change service-AB-pipeline`

`user `[`$`]`ps xf -o pid,ppid,pgrp,euser,args`

     PID  PPID  PGRP EUSER    COMMAND
    ...
    2128  2121  2128 user     -bash
    2473  2128  2473 user      \_ s6-svscan
    2477  2473  2473 user          \_ s6-supervise reader-A
    2506  2477  2506 user          |   \_ /usr/lib/python-exec/python3.6/python3 ./run.user
    2478  2473  2473 user          \_ s6-supervise service-B
    2511  2478  2511 user          |   \_ test-daemon
    2479  2473  2473 user          \_ s6-supervise s6rc-oneshot-runner
    2480  2473  2473 user          \_ s6-supervise service-A
    2515  2480  2515 user          |   \_ test-daemon
    2481  2473  2473 user          \_ s6-supervise s6rc-fdholder
    2489  2481  2489 user          |   \_ s6-fdholderd -1 -i data/rules
    2482  2473  2473 user          \_ s6-supervise reader-B
    2505  2482  2505 user          |   \_ /usr/lib/python-exec/python3.6/python3 ./run.user
    2483  2473  2473 user          \_ s6-supervise final-logger
    2498  2483  2498 user              \_ s6-log /home/user/logdir
    ...

This shows that all services in the pipeline are now in up state, including [s6rc-fdholder], which is a supervised [s6-fdholderd] process. Sending a few `SIGHUP` signals to the [test-daemon] processes that correspond to services A and B:

`user `[`$`]`for i in A A B B A B B A`

    >do
    >s6-svc -h service-$i
    >done

`user `[`$`]`cat /home/user/logdir/current`

    This comes from service A: Message #1
    This comes from service A: Message #2
    This comes from service B: Message #1
    This comes from service B: Message #2
    This comes from service A: Message #3
    This comes from service B: Message #3
    This comes from service B: Message #4
    This comes from service A: Message #4

This shows that all messages passed through the pipeline and got logged in the logging directory. Using [s6-rc-db] to display information about the pipeline:

`user `[`$`]`s6-rc-db -l ../live pipeline reader-B`

    service-B | reader-B
    reader-B | final-logger
    service-A | reader-A
    reader-A | final-logger

Reader B is a member of pipeline [service-AB-pipeline], so that is what is printed. []

### [s6-rc as an init system component]

s6-rc can be used as the service manager of [an init system based on s6](https://wiki.gentoo.org/wiki/S6_and_s6-rc-based_init_system "S6 and s6-rc-based init system"). Such an init system runs program [s6-svscan] from the s6 package as process 1 for most of the machine\'s uptime, and separate programs (usually execline scripts), the *stage1 init* and the *stage3 init*, during the boot and shutdown sequences, respectively. Therefore, process 1 is the root of an s6 supervision tree for most of the machine\'s uptime, and has an associated scan directory, usually in a read-write tmpfs. s6-rc uses this supervision tree and a compiled service database, the *boot-time service database*, that must be available during the machine\'s boot sequence, usually in the rootfs.

Because s6-rc must be initialized using the [s6-rc-init] program (see [initializing s6-rc](#initialization)) when the [s6-svscan] process is already running, this takes place in the *stage2 init*, a program (usually an execline or shell script) that is launched by the stage1 init and blocks until the init system\'s catch-all logger is started. The s6-rc live state database is usually created in the same read-write tmpfs that is used for the init system\'s scan directory. The tmpfs is customarily mounted on [/run], and the live state directory is left to be [/run/s6-rc], s6-rc\'s default, so that no `-l` options have to be specified each time to s6-rc tools. After initializing s6-rc, atomic services (oneshots and longruns) that are needed to complete the machine\'s initialization, and longruns that are wanted in up state at the end of the boot sequence, must be started. This is customarily done by defining a service bundle that contains all those services, and starting it in the stage2 init with an [s6-rc -u change] command naming that bundle.

The boot-time service database becomes live during the machine\'s boot sequence, so any service modification must be generally performed by creating a new database using [s6-rc-compile], and then replacing the currently live one with this database using the [s6-rc-update] program (see [live updates to the service database](#s6rcupdate)). If during the machine\'s uptime the s6-rc package is upgraded to a backwards-incompatible version, the current live database must be recompiled after the package upgrade using the same service definitions in [s6-rc-compile]\'s source format, and the [s6-rc-format-upgrade] program must be used to switch databases.

Here is a summary of possible ways of performing modifications to s6-rc-managed services after boot:

-   Bundle modifications can be performed directly on the live database using [s6-rc-bundle], without requiring a database switch, and these changes are \'sticky\' (i.e. are preserved across machine reboots).
-   Longrun file modifications *could* be performed directly in the copy of their compiled s6 service directory (including modifications of the contents of their [env] and [data] subdirectories, if present) using the corresponding symlink in the init system\'s scan directory, but this is a non-atomic operation that can have issues if the corresponding supervised process terminates and gets restarted by its supervisor in the middle of the directory update ^[\[2\]](#cite_note-2)^. Also, changes done this way are not \'sticky\', because the service directory would be restored to the contents of the boot-time service database on the next reboot, so this is generally discouraged.
-   Supporting files of oneshots (e.g. external scripts invoked from an [up] or [down] file) must be generally referred to by absolute pathname, can be modified in their corresponding locations, and these changes are \'sticky\'.
-   Any other modification must generally be done using [s6-rc-update] with a new compiled service database; changes are \'sticky\' this way and safe.

Finally, before [s6-svscan] replaces itself with the stage3 init during the shutdown sequence, all s6-rc-managed services must be stopped, usually with an [s6-rc -da change] command. This takes place in an an execline or shell script, the *shutdown script*, that is invoked from an [s6-svscan] [diverted signal handler](https://wiki.gentoo.org/wiki/S6_and_s6-rc-based_init_system#signals "S6 and s6-rc-based init system").

## [Removal]

### [Unmerge]

`root `[`#`]`emerge --ask --depclean --verbose sys-apps/s6-rc`

All live state directories, compiled service databases and service definitions in [s6-rc-compile]\'s source format must be manually deleted if no longer wanted after removing the package. And obviously, if s6-rc is being used as an init system component, an alternative init system must be installed in parallel, and the machine rebooted to use it (possibly by reconfiguring the [bootloader](https://wiki.gentoo.org/wiki/Bootloader "Bootloader")), before the package is removed, or otherwise the machine will become unbootable.

## [See also]

-   [OpenRC](https://wiki.gentoo.org/wiki/OpenRC "OpenRC") --- a dependency-based [init system](https://en.wikipedia.org/wiki/Init "wikipedia:Init") for Unix-like systems that maintains compatibility with the system-provided [init system](https://wiki.gentoo.org/wiki/Init_system "Init system")
-   [Systemd](https://wiki.gentoo.org/wiki/Systemd "Systemd") --- a modern SysV-style init and [[rc](https://wiki.gentoo.org/wiki/Rc "Rc")] replacement for Linux systems.

## [References]

1.  [[[↑](#cite_ref-1)] [Laurent Bercot, [On upgrading from s6-rc version 0.3.0.1 to version 0.4.0.0](https://skarnet.org/cgi-bin/archive.cgi?2:mss:1973:201805:omimnjmkdciaebibmpkp), May 20th, 2018.]]
2.  [[[↑](#cite_ref-2)] [Laurent Bercot, [On updating a live service directory](https://www.skarnet.org/cgi-bin/archive.cgi?2:mss:1871:201710:nadggnhoigbpknlffnni), October 29th, 2017.]]