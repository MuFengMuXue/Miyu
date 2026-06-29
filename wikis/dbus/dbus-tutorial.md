## D-Bus Tutorial

Version 0.5.0

## Tutorial Work In Progress

This tutorial is not complete; it probably contains some useful information, but also has plenty of gaps. Right now, you'll also need to refer to the D-Bus specification, Doxygen reference documentation, and look at some examples of how other apps use D-Bus.

Enhancing the tutorial is definitely encouraged - send your patches or suggestions to the mailing list. If you create a D-Bus binding, please add a section to the tutorial for your binding, if only a short section with a couple of examples.

## What is D-Bus?

D-Bus is a system for *interprocess communication* (IPC). Architecturally, it has several layers:

- A library, *libdbus*, that allows two applications to connect to each other and exchange messages.

- A *message bus daemon* executable, built on libdbus, that multiple applications can connect to. The daemon can route messages from one application to zero or more other applications.

- *Wrapper libraries* or *bindings* based on particular application frameworks. For example, libdbus-glib and libdbus-qt. There are also bindings to languages such as Python. These wrapper libraries are the API most people should use, as they simplify the details of D-Bus programming. libdbus is intended to be a low-level backend for the higher level bindings. Much of the libdbus API is only useful for binding implementation.

libdbus only supports one-to-one connections, just like a raw network socket. However, rather than sending byte streams over the connection, you send *messages*. Messages have a header identifying the kind of message, and a body containing a data payload. libdbus also abstracts the exact transport used (sockets vs. whatever else), and handles details such as authentication.

The message bus daemon forms the hub of a wheel. Each spoke of the wheel is a one-to-one connection to an application using libdbus. An application sends a message to the bus daemon over its spoke, and the bus daemon forwards the message to other connected applications as appropriate. Think of the daemon as a router.

The bus daemon has multiple instances on a typical computer. The first instance is a machine-global singleton, that is, a system daemon similar to sendmail or Apache. This instance has heavy security restrictions on what messages it will accept, and is used for systemwide communication. The other instances are created one per user login session. These instances allow applications in the user's session to communicate with one another.

The systemwide and per-user daemons are separate. Normal within-session IPC does not involve the systemwide message bus process and vice versa.

### D-Bus applications

There are many, many technologies in the world that have "Inter-process communication" or "networking" in their stated purpose: CORBA, DCE, DCOM, DCOP, XML-RPC, SOAP, MBUS, Internet Communications Engine (ICE), and probably hundreds more. Each of these is tailored for particular kinds of application. D-Bus is designed for two specific cases:

- Communication between desktop applications in the same desktop session; to allow integration of the desktop session as a whole, and address issues of process lifecycle (when do desktop components start and stop running).

- Communication between the desktop session and the operating system, where the operating system would typically include the kernel and any system daemons or processes.

For the within-desktop-session use case, the GNOME and KDE desktops have significant previous experience with different IPC solutions such as CORBA and DCOP. D-Bus is built on that experience and carefully tailored to meet the needs of these desktop projects in particular. D-Bus may or may not be appropriate for other applications; the FAQ has some comparisons to other IPC systems.

The problem solved by the systemwide or communication-with-the-OS case is explained well by the following text from the Linux Hotplug project:

> A gap in current Linux support is that policies with any sort of dynamic "interact with user" component aren't currently supported. For example, that's often needed the first time a network adapter or printer is connected, and to determine appropriate places to mount disk drives. It would seem that such actions could be supported for any case where a responsible human can be identified: single user workstations, or any system which is remotely administered.
>
> This is a classic "remote sysadmin" problem, where in this case hotplugging needs to deliver an event from one security domain (operating system kernel, in this case) to another (desktop for logged-in user, or remote sysadmin). Any effective response must go the other way: the remote domain taking some action that lets the kernel expose the desired device capabilities. (The action can often be taken asynchronously, for example letting new hardware be idle until a meeting finishes.) At this writing, Linux doesn't have widely adopted solutions to such problems. However, the new D-Bus work may begin to solve that problem.

