# Concepts

The AppImage development follows a few easy-to-understand core principles and concepts that keep it simple to use for developers and users. In this section, the most prominent concepts are explained.

## One app = one file

AppImages are simple to understand. Every AppImage is a regular file, and every AppImage contains exactly one app with all its dependencies. Once the AppImage is `made executable`, a user can just run it, either by double clicking it in their desktop environment's file manager, by running it from the console etc.

> [!NOTE]
> On a regular basis, [users ask](https://github.com/AppImage/AppImageKit/issues/848) about implementing support for some sort of "reusable/shared frameworks". These frameworks are supposed to contain bundles of libraries which are needed by more than one AppImage, and hence could save some disk space. For management, they suggest complex automagic systems that will automatically fetch the "frameworks" from the Internet if they're not available, or some complicated, mostly manual methods how to users could bundle frameworks together with the AppImages on portable disks like USB sticks.
>
> These may be good ideas for some people, and even if they worked perfectly fine, they'd break with our most important concept: `one app = one file`. AppImages are so simple to understand *because* every application is a single file. There's no complexity in this approach, even grandma could understand it. And after all, disk space is cheap nowadays, right?
>
> If you prefer this approach or absolutely need it, please check out alternative approaches. AppImage will never implement such a feature.

## Do not depend on system-provided resources

The author of an AppImage needs to decide for which target systems (Linux distributions) they want to offer the AppImage. Then, the author needs to bundle any dependencies that cannot reasonably be assumed to come with every target system (Linux distributions) in its default installation in a recent enough version.

To be able to run on any Linux distribution, an AppImage should bundle all the resources it needs at runtime that cannot be reasonably expected to be "there" in the default installation of all still-supported target systems (Linux distributions). The most common resources are the actual binaries, shared library dependencies, icons and other graphics and of course one or more desktop files for desktop integration.

This doesn't mean an AppImage must not use resources provided by the system, like for example basic libraries that can be assumed to be part of every target system (e.g., the C standard library or graphics libraries), user interface themes or the like. See the [excludelist](https://github.com/AppImage/pkg2appimage/blob/master/excludelist) for a list of the libraries we consider to currently be part of each still-supported target system (distribution).

## Build on old systems, run on newer systems

It is considered best practice to develop and compile the application on the oldest still-supported Linux distribution that we can assume users to still use. For example, the oldest still-supported LTS release of Ubuntu is a good choice to develop applications against and build applications on.

Applications should be built on the oldest possible system, allowing them to run on newer system. This allows the exclusion of certain "base libraries", which can be expected to be present on all major desktop Linux distributions, reducing the overhead of `one app = one file`. These dependencies are mostly shared libraries and involve low level libraries like `libc.so.6` (the GNU C library, the C language standard library the majority of all Linux distributions use), but also common libraries like [zlib](https://zlib.net/) or the [GLib](https://developer.gnome.org/glib/) libraries are normally present.

It may seem contradictory to `the previous section` to rely on distribution provided resources. This is a trade-off between trying to reduce redundancies while at the same time being as self-contained as possible.

In some cases, including the libraries might even break the AppImage on the target system. Those libraries involve, among others, hardware dependent libraries such as graphics card drivers provided libraries (e.g., `libGL.so.1`, ([source](https://github.com/AppImage/pkg2appimage/blob/14c255b528dd88ef3e00ae0446ac6d84a20ac798/excludelist\#L38-L41))), or libraries that are build and linked differently on different distributions (e.g.,`libharfbuzz.so.0` and `libfreetype.so.6` ([source](https://github.com/AppImage/pkg2appimage/blob/14c255b528dd88ef3e00ae0446ac6d84a20ac798/excludelist\#L98-L102)).

The list of libraries that can resp. have to be excluded, the so-called [excludelist](https://github.com/AppImage/pkg2appimage/blob/master/excludelist), is carefully curated by the AppImage team, and is regularly updated.

## AppImage specification

The term *AppImage* does not refer to some software project, but is actually a standard specified in the `AppImage specification`. Its reference implementation is called `ref-appimagekit`.

Being designed as a standard with a reference implementation allows users to implement their own tools to build AppImages, and helps maintaining compatibility between different tools and components.

## AppDirs

The term *AppDir* refers to an application directory. These directories are the "source" of AppImages. When `ref-appimagetool` builds an AppImage, it creates a read-only image of such a directory, prepends the `ref-runtime`, and marks the file executable.

The AppDir format is described in the `ref-appdir-specification`.
