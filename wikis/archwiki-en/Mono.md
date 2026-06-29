# Mono

From Wikipedia:

:Mono is a project to create a .NET Framework-compatible set of tools including, among others, a C# compiler and a Common Language Runtime.

## Installation
Install the  package.

If you need VisualBasic.Net support you have to install the VisualBasic.Net interpreter with the package .

## Running Mono applications
You can execute Mono binaries by calling  manually:

 $ mono programsname.exe

You can also execute Mono binaries directly, just like native binaries:

 $ chmod 755 exefile.exe
 $ ./exefile.exe

## Testing Mono
Make a new file:
{{hc|test.cs|
using System;

public class Test {
 public static void Main(string[ args) {
  Console.WriteLine("Hello World!");
 }
}
}}
Then run:

## Development
OmniSharp provides .NET/Mono development plugins/integrations for several editors, including Vim, Emacs, and Visual Studio Code.

Alternatively, you can install the  IDE. If you install Rider not from AUR, you would need to install , as recent Rider versions dropped support of xbuild in favour of MSBuild from net-core.

If you want the API documentation browser and some testing and development tools you have to install .

## Troubleshooting
## I get an error when I try to run Mono binaries directly: "cannot execute binary file"
The binfmt_misc handler for Mono has not yet been set up, as explained in detail on the Mono Project website.

To fix this, restart the  service.

## I get an TLS handshake (or similar certificate based) error
This can be caused by either certificates missing from Mono's certificate store, or stale broken certificates remaining in Mono's certificate store.

If possible, ensure that the system certificate store is in good order by running  or similar to replicate the failing request outside Mono.

*  synchronises the mono store with the system store, adding missing certificates.
* To remove broken certificates (i.e., if above did not help), remove the directory , then re-run
* As last resort, the older tool  bypasses the system certificate store and directly downloads Mozilla's trust store. This again does not remove broken certificates, and can cause other problems if you rely on private CAs.

Both  and  are part of the mono package.
