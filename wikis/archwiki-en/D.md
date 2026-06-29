# D

From Wikipedia:D (programming language):

* it is an object-oriented, imperative, multi-paradigm system programming language,
* it is predominantly influenced by C++, but it is not a variant of it,
* it also has been influenced by concepts used in C#, Eiffel and Java.

## Installation
To program in D you will need two things—a D compiler and a library. The easiest way to get started fast is to install  package group. It will provide the official compiler , the standard library , and —a collection of small development tools.

## Testing the installation
To make sure that everything is installed and set up correctly, a simple "Hello World" program should suffice.

{{hc|hello.d|2=
import std.stdio;

void main() {
   string yourName = "archer";
   writefln("Hello %s!", yourName);
}
}}

And run:

 $ dmd hello.d

in the same directory as the file. You should then be able to execute the program with:

 $ ./hello

You can also execute

 $ dmd -run hello.d

which will simply compile and run without leaving any object files in the directory.

## Considerations
There are however possible choices regarding the compiler you choose. The reference implementation is , but  (D frontend for GCC) and  (LLVM D Compiler) are also available.

As of April 2017 dmd's backend is now FOSS (Boost-licensed). All compilers share the same front-end code and thus have almost identical support for language features (assuming same front-end version).

## Useful libraries and bindings
* DDT - Eclipse plugin for project and code management in D
* Mono-D - MonoDevelop addin for programming in D
* QtD - Qt bindings for D
* GtkD - An object oriented GTK wrapper for D
* Derelict - Bindings for multimedia libraries, focused toward game development
* Deimos - A project that houses a lot of bindings to different C libraries
