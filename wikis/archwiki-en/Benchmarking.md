# Benchmarking

Benchmarking is the act of measuring performance and comparing the results to another system's results or a widely accepted standard through a unified procedure. This unified method of evaluating system performance can help answer questions such as:

* Is the system performing as it should?
* What driver version should be used to get optimal performance?
* Is the system capable of doing task x?

Many tools can be used to determine system performance, the following provides a list of tools available.

## Standalone tools
## UnixBench
Install , to run the benchmark run ubench.

See also:

* https://github.com/kdlucas/byte-unixbench
* https://github.com/kdlucas/byte-unixbench/blob/master/UnixBench/USAGE

## interbench
interbench is an application designed to benchmark interactivity in Linux. It is designed to measure the effect of changes in Linux kernel design or system configuration changes such as CPU, I/O scheduler and filesystem changes and options.

interbench is available in the AUR: .

See also:

* Realtime process management
* Advanced traffic control
* Linux-pf

## fio
 (Flexible I/O Tester) is a utility that can simulate various workloads such as several threads issuing reads using asynchronous I/O. Fio spawns a number of threads or processes doing a particular type of I/O action as specified by the user. Docs

Example usage:

 # fio --filename=/mnt/test.fio --size=8GB --direct=1 --rw=randrw --bs=4k --ioengine=libaio --iodepth=256 --runtime=120 --numjobs=4 --time_based --group_reporting --name=iops-test-job --eta-newline=1

## ttcp
ttcp (Test TCP) measures point-to-point bandwidth over any network connection. The program must be provided on both nodes between which bandwidth is to be determined.

Various flavors of ttcp can be found in the AUR:

*
*

## iperf
iperf is an easy to use point-to-point bandwidth testing tool that can use either TCP or UDP. It has nicely formatted output and a parallel test mode.

 can be installed, or a different version of iperf is available with .

## time
The  command provides timing statistics about the command run by displaying the time that passed between invocation and termination.  contains the  command and some shells provide  as a builtin command.

 $ time tar -zxvf archive.tar.gz

## hdparm
Storage media can be benchmarked with hdparm (). Using hdparm with the  switch, one can time sequential reads. This method is independent of partition alignment!

## gnome-disks
There is a graphical benchmark called gnome-disks contained in the  package that will give min/max/ave reads along with average access time and a nice graphical display. This method is independent of partition alignment!

 # gnome-disks

Users will need to navigate through the GUI to the benchmark button ("More actions..." > "Benchmark Volume...").

## KDiskMark
 is an HDD and SSD benchmark tool with a very friendly graphical user interface. KDiskMark with its presets and powerful GUI calls Flexible I/O Tester and handles the output to provide an easy to view and interpret comprehensive benchmark result.

## systemd-analyze
 $ systemd-analyze plot > boot.svg

Will plot a detailed graphic with the boot sequence: kernel time, userspace time, time taken by each service.

## dd
The dd utility can be used to measure both reads and writes. This method is dependent on partition alignment! In other words, if you failed to properly align your partitions, this fact will be seen here since you are writing and reading to a mounted filesystem.

First, enter a directory on the SSD with at least 1.1 GB of free space (and one that gives your user wrx permissions) and write a test file to measure write speeds and to give the device something to read:

Next, clear the buffer-cache to accurately measure read speeds directly from the device:

Now that the last file is in the buffer, repeat the command to see the speed of the buffer-cache:

Finally, delete the temp file

 $ rm tempfile

## dcfldd
Dcfldd does not print the average speed in MB/s like good old dd does but with time you can work around that.

Time the run clearing the disk:

Calculate MiB/s by dividing the output of the dcfldd command (in MiB; note that dcfldd displays byte as 'b') by the time in seconds. For this example: 75776 MiB / (16.4 * 60 s) = 77.0 MiB/s.

## 7z
7z benchmark command can be used to measure the CPU speed in MIPS and also to check RAM for errors. Just install 7-Zip and run the command below. More detailed information can be found at $ 7z b

## peakperf
 is a microbenchmark that achieves peak performance on x86_64 CPUs. Some issues may reduce the performance provided by your CPU, like CPU cooling. With peakperf you can check if your CPU provides the full power it is capable of doing.

