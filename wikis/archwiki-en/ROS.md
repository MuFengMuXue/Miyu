# ROS

ROS is an open-source, meta-operating system for your robot. It provides the services you would expect from an operating system, including hardware abstraction, low-level device control, implementation of commonly-used functionality, message-passing between processes, and package management.

## ROS 1
## Installation
You can install . It is also available through an unofficial user repository: Unofficial user repositories#arch4edu.

## catkin_make in Melodic
As specified by the ROS wiki, the first catkin_make command in a clean workspace should be:

 $ catkin_make -DPYTHON_EXECUTABLE=/usr/bin/python3 -DBOOST_ROOT=/opt/boost1.69 -DBoost_NO_SYSTEM_PATHS=TRUE

Subsequent builds should be done with just
 $ catkin_make

## Using Catkin/ROS with an IDE
## CLion
To make  support ROS packages, you can change the  parameter of its desktop file as follows.

However,  must be exchanged with your Catkin workspace. You can now open a Catkin project without  complaining about missing packages, hopefully.
If desired or needed you can use Python 3 by adding  to the CMake options which can be found in the settings.

## catkin build in Melodic
For configuring the systems using the  environment, one have to configure the catkin workspace as usual and run:

 $ catkin config -DPYTHON_EXECUTABLE=/usr/bin/python3 -DBOOST_ROOT=/opt/boost1.69 -DBoost_NO_SYSTEM_PATHS=TRUE

Afterwards, use  as normal. Please remember to reconfigure your catkin whenever you delete the configuration files (i.e. the  directory)

## Rebuild when shared libraries are updated
When you update a library that ROS depends on (e.g. Boost), all packages that link to it must be rebuilt. Most AUR helpers will not detect this situation. The following script will generate a list of all packages that are linked to missing so files:

https://seangreenslade.com/h/snippets/ros-find-outofdate.py

(Note that the script requires  to be installed.)

## ROS 2
## Installation
## Building using AUR
 package aims to provide an easy way to install ROS 2 on Arch Linux. After installing the package, you need to configure your environment (i.e. source) in order to use ROS 2 — See #Usage Examples.

## Distrobox
Distrobox allows to use any Linux distribution inside your terminal including Ubuntu, which in turn allows to run ROS2 natively. Distrobox is available in the official repository as , and relies on Docker or Podman containers.

Once Ubuntu is up and running, install ROS by reading the [https://docs.ros.org/en/humble/Releases.html official installation guide.

## Running on Wayland
Although ROS2 packages run fine on Wayland, graphical applications such as gazebo or rviz2 do not. To make them work, set the environment variable  to . You can later test the result with:

 $ rviz2

## Usage examples
First source the workspace, or change the directory to where you installed as before.

If you are using zsh, change source /opt/ros2/foxy/setup.bash to source /opt/ros2/foxy/setup.zsh

 $ source /opt/ros2/foxy/setup.bash

A tip to source workspace is adding a function like this your shell startup file:

 ros2_on(){
      export ROS_DOMAIN_ID=42
      export ROS_VERSION=2
      export ROS_PYTHON_VERSION=3
      export ROS_DISTRO=foxy
      source /opt/ros2/foxy/setup.bash
 }

Remember to make any applicable changes, namely changing the ROS_DISTRO variable to the distrobution you have installed.

You can change ROS_DOMAIN_ID to your favourite number, or the number you are actually using.

Functionality comparable to , , , , ,  and  is available via :

 $ ros2 -h
 usage: ros2 -h Call `ros2  -h` for more detailed usage. ...

 ros2 is an extensible command-line tool for ROS 2.

 optional arguments:
   -h, --help            show this help message and exit

 Commands:
   daemon    Various daemon related sub-commands
   msg       Various msg related sub-commands
   node      Various node related sub-commands
   pkg       Various package related sub-commands
   run       Run a package specific executable
   security  Various security related sub-commands
   service   Various service related sub-commands
   srv       Various srv related sub-commands
   topic     Various topic related sub-commands

   Call `ros2  -h` for more detailed usage.

A typical "Hello World" example starts with running a publisher node:

 $ ros2 topic pub /chatter 'std_msgs/String' "data: 'Hello World'"

Then, in another terminal, you can run a subscriber (Do not forget to source the workspace in every new terminal):

 $ ros2 topic echo /chatter

List existing nodes:

 $ ros2 node list
 publisher_std_msgs_String

List topics:

 $ ros2 topic list
 /chatter

ROS 2's version of rviz is

 $ rviz2
