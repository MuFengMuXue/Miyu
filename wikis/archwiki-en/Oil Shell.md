# Oil Shell

Oil Shell (OSH) is a Bash-compatible UNIX command-line shell. OSH can be run on most UNIX-like operating systems, including GNU/Linux. It is written in Python (v2.7), but ships with a native executable. The dialect of Bash recognized by OSH is called the OSH language.

## Installation
Install the  package.

## Smoke Test
Make sure that OSH has been installed correctly by running the following in a terminal:

 $ osh

This will start an OSH session and display a shell prompt:

 osh$

Identify an installed binary and attempt to invoke it in the OSH session to confirm that the output is correct.

For example:

 osh$ ls
 ...

## Making OSH your default shell
See Command-line shell#Changing your default shell.

## Removal
See Command-line shell#Uninstalling shell.

## Troubleshooting
Reproducible bugs/errors may be reported on Github. When filing a report, please include the output of OSH when it is running in verbose mode. To enable verbose mode, execute the following:

 $> export OVM_VERBOSE=1