D-Bus may happen to be useful for purposes other than the one it was designed for. Its general properties that distinguish it from other forms of IPC are:

- Binary protocol designed to be used asynchronously (similar in spirit to the X Window System protocol).

- Stateful, reliable connections held open over time.

- The message bus is a daemon, not a "swarm" or distributed architecture.

- Many implementation and deployment issues are specified rather than left ambiguous/configurable/pluggable.

- Semantics are similar to the existing DCOP system, allowing KDE to adopt it more easily.

- Security features to support the systemwide mode of the message bus.

## Concepts

Some basic concepts apply no matter what application framework you're using to write a D-Bus application. The exact code you write will be different for GLib vs. Qt vs. Python applications, however.

Here is a diagram (png svg) that may help you visualize the concepts that follow.

### Native Objects and Object Paths

Your programming framework probably defines what an "object" is like; usually with a base class. For example: java.lang.Object, GObject, QObject, python's base Object, or whatever. Let's call this a *native object*.

The low-level D-Bus protocol, and corresponding libdbus API, does not care about native objects. However, it provides a concept called an *object path*. The idea of an object path is that higher-level bindings can name native object instances, and allow remote applications to refer to them.

The object path looks like a filesystem path, for example an object could be named `/org/kde/kspread/sheets/3/cells/4/5`. Human-readable paths are nice, but you are free to create an object named `/com/mycompany/c5yo817y0c1y1c5b` if it makes sense for your application.

Namespacing object paths is smart, by starting them with the components of a domain name you own (e.g. `/org/kde`). This keeps different code modules in the same process from stepping on one another's toes.

### Methods and Signals

Each object has *members*; the two kinds of member are *methods* and *signals*. Methods are operations that can be invoked on an object, with optional input (aka arguments or "in parameters") and output (aka return values or "out parameters"). Signals are broadcasts from the object to any interested observers of the object; signals may contain a data payload.

Both methods and signals are referred to by name, such as "Frobate" or "OnClicked".

### Interfaces

Each object supports one or more *interfaces*. Think of an interface as a named group of methods and signals, just as it is in GLib or Qt or Java. Interfaces define the *type* of an object instance.

DBus identifies interfaces with a simple namespaced string, something like `org.freedesktop.Introspectable`. Most bindings will map these interface names directly to the appropriate programming language construct, for example to Java interfaces or C++ pure virtual classes.

### Proxies

A *proxy object* is a convenient native object created to represent a remote object in another process. The low-level DBus API involves manually creating a method call message, sending it, then manually receiving and processing the method reply message. Higher-level bindings provide proxies as an alternative. Proxies look like a normal native object; but when you invoke a method on the proxy object, the binding converts it into a DBus method call message, waits for the reply message, unpacks the return value, and returns it from the native method..

In pseudocode, programming without proxies might look like this:

``` programlisting
          Message message = new Message("/remote/object/path", "MethodName", arg1, arg2);
          Connection connection = getBusConnection();
          connection.send(message);
          Message reply = connection.waitForReply(message);
          if (reply.isError()) {
             
          } else {
             Object returnValue = reply.getReturnValue();
          }
        
```

Programming with proxies might look like this:

``` programlisting
          Proxy proxy = new Proxy(getBusConnection(), "/remote/object/path");
          Object returnValue = proxy.MethodName(arg1, arg2);
        
```

### Bus Names

When each application connects to the bus daemon, the daemon immediately assigns it a name, called the *unique connection name*. A unique name begins with a ':' (colon) character. These names are never reused during the lifetime of the bus daemon - that is, you know a given name will always refer to the same application. An example of a unique name might be `:34-907`. The numbers after the colon have no meaning other than their uniqueness.

When a name is mapped to a particular application's connection, that application is said to *own* that name.

