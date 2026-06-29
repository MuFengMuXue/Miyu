# Conda

From conda document:
:Package, dependency and environment management for any language—Python, R, Ruby, Lua, Scala, Java, JavaScript, C/ C++, Fortran, and more.

:Conda is an open source package management system and environment management system that runs on Windows, macOS, and Linux. Conda quickly installs, runs and updates packages and their dependencies. Conda easily creates, saves, loads and switches between environments on your local computer. It was created for Python programs, but it can package and distribute software for any language.

## Installation
There are multiple methods to install conda.

## AUR
Install the  package, or the  package for miniconda.

## miniforge
Download miniforge from the GitHub repository.

Then run the installer with

 $ bash /path/to/Miniforge3-Linux-x86_64.sh

Miniforge uses conda-forge as the default channel.

## Usage
It is recommended to install new packages in a new environment instead of the  environment.
To avoid conda automatically activating the  environment, edit:

## Set default packages
Add  section in . For example:

## Create an environment
To create a new environment  with default packages specified in previous section, run:

 $ conda create --name myenv

To crate a new environment without default packages, run:

 $ conda create --no-default-packages --name myenv

To create a environment with specified python version and packages, run:

 $ conda create --name myenv python=3.9 numpy=1.23.5 astropy

To activate the environment:

 $ conda activate myenv

## List environments
To list all environment:

 $ conda env list

## Clone an environment
 $ conda create --name myenvclone --clone myenv

## Remove an environment
 $ conda remove --name myenv --all

## Export and import an environment
To export all packages in  environment:

 $ conda activate myenv
 $ conda env export > myenv.yml

If you only want to include packages you explicitly installed, add  flag when exporting.

 $ conda env export --from-history > myenv.yml

To create a new environment from a , run:

 $ conda env create -f myenv.yml

## Troubleshooting
## qt.qpa.plugin: Could not find the Qt platform plugin "wayland" in ""
Install  to conda environment.
 $ conda install qt6-wayland
