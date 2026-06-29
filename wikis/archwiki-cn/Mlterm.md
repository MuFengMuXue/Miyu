##  介绍

Mlterm 是一个轻量级的, 高性能的, 多功能的[终端模拟器](<../zh-cn/%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F%E5%88%97%E8%A1%A8/%E5%B7%A5%E5%85%B7.html#%E7%BB%88%E7%AB%AF%E6%A8%A1%E6%8B%9F%E5%99%A8> "终端模拟器")。 

##  安装

请安装 [mlterm-git](<https://aur.archlinux.org/packages/mlterm-git/>)AUR。 

##  使用

打开 Mlterm 后, 即可使用 bash 开始工作, 若需要支持输入法, 请参见 [Mlterm#配置输入法](<#%E9%85%8D%E7%BD%AE%E8%BE%93%E5%85%A5%E6%B3%95>)。 

##  配置

在 Mlterm 中, 我们使用 Ctrl+鼠标Right 组合键打开配置菜单, 如果无效, 请尝试执行 /usr/libexec/mlterm/mlconfig 手动打开。 

调整配置之后, 可以通过 **Apply & Exit** 临时应用, 或 **Save & Exit** 永久应用。 

###  配置输入法

Mlterm 默认不使用输入法, 需要在配置菜单中手动设置, 一般选择 **XIM** 即可, 如果使用 [iBus](<../zh-cn/IBus.html> "IBus"), 请选择 **iBus** 。 

###  配置外观

滚动条

在配置界面中, 进入 Scrollbar 标签, 可以调整滚动条位置。 

背景

在配置界面中, 进入 Background 标签, 可以调整背景, 以下是各个选项简要说明： 

  * Image: 使用一张图片作为背景。
  * Pseudo Transport: 透明, 需要注意的是, 这只能看到桌面墙纸, 不能看到其他窗口。