Applications may ask to own additional *well-known names*. For example, you could write a specification to define a name called `com.mycompany.TextEditor`. Your definition could specify that to own this name, an application should have an object at the path `/com/mycompany/TextFileManager` supporting the interface `org.freedesktop.FileHandler`.

Applications could then send messages to this bus name, object, and interface to execute method calls.

You could think of the unique names as IP addresses, and the well-known names as domain names. So `com.mycompany.TextEditor` might map to something like `:34-907` just as `mycompany.com` maps to something like `192.168.0.5`.

Names have a second important use, other than routing messages. They are used to track lifecycle. When an application exits (or crashes), its connection to the message bus will be closed by the operating system kernel. The message bus then sends out notification messages telling remaining applications that the application's names have lost their owner. By tracking these notifications, your application can reliably monitor the lifetime of other applications.

Bus names can also be used to coordinate single-instance applications. If you want to be sure only one `com.mycompany.TextEditor` application is running for example, have the text editor application exit if the bus name already has an owner.

### Addresses

Applications using D-Bus are either servers or clients. A server listens for incoming connections; a client connects to a server. Once the connection is established, it is a symmetric flow of messages; the client-server distinction only matters when setting up the connection.

If you're using the bus daemon, as you probably are, your application will be a client of the bus daemon. That is, the bus daemon listens for connections and your application initiates a connection to the bus daemon.

A D-Bus *address* specifies where a server will listen, and where a client will connect. For example, the address `unix:path=/tmp/abcdef` specifies that the server will listen on a UNIX domain socket at the path `/tmp/abcdef` and the client will connect to that socket. An address can also specify TCP/IP sockets, or any other transport defined in future iterations of the D-Bus specification.

When using D-Bus with a message bus daemon, libdbus automatically discovers the address of the per-session bus daemon by reading an environment variable. It discovers the systemwide bus daemon by checking a well-known UNIX domain socket path (though you can override this address with an environment variable).

If you're using D-Bus without a bus daemon, it's up to you to define which application will be the server and which will be the client, and specify a mechanism for them to agree on the server's address. This is an unusual case.

### Big Conceptual Picture

Pulling all these concepts together, to specify a particular method call on a particular object instance, a number of nested components have to be named:

``` programlisting
          Address -> [Bus Name] -> Path -> Interface -> Method
        
```

The bus name is in brackets to indicate that it's optional -- you only provide a name to route the method call to the right application when using the bus daemon. If you have a direct connection to another application, bus names aren't used; there's no bus daemon.

The interface is also optional, primarily for historical reasons; DCOP does not require specifying the interface, instead simply forbidding duplicate method names on the same object instance. D-Bus will thus let you omit the interface, but if your method name is ambiguous it is undefined which method will be invoked.

### Messages - Behind the Scenes

D-Bus works by sending messages between processes. If you're using a sufficiently high-level binding, you may never work with messages directly.

There are 4 message types:

- Method call messages ask to invoke a method on an object.

- Method return messages return the results of invoking a method.

- Error messages return an exception caused by invoking a method.

- Signal messages are notifications that a given signal has been emitted (that an event has occurred). You could also think of these as "event" messages.

A method call maps very simply to messages: you send a method call message, and receive either a method return message or an error message in reply.

Each message has a *header*, including *fields*, and a *body*, including *arguments*. You can think of the header as the routing information for the message, and the body as the payload. Header fields might include the sender bus name, destination bus name, method or signal name, and so forth. One of the header fields is a *type signature* describing the values found in the body. For example, the letter "i" means "32-bit integer" so the signature "ii" means the payload has two 32-bit integers.

### Calling a Method - Behind the Scenes

A method call in DBus consists of two messages; a method call message sent from process A to process B, and a matching method reply message sent from process B to process A. Both the call and the reply messages are routed through the bus daemon. The caller includes a different serial number in each call message, and the reply message includes this number to allow the caller to match replies to calls.

The call message will contain any arguments to the method. The reply message may indicate an error, or may contain data returned by the method.

