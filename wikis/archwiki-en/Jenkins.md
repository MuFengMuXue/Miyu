# Jenkins

Jenkins is an open source continuous integration server written in Java. It is capable of running scheduled automated builds and test suites of managed software projects. The build or tests for example may be triggered on a per commit basis or in a calendar driven manner. Jenkins thereby relies on the code being managed via a version control system (see git) and an automated build process. Note that Jenkins is not limited to Java applications and is suitable to manage projects in all common languages. Its capabilities can be further expanded by plugins.

## Installation
Install  for the latest stable release or  for the long-term-support version. The package will create a Jenkins user for the daemon using systemd-sysusers.
If running on a server with only console access, also install packages  and .

## Configuration
In order to enable , you need to have  installed and the path to your version of the Java Runtime Environment must be in the first line of the jenkins config file at , if this is not the case, the  will fail to start.

Project configuration can be done using the built-in web interface. To access it start/enable .

You can now open  with your browser and start setting up Jenkins.

The configuration file of the daemon running Jenkins is located at . It is sourced by the according  file and takes effect immediately after a restart.

jenkins listens on  and is immediately available remotely. If this is unwanted, for example on a test server, consider adding  to the configuration file (e.g. in ).

## Log in as the Jenkins user
The default Admin username is Admin. When you log into the Web interface at ; you will need to view the file at  or run  and search for the default password that was created upon installation.

The home folder of the  user is located at . The Jenkins user does not have a default shell, so if you need to log in this user (for example to manage SSH keys) see su#Nologin users.

## Running Jenkins with access to the display
If Jenkins needs to run graphical applications that fail without a display (for example, the Unity Editor), you must run it from a desktop session. If you are running GNOME, you can do the following to automatically run Jenkins with access to the display:

* Give Jenkins a login shell.

 # usermod -s /bin/bash jenkins

* Give Jenkins a password.

 # passwd jenkins

* Set Jenkins to automatically login using GDM.

* Add a new autostart application of your favorite terminal running jenkins.

After a reboot, GDM should automatically log into a gnome session. Then gnome should launch a terminal running a jenkins instance. This instance should be able to build Unity games without issue!
