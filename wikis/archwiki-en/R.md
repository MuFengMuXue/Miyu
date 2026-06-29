# R

From "What is R?" in the R FAQ:

:R is a system for statistical computation and graphics. It consists of a language plus a run-time environment with graphics, a debugger, access to certain system functions, and the ability to run programs stored in script files.

## Installation
Install the  package. The installation of external packages within the R environment may require .

## Usage
To start an R session, open your terminal and type this command:

 $ R

Run  to read the documentation about system file configuration,  for the on-line help,  for the HTML browser interface to help,  for some demos and  to close the session and quit.

When closing the session, you will be prompted as follows:

 Save workspace image? The workspace is your current working environment and include any user-defined objects, functions. The saved image is stored in  format and will be automatically reloaded the next time  is started. You can manually save the workspace at any time in the session with the  command, save as many images as you want (eg: image1.RData, image2.RData). You can load image with the  command at any time of your session.

## Configuration
Whenever R starts, its configuration is controlled by several files. Please refer to [https://stat.ethz.ch/R-manual/R-devel/library/base/html/Startup.html Initialization at Start of an R Session to get a detailed understanding of startup process.

## Environment
R first loads site and user environment variable files. The name of the site file is controlled by the environment variable  if it exists, and defaults to . The name of the user file is specified by . If that is unset, it defaults to  in the current working directory if it exists, or  otherwise.

The most important variables can be found on Environment Variables R Documentation.

You may disable loading environment files with

Lines in the  file should be either comment lines starting with  or lines of the form . Here is a very basic :

{{hc|1=.Renviron|2=
R_HOME_USER = /path/to/your/r/directory
R_PROFILE_USER = ${HOME}/.config/r/.Rprofile
R_LIBS_USER = /path/to/your/r/library
R_HISTFILE = /path/to/your/filename.Rhistory
MYSQL_HOME = /var/lib/mysql
}}

Alternatively, environmental variables may be set from within your R session via the  function. For instance, to set the time zone () environmental variable to :

## Profile
R then loads a  file, which contains R code that is executed. These files are read in the following order of preference (only one file is loaded):

# A file specified by the environment variable .
# A  file in the current working directory.
# .

A  file can contain arbitrary R code, though best practice suggests that one should not load packages at startup, or execute any code that would hinder package upgrades and reproducibility.

:To make this change permanent, add the above command to your Rprofile.
}}

Within your R session, run this command to check that your user library exists and is set correctly:

Alternatively, you may install from the command line like so:

## With Guix and
While compiled binaries of some R packages are available through Arch repositories and the AUR, there are many which are not packaged. This can mean long compilation times (which need to be repeated when R is updated).

One way to get access to prebuilt R packages is by using the Guix package manager which provides a way to get fully reproducible builds of packages through "substitutes". See the Guix page and manual for how to set up Guix.

After you have a working installation of Guix, you can install R packages that will be used.

To emulate the  workflow with Guix one can use the  function from the guix.install package.

## Upgrading R packages
## Within an R session
 > update.packages(ask=FALSE)

Or when you also need to rebuild packages which were built for an older version:

 > update.packages(ask=FALSE, checkBuilt=TRUE)

