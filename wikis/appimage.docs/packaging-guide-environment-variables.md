# Environment variables

The AppImage runtimes make some environment variables available that can be used by applications bundled as AppImages during runtime, e.g., to recognize whether it's currently run from an AppImage, or to get some path information.

Depending on the type of the AppImage, the runtimes offer different feature sets.

## Type 1 AppImage runtime

> [!NOTE]
> Type 1 is the deprecated/outdated AppImage type that is only in legacy support mode. It is not recommended to make new type 1 AppImages. We strongly recommend you to use `appimagetool` to make type 2 AppImages.

| Variable name | Contents |
|----|----|
| `APPIMAGE` | (Absolute) path to AppImage file (with symlinks resolved) |
| `APPDIR` | Path of mountpoint of the ISO9660 image contained in the AppImage |
| `OWD` | Path to working directory at the time the AppImage is called |

## Type 2 AppImage runtime

The type 2 AppImage runtime makes a few environment variables available for use in e.g., `AppRun` scripts:

| Variable name | Contents |
|----|----|
| `APPIMAGE` | (Absolute) path to AppImage file (with symlinks resolved) |
| `APPDIR` | Path of mountpoint of the SquashFS image contained in the AppImage |
| `OWD` | Path to working directory at the time the AppImage is called |
| `ARGV0`| Name/path used to execute the script. This corresponds to the value you'd normally receive via the `argv` argument passed to your `main` method. Usually contains the filename or path to the AppImage, relative to the current working directory. |

> [!NOTE]
> `APPIMAGE` and `ARGV0` have very different use cases.
>
> `APPIMAGE` shall be used every time the full path of the AppImage is needed, e.g., if you need to touch the AppImage file, for example when you want to update it or read some meta information.
>
> `ARGV0` provides information how the AppImage was called. When you call an AppImage through a symlink for instance, you can get the path to this symlink through `ARGV0`, while `APPIMAGE` would contain the absolute path to the file behind that symlink.
>
> Scenarios where `ARGV0` is really useful involve so-called multi-binary AppImages, where the filename in `ARGV0` defines which program is called inside the AppImage. This concept is also known from single-binary tools like [BusyBox](https://en.wikipedia.org/wiki/BusyBox), and can be implemented in a custom `AppRun` script (see `Architecture` for more information).
