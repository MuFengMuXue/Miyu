# Java

From the Wikipedia article:

:Java is a programming language originally developed by Sun Microsystems and released in 1995 as a core component of Sun Microsystems' Java platform. The language derives much of its syntax from C and C++ but has a simpler object model and fewer low-level facilities. Java applications are typically compiled to bytecode that can run on any Java virtual machine (JVM) regardless of computer architecture.

Arch Linux officially supports the open source OpenJDK versions 8, 11, 17, 21, and 25 — Long-Term Support (LTS) versions, and 26 — the latest released version. All these JVMs can be installed without conflict and switched between using helper script archlinux-java (installed with  package). Several other Java environments are available in Arch User Repository but are not officially supported.

## Installation
Two common packages are respectively pulled as dependency, named  (containing common files for Java Runtime Environments) and  (containing common files for Java Development Kits).

The provided  and  files point to a linked location , set by the archlinux-java helper script.

Most executables of the Java installation are provided by direct links in , while others are available in .

Arch does not use . If a program explicitly requires , set .

## OpenJDK
OpenJDK is an open-source implementation of the Java Platform, Standard Edition (Java SE), designated as the official reference implementation. There are several distributors of OpenJDK builds such as Adoptium (formerly known as AdoptOpenJDK) and Amazon Corretto. The Arch Linux OpenJDK packages are built from the upstream OpenJDK source code.

;Headless JRE: The minimal Java runtime environment—is needed for executing non-GUI Java programs.
;Full JRE: Full Java runtime environment—is needed for executing GUI Java programs.
;JDK:Java Development Kit—is needed for Java development.

JDK, full JRE and  headless JRE conflict with each other, as the smaller packages are subsets:

* JDK conflicts and provides full JRE,
* full JRE conflicts and provides headless JRE.

{| class="wikitable"
! Version !! Headless JRE !! Full JRE !! JDK !! Documentation !! Sources
|-
| OpenJDK 26 ||  ||  ||  ||  ||
|-
| OpenJDK 25 ||  ||  ||  ||  ||
|-
| OpenJDK 21 ||  ||  ||  ||  ||
|-
| OpenJDK 17 ||  ||  ||  ||  ||
|-
| OpenJDK 11 ||  ||  ||  ||  ||
|-
| OpenJDK 8 ||  ||  ||  ||  ||
|}

## OpenJFX
OpenJFX is the open-source implementation of JavaFX. You do not need to install this package if you are using Oracle JDK. This package only concerns users of the open source implementation of Java (OpenJDK project), and its derivatives.

{| class="wikitable"
! Version !! Runtime Environment and Development Kit!! Documentation !! Sources
|-
| OpenJFX 27 ||  ||  ||
|-
| OpenJFX 21 ||  ||  ||
|-
| OpenJFX 17 ||  ||  ||
|-
| OpenJFX 11 ||  ||  ||
|-
| OpenJFX 8 ||  ||  ||
|}

## Other implementations
*
*
*
*
*
*
*
*
*

## Development tools
For integrated development environments, see List of applications/Utilities#Integrated development environments and the Java IDEs subsection specifically.

To discourage reverse engineering an obfuscator like  can be used.

## Decompilers
*
*
*
*
*
*
*
*

## GUI Frontends
*
*
*
*
*

## Switching between JVM
The helper script archlinux-java (package : ) provides such functionalities:

 archlinux-java

 COMMAND:
 status          List installed Java environments and enabled one
 get             Return the short name of the Java environment set as default
 set   Force  as default
 unset           Unset current default Java environment
 fix             Fix an invalid/broken default Java environment configuration

## List compatible Java environments installed
 $ archlinux-java status

Example:

Note the  denoting that  is currently set as default. Invocation of  and other binaries will rely on this Java install. Also note on the previous output that only the JRE part of OpenJDK 8 is installed here.

## Change default Java environment
 # archlinux-java set JAVA_ENV_NAME

Example:

 # archlinux-java set java-8-openjdk/jre

Note that  will not let you set an invalid Java environment. In the previous example,  is installed but  is not so trying to set  will fail:

