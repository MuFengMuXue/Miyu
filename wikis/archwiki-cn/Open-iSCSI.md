**翻译状态：**

  * 本文（或部分内容）译自 [Open-iSCSI](<https://wiki.archlinux.org/title/Open-iSCSI> "arch:Open-iSCSI")，最近一次同步于 2023-12-12，若英文版本有所[更改](<https://wiki.archlinux.org/title/Open-iSCSI?diff=0&oldid=781573>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Open-iSCSI_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

本文讲述如何通过 [Open-iSCSI](<https://github.com/open-iscsi/open-iscsi>) initiator 访问 [iSCSI](<../zh-cn/ISCSI.html> "ISCSI") 目标。 

**注意：** iSCSI 是**非** 加密的，不建议通过不安全的信道进行数据传输。

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [open-iscsi](<https://archlinux.org/packages/?name=open-iscsi>)包 包。 

**注意：** 旧版的 [Linux-iSCSI](<https://sourceforge.net/projects/linux-iscsi/>) initiator 已经于2005年4月合并进 Open-iSCSI 。不要和 [linux-iscsi.org](<http://linux-iscsi.org/>) 搞混了，这个是 LIO [目标](<../zh-cn/ISCSI_Target.html> "ISCSI Target")的网站。

##  概览

下图显示各组件是如何协同工作的。更详细的版本参见：[Open-iSCSI 模块（已过时）](<https://archive.is/HHYKR/90a7a1c178a2c069a7cbc0b578b6fb5854f827fa.jpg>)。 
    
     +--------------------------------------------------------+             
     | Targets & Sessions configuration files and directories |             
     +--------------------------------------------------------+             
                                                                           
     +--------------------------+     +----------------------------------+ 
     | iscsiadm                 |     | iscsid: iSCSI daemon             | 
     |                          |     |                                  | 
     |  * Command line tool     |<--->|  * Implements Session management | 
     |  * Manages database of   |     |  * Communicates with iscsiadm    | 
     |    sessions and targets  |     |    and iscsi kernel modules      | 
     +--------------------------+     +---------------+------------------+ 
                                                      |                    
     User space                                       |                    
    - - - - - - - - - - - - - - - - - - - - - - - - - | - - - - - - - - - -
     Kernel                                           v                    
             +-----------------------------------------------------------+ 
             | kernel modules: scsi_transport_iscsi, iscsi_tcp, libiscsi | 
             +-----------------------------------------------------------+ 
    
来自 Open-iSCSI [README](<https://github.com/open-iscsi/open-iscsi>)： 

配置持久化由一套文件及目录树实现，一共包括在两个目录中： 

**注意：** 从 [open-iscsi](<https://archlinux.org/packages/?name=open-iscsi>)包 2.1.9-2 开始，数据库主目录由 `/etc/iscsi/` 变更为 `/var/lib/iscsi/`。这一迁移过程不是自动的，需要先断开所有目标并[停止](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "停止")服务，手动迁移后再重新连接。另外，需检查文件系统权限。 

`/etc/iscsi/` 应只包含 `initiatorname.iscsi` 和 `iscsid.conf`

  * 发现目录 `/var/lib/iscsi/send_targets`：包含由目标地址命名的目录
  * 节点目录 `/var/lib/iscsi/nodes`：包含由特定设备的 ION（ISCSI Unique Name）命名的目录

##  配置

###  启动服务

`iscsid` 由一个 systemd 单元来管理。 

[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动") `iscsid.service` 或是 `iscsid.socket`。 

###  ISCSI Qualified Name (IQN)

IQN 被用于识别每个设备。 

Open-ISCSI 将它的 initiator IQN 存放于 `/etc/iscsi/initiatorname.iscsi` 文件中，格式为 `InitiatorName=_iqn_`

在安装过程中会生成初始 IQN，如果你想生成新的 IQN，可以使用 `iscsi-iname` 工具来输出新的 IQN。 

###  认证

如果 ISCSI 目标要求 initiator 进行认证，则需要更新配置文件（`/etc/iscsi/iscsid.conf`）的内容。 

下列参数用于验证从 initiator 到目标的登录会话： 
    
    node.session.auth.authmethod = CHAP
    node.session.auth.username = _initiators_username_
    node.session.auth.password = _initiators_password_
    
如果目标启用了双向验证，则需要额外修改下列参数： 
    
    node.session.auth.username_in = _targets_username_
    node.session.auth.password_in = _targets_password_
    
如果目标需要验证才能获取节点清单（少数情况下出现），则需要额外修改下列参数： 
    
    discovery.sendtargets.auth.authmethod = CHAP
    discovery.sendtargets.auth.username = _initiators_username_
    discovery.sendtargets.auth.password = _initiators_password_
    
如果目标启用了双向验证，则需要额外修改下列参数： 
    
    discovery.sendtargets.auth.username_in = _targets_username_
    discovery.sendtargets.auth.password_in = _targets_password_
    
**警告：** 不能出现两个一样的密码，意味着上述配置中需要四个不同的密码。

**注意：** 验证数据存放在按节点区分的配置文件中。要更新这些数据，可以打开 `/var/lib/iscsi/nodes/iqn._node-name_ /_node-ip-address_ ,_port_ ,1/default` 并按需添加或编辑选项。[[1]](<https://serverfault.com/a/790835>)

###  发现目标

向目标请求节点清单： 
    
    # iscsiadm --mode discovery --portal _target_ip_ --type sendtargets
    
成功后，节点和目标的信息会保存到你的 initiator 中。 

###  手动添加目标
    
    # iscsiadm -m node --target _targetname_ --portal _target_ip_ -o new
    
可以在服务器不允许发现时使用该方法。 

###  删除废旧目标
    
    # iscsiadm -m discovery -p _target_ip_ -o delete
    
###  登录到有效的目标
    
    # iscsiadm -m node -L all
    
或者，登录到指定目标 
    
    # iscsiadm -m node --targetname=_targetname_ --login
    
登出： 
    
    # iscsiadm -m node -U all
    
###  信息

对于运行中的会话 
    
    # iscsiadm -m session -P 3
    
上面命令输出的最后一行会显示连接到的设备名，比如 
    
    Attached scsi disk **sdd** State: running
    
对于已知节点 
    
    # iscsiadm -m node
    
###  在线修改卷大小

如果 iscsi 块设备包含一个分区表，则不能在线修改卷大小。这种情况下必须首先卸载文件系统，然后再调整相关分区的大小。 

  1. 重新扫描当前会话中的活动节点。
         
         # iscsiadm -m node -R

  2. 在多路径环境中，也必须重新扫描多路径下的卷信息。
         
         # multipathd -k"resize map sdx"

  3. 完成后再调整文件系统大小。
         
         # resize2fs /dev/sdx

##  提示

###  检查已连接的 iSCSI 设备

可以用下列命令检查已连接的 iSCSI 设备在 `/dev/` 设备树中的位置： 
    
    $ ls -l /dev/disk/by-path/ip-*
    
###  启动时登录到目标

要在启动时登录到目标，需[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用") `iscsi.service` 服务，并确保节点的配置（`/var/lib/iscsi/nodes/iqn._node-name_ /_node-ip-address_ ,_port_`）中包含 `node.startup = automatic` 一项。 

**注意：** systemd 单元名称为 `iscsi.service`，而不是 `iscsi**d**.service`。[[2]](<https://bbs.archlinux.org/viewtopic.php?pid=1961776#p1961776>)

##  排障

###  客户端 IQN

你可能需要在服务端（target）的账户配置中添加客户端的 IQN（位于 `/etc/iscsi/initiatorname.iscsi`）。 

###  调试 iSCSI daemon

可以使用如下命令以调试模式运行 iSCSI daemon（确保已停止 `iscsid.service`）： 
    
    # iscsid -d 8 -c /etc/iscsi/iscsid.conf -i /etc/iscsi/initiatorname.iscsi -f
    