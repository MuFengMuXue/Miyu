# Installing umu-launcher

## Building

Building umu-launcher currently requires `bash`,`make`, and `scdoc` for distribution, as well as the following Python build tools: [build](https://github.com/pypa/build), [hatchling](https://github.com/pypa/hatch), [installer](https://github.com/pypa/installer), and [pip](https://github.com/pypa/pip).

Additionally, [cargo](https://github.com/rust-lang/cargo) will be required with the minimum MSRV being the latest stable versions of it's direct dependencies.

To build umu-launcher, after downloading and extracting the source code from this repository, change into the newly extracted directory
``` shell
cd umu-launcher
```

To configure the installation `PREFIX`(this is not related to wine's `WINEPREFIX`) use the `configure.sh` script

``` shell
./configure.sh --prefix=/usr
```
Change the `--prefix` as fit for your distribution, for example `/usr/local`, or `/app` for packaging through Flatpak.

Then run `make` to build. After a successful build the resulting files should be available in the `./builddir` directory

## Installing

To install umu-launcher run the following command after completing the steps described above
``` shell
make install
```

Or if you are packaging umu-launcher
``` shell
make DESTDIR=<packaging_directory> install
```

### Installing as user

Additionally, user installations are supported if desired.

First, configure the build for a user installation
``` shell
./configure.sh --user-install
```

Then run `make` install

``` shell
make install
```

**Note**: When installing as a user, this will place the executable `umu-run` in `$HOME/.local/bin`. You will need to add `$HOME/.local/bin` in your `$PATH` to be able to run umu-launcher this way by exporting the path in your shell's configuration, for example `$HOME/.bash_profile`

``` shell
export PATH="$HOME/.local/bin:$PATH"
```

### Installing through uv
Alternatively, [uv](https://github.com/astral-sh/uv) can be used to quickly setup umu-launcher. For more detail on how this feature works, see the [documentation](https://docs.astral.sh/uv/guides/scripts/).

First, create the script within the project directory.
``` shell
touch umu-run
```

Then, assuming you have `uv` installed, create the virtual environment and install the [project's dependencies](https://github.com/Open-Wine-Components/umu-launcher/blob/main/pyproject.toml).

For example
``` shell
uv add --script umu-run 'python-xlib' 'urllib3' 'truststore'
```

Afterwards, run the script through `uv`

``` shell
uv run umu-run -h
```

### Nobara
``` shell
dnf install umu-launcher
```

### Arch Linux
``` shell
pacman -S umu-launcher
```