## Unsetting the default Java environment
There should be no need to unset a Java environment as packages providing them should take care of this. Still should you want to do so, just use command :

 # archlinux-java unset

## Fixing the default Java environment
If an invalid Java environment link is set, calling the  command tries to fix it. Also note that if no default Java environment is set, this will look for valid ones and try to set it for you. Officially supported package "OpenJDK 8" will be considered first in this order, then other installed environments.

 # archlinux-java fix

## Launching an application with the non-default Java version
If you want to launch an application with another version of Java than the default one (for example if you have both versions 18—the default—and 11 installed on your system, and you want to use Java 11), you can wrap your application in a small shell script to locally change the default path of Java:

 #!/bin/sh

 export PATH="/usr/lib/jvm/java-11-openjdk/bin/:$PATH"
 exec /path/to/application "$@"

For a systemd service you can append  to environment variables in the drop-in file:

## Package pre-requisites to support archlinux-java
This section is targeted at packagers willing to provide packages in the AUR for an alternate JVM and be able to integrate with the Arch Linux JVM scheme (i.e. to be compatible with ); to do so, packages should:

* Place all files under {{ic|/usr/lib/jvm/java-${JAVA_MAJOR_VERSION}-${VENDOR_NAME} }}
* Ensure all executables for which  and  provide links are available in the corresponding package
* Ship links from  to executables, only if these links do not already belong to  and
* Suffix man pages with {{ic|-${VENDOR_NAME}${JAVA_MAJOR_VERSION} }} to prevent conflicts (see  file list where man pages are suffixed with )
* Do not declare any conflicts nor replaces with other JDKs, ,  nor
* Use script  in install functions to set the Java environment as default if no other valid Java environment is already set (ie: package should not force install as default). See officially supported Java environment package sources for examples

Also please note that:

* Packages that need any Java environment should declare dependency on ,  or  as usual
* Packages that need a specific Java vendor should declare dependency on the corresponding package
* OpenJDK packages now declare {{ic|1=provides="java-runtime-openjdk=${pkgver}"}} etc. This enables a third-party package to declare dependency on an OpenJDK without specifying a version

## Tips and tricks
Behavior of most Java applications can be controlled by supplying predefined environment variables to the Java runtime. A way to do it consists of adding the following environment variable:export JDK_JAVA_OPTIONS="-D' -D'..."

For example, to use system anti-aliased fonts and make swing use the GTK look and feel:

 export JDK_JAVA_OPTIONS='-Dawt.useSystemAAFontSettings=on -Dswing.aatext=true -Dswing.defaultlaf=com.sun.java.swing.plaf.gtk.GTKLookAndFeel'

Three such variables exist, the options which are explained later in the table below take priority.

{| class="wikitable"
|-
|
| Affects applications as well as tools like javac or the jshell.
|-
|
| Affects applications (everything started via the java command). Requires Java 9.
|-
| (command line options)
| Arguments specified before the "class name" argument are Java options.
|-
|
| The old way, affects applications and tools.
|}

## Better font rendering
Both closed source and open source implementations of Java are known to have improperly implemented anti-aliasing of fonts. This can be fixed with the following options: ,

See Java Runtime Environment fonts for more detailed information.

## Silence 'Picked up JDK_JAVA_OPTIONS' message on command line
Setting the  environment variable makes java (openjdk) write messages like 'Picked up JDK_JAVA_OPTIONS=...' to stderr. To suppress those messages in your terminal you can unset the environment variable and alias java in your shell configuration file to pass those same options as command line arguments:

 SILENT_JAVA_OPTIONS="$JDK_JAVA_OPTIONS"
 unset JDK_JAVA_OPTIONS
 alias java='java "$SILENT_JAVA_OPTIONS"'

## GTK LookAndFeel
If your Java programs look ugly, you may want to set up the default look and feel for the swing components:

 swing.defaultlaf=com.sun.java.swing.plaf.gtk.GTKLookAndFeel

