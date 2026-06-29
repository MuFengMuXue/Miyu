# Faction

Faction is a C library for test-driven software development.

## Installation
Install the  package.

## Usage
The library provides several C macros to make writing tests quicker.

* FI represents Faction Initialization
* FT denotes a Faction Test
* FC represents Faction Close

Using the FT macro, three fields are required.

* AUTHORS() takes a comma-separated list of double-quotation surrounded author names
* SPEC() takes a single double-quotation surrounded test specification description
* A C boolean expression (just like when using C assert macros)

Convention dictates that Faction tests are to be written at the bottom of the source file containing the code that will be tested. Tests are to be surrounded by a FACTION macro guard (see below example) so that they can be enabled/disabled at compile time. C compilers such as the GNU C Compiler (GCC) offer a way to enable macros on the command-line (i.e. the  flag)

## Example
 /* This is the function to be tested */
 int
 increment(int input)
 {
    return (input + 1);
 }

 #ifdef FACTION
 #include
 #include
 FI

   FT(
     AUTHORS( "timetoplatypus" ),
     SPEC( "increment() returns 1 when given 0" ),
     increment(0) == 1
   );

   FT(
     AUTHORS( "timetoplatypus" ),
     SPEC( "increment() returns 0 when given the largest integer value" ),
     increment(INT_MAX) == 0
   );

 FC
 #endif

This can be compiled using

## Modes
There are two modes that Faction can compile in: minimal mode and extended mode.

The above example compiles Faction in minimal mode. A minimal compilation has exactly three library dependencies: stdlib, stdio, and getopt. An extended compilation has additional dependencies, including some functions that are only available through the GNU feature test macro.

So, to compile in extended mode, simply define the GNU feature test macro at the top of the file. For instance, the previous example modified to be compiled in extended mode would look like this:

{{hc|head=
#ifdef FACTION
#define _GNU_SOURCE
#endif
| output=
/* This is the function to be tested */
increment(int input)
{
  return (input + 1);
}

#ifdef FACTION
#include
#include
FI

  FT(
    AUTHORS( "timetoplatypus" ),
    SPEC( "increment() returns 1 when given 0" ),
    increment(0) == 1
  );

  FT(
    AUTHORS( "timetoplatypus" ),
    SPEC( "increment() returns 0 when given the largest integer value" ),
    increment(INT_MAX) == 0
  );

FC
#endif
}}

## Extended Mode Features
In extended mode,

* the output can be optionally mirrored to a user-specified log file using the  flag at runtime.
* the results table will dynamically resize to the width of the terminal being used. Otherwise, it defaults to a 78 character width.
