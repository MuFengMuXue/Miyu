# Rust

From Wikipedia:

:Rust is a multi-paradigm, general-purpose programming language that emphasizes performance, type safety, and concurrency. It enforces memory safety—meaning that all references point to valid memory—without a garbage collector. To simultaneously enforce memory safety and prevent data races, its "borrow checker" tracks the object lifetime of all references in a program during compilation. Rust was influenced by ideas from functional programming, including immutability, higher-order functions, and algebraic data types. It is popular for systems programming.

## Core language
## Rust Core Library
The Rust Core Library is the dependency-free foundation of the Rust Standard Library. It interfaces directly with LLVM primitives, which allows Rust to be platform and hardware-agnostic. It is this integration with LLVM that allows Rust to obtain greater performance than equivalent C applications compiled with Clang, making Rust software designed with libcore lower level than C. It contains only basic platform-independent types such as , , and . Developers looking to target software for embedded platforms may forego the standard library with  to exclusively use the no-batteries-included core library for smaller binary sizes and improved performance. However, using  limits the amount of software support that you can get from the larger Rust community as a majority of libraries require the standard library.

## Rust Standard Library
The Rust Standard Library provides the convenient high level abstractions by which a majority of portable Rust software is created with. It includes the  and  types; a vast amount of methods for language primitives; a large number of standard macros; I/O and multithreading support; heap allocations with ; and many more high level features not available in the core library.

## Release cycle
Rust follows a regular six-week release cycle, similar to the release cycle of Firefox. With each new release, the core and standard libraries are improved to support more platforms, improve performance, and stabilize new features for use with stable Rust.

## Installation
The two main ways to install Rust are:

* The Native installation, recommended if you only use Rust for building or installing software made with Rust
* The rustup installation, recommended if you intend to program anything in Rust

## Native installation
To install the latest stable version of Rust from the official Arch Linux software repository, install the  package. This will install the  compiler and Cargo.

## rustup
The official and recommended method of installing Rust for the purpose of developing software is to use the rustup toolchain manager, written in Rust.

The benefit of using the rustup toolchain manager instead of the standalone prepackaged Rust in the software repository is the ability to install multiple toolchains (stable, beta, nightly) for multiple targets (windows, mac, android) and architectures (x86, x86_64, arm). It should be noted that installing rustup does not automatically install a Rust toolchain with it, nor does updating rustup through any method automatically provide the latest toolchain release of Rust.  See #Usage or rustup toolchain documentation for more on toolchains.

There are two choices for a rustup installation, one is supported by Arch Linux via pacman, while the other is officially supported by Rust via their installation script.

## Arch Linux package
 is available on the Arch Linux software repository. Note that  will not work when installed this way, the package needs to be updated by pacman. However, this change does not extend to other rustup functionality, such as  for updating Rust toolchains.

This package has the advantage that the various Rust executables live in , instead of , removing the need to add another directory to your .

In order to install the toolchain, you need to tell rustup which version to use, between  and :

## Building Rust against a new version of LLVM
Since Rust builds using a bootstrap strategy, a functional Rust package is required.  In the case of building a version of  which is newer than the version in the official repos, users will encounter the need to have a shared object from a previous version of  (one which was used to build the repo version of Rust) in order to build against the newer version of LLVM.

Example: the official repos offer llvm-18.1.8 and the goal is to build llvm-19.1.6.

The bootstrap step requires  from llvm-libs-18.1.8.  This file can be manually placed in the build root or placed by a package such as .

## Upstream installation script
rustup is also available to download and install manually via rustup's official web page.

Download the file with , view it: , and run the script  to start rustup installation. The script makes PATH changes only to login shell configuration files.  You need to  until you logout and login back into the system. To update rustup afterwards, run .

The script installs and activates the default toolchain by default (the one used by the  package), so there is no need to manually install it to start using Rust.

## Usage
You might need to manually install a toolchain, e.g. , ,  or . You also need to do this if you want to use/test another toolchain.

 $ rustup toolchain install toolchain

You can now run the Rust commands by running, . However, to use these commands directly, you need to activate the toolchain:

 $ rustup default toolchain

## Test your installation
Check the installed Rust version using :

Check that Rust is installed correctly by building a simple program, as follows:

{{hc|~/hello.rs|
fn main() {
    println!("Hello, World!");
}
}}

You can compile it with , then run it:

## Cross compiling
## Setup
Cross-compiling Rust requires installing the appropriate standard library (a separate compiler is not necessary), but also downloading the appropriate low-level tools (most often, a C compiler).
For example, for cross-compiling to Windows, the  (32-bit) and/or  (64-bit) Rust target triple(s) must be set up, and  must be installed.