You can calculate the performance (measured in GFLOP/s) you should get using your CPU (see [https://github.com/Dr-Noob/peakperf#understanding-the-microbenchmark) and compare it with the performance that peakperf gives you. If both values are the same (or very similar), your CPU behaves as it should.

## cryptsetup
cryptsetup benchmark can be used to measure the speed of various cryptographic algorithms (ciphers).

 $ cryptsetup benchmark

## kcapi
 allows user-space to access the Linux kernel crypto API. The package provides several binaries, in particular kcapi-speed to benchmark hash, symmetric ciphers, AEAD ciphers, hash-based and cipher-based rng.

To list available ciphers:
 $ kcapi-speed -l
Usage example of benchmarking AES using AES-NI in ECB mode 128bit keys tested for 3 seconds and using 1024 blocks to process
 $ kcapi-speed -c 'AES(AESNI) ECB(ASM) 128' -b 1024 -t 3
Output for both decription and encryption:
 AES(AESNI) ECB(ASM) 128 |d|   16384 bytes|                5.41 GB/s|330631 ops/s
 AES(AESNI) ECB(ASM) 128 |e|   16384 bytes|                5.47 GB/s|334185 ops/s

## Software suites
## Bonnie++
 is a C++ rewrite of the original Bonnie benchmarking suite is aimed at performing several tests of hard drive and filesystem performance.

See also:

* Author's site
* Wikipedia:Bonnie++

## IOzone
IOzone is useful for performing a broad filesystem analysis of a vendor’s computer platform.

This program is available in the AUR: .

The following can approximate the output of several tests of CrystalDiskMark, a popular Windows benchmarking utility:
* Sequential 1MiB read/write:
* Sequential 128KiB read/write:
* Random 4KiB read/write:

Results will be in KiB/s so divide by 1024 to get them in MiB/s.

See also BBS Article: iozone to evaluate I/O schedulers... results NOT what you would expect!.

## HardInfo
 can gather information about your system's hardware and operating system, perform benchmarks, and generate printable reports either in HTML or in plain text formats. HardInfo performs CPU and FPU benchmarks and has a very clean GTK-based interface.

## Phoronix Test Suite
The Phoronix Test Suite is the most comprehensive testing and benchmarking platform available that provides an extensible framework for which new tests can be easily added. The software is designed to effectively carry out both qualitative and quantitative benchmarks in a clean, reproducible, and easy-to-use manner.

The Phoronix Test Suite is based upon the extensive testing and internal tools developed by Phoronix.com since 2004 along with support from leading tier-one computer hardware and software vendors. This software is open-source and licensed under the GNU GPLv3.

Originally developed for automated Linux testing, support to the Phoronix Test Suite has since been added for OpenSolaris, Apple macOS, Microsoft Windows, and BSD operating systems. The Phoronix Test Suite consists of a lightweight processing core (pts-core) with each benchmark consisting of an XML-based profile and related resource scripts. The process from the benchmark installation, to the actual benchmarking, to the parsing of important hardware and software components is heavily automated and completely repeatable, asking users only for confirmation of actions.

The Phoronix Test Suite interfaces with OpenBenchmarking.org as a collaborative web platform for the centralized storage of test results, sharing of test profiles and results, advanced analytical features, and other functionality. Phoromatic is an enterprise component to orchestrate test execution across multiple systems with remote management capabilities.

This suite can be installed with the package . There is also a developmental version available with .

## S
S, an I/O Benchmark Suite, is a small collection of scripts to measure storage I/O performance.

Download or clone the project, install its dependencies and run it as root (privileges needed to change disk scheduler).

## s-tui
s-tui is an aesthetically pleasing and useful curses-style interface that shows graphs of CPU frequency, utilization, temperature, power consumption and has a built in stress tester.

## sysbench
 is an all-round multi-threaded benchmark tool. Written in C and Perl, it can be used in CLI directly to benchmark filesystem, DRAM, CPU, thread-based scheduler and POSIX mutex performance. Or it can be used as Lua script interpreter to benchmark any arbitrarily complex workload. It provides a collection of scripts for database benchmarks.

## Geekbench
 is a proprietary cross-platform suite of benchmarks that measures processor, GPU and memory performance by simulating a variety of real-world workloads, and provides scores that can be saved on Geekbench's website and compared (within the same version) against other systems, both your own and others'.

Geekbench is not useful as an independent objective test of performance, since the scores it give do not relate to any one individual task or how well a PC will perform at one or any of them; however it can be useful as a rough indication of a computer's performance relative to others, or the same computer on different operating systems/distros or under different conditions. It is commonly used in CPU benchmark comparison charts for this reason.

## Flash media
Performance characteristics can be measured quantitatively using . Sustained read and write values can, but often do not, correlate to real-world use cases of I/O heavy operations, such as unpacking and writing a number of files on a system update. A relevant metric to consider in these cases is the random write speed for small files.

The example invocation tests a 10MiB file using a 4KiB record size:

## Graphics
## Basemark GPU
Basemark GPU is an evaluation tool to analyze and measure graphics API (OpenGL 4.5, OpenGL ES 3.1, Vulkan and Microsoft DirectX 12) performance across mobile and desktop platforms. Basemark GPU targets both Desktop and Mobile platforms by providing both High Quality and Medium Quality modes. The High-Quality mode addresses cutting-edge Desktop workloads while the Medium Quality mode addresses equivalent Mobile workloads.

If you are using AMD GPU and have several vulkan implementations installed simultaneously, in the Test page you will see them as separate GPUs in Graphics Device dropdown list.

Basemark GPU is available in  package.

## Blender-benchmark
Blender-benchmark will gather information about the system, such as operating system, RAM, graphics cards, CPU model, as well as information about the performance of the system during the execution of the benchmark. After that, the user will be able to share the result online on the Blender Open Data platform, or to save the data locally.

Blender-benchmark is available in the  package.

## Furmark
 displays a very graphically-intensive image and the frame rate that results. While it can be used as a benchmark for GPU performance, its main purpose is instead as a stress test, intended to maximise GPU usage - this makes it useful for assessing system stability under full load and also for assessing the thermal performance of a graphics card.

## GFXBench
GFXBench is a high-end graphics benchmark that measures mobile and desktop performance with next-gen graphics features across all platforms. As a true cross-API benchmark, GFXBench supports all the industry-standard and vendor-specific APIs including OpenGL, OpenGL ES, Vulkan, Metal, DirectX/Direct3D and DX12.

Vulkan API tests are currently under development and are only available for their corporate partners.

GFXBench is available in  package.

## glmark2
glmark2 is an OpenGL 2.0 and ES 2.0 benchmark.

glmark2 is available in  package.

## glxgears
glxgears is a popular OpenGL test that renders a very simple OpenGL performance and outputs the frame rate. Though glxgears can be useful as a test of direct rendering capabilities of the graphics driver, it is an outdated tool that is not representative of the current state of GNU/Linux graphics and overall OpenGL possibilities. glxgears only tests a small segment of the OpenGL capabilities that might be used in a game. Performance increases noted in glxgears will not necessarily be realized in any given game. See here for more information.

glxgears can be installed via the  and  (for multilib) packages.

## GpuTest
GpuTest is a cross-platform (Windows, Linux and Mac OS X) GPU stress test and OpenGL benchmark. GpuTest comes with several GPU tests including some popular ones from Windows' world (FurMark or TessMark).

GpuTest is available in  package.

## intel-gpu-tools
intel-gpu-tools gives you some top-like info for the integrated GPU. This can be quite useful in diagnosing GPU acceleration issues.

To use it, install the  package.

## MangoHud
See MangoHud.

## Unigine Engine
Unigine corp. has produced several modern OpenGL benchmarks based on their graphics engine with features such as:

* Per-pixel dynamic lighting
* Normal & parallax occlusion mapping
* 64-bit HDR rendering
* Volumetric fog and light
* Powerful particle systems: fire, smoke, explosions
* Extensible set of shaders (GLSL / HLSL)
* Post-processing: depth of field, refraction, glow, blurring, color correction and much more.

Unigine benchmarks have found recent usage by those looking to overclock their systems. Heaven especially has been used for initial stability testing of overclocks.

These benchmarks can be found in AUR:

*  (2007)
*  (2008)
*  (2009)
*  (2013)
*  (2017)

## vkmark
vkmark is an extensible Vulkan benchmarking suite with targeted, configurable scenes.

vkmark is available in  package.

## xmrig
 is a high performance, open source, cross platform RandomX, KawPow, CryptoNight and GhostRider unified CPU/GPU miner and RandomX benchmark.

## For Radeon GPUs
Radeon GPU users running the open-source  driver, both  and  are required. To stress-test the GPU:

 $ xmrig --stress --no-cpu --opencl
