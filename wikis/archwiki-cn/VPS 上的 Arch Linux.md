相关文章

  * [服务器](<../zh-cn/Category:%E6%9C%8D%E5%8A%A1%E5%99%A8.html> "服务器")

**翻译状态：**

  * 本文（或部分内容）译自 [Arch Linux on a VPS](<https://wiki.archlinux.org/title/Arch_Linux_on_a_VPS> "arch:Arch Linux on a VPS")，最近一次同步于 2025-04-11，若英文版本有所[更改](<https://wiki.archlinux.org/title/Arch_Linux_on_a_VPS?diff=0&oldid=822219>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Arch_Linux_on_a_VPS_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

摘自 [Wikipedia:Virtual private server](<https://en.wikipedia.org/wiki/Virtual_private_server> "wikipedia:Virtual private server"): 

    Virtual private server (VPS) is a term used by Internet hosting services to refer to a virtual machine. The term is used for emphasizing that the virtual machine, although running in software on the same physical computer as other customers' virtual machines, is in many respects functionally equivalent to a separate physical computer, is dedicated to the individual customer's needs, has the privacy of a separate physical computer, and can be configured to run server software.

本文主要讨论 Arch Linux 在 VPS 上的应用，并且包括了一些适用于 VPS 的安装与维护指南. 

##  Arch Linux 官方云映像

作为 [arch-boxes 项目](<https://gitlab.archlinux.org/archlinux/arch-boxes>)的一部分，Arch Linux 提供了官方云映像。映像预装了 [Cloud-init](<../zh-cn/Cloud-init.html> "Cloud-init")，应可用于多数云服务供应商。 

可以从镜像源的 `images` 目录下找到该映像，具体使用步骤参考下方。 

### DigitalOcean

网站：[Digital Ocean](<https://digitalocean.com>)

位置：全球 

创建 Arch Linux VM 的步骤： 

  1. 在镜像源上找到云映像的位置，例如：<https://geo.mirror.pkgbuild.com/images/latest/Arch-Linux-x86_64-cloudimg.qcow2>
  2. 将其[导入](<https://docs.digitalocean.com/products/images/custom-images/how-to/upload/>)为自定义映像
  3. [从自定义映像创建新 VM](<https://docs.digitalocean.com/products/images/custom-images/how-to/create-droplets/>)
  4. 通过 SSH 连接到 VM：`ssh root@_ip_`

### Hetzner Cloud

网站：[Hetzner Cloud](<https://www.hetzner.com/cloud>)

位置：纽伦堡（德国），法尔肯施泰因（德国），赫尔辛基（芬兰），新加坡，希尔斯伯勒（美国西部），阿什本（美国东部） 

创建 Arch Linux VM 的步骤： 

  1. 使用该用户数据创建新 VM：
         
         #cloud-config  
         vendor_data: {'enabled': false}

Hetzner 的 `vendor_data` 会覆盖掉`发行版`中设定的值，并在将默认用户设定为 `root` 的同时没有设置 `disable_root: false`，使得你无法登陆到机子上。

  2. 以恢复模式启动 VM
  3. 通过 SSH 连接到 VM，然后从镜像源下载云映像，例如：`curl -O https://geo.mirror.pkgbuild.com/images/latest/Arch-Linux-x86_64-cloudimg.qcow2`
  4. 将映像写入到硬盘：`qemu-img convert -f qcow2 -O raw Arch-Linux-x86_64-cloudimg.qcow2 /dev/sda`
  5. 重启 VM
  6. 通过 SSH 连接到 VM：`ssh arch@_ip_`

### Linode

网站：[Linode](<https://www.linode.com>)

位置：[全球多地](<https://www.linode.com/global-infrastructure/>)

创建 Arch Linux VM 的步骤： 

  1. 创建一台新 VM，并选择 Arch 作为发行版（如果要使用 Linode 提供的映像，到这一步就行；如果要使用官方映像，继续下列步骤）
  2. 以恢复模式启动 VM
  3. 通过 Lish 控制台连接到 VM，然后从镜像源下载基础映像，例如：`curl -O https://geo.mirror.pkgbuild.com/images/latest/Arch-Linux-x86_64-basic.qcow2`
  4. 安装 [qemu-utils](<https://archlinux.org/packages/?name=qemu-utils>)包：`apt update && apt install qemu-utils`
  5. 将映像写入到硬盘：`qemu-img convert -f qcow2 -O raw Arch-Linux-x86_64-basic.qcow2 /dev/sda`
  6. 在 Linode 控制台上，进入到 VM 配置菜单，然后将内核选项修改为 ”Direct Disk“
  7. 重启 VM
  8. 通过 SSH 连接到 VM：`ssh arch@_ip_`

### OVH Eco

网站：[Kimsufi](<https://www.kimsufi.com/en/dedicated-servers>) [OVH Eco](<https://eco.ovhcloud.com/en-gb>)

位置：加拿大，法国 

基于[官方文档](<https://docs.ovh.com/gb/en/dedicated/bringyourownimage>)的 Arch Linux VM 创建步骤如下： 

  1. Navigate to the [Dedicated Servers](<https://www.ovh.com/manager/#/dedicated/server>) section in your OVH management panel, then select the server you want to deploy Arch Linux to.
  2. Click the ... button next to "Last operating system (OS) installed by OVHcloud" and choose "Install"
  3. Select "Install from custom image"
  4. For "Image URL" put `https://geo.mirror.pkgbuild.com/images/latest/Arch-Linux-x86_64-cloudimg.qcow2`
  5. For "Image type" select `qcow2`
  6. For "Checksum type" select `sha256`
  7. For "Image checksum" put the fingerprint value from <https://geo.mirror.pkgbuild.com/images/latest/Arch-Linux-x86_64-cloudimg.qcow2.SHA256>
  8. Enable "ConfigDrive" to enter "Server host name" and your public "SSH key" (both are mandatory for Arch Cloud Init install)
  9. Click "Install the system"
  10. Wait (it takes a while) for an email from OVH titled "Installation of your image", it will say "Congratulations! Your dedicated server has just been installed! Connect to your server with ssh key provided during your installation."
  11. Use `ssh arch@_ip_` to log in.

### Proxmox

网站：[Proxmox](<https://www.proxmox.com/>)

位置：N/A 

创建 Arch Linux VM 的步骤： 

  1. 创建一台新 VM
  2. 在 OS 选择步骤选中 “Do not use any media”
  3. 在 VM 创建完成后从 VM 移除刚创建的硬盘
  4. 使用 `qm disk import` 将刚下载好的映像连接到 VM，例如：  
`qm disk import 100 Arch-Linux-x86_64-cloudimg.qcow2 local`.
  5. 在 Options 下，编辑启动顺序，添加刚创建的硬盘
  6. 添加 cloudinit 盘，在 Cloud-Init 一项中添加你的配置
  7. 启动 VM！
