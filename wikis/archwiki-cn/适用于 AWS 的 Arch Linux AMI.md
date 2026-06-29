**翻译状态：**

  * 本文（或部分内容）译自 [Arch Linux AMIs for Amazon Web Services](<https://wiki.archlinux.org/title/Arch_Linux_AMIs_for_Amazon_Web_Services> "arch:Arch Linux AMIs for Amazon Web Services")，最近一次同步于 2024-05-29，若英文版本有所[更改](<https://wiki.archlinux.org/title/Arch_Linux_AMIs_for_Amazon_Web_Services?diff=0&oldid=807254>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Arch_Linux_AMIs_for_Amazon_Web_Services_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

##  开放社区的 Arch AMI

**注意：** Arch Linux 目前暂不提供 _A_ mazon _M_ achine _I_ mages 的官方支持。以下 AMI 由社区创建。

### AMI

**可以在这里找到 Arch Linux AMI：**<http://arch-ami-list.drzee.net/>

AMI 每月构建两次（一号及15号的 2:00am UTC），并在所有默认启用的地区中提供（参见[地域列表](<https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-available-regions>)）。如果需要在目前不支持的地域使用，可以手动将 AMI [复制](<https://aws.amazon.com/premiumsupport/knowledge-center/copy-ami-region/>)到目标区域。 

这些 AMI 属于 EBS HVM AMI，并提供了两个内核选项： 

  * **std** \- 使用来自默认 Arch 软件源的标准内核，并带有一些在 EC2 上使用所必须的模块。调度器和 I/O 并没有针对云端使用进行优化，性能上可能较低。
  * **ec2** \- 使用了由 UplinkLabs 从默认 Arch Linux 内核修改而来的，针对 EC2 进行优化的内核，存放于独立的源内：参见 <https://git.uplinklabs.net/steven/ec2-packages.git>

两个内核都已在多种 EC2 实例上经过测试（t2，t3，t3a，m/r/c5，m/r/c6 以及带有多 GPU 等高级硬件的实例上）并能正常启动。 

**注意：** 截止至 2023-06-12，已确认到 UplinkLabs 提供的 EC2 优化内核在使用 XEN 虚拟化管理器的实例（例如 `t2-micro`）上启动时会卡住，原因是 XEN 内核模块默认没有打包进最新的内核里。请确保仅使用新的 Nitro 虚拟化管理器实例 - 参见 [Instances build on Nitro](<https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/instance-types.html#ec2-nitro-instances>)。这些实例仍可以使用 EC2 优化内核。

**注意：****ec2** 仓库除 **linux-ec2** 内核外也提供了其它的包。默认情况下，**ec2** 被设置为 `pacman.conf` 中最顶层的镜像，导致 **ec2** 中的包比[官方仓库](<../zh-cn/%E5%AE%98%E6%96%B9%E4%BB%93%E5%BA%93.html> "官方仓库")拥有更高的优先级。取决于具体的包版本，这可能会导致一些一致性问题。

未构建使用 LTS 内核的 AMI。 

###  使用 REST API 获取 AMI 列表

可以使用如下 REST API 获取 JSON 格式的可用 AMI 列表： 

**注意：** API 终端已配置为自定义域名，应不会出现更改。

  * 获取所有 AMI：`<https://arch-ami-api.drzee.net/>`
  * 获取各个地域最新 AMI 的清单：`<https://arch-ami-api.drzee.net/latest>`（与 <http://arch-ami-list.drzee.net/> 的内容相同，但格式为 JSON）
  * 获取单个地域内的的所有 AMI：`<https://arch-ami-api.drzee.net/region>` \- 将 `region` 替换为要查看的地域：例如 `eu-north-1`, `eu-west-1`，`us-east-1` 等等。
  * 按照 CPU 架构列出地域中的所有 AMI：`<https://arch-ami-api.drzee.net/region/arch>` \- 将 `arch` 替换为 `x86_64`
  * 按照 CPU 架构和内核类型列出地域中的所有 AMI：`<https://arch-ami-api.drzee.net/region/arch/type>` \- 将 `type` 替换为 `std` 或者 `ec2`
  * 按照 CPU 架构和内核类型列出地域中的最新 AMI：`<https://arch-ami-api.drzee.net/region/arch/type/latest>` \- 替换 `region`、`arch` 和 `type`

###  初次运行

**注意：** AMI 内置的镜像源清单在镜像构建时生成，使用位于德国的服务器。

启动了 AMI 后，建议/必须执行以下步骤以初始化 pacman 并选择最快的软件源： 
    
    # pacman-key --init
    # pacman-key --populate
    # reflector --country "_ISO 3166-1 Alpha-2 Country Code_ " --protocol https,http --score 20 --sort rate --save /etc/pacman.d/mirrorlist
    # pacman -Syu
    
[Reflector](<../zh-cn/Reflector.html> "Reflector") 包已随 AMI 附带。 

建议在 `/etc/xdg/reflector/reflector.conf` 配置设置，然后启用定时服务来自动定时更新镜像清单。具体信息请参考 [Reflector](<../zh-cn/Reflector.html> "Reflector") 文档。 

你也可以使用自己的镜像源清单，而不使用 reflector。 

###  构建流程

**注意：** 该部分简单介绍了 AMI 是如何构建的。

整个构建流程位于 AWS 上，并完全自动化进行。 

构建流程由 AWS Step Function 控制，并随一个 Amazon EventBridge 定时事件周期运行。 

Step function 负责启动构建，在更复杂的功能上结合使用了一系列本地调用及 AWS Lambda 函数来达成。 

新的 AMI 构建流程为：使用旧的 AMI 启动一台 EC2 实例作为 _工作/构建机器_ ，该实例上带了一套特殊的构建脚本，使用了 pacstrap 和一些额外步骤来生成镜像。大致步骤在下一节进行介绍。 

完成 AMI 构建后，新的 AMI 会在新的 EC2 实例上进行 _测试启动_ 以验证其可以正常启动。成功后，AMI 将会被分发到各个地域，并在一个 DynamoDB 数据库上进行记录。数据库内容可以由 REST API 进行调取。旧 AMI 将从各个地域及 DynamoDB 数据库中删除。 

###  致谢

感谢来自 UplinkLabs 的 **Steven** 协助解析构建流程，并测试了镜像的早期质量。同时感谢 **Mathcom** 的脚本（遗憾的是文章已被移除），帮助加快了构建流程的基础搭建。 

你可以发送评论和建议（不保证会被查看）到：**arch-ami 'at' drzee.net**

###  未来工作

  * 在默认 Arch Linux 源中加入官方的 EC2/云平台优化内核
  * 在默认 Arch Linux 源中加入 AWS CLI v2（v1 已在源内，但未来可能会停止更新） 
    * 由于 AWS CLI v2 与 Python 3.12 的兼容问题，其已被移出 Extra 源 - 当前镜像将继续使用 aws-cli v1

##  构建 Arch AMI

你也可以自己构建 Arch Linux AMI，具体步骤可以参考 [[1]](<http://arch-ami-list.drzee.net/ami_build_howto.html>)。 
