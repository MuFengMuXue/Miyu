**Resources**

[[]][GitHub](https://github.com/doitsujin/dxvk)

**DXVK** is a [Vulkan](https://wiki.gentoo.org/wiki/Vulkan "Vulkan")-based translation layer for [Direct3D](https://en.wikipedia.org/wiki/Direct3D "wikipedia:Direct3D") 9/10/11 which allows running 3D applications on Linux using [Wine](https://wiki.gentoo.org/wiki/Wine "Wine").

## Contents

-   [[1] [Requirements]](#Requirements)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Quick start]](#Quick_start)
    -   [[2.2] [USE flags]](#USE_flags)
    -   [[2.3] [Using crossdev toolchain]](#Using_crossdev_toolchain)
-   [[3] [Configuration]](#Configuration)
    -   [[3.1] [Lutris]](#Lutris)
    -   [[3.2] [Wine]](#Wine)
-   [[4] [See also]](#See_also)
-   [[5] [External resources]](#External_resources)
-   [[6] [References]](#References)

## [Requirements]

-   [Vulkan capable GPU](https://en.wikipedia.org/wiki/Vulkan_(API)#Compatibility)
-   [Driver supported by DXVK](https://github.com/doitsujin/dxvk/wiki/Driver-support) (With AMD, you can check which driver is used by running [lspci -k]. If it says that the driver in use is radeon, your system will not be able to use DXVK.)

## [Installation]

### [Quick start]

To include both 64-bit and 32-bit bindings:

`root `[`#`]`echo 'app-emulation/dxvk ABI_X86: 64 32' >> /etc/portage/package.use/dxvk `

`root `[`#`]`emerge --ask app-emulation/dxvk`

### [USE flags]

### [USE flags for] [app-emulation/dxvk](https://packages.gentoo.org/packages/app-emulation/dxvk) [[]] [Vulkan-based implementation of D3D9, D3D10 and D3D11 for Linux / Wine]

  ------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+d3d10`](https://packages.gentoo.org/useflags/+d3d10)                   Enable support for DirectX 10 (d3d10.dll)
  [`+d3d11`](https://packages.gentoo.org/useflags/+d3d11)                   Enable support for DirectX 11 (d3d11.dll)
  [`+d3d8`](https://packages.gentoo.org/useflags/+d3d8)                     Enable support for DirectX 8 (d3d8.dll)
  [`+d3d9`](https://packages.gentoo.org/useflags/+d3d9)                     Enable support for DirectX 9 (d3d9.dll)
  [`+dxgi`](https://packages.gentoo.org/useflags/+dxgi)                     Enable support for the DirectX Graphics Infrastructure (dxgi.dll)
  [`+strip`](https://packages.gentoo.org/useflags/+strip)                   Allow symbol stripping to be performed by the ebuild for special files
  [`crossdev-mingw`](https://packages.gentoo.org/useflags/crossdev-mingw)   Use sys-devel/crossdev for the toolchain rather than dev-util/mingw64-toolchain (requires manual setting up and is mostly unsupported, try disabling if have issues)
  ------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-11-12 18:15] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Using crossdev toolchain]

To use toolchains compiled with [[[sys-devel/crossdev]](https://packages.gentoo.org/packages/sys-devel/crossdev)[]] rather than [[[dev-util/mingw64-toolchain]](https://packages.gentoo.org/packages/dev-util/mingw64-toolchain)[]], they have to be set up like this:

It is recommended to create an ebuild repository by following this [section in the Crossdev article](https://wiki.gentoo.org/wiki/Crossdev#Crossdev_overlay "Crossdev").

** Note**\
Make sure that mingw64-runtime does **not** have the `tools` useflag enabled when bootstrapping. See [[[bug #644556]](https://bugs.gentoo.org/show_bug.cgi?id=644556)[]].

The improved performance version for ABI_X86_32 `--disable-sjlj-exceptions --with-dwarf2` to `EXTRA_ECONF` for cross-i686-w64-mingw32/gcc (but not for cross-x86_64-w64-mingw32/gcc) ^[\[1\]](#cite_note-1)[\[2\]](#cite_note-2)^

`user `[`$`]`for toolchain in cross-x86_64-w64-mingw32 cross-i686-w64-mingw32; do `

      crossdev --stable --libc ">=8.0.0" --target $
      if $toolchain = "cross-i686-w64-mingw32"
      then
          crossdev --stable --libc ">=8.0.0" --lenv 'USE="libraries"' \
          --genv 'EXTRA_ECONF="--enable-treads=posix --disable-sjlj-exceptions --with-dwarf2"' \
          --init-target --target $
      else
          crossdev --stable --libc ">=8.0.0" --lenv 'USE="libraries"' \
          --genv 'EXTRA_ECONF="--enable-threads=posix"' \
          --init-target --target $
      fi
      sed "s|-libraries ||" -i /etc/portage/package.use/$
      emerge --oneshot $/mingw64-runtime
      emerge --oneshot $/gcc

done

If crossdev generation of the target toolchain should fail, ensure that `USE="libraries"` is enabled on `$/mingw64-runtime` by simply prefixing the relevant emerge command with `env USE="libraries"`, mirroring the application of the USE flag to libc via crossdev\'s `lenv` argument. Revert edits to [/etc/portage/env/mingw-gcc.conf], [/etc/portage/package.env/mingw], and [/etc/portage/package.use/mingw] before retrying, or toolchain generation will fail due to the `--enable-threads` flag.

## [Configuration]

### [Lutris]

Link the folder containing [x32] and [x64] to a subdirectory of [\~/.local/share/lutris/runtime/dxvk].

`user `[`$`]`mkdir -p ~/.local/share/lutris/runtime/dxvk `

`user `[`$`]`ln -s /usr/lib/dxvk ~/.local/share/lutris/runtime/dxvk/system `

To use the newly installed DXVK, configure the Wine runner in the Lutris GUI, show advanced options, and enter the subdirectory name ([system] in this case) as DXVK version.

### [Wine]

It is recommended to create the [\~/.wine-32] or [\~/.wine-64] directories for different architectures.

`user `[`$`]`WINEPREFIX=~/.wine-64 setup_dxvk.sh install --symlink `

`user `[`$`]`WINEPREFIX=~/.wine-32 setup_dxvk.sh install --symlink `

## [See also]

-   [Vulkan](https://wiki.gentoo.org/wiki/Vulkan "Vulkan") --- a next-generation graphics API created by The Khronos Group.
-   [Wine](https://wiki.gentoo.org/wiki/Wine "Wine") --- an application compatibility layer that allows [Microsoft Windows](https://en.wikipedia.org/wiki/Microsoft_Windows "wikipedia:Microsoft Windows") software to run on Linux and other [POSIX](https://en.wikipedia.org/wiki/POSIX "wikipedia:POSIX")-compliant operating systems.

## [External resources]

-   [DXVK README](https://github.com/doitsujin/dxvk/blob/master/README.md)
-   [Lutris DXVK Configuration](https://github.com/lutris/docs/blob/master/HowToDXVK.md)

## [References]

1.  [[[↑](#cite_ref-1)] [[GCC Wiki: Exception Handling](http://gcc.gnu.org/wiki/WindowsGCCImprovements#Exception_Handling)]]
2.  [[[↑](#cite_ref-2)] [[MinGW-w64 FAQ: Exception Handling](https://sourceforge.net/p/mingw-w64/wiki2/Exception%20Handling/)]]