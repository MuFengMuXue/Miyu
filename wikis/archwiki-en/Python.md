# Python

From Wikipedia:Python (programming language):

: Python is a high-level, general-purpose programming language that emphasizes code readability, simplicity, and ease-of-writing with the use of significant indentation… and garbage collection. Python supports multiple programming paradigms but with an emphasis on object-oriented programming and dynamic typing.

From What is Python?:

* it is an interpreted, interactive, object-oriented programming language;
* it incorporates modules, exceptions, dynamic typing, very high level dynamic data types, and classes;
* it supports multiple programming paradigms beyond object-oriented programming, such as procedural and functional programming;
* it combines remarkable power with very clear syntax;
* it has interfaces to many system calls and libraries, as well as to various window systems, and is extensible in C or C++;
* it is also usable as an extension language for applications that need a programmable interface;
* it is portable—it runs on many Unix variants including Linux and macOS, and on Windows.

## Installation
Install the  package.

## Other versions
Previous and future versions of Python are available via the Arch User Repository (AUR). These are useful for applications or projects that require specific versions, or just for curiosity. See Status of Python versions and Status key for more information.

Feature (can accept new features) and prerelease (no new features can go in):

* Python 3.15:  (feature)

Bugfix (also called maintenance or stable):

* Python 3.14:  (free-threaded—with Global Interpreter Lock, or GIL, disabled)
* Python 3.13:
* Python 3.13:  (free-threaded)

Security (accept security fixes only):

* Python 3.12:
* Python 3.11:
* Python 3.10:

End-of-life (unmaintained):

* Python 3.9:  — PEP 596
* Python 3.8:  — PEP 569
* Python 3.7:  — PEP 537
* Python 3.6:  — PEP 494
* Python 2.7:  — Sunsetting Python 2

Each of these packages installs a distinct binary named after the version number, e.g. python3.13 for Python 3.13, allowing multiple versions to coexist on a system. You can also use  or  to easily install and switch between multiple versions of Python.

Extra modules and libraries for old versions of Python may be found in the AUR by searching for , e.g. searching for  for Python 3.10 modules.

You can also download the source for any release on the https://www.python.org/downloads/ page.

## Alternative implementations
The  package installs CPython, the reference implementation of Python. However, there are also other implementations available. These implementations are usually based on older versions of Python and are not fully compatible with CPython.

Implementations available on Arch Linux include:

*
*
*
*

## Alternative shells
The  package includes an interactive Python shell (REPL) which can be launched with the  command. The following shells are also available:

*
*
*
*

## Package management
There are several ways to install Python packages on Arch Linux.

## Arch repositories
A large number of popular packages are available in the official repositories and AUR. This is the preferred way to install system-wide packages, and the only method officially supported on Arch Linux.

## Third-party packages
Developers working with Python may need to use packages or package versions not available in the Arch repositories. The recommended practice is to use a separate virtual environment to isolate each project, preventing conflicts with system packages in . Various tools are available to install packages within a virtual environment:

*
*
*
*
*

pip, pipx, poetry and uv install packages from the Python Package Index and other indexes. Conda and Miniconda use the Anaconda repositories.

As an alternative to virtual environments,  can be used to install packages into the user scheme instead of . This separates packages per-user rather than per-project. Virtual environments are usually the better choice.

See the Python Packaging User Guide for the official best practices for package management.

## Historical notes
Historically, easy_install (part of ) was used to install packages distributed as Eggs. easy_install and Eggs have been replaced with pip and Wheels. See pip vs easy_install and Package Formats for more information.

Previous versions of pip could install third-party packages system-wide, but this caused a number of problems outlined in PEP668. The system-wide environment is now marked as an externally managed environment, and pip no longer allows system-wide installation.

## Widget bindings
The following widget toolkit bindings are available:

*
*
*
*
*
*

To use these with Python, you may also need to install the associated widget toolkit packages (e.g.  must also be installed to use Tkinter).

## Tips and tricks
## Virtual environment
Python provides tools to create isolated virtual environments into which packages may be installed without conflicting with other virtual environments or the system packages. Virtual environments can also run applications with different versions of Python on the same system.

See Python/Virtual environment for details.

## Tab completion in Python shell
Tab completion is available in the interactive shell by default. Note that the readline completer will only complete names in the global namespace. You can use  for a richer tab completion experience === List packages built for a specific Python version ===

Sometimes it is useful to know which installed packages were built for a specific version of Python. For example,

 $ pacman -Qoq /usr/lib/python3.12

will list all those built for Python version 3.12. This is especially useful when the official Python version is updated and one wants to get a list of packages from the AUR that need rebuilding because they were built for a possibly no longer installed Python version, see #Module not found after Python version update.

## Troubleshooting
## Module not found after Python version update
A Python-based application might output  for an installed dependency named  after having upgraded the  package to a new minor version (e.g. from version 3.10 to 3.11).

The above scenario happens when a dependency is not available for that Python version or not installed at all. Python packages are installed in a versioned site-packages directory ( if system-wide, or  if per-user, where  is a version like "3.11"). So whenever there is a new minor version upgrade, the Python-based package built with previous Python version must be rebuilt against the new one in order to be properly used.

Please notice it is the user's responsibility to rebuild non-official packages, including Python-based packages installed from AUR. See AUR#Updating packages and FAQ#What if I run a full system upgrade and there will be an update for a shared library, but not for the applications that depend on it?

## Official
* [https://docs.python.org/ Official Python documentation (Can be installed with the  package for offline access.)
* Official Python tutorial

## Third-Party
* Automate the Boring Stuff with Python - Creative Commons book
* Awesome Python - A curated list of Python resources
* A Byte of Python - Creative Commons book
* Cracking Codes With Python - Free online book
* Crash into Python - Free tutorial
* Python Debugging With Pdb - Guide to using , the Python debugger
* Dive Into Python - Creative Commons book
* Fluent Python - Commercial book
* Introducing Python - Commercial book
* Invent Your Own Computer Games with Python - Free online book
* Learn Python - Free interactive tutorial
* Learn Python the Hard Way - Commercial book
* Pythonspot Python Tutorials - Free online tutorials
* Think Python - Creative Commons book
