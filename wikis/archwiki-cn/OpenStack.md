**翻译状态：**

  * 本文（或部分内容）译自 [OpenStack](<https://wiki.archlinux.org/title/OpenStack> "arch:OpenStack")，最近一次同步于 2023-01-16，若英文版本有所[更改](<https://wiki.archlinux.org/title/OpenStack?diff=0&oldid=425647>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/OpenStack_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[OpenStack](<https://www.openstack.org/>) 是由来自全球的开发者及云计算专家合作开放的一套被广泛使用的公有/私有云计算平台。该项目着重于为所有类型的云创造一套易于实现、高可扩展性且功能丰富的解决方案。该平台由一系列互相关联的项目组成，为云基础设施方案提供各种组件。 

##  组件

  * **计算 (Nova)** — Nova 是用于提供计算实例（即虚拟机）的 Openstack 项目。

     <https://docs.openstack.org/nova/latest/> || [openstack-nova](<https://aur.archlinux.org/packages/openstack-nova/>)AUR

  * **网络 (Neutron)** — Neutron 是用于在其它 OpenStack 服务（例如 Nova）管理的接口设备（例如 vNIC）之间提供“网络即服务”功能的 OpenStack 项目。它实现了 OpenStack 网络 API。

     <https://docs.openstack.org/neutron/latest/> || [openstack-neutron](<https://aur.archlinux.org/packages/openstack-neutron/>)AUR

  * **镜像服务 (Glance)** — 镜像服务 (glance) 项目提供了让用户上传并发现用于让其它服务使用的数据资产的功能。

     <https://docs.openstack.org/glance/latest/> || [openstack-glance](<https://aur.archlinux.org/packages/openstack-glance/>)AUR

  * **块存储 (Cinder)** — Cinder 是用于为 Nova 虚拟机、Ironic 裸金属、容器等服务提供存储盘的 OpenStack 服务。

     <https://docs.openstack.org/cinder/latest/> || [openstack-cinder](<https://aur.archlinux.org/packages/openstack-cinder/>)AUR

  * **鉴权 (Keystone)** — Keystone 是通过 OpenStack 身份 API 提供 API 用户验证，服务发现及分布式多租户授权的 OpenStack 服务。

     <https://docs.openstack.org/keystone/latest/> || [openstack-keystone](<https://aur.archlinux.org/packages/openstack-keystone/>)AUR

  * **控制面板 (Horizon)** — Horizon 是 canonical 对于 OpenStack 面板的实现，它为 Nova、Swift、Keystone 等 OpenStack 服务提供了网页用户界面。

     <https://docs.openstack.org/horizon/latest/> || [openstack-horizon](<https://aur.archlinux.org/packages/openstack-horizon/>)AUR

##  部署 OpenStack

[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：** 请提供模板的第一个位置参数以概括原因。 (在 [Talk:OpenStack](<../zh-cn/Talk:OpenStack.html>) 中讨论)

##  镜像

###  可用镜像

[Openstack 官方镜像](<https://docs.openstack.org/image-guide/obtain-images.html>)包含了大部分流行的 GNU/Linux 发行版。 

Arch Linux 官方云镜像可以在以下链接下载：<https://gitlab.archlinux.org/archlinux/arch-boxes>

###  自己创建镜像

OpenStack 镜像需要满足[一些要求](<https://docs.openstack.org/image-guide/openstack-images.html>)。可以手动或是使用工具来协助准备镜像。 

若要使用工具，可以考虑将 [image-bootstrap](<https://github.com/hartwork/image-bootstrap>) 搭配 `--openstack` 选项使用。 

若要手动创建，下面为一系列 _必须_ 步骤： 

  * 将一个硬盘[分区](<../zh-cn/%E5%88%86%E5%8C%BA.html> "分区")为单一的 [ext3/4](<../zh-cn/Ext4.html> "Ext4") 分区。
  * 安装基础系统到分区中（例如使用 [arch-install-scripts](<https://archlinux.org/packages/?name=arch-install-scripts>)包 中的 `pacstrap`）
  * 安装引导程序（例如 [GRUB](<../zh-cn/GRUB.html> "GRUB") 或是 [extlinux](</wzh/index.php?title=Extlinux&action=edit&redlink=1> "Extlinux（页面不存在）")）
  * 安装并配置 [cloud-init](<../zh-cn/Cloud-init.html> "Cloud-init")
  * 添加一个可以无密码运行 [sudo](<../zh-cn/Sudo.html> "Sudo") 的用户
  * 为 `eth0` 配置 [DHCP](</wzh/index.php?title=DHCP&action=edit&redlink=1> "DHCP（页面不存在）")
    * 配置 [udev](<../zh-cn/Udev.html> "Udev") 将网络接口命名为 `eth*`
    * 配置 [systemd-networkd](<../zh-cn/Systemd-networkd.html> "Systemd-networkd") 在 `eth0` 上使用 [DHCP](</wzh/index.php?title=DHCP&action=edit&redlink=1> "DHCP（页面不存在）")
  * 安装 [SSH](<../zh-cn/%E5%AE%89%E5%85%A8%E5%A4%96%E5%A3%B3%E5%8D%8F%E8%AE%AE.html> "SSH") 服务器
  * 调整 [initramfs](<../zh-cn/Arch_%E7%9A%84%E5%90%AF%E5%8A%A8%E6%B5%81%E7%A8%8B.html#initramfs> "Initramfs") 配置并重新生成 initramfs 镜像 
    * Disabling the `autodetect` hook (since autodetection works differently from a chroot)
    * Either activating hook `growfs` from [mkinitcpio-growrootfs](<https://aur.archlinux.org/packages/mkinitcpio-growrootfs/>)AUR or installing `growpart` from [cloud-utils](<https://archlinux.org/packages/?name=cloud-utils>)包 and have [cloud-init](<../zh-cn/Cloud-init.html> "Cloud-init") do resizing by itself
  * 通过 [enabling](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Enabling") 来使服务自动启动
  * 删除生成的密钥（例如 SSH 服务器及 pacman)；可以配置为在系统初次启动时自动生成密钥
  * 删除设备ID（`/etc/machine-id` 及 `/var/lib/dbus/machine-id`）以使系统间不会冲突

##  参阅

  * [Wikipedia:OpenStack](<https://en.wikipedia.org/wiki/OpenStack> "wikipedia:OpenStack")
