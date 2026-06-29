**翻译状态：**

  * 本文（或部分内容）译自 [GoldenDict](<https://wiki.archlinux.org/title/GoldenDict> "arch:GoldenDict")，最近一次同步于 2021-09-25，若英文版本有所[更改](<https://wiki.archlinux.org/title/GoldenDict?diff=0&oldid=697268>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/GoldenDict_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[GoldenDict](<http://goldendict.org>) 一个是功能丰富的字典查找程序。 

##  安装

有几个 AUR 包可以用来[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")

  * [goldendict-git](<https://aur.archlinux.org/packages/goldendict-git/>)AUR 上游不活跃的原版
  * [goldendict-ng-git](<https://aur.archlinux.org/packages/goldendict-ng-git/>)AUR 包含了许多改进的新版本

##  配置

###  脱机字典查找与 dictd

必须先配置 `dictd` 以托管脱机字典。请参阅[托管脱机字典](</wzh/index.php?title=Dictd&action=edit&redlink=1> "Dictd（页面不存在）")。 

一旦安装了字典并配置了 `dictd`，就可以按照以下步骤将 `goldendict` 进行配置以访问 `dictd` 字典数据库： 

  * 按 F3 弹出 "Dictionaries" 窗口
  * 点击 "DICT servers" 选项卡
  * 点击 "Add..."
  * 点击以在 "Enabled" 下打勾
  * 在 "Address" 下双击，然后输入：`dict://localhost`。如果 `dictd` 在另一台服务器上运行，请确保更改 `localhost`。
  * 最后点击 "OK"

### HiDPI

HiDPI下查询结果页面字体过小：使用`Ctrl +`放大，`Ctrl -`缩小。 
