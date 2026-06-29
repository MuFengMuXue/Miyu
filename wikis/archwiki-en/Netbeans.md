# Netbeans

Netbeans is an integrated development environment (IDE) for developing with Java, JavaScript, PHP, Python, Ruby, Groovy, C, C++, Scala, Clojure, and other languages.

From Wikipedia:Netbeans:

:The NetBeans IDE is written in Java and can run anywhere a compatible JVM is installed, including Windows, Mac OS, Linux, and Solaris. A JDK is required for Java development functionality, but is not required for development in other programming languages.

## Installation
Install the  package.

## Tips and tricks
## Preserving configuration changes
* Settings in local version of  override the same settings in the global copy of the file.
* Command-line options override settings in either of the configuration files.

Another alternative is to use a pacman hook that modifies the system-wide configuration file. For example:

## Font antialiasing in Netbeans
As Netbeans is written in Java, the font rendering is managed by Java itself and also by Netbeans. Modifying the font antialiasing parameters can thus happen at two levels:

* Java.
* In the Netbeans configuration. If the file is missing, you may need to create it.

## Look and feel
To change Netbeans's look and feel, go to Tools > Options > Appearance > Look and Feel.

To add a dark look and feel to the GUI but also to the colorschemes used in the code, you can install one of the following certified extensions from the plugin directory which can be reached from Tools > Plugins > Available Plugins:

* Dark Look And Feel Themes
* Darcula LAF for NetBeans: which, as of January 2017, better integrates with current desktop environments and mimic the default Darcula look and feel from used in IntelliJ IDEA or Android Studio.

## Integrate with the Apache Tomcat Servlet Container
It is possible to debug web applications running on Tomcat from within Netbeans, using stock Arch packages for both Netbeans and Tomcat.

* First install your desired version of Tomcat (see Tomcat).
* While you can modify the configuration files in  to work with Netbeans debugging, it is recommended you create local copies and use those instead. That way, you still can run Tomcat as an ongoing system service, while debuggging with a different instance:
** Pick a location for the local configuration files, such as  and create that directory.
** Copy  to , e.g.  and , both with root privileges
* Clean up the Tomcat users and permission file, so Netbeans can insert what it needs. Edit the tomcat user file without any user and role information in it:

* Make the "manager" app accessible from your local configuration:  and
* Provide a  directory:
* If needed, change the port at which Tomcat runs by editing .
* Have Tomcat write its logs somewhere else than
* Unfortunately, Netbeans refuses to continue unless it can read , so temporarily give the file  permissions. Change the permissions back later.

Then, in Netbeans:

* Go to Tools > Servers > Add Server and select Apache Tomcat. Click Next.
* In Server location, specify .
* Check Use Private Configuration Folder (Catalina Base) and specify the full path to directory . This must be the full path, as Netbeans does not recognize the meaning of .
* Finally, pick a username and password. Check Create user if it does not exist. This will configure Netbeans, but also add the user information to the  file.

Note that this local instance of Tomcat will write its logs to , not .

## Integrate Netbeans with GNOME-Keyring
Install .

## Troubleshooting
## Maven problems with small tmpfs
If your system has a small tmpfs partition, you will have problems unpacking the maven index (will continue downloading again after failing to unpack). To fix this issue, append the following pieces of information in the Netbeans configuration file accordingly:

## Wrong Directory for JDK/JRE
It might be that after installation,  is set incorrectly:

Just comment out this line; netbeans will find the proper path on startup. Since  might be overwritten during an update, this procedure might need to be done again after an update, or you put  into the configuration file in your home directory (see above).

## Plugin installation fails due to lack of unpack200
The unpack200 plugin was removed in JDK version 14, causing plugin installation in Netbeans to fail. As a workaround, one can set  in  to an earlier JDK version. After plugin installation, you can return to the default JDK, but this will have to be repeated for each plugin update.
