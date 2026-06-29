# KDE package guidelines

The KDE packages on Arch Linux follow a certain schema.

## Build directory
A good way of building CMake packages is to make a build directory outside the root of the project and run cmake from that directory. The PKGBUILD should look this way:

{{bc|
prepare() {
  mkdir -p build
}

build() {
  cd build
  cmake ../${pkgname}-${pkgver}
}
}}

## Install prefix
Every packages must set the  variable.

 -DCMAKE_INSTALL_PREFIX=/usr

## Build type
Generally you should not specify the build type; this makes CMake honor environmental variables like such as , , etc. == Force Qt version ==

## KF package naming
## Plasma widgets
Plasma widgets (formerly Plasmoids) packages should be named  so that they are recognizable as Plasma 6-related packages; this also distinguishes them from the official packages. See [https://aur.archlinux.org/packages?K=plasma6-applets plasma6-applets examples.

## Runners
Plasma runners packages should be named  so that they are recognizable as Plasma 6-related packages; this also distinguishes them from the official packages. See plasma6-runners examples.

## Service menus
Service menus packages should be named  so that they are recognizable as KF6 related packages. See kf6-servicemenus examples.

## Themes
Plasma themes packages should be named  so that they are recognizable as Plasma 6-related packages. See plasma6-themes examples.

## Icons and .desktop files installation
Some KDE software provide icons in the hicolor icon theme and  files, which must be installed via pacman hooks. Refrain from using installation command for these type of files in a , as it would result in unnecessary double execution of them.
