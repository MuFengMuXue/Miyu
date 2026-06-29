# Folding@home

Help scientists studying Alzheimer's, Huntington's, Parkinson's, and SARS-CoV-2 by simply running a piece of software on your computer. Add your computer to a network of millions of others around the world to form the world's largest distributed supercomputer.

## Installation
Install the  package. In order to use your GPU for folding (highly recommended), you will need  and the appropriate OpenCL package for your GPU. NVIDIA users can also use CUDA.

## Configuration
start/enable  to start the backend.

The Folding@home software is controlled via a web browser using Web Control, which is accessed at https://v8-4.foldingathome.org/Your local machine should appear under the Machines subpage. By pressing the settings cog icon you can change Account Settings, Scheduling, and Resource Usage.

To start folding, on the Machines page press Fold All.

## The terminal way
The current version of Folding@home does not support editing config through the terminal. You should use the Web Control accessible at https://v8-4.foldingathome.org/.

## Account Settings
* : Choose the name for your Folding@home account. Since it does not have to be unique, others could have the same Username as you. If you wish to remain anonymous you can use the username "Anonymous".
* : Choose which team you would like to join. (the Arch Linux team number is 45032)
* : To uniquely identify you. Though not needed, it provides some measure of security. You can obtain a passkey from https://apps.foldingathome.org/passkey/create.[https://foldingathome.org/faq/points/passkey/
* : Choose which cause you wish to donate to. By default uses "any".

## Scheduling
* : Will only donate when the system is not being used.
* : Will donate even when the system is running on battery power.
* : Will prevent the system from sleeping/hibernating while the machine is not on battery power.

## Resource Usage
* : Choose the number of threads will be donated.
* : Choose which GPUs should be used for folding.

## Run f@h with limited privileges
The updated version of  package (>7.6.9) already runs as a limited user. It also installs a systemd user script that you can use, which users without root access can enable (you will still need video group access to be able to use the GPU).

## Monitoring work-unit progress
There are several ways of monitoring the progress of your FAH clients, both on the command line and by GUI.

Folding@home writes its log file to the data directory. By checking out a few last lines you can check its progress, e.g. .

The latest Folding@home already provides local and remote monitoring with their Web Control panel. fahcontrol is no longer needed.

For checking NVIDIA GPU utilisation, core temperature and power usage,  can be used. For AMD GPUs, use .

## Troubleshooting
## “Disabled” on AMDGPU
Navi 10 based GPUs and later suffer from ROCm conflicting with Folding@home's shipped libstdc++ library.
In order to fix this, try to apply this temporary workaround* start Folding@home, and wait for the GPU to fail;
:the GPU slot may need to be re-enabled for this.
* replace Folding@home's current core's  by your system's own library, e.g.,
: Folding@home's core can be found at
:
: To access the exact path on your system, run:
:
:

The fix will stop working when a new Folding@home core version is released:
it will need to be reapplied.

If it's not working yet, try editing  file to attempt to autoconfigure GPUs:

It if it's not working, you may wish to try using either  or .
Mesa OpenCL implementations are unlikely to work.

If you still receive errors that the GPU is disabled, check if  is installed and remove them so they do not conflict.

If it still does not work, make sure that there is only one vendor listed in ;
Folding@home may not work correctly if there are multiple vendors.
