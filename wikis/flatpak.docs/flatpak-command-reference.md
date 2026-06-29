# Flatpak Command Reference

Version 1.17.0

### Important

The command reference is generated from the flatpak repo; see [https://github.com/flatpak/flatpak/tree/main/doc](https://github.com/flatpak/flatpak/tree/main/doc)

Flatpak comes with a rich commandline interface.

**Table of Contents**

[Executables](#id1338)

[flatpak](#flatpak) — Build, install and run applications and runtimes

[Commands](#id1339)

[flatpak build-bundle](#flatpak-build-bundle) — Create a single-file bundle from a local repository

[flatpak build-commit-from](#flatpak-build-commit-from) — Create new commits based on existing one (possibly from another repository)

[flatpak build-export](#flatpak-build-export) — Create a repository from a build directory

[flatpak build-finish](#flatpak-build-finish) — Finalize a build directory

[flatpak build-import-bundle](#flatpak-build-import-bundle) — Import a file bundle into a local repository

[flatpak build-init](#flatpak-build-init) — Initialize a build directory

[flatpak build-sign](#flatpak-build-sign) — Sign an application or runtime

[flatpak build-update-repo](#flatpak-build-update-repo) — Create a repository from a build directory

[flatpak build](#flatpak-build) — Build in a directory

[flatpak config](#flatpak-config) — Manage configuration

[flatpak create-usb](#flatpak-create-usb) — Copy apps and/or runtimes onto removable media.

[flatpak document-export](#flatpak-document-export) — Export a file to a sandboxed application

[flatpak document-info](#flatpak-document-info) — Show information about exported files

[flatpak documents](#flatpak-documents) — List exported files

[flatpak document-unexport](#flatpak-document-unexport) — Stop exporting a file

[flatpak enter](#flatpak-enter) — Enter an application or runtime's sandbox

[flatpak history](#flatpak-history) — Show history

[flatpak info](#flatpak-info) — Show information about an installed application or runtime

[flatpak install](#flatpak-install) — Install an application or runtime

[flatpak kill](#flatpak-kill) — Stop a running application

[flatpak list](#flatpak-list) — List installed applications and/or runtimes

[flatpak make-current](#flatpak-make-current) — Make a specific version of an app current

[flatpak override](#flatpak-override) — Override application requirements

[flatpak permission-remove](#flatpak-permission-remove) — Remove permissions

[flatpak permissions](#flatpak-permissions) — List permissions

[flatpak permission-show](#flatpak-permission-show) — Show permissions

[flatpak permission-reset](#flatpak-permission-reset) — Reset permissions

[flatpak permission-set](#flatpak-permission-set) — Set permissions

[flatpak preinstall](#flatpak-preinstall) — Install flatpaks that are part of the operating system

[flatpak ps](#flatpak-ps) — Enumerate running instances

[flatpak remote-add](#flatpak-remote-add) — Add a remote repository

[flatpak remote-delete](#flatpak-remote-delete) — Delete a remote repository

[flatpak remote-info](#flatpak-remote-info) — Show information about an application or runtime in a remote

[flatpak remote-ls](#flatpak-remote-ls) — Show available runtimes and applications

[flatpak remote-modify](#flatpak-remote-modify) — Modify a remote repository

[flatpak remotes](#flatpak-remotes) — List remote repositories

[flatpak repair](#flatpak-repair) — Repair a flatpak installation

[flatpak repo](#flatpak-repo) — Show information about a local repository

[flatpak run](#flatpak-run) — Run an application or open a shell in a runtime

[flatpak search](#flatpak-search) — Search for applications and runtimes

[flatpak uninstall](#flatpak-uninstall) — Uninstall an application or runtime

[flatpak update](#flatpak-update) — Update an application or runtime

[flatpak spawn](#flatpak-spawn) — Run commands in a sandbox

[File Formats](#id1340)

[flatpakrepo](#flatpakrepo) — Reference to a remote

[flatpakref](#flatpakref) — Reference to a remote for an application or runtime

[flatpak installation](#flatpak-installation) — Configuration for an installation location

[flatpak metadata](#flatpak-metadata) — Information about an application or runtime

[flatpak remote](#flatpak-remote) — Configuration for a remote

## Executables

**Table of Contents**

[flatpak](#flatpak) — Build, install and run applications and runtimes

## Name

flatpak — Build, install and run applications and runtimes

## Synopsis

`flatpak` \[OPTION...\] {COMMAND}

## Description

Flatpak is a tool for managing applications and the runtimes they use. In the Flatpak model, applications can be built and distributed independently from the host system they are used on, and they are isolated from the host system ('sandboxed') to some degree, at runtime.

Flatpak can operate in system-wide or per-user mode. The system-wide data (runtimes, applications and configuration) is located in `$prefix/var/lib/flatpak/`, and the per-user data is in `$HOME/.local/share/flatpak/`. Below these locations, there is a local repository in the `repo/` subdirectory and installed runtimes and applications are in the corresponding `runtime/` and `app/` subdirectories.

System-wide remotes can be statically preconfigured by dropping [flatpakrepo(5)](#flatpakrepo) files into `/usr/share/flatpak/remotes.d/` and `/etc/flatpak/remotes.d/`. If a file with the same name exists in both, the file under `/etc` will take precedence.

In addition to the system-wide installation in `$prefix/var/lib/flatpak/`, which is always considered the default one unless overridden, more system-wide installations can be defined via configuration files in `/etc/flatpak/installations.d/`, which must define at least the id of the installation and the absolute path to it. Other optional parameters like DisplayName , Priority or StorageType are also supported.

Flatpak uses OSTree to distribute and deploy data. The repositories it uses are OSTree repositories and can be manipulated with the **ostree** utility. Installed runtimes and applications are OSTree checkouts.

Basic commands for building flatpaks such as build-init, build and build-finish are included in the flatpak utility. For higher-level build support, see the separate [flatpak-builder(1)](#flatpak-builder) tool.

Flatpak supports installing from sideload repos. These are partial copies of a repository (generated by **flatpak create-usb**) that are used as an installation source when offline (and online as a performance improvement). Such repositories are configured by creating symlinks to the sideload sources in the `sideload-repos` subdirectory of the installation directory (i.e. typically `/var/lib/flatpak/sideload-repos` or `~/.local/share/flatpak/sideload-repos`). Additionally symlinks can be created in `/run/flatpak/sideload-repos` which is a better location for non-persistent sources (as it is cleared on reboot). These symlinks can point to either the directory given to **flatpak create-usb** which by default writes to the subpath `.ostree/repo`, or directly to an ostree repo.

## Options

The following global options are understood. Individual commands have their own options.

`-h`, `--help`  
Show help options and exit.

`-v`, `--verbose`  
Show debug information during command processing. Use -vv for more detail.

`--ostree-verbose`  
Show OSTree debug information during command processing.

`--version`  
Print version information and exit.

`--default-arch`  
Print the default arch and exit.

`--supported-arches`  
Print the supported arches in priority order and exit.

`--gl-drivers`  
Print the list of active gl drivers and exit.

`--installations`  
Print paths of system installations and exit.

`--print-system-only`  
When the **flatpak --print-updated-env** command is run, only print the environment for system flatpak installations, not including the user’s home installation.

`--print-updated-env`  
Print the set of environment variables needed to use flatpaks, amending the current set of environment variables. This is intended to be used in a systemd environment generator, and should not need to be run manually.

## Commands

Commands for managing installed applications and runtimes:

[flatpak-install(1)](#flatpak-install)  
Install an application or a runtime from a remote or bundle.

[flatpak-update(1)](#flatpak-update)  
Update an installed application or runtime.

[flatpak-uninstall(1)](#flatpak-uninstall)  
Uninstall an installed application or runtime.

[flatpak-mask(1)](#flatpak-mask)  
Mask out updates and automatic installation.

[flatpak-pin(1)](#flatpak-pin)  
Pin runtimes to prevent automatic removal.

[flatpak-list(1)](#flatpak-list)  
List installed applications and/or runtimes.

[flatpak-info(1)](#flatpak-info)  
Show information for an installed application or runtime.

[flatpak-history(1)](#flatpak-history)  
Show history.

[flatpak-config(1)](#flatpak-config)  
Manage flatpak configuration.

[flatpak-repair(1)](#flatpak-repair)  
Repair flatpak installation.

[flatpak-create-usb(1)](#flatpak-create-usb)  
Copy apps and/or runtimes onto removable media.

Commands for finding applications and runtimes:

[flatpak-search(1)](#flatpak-search)  
Search for applications and runtimes.

Commands for managing running applications:

[flatpak-run(1)](#flatpak-run)  
Run an application.

[flatpak-kill(1)](#flatpak-kill)  
Stop a running application.

[flatpak-override(1)](#flatpak-override)  
Override permissions for an application.

[flatpak-make-current(1)](#flatpak-make-current)  
Specify the default version to run.

[flatpak-enter(1)](#flatpak-enter)  
Enter the namespace of a running application.

Commands for managing file access:

[flatpak-document-export(1)](#flatpak-document-export)  
Grant an application access to a specific file.

[flatpak-document-unexport(1)](#flatpak-document-unexport)  
Revoke access to a specific file.

[flatpak-document-info(1)](#flatpak-document-info)  
Show information about a specific file.

[flatpak-documents(1)](#flatpak-documents)  
List exported files.

Commands for managing the dynamic permission store:

[flatpak-permission-remove(1)](#flatpak-permission-remove)  
Remove item from permission store.

[flatpak-permissions(1)](#flatpak-permissions)  
List permissions.

[flatpak-permission-show(1)](#flatpak-permission-show)  
Show app permissions.

[flatpak-permission-reset(1)](#flatpak-permission-reset)  
Reset app permissions.

[flatpak-permission-set(1)](#flatpak-permission-set)  
Set app permissions.

Commands for managing remote repositories:

[flatpak-remotes(1)](#flatpak-remotes)  
List all configured remote repositories.

[flatpak-remote-add(1)](#flatpak-remote-add)  
Add a new remote repository.

[flatpak-remote-modify(1)](#flatpak-remote-modify)  
Modify properties of a configured remote repository.

[flatpak-remote-delete(1)](#flatpak-remote-delete)  
Delete a configured remote repository.

[flatpak-remote-ls(1)](#flatpak-remote-ls)  
List contents of a configured remote repository.

[flatpak-remote-info(1)](#flatpak-remote-info)  
Show information about a ref in a configured remote repository.

Commands for building applications:

[flatpak-build-init(1)](#flatpak-build-init)  
Initialize a build directory.

[flatpak-build(1)](#flatpak-build)  
Run a build command in a build directory.

[flatpak-build-finish(1)](#flatpak-build-finish)  
Finalizes a build directory for export.

[flatpak-build-export(1)](#flatpak-build-export)  
Export a build directory to a repository.

[flatpak-build-bundle(1)](#flatpak-build-bundle)  
Create a bundle file from a ref in a local repository.

[flatpak-build-import-bundle(1)](#flatpak-build-import-bundle)  
Import a file bundle into a local repository.

[flatpak-build-sign(1)](#flatpak-build-sign)  
Sign an application or runtime after its been exported.

[flatpak-build-update-repo(1)](#flatpak-build-update-repo)  
Update the summary file in a repository.

[flatpak-build-commit-from(1)](#flatpak-build-commit-from)  
Create a new commit based on an existing ref.

[flatpak-repo(1)](#flatpak-repo)  
Print information about a repo.

Commands available inside the sandbox:

[flatpak-spawn(1)](#flatpak-spawn)  
Run a command in another sandbox.

## File formats

File formats that are used by Flatpak commands:

[flatpakref(5)](#flatpakref)  
Reference to a remote for an application or runtime

[flatpakrepo(5)](#flatpakrepo)  
Reference to a remote

[flatpak-remote(5)](#flatpak-remote)  
Configuration for a remote

[flatpak-installation(5)](#flatpak-installation)  
Configuration for an installation location

[flatpak-metadata(5)](#flatpak-metadata)  
Information about an application or runtime

## Environment

Besides standard environment variables such as `XDG_DATA_DIRS` and `XDG_DATA_HOME`, flatpak consults some of its own.

`FLATPAK_BINARY`  
Path to the flatpak executable that will be written into exported `.desktop` files and scripts when an app is installed. The default is `/usr/bin/flatpak`, unless overridden at build time by `--bindir`.

`FLATPAK_BWRAP`  
Path to the [bwrap(1)](#bwrap) executable that will be used to create the sandbox. Depending on how Flatpak was configured at build-time, the default is either to search the `PATH`, or use a vendored copy which is normally installed as `/usr/libexec/flatpak-bwrap`.

`FLATPAK_CONFIG_DIR`  
The location of flatpak site configuration. If this is not set, `/etc/flatpak` is used (unless overridden at build time by --sysconfdir).

`FLATPAK_DATA_DIR`  
The location of Flatpak's OS-level defaults and integration hooks. If this is not set, `/usr/share/flatpak` is used, unless overridden at build time by `--datadir`.

`FLATPAK_DBUSPROXY`  
Path to the [xdg-dbus-proxy(1)](#xdg-dbus-proxy) executable that will be used to filter D-Bus traffic between the sandbox and the host system. Depending on how Flatpak was configured at build-time, the default is either to search the `PATH`, or use a vendored copy which is normally installed as `/usr/libexec/flatpak-dbus-proxy`.

`FLATPAK_DOWNLOAD_TMPDIR`  
Path to a directory that will be used temporarily when downloading OCI layers, and potentially for other downloads in future. The standard `TMPDIR` is not used for this, because Flatpak apps are frequently too large to fit on a tmpfs.

`FLATPAK_FANCY_OUTPUT`  
May be set to `0` to avoid fancy formatting when outputting to a terminal. This feature is also disabled automatically when standard output is not a terminal, or when `G_MESSAGES_DEBUG` is set.

`FLATPAK_FORCE_TEXT_AUTH`  
May be set to `1` to force use of a simple built-in [polkit(8)](#polkit) agent when authentication is required to modify the system-wide installation. By default, the desktop environment's polkit agent is used, if one is available, usually resulting in a graphical prompt.

`FLATPAK_GL_DRIVERS`  
A colon-separated list of graphics driver extensions to try to use for OpenGL, Vulkan and similar APIs, most-preferred first. The default is to select a graphics driver automatically. Values in this list match the last dot-separated component of the names of extensions with the `active-gl-driver` condition. Typical values are `default`, `mesa-git` or `nvidia-550-120` (replacing the version number by the major and minor version of the `nvidia` kernel module).

`FLATPAK_RUN_DIR`  
The location of flatpak runtime global files. If this is not set, `/run/flatpak` is used.

`FLATPAK_SYSTEM_CACHE_DIR`  
The location where temporary child repositories will be created during pulls into the system-wide installation. If this is not set, a directory in `/var/tmp/` is used. This is useful because it is more likely to be on the same filesystem as the system repository (thus increasing the chances for e.g. reflink copying), and we can avoid filling the user's home directory with temporary data.

`FLATPAK_SYSTEM_DIR`  
The location of the default system-wide installation. If this is not set, `/var/lib/flatpak` is used (unless overridden at build time by `--localstatedir` or `-Dsystem_install_dir`).

`FLATPAK_TTY_PROGRESS`  
May be set to `1` to enable reporting machine-readable progress to the terminal. This feature is not currently enabled by default because it uses the OSC 9;4 sequence, which some terminal emulators interpret as a popup notification.

`FLATPAK_USER_DIR`  
The location of the per-user installation. If this is not set, `$XDG_DATA_HOME/flatpak` is used.

## See also

[ostree(1)](#ostree), [ostree.repo(5)](#ostree.repo), [flatpak-remote(5)](#flatpak-remote), [flatpak-installation(5)](#flatpak-installation), [https://www.flatpak.org](https://www.flatpak.org)

## Commands

**Table of Contents**

[flatpak build-bundle](#flatpak-build-bundle) — Create a single-file bundle from a local repository

[flatpak build-commit-from](#flatpak-build-commit-from) — Create new commits based on existing one (possibly from another repository)

[flatpak build-export](#flatpak-build-export) — Create a repository from a build directory

[flatpak build-finish](#flatpak-build-finish) — Finalize a build directory

[flatpak build-import-bundle](#flatpak-build-import-bundle) — Import a file bundle into a local repository

[flatpak build-init](#flatpak-build-init) — Initialize a build directory

[flatpak build-sign](#flatpak-build-sign) — Sign an application or runtime

[flatpak build-update-repo](#flatpak-build-update-repo) — Create a repository from a build directory

[flatpak build](#flatpak-build) — Build in a directory

[flatpak config](#flatpak-config) — Manage configuration

[flatpak create-usb](#flatpak-create-usb) — Copy apps and/or runtimes onto removable media.

[flatpak document-export](#flatpak-document-export) — Export a file to a sandboxed application

[flatpak document-info](#flatpak-document-info) — Show information about exported files

[flatpak documents](#flatpak-documents) — List exported files

[flatpak document-unexport](#flatpak-document-unexport) — Stop exporting a file

[flatpak enter](#flatpak-enter) — Enter an application or runtime's sandbox

[flatpak history](#flatpak-history) — Show history

[flatpak info](#flatpak-info) — Show information about an installed application or runtime

[flatpak install](#flatpak-install) — Install an application or runtime

[flatpak kill](#flatpak-kill) — Stop a running application

[flatpak list](#flatpak-list) — List installed applications and/or runtimes

[flatpak make-current](#flatpak-make-current) — Make a specific version of an app current

[flatpak override](#flatpak-override) — Override application requirements

[flatpak permission-remove](#flatpak-permission-remove) — Remove permissions

[flatpak permissions](#flatpak-permissions) — List permissions

[flatpak permission-show](#flatpak-permission-show) — Show permissions

[flatpak permission-reset](#flatpak-permission-reset) — Reset permissions

[flatpak permission-set](#flatpak-permission-set) — Set permissions

[flatpak preinstall](#flatpak-preinstall) — Install flatpaks that are part of the operating system

[flatpak ps](#flatpak-ps) — Enumerate running instances

[flatpak remote-add](#flatpak-remote-add) — Add a remote repository

[flatpak remote-delete](#flatpak-remote-delete) — Delete a remote repository

[flatpak remote-info](#flatpak-remote-info) — Show information about an application or runtime in a remote

[flatpak remote-ls](#flatpak-remote-ls) — Show available runtimes and applications

[flatpak remote-modify](#flatpak-remote-modify) — Modify a remote repository

[flatpak remotes](#flatpak-remotes) — List remote repositories

[flatpak repair](#flatpak-repair) — Repair a flatpak installation

[flatpak repo](#flatpak-repo) — Show information about a local repository

[flatpak run](#flatpak-run) — Run an application or open a shell in a runtime

[flatpak search](#flatpak-search) — Search for applications and runtimes

[flatpak uninstall](#flatpak-uninstall) — Uninstall an application or runtime

[flatpak update](#flatpak-update) — Update an application or runtime

[flatpak spawn](#flatpak-spawn) — Run commands in a sandbox

## Name

flatpak-build-bundle — Create a single-file bundle from a local repository

## Synopsis

`flatpak build-bundle` \[OPTION...\] LOCATION FILENAME NAME \[BRANCH\]

## Description

Creates a single-file named FILENAME for the application (or runtime) named NAME in the repository at LOCATION . If a BRANCH is specified, this branch of the application is used.

The collection ID set on the repository at LOCATION (if set) will be used for the bundle.

Unless `--oci` is used, the format of the bundle file is that of an ostree static delta (against an empty base) with some flatpak specific metadata for the application icons and appdata.

## Options

The following options are understood:

`-h`, `--help`  
Show help options and exit.

`--runtime`  
Export a runtime instead of an application.

`--arch=ARCH`  
The arch to create a bundle for. See **flatpak --supported-arches** for architectures supported by the host.

`--repo-url=URL`  
The URL for the repository from which the application can be updated. Installing the bundle will automatically configure a remote for this URL.

`--runtime-repo=URL`  
The URL for a `.flatpakrepo` file that contains the information about the repository that supplies the runtimes required by the app.

`--gpg-keys=FILE`  
Add the GPG key from FILE (use - for stdin).

`--gpg-homedir=PATH`  
GPG Homedir to use when looking for keyrings.

`--from-commit=COMMIT`  
The OSTree commit to create a delta bundle from.

`--oci`  
Export to an OCI image instead of a Flatpak bundle.

`-v`, `--verbose`  
Print debug information during command processing.

`--ostree-verbose`  
Print OSTree debug information during command processing.

## Examples

**\$ flatpak build-bundle /var/lib/flatpak/repo gnome-calculator.flatpak org.gnome.Calculator stable**

**\$ flatpak build-bundle ~/.local/share/flatpak/repo gnome-calculator.flatpak org.gnome.Calculator stable**

## See also

[ostree(1)](#ostree), [flatpak(1)](#flatpak), [flatpak-build-init(1)](#flatpak-build-init), [flatpak-build(1)](#flatpak-build), [flatpak-build-finish(1)](#flatpak-build-finish), [flatpak-build-import-bundle(1)](#flatpak-build-import-bundle), [flatpak-build-update-repo(1)](#flatpak-build-update-repo)

## Name

flatpak-build-commit-from — Create new commits based on existing one (possibly from another repository)

## Synopsis

`flatpak build-commit-from` \[OPTION...\] DST-REPO DST-REF...

## Description

Creates new commits on the DST-REF branch in the DST-REPO , with the contents (and most of the metadata) taken from another branch, either from another repo, or from another branch in the same repository.

The collection ID set on DST-REPO (if set) will be used for the newly created commits.

This command is very useful when you want to maintain a branch with a clean history that has no unsigned or broken commits. For instance, you can import the head from a different repository from an automatic builder when you've verified that it worked. The new commit will have no parents or signatures from the autobuilder, and can be properly signed with the official key.

Any deltas that affect the original commit and that match parent commits in the destination repository are copied and rewritten for the new commit id.

## Options

The following options are understood:

`-h`, `--help`  
Show help options and exit.

`--src-repo=SRC-REPO`  
The (local) repository to pull the source branch from. Defaults to the destination repository.

`--src-ref=SRC-REF`  
The branch to use as the source for the new commit. Defaults to the same as the destination ref, which is useful only if a different source repo has been specified.

`--extra-collection-id=COLLECTION-ID`  
Add an extra collection-ref binding for this collection, in addition to whatever would normally be added due to the destination repository collection id. This option can be used multiple times.

`--subset=SUBSET`  
Mark the commit to be included in the named subset. This will cause the commit to be put in the named subset summary (in addition to the main one), allowing users to see only this subset instead of the whole repo.

`--untrusted`  
The source repostory is not trusted, all objects are copied (not hardlinked) and all checksums are verified.

`-s`, `--subject=SUBJECT`  
One line subject for the commit message. If not specified, will be taken from the source commit.

`-b`, `--body=BODY`  
Full description for the commit message. If not specified, will be taken from the source commit.

`--update-appstream`  
Update the appstream branch after the build.

`--no-update-summary`  
Don't update the summary file after the new commit is added. This means the repository will not be useful for serving over http until build-update-repo has been run. This is useful is you want to do multiple repo operations before finally updating the summary.

`--force`  
Create new commit even if the content didn't change from the existing branch head.

`--disable-fsync`  
Don't fsync when writing to the repository. This can result in data loss in exceptional situations, but can improve performance when working with temporary or test repositories.

`--gpg-sign=KEYID`  
Sign the commit with this GPG key. This option can be used multiple times.

`--gpg-homedir=PATH`  
GPG Homedir to use when looking for keyrings

`--end-of-life=REASON`  
Mark build as end-of-life

`--end-of-life-rebase=OLDID=NEWID`  
Mark new refs as end-of-life. Unlike `--end-of-life`, this one takes an ID that supersedes the current one. By the user's request, the application data may be preserved for the new application. Note, this is actually a prefix match, so if you say org.the.app=org.new.app, then something like org.the.app.Locale will be rebased to org.new.app.Locale.

`--timestamp=TIMESTAMP`  
Override the timestamp of the commit. Use an ISO 8601 formatted date, or NOW for the current time

`--disable-fsync`  
Don't fsync when writing to the repository. This can result in data loss in exceptional situations, but can improve performance when working with temporary or test repositories.

`-v`, `--verbose`  
Print debug information during command processing.

`--ostree-verbose`  
Print OSTree debug information during command processing.

## Examples

To revert a commit to the commit before:

**\$ flatpak build-commit-from --timestamp=NOW --src-ref=app/org.gnome.gedit/x86_64/master^ repo app/org.gnome.gedit/x86_64/master**

## See also

[ostree(1)](#ostree), [flatpak(1)](#flatpak), [flatpak-build-init(1)](#flatpak-build-init), [flatpak-build(1)](#flatpak-build), [flatpak-build-finish(1)](#flatpak-build-finish), [flatpak-build-sign(1)](#flatpak-build-sign), [flatpak-build-update-repo(1)](#flatpak-build-update-repo)

## Name

flatpak-build-export — Create a repository from a build directory

## Synopsis

`flatpak build-export` \[OPTION...\] LOCATION DIRECTORY \[BRANCH\]

## Description

Creates or updates a repository with an application build. LOCATION is the location of the repository. DIRECTORY must be a finalized build directory. If BRANCH is not specified, it is assumed to be "master".

If LOCATION exists, it is assumed to be an OSTree repository, otherwise a new OSTree repository is created at this location. The repository can be inspected with the **ostree** tool.

The contents of DIRECTORY are committed on the branch with name `app/APPNAME/ARCH/BRANCH`, where ARCH is the architecture of the runtime that the application is using. A commit filter is used to enforce that only the contents of the `files/` and `export/` subdirectories and the `metadata` file are included in the commit, anything else is ignored.

When exporting a flatpak to be published to the internet, `--collection-id=COLLECTION-ID` should be specified as a globally unique reverse DNS value to identify the collection of flatpaks this will be added to. Setting a globally unique collection ID allows the apps in the repository to be shared over peer to peer systems without needing further configuration.

The build-update-repo command should be used to update repository metadata whenever application builds are added to a repository.

## Options

The following options are understood:

`-h`, `--help`  
Show help options and exit.

`-s`, `--subject=SUBJECT`  
One line subject for the commit message.

`-b`, `--body=BODY`  
Full description for the commit message.

`--collection-id=COLLECTION-ID`  
Set as the collection ID of the repository. Setting a globally unique collection ID allows the apps in the repository to be shared over peer to peer systems without needing further configuration. If exporting to an existing repository, the collection ID must match the existing configured collection ID for that repository.

`--subset=SUBSET`  
Mark the commit to be included in the named subset. This will cause the commit to be put in the named subset summary (in addition to the main one), allowing users to see only this subset instead of the whole repo.

`--arch=ARCH`  
Specify the architecture component of the branch to export. Only host compatible architectures can be specified; see **flatpak --supported-arches** for valid values.

`--exclude=PATTERN`  
Exclude files matching PATTERN from the commit. This option can be used multiple times.

`--include=PATTERN`  
Don't exclude files matching PATTERN from the commit, even if they match the `--exclude` patterns. This option can be used multiple times.

`--metadata=FILENAME`  
Use the specified filename as metadata in the exported app instead of the default file (called `metadata`). This is useful if you want to commit multiple things from a single build tree, typically used in combination with `--files` and `--exclude`.

`--files=SUBDIR`  
Use the files in the specified subdirectory as the file contents, rather than the regular `files` directory.

`--timestamp=DATE`  
Use the specified ISO 8601 formatted date or NOW, for the current time, in the commit metadata and, if `--update-appstream` is used, the appstream data.

`--end-of-life=REASON`  
Mark the build as end-of-life. REASON is a message that may be shown to users installing this build.

`--end-of-life-rebase=ID`  
Mark the build as end-of-life. Unlike `--end-of-life`, this one takes an ID that supersedes the current one. By the user's request, the application data may be preserved for the new application.

`--disable-fsync`  
Don't fsync when writing to the repository. This can result in data loss in exceptional situations, but can improve performance when working with temporary or test repositories.

`--update-appstream`  
Update the appstream branch after the build.

`--no-update-summary`  
Don't update the summary file after the new commit is added. This means the repository will not be useful for serving over http until build-update-repo has been run. This is useful is you want to do multiple repo operations before finally updating the summary.

`--gpg-sign=KEYID`  
Sign the commit with this GPG key. This option can be used multiple times.

`--gpg-homedir=PATH`  
GPG Homedir to use when looking for keyrings

`-r`, `--runtime`  
Export a runtime instead of an app (this uses the usr subdir as files).

`-v`, `--verbose`  
Print debug information during command processing.

`--ostree-verbose`  
Print OSTree debug information during command processing.

## Examples

**\$ flatpak build-export ~/repos/gnome-calculator/ ~/build/gnome-calculator/ org.gnome.Calculator**

``` programlisting
Commit: 9d0044ea480297114d03aec85c3d7ae3779438f9d2cb69d717fb54237acacb8c
Metadata Total: 605
Metadata Written: 5
Content Total: 1174
Content Written: 1
Content Bytes Written: 305
```

## See also

[ostree(1)](#ostree), [flatpak(1)](#flatpak), [flatpak-build-init(1)](#flatpak-build-init), [flatpak-build(1)](#flatpak-build), [flatpak-build-finish(1)](#flatpak-build-finish), [flatpak-build-sign(1)](#flatpak-build-sign), [flatpak-build-update-repo(1)](#flatpak-build-update-repo)

## Name

flatpak-build-finish — Finalize a build directory

## Synopsis

`flatpak build-finish` \[OPTION...\] DIRECTORY

## Description

Finalizes a build directory, to prepare it for exporting. DIRECTORY is the name of the directory.

The result of this command is that desktop files, icons, D-Bus service files, and AppStream metainfo files from the `files` subdirectory are copied to a new `export` subdirectory. In the `metadata` file, the command key is set in the \[Application\] group, and the supported keys in the \[Environment\] group are set according to the options.

As part of finalization you can also specify permissions that the app needs, using the various options specified below. Additionally during finalization the permissions from the runtime are inherited into the app unless you specify `--no-inherit-permissions`

You should review the exported files and the application metadata before creating and distributing an application bundle.

It is an error to run build-finish on a directory that has not been initialized as a build directory, or has already been finalized.

## Options

The following options are understood:

`-h`, `--help`  
Show help options and exit.

`--command=COMMAND`  
The command to use. If this option is not specified, the first executable found in `files/bin` is used.

Note that the command is used when the application is run via **flatpak run**, and does not affect what gets executed when the application is run in other ways, e.g. via the desktop file or D-Bus activation.

`--require-version=MAJOR.MINOR.MICRO`  
Require this version or later of flatpak to install/update to this build.

`--share=SUBSYSTEM`  
Share a subsystem with the host session. This updates the \[Context\] group in the metadata. SUBSYSTEM must be one of: network, ipc. This option can be used multiple times.

`--unshare=SUBSYSTEM`  
Don't share a subsystem with the host session. This updates the \[Context\] group in the metadata. SUBSYSTEM must be one of: network, ipc. This option can be used multiple times.

`--socket=SOCKET`  
Expose a well-known socket to the application. This updates the \[Context\] group in the metadata. SOCKET must be one of: x11, wayland, fallback-x11, pulseaudio, system-bus, session-bus, ssh-auth, pcsc, cups, gpg-agent, inherit-wayland-socket. This option can be used multiple times.

The fallback-x11 option makes the X11 socket available only if there is no Wayland socket. This option was introduced in 0.11.3. To support older Flatpak releases, specify both x11 and fallback-x11. The fallback-x11 option takes precedence when both are supported.

`--nosocket=SOCKET`  
Don't expose a well known socket to the application. This updates the \[Context\] group in the metadata. SOCKET must be one of: x11, wayland, fallback-x11, pulseaudio, system-bus, session-bus, ssh-auth, pcsc, cups, gpg-agent, inherit-wayland-socket. This option can be used multiple times.

`--device=DEVICE`  
Expose a device to the application. This updates the \[Context\] group in the metadata. DEVICE must be one of: dri, input, usb, kvm, shm, all. This option can be used multiple times.

`--nodevice=DEVICE`  
Don't expose a device to the application. This updates the \[Context\] group in the metadata. DEVICE must be one of: dri, input, usb, kvm, shm, all. This option can be used multiple times.

`--allow=FEATURE`  
Allow access to a specific feature. This updates the \[Context\] group in the metadata. FEATURE must be one of: devel, multiarch, bluetooth, canbus, per-app-dev-shm. This option can be used multiple times.

The `devel` feature allows the application to access certain syscalls such as `ptrace()`, and `perf_event_open()`.

The `multiarch` feature allows the application to execute programs compiled for an ABI other than the one supported natively by the system. For example, for the `x86_64` architecture, 32-bit `x86` binaries will be allowed as well.

The `bluetooth` feature allows the application to use bluetooth (AF_BLUETOOTH) sockets. Note, for bluetooth to fully work you must also have network access.

The `canbus` feature allows the application to use canbus (AF_CAN) sockets. Note, for this work you must also have network access.

The `per-app-dev-shm` feature shares a single instance of `/dev/shm` between the application, any unrestricted subsandboxes that it creates, and any other instances of the application that are launched while it is running.

`--disallow=FEATURE`  
Disallow access to a specific feature. This updates the \[Context\] group in the metadata. FEATURE must be one of: devel, multiarch, bluetooth, canbus, per-app-dev-shm. This option can be used multiple times.

`--filesystem=FS`  
Allow the application access to a subset of the filesystem. This updates the \[Context\] group in the metadata. FS can be one of: home, host, host-os, host-etc, host-root, xdg-desktop, xdg-documents, xdg-download, xdg-music, xdg-pictures, xdg-public-share, xdg-templates, xdg-videos, xdg-run, xdg-config, xdg-cache, xdg-data, an absolute path, or a homedir-relative path like ~/dir or paths relative to the xdg dirs, like xdg-download/subdir. The optional :ro suffix indicates that the location will be read-only. The optional :create suffix indicates that the location will be read-write and created if it doesn't exist. This option can be used multiple times. See the "\[Context\] filesystems" list in [flatpak-metadata(5)](#flatpak-metadata) for details of the meanings of these filesystems.

`--nofilesystem=FILESYSTEM`  
Remove access to the specified subset of the filesystem from the application. This overrides to the Context section from the application metadata. FILESYSTEM can be one of: home, host, host-os, host-etc, host-root, xdg-desktop, xdg-documents, xdg-download, xdg-music, xdg-pictures, xdg-public-share, xdg-templates, xdg-videos, an absolute path, or a homedir-relative path like ~/dir. This option can be used multiple times.

`--add-policy=SUBSYSTEM.KEY=VALUE`  
Add generic policy option. For example, "--add-policy=subsystem.key=v1 --add-policy=subsystem.key=v2" would map to this metadata:

``` programlisting
[Policy subsystem]
key=v1;v2;
```

This option can be used multiple times.

`--remove-policy=SUBSYSTEM.KEY=VALUE`  
Remove generic policy option. This option can be used multiple times.

`--usb=TYPE[:DATA]`  
Makes USB devices matching the query visible to the USB portal by adding the query to the application metadata. This does not have any effect on the devices exposed in /dev. TYPE must be one of: all, cls, dev, vnd.

`all`  
Match all devices.

`cls`  
A device class and subclass query. DATA must be in the form of CLASS:SUBCLASS where both CLASS and SUBCLASS must valid 2-digit hexadecimal class id numbers. Alternatively, SUBCLASS may be `*` to match all subclasses.

`dev`  
A device product id query. DATA must be a valid 4-character hexadecimal product id number, for example `0a1b`. It requires a `vnd` filter in the query.

`vnd`  
A device vendor id query. DATA must be a valid 4-character hexadecimal vendor id number greater than zero, for example `0fab`.

It is possible to compose multiple device queries together with the `+` sign, for example `--usb=vnd:0123+dev:4567`. The dev filter requires a vnd . Available since 1.15.11.

`--nousb=TYPE[:DATA]`  
Hides USB devices matching the query from the USB portal by adding the query to the application metadata. Queries hiding devices take precedence over queries making devices visible (see `--usb`). The syntax is exactly equal to `--usb`. This does not have any effect on the devices exposed in /dev. Available since 1.15.11.

`--usb-list-file=FILENAME`  
Adds USB device queries to the application metadata from the file FILE_NAME . The line syntax is exactly equal to `--usb`. Additionally, if it starts with ! then the query is like for `--nousb`. Lines sthat starts with `#` are ignored, like a comment. Comments will not be persisted. Available since 1.15.11.

`--usb-list=LIST`  
Adds USB device queries to the application metadata from LIST . The syntax is exactly equal to `--usb` with queries separated by `;`. Additionally, if the query starts with `!` then the query is like for `--nousb`. Available since 1.15.11.

`--env=VAR=VALUE`  
Set an environment variable in the application. This updates the \[Environment\] group in the metadata. This overrides to the Context section from the application metadata. This option can be used multiple times.

`--unset-env=VAR`  
Unset an environment variable in the application. This updates the unset-environment entry in the \[Context\] group of the metadata. This option can be used multiple times.

`--env-fd=`*`FD`*  
Read environment variables from the file descriptor *`FD`*, and set them as if via `--env`. This can be used to avoid environment variables and their values becoming visible to other users.

Each environment variable is in the form *`VAR`*=*`VALUE`* followed by a zero byte. This is the same format used by `env -0` and `/proc/*/environ`.

`--own-name=NAME`  
Allow the application to own the well known name NAME on the session bus. If NAME ends with .\*, it allows the application to own all matching names. This updates the \[Session Bus Policy\] group in the metadata. This option can be used multiple times.

`--talk-name=NAME`  
Allow the application to talk to the well known name NAME on the session bus. If NAME ends with .\*, it allows the application to talk to all matching names. This updates the \[Session Bus Policy\] group in the metadata. This option can be used multiple times.

`--system-own-name=NAME`  
Allow the application to own the well known name NAME on the system bus. If NAME ends with .\*, it allows the application to own all matching names. This updates the \[System Bus Policy\] group in the metadata. This option can be used multiple times.

`--system-talk-name=NAME`  
Allow the application to talk to the well known name NAME on the system bus. If NAME ends with .\*, it allows the application to talk to all matching names. This updates the \[System Bus Policy\] group in the metadata. This option can be used multiple times.

`--persist=FILENAME`  
If the application doesn't have access to the real homedir, make the (homedir-relative) path FILENAME a bind mount to the corresponding path in the per-application directory, allowing that location to be used for persistent data. This updates the \[Context\] group in the metadata. This option can be used multiple times.

`--runtime=RUNTIME`, `--sdk=SDK`  
Change the runtime or sdk used by the app to the specified partial ref. Unspecified parts of the ref are taken from the old values or defaults.

`--metadata=GROUP=KEY[=VALUE]`  
Set a generic key in the metadata file. If value is left out it will be set to "true".

`--extension=NAME=VARIABLE[=VALUE]`  
Add extension point info. See the documentation for [flatpak-metadata(5)](#flatpak-metadata) for the possible values of *`VARIABLE`* and *`VALUE`*.

`--remove-extension=NAME`  
Remove extension point info.

`--extension-priority=VALUE`  
Set the priority (library override order) of the extension point. Only useful for extensions. 0 is the default, and higher value means higher priority.

`--extra-data=NAME:SHA256:DOWNLOAD-SIZE:INSTALL-SIZE:URL`  
Adds information about extra data uris to the app. These will be downloaded and verified by the client when the app is installed and placed in the `/app/extra` directory. You can also supply an `/app/bin/apply_extra` script that will be run after the files are downloaded.

`--no-exports`  
Don't look for exports in the build.

`--no-inherit-permissions`  
Don't inherit runtime permissions in the app.

`-v`, `--verbose`  
Print debug information during command processing.

`--ostree-verbose`  
Print OSTree debug information during command processing.

## Examples

**\$ flatpak build-finish /build/my-app --socket=x11 --share=ipc --usb=vnd:0fd9**

``` programlisting
Exporting share/applications/gnome-calculator.desktop
Exporting share/dbus-1/services/org.gnome.Calculator.SearchProvider.service
More than one executable
Using gcalccmd as command
Please review the exported files and the metadata
```

## See also

[flatpak(1)](#flatpak), [flatpak-build-init(1)](#flatpak-build-init), [flatpak-build(1)](#flatpak-build), [flatpak-build-export(1)](#flatpak-build-export)

## Name

flatpak-build-import-bundle — Import a file bundle into a local repository

## Synopsis

`flatpak build-import-bundle` \[OPTION...\] LOCATION FILENAME

## Description

Imports a bundle from a file named FILENAME into the repository at LOCATION .

The format of the bundle file is that generated by build-bundle.

## Options

The following options are understood:

`-h`, `--help`  
Show help options and exit.

`-v`, `--verbose`  
Print debug information during command processing.

`--ostree-verbose`  
Print OSTree debug information during command processing.

`--ref=REF`  
Override the ref specified in the bundle.

`--oci`  
Import an OCI image instead of a Flatpak bundle.

`--update-appstream`  
Update the appstream branch after the build.

`--no-update-summary`  
Don't update the summary file after the new commit is added. This means the repository will not be useful for serving over http until build-update-repo has been run. This is useful is you want to do multiple repo operations before finally updating the summary.

`--gpg-sign=KEYID`  
Sign the commit with this GPG key. This option can be used multiple times.

`--gpg-homedir=PATH`  
GPG Homedir to use when looking for keyrings

## See also

[ostree(1)](#ostree), [flatpak(1)](#flatpak), [flatpak-build-bundle(1)](#flatpak-build-bundle), [flatpak-build-update-repo(1)](#flatpak-build-update-repo)

## Name

flatpak-build-init — Initialize a build directory

## Synopsis

`flatpak build-init` \[OPTION...\] DIRECTORY APPNAME SDK RUNTIME \[BRANCH\]

## Description

Initializes a separate build directory. DIRECTORY is the name of the directory. APPNAME is the application id of the app that will be built. SDK and RUNTIME specify the sdk and runtime that the application should be built against and run in. BRANCH specify the version of sdk and runtime

Initializes a directory as build directory which can be used as target directory of **flatpak build**. It creates a `metadata` inside the given directory. Additionally, empty `files` and `var` subdirectories are created.

It is an error to run build-init on a directory that has already been initialized as a build directory.

## Options

The following options are understood:

`-h`, `--help`  
Show help options and exit.

`--arch=ARCH`  
The architecture to use. See **flatpak --supported-arches** for architectures supported by the host.

`-v`, `--var=RUNTIME`  
Initialize var from the named runtime.

`-w`, `--writable-sdk`  
Initialize /usr with a copy of the sdk, which is writable during flatpak build. This can be used if you need to install build tools in /usr during the build. This is stored in the `usr` subdirectory of the app dir, but will not be part of the final app.

`--tag=TAG`  
Add a tag to the metadata file. This option can be used multiple times.

`--sdk-extension=EXTENSION`  
When using `--writable-sdk`, in addition to the sdk, also install the specified extension. This option can be used multiple times.

`--extension=NAME=VARIABLE[=VALUE]`  
Add extension point info.

`--sdk-dir`  
Specify a custom subdirectory to use instead of `usr` for `--writable-sdk`.

`--update`  
Re-initialize the sdk and var, don't fail if already initialized.

`--base=APP`  
Initialize the application with files from another specified application.

`--base-version=VERSION`  
Specify the version to use for `--base`. If not specified, will default to "master".

`--base-extension=EXTENSION`  
When using `--base`, also install the specified extension from the app. This option can be used multiple times.

`--type=TYPE`  
This can be used to build different types of things. The default is "app" which is a regular app, but "runtime" creates a runtime based on an existing runtime, and "extension" creates an extension for an app or runtime.

`--extension-tag=EXTENSION_TAG`  
If building an extension, the tag to use when searching for the mount point of the extension.

`--verbose`  
Print debug information during command processing.

`--ostree-verbose`  
Print OSTree debug information during command processing.

## Examples

**\$ flatpak build-init /build/my-app org.example.myapp org.gnome.Sdk org.gnome.Platform 3.36**

## See also

[flatpak(1)](#flatpak), [flatpak-build(1)](#flatpak-build), [flatpak-build-finish(1)](#flatpak-build-finish), [flatpak-build-export(1)](#flatpak-build-export)

## Name

flatpak-build-sign — Sign an application or runtime

## Synopsis

`flatpak build-sign` \[OPTION...\] LOCATION ID \[BRANCH\]

## Description

Signs the commit for a specified application or runtime in a local repository. LOCATION is the location of the repository. ID is the name of the application, or runtime if --runtime is specified. If BRANCH is not specified, it is assumed to be "master".

Applications can also be signed during build-export, but it is sometimes useful to add additional signatures later.

## Options

The following options are understood:

`-h`, `--help`  
Show help options and exit.

`--gpg-sign=KEYID`  
Sign the commit with this GPG key. This option can be used multiple times.

`--gpg-homedir=PATH`  
GPG Homedir to use when looking for keyrings

`--runtime`  
Sign a runtime instead of an app.

`--arch=ARCH`  
The architecture to use. See **flatpak --supported-arches** for architectures supported by the host.

`-v`, `--verbose`  
Print debug information during command processing.

`--ostree-verbose`  
Print OSTree debug information during command processing.

## Examples

**\$ flatpak build-sign --gpg-sign=D8BA6573DDD2418027736F1BC33B315E53C1E9D6 /some/repo org.my.App**

## See also

[ostree(1)](#ostree), [flatpak(1)](#flatpak), [flatpak-build-export(1)](#flatpak-build-export), [flatpak-build(1)](#flatpak-build),

## Name

flatpak-build-update-repo — Create a repository from a build directory

## Synopsis

`flatpak build-update-repo` \[OPTION...\] LOCATION

## Description

Updates repository metadata for the repository at LOCATION . This command generates an OSTree summary file that lists the contents of the repository. The summary is used by flatpak remote-ls and other commands to display the contents of remote repositories.

After this command, LOCATION can be used as the repository location for flatpak remote-add, either by exporting it over http, or directly with a file: url.

## Options

The following options are understood:

`-h`, `--help`  
Show help options and exit.

`--redirect-url=URL`  
Redirect this repo to a new URL.

`--title=TITLE`  
A title for the repository, e.g. for display in a UI. The title is stored in the repository summary.

`--comment=COMMENT`  
A single-line comment for the remote, e.g. for display in a UI. The comment is stored in the repository summary.

`--description=DESCRIPTION`  
A full-paragraph description for the remote, e.g. for display in a UI. The description is stored in the repository summary.

`--homepage=URL`  
URL for a website for the remote, e.g. for display in a UI. The url is stored in the repository summary.

`--icon=URL`  
URL for an icon for the remote, e.g. for display in a UI. The url is stored in the repository summary.

`--default-branch=BRANCH`  
A default branch for the repository, mainly for use in a UI.

`--gpg-import=FILE`  
Import a new default GPG public key from the given file.

`--collection-id=COLLECTION-ID`  
The globally unique identifier of the remote repository, to allow mirrors to be grouped. This must be set to a globally unique reverse DNS string if the repository is to be made publicly available. If a collection ID is already set on an existing repository, this will update it. If not specified, the existing collection ID will be left unchanged.

`--deploy-collection-id`  
Deploy the collection ID (set using `--collection-id`) in the static remote configuration for all clients. This is irrevocable once published in a repository. Use it to decide when to roll out a collection ID to users of an existing repository. If constructing a new repository which has a collection ID, you should typically always pass this option.

`--deploy-sideload-collection-id`  
This is similar to --deploy-collection-id, but it only applies the deploy to clients newer than flatpak 1.7 which supports the new form of sideloads.

`--gpg-sign=KEYID`  
Sign the commit with this GPG key. This option can be used multiple times.

`--gpg-homedir=PATH`  
GPG Homedir to use when looking for keyrings

`--generate-static-deltas`  
Generate static deltas for all references. This generates from-empty and delta static files that allow for faster download.

`--static-delta-jobs=NUM-JOBS`  
Limit the number of parallel jobs creating static deltas. The default is the number of cpus.

`--static-delta-ignore-ref=PATTERN`  
Don't generate deltas for runtime or application id matching this pattern. For instance, --static-delta-ignore-ref=\*.Sources means there will not be any deltas for source refs.

`--prune`  
Remove unreferenced objects in repo.

`--prune-depth`  
Only keep at most this number of old versions for any particular ref. Default is -1 which means infinite.

`-v`, `--verbose`  
Print debug information during command processing.

`--ostree-verbose`  
Print OSTree debug information during command processing.

## See also

[ostree(1)](#ostree), [flatpak(1)](#flatpak), [flatpak-remote-ls(1)](#flatpak-remote-ls), [flatpak-build-export(1)](#flatpak-build-export)

## Name

flatpak-build — Build in a directory

## Synopsis

`flatpak build` \[OPTION...\] DIRECTORY \[COMMAND \[ARG...\]\]

## Description

Runs a build command in a directory. DIRECTORY must have been initialized with **flatpak build-init**.

The sdk that is specified in the `metadata` file in the directory is mounted at `/usr` and the `files` and `var` subdirectories are mounted at `/app` and `/var`, respectively. They are writable, and their contents are preserved between build commands, to allow accumulating build artifacts there.

## Options

The following options are understood:

`-h`, `--help`  
Show help options and exit.

`-v`, `--verbose`  
Print debug information during command processing.

`--ostree-verbose`  
Print OSTree debug information during command processing.

`-r`, `--runtime`  
Use the non-devel runtime that is specified in the application metadata instead of the devel runtime.

`-p`, `--die-with-parent`  
Kill the build process and all children when the launching process dies.

`--bind-mount=DEST=SOURCE`  
Add a custom bind mount in the build namespace. Can be specified multiple times.

`--build-dir=PATH`  
Start the build in this directory (default is in the current directory).

`--share=SUBSYSTEM`  
Share a subsystem with the host session. This overrides the Context section from the application metadata. SUBSYSTEM must be one of: network, ipc. This option can be used multiple times.

`--unshare=SUBSYSTEM`  
Don't share a subsystem with the host session. This overrides the Context section from the application metadata. SUBSYSTEM must be one of: network, ipc. This option can be used multiple times.

`--socket=SOCKET`  
Expose a well-known socket to the application. This overrides to the Context section from the application metadata. SOCKET must be one of: x11, wayland, fallback-x11, pulseaudio, system-bus, session-bus, ssh-auth, pcsc, cups, gpg-agent, inherit-wayland-socket. This option can be used multiple times.

`--nosocket=SOCKET`  
Don't expose a well-known socket to the application. This overrides to the Context section from the application metadata. SOCKET must be one of: x11, wayland, fallback-x11, pulseaudio, system-bus, session-bus, ssh-auth, pcsc, cups, gpg-agent, inherit-wayland-socket. This option can be used multiple times.

`--device=DEVICE`  
Expose a device to the application. This overrides to the Context section from the application metadata. DEVICE must be one of: dri, input, usb, kvm, shm, all. This option can be used multiple times.

`--nodevice=DEVICE`  
Don't expose a device to the application. This overrides to the Context section from the application metadata. DEVICE must be one of: dri, input, usb, kvm, shm, all. This option can be used multiple times.

`--allow=FEATURE`  
Allow access to a specific feature. This updates the \[Context\] group in the metadata. FEATURE must be one of: devel, multiarch, bluetooth, canbus, per-app-dev-shm. This option can be used multiple times.

See [flatpak-build-finish(1)](#flatpak-build-finish) for the meaning of the various features.

`--disallow=FEATURE`  
Disallow access to a specific feature. This updates the \[Context\] group in the metadata. FEATURE must be one of: devel, multiarch, bluetooth, canbus, per-app-dev-shm. This option can be used multiple times.

`--filesystem=FILESYSTEM[:ro|:create]`  
Allow the application access to a subset of the filesystem. This overrides to the Context section from the application metadata. FILESYSTEM can be one of: home, host, host-os, host-etc, host-root, xdg-desktop, xdg-documents, xdg-download, xdg-music, xdg-pictures, xdg-public-share, xdg-templates, xdg-videos, xdg-run, xdg-config, xdg-cache, xdg-data, an absolute path, or a homedir-relative path like ~/dir or paths relative to the xdg dirs, like xdg-download/subdir. The optional :ro suffix indicates that the location will be read-only. The optional :create suffix indicates that the location will be read-write and created if it doesn't exist. This option can be used multiple times. See the "\[Context\] filesystems" list in [flatpak-metadata(5)](#flatpak-metadata) for details of the meanings of these filesystems.

`--nofilesystem=FILESYSTEM`  
Remove access to the specified subset of the filesystem from the application. This overrides to the Context section from the application metadata. FILESYSTEM can be one of: home, host, host-os, host-etc, host-root xdg-desktop, xdg-documents, xdg-download, xdg-music, xdg-pictures, xdg-public-share, xdg-templates, xdg-videos, an absolute path, or a homedir-relative path like ~/dir. This option can be used multiple times.

`--with-appdir`  
Expose and configure access to the per-app storage directory in `$HOME/.var/app`. This is not normally useful when building, but helps when testing built apps.

`--add-policy=SUBSYSTEM.KEY=VALUE`  
Add generic policy option. For example, "--add-policy=subsystem.key=v1 --add-policy=subsystem.key=v2" would map to this metadata:

``` programlisting
[Policy subsystem]
key=v1;v2;
```

This option can be used multiple times.

`--remove-policy=SUBSYSTEM.KEY=VALUE`  
Remove generic policy option. This option can be used multiple times.

`--env=VAR=VALUE`  
Set an environment variable in the application. This overrides to the Context section from the application metadata. This option can be used multiple times.

`--unset-env=VAR`  
Unset an environment variable in the application. This overrides the unset-environment entry in the \[Context\] group of the metadata, and the \[Environment\] group. This option can be used multiple times.

`--env-fd=`*`FD`*  
Read environment variables from the file descriptor *`FD`*, and set them as if via `--env`. This can be used to avoid environment variables and their values becoming visible to other users.

Each environment variable is in the form *`VAR`*=*`VALUE`* followed by a zero byte. This is the same format used by `env -0` and `/proc/*/environ`.

`--own-name=NAME`  
Allow the application to own the well-known name NAME on the session bus. This overrides to the Context section from the application metadata. This option can be used multiple times.

`--talk-name=NAME`  
Allow the application to talk to the well-known name NAME on the session bus. This overrides to the Context section from the application metadata. This option can be used multiple times.

`--system-own-name=NAME`  
Allow the application to own the well-known name NAME on the system bus. This overrides to the Context section from the application metadata. This option can be used multiple times.

`--system-talk-name=NAME`  
Allow the application to talk to the well-known name NAME on the system bus. This overrides to the Context section from the application metadata. This option can be used multiple times.

`--persist=FILENAME`  
If the application doesn't have access to the real homedir, make the (homedir-relative) path FILENAME a bind mount to the corresponding path in the per-application directory, allowing that location to be used for persistent data. This overrides to the Context section from the application metadata. This option can be used multiple times.

`--sdk-dir=DIR`  
Normally if there is a `usr` directory in the build dir, this is used for the runtime files (this can be created by `--writable-sdk` or `--type=runtime` arguments to build-init). If you specify `--sdk-dir`, this directory will be used instead. Use this if you passed `--sdk-dir` to build-init.

`--readonly`  
Mount the normally writable destination directories read-only. This can be useful if you want to run something in the sandbox but guarantee that it doesn't affect the build results. For example tests.

`--metadata=FILE`  
Use the specified filename as metadata in the exported app instead of the default file (called `metadata`). This is useful if you build multiple things from a single build tree (such as both a platform and a sdk).

`--log-session-bus`  
Log session bus traffic. This can be useful to see what access you need to allow in your D-Bus policy.

`--log-system-bus`  
Log system bus traffic. This can be useful to see what access you need to allow in your D-Bus policy.

## Examples

**\$ flatpak build /build/my-app rpmbuild my-app.src.rpm**

## See also

[flatpak(1)](#flatpak), [flatpak-build-init(1)](#flatpak-build-init), [flatpak-build-finish(1)](#flatpak-build-finish), [flatpak-build-export(1)](#flatpak-build-export)

## Name

flatpak-config — Manage configuration

## Synopsis

`flatpak config` \[OPTION...\]

`flatpak config` \[OPTION...\] --set KEY VALUE

`flatpak config` \[OPTION...\] --unset\|--get KEY

## Description

The flatpak config command shows or modifies the configuration of a flatpak installation. The following keys are supported:

`languages`  
The languages that are included when installing Locale extensions. The value is a semicolon-separated list of two-letter language codes, or one of the special values `*` or `*all*`. If this key is unset, flatpak defaults to including the `extra-languages` key and the current locale.

`extra-languages`  
This key is used when languages is not set, and it defines extra locale extensions on top of the system configured languages. The value is a semicolon-separated list of locale identifiers (language, optional locale, optional codeset, optional modifier) as documented by [setlocale(3)](#setlocale) (for example, `en;en_DK;zh_HK.big5hkscs;uz_UZ.utf8@cyrillic`).

For configuration of individual remotes, see [flatpak-remote-modify(1)](#flatpak-remote-modify). For configuration of individual applications, see [flatpak-override(1)](#flatpak-override).

## Options

The following options are understood:

`-h`, `--help`  
Show help options and exit.

`--list`  
Print all keys and their values.

`--set`  
Set key KEY to VALUE .

`--unset`  
Unset key KEY .

`--get`  
Print value of KEY .

`-u`, `--user`  
Configure per-user installation.

`--system`  
Configure system-wide installation.

`--installation=NAME`  
Configure the system-wide installation specified by NAME among those defined in `/etc/flatpak/installations.d/`. Using `--installation=default` is equivalent to using `--system`.

`-v`, `--verbose`  
Print debug information during command processing.

`--ostree-verbose`  
Print OSTree debug information during command processing.

## Examples

**\$ flatpak config --set languages "sv;en;fi"**

## See also

[flatpak(1)](#flatpak), [flatpak-remote-modify(1)](#flatpak-remote-modify), [flatpak-override(1)](#flatpak-override)

## Name

flatpak-create-usb — Copy apps and/or runtimes onto removable media.

## Synopsis

`flatpak create-usb` \[OPTION...\] MOUNT-PATH REF...

## Description

Copies the specified apps and/or runtimes REF s onto the removable media mounted at MOUNT-PATH , along with all the dependencies and metadata needed for installing them. This is one way of transferring flatpaks between computers that doesn't require an Internet connection. After using this command, the USB drive can be connected to another computer which already has the relevant remote(s) configured, and Flatpak will install or update from the drive offline (see below). If online, the drive will be used as a cache, meaning some objects will be pulled from it and others from the Internet. For this process to work a collection ID must be configured on the relevant remotes on both the source and destination computers, and on the remote server.

On the destination computer one can install from the USB (or any mounted filesystem) using the `--sideload-repo` option with **flatpak install**. It's also possible to configure sideload paths using symlinks; see [flatpak(1)](#flatpak). Flatpak also includes systemd units to automatically sideload from hot-plugged USB drives, but these may or may not be enabled depending on your Linux distribution.

Each REF argument is a full or partial identifier in the flatpak ref format, which looks like "(app\|runtime)/ID/ARCH/BRANCH". All elements except ID are optional and can be left out, including the slashes, so most of the time you need only specify ID. Any part left out will be matched against what is installed, and if there are multiple matches an error message will list the alternatives.

By default this looks for both installed apps and runtimes with the given REF , but you can limit this by using the `--app` or `--runtime` option.

All REF s must be in the same installation (user, system, or other). Otherwise it's ambiguous which repository metadata refs to put on the USB drive.

By default **flatpak create-usb** uses `.ostree/repo` as the destination directory under MOUNT-PATH but if you specify another location using `--destination-repo` a symbolic link will be created for you in `.ostree/repos.d`. This ensures that either way the repository will be found by flatpak (and other consumers of libostree) for install/update operations.

Unless overridden with the `--system`, `--user`, or `--installation` options, this command searches both the system-wide installation and the per-user one for REF and errors out if it exists in more than one.

## Options

The following options are understood:

`-h`, `--help`  
Show help options and exit.

`-u`, `--user`  
Copy refs from the per-user installation.

`--system`  
Copy refs from the default system-wide installation.

`--installation=NAME`  
Copy refs from a system-wide installation specified by NAME among those defined in `/etc/flatpak/installations.d/`. Using `--installation=default` is equivalent to using `--system`.

`--app`  
Assume that all REF s are apps if not explicitly specified.

`--runtime`  
Assume that all REF s are runtimes if not explicitly specified.

`--destination-repo`=DEST  
Create the repository in DEST under MOUNT-PATH , rather than the default location.

`--allow-partial`  
Don't print a warning when exporting partially installed commits, for example locale extensions without all languages. These can cause problems when installing them, for example if the language config is different on the installing side.

`-v`, `--verbose`  
Print debug information during command processing.

`--ostree-verbose`  
Print OSTree debug information during command processing.

## Examples

**\$ flatpak create-usb /run/media/mwleeds/1a9b4cb2-a7ef-4d9b-91a5-6eaf8fdd2bf6/ com.endlessm.wiki_art.en**

## See also

[flatpak(1)](#flatpak), [flatpak remote-modify(1)](#flatpak%20remote-modify), [flatpak-install(1)](#flatpak-install), [flatpak-list(1)](#flatpak-list), [ostree-create-usb(1)](#ostree-create-usb)

## Name

flatpak-document-export — Export a file to a sandboxed application

## Synopsis

`flatpak document-export` \[OPTION...\] FILE

## Description

Creates a document id for a local file that can be exposed to sandboxed applications, allowing them access to files that they would not otherwise see. The exported files are exposed in a fuse filesystem at `/run/user/$UID/doc/`.

This command also lets you modify the per-application permissions of the documents, granting or revoking access to the file on a per-application basis.

## Options

The following options are understood:

`-h`, `--help`  
Show help options and exit.

`-u`, `--unique`  
Don't reuse an existing document id for the file. This makes it safe to later remove the document when you're finished with it.

`-t`, `--transient`  
The document will only exist for the length of the session. This is useful for temporary grants.

`-n`, `--noexist`  
Don't require the file to exist already.

`-a`, `--app=APPID`  
Grant read access to the specified application. The `--allow` and `--forbid` options can be used to grant or remove additional privileges. This option can be used multiple times.

`-r`, `--allow-read`  
Grant read access to the applications specified with `--app`. This defaults to TRUE.

`--forbid-read`  
Revoke read access for the applications specified with `--app`.

`-w`, `--allow-write`  
Grant write access to the applications specified with `--app`.

`--forbid-write`  
Revoke write access for the applications specified with `--app`.

`-d`, `--allow-delete`  
Grant the ability to remove the document from the document portal to the applications specified with `--app`.

`--forbid-delete`  
Revoke the ability to remove the document from the document portal from the applications specified with `--app`.

`-g`, `--allow-grant-permission`  
Grant the ability to grant further permissions to the applications specified with `--app`.

`--forbid-grant-permission`  
Revoke the ability to grant further permissions for the applications specified with `--app`.

`-v`, `--verbose`  
Print debug information during command processing.

`--ostree-verbose`  
Print OSTree debug information during command processing.

## Examples

**\$ flatpak document-export --app=org.gnome.gedit ~/test.txt**

``` programlisting
/run/user/1000/doc/e52f9c6a/test.txt
```

## See also

[flatpak(1)](#flatpak), [flatpak-document-unexport(1)](#flatpak-document-unexport), [flatpak-document-info(1)](#flatpak-document-info), [flatpak-documents(1)](#flatpak-documents)

## Name

flatpak-document-info — Show information about exported files

## Synopsis

`flatpak document-info` \[OPTION...\] FILE

## Description

Shows information about an exported file, such as the document id, the fuse path, the original location in the filesystem, and the per-application permissions.

FILE can either be a file in the fuse filesystem at `/run/user/$UID/doc/`, or a file anywhere else.

## Options

The following options are understood:

`-h`, `--help`  
Show help options and exit.

`-v`, `--verbose`  
Print debug information during command processing.

`--ostree-verbose`  
Print OSTree debug information during command processing.

## Examples

**\$ flatpak document-info ~/Sources/gtk/gail-3.0.pc**

``` programlisting
id: dd32c34a
path: /run/user/1000/doc/dd32c34a/gail-3.0.pc
origin: /home/mclasen/Sources/gtk/gail-3.0.pc
permissions:
        org.gnome.gedit read, write
```

## See also

[flatpak(1)](#flatpak), [flatpak-document-export(1)](#flatpak-document-export), [flatpak-document-unexport(1)](#flatpak-document-unexport), [flatpak-documents(1)](#flatpak-documents)

## Name

flatpak-documents — List exported files

## Synopsis

`flatpak documents` \[OPTION...\] \[APPID\]

## Description

Lists exported files, with their document id and the full path to their origin. If an APPID is specified, only the files exported to this app are listed.

## Options

The following options are understood:

`-h`, `--help`  
Show help options and exit.

`-v`, `--verbose`  
Print debug information during command processing.

`--ostree-verbose`  
Print OSTree debug information during command processing.

## See also

[flatpak(1)](#flatpak), [flatpak-document-export(1)](#flatpak-document-export), [flatpak-document-unexport(1)](#flatpak-document-unexport), [flatpak-document-info(1)](#flatpak-document-info)

## Name

flatpak-document-unexport — Stop exporting a file

## Synopsis

`flatpak document-unexport` \[OPTION...\] FILE

## Description

Removes the document id for the file from the document portal. This will make the document unavailable to all sandboxed applications.

## Options

The following options are understood:

`--doc-id`  
Interpret FILE as a document ID rather than a file path. This is useful for example when the file has been deleted.

`-h`, `--help`  
Show help options and exit.

`-v`, `--verbose`  
Print debug information during command processing.

`--ostree-verbose`  
Print OSTree debug information during command processing.

## See also

[flatpak(1)](#flatpak), [flatpak-document-export(1)](#flatpak-document-export), [flatpak-document-info(1)](#flatpak-document-info), [flatpak-documents(1)](#flatpak-documents)

## Name

flatpak-enter — Enter an application or runtime's sandbox

## Synopsis

`flatpak enter` \[OPTION...\] INSTANCE COMMAND \[ARG...\]

## Description

Enter a running sandbox.

INSTANCE must be either the pid of a process running in a flatpak sandbox, or the ID of a running application, or the instance ID of a running sandbox. You can use **flatpak ps** to find the instance IDs of running flatpaks.

COMMAND is the command to run in the sandbox. Extra arguments are passed on to the command.

This creates a new process within the running sandbox, with the same environment. This is useful when you want to debug a problem with a running application.

This command works as a regular user if the system support unprivileged user namespace. If that is not available you need to run run it like: **sudo -E flatpak enter**.

## Options

The following options are understood:

`-h`, `--help`  
Show help options and exit.

`-v`, `--verbose`  
Print debug information during command processing.

`--ostree-verbose`  
Print OSTree debug information during command processing.

## Examples

**\$ flatpak enter 15345 sh**

## See also

[flatpak(1)](#flatpak), [flatpak-run(1)](#flatpak-run) [flatpak-ps(1)](#flatpak-ps)

## Name

flatpak-history — Show history

## Synopsis

`flatpak history` \[OPTION...\]

## Description

Shows changes to the flatpak installations on the system. This includes installs, updates and removals of applications and runtimes.

By default, both per-user and system-wide installations are shown. Use the `--user`, `--installation` or `--system` options to change this.

The information for the history command is taken from the systemd journal, and can also be accessed using e.g. **journalctl MESSAGE_ID=c7b39b1e006b464599465e105b361485**

## Options

The following options are understood:

`-h`, `--help`  
Show help options and exit.

`-u`, `--user`  
Show changes to the user installation.

`--system`  
Show changes to the default system-wide installation.

`--installation=NAME`  
Show changes to the installation specified by NAME among those defined in `/etc/flatpak/installations.d/`. Using `--installation=default` is equivalent to using `--system`.

`--since=TIME`  
Only show changes that are newer than the time specified by TIME .

TIME can be either an absolute time in a format like YYYY-MM-DD HH:MM:SS, or a relative time like "2h", "7days", "4days 2hours".

`--until=TIME`  
Only show changes that are older than the time specified by TIME .

`--reverse`  
Show newest entries first.

`-v`, `--verbose`  
Print debug information during command processing.

`--ostree-verbose`  
Print OSTree debug information during command processing.

`--columns=FIELD,…`  
Specify what information to show about each ref. You can list multiple fields, or use this option multiple times.

Append :s\[tart\], :m\[iddle\], :e\[nd\] or :f\[ull\] to column names to change ellipsization.

## Fields

The following fields are understood by the `--columns` option:

time  
Show when the change happened

change  
Show the kind of change

ref  
Show the ref

application  
Show the application/runtime ID

arch  
Show the architecture

branch  
Show the branch

installation  
Show the affected installation.

This will be either the ID of a Flatpak installation, or the path to a temporary OSTree repository.

remote  
Show the remote that is used.

This will be either the name of a configured remote, or the path to a temporary OSTree repository.

old-commit  
Show the previous commit. For pulls, this is the previous HEAD of the branch. For deploys, it is the previously active commit

commit  
Show the current commit. For pulls, this is the HEAD of the branch. For deploys, it is the active commit

url  
Show the remote url

user  
Show the user doing the change.

If this is the system helper operating as root, also show which user triggered the change.

tool  
Show the tool that was used.

If this is the system helper, also show which tool was used to triggered the change.

all  
Show all columns

help  
Show the list of available columns

Note that field names can be abbreviated to a unique prefix.

## See also

[flatpak(1)](#flatpak), [journalctl(1)](#journalctl)

## Name

flatpak-info — Show information about an installed application or runtime

## Synopsis

`flatpak info` \[OPTION...\] NAME \[BRANCH\]

## Description

Show info about an installed application or runtime.

By default, the output is formatted in a friendly format. If you specify any of the `--show-…` or `--file-access` options, the output is instead formatted in a machine-readable format.

By default, both per-user and system-wide installations are queried. Use the `--user`, `--system` or `--installation` options to change this.

## Options

The following options are understood:

`-h`, `--help`  
Show help options and exit.

`-u`, `--user`  
Query per-user installations.

`--system`  
Query the default system-wide installation.

`--installation=NAME`  
Query a system-wide installation by NAME among those defined in `/etc/flatpak/installations.d/`. Using `--installation=default` is equivalent to using `--system`.

`--arch=ARCH`  
Query for this architecture. See **flatpak --supported-arches** for architectures supported by the host.

`-r`, `--show-ref`  
Show the installed ref.

`-o`, `--show-origin`  
Show the remote the ref is installed from.

`-c`, `--show-commit`  
Show the installed commit id.

`-s`, `--show-size`  
Show the installed size.

`-m`, `--show-metadata`  
Show the metadata.

`--show-runtime`  
Show the runtime.

`--show-sdk`  
Show the SDK.

`-M`, `--show-permissions`  
Show the permissions.

`--file-access=PATH`  
Show the level of access to the given path.

`-e`, `--show-extensions`  
Show the matching extensions.

`-l`, `--show-location`  
Show the on-disk location of the app or runtime. See the examples below.

`-v`, `--verbose`  
Print debug information during command processing.

`--ostree-verbose`  
Print OSTree debug information during command processing.

## Examples

**\$ flatpak info org.gnome.Builder//master**

**\$ tree \`flatpak info -l org.gnome.Builder//master\`/files**

## See also

[flatpak(1)](#flatpak), [flatpak-install(1)](#flatpak-install), [flatpak-update(1)](#flatpak-update)

## Name

flatpak-install — Install an application or runtime

## Synopsis

`flatpak install` \[OPTION...\] \[REMOTE\] REF...

`flatpak install` \[OPTION...\] \[--from\|--bundle\|--image\] LOCATION

## Description

Installs an application or runtime. The primary way to install is to specify a REMOTE name as the source and one ore more REF s to specify the application or runtime to install. If REMOTE is omitted, the configured remotes are searched for the first REF and the user is asked to confirm the resulting choice.

Each REF argument is a full or partial identifier in the flatpak ref format, which looks like "(app\|runtime)/ID/ARCH/BRANCH". All elements except ID are optional and can be left out, including the slashes, so most of the time you need only specify ID. Any part left out will be matched against what is in the remote, and if there are multiple matches you will be prompted to choose one of them. You will also be prompted with choices if REF doesn't match anything in the remote exactly but is similar to one or more refs in the remote (e.g. "devhelp" is similar to "org.gnome.Devhelp"), but this fuzzy matching behavior is disabled if REF contains any slashes or periods.

By default this looks for both apps and runtimes with the given REF in the specified REMOTE , but you can limit this by using the `--app` or `--runtime` option, or by supplying the initial element in the REF .

If REMOTE is a uri or a path (absolute or relative starting with ./) to a local repository, then that repository will be used as the source, and a temporary remote will be created for the lifetime of the REF .

If the specified REMOTE has a collection ID configured on it, Flatpak will search the `sideload-repos` directories configured either with the `--sideload-repo` option, or on a per-installation or system-wide basis (see [flatpak(1)](#flatpak)).

The alternative form of the command (with `--from`, `--bundle`, or `--image`) allows to install directly from a source. The source can be a `.flatpak` single-file bundle, `.flatpakref` application description, or a reference to an OCI image. The options are optional if the first argument has the expected filename extension or prefix.

Note that flatpak allows to have multiple branches of an application and runtimes installed and used at the same time. However, only one version of an application can be current, meaning its exported files (for instance desktop files and icons) are visible to the host. The last installed version is made current by default, but this can manually changed with flatpak make-current.

Unless overridden with the `--user` or the `--installation` option, this command installs the application or runtime in the default system-wide installation.

## Options

The following options are understood:

`-h`, `--help`  
Show help options and exit.

`--bundle`  
Treat LOCATION as a single-bundle file. This is assumed if the argument ends with `.flatpak`.

`--from`  
Treat LOCATION as an application description file. This is assumed if the argument ends with `.flatpakref`.

`--image`  
Treat LOCATION as the location of a Flatpak in OCI image format. \[LOCATION\] is in the format of [containers-transports(5)](#containers-transports). Supported schemes are `docker://`, `oci:`, and `oci-archive:`. This is assumed if the argument starts with one of these schemes.

`--reinstall`  
Uninstall first if already installed.

`-u`, `--user`  
Install the application or runtime in a per-user installation.

`--system`  
Install the application or runtime in the default system-wide installation.

`--installation=NAME`  
Install the application or runtime in a system-wide installation specified by NAME among those defined in `/etc/flatpak/installations.d/`. Using `--installation=default` is equivalent to using `--system`.

`--arch=ARCH`  
The default architecture to install for, if not given explicitly in the REF . See **flatpak --supported-arches** for architectures supported by the host.

`--subpath=PATH`  
Install only a subpath of REF . This is mainly used to install a subset of locales. This can be added multiple times to install multiple subpaths.

`--gpg-file=FILE`  
Check bundle signatures with GPG key from FILE (- for stdin).

`--no-deploy`  
Download the latest version, but don't deploy it.

`--no-pull`  
Don't download the latest version, deploy whatever is locally available.

`--no-related`  
Don't download related extensions, such as the locale data.

`--no-deps`  
Don't verify runtime dependencies when installing.

`--or-update`  
Normally install just ignores things that are already installed (printing a warning), but if --or-update is specified it silently turns it into an update operation instead.

`--app`  
Assume that all REF s are apps if not explicitly specified.

`--runtime`  
Assume that all REF s are runtimes if not explicitly specified.

`--sideload-repo=PATH`  
Adds an extra local ostree repo as a source for installation. This is equivalent to using the `sideload-repos` directories (see [flatpak(1)](#flatpak)), but can be done on a per-command basis. Any path added here is used in addition to ones in those directories.

`--include-sdk`  
For each app being installed, also installs the SDK that was used to build it. Implies `--or-update`; incompatible with `--no-deps`.

`--include-debug`  
For each ref being installed, as well as all dependencies, also installs its debug info. Implies `--or-update`; incompatible with `--no-deps`.

`-y`, `--assumeyes`  
Automatically answer yes to all questions (or pick the most prioritized answer). This is useful for automation.

`--noninteractive`  
Produce minimal output and avoid most questions. This is suitable for use in non-interactive situations, e.g. in a build script.

`-v`, `--verbose`  
Print debug information during command processing.

`--ostree-verbose`  
Print OSTree debug information during command processing.

## Examples

**\$ flatpak install gedit**

**\$ flatpak install flathub org.gnome.gedit**

**\$ flatpak --installation=default install flathub org.gnome.gedit**

**\$ flatpak --user install flathub org.gnome.gedit//3.30**

**\$ flatpak --user install https://flathub.org/repo/appstream/org.gnome.gedit.flatpakref**

**\$ flatpak --system install org.gnome.gedit.flatpakref**

## See also

[flatpak(1)](#flatpak), [flatpak-update(1)](#flatpak-update), [flatpak-list(1)](#flatpak-list), [flatpak-build-bundle(1)](#flatpak-build-bundle), [flatpakref(5)](#flatpakref), [flatpak-make-current(1)](#flatpak-make-current), [ostree-find-remotes(1)](#ostree-find-remotes)

## Name

flatpak-kill — Stop a running application

## Synopsis

`flatpak kill` INSTANCE

## Description

Stop a running Flatpak instance.

INSTANCE can be either the numeric instance ID or the application ID of a running Flatpak. You can use **flatpak ps** to find the instance IDs of running flatpaks.

## Options

The following options are understood:

`-h`, `--help`  
Show help options and exit.

`-v`, `--verbose`  
Print debug information during command processing.

`--ostree-verbose`  
Print OSTree debug information during command processing.

## Examples

**\$ flatpak kill org.gnome.Todo**

## See also

[flatpak(1)](#flatpak), [flatpak-run(1)](#flatpak-run), [flatpak-ps(1)](#flatpak-ps)

## Name

flatpak-list — List installed applications and/or runtimes

## Synopsis

`flatpak list` \[OPTION...\]

## Description

Lists the names of the installed applications and runtimes.

By default, both apps and runtimes are shown, but you can change this by using the `--app` or `--runtime` options.

By default, both per-user and system-wide installations are shown. Use the `--user`, `--installation` or `--system` options to change this.

The list command can also be used to find installed apps that use a certain runtime, with the `--app-runtime` option.

## Options

The following options are understood:

`-h`, `--help`  
Show help options and exit.

`-u`, `--user`  
List per-user installations.

`--system`  
List the default system-wide installations.

`--installation=NAME`  
List a system-wide installation specified by NAME among those defined in `/etc/flatpak/installations.d/`. Using `--installation=default` is equivalent to using `--system`.

`--arch=ARCH`  
List apps/runtimes for this architecture. See **flatpak --supported-arches** for architectures supported by the host.

`-d`, `--show-details`  
Show origin, sizes and other extra information. Equivalent to `--columns=all`.

`--app`  
List applications.

`--runtime`  
List runtimes.

`--all`, `-a`  
List all installed runtimes, including locale and debug extensions. These are hidden by default.

`--app-runtime=RUNTIME`  
List applications that use the given runtime.

`-v`, `--verbose`  
Print debug information during command processing.

`--ostree-verbose`  
Print OSTree debug information during command processing.

`--columns=FIELD,…`  
Specify what information to show about each ref. You can list multiple fields, or use this option multiple times.

Append :s\[tart\], :m\[iddle\], :e\[nd\] or :f\[ull\] to column names to change ellipsization.

## Fields

The following fields are understood by the `--columns` option:

name  
Show the name

description  
Show the description

application  
Show the application or runtime ID

arch  
Show the architecture

branch  
Show the branch

runtime  
Show the used runtime

version  
Show the version

ref  
Show the ref

origin  
Show the origin remote

installation  
Show the installation

active  
Show the active commit

latest  
Show the latest commit

size  
Show the installed size

options  
Show options

all  
Show all columns

help  
Show the list of available columns

Note that field names can be abbreviated to a unique prefix.

## Examples

**\$ flatpak --user --columns=app list**

``` programlisting
Application
org.gnome.Builder
org.freedesktop.glxgears
org.gnome.MyApp
org.gnome.gedit
```

## See also

[flatpak(1)](#flatpak), [flatpak-install(1)](#flatpak-install), [flatpak-update(1)](#flatpak-update)

## Name

flatpak-make-current — Make a specific version of an app current

## Synopsis

`flatpak make-current` \[OPTION...\] APP BRANCH

## Description

Makes a particular branch of an application current. Only the current branch of an app has its exported files (such as desktop files and icons) made visible to the host.

When a new branch is installed it will automatically be made current, so this command is often not needed.

Unless overridden with the `--user` or `--installation` options, this command changes the default system-wide installation.

## Options

The following options are understood:

`-h`, `--help`  
Show help options and exit.

`-u`, `--user`  
Update a per-user installation.

`--system`  
Update the default system-wide installation.

`--installation=NAME`  
Updates a system-wide installation specified by NAME among those defined in `/etc/flatpak/installations.d/`. Using `--installation=default` is equivalent to using `--system`.

`--arch=ARCH`  
The architecture to make current for. See **flatpak --supported-arches** for architectures supported by the host.

`-v`, `--verbose`  
Print debug information during command processing.

`--ostree-verbose`  
Print OSTree debug information during command processing.

## Examples

**\$ flatpak --user make-current org.gnome.gedit 3.14**

## See also

[flatpak(1)](#flatpak), [flatpak-install(1)](#flatpak-install), [flatpak-list(1)](#flatpak-list)

## Name

flatpak-override — Override application requirements

## Synopsis

`flatpak override` \[OPTION...\] \[APP\]

## Description

Overrides the application specified runtime requirements. This can be used to grant a sandboxed application more or less resources than it requested.

By default the application gets access to the resources it requested when it is started. But the user can override it on a particular instance by specifying extra arguments to **flatpak run**, or every time by using **flatpak override**.

The application overrides are saved in text files residing in \$XDG_DATA_HOME/flatpak/overrides in user mode.

If the application ID APP is not specified then the overrides affect all applications, but the per-application overrides can override the global overrides.

Unless overridden with the `--user` or `--installation` options, this command changes the default system-wide installation.

## Options

The following options are understood:

`-h`, `--help`  
Show help options and exit.

`-u`, `--user`  
Update a per-user installation.

`--system`  
Update the default system-wide installation.

`--installation=NAME`  
Updates a system-wide installation specified by NAME among those defined in `/etc/flatpak/installations.d/`. Using `--installation=default` is equivalent to using `--system`.

`--share=SUBSYSTEM`  
Share a subsystem with the host session. This overrides the Context section from the application metadata. SUBSYSTEM must be one of: network, ipc. This option can be used multiple times.

`--unshare=SUBSYSTEM`  
Don't share a subsystem with the host session. This overrides the Context section from the application metadata. SUBSYSTEM must be one of: network, ipc. This option can be used multiple times.

`--socket=SOCKET`  
Expose a well-known socket to the application. This overrides to the Context section from the application metadata. SOCKET must be one of: x11, wayland, fallback-x11, pulseaudio, system-bus, session-bus, ssh-auth, pcsc, cups, gpg-agent, inherit-wayland-socket. This option can be used multiple times.

`--nosocket=SOCKET`  
Don't expose a well-known socket to the application. This overrides to the Context section from the application metadata. SOCKET must be one of: x11, wayland, fallback-x11, pulseaudio, system-bus, session-bus, ssh-auth, pcsc, cups, gpg-agent, inherit-wayland-socket. This option can be used multiple times.

`--device=DEVICE`  
Expose a device to the application. This overrides to the Context section from the application metadata. DEVICE must be one of: dri, input, usb, kvm, shm, all. This option can be used multiple times.

`--nodevice=DEVICE`  
Don't expose a device to the application. This overrides to the Context section from the application metadata. DEVICE must be one of: dri, input, usb, kvm, shm, all. This option can be used multiple times.

`--allow=FEATURE`  
Allow access to a specific feature. This updates the \[Context\] group in the metadata. FEATURE must be one of: devel, multiarch, bluetooth, canbus, per-app-dev-shm. This option can be used multiple times.

See [flatpak-build-finish(1)](#flatpak-build-finish) for the meaning of the various features.

`--disallow=FEATURE`  
Disallow access to a specific feature. This updates the \[Context\] group in the metadata. FEATURE must be one of: devel, multiarch, bluetooth, canbus, per-app-dev-shm. This option can be used multiple times.

`--filesystem=FILESYSTEM`  
Allow the application access to a subset of the filesystem. This overrides to the Context section from the application metadata. FILESYSTEM can be one of: home, host, host-os, host-etc, host-root, xdg-desktop, xdg-documents, xdg-download, xdg-music, xdg-pictures, xdg-public-share, xdg-templates, xdg-videos, xdg-run, xdg-config, xdg-cache, xdg-data, an absolute path, or a homedir-relative path like ~/dir or paths relative to the xdg dirs, like xdg-download/subdir. The optional :ro suffix indicates that the location will be read-only. The optional :create suffix indicates that the location will be read-write and created if it doesn't exist. This option can be used multiple times. See the "\[Context\] filesystems" list in [flatpak-metadata(5)](#flatpak-metadata) for details of the meanings of these filesystems.

`--nofilesystem=FILESYSTEM`  
Undo the effect of a previous `--filesystem=` FILESYSTEM in the app's manifest or a lower-precedence layer of overrides, and/or remove a previous `--filesystem=` FILESYSTEM from this layer of overrides. This overrides the Context section of the application metadata. FILESYSTEM can take the same values as for `--filesystem`, but the :ro and :create suffixes are not used here. This option can be used multiple times.

This option does not prevent access to a more narrowly-scoped `--filesystem`. For example, if an application has the equivalent of `--filesystem=xdg-config/MyApp` in its manifest or as a system-wide override, and `flatpak override --user --nofilesystem=home` as a per-user override, then it will be prevented from accessing most of the home directory, but it will still be allowed to access `$XDG_CONFIG_HOME/MyApp`.

As a special case, `--nofilesystem=host:reset` will ignore all `--filesystem` permissions inherited from the app manifest or a lower-precedence layer of overrides, in addition to having the behaviour of `--nofilesystem=host`.

`--add-policy=SUBSYSTEM.KEY=VALUE`  
Add generic policy option. For example, "--add-policy=subsystem.key=v1 --add-policy=subsystem.key=v2" would map to this metadata:

``` programlisting
[Policy subsystem]
key=v1;v2;
```

This option can be used multiple times.

`--remove-policy=SUBSYSTEM.KEY=VALUE`  
Remove generic policy option. This option can be used multiple times.

`--env=VAR=VALUE`  
Set an environment variable in the application. This overrides to the Context section from the application metadata. This option can be used multiple times.

`--unset-env=VAR`  
Unset an environment variable in the application. This overrides the unset-environment entry in the \[Context\] group of the metadata, and the \[Environment\] group. This option can be used multiple times.

`--env-fd=`*`FD`*  
Read environment variables from the file descriptor *`FD`*, and set them as if via `--env`. This can be used to avoid environment variables and their values becoming visible to other users.

Each environment variable is in the form *`VAR`*=*`VALUE`* followed by a zero byte. This is the same format used by `env -0` and `/proc/*/environ`.

`--own-name=NAME`  
Allow the application to own the well-known name NAME on the session bus. This overrides to the Context section from the application metadata. This option can be used multiple times.

`--talk-name=NAME`  
Allow the application to talk to the well-known name NAME on the session bus. This overrides to the Context section from the application metadata. This option can be used multiple times.

`--no-talk-name=NAME`  
Don't allow the application to talk to the well-known name NAME on the session bus. This overrides to the Context section from the application metadata. This option can be used multiple times.

`--system-own-name=NAME`  
Allow the application to own the well known name NAME on the system bus. If NAME ends with .\*, it allows the application to own all matching names. This overrides to the Context section from the application metadata. This option can be used multiple times.

`--system-talk-name=NAME`  
Allow the application to talk to the well known name NAME on the system bus. If NAME ends with .\*, it allows the application to talk to all matching names. This overrides to the Context section from the application metadata. This option can be used multiple times.

`--system-no-talk-name=NAME`  
Don't allow the application to talk to the well known name NAME on the system bus. If NAME ends with .\*, it allows the application to talk to all matching names. This overrides to the Context section from the application metadata. This option can be used multiple times.

`--persist=FILENAME`  
If the application doesn't have access to the real homedir, make the (homedir-relative) path FILENAME a bind mount to the corresponding path in the per-application directory, allowing that location to be used for persistent data. This overrides to the Context section from the application metadata. This option can be used multiple times.

`--reset`  
Remove overrides. If an APP is given, remove the overrides for that application, otherwise remove the global overrides.

`--show`  
Shows overrides. If an APP is given, shows the overrides for that application, otherwise shows the global overrides.

`-v`, `--verbose`  
Print debug information during command processing.

`--ostree-verbose`  
Print OSTree debug information during command processing.

## Examples

**\$ flatpak override --nosocket=wayland org.gnome.gedit**

**\$ flatpak override --filesystem=home org.mozilla.Firefox**

## See also

[flatpak(1)](#flatpak), [flatpak-run(1)](#flatpak-run)

## Name

flatpak-permission-remove — Remove permissions

## Synopsis

`flatpak permission-remove` \[OPTION...\] TABLE ID \[APP_ID\]

## Description

Removes an entry for the object with id ID to the permission store table TABLE . The ID must be in a suitable format for the table. If APP_ID is specified, only the entry for that application is removed.

The permission store is used by portals. Each portal generally has its own table in the permission store, and the format of the table entries is specific to each portal.

## Options

The following options are understood:

`-h`, `--help`  
Show help options and exit.

`-v`, `--verbose`  
Print debug information during command processing.

`--ostree-verbose`  
Print OSTree debug information during command processing.

## See also

[flatpak(1)](#flatpak), [flatpak-permissions(1)](#flatpak-permissions), [flatpak-permission-show(1)](#flatpak-permission-show), [flatpak-permission-reset(1)](#flatpak-permission-reset), [flatpak-permission-set(1)](#flatpak-permission-set)

## Name

flatpak-permissions — List permissions

## Synopsis

`flatpak permissions` \[OPTION...\] \[TABLE\] \[ID\]

## Description

Lists dynamic permissions which are stored in the Flatpak permission store.

When called without arguments, lists all the entries in all permission store tables. When called with one argument, lists all the entries in the named table. When called with two arguments, lists the entry in the named table for the given object ID .

The permission store is used by portals. Each portal generally has its own table in the permission store, and the format of the table entries is specific to each portal.

## Options

The following options are understood:

`-h`, `--help`  
Show help options and exit.

`-v`, `--verbose`  
Print debug information during command processing.

`--ostree-verbose`  
Print OSTree debug information during command processing.

## See also

[flatpak(1)](#flatpak), [flatpak-permission-show(1)](#flatpak-permission-show), [flatpak-permission-remove(1)](#flatpak-permission-remove), [flatpak-permission-reset(1)](#flatpak-permission-reset), [flatpak-permission-set(1)](#flatpak-permission-set)

## Name

flatpak-permission-show — Show permissions

## Synopsis

`flatpak permission-show` \[OPTION...\] APP_ID

## Description

Lists dynamic permissions for the given app which are stored in the Flatpak permission store.

The permission store is used by portals. Each portal generally has its own table in the permission store, and the format of the table entries is specific to each portal.

## Options

The following options are understood:

`-h`, `--help`  
Show help options and exit.

`-v`, `--verbose`  
Print debug information during command processing.

`--ostree-verbose`  
Print OSTree debug information during command processing.

## See also

[flatpak(1)](#flatpak), [flatpak-permissions(1)](#flatpak-permissions), [flatpak-permission-remove(1)](#flatpak-permission-remove), [flatpak-permission-reset(1)](#flatpak-permission-reset), [flatpak-permission-set(1)](#flatpak-permission-set)

## Name

flatpak-permission-reset — Reset permissions

## Synopsis

`flatpak permission-reset` \[OPTION...\] APP_ID

`flatpak permission-reset` \[OPTION...\] --all

## Description

Removes all permissions for the given app from the Flatpak permission store.

The permission store is used by portals. Each portal generally has its own table in the permission store, and the format of the table entries is specific to each portal.

## Options

The following options are understood:

`--all`  
Remove permissions for all applications.

`-h`, `--help`  
Show help options and exit.

`-v`, `--verbose`  
Print debug information during command processing.

`--ostree-verbose`  
Print OSTree debug information during command processing.

## See also

[flatpak(1)](#flatpak), [flatpak-permissions(1)](#flatpak-permissions), [flatpak-permission-show(1)](#flatpak-permission-show), [flatpak-permission-remove(1)](#flatpak-permission-remove), [flatpak-permission-set(1)](#flatpak-permission-set)

## Name

flatpak-permission-set — Set permissions

## Synopsis

`flatpak permission-set` \[OPTION...\] TABLE ID APP_ID \[PERMISSION...\]

## Description

Set the permissions for an application in an entry in the permission store. The entry is identified by TABLE and ID, the application is identified by APP_ID. The PERMISSION strings must be in a format suitable for the table.

The permission store is used by portals. Each portal generally has its own table in the permission store, and the format of the table entries is specific to each portal.

## Options

The following options are understood:

`-h`, `--help`  
Show help options and exit.

`--data=DATA`  
Associate DATA with the entry. The data must be a serialized GVariant.

`-v`, `--verbose`  
Print debug information during command processing.

`--ostree-verbose`  
Print OSTree debug information during command processing.

## Examples

**\$ flatpak permission-set --data "{'always-ask':\<true\>}" desktop-used-apps text/plain org.mozilla.Firefox org.gnome.gedit 0 3**

## See also

[flatpak(1)](#flatpak), [flatpak-permissions(1)](#flatpak-permissions), [flatpak-permission-remove(1)](#flatpak-permission-remove), [flatpak-permission-reset(1)](#flatpak-permission-reset), [flatpak-permission-show(1)](#flatpak-permission-show)

## Name

flatpak-preinstall — Install flatpaks that are part of the operating system

## Synopsis

`flatpak preinstall` \[OPTION...\]

## Description

This command manages flatpaks that are part of the operating system. If no options are given, running **flatpak preinstall** will synchronize (install and remove) flatpaks to match the set that the OS vendor has chosen.

Preinstalled flatpaks are defined by dropping .preinstall files into the directories `/usr/share/flatpak/preinstall.d/` and `/etc/flatpak/preinstall.d/`. The OS runs **flatpak preinstall -y** (or its GUI equivalent) on system startup, which then does the actual installation.

This system allows the OS vendor to define the list of flatpaks that are installed together with the OS, and also makes it possible for the OS vendor to make changes to the list in the future, which is then applied once **flatpak preinstall** is run next time. Users can opt out of preinstalled flatpaks by simply uninstalling them, at which point they won't get automatically reinstalled again.

## File format

The .preinstall file is using the same .ini file format that is used for systemd unit files or application .desktop files.

### \[Flatpak Preinstall NAME\]

The NAME is the fully qualified name of the runtime or application. All the information for a single runtime or application is contained in one \[Flatpak Preinstall NAME\] group. Multiple groups can be defined in a single file.

The following keys can be present in this group:

`Install` (boolean)  
Whether this group should be installed. If this key is not specified, the group will be installed.

`Branch` (string)  
The name of the branch from which to install the application or runtime. If this key is not specified, the "master" branch is used.

`IsRuntime` (boolean)  
Whether this group refers to a runtime. If this key is not specified, the group is assumed to refer to an application.

`CollectionID` (string)  
The collection ID of the remote to use, if it has one.

## Example

``` programlisting
[Flatpak Preinstall org.gnome.Loupe]
Branch=stable
IsRuntime=false
```

## Options

The following options are understood:

`-h`, `--help`  
Show help options and exit.

`--reinstall`  
Uninstall first if already installed.

`-u`, `--user`  
Install the application or runtime in a per-user installation.

`--system`  
Install the application or runtime in the default system-wide installation.

`--installation=NAME`  
Install the application or runtime in a system-wide installation specified by NAME among those defined in `/etc/flatpak/installations.d/`. Using `--installation=default` is equivalent to using `--system`.

`--no-deploy`  
Download the latest version, but don't deploy it.

`--no-pull`  
Don't download the latest version, deploy whatever is locally available.

`--no-related`  
Don't download related extensions, such as the locale data.

`--no-deps`  
Don't verify runtime dependencies when installing.

`--sideload-repo=PATH`  
Adds an extra local ostree repo as a source for installation. This is equivalent to using the `sideload-repos` directories (see [flatpak(1)](#flatpak)), but can be done on a per-command basis. Any path added here is used in addition to ones in those directories.

`--include-sdk`  
For each app being installed, also installs the SDK that was used to build it. Implies `--or-update`; incompatible with `--no-deps`.

`--include-debug`  
For each ref being installed, as well as all dependencies, also installs its debug info. Implies `--or-update`; incompatible with `--no-deps`.

`-y`, `--assumeyes`  
Automatically answer yes to all questions (or pick the most prioritized answer). This is useful for automation.

`--noninteractive`  
Produce minimal output and avoid most questions. This is suitable for use in non-interactive situations, e.g. in a build script.

`-v`, `--verbose`  
Print debug information during command processing.

`--ostree-verbose`  
Print OSTree debug information during command processing.

## Examples

**\$ flatpak preinstall**

## See also

[flatpak(1)](#flatpak),

## Name

flatpak-ps — Enumerate running instances

## Synopsis

`flatpak ps` \[OPTION...\]

## Description

Lists useful information about running Flatpak instances.

To see full details of a running instance, you can open the file `/run/user/$UID/.flatpak/$INSTANCE/info`, where *`$INSTANCE`* is the instance ID reported by flatpak ps.

## Options

The following options are understood:

`-h`, `--help`  
Show help options and exit.

`-v`, `--verbose`  
Print debug information during command processing.

`--ostree-verbose`  
Print OSTree debug information during command processing.

`--columns=FIELD,…`  
Specify what information to show about each instance. You can list multiple fields, or use this option multiple times.

Append :s\[tart\], :m\[iddle\], :e\[nd\] or :f\[ull\] to column names to change ellipsization.

## Fields

The following fields are understood by the `--columns` option:

instance  
Show the instance ID

application  
Show the application ID

arch  
Show the architecture

branch  
Show the application branch

commit  
Show the application commit

runtime  
Show the runtime ID

runtime-branch  
Show the runtime branch

runtime-commit  
Show the runtime commit

pid  
Show the PID of the wrapper process

child-pid  
Show the PID of the sandbox process

active  
Show whether the app is active (i.e. has an active window)

background  
Show whether the app is in the background (with no open windows)

all  
Show all columns

help  
Show the list of available columns

Note that field names can be abbreviated to a unique prefix.

## Examples

**\$ flatpak ps --columns=application,pid,runtime,runtime-branch**

## See also

[flatpak(1)](#flatpak), [flatpak-run(1)](#flatpak-run)

## Name

flatpak-remote-add — Add a remote repository

## Synopsis

`flatpak remote-add` \[OPTION...\] NAME LOCATION

## Description

Adds a remote repository to the flatpak repository configuration. NAME is the name for the new remote, and LOCATION is a url or pathname. The LOCATION is either a flatpak repository, or a `.flatpakrepo` file which describes a repository. In the former case you may also have to specify extra options, such as the gpg key for the repo.

Unless overridden with the `--user` or `--installation` options, this command changes the default system-wide installation.

## Options

The following options are understood:

`-h`, `--help`  
Show help options and exit.

`--from`  
Assume the URI is a .flatpakrepo file rather than the repository itself. This is enabled by default if the extension is .flatpakrepo, so generally you don't need this option.

`-u`, `--user`  
Modify the per-user configuration.

`--system`  
Modify the default system-wide configuration.

`--installation=NAME`  
Modify a system-wide installation specified by NAME among those defined in `/etc/flatpak/installations.d/`. Using `--installation=default` is equivalent to using `--system`.

`--no-gpg-verify`  
Disable GPG verification for the added remote.

`--prio=PRIO`  
Set the priority for the remote. Default is 1, higher is more prioritized. This is mainly used for graphical installation tools. It is also used when searching for a remote to provide an app's runtime. The app's origin is checked before other remotes with the same priority.

`--subset=SUBSET`  
Limit the refs available from the remote to those that are part of the named subset.

`--no-enumerate`  
Mark the remote as not enumerated. This means the remote will not be used to list applications, for instance in graphical installation tools.

`--no-use-for-deps`  
Mark the remote as not to be used for automatic runtime dependency resolution.

`--if-not-exists`  
Do nothing if the provided remote already exists.

`--disable`  
Disable the added remote.

`--title=TITLE`  
A title for the remote, e.g. for display in a UI.

`--comment=COMMENT`  
A single-line comment for the remote, e.g. for display in a UI.

`--description=DESCRIPTION`  
A full-paragraph description for the remote, e.g. for display in a UI.

`--homepage=URL`  
URL for a website for the remote, e.g. for display in a UI.

`--icon=URL`  
URL for an icon for the remote, e.g. for display in a UI.

`--default-branch=BRANCH`  
A default branch for the remote, mainly for use in a UI.

`--filter=PATH`  
Add a local filter to the remote. A filter file is a list of lines, each file starting with "allow" or "deny", and then a glob for the ref to allow or disallow. The globs specify a partial ref (i.e. you can leave out trailing parts which will then match everything), but otherwise only "\*" is special, matching anything in that part of the ref.

By default all refs are allowed, but if a ref matches a deny rule it is disallowed unless it specifically matches an allow rule. This means you can use this to implement both allowlisting and blocklisting.

Here is an example filter file:

``` programlisting
# This is an allowlist style filter as it denies all first
deny *
allow runtime/org.freedesktop.*
allow org.some.app/arm
allow org.signal.Signal/*/stable
allow org.signal.Signal.*/*/stable
```

`--gpg-import=FILE`  
Import gpg keys from the specified keyring file as trusted for the new remote. If the file is - the keyring is read from standard input.

`--authenticator-name=NAME`  
Specify the authenticator to use for the remote.

`--authenticator-option=KEY=VALUE`  
Specify an authenticator option for the remote.

`--authenticator-install`  
Enable auto-installation of authenticator.

`--no-authenticator-install`  
Disable auto-installation of authenticator.

`--no-follow-redirect`  
Do not follow xa.redirect-url defined in the summary file.

`-v`, `--verbose`  
Print debug information during command processing.

`--ostree-verbose`  
Print OSTree debug information during command processing.

## Examples

**\$ flatpak remote-add gnome https://sdk.gnome.org/gnome.flatpakrepo**

**\$ flatpak --user remote-add --no-gpg-verify test-repo https://people.gnome.org/~alexl/gnome-sdk/repo/**

## See also

[flatpak(1)](#flatpak), [flatpak-remote-modify(1)](#flatpak-remote-modify), [flatpak-remote-delete(1)](#flatpak-remote-delete), [flatpak-remotes(1)](#flatpak-remotes), [flatpakrepo(5)](#flatpakrepo)

## Name

flatpak-remote-delete — Delete a remote repository

## Synopsis

`flatpak remote-delete` \[OPTION...\] NAME

## Description

Removes a remote repository from the flatpak repository configuration. NAME is the name of an existing remote.

Unless overridden with the `--system`, `--user`, or `--installation` options, this command uses either the default system-wide installation or the per-user one, depending on which has the specified REMOTE .

## Options

The following options are understood:

`-h`, `--help`  
Show help options and exit.

`-u`, `--user`  
Modify the per-user configuration.

`--system`  
Modify the default system-wide configuration.

`--installation=NAME`  
Modify a system-wide installation specified by NAME among those defined in `/etc/flatpak/installations.d/`. Using `--installation=default` is equivalent to using `--system`.

`--force`  
Remove remote even if its in use by installed apps or runtimes.

`-v`, `--verbose`  
Print debug information during command processing.

`--ostree-verbose`  
Print OSTree debug information during command processing.

## Examples

**\$ flatpak --user remote-delete dried-raisins**

## See also

[flatpak(1)](#flatpak), [flatpak-remote-add(1)](#flatpak-remote-add), [flatpak-remote-modify(1)](#flatpak-remote-modify), [flatpak-remotes(1)](#flatpak-remotes)

## Name

flatpak-remote-info — Show information about an application or runtime in a remote

## Synopsis

`flatpak remote-info` \[OPTION...\] REMOTE REF

## Description

Shows information about the runtime or application REF from the remote repository with the name REMOTE . You can find all configured remote repositories with flatpak remotes.

By default, the output is formatted in a friendly format. If you specify one of the `--show-…` options, the output is instead formatted in a machine-readable format.

Unless overridden with the `--system`, `--user`, or `--installation` options, this command uses either the default system-wide installation or the per-user one, depending on which has the specified REMOTE .

## Options

The following options are understood:

`-h`, `--help`  
Show help options and exit.

`-u`, `--user`  
Use the per-user configuration.

`--system`  
Use the default system-wide configuration.

`--installation=NAME`  
Use a system-wide installation specified by NAME among those defined in `/etc/flatpak/installations.d/`. Using `--installation=default` is equivalent to using `--system`.

`--cached`  
Prefer to use locally cached information if possible, even though it may be out of date. This is faster, but risks returning stale information. Also, some information is not cached so will not be available.

`--runtime`  
Assume that REF is a runtime if not explicitly specified.

`--app`  
Assume that REF is an app if not explicitly specified.

`--arch=ARCH`  
The default architecture to look for, if not given explicitly in the REF . See **flatpak --supported-arches** for architectures supported by the host.

`--commit=COMMIT`  
Show information about the specific commit, rather than the latest version.

`--log`  
Display a log of previous versions.

`-r`, `--show-ref`  
Show the matched ref.

`-c`, `--show-commit`  
Show the commit id.

`-p`, `--show-parent`  
Show the parent commit id.

`-m`, `--show-metadata`  
Show the metadata.

`-v`, `--verbose`  
Print debug information during command processing.

`--ostree-verbose`  
Print OSTree debug information during command processing.

## Examples

**\$ flatpak --user remote-info flathub org.gnome.gedit**

``` programlisting
Ref: app/org.gnome.gedit/x86_64/stable
ID: org.gnome.gedit
Arch: x86_64
Branch: stable
Date: 2017-07-31 16:05:22 +0000
Subject: Build org.gnome.gedit at 3ec291fc1ce4d78220527fa79576f4cc1481ebe5
Commit: 3de7e9dde3bb8382aad9dfbbff20eccd9bf2100bc1887a3619ec0372e8066bf7
Parent: -
Download size: 3,4 MB
Installed size: 11,1 MB
Runtime: org.gnome.Platform/x86_64/3.24
```

## See also

[flatpak(1)](#flatpak), [flatpak-remotes(1)](#flatpak-remotes) [flatpak-remote-ls(1)](#flatpak-remote-ls)

## Name

flatpak-remote-ls — Show available runtimes and applications

## Synopsis

`flatpak remote-ls` \[OPTION...\] \[REMOTE\]

## Description

Shows runtimes and applications that are available in the remote repository with the name REMOTE , or all remotes if one isn't specified. You can find all configured remote repositories with **flatpak remotes**.

REMOTE can be a file:// URI pointing to a local repository instead of a remote name.

Unless overridden with the `--system`, `--user`, or `--installation` options, this command uses either the default system-wide installation or the per-user one, depending on which has the specified REMOTE .

## Options

The following options are understood:

`-h`, `--help`  
Show help options and exit.

`-u`, `--user`  
Use the per-user configuration.

`--system`  
Use the default system-wide configuration.

`--installation=NAME`  
Use a system-wide installation specified by NAME among those defined in `/etc/flatpak/installations.d/`. Using `--installation=default` is equivalent to using `--system`.

`--cached`  
Prefer to use locally cached information if possible, even though it may be out of date. This is faster, but risks returning stale information.

`-d`, `--show-details`  
Show arches, branches and commit ids, in addition to the names. Equivalent to `--columns=all`.

`--runtime`  
Show only runtimes, omit applications.

`--app`  
Show only applications, omit runtimes.

`--all`, `-a`  
Show everything. By default locale and debug extensions as well as secondary arches when the primary arch is available are hidden.

`--updates`  
Show only those which have updates available.

`--arch=ARCH`  
Show only those matching the specified architecture. By default, only supported architectures are shown. Use `--arch=*` to show all architectures. See **flatpak --supported-arches** for architectures supported by the host.

`-v`, `--verbose`  
Print debug information during command processing.

`--ostree-verbose`  
Print OSTree debug information during command processing.

`--app-runtime=RUNTIME`  
List applications that use the given runtime

`--columns=FIELD,…`  
Specify what information to show about each ref. You can list multiple fields, or use this option multiple times.

Append :s\[tart\], :m\[iddle\], :e\[nd\] or :f\[ull\] to column names to change ellipsization.

## Fields

The following fields are understood by the `--columns` option:

name  
Show the name

description  
Show the application description

application  
Show the application or runtime ID

arch  
Show the arch

branch  
Show the branch

version  
Show the version

ref  
Show the ref

origin  
Show the origin remote

commit  
Show the active commit

runtime  
Show the used runtime

installed-size  
Show the installed size

download-size  
Show the download size

options  
Show options

all  
Show all columns

help  
Show the list of available columns

Note that field names can be abbreviated to a unique prefix.

## Examples

**\$ flatpak --user remote-ls --app testrepo**

``` programlisting
Ref
org.gnome.Builder
org.freedesktop.glxgears
```

**\$ flatpak remote-ls file:///run/media/mwleeds/d4d37026-cde2-4e5e-8bcc-d23ebbf231f9/.ostree/repo**

``` programlisting
Ref
org.kde.Khangman
```

## See also

[flatpak(1)](#flatpak), [flatpak-remotes(1)](#flatpak-remotes)

## Name

flatpak-remote-modify — Modify a remote repository

## Synopsis

`flatpak remote-modify` \[OPTION...\] NAME

## Description

Modifies options for an existing remote repository in the flatpak repository configuration. NAME is the name for the remote.

Unless overridden with the `--system`, `--user`, or `--installation` options, this command uses either the default system-wide installation or the per-user one, depending on which has the specified REMOTE .

## Options

The following options are understood:

`-h`, `--help`  
Show help options and exit.

`-u`, `--user`  
Modify the per-user configuration.

`--system`  
Modify the default system-wide configuration.

`--installation=NAME`  
Modify a system-wide installation specified by NAME among those defined in `/etc/flatpak/installations.d/`. Using `--installation=default` is equivalent to using `--system`.

`--no-gpg-verify`  
Disable GPG verification for the added remote.

`--gpg-verify`  
Enable GPG verification for the added remote.

`--prio=PRIO`  
Set the priority for the remote. Default is 1, higher is more prioritized. This is mainly used for graphical installation tools.

`--subset=SUBSET`  
Limit the refs available from the remote to those that are part of the named subset.

`--no-enumerate`  
Mark the remote as not enumerated. This means the remote will not be used to list applications, for instance in graphical installation tools. It will also not be used for runtime dependency resolution (as with `--no-use-for-deps`).

`--no-use-for-deps`  
Mark the remote as not to be used for automatic runtime dependency resolution.

`--disable`  
Disable the remote. Disabled remotes will not be automatically updated from.

`--enable`  
Enable the remote.

`--enumerate`  
Mark the remote as enumerated. This means the remote will be used to list applications, for instance in graphical installation tools.

`--use-for-deps`  
Mark the remote as to be used for automatic runtime dependency resolution.

`--title=TITLE`  
A title for the remote, e.g. for display in a UI.

`--comment=COMMENT`  
A single-line comment for the remote, e.g. for display in a UI.

`--description=DESCRIPTION`  
A full-paragraph description for the remote, e.g. for display in a UI.

`--homepage=URL`  
URL for a website for the remote, e.g. for display in a UI.

`--icon=URL`  
URL for an icon for the remote, e.g. for display in a UI.

`--default-branch=BRANCH`  
A default branch for the remote, mainly for use in a UI.

`--collection-id=COLLECTION-ID`  
The globally unique identifier of the remote repository, to allow mirrors to be grouped. This must only be set to the collection ID provided by the remote, and must not be set if the remote does not provide a collection ID.

`--url=URL`  
Set a new URL.

`--update-metadata`  
Update the remote's extra metadata from the OSTree repository's summary file. Only xa.title and xa.default-branch are supported at the moment.

`--no-filter`, `--filter=FILE`  
Modify the path (or unset) for the local filter used for this remote. See [flatpak-remote-add(1)](#flatpak-remote-add) for details about the filter file format.

`--gpg-import=FILE`  
Import gpg keys from the specified keyring file as trusted for the new remote. If the file is - the keyring is read from standard input.

`--authenticator-name=NAME`  
Specify the authenticator to use for the remote.

`--authenticator-option=KEY=VALUE`  
Specify an authenticator option for the remote.

`--authenticator-install`  
Enable auto-installation of authenticator.

`--no-authenticator-install`  
Disable auto-installation of authenticator.

`--follow-redirect`  
Follow xa.redirect-url defined in the summary file.

`--no-follow-redirect`  
Do not follow xa.redirect-url defined in the summary file.

`-v`, `--verbose`  
Print debug information during command processing.

`--ostree-verbose`  
Print OSTree debug information during command processing.

## Examples

**\$ flatpak --user remote-modify --no-gpg-verify test-repo**

## See also

[flatpak(1)](#flatpak), [flatpak-remote-add(1)](#flatpak-remote-add), [flatpak-remote-delete(1)](#flatpak-remote-delete), [flatpak-remotes(1)](#flatpak-remotes)

## Name

flatpak-remotes — List remote repositories

## Synopsis

`flatpak remotes` \[OPTION...\]

## Description

Lists the known remote repositories, in priority order.

By default, both per-user and system-wide installations are shown. Use the `--user`, `--system` or `--installation` options to change this.

## Options

The following options are understood:

`-h`, `--help`  
Show help options and exit.

`-u`, `--user`  
Show the per-user configuration.

`--system`  
Show the default system-wide configuration.

`--installation=NAME`  
Show a system-wide installation by NAME among those defined in `/etc/flatpak/installations.d/`. Using `--installation=default` is equivalent to using `--system`.

`-d`, `--show-details`  
Show more information for each repository in addition to the name. Equivalent to `--columns=all`.

`--show-disabled`  
Show disabled repos.

`-v`, `--verbose`  
Print debug information during command processing.

`--ostree-verbose`  
Print OSTree debug information during command processing.

`--columns=FIELD,…`  
Specify what information to show about each ref. You can list multiple fields, or use this option multiple times.

Append :s\[tart\], :m\[iddle\], :e\[nd\] or :f\[ull\] to column names to change ellipsization.

## Fields

The following fields are understood by the `--columns` option:

name  
Show the name of the remote

title  
Show the title of the remote

url  
Show the URL of the remote

filter  
Show the path to the client-side filter of the remote.

collection  
Show the collection ID of the remote

priority  
Show the priority of the remote

options  
Show options

comment  
Show comment

description  
Show description

homepage  
Show homepage

icon  
Show icon

all  
Show all columns

help  
Show the list of available columns

Note that field names can be abbreviated to a unique prefix.

## Examples

**\$ flatpak remotes --user --show-details**

``` programlisting
testrepo    Test Repository  http://209.132.179.91/repo/ no-gpg-verify
```

## See also

[flatpak(1)](#flatpak), [flatpak-remote-add(1)](#flatpak-remote-add), [flatpak-remote-delete(1)](#flatpak-remote-delete)

## Name

flatpak-repair — Repair a flatpak installation

## Synopsis

`flatpak repair` \[OPTION...\]

## Description

Repair a flatpak installation by pruning and reinstalling invalid objects. The repair command does all of the following:

- Scan all locally available refs, removing any that don't correspond to a deployed ref.

- Verify each commit they point to, removing any invalid objects and noting any missing objects.

- Remove any refs that had an invalid object, and any non-partial refs that had missing objects.

- Prune all objects not referenced by a ref, which gets rid of any possibly invalid non-scanned objects.

- Enumerate all deployed refs and re-install any that are not in the repo (or are partial for a non-subdir deploy).

Note that **flatpak repair** has to be run with root privileges to operate on the system installation.

An alternative command for repairing OSTree repositories is ostree fsck.

## Options

The following options are understood:

`-h`, `--help`  
Show help options and exit.

`-u`, `--user`  
Repair per-user installation.

`--system`  
Repair system-wide installation.

`--installation=NAME`  
Repair the system-wide installation specified by NAME among those defined in `/etc/flatpak/installations.d/`. Using --installation=default is equivalent to using --system .

`--dry-run`  
Only report inconsistencies, don't make any changes

`--reinstall-all`  
Reinstall all refs, regardless of whether they were removed from the repo or not

`-v`, `--verbose`  
Print debug information during command processing.

`--ostree-verbose`  
Print OSTree debug information during command processing.

## Examples

**\$ sudo flatpak repair**

**\$ flatpak repair --user**

## See also

[flatpak(1)](#flatpak), [ostree-fsck(1)](#ostree-fsck)

## Name

flatpak-repo — Show information about a local repository

## Synopsis

`flatpak repo` \[OPTION...\] LOCATION

## Description

Show information about a local repository.

If you need to modify a local repository, see the **flatpak build-update-repo** command, or use the **ostree** tool.

## Options

The following options are understood:

`-h`, `--help`  
Show help options and exit.

`--info`  
Print general information about a local repository.

`--branches`  
List the branches in a local repository.

`--metadata=BRANCH`  
Print metadata for a branch in the repository.

`--commits=BRANCH`  
Show commits and deltas for a branch in the repository.

`-v`, `--verbose`  
Print debug information during command processing.

`--ostree-verbose`  
Print OSTree debug information during command processing.

## Examples

**\$ flatpak repo --info ~/my-repo**

## See also

[flatpak(1)](#flatpak), [flatpak-info(1)](#flatpak-info) [flatpak-build-update-repo(1)](#flatpak-build-update-repo) [ostree(1)](#ostree)

## Name

flatpak-run — Run an application or open a shell in a runtime

## Synopsis

`flatpak run` \[OPTION...\] REF \[ARG...\]

## Description

If REF names an installed application, Flatpak runs the application in a sandboxed environment. Extra arguments are passed on to the application. The current branch and arch of the application is used unless otherwise specified with `--branch` or `--arch`. See [flatpak-make-current(1)](#flatpak-make-current).

If REF names a runtime, a shell is opened in the runtime. This is useful for development and testing. If there is ambiguity about which branch to use, you will be prompted to choose. Use `--branch` to avoid this. The primary arch is used unless otherwise specified with `--arch`.

By default, Flatpak will look for the application or runtime in the per-user installation first, then in all system installations. This can be overridden with the `--user`, `--system` and `--installation` options.

Flatpak creates a sandboxed environment for the application to run in by mounting the right runtime at `/usr` and a writable directory at `/var`, whose content is preserved between application runs. The application itself is mounted at `/app`.

The details of the sandboxed environment are controlled by the application metadata and various options like `--share` and `--socket` that are passed to the run command: Access is allowed if it was requested either in the application metadata file or with an option and the user hasn't overridden it.

The remaining arguments are passed to the command that gets run in the sandboxed environment. See the `--file-forwarding` option for handling of file arguments.

Environment variables are generally passed on to the sandboxed application, with certain exceptions. The application metadata can override environment variables, as well as the `--env` option. Apart from that, Flatpak always unsets or overrides the following variables, since their session values are likely to interfere with the functioning of the sandbox:

|                                            |
|--------------------------------------------|
| PATH                                       |
| LD_LIBRARY_PATH                            |
| LD_PRELOAD                                 |
| LD_AUDIT                                   |
| XDG_CONFIG_DIRS                            |
| XDG_DATA_DIRS                              |
| SHELL                                      |
| TEMP                                       |
| TEMPDIR                                    |
| TMP                                        |
| TMPDIR                                     |
| XDG_RUNTIME_DIR                            |
| container                                  |
| TZDIR                                      |
| PYTHONPATH                                 |
| PYTHONPYCACHEPREFIX                        |
| PERLLIB                                    |
| PERL5LIB                                   |
| XCURSOR_PATH                               |
| GST_PLUGIN_PATH_1_0                        |
| GST_REGISTRY                               |
| GST_REGISTRY_1_0                           |
| GST_PLUGIN_PATH                            |
| GST_PLUGIN_SYSTEM_PATH                     |
| GST_PLUGIN_SCANNER                         |
| GST_PLUGIN_SCANNER_1_0                     |
| GST_PLUGIN_SYSTEM_PATH_1_0                 |
| GST_PRESET_PATH                            |
| GST_PTP_HELPER                             |
| GST_PTP_HELPER_1_0                         |
| GST_INSTALL_PLUGINS_HELPER                 |
| KRB5CCNAME                                 |
| XKB_CONFIG_ROOT                            |
| GIO_EXTRA_MODULES                          |
| GDK_BACKEND                                |
| VK_ADD_DRIVER_FILES                        |
| VK_ADD_LAYER_PATH                          |
| VK_DRIVER_FILES                            |
| VK_ICD_FILENAMES                           |
| VK_LAYER_PATH                              |
| \_\_EGL_EXTERNAL_PLATFORM_CONFIG_DIRS      |
| \_\_EGL_EXTERNAL_PLATFORM_CONFIG_FILENAMES |
| \_\_EGL_VENDOR_LIBRARY_DIRS                |
| \_\_EGL_VENDOR_LIBRARY_FILENAMES           |

Also several environment variables with the prefix "GST\_" that are used by gstreamer are unset (since Flatpak 1.12.5).

Flatpak also overrides the XDG environment variables to point sandboxed applications at their writable filesystem locations below `~/.var/app/$APPID/`:

|                                     |
|-------------------------------------|
| XDG_DATA_HOME                       |
| XDG_CONFIG_HOME                     |
| XDG_CACHE_HOME                      |
| XDG_STATE_HOME (since Flatpak 1.13) |

Apps can use the `--persist=.local/state` and `--unset-env=XDG_STATE_HOME` options to get a Flatpak 1.13-compatible `~/.local/state` on older versions of Flatpak.

The host values of these variables are made available inside the sandbox via these HOST\_-prefixed variables:

|                                          |
|------------------------------------------|
| HOST_XDG_DATA_HOME                       |
| HOST_XDG_CONFIG_HOME                     |
| HOST_XDG_CACHE_HOME                      |
| HOST_XDG_STATE_HOME (since Flatpak 1.13) |

Flatpak sets the environment variable `FLATPAK_ID` to the application ID of the running app.

Flatpak also bind-mounts as read-only the host's `/etc/os-release` (if available, or `/usr/lib/os-release` as a fallback) to `/run/host/os-release` in accordance with the [os-release specification](https://www.freedesktop.org/software/systemd/man/os-release.html).

If parental controls support is enabled, flatpak will check the current user’s parental controls settings, and will refuse to run an app if it is blocklisted for the current user.

## Options

The following options are understood:

`-h`, `--help`  
Show help options and exit.

`-u`, `--user`  
Look for the application and runtime in per-user installations.

`--system`  
Look for the application and runtime in the default system-wide installations.

`--installation=NAME`  
Look for the application and runtime in the system-wide installation specified by NAME among those defined in `/etc/flatpak/installations.d/`. Using `--installation=default` is equivalent to using `--system`.

`-v`, `--verbose`  
Print debug information during command processing.

`--ostree-verbose`  
Print OSTree debug information during command processing.

`--arch=ARCH`  
The architecture to run. See **flatpak --supported-arches** for architectures supported by the host.

`--command=COMMAND`  
The command to run instead of the one listed in the application metadata.

`--cwd=DIR`  
The directory to run the command in. Note that this must be a directory inside the sandbox.

`--branch=BRANCH`  
The branch to use.

`-d`, `--devel`  
Use the devel runtime that is specified in the application metadata instead of the regular runtime, and use a seccomp profile that is less likely to break development tools.

`--runtime=RUNTIME`  
Use this runtime instead of the one that is specified in the application metadata. This is a full tuple, like for example org.freedesktop.Sdk/x86_64/1.2 , but partial tuples are allowed. Any empty or missing parts are filled in with the corresponding values specified by the app.

`--runtime-version=VERSION`  
Use this version of the runtime instead of the one that is specified in the application metadata. This overrides any version specified with the --runtime option.

`--share=SUBSYSTEM`  
Share a subsystem with the host session. This overrides the Context section from the application metadata. SUBSYSTEM must be one of: network, ipc. This option can be used multiple times.

`--unshare=SUBSYSTEM`  
Don't share a subsystem with the host session. This overrides the Context section from the application metadata. SUBSYSTEM must be one of: network, ipc. This option can be used multiple times.

`--socket=SOCKET`  
Expose a well known socket to the application. This overrides to the Context section from the application metadata. SOCKET must be one of: x11, wayland, fallback-x11, pulseaudio, system-bus, session-bus, ssh-auth, pcsc, cups, gpg-agent, inherit-wayland-socket. This option can be used multiple times.

`--nosocket=SOCKET`  
Don't expose a well known socket to the application. This overrides to the Context section from the application metadata. SOCKET must be one of: x11, wayland, fallback-x11, pulseaudio, system-bus, session-bus, ssh-auth, pcsc, cups, gpg-agent, inherit-wayland-socket. This option can be used multiple times.

`--device=DEVICE`  
Expose a device to the application. This overrides to the Context section from the application metadata. DEVICE must be one of: dri, usb, input, kvm, shm, all. This option can be used multiple times.

`--nodevice=DEVICE`  
Don't expose a device to the application. This overrides to the Context section from the application metadata. DEVICE must be one of: dri, usb, input, kvm, shm, all. This option can be used multiple times.

`--allow=FEATURE`  
Allow access to a specific feature. This overrides to the Context section from the application metadata. FEATURE must be one of: devel, multiarch, bluetooth. This option can be used multiple times.

See [flatpak-build-finish(1)](#flatpak-build-finish) for the meaning of the various features.

`--disallow=FEATURE`  
Disallow access to a specific feature. This overrides to the Context section from the application metadata. FEATURE must be one of: devel, multiarch, bluetooth. This option can be used multiple times.

`--filesystem=FILESYSTEM`  
Allow the application access to a subset of the filesystem. This overrides to the Context section from the application metadata. FILESYSTEM can be one of: home, host, host-os, host-etc, host-root, xdg-desktop, xdg-documents, xdg-download, xdg-music, xdg-pictures, xdg-public-share, xdg-templates, xdg-videos, xdg-run, xdg-config, xdg-cache, xdg-data, an absolute path, or a homedir-relative path like ~/dir or paths relative to the xdg dirs, like xdg-download/subdir. The optional :ro suffix indicates that the location will be read-only. The optional :create suffix indicates that the location will be read-write and created if it doesn't exist. This option can be used multiple times. See the "\[Context\] filesystems" list in [flatpak-metadata(5)](#flatpak-metadata) for details of the meanings of these filesystems.

`--nofilesystem=FILESYSTEM`  
Undo the effect of a previous `--filesystem=` FILESYSTEM in the app's manifest and/or the overrides set up with [flatpak-override(1)](#flatpak-override). This overrides the Context section of the application metadata. FILESYSTEM can take the same values as for `--filesystem`, but the :ro and :create suffixes are not used here. This option can be used multiple times.

This option does not prevent access to a more narrowly-scoped `--filesystem`. For example, if an application has the equivalent of `--filesystem=xdg-config/MyApp` in its manifest or as a system-wide override, and `flatpak override --user --nofilesystem=home` as a per-user override, then it will be prevented from accessing most of the home directory, but it will still be allowed to access `$XDG_CONFIG_HOME/MyApp`.

As a special case, `--nofilesystem=host:reset` will ignore all `--filesystem` permissions inherited from the app manifest or [flatpak-override(1)](#flatpak-override), in addition to having the behaviour of `--nofilesystem=host`.

`--add-policy=SUBSYSTEM.KEY=VALUE`  
Add generic policy option. For example, "--add-policy=subsystem.key=v1 --add-policy=subsystem.key=v2" would map to this metadata:

``` programlisting
[Policy subsystem]
key=v1;v2;
```

This option can be used multiple times.

`--remove-policy=SUBSYSTEM.KEY=VALUE`  
Remove generic policy option. This option can be used multiple times.

`--usb=TYPE[:DATA]`  
Adds a USB device query to the application metadata. This allows device enumeration and usage by the USB portal. TYPE must be one of: all, cls, dev, vnd.

`all`  
Match all devices.

`cls`  
A device class and subclass query. DATA must be in the form of CLASS:SUBCLASS where both CLASS and SUBCLASS must be a valid 2-digit hexadecimal class id number. Alternatively, SUBCLASS may be `*` to match all subclasses.

`dev`  
A device product id query. DATA must be a valid 4-digit hexadecimal product id number, for example `0a1b`. It requires a `vnd` filter in the query.

`vnd`  
A device vendor id query. DATA must be a valid 4-digit hexadecimal vendor id number greater than zero, for example `0fab`.

It is possible to compose multiple device queries together with the `+` sign, for example `--usb=vnd:0123+dev:4567`. The dev filter requires a vnd . Available since 1.15.11.

`--nousb=VENDOR_ID:PRODUCT_ID`  
Adds a blocking USB device query to the application metadata. Blocked devices take precedence over allowed devices. The syntax is exactly equal to `--usb`. Available since 1.15.11.

`--env=VAR=VALUE`  
Set an environment variable in the application. This overrides to the Context section from the application metadata. This option can be used multiple times.

`--unset-env=VAR`  
Unset an environment variable in the application. This overrides the unset-environment entry in the \[Context\] group of the metadata, and the \[Environment\] group. This option can be used multiple times.

`--env-fd=`*`FD`*  
Read environment variables from the file descriptor *`FD`*, and set them as if via `--env`. This can be used to avoid environment variables and their values becoming visible to other users.

Each environment variable is in the form *`VAR`*=*`VALUE`* followed by a zero byte. This is the same format used by `env -0` and `/proc/*/environ`.

`--own-name=NAME`  
Allow the application to own the well known name NAME on the session bus. If NAME ends with .\*, it allows the application to own all matching names. This overrides to the Context section from the application metadata. This option can be used multiple times.

`--talk-name=NAME`  
Allow the application to talk to the well known name NAME on the session bus. If NAME ends with .\*, it allows the application to talk to all matching names. This overrides to the Context section from the application metadata. This option can be used multiple times.

`--no-talk-name=NAME`  
Don't allow the application to talk to the well known name NAME on the session bus. If NAME ends with .\*, it allows the application to talk to all matching names. This overrides to the Context section from the application metadata. This option can be used multiple times.

`--system-own-name=NAME`  
Allow the application to own the well known name NAME on the system bus. If NAME ends with .\*, it allows the application to own all matching names. This overrides to the Context section from the application metadata. This option can be used multiple times.

`--system-talk-name=NAME`  
Allow the application to talk to the well known name NAME on the system bus. If NAME ends with .\*, it allows the application to talk to all matching names. This overrides to the Context section from the application metadata. This option can be used multiple times.

`--system-no-talk-name=NAME`  
Don't allow the application to talk to the well known name NAME on the system bus. If NAME ends with .\*, it allows the application to talk to all matching names. This overrides to the Context section from the application metadata. This option can be used multiple times.

`--a11y-own-name=NAME`  
Allow the application to own the well known name NAME on the a11y bus. If NAME ends with .\*, it allows the application to own all matching names. This overrides to the Context section from the application metadata. This option can be used multiple times.

`--persist=FILENAME`  
If the application doesn't have access to the real homedir, make the (homedir-relative) path FILENAME a bind mount to the corresponding path in the per-application directory, allowing that location to be used for persistent data. This overrides to the Context section from the application metadata. This option can be used multiple times.

`--no-session-bus`  
Run this instance without the filtered access to the session dbus connection. Note, this is the default when run with --sandbox.

`--session-bus`  
Allow filtered access to the session dbus connection. This is the default, except when run with --sandbox.

In sandbox mode, even if you allow access to the session bus the sandbox cannot talk to or own the application ids (org.the.App.\*) on the bus (unless explicitly added), only names in the .Sandboxed subset (org.the.App.Sandboxed.\* and org.mpris.MediaPlayer2.org.the.App.Sandboxed.\*).

`--no-a11y-bus`  
Run this instance without the access to the accessibility bus. Note, this is the default when run with --sandbox.

`--a11y-bus`  
Allow access to the accessibility bus. This is the default, except when run with --sandbox.

`--sandbox`  
Run the application in sandboxed mode, which means dropping all the extra permissions it would otherwise have, as well as access to the session/system/a11y busses and document portal.

`--log-session-bus`  
Log session bus traffic. This can be useful to see what access you need to allow in your D-Bus policy.

`--log-system-bus`  
Log system bus traffic. This can be useful to see what access you need to allow in your D-Bus policy.

`-p`, `--die-with-parent`  
Kill the entire sandbox when the launching process dies.

`--parent-pid=PID`  
Specifies the pid of the "parent" flatpak, used by --parent-expose-pids and --parent-share-pids.

`--parent-expose-pids`  
Make the processes of the new sandbox visible in the sandbox of the parent flatpak, as defined by --parent-pid.

`--parent-share-pids`  
Use the same process ID namespace for the processes of the new sandbox and the sandbox of the parent flatpak, as defined by --parent-pid. Implies --parent-expose-pids.

`--instance-id-fd`  
Write the instance ID string to the given file descriptor.

`--file-forwarding`  
If this option is specified, the remaining arguments are scanned, and all arguments that are enclosed between a pair of '@@' arguments are interpreted as file paths, exported in the document store, and passed to the command in the form of the resulting document path. Arguments between "@@u" and "@@" are considered URIs, and any "file:" URIs are exported. The exports are non-persistent and with read and write permissions for the application.

`--app-path=`*`PATH`*  
Instead of mounting the app's content on `/app` in the sandbox, mount *`PATH`* on `/app`, and the app's content on `/run/parent/app`. If the app has extensions, they will also be redirected into `/run/parent/app`, and will not be included in the `LD_LIBRARY_PATH` inside the sandbox.

`--app-path=`  
As a special case, `--app-path=` (with an empty *`PATH`*) results in an empty directory being mounted on `/app`.

`--usr-path=`*`PATH`*  
Instead of mounting the runtime's files on `/usr` in the sandbox, mount *`PATH`* on `/usr`, and the runtime's normal files on `/run/parent/usr`. If the runtime has extensions, they will also be redirected into `/run/parent/usr`, and will not be included in the `LD_LIBRARY_PATH` inside the sandbox.

This option will usually only be useful if it is combined with `--app-path=` and `--env=LD_LIBRARY_PATH=`*`...`*.

## Examples

**\$ flatpak run org.gnome.gedit**

**\$ flatpak run --devel --command=bash org.gnome.Builder**

**\$ flatpak run --command=bash org.gnome.Sdk**

**\$ flatpak run org.gnome.Boxes --nousb=0fd9:\***

## See also

[flatpak(1)](#flatpak), [flatpak-override(1)](#flatpak-override), [flatpak-enter(1)](#flatpak-enter)

## Name

flatpak-search — Search for applications and runtimes

## Synopsis

`flatpak search` TEXT

## Description

Searches for applications and runtimes matching TEXT . Note that this uses appstream data that can be updated with the **flatpak update** command. The appstream data is updated automatically only if it's at least a day old.

## Options

The following options are understood:

`-u`, `--user`  
Only search through remotes in the per-user installation.

`--system`  
Only search through remotes in the default system-wide installation.

`--installation=NAME`  
Show a system-wide installation by NAME among those defined in `/etc/flatpak/installations.d/`. Using `--installation=default` is equivalent to using `--system`.

`-h`, `--help`  
Show help options and exit.

`-v`, `--verbose`  
Print debug information during command processing.

`--ostree-verbose`  
Print OSTree debug information during command processing.

`--columns=FIELD,…`  
Specify what information to show about each result. You can list multiple fields, or use this option multiple times.

Append :s\[tart\], :m\[iddle\], :e\[nd\] or :f\[ull\] to column names to change ellipsization.

## Fields

The following fields are understood by the `--columns` option:

name  
Show the name

description  
Show the description

application  
Show the application ID

version  
Show the version

branch  
Show the branch

remotes  
Show the remotes

all  
Show all columns

help  
Show the list of available columns

Note that field names can be abbreviated to a unique prefix.

## See also

[flatpak(1)](#flatpak)

## Name

flatpak-uninstall — Uninstall an application or runtime

## Synopsis

`flatpak uninstall` \[OPTION...\] \[REF...\]

## Description

Uninstalls an application or runtime. REF is a reference to the application or runtime to uninstall.

Each REF argument is a full or partial identifier in the flatpak ref format, which looks like "(app\|runtime)/ID/ARCH/BRANCH". All elements except ID are optional and can be left out, including the slashes, so most of the time you need only specify ID. Any part left out will be matched against what is installed, and if there are multiple matches you will be prompted to choose between them. You will also be prompted if REF doesn't match any installed ref exactly but is similar (e.g. "gedit" is similar to "org.gnome.gedit"), but this fuzzy matching behavior is disabled if REF contains any slashes or periods.

By default this looks for both installed apps and runtimes with the given REF , but you can limit this by using the `--app` or `--runtime` option, or by supplying the initial element in the REF .

Normally, this command removes the ref for this application/runtime from the local OSTree repository and purges any objects that are no longer needed to free up disk space. If the same application is later reinstalled, the objects will be pulled from the remote repository again. The `--keep-ref` option can be used to prevent this.

When `--delete-data` is specified while removing an app, its data directory in `~/.var/app` and any permissions it might have are removed. When `--delete-data` is used without a REF , all 'unowned' app data is removed.

Unless overridden with the `--system`, `--user`, or `--installation` options, this command searches both the system-wide installation and the per-user one for REF and errors out if it exists in more than one.

## Options

The following options are understood:

`-h`, `--help`  
Show help options and exit.

`--keep-ref`  
Keep the ref for the application and the objects belonging to it in the local repository.

`-u`, `--user`  
Uninstalls from a per-user installation.

`--system`  
Uninstalls from the default system-wide installation.

`--installation=NAME`  
Uninstalls from a system-wide installation specified by NAME among those defined in `/etc/flatpak/installations.d/`. Using `--installation=default` is equivalent to using `--system`.

`--arch=ARCH`  
The architecture to uninstall, instead of the architecture of the host system. See **flatpak --supported-arches** for architectures supported by the host.

`--all`  
Remove all refs on the system.

`--unused`  
Remove unused refs on the system.

`-y`, `--assumeyes`  
Automatically answer yes to all questions. This is useful for automation.

`--noninteractive`  
Produce minimal output and avoid most questions. This is suitable for use in non-interactive situations, e.g. in a build script.

`--app`  
Only look for an app with the given name.

`--runtime`  
Only look for a runtime with the given name.

`--no-related`  
Don't uninstall related extensions, such as the locale data.

`--force-remove`  
Remove files even if they're in use by a running application.

`--delete-data`  
Remove app data in `~/.var/app` and in the permission store.

`-v`, `--verbose`  
Print debug information during command processing.

`--ostree-verbose`  
Print OSTree debug information during command processing.

## Examples

**\$ flatpak --user uninstall org.gnome.gedit**

## Name

flatpak-update — Update an application or runtime

## Synopsis

`flatpak update` \[OPTION...\] \[REF...\]

`flatpak update` \[OPTION...\] --appstream \[REMOTE\]

## Description

Updates applications and runtimes. REF is a reference to the application or runtime to update. If no REF is given, everything is updated, as well as appstream info for all remotes.

Each REF argument is a full or partial identifier in the flatpak ref format, which looks like "(app\|runtime)/ID/ARCH/BRANCH". All elements except ID are optional and can be left out, including the slashes, so most of the time you need only specify ID. Any part left out will be matched against what is installed, and if there are multiple matches an error message will list the alternatives.

By default this looks for both apps and runtimes with the given REF , but you can limit this by using the `--app` or `--runtime` option, or by supplying the initial element in the REF .

Normally, this command updates the application to the tip of its branch. But it is possible to check out another commit, with the `--commit` option.

If the configured remote for a ref being updated has a collection ID configured on it, Flatpak will search the `sideload-repos` directories configured either with the `--sideload-repo` option, or on a per-installation or system-wide basis (see [flatpak(1)](#flatpak)).

Note that updating a runtime is different from installing a different branch, and runtime updates are expected to keep strict compatibility. If an application update does cause a problem, it is possible to go back to the previous version, with the `--commit` option.

In addition to updates, this command will offer to uninstall any unused end-of-life runtimes. Runtimes that were explicitly installed (not as a dependency) or explicitly pinned (see [flatpak-pin(1)](#flatpak-pin)) are left installed even if unused and end-of-life.

Unless overridden with the `--user`, `--system` or `--installation` option, this command updates any matching refs in the standard system-wide installation and the per-user one.

## Options

The following options are understood:

`-h`, `--help`  
Show help options and exit.

`-u`, `--user`  
Update a per-user installation.

`--system`  
Update the default system-wide installation.

`--installation=NAME`  
Updates a system-wide installation specified by NAME among those defined in `/etc/flatpak/installations.d/`. Using `--installation=default` is equivalent to using `--system`.

`--arch=ARCH`  
The architecture to update for. See **flatpak --supported-arches** for architectures supported by the host.

`--subpath=PATH`  
Install only a subpath of the ref. This is mainly used to install a subset of locales. This can be added multiple times to install multiple subpaths. If this is not specified the subpaths specified at install time are reused.

`--commit=COMMIT`  
Update to this commit, instead of the tip of the branch. You can find commits using **flatpak remote-info --log REMOTE REF**.

`--no-deploy`  
Download the latest version, but don't deploy it.

`--no-pull`  
Don't download the latest version, deploy whatever is locally available.

`--no-related`  
Don't download related extensions, such as the locale data.

`--no-deps`  
Don't update or install runtime dependencies when installing.

`--app`  
Only look for an app with the given name.

`--appstream`  
Update appstream for REMOTE , or all remotes if no remote is specified.

`--runtime`  
Only look for a runtime with the given name.

`--sideload-repo=PATH`  
Adds an extra local ostree repo as a source for installation. This is equivalent to using the `sideload-repos` directories (see [flatpak(1)](#flatpak)), but can be done on a per-command basis. Any path added here is used in addition to ones in those directories.

`-y`, `--assumeyes`  
Automatically answer yes to all questions (or pick the most prioritized answer). This is useful for automation.

`--noninteractive`  
Produce minimal output and avoid most questions. This is suitable for use in non-interactive situations, e.g. in a build script.

`--force-remove`  
Remove old files even if they're in use by a running application.

`-v`, `--verbose`  
Print debug information during command processing.

`--ostree-verbose`  
Print OSTree debug information during command processing.

## Examples

**\$ flatpak --user update org.gnome.gedit**

## See also

[flatpak(1)](#flatpak), [flatpak-install(1)](#flatpak-install), [flatpak-list(1)](#flatpak-list), [ostree-find-remotes(1)](#ostree-find-remotes)

## Name

flatpak-spawn — Run commands in a sandbox

## Synopsis

`flatpak-spawn` \[OPTION...\] COMMAND \[ARGUMENT...\]

## Description

Unlike other flatpak commands, **flatpak-spawn** is available to applications inside the sandbox. It runs COMMAND outside the sandbox: either in another sandbox, or on the host.

When called without `--host`, **flatpak-spawn** uses the Flatpak portal to create a copy of the sandbox it was called from, optionally using tighter permissions and optionally the latest version of the app and runtime (see `--latest-version`).

## Options

The following options are understood:

`-h`, `--help`  
Show help options and exit.

`-v`, `--verbose`  
Print debug information

`--forward-fd=FD`  
Forward a file descriptor

`--clear-env`  
Run with a clean environment

`--watch-bus`  
Make the spawned command exit when **flatpak-spawn** itself exits; notably, this occurs when its connection to the session bus is closed.

`--env=VAR=VALUE`  
Set an environment variable

`--latest-version`  
Use the latest version of the refs that are used to set up the sandbox

`--no-network`  
Run without network access

`--sandbox`  
Run fully sandboxed. See the documentation for the `--sandbox` option in [flatpak-run(1)](#flatpak-run)

See the `--sandbox-expose` and `--sandbox-expose-ro` options for selective file access.

`--sandbox-expose=NAME`  
Expose read-write access to a file in the sandbox.

Note that absolute paths or subdirectories are not allowed. The files must be in the `sandbox` subdirectory of the instance directory (i.e. `~/.var/app/$APP_ID/sandbox`).

This option is useful in combination with `--sandbox` (otherwise the instance directory is accessible anyway).

`--sandbox-expose-ro=NAME`  
Expose readonly access to a file in the sandbox.

Note that absolute paths or subdirectories are not allowed. The files must be in the `sandbox` subdirectory of the instance directory (i.e. `~/.var/app/$APP_ID/sandbox`).

This option is useful in combination with `--sandbox` (otherwise the instance directory is accessible anyway).

`--host`  
Run the command unsandboxed on the host. This requires access to the org.freedesktop.Flatpak D-Bus interface.

`--directory=DIR`  
The working directory in which to run the command.

Note that the given directory must exist in the sandbox or, when used in conjunction with `--host`, on the host.

## Examples

**\$ flatpak-spawn ls /var/run**

## See also

[flatpak(1)](#flatpak)

## File Formats

**Table of Contents**

[flatpakrepo](#flatpakrepo) — Reference to a remote

[flatpakref](#flatpakref) — Reference to a remote for an application or runtime

[flatpak installation](#flatpak-installation) — Configuration for an installation location

[flatpak metadata](#flatpak-metadata) — Information about an application or runtime

[flatpak remote](#flatpak-remote) — Configuration for a remote

## Name

flatpakrepo — Reference to a remote

## Description

Flatpak uses flatpakrepo files to share information about remotes. The `flatpakrepo` file contains enough information to add the remote. Use the **flatpak remote-add --from** command to do so.

flatpakrepo files may also contain additional information that is useful when displaying a remote to the user, e.g. in an app store.

The filename extension commonly used for flatpakrepo files is `.flatpakrepo`.

flatpakrepo files can also be placed in `/usr/share/flatpak/remotes.d/` and `/etc/flatpak/remotes.d/` to statically preconfigure system-wide remotes. Such files must use the `.flatpakrepo` extension. If a file with the same name exists in both, the file under `/etc` will take precedence.

## File format

The flatpakrepo file is using the same .ini file format that is used for systemd unit files or application .desktop files.

### \[Flatpak Repo\]

All the information is contained in the \[Flatpak Repo\] group.

The following keys can be present in this group:

`Version` (uint64)  
The version of the file format, must be 1 if present.

`Url` (string)  
The url for the remote. This key is mandatory.

`GPGKey` (string)  
The base64-encoded gpg key for the remote.

`DefaultBranch` (string)  
The default branch to use for this remote.

`Subset` (string)  
Limit the remote to the named subset of refs.

`Title` (string)  
The title of the remote. This should be a user-friendly name that can be displayed e.g. in an app store.

`Comment` (string)  
A short summary of the remote, for display e.g. in an app store.

`Description` (string)  
A longer description of the remote, for display e.g. in an app store.

`Icon` (string)  
The url for an icon that can be used to represent the remote.

`Homepage` (string)  
The url of a webpage describing the remote.

`Filter` (string)  
The path of a local file to use to filter remote refs. See [flatpak-remote-add(1)](#flatpak-remote-add) for details on the format of the file.

Note: This field is treated a bit special by flatpak remote-add. If you install a remote with --if-not-exists then and the remote is already configured, then the filter field of the remote configuration will be update anyway. And, if the filter field is \*not\* specified then any existing filters are cleared. The goal here is to allow a pre-configured filtered remote to be replaced with the regular one if you add the normal upstream (unfiltered) flatpakrepo file.

`DeploySideloadCollectionID` (string)  
The collection ID of the remote, if it has one. This uniquely identifies the collection of apps in the remote, to allow peer to peer redistribution (see [flatpak(1)](#flatpak)). It is recommended to use this key over DeployCollectionID or CollectionID because only newer clients (Flatpak 1.12.8 or later) pay attention to it (and older clients don't handle collection IDs properly).

`DeployCollectionID` (string)  
This is deprecated but still supported for backwards compatibility. Use DeploySideloadCollectionID instead.

`CollectionID` (string)  
This is deprecated but still supported for backwards compatibility. Use DeploySideloadCollectionID instead.

## Example

``` programlisting
[Flatpak Repo]
Title=gedit
Url=http://sdk.gnome.org/repo-apps/
GPGKey=mQENBFUUCGcBCAC/K9WeV4xCaKr3NKRqPXeY5mpaXAJyasLqCtrDx92WUgbu0voWrhohNAKpqizod2dvzc/XTxm3rHyIxmNfdhz1gaGhynU75Qw4aJVcly2eghTIl++gfDtOvrOZo/VuAq30f32dMIgHQdRwEpgCwz7WyjpqZYltPAEcCNL4MTChAfiHJeeiQ5ibystNBW8W6Ymf7sO4m4g5+/aOxI54oCOzD9TwBAe+yXcJJWtc2rAhMCjtyPJzxd0ZVXqIzCe1xRvJ6Rq7YCiMbiM2DQFWXKnmYQbj4TGNMnwNdAajCdrcBWEMSbzq7EzuThIJRd8Ky4BkEe1St6tuqwFaMZz+F9eXABEBAAG0KEdub21lIFNESyAzLjE2IDxnbm9tZS1vcy1saXN0QGdub21lLm9yZz6JATgEEwECACIFAlUUCGcCGwMGCwkIBwMCBhUIAgkKCwQWAgMBAh4BAheAAAoJEArkz6VV0VKBa5cH/0vXa31YgEjNk78gGFXqnQxdD1WYA87OYxDi189l4lA802EFTF4wCBuZyDOqdd5BhS3Ab0cR778DmZXRUP2gwe+1zTJypU2JMnDpkwJ4NK1VP6/tE4SAPrznBtmb76BKaWBqUfZ9Wq1zg3ugvqkZB/Exq+usypIOwQVp1KL58TrjBRda0HvRctzkNhr0qYAtkfLFe0GvksBp4vBm8uGwAx7fw/HbhIjQ9pekTwvB+5GwDPO/tSip/1bQfCS+XJB8Ffa04HYPLGedalnWBrwhYY+G/kn5Zh9L/AC8xeLwTJTHM212rBjPa9CWs9C6a57MSaeGIEHLC1hEyiJJ15w8jmY=
DeployCollectionID=org.gnome.Apps
```

## See also

[flatpak(1)](#flatpak), [flatpak-remote-add(1)](#flatpak-remote-add), [flatpakref(5)](#flatpakref)

## Name

flatpakref — Reference to a remote for an application or runtime

## Description

Flatpak uses flatpakref files to share information about a remote for a single application. The `flatpakref` file contains enough information to add the remote and install the application. Use the **flatpak install --from** command to do so.

flatpakref files may also contain additional information that is useful when displaying the application to the user, e.g. in an app store.

The filename extension commonly used for flatpakref files is `.flatpakref`.

A flatpakref file can also refer to a remote for a runtime.

## File format

The flatpakref file is using the same .ini file format that is used for systemd unit files or application .desktop files.

### \[Flatpak Ref\]

All the information is contained in the \[Flatpak Ref\] group.

The following keys can be present in this group:

`Version` (uint64)  
The version of the file format, must be 1 if present.

`Name` (string)  
The fully qualified name of the runtime or application. This key is mandatory.

`Url` (string)  
The url for the remote. This key is mandatory.

`Branch` (string)  
The name of the branch from which to install the application or runtime. If this key is not specified, the "master" branch is used.

`Title` (string)  
The title of the application or runtime. This should be a user-friendly name that can be displayed e.g. in an app store.

`Comment` (string)  
A short summary of the application or runtime, for display e.g. in an app store.

`Description` (string)  
A longer description of the application or runtime, for display e.g. in an app store.

`Icon` (string)  
The url for an icon that can be used to represent the application or runtime.

`Homepage` (string)  
The url of a webpage describing the application or runtime.

`DeploySideloadCollectionID` (string)  
The collection ID of the remote, if it has one. This uniquely identifies the collection of apps in the remote, to allow peer to peer redistribution (see [flatpak(1)](#flatpak)). It is recommended to use this key over DeployCollectionID or CollectionID because only newer clients (Flatpak 1.12.8 or later) pay attention to it (and older clients don't handle collection IDs properly).

`DeployCollectionID` (string)  
This is deprecated but still supported for backwards compatibility. Use DeploySideloadCollectionID instead.

`CollectionID` (string)  
This is deprecated but still supported for backwards compatibility. Use DeploySideloadCollectionID instead.

`IsRuntime` (boolean)  
Whether this file refers to a runtime. If this key is not specified, the file is assumed to refer to an application.

`GPGKey` (string)  
The base64-encoded gpg key for the remote.

`RuntimeRepo` (string)  
The url for a .flatpakrepo file for the remote where the runtime can be found. Note that if the runtime is available in the remote providing the app, that remote may be used instead but the one specified by this option will still be added.

`SuggestRemoteName` (string)  
A suggested name for the remote.

## Example

``` programlisting
[Flatpak Ref]
Title=gedit
Name=org.gnome.gedit
Branch=stable
Url=http://sdk.gnome.org/repo-apps/
IsRuntime=false
GPGKey=mQENBFUUCGcBCAC/K9WeV4xCaKr3NKRqPXeY5mpaXAJyasLqCtrDx92WUgbu0voWrhohNAKpqizod2dvzc/XTxm3rHyIxmNfdhz1gaGhynU75Qw4aJVcly2eghTIl++gfDtOvrOZo/VuAq30f32dMIgHQdRwEpgCwz7WyjpqZYltPAEcCNL4MTChAfiHJeeiQ5ibystNBW8W6Ymf7sO4m4g5+/aOxI54oCOzD9TwBAe+yXcJJWtc2rAhMCjtyPJzxd0ZVXqIzCe1xRvJ6Rq7YCiMbiM2DQFWXKnmYQbj4TGNMnwNdAajCdrcBWEMSbzq7EzuThIJRd8Ky4BkEe1St6tuqwFaMZz+F9eXABEBAAG0KEdub21lIFNESyAzLjE2IDxnbm9tZS1vcy1saXN0QGdub21lLm9yZz6JATgEEwECACIFAlUUCGcCGwMGCwkIBwMCBhUIAgkKCwQWAgMBAh4BAheAAAoJEArkz6VV0VKBa5cH/0vXa31YgEjNk78gGFXqnQxdD1WYA87OYxDi189l4lA802EFTF4wCBuZyDOqdd5BhS3Ab0cR778DmZXRUP2gwe+1zTJypU2JMnDpkwJ4NK1VP6/tE4SAPrznBtmb76BKaWBqUfZ9Wq1zg3ugvqkZB/Exq+usypIOwQVp1KL58TrjBRda0HvRctzkNhr0qYAtkfLFe0GvksBp4vBm8uGwAx7fw/HbhIjQ9pekTwvB+5GwDPO/tSip/1bQfCS+XJB8Ffa04HYPLGedalnWBrwhYY+G/kn5Zh9L/AC8xeLwTJTHM212rBjPa9CWs9C6a57MSaeGIEHLC1hEyiJJ15w8jmY=
DeployCollectionID=org.gnome.Apps
```

## See also

[flatpak(1)](#flatpak), [flatpak-install(1)](#flatpak-install) [flatpakrepo(5)](#flatpakrepo),

## Name

flatpak-installation — Configuration for an installation location

## Description

flatpak can operate in system-wide or per-user mode. The system-wide data is located in `$prefix/var/lib/flatpak/`, and the per-user data is in `$HOME/.local/share/flatpak/`.

In addition to the default installation locations, more system-wide installations can be defined via configuration files `/etc/flatpak/installations.d/`, which must have the .conf extension and follow the format described below.

## File format

The installation config file format is using the same .ini file format that is used for systemd unit files or application .desktop files.

### \[Installation …\]

All the configuration for the the installation location with name NAME is contained in the \[Installation "NAME"\] group.

The following keys are recognized:

`Path` (string)  
The path for this installation. This key is mandatory.

`DisplayName` (string)  
The name to use when showing this installation in the UI.

`Priority` (integer)  
A priority for this installation.

`StorageType` (string)  
The type of storage used for this installation. Possible values include: network, mmc, sdcard, harddisk.

## Examples

``` programlisting
[Installation "extra"]
Path=/location/of/sdcard
DisplayName=Extra Installation
StorageType=sdcard
```

## Name

flatpak-metadata — Information about an application or runtime

## Description

Flatpak uses metadata files to describe applications and runtimes. The `metadata` file for a deployed application or runtime is placed in the toplevel deploy directory. For example, the metadata for the locally installed application org.gnome.Calculator is in `~/.local/share/flatpak/app/org.gnome.Calculator/current/active/metadata`.

Most aspects of the metadata configuration can be overridden when launching applications, either temporarily via options of the flatpak run command, or permanently with the flatpak override command.

A metadata file describing the effective configuration is available inside the running sandbox at `/.flatpak-info`. For compatibility with older Flatpak versions, `/run/user/$UID/flatpak-info` is a symbolic link to the same file.

## File format

The metadata file is using the same .ini file format that is used for systemd unit files or application .desktop files.

### \[Application\] or \[Runtime\]

Metadata for applications starts with an \[Application\] group, metadata for runtimes with a \[Runtime\] group.

The following keys can be present in these groups:

`name` (string)  
The name of the application or runtime. This key is mandatory.

`runtime` (string)  
The fully qualified name of the runtime that is used by the application. This key is mandatory for applications.

`sdk` (string)  
The fully qualified name of the sdk that matches the runtime. Available since 0.1.

`command` (string)  
The command to run. Only relevant for applications. Available since 0.1.

`required-flatpak` (string list)  
The required version of Flatpak to run this application or runtime. For applications, this was available since 0.8.0. For runtimes, this was available since 0.9.1, and backported to 0.8.3 for the 0.8.x branch.

Flatpak after version 1.4.3 and 1.2.5 support multiple versions here. This can be useful if you need to support features that are backported to a previous stable series. For example if you want to use a feature added in 1.6.0 that was also backported to 1.4.4 you would use `1.6.0;1.4.4;`. Note that older versions of flatpak will just use the first element in the list, so make that the largest version.

`tags` (string list)  
Tags to include in AppStream XML. Typical values in use on Flathub include `beta`, `stable`, `proprietary` and `upstream-maintained`. Available since 0.4.12.

### \[Context\]

This group determines various system resources that may be shared with the application when it is run in a flatpak sandbox.

All keys in this group (and the group itself) are optional.

`shared` (list)  
List of subsystems to share with the host system. Possible subsystems: network, ipc. Available since 0.3.

`sockets` (list)  
List of well-known sockets to make available in the sandbox. Possible sockets: x11, wayland, fallback-x11, pulseaudio, session-bus, system-bus, ssh-auth, pcsc, cups, gpg-agent, inherit-wayland-socket. When making a socket available, flatpak also sets well-known environment variables like DISPLAY or DBUS_SYSTEM_BUS_ADDRESS to let the application find sockets that are not in a fixed location. Available since 0.3.

`devices` (list)  
List of devices to make available in the sandbox. This just expose the devices nodes, it doesn't grant any permission that the user doesn't already have. Possible values:

`dri`  
Graphics direct rendering (`/dev/dri`). Available since 0.3.

`input`  
Input devices (`/dev/input`). Available since 1.15.6.

`usb`  
USB device bus (all device nodes below `/dev/bus/usb`). Available since 1.15.11.

`kvm`  
Virtualization (`/dev/kvm`). Available since 0.6.12.

`all`  
All device nodes in `/dev`, but not /dev/shm (which is separately specified). Available since 0.6.6.

`shm`  
Access to the host /dev/shm (`/dev/shm`). Available since 1.6.1.

`filesystems` (list)  
List of filesystem subsets to make available to the application. Possible values:

`home`  
The entire home directory. Available since 0.3.

`home/`*`path`*  
Alias for `~/path` Available since 1.10. For better compatibility with older Flatpak versions, prefer to write this as `~/path`.

`host`  
The entire host file system, except for directories that are handled specially by Flatpak. In particular, this shares `/home`, `/media`, `/opt`, `/run/media` and `/srv` if they exist.

`/dev` is not shared: use `devices=all;` instead.

Parts of `/sys` are always shared. This option does not make additional files in /sys available.

Additionally, this keyword provides all of the same directories in `/run/host` as the `host-os` and `host-etc` keywords. If this keyword is used in conjunction with one of the `host-` keywords, whichever access level is higher (more permissive) will be used for the directories in `/run/host`: for example, `host:rw;host-os:ro;` is equivalent to `host:rw;`.

These other reserved directories are currently excluded: `/app`, `/bin`, `/boot`, `/efi`, `/etc`, `/lib`, `/lib32`, `/lib64`, `/proc`, `/root`, `/run`, `/sbin`, `/tmp`, `/usr`, `/var`.

Available since 0.3.

`host-os`  
The host operating system's libraries, executables and static data from `/usr` and the related directories `/bin`, `/lib`, `/lib32`, `/lib64`, `/sbin`. Additionally, this keyword provides access to a subset of `/etc` that is associated with packaged libraries and executables, even if the `host-etc` keyword was not used: `/etc/ld.so.cache`, (used by the dynamic linker) and `/etc/alternatives` (on operating systems that use it, such as Debian).

To avoid conflicting with the Flatpak runtime, these are mounted in the sandbox at `/run/host/usr`, `/run/host/etc/ld.so.cache` and so on.

Available since 1.7.

`host-etc`  
The host operating system's configuration from `/etc`.

To avoid conflicting with the Flatpak runtime, this is mounted in the sandbox at `/run/host/etc`.

Available since 1.7.

`host-root`  
The complete host operating system.

To avoid conflicting with the Flatpak runtime, this is mounted in the sandbox at `/run/host/root`.

This permission is only intended to be used as a last resort when there is no possible alternative with other filesystem permissions for applications that need the entire root filesystem of the host.

Please note that following symlinks under `/run/host/root` naively will result in a wrong path. For example, using `realpath()` is wrong. Instead, applications will have to implement some way of following symlinks in a way that behaves as if it were chroot'd into `/run/host/root`.

There are a few ways to do this. Modern kernels support the [openat2()](https://man7.org/linux/man-pages/man2/openat2.2.html) call with `RESOLVE_IN_ROOT`. For a more portable solution with support for older kernels, see the implementation from the [steam-runtime-tools](https://gitlab.steamos.cloud/steamrt/steam-runtime-tools/-/blob/65adfdd5fc812aeb5f33986755f6ff72c9612afa/steam-runtime-tools/resolve-in-sysroot.c) as an example.

Available since 1.17.

`xdg-desktop`, `xdg-documents`, `xdg-download`, `xdg-music`, `xdg-pictures`, `xdg-public-share`, `xdg-videos`, `xdg-templates`  
[freedesktop.org special directories](https://www.freedesktop.org/wiki/Software/xdg-user-dirs/). Available since 0.3.

`xdg-desktop/`*`path`*, `xdg-documents/`*`path`*, etc.  
Subdirectories of freedesktop.org special directories. Available since 0.4.13.

`xdg-cache`, `xdg-config`, `xdg-data`  
Directories defined by the [freedesktop.org Base Directory Specification](https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html). Available since 0.6.14.

`xdg-cache/`*`path`*, `xdg-config/`*`path`*, `xdg-data/`*`path`*  
Subdirectories of directories defined by the freedesktop.org Base Directory Specification. Available since 0.6.14.

`xdg-run/`*`path`*  
Subdirectories of the `XDG_RUNTIME_DIR` defined by the freedesktop.org Base Directory Specification. Note that `xdg-run` on its own is not supported. Available since 0.4.13.

`/`*`path`*  
An arbitrary absolute path. Available since 0.3.

`~/`*`path`*  
An arbitrary path relative to the home directory. Available since 0.3.

`~`  
The same as `home`. Available since 1.10. For better compatibility with older Flatpak versions, prefer to write this as `home`.

One of the above followed by `:ro`  
Make the given directory available read-only.

One of the above followed by `:rw`  
Make the given directory available read/write. This is the default.

One of the above followed by `:create`  
Make the given directory available read/write, and create it if it does not already exist.

`persistent` (list)  
List of homedir-relative paths to make available at the corresponding path in the per-application home directory, allowing the locations to be used for persistent data when the application does not have access to the real homedir. For instance making ".myapp" persistent would make "~/.myapp" in the sandbox a bind mount to "~/.var/app/org.my.App/.myapp", thus allowing an unmodified application to save data in the per-application location. Available since 0.3.

`features` (list)  
List of features available or unavailable to the application, currently from the following list:

`devel`  
Allow system calls used by development-oriented tools such as **perf**, **strace** and **gdb**. Available since 0.6.10.

`multiarch`  
Allow running multilib/multiarch binaries, for example `i386` binaries in an `x86_64` environment. Available since 0.6.12.

`bluetooth`  
Allow the application to use bluetooth (AF_BLUETOOTH) sockets. Note, for bluetooth to fully work you must also have network access. Available since 0.11.8.

`canbus`  
Allow the application to use canbus (AF_CAN) sockets. Note, for this work you must also have network access. Available since 1.0.3.

`per-app-dev-shm`  
Share a single instance of `/dev/shm` between all instances of this application run by the same user ID, including sub-sandboxes. If the application has the `shm` device permission in its `devices` list, then this feature flag is ignored. Available since 1.12.0.

A feature can be prefixed with `!` to indicate the absence of that feature, for example `!devel` if development and debugging are not allowed.

`unset-environment` (list)  
A list of names of environment variables to unset. Note that environment variables to set to a value (possibly empty) appear in the \[Environment\] group instead.

### \[Instance\]

This group only appears in `/.flatpak-info` for a running app, and not in the metadata files written by application authors. It is filled in by Flatpak itself.

`instance-id` (string)  
The ID of the running instance. This number is used as the name of the directory in `XDG_RUNTIME_DIR``/.flatpak` where Flatpak stores information about this instance.

`instance-path` (string)  
The absolute path on the host system of the app's persistent storage area in `$HOME/.var`.

`app-path` (string)  
The absolute path on the host system of the app's app files, as mounted at `/app` inside the container. Available since 0.6.10.

Since 1.12.0, if **flatpak run** was run with the `--app-path` option, this key gives the absolute path of whatever files were mounted on `/app`, even if that differs from the app's normal app files.

If **flatpak run** was run with `--app-path=` (resulting in an empty directory being mounted on `/app`), the value is set to the empty string.

`original-app-path` (string)  
If **flatpak run** was run with the `--app-path` option, this key gives the absolute path of the app's original files, as mounted at `/run/parent/app` inside the container. Available since 1.12.0.

If this key is missing, the app files are given by `app-path`.

`app-commit` (string)  
The commit ID of the application that is running. The filename of a deployment of this commit can be found in `original-app-path` if present, or `app-path` otherwise.

`app-extensions` (list of strings)  
A list of app extensions that are mounted into the running instance. The format for each list item is `EXTENSION_ID=COMMIT`. If `original-app-path` is present, the extensions are mounted below `/run/parent/app`; otherwise, they are mounted below `/app`.

`branch` (string)  
The branch of the app, for example `stable`. Available since 0.6.10.

`arch` (string)  
The architecture of the running instance.

`flatpak-version` (string)  
The version number of the Flatpak version that ran this app. Available since 0.6.11.

`runtime-path` (string)  
The absolute path on the host system of the app's runtime files, as mounted at `/usr` inside the container. Available since 0.6.10.

Since 1.12.0, if **flatpak run** was run with the `--usr-path` option, this key gives the absolute path of whatever files were mounted on `/usr`, even if that differs from the app's normal runtime files.

`original-runtime-path` (string)  
If **flatpak run** was run with the `--runtime-path` option, this key gives the absolute path of the app's original runtime, as mounted at `/run/parent/usr` inside the container. Available since 1.12.0.

If this key is missing, the runtime files are given by `runtime-path`.

`runtime-commit` (string)  
The commit ID of the runtime that is used. The filename of a deployment of this commit can be found in `original-runtime-path` if present, or `runtime-path` otherwise.

`runtime-extensions` (list of strings)  
A list of runtime extensions that are mounted into the running instance. The format for each list item is `EXTENSION_ID=COMMIT`. If `original-app-path` is present, the extensions are mounted below `/run/parent/usr`; otherwise, they are mounted below `/usr`.

`extra-args` (string)  
Extra arguments that were passed to flatpak run.

`sandbox` (boolean)  
Whether the `--sandbox` option was passed to flatpak run.

`build` (boolean)  
Whether this instance was created by flatpak build.

`session-bus-proxy` (boolean)  
True if this app cannot access the D-Bus session bus directly (either it goes via a proxy, or it cannot access the session bus at all). Available since 0.8.0.

`system-bus-proxy` (boolean)  
True if this app cannot access the D-Bus system bus directly (either it goes via a proxy, or it cannot access the system bus at all). Available since 0.8.0.

### \[Session Bus Policy\]

If the `sockets` key is not allowing full access to the D-Bus session bus, then flatpak provides filtered access.

The default policy for the session bus only allows the application to own its own application ID, its subnames and its own application ID as a subname of `org.mpris.MediaPlayer2`. For instance if the app is called `org.my.App`, it can only own `org.my.App`, `org.my.App.*` and `org.mpris.MediaPlayer2.org.my.App`. It is only allowed to talk to names matching those patterns, plus the bus itself (`org.freedesktop.DBus`) and the portal APIs (bus names of the form `org.freedesktop.portal.*`).

Additionally the app is always allowed to reply to messages sent to it, and emit broadcast signals (but these will not reach other sandboxed apps unless they are allowed to talk to your app.

If the `[Session Bus Policy]` group is present, it provides policy for session bus access.

Each key in this group has the form of a D-Bus bus name or prefix thereof, for example `org.gnome.SessionManager` or `org.freedesktop.portal.*`.

The possible values for an entry are the following, in increasing order of access. Each value implies all the access from any lower values:

`none`  
The bus name is invisible to the application. Available since 0.2.

`see`  
The bus name can be enumerated by the application. Available since 0.2.

`talk`  
The application can send messages to, and receive replies and signals from, the bus name. Available since 0.2.

`own`  
The application can own the bus name. Available since 0.2.

### \[System Bus Policy\]

If the `sockets` key is not allowing full access to the D-Bus system bus, then flatpak does not make the system bus available unless the `[System Bus Policy]` group is present and provides a policy for filtered access. Available since 0.2.

Entries in this group have the same form as for the `[Session Bus Policy]` group. However, the app has no permissions by default.

### \[Environment\]

The \[Environment\] group specifies environment variables to set when running the application. Available since 0.3.

Entries in this group have the form `VAR=VALUE` where `VAR` is the name of an environment variable to set.

Note that environment variables can also be unset (removed from the environment) by listing them in the `unset-environment` entry of the \[Context\] group.

### \[Extension NAME\]

Runtimes and applications can define extension points, which allow optional, additional runtimes to be mounted at a specified location inside the sandbox when they are present on the system. Typical uses for extension points include translations for applications, or debuginfo for sdks. The name of the extension point is specified as part of the group heading. Since 0.11.4, the name may optionally include a tag in the NAME in the name@tag ref syntax if you wish to use different configurations (eg, versions) of the same extension concurrently. The "tag" is effectively ignored, but is necessary in order to allow the same extension name to be specified more than once.

`directory` (string)  
The relative path at which the extension will be mounted in the sandbox. If the extension point is for an application, the path is relative to `/app`, otherwise it is relative to `/usr`. This key is mandatory. Available since 0.1.

`version` (string)  
The branch to use when looking for the extension. If this is not specified, it defaults to the branch of the application or runtime that the extension point is for. Available since 0.4.1.

`versions` (string)  
The branches to use when looking for the extension. If this is not specified, it defaults to the branch of the application or runtime that the extension point is for. Available since 0.9.1, and backported to the 0.8.x branch in 0.8.4.

`add-ld-path` (string)  
A path relative to the extension point directory that will be appended to LD_LIBRARY_PATH. Available since 0.9.1, and backported to the 0.8.x branch in 0.8.3.

`merge-dirs` (string)  
A list of relative paths of directories below the extension point directory that will be merged. Available since 0.9.1, and backported to the 0.8.x branch in 0.8.3.

`download-if` (string)  
A condition that must be true for the extension to be auto-downloaded. As of 1.1.1 this supports multiple conditions separated by semi-colons.

These are the supported conditions:

`active-gl-driver`  
Is true if the name of the active GL driver matches the extension point basename. Available since 0.9.1, and backported to the 0.8.x branch in 0.8.3.

`active-gtk-theme`  
Is true if the name of the current GTK theme (via org.gnome.desktop.interface GSetting) matches the extension point basename. Added 0.10.1.

`have-intel-gpu`  
Is true if the i915 kernel module is loaded. Added 0.10.1.

`have-kernel-module-*`  
Is true if the suffix (case-sensitive) is found in `/proc/modules`. For example `have-kernel-module-nvidia`. Added 1.13.1.

`on-xdg-desktop-*`  
Is true if the suffix (case-insensitively) is in the `XDG_CURRENT_DESKTOP` env var. For example `on-xdg-desktop-GNOME-classic`. Added 1.1.1.

`autoprune-unless` (string)  
A condition that must be false for the extension to be considered unused when pruning. For example, **flatpak uninstall --unused** and **flatpak update** use this information. The only currently recognized value is active-gl-driver, which is true if the name of the active GL driver matches the extension point basename. Available since 0.11.8.

`enable-if` (string)  
A condition that must be true for the extension to be enabled. As of 1.1.1 this supports multiple conditions separated by semi-colons. See `download-if` for available conditions.

`subdirectory-suffix` (string)  
A suffix that gets appended to the directory name. This is very useful when the extension point naming scheme is "reversed". For example, an extension point for GTK+ themes would be /usr/share/themes/\$NAME/gtk-3.0, which could be achieved using subdirectory-suffix=gtk-3.0. Available since 0.9.1, and backported to the 0.8.x branch in 0.8.3.

`subdirectories` (boolean)  
If this key is set to true, then flatpak will look for extensions whose name is a prefix of the extension point name, and mount them at the corresponding name below the subdirectory. Available since 0.1.

`no-autodownload` (boolean)  
Whether to automatically download extensions matching this extension point when updating or installing a 'related' application or runtime. Available since 0.6.7.

`locale-subset` (boolean)  
If set, then the extensions are partially downloaded by default, based on the currently configured locales. This means that the extension contents should be a set of directories with the language code as name. Available since 0.9.13 (and 0.6.6 for any extensions called \*.Locale)

`autodelete` (boolean)  
Whether to automatically delete extensions matching this extension point when deleting a 'related' application or runtime. Available since 0.6.7.

`collection-id` (string)  
The ID of the collection that this extension point belongs to. If this is unspecified, it defaults to the collection ID of the application or runtime that the extension point is for. Currently, extension points must be in the same collection as the application or runtime that they are for. Available since 0.99.1.

### \[ExtensionOf\]

This optional group may be present if the runtime is an extension.

`ref` (string)  
The ref of the runtime or application that this extension belongs to. Available since 0.9.1.

`runtime` (string)  
The runtime this extension will be inside of. If it is an app extension, this is the app's runtime; otherwise, this is identical to ref, without the runtime/ prefix. Available since 1.5.0.

`priority` (integer)  
The priority to give this extension when looking for the best match. Default is 0. Available since 0.9.1, and backported to the 0.8.x branch in 0.8.3.

`tag` (string)  
The tag name to use when searching for this extension's mount point in the parent flatpak. Available since 0.11.4.

### \[Extra Data\]

This optional group may be present if the runtime or application uses extra data that gets downloaded separately. The data in this group gets merged into the repository summary, with the xa.extra-data-sources key.

If multiple extra data sources are present, their uri, size and checksum keys are grouped together by using the same suffix. If only one extra data source is present, the suffix can be omitted.

`NoRuntime` (boolean)  
Whether to mount the runtime while running the /app/bin/apply_extra script. Defaults to true, i.e. not mounting the runtime. Available since 0.9.1, and backported to the 0.8.x branch in 0.8.4.

`uri`*`X`* (string)  
The uri for extra data source *`X`*. The only supported uri schemes are http and https. Available since 0.6.13.

`size`*`X`* (integer)  
The size for extra data source *`X`*. Available since 0.6.13.

`checksum`*`X`* (string)  
The sha256 sum for extra data source *`X`*. Available since 0.6.13.

### \[Policy SUBSYSTEM\]

Subsystems can define their own policies to be placed in a group whose name has this form. Their values are treated as lists, in which items can have their meaning negated by prepending ! to the value. They are not otherwise parsed by Flatpak. Available since 0.6.13.

### \[USB Devices\]

USB devices can be enumerable or hidden by the USB portal as specified by the keys in this group. The vendor and product ids are validated by Flatpak, but aren't otherwise used or parsed. This merely grant the permission to enumerate USB device for use by the portal. This does give access to the devices. Available since 1.15.11.

`enumerable-devices` (string list)  
List of enumerable USB devices. Each element is the same syntax the arguments to \`--usb\`. Available since 1.15.11.

`hidden-devices` (string list)  
List of hidden USB devices, i.e. to remove the enumarable devices list. Each element is the same syntax the arguments to \`--nousb\`. Hidden devices take precedence over enumerable devices. Available since 1.15.11.

## Example

``` programlisting
[Application]
name=org.gnome.Calculator
runtime=org.gnome.Platform/x86_64/3.20
sdk=org.gnome.Sdk/x86_64/3.20
command=gnome-calculator

[Context]
shared=network;ipc;
sockets=x11;wayland;
filesystems=xdg-run/dconf;~/.config/dconf:ro;

[Session Bus Policy]
ca.desrt.dconf=talk

[Environment]
DCONF_USER_CONFIG_DIR=.config/dconf

[USB Devices]
enumerable-devices=0fd9:*;
hidden-devices=0fd9:0063;

[Extension org.gnome.Calculator.Locale]
directory=share/runtime/locale
subdirectories=true

[Extension org.gnome.Calculator.Debug]
directory=lib/debug
```

## See also

[flatpak(1)](#flatpak), [flatpak-run(1)](#flatpak-run), [flatpak-override(1)](#flatpak-override)

## Name

flatpak-remote — Configuration for a remote

## Description

Flatpak stores information about configured remotes for an installation location in `$installation/repo/config`. For example, the remotes for the default system-wide installation are in `$prefix/var/lib/flatpak/repo/config`, and the remotes for the per-user installation are in `$HOME/.local/share/flatpak/repo/config`.

Normally, it is not necessary to edit remote config files directly, the **flatpak remote-modify** command should be used to change properties of remotes.

System-wide remotes can be statically preconfigured by dropping [flatpakrepo(5)](#flatpakrepo) files into `/usr/share/flatpak/remotes.d/` and `/etc/flatpak/remotes.d/`. Ifa file with the same name exists in both, the file under `/etc` will take precedence.

## File format

The remote config file format is using the same .ini file format that is used for systemd unit files or application .desktop files.

### \[remote …\]

All the configuration for the the remote with name NAME is contained in the \[remote "NAME"\] group.

The following keys are recognized by OSTree, among others:

`url` (string)  
The url for the remote. An URL of the form oci+https:// or oci+http:// is a Flatpak extension that indicates that the remote is not an ostree repository, but is rather an URL to an index of OCI images that are stored within a container image registry.

For OCI remotes, client and CA certificates are read from `/etc/containers/certs.d` and `~/.config/containers/certs.d` as documented in [containers-certs.d(5)](#containers-certs.d).

`gpg-verify` (boolean)  
Whether to use GPG verification for content from this remote.

`gpg-verify-summary` (boolean)  
Whether to use GPG verification for the summary of this remote.

This is ignored if `collection-id` is set, as refs are verified in commit metadata in that case. Enabling `gpg-verify-summary` would break peer to peer distribution of refs.

`collection-id` (string)  
The globally unique identifier for the upstream collection repository, to allow mirrors to be grouped.

All flatpak-specific keys have a xa. prefix:

`xa.disable` (boolean)  
Whether the remote is disabled. Defaults to false.

`xa.prio` (integer)  
The priority for the remote. This is used when listing remotes, and when searching them for the runtime needed by an app. The remote providing the app is searched for its runtime before others with equal priority. Defaults to 1.

`xa.noenumerate` (boolean)  
Whether this remote should be ignored when presenting available apps/runtimes, or when searching for a runtime dependency. Defaults to false.

`xa.nodeps` (boolean)  
Whether this remote should be excluded when searching for dependencies. Defaults to false.

`xa.title` (string)  
An optional title to use when presenting this remote in a UI.

`xa.title-is-set` (boolean)  
This key is set to true if `xa.title` has been explicitly set.

`xa.comment` (string)  
An optional single-line comment to use when presenting this remote in a UI.

`xa.comment-is-set` (boolean)  
This key is set to true if `xa.comment` has been explicitly set.

`xa.description` (string)  
An optional full-paragraph of text to use when presenting this remote in a UI.

`xa.description-is-set` (boolean)  
This key is set to true if `xa.description` has been explicitly set.

`xa.homepage` (string)  
An optional URL that points to a website for this repository to use when presenting this remote in a UI.

`xa.homepage-is-set` (boolean)  
This key is set to true if `xa.homepage` has been explicitly set.

`xa.icon` (string)  
An optional URL that points to an icon for this repository to use when presenting this remote in a UI.

`xa.icon-is-set` (boolean)  
This key is set to true if `xa.icon` has been explicitly set.

`xa.default-branch` (string)  
The default branch to use when installing from this remote.

`xa.default-branch-is-set` (boolean)  
This key is set to true if `xa.default-branch` has been explicitly set.

`xa.main-ref` (string)  
The main reference served by this remote. This is used for origin remotes of applications installed via a flatpakref file.

## Examples

``` programlisting
[remote "gnome-nightly-apps"]
gpg-verify=true
gpg-verify-summary=true
url=https://sdk.gnome.org/nightly/repo-apps/
xa.title=GNOME Applications
```

``` programlisting
[remote "flathub"]
gpg-verify=true
gpg-verify-summary=false
collection-id=org.flathub.Stable
url=https://dl.flathub.org/repo/
xa.title=Flathub
```

## See also

[flatpak-remote-modify(1)](#flatpak-remote-modify)
