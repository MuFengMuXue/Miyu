# Stress testing

Stress testing is the process of running various work loads on a computer to assess its stability. This is often used to reliably check the stability of overclocked/undervolted hardware and monitor the thermal behavior of the system (e.g. maximum temperatures, throttling, noise levels). There are several programs available to stress test various parts of the system such as CPU, GPU, RAM, and storage, using different types of work loads.

## Stress testing tasks
The table below lists some stress testing software based on the kind of test and the overall intensity of the work load. It is important to stress test using mixed loads to verify stability under many use cases.

{| class="wikitable" align="center"
|-
! Work load !! Tested hardware1 !! Task !! Description
|-
| rowspan="4"
|-
| CPU, storage || Updating patches || Custom script Refreshing hundreds of kernel patches in the OpenWRT project. See #Updating patches for OpenWRT.
|-
| CPU, storage || Writing a disk image || See #Writing to an image file.
|-
| RAM || Memory stressing || See #Memtest86+.
|-
| rowspan="5"
|-
| CPU, RAM, storage || Compilation || Parallel compilation is a good way to stress test the CPU. See #GCC.
|-
| CPU, RAM || Video encoding || , , , etc. can be used to encode video. See #Video encoding.
|-
| CPU, GPU, RAM || Cryptocurrencies mining ||  is a CPU/GPU mine which uses different cryptocurrency mining algorithms to generate load on the GPU for stability and temperature testing. See Benchmarking#xmrig.
|-
| GPU || 3D rendering ||  is a GPU benchmark that runs in a loop. It is a decent stress test for GPUs. See Benchmarking#Unigine Engine.
|-
| rowspan="6"
| CPU, RAM, storage || Synthetic stressing ||  is a simple CPU, memory, I/O, and disk workload generator implemented in C. See #stress.
|-
| CPU, RAM || Prime numbers calculation ||  factors large numbers and is an excellent way to stress CPU and memory. See #MPrime.
|-
| CPU || Algebra calculation ||  - Linpack makes use of the BLAS (Basic Linear Algebra Subprograms) libraries for performing basic vector and matrix operations and is an excellent way to stress CPUs for stability. See #Linpack.
|-
| CPU || Pi decimals calculation ||  Systester is a multithreaded piece of software capable of deriving values of pi out to 128,000,000 decimal places. It has built in check for system stability. See #Systester.
|-
| RAM || Memory stressing ||  is a memory interface test.
|-
| CPU || Various ||  A multi-function stress-testing utility. Written in Rust.
|-
|}

* 1 The main target of the test, virtually all testing will also involve the CPU and RAM to some extent.
* 2 Light tests do not push the components very hard (in terms of power/heat limits). These tests are still useful to test how the hardware behaves in lower power levels (P states), in particular for undervolted systems.
* 3 Realistic tests are based on real world workloads.
* 4 Synthetic tests are explicitly designed to torture the hardware as much as possible and may not be representative of real-world workloads.

## Updating patches for OpenWRT
A good stability test of a low load workload is to run through updating the patch sets in the OpenWRT project. Follow these steps.

 $ git clone --depth 1 https://github.com/openwrt/openwrt.git
 $ cd openwrt
 $ mkdir -p staging_dir/host/bin
 $ cp /usr/bin/sed ./staging_dir/host/bin
 $ curl -Os https://raw.githubusercontent.com/KanjiMonster/maintainer-tools/master/update_kernel.sh
 $ chmod +x update_kernel.sh
 $ ./update_kernel.sh -v -u 6.6

## stress
 performs a loop that calculates the square root of a random number in order to stress the CPU. It can run simultaneously several workers to load all the cores of a CPU for example. It can also generate memory, I/O or disk workload depending on the parameters passed. The FAQ provides examples and explanations.

To spawn 4 workers working on calculating a square root, use the command:

 $ stress --cpu 4

## s-tui
 is terminal-based CPU stress and monitoring utility. It can both monitor CPU usage and temperatures and can also stress the CPU. It is a one stop shop tool where you can see all the information needed in one single screen, with a terminal graphical interface.

## MPrime
MPrime (also known as Prime95 in its Windows and MacOS implementation) is recognised universally as one de facto measure of system stability. MPrime under torture test mode will perform a series of very CPU intensive calculations and compare the values it gets to known good values.

The Linux implementation is called .

To run mprime, simply open a shell and type "mprime":

 $ mprime

When the software loads, simply answer 'N' to the first question to begin the torture testing:

There are several options for the torture test (menu option 16).

# Smallest FFTs to test the CPU L1/L2 (high CPU stress)
# Small FFTs to test the CPU L1/L2/L3 (maximum CPU stress)
# Large FFTs to test the memory controller and RAM (medium CPU stress)
# Blend is the default and constitutes a hybrid mode which stresses the CPU and RAM.

The "Customize settings (N)" prompt allows you to customize settings such as FFT size range and memory use. The default for Large and Blend is to use about 90% of the current amount of available memory, and to alternate between in-memory FFT and in-place FFT.

Errors will be reported should they occur both to stdout and to  for review later. Many do not consider a system as 'stable' unless it can run the Large FFTs without error for a 24 hour period. (The stdout is more useful as it includes information on which worker produced the error, so consider using  or  to save the stdout. By default, each core is assigned one worker, so weak cores can be easily identified.)

