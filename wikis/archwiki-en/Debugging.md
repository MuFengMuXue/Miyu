# Debugging

This page is mainly about how to gather more information in connection with bug reports. Even though the word "debug" is used, it is not intended as a guide for how to debug programs while developing.

## Check availability of a core dump
A core dump is a file containing a process's address space (memory) when the process terminates unexpectedly. If the application is compiled in a debug-friendly way, the "core" file can be used to find out where things went wrong.

The location of core dumps may vary depending on the operating system configuration. See core dump to find whether generation of core dump files is enabled on your system and where do they go.

## Segmentation faults
There are several techniques that can be used to figure out what went wrong. Put your detective hat on.

## GDB
 is an ancient and well tested application for debugging applications. See Debugging/Getting traces#Getting the trace for more instructions how to use it to obtain a trace. While running from , you might have to wait for the segfault. Afterwards, post the trace to a pastebin service and include the URL in your bug report.

If you have a "core" file, it can be used together with GDB to get a backtrace:

 $ gdb appname core
 bt full

## Valgrind
Assuming you have an unstripped binary without inlined functions, it is usually a good idea to also run that program through . valgrind is a tool that emulates a CPU and usually shows where things go wrong or provide info in addition to gdb.

 $ valgrind appname

it will provide a lot of helpful debug output if there is a crash. Consider  and  to get even more info.

Alternatively, use:

 $ valgrind --tool=callgrind appname

and run the output through  to graphically explore the functions the program uses. If a program hangs, this makes it easier to pinpoint the location of the error.

## Memory errors
In some cases, it may be necessary to find out if the application handles its memory correctly. This only affects applications written in memory-unsafe languages.
For example, some crashes may be caused by memory errors such as a heap overflow.

Keep in mind that packages on Arch Linux are compiled with additional flags to harden the application, which may influence memory errors. See Arch package guidelines/Security.

## AddressSanitizer
In order for ASan to work, the application must be compiled with  and debugging symbols.

The compiled application will be slower with ASan enabled, but it heavily depends on the software itself, the compiler used (including its version) and the used  value, among other things. If the application is unbearably slow, it is worth trying out different combinations.
An extreme example is that Cataclysm: Dark Days Ahead took 60 minutes to load a simple save with GCC 9 and ASan enabled. Without ASan, the save would take under a minute to load. GCC 14 cut the loading time in half with ASan, but it still remained at 30 minutes, which is unacceptably slow. Clang 18 with ASan did not have that issue and the slowdown was negligible. However, forcing GCC 14 to use  with ASan massively sped up the loading, but it still took a minute to load and was not as fast as clang.

An additional complication was that only GCC 9 was able to trigger the specific bug, a heap overflow. A version compiled with GCC 14 was unable to reproduce the bug. As such, it is important to keep the compiler versions in mind, too.

To find memory errors, simply run the application as normal. ASan will automatically crash the application on things such as a heap overflow or even use-after-free. When this happens, a detailed and helpful trace can be found in the output.
The behavior of ASan can be influenced at runtime via the  environment variable. Additionally, there are compilation flags to alter its behavior.

A common use for this environment variable is to tell ASan to not fatally crash the application when it finds something other than a memory leak:

 ASAN_OPTIONS=halt_on_error=0

Further information can be found at:

* https://github.com/google/sanitizers/wiki/AddressSanitizer
* https://github.com/google/sanitizers/wiki/AddressSanitizerFlags
* https://clang.llvm.org/docs/AddressSanitizer.html

## Valgrind
Valgrind can also be used to detect these behaviors and in contrast to ASan it does not need to be compiled in.
Compared to ASan, it is massively slower and a bit more limited.

In order to find memory errors, invoke Valgrind with:

 $ valgrind --tool=memcheck --track-origins=yes --keep-stacktraces=alloc-and-free application

Also see #Valgrind.

## Missing files or libraries
## Strace
 finds out in detail what an application is actually doing. If an application tries to open a file that is not there, it can be discovered by strace.

For finding which files a program named appname tries to open:

 $ strace -eopen appname

## LD_DEBUG
Setting  gives another overview of what files an application is looking for. For an application named appname:

 $ LD_DEBUG=files appname > appname.log 2>&1

The output will end up in .

For more information, see .

## Readelf
If you get  when running an application, try the following command:

 $ readelf -a /usr/bin/appname | grep interp

(replace  with the location of your executable)

Make sure the interpreter in question (like ) actually exists. Install  if need be.

## Not a binary file
Use  on the executable to get more information:

 $ file /usr/bin/appname

If it says , it is a binary executable. If it says , you know you are dealing with an application written in Python.

If it is a shell script, open up the shell script in a text editor and see (usually at the bottom of the file) if you can find the name of the real application (ELF file). You can then temporarily put "gdb" right in the shellscript, before the name of the executable, for debugging purposes. See the sections about gdb further up. Prefix the command with  if the executable in question needs arguments as well.

For pure shell scripts, you can also use  or .

For Python applications, the output will often say which file and line number the crash occurred at. If you are proficient with Python, you can try to fix this and include the fix in the bug report.

## Report the bug
First check if the bug in question is a packaging bug. If the bug is introduced due to how Arch Linux packages this application, report it to https://gitlab.archlinux.org/groups/archlinux/packaging/-/issues. This also includes issues with libraries or dependencies (e.g if one of them is not built with a specific feature that is needed).
Inspect the PKGBUILD of the package, which is possible with the Arch build system, to see how it gets packaged.
See Bug reporting guidelines#Upstream or Arch? for more information.

If the bug is not related to Arch Linux and is reproducible anywhere else, only report it to upstream. Arch Linux can not magically fix upstream bugs. Reporting it to the Arch bugtracker would not help and might even be counterproductive because it tends to waste time of the bug wranglers.
