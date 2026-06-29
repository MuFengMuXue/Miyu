\[next\] \[prev\] \[prev-tail\] \[tail\] \[up\]

### 1  Introduction

This document describes how to use the Java implementation of D-Bus. D-Bus is an IPC mechanism which at a low level uses message passing over Unix Sockets or IP. D-Bus models its messages as either function calls on remote objects, or signals emitted from them.

Java is an object-oriented language and this implementation attempts to match the D-Bus IPC model to the Java object model. The implementation also make heavy use of threads and exceptions. The programmer should be careful to take care of synchronisation issues in their code. All method calls by remote programs on exported objects and all signal handlers are run in new threads. Any calls on remote objects may throw DBusExecutionException, which is a runtime exception and so the compiler will not remind you to handle it.

The Java D-Bus API is also documented in the JavaDoc<sup>1</sup> , D-Bus is described in the specification<sup>2</sup> and the API documentation<sup>3</sup> .

#### 1.1  Protocol Implementation

This library is a native Java implementation of the D-Bus protocol and not a wrapper around the C reference implementation.

#### 1.2  Dependencies

This library requires Java 1.5-compatible VM and compiler (either Sun, or ecj+jamvm with classpath-generics newer than 0.19) and the unix socket, debug and hexdump libraries from http://www.matthew.ath.cx/projects/java/.

#### 1.3  D-Bus Terminology

D-Bus has several notions which are exposed to the users of the Java implementation.

##### 1.3.1  Bus Names

Programs on the bus are issued a unique identifier by the bus. This is guaranteed to be unique within one run of the bus, but is assigned sequentially to each new connection.

There are also so called well-known bus names which a device can request on the bus. These are of the form “org.freedesktop.DBus”, and any program can request them if they are not already owned.

##### 1.3.2  Interfaces

All method calls and signals are specified using an interface, similar to those in Java. When executing a method or sending a signal you specify the interface the method belongs to. These are of the form “org.freedesktop.DBus”.

##### 1.3.3  Object Paths

A program may expose more than one object which implements an interface. Object paths of the form “/org/freedesktop/DBus” are used to distinguish objects.

##### 1.3.4  Member Names

Methods and Signals have names which identify them within an interface. D-Bus does not support method overloading, only one method or signal should exist with each name.

##### 1.3.5  Errors

A reply to any message may be an error condition. In which case you reply with an error message which has a name of the form “org.freedesktop.DBus.Error.ServiceUnknown”.

\[next\] \[prev\] \[prev-tail\] \[front\] \[up\]
