# Debugging/Profiling

Due to performance regressions, unoptimized new features or simply unknown factors affecting performance, it may be necessary to profile an application. According to Wikipedia:

:In software engineering, profiling ("program profiling", "software profiling") is a form of dynamic program analysis that measures, for example, the space (memory) or time complexity of a program, the usage of particular instructions, or the frequency and duration of function calls. ... Profilers may use a number of different techniques, such as event-based, statistical, instrumented, and simulation methods.

Statistical profilers periodically sample resources such as the program's callstack or the CPU's hardware performance counters to build an approximate profile of the running program. Instrumented profilers are more invasive, often requiring recompilation to instrument the program to record events for a verbose trace of the running program. Although profiling and tracing are distinct,many profilers (including perf_events) integrate both data collection methods.

See List of applications/Utilities#Profilers and trace recorders for additional software not discussed on this page.

## Profiling with perf
The Linux kernel has a built-in perf_events subsystem (herein perf) for profiling code at the kernel and/or user level, with support for adding low-overhead tracepoints.

To get started, install the  userspace utility.

## Getting debug symbols
In order to get interpretable results, debugging symbols for the application you are debugging are mandatory. See Debugging/Getting traces#Manually getting debug info. perf does not support debuginfod yet and thus the debugging symbols must be obtained manually.

Should the application be profiled or otherwise debugged without debugging symbols, there will only be [https://xkcd.com/138/ pointers instead of actual function names, which are quite useless.

## Usage
Just as with GDB, the application will be run within perf.

 $ perf record -g -- command

This will record the data to . After the program is finished, display the results with:

 $ perf report --stdio

For a prettier display, consider using .

If reporting a bug to upstream, submit the  file.
