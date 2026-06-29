**翻译状态：**

  * 本文（或部分内容）译自 [Cloud-init](<https://wiki.archlinux.org/title/Cloud-init> "arch:Cloud-init")，最近一次同步于 2024-11-02，若英文版本有所[更改](<https://wiki.archlinux.org/title/Cloud-init?diff=0&oldid=819930>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Cloud-init_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[Cloud-init](<https://cloud-init.io/>) 包含多个用于云实例早期初始化的工具，提供给在云上环境（如 OpenStack，[AWS](<../zh-cn/%E9%80%82%E7%94%A8%E4%BA%8E_AWS_%E7%9A%84_Arch_Linux_AMI.html> "AWS") 等）运行的 Arch Linux 映像所用。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [cloud-init](<https://archlinux.org/packages/?name=cloud-init>)包 包。 

如果你需要使用 [growpart 模块](<https://cloudinit.readthedocs.io/en/latest/reference/modules.html#growpart>)，须同时安装 [cloud-guest-utils](<https://archlinux.org/packages/?name=cloud-guest-utils>)包 包。 

##  配置

该部分仅描述了最基础的配置选项，完整选项可参考 [cloud-init 文档](<https://cloudinit.readthedocs.io>)。 

主配置文件为 `/etc/cloud/cloud.cfg`。需要加载的其它 `*.cfg` 配置文件可放置于 `/etc/cloud/cloud.cfg.d` 目录下，所有配置内容都将被[整合到一起](<https://cloudinit.readthedocs.io/en/latest/reference/merging.html>)。 

cloud-init 19.3 及更新版本的默认配置可直接用于多数知名云环境中。简单来讲，该配置文件进行了如下操作： 

  * 禁用根用户，创建用于登录的 `arch` 用户
  * 依靠 cloud-init 的内置数据源检测
  * 运行所有在 Arch Linux 上已知可用的模块

根据用例不同，可能需要修改默认配置文件。 

###  配置默认用户

默认配置中包含了如下内容（为简洁起见已省略注释）： 
    
    users:
       - default
    
该配置指定了要添加到系统中的用户。`default` 这一特殊名称意为 `system_info` 一节中的 `default_user`（参考下列内容），但[该部分语法](<https://cloudinit.readthedocs.io/en/latest/reference/examples.html#including-users-and-groups>)可使用多种参数配置任意用户信息。该列表中的第一个用户将被其它模块作为“默认用户”（例如通过云环境传递的信息配置 SSH 的模块）。 
    
    disable_root: true
    
禁用根用户通过 SSH 进行访问。你也可以在映像中删除根用户密码： 
    
    # passwd -d root
    
    system_info:
       default_user:
         name: arch
         lock_passwd: true
         gecos: arch Cloud User
         groups: [wheel, adm]
         sudo: ["ALL=(ALL) NOPASSWD:ALL"]
         shell: /bin/bash
    
以上为分发包中指定的默认用户信息： 

  * 默认用户名为 `arch`
  * 默认用户为密码锁定状态，即你只可以通过启动时配置的 SSH 密钥登录到实例中
  * 默认用户将加入到 `adm` 和 `wheel` 组中
  * 默认用户可以无密码使用 `sudo`
  * 默认用户的终端环境为 `/bin/bash`

注意，只有当上面的 `users:` 一节包含了特殊用户“default”（或这一节被完全移除）时，这里配置的用户信息才会被应用。 

###  配置数据源

数据源指定了启动时如何拉取实例的元数据，取决于实例运行的具体云环境（OpenStack，AWS，OpenNebula 等）。在这背后，这一操作为对应模块实现的部分公用接口的方法。 

默认配置文件不指定任何数据源，即 cloud-init 将自动检测云环境。但是，部分云环境无法被自动检测，或是需要特殊配置才能正常工作。在这一情况下，数据源可用于手动进行指定和配置。详细信息可参考文档中的[已知数据源列表](<https://cloudinit.readthedocs.io/en/latest/reference/datasources.html#known-sources>)一节。 

如需指定数据源列表，可在 `/etc/cloud/cloud.cfg` 配置文件中加入如下内容： 
    
    datasource_list: [ NoCloud, ConfigDrive, OpenNebula, Azure, AltCloud, OVF, MAAS, GCE, OpenStack, CloudSigma, Ec2, CloudStack, None ]
    
这一操作将指示 cloud-init 在下载实例元数据时需要加载哪些模块。另外，可以对单个数据源进行更详细的配置： 
    
    datasource:
      OpenStack:
        metadata_urls: [ 'http://169.254.169.254:80' ]
        dsmode: net
    
上述配置告知 OpenStack 数据源使用 `http://169.254.169.254:80` URL 来下载元数据，并在网络初始化之后再运行。这两项都是默认行为，可以省略不写。 

###  模块

Cloud-init 默认包含了[一系列模块](<https://cloudinit.readthedocs.io/en/latest/reference/modules.html>)，可按需进行启用或禁用。默认配置启用了所有已知在 Arch Linux 上可用的模块。被忽略的模块包含如分发版或操作系统特定模块等。 

实际上，模块被启用不代表它们一定会进行任何操作。它们会检查是否有任何相关配置被传入（如云环境通过数据源传入的配置），之后再进行相关操作。因此，启用所有模块通常可以最大化对不同云环境的兼容性。不论如何，你可以在配置文件中移除确定不需要的模块，以达到提升启动速度等效果。你可以在启动的实例上运行 `cloud-init analyze` 命令来检查各模块占用的启动时长。 

部分模组会向 cloud-init 宣称它在哪些分发版上进行过验证。除非在 `cloud.cfg` 中指定的分发版与模组已验证的分发版匹配，就算配置文件中进行了指定，它们也不会运行。如果你想强制绕过该行为，可在配置文件的 `unverified_modules` 部分添加对应模块，例如： 
    
    unverified_modules: ['ssh-import-id']
    
##  Systemd 整合

cloud-init 包提供了四个 [systemd.service(5)](<https://man.archlinux.org/man/systemd.service.5>)，两个 [systemd.target(5)](<https://man.archlinux.org/man/systemd.target.5>) 和一个 [systemd.generator(7)](<https://man.archlinux.org/man/systemd.generator.7>)，并通过依赖关系配置为按如下顺序激活： 

  * `cloud-init-generator`：判断可用数据源，并启用或禁用 `cloud-init.target`
  * `cloud-init-local.service`：需要文件系统可用。将执行 `cloud-init init --local`
  * `cloud-init-main.service`：需要网络可用。将执行 `cloud-init init --all-stages`
  * `cloud-config.target`：对应 cloud-config 启动事件“to inform third parties that cloud-config is available”
  * `cloud-config.service`：执行 `cloud-init modules --mode=config`
  * `cloud-final.service`：执行 `cloud-init modules --mode=final`
  * `cloud-init.target`：当所有服务启动后激活

[Uplink Labs EC2 映像](<../zh-cn/Arch_Linux_AMIs_for_Amazon_Web_Services.html> "Arch Linux AMIs for Amazon Web Services")启用了上述的所有内容，但出于依赖关系这显得有点繁杂。在准备映像时，启用 `cloud-init-main.service` 和 `cloud-final.service` 服务即可。注意，这不代表 cloud-init 一定会被运行 - 这取决于启动早期时 generator 是否成功启用了 `cloud-init.target`。 

更多信息可参考 [cloud-init 启动阶段文档](<https://cloudinit.readthedocs.io/en/latest/explanation/boot.html>)。 

##  用法

### Archiso

[![](../File:Merge-arrows-2.png)](<../File:Merge-arrows-2.png>)**本文或本章节可能需要合并到[Install Arch Linux via SSH#Installation on a headless server](<../zh-cn/Install_Arch_Linux_via_SSH.html#Installation_on_a_headless_server> "Install Arch Linux via SSH")。**

**附注：** It gives more details and illustrates Archiso's cloud-init usage on bare metal.（在 [Talk:Cloud-init](<../zh-cn/Talk:Cloud-init.html>) 中讨论）

以下演示了如何使用 [QEMU](<../zh-cn/QEMU.html> "QEMU") 测试带有 cloud-init 的 [Archiso](<../zh-cn/Archiso.html> "Archiso")（参考 [archlinux/archiso#27](<https://gitlab.archlinux.org/archlinux/archiso/-/issues/27>)）： 

首先使用 YAML 格式创建包含用户名及 SSH 公钥信息的 `user-data` 配置文件。你可以使用 [archiso Merge Request #117](<https://gitlab.archlinux.org/archlinux/archiso/-/merge_requests/117/diffs>) 提供的 `create_cloud-init.sh` 脚本，也可以参考如下示例手动编写，并添加任何 [cloud-init 文档中的额外选项](<https://cloudinit.readthedocs.io/en/latest/reference/examples.html>)。注意，`#cloud-config` 不是 YAML 注释，而是 cloud-init 要求包含的内容。 
    
    #cloud-config
    users:
      - name: vorburger
        ssh_authorized_keys:
          - ssh-rsa (...)
    
我们也可以使用 `meta-data`，但这不是强制需求，可仅放置一空文件（但文件本身需存在）： 
    
    $ touch meta-data
    
然后使用 [libisoburn](<https://archlinux.org/packages/?name=libisoburn>)包 的 _xorriso_ 编译（仅）包含 `user-data` 和 `meta-data` 的 `cloud-init.iso` 文件： 
    
    $ xorriso -as genisoimage -output cloud-init.iso -volid CIDATA -joliet -rock user-data meta-data
    
现在将 `cloud-init.iso` 作为额外驱动器加载到虚拟机中，例如 `qemu-system-x86_64 ... -cdrom cloud-init.iso`，或在使用 [archiso](<../zh-cn/Archiso.html> "Archiso") 时执行 `run_archiso -c`。 

你现在应该能使用 `user-data` 中指定的用户和公钥信息通过 SSH 登录到机子上了。注意，由于启动菜单的延迟时间，可能会需要等待一会才能正常登录（例如 `archlinux*.iso` 的默认启动等待时长为 30s）。对于需要反复测试带有新主机签名的新实例的情况，可以考虑使用 `ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null`。 

**提示：**[Cloud-init's nocloud documenation](<https://cloudinit.readthedocs.io/en/latest/reference/datasources/nocloud.html>) explains an alternative approach, based on using `-smbios type=1,serial=ds=nocloud`. This can be accomplished locally on a host running QEMU and an ad hoc Python webserver as described in the [cloud-init tutorial](<https://cloudinit.readthedocs.io/en/latest/tutorial/qemu.html>). To boot on bare metal you could just "burn" two separate USB sticks, for `archlinux*.iso` and `cloud-init.iso`, and boot from `archlinux*.iso`. When doing this, cloud-init will run using the configuration on `cloud-init.iso`.

##  排障

### FAQ

[Cloud-init FAQ](<https://cloudinit.readthedocs.io/en/latest/reference/faq.html>) 提供了如何对 cloud-init 进行排障的相关资料，其中包括 log 文件的位置，以及如何在开发过程中重新进行数据源检测和重新运行 cloud-init。 

###  映像未挂载

通常先使用 `lsblk` 和 `mount` 检查是否能检测到 cloud-init 映像（ISO）。 

###  "device /dev/sr0 with label cidata not a valid seed"

`user-data` 和 `meta-data` 需要都存在，可以留空。例如，当 nocloud 数据源发现 ISO 只包含 `user-data` 而没有 `meta-data` 时，就会提示 `datasourcenocloud.py warning device /dev/sr0 with label cidata not a valid seed` 报错。 

###  "unhandled non-multipart [...] ssh_authorized_keys"

当 `user-data` 没有以 `#cloud-config` 开头时（虽然 `yamllint` 会提示 `missing starting space in comment`，中间不能出现空格），就会出现 `unhandled non-multipart (text-x-not-multipart) userdata 'b'ssh_authorized_keys` 报错。 

##  参考

  * [cloud-init 文档](<https://cloudinit.readthedocs.io/en/latest/>)
