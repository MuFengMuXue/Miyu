# KDevelop

From KDevelop's website:
:KDevelop is a free and open-source integrated development environment (IDE) that is Provided by the same community as KDE. It provides editing, navigation and debugging features for several programming languages, autocorrect and suggestions and integration with build automation and many version-control systems such as git, using a plugin-based architecture that ensures that the features can be expanded and tailored to one's need.

KDevelop 5 has parser backends for C, C++, Objective-C, OpenCL and JavaScript/QML, with plugins supporting PHP, Python 3 and Ruby. Basic syntax highlighting and code folding are available for dozens of other source-code and markup formats, but without semantic analysis.

KDevelop is part of the KDE project, and is based on KDE Frameworks and Qt. The C/C++ backend uses Clang, clang-tidy and heaptrack to provide accurate information even for very complex codebases.

## Installation
Install the  package to get started.

## Features
KDevelop uses an embedded text editor component through the KParts framework. The default editor is KDE Advanced Text Editor (Kate), which can optionally be replaced with a Qt Designer-based editor. This list focuses on the features of KDevelop itself.

* Source code editor with syntax highlighting and automatic indentation (Kate).
* C/C++ language is now supported with a Clang's backend (as of KDevelop-5.0)
* Project management for different project types, such as Automake, CMake, qmake for Qt based projects and Ant for Java based projects.
* Class browser.
* GUI Designer
* Front-end for the GNU Compiler Collection and GNU Debugger.
* Wizards to generate and update class definitions and application framework.
* Automatic code completion (C/C++).
* Built-in Doxygen support.
* Revision control (also known as SCM) support. Supported systems include CVS, Subversion, Perforce, ClearCase, Git, Mercurial, and Bazaar
KDevelop 4 is a completely plugin-based architecture. When a developer makes a change, they only must compile the plugin.

Code completion is available for C and C++. Symbols are kept in a Berkeley DB file for quick lookups without re-parsing. KDevelop also offers a developer framework which helps to write new parsers for other programming languages.

An integrated debugger allows graphically doing all debugging with breakpoints and backtraces. It even works with dynamically loaded plugins unlike command line GDB.

Quick Open allows quick navigation between files.

## Plugins
Currently, around 50 to 100 plugins exist for this IDE. Major ones include persistent project-wide code bookmarks, Code abbreviations which allow expanding text quickly, a Source formatter which reformats code to a style guide before saving, Regular expressions search, and project-wide search/replace which helps in refactoring code.

Install plugins to provide autocompletion and other language-specific features:

*For PHP, install the  package
*For Python, install the  package
*For C++, install either  or  package, although Options for other Compilers also exist.

## Building additional plugins
The KDevelop Parser Generator ( package) is required to build additional plugins. Plugins will not compile if this package is not installed beforehand.

## Troubleshooting
## KDevCMakeManager
Make sure  is installed if you get the  error.

## Debugging with gdb
The debugging option to use  will not appear unless  is installed. Install  and restart KDevelop to enable  support.
