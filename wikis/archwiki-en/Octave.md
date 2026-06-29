# Octave

From the official website:

:GNU Octave is a high-level interpreted language, primarily intended for numerical computations. It provides capabilities for the numerical solution of linear and nonlinear problems, and for performing other numerical experiments. It also provides extensive graphics capabilities for data visualization and manipulation. Octave is normally used through its interactive command line interface, but it can also be used to write non-interactive programs. The Octave language is quite similar to Matlab so that most programs are easily portable.

## Installation
Install the  package.

Run the GUI with  or the CLI with .

## Alternative graphical interfaces
The default octave GUI is included in the  package. Alternatively, you can use one of the following unofficial GUIs:
*
*

## Performance
Octave uses the  package for linear algebra computation by default.  However, this implementation does not take advantage of modern CPU instructions.  To accelerate performance, the  package can be installed as a drop-in replacement for blas.  Other BLAS implementations can also be used depending on available hardware, such as  for Intel CPUs or  for NVIDIA GPUs.

To illustrate this point, the following code can be used to get an estimate for how many GFLOPS are being executed on an NxN matrix multiply:

 N = 4096;
 A = single(rand(N, N));
 B = single(rand(N, N));
 start = clock();
 C = A * B;
 elapsedTime = etime(clock(), start);
 gFlops = 2 * N * N * N / (elapsedTime * 1e9)

Running the following code on an Intel Core i7-9750H:

After installing openblas and running the program on a single thread:

After letting openblas use all 12 threads available on the 9750H:

## Octave-Forge
Octave provides a set of packages, similar to Matlab's Toolboxes, through Octave-Forge. The complete list of packages is here.

Packages can be installed #Using Octave's installer or #Using the AUR.

## Using Octave's installer
Packages can be managed using Octave's installer. They are installed to ~/octave, or in a system directory with the -global option. To install a package:

 octave:1> pkg install -forge packagename

To uninstall a package:

 octave:3> pkg uninstall packagename

Some packages get loaded automatically by Octave, for those which do not:

 octave:4> pkg load packagename

Loading all packages is discouraged, as it may affect performance and create name conflicts. If you however wish to load all packages, you can issue:

 octave:5> cellfun (@(x) pkg ("load", x.name), pkg ("list"));

To see which packages have been loaded use , the packages with an asterisk are the ones that are already loaded.

A way to make sure that all packages gets loaded at Octave startup:

## Using the AUR
Some packages may be found in the AUR (search packages). New Octave-forge packages for Arch can be created semi-automatically using the Octave-forge helper scripts for Arch Linux.

## Plotting
Qt is the default plotting backend:

 >> available_graphics_toolkits
 ans =
 {
   = fltk
   [1,2 = qt
 }
 >> graphics_toolkit
 ans = qt

Alternatively you can use either FLTK or Gnuplot backend (by installing ) and running the following command:

 >> graphics_toolkit("gnuplot");

To make this change permanent add it to your  file.

## Reading Microsoft Excel Spreadsheets
You can open ,  and  files with the  or  function, which requires the  package:

 octave:1> odsread('myfile.ods');
 octave:1> xlsread('myfile.xls');
 octave:1> xlsread('myfile.xlsx');

## Converting to CSV format
Alternatively, first convert the files to  using LibreOffice Calc (limited to 1024 columns) or Calligra Sheets (, limited to 32768 columns).

After the conversion is complete you can use the build-in Octave function  for  files:

 octave:1> csvread('myfile.csv');

## Troubleshooting
## Zsh Undecodable Token
If you get error
 undecodable token: b(hex)[23m
when printing, install   and relogin.

## vi Mode Undecodable Token
Users with their  configured for vi-mode, for example, as

may have the Octave GUI prompt corrupted as .
To remedy this, disable the  setting for Octave, by changing the above  to be
