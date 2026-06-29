# Go

Go is an open source programming language supported by Google.

From the Go documentation:

* it is a statically typed, compiled language that feels like a dynamically typed, interpreted language:
** it compiles to machine code yet has the convenience of garbage collection and the power of run-time reflection;
** its concurrency mechanisms make it easy to write programs that get the most out of multicore and networked machines, while its novel type system enables flexible and modular program construction.

## Installation
Install the  package, which includes the standard Go compiler and other development tools. See the  command documentation for a list of included subcommands.

## Alternative compilers
## gccgo
A frontend for GCC called gccgo is provided by the  package. gccgo may produce faster binaries than the standard ("gc") compiler in some cases and can target additional operating systems and architectures. In practice, gc produces faster binaries than gccgo for almost all workloads.

## TinyGo
TinyGo is an LLVM based compiler designed to produce very small binaries for embedded systems and WebAssembly. It is provided by the  package.

## Tools
The following packages provide developer tools for Go:

*
*
*
*
*
*
*
*
*

You can also install and run developer tools within modules using  and . See the official documentation on tool dependencies for instructions.

## Install directory
The  command installs Go executables in the directory named by the  environment variable.  defaults to , or  if the  environment variable is not set.

For convenience, add the bin subdirectory to :

 $ export PATH="$PATH:$(go env GOBIN):$(go env GOPATH)/bin"

See How to Write Go Code and  for more information.

## Tips and tricks
## Compiling source code
You can write a Hello World program as follows:

{{hc|hello.go|
package main

import "fmt"

func main() {
    fmt.Println("Hello, Arch!")
}
}}

Then run it with the go tool:

Compilation with the standard compiler (same as ):

 $ go build hello.go

Compilation with gccgo (same as ):

 $ gccgo hello.go -o hello

Compilation with tinygo:

 $ tinygo build -o hello ./hello.go

## Cross compiling to other platforms
The standard compiler can natively cross-compile to a number of platforms. The procedure varies depending on whether the source code calls C code using cgo.

## Without cgo
If cgo is not required for your build, then simply specify the target OS and architecture as environment variables to :

 $ GOOS=linux GOARCH=arm64 go build .

See the official documentation for the valid combinations of  and .

## With cgo
If cgo is required for your build, you have to provide the path to your C/C++ cross-compilers, via the / environment variables.

Say you want to cross-compile for  and .

You need first to install the  cross-compiler.

Here is a sample program that requires cgo, so that we can test the cross-compilation process:

{{hc|hello.go|
package main

// #include
// void hello() { puts("Hello, Arch!"); }
import "C"

func main() {
    C.hello()
}
}}

Then, you can cross-compile it like this:

 $ GOOS=linux GOARCH=arm64 CGO_ENABLED=1 CC=/usr/bin/aarch64-linux-gnu-gcc go build hello.go

You can check that the architecture of the generated binary is actually aarch64:

 $ file hello
 hello: ELF 64-bit LSB executable, ARM aarch64, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux-aarch64.so.1, BuildIDfor GNU/Linux 3.7.0, not stripped

If you copy  to a suitable host, you can test-run it:

 [alarm@rpi3 ~$ uname -a
 Linux alarm 5.3.8-1-ARCH #1 SMP Tue Oct 29 19:31:23 MDT 2019 aarch64 GNU/Linux
 ~$ ./hello
 Hello, Arch!

## Using an alternate Go module mirror
By default, Go uses Google's service proxy.golang.org as a module mirror.

If an alternate mirror is desired, it can be changed with the environment variable , for example:

 $ export GOPROXY=https://goproxy.io/

A number of public module mirrors are available, see for example: Go and Hugo Proxy Servers.

## Troubleshooting
## JetBrains Go Plugin
If you are using a JetBrains IDE and the Go plugin cannot find your Go SDK path, you might be using an incompatible package. Remove the gcc-go package and replace it with go. If your  is set, the IDE should now be able to find your Go SDK at .
