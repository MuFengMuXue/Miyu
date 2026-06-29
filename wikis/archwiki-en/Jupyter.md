# Jupyter

Jupyter is a project which produces browser-based interactive environments for programming, mathematics, and data science. It supports a number of languages via plugins ("kernels"), such as Python, Ruby, Haskell, R, Scala, Julia and Kotlin.

JupyterLab is "Jupyter’s Next-Generation Notebook Interface", while Jupyter Notebook is the original. See the Jupyter website for a comparison.

## Installation
* For JupyterLab, install the  package.
* For Jupyter Notebook, install the  package.

To install third-party Jupyter Notebook extensions for the current user, use the  option while executing . To do the same for installation of JupyterLab extensions, set the following environment variable:

 JUPYTERLAB_DIR=$HOME/.local/share/jupyter/lab

and verify it by running . Then onwards follow usual installation instructions.

## Running
To start JupyterLab run:

 $ jupyter lab

To start Jupyter Notebook run:

 $ jupyter notebook

Navigate to the URL given on the standard output if a web browser does not automatically open.

To start JupyterLab without launching browser and listening on port  run

 $ jupyter lab --no-browser --port 9999

To change the default behavior, edit the configuration file:

See  for an overview of all options or run  to generate a default configuration file.

## Kernels
## C++
Install the  package.

## Haskell
Install the  package. Then run .

## Julia
Install the  package and run  to get a REPL prompt. Then run:

 using Pkg
 Pkg.add("IJulia")

See the Julia manual for more details on package management.

## Python
Python 3 kernel is used by default via .

## Perl
Install the  package and run . Then press . Now if you run jupyter you will see perl there.

## R
Install the  package. Then in an R console run:

 require(IRkernel)
 IRkernel::installspec()

Alternatively you could follow the installation instructions in IR Kernel.

## Rust
Install the  package.

## SageMath
Install the  package.

## Octave
Install the  package.

## Maxima
Install the  package.

## Cadabra
Install the  package.

## Kotlin
Install the  package.

## Interactive widgets in JupyterLab
In order to enable interactive widgets in Jupyter Lab install  and  according to this github issue.
Afterwards, in your notebook use:
 %matplotlib widget
Don't forget to restart you JupyterLab instance after installing extensions.

It also might be helpful to RMB->Clear Outputs of All Cells after your extension manipulations
