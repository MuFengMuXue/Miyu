** Important**\
It is unlikely that tmpfs will provide any performance gain for modern systems that have `-pipe` set in the `CFLAGS` environment variable, even for systems with a spinning drive.

\
When [emerging](https://wiki.gentoo.org/wiki/Emerge "Emerge") packages it is possible to unpack and build them in [tmpfs](https://wiki.gentoo.org/wiki/Tmpfs "Tmpfs") (RAM) instead of on a disk drive. Building packages in tmpfs is **unlikely to provide any benefit on a modern system**.

Any potential performance benefits are hard to quantify:

-   Modern filesystems are designed to prevent fragmentation
-   modern operating systems use RAM as [disk cache](https://en.wikipedia.org/wiki/Page_cache "wikipedia:Page cache") which prevents unnecessary reads
-   if the tmpfs is set up incorrectly for the system (or package in question) it may lead to more [swapping](https://wiki.gentoo.org/wiki/Swap "Swap") instead of less
-   per-package configuration and management is likely to be required on systems with \< 16G of **dedicated tmpfs memory**.

Generally speaking, unless the system in question has an excessive amount of RAM, the overheads of tmpfs make it unpalatable for most use cases; the greatest benefit of using tmpfs for compilation is on large packages that require **a significant investment in RAM**. **It is more cost-effective to replace a SSD after many years of writes than to buy more RAM upfront to save on writes**.

** Important**\
Users are strongly cautioned **against buying additional RAM to use as tmpfs**.

If there is some reason that compiling on a tmpfs is desirable, consider \"Portage TMPDIR on [zram](https://wiki.gentoo.org/wiki/Zram "Zram")\" instead, where the choice of compression-algorithm is a tradeoff between preserving RAM space and performance.

In short, if there is sufficient RAM to build in tmpfs the kernel caching will do it anyway. tmpfs will only save writes that will never be read.

## Contents

-   [[1] [Configuration]](#Configuration)
    -   [[1.1] [Considering tmpfs size]](#Considering_tmpfs_size)
    -   [[1.2] [fstab]](#fstab)
    -   [[1.3] [Per-package choices at compile time]](#Per-package_choices_at_compile_time)
-   [[2] [Tips]](#Tips)
    -   [[2.1] [Resizing tmpfs]](#Resizing_tmpfs)
    -   [[2.2] [Save an emerge and resume later]](#Save_an_emerge_and_resume_later)
-   [[3] [Troubleshooting]](#Troubleshooting)
    -   [[3.1] [No space left on device]](#No_space_left_on_device)
-   [[4] [See also]](#See_also)

## [Configuration]

### [Considering tmpfs size]

The system\'s tmpfs space should be large enough to handle the largest packages to be compiled on the system. If the tmpfs space were to ever become completely full then the emerge will fail. Most packages would not need more than 1 GB for compilation, but there are a few that are very large and would need more. Those still wanting to compile these packages on tmpfs should verify enough free tmpfs space exists. The following list contains estimates of how much space is allocated on each package. Some of these are based on the minimum space requirements specified in the ebuilds. Note that the actual allocated size may vary depending on the features included when building the package, and it may also vary on every version update.

An example of a size check failure:

    * There is NOT at least 13 GiB disk space at "/var/tmp/portage/www-client/firefox-81.0.1/temp"
    *
    * Space constraints set in the ebuild were not met!
    * The build will most probably fail, you should enhance the space
    * as per failed tests.

\

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -----------------------------------------------------------------------------------------------------
  Package                                                                                                                                                                                                                                                                                                                                                                                                                              Memory usage (uncompressed)
  [[[app-office/libreoffice]](https://packages.gentoo.org/packages/app-office/libreoffice)[]]                                             \~6 GB with 512 MB of extra system memory
  [[[dev-db/mysql]](https://packages.gentoo.org/packages/dev-db/mysql)[]]                                                                           8 GB (versions \>= 8.0.19-r1)
  [[[dev-lang/ghc]](https://packages.gentoo.org/packages/dev-lang/ghc)[]]                                                                           \> 4 GB (**will** fail with less)
  [[[dev-lang/mono]](https://packages.gentoo.org/packages/dev-lang/mono)[]]                                                                        \> 4 GB (**will** fail with less)
  [[[dev-lang/rust]](https://packages.gentoo.org/packages/dev-lang/rust)[]]                                                                        \~7 GB; \~10 GB if FLAGS has `-ggdb` set
  [[[dev-lang/spidermonkey]](https://packages.gentoo.org/packages/dev-lang/spidermonkey)[]]                                                \> 6.4 GB (**will** fail with less)
  [[[dev-qt/qtwebengine]](https://packages.gentoo.org/packages/dev-qt/qtwebengine)[]]                                                         Builds a fork of Chromium in the background: \~10 GB with 3 GB of extra system memory
  [[[llvm-core/clang]](https://packages.gentoo.org/packages/llvm-core/clang)[]]                                                                  8.8 GB
  [[[llvm-core/llvm]](https://packages.gentoo.org/packages/llvm-core/llvm)[]]                                                                     8.0 GB
  [[[llvm-runtimes/compiler-rt-sanitizers]](https://packages.gentoo.org/packages/llvm-runtimes/compiler-rt-sanitizers)[]]   11.0 GB if the `test` USE flag is enabled
  [[[mail-client/thunderbird]](https://packages.gentoo.org/packages/mail-client/thunderbird)[]]                                          Approximately the same as Firefox
  [[[sci-libs/tensorflow]](https://packages.gentoo.org/packages/sci-libs/tensorflow)[]]                                                      \~5 GB per Python target, e.g. if targeting both Python 3.6 and Python 3.7, it will require \~10 GB
  [[[sys-devel/gcc]](https://packages.gentoo.org/packages/sys-devel/gcc)[]]                                                                        \> 4 GB (**will** fail with less), even more if Java and Objective C are also included
  [[[www-client/chromium]](https://packages.gentoo.org/packages/www-client/chromium)[]]                                                      \~10 GB with 3 GB of extra system memory
  [[[www-client/firefox]](https://packages.gentoo.org/packages/www-client/firefox)[]]                                                         \~4.5 GB; \~13 GB if the `pgo`, `debug`, or `test` USE flag has been enabled
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -----------------------------------------------------------------------------------------------------

When using [[ccache](https://wiki.gentoo.org/wiki/Ccache "Ccache")] to assist in resuming compiles, it should be noted an equal size of the [/var/tmp] and [/var/tmp/portage] directories is necessary. Alternatively the per-package choices as shown below for large packages requiring large amounts of space can be implemented.

[ccache] creates a directory in [/var/cache/ccache] to store compiled elements for resuming.

### [fstab]

Mount Portage\'s `TMPDIR` ([/var/tmp/portage] is where Portage stores files while building packages. ) to tmpfs by adding the following to the system\'s [[/etc/fstab](https://wiki.gentoo.org/wiki//etc/fstab "/etc/fstab")] config file:

[FILE] **`/etc/fstab`tmpfs fstab example**

    tmpfs     /var/tmp/portage        tmpfs   size=4G,uid=portage,gid=portage,mode=775    0 0

** Note**\
If using [SELinux](https://wiki.gentoo.org/wiki/SELinux "SELinux"), the following option can be added: `rootcontext=system_u:object_r:portage_tmp_t`.

The `size` parameter can be adjusted in [/etc/fstab] to set the max size of the tmpfs, limiting RAM usage. Systems with large amounts of RAM can increase the value quite significantly.

** Note**\
If mounting Portage\'s tmp dir as a tmpfs, there is **no** need to change Portage\'s `PORTAGE_TMPDIR` in [/etc/portage/make.conf].

** Important**\
If setting `PORTAGE_TMPDIR` and using a different path, Portage will automatically add */portage* to the specified path. Setting this to **/tmp** actually uses **/tmp/portage** so the tmpfs should be mounted there.

After [/etc/fstab] has been modified, mount Portage\'s `TMPDIR` to RAM by running the [mount] command followed by the directory location outline in [fstab] (this does not need to be done manually after every boot. After a reboot [/var/tmp/portage] should be mounted by [/etc/fstab] automatically):

`root `[`#`]`mount /var/tmp/portage`

In the unlikely event that the entire [/var/tmp/] directory is *already* mounted as tmpfs, it can be worked around by the special `x-mount.mkdir` mount option:

[FILE] **`/etc/fstab`tmpfs fstab example**

    tmpfs /var/tmp         tmpfs rw,nosuid,nodev,size=4G,mode=1777 0 0
    tmpfs /var/tmp/portage tmpfs rw,nosuid,nodev,size=4G,mode=775,uid=portage,gid=portage,x-mount.mkdir=775 0 0

### [Per-package choices at compile time]

Portage can be configured to build large packages outside of the tmpfs space on a per-package basis.

Create a file to tell Portage where to place the temporary files directory:

[FILE] **`/etc/portage/env/notmpfs.conf`**

    PORTAGE_TMPDIR="/var/tmp/notmpfs"

Create a separate temporary file directory outside of the tmpfs mount location:

`root `[`#`]`mkdir /var/tmp/notmpfs `

`root `[`#`]`chown portage:portage /var/tmp/notmpfs `

`root `[`#`]`chmod 775 /var/tmp/notmpfs `

Create a special Portage file called [[package.env]](https://wiki.gentoo.org/wiki//etc/portage/package.env "/etc/portage/package.env") in [[/etc/portage/]](https://wiki.gentoo.org/wiki//etc/portage "/etc/portage") and list all the packages that are too large to be compiled using tmpfs:

[FILE] **[`/etc/portage/package.env`](https://wiki.gentoo.org/wiki//etc/portage/package.env "/etc/portage/package.env")**

    app-office/libreoffice        notmpfs.conf
    dev-lang/ghc            notmpfs.conf
    dev-lang/mono           notmpfs.conf
    dev-lang/rust           notmpfs.conf
    dev-lang/spidermonkey       notmpfs.conf
    mail-client/thunderbird     notmpfs.conf
    sys-devel/gcc           notmpfs.conf
    llvm-core/clang                 notmpfs.conf
    llvm-core/llvm                  notmpfs.conf
    www-client/chromium     notmpfs.conf
    www-client/firefox      notmpfs.conf
    dev-qt/qtwebengine              notmpfs.conf
    games-strategy/0ad              notmpfs.conf

## [Tips]

### [Resizing tmpfs]

To resize the current tmpfs instance in [/var/tmp/portage], run:

`root `[`#`]`mount -o remount,size=N /var/tmp/portage `

Where `N` is in the form of bytes. It can also be suffixed with `k`, `m`, or `g` to respectively have the form of (k)ilobytes, (m)egabytes or (g)igabytes. It can also be suffixed with a `%` to limit the tmpfs instance to the percentage of current physical RAM, the default being 50% when the parameter is not specified.

The resized tmpfs will not persist to the next boot unless the `size` parameter is modified in [/etc/fstab]. This is not necessary since a larger tmpfs is only needed during large package compilations.

It is recommended to leave-out at least 1 GB of space for the system to prevent out-of-memory problems. Using swap-disks for some heavy compile-time and link-time instances which are unexpected may also be helpful. Now even if swap-disks are used, reads and writes to it would only be minimal compared to having a physical filesystem behind [/var/tmp/portage].

Here is a note about the size parameter in Linux kernel\'s documentation which can be found in [/usr/src/linux/Documentation/filesystems/tmpfs.txt] as long as a kernel has been emerged:

[FILE] **`tmpfs.txt`TMPFS information**

    size: The limit of allocated bytes for this tmpfs instance. The default is half of your physical RAM without swap. If you oversize your tmpfs instances the machine will deadlock since the OOM handler will not be able to free that memory.

Besides the obvious danger of choking the system by allocating too much memory for tmpfs space, it should be generally safe to enlarge the tmpfs during an emerge as this would only increase the size limit of the tmpfs without destroying any data from the emerge process.

For example, if a system has 12 GB of RAM and 3 disks with 2 GB of swap space working in parallel on each disk, then it would be pretty safe to choose size limit equal to `16G`. 16 GB size is usually enough to compile Libreoffice and Chromium in parallel (usual [emerge -1uDN \@world]) while reading Internet in a web browser.

It\'s not often that you\'ll ever have to do it and [emerge] would tell you that tmpfs is too small however there are instances that the package\'s ebuild would be not accurate at estimating the amount of disk space necessary for building the package. Newer packages may end up allocating more space, whereas using lesser USE flags would make it allocate less.

The solution for this is to either enlarge tmpfs, or add the exception to [/etc/portage/package.env], and then run [emerge] again.

### [Save an emerge and resume later]

** Note**\
This is experimental. ebuild experts should be queried about how reliable this command is; when to use it and when not to. [[[bug #549580]](https://bugs.gentoo.org/show_bug.cgi?id=549580)[]] tracks possibly doing this automatically in Portage.

**Example**: emerging webkit-gtk can take a long time. I want to reboot into another OS and resume this ebuild later.

*Optional*: I use [[[app-portage/genlop]](https://packages.gentoo.org/packages/app-portage/genlop)[]] to inspect the current emerge session. I like using it to remind me of the ebuild version number or hopefully to get an estimated time remaining.

`user `[`$`]`genlop -c`

    Currently merging 1 out of 2

     * net-libs/webkit-gtk-2.4.8

           current merge time: 4 hours, 27 minutes and 35 seconds.
           ETA: unknown.

Press [Ctrl]+[c] to quit the current [emerge] session.

Since I am rebooting, I\'ll have to use [cp -a] or [tar -cpf] to save [/var/tmp/portage/\*] while preserving permissions. Otherwise the tmpfs contents will be lost; You may want to inspect the memory size of [/var/tmp/portage] by using [du]:

`root `[`#`]`du -sh /var/tmp/portage/`

    251M   /var/tmp/portage/

Reboot, do other stuff, come back later.

Restore [/var/tmp/portage/\*].

Resume the ebuild with [ebuild \<repository_directory\>/\<category\>/\-\<version\>.ebuild merge]:

`root `[`#`]`ebuild /var/db/repos/gentoo/net-libs/webkit-gtk/webkit-gtk-2.6.5.ebuild merge `

    >>> Existing $/environment for 'webkit-gtk-2.6.5' will be sourced. Run
    >>> 'clean' to start with a fresh environment.
    >>> Checking webkitgtk-2.6.5.tar.xz's mtime...
    >>> WORKDIR is up-to-date, keeping...
     * checking ebuild checksums ;-) ...                                                                                                                   [ ok ]
     * checking auxfile checksums ;-) ...                                                                                                                  [ ok ]
     * checking miscfile checksums ;-) ...                                                                                                                 [ ok ]
    >>> It appears that 'setup' has already executed for 'webkit-gtk-2.6.5'; skipping.
    >>> Remove '/var/tmp/portage/net-libs/webkit-gtk-2.6.5/.setuped' to force setup.
    >>> It appears that 'unpack' has already executed for 'webkit-gtk-2.6.5'; skipping.
    >>> Remove '/var/tmp/portage/net-libs/webkit-gtk-2.6.5/.unpacked' to force unpack.
    >>> It appears that 'prepare' has already executed for 'webkit-gtk-2.6.5'; skipping.
    >>> Remove '/var/tmp/portage/net-libs/webkit-gtk-2.6.5/.prepared' to force prepare.
    >>> Configuring source in /var/tmp/portage/net-libs/webkit-gtk-2.6.5/work/webkitgtk-2.6.5 ...
    >>> Working in BUILD_DIR: "/var/tmp/portage/net-libs/webkit-gtk-2.6.5/work/webkit-gtk-2.6.5_build"
    ..
    ..
    .

If you\'re using other repository sources besides `gentoo` like layman overlays, make sure that you\'re using the correct repository directory of the ebuild as one package can also belong to other repositories and be chosen to be installed over the one in `gentoo`. You can get the repository name of the current package by reading the last action entry in [/var/log/emerge.log] or reading the build.log file in the package\'s build directory with a command like:

`user `[`$`]`fgrep Repository: /var/tmp/portage/net-libs/webkit-gtk-2.6.5/temp/build.log`

Do not use the [.ebuild] file found in [/var/tmp/portage/\<category\>/\-\<version\>/build-info/\-\<version\>.ebuild] as it seems to be only a reference. Perhaps there\'s a way to use it, but one would have to thoroughly understand how [ebuild] and [ebuild.sh] work.

Happy hacking!

## [Troubleshooting]

### [No space left on device]

When emerging, an error may arise:

`root `[`#`]`emerge -1 wget`

    ...
    >>> Emerging (1 of 2) sec-keys/openpgp-keys-wget-20241111::gentoo
    >>> Downloading 'https://mirror.clarkson.edu/gentoo/distfiles/19/openpgp-keys-wget-20241111-7845120B07CBD8D6ECE5FF2B2A1743EDA91A35B6.asc'
    [ERROR] Exception in callback PipeLogger._io_loop_done(<Task finishe...t on device')>)
    handle: <Handle PipeLogger._io_loop_done(<Task finishe...t on device')>)>
    Traceback (most recent call last):
      File "/usr/lib/python3.12/asyncio/events.py", line 88, in _run
        self._context.run(self._callback, *self._args)
      File "/usr/lib/python3.12/site-packages/portage/util/_async/PipeLogger.py", line 161, in _io_loop_done
        future.result()
      File "/usr/lib/python3.12/site-packages/portage/util/_async/PipeLogger.py", line 157, in _io_loop
        log_file.flush()
    OSError: [Errno 28] No space left on device
    Terminated

`user `[`$`]`df -h`

    Filesystem      Size  Used Avail Use% Mounted on
    ...
    tmpfs           3.6G  3.6G     0 100% /var/tmp/portage

If you encounter a not-enough space error or anything similar, there are basically two things to do:

1.  Check the [/var/tmp/portage] directory for old package directories from previously failed compiles. Any packages found therein should be deleted; with exceptions made for any failed packages the user would like to resume compiling later.
2.  [Resize the tmpfs](#Resizing_tmpfs).
3.  In case you still get messages related to exhausted disk space during emerge, even though the allocated tmpfs size is not nearly exceeded (check with [du -h] during emerge), you may have stumbled upon an inodes shortage. So far it definitely may be a problem for the [[[www-client/chromium]](https://packages.gentoo.org/packages/www-client/chromium)[]] package, for it\'s grand storage requirements, but can be expected for other large packages as well. To workaround - append `nr_inodes=0` to the list of your options for the tmpfs mount in the [/etc/fstab] file. For additional information refer to \'tmpfs\' section in [man mount].

As last instance, add a (temporary) swap file somewhere on your system with enough capacity:

`root `[`#`]`touch /swap.img `

`root `[`#`]`chmod 600 /swap.img `

`root `[`#`]`dd if=/dev/zero bs=1024M of=/swap.img count=8 `

This will create the file [/swap.img] with [8GB] filled with zeroes.

Set up the swap area using:

`root `[`#`]`mkswap /swap.img`

Enable the file for swapping:

`root `[`#`]`swapon /swap.img`

Check, if the swap file is active:

`root `[`#`]`swapon --summary`

    Filename                     Type            Size    Used    Priority
    /swap.img                    file            8388604 3876352 -2

Compile the packages which would deadlock the computer because of high RAM usage (e.g. chromium):

`root `[`#`]`emerge --ask www-client/chromium`

Alternatively, disable and remove the swap file when finished:

`root `[`#`]`swapoff /swap.img `

`root `[`#`]`rm /swap.img `

## [See also]

-   [Zram](https://wiki.gentoo.org/wiki/Zram "Zram") --- a [Linux kernel](https://wiki.gentoo.org/wiki/Kernel "Kernel") feature and set of userspace tools for creating compressible RAM-based block devices.
-   [Zswap](https://wiki.gentoo.org/wiki/Zswap "Zswap") --- a lightweight compressed cache for swap pages.