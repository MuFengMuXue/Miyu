# Bootchart

Bootchart is a handy tool used for profiling the Linux boot sequence, generally used for making your computer boot faster. It consists of the bootchartd daemon, which records and renders a chart of profiling data.

## Installation
Install the  package.

## Usage
To make use of bootchart, you have to either set it as the init process in your boot loader. Note that if you start bootchartd manually, you have to stop it manually too. In general, be extra careful with this step.

## Boot loader setup
This generally involves making a copy of the boot option you want to profile and adding  to it. See kernel parameters for instructions. When started from the boot loader, bootchart will stop when you get to the login prompt.

## Generating a chart
Generating a bootchart involves running  in a folder to which you have write access. This will generate a  image with your chart.
You will have to have a Java runtime installed and properly set up before you can do this.

## Troubleshooting
Bootchart-render cannot generate a  image and shows the error message:

 /var/log/bootchart.tgz not found

It mostly means that bootchartd was unable to detect when the booting process was finished. This can happen when you are using different login manager than GDM such as SLiM or entrance. You have to open  script and append those applications to  variable, for example:

 # The processes we have to wait for
 local exit_proc="gdmgreeter gdm-binary slim"

If you are using no login manager, edit the  variable in this way:

 # The processes we have to wait for
 local exit_proc="login"

## Example bootcharts
## Boot in 5 seconds
LWN Article on fast booting netbooks

This article is really awesome and along with a bunch of bootcharts provides some tips on how to boot faster. Some of those improvements are beyond reach of the ordinary user though (patching X.org, kernel, etc.).

## Bootchart2
## Running Bootchart2
## Boot loader setup
This generally involves making a copy of the boot option you want to profile and adding  to it. See kernel parameters for instructions. When started from the boot loader, bootchart2 will stop after either a default 120 seconds, or when you get to the login prompt (as opposite). Note that Bootchart2-git can also be run as a systemd service, as described in Improve boot performance#Using bootchart2

## bootchart2.service
The  package from AUR comes with an undocumented systemd service. After you have installed bootchart2, enable .

You can visualize the results by opening , or if you would like more features by launching:

 $ pybootchartgui -i

Read the bootchart2 documentation for further details on using this version of Bootchart.

## Configure Bootchart2
## Stop Bootchartd2 after login
Bootchart2 configuration file can be adjusted:

It can also be left empty for logging to be stopped manually rather than at a predetermined program start.

## Generating a chart
Is as straightforward with Bootchart2 as it is with Bootchart Legacy: After bootup, run

 $ pybootchartgui -i

to get an interactive chart rendering tool. See Gentoo:Bootchart2 for more information.
