# Binfmt misc for Java

From Wikipedia:
: is a capability of the Linux kernel which allows arbitrary executable file formats to be recognized and passed to certain user space applications, such as emulators and virtual machines.

In plain language, this allows you to take a file such as a Java jar or Mono exe that you would ordinarily run via a line such as
 $ java -jar /path/to/MyProgram.jar
 $ mono /path/to/MyProgram.exe
and instead run it simply with
 $ MyProgram.jar
 $ MyProgram.exe
as long as the executables are in the .

The information in this article is almost entirely taken from the files  and  in the  sub-directory of the Linux kernel source tree.

## Setup
## Mounting binfmt_misc
For an ad-hoc mount:
 # mount binfmt_misc -t binfmt_misc /proc/sys/fs/binfmt_misc
For a persistent mount via fstab add the line:
 none  /proc/sys/fs/binfmt_misc binfmt_misc defaults 0 0

## Registering file type with binfmt_misc
Filetype registration on Arch is handled by  (provided by ).

Binfmt registration lines can be placed in a file in .

The contents of the line is explained in the  file of the kernel source tree.

The following lines will create registration files for running Java binaries without having to explicitly call the java command (you still need to have it installed). The first two work by redirecting Java class and jar files to a set of 'wrapper' scripts described in the next section. The final entry runs Java applets in the usual way.
 # binfmt_misc support for Java applications:
 echo ':Java:M::\xca\xfe\xba\xbe::/usr/local/bin/javawrapper:' > /etc/binfmt.d/Java.conf
 # binfmt_misc support for executable Jar files:
 echo ':ExecutableJAR:E::jar::/usr/local/bin/jarwrapper:' > /etc/binfmt.d/ExecutableJAR.conf
 # binfmt_misc support for Java Applets:
 echo ':Applet:E::html::/opt/java/bin/appletviewer:' > /etc/binfmt.d/Applet.conf

Restart  to register the new handlers. Registered binfmt handlers show up as files in . Viewing this file should show the name of the registered wrapper script and either the magic bytes or file extension used to recognize that file type.

## Wrapper scripts
Please see /Wrapper_examples for jarwrapper and javawrapper scripts and related programs.

## A simple solution
This simple solution is suitable in most cases, no bugs are detected during execution.
Create file :
 :Java:E::class::/usr/local/bin/javawrapper:
Create file :
 #!/bin/sh
 file=${1%%.class}
 file=${file/.\//}
 java $file
Do not forget to make it executable

Restart .  Now you can test!

## Testing
Create a simple  program such as the following:
 class HelloWorld {
     public static void main(String args{
         System.out.println("Hello World!");
     }
 }
Compile it as normal and make the  file executable.

You should then be able to run it by simply entering:
 $ ./HelloWorld.class

## Notes
* Some of the material on binfmt_misc refers to it as a module but Arch builds it into the standard kernel.
* The setup given here works with both the Sun JRE & openjdk6.
* binfmt_misc can be used for other file types as well. For example, to be able to run DOS/Windows files without having to explicitly specify the wine program, add the following registration entry:
 # binfmt_misc support for DOS / Windows applications via Wine
 echo ':DOSWin:M::MZ::/usr/bin/wine:' > /proc/sys/fs/binfmt_misc/register
