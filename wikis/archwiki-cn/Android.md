**翻译状态：**

  * 本文（或部分内容）译自 [Android](<https://wiki.archlinux.org/title/Android> "arch:Android")，最近一次同步于 2023-03-13，若英文版本有所[更改](<https://wiki.archlinux.org/title/Android?diff=0&oldid=772441>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Android_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [Android tethering](</wzh/index.php?title=Android_tethering&action=edit&redlink=1> "Android tethering（页面不存在）")
  * [Android Debug Bridge](<../zh-cn/Android_Debug_Bridge.html> "Android Debug Bridge")

##  同步

有各种应用程序可以用来传输文件，同步通知等。 

###  多合一

  * [KDE Connect](<../zh-cn/KDE_Connect.html> "KDE Connect") ([kdeconnect](<https://archlinux.org/packages/?name=kdeconnect>)包) – 将安卓设备整合到 KDE/Gnome 桌面，具有通知同步、剪贴板同步、多媒体控制和文件/ URL 共享等功能。

###  同步通知

  * [a2ln](<https://aur.archlinux.org/packages/a2ln/>)AUR – 通过局域网提供通知同步，具有认证、加密等功能。

###  传输文件

  * USB数据线 
    * 现代安卓设备使用[媒体传输协议](<../zh-cn/%E5%AA%92%E4%BD%93%E4%BC%A0%E8%BE%93%E5%8D%8F%E8%AE%AE.html> "媒体传输协议")。
    * 旧设备使用 [USB大容量存储设备](<https://zh.wikipedia.org/wiki/USB%E5%A4%A7%E5%AE%B9%E9%87%8F%E5%AD%98%E5%82%A8%E8%AE%BE%E5%A4%87> "zhwp:USB大容量存储设备")。
    * [安卓调试桥](<../zh-cn/Android_Debug_Bridge.html> "Android Debug Bridge")
  * 特殊U盘 / 带适配器的普通U盘
  * [蓝牙](<../zh-cn/%E8%93%9D%E7%89%99.html> "Bluetooth")
  * 与 Android 对应的 Arch Linux 软件 
    * 用于传输文件的协议（如[SSH](<../zh-cn/%E5%AE%89%E5%85%A8%E5%A4%96%E5%A3%B3%E5%8D%8F%E8%AE%AE.html> "SSH")、FTP、Samba 或 HTTP）的客户端或服务器。
    * [云同步客户端](</wzh/index.php?title=Cloud_synchronization_clients&action=edit&redlink=1> "Cloud synchronization clients（页面不存在）")
    * [Syncthing](</wzh/index.php?title=Syncthing&action=edit&redlink=1> "Syncthing（页面不存在）")
    * [sendanywhere](<https://aur.archlinux.org/packages/sendanywhere/>)AUR – 跨平台文件共享
    * [qrcp](<https://aur.archlinux.org/packages/qrcp/>)AUR –通过扫描二维码，使用 wifi 从电脑向移动设备传输文件
    * [localsend](<https://aur.archlinux.org/packages/localsend/>)AUR – 跨平台文件共享

##  应用开发

官方支持的构建 Android 应用程序的方式是使用 [#Android Studio](<#Android_Studio>)。[[1]](<https://developer.android.com/training/basics/firstapp/creating-project>)

### Android Studio

[Android Studio](<https://developer.android.com/studio/index.html>) 是基于 [IntelliJ IDEA](<https://en.wikipedia.org/wiki/IntelliJ_IDEA> "wikipedia:IntelliJ IDEA") 的官方 Android 开发环境。它为开发和调试提供了集成的 Android 开发者工具。 

通过 [android-studio](<https://aur.archlinux.org/packages/android-studio/>)AUR 进行安装。 

Android Studio在主目录下创建了一个`.android` 目录。要重置 Android Studio ，可以删除此目录。 

**注意：**

  * 请正确[设置 Java 环境](<../zh-cn/Java.html> "Java")，否则无法启动 android-studio。
  * 如果 Android Studio 显示为一个空白窗口，请尝试 [export](</wzh/index.php?title=Export&action=edit&redlink=1> "Export（页面不存在）")ing `_JAVA_AWT_WM_NONREPARENTING=1`， 见 [issue #57675](<https://code.google.com/p/android/issues/detail?id=57675>).

Android Studio 设置向导会安装所需的 [#SDK packages](<#SDK_packages>) ，默认的 SDK 目录是 `~/Android/Sdk`。 

要从命令行构建应用程序 (使用例如 `./gradlew assembleDebug`) 将 [ANDROID_HOME](<https://developer.android.com/studio/command-line/variables#android_home>) [环境变量](<../zh-cn/Environment_variable.html> "Environment variable")设置为你的SDK位置。 

###  SDK 软件包

Android SDK 包可以使用 [#Android Studio](<#Android_Studio>) 的 [SDK Manager](<https://developer.android.com/studio/intro/update#sdk-manager>) 或 [sdkmanager](<https://developer.android.com/studio/command-line/sdkmanager>) 命令行工具（Android SDK工具的一部分）直接从上游安装。 一些 Android SDK 包也可以使用 [AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR") 包， 它们通常安装在 `/opt/android-sdk/`中。 

[必须的软件包](<https://developer.android.com/studio/intro/update#recommended>) : 

Android SDK Package | SDK-style path | AUR package | AUR dummy | CLI tools   
---|---|---|---|---  
[Command-Line Tools](<https://developer.android.com/studio/releases/cmdline-tools>) | tools | [android-sdk-cmdline-tools-latest](<https://aur.archlinux.org/packages/android-sdk-cmdline-tools-latest/>)AUR | [android-sdk-cmdline-tools-latest-dummy](<https://aur.archlinux.org/packages/android-sdk-cmdline-tools-latest-dummy/>)AUR | apkanalyzer, avdmanager, lint, retrace, screenshot2, sdkmanager   
[SDK Build-Tools](<https://developer.android.com/studio/releases/build-tools>) | build-tools;_version_ | [android-sdk-build-tools](<https://aur.archlinux.org/packages/android-sdk-build-tools/>)AUR | [android-sdk-build-tools-dummy](<https://aur.archlinux.org/packages/android-sdk-build-tools-dummy/>)AUR | aapt, aapt2, aidl, apksigner, bcc_compat, d8, dexdump, dx, lld, llvm-rs-cc, mainDexClases, split-select, zipalign   
[SDK Platform-Tools](<https://developer.android.com/studio/releases/platform-tools>) | platform-tools | [android-sdk-platform-tools](<https://aur.archlinux.org/packages/android-sdk-platform-tools/>)AUR | [android-sdk-platform-tools-dummy](<https://aur.archlinux.org/packages/android-sdk-platform-tools-dummy/>)AUR |  [adb](<../zh-cn/Android_%E8%B0%83%E8%AF%95%E6%A1%A5.html> "Adb"), dmtracedump, e2fsdroid, etc1tool, [#fastboot](<#Fastboot>), hprof-conv, make_f2fs, make_f2fs_casefold, mke2fs, sload_f2fs, sqlite3, systrace   
[SDK Platform](<https://developer.android.com/studio/releases/platforms>) | platforms;android-_level_ |  [android-platform](<https://aur.archlinux.org/packages/android-platform/>)AUR, [older versions](<https://aur.archlinux.org/packages/?K=android-platform->) |  [android-platform-dummy](<https://aur.archlinux.org/packages/android-platform-dummy/>)AUR (unnecessary)   
  
[android-tools](<https://archlinux.org/packages/?name=android-tools>)包 软件包提供了 [adb](<../zh-cn/Android_Debug_Bridge.html> "Android Debug Bridge"), [#fastboot](<#Fastboot>)， `e2fsdroid` 和 `mke2fs.android`， SDK Platform-Tools along 提供了 `mkbootimg` 和 `ext2simg`。 

**注意：**

  * 由于Android SDK包含32位的二进制文件， 你必须启用 [multilib](<../zh-cn/%E5%AE%98%E6%96%B9%E4%BB%93%E5%BA%93.html> "Multilib") 仓库。否则你会得到 `error: target not found: lib32-*` 错误信息。
  * 如果你选择直接从上游安装 SDK 包，请安装 _AUR dummy_ 列的 AUR 包来拉入所需的依赖。
  * 如果你在试图运行 `sdkmanager` 时得到一个 `java.lang.NoClassDefFoundError` 异常，暂时使用 OpenJDK 8 的JRE，通过安装 [jre8-openjdk](<https://archlinux.org/packages/?name=jre8-openjdk>)包 并且 [切换 java 环境](<../zh-cn/Java.html#Switching_between_JVM> "Java")。 详见 [Failed to run sdkmanager --list with Java 9](<https://stackoverflow.com/questions/47150410/failed-to-run-sdkmanager-list-with-java-9>)

####  Android 模拟器

如下方式可以安装 [Android 模拟器](<https://developer.android.com/studio/run/emulator>)： `emulator` SDK 包、[android-emulator](<https://aur.archlinux.org/packages/android-emulator/>)AUR 软件包。如果 [android-emulator-dummy](<https://aur.archlinux.org/packages/android-emulator-dummy/>)AUR 可以作为占位空软件包使用。 

运行安卓模拟器需要英特尔或 ARM 系统镜像。可以通过 AUR 安装[[2]](<https://aur.archlinux.org/packages/?K=android-+system+image>)、 `sdkmanager` 或者 [AVD Manager](<https://developer.android.com/studio/run/managing-avds>) 进行安装。 

####  Making /opt/android-sdk group-writeable

[![](../File:Tango-inaccurate.png)](<../File:Tango-inaccurate.png>)**本文或本章节的事实准确性存在争议。**

**原因：** 请不要这样做。使用另一个软件包管理器 (Android SDK manager) 来管理 pacman 安装的文件是一个坏主意。这将使软件包管理器变得毫无用处。（在 [Talk:Android](<../zh-cn/Talk:Android.html>) 中讨论）

AUR 包将 SDK 安装在 `/opt/android-sdk/`。 这个目录有root [权限](<../zh-cn/%E6%96%87%E4%BB%B6%E6%9D%83%E9%99%90%E4%B8%8E%E5%B1%9E%E6%80%A7.html> "Permissions")，所以请注意 sdk 管理器正以 root 身份运行。如果你打算以普通用户身份使用它，创建 android-sdk 用户组，并添加你的用户。 
    
    # groupadd android-sdk
    # gpasswd -a <user> android-sdk
    
设置一个访问控制列表，让新创建的组的成员可以写入 android-sdk 文件夹中。由于运行 sdkmanager 也可以创建新的文件，将 ACL 设置为默认 ACL 。默认组项中的 X 意味着 "如果所有者（或其他任何用户）可执行，允许其执行" 
    
    # setfacl -R -m g:android-sdk:rwx /opt/android-sdk
    # setfacl -d -m g:android-sdk:rwX /opt/android-sdk  
    
重新登录或以 <user> 身份登录你的终端到新创建的组： 
    
    $ newgrp android-sdk
    
###  其他的 IDEs

Android Studio 是基于 IntelliJ IDEA 的官方 Android 开发环境。另外，你也可以使用 [Netbeans](</wzh/index.php?title=Netbeans&action=edit&redlink=1> "Netbeans（页面不存在）") 的 NBAndroid-V2。介绍如下。 

#### Netbeans

如果你喜欢使用 [Netbeans](</wzh/index.php?title=Netbeans&action=edit&redlink=1> "Netbeans（页面不存在）") 作为你的 IDE，并想开发 Android 应用程序，请使用 [NBAndroid-V2](<https://github.com/NBANDROIDTEAM/NBANDROID-V2>) 。 

安装 [android-sdk](<https://aur.archlinux.org/packages/android-sdk/>)AUR 包 并遵循 [NBANDROID README](<https://github.com/NBANDROIDTEAM/NBANDROID-V2/blob/master/README.md>) 的指示。 

####  Vim / Neovim

可以使用 (Neo)vim 像 IDE 一样为 Android 和 iOS 编写 `flutter` 应用程序。使用 [Vim插件管理器](<../zh-cn/Vim.html#Using_a_plugin_manager> "Vim")安装 [coc](<https://github.com/neoclide/coc.nvim>) 。同时安装 [coc-flutter](<https://github.com/iamcco/coc-flutter>) 扩展，用于代码补全（像在 Android Studio 中），并将代码加载到 Android 模拟器中。 

#### Emacs

要使用 Emacs 开发一个移动的 `flutter` 应用程序，正如 [flutter.dev](<https://flutter.dev/docs/get-started/editor?tab=emacs>) 的官方说明所建议的，安装 [lsp-dart](<https://emacs-lsp.github.io/lsp-dart/>)。 

###  其他工具

#### Marvin

Marvin 是一个帮助初学者建立 Android 开发环境的工具。安装 [marvin_dsc](<https://aur.archlinux.org/packages/marvin_dsc/>)AUR 可以帮助你设置以下东西：JDK、Android SDK、IDE(s) 和 AVD。 

##  编译

Please note that these instructions are based on the [official AOSP build instructions](<https://source.android.com/source/building>). Other Android-derived systems such as LineageOS will often require extra steps. 

[![](../File:Tango-view-refresh-red.png)](<../File:Tango-view-refresh-red.png>)**本文或本节内容已经过时。**

**原因：** The upstream [envsetup.sh](<https://android.googlesource.com/platform/build/+/refs/heads/master/envsetup.sh>) script uses python3, not python2 as described in this section. (在[Talk:Android](<../zh-cn/Talk:Android.html>)讨论)

### Required packages

**注意：** Before doing the following steps, the [multilib](<../zh-cn/%E5%AE%98%E6%96%B9%E4%BB%93%E5%BA%93.html> "Multilib") repository must be enabled in `/etc/pacman.conf`.

To build AOSP 13 you need a TTF font installed (e.g. [ttf-dejavu](<https://archlinux.org/packages/?name=ttf-dejavu>)包) and the dependencies of the [aosp-devel](<https://aur.archlinux.org/packages/aosp-devel/>)AUR metapackage. 

Additionally, LineageOS (as well as other many Android distributions like ArrowOS,PixelExperience etc) requires the following dependencies of the [lineageos-devel](<https://aur.archlinux.org/packages/lineageos-devel/>)AUR metapackage. 

### Java Development Kit

The [required JDK version](<https://source.android.com/source/requirements>) depends on the Android version you are building: 

  * For Android 9 (Pie) and up, Java is included with the Android source and no separate installation is needed.
  * For Android 7 and 8 (Nougat and Oreo), OpenJDK 8 is required, which is available with the [jdk8-openjdk](<https://archlinux.org/packages/?name=jdk8-openjdk>)包 package.

**注意：** For older Android versions, where Java is not included, Java is expected to be in `/usr/lib/jvm/java-_version_ -openjdk-amd64`. 

Set JAVA_HOME to avoid this requirement and match the Arch Linux installation path. Example: 
    
    $ export JAVA_HOME=/usr/lib/jvm/java-_version_ -openjdk
    
This change will be valid only for the current terminal session.

### Setting up the build environment

[Install](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "Install") the [repo](<https://archlinux.org/packages/?name=repo>)包 package. 

Create a directory to build. 
    
    $ mkdir ~/android
    $ cd ~/android
    
**注意：** Do not build under a directory where you do not have read/write access.

### Downloading the source code

This will clone the repositories. You **only** need to do this the first time you build Android, or if you want to switch branches. 

  * The `repo` has a `-j` switch that operates similarly to the one used with `make`. Since it controls the number of simultaneous downloads, you should adjust the value depending on downstream network bandwidth.

  * You will need to specify a **branch** ([list of branches](<https://android.googlesource.com/platform/manifest/+refs>)) to check out with the `-b` switch. If you leave the switch out, you will get the so-called **master branch**.

    $ repo init -u <https://android.googlesource.com/platform/manifest> -b master
    $ repo sync -j4
    
**注意：** To further decrease sync times, you can use the `-c` switch with the _repo_ command as such: 
    
    $ repo sync -j8 -c
    
The `-c` switch will only sync the branch which is specified in the manifest, which in turn is determined by the branch specified with the `-b` switch, or the default branch set by the repository maintainer. 

Wait a long time. Just the uncompiled source code, along with the `.repo` and `.git` directories that are used to keep track of it, are very large. As of Android 10, at least 250 GB of free disk space is [required](<https://source.android.com/setup/build/requirements>). 

**注意：** If you want to update your local copy of the Android source, at a later time, simply enter the build directory, load the Virtualenv, and re-sync: 
    
    $ repo sync
    
### Building the code

This should do what you need for AOSP: 
    
    $ source build/envsetup.sh
    $ lunch full-eng
    $ make -j4
    
If you run **lunch** without arguments, it will ask what build you want to create. Use -j with a number between one and two times number of cores/threads. 

The build takes a very long time. 

**注意：**

  * Make sure you have enough RAM. Android will use the `/tmp` directory heavily. By default the size of `/tmp` is half the size of your RAM. If it fills up, the build will fail. 4 GiB of RAM or more is recommended. If `/tmp` is not large enough, you can [increase it](<../zh-cn/Tmpfs.html#Examples> "Tmpfs"). Make sure you have the combined RAM and swap space to back it. Alternatively, you can get rid of the tmpfs from [fstab](<../zh-cn/Fstab.html> "Fstab") all together.
  * From the [Android Building and Running guide](<https://source.android.com/source/building#build-the-code>):

    GNU make can handle parallel tasks with a `-jN` argument, and it is common to use a number of tasks N that is between 1 and 2 times the number of hardware threads on the computer being used for the build. E.g. on a dual-E5520 machine (2 CPUs, 4 cores per CPU, 2 threads per core), the fastest builds are made with commands between `make -j16` and `make -j32`.

### Testing the build

When finished, run/test the final image(s). 
    
    $ emulator
    
### Creating a flashable Image

To create an image that can be flashed it is necessary to: 
    
    make -j8 updatepackage
    
This will create a zip image under `**out/target/product/hammerhead**` (hammerhead being the device name) that can be flashed. 

## Flashing

In some cases, you want to return to the stock Android after flashing custom ROMs to your Android mobile device. For flashing instructions of your device, please use [XDA forums](<https://forum.xda-developers.com/>). 

### Fastboot

Fastboot (as well as [ADB](<../zh-cn/Android_%E8%B0%83%E8%AF%95%E6%A1%A5.html> "ADB")) is included in the [android-tools](<https://archlinux.org/packages/?name=android-tools>)包 package. 

**注意：**

  * Restoring firmwares using `fastboot` can be quite tricky, but you might want to browse [XDA developers forums](<https://www.xda-developers.com/>) for a stock firmware, which is mostly a `*.zip` file, but inside of it, comes with the firmware files and `flash-all.sh` script. For example, [Google Nexus](<https://developers.google.com/android/nexus/images>) firmwares include `flash-all.sh` script or another example could be for OnePlus One - [XDA thread](<https://forum.xda-developers.com/oneplus-one/general/guide-return-opo-to-100-stock-t2826541>), where you can find firmwares with included `flash-all.sh` script.
  * If you get a `no permissions` error or execution just hangs with `< waiting for any device >` then you need to run `fastboot` as the root user. Alternatively you can install [android-udev](<https://archlinux.org/packages/?name=android-udev>)包 or the AUR package [android-udev-git](<https://aur.archlinux.org/packages/android-udev-git/>)AUR and reconnect your device.

### Samsung devices

Samsung devices cannot be flashed using **Fastboot** tool. Alternatives are [Heimdall](<#Heimdall>) and [Odin](<#Odin_\(Virtualbox\)>) (by using Windows and VirtualBox). 

#### samloader

To download original Samsung firmware, a platform independent script, [samloader](<https://github.com/nlscc/samloader>) can be used. 

#### Heimdall

[Heimdall](<https://glassechidna.com.au/heimdall/>) is a cross-platform open-source tool suite used to flash firmware (also known as ROMs) onto Samsung mobile devices and is also known as an alternative to [Odin](<https://odindownload.com/>). It can be installed as [heimdall](<https://archlinux.org/packages/?name=heimdall>)包. 

The flashing instructions can be found on Heimdall's [GitHub repository](<https://github.com/Benjamin-Dobell/Heimdall/tree/master/Linux>) or on [XDA forums](<https://forum.xda-developers.com/showthread.php?t=1922461>). 

####  Odin (Virtualbox)

**注意：** This section only covers preparation and **not** flashing instructions. Search [XDA developers forums](<https://www.xda-developers.com>) to find flashing instructions for a specific device. For example, [Samsung Galaxy S4](<https://forum.xda-developers.com/showthread.php?t=2265477>).

It is also possible to restore [firmware (Android)](<https://www.sammobile.com/firmwares/>) on the Samsung devices using [Odin](<https://odindownload.com/>), but inside the [VirtualBox](<../zh-cn/VirtualBox.html> "VirtualBox"). 

Arch Linux (host) preparation: 

  1. Install [VirtualBox](<../zh-cn/VirtualBox.html> "VirtualBox") together with its [extension pack](<../zh-cn/VirtualBox.html#Extension_pack> "VirtualBox") and [guest additions](<../zh-cn/VirtualBox.html#Guest_additions_disc> "VirtualBox").
  2. Install your preferred, but compatible with Odin, Windows operating system (with VirtualBox guest additions) into a virtual hard drive using VirtualBox.
  3. Open VirtualBox settings of your Windows operating system, navigate to _USB_ , then tick (or make sure it is ticked) **Enable USB 2.0 (EHCI) Controller**.
  4. At VirtualBox running Windows operating system, click in the menu bar _Devices > USB Devices_, then click on your Samsung mobile device from the list, which is connected to your computer via USB.

Windows (guest) preparation: 

  1. Install [Samsung drivers](<https://androidxda.com/download-samsung-usb-drivers>).
  2. Install [Odin](<https://odindownload.com/>).
  3. Download required [Samsung firmware (Android)](<https://www.sammobile.com/firmwares/>) for your smartphone model.

Check if configuration is working: 

  1. Turn your device into Download mode and connect to your Linux machine.
  2. In virtual machine toolbar, select _Devices > USB > ...Samsung..._ device.
  3. Open Odin. The white box (a big one at the bottom-left side) named **Message** , should print a line similar to this:

    <ID:0/003> Added!!
    
which means that your device is visible to Odin & Windows operating system and is ready to be flashed. 

##  在 Arch Linux 运行 Android 应用

一些工具致力于在 Arch Linux （或其他发行版）下运行 Android 程序，如下表所示： 

  * [基于容器](<https://en.wikipedia.org/wiki/Containerization_\(computing\)> "wikipedia:Containerization \(computing\)")的技术应当是最流行的。这些技术是在 Android 以外的 Linux 内核中使用 Android 应用最原生的方式，对系统的兼容性、运行性能都是最强大的。其中值得注意的有： 
    * [Anbox](<../zh-cn/Anbox.html> "Anbox") 是 Linux 最流行的 Android 容器技术。它在 Lineageos 中运行 Android 7.1 镜像。
    * [Waydroid](<../zh-cn/Waydroid.html> "Waydroid") 是 Anbox 的一个分支，正在变得流行。它更贴近硬件，也就更加高效。它基于 Lineageos 17.1 （Android 10）镜像，提供安装 Google Play Store 与其他开源应用的选项。在独立窗口中运行 Android 程序，它也提供完整的 Android UI。

  * 一些 Chromium 扩展也可运行 Android 应用： 
    * **Arc Welder** 是谷歌在 Chrome OS 中测试新应用的扩展，目前已经弃用。
    * [ARChon](<https://archon-runtime.github.io/>) 是在基于 Chromium 的浏览器中运行 Android 应用的开源扩展。
  * 当然也可以运行完整的 Android 模拟器。它的优势是你可以在 x86 平台上运行 arm 应用，劣势则是它的性能不佳。以下是几个例子： 
    * [Android studio 内置模拟器](<#Android_Emulator>)，正如前文所示。
    * [Genymotion](<https://www.genymotion.com/>) 是 Android 模拟、测试的套装。

**提示：** 如果你想运行基于 x86 的安卓应用，同时愿意另外安装操作系统，你可以使用 [Android-x86](<https://www.android-x86.org/>)：Android 在 x86 的移植。

##  故障排除

###  Android Studio: Android Virtual Devices show 'failed to load'.

确保按 [#Android Studio](<#Android_Studio>) 中的说明正确设置环境变量 `ANDROID_HOME`。 

###  Android Studio: 'failed to create the SD card'

如果你试图在 x86_64 Arch下运行AVD（Android Virtual Device）并得到上述错误，请从 [multilib](<../zh-cn/%E5%AE%98%E6%96%B9%E4%BB%93%E5%BA%93.html> "Multilib") 仓库安装 [lib32-gcc-libs](<https://archlinux.org/packages/?name=lib32-gcc-libs>)包 软件包。 

###  Eclipse: During Debugging "Source not found"

最有可能的是，调试器想要跳到 Java 源代码中。由于安卓的源代码并不随 Android SDK 一起提供，这就导致了错误。最好的解决办法是使用步骤过滤器，不要跳到 Java 源代码中。默认情况下，步骤过滤器没有被激活。要激活它们： _Window > Preferences > Java > Debug > Step Filtering_. 考虑将它们全部选中。如果合适，你可以添加 android.* 包。参见[使用步骤过滤器](<https://help.eclipse.org/latest/index.jsp?topic=%2Forg.eclipse.jdt.doc.user%2Freference%2Fviews%2Fdebug%2Fref-usestepfilters.htm>)。 

### ValueError: unsupported pickle protocol

一个解决方案是： 
    
    $ rm ~/.repopickle_.gitconfig
    
如果这不起作用，那就试试这个： 
    
    $ find /path/to/android-root -name .repopickle_config -delete
    
### libGL error: failed to load driver: swrast OR AVD does not load and no error message displayed

Sometimes, beginning to load an AVD will cause an error message similar to this to be displayed, or the loading process will appear to finish but no AVD will load and no error message will be displayed. 

The AVD loads an incorrect version of libstdc++, you can remove the folder libstdc++ from `~/.android-sdk/emulator/lib64` (for 64-bit) or `~/.android-sdk/emulator/lib` (for 32-bit) , e.g.: 
    
    $ rm -r ~/.android-sdk/emulator/lib64/libstdc++
    
Note that in versions before Android Studio 3.0, this directory was in a different location: 
    
    $ rm -r ~/Android/Sdk/emulator/lib64/libstdc++
    
Alternatively you can set and export ANDROID_EMULATOR_USE_SYSTEM_LIBS in ~/.profile as: 
    
    export ANDROID_EMULATOR_USE_SYSTEM_LIBS=1
    
Reference: [Android Studio user guide](<https://developer.android.com/studio/command-line/variables.html#studio_jdk>)

Fix for the .desktop file might be achieved by using env command, prefixing the Exec line [Desktop entries#Modify environment variables](<../zh-cn/Desktop_entries.html#Modify_environment_variables> "Desktop entries")
    
    env ANDROID_EMULATOR_USE_SYSTEM_LIBS=1
    
### sh: glxinfo: command not found

以下是完整的错误： 
    
    Cannot launch AVD in emulator.
    Output:
    sh: glxinfo: command not found
    sh: glxinfo: command not found
    libGL error: unable to load driver: swrast_dri.so
    libGL error: failed to load driver: swrast
    X Error of failed request:  BadValue (integer parameter out of range for operation)
      Major opcode of failed request:  154 (GLX)
      Minor opcode of failed request:  24 (X_GLXCreateNewContext)
      Value in failed request:  0x0
      Serial number of failed request:  32
      Current serial number in output stream:  33
    QObject::~QObject: Timers cannot be stopped from another thread
    
你可以尝试安装 glxinfo([mesa-utils](<https://archlinux.org/packages/?name=mesa-utils>)包)，但如果你的电脑有足够的能力，你可以简单地使用软件来渲染图形。要做到这一点，进入 _Tools > Android > AVD Manager_ ，编辑 AVD（点击铅笔图标），然后选择 _Software_ \- GLES 2.0 用于 _Emulated Performance > Graphics_ 。 

### Android Emulator: no keyboard input in xfwm4

In xfwm4, the vertical toolbar buttons window that is on the right of the emulator takes focus from the emulator and consumes keyboard events. ([bug report](<https://issuetracker.google.com/issues/37094173>)) 

You can use the workaround described in [[3]](<https://stackoverflow.com/a/42720450>): 

  1. Open the xfwm4 settings.
  2. Switch to the Focus tab.
  3. Change the Focus Model to "Focus follow mouse".
  4. Disable _Automatically raise windows when they receive focus_ option below.\

###  Android 模拟器: 在 WM 平铺模式下使用时，窗口晃动和闪动

当使用像 [dwm](<../zh-cn/Dwm.html> "Dwm") 这样的平铺窗口管理器时，安卓模拟器会摇晃和闪烁。你可以使用 [krohnkite issue 72](<https://github.com/esjeon/krohnkite/issues/72#issuecomment-613789987>) 中描述的解决方法（窗口浮动是由 [dwm](<../zh-cn/Dwm.html> "Dwm") 的 `Alt+f` 引起的）。 

###  Android Emulator: Segmentation fault (core dumped)

When using [Nouveau](<../zh-cn/Nouveau.html> "Nouveau") drivers try to disable gpu hardware acceleration. 

In some devices it can only be done by editing `$HOME/.avd/_device_name_.avd/config.ini`.[[4]](<https://stackoverflow.com/a/58376934>)

  1. Set `hw.gpu.enabled=no`
  2. Set `hw.gpu.mode=off`

###  Android Emulator: Not launching / qemu-system: address resolution failed

There is an issue where no emulator-window shows up after starting a virtual device in android-studio. If this applies to you, launch the emulator from the console and inspect its output: 
    
    $ emulator -avd $(emulator -list-avds)
    
If on any line, it says anything similar to: 
    
    qemu-system-x86_64 : address resolution failed for ::1:46189: Name or service not known
    
you may try disabling IPv6: 
    
    $ sysctl net.ipv6.conf.all.disable_ipv6=1
    
If this solves the issue and the virtual device shows up in android-studio, you may consider a permanent change: 
    
    $ echo "net.ipv6.conf.all.disable_ipv6=1" | sudo tee -a /etc/sysctl.d/99-sysctl.conf
    
### adb: sideload connection failed: insufficient permissions for device

如果得到如下错误： 
    
    adb: sideload connection failed: insufficient permissions for device
    See [[https://developer.android.com/tools/device.html](<https://developer.android.com/tools/device.html>)] for more information
    
或者 
    
    adb: trying pre-KitKat sideload method...
    adb: pre-KitKat sideload connection failed: insufficient permissions for device
    See [[https://developer.android.com/tools/device.html](<https://developer.android.com/tools/device.html>)] for more information
    
尝试重启 adb 服务器，看能否解决这个问题： 
    
     $ adb kill-server
     # adb start-server
    
或者，确保已经安装了 Android 的 [udev 规则](<../zh-cn/Udev.html#About_udev_rules> "Udev")。 参见 [#Fastboot](<#Fastboot>). 
