**翻译状态：**

  * 本文（或部分内容）译自 [Preboot Execution Environment](<https://wiki.archlinux.org/title/Preboot_Execution_Environment> "arch:Preboot Execution Environment")，最近一次同步于 2025-07-28，若英文版本有所[更改](<https://wiki.archlinux.org/title/Preboot_Execution_Environment?diff=0&oldid=837790>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Preboot_Execution_Environment_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [Diskless System](</wzh/index.php?title=Diskless_System&action=edit&redlink=1> "Diskless System（页面不存在）")

[维基百科：预启动执行环境](<https://en.wikipedia.org/wiki/Preboot_Execution_Environment> "wikipedia:Preboot Execution Environment")： 

    预启动执行环境（Preboot eXecution Environment，PXE，也被称为预执行环境）提供了一种使用网络接口（Network Interface）启动计算机的机制。这种机制让计算机的启动可以不依赖本地数据存储设备（如硬盘）或本地已安装的操作系统。

在本指南中，PXE 用于通过支持 PXE 的 Option ROM 在目标机器上启动安装介质，适用于安装了服务器的情况。 

##  准备

###  概览

在开始前，需要先了解下 PXE 启动流程，以理解[#服务器搭建](<#%E6%9C%8D%E5%8A%A1%E5%99%A8%E6%90%AD%E5%BB%BA>)，目标设备上的[#安装](<#%E5%AE%89%E8%A3%85>)流程以及所需的 Arch Linux 文件。 

目标设备会先广播数据包，请求 DHCP 服务器并包含特定的 PXE 选项。接下来，DHCP 服务器会发送包含网络信息（分配给目标设备的 IP 地址）的回应，并通过 DHCP 的特定[引导协议（bootstrap protocol，BOOTP）](<https://en.wikipedia.org/wiki/Bootstrap_Protocol> "wikipedia:Bootstrap Protocol")参数提供如 [TFTP](</wzh/index.php?title=TFTP&action=edit&redlink=1> "TFTP（页面不存在）") 服务器地址，初始网络引导程序（initial network bootstrap program，NBP）的下载路径或启动配置文件名称等额外信息。 

NBP 会通过 TFTP 从 PXE 服务器传输到目标设备上，然后加载到内存中并执行。内核以及 initramfs 也是通过一样的方式进行传输。 

接下来根文件系统会通过以下协议之一进行传输：HTTP，NFS 或 NBD。 

**警告：**[PXELINUX](<../zh-cn/Syslinux.html#PXELINUX> "PXELINUX") 不支持以任何形式对通过 TFTP 或 HTTP 收到的数据进行验证，具体信息请参考 [RFC 5071 section8](<https://tools.ietf.org/html/rfc5071#section-8> "rfc:5071")。替代方法是使用[网络引导](<../zh-cn/%E7%BD%91%E7%BB%9C%E5%BC%95%E5%AF%BC.html> "网络引导")（Netboot）映像，它可以使用 iPEX 中嵌入的代码签名凭证来[验证](<https://ipxe.org/cmd/imgverify>)签名。注意，网络引导映像需要放置在本地设备上。

###  启动安装介质

首先从[下载页](<https://archlinux.org/download/>)获取最新的官方安装映像，以获取启动时需要从服务器传输到客户端的文件。 

接下来需要挂载映像： 
    
    # mount --mkdir -o loop,ro archlinux-_release_date_ -x86_64.iso /mnt/archiso
    
其中 `_release_date_` 是 ISO 文件名中的发布日期，例如 `2022.10.01`。 

**注意：** Arch ISO 现在只支持 **BIOS** 风格的 PXE 引导。更多信息请参考 [archlinux/archiso#55](<https://gitlab.archlinux.org/archlinux/archiso/-/issues/55>)。

###  从网络引导启动

Arch Linux [网络引导](<../zh-cn/%E7%BD%91%E7%BB%9C%E5%BC%95%E5%AF%BC.html> "网络引导")映像可以在系统启动时即时下载最新发布的 Arch Linux 版本。请下载适用于你的配置的版本。 

**注意：** Arch 网络引导映像同时支持 **BIOS** 和 **UEFI** 引导方式。

## Pixiecore

[pixiecore](<https://github.com/danderson/netboot/tree/master/pixiecore>) 提供了一体化解决方案： 

  1. 安装 [pixiecore-git](<https://aur.archlinux.org/packages/pixiecore-git/>)AUR
  2. 以根用户身份执行 `pixiecore quick arch --dhcp-no-bind`
  3. 通过 PXE 进行引导

##  服务器搭建

你需要搭建一个 [DHCP 服务器](<../zh-cn/%E7%BD%91%E7%BB%9C%E9%85%8D%E7%BD%AE.html#%E7%BD%91%E7%BB%9C%E7%AE%A1%E7%90%86%E5%99%A8> "网络配置")和一个 [TFTP 服务器](</wzh/index.php?title=TFTP&action=edit&redlink=1> "TFTP（页面不存在）")来传输 NBP，以及下列服务之一来传输根文件系统：[HTTP 服务器](<../zh-cn/%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F%E5%88%97%E8%A1%A8/%E4%BA%92%E8%81%94%E7%BD%91.html#%E7%BD%91%E7%BB%9C%E6%9C%8D%E5%8A%A1%E5%99%A8> "应用程序列表/互联网")，[NFS](<../zh-cn/NFS.html> "NFS") 或 NBD。 

###  网络

激活网卡，并分配一个合适的地址。 
    
    # ip link set _eth0_ up
    # ip addr add 192.168.0.1/24 dev _eth0_
    
你还可以使用[网络管理器](<../zh-cn/%E7%BD%91%E7%BB%9C%E9%85%8D%E7%BD%AE.html#%E7%BD%91%E7%BB%9C%E7%AE%A1%E7%90%86%E5%99%A8> "网络配置")来配置静态 IP。 

###  DHCP + TFTP

为了在安装目标上配置网络并在 PXE 服务端和客户端之间传输文件，需要搭建 [DHCP](<../zh-cn/%E7%BD%91%E7%BB%9C%E9%85%8D%E7%BD%AE.html#%E7%BD%91%E7%BB%9C%E7%AE%A1%E7%90%86%E5%99%A8> "网络配置") 和 [TFTP](</wzh/index.php?title=TFTP&action=edit&redlink=1> "TFTP（页面不存在）") 服务器。[dnsmasq](<../zh-cn/Dnsmasq.html> "Dnsmasq") 能同时做到这两点，也很容易配置。 

首先[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [dnsmasq](<https://archlinux.org/packages/?name=dnsmasq>)包。 

接下来需要配置 _dnsmasq_ ，请参考 [dnsmasq#TFTP 服务器](<../zh-cn/Dnsmasq.html#TFTP_%E6%9C%8D%E5%8A%A1%E5%99%A8> "Dnsmasq")和 [dnsmasq#PXE 服务器](<../zh-cn/Dnsmasq.html#PXE_%E6%9C%8D%E5%8A%A1%E5%99%A8> "Dnsmasq")。 

以下为一些常用配置，其中 _tftp_root_ 为 Arch ISO 的挂载目录（例如 `/mnt/archiso`）或网络引导程序的挂载路径： 
    
    # /etc/dnsmasq.conf
    
    # Listen only to the specified interface
    interface=_eth0_
    
    # Do not function as DNS server
    port=0
    
    # TFTP server setup
    enable-tftp
    tftp-root=_tftp_root_
    
    # Log extra information about DHCP transactions (for debug purposes)
    log-dhcp

要启用 DHCP 服务器并分配 IPv4 地址段，需在配置文件中添加如下一行： 
    
    dhcp-range=192.168.0.50,192.168.0.150
    
如果已有 DHCP 服务器并希望与其搭配使用，请参考 [dnsmasq#Proxy DHCP](<../zh-cn/Dnsmasq.html#Proxy_DHCP> "Dnsmasq")。 

下文提供了两种通过不同方式启动到安装介质的示例。 

配置完成后，[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动") `dnsmasq.service`。 

####  使用 BIOS 启动到安装介质

在配置文件中，使用 `dhcp-boot` 选项定义要发送的初始引导程序的路径： 
    
    dhcp-boot=/boot/syslinux/lpxelinux.0
    
要发送如配置文件路径等特定[引导协议（ _boot_ strap _p_ rotocol，BOOTP）参数](<https://www.iana.org/assignments/bootp-dhcp-parameters/bootp-dhcp-parameters.xhtml>)，需使用 `dhcp-option-force=_flag_ ,_value_` 配置： 
    
    dhcp-option-force=209,archiso_pxe.cfg # this file might be under /mnt/archiso/boot/syslinux
    dhcp-option-force=210,
    
####  使用 UEFI 从网络引导启动

要根据架构发送文件（此处为用于 UEFI 引导的网络引导映像），请使用： 
    
    pxe-service=BC_EFI, "Boot from network BC EFI", ipxe.efi
    pxe-service=X86-64_EFI, "Boot from network X86-64 EFI", ipxe.efi
    
剩余的服务器搭建环节仅适用于 Arch ISO，如果使用了网络引导（netboot），那以下部分将不再适用。 

###  传送 archiso 根文件系统

得益于 [archiso](<../zh-cn/Archiso.html> "Archiso") 中的 `archiso_pxe_http`，`archiso_pxe_nfs` 和 `archiso_pxe_nbd` initcpio 钩子，你可以选择使用 HTTP，NFS 或 NBD 进行启动。这三种方式的启动时间基本没有区别，但使用 HTTP 方式能以百分比形式查看 `airootfs.sfs` 的下载进度。 

#### HTTP

在所有备选方案中， _darkhttpd_ 是最容易设置的（也是最轻量的）。 

首先，[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [darkhttpd](<https://archlinux.org/packages/?name=darkhttpd>)包。 

然后以 `/mnt/archiso` 作为文件根目录启动 _darkhttpd_ ： 
    
    # darkhttpd /mnt/archiso
    
    darkhttpd/1.8, copyright (c) 2003-2011 Emil Mikulic.
    listening on: http://0.0.0.0:80/
    
**注意：** 请确保服务器使用的是 `**80**` 端口。如果你没有以根用户启动 _darkhttpd_ ，那么它会默认使用 `**8080**` 端口，导致目标设备尝试访问无效的 80 端口并启动失败。

#### NFS

您需搭建 [NFS 服务器](<../zh-cn/NFS.html> "NFS")并将安装镜像的挂载点作为出口（export）。如果您按照[#准备](<#%E5%87%86%E5%A4%87>)段落做了的话，出口就是 `/mnt/archiso`。服务器搭建起来后，往 `/etc/exports` 写入这行： 
    
    /etc/exports
    
    /mnt/archiso 192.168.0.0/24(ro,no_subtree_check)
    
如果服务器已经在运行了，用 `exportfs -r -a -v` 重新导出文件系统。 

安装程序会在 `/run/archiso/bootmnt/` 查找 NFS，因此您需要编辑启动选项。在启动菜单按下 Tab，参考如下修改 `archiso_nfs_srv`： 
    
    archiso_nfs_srv=${pxeserver}:/mnt/archiso
    
或者，您也可以整个过程中都使用 `/run/archiso/bootmnt`。 

在内核加载后，Arch bootstrap 镜像会通过 NFS 复制根文件系统到引导主机（booting host）。这需要一定的时间。一旦复制完成，您就有可运作的系统了。 

#### NBD

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [nbd](<https://archlinux.org/packages/?name=nbd>)包 并配置： 
    
    /etc/nbd-server/config
    
    [generic]
    [archiso]
        readonly = true
        exportname = /srv/archlinux-_release_date_ -x86_64.iso

其中 `_release_date_` 是 ISO 文件名中的发布日期，例如 `2022.10.01`。 

[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动") `nbd.service`。 

###  已有的 PXE 服务器

如果已经有了 [PXELINUX](<../zh-cn/Syslinux.html#PXELINUX> "PXELINUX") 配置（例如 DHCP + [TFTP](</wzh/index.php?title=TFTP&action=edit&redlink=1> "TFTP（页面不存在）")）的 PXE 服务器，可以通过在 `/tftpboot/pxelinux.cfg/default` 文件中添加以下菜单项来通过偏好的方式启动 Arch。 

鉴于 PXELINUX 支持 HTTP，可以只通过 TFTP 发送引导加载程序，其它的都通过 HTTP 进行传输，例如： 
    
    LABEL archlinux
            MENU LABEL Arch Linux x86_64
            LINUX _http://httpserver/path/to/extracted/Arch/ISO_ /arch/boot/x86_64/vmlinuz-linux
            INITRD _http://httpserver/path/to/extracted/Arch/ISO_ /arch/boot/x86_64/initramfs-linux.img
            APPEND archisobasedir=arch archiso_http_srv=_http://httpserver/path/to/extracted/Arch/ISO_ / cms_verify=y
            SYSAPPEND 3
            TEXT HELP
            Arch Linux 2022.10.01 x86_64
            ENDTEXT

如果使用 NFS 和 NBD，那么必须通过 TFTP 传输内核及 initramfs。以 NFS 为例： 
    
    LABEL archlinux
            MENU LABEL Arch Linux x86_64
            LINUX _/path/to/extracted/Arch/ISO_ /arch/boot/x86_64/vmlinuz-linux
            INITRD _/path/to/extracted/Arch/ISO_ /arch/boot/x86_64/initramfs-linux.img
            APPEND archisobasedir=arch archiso_nfs_srv=_pxeserver_ :/run/archiso/bootmnt cms_verify=y
            SYSAPPEND 3
            TEXT HELP
            Arch Linux 2022.10.01 x86_64
            ENDTEXT

其中 `LINUX` 和 `INITRD` 路径是相对于 TFTP 根路径的。对于 NBD，需要将上面的 `archiso_nfs_srv` 替换为 `archiso_nbd_srv`。可以参考一下 Arch Linux ISO 中的 `boot/syslinux/archiso_pxe.cfg` 示例文件。 

无论使用了哪种方法，都必须在尝试通过网络挂载安装介质前通过 `ip=` 参数让内核拉起网络接口。如果目标设备上有多个有线网卡，或是需要在 archiso 启动后预配置 `resolv.conf`，就需要传递 `BOOTIF=` 参数。你可以通过 [sysappend mask](<https://wiki.syslinux.org/wiki/index.php?title=Config#SYSAPPEND>) `3`（即 `1` \+ `2`）来自动传递这些参数。所有可用启动参数请参考 [README.bootparams](<https://gitlab.archlinux.org/archlinux/mkinitcpio/mkinitcpio-archiso/blob/master/docs/README.bootparams>)。 

##  安装

在进行该部分操作前，需要知道如何让你的目标设备进行 PXE 引导，通常在正常引导时屏幕角落会提示进行 PXE 引导需要按下的按键。例如在 IBM x3650 上按下 `F12` 会出现一个引导菜单，可以选择第一项 _Network_ ；在 Dell PE 1950/2950 上按下 `F12` 会直接进行 PXE 引导。 

###  启动

通过查看 PXE 服务器的 [journald](<../zh-cn/Systemd/Journal.html> "Journald")，可以了解 PXE 早期启动阶段时的具体流程： 
    
    # journalctl -u dnsmasq.service -f
    
    dnsmasq-dhcp[2544]: DHCPDISCOVER(eth1) 00:1a:64:6a:a2:4d 
    dnsmasq-dhcp[2544]: DHCPOFFER(eth1) 192.168.0.110 00:1a:64:6a:a2:4d 
    dnsmasq-dhcp[2544]: DHCPREQUEST(eth1) 192.168.0.110 00:1a:64:6a:a2:4d 
    dnsmasq-dhcp[2544]: DHCPACK(eth1) 192.168.0.110 00:1a:64:6a:a2:4d 
    dnsmasq-tftp[2544]: sent /mnt/archiso/boot/syslinux/pxelinux.0 to 192.168.0.110
    dnsmasq-tftp[2544]: sent /mnt/archiso/boot/syslinux/archiso.cfg to 192.168.0.110
    dnsmasq-tftp[2544]: sent /mnt/archiso/boot/syslinux/whichsys.c32 to 192.168.0.110
    dnsmasq-tftp[2544]: sent /mnt/archiso/boot/syslinux/archiso_pxe_choose.cfg to 192.168.0.110
    dnsmasq-tftp[2544]: sent /mnt/archiso/boot/syslinux/ifcpu64.c32 to 192.168.0.110
    dnsmasq-tftp[2544]: sent /mnt/archiso/boot/syslinux/archiso_pxe_both_inc.cfg to 192.168.0.110
    dnsmasq-tftp[2544]: sent /mnt/archiso/boot/syslinux/archiso_head.cfg to 192.168.0.110
    dnsmasq-tftp[2544]: sent /mnt/archiso/boot/syslinux/archiso_pxe32.cfg to 192.168.0.110
    dnsmasq-tftp[2544]: sent /mnt/archiso/boot/syslinux/archiso_pxe64.cfg to 192.168.0.110
    dnsmasq-tftp[2544]: sent /mnt/archiso/boot/syslinux/archiso_tail.cfg to 192.168.0.110
    dnsmasq-tftp[2544]: sent /mnt/archiso/boot/syslinux/vesamenu.c32 to 192.168.0.110
    dnsmasq-tftp[2544]: sent /mnt/archiso/boot/syslinux/splash.png to 192.168.0.110
    
在通过 TFTP 加载了 `pxelinux.0` 和 `archiso.cfg` 后，应该会出现带有多个选项的 [syslinux](<../zh-cn/Syslinux.html> "Syslinux") 菜单，这时候需选择 _Boot Arch Linux (x86_64) (HTTP)_ 。 

接下来将通过 TFTP 传输架构对应的内核与 initramfs： 
    
    dnsmasq-tftp[2544]: sent /mnt/archiso/arch/boot/x86_64/vmlinuz to 192.168.0.110
    dnsmasq-tftp[2544]: sent /mnt/archiso/arch/boot/x86_64/initramfs-linux.img to 192.168.0.110

如果一切正常，你将可以在 darkhttpd 上看到 PXE 目标设备的一系列活动。这时 PXE 目标设备将加载内核并初始化： 
    
    1348347586 192.168.0.110 "GET /arch/aitab" 200 678 "" "curl/7.27.0"
    1348347587 192.168.0.110 "GET /arch/x86_64/root-image.fs.sfs" 200 107860206 "" "curl/7.27.0"
    1348347588 192.168.0.110 "GET /arch/x86_64/usr-lib-modules.fs.sfs" 200 36819181 "" "curl/7.27.0"
    1348347588 192.168.0.110 "GET /arch/any/usr-share.fs.sfs" 200 63693037 "" "curl/7.27.0"

在通过 HTTP 下载根文件系统后，最终将看到正常 live 环境的根用户 [zsh](<../zh-cn/Zsh.html> "Zsh") 提示符。 

###  启动后

除非你想让所有流量都路由过 PXE 服务器（在[正确配置](<#%E4%B8%8E_PXE_%E7%9B%AE%E6%A0%87%E8%AE%BE%E5%A4%87%E5%85%B1%E4%BA%AB%E7%BD%91%E7%BB%9C>)前都无法使用），否则就需要[停止](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "停止") `dnsmasq.service` 服务，并根据网络环境为安装目标获取新的租约。 

你还可以杀掉 _darkhttpd_ ：目标已经下载好了根文件系统，不再需要该进程。在进行该操作时，可以顺便卸载掉安装映像： 
    
    # umount /mnt/archiso
    
这时候就可以根据[安装指南](<../zh-cn/%E5%AE%89%E8%A3%85%E6%8C%87%E5%8D%97.html> "安装指南")进行安装了。 

###  小内存设备

`copytoram` [initramfs](<../zh-cn/Arch_%E7%9A%84%E5%90%AF%E5%8A%A8%E6%B5%81%E7%A8%8B.html#initramfs> "Initramfs") 选项可以控制在启动早期时是否将整个根文件系统复制到内存中。 

强烈建议不去改动该选项，且只在必要的时候禁用（物理内存小于 ~256MB）。如果要这么做，需向内核参数加入 `copytoram=n` 设置。 

**注意：** 由于该操作需要从已挂载的远程文件系统循环挂载 squashfs，因此 `copytoram=n` 和 `[archiso_pxe_http](<#HTTP>)` 不能同时使用。

###  与 PXE 目标设备共享网络

如果 PXE 目标设备使用的是内部网络（例如 192.168.1.0/24），但还需要访问互联网（如需要安装软件包），那么就需要配置 masquerade/source nat。PXE 服务器上必须有连接到互联网的单独网卡。可以使用如下命令让目标设备访问到互联网： 
    
    iptables -t nat -A POSTROUTING -s 192.168.1.0/24 -j MASQUERADE
    
要将配置持久化，需使用如下命令： 
    
    iptables-save -f /etc/iptables/iptables.rules
    
然后[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用") `iptables.service`。 

具体信息请参考 [Simple stateful firewall#Setting up a NAT gateway](<../zh-cn/Simple_stateful_firewall.html#Setting_up_a_NAT_gateway> "Simple stateful firewall") 和[网络分享#启用 NAT](<../zh-cn/%E7%BD%91%E7%BB%9C%E5%88%86%E4%BA%AB.html#%E5%90%AF%E7%94%A8_NAT> "网络分享")。 

##  排障

### DHCP interface rename bug

[FS#36749](<https://bugs.archlinux.org/task/36749>) causes default [predictable network interface renaming](<https://systemd.io/PREDICTABLE_INTERFACE_NAMES/>) to fail and then DHCP client to fail because of it. A workaround is to add the kernel boot parameter `net.ifnames=0` to disable predictable interface names. 

### VirtualBox cannot boot while real machines can

When using [VirtualBox](<../zh-cn/VirtualBox.html> "VirtualBox") to test your configuration, the virtual machine may get stuck at: 
    
    Probing EDD (edd=off to disable)... ok
    
While PXE booting with a real machine works fine. The problem may be because you have set several CPU cores to your client machine, and you set its type as _Other_ and version as _Other/Unknown (64 bit)_. So VirtualBox does not know which paravirtualization interface to use by default. 

Adding `loglevel=7` to the [kernel parameters](<../zh-cn/Kernel_parameters.html> "Kernel parameters") lets you see where it actually got stuck: 
    
    [    0.063697] smp: Bringing up secondary CPUs...
    [    0.103768] x86: Booting SMP configuration:
    
To resolve this, either use one CPU core, or go to _Machine > Settings > System > Acceleration_ and set one of the following paravirtualization interface: _Minimal_ , _Hyper-V_ or _KVM_. 