## Using rustup
rustup is the recommended way to cross-compile Rust.
The documentation explains the steps involved, how to list targets, etc.

Let's take cross-compiling to 64-bit Windows as an example:

# Install the  package
# Run  to install the Rust standard library and compiler for your architecture.
# Tell Cargo where to find MinGW's GCC by adding the following to its configuration:
# Finally, you can cross compile for Windows by passing the  flag to cargo:

## Arch packages
Some packages can be installed on top of the Arch-provided , such as ; they take care of installing the necessary compiler toolchains also.

The unofficial repository archlinuxcn provides the Rust standard library for some targets as rust-std-nightly-* packages.
Some of them have optional dependencies on the necessary compiler toolchains, but others will require you to e.g. find an ARM toolchain by yourself.

## Running cross-compiled programs
 and friends can be configured to execute the built binaries using a runner.
For example, to use Wine to run 64-bit Windows programs, add the following to Cargo's configuration:

## Cargo
Cargo, Rust's package manager, is part of the  package. If you use , it already includes cargo.

Cargo is a tool that allows Rust projects to declare their various dependencies, and ensure that you will always get a repeatable build. You are encouraged to read the official guide.

## Usage
To create a new project using Cargo:

 $ cargo new hello_world

This creates a directory with a default  file, set to build an executable.

## Optimizing for native CPU platform
In order to instruct Cargo to always compile optimal code for your CPU platform, you can achieve this by adding a flag to . Please be aware that the resulting binaries can not be distributed for use on other computers, and might even fail on your own system if you decide to change your CPU in the future.

Find out which target platform is used by default on your installation:

In this example, we are using  Rust on the  platform.

Instruct Cargo to always compile code optimized for the native CPU platform:

## sccache
Compilation times can be greatly reduced by using sccache ( package). This will maintain a local cache of compiler artifacts, eliminating the need to recompile code that has not changed since the last time it was compiled.

To enable sccache, you can use  environment variable:

 $ export RUSTC_WRAPPER=sccache
 $ cargo build

or

 $ RUSTC_WRAPPER=sccache cargo build

Alternatively, add the following configuration to :

## IDE support
## Tools
See https://www.rust-lang.org/tools for the recommended tools of the Rust project.

## rust-analyzer
rust-analyzer is the official Language Server Protocol implementation for Rust which has replaced RLS.

It is available as the  package, and the latest Git version is available as . Alternatively, if you have  installed, you can install rust-analyzer with:

 $ rustup component add rust-analyzer

rust-analyzer needs the source code of the standard library. If it is not present, rust-analyzer will attempt to install it automatically using rustup. To install the source code manually using rustup, run the following command:

 $ rustup component add rust-src

## Clippy
Clippy takes advantage of compiler plugin support to provide a large number of additional lints for detecting and warning about a larger variety of errors and non-idiomatic Rust.

Clippy is included in the  package. To install it with rustup use:

 $ rustup component add clippy

## Rustfmt
Rustfmt is a tool to format Rust code according to the official style guidelines.

Rustfmt is included in the  package. To install it with rustup use:

 $ rustup component add rustfmt

## Editors
## Emacs
Emacs support for Rust can be obtained via the official rust-mode plugin.

## GNOME Builder
GNOME Builder support for Rust is achieved using Language Server Protocol. It uses rust-analyzer by default; all you need to do is install it along with the Rust source.

## Helix
Helix editor is written in Rust and has the Rust language server protocol included. Helix is inspired by Neovim and Kakoune.

## Kate
Kate support for Rust is achieved using Language Server Protocol. It uses rust-analyzer by default; all you need to do is install it along with the Rust source.

## IntelliJ IDEA
IntelliJ IDEA has a Rust plugin. The same plugin also works with CLion.

If using rustup, use rustup to download the source (), and then select  as the toolchain location.

If using Rust from the official Arch Linux software repository, select  as the toolchain location and  as the stdlib sources location.

## Jetbrains RustRover
Jetbrains is also working on a special Editor just for Rust. It can be found and downloaded under their official Website or in the AUR under  and .

## Visual Studio Code
Visual Studio Code support for Rust can be obtained via rust-analyzer with the rust-lang.rust-analyzer extension.

## Vim
Vim support for Rust can be obtained via the official rust.vim plugin, which provides file detection, syntax highlighting, formatting and support for the Syntastic syntax checking plugin. Many completion engines have Rust support, like coc (via the coc-rust-analyzer plugin) and YouCompleteMe.
