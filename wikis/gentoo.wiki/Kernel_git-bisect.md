**git-bisect** is a [Git](https://wiki.gentoo.org/wiki/Git "Git") tool to find the commit that caused problems between versions. It is used to identify last working [kernel](https://wiki.gentoo.org/wiki/Kernel "Kernel") patch.

## Contents

-   [[1] [How it works]](#How_it_works)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Get the git sources]](#Get_the_git_sources)
    -   [[2.2] [Link the new sources]](#Link_the_new_sources)
    -   [[2.3] [Start bisect]](#Start_bisect)
    -   [[2.4] [Build the kernel]](#Build_the_kernel)
    -   [[2.5] [Bad bisect]](#Bad_bisect)
    -   [[2.6] [Good bisect]](#Good_bisect)
    -   [[2.7] [Final bisect]](#Final_bisect)
    -   [[2.8] [Log file]](#Log_file)
    -   [[2.9] [Reset bisect]](#Reset_bisect)
-   [[3] [External resources]](#External_resources)
-   [[4] [See also]](#See_also)

## [How it works]

Suppose 2.6.39.1 is working fine and the problem occurs with the 2.6.39.2 upgrade. Let there be 8 patches between 2.6.39.1 and 2.6.39.2. When you start to bisect, it enables only half of those patches and you build a kernel with 4 of the 8 patches between those two versions.

Now you boot your new compiled kernel and see if you can reproduce the problem. If the kernel is good you take the second half of those 8 patches to build the next kernel, if the kernel is bad you take half of the patches used to narrow down on the patch that causes problems.

For this given example, here is what might happen to find the bad patch (each step you have to build the kernel and reboot into it). We call the patches 1,2,3,4,5,6,7,8:

1.  2.6.39.1 + 1,2,3,4
2.  bad → 2.6.39.1 + 1,2
3.  good → 2.6.39.1 + 3,4
4.  bad → 2.6.39.1 + 3
5.  bad → patch 3 it is!

## [Usage]

Step by step example to bisect Linux-2.6.39.

### [Get the git sources]

Get the git sources for a certain branch:

`root `[`#`]`cd /usr/src `

`root `[`#`]`git clone git://git.kernel.org/pub/scm/linux/kernel/git/stable/linux-stable.git linux-stable`

Or, to avoid fetching older commits, e.g. `--shallow-exclude v4.1`, commits since v4.2 will be fetched:

`root `[`#`]`cd /usr/src `

`root `[`#`]`git clone git://git.kernel.org/pub/scm/linux/kernel/git/stable/linux-stable.git --shallow-exclude v4.1 linux-stable`

To bisect a particular stable / longterm branch, e.g. since v5.16 up to v5.16.y, add `--shallow-exclude v5.16 --branch v5.16.y`:

`root `[`#`]`cd /usr/src `

`root `[`#`]`git clone --shallow-exclude v5.16 --branch v5.16.y git://git.kernel.org/pub/scm/linux/kernel/git/stable/linux.git`

This creates the folder [/usr/src/linux-stable].

There are two branches:

-   *linux-stable.git* = [[[sys-kernel/gentoo-sources]](https://packages.gentoo.org/packages/sys-kernel/gentoo-sources)[]] or [[[sys-kernel/vanilla-sources]](https://packages.gentoo.org/packages/sys-kernel/vanilla-sources)[]]
-   *linux.git* = [[[sys-kernel/git-sources]](https://packages.gentoo.org/packages/sys-kernel/git-sources)[]]

** Note**\
This process might take a long time, current size of the git repository is about 500MB.

### [Link the new sources]

Create the symbolic link to the git sources in [/usr/src], mount [/boot] (if needed) and change into the folder:

`root `[`#`]`ln -s linux-stable linux `

`root `[`#`]`mount /boot `

`root `[`#`]`cd /usr/src/linux`

### [Start bisect]

Once here we need to start bisect and tell him which kernel version works and which doesn\'t. In our example 2.6.39.1 has no problems and 2.6.39.2 contains a bad patch. The name could also contain an -rcX at the end, which means it\'s a release candidate, you would have to append that like v2.6.39.1-rc3. I use tee to log every output of bisect into the file [bisect.log].

`root `[`#`]`git bisect start | tee -a /root/bisect.log `

`root `[`#`]`git bisect bad v2.6.39.2 | tee -a /root/bisect.log `

`root `[`#`]`git bisect good v2.6.39.1 | tee -a /root/bisect.log`

** Note**\
Try to narrow the versions down as much as possible before starting the bisect, you might need to recompile the kernel a lot of times otherwise.

### [Build the kernel]

Now compile your kernel as usual using e.g. [genkernel](https://wiki.gentoo.org/wiki/Genkernel "Genkernel") or just make to build it and anything you might need to boot, like initramfs for LVM, Raid etc. Here is the normal method using make.

`root `[`#`]`cp ../linux-2.6.39.1/.config . `

`root `[`#`]`make oldconfig `

`root `[`#`]`make -j4 && make modules_install && make install `

`root `[`#`]`reboot`

### [Bad bisect]

Once booted into the new kernel (make sure your [bootloader](https://wiki.gentoo.org/wiki/Bootloader "Bootloader") is booting the new kernel), test, if the problem still persists. In this example we assume the problem is still there, so we tell bisect. It will now take half the used patchset and we have to build our next kernel.

`root `[`#`]`mount /boot `

`root `[`#`]`cd /usr/src/linux `

`root `[`#`]`git bisect bad | tee -a /root/bisect.log`

Goto [#Build the kernel](#Build_the_kernel)

### [Good bisect]

Now test again and let\'s say this time the problem is gone, so we tell bisect, build the next kernel and reboot.

`root `[`#`]`mount /boot `

`root `[`#`]`cd /usr/src/linux `

`root `[`#`]`git bisect good | tee -a /root/bisect.log`

Goto [#Build the kernel](#Build_the_kernel)

### [Final bisect]

You repeat those steps [#Bad bisect](#Bad_bisect) and [#Good bisect](#Good_bisect) until it shows the content of the bad patch, like shown below (there is more text in the output, this is just half of it).

[CODE] **Final output**

    87cc4d1e3e05af38c7c51323a3d86fe2572ab033 is the first bad commit
    commit 87cc4d1e3e05af38c7c51323a3d86fe2572ab033
    Author: Chris Wright <chrisw@sous-sol.org>
    Date: Sat May 28 13:15:04 2011 -0500

    intel-iommu: Dont cache iova above 32bit

    commit 1c9fc3d11b84fbd0c4f4aa7855702c2a1f098ebb upstream.

    Mike Travis and Mike Habeck reported an issue where iova allocation
    would return a range that was larger than a device's dma mask.

    https://lkml.org/lkml/2011/3/29/423

With this information, you can create a bug report at [bugs.gentoo.org](https://bugs.gentoo.org) and tell the developers what patch causes problems. The [bisect.log] file can be attached to the bug report.

### [Log file]

If you did not create the logfile, you can use the following command to create some log output.

`root `[`#`]`git bisect log`

### [Reset bisect]

If you get stuck somewhere or made a mistake, you can reset.

`root `[`#`]`git bisect reset`

## [External resources]

-   [Bisecting a Bug](https://www.kernel.org/doc/html/latest/admin-guide/bug-bisect.html) - From kernel.org
-   [Binary Search](https://git-scm.com/book/en/v2/Git-Tools-Debugging-with-Git#Binary-Search) - From git-scm.com (*Pro Git* book)

## [See also]

-   [Bisecting with live ebuilds](https://wiki.gentoo.org/wiki/Bisecting_with_live_ebuilds "Bisecting with live ebuilds")