Some Java programs insist on using the cross platform Metal look and feel. In some of these cases you can force these applications to use the GTK look and feel by setting the following property:

 swing.crossplatformlaf=com.sun.java.swing.plaf.gtk.GTKLookAndFeel

## HiDPI
Depending on the GUI framework, HiDPI#Java applications can be enabled using different methods.

## Troubleshooting
## MySQL
Since JDBC drivers often use the port in the URL to establish a connection to the database, it is considered "remote" (i.e., by default, MySQL does not listen on the port) even though they may be running on the same host. Thus, to use JDBC and MySQL, you should enable remote access to MySQL, following the instructions in MariaDB#Grant remote access.

## IntelliJ IDEA
If IntelliJ IDEA outputs  with the system Java SDK path, you may have to install a different JDK package and select it as IDEA's JDK.

## Impersonate another window manager
You may use the  from [https://tools.suckless.org/x/wmname suckless.org to make the JVM believe you are running a different window manager. This may solve a rendering issue of Java GUIs occurring in window managers like Awesome or Dwm or Ratpoison. This works because the JVM contains a hard-coded list of known, non-re-parenting window managers. For maximum irony, some users prefer to impersonate , the non-re-parenting window manager written by Sun, in Java. Try setting ,  or .

 $ wmname window_manager_name

You must restart the application in question after issuing the wmname command.

Alternatively, the javaagent JavaMatePatch, created to set the WM name in MATE and resolve the bug with java swing apps working incorrectly when launched in full screen, can be used. Add  to the java options to use it.

## Illegible fonts
In addition to the suggestions mentioned below in #Better font rendering, some fonts may still not be legible afterwards. If this is the case, there is a good chance Microsoft fonts are being used. Install .

## Missing text in some applications
If some applications are completely missing texts it may help to use the options under #Tips and tricks as suggested in .

## Gray window, applications not resizing with WM, menus immediately closing
The standard Java GUI toolkit has a hard-coded list of "non-reparenting" window managers. If using one that is not on that list, there can be some problems with running some Java applications. One of the most common problems is "gray blobs", when the Java application renders as a plain gray box instead of rendering the GUI. Another one might be menus responding to your click, but closing immediately.

There are several things that may help:

* See #Impersonate another window manager.
* Set the  environment variable.
* For later versions, set the  environment variable.
* For xmonad, use SetWMName. However, its effect may be canceled when also using . In this case, appending  to the  may help.

For more information, see Problems with Java applications, Applet java console.

## System freezes when debugging JavaFX Applications
If your system freezes while debugging a JavaFX Application, you can try to supply the JVM option .

See https://bugs.java.com/bugdatabase/view_bug?bug_id=6714678

## JavaFX's MediaPlayer constructor throws an exception
Creating instance of MediaPlayer class from JavaFX's sound modules might throw following exception (both Oracle JDK and OpenJDK)

 ... (i.e. FXMLLoader construction exceptions) ...
 Caused by: MediaException: UNKNOWN : com.sun.media.jfxmedia.MediaException: Could not create player! : com.sun.media.jfxmedia.MediaException: Could not create player!
  at javafx.scene.media.MediaException.exceptionToMediaException(MediaException.java:146)
  at javafx.scene.media.MediaPlayer.init(MediaPlayer.java:511)
  at javafx.scene.media.MediaPlayer.(MediaPlayer.java:414)
  at
 ...

which is a result of some incompatibilities of JavaFX with modern  build delivered within Arch Linux repository.

Working solution is to install . Alternatively, installing  may work if the previous version fails to build.

See https://www.reddit.com/r/archlinux/comments/70o8o6/using_a_javafx_mediaplayer_in_arch/

## Java applications cannot open external links
If a Java application is not able to open a link to, for example, your web browser, install . This is required by the  method. See https://bugs.launchpad.net/ubuntu/+source/openjdk-8/+bug/1574879/comments/2
An application printing the error message  is a solid indicator for this problem.

## Error initializing QuantumRenderer: no suitable pipeline found
Possible issues / solutions:

* GTK2 is missing. Install
* OpenJFX is missing. Install
