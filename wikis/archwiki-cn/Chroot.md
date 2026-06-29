**翻译状态：**

  * 本文（或部分内容）译自 [Chroot](<https://wiki.archlinux.org/title/Chroot> "arch:Chroot")，最近一次同步于 2022-05-10，若英文版本有所[更改](<https://wiki.archlinux.org/title/Chroot?diff=0&oldid=723126>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Chroot_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[Chroot](<https://en.wikipedia.org/wiki/Chroot> "wikipedia:Chroot") 是一种修改当前进程及其子进程的可见根目录的操作。修改后，进程将不能访问该环境目录树以外的任何文件和命令，这种修改后的环境叫作 _chroot jail_ （直译为 chroot 监狱）。 

##  原因

改变根目录通常是为了在无法启动或登录的系统上进行系统维护，例如： 

  * 重新安装 [bootloader](<../zh-cn/Arch_%E7%9A%84%E5%90%AF%E5%8A%A8%E6%B5%81%E7%A8%8B.html#%E5%BC%95%E5%AF%BC%E5%8A%A0%E8%BD%BD%E7%A8%8B%E5%BA%8F> "Bootloader")。
  * 重建 [initramfs 镜像](<../zh-cn/Mkinitcpio.html> "Mkinitcpio")。
  * 升级或[降级软件包](<../zh-cn/Downgrading_packages.html> "Downgrading packages")。
  * 重置[忘记的密码](<../zh-cn/Password_recovery.html> "Password recovery")。
  * 在[在干净的 chroot 环境中构建](<../zh-cn/%E5%88%9B%E5%BB%BA%E4%B8%80%E4%B8%AA%E5%B9%B2%E5%87%80%E7%9A%84_chroot.html> "创建一个干净的 chroot")中构建软件包。

另见 [Wikipedia:Chroot#Limitations](<https://en.wikipedia.org/wiki/Chroot#Limitations> "wikipedia:Chroot")。 

##  必要条件

  * root 权限
  * 另一个 linux 环境，例如 liveCD、USB 闪存介质或者一个已经安装的另一个 linux 发行版。
  * 匹配的架构，chroot 前后的环境架构要一致(例如，都是 i686 或 x86_64)。可以用以下命令查看当前环境的架构 
        
        uname -m

  * 提前加载 chroot 环境需要的内核模块
  * 如果需要 [swap](<../zh-cn/Swap.html> "Swap")， chroot 前先启用 swap （`swapon /dev/sdxY`）
  * 如果需要网络，chroot 之前先建立好网络连接。

##  用法

**注意：**

  * 有些[systemd](<../zh-cn/Systemd.html> "Systemd") 工具无法在 chroot 中运行，例如 _hostnamectl_ 、 _localectl_ 和 _timedatectl_ ，因为这些程序需要可用的 [dbus](<../zh-cn/D-Bus.html> "Dbus") 连接。 [[1]](<https://github.com/systemd/systemd/issues/798#issuecomment-126568596>)
  * 新的 root (`/`) 所在的文件系统必须是可用访问的状态(提前解密、[挂载](<../zh-cn/File_systems.html#%E6%8C%82%E8%BD%BD%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F> "File systems"))。

有两种使用 chroot 的方式： 

###  使用 arch-chroot

`arch-chroot` bash 脚本是软件包 [arch-install-scripts](<https://archlinux.org/packages/?name=arch-install-scripts>)包 的一部分，在运行 `/usr/bin/chroot` 前，这个脚本会挂载类似 `/proc` 的 API 文件系统，建立可用的 `/etc/resolv.conf`。 

进入 chroot 
    
    # arch-chroot _/location/of/new/root_
    
例如在[安装指南](<../zh-cn/Installation_guide.html> "Installation guide")中，chroot 到 `/mnt`: 
    
    # arch-chroot /mnt
    
退出 chroot: 
    
    # exit
    
####  运行一个命令并退出

用下面命令在 chroot 中运行一个命令并退出： 
    
    # arch-chroot _/location/of/new/root_ _mycommand_
    
例如要在 `/mnt/arch` 中运行 `mkinitcpio -p linux` 并退出: 
    
    # arch-chroot /mnt/arch mkinitcpio -p linux
    
###  使用 chroot

**警告：** 使用 `--rbind` 选项时，将无法卸载某些 `dev/` 和 `sys/` 的子目录，用 `umount -l` 卸载将会破坏会话并需要重启，所以请尽可能使用 `-o bind`。

在下面的例子中，` _/location/of/new/root_` 代指新的根目录所在的文件夹。 首先，临时挂载 API 文件系统： 
    
    # cd _/location/of/new/root_
    # mount -t proc /proc proc/
    # mount -t sysfs /sys sys/
    # mount --rbind /dev dev/
    
可选挂载: 
    
    # mount --rbind /run run/
    
如果正运行在 UEFI 系统，则还需要能够访问 EFI 变量，不然在安装 GRUB 时会得到类似这样的消息：`UEFI variables not supported on this machine`： 
    
    # mount --rbind /sys/firmware/efi/efivars sys/firmware/efi/efivars/
    
如果已经建立了一个网络连接并且想在 chroot 环境中继续使用，将 DNS 服务器配置复制到新环境： 
    
    # cp -L /etc/resolv.conf etc/resolv.conf
    
chroot 到新环境中并启用指定 shell 
    
    # chroot /mnt/arch /usr/bin/bash
    
**注意：**

  * 如果遇到错误 `chroot: cannot run command '/bin/bash': Exec format error`，很可能是因为两个环境架构不匹配。
  * 如果遇到错误 `chroot: '/usr/bin/bash': permission denied`,用执行权限重新挂载: `mount -o remount,exec _/location/of/new/root_`。 
    * 如果以上方式无效，那么请[确保](<https://www.tldp.org/LDP/LG/issue52/okopnik.html>)新环境的基础组件完整（如果是 Arch 根目录，请尝试 `paccheck --root=_/location/of/new/root_ --files --file-properties --md5sum glibc filesystem`，来自 [pacutils](<https://archlinux.org/packages/?name=pacutils>)包）。

（可选）加载 Bash 配置文件(`~/.bashrc` 和 `/etc/bash.bashrc`)，运行： 
    
    # source ~/.bashrc
    # source /etc/profile
    
或创建一个独特的提示符来区别你的chroot环境： 
    
    # export PS1="(chroot) $PS1"
    
退出 chroot 环境： 
    
    # exit
    
然后卸载临时文件系统: 
    
    # cd /
    # umount --recursive _/location/of/new/root_
    
如果出现 `/mnt`(或其它任何分区) is busy, 这可能意味着： 

  * chroot环境中残留了一个运行的程序或者还有分区没有被卸载，退出程序并用 `findmnt -R _/location/of/new/root_` 查找然后卸载未卸载的分区。
  * 如果你仍然不能卸载分区，使用`--force`选项：
        
        # umount -f /mnt

， 或使用 `umount --lazy` 直接释放挂载。这是，请立即重启系统以避免不一致的状态导致冲突。

##  在 chroot 中运行图形程序

如果系统上运行了[X](<../zh-cn/Xorg.html> "X")，可以在 chroot 环境启动图形应用。 

为了chroot环境能连接到你的X服务器，在X服务器中打开一个终端(例如，在用户当前登录的桌面中)，然后运行如下命令给任何人连接到用户X服务器的权限(另见 [Xhost](<../zh-cn/Xhost.html> "Xhost"))： 
    
    $ xhost +local:
    
然后，从chroot环境中将应用指向你的X服务器，将chroot中的DISPLAY环境变量设定成和拥有X服务器的用户DISPLAY变量相匹配。例如运行： 
    
    $ echo $DISPLAY
    
作为拥有X服务器的用户查看DISPLAY的值。如果是“:0”(例如是)，然后在chroot环境中运行 
    
    # export DISPLAY=:0
    
现在就可以从chroot命令行启动图形界面应用 

##  不使用 root 权限

Chroot 需要 root 权限，有时用户并没有这个权限，下面工具可用实现类似的功能： 

### PRoot

[PRoot](<../zh-cn/PRoot.html> "PRoot") 可用在没有 root 权限的情况下，用 `mount --bind` 设置可见根目录，这样可用为不同的 CPU 架构编译程序。这个程序的缺点是文件属于主机系统。可用用 `--root-id` 选项解决一部分问题。 

### Fakechroot

[fakechroot](<https://archlinux.org/packages/?name=fakechroot>)包 是一个拦截 chroot 调用并伪造结果的程序。用 [fakeroot](<https://archlinux.org/packages/?name=fakeroot>)包 可用为普通用户伪造一个 chroot 环境： 
    
    $ fakechroot fakeroot chroot ~/my-chroot bash
    
### Unshare

Unshare 是 [util-linux](<https://archlinux.org/packages/?name=util-linux>)包 的一部分，可以用来创建新的内核命名空间。它使用常规的 chroot 命令运行，例如： 
    
    $ unshare --map-root-user chroot ~/namespace /bin/sh
    
##  疑难解答

###  arch-chroot: /location/of/new/root is not a mountpoint. This may have undesirable side effects.

执行 `arch-chroot _/location/of/new/root_` 命令后，出现以下警告： 
    
    ==> WARNING: _/location/of/new/root_ is not a mountpoint. This may have undesirable side effects.
    
见 [arch-chroot(8)](<https://man.archlinux.org/man/arch-chroot.8>) 中的解释和使用绑定挂载让 chroot 目录变成挂载点的例子。 

##  另见

  * [基础 Chroot](<https://help.ubuntu.com/community/BasicChroot>)
