[] This article has been flagged for not conforming to the [wiki guidelines](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Guidelines "Gentoo Wiki:Guidelines"). Please [help Gentoo out](https://wiki.gentoo.org/wiki/Help_improve_Gentoo_by_getting_involved_with_documentation!#Make_articles_conform_to_the_guidelines "Help improve Gentoo by getting involved with documentation!") by starting fixing things.

**Resources**

[[]][Home](http://www.ros.org/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Robot_Operating_System "wikipedia:Robot Operating System")

[[]][Ebuild repository](https://github.com/ros/ros-overlay)

## Contents

-   [[1] [Preface]](#Preface)
-   [[2] [Following the official guide and using the ebuild repository]](#Following_the_official_guide_and_using_the_ebuild_repository)
    -   [[2.1] [Prerequisites]](#Prerequisites)
    -   [[2.2] [Installation]](#Installation)
-   [[3] [Linux distro agnostic ROS install]](#Linux_distro_agnostic_ROS_install)
-   [[4] [Installing ROS from Portage]](#Installing_ROS_from_Portage)
-   [[5] [Troubleshooting]](#Troubleshooting)

## [Preface]

There are currently (June 2016) three ways of installing ROS on Gentoo:

1.  Following the official (but experimental) guide using an ebuild repository.
2.  Following the official Linux distribution agnostic guide.
3.  Using ROS provided by the Gentoo ebuild repository (Portage\'s default).

If you are unsure which one to pick, stick with the ebuild repository-based method since the other two methods may require some troubleshooting. The other two options may be more attractive to purists.

** Note**\
ROS provides two links on ROS installation on Gentoo:

-   [http://wiki.ros.org/kinetic/Installation/Gentoo](http://wiki.ros.org/kinetic/Installation/Gentoo)
-   [http://wiki.ros.org/Installation/Gentoo](http://wiki.ros.org/Installation/Gentoo)

Be aware that the latter, ROS-distro agnostic documentation is just (wiki-)including the ROS-distro specific documentation. Hence both links show exactly the same information, assuming that you selected the corresponding ROS-distro on the ROS-distro agnostic link.

## [Following the official guide and using the ebuild repository]

This section is intended to be complementary to the official [ROS Jade Installation Guide](http://wiki.ros.org/jade/Installation/Gentoo).

### [Prerequisites]

ROS jade has an ebuild repository that is currently being maintained by the ROS Organization found [here.](https://github.com/ros/ros-overlay)

You will need to set up the ROS [ebuild repository](https://wiki.gentoo.org/wiki/Ebuild_repository "Ebuild repository") manually.

[FILE] **`/etc/portage/repos.conf/ros.conf`**

    [ros-overlay]
    location = /var/repo/ros-overlay
    sync-type = git
    sync-uri = https://github.com/ros/ros-overlay.git
    masters = gentoo

** Note**\
The location directory must exist before sync. Create the path or adjust it to somewhere appropriate.

Then sync the repository (future [emerge \--sync] operations will do this automatically):

`root `[`#`]`emaint sync -r ros-overlay`

In system dependencies:

It is not recommended to use pip in Gentoo. A large effort was made to ensure that all dependencies for primarily supported OS\'s (e.g. Ubuntu) are also resolved for Gentoo. Core ROS packages can be installed from the ebuild repository.

`root `[`#`]`emerge --ask dev-python/wstool dev-python/rosdep dev-python/rospkg dev-python/catkin_pkg dev-python/rosinstall_generator`

### [Installation]

The instructions from the official guide can be followed from this point.

## [Linux distro agnostic ROS install]

This section is intended to be complementary to [http://wiki.ros.org/Installation/Source](http://wiki.ros.org/Installation/Source).

The method suggested will install all ROS packages directly into your catkin workspace (so they won\'t be available in other workspaces) and installs ROS software dependencies from portage. As in the ebuild repository based guide, avoid using [pip] and install the required software for bootstrapping the ROS installation instead.

`root `[`#`]`emerge --ask dev-vcs/wstool dev-python/rosdep dev-python/rospkg dev-python/catkin_pkg dev-python/rosinstall_generator`

## [Installing ROS from Portage]

ROS is already represented in Portage. For example:

`root `[`#`]`emerge --ask ros-meta/desktop`

Some environment variables should be set for correct operation of ROS:

`user `[`$`]`export CMAKE_PREFIX_PATH=/usr `

`user `[`$`]`export PYTHONPATH=/usr/lib64/python2.7/site-packages/ `

`user `[`$`]`export ROS_DISTRO=kinetic `

`user `[`$`]`export ROS_ETC_DIR=/usr/etc/ros `

`user `[`$`]`export ROS_MASTER_URI='`[`http://localhost:11311'`](http://localhost:11311')` `

`user `[`$`]`export ROS_PACKAGE_PATH=/usr/share/ros_packages `

`user `[`$`]`export ROS_ROOT=/usr/share/ros `

It is easiest to simply put them in the user\'s [\~/.bashrc] file.

## [Troubleshooting]

-   ROScore won\'t start (it will appear inactive for some minutes and then display a message) unless the hostname is resolved correctly. The message will refer to [http://wiki.ros.org/ROS/NetworkSetup](http://wiki.ros.org/ROS/NetworkSetup)
-   If you miss rosrun and other shell commands, install [[[dev-ros/rosbash]](https://packages.gentoo.org/packages/dev-ros/rosbash)[]]
-   Sourcing /etc/profile may help
-   [[[sci-libs/vtk]](https://packages.gentoo.org/packages/sci-libs/vtk)[]] requires use-flag rendering
-   [[[dev-ros/std_msgs]](https://packages.gentoo.org/packages/dev-ros/std_msgs)[]] requires use-flags ros_messages_eus ros_messages_lisp ros_messages_nodejs if you want to avoid warning at compile time
-   the same use-flags should also be set for [[[dev-ros/sensor_msgs]](https://packages.gentoo.org/packages/dev-ros/sensor_msgs)[]] [[[dev-ros/geometry_msgs]](https://packages.gentoo.org/packages/dev-ros/geometry_msgs)[]] and other msgs as required
-   Setting PYTHONPATH to the above export can break regular 3.x systems. The requirements of ROS on Python can clash with the requirements of Portage and create emerge hell. Just like the standard implementation for development and experimentation it might be best to have the Gentoo install in a VM.