A method invocation in DBus happens as follows:

- The language binding may provide a proxy, such that invoking a method on an in-process object invokes a method on a remote object in another process. If so, the application calls a method on the proxy, and the proxy constructs a method call message to send to the remote process.

- For more low-level APIs, the application may construct a method call message itself, without using a proxy.

- In either case, the method call message contains: a bus name belonging to the remote process; the name of the method; the arguments to the method; an object path inside the remote process; and optionally the name of the interface that specifies the method.

- The method call message is sent to the bus daemon.

- The bus daemon looks at the destination bus name. If a process owns that name, the bus daemon forwards the method call to that process. Otherwise, the bus daemon creates an error message and sends it back as the reply to the method call message.

- The receiving process unpacks the method call message. In a simple low-level API situation, it may immediately run the method and send a method reply message to the bus daemon. When using a high-level binding API, the binding might examine the object path, interface, and method name, and convert the method call message into an invocation of a method on a native object (GObject, java.lang.Object, QObject, etc.), then convert the return value from the native method into a method reply message.

- The bus daemon receives the method reply message and sends it to the process that made the method call.

- The process that made the method call looks at the method reply and makes use of any return values included in the reply. The reply may also indicate that an error occurred. When using a binding, the method reply message may be converted into the return value of of a proxy method, or into an exception.

The bus daemon never reorders messages. That is, if you send two method call messages to the same recipient, they will be received in the order they were sent. The recipient is not required to reply to the calls in order, however; for example, it may process each method call in a separate thread, and return reply messages in an undefined order depending on when the threads complete. Method calls have a unique serial number used by the method caller to match reply messages to call messages.

### Emitting a Signal - Behind the Scenes

A signal in DBus consists of a single message, sent by one process to any number of other processes. That is, a signal is a unidirectional broadcast. The signal may contain arguments (a data payload), but because it is a broadcast, it never has a "return value." Contrast this with a method call (see the section called “Calling a Method - Behind the Scenes”) where the method call message has a matching method reply message.

The emitter (aka sender) of a signal has no knowledge of the signal recipients. Recipients register with the bus daemon to receive signals based on "match rules" - these rules would typically include the sender and the signal name. The bus daemon sends each signal only to recipients who have expressed interest in that signal.

A signal in DBus happens as follows:

- A signal message is created and sent to the bus daemon. When using the low-level API this may be done manually, with certain bindings it may be done for you by the binding when a native object emits a native signal or event.

- The signal message contains the name of the interface that specifies the signal; the name of the signal; the bus name of the process sending the signal; and any arguments

- Any process on the message bus can register "match rules" indicating which signals it is interested in. The bus has a list of registered match rules.

- The bus daemon examines the signal and determines which processes are interested in it. It sends the signal message to these processes.

- Each process receiving the signal decides what to do with it; if using a binding, the binding may choose to emit a native signal on a proxy object. If using the low-level API, the process may just look at the signal sender and name and decide what to do based on that.

### Introspection

D-Bus objects may support the interface `org.freedesktop.DBus.Introspectable`. This interface has one method `Introspect` which takes no arguments and returns an XML string. The XML string describes the interfaces, methods, and signals of the object. See the D-Bus specification for more details on this introspection format.

## GLib APIs

The recommended GLib API for D-Bus is GDBus, which has been distributed with GLib since version 2.26. It is not documented here. See the GLib documentation for details of how to use GDBus.

An older API, dbus-glib, also exists. It is deprecated and should not be used in new code. Whenever possible, porting existing code from dbus-glib to GDBus is also recommended.

## Python API

The Python API, dbus-python, is now documented separately in the dbus-python tutorial (also available in doc/tutorial.txt, and doc/tutorial.html if built with python-docutils, in the dbus-python source distribution).

## Qt API

The Qt binding for libdbus, QtDBus, has been distributed with Qt since version 4.2. It is not documented here. See the Qt documentation for details of how to use QtDBus.
