# CMake package guidelines

This document covers standards and guidelines on writing PKGBUILDs for software that uses .

From the CMake web page:

:CMake is an open-source, cross-platform family of tools designed to build, test and package software. CMake is used to control the software compilation process using simple platform and compiler independent configuration files, and generate native makefiles and workspaces that can be used in the compiler environment of your choice.

## Typical usage
The typical usage consists of running the  command and after that execute the building command. The  command usually sets some parameters, checks for the needed dependencies and creates the build files, letting the software ready to be built by other tools like  and .

## CMake undesired behaviors
Due to its own internal characteristics for generating the build files, sometimes CMake can behave in undesired ways. Being such, some steps should be noted when writing PKGBUILDs for CMake-based software.

## CMake can automatically override the default compiler optimization flag
It is very common to see people running CMake with the  option. Some upstream projects even inadvertently include this option in their building instructions, but this produces an undesired behavior.

Each build type causes CMake to automatically append a set of flags to  and . When using the common  build type, it automatically appends the compiler optimization flag, and this overrides the default Arch Linux flag which currently is  (defined in the makepkg configuration file). This is undesired, as it deviates from the Arch Linux targeted optimization level.

## Notes about -O3
Using  does not guarantee that the software will perform better, and sometimes it can even slow down the program. It can also break software in some situations. There is a good reason why the Arch Linux developers choose  as the target optimization level and we should stick with it. Unless you know exactly what you are doing, or if upstream explicitly tells or implies that  is needed, we should avoid using it in our packages.

## Fixing the automatic optimization flag override
Fixing this in a 100% guaranteed way is not a simple question due to CMake flexibility. Please note that there is no standard solution that can be applied to all cases. This section will discuss possible solutions and some points that should be observed.

The default CMake build type is  and it does not append any flags to  and  by default, so simply omitting the usage of the  option can work as it will default to . But note that omitting this option is not guaranteed to fix the problem, as many software projects automatically set the build type to  (or other type) in the CMake files if  is not set at command line. Also be aware of possible references to source files in the resulting package and the corresponding makepkg's  caused by a missing  definition in the  build type.

Since the default  build type does not append any flags to  and  by default, using the  option can also work. Generally speaking, using the  option is better than omitting the usage of . It will cover the case when upstream automatically sets the build type to  when  is omitted, it will not append any flags by default and it is uncommon to see software setting undesired flags for the  build type.

But unfortunately, things are not that simple like only using  to fix this. When using the  build type to fix the  issue, one may fall into another problem. It is a common practice for many software projects to define some required compiler flags for the  build type in the CMake files (for example, like setting the  and  CMake variables). Such software may break or misbehave when compiled without these upstream defined flags if you use the  build type. In order to determine if you are missing some flags you will need to look at the CMake files, or you can compare the output of  for the  and  build types. What to do if the  build type causes some upstream defined flags to be missed? In this case you may be at the middle of two problematic situations, because if you use the  build type you may be using the undesired  flag, and if you use the  build type you will miss some required upstream defined flags. There is no standard way of solving this situation and it should be analyzed on a case-by-case basis. If upstream defines  for the  build type, you can use  (see below). Otherwise, patching the CMake files may be a solution.

Some few software projects hardcode  for the  build type in their CMake files, and thus  can be safely set in this case if you are sure that  is the optimization level being used.

## Verifying the fixes
You can verify if the fixes are being correctly used by CMake by enabling the verbose mode of the build tool. For example, when using  (which is the CMake default), this can be done by adding  to it (like ). This will enable  to output the compiler commands that are being executed. You can then run makepkg and examine the output to see if the compiler is using the  and  flags. If multiple optimization flags are being displayed in each command line, the last flag in the line will be the one used by the compiler (it means that  needs to be the last optimization flag in order to be effective).

## Prefix and library install directories
The standard Arch Linux  prefix can be specified by the  CMake option. This is usually needed because a lot of software defaults to install files into the  prefix.

Some upstream projects set their CMake files to install libraries into the  directory. If this is the case, you can correctly set the library installation directory to  by using the  CMake option.

## Tips and tricks
## Specifying directories
Since CMake version 3.13, there is a  option that automatically creates the build directory. This avoids the creation of the build directory by a separated  (or ) command. The  option specifies the source directory (where to search for a  file) and avoids the need of 'ing into the source tree before executing . Combined together, these two options are a convenient way to specify the build and the source directories.

Since building a typical CMake project requires many options, it is convenient to specify them in a local array in the build function. This avoids the need to use backslashes to split the long command to multiple lines and allows to include comments for each option separately.

{{hc|PKGBUILD|2=
build() {
  local cmake_options=(
    -B build
    -S $pkgname-$pkgver
    # Any other options required to build a project may follow
    [other_cmake_options
  )
  cmake "${cmake_optionscmake --build build
}
}}

## Reducing possible unneeded output
The  CMake option will suppress the output of some warnings that are meant only for the upstream project developers who write the  files. Removing these warnings makes the CMake output smoother and reduces the burden on examining it. As a general rule, these warnings usually can be safely ignored by packagers.

## Removing insecure RPATH references from binaries
Sometimes the resulting binaries can contain insecure references in . This can be verified by running Namcap on the built package and consists in a security issue that should be fixed. There is a good chance to fix this by using the  or  CMake options. You need to experiment with both and see what will work in the software in question (using both options is not needed).

## Getting all available CMake options
For getting all "visible" CMake options that are available for a software project, execute  in the source tree (where the main  file is located).

If you want to save the output for later reference, you can redirect it to a file:

 $ cmake -LAH >options.txt 2>&1

## Avoiding FetchContent downloads during the build
CMake provides the [https://cmake.org/cmake/help/latest/module/FetchContent.html FetchContent module that allows fetching additional resources or subprojects at build-time. However, ideally all sources should be fetched by makepkg prior to the build, as they are specified in the  array. This can be accomplished via the option FETCHCONTENT_SOURCE_DIR_, which allows specifying the path to the files that would otherwise be fetched. Additionally, FETCHCONTENT_FULLY_DISCONNECTED=ON can be used to skip all downloads during the build, even if you missed any  declarations.

## Example
Assume a project fetches the resource :

Then, instead of downloading it during the build, this resource can be added to the  array and declared when generating the build files:

 $ cmake -B build -S "$pkgname-$pkgver" -DFETCHCONTENT_FULLY_DISCONNECTED=ON -DFETCHCONTENT_SOURCE_DIR_FOO="$srcdir/foo"

## Template
Here is a general template for the  function that serves as a starting point for CMake-based packages. Supposing the package is C and C++ based and that it does not define any required compiler flags for the  build type in the CMake files.

{{hc|1=PKGBUILD|2=
build() {
  local cmake_options=(
    -B build
    -S $pkgname-$pkgver
    -W no-dev
    -D CMAKE_BUILD_TYPE=None
    -D CMAKE_INSTALL_PREFIX=/usr
  )
  cmake "${cmake_optionscmake --build build
}

check() {
  local excluded_tests=""
  local ctest_flags=(
    --test-dir build
    # show the stdout and stderr when the test fails
    --output-on-failure
    # execute tests in parallel
    --parallel $(nproc)
    # exclude problematic tests
    --exclude-regex "$excluded_tests"
  )
  ctest "${ctest_flags[@}"
}

package() {
  DESTDIR="$pkgdir" cmake --install build
}
}}

Do not forget to place  in makedepends.

## Example packages
*
*
