# Allegro

Allegro is, as their website states,

:a cross-platform library mainly aimed at video game and multimedia programming. It handles common, low-level tasks such as creating windows, accepting user input, loading data, drawing images, playing sounds, etc. and generally abstracting away the underlying platform. However, Allegro is not a game engine: you are free to design and structure your program as you like.

## Installation
Install the  package.

There is also a package for the legacy version of Allegro, , which you can use for source which requires it.

## Use
Once installed, include the necessary base header into necessary source files:

If your main function is inside a C++ file, then it must have this signature:

## Troubleshooting
* A common first mistake is to forget to link against the Allegro libraries. For an overview, use .

* Another trap for young players is to forget to include and initialise the necessary modules. Each module is a header, which needs to be included in the source file. Make sure you initialised it with the correct command and linked against the module, see above. For the exact details, refer to the manual.
