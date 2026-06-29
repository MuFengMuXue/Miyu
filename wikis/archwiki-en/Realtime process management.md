# Realtime process management

This article provides information on prioritizing process threads in real time, as opposed to at startup only. It shows how you can control CPU, memory, and other resource utilization of individual processes, or all processes run by a particular group.

While many recent processors are powerful enough to play a dozen video or audio streams simultaneously, it is still possible that another thread hijacks the processor for half a second to complete another task. This results in short interrupts in audio or video streams. It is also possible that video/audio streams get out of sync. While this is annoying for a casual music listener; for a content producer, composer or video editor this issue is much more serious as it interrupts their workflow.

The solution is to run time-sensitive processes in realtime. In linux, this means changing the process to a realtime scheduler, like  or . See  for descriptions of these schedulers.

## Configuration
On Arch Linux, system, group and user-wide configuration can be achieved using PAM and systemd.

The  package group provides additional tools to modify the realtime scheduling policies of IRQs and processes.

## Configuring PAM
The  file provides configuration for the  PAM module, which sets limits on system resources (see ).

There are two types of resource limits that  provides: hard limits and soft limits. Hard limits are set by  and enforced by the kernel, while soft limits may be configured by the user within the range allowed by the hard limits.

Installing the package  and adding the user to the  group, provides reasonable default values (e.g. relevant for Professional audio).

## Configuring systemd services
Processes spawned by systemd system services need to specifically set up equivalents to . Further information can be found in the sections  and  in .

## Usage
To run in realtime, a process running in the  group must set  to any value above 0, then change to a realtime scheduler, like  or . Here is an example:

 #include
 #include
 #include

 void realtime()
 {
     struct rlimit rl;
     assert(getrlimit(RLIMIT_RTPRIO, &rl) == 0);
     assert(rl.rlim_max != 0);
     rl.rlim_cur = rl.rlim_max;
     assert(setrlimit(RLIMIT_RTPRIO, &rl) == 0);

     assert(sched_setscheduler(0, SCHED_FIFO, &(struct sched_param){
             .sched_priority = rl.rlim_cur
         }) != -1);
 }

Again,  must be above 0 for the process to be able to change its scheduler. This is why  raises the  limit to 98 for all processes in the  group. See  for more.

## Using chrt
To do this automatically, or in case you are running somebody else's software, you can use . Here is an example of starting  in realtime under the  scheduler:

 $ chrt --fifo 98 ls -al

This shouldn't normally be required. Applications that need to run in realtime, like , normally set their schedulers all on their own.

## Hard and soft realtime
Realtime is a synonym for a process which has the capability to run
in time without being interrupted by any other process. However, cycles can occasionally be dropped despite this. Low power supply or a process with higher priority could be a potential cause. To solve this problem, there is a scaling of realtime quality. This article deals with soft realtime.  Hard realtime is usually not so much desired as it is needed. An example could be made for car's ABS (anti-lock braking system). This can not be "rendered" and there is no second chance.

## Tips and tricks
## PAM-enabled login
PAM is installed and configured on default Arch Linux installations. Nearly all display managers are pam-enabled, too. You can check which modules use  with the following command:

 $ grep pam_limits.so /etc/pam.d/*

On a default installation, only two files use the module directly:

 is included by other pam-aware applications. You can further search :

 $ grep system-auth /etc/pam.d/*

In the default configuration this shows which applications are using  and thus . For example

This covers both graphical and console login.

## Checking Limits
In Bash, use  (see ) to check limits, for example the  limit can be checked as follows:

 $ ulimit -r
 98

This is the value configured by .
