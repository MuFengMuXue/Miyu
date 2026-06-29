# AWK

AWK is a small programming language designed for text processing. Its name is derived from the surnames of its authors: Alfred Aho, Peter Weinberger, and Brian Kernighan. The language is standardized and widely available on Unix-like systems.

## Installation
On Arch, the  command is provided by , which is installed by default, with native Unicode support and a load of extrafeatures.

## Alternative implementations
Like many other core utilities, there are several more-or-less compliant implementations available:

*
*
*
*

## Troubleshooting
## Assignment to  variable via  option does not preserve in runtime
Although undocumented, it appears that many implementations will reset the  variable internally after processing the variable assignment of  options specified on command line. Therefore, to get desired value of  variable in runtime (e.g.  code blocks), it's required to set the variable in code block directly:

 BEGIN {
   ARGC=1;
   ...
 }
