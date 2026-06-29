**翻译状态：**

  * 本文（或部分内容）译自 [ISCSI/LIO](<https://wiki.archlinux.org/title/ISCSI/LIO> "arch:ISCSI/LIO")，最近一次同步于 2025-07-13，若英文版本有所[更改](<https://wiki.archlinux.org/title/ISCSI/LIO?diff=0&oldid=830837>)，则您可以帮助同步与[翻译](<../../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/ISCSI_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)/LIO_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[LIO](<https://web.archive.org/web/20221006024049/http://linux-iscsi.org/wiki/Main_Page>)（LinuxIO）是从 Linux 2.6.38 开始内置在内核的 [iSCSI](<../../zh-cn/ISCSI.html> "ISCSI") 目标。 

##  安装

Linux 从 3.1 版本开始自带 iSCSI 目标框架。 

需要用到的两个内核模块为 _target_core_mod_ 和 _iscsi_target_mod_ ，应已内置在内核中，并会自动加载。 

强烈建议使用开放分支版本的包：[targetcli-fb](<https://aur.archlinux.org/packages/targetcli-fb/>)AUR，[python-rtslib-fb](<https://aur.archlinux.org/packages/python-rtslib-fb/>)AUR 和 [python-configshell-fb](<https://archlinux.org/packages/?name=python-configshell-fb>)包。 

[启动/启用](<../../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动/启用")随 [python-rtslib-fb](<https://aur.archlinux.org/packages/python-rtslib-fb/>)AUR 安装的 `target.service` 来加载需要的模块，载入配置并加载之前保存的 iSCSI 目标配置。 

## targetcli

以 [root](<../../zh-cn/%E7%94%A8%E6%88%B7%E5%92%8C%E7%94%A8%E6%88%B7%E7%BB%84.html#%E6%A6%82%E8%A7%88> "Root") 身份运行 `targetcli status` 来查看使用中配置的相关信息。 

你可以使用 **targetcli** 来创建完整配置文件，具体信息可参考 targetcli(8)。 

交互式配置终端会自动为你填充大部分名称和参数，但你也可以自行指定配置信息。 在终端内的任何时候，你都可以输入 `help` 来查看当前的可用命令。 

**提示：** 在该终端内，你可以使用 tab 进行命令补全，也可以使用 `cd` 来查看并选择路径。

在启动目标后（步骤参考上方），你可以通过 
    
    # targetcli

进入到交互式配置终端。 

在该终端下，选定一个块设备（此处以 `/dev/disk/by-id/md-name-nas:iscsi` 为例）： 
    
    /backstores/block> create md_block0 /dev/disk/by-id/md-name-nas:iscsi
    
**注意：** 你可以使用任意块设备，也可以使用 RAID 和 LVM 卷。如果你打算使用 fileio 而不是块存储对象，也可以指定一个文件。

然后创建一个 iSCSI 限定名称（IQN）和目标门户组（TPG）： 
    
    ...> cd /iscsi
    /iscsi> create
    
**注意：** 如果要自行指定 IQN，可在 `create` 后加上想要的名称。

接下来让 LIO 使用你指定的块设备作为目标的后端存储（ _backstore_ ）： 

**注意：** 你可以通过 `cd` 进入到你环境下的 <iqn>/tpg1 路径。
    
    .../tpg1> cd luns
    .../tpg1/luns> create /backstores/block/md_block0
    
然后创建一个门户（ _portal_ ），这将创建一个守护进程来监听上行连接： 
    
    .../luns/lun0> cd ../../portals
    .../portals> create
    
Targetcli 将汇报 LIO 监听的 IP 及端口（默认为 0.0.0.0（所有地址））。 你至少需要将 IP 提供给客户端，端口应为标准的 3260 端口。 

为了让客户端/[发起方](<../../zh-cn/ISCSI_initiator.html> "ISCSI initiator")能够连接到目标，你需要将发起端的 IQN 加入到目标的配置中： 
    
    ...> cd ../../acls
    .../acls> create iqn.2005-03.org.open-iscsi:SERIAL
    
你应使用发起端的 IQN，而不是照抄 `iqn.2005-03.org.open-iscsi:SERIAL` 到命令中。 一般可以在 `/etc/iscsi/initiatorname.iscsi` 找到 IQN。 你需要对每一个用到该目标的发起端都进行该操作。 Targetcli 会自动将创建的 LUN 映射到最近创建的 ACL 下。 

**注意：** 你可以修改自动映射的 LUN，也可以修改其读写权限。具体信息可在该步骤时输入 `help create` 来查看。

确认配置起效后，最后一步是保存配置： 
    
    ...> cd /
    /> saveconfig
    
这一步将把配置保存在 `/etc/target/saveconfig.json` 文件内。 你现在就可以安全地启动和停止 `target.service` 了，不用担心丢失配置。 

**提示：** 你可以在使用 `saveconfig` 时将文件名作为参数传入，也可以使用 `clearconfig` 清空所有配置。

###  认证

目标默认启用 CHAP 认证。 你可以选择配置一个密码，也可以禁用认证。 

####  禁用认证

在 targetcli 中进入到目标的路径下（例如 /iscsi/iqn.../tpg1），然后： 
    
    .../tpg1> set attribute authentication=0
    
**警告：** 设置该参数后，知道任一发起方 IQN 的人都可以连接到该目标。建议仅用于测试或家庭环境中。

####  配置凭据

在 targetcli 中进入到目标的具体 ACL 路径下（例如 /iscsi/iqn.../tpg1/acls/iqn.../），然后： 
    
    ...> get auth
    
这将显示当前的认证凭据。 
    
    ...> set auth userid=<username in target>
    ...> set auth password=<password in target>
    ...> set auth mutual_userid=<username in initiator>  (optional)
    ...> set auth mutual_password=<password in initiator>  (optional)
    
前两个字段是目标的用户名和密码，发起方会使用该信息登录到目标。后两个字段（以“mutual_”开头）是发起方的用户名和密码（注意，所有发起方都使用同一个用户名和密码）。这两个是可选参数，用于确保发起方仅接受已授权的目标的连接。 

##  小技巧

  * 可以使用 `targetcli sessions` 查看当前开启的会话。

##  参考

  * [targetcli](<http://www.linux-iscsi.org/wiki/Targetcli>)
  * [Persistent block device naming](<../../zh-cn/Persistent_block_device_naming.html> "Persistent block device naming") in order to use the correct block device for a target
