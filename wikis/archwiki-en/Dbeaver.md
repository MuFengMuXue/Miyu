# Dbeaver

Dbeaver is a free multi-platform database administration tool. For more information about features, see the official homepage.

It supports popular databases such as MySQL, MariaDB, PostgreSQL, SQLite, Oracle database.

It provides a plugin architecture (based on Eclipse plugins architecture) that allows to modify much of the application behavior to provide database-specific functionality or features that are database-independent. This is a desktop application written in Java and based on Eclipse platform.

## Installation
Install the  package. DBeaver relies on Java: for jvm installation and configuration, see Java.

## Troubleshooting
## JVM terminated error
If you are getting an error like this:

Try adding  to your xinitrc.

## DBeaver configuration location
The location of the DBeaver configuration files are located

## Java version
DBeaver relies on Java 17 or above.

If you get an error message like this:

  Version  of the JVM is not suitable for this product. Version: 17 or greater is required.

This means that your Java version is outdated. You can fix it by installing a newer Java version and changing the default java.

## GUI elements too big or filled with black rectangles
For HiDPI screens, GUI elements of Dbeaver might appear too big and certain parts of the interface might be filled with black rectangles.

This can be fixed by setting the following environment variables:

 GDK_SCALE=2
 GDK_DPI_SCALE=0.5

or:

 GDK_BACKEND=x11

Obviously the optimal values depend on the resolution of the screen, so a bit of trial and error might be needed. See HiDPI for more information.

## Broken clipboard on Plasma Wayland between DBeaver and other applications
Running DBeaver with Xwayland seems to fix the problem :

 $ GDK_BACKEND=x11 dbeaver
