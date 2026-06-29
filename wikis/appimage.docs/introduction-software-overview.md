# Software Overview

\- list deprecated components

## AppImage project

### AppImageKit

[AppImageKit](https://github.com/AppImage/AppImageKit) is the reference implementation of the `AppImage specification`. It is split up into several components, which are described in this subsection.

#### runtime

The runtime provides the "executable header" of every AppImage. When executing an AppImage, the runtime within the AppImage is run, which mounts the embedded file system image read-only in a temporary location, and launches the payload application within there. After the payload application exited, the runtime unmounts the squashfs image and cleans up the temporary resources (such as, the temporary mountpoint directory).

**Download:** There is usually no reason to download this manually, but if you still want to, you can get it from <https://github.com/AppImage/type2-runtime/releases/continuous>. Keep in mind that on its own it does nothing, it needs to be combined with a filesystem image to form a valid AppImage, usually by using appimagetool which comes with its own copy of the runtime.

#### appimagetool

appimagetool is the easiest way to create AppImages from existing directories on the system, the so-called `AppDirs`. It creates the AppImage by embedding the `runtime`, and creating and appending the filesystem image.

appimagetool implements all optional features, like for instance [update information](https://github.com/AppImage/AppImageSpec/blob/master/draft.md#update-information), `signing`, and some linting options to make sure the information in the AppImage is valid (for instance, it can validate `AppStream files`).

**Download:** You can get it as an AppImage from <https://github.com/AppImage/appimagetool/releases/continuous>.

#### AppRun

Every AppImage's AppDir must contain a file called `AppRun`, providing the "entry point". When running the AppImage, the `runtime` executes the `AppRun` file within the `AppDir`.`AppRun` doesn't necessarily have to be a regular file. If the application is `relocatable`, it can just be a symlink to the main binary. Tools like `ref-linuxdeploy` can turn applications into relocatable applications, and therefore create such a symlink.

In some cases, though, when an existing application must not be altered (e.g., when the license prohibits any modifications) or tools like linuxdeploy cannot be used, AppImageKit's `AppRun.c` can be used.`AppRun.c` attempts to make programs load bundled shared libraries instead of system ones by manipulating environment variable. Furthermore, it attempts to prevent warnings users might encounter that are coming from the fact the `AppDir` is mounted read-only.

Using `AppRun.c` is not a guarantee that an application will run, and the packager must provide all the resources an application could need manually (or by using external tools) before creating the AppImage with `appimagetool`.`AppRun` force-changes the current working directory, and therefore applications can not detect where the AppImage was called originally. This may be especially annoying for CLI tools, but can also be a problem for GUI applications expecting paths via parameters.

> [!NOTE]
> `AppRun.c`, the binary from AppImageKit, is legacy technology and should be avoided if possible. Tools like `linuxdeploy` deploy applications in a different way (they are smart enough so that a simple symlink called `AppRun` to the main binary works just fine), and made using `AppRun.c` obsolete in most cases.
>
> There are some edge cases where `AppRun.c` is still in use, and there it might be useful. However, it suffers from many limitations and requires some workarounds (which require troublesome mechanisms, such as e.g., force-changing current working directory, as described in this section), which can cause a lot of trouble while trying to debug an AppImage. Please beware of these before thinking about using `AppRun.c` in your AppImage.

**Download:** There is usually no reason to download this manually, but if you still want to, you can get it from <https://github.com/AppImage/AppImageKit/releases/continuous>.

#### Helpers

AppImageKit ships with a few helpers that can be used to verify and validate some AppImage features.

##### validate

`validate` can validate the PGP signatures inside AppImages.

Normally there is no need to use this directly, this is mainly for debugging for AppImage developers.

**Download:** Currently this needs to be build from source. The source is in <https://github.com/AppImage/AppImageKit/>. In the future it may become bundled with or its functionality may become integrated into appimagetool.

##### digest-md5

Calculates the MD5 digest used for desktop integration purposes for a given AppImage. This digest depends on the path, not on the contents.

Normally there is no need to use this directly, this is mainly for debugging for AppImage developers.

**Download:** Currently this needs to be build from source. The source is in <https://github.com/AppImage/AppImageKit/>. In the future it may become bundled with or its functionality may become integrated into appimagetool.

### AppImageUpdate

[AppImageUpdate](https://github.com/AppImage/AppImageUpdate) lets you update AppImages in a decentralized way using information embedded in the AppImage itself.

The project consists of two tools: `appimageupdatetool`, a full-featured CLI tool for updating AppImages and dealing with [update information](https://github.com/AppImage/AppImageSpec/blob/master/draft.md\#update-information), and `AppImageUpdate`, a user interface for updating AppImages written in Qt.

**Download:** You can get it as an AppImage from <https://github.com/AppImage/AppImageUpdate/releases/continuous>.

### appimaged

[appimaged](https://github.com/probonopd/go-appimage/releases) is a daemon that monitors a predefined set of directories on the system, looking for AppImages. It automatically integrates all AppImages it can find during an initial search, and then live watches for new AppImage (or AppImages that were removed) and (de)integrates these immediately.

It is shipped as an AppImage.

> [!WARNING]
> One of the monitored directories is `$HOME/Downloads`. If the directory is very large, appimaged usually needs quite long to visit all files. It is likely to slow down the system (specifically, the filesystem).

**Download:** You can get it as an AppImage from <https://github.com/probonopd/go-appimage/releases>.

## Third-party tools

This section showcases a couple of third-party tools that can be used to create and handle AppImage files.

### linuxdeployqt

[linuxdeployqt](https://github.com/probonopd/linuxdeployqt) is a simple Qt-based command line tool that can be used to create AppDirs and AppImages. It is based on the similar macdeployqt tool that comes with Qt. It can be used to produce AppDirs and AppImages for C, C++, and Qt/QML applications, as well as applications written in other compiled languages.

See also:

> There is a copy-and-paste example for how to use it on Travis CI at <https://github.com/probonopd/linuxdeployqt#using-linuxdeployqt-with-travis-ci>.

**Download:** You can get it as an AppImage from <https://github.com/probonopd/linuxdeployqt/releases/tag/continuous>.

### linuxdeploy

[linuxdeploy](https://github.com/linuxdeploy/linuxdeploy) is a simple yet flexible, plugins-based to use tool that can be used to create AppDirs and AppImages. It has been developed in 2018, and describes itself as an "AppDir creation and maintenance tool".

linuxdeploy is planned to succeed of `linuxdeployqt`, and can be used in all projects that use `linuxdeployqt`. The list of plugins is continually growing, providing solutions for bundling frameworks such as [Qt](https://github.com/linuxdeploy/linuxdeploy-plugin-qt) as well as complete environments for non-native programming languages such as [Python](https://github.com/linuxdeploy/linuxdeploy-plugin-conda).

See also:

> There's a guide on `native binary packaging` and a general `linuxdeploy user guide` in the `ref-packaging-guide`.

**Download:** You can get it as an AppImage from <https://github.com/linuxdeploy/linuxdeploy/releases/continuous>.

### AppImageLauncher

[AppImageLauncher](https://github.com/TheAssassin/AppImageLauncher) is a helper application for Linux distributions serving as a kind of "entry point" for running and integrating AppImages.

Quoting the README:

> AppImageLauncher makes your Linux desktop AppImage ready™. By installing it, you won't ever have to worry about AppImages again. You can always double click them without making them executable first, just like you should be able to do nowadays. You can integrate AppImages with a single mouse click, and manage them from your application launcher. Updating and removing AppImages becomes as easy as never before.
>
> Due to its simple but efficient way to integrate into your system, it plays well with other applications that can be used to manage AppImages, for example app stores. However, it doesn't depend on any of those, and can run completely standalone.
>
> Install AppImageLauncher today for your distribution and enjoy using AppImages as easy as never before!
>
> -- <https://github.com/TheAssassin/AppImageLauncher/blob/master/README.md>

AppImageLauncher doesn't provide any kind of "app store" software, but integrates into system-provided launchers' context menus. It provides tools for updating (based on `AppImageUpdate`) and removing AppImages.

**Download:** You can get AppImageLauncher-Lite as an AppImage and the full version as a deb from <https://github.com/TheAssassin/AppImageLauncher/releases/continuous>.

### NX Software Center

A portable Software Center for portable applications thanks to AppImage.

**Download:** You can get NX Software Center as part of Nitrux OS from <https://nxos.org/>. There are currently no recent continuous standalone AppImage builds available.

Describe the rest of the third-party tools
