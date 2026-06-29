\[prev\] \[prev-tail\] \[tail\] \[up\]

### 10  CreateInterface

D-Bus provides a method to get introspection data on a remote object, which describes the interfaces, methods and signals it provides. This introspection data is in XML format<sup>19</sup> . The library automatically provides XML introspection data on all objects which are exported by it. Introspection data can be used to create Java interface definitions automatically.

The CreateInterface<sup>20</sup> class will automatically create Java source files from an XML file containing the introspection data, or by querying the remote object over D-Bus. CreateInterface can be called from Java code, or can be run as a stand alone program.

The syntax for the CreateInterface program is

CreateInterface \[--system\] \[--session\] \[--create-files\]    
                  \<bus name\> \<object\>    
CreateInterface \[--create-files\] \<introspection-file.xml\>

The Java source code interfaces will be written to the standard ouput. If the --create-files option is specified the correct files in the correct directory structure will be created.

#### 10.1  Nested Interfaces

In some cases there are nested interfaces. In this case CreateInterface will not correctly create the Java equivalent. This is because Java cannot have both a class and a package with the same name. The solution to this is to create nested classes in the same file.

An example would be the Hal interface:

\<interface name="org.freedesktop.Hal.Device"\>    
   ...    
\</interface\>    
\<interface name="org.freedesktop.Hal.Device.Volume"\>    
   ...    
\</interface\>

When converted to Java you would just have one file org/freedesktop/Hal/Device.java in the package org.freedesktop.Hal, which would contain one class and one nested class:

public interface Device extends DBusInterface {    
   public interface Volume extends DBusInterface {    
      ... methods in Volume ...    
   }    
   ... methods in Device ...    
}

\[prev\] \[prev-tail\] \[front\] \[up\]
