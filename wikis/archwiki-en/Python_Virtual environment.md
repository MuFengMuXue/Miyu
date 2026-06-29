# Python/Virtual environment

Virtual environment tools are used to create an isolated workspace for a Python application. They have various advantages such as the ability to install modules locally, export a working environment, and execute a Python program in that environment.

## Overview
A virtual environment is a directory into which some binaries and shell scripts are installed. The binaries include python for executing scripts and pip for installing other modules within the environment. There are also shell scripts (one for bash, csh, and fish) to activate the environment. Essentially, a virtual environment mimics a full system install of Python and all of the desired modules without interfering with any system on which the application might run.

In 2017, Pipenv was published which manages all the above tools - managing virtual environments of python interpreters, package dependencies, their activation and reproducible locking of versions in Pipfiles.

## Installation
Python 3.3+ comes with a module called venv. For applications that require an older version of Python, virtualenv must be used.

## Packages
Install one of these packages to use a Python virtual environment:

* Python 3.3+:
* Python 3:

For Pipenv:

* Python 3:

## Usage
All three tools use a similar workflow.

## Creation
Use venv or virtualenv to create the virtual environment within your project directory. Be sure to exclude the venv directory from version control--a copy of  will be enough to rebuild it.

## venv
This tool is provided by  (3.3+):
 $ python -m venv envname

## virtualenv
Use virtualenv for Python 3, available in .
 $ virtualenv envname

## Activation
Use one of the provided shell scripts to activate and deactivate the environment. This example assumes bash is used.

 $ source envname/bin/activate
 (envname) $

Once inside the virtual environment, modules can be installed with pip and scripts can be run as normal.

To exit the virtual environment, run the function provided by :

 (envname) $ deactivate

## Python versions
By default, virtual environments are created using system Python. The bin/python binary is just a symlink to system python:

 $ ls -l envname/bin/python
 lrwxrwxrwx 1 foo foo 15 Jan 29 18:48 envname/bin/python -> /usr/bin/python

If you want to use a different Python version inside the virtual environment, you can use the / option of virtualenv:

 $ virtualenv -p 3.8 envname
 $ ls -l envname/bin/python
 lrwxrwxrwx 1 foo foo 18 Jan 29 18:48 envname/bin/python -> /usr/bin/python3.8

 can also be used:

 $ virtualenv -p pypy3 envname

## virtualenvwrapper
virtualenvwrapper allows more natural command line interaction with your virtual environments by exposing several useful commands to create, activate and remove virtual environments. This package is a wrapper for .

## Installation
Install the  package and add the following lines to your :

The line  can cause some slowdown when starting a new shell. To fix this try using , which will load virtualenvwrapper the first time virtualenvwrapper functions are called.

Re-open your console to apply changes. The  directory will be created automatically.

## Basic usage
See https://virtualenvwrapper.readthedocs.io/en/latest/ for usage (and extension capability).

Create the virtual environment (all command line options except , , , and  are passed directly to virtualenv, so you can use  to select Python version):
 $ mkvirtualenv envname

Activate the virtual environment:
 $ workon envname

Install some package inside the virtual environment (say, Django):
 (envname) $ pip install django

After you have done your things, leave the virtual environment:
 (envname) $ deactivate

## Pipenv
pipenv allows better managed CLI interactions by providing a single program that does all the functions of the above tools.

## Installation
Install the  package.

## Basic usage
All commands can be executed in the project folder, and pipenv will recognize the specific situation - whether a virtualenv exists in the directory, locating it, and running on the specific virtual interpreter when pipenv is executed.

More information at [https://realpython.com/pipenv-guide/, == See also ==

* [https://docs.python.org/3/library/venv.html Python venv
* virtualenv PyPI page
* virtualenvwrapper documentation
