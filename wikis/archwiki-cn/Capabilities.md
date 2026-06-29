**翻译状态：**

  * 本文（或部分内容）译自 [Capabilities](<https://wiki.archlinux.org/title/Capabilities> "arch:Capabilities")，最近一次同步于 2025-03-04，若英文版本有所[更改](<https://wiki.archlinux.org/title/Capabilities?diff=0&oldid=815966>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Capabilities_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

**能力（capability）** 是 POSIX 1003.1e 标准引入的功能，手册说明参见 [capabilities(7)](<https://man.archlinux.org/man/capabilities.7>)。它允许使用更小的粒度控制超级管理员权限，可以避免 root 权限的滥用。软件开发者应当尽可能为二进制文件赋予最小权限，而不是过度使用强大的 [setuid](<https://en.wikipedia.org/wiki/Setuid> "wikipedia:Setuid")。Arch Linux 中很多软件包用了 capability，例如 [fping](<https://archlinux.org/packages/?name=fping>)包 中的 `fping` 就使用了 `CAP_NET_RAW` （能力的一种）。这样一来，普通用户也可以正常执行 `fping`，效果与使用 **setuid** 相似，同时减少了 `fping` 的潜在安全隐患。 

##  实现

在 Linux 中，能力通过 _security_ 名空间下的[扩展属性](<../zh-cn/%E6%96%87%E4%BB%B6%E6%9D%83%E9%99%90%E4%B8%8E%E5%B1%9E%E6%80%A7.html#%E6%89%A9%E5%B1%95%E5%B1%9E%E6%80%A7> "文件权限与属性")（详见[xattr(7)](<https://man.archlinux.org/man/xattr.7>)）实现。主流 Linux [文件系统](<../zh-cn/%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F.html> "文件系统")均支持扩展属性 ，包括Ext2，Ext3，Ext4，Btrfs，JFS，XFS 和 Reiserfs 等。 

下面的示例使用 `getcap` 显示“fping”的能力（Capabilities），以及通过 `getfattr` 显示其编码后的“fping”的能力信息。 
    
    $ getcap /usr/bin/fping
    
    /usr/bin/fping = cap_net_raw+ep
    
    $ getfattr -d -m "^security\\." /usr/bin/ping
    
    # file: usr/bin/ping
    security.capability=0sAQAAAgAgAAAAAAAAAAAAAAAAAAA=

部分程序能够自动保留文件的扩展属性，但更多的情况下需要单独指定参数，详情可以参考页面[文件权限与属性#保留扩展属性](<../zh-cn/%E6%96%87%E4%BB%B6%E6%9D%83%E9%99%90%E4%B8%8E%E5%B1%9E%E6%80%A7.html#%E4%BF%9D%E7%95%99%E6%89%A9%E5%B1%95%E5%B1%9E%E6%80%A7> "文件权限与属性")。 

在 Arch 中, 能力可以通过包的[安装脚本](<../zh-cn/PKGBUILD.html#install> "PKGBUILD")（如 [fping](<https://archlinux.org/packages/?name=fping>)包 中的 [[1]](<https://gitlab.archlinux.org/archlinux/packaging/packages/fping/-/blob/main/fping.install%7Cfping.install>)）设置。 

##  管理和维护

如果一个软件包设置了过度宽松的能力，那应当被视为一个错误（bug）并上报, 而不是在这里列举出来。 同时，因为Arch不支持 [MAC/RBAC](<../zh-cn/%E5%AE%89%E5%85%A8.html#%E5%BC%BA%E5%88%B6%E8%AE%BF%E9%97%AE%E6%8E%A7%E5%88%B6> "Security") ，所以设置 `CAP_SYS_ADMIN` 或 `CAP_DAC_OVERRIDE` ，不应当被视为错误（bug）。 

**警告：** 过多的能力会可能会导致权限问题。可以在 Brad Spengler的帖子中查看例子和解释：[False Boundaries and Arbitrary Code Execution](<https://forums.grsecurity.net/viewtopic.php?f=7&t=2522&sid=c6fbcf62fd5d3472562540a7e608ce4e#p10271>).

##  其他从capabilities受益的程序

下面列举的软件中没有使用 setuid 属性的文件，但是他们中的部分命令需要 root 权限才能正常使用。通过设置能力，普通用户可以在不提升权限的情况下使用这些软件。 

下文中能力后面的 `+ep` 表示相关能力标记为 _生效（effective）_ 和 _允许（permitted）_ 。更多信息请参阅 [capabilities(7) § File capabilities](<https://man.archlinux.org/man/capabilities.7#File_capabilities>)

软件 | 执行命令（以 root 权限执行）   
---|---  
[beep(1)](<https://man.archlinux.org/man/beep.1>) |  `setcap cap_dac_override,cap_sys_tty_config+ep /usr/bin/beep`  
[chvt(1)](<https://man.archlinux.org/man/chvt.1>) |  `setcap cap_dac_read_search,cap_sys_tty_config+ep /usr/bin/chvt`  
[iftop(8)](<https://man.archlinux.org/man/iftop.8>) |  `setcap cap_net_raw+ep /usr/bin/iftop`  
[mii-tool(8)](<https://man.archlinux.org/man/mii-tool.8>) |  `setcap cap_net_admin+ep /usr/bin/mii-tool`  
[nethogs(8)](<https://man.archlinux.org/man/nethogs.8>) |  `setcap cap_net_admin,cap_net_raw+ep /usr/bin/nethogs`  
[wavemon(1)](<https://man.archlinux.org/man/wavemon.1>) |  `setcap cap_net_admin+ep /usr/bin/wavemon`  
  
在 ArchLinux 中，部分软件（例如 [mtr](<https://archlinux.org/packages/?name=mtr>)包）已经在其打包所使用的 `.install` 文件中配置了所需的“能力”。 因此部分软件不需要手动执行上面的命令。 

##  实用命令

找到具有 setuid-root 权限的文件: 
    
    $ find /usr/bin /usr/lib -perm /4000 -user root
    
找到具有 setgid-root 权限的文件: 
    
    $ find /usr/bin /usr/lib -perm /2000 -group root
    
##  为程序临时授予能力

[capsh(1)](<https://man.archlinux.org/man/capsh.1>)可以以指定的能力运行程序，而不需要修改文件扩展属性。 

下面的例子展示了如何为 [gdb(1)](<https://man.archlinux.org/man/gdb.1>) 赋予 `CAP_SYS_PTRACE` 能力来调试程序： 
    
    $ sudo -E capsh --caps="cap_setpcap,cap_setuid,cap_setgid+ep cap_sys_ptrace+eip" --keep=1 --user="$USER" --addamb="cap_sys_ptrace" --shell=/usr/bin/gdb -- -p <pid>
    
上面的命令用 `-E` 参数是 [sudo](<../zh-cn/Sudo.html> "Sudo") 命令中，保留当前用户环境变量的参数。详细说明参阅 [sudo(8)](<https://man.archlinux.org/man/sudo.8>)。 

[nc(1)](<https://man.archlinux.org/man/nc.1>) 监听低端口号的例子： 
    
    $ sudo -E capsh --caps="cap_setpcap,cap_setuid,cap_setgid+ep cap_net_bind_service+eip" --keep=1 --user="$USER" --addamb="cap_net_bind_service" --shell=/usr/bin/nc -- -lvtn 123
    Listening on 0.0.0.0 123
    
## systemd

可以使用 `AmbientCapabilities` 和 `CapabilityBoundingSet` 为 systemd 单元分配能力，相较于在二进制文件上设置能力，这种方式更安全。参见 [systemd.exec(5)](<https://man.archlinux.org/man/systemd.exec.5>)。 

##  参阅

  * Man Pages: [capabilities(7)](<https://man.archlinux.org/man/capabilities.7>), [setcap(8)](<https://man.archlinux.org/man/setcap.8>), [getcap(8)](<https://man.archlinux.org/man/getcap.8>)
  * [Wikibooks:Grsecurity/Appendix/Capability Names and Descriptions](<https://en.wikibooks.org/wiki/Grsecurity/Appendix/Capability_Names_and_Descriptions> "wikibooks:Grsecurity/Appendix/Capability Names and Descriptions")
  * [Seccomp BPF (SECure COMPuting with filters)](<https://docs.kernel.org/userspace-api/seccomp_filter.html>)
