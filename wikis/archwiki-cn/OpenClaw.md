**注意：** 本文先于其对应的英文页面创建，请英文水平较高的翻译者尽快同步到英文页面。直到英文页面足够完善为止，请编辑人员不要移除此提示，也不要不加选择地将英文页面同步到本页面。

相关文章

  * [Node.js](<../zh-cn/Node.js.html> "Node.js")

[OpenClaw](<https://openclaw.ai/>)是奥地利程序员彼得·斯坦伯格开发的开源AI智能体，用户可以通过即时通讯工具与其对接，远程操控电脑实现自动化处理邮件、阅读文档、编写代码、发布社交媒体内容等工作。 

##  安装

安装 [openclaw](<https://aur.archlinux.org/packages/openclaw/>)AUR 软件包。如需安装开发版，安装 [openclaw-git](<https://aur.archlinux.org/packages/openclaw-git/>)AUR 软件包。 

###  官方安装方法

首先，安装 [nodejs](<https://archlinux.org/packages/?name=nodejs>)包，[npm](<https://archlinux.org/packages/?name=npm>)包 和 [git](<https://archlinux.org/packages/?name=git>)包。其中，[nodejs](<https://archlinux.org/packages/?name=nodejs>)包 可以用其长期支持版本 [nodejs-lts-krypton](<https://archlinux.org/packages/?name=nodejs-lts-krypton>)包 或 [nodejs-lts-jod](<https://archlinux.org/packages/?name=nodejs-lts-jod>)包 替代。终端输入：
    
    curl -fsSL https://openclaw.ai/install.sh | bash
    
一条语句即可完成整个安装过程。当前两个 [AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR") 包的表现均不稳定，经常出现各种各样的 bug，使用官方安装方法可以避免 [AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR") 打包造成的 bug，如果你需要你的 OpenClaw 长时间不间断工作，而不在乎它是否能用 [pacman](<../zh-cn/Pacman.html> "Pacman") 管理，建议使用官方安装方法。 

###  通过 [nix](<../zh-cn/Nix.html> "Nix") 安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [nix](<https://archlinux.org/packages/?name=nix>)包，切换到 unstable 源，然后运行：
    
    nix-env -iA nixpkgs.openclaw
    
注意，除非你正在使用 nix 管理其他软件包，否则不建议单独为了 OpenClaw 使用这种安装方法，因为这会导致 nix 下载海量的与 Arch Linux 已有软件包重复的依赖，占用大量磁盘空间。 

##  配置

安装好 OpenClaw 之后，通过以下命令运行新手引导：
    
    openclaw onboard --install-daemon
    
详细的配置方法详见[官方文档](<https://docs.openclaw.ai/zh-CN/start/wizard>)。 

为了使用 OpenClaw，你需要提前准备一个大模型的 API Key，一个 AI 搜索引擎的 API Key，以及一个即时通讯软件，并且你可能需要为大模型提供商进行适当充值。OpenClaw 兼容的大模型、AI搜索引擎和即时通讯软件会在新手引导中全部列出，如果你没有提前准备，在新手引导过程中选择并注册一个也是可以的。 

配置完成后，运行
    
    openclaw dashboard
    
即可在浏览器中打开控制 UI 。你也可以把该页面加入浏览器的书签，之后可以通过浏览器直接进入。 

##  迁移

如果你重新安装了 Arch Linux，从其他发行版迁移到了 Arch Linux，从 Arch Linux 迁移到了其他发行版，更换了安装方式，或者更换了电脑，那么你都需要进行迁移工作。 

首先，在**迁移之前** ，在**旧系统** 的终端运行：
    
    openclaw gateway stop
    
停止 OpenClaw 网关运行，以防止迁移过程中数据发生改变。然后，备份家目录下的 .openclaw 目录。之后，在新系统上安装 OpenClaw。如果是同一系统，仅变更安装方式，需要删除旧的软件包以避免冲突。之后，将 .openclaw 目录复制到新系统的家目录。不必运行新手引导，而是直接运行：
    
    openclaw doctor
    
程序会自动修复配置文件，原来的数据都会保留，不需要重新配置。之后，在**新系统** 的终端运行：
    
    openclaw gateway restart
    
即可在新系统上使用 OpenClaw。 

##  注意事项

OpenClaw 需要系统级权限来执行任务，不当使用会造成数据泄露、误删除重要数据、感染病毒等多种风险。一些降低安全风险的方法包括： 

  * 如果你有两台以上的电脑，专门用一台运行 OpenClaw，其他电脑存放重要数据。（物理隔离，最安全）
  * 使用沙盒运行 OpenClaw。如果你通过 [openclaw](<https://aur.archlinux.org/packages/openclaw/>)AUR 或 [openclaw-git](<https://aur.archlinux.org/packages/openclaw-git/>)AUR 安装了OpenClaw，则 [bubblewrap](<../zh-cn/Bubblewrap.html> "Bubblewrap") 沙盒一般已作为依赖安装。
  * 在[虚拟机](<https://zh.wikipedia.org/wiki/%E8%99%9A%E6%8B%9F%E6%9C%BA> "wiki-zh:虚拟机")中安装 OpenClaw。
  * 使用 [Arch + Windows 双系统](<../zh-cn/Arch_+_Windows_%E5%8F%8C%E7%B3%BB%E7%BB%9F.html> "Arch + Windows 双系统")，将重要数据放在 Windows 一侧，并尽量不要直接挂载 Windows 所在分区。你甚至可以用 BitLocker 加密 Windows 所在分区以阻止 Arch Linux 挂载 Windows 所在分区。

##  常见问题

###  [openclaw](<https://aur.archlinux.org/packages/openclaw/>)AUR 编译太慢了

[openclaw](<https://aur.archlinux.org/packages/openclaw/>)AUR 编译时使用 [npm](<https://archlinux.org/packages/?name=npm>)包，而 [npm](<https://archlinux.org/packages/?name=npm>)包 官方服务器在国外，国内访问延迟较大。改为使用国内 NPM 镜像可以大大增加下载速度：
    
    npm config set registry https://registry.npmmirror.com #阿里云镜像
    
或
    
    npm config set registry https://mirrors.cloud.tencent.com/npm/ #腾讯云镜像
    
或
    
    npm config set registry https://mirrors.tuna.tsinghua.edu.cn/npm/ #清华大学镜像
    
###  [Bash](<../zh-cn/Bash.html> "Bash") 找不到命令

常见于使用 [nix](<../zh-cn/Nix.html> "Nix") 安装的 OpenClaw，或从 [nix](<../zh-cn/Nix.html> "Nix") 迁移到其他安装方法的 OpenClaw。重启系统即可解决。 

###  安装 [openclaw-git](<https://aur.archlinux.org/packages/openclaw-git/>)AUR 时 prepare 中发生一个错误

[openclaw-git](<https://aur.archlinux.org/packages/openclaw-git/>)AUR 上游的部分文件逻辑已经改变，而打包者仍未更新 [PKGBUILD](<../zh-cn/PKGBUILD.html> "PKGBUILD") 及 openclaw-patch.sh。SolarAquarion 提供了[一个修改后的版本](<https://gist.github.com/SolarAquarion/10b9b2fb0a9bc7fd02f8c49e382a0a4e>)，可以尝试替换源文件后手动 [makepkg](<../zh-cn/Makepkg.html> "Makepkg")。 

###  在[即时通讯软件](<../zh-cn/%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F%E5%88%97%E8%A1%A8/%E4%BA%92%E8%81%94%E7%BD%91.html#%E5%8D%B3%E6%97%B6%E9%80%9A%E8%AE%AF%E5%AE%A2%E6%88%B7%E7%AB%AF> "应用程序列表/互联网")上向 OpenClaw 发送消息没有反应

短期解决方法是在 OpenClaw 控制界面提示 OpenClaw 查收即时通讯软件消息，长期解决方法是让 OpenClaw 自己诊断并修复。 

##  参见

  * [官方文档](<https://docs.openclaw.ai/>)
  * [如何解决使用npm安装依赖时遇到卡住不动速度慢的问题，有那些可用的npm源能解决？](<https://cloud.tencent.com/developer/article/2471855>)
