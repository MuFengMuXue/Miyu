相关文章

  * [Kakoune](</wzh/index.php?title=Kakoune&action=edit&redlink=1> "Kakoune（页面不存在）")
  * [Neovim](<../zh-cn/Neovim.html> "Neovim")
  * [Vis](<../zh-cn/%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F%E5%88%97%E8%A1%A8/%E6%96%87%E6%A1%A3.html#Vi_%E9%A3%8E%E6%A0%BC%E7%9A%84%E6%96%87%E6%9C%AC%E7%BC%96%E8%BE%91%E5%99%A8> "Vis")

**翻译状态：**

  * 本文（或部分内容）译自 [Helix](<https://wiki.archlinux.org/title/Helix> "arch:Helix")，最近一次同步于 2024-10-02，若英文版本有所[更改](<https://wiki.archlinux.org/title/Helix?diff=0&oldid=817676>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Helix_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[Helix](<https://github.com/helix-editor/helix>) 是一个用 Rust 编写的模态（modal）文本编辑器，灵感来自于 [Neovim](<../zh-cn/Neovim.html> "Neovim") 和 [Kakoune](</wzh/index.php?title=Kakoune&action=edit&redlink=1> "Kakoune（页面不存在）")。它对传统的 Vim 工作流程进行了与 Kakoune 类似的修改，如基于选择的编辑和多光标支持。Helix 捆绑并启用了许多开箱即用的功能，目前还没有插件系统。但它可以添加[自定义语言支持](<https://docs.helix-editor.com/languages.html>)。因此，与 Vim 和类似的编辑器相比，Helix 更容易设置，但可定制性较差。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [helix](<https://archlinux.org/packages/?name=helix>)包 软件包，或 [helix-git](<https://aur.archlinux.org/packages/helix-git/>)AUR 开发版本。 

##  配置

Helix 会读取一个可选的 `~/.config/helix/config.toml` 配置文件。可用选项列表请参见官方文档[此](<https://docs.helix-editor.com/configuration.html>)页。 

##  参见

  * [Github 仓库](<https://github.com/helix-editor/helix>)
  * [官方文档](<https://docs.helix-editor.com/title-page.html>)
