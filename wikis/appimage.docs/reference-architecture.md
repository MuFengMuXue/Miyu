# Architecture

AppImage follows a very simple architecture, which is explained in this section.

## Overview

An AppImage consists of two parts: a *runtime* and a *file system image*. For the current type 2, the file system in use is SquashFS.

<figure class="align-center">
<img src="/_static/img/reference/architecture-overview.svg" alt="/_static/img/reference/architecture-overview.svg" />
<figcaption>AppImage file structure. Copyright © [@TheAssassin](https://github.com/TheAssassin) 2019. Licensed under CC-By-SA Intl 4.0.</figcaption>
</figure>

What happens when an AppImage is run is that the operating system runs the AppImage as an executable. The runtime, the executable part, tries to mount the file system image using `FUSE`. If that succeeds, the `AppDir` is available in a `temporary mountpoint`, and can be used like a read-only directory.

The runtime continues by calling the AppDir's "entrypoint" `AppRun` using the operating system facilities. There are no checks performed by the runtime, the operating system is simply tasked with the execution of `<AppDir mountpoint>/AppRun`. This provides a lot of flexibility, as AppRun can be an arbitrary executable, a script with a [shebang](https://en.wikipedia.org/wiki/Shebang_(Unix)), or even a simple symlink to another executable within the AppDir. The file must be executable.

The contents of an AppDir are completely user-specified, although there are tools that help with packaging. For more information, see the `packaging guide`.
