This page is a temporary home for documentation intended as a reference for ZFS developers on how ZFSOnLinux development is done. It is a WIP and it is only meant for developers.

## Contents

-   [[1] [Setting up a development environment]](#Setting_up_a_development_environment)
-   [[2] [Setting up a VM environment]](#Setting_up_a_VM_environment)
    -   [[2.1] [Gentoo with a 9p-virtio rootfs]](#Gentoo_with_a_9p-virtio_rootfs)
    -   [[2.2] [Development]](#Development)
    -   [[2.3] [Debugging]](#Debugging)
    -   [[2.4] [Regression Tests]](#Regression_Tests)
        -   [[2.4.1] [File Bench]](#File_Bench)
        -   [[2.4.2] [Solaris Porting LAyer Tests (splat)]](#Solaris_Porting_LAyer_Tests_.28splat.29)
        -   [[2.4.3] [XFS Test Suite]](#XFS_Test_Suite)
        -   [[2.4.4] [ztest]](#ztest)
-   [[3] [Profiling]](#Profiling)
    -   [[3.1] [Flame Graphs]](#Flame_Graphs)
        -   [[3.1.1] [Generating a Flame Graph with Perf]](#Generating_a_Flame_Graph_with_Perf)
            -   [[3.1.1.1] [Flame Graph of Entire System while a userland program is running]](#Flame_Graph_of_Entire_System_while_a_userland_program_is_running)
            -   [[3.1.1.2] [Flame Graph of Entire System until perf record is killed]](#Flame_Graph_of_Entire_System_until_perf_record_is_killed)
            -   [[3.1.1.3] [Flame Graph of all threads with a unique name]](#Flame_Graph_of_all_threads_with_a_unique_name)
            -   [[3.1.1.4] [Flame Graph of a specific thread by PID]](#Flame_Graph_of_a_specific_thread_by_PID)
            -   [[3.1.1.5] [Flame Graph of all frames with a specific function]](#Flame_Graph_of_all_frames_with_a_specific_function)
    -   [[3.2] [Perf]](#Perf)
    -   [[3.3] [DTrace]](#DTrace)

# [Setting up a development environment]

This is easiest with a Linux environment. It is theoretically possible to use non-Linux environments, but no one does it in practice and anyone trying to use a non-Linux environment will be in new territory.

Once you have a Linux environment, you will want to install and configure git. The [\"Git book\"](http://git-scm.com/book/en/Getting-Started-First-Time-Git-Setup) is a good resource for this, but the simplest setup is:

`user `[`$`]`git config --global user.name "John Doe" `

`user `[`$`]`git config --global user.email johndoe@example.com`

In addition, you will want to setup a github account and configure it so that you can do clones over SSH. Once that is done, clone the repositories:

`user `[`$`]`mdkir ~/devel `

`user `[`$`]`cd ~/devel `

`user `[`$`]`git clone git@github.com:zfsonlinux/spl.git `

`user `[`$`]`git clone git@github.com:zfsonlinux/zfs.git`

Also, you will likely want to install and use cscope. Using cscope is easy with the following bash alias.

`user `[`$`]`alias cscope-init='find . -name '*.c' -o -name '*.h' > cscope.files'`

After running that in your shell, you can run \`cscope-init && cscope -d\` inside directories to get a nice curses interface for browsing the code.

# [Setting up a VM environment]

Virtual machines can save time when running regression tests reveal problems in new code by allowing inspection of the environment from the hypervisor. It is desireable to test module loading and unloading in the virtual environment, so it is best to use a non-ZFS rootfs in the environment running regression tests. The simplest one to use is 9p-virtio, which is a network filesystem whose server is integrated with QEMU and operates over a virtio transport. It also introduces a few quirks of its own, but those can be worked around by compiling in a chroot.

## [Gentoo with a 9p-virtio rootfs]

We pick /guest as a place to store the virtual machines. /guest/gentoo will store the rootfs and we will make clever use of bind mounts to have a chroot at /guest/gentoo-chroot to alow us to operate on the rootfs even while the VM is running.

`root `[`#`]`mkdir -p /guest/gentoo `

`root `[`#`]`cd /guest/gentoo`

Now we install the current stage3:

`root `[`#`]`wget '`[`ftp://gentoo.osuosl.org/pub/gentoo/releases/amd64/autobuilds/current-stage3-amd64/stage3-amd64-`](ftp://gentoo.osuosl.org/pub/gentoo/releases/amd64/autobuilds/current-stage3-amd64/stage3-amd64-)`[0-9]*.tar.bz2' `

`root `[`#`]`tar -xvjpf stage3-amd64-*.tar.bz2 -C .`

Setup the bind mounts:

`root `[`#`]`mount --bind /guest/gentoo `

`root `[`#`]`mount -t proc none /guest/gentoo-chroot/proc `

`root `[`#`]`mount --rbind /dev /guest/gentoo-chroot/dev `

`root `[`#`]`mount --rbind /sys /guest/gentoo-chroot/sys`

Also setup a bind mount to allow the chroot to access code from our development environment:

`root `[`#`]`mount --bind /home/richard/devel /guest/gentoo-chroot/mnt/code `

`root `[`#`]`mount -o remount,ro /guest/gentoo-chroot/mnt/code`

** Note**\
You will need to adjust the paths if you had picked different locations.

** Warning**\
A bug in the Linux kernel prevents us from creating a readonly bind mount that points to a rw location. The bind mount must be created and then remounted as readonly.

Copy resolv.conf so that DNS resolution inside our chroot works:

`root `[`#`]`cp /etc/resolv.conf /guest/gentoo-chroot/etc/`

Now enter the chroot for additional setup:

`root `[`#`]`chroot /guest/gentoo-chroot /bin/bash `

`root `[`#`]`env-update `

`root `[`#`]`source /etc/profile `

`root `[`#`]`cd`

Setup serial terminals

`(chroot) root #``sed -i -e 's\#s0:12345:respawn:/sbin/agetty -L 115200 ttyS0 vt100\s0:12345:respawn:/sbin/agetty -a root -L 115200 ttyS0 vt100\' /etc/inittab `

`(chroot) root #``sed -i -e 's\#s1:12345:respawn:/sbin/agetty -L 115200 ttyS1 vt100\s1:12345:respawn:/sbin/agetty -a root -L 115200 ttyS1 vt100\' /etc/inittab`

Disable the fstab entries. We do not need them with a 9p-virtio rootfs:

`(chroot) root #``sed -i -e "s/\(.*\)\/\(BOOT\|ROOT\|SWAP\)\(.*\)/\#\1\/\2\3/g" /etc/fstab`

Put /tmp and /var/tmp/portage (PORTAGE_TMPDIR) on a tmpfs.

`(chroot) root #``echo -e 'tmpfs\t\t\t/tmp\t\ttmpfs\t\tnosuid\t\t0 0' >> /etc/fstab `

`(chroot) root #``echo -e 'tmpfs\t\t/var/tmp/portage\ttmpfs\t\tnosuid\t\t0 0' >> /etc/fstab`

** Note**\
Anonymous files are files that have been unlinked, but still have open file handles. QEMU\'s 9p-virtio server immediately closes all open file handles that it has when a file is unlinked, which breaks software that relies upon them. The main victims are bash scripts because bash uses anonymous files to implement the \`\<\< KEYWORD\` idiom. Most of the time, these anonymous files are made in /tmp, so putting /tmp on a tmpfs will avoid this issue. The one known exception is building packages, where anonymous files go into PORTAGE_TMPDIR, which is /var/tmp/portage by default. Placing PORTAGE_TMPDIR on a tmpfs will workaround that limitation.

** Warning**\
Failing to use a tmpfs for /tmp will break the XFS test suite, gcc-config and other things. Failing to use a tmpfs for PORTAGE_TMPDIR will require that you build packages outside of the VM.

Now lets setup portage:

`(chroot) root #``mkdir -p /var/db/repos/gentoo `

`(chroot) root #``chown portage:portage /var/db/repos/gentoo`

Lets also setup distfiles and packages:

`(chroot) root #``mkdir -p /var/cache/distfiles /var/cache/binpkgs `

`(chroot) root #``chown portage:portage /var/cache/distfiles /var/cache/binpkgs `

** Note**\
If you wish to share the portage tree, distfiles or packages between your main system and the chroot, it is rather trivial to use bind mounts to do it

Do some portage configuration.

`(chroot) root #``echo 'dev-libs/beecrypt threads' >> /etc/portage/package.use `

`(chroot) root #``echo 'app-emulation/qemu ~amd64' >> /etc/portage/package.accept_keywords `

`(chroot) root #``echo 'dev-util/perf ~*' >> /etc/portage/package.accept_keywords `

`(chroot) root #``echo 'sys-kernel/vanilla-sources ~amd64' >> /etc/portage/package.accept_keywords`

Keyword the 9999 ebuilds.

`(chroot) root #``echo "sys-kernel/spl **" >> /etc/portage/package.accept_keywords `

`(chroot) root #``echo "sys-fs/zfs-kmod **" >> /etc/portage/package.accept_keywords `

`(chroot) root #``echo "sys-fs/zfs **" >> /etc/portage/package.accept_keywords`

Configure ZFS packaging

`(chroot) root #``echo "sys-kernel/spl custom-cflags debug debug-log" >> /etc/portage/package.use `

`(chroot) root #``echo "sys-fs/zfs-kmod custom-cflags debug -rootfs" >> /etc/portage/package.use `

`(chroot) root #``echo "sys-fs/zfs custom-cflags debug -rootfs test-suite" >> /etc/portage/package.use`

If you are not bind mounting a portage tree, install one:

`(chroot) root #``emerge-webrsync`

Install a few tools we will need:

`(chroot) root #``emerge ccache debugedit`

Configure make.conf:

`(chroot) root #``cat << END > /etc/portage/make.conf `

USE=\"mmx sse sse2 multilib dlz -X -gtk -sdl -qt -nptl -xpm -gpm\" CFLAGS=\"-march=native -O2 -pipe -ggdb\" CXXFLAGS=\"\\\$\" MAKEOPTS=\"-j12\" CHOST=\"x86_64-pc-linux-gnu\"

PORTDIR=\"/var/db/repos/gentoo\" DISTDIR=\"/var/cache/distfiles\" PKGDIR=\"/var/cache/binpkgs\"

FEATURES=\"buildpkg ccache collision-protect installsources metadata-transfer multilib-strict noinfo parallel-fetch parallel-install sign split-log splitdebug userpriv usersandbox usersync webrsync-gpg\"

spl_LIVE_BRANCH=master spl_LIVE_REPO=\'/mnt/code/spl\' zfs_kmod_LIVE_BRANCH=master zfs_kmod_LIVE_REPO=\'/mnt/code/zfs\' zfs_LIVE_BRANCH=master zfs_LIVE_REPO=\'/mnt/code/zfs\' END

** Note**\
The wiki markdown is not properly showing line breaks at the moment. Also, you will want to adapt a few of these settings for your system. For instance, MAKEOPTS should be consistent with the number of logical cores that you have in your system.

We compile quite a bit, so we therefore try to optimize GCC somewhat

`(chroot) root #``mkdir -p /etc/portage/env/sys-devel `

`(chroot) root #``echo 'GCC_MAKE_TARGET="profiledbootstrap"' >> /etc/portage/env/sys-devel/gcc`

Lets rebuild everything and install the tools we need at the same time

`(chroot) root #``emerge --jobs --keep-going -ave @world qemu tmux wgetpaste gdb dev-vcs/git htop genlop gentoolkit gentoolkit-dev vim layman ccache debugedit perf sys-kernel/vanilla-sources genkernel pax-utils strace iotop`

Lets cheat at kernel configuration

`(chroot) root #``zcat /proc/config.gz > /usr/src/linux/.config `

`(chroot) root #``make -C /usr/src/linux olddefconfig menuconfig`

In menuconfig, make certain that you enable the following

-   CONFIG_MODULES=y
-   CONFIG_MODULE_UNLOAD=y
-   CONFIG_EXPERT=y
-   CONFIG_KALLSYMS=y
-   CONFIG_KPROBES=y
-   CONFIG_FTRACE=y
-   CONFIG_KPROBE_EVENT=y (probably already set)
-   CONFIG_UPROBE_EVENT=y
-   CONFIG_FUNCTION_TRACER=y
-   CONFIG_FUNCTION_GRAPH_TRACER=y (probably already set)
-   CONFIG_DEBUG_INFO=y
-   CONFIG_READABLE_ASM=y
-   CONFIG_LOCKUP_DETECTOR=y
-   CONFIG_DEBUG_LIST=y
-   CONFIG_KGDB=y
-   CONFIG_DEBUG_SET_MODULE_RONX=y
-   CONFIG_CC_STACKPROTECTOR_REGULAR=y (CONFIG_CC_STACKPROTECTOR_STRONG preferred, but we don\'t have GCC 4.9 yet)
-   CONFIG_VIRTIO_PCI=y
-   CONFIG_NET_9P=y
-   CONFIG_NET_9P_VIRTIO=y
-   CONFIG_9P_FS=y
-   CONFIG_9P_FS_POSIX_ACL=y
-   CONFIG_9P_FS_SECURITY=y

** Note**\
You can type the \'/\' character to open a search dialog in the menuconfig interface. Use it to help you navigate.

Then compile the kernel:

`(chroot) root #``make -C /usr/src/linux bzImage`

Now install ZFS. It should pull from your local checkout.

`(chroot) root #``emerge zfs`

Now you should be able to start a VM:

`user `[`$`]`sudo qemu-kvm -smp 12,cores=6,threads=1,sockets=1 -cpu host -m 1024 -kernel /guest/gentoo/usr/src/linux/arch/x86/boot/bzImage -append 'root=/dev/root rootfstype=9p rootflags=trans=virtio,version=9p2000.L ro console=ttyS0' -serial mon:stdio -serial pty -fsdev local,id=root,path=/guest/gentoo,security_model=passthrough -device virtio-9p-pci,fsdev=root,mount_tag=/dev/root -vga none -nographic`

** Note**\
Here we specify a SMP configuration consistent with a single Xeon E5-2620. You will likely want to adjust this based on your own system configuration.

## [Development]

You will commit changes to a branch in your git checkouts in your home directory. Inside the chroot, you will rebuild the ZFS kernel modules and userland tools as needed:

`(chroot) root #``emerge --oneshot @module-rebuild sys-fs/zfs`

Edit the appropriate variables in /etc/portage/make.conf to point to the branch that you want to compile. Sometimes, you will encounter situations where a running virtual machine has old copies of the files from the chroot. You can resolve that by running drop_caches inside the VM:

`root `[`#`]`echo 3 > /proc/sys/vm/drop_caches`

## [Debugging]

QEMU\'s monitor and first serial console are multiplexed on the terminal by the QEMU command in the previous section. Switching between them can be done by typing Ctrl+A C. QEMU\'s monitor has several interesting functions. One being that it permits you to start the gdb server by typing \`gdbserver\`. gdb can then be attached to debug. This has an issue where gdb cannot find the kernel sources, but this can be resolved by using gdb from the chroot to debug the running VM:

`user `[`$`]`sudo -i chroot /guest/gentoo /usr/bin/gdb /usr/src/linux/vmlinux`

If on a 64-bit architecture, it is often necessary to specify that to gdb explicitly. Afterward, gdb can be sanely told to attach to the server. The default port is 1234.

`(gdb)``set architecture i386:x86-64 `

`(gdb)``target remote localhost:1234`

Since the ZFSOnLinux code is loaded as modules, we will need to tell gdb about them. At present, the only known way of doing this is getting the module address from /proc/modules inside the VM environment and then telling gdb to load the symbol files. The zfs module must be loaded when you access /proc/modules or it will not appear. Loading the module symbol tables into gdb is relatively straightforward:

`(gdb)``set confirm off `

`(gdb)``add-symbol-file /lib/modules/2.6.32-431.11.2.el6.x86_64/extra/zfs/zfs.ko 0xffffffffa0181000 `

`(gdb)``add-symbol-file /lib/modules/2.6.32-431.11.2.el6.x86_64/extra/taskq/ztaskq.ko 0xffffffffa0177000 `

`(gdb)``add-symbol-file /lib/modules/2.6.32-431.11.2.el6.x86_64/extra/spl/spl.ko 0xffffffffa00cb000 `

`(gdb)``set confirm on`

** Note**\
By default, gdb will ask if we are sure whenever we want to add a symbol file. We can use the condfirm variable to temporarily disable this behavior.

Generating such commands is time consuming, so we can tell the guest to generate them and print them to stdout for us to copy and paste to the host:

`user `[`$`]`while IFS=' ' read a b c d e f g; do echo "add-symbol-file $(modinfo -0 --filename $) $"; done </proc/modules`

Loading the module symbol files into gdb will enable you to use gdb break points on the ZFS code in gdb and step through execution. These breakpoints will be lost in the event that you reset the virtual machine using \`system_reset\` from the QEMU monitor.

Since gdbserver is running at the level of QEMU, you will not be able to see individual threads. Instead, you will see cores, but that in itself can be advantageous in certain scenarios. Getting direct access to threads requires using kgdb.

## [Regression Tests]

### [File Bench]

Stress testing the code via random IO can be helpful when making changes that affect performance or potentially correctness.

`root `[`#`]`modprobe brd rd_size=8388608 `

`root `[`#`]`zpool create -m /tmp/test -o cachefile=/tmp/zpool.cache -O compression=lz4 test /dev/ram0 `

`root `[`#`]`filebench << END `

load randomwrite set \\\$dir=/tmp/test set \\\$nthreads=32 set \\\$iosize=4096 run 60

END

** Warning**\
Care should be taken when running these commands. The wiki does not seem to handle the multiline command very well, so the display is not quite correct.

### [][Solaris Porting LAyer Tests (splat)]

The Solaris Porting Layer consists of a module that implements Solaris kernel APIs on top of Linux kernel APIs. SPLAT is a regression test platform for verifying the operation of these tests. Running them is simple:

`root `[`#`]`modprobe splat `

`root `[`#`]`splat -a`

### [XFS Test Suite]

The XFS Test Suite is a POSIX filesystem API conformance test originally developed by SGI for use on IRIX. It was ported to Linux after IRIX around the time SGI was accquired by Rackable Systems. It is the primary test suite used to test the POSIX filesystem API conformance of Linux filesystems. Brian Behlendorf at LLNL maintains a couple of forks of the XFS Test Suite that have been adapted to permit use with ZFS in two separate branches. They are located at:

[https://github.com/behlendorf/xfstests](https://github.com/behlendorf/xfstests)

The zfs branch contains the original fork of the XFS tests from mid-2011. The zfs-upstream branch contains a rebase on upstream that was done in November 2013 with the intention of upstreaming ZFS support. The latter is far easier to use than the former and is presently the master branch, so we shall document use of the latter.

It requires that you install git to fetch it and the xfsprogs to build it. Once these requirements are met, we can fetch and build it:

`user `[`$`]`git clone git@github.com:behlendorf/xfstests.git `

`user `[`$`]`cd xfstests `

`user `[`$`]`make -s`

Running them requires that \`hostname -f\` works properly on your system. On a Gentoo workstation, this means editing the 127.0.0.1 line in /etc/hosts to be something like \'127.0.0.1 localhost myhostname\' where myhostname is the value in /etc/conf.d/hostname. Once that works, we can setup the system to run them:

`root `[`#`]`truncate -s 3G /xfs-scratch `

`root `[`#`]`truncate -s 3G /xfs-test `

`root `[`#`]`losetup loop0 /xfs-test && losetup loop1 /xfs-scratch `

`root `[`#`]`export TEST_DEV=/dev/loop0 `

`root `[`#`]`export SCRATCH_DEV=/dev/loop1 `

`root `[`#`]`export TEST_DIR=/test `

`root `[`#`]`export SCRATCH_MNT=/scratch `

`root `[`#`]`zpool create -f -m legacy -O acltype=posixacl test /dev/loop0 `

`root `[`#`]`zpool create -f -m legacy -O acltype=posixacl zscratch /dev/loop1 `

`root `[`#`]`cd ~/xfstests && ./check -zfs generic/[0-9][0-9][0-9] `

** Note**\
If \`./configs/\$(hostname -f).config exists, ./check will ignore the environment variables and use it. This requires configuring that file instead.

Unfortunately, not all of the newer XFS tests currently work. In specific, generic/317 has a bash script that hangs in a subshell. Killing the bash interpreter for that subshell will make it correctly report that generic/317 is not able to run because of a missing user account. This is something that needs to be fixed, but it can be worked around by running a subset of tests that are known to actually test things on ZFS:

`root `[`#`]`./check -zfs generic/001 generic/002 generic/005 generic/006 generic/007 generic/010 generic/011 generic/013 generic/014 generic/015 generic/020 generic/053 generic/062 generic/069 generic/070 generic/074 generic/075 generic/076 generic/079 generic/083 generic/088 generic/089 generic/100 generic/105 generic/117 generic/120 generic/124 generic/126 generic/127 generic/129 generic/131 generic/132 generic/141 generic/169 generic/184 generic/192 generic/204 generic/215 generic/221 generic/224 generic/236 generic/237 generic/245 generic/246 generic/247 generic/248 generic/249 generic/257 generic/258 generic/269 generic/273 generic/275 generic/277 generic/285 generic/286 generic/294 generic/306 generic/307 generic/308 generic/309 generic/310 generic/313 generic/315 generic/318 generic/319 generic/320`

In addition, a few currently fail as of 0.6.3. These failures need to be investigated and fixed.

### [ztest]

ztest is a userland tool. It links to a userland copy of the ZFS kernel code, creates a pool and then stresses the code by randomly selects from many possible operations runs many possible operations in many parallel threads at the same time. It will occasionally kill itself and resume to simulate system failures. It has some issues on 9p-virtio, so it will need to be run inside the chroot. This can be done much like we run gdb:

`user `[`$`]`sudo -i chroot /guest/gentoo /bin/mkdir -p /tmp/ztest-0 `

`user `[`$`]`sudo -i chroot /guest/gentoo /sbin/ztest -f /tmp/ztest-0 -k 50 -V -T 43200`

The above example will run ztest for 12 hours with the files in /tmp/ztest-0 of the chroot and it will kill itself half of all runs. If a segmentation fault or assertion failure occurs, it will die leaving a core dump, which could be analyzed with gdb:

`user `[`$`]`sudo -i chroot /guest/gentoo /usr/bin/gdb /sbin/ztest -c /tmp/ztest-0/core`

# [Profiling]

## [Flame Graphs]

Flame Graphs are an indispensible tool for visualizing profile data. They are documented at Brendan Gregg\'s site:

[http://www.brendangregg.com/FlameGraphs/cpuflamegraphs.html](http://www.brendangregg.com/FlameGraphs/cpuflamegraphs.html)

They require that something generate data. Perf is the primary tool for doing that on Linux. On other platforms, it is DTrace.

### [Generating a Flame Graph with Perf]

You will need the following prerequisites to generate a sane flame graph with perf:

1.  The kernel must be compiled with CONFIG_FRAME_POINTER=y
2.  The kernel modules must not have been stripped. Some distributions strip them in a way that the file utility does not report that they have been stripped. You can use \`ls -lh \$(modinfo -n zfs)\` to check. The unstripped ZFS module should be about 28MB while the stripped ZFS module should be about 2MB to 3MB.
3.  The perf binary must be \[[](https://github.com/torvalds/linux/commit/61d4290cc1f10588147b76b385875f06827d47ff)\] to support profiling of out-of-tree kernel modules. perf 3.15 and later have the patch included.
4.  You must obtain the flame graph scripts from \[[](https://github.com/brendangregg/FlameGraph)\] on github.

Once those requirements are met, it is simple to profile and generate flame graphs. The general idea is to generate a perf.data file containing the trace. The perf.data file does not have symbols, so the perf script command is used to convert it into a human readable format using symbols from your system. After that, the data can be processed anywhere to generate the flame graph.

#### [Flame Graph of Entire System while a userland program is running]

The program chosen for this example is the sleep command with argument 60, such that it will stay alive for 60 seconds and then terminate, generating output. This is good if you want a timer, although if you have a specific program in mind where you want to profile the whole system, you can invoke it from perf:

`root `[`#`]`perf record -F 997 -ag -- sleep 60 `

`root `[`#`]`perf script | /path/to/stackcollapse-perf.pl > out.perf-folded `

`root `[`#`]`/path/to/flamegraph.pl < out.perf-folded > perf-kernel.svg`

#### [Flame Graph of Entire System until perf record is killed]

The perf record command below will block indefinitely until killed with Ctrl+C (SIGTERM) when it will generate perf.data. Killing it with SIGKILL will prevent it from generating perf.data.

`root `[`#`]`perf record -F 997 -ag `

`root `[`#`]`perf script | /path/to/stackcollapse-perf.pl > out.perf-folded `

`root `[`#`]`/path/to/flamegraph.pl < out.perf-folded > perf-kernel.svg`

#### [Flame Graph of all threads with a unique name]

We use sleep 60 here to do perform this over 60 seconds, but any of the previous variations on invoking perf record would work.

`root `[`#`]`perf record -F 997 -ag -- sleep 60 `

`root `[`#`]`perf script | /path/to/stackcollapse-perf.pl > out.perf-folded `

`root `[`#`]`grep '^txg_sync;' out.perf-folded | /path/to/flamegraph.pl > perf-kernel.svg`

** Note**\
We use the name \"txg_sync\" as an example, but it could be any thread that grep matches.

#### [Flame Graph of a specific thread by PID]

We use sleep 60 here to do perform this over 60 seconds, but any of the previous variations on invoking perf record would work.

`root `[`#`]`perf record -p $PID -F 997 -g -- sleep 60 `

`root `[`#`]`perf script | /path/to/stackcollapse-perf.pl > out.perf-folded `

`root `[`#`]`/path/to/flamegraph.pl < out.perf-folded > perf-kernel.svg`

** Note**\
The \$PID must be specified as an integer

#### [Flame Graph of all frames with a specific function]

We use sleep 60 here to do perform this over 60 seconds, but any of the previous variations on invoking perf record would work.

`root `[`#`]`perf record -F 997 -ag -- sleep 60 `

`root `[`#`]`perf script | /path/to/stackcollapse-perf.pl > out.perf-folded `

`root `[`#`]`grep ';\<dbuf_find\>' out.perf-folded | /path/to/flamegraph.pl > perf-kernel.svg`

** Note**\
We use the name \"dbuf_find\" as an example, but it could be any function.

The purpose of particular flame graph is to identify the call paths of specific function(s) under a workload. By identifying the call paths and examining the code for the stack frames, we can gain insight into things like concurrency by thinking about whether two stacks can occur simultaneously and what that means for performance with respect to locks held by each stack frame. We can also use the knowledge gained to design workloads that exercise particular functions, which is useful when evaluating the impact of changes on concurrency.

## [Perf]

Brendan Greg has excellent documentation on doing profiling with perf. There is not much one can add to it:

[http://www.brendangregg.com/perf.html](http://www.brendangregg.com/perf.html)

## [DTrace]

There is an experimental Linux DTrace port called DTrace4Linux. It is prone to crash systems and should not be run in production. If you wish to profile inside a test environment and are willing to help development, then it is an option:

[https://github.com/dtrace4linux/linux](https://github.com/dtrace4linux/linux)

** Note**\
The techniques shown for debugging ZFS can be applied to dtrace4linux.