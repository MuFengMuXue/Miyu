# Rusticl

Rusticl is an OpenCL implementation on top of Gallium drivers.

## Enabling

In order to use Rusticl on any platform the environment variable
`RUSTICL_ENABLE` has to be used. Rusticl does not advertise devices
for any driver by default yet as doing so can impact system stability until
remaining core issues are ironed out.

## Enabling drivers by default

Distributions and everybody building rusticl themselves can opt-in or opt-out
certain drivers from being enabled by default. The
`gallium-rusticl-enable-drivers` takes a list of drivers to enable by
default. The environment variable `RUSTICL_ENABLE` will overwrite this
list at runtime.

Not all drivers are supported to be enabled by default, because that should
require opt-in by the driver maintainers. Check out the meson option
documentation to see for which drivers this option is supported.

The `auto` option might not enable all drivers supported by this flag, but
for distribution it's recommended to use that one unless they get an ack from
driver maintainers to expand the list.

## Building

To build Rusticl you need to satisfy the following build dependencies:

-  `rustc`
-  `rustfmt` (highly recommended, but only *required* for CI builds
   or when authoring patches)
-  `bindgen`
-  [LLVM](https://github.com/llvm/llvm-project/) built with
   `libclc` and `-DLLVM_ENABLE_DUMP=ON`.
-  [SPIRV-Tools](https://github.com/KhronosGroup/SPIRV-Tools)
-  [SPIRV-LLVM-Translator](https://github.com/KhronosGroup/SPIRV-LLVM-Translator) for a
   `libLLVMSPIRVLib.so` matching your version of LLVM, i.e. if you're
   using LLVM 15 (`libLLVM.so.15`), then you need a
   `libLLVMSPIRVLib.so.15`.

The minimum versions to build Rusticl are:

-  Rust: 1.82
-  Meson: 1.7.0
-  Bindgen: 0.71.1
-  LLVM: 15.0.0 (recommended 19.0.0)
-  Clang: 15.0.0
   Updating clang requires a rebuilt mesa and rusticl if and only if the value of
   `CLANG_RESOURCE_DIR` changes. It is defined through `clang/Config/config.h`.
-  SPIRV-Tools: any version (recommended: v2025.1)

Afterwards you only need to add `-Dgallium-rusticl=true -Dllvm=enabled
-Drust_std=2021` to your build options.

Most of the code related to Mesa's C code lives inside `/mesa`, with
the occasional use of enums, structs or constants through the code base.

If you need help ping `karolherbst` either in `#dri-devel` or
`#rusticl` on OFTC.

## Known issues

One issue you might come across is, that the Rust edition meson sets is
not right. This is a known [meson bug](https://github.com/mesonbuild/meson/issues/10664) and in order to
fix it, simply run `meson configure $your_build_dir -Drust_std=2021`
