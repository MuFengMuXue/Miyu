# Flatpak Builder Command Reference

Version 1.4.8

### Important

The command reference is generated from the flatpak-builder repo; see [https://github.com/flatpak/flatpak-builder/tree/master/doc](https://github.com/flatpak/flatpak-builder/tree/master/doc)

Flatpak-builder is a tool to build flatpak applications.

**Table of Contents**

[Executables](#id1338)

[flatpak-builder](#flatpak-builder) — Help build application dependencies

[File Formats](#id1339)

[flatpak manifest](#flatpak-manifest) — Information for building an application

## Executables

**Table of Contents**

[flatpak-builder](#flatpak-builder) — Help build application dependencies

## Name

flatpak-builder — Help build application dependencies

## Synopsis

`flatpak-builder` \[OPTION...\] DIRECTORY MANIFEST

`flatpak-builder` --run \[OPTION...\] DIRECTORY MANIFEST COMMAND

`flatpak-builder` --show-deps \[OPTION...\] MANIFEST

`flatpak-builder` --show-manifest \[OPTION...\] MANIFEST

## Description

**flatpak-builder** is a wrapper around the **flatpak build** command that automates the building of applications and their dependencies. It is one option you can use to build applications.

The goal of **flatpak-builder** is to push as much knowledge about how to build modules to the individual upstream projects. It does this by assuming that the modules adhere to the Build API specified at https://github.com/cgwalters/build-api. This essentially means that it follows the **./configure && make && make install** scheme with an optional autogen script. If the upstream does not adhere to the API you can make it do so by adding patches and extra files.

An invocation of **flatpak-builder** proceeds in these stages, each being specified in detail in json format in MANIFEST :

- Download all sources

- Initialize the application directory with **flatpak build-init**

- Build and install each module with **flatpak build**

- Clean up the final build tree by removing unwanted files and e.g. stripping binaries

- Finish the application directory with **flatpak build-finish**

After this you will end up with a build of the application in DIRECTORY , which you can export to a repository with the **flatpak build-export** command. If you use the `--repo` option, flatpak-builder will do the export for you at the end of the build process. When flatpak-builder does the export, it also stores the manifest that was used for the build in /app/manifest.json. The manifest is 'resolved', i.e. git branch names are replaced by the actual commit IDs that were used in the build.

At each of the above steps flatpak caches the result, and if you build the same file again, it will start at the first step where something changes. For instance the first version controlled source that had new commits added, or the first module where some changes to the MANIFEST file caused the build environment to change. This makes flatpak-builder very efficient for incremental builds.

When building a flatpak to be published to the internet, `--collection-id=COLLECTION-ID` should be specified as a globally unique reverse DNS value to identify the collection of flatpaks this will be added to. Setting a globally unique collection ID allows the apps in the repository to be shared over peer to peer systems without needing further configuration.

## Manifest

The manifest file is a json or yaml file whose format is described in detail in its own manual page.

## Options

The following options are understood:

`-h`, `--help`  
Show help options and exit.

`-v`, `--verbose`  
Print debug information during command processing.

`--version`  
Print version information and exit.

`--arch=ARCH`  
Specify the machine architecture to build for. If no architecture is specified, the host architecture will be automatically detected. Only host compatible architectures can be specified.

`--default-branch=`*`BRANCH`*  
Set the default branch to *`BRANCH`*. This is used if the manifest does not specify a branch. The default is `master`.

`--disable-cache`  
Don't look at the existing cache for a previous build, instead always rebuild modules.

`--disable-rofiles-fuse`  
Disable the use of rofiles-fuse to optimize the cache use via hardlink checkouts.

`--disable-download`  
Don't download any sources. This only works if some version of all sources are downloaded already. This is useful if you want to guarantee that no network i/o is done. However, the build will fail if some source is not locally available.

`--disable-updates`  
Download missing sources, but don't update local mirrors of version control repos. This is useful to rebuild things but without updating git, bzr or svn repositories from the remote repository.

`--disable-tests`  
Don't run any of the tests.

`--run`  
Run a command in a sandbox based on the build dir. This starts flatpak build, with some extra arguments to give the same environment as the build, and the same permissions the final app will have (except filesystem permissions). The command to run must be the last argument passed to flatpak-builder, after the directory and the manifest.

Only the `--arch=`*`ARCH`*, `--ccache`, `--verbose` and `--state-dir`*`PATH`* (since 1.4.8) options can be combined with this option.

`--build-shell=MODULENAME`  
Extract and prepare the sources for the named module, and then start a shell in a sandbox identical to the one flatpak-builder would use for building the module. This is useful to debug a module.

`--show-deps`  
List all the (local) files that the manifest depends on.

Only the `--verbose` option can be combined with this option.

`--show-manifest`  
Loads the manifest, including any included files and prints it in a canonical json format. This is useful for tools that want to handle manifest files to avoid having to support both yaml and json, as well as some non-standard json handling that is supported (for example comments and multiline strings).

Only the `--verbose` option can be combined with this option.

`--download-only`  
Exit successfully after downloading the required sources.

`--bundle-sources`  
Create an additional runtime with the source code for this module. It will be named *`app-id`*`.Sources`, for example `org.gnome.Maps.Sources`.

`--build-only`  
Don't do the cleanup and finish stages, which is useful if you want to build more things into the app.

`--finish-only`  
Only do the cleanup, finish and export stages, picking up where a --build-only command left off.

`--export-only`  
Only do the export stages, picking up the build result from a previous build. This can be used to split the build and export/signature into two calls by leaving out --repo in the first call.

`--require-changes`  
Do nothing, leaving a non-existent DIRECTORY if nothing changes since last cached build. If this is not specified, the latest version from the cache will be put into DIRECTORY .

`--state-dir=PATH`  
Use this directory for storing state (downloads, build dirs, build cache, etc) rather than .flatpak-builder. This can be an absolute or relative path, but must be on the same filesystem as the specified target DIRECTORY .

`--keep-build-dirs`  
Don't remove the sources and build after having built and installed each module. This also creates a symlink to the build directory with a stable name ("build-modulename").

`--delete-build-dirs`  
Always remove the sources and build after having built each module, even if the build failed. The default is to keep failed build directories but remove successful ones. This is useful in e.g. automatic build systems.

`--ccache`  
Enable use of ccache in the build (needs ccache in the sdk). The default ccache folder can be overridden by setting the environment variable CCACHE_DIR.

`--stop-at=MODULENAME`  
Stop at the specified module, ignoring it and all the following ones in both the "download" and "build" phases. This is useful for debugging and development. For instance, you can build all the dependencies, but stop at the main application so that you can then do a build from a pre-existing checkout. Implies --build-only.

`--repo=DIR`  
After the build finishes, run **flatpak build-export** to export the result to the repository DIR . If DIR exists, it must be an OSTree repository; otherwise a new one will be created.

`-s`, `--subject=SUBJECT`  
One line subject for the commit message. Used when exporting the build results.

`-b`, `--body=BODY`  
Full description for the commit message. Used when exporting the build results.

`--collection-id=COLLECTION-ID`  
Set as the collection ID of the repository. Setting a globally unique collection ID allows the apps in the repository to be shared over peer to peer systems without needing further configuration. If building in an existing repository, the collection ID must match the existing configured collection ID for that repository.

`--token-type=VAL`  
Set type of token needed to install this commit. Setting this to a value greater than 0 implies that authentication will be needed to install the flatpak. A `token-type` property set in the manifest takes precedence over this option. Used when exporting the build results.

`--gpg-sign=KEYID`  
Sign the commit with this GPG key. Used when exporting the build results. This option can be used multiple times.

`--gpg-homedir=PATH`  
GPG Homedir to use when looking for keyrings. Used when exporting the build results.

`--jobs=JOBS`  
Limit the number of parallel jobs during the build. The default is the number of CPUs on the machine.

`--force-clean`  
Erase the previous contents of DIRECTORY if it is not empty. Since 1.4.6, deletion will be refused if DIRECTORY is the current working directory, the state directory, or any of their parent directories.

`--sandbox`  
Disable the possibility to specify build-args that are passed to flatpak build. This means the build process can't break out of its sandbox, and is useful when building less trusted software.

`--allow-missing-runtimes`  
Do not immediately fail if the sdk or platform runtimes are not installed on this system. Attempting to build any manifest modules will still fail if the sdk is missing, but may be useful for apps that install files without a sandbox build.

`--rebuild-on-sdk-change`  
Record the exact version of the sdk in the cache, and rebuild everything if it changes. This is useful if you're building against an API-unstable runtime, like a nightly build.

`--skip-if-unchanged`  
If the json is unchanged since the last build of this filename, then do nothing, and return exit code 42.

`--mirror-screenshots-url=URL`  
Mirror any media in the appstream and rewrite the media URLs in the appstream xml to the specified URL. The resulting files will be stored in the "screenshots" subdirectory in the app directory for versions earlier than 1.3.4 and "files/share/app-info/media" subdirectory for newer versions. Since version 1.4.5 this will also create a screenshot ref in the exported OSTree repo for each architecture containing the mirrored media.

`--extra-sources=SOURCE-DIR`  
When downloading sources (archives, files, git, bzr, svn), look in this directory for pre-existing copies and use them instead of downloading. The directory must match the state directory structure:

- Files and archives must be inside the folder: `downloads/<sha256>/`

- Sources of type `git`, `bzr` and `svn` must be inside the folder: `<type>/<converted-uri>/`

The `converted-uri` is constructed from `path` or `url` (in case of `git`) and from `url` (in case of `bzr` and `svn`). `://` is converted to a single underscore and every other `/` is replaced by an underscore. For example, `https://github.com/user/repo.git` becomes `https_github.com_user_repo.git`. In case of `svn` sources if `revision` is present, the folder name is `svn/<converted-uri>__r<revision>/`. In case of `git` sources, it needs to be a mirrored clone.

`--extra-sources-url=URL`  
When downloading sources (archives, files, git, bzr, svn), look at this url for mirrored downloads before downloading from the original url.

`--from-git=GIT`  
Look for the manifest in the given git repository. If this option is given, MANIFEST is interpreted as a relative path inside the repository.

`--from-git-branch=BRANCH`  
The branch to use with --from-git.

`--no-shallow-clone`  
Don't use shallow clones when mirroring git repos.

`--override-source-date-epoch`  
Set this timestamp as SOURCE_DATE_EPOCH to perform the build, instead of the last modification time of the manifest. This is available since 1.3.1.

`--compose-url-policy=POLICY`  
Set the AppStream compose URL policy. Accepted values are `partial` and `full`. `full` requires AppStream version \>= 0.16.3. Defaults to `partial` if unspecified. This policy only takes effect when used in conjunction with `--mirror-screenshots-url=URL`; otherwise the Appstream catalogue will preserve the source media URLs.

`--add-tag=TAG`  
Add this tag to the tags list of the manifest before building.

`--remove-tag=TAG`  
Remove this tag to the tags list of the manifest before building. The remove happen before processing the --add-tag option, so if both are specified, then --app-tag wins.

`--install-deps-from=REMOTE`  
Install/update build required dependencies from the specified remote.

`--install-deps-only`  
Stop after downloading dependencies.

`--install`  
When the build is finished, install the result locally.

`--user`  
Install the dependencies in a per-user installation.

`--system`  
Install the dependencies in the default system-wide installation.

`--installation=NAME`  
Install the dependencies in a system-wide installation specified by NAME among those defined in `/etc/flatpak/installations.d/`. Using --installation=default is equivalent to using --system .

## Caching

flatpak-builder caches sources and partial build results in the state directory (defaulting to the .flatpak-builder subdirectory of the current directory). If you use `--keep-build-dirs`, build directories for each module are also stored here.

It is safe to remove the state directory. This will force a full build the next time you build.

## Examples

**\$ flatpak-builder my-app-dir manifest.json**

Example manifest file:

``` programlisting
{
    "id": "org.test.TestApp",
    "runtime": "org.freedesktop.Platform",
    "runtime-version": "1.2",
    "sdk": "org.freedesktop.Sdk",
    "command": "test",
    "cleanup": [ "/include", "*.la" ],
    "build-options" : {
        "cflags": "-O2 -g",
        "cxxflags": "-O2 -g",
        "env": {
            "V": "1"
        },
        "arch": {
            "x86_64": {
                "cflags": "-O3 -g",
            }
        }
    },
    "modules": [
        {
            "name": "pygobject",
            "config-opts": [ "--disable-introspection" ],
            "sources": [
                {
                    "type": "archive",
                    "url": "http://ftp.gnome.org/pub/GNOME/sources/pygobject/2.28/pygobject-2.28.6.tar.xz",
                    "sha256": "fb8a1d4f665130a125011659bd347c7339c944232163dbb9a34fd0686577adb8"
                },
                {
                    "type": "patch",
                    "path": "required-pygobject-fix.patch"
                },
                {
                    "type": "file",
                    "path": "pygobject-extra-file",
                    "dest-filename": "extra-file"
                }
            ]
        },
        {
            "name": "babl",
            "build-options" : { "cxxflags": "-O2 -g -std=c++11" },
            "cleanup": [ "/bin" ],
            "sources": [
                {
                    "type": "git",
                    "url": "https://gitlab.gnome.org/GNOME/babl.git"
                }
            ]
        },
        {
            "name": "testapp",
            "sources": [
                {
                    "type": "bzr",
                    "url": "lp:testapp"
                }
            ]
        }
    ]
}
```

## See also

[flatpak(1)](#flatpak), [flatpak-manifest(5)](#flatpak-manifest), [flatpak-build-init(1)](#flatpak-build-init), [flatpak-build(1)](#flatpak-build), [flatpak-build-finish(1)](#flatpak-build-finish), [flatpak-build-export(1)](#flatpak-build-export)

## File Formats

**Table of Contents**

[flatpak manifest](#flatpak-manifest) — Information for building an application

## Name

flatpak-manifest — Information for building an application

## Description

Flatpak uses manifest, or recipe, files in a json or yaml format to describe how an application and its bundled dependencies can be built from sources. The manifest gets used by flatpak-builder.

## File format

The top level of the manifest file describes global attributes of the application, how it can be built, and the list of modules that need to be built.

### Toplevel properties

These are the properties that are accepted:

`id` or `app-id` (string)  
A string defining the application id.

Note, "app-id" is deprecated and preserved only for backwards compatibility.

`branch` (string)  
The branch to use when exporting the application. If this is unset the default comes from the default-branch option.

This key overrides both the default-branch key, and the --default-branch commandline option. Unless you need a very specific branchname (like for a runtime or an extension) it is recommended to use the default-branch key instead, as that can be overridden by the --default-branch option.

`default-branch` (string)  
The default branch to use when exporting the application. Defaults to master.

This key can be overridden by the --default-branch commandline option.

`collection-id` (string)  
The collection ID of the repository, defaults to being unset. Setting a globally unique collection ID allows the apps in the repository to be shared over peer-to-peer systems without needing further configuration. If building in an existing repository, the collection ID must match the existing configured collection ID for that repository.

`extension-tag` (string)  
If building an extension, the tag for the extension point to use. Since flatpak 0.11.4 a runtime may define multiple locations for the same extension point with the intention that different branches for the extension are mounted at each location. When building an extension it is necessary to know what extension point to install the extension to. This option resolves any ambiguity in which extension point to choose. If not specified, the default choice is to install into either the only location for the extension point or into the location for the untagged extension point. If there are multiple locations for the same extension point defined with different tags then an error will occur.

`token-type` (integer)  
The type of token needed to install this commit. Setting this to a value greater than 0 implies that authentication will be needed to install the flatpak.

`runtime` (string)  
The name of the runtime that the application uses.

`runtime-version` (string)  
The version of the runtime that the application uses, defaults to master.

`sdk` (string)  
The name of the development runtime that the application builds with.

`var` (string)  
Initialize the (otherwise empty) writable /var in the build with a copy of this runtime.

`metadata` (string)  
Use this file as the base metadata file when finishing.

`command` (string)  
The filename or path to the main binary of the application. Note that this must be a single executable, not a commandline or an absolute path. If you want to pass arguments, install a shell script wrapper and use that as the command.

Also note that the command is used when the application is run via **flatpak run**, and does not affect what gets executed when the application is run in other ways, e.g. via the desktop file or D-Bus activation.

`build-runtime` (boolean)  
Build a new runtime instead of an application.

`build-extension` (boolean)  
Build an extension.

`separate-locales` (boolean)  
Separate out locale files and translations to an extension runtime. Defaults to true.

`id-platform` (string)  
When building a runtime sdk, also create a platform based on it with this id.

`metadata-platform` (string)  
The metadata file to use for the platform we create.

`writable-sdk` (boolean)  
If true, use a writable copy of the sdk for /usr. Defaults to true if build-runtime is specified.

`appstream-compose` (boolean)  
Run **appstreamcli compose** during cleanup phase. Defaults to true.

`sdk-extensions` (array of strings)  
Install these extra sdk extensions in /usr.

`platform-extensions` (array of strings)  
Install these extra sdk extensions when creating the platform.

`base` (string)  
Start with the files from the specified application. This can be used to create applications that extend another application.

`base-version` (string)  
Use this specific version of the application specified in base. If unspecified, this uses the value specified in branch

`base-extensions` (array of strings)  
Install these extra extensions from the base application when initializing the application directory.

`inherit-extensions` (array of strings)  
Inherit these extra extension points from the base application or sdk when finishing the build.

`inherit-sdk-extensions` (array of strings)  
Inherit these extra extension points from the base application or sdk when finishing the build, but do not inherit them into the platform.

`tags` (array of strings)  
Add these tags to the metadata file.

`build-options` (object)  
Object specifying the build environment. See below for details.

`modules` (array of objects or strings)  
An array of objects specifying the modules to be built in order. String members in the array are interpreted as the name of a separate json or yaml file that contains a module. See below for details.

`add-extensions` (objects)  
This is a dictionary of extension objects. The key is the name of the extension. See below for details.

`add-build-extensions` (objects)  
This is a dictionary of extension objects similar to add-extensions. The main difference is that the extensions are added early and are available for use during the build.

`cleanup` (array of strings)  
An array of file patterns that should be removed at the end. Patterns starting with / are taken to be full pathnames (without the /app prefix), otherwise they just match the basename.

`cleanup-commands` (array of strings)  
An array of commandlines that are run during the cleanup phase.

`cleanup-platform` (array of strings)  
Extra files to clean up in the platform.

`cleanup-platform-commands` (array of strings)  
An array of commandlines that are run during the cleanup phase of the platform.

`prepare-platform-commands` (array of strings)  
An array of commandlines that are run after importing the base platform, but before applying the new files from the sdk. This is a good place to e.g. delete things from the base that may conflict with the files added in the sdk.

`finish-args` (array of strings)  
An array of arguments passed to the **flatpak build-finish** command.

`rename-desktop-file` (string)  
Any desktop file with this name will be renamed to a name based on id during the cleanup phase. The appdata file launchable will be updated if needed.

`rename-appdata-file` (string)  
Any appdata (metainfo) file with this name will be renamed to a name based on id during the cleanup phase. The id in the file will be updated as needed and the subsequent provides. (since 1.4.1)

`rename-mime-file` (string)  
Any mimetypes file with this name will be renamed to a name based on id during the cleanup phase. (since 1.4.0)

`rename-icon` (string)  
Any icon with this name will be renamed to a name based on id during the cleanup phase. Note that this is the icon name, not the full filename, so it should not include a filename extension.

`rename-mime-icons` (array of string)  
Any mime icons with any of these names will be renamed to a name prefixed with id during the cleanup phase. Note that these are the icon names, not the full filenames, so they should not include a filename extension. (since 1.4.0)

`appdata-license` (string)  
Replace the appdata (metainfo) project_license field with this string. This is useful as the upstream license is typically only about the application itself, whereas the bundled app can contain other licenses too.

`copy-icon` (boolean)  
If rename-icon is set, keep a copy of the old icon file.

`desktop-file-name-prefix` (string)  
This string will be prefixed to the Name key in the main application desktop file.

`desktop-file-name-suffix` (string)  
This string will be suffixed to the Name key in the main application desktop file.

### Build Options

Build options specify the build environment of a module, and can be specified globally as well as per-module. Options can also be specified on a per-architecture basis using the arch property.

These are the properties that are accepted:

`cflags` (string)  
This is set in the environment variable CFLAGS during the build. Multiple specifications of this (in e.g. per-arch area) are concatenated, separated by spaces.

`cflags-override` (boolean)  
If this is true, clear cflags from previous build options before adding it from these options.

`cppflags` (string)  
This is set in the environment variable CPPFLAGS during the build. Multiple specifications of this (in e.g. per-arch area) are concatenated, separated by spaces.

`cppflags-override` (boolean)  
If this is true, clear cppflags from previous build options before adding it from these options.

`cxxflags` (string)  
This is set in the environment variable CXXFLAGS during the build. Multiple specifications of this (in e.g. per-arch area) are concatenated, separated by spaces.

`cxxflags-override` (boolean)  
If this is true, clear cxxflags from previous build options before adding it from these options.

`ldflags` (string)  
This is set in the environment variable LDFLAGS during the build. Multiple specifications of this (in e.g. per-arch area) are concatenated, separated by spaces.

`ldflags-override` (boolean)  
If this is true, clear ldflags from previous build options before adding it from these options.

`prefix` (string)  
The build prefix for the modules (defaults to `/app` for applications and `/usr` for runtimes).

`libdir` (string)  
The build libdir for the modules (defaults to `/app/lib` for applications and `/usr/lib` for runtimes).

`append-path` (string)  
This will get appended to PATH in the build environment (with an leading colon if needed).

`prepend-path` (string)  
This will get prepended to PATH in the build environment (with an trailing colon if needed).

`append-ld-library-path` (string)  
This will get appended to LD_LIBRARY_PATH in the build environment (with an leading colon if needed).

`prepend-ld-library-path` (string)  
This will get prepended to LD_LIBRARY_PATH in the build environment (with an trailing colon if needed).

`append-pkg-config-path` (string)  
This will get appended to PKG_CONFIG_PATH in the build environment (with an leading colon if needed).

`prepend-pkg-config-path` (string)  
This will get prepended to PKG_CONFIG_PATH in the build environment (with an trailing colon if needed).

`env` (object)  
This is a dictionary defining environment variables to be set during the build. Elements in this override the properties that set the environment, like cflags and ldflags. Keys with a null value unset the corresponding variable.

`secret-env` (array of strings)  
This is an array defining which host environment variables are transfered to the build-commands or post-install environment.

`build-args` (array of strings)  
This is an array containing extra options to pass to flatpak build.

`test-args` (array of strings)  
Similar to build-args but affects the tests, not the normal build.

`config-opts` (array of strings)  
This is an array containing extra options passed to the build system during configuration.

`secret-opts` (array of strings)  
This is an array of options that will be passed to configure. This is meant to be used to pass secrets through host environment variables. Environment variables in the options will be expanded. '-DSECRET_ID=\$CI_SECRET'

`make-args` (array of strings)  
An array of extra arguments that will be passed to make

`make-install-args` (array of strings)  
An array of extra arguments that will be passed to make install

`strip` (boolean)  
If this is true (the default is false) then all ELF files will be stripped after install.

`no-debuginfo` (boolean)  
By default (if strip is not true) flatpak-builder extracts all debug info in ELF files to separate files and puts them into an extension. If you want to disable this, set no-debuginfo to true.

`no-debuginfo-compression` (boolean)  
By default when extracting debuginfo the debug sections are compressed. If you want to disable this, set no-debuginfo-compression to true.

`arch` (object)  
This is a dictionary defining a separate build options object for each arch, to override the main build options.

### Extension

Defines extension points in the app or runtime that can be implemented by extensions, supplying extra files which are available during runtime.

These are the properties that are accepted:

`directory` (string)  
The directory where the extension is mounted. If the extension point is for an application, this path is relative to /app, otherwise it is relative to /usr.

`bundle` (boolean)  
If this is true, then the data created in the extension directory is omitted from the result, and instead packaged in a separate extension.

`remove-after-build` (boolean)  
If this is true, the extension is removed when finishing. This is only interesting for extensions in the add-build-extensions property.

Additionally the standard flatpak extension properties are supported, and put directly into the metadata file: autodelete, no-autodownload, subdirectories, add-ld-path, download-if, enable-if, autoprune-unless, merge-dirs, subdirectory-suffix, locale-subset, version, versions. See the flatpak metadata documentation for more information on these.

### Module

Each module specifies a source that has to be separately built and installed. It contains the build options and a list of sources to download and extract before building.

Modules can be nested, in order to turn related modules on and off with a single key. Module scopes are always isolated, so nested modules do not inherit attributes from parent modules.

These are the properties that are accepted:

`name` (string)  
The name of the module, used in e.g. build logs. The name is also used for constructing filenames and commandline arguments, therefore using spaces or '/' in this string is a bad idea.

`disabled` (boolean)  
If true, skip this module

`sources` (array of objects or strings)  
An array of objects defining sources that will be downloaded and extracted in order. String members in the array are interpreted as the name of a separate json or yaml file that contains sources. See below for details.

`secret-env` (array of strings)  
An array defining which host environment variables is transfered to build-commands or post-install environment.

`config-opts` (array of strings)  
An array of options that will be passed to configure

`secret-opts` (array of strings)  
An array of options that will be passed to configure, meant to be used to pass secrets through host environment variables. Put the option with an environment variables and will be resolved beforehand. '-DSECRET_ID=\$CI_SECRET'

`make-args` (array of strings)  
An array of arguments that will be passed to make

`make-install-args` (array of strings)  
An array of arguments that will be passed to make install

`rm-configure` (boolean)  
If true, remove the configure script before starting build. This requires the configure script to exist in the source directory.

`no-autogen` (boolean)  
Ignore the existence of an autogen script

`no-parallel-make` (boolean)  
Don't call make with arguments to build in parallel

`install-rule` (string)  
Name of the rule passed to make for the install phase, default is install

`no-make-install` (boolean)  
Don't run the make install (or equivalent) stage

`no-python-timestamp-fix` (boolean)  
Don't fix up the \*.py\[oc\] header timestamps for ostree use.

`cmake` (boolean)  
Use cmake instead of configure (deprecated: use buildsystem instead)

`buildsystem` (string)  
Build system to use: autotools, cmake, cmake-ninja, meson, simple, qmake

`builddir` (boolean)  
Use a build directory that is separate from the source directory

`subdir` (string)  
Build inside this subdirectory of the extracted sources

`build-options` (object)  
A build options object that can override global options. Note that this is not inherited by nested modules.

`build-commands` (array of strings)  
An array of commands to run during build (between make and make install if those are used). This is primarily useful when using the "simple" buildsystem. Each command is run in `/bin/sh -c`, so it can use standard POSIX shell syntax such as piping output. If any individual entry in the array fails, then the whole build process will fail, similar to commands in a [make(1)](#make) recipe.

`post-install` (array of strings)  
An array of shell commands that are run after the install phase. Can for example clean up the install dir, or install extra files.

`cleanup` (array of strings)  
An array of file patterns that should be removed at the end. Patterns starting with / are taken to be full pathnames (without the /app prefix), otherwise they just match the basename. Note that any patterns will only match files installed by this module.

`ensure-writable` (array of strings)  
The way the builder works is that files in the install directory are hard-links to the cached files, so you're not allowed to modify them in-place. If you list a file in this then the hardlink will be broken and you can modify it. This is a workaround, ideally installing files should replace files, not modify existing ones.

`only-arches` (array of strings)  
If non-empty, only build the module on the arches listed.

`skip-arches` (array of strings)  
Don't build on any of the arches listed.

`cleanup-platform` (array of strings)  
Extra files to clean up in the platform.

`run-tests` (boolean)  
If true this will run the tests after installing.

`test-rule` (string)  
The target to build when running the tests. Defaults to "check" for make and "test" for ninja. Set to empty to disable.

`test-commands` (array of strings)  
Array of commands to run during the tests.

`license-files` (array of strings)  
Array of paths to LICENSE files of the module.

`modules` (array of objects or strings)  
An array of objects specifying nested modules to be built before this one. String members in the array are interpreted as names of a separate json or yaml file that contains a module.

### Sources

These contain a pointer to the source that will be extracted into the source directory before the build starts. They can be of several types, distinguished by the type property.

Additionally, the sources list can contain a plain string, which is interpreted as the name of a separate json or yaml file that is read and inserted at this point. The file can contain a single source, or an array of sources.

#### All sources

`only-arches` (array of strings)  
If non-empty, only build the module on the arches listed.

`skip-arches` (array of strings)  
Don't build on any of the arches listed.

`dest` (string)  
Directory inside the source dir where this source will be extracted.

#### Archive sources (tar, zip)

`type`  
"archive"

`path` (string)  
The path of the archive

`url` (string)  
The URL of a remote archive that will be downloaded. This overrides path if both are specified.

`mirror-urls` (array of strings)  
A list of alternative urls that are used if the main url fails.

`referer` (string)  
Sets the HTTP "Referer" header when downloading the archive.

`disable-http-decompression` (boolean)  
Disables decompression of downloads over HTTP for misconfigured servers.

`git-init` (boolean)  
Whether to initialise the repository as a git repository.

`archive-type` (string)  
The type of archive if it cannot be guessed from the path. Possible values are "rpm", "tar", "tar-gzip", "tar-compress", "tar-bzip2", "tar-lzip", "tar-lzma", "tar-lzop", "tar-xz", "tar-zst", "zip" and "7z".

`md5` (string)  
The md5 checksum of the file, verified after download

Note that md5 is no longer considered a safe checksum, we recommend you use at least sha256.

`sha1` (string)  
The sha1 checksum of the file, verified after download

Note that sha1 is no longer considered a safe checksum, we recommend you use at least sha256.

`sha256` (string)  
The sha256 checksum of the file, verified after download

`sha512` (string)  
The sha512 checksum of the file, verified after download

`strip-components` (integer)  
The number of initial pathname components to strip during extraction. Defaults to 1.

`dest-filename` (string)  
Filename to for the downloaded file, defaults to the basename of url.

#### Git sources

`type`  
"git"

`path` (string)  
The path to a local checkout of the git repository. Due to how git-clone works, this will be much faster than specifying a URL of file:///...

`url` (string)  
URL of the git repository. This overrides path if both are specified. When using git via SSH, the correct syntax is ssh://user@domain/path/to/repo.git.

`branch` (string)  
The branch to use from the git repository. As of 1.2.3 this will try to auto-detect the upstream default branch. Previously this defaulted to `master`.

`tag` (string)  
The tag to use from the git repository

`commit` (string)  
The commit to use from the git repository. If branch is also specified, then it is verified that the branch/tag is at this specific commit. This is a readable way to document that you're using a particular tag, but verify that it does not change.

`disable-fsckobjects` (boolean)  
Don't use transfer.fsckObjects=1 to mirror git repository. This may be needed for some (broken) repositories.

`disable-shallow-clone` (boolean)  
Don't optimize by making a shallow clone when downloading the git repo.

`disable-submodules` (boolean)  
Don't checkout the git submodules when cloning the repository.

`disable-lfs` (boolean)  
Don't explicitly fetch or checkout LFS git objects. This will be ignored by Git if LFS filters are active in system or global gitconfig.

#### Bzr sources

`type`  
"bzr"

`url` (string)  
URL of the bzr repository

`revision` (string)  
A specific revision to use in the branch

#### Svn sources

`type`  
"svn"

`url` (string)  
URL of the svn repository, including branch/tag part

`revision` (string)  
A specific revision number to use

#### Directory sources

`type`  
"dir"

`path` (string)  
The path of a local directory whose content will be copied into the source dir. Note that directory sources don't currently support caching, so they will be rebuilt each time.

`skip` (array of strings)  
Source files to ignore in the directory.

#### File sources

`type`  
"file"

`path` (string)  
The path of a local file that will be copied into the source dir

`url` (string)  
The URL of a remote file that will be downloaded and copied into the source dir. This overrides path if both are specified.

`mirror-urls` (array of strings)  
A list of alternative urls that are used if the main url fails.

`referer` (string)  
Sets the HTTP "Referer" header when downloading the file.

`disable-http-decompression` (boolean)  
Disables decompression of downloads over HTTP for misconfigured servers.

`md5` (string)  
The md5 checksum of the file, verified after download. This is optional for local files.

Note that md5 is no longer considered a safe checksum, we recommend you use at least sha256.

`sha1` (string)  
The sha1 checksum of the file, verified after download. This is optional for local files.

Note that sha1 is no longer considered a safe checksum, we recommend you use at least sha256.

`sha256` (string)  
The sha256 checksum of the file, verified after download. This is optional for local files.

`sha512` (string)  
The sha512 checksum of the file, verified after download. This is optional for local files.

`dest-filename` (string)  
Filename to use inside the source dir, default to the basename of path.

#### Script sources

This is a way to create a shell (/bin/sh) script from an inline set of commands.

`type`  
"script"

`commands` (array of strings)  
An array of shell commands that will be put in a shellscript file

`dest-filename` (string)  
Filename to use inside the source dir, default to autogen.sh.

#### Inline data sources

This is a way to create a file with given contents.

`type`  
"inline"

`dest-filename` (string)  
Filename to use inside the source dir.

`contents` (string)  
Text data that will be put in the file.

`base64` (boolean)  
Whether content is base64-encoded.

#### Shell sources

This is a way to create/modify the sources by running shell commands.

`type`  
"shell"

`commands` (array of strings)  
An array of shell commands that will be run during source extraction

#### Patch sources

`type`  
"patch"

`path` (string)  
The path of a patch file that will be applied in the source dir

`paths` (array of strings)  
An list of paths to a patch files that will be applied in the source dir, in order

`strip-components` (integer)  
The value of the -p argument to patch, defaults to 1.

`use-git` (boolean)  
Whether to use "git apply" rather than "patch" to apply the patch, required when the patch file contains binary diffs.

`use-git-am` (boolean)  
Whether to use "git am" rather than "patch" to apply the patch, required when the patch file contains binary diffs. You cannot use this at the same time as `use-git`.

`options` (array of strings)  
Extra options to pass to the patch command.

#### Extra data sources

`type`  
"extra-data"

`filename` (string)  
The name to use for the downloaded extra data

`url` (string)  
The url to the extra data.

`sha256` (string)  
The sha256 of the extra data.

`size` (number)  
The size of the extra data in bytes.

`installed-size` (string)  
The extra installed size this adds to the app (optional).

## Build environment

When building the application each command is run in a separate sandbox with access to only the things required for it. This section describes the details of the sandbox. Any options here can be overridden globally or per-module with the `build-args` option (although such manifest will not work if you start flatpak-builder with `--sandbox`).

### Filesystem

Each module is built in its own build directory, stored in a sub directory called `build/$modulename-$count` in the state dir (which is typically `.flatpak-builder/`). Additionally there is a symlink `build/$modulename` to the latest version. In order to generate reproducible builds this directory is also mounted as `/run/build/$modulename` in the sandbox (or `/run/build-runtime/$modulename` when building runtimes) and also as `/run/active-build` since 1.4.7. This is used as current working directory for all build ops.

The destination directory for installation is accessible for writing at the place it will seen at runtime. In the case of a regular application this will be /app. If building a runtime it will instead be /usr, and when building an extension it will be at the extensionpoint directory somewhere below /app (for app extension) or /usr (for runtime extensions).

Additionally the there will be (as needed, depending on what is building) read-only mounts of the sdk at /usr, sdk extensions below that, and the application at /app. No other filesystem access is available.

### Environment

The environment can be modified in several ways in the manifest, but the default values are:

FLATPAK_ID  
The id of the application currently building.

FLATPAK_ARCH  
The architecture currently building.

FLATPAK_DEST  
The path to where the current build should install into. This is `/app` for application builds.

FLATPAK_BUILDER_N_JOBS  
The number of jobs that flatpak-builder would normally use for make -j. Defaults to ncpus unless the module disabled parallel make.

FLATPAK_BUILDER_BUILDDIR  
The path to the build directory of the module currently building. This is normally `/run/build/$MODULE`.

PATH  
`/app/bin:/usr/bin`

LD_LIBRARY_PATH  
`/app/lib`

PKG_CONFIG_PATH  
`/app/lib/pkgconfig:/app/share/pkgconfig:/usr/lib/pkgconfig:/usr/share/pkgconfig`

ACLOCAL_PATH  
`/app/share/aclocal`

C_INCLUDE_PATH  
`/app/include`

CPLUS_INCLUDE_PATH  
`/app/include`

LDFLAGS  
-L/app/lib

LC_ALL  
en_US.utf8

### Permissions

Builds have the --allow=devel and --allow=multiarch permissions that regular flatpak runs don't have by default. This limits the syscall filtering that is normally done so development tools like debuggers work. Otherwise the build sandbox is very limited, for example there is no network access.

## Examples

**\$ flatpak-builder my-app-dir manifest.json**

Example manifest file:

``` programlisting
{
    "id": "org.test.TestApp",
    "runtime": "org.freedesktop.Platform",
    "runtime-version": "1.2",
    "sdk": "org.freedesktop.Sdk",
    "command": "test",
    "clean": [ "/include", "*.la" ],
    "build-options" : {
        "cflags": "-O2 -g",
        "cxxflags": "-O2 -g",
        "env": {
            "V": "1"
        },
        "arch": {
            "x86_64": {
                "cflags": "-O3 -g",
            }
        }
    },
    "modules": [
        {
            "name": "pygobject",
            "config-opts": [ "--disable-introspection" ],
            "sources": [
                {
                    "type": "archive",
                    "url": "http://ftp.gnome.org/pub/GNOME/sources/pygobject/2.28/pygobject-2.28.6.tar.xz",
                    "sha256": "fb8a1d4f665130a125011659bd347c7339c944232163dbb9a34fd0686577adb8"
                },
                {
                    "type": "patch",
                    "path": "required-pygobject-fix.patch"
                },
                {
                    "type": "file",
                    "path": "pygobject-extra-file",
                    "dest-filename": "extra-file"
                }
            ]
        },
        {
            "name": "babl",
            "build-options" : { "cxxflags": "-O2 -g -std=c++11" },
            "cleanup": [ "/bin" ],
            "sources": [
                {
                    "type": "git",
                    "url": "https://gitlab.gnome.org/GNOME/babl.git"
                }
            ]
        },
        {
            "name": "testapp",
            "sources": [
                {
                    "type": "bzr",
                    "url": "lp:testapp"
                }
            ]
        }
    ]
}
```

## See also

[flatpak-builder(1)](#flatpak-builder)
