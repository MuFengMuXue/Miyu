**警告：** 在对磁盘进行任何操作之前一定要慎重！

相关文章

  * [fdisk](<../zh-cn/Fdisk.html> "Fdisk")
  * [parted](<../zh-cn/Parted.html> "Parted")
  * [GPT fdisk](<../zh-cn/GPT_fdisk.html> "GPT fdisk")
  * [分区](<../zh-cn/%E5%88%86%E5%8C%BA.html> "分区")

[![](../File:700px-Cfdisk%E7%95%8C%E9%9D%A2%E6%88%AA%E5%9B%BE.png)](<../File:Cfdisk%E7%95%8C%E9%9D%A2%E6%88%AA%E5%9B%BE.png>)简体中文环境下 cfdisk 用户界面

cfdisk 是 [fdisk](<../zh-cn/Fdisk.html> "Fdisk") 的 TUI 版本，提供了基本的分区功能和基于 curses 库的用户界面。 

与 [fdisk](<../zh-cn/Fdisk.html> "Fdisk") 不同的是，cfdisk 可能对新手会更友好，因为它为之提供了一个可视化的界面。 

##  安装

cfdisk 由 [util-linux](<https://archlinux.org/packages/?name=util-linux>)包 软件包提供，而 [util-linux](<https://archlinux.org/packages/?name=util-linux>)包 软件包是 [base](<https://archlinux.org/packages/?name=base>)包 元软件包的依赖软件包。所以，一般您无需显式安装 cfdisk。 

##  使用

要使用 cfdisk 管理某[块设备](<../zh-cn/%E8%AE%BE%E5%A4%87%E6%96%87%E4%BB%B6.html#%E5%9D%97%E8%AE%BE%E5%A4%87> "块设备")，输入： 
    
    # cfdisk _/dev/sda_
    
**注意：** 将 _/dev/sda_ 改为您希望进行操作的[块设备](<../zh-cn/%E8%AE%BE%E5%A4%87%E6%96%87%E4%BB%B6.html#%E5%9D%97%E8%AE%BE%E5%A4%87> "块设备")，而**不是** 分区。

关于用户界面的使用，参见 [cfdisk(8) § COMMANDS](<https://man.archlinux.org/man/cfdisk.8#COMMANDS>)。 

关于 cfdisk 命令行选项，参见 [cfdisk(8) § OPTIONS](<https://man.archlinux.org/man/cfdisk.8#OPTIONS>)。 

##  技巧与提示

###  输出着色

####  使用配置文件

输出着色由 [terminal-colors.d(5)](<https://man.archlinux.org/man/terminal-colors.d.5>) 功能实现。可以通过空文件 `/etc/terminal-colors.d/cfdisk.disable` 禁用针对 cfdisk 的隐式着色。 

用户指定的 `$XDG_CONFIG_HOME/terminal-colors.d` 或 `$HOME/.config/terminal-colors.d` 会覆盖全局设置。 

**注意：** 输出着色可能默认启用，在这种情况下，terminal-colors.d 目录不必存在。

cfdisk 不支持使用 color-scheme 文件自定义颜色。 

####  使用命令行选项

可以使用命令行选项 `-L, --color[=_when_]` 为输出结果着色。可选参数 _when_ 可以是 **auto** 、**never** 或 **always** 。如果省略 _when_ 参数，则默认为 **auto** 。可以禁用颜色，有关当前内置默认值，请参阅 `--help` 输出。 

##  参见

[cfdisk(8)](<https://man.archlinux.org/man/cfdisk.8>)
