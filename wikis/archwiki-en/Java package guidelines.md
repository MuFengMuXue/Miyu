# Java package guidelines

This document defines a proposed standard for packaging Java programs under Arch Linux. Java programs are notoriously difficult to package cleanly without overlapping dependencies. This document describes a way to remedy this situation. These guidelines are flexible in order to cover the many different scenarios that arise when dealing with Java applications.

## Introduction
Arch Linux packagers cannot seem to agree on how to handle Java packages. Various methods are used in PKGBUILDs across the official and unofficial repositories and in the AUR. These solutions include placing the whole mess in  with shell scripts in  or profiles placed in . Others are placed in directories in  with scripts placed in . Many add unnecessary files to the system  and .

## Structure of a typical Java application
Most Desktop Java applications have a similar structure. They are installed from a system-independent (but package dependent!) installer. This usually installs everything in a single directory with subdirectories called , , , , etc. There is usually a main jar file containing the main executable classes. A shell script is usually provided to run the main class so users do not have to invoke the Java interpreter directly. This shell script is usually quite complex, as it is generic across distributions and often includes special cases for different systems (e.g., Cygwin).

The  directory often contains bundled jar files that satisfy dependencies of the Java application. This makes it simple for a user to install the program (all dependencies included), but is a package developer's nightmare. It is a waste of space when several packages bundle the same dependency. This was not a big issue in the past when there were fewer desktop Java applications and libraries, and those that existed tended to be very large anyway. Things are different now...

Other files necessary to run the program are usually stored in the same folder as the main jar file, or a subdirectory thereof. Since Java programs do not know where their classes were loaded from, they usually need to be run from within this directory (i.e. the shell script should  into the directory), or an environment variable is set to indicate the directory's location.

## Java packaging on Arch Linux
Packaging Java applications in Arch is going to take quite a bit more work for packagers than it currently does. The effort will be worth it, however, resulting in a cleaner filesystem and fewer bundled dependencies (as more and more Java libraries are refactored into their own packages, packaging will become easier). The following guidelines should be followed in creating an Arch Linux Java package:

* If a Java library has a generic name, the package name should be prepended with the title  to help distinguish it from other libraries. This is not necessary with uniquely named packages (like JUnit), end-user programs (like Eclipse), or libraries that can be uniquely described with another prefix (like jakarta-commons-collections or apache-ant).

* Place all jar files (and no other files) distributed with the program in a  directory. This includes all dependency jar files distributed with the application. However, effort should be made to place common or large dependency libraries into their own packages. This can only happen if the program does not depend on a specific version of a dependency library.

:This rule makes it possible to iteratively refactor dependencies. That is, the package and all its dependencies can be placed into one directory at first. After this has been tested, major dependencies can be refactored out one at a time. Note that some applications include bundled dependencies inside the main jar file. That is, they unjar the bundled dependencies and include them in the main jar. Such dependencies are usually very small and there is little point in refactoring them.

* If the program is meant to be run by the user, write a custom shell script that runs the main jar file. This script should be placed in . Libraries generally do not require shell scripts. Write the shell script from scratch, rather than using one that is bundled with the program. Remove code that tests for custom environments (like Cygwin), and code that tries to determine if  has been set (Arch does not use , it uses  to set the  symlink).

:such script should look like this for jar files:
:

: and like this for single class files:
:

* Set the  using the  option to the Java interpreter unless there is an explicit reason not to (ie: the  is used as a plugin mechanism). The  should include all jar files in the  direcory, as well as jar files that are from dependency libraries that have been refactored to other directories. You can use something like the following code:

:

* Make sure the shell script is executable!

* Other files distributed with the package should be stored in a directory named after the package under . You may need to set the location of this directory in a variable like  inside the shell script. This guideline assumes that the program expects all files to be in the same directory (as is standard with Java packages). If it seems more natural to put a configuration file elsewhere (for example, logs in ), then feel free to do so.

: Bear in mind that  may be mounted as read-only on some systems. If there are files in the shared directory that need to be written by the application, they may have to be relocated to , , or the user's home directory.

* As is standard with Arch Linux packages, if the above standards cannot be adhered to without a serious amount of work, the package should be installed in its preferred manner, with the resulting directory located in . This is useful for programs that bundle JREs or include customized versions of dependencies, or do other strange or painful tasks.

## Multiple API implementations
If your package distributes commonly used API implementation(like jdbc driver) you should place the library under . So that applications that allow user to select from various implementations will know where to look for them. Use this location only for raw library packages. If such a implementation is part of distribution of application, do not place this jar file under common location but use ordinary package structure.

## Example directory structure
To clarify, here is an example directory structure for a hypothetical program called . Since  is a common name, the package is named , but notice this is not reflected in the directory structure:

*
*
*  (included dependency of )
*
*  (some general files required by )
*  (executable shell script)

## Dependencies
Java packages might specify  or  as dependency, based on what they need. For most packages,  (Java Runtime Environment) is what is needed to simply run software written in Java.  (Java Development Toolkit) is needed by packages that will need to compile Java source code into bytecode.

See Java for more information.
