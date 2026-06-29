# OpenFOAM

According to Wikipedia:
:OpenFOAM (for "Open source Field Operation And Manipulation") is a C++ toolbox for the development of customized numerical solvers, and pre-/post-processing utilities for the solution of continuum mechanics problems, including computational fluid dynamics (CFD).

## Installation
## Basic
If you do not plan on doing development tasks with OpenFOAM, there is an updated version of the program available as . For most users, this will be everything needed to get an installation up and running.

OpenFOAM is installed in the  directory and provides a script in  that allows to activate the OpenFOAM environment with the  command (a shell alias).

## Development
For installation of OpenFOAM in a development environment, the process is fairly straight forward on Arch Linux. The basic steps are as follows:

# Obtain source files from OpenFOAM
# Prepare build directory
# Create Preference File and Set Environment Variables for your installation
# Compile OpenFOAM sources
# Test OpenFOAM installation

## Prerequisites
*
*
*
*
*
*

## Obtain source files
Since OpenFoam is a picky about its location, create a directory following its naming convention and extract the source code there:

 $ mkdir $HOME/OpenFOAM
 $ wget -P $HOME/OpenFOAM https://dl.openfoam.com/source/v2206/OpenFOAM-v2206.tgz
 $ tar -xvfz $HOME/OpenFOAM/OpenFOAM-v2206.tgz -C $HOME/OpenFOAM

## Environment variables
Paste the following code into your .bashrc file. Whenever you want to run OpenFOAM you just have to run  to initialize the environment. This has to be done prior to compilation.

 $ export FOAM_INST_DIR="$HOME/OpenFOAM"
 $ alias of2206='source $FOAM_INST_DIR/OpenFOAM-v2206/etc/bashrc'

## Compilation
Run  to initialize the environment. Use  to check if all requirements are installed, then  to change into the project directory. Then you can use the following command to compile:

 $ ./Allwmake -j -s -q -l

This compiles with all cores (-j), reduced output (-s, -silent), with queuing (-q, -queue) and logs (-l, -log) that can be inspected later.

## Testing
To test for successful installation, run any test case, for example:

 $ foamInstallationTest -full incompressible/simpleFoam/pitzDaily

## Troubleshooting
## zsh
Some things do not work correctly if you are not using bash. In the case of using zsh, you will need the  package, and add the following to your zshrc for the OpenFOAM scripts to work:

{{hc|zshrc|2=autoload bashcompinit
bashcompinit
alias ofoam="source ${FOAM_INST_DIR}/OpenFOAM-10/etc/bashrc"}}

Then add the following environment variables, preferably into a zshenv file:

## Paraview not installed
This happens because the dependencies are installed as separate packages, and not in the third-party apps directory of OpenFOAM. Either;

* Add  to your .
* For each project, {{ic|touch $(echo "${PWD##*/}").foam}} and then open the touched file from paraview.
