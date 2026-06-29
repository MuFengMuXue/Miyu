# Scala

From Wikipedia:

:Scala is an object-functional programming and scripting language for general software applications. Scala has full support for functional programming (including currying, pattern matching, algebraic data types, lazy evaluation, tail recursion, immutability, etc.) and a very strong static type system. This allows programs written in Scala to be very concise and thus smaller in size than most general purpose programming languages. Many of Scala's design decisions were inspired by criticism over the shortcomings of Java.

## Installation
Install the  package. Additionally you can install the packages  and/or  for further reference.

Since Scala runs on the JVM (Java Virtual Machine), you will need a fully functional Java Runtime Environment (JRE) in order to execute or compile your programs.

For scala3 (which is also known as dotty), you can install  or . Note that scala3 is incompatible with scala 2.13 or older.

## Build tools
Most build tools are available:

*
*
*
*

## Scala CLI
As an alternative to using build tools or the compiler directly, you can use Scala CLI for building and distributing your software.

Install the  package.

## Usage and IDEs
Just as in other programming languages like Python, you can interact with an interpreter

 $ scala

 Welcome to Scala version 2.*.* (OpenJDK Server VM, Java 1.*.*).
 Type in expressions to have them evaluated.
 Type :help for more information.

 scala>

as well as simply compile and run your programs from the command line.

 $ scalac HelloWorld.scala
 $ scala HelloWorld

Many different IDEs such as Eclipse or Netbeans offer support for Scala. Alternatively, consider  or . You can also download an IDE that is optimized for Scala and also based on Eclipse directly from the official Scala Website.
