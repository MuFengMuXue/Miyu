# Realtime kernel

This article describes the Linux kernel realtime patch set, and some utilities useful for trouble shooting scheduling latencies.

## What is realtime?
Realtime applications have operational deadlines between some triggering event and the application's response to that event. To meet these operational deadlines, programmers use realtime operating systems (RTOS) on which the maximum response time can be calculated or measured reliably for the given application and environment.
A typical RTOS uses priorities. The highest priority task wanting the CPU always gets the CPU within a fixed amount of time after the event waking the task has taken place. On such an RTOS the latency of a task only depends on the tasks running at equal or higher priorities; tasks running at lower priorities may be ignored. On a non-realtime OS (most GNU/Linux distributions running their default kernels), since latencies depend on each process running on the system, it is obviously much harder to ensure deadlines will be met every time, and this difficulty scales nonlinearly with system complexity. Determinism in scheduling becomes yet more difficult to achieve because preemption can be switched off for an arbitrary amount of time. A high priority task wanting to run can thus be delayed indefinitely by lower priority tasks with preemption disabled.

## How does the realtime patch work
The RT-Preempt patch converts Linux into a fully preemptible kernel. This is done through:

* Making in-kernel locking-primitives (using spinlocks) preemptible by reimplementation with rtmutexes.
* Critical sections protected by i.e. spinlock_t and rwlock_t are now preemptible. The creation of non-preemptible sections (in kernel) is still possible with raw_spinlock_t (same APIs like spinlock_t).
* Implementing priority inheritance for in-kernel spinlocks and semaphores.
* Converting interrupt handlers into preemptible kernel threads: The RT-Preempt patch treats soft interrupt handlers in kernel thread context, which is represented by a task_struct like a common user space process. However it is also possible to register an IRQ in kernel context.
* Converting the old Linux timer API into separate infrastructures for high resolution kernel timers plus one for timeouts, leading to user space POSIX timers with high resolution.

## Installation
There are two realtime patched kernels available:  and , which both have a configuration based on the main  kernel package. linux-rt follows the development branch of the -rt patch, while linux-rt-lts tracks a stable branch of the rt patchset.

## Scheduling latency
In the context of the scheduler, latency is the time that passes from the occurrence of an event until the handling of said event.  Often the delay from the firing of an interrupt until the interrupt handler starts running, but could also be from the expiration of a timer, etc.

There can be many varied causes for high scheduling latencies. Some worth mentioning (in no particular order) are: a misconfigured system, bad hardware, badly programmed kernel modules, CPU power management, faulty hardware timers, SMIs and SMT.

When trying to determine a system's maximum scheduling latency, the system needs to be put under load. A busy system will tend to experience greater latencies than an idle one. To sufficiently characterize latencies of interest, it would be prudent to run tests for a long time and under a variety of nominal and worst-case load conditions. Further, since many subsystems such as disks, network devices, USB and graphics may be used sparsely after a system is brought online, care should be taken to characterize latency with these subsystems active as well.

## Latency testing utilities
Understanding latency is non-intuitive. In measuring and interpreting latency, errors are common and very likely to happen even with experienced computer scientists. Popular tools are often incorrect. This talk explains some common pitfalls. There are several tools available to check kernel scheduling latencies, and to track down the causes of latency spikes. One set of tools comes in a package called .

## cyclictest
One of the programs in rt-tests is called cyclictest, which can be used to verify the  maximum scheduling latency, and for tracking down the causes of latency spikes. cyclictest works by measuring the time between the expiration of a timer a thread sets and when the thread starts running again.

Here is the result of a typical test run:

It shows a four CPU core system running one thread (SCHED_FIFO) per core at priority 98, with memory locked, the system is also under a high load due to running hackbench in a separate terminal.  What is most interesting is the max scheduling latency detected, in this case 32 usecs on core 3.

See  man page.

## hackbench
An idle kernel will tend to show much lower scheduling latencies, it is essential to put some load on it to get a realistic result. This can be done with another utility in the rt-tests package called hackbench. It works by creating multiple pairs of threads or processes, that pass data between themselves either over sockets or pipes. To make it run longer add the -l parameter: .

See  man page.

## hwlatdetect
hwlatdetect can be used to detect SMIs taking an inordinate time, thus introducing latency by blocking normal kernel execution.  It consists of a kernel module (present in both linux-rt and linux-rt-lts), and a python script to launch the process and report the results back to the user. To check if the system uses NMIs run the following command:

The hwlatdetect kernel module works by turning everything running on the CPUs off through the stop_machine() call.  It then polls the TSC (Time Stamp Counter) looking for gaps in the generated data stream.  Any gaps indicates that it was interrupted by a NMI, as they are the only possible mechanism (apart from a broken TSC implementation). To run the program for 120 secs, with  a detection threshold of 15 usecs, execute the following:

The result shows 16 NMIs detected that exceeded the 15 usecs threshold specified, the maximum latency detected was 21 usecs.

See  man page.
