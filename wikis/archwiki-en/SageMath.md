# SageMath

SageMath (formerly Sage) is a program for numerical and symbolic mathematical computation that uses Python as its main language. It is meant to provide an alternative for commercial programs such as Maple, Matlab, and Mathematica.

SageMath provides support for the following:
* Calculus: using Maxima and SymPy.
* Linear Algebra: using the GSL, SciPy and NumPy.
* Statistics: using R (through RPy) and SciPy.
* Graphs: using matplotlib.
* An interactive shell using IPython.
* Access to Python modules such as PIL, SQLAlchemy, etc.

## Installation
*  contains the command-line version;
*  for HTML documentation and inline help from the command line.

## Usage
SageMath mainly uses Python as a scripting language with a few modifications to make it better suited for mathematical computations.

## SageMath command-line
SageMath can be started from the command-line:
 $ sage

For information on the SageMath command-line see this page.

The command-line is based on the IPython shell so you can use all its tricks with SageMath. For an extensive tutorial on IPython see the community maintained IPython Cookbook.

Note, however, that it is not very comfortable for some uses such as plotting. When you try to plot something, for example:
 sage: plot(sin,(x,0,10))
SageMath opens the plot in an external application.

## Jupyter Notebook
SageMath also provides a kernel for the Jupyter notebook. To use it, launch the notebook with the command
 $ jupyter notebook
and choose "SageMath" in the drop-down "New..." menu. The SageMath Jupyter notebook supports LaTeX output via the  command and 3D plots if  is installed.

## Cantor
Cantor is an application included in the KDE Edu Project. It acts as a front-end for various mathematical applications such as Maxima, SageMath, Octave, Scilab, etc. See the Cantor page on the Sage wiki for more information on how to use it with SageMath.

Cantor can be installed with the  package or as part of the  or  groups.

## Optional additions
## SageTeX
If you have TeX Live installed on your system, you may be interested in using SageTeX, a package that makes the inclusion of SageMath code in LaTeX files possible. TeX Live is made aware of SageTeX automatically so you can start using it straight away.

As a simple example, here is how you include a Sage 2D plot in your TEX document (assuming you use ):
* include the  package in the preamble of your document with the usual
 \usepackage{sagetex}

* create a  environment in which you insert your code:
 \begin{sagesilent}
 dob(x) = sqrt(x^2 - 1) / (x * arctan(sqrt(x^2 - 1)))
 dpr(x) = sqrt(x^2 - 1) / (x * log( x + sqrt(x^2 - 1)))
 p1 = plot(dob,(x, 1, 10), color='blue')
 p2 = plot(dpr,(x, 1, 10), color='red')
 ptot = p1 + p2
 ptot.axes_labels(\end{sagesilent}

* create the plot, e.g. inside a  environment:
 \begin{figure}
 \begin{center}
 \sageplot[width=\linewidth{ptot}
 \end{center}
 \end{figure}

* compile your document with the following procedure:
 $ pdflatex
 $ sage
 $ pdflatex

* you can have a look at your output document.

The full documentation of SageTeX is available on CTAN.

## Troubleshooting
## TeX Live does not recognize SageTex
If your TeX Live installation does not find the SageTex package, you can try the following procedure (as root or use a local folder):
* Copy the files to the texmf directory:
 # cp /opt/sage/local/share/texmf/tex/* /usr/share/texmf/tex/
* Refresh TeX Live:
