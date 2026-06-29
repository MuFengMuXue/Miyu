## D-Bus Test Plan

## Introduction

This document tries to explain the details of the test plan for D-Bus

### The importance of testing

As with any big library or program, testing is important. It can help find bugs and regressions and make the code better overall.

D-Bus is a large and complex piece of software (about 25,000 lines of code for the client library, and 2,500 lines of code for the bus daemon) and it's therefore important to try to make sure that all parts of the software is functioning correctly.

D-Bus can be built with support for testing by passing `--enable-tests`. to the configure script. It is recommended that production systems build without testing since that reduces the D-Bus client library size.

## Testing the D-Bus client library

The tests for the client library consist of the test-dbus program which is a unit test for all aspects of the client library. Whenever a bug in the client library is found and fixed, a test is added to make sure that the bug won't occur again.

### Data Structures

The D-Bus client library consists of some data structures that are used internally; a linked list class, a hashtable class and a string class. All aspects of those are tested by test-dbus.

### Message loader

The message loader is the part of D-Bus that takes messages in raw character form and parses them, turning them into DBusMessages.

This is one of the parts of D-Bus that *must* be absolutely bug-free and robust. The message loader should be able to handle invalid and incomplete messages without crashing. Not doing so is a serious issue and can easily result in D-Bus being exploitable to DoS attacks.

To solve these problems, there is a testing feature called the Message Builder. The message builder can take a serialized message in string-form and convert it into a raw character string which can then be loaded by the message loader.

**Figure 1. Example of a message in string form**

``` programlisting
          # Standard org.freedesktop.DBus.Hello message

          VALID_HEADER
          FIELD_NAME name
          TYPE STRING
          STRING 'org.freedesktop.DBus.Hello'
          FIELD_NAME srvc
          TYPE STRING
          STRING 'org.freedesktop.DBus'
          ALIGN 8
          END_LENGTH Header
          START_LENGTH Body
          END_LENGTH Body
        
```

  

The file format of messages in string form is documented in the D-Bus Reference Manual.

The message test part of test-dbus is using the message builder to build different kinds of messages, both valid, invalid, and invalid ones, to make sure that the loader won't crash or leak memory of any of those, and that the loader knows if a message is valid or not.

There is also a test program called `break-loader` that loads a message in string-form into raw character form using the message builder. It then randomly changes the message, it can for example replace single bytes of data or modify the length of the message. This is to simulate network errors. The break-loader program saves all the messages leading to errors so it can easily be run for a long period of time.

### Authentication

For testing authentication, there is a testing feature that can read authentication sequences from a file and play them back to a dummy server and client to make sure that authentication is working according to the specification.

**Figure 2. Example of an authentication script**

``` programlisting
          ## this tests a successful auth of type EXTERNAL
          
          SERVER
          SEND 'AUTH EXTERNAL USERNAME_HEX'
          EXPECT_COMMAND OK
          EXPECT_STATE WAITING_FOR_INPUT
          SEND 'BEGIN'
          EXPECT_STATE AUTHENTICATED
        
```

  

## Testing the D-Bus bus daemon

Since the D-Bus bus daemon is using the D-Bus client library it will benefit from all tests done on the client library, but there is still the issue of testing client-server communication. This is more complicated since it it may require another process running.

### The debug transport

In D-Bus, a *transport* is a class that handles sending and receiving raw data over a certain medium. The transport that is used most in D-Bus is the UNIX transport with sends and recevies data over a UNIX socket. A transport that tunnels data through X11 client messages is also under development.

The D-Bus debug transport is a specialized transport that works in-process. This means that a client and server that exists in the same process can talk to eachother without using a socket.

### The test-bus program

The test-bus program is a program that is used to test various parts of the D-Bus bus daemon; robustness and that it conforms to the specifications.

The test program has the necessary code from the bus daemon linked in, and it uses the debug transport for communication. This means that the bus daemon code can be tested without the real bus actually running, which makes testing easier.

The test-bus program should test all major features of the bus, such as service registration, notification when things occurs and message matching.

## Other tests

### Out-Of-Memory robustness

Since D-Bus should be able to be used in embedded devices, and also as a system service, it should be able to cope with low-memory situations without exiting or crashing.

In practice, this means that both the client and server code must be able to handle dbus_malloc returning NULL.

To test this, two environment variables exist. `DBUS_MALLOC_FAIL_NTH` will make every nth call to dbus_malloc return NULL, and `DBUS_MALLOC_FAIL_GREATER_THAN` will make any dbus_malloc call with a request for more than the specified number of bytes fail.

### Memory leaks and code robustness

Naturally there are some things that tests can't be written for, for example things like memory leaks and out-of-bounds memory reading or writing.

Luckily there exists good tools for catching such errors. One free good tool is Valgrind, which runs the program in a virtual CPU which makes catching errors easy. All test programs can be run under Valgrind,
