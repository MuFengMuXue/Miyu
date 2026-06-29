# Electron package guidelines

This document covers standards and guidelines on writing PKGBUILDs for Electron.

## Using the system electron
Arch Linux provides versioned electron* packages and an  metapackage for the latest version. They can be used to run an electron application via a shell script wrapper:

The  directory, or alternatively a file bundle called , can be found in a prebuilt electron application as the  folder (or ). Everything else is just a copy of the electron runtime and can be removed from the final package.

## Editing version on package.json
It is dangerous to edit version of Electron in  or  using . You can use  instead.

## Building compiled extensions against the system electron
Some electron applications have compiled native extensions which link to the electron runtime, and must be built using the correct electron version. Since npm/yarn will always build against a private prebuilt copy of electron, patch the electron dependency from  to reference the same version as the system electron dependency. The build system will download the prebuilt copy it requires, compile the native extensions, and package everything into a final distribution, but this can be pruned during the  step as usual.

Alternatively, you can remove the electron dependency from  and set the correct environment variables before running npm:

 export npm_config_target=$(tail /usr/lib/electron/version)
 export npm_config_arch=x64
 export npm_config_target_arch=x64
 export npm_config_disturl=https://electronjs.org/headers
 export npm_config_runtime=electron
 export npm_config_build_from_source=true
 HOME="$srcdir/.electron-gyp" npm install

Set  to a path inside the  so the build process does not place any files in your real  directory. Make sure to adjust the path for all further commands that make use of the  cache.

(more details in Electron docs).

## Using electron-builder with system electron
Many projects use electron-builder to build and package the Javascript file and Electron binaries. By default electron-builder downloads the entire electron version that is defined in the package management file (e.g. ). This might not be desired if you want to use the system electron and save the bandwidth since you are going to throw away the electron binaries anyway. The electron-builder provides the configurations  and , to specify a custom path of Electron and the version the application is packaged for respectively.

Find the electron-builder configuration file (e.g. ) and add the following settings:

*  to　 for
*  to the contents of  (without the leading  if exists)

Packages that apply this:

electron-builder configuration

Alternatively you can use the CLI to change/add these settings like this:

 ./node_modules/.bin/electron-builder --linux --x64 --dir $dist -c.electronDist=$electronDist -c.electronVersion=$electronVer

Note that you have to specify all these options or it will not work.

## Architecture
See PKGBUILD#arch.

An Electron package that contains compiled native extensions is architecture-dependent. Otherwise it is most likely architecture-independent.

If the package contains a prebuilt copy of electron, it is always architecture-dependent.

## Directory structure
If the package is architecture-dependent, install the  directory to . Otherwise use .

If the package contains a prebuilt copy of electron, copy the final distribution in its entirety to .

## Getting version of Electron
Version of Electron could be given by  in the directory containing  or .

Prebuild or Nonfree application hides version of electron from , , and  files. In such case, you may get version by replacing  or  with  and running .