Example ; note that the two runs from 26-June indicate a hardware failure. In this case, due to insufficient vcore to the CPU:

## Linpack
 makes use of the BLAS (Basic Linear Algebra Subprograms) libraries for performing basic vector and matrix operations. It is an excellent way to stress CPUs for stability (only Intel CPUs are supported). After installation, users should copy  to  and adjust it according to the amount of memory on the system.

## Systester
 (aka SuperPi for Windows) is available in both CLI and GUI version. It tests system stability by calculating up to 128 millions of Pi digits and includes error checking. Note that one can select from two different calculation algorithms: Quadratic Convergence of Borwein and Gauss-Legendre. The latter being the same method that the popular SuperPi for Windows uses.

A CLI example using 8 threads is given:

 $ systester-cli -gausslg 64M -threads 8

## Memtest86+
Use MemTest86 (proprietary) or Memtest86+ (GPL) to test your memory (RAM).

* The GPL version is available on the Arch Linux install image. It can be installed:
** for EFI systems with ,
** or for BIOS systems with .
* The proprietary version does not support BIOS. Install it with .
* After installation, its users can update GRUB; it will auto-detect the package and allow users to boot directly to it.
* Users of systemd-boot must manually configure a boot loader entry.

## Writing to an image file
A good stability test under a low load workload is using  to format an image. This can be a physical disk or a loop mounted image. The script below uses mounted image and cycles through each core one-by-one. Note that you should adjust the variables in the top of script to match your system. By default the script will run the command just once per core. It can be easily customised to run on known-weak cores rather than scanning all core 0 through n by altering the for loop. Run the script as root.

{{hc|format-test.sh|
#!/bin/bash

# define the path to store the image, recommended to be a tmpfs mounted location to avoid read/writes
img=/scratch/image.img

# define the mount point
mnt=/mnt/loop

# size of time arg to pass to truncate, make sure you select something less than the free memory on the system
# see truncate --help for available options
size=40G

# defaults to 1 less than the number of virtual cores, manually redefine if desired
max=$(($(nproc) - 1))

if  ! -f $img ; then
  truncate -s $size $img
  mkfs.ext4 $img
   -d $mnt  || mkdir -p $mnt
  if ! mountpoint -q $mnt; then
    mount -o loop $img $mnt || exit 1
  fi
fi

for i in $(eval echo "{0..$max}"); do
  echo "using core $i of $max"
  taskset -c "$i" time dd if=/dev/zero of=$mnt/zerofill status=progress
done

umount $mnt
rm $img
}}

## GCC
Parallel compilation using GCC (or other compilers) will generate a heavy load on the CPU and memory. To avoid I/O bottlenecking, compile on an SSD or in a tmpfs.

A good example would be compiling the kernel: see Kernel/Arch build system for detailed instructions, run  at Kernel/Arch build system#Compiling.

## Video encoding
Most video encoders are highly parallel and are designed to use most of a CPU's capabilities. The example below will encode noise using x265, and discard the result. This will heavily load the CPU.

 ffmpeg -y -f rawvideo -video_size 1920x1080 -pixel_format yuv420p -framerate 60 -i /dev/urandom -c:v libx265 -preset placebo -f matroska /dev/null

## Discovering errors
Some stressing applications like #MPrime, #Linpack, or systester have built in consistency checks to discover errors due to non-matching results. This is more sensitive than looking for kernel errors and should be preferred to it.

A more general method for measuring hardware instabilities can be found in the kernel itself, through hardware error detection or outright failures. Most mistakes in data transfer or calculation do not trigger a failure dramatic enough to be reported as a machine check error.

## Using journalctl manually searching
Simply filter the journal to identify machine check errors:
 # journalctl -k --grep=mce

## Using rasdaemon
Alternatively, build  and start the included service. Rasdaemon keeps an sqlite database of errors which can be queried with the included  binary.
Example:

 # ras-mc-ctl --errors
 No Memory errors.
 No PCIe AER errors.
 No ARM processor errors.
 No Extlog errors.
 No devlink errors.
 MCE events:
 1 2025-06-23 08:24:48 -0400 error: Corrected error, no action required., CPU 2, bank Load Store Unit (bank=0), mcg mcgstatus=0, mci CECC, mca DC data error type 2. Ext Err Code: 13 Memory Error 'mem-tx: evict, tx: data, level: L1', mcgcap=0x00000107, status=0x9c204000000d0175, addr=0x185dd56627, misc=0xd01a000100000000, walltime=0x68594791, cpu=0x00000002, cpuid=0x00b40f40, apicid=0x00000004, microcode=0x0b404032

## Tracking errors back to cores
When optimizing settings, it becomes critical to understand stability on a per-core basis which is the context many BIOS overclocking sections use. A physical core can contain multiple logical CPUs.

Consider the following error from the journal on a Ryzen 9950X (16-physical cores/32-CPUs):

 Error: Corrected error, no action required.
 Error: CPU:5 (1a:44:0) MC0_STATUS0x9c204000000d0175
 [Hardware Error: Error Addr: 0x000000185d960d07
 Error: IPID: 0x000000b000000000, Syndrome: 0x0000000b1a173405
 Error: Load Store Unit Ext. Error Code: 13
 Error: cache level: L1, tx: DATA, mem-tx: EV

The mapping of logical to physical processing units (PUs) can be obtained with lstopo-no-graphics from :