Or when you also need to select a specific mirror (https://cran.r-project.org/mirrors.html) to download the packages from (changing the URL as needed):

 > update.packages(ask=FALSE, checkBuilt=TRUE, repos="https://cran.ma.imperial.ac.uk/")

## Within a shell
You can use , which comes with r to update packages from a shell:

## Makevars
The Makevars file can be used to set the default make options when installing packages. An example optimized Makevars file is as follow:

## Alternative shells
As an alternative to the default R program, the following shell is also available:

*

## Adding a graphical frontend to R
R does not include a point-and-click graphical user interface for statistics or data manipulation. However, third-party user interfaces for R are available, such as R Commander and Rattle.

## R Commander frontend
R Commander(CRAN repo) is a popular user interface to R. There is no Arch Linux package available to install R Commander, but it is an R package so it can be installed easily from within R. R Commander requires  and  to be installed.

To install R Commander, run  from the command line. Then type:

 > install.packages("Rcmdr", dependencies=TRUE)

This can take some time.

You can then start R Commander from within R using the library command:

 > library("Rcmdr")

## Rattle frontend
Rattle is a popular user interface to R with focus on data mining. There is no Arch Linux package available but it can be installed easily from within R.

To install Rattle, run  from the command line. Then type:

 > install.packages("rattle", dependencies=TRUE)

This can take some time.

You can then start Rattle from within R using the library command:

 > library("rattle")
 > rattle()

## JASP
jasp-desktop provides a menu-driven interface for common statistical analysis using R as the backend. A Flatpak package is also available.

## jamovi
jamovi () provides a menu-driven interface for common statistical analysis using R as the backend. A Flatpak package is also available.

## Editors, IDEs, and notebooks with R support
## RKWard IDE
RKWard is an IDE developed by KDE, which allows for data import and browsing as well as running common statistical tests and plots. You can install  from the official Arch repositories.

## RStudio IDE
RStudio is an open-source R IDE. It includes many modern conveniences such as parentheses matching, tab-completion, tool-tip help popups, and a spreadsheet-like data viewer.

Install .

The R library path is often configured with the  environment variable. RStudio ignores this, so the user must set  in , as documented above.

RStudio uses a four-pane layout by default. However, if only the taskbar and toolbar located at the vertical top of an otherwise blank screen are visible, create with elevated privileges the following file and populate it with contents as shown below:

Restart RStudio and observe the expected split-screen layout with four panes. See RStudio does not show any pane on Stack Overflow and https://github.com/rstudio/rstudio/issues/5961 for more information.

If, at startup, RStudio throws at you the following error:

you need to install the  package.

## RStudio server
RStudio Server enables you to provide a browser based interface to a version of R running on a remote Linux server.

Install . The two main configuration files are  and . They are not created during the install, so you will need to create and edit them.

To start the server, please enable and start the   unit file provided with the package.

## Emacs Speaks Statistics
Emacs users can interact with R via the  package.

## Nvim-R and R.nvim
The  package helps  users to code in R, by including editing and rendering of R markdown (.Rmd) files, execution of R code in a separate pane, inspection of variables, and integrated help panes.

 users should use R.nvim instead.

## Cantor
 is a notebook application developed by KDE that includes support for R.

## Visual Studio Code
The Visual Studio Code () editor has plugin support for R.

## Positron
Positron is a Data Science IDE built by Posit PBC (formerly known as RStudio, the company behind the respectively named IDE) based on Visual Studio Code.
It is configured out of the box with options and plugins suited for a Data Science workflow, and maintains compatibility with VS Code plugins.

Install .

## Jupyter notebook
Jupyter is a browser based notebook with support for many programming languages. R support can be added by installing the IRkernel.

## Architect
Architect is an integrated development environment (IDE) that focuses specifically on the needs of the data scientist. Install .

## Radiant
Radiant is a platform-independent browser-based interface for business analytics in R, based on the Shiny package.

Install .

## Tips and tricks
## Optimized packages
The numerical libraries that come with the r package ( and consequently ) do not have multithreading capabilities. Replacing the reference  package with an optimized BLAS can produce dramatic speed increases for many common computations in R. See these threads for an overview of the potential speed increases:

* https://github.com/tmolteno/necpp/issues/18
* http://blog.nguyenvq.com/blog/2014/11/10/optimized-r-and-python-standard-blas-vs-atlas-vs-openblas-vs-mkl/
* https://freddie.witherden.org/pages/blas-gemm-bench/
* https://nghiaho.com/?p=1726

To find out which numerical libraries R is using, call  or  within an R session.

## OpenBLAS
 can replace the reference .

If you are using the regular r package from the extra repository, no further configuration is needed; R is configured to use the system BLAS and will use OpenBLAS once it is installed.

If that does not work, use the ropenblas package to compile, install and use the latest version of openblas:

## Intel MKL
If your processors are Intel, you can use the Intel Math Kernel Library. The MKL, beyond the capabilities of multithreading, also has specific optimizations for Intel processors.

Please first install the , then the  package.

## Intel Advisor
Intel Advisor delivers top application performance with C, C++ and Fortran compilers, libraries and analysis tools.

Install the  package.

## AMD AOCL
AMD Optimizing CPU Libraries are a set of numerical libraries optimized for AMD processors, and is essentially AMD's counterpart to Intel's Math Kernel Library.

Install the  or  package (requires downloading AOCL tarballs from upstream), and enable the libraries systemwide using either , or manually.

## Set CRAN mirror across R sessions
Instead of having R ask which CRAN mirror to use every time you install or update a package, you can set the mirror in the  file. https://cloud.r-project.org/ should be a good default for everywhere as it redirects to your closest CRAN mirror:

{{hc|head=~/.Rprofile|
output=
## Set CRAN Mirror:
local({
  r  q()|Save workspace image? On face value, this may seem convenient, but using workspace images will render your code less portable. The "Save workspace image?" prompt may be disabled by creating a hidden environment (), adding a new version of the  function to it in which the default value for the  argument has been altered to , then attaching the hidden environment. This will mask the  function of R's base package, effectively switching off the prompt. To make this change permanent, add the following code to your  file:

{{hc|~/.Rprofile|2=
## Create hidden environment
.env <- new.env()

## Define new q() function
.env$q <- function(save = "no", ...) {

  quit(save = save, ...)

}

## Attach hidden environment
attach(.env, warn.conflicts = FALSE)
}}

The above will make  exit R without displaying a prompt, but it will not have an effect on quitting with .

If you never want to see the save workspace prompt, it is more convenient to start R with . Add  to e.g.  to make the change persistent.

## Running R from a shell
Run the following command to execute R code from a command-line shell:

 $ R CMD BATCH script.R

This command will return a .Rout file with results from . The .Rout file will always contain a  call at the end as a benchmark.  can be added to the end of the R code to keep a record of packages and versions.

## Installing V8 package
To install the [https://cran.r-project.org/web/packages/V8/index.html V8 R package you need the V8 engine installed on your system.

To do so, you can install the  package (warning: compiled from source, long compilation time).

As compilation of the V8 package is a substantial and resource-intensive undertaking, a means to avoid it was added by the package maintainer(s). Explanation of this is provided in the package GitHub page. To summarise, to force the use of a pre-compiled libv8:

## Troubleshooting
## Unable to load stringi.so
The following error may be encountered when running R code that depends on the stringi CRAN package:

 unable to load shared object R_LIBS_USER/stringi/libs/stringi.so':
 libicui18n.so.MAJOR: cannot open shared object file: No such file or directory

This often occurs following a soname bump to the library (provided by ).  will need to be rebuilt in R by installing the package again.
