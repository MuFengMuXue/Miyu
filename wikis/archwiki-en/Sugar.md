# Sugar

Initially developed for the OLPC initiative, Sugar is a desktop environment geared towards children and education.

Sugar has a special Taxonomy to name the parts of its system. The graphical interface itself constitute the Glucose group. This is the core system can reasonably expect to be present when installing Sugar. But to really use the environment, you need activities (some sort of applications). Base activities are part of Fructose. Then, Sucrose is constituted by both Glucose and Fructose and represents what should be distributed as a basic sugar desktop environment. Extra activities are part of Honey. Note that Ribose (the underlaying operating system) is here replaced by Arch.

## Installation
* For the core system (Glucose), install . It provides the graphical interface and a desktop session, but not very useful on its own.
* The  group contains the base activities (Fructose) including a web browser, a text editor, a media player and a terminal emulator.
* The  package provides a helper script that makes it possible to launch Sugar within another desktop environment, or from the command line directly.

## From Activity Library
The Sugar Activity Library provides many Activity Bundles packaged as zip files with the .xo extension. These bundles can be downloaded and installed to the user's directory from Sugar, but the installation does not ensure that the dependencies are satisfied. Therefore it is not the recommended way to install activities, because they likely fail to start due missing dependencies. A commonly used dependency is  for web activities.

In order to check why the activity fails to start, look at the log file located at .

## Starting Sugar
Sugar can be started either graphically, using a display manager, or manually from the console.

## Graphically
Select the session Sugar from the display manager's session menu.

## Manually
If  is installed, Sugar can be launched with the  command.

Alternative method is to add  to the  file. After that, Sugar can be launched with the  command (see xinitrc for additional details). After setting up the  file, it can also be arranged to start X at login.
