**翻译状态：**

  * 本文（或部分内容）译自 [Install Arch Linux via SSH](<https://wiki.archlinux.org/title/Install_Arch_Linux_via_SSH> "arch:Install Arch Linux via SSH")，最近一次同步于 2023-05-27，若英文版本有所[更改](<https://wiki.archlinux.org/title/Install_Arch_Linux_via_SSH?diff=0&oldid=779657>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Install_Arch_Linux_via_SSH_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

本文介绍如何通过 [SSH](<../zh-cn/%E5%AE%89%E5%85%A8%E5%A4%96%E5%A3%B3%E5%8D%8F%E8%AE%AE.html> "SSH") 连接远程安装 Arch。如果计算机位于远程位置或者希望在安装 Arch 时使用 SSH 客户端的复制/粘贴功能，则可以考虑这种方法。 

##  在远程（目标）计算机上

**注意：** 这些步骤需要物理访问计算机。如果计算机位于其他位置，则可能需要与其他人协调。

通过 [Live CD/USB 镜像](<../zh-cn/%E5%AE%89%E8%A3%85%E6%8C%87%E5%8D%97.html> "安装指南")启动计算机进入 Live Arch 环境：用户将以 root 用户身份登录。 

这时，按照[安装指南#连接到互联网](<../zh-cn/%E5%AE%89%E8%A3%85%E6%8C%87%E5%8D%97.html#%E8%BF%9E%E6%8E%A5%E5%88%B0%E4%BA%92%E8%81%94%E7%BD%91> "安装指南")在目标计算机上设置网络。 

为 SSH 连接设置 root 密码，因为 Arch 中 root 的默认密码为空： 
    
    # passwd
    
确认在 `/etc/ssh/sshd_config` 中设置了 `PermitRootLogin yes`。如果没有，请设置并[重新加载](<../zh-cn/Systemd.html#%E4%BD%BF%E7%94%A8%E5%8D%95%E5%85%83> "Systemd")OpenSSH 守护进程 `sshd.service` 使更改生效。 

**注意：** 如果目标计算机在 NAT 路由器后面，并且需要从外部访问， 则需要将 SSH 端口（默认为 22）转发到目标计算机的 LAN IP 地址。也可以设置一个到本地（客户端）机器的反向 SSH 隧道，并通过它连接，请参见 [ssh(1)](<https://man.archlinux.org/man/ssh.1>) 的 `-R` 标志。

##  在本地计算机上

在本地计算机上，使用以下命令通过 SSH 连接到目标计算机： 
    
    $ ssh -o StrictHostKeyChecking=no -o "UserKnownHostsFile /dev/null" root@_目标计算机的_IP_地址_
    
**注意：**`-o StrictHostKeyChecking=no -o "UserKnownHostsFile /dev/null"` 选项将阻止验证 Live 环境的 SSH 主机密钥并将其写入到 `~/.ssh/known_hosts`。如果您以前连接过这一 IP 地址，这将避免 `REMOTE HOST IDENTIFICATION HAS CHANGED` 警告。

从这里可以看到 Live 环境的欢迎信息，并且能够像坐在物理键盘旁一样管理目标计算机。此时，如果只想安装 Arch，请遵循[安装指南](<../zh-cn/%E5%AE%89%E8%A3%85%E6%8C%87%E5%8D%97.html> "安装指南")。如果要编辑现有的已损坏的 Linux 安装，参见[从现有 Linux 发行版安装 Arch Linux](<../zh-cn/%E4%BB%8E%E7%8E%B0%E6%9C%89_Linux_%E5%8F%91%E8%A1%8C%E7%89%88%E5%AE%89%E8%A3%85_Arch_Linux.html> "从现有 Linux 发行版安装 Arch Linux")。 

**提示：** 考虑在目标计算机上使用 [GNU Screen](<../zh-cn/GNU_Screen.html> "GNU Screen") 或 [tmux](<../zh-cn/Tmux.html> "Tmux")（在 Live 环境中两者都可用）。这样，如果断开连接，还可以重新连接到多路复用器的会话。

##  在无头服务器上安装

**注意：** 这些步骤需要物理访问远程计算机。需要有人插入安装介质并启动服务器。

本节介绍在没有键盘、鼠标和显示器的无头服务器上安装 Arch Linux。这种方法使用一个带有 [cloud-init](<../zh-cn/Cloud-init.html> "Cloud-init") NoCloud 配置的额外驱动器来自动配置 [OpenSSH](<../zh-cn/OpenSSH.html> "OpenSSH") 授权密钥和可选的 [iwd](<../zh-cn/Iwd.html> "Iwd") 连接。 

###  准备 cloud-init 配置文件

需要两个 [cloud-init](<../zh-cn/Cloud-init.html> "Cloud-init") 配置文件：`meta-data` 和 `user-data`。 

`meta-data` 文件可以为空： 
    
    $ printf "" > meta-data
    
`user-data` 将包含相关配置： 
    
    user-data
    
    #cloud-config
    users:
      - name: root
        ssh_authorized_keys:
          - ssh-ed25519 _XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX_
          - ssh-ed25519 _YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY_

将 `ssh-ed25519 _XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX_` 替换为 [SSH 公钥](<../zh-cn/SSH_%E5%AF%86%E9%92%A5.html> "SSH 密钥")。要添加多个密钥，只需重复上述语句。 

要自动连接到 Wi-Fi 网络，请使用 `write_files:` 语句在正确的目录中创建 [iwd 网络配置文件](<../zh-cn/Iwd.html#%E7%BD%91%E7%BB%9C%E9%85%8D%E7%BD%AE> "Iwd")。例如： 
    
    user-data
    
    #cloud-config
    users:
      - name: root
        ssh_authorized_keys:
          - ssh-ed25519 _XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX_
          - ssh-ed25519 _YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY_
    
    write_files:
    - content: |
        [Security]
        PreSharedKey=aafb192ce2da24d8c7805c956136f45dd612103f086034c402ed266355297295
      path: /var/lib/iwd/spaceship.psk
      
    runcmd:
    - systemctl restart iwd.service

创建了这两个文件之后，需要将其放置在一个标签为 `CIDATA` 的 ISO 9660 或 FAT 卷的驱动器上。 

###  使用额外的 FAT 格式驱动器

使用 [FAT](<../zh-cn/FAT.html> "FAT") 格式的驱动器。将 `meta-data` 和 `user-data` 复制到驱动器并将文件系统的 [LABEL](<../zh-cn/%E5%9D%97%E8%AE%BE%E5%A4%87%E6%8C%81%E4%B9%85%E5%8C%96%E5%91%BD%E5%90%8D.html#%E9%80%9A%E8%BF%87%E5%88%86%E5%8C%BA%E6%A0%87%E7%AD%BE> "块设备持久化命名") 更改为 `CIDATA`。 

除了包含官方 ISO 的驱动器外，还需要将这个驱动器连接到无头计算机上。 

###  使用额外的 ISO

使用 [libisoburn](<https://archlinux.org/packages/?name=libisoburn>)包 中的 _xorriso_ 创建一个 `cloud-init.iso` 文件： 
    
    $ xorrisofs -output cloud-init.iso -volid CIDATA -joliet -rational-rock meta-data user-data
    
将 cloud-init 数据介质[刻录](<../zh-cn/%E5%85%89%E7%9B%98%E9%A9%B1%E5%8A%A8%E5%99%A8.html#%E5%88%BB%E5%BD%95> "光盘驱动器")到光盘，如果部署选项允许的话，按原样使用 ISO。 

###  使用单个 U 盘

如果将安装映像写入到了 U 盘之类的驱动器，并且驱动器上有足够的空间，就可以创建一个额外的分区来存储 cloud-init 数据。 

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [dosfstools](<https://archlinux.org/packages/?name=dosfstools>)包、[mtools](<https://archlinux.org/packages/?name=mtools>)包 和 [libisoburn](<https://archlinux.org/packages/?name=libisoburn>)包。 

首先创建一个 [LABEL](<../zh-cn/%E5%9D%97%E8%AE%BE%E5%A4%87%E6%8C%81%E4%B9%85%E5%8C%96%E5%91%BD%E5%90%8D.html#%E9%80%9A%E8%BF%87%E5%88%86%E5%8C%BA%E6%A0%87%E7%AD%BE> "块设备持久化命名") 设置为 `CIDATA` 的 [FAT](<../zh-cn/FAT.html> "FAT") 镜像： 
    
    $ mkfs.fat -C -n CIDATA cloud-init.img 2048
    
将 `meta-data` 和 `user-data` 文件复制到其根目录： 
    
    $ mcopy -i cloud-init.img meta-data user-data ::
    
重新打包官方 ISO，将 FAT 镜像作为第三个分区包括进来： 
    
    $ xorriso -indev archlinux-_version_ -x86_64.iso -outdev archlinux-_version_ -x86_64-with-cidata.iso -append_partition 3 0x0c cloud-init.img -boot_image any replay
    
最后按照 [USB flash installation medium#Using the ISO as is (BIOS and UEFI)](<../zh-cn/USB_flash_installation_medium.html#Using_the_ISO_as_is_\(BIOS_and_UEFI\)> "USB flash installation medium") 使用重新打包的 ISO（`archlinux-_version_ -x86_64-with-cidata.iso`）准备 U 盘安装介质。 

###  使用单个定制的 ISO

除了上述方法，也使用 [Archiso](<../zh-cn/Archiso.html> "Archiso") 创建一个自定义 ISO。这样，无论类型如何，都可以只使用一个驱动器。 

以 releng 配置文件作为基础。将 [cloud-init 配置文件](<#%E5%87%86%E5%A4%87_cloud-init_%E9%85%8D%E7%BD%AE%E6%96%87%E4%BB%B6>)放在 `airootfs/var/lib/cloud/seed/nocloud/` 中，然后构建 ISO。 

###  从安装介质启动

完成后，使用适当的方法将安装介质和 cloud-init 数据介质（如果是单独的）部署到无头计算机。 

启动无头计算机，从安装介质启动到 Live Arch 环境。等待一分钟左右来让无头计算机启动并连接到网络。 

从您现有的计算机（带键盘和显示器）通过 [SSH](<../zh-cn/%E5%AE%89%E5%85%A8%E5%A4%96%E5%A3%B3%E5%8D%8F%E8%AE%AE.html> "SSH") 连接到无头服务器上的 Live Arch 环境，并按照[安装指南](<../zh-cn/%E5%AE%89%E8%A3%85%E6%8C%87%E5%8D%97.html> "安装指南")完成安装。 

**注意：** 显然，启动镜像中的所有 Wi-Fi 和 SSH 配置都需要在实际的 Arch Linux 安装中再次配置，以便在安装后允许 WiFi SSH 访问无头计算机。
