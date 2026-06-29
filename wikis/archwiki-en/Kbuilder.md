# Kbuilder

kbuilder is a bash script that allows you to build one of the four officially supported kernels locally with your own optional patches and configuration, under a different package name.

For example, you could fetch the sources of the  kernel, apply a patch that optimizes the kernel for intel processors, and install that kernel as linux-lts-intel-optimized.

## Installation
The following methods can be used to get kbuilder:
* Install the  package.
* Install the latest development version from the github repository.

## Building a kernel
To fetch the default vanilla  kernel sources and build the package with the default name linux-kbuilder-custom:

 $ kbuilder build

During the build process, kbuilder will inject a bash shell into the PKGBUILD. The shell will be run right before  is called, allowing you to add any patches or change the kernel config interactively. The build will continue once you exit from the shell.

To install the built packages:

 $ kbuilder install

## Build variables
Although kbuilder does not have a configuration file, you can control the build process with environment variables.

*  should be set as 'linux', 'linux-lts', 'linux-zen' or 'linux-hardened'. kbuilder will fetch and build the kernel specified with this variable. Defaults to 'linux'. For more information about the official kernels, see kernel.

*  can be set as any string. It will be appended to the end of the kernel version and the kernel package. Defaults to 'kbuilder-custom'.

*  should be set as an integer. kbuilder will replace the  line in the PKGBUILD with , where X is the integer specified.

Example usage:
 $ KBUILDER_BUILD_JOBS=4 KBUILDER_PKG_NAME_APPEND="my-custom-patch" KBUILDER_SOURCE_PKG="linux-zen" kbuilder build

## Hooks
kbuilder looks for hooks in , and uses run-parts to execute them right before  is called. The run-parts command is executed with the flag .

An example hook:

{{hc|/etc/kbuilder/hooks/05-kbuilder-hook-cpu-optimize.sh|
#!/bin/bash
#
# kbuilder hook for applying graysky2's kernel compiler patch:
# https://github.com/graysky2/kernel_compiler_patch
#

SOURCE="https://raw.githubusercontent.com/graysky2/kernel_compiler_patch/master"
PATCH="more-uarches-for-kernel-5.17+.patch"
HOOK_NAME="cpu-optimize-hook"

curl -o $PATCH $SOURCE/$PATCH || { echo "$HOOK_NAME failed when fetching $PATCH from $SOURCE" ; exit 1 ; }
patch -Np1 -i "$PATCH" || { echo "$HOOK_NAME failed when applying $PATCH" ; exit 1 ; }
}}

To create a hook, create and make executable a file, with a name following the  form: they will be run in order according to the xx value.
