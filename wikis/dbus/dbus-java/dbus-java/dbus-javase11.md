\[prev\] \[prev-tail\] \[tail\] \[up\]

### 11  Debugging

It is possible to enable debugging in the library. This will be a lot slower, but can print a lot of useful information for debugging your program.

To enable a debug build compile with DEBUG=enable. This will then need to be enabled at runtime by using the debug jar with debugging enabled (usually installed as debug-enable.jar alongside the normal jar).

Running a program which uses this library will print some informative messages. More verbose debug information can be got by supplying a custom debug configuration file. This should be placed in the file debug.conf and has the format:

classname = LEVEL

Where classname is either the special word ALL or a full class name like org.freedesktop.dbus and LEVEL is one of NONE, CRIT, ERR, WARN, INFO, DEBUG, VERBOSE, YES, ALL or TRUE. This will set the debug level for a particular class. Any messages from that class at that level or higher will be printed. Verbose debugging is extremely verbose.

In addition, setting the environment variable DBUS\_JAVA\_EXCEPTION\_DEBUG will cause all exceptions which are handled internally to have their stack trace printed when they are handled. This will happen unless debugging has been disabled for that class.

\[prev\] \[prev-tail\] \[front\] \[up\]
