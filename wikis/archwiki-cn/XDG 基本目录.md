  
**翻译状态：**

  * 本文（或部分内容）译自 [XDG Base Directory](<https://wiki.archlinux.org/title/XDG_Base_Directory> "arch:XDG Base Directory")，最近一次同步于 2024-09-01，若英文版本有所[更改](<https://wiki.archlinux.org/title/XDG_Base_Directory?diff=0&oldid=815679>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/XDG_Base_Directory_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [Dotfiles](<../zh-cn/Dotfiles.html> "Dotfiles")
  * [XDG 用户目录](<../zh-cn/XDG_%E7%94%A8%E6%88%B7%E7%9B%AE%E5%BD%95.html> "XDG 用户目录")

此文章在[#规范](<#%E8%A7%84%E8%8C%83>)中总结了[XDG基本目录规范](<https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html>)，并在[#支持](<#%E6%94%AF%E6%8C%81>)中跟进软件支持情况。 

##  规范

请阅读[完整规范](<https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html>)。本节将尝试分解其试图实现的核心内容。 

只有`XDG_RUNTIME_DIR`是通过[pam_systemd(8)](<https://man.archlinux.org/man/pam_systemd.8>)默认设置的。根据规范，用户需要显式定义其他变量。更改它可能会导致[PipeWire和Chromium上的屏幕共享出现问题](<../zh-cn/PipeWire.html#KDE_Plasma%E4%B8%8D%E6%98%BE%E7%A4%BA%E9%9F%B3%E9%A2%91%E8%AE%BE%E5%A4%87> "PipeWire")。 

有关变量如何定义，请参见[环境变量#全局](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html#%E5%85%A8%E5%B1%80> "环境变量")。 

###  用户目录

  * `XDG_CONFIG_HOME`
    * 仅可设置单个用于存放特定用户的配置的目录（类似于`/etc`）。
    * 默认应为`$HOME/.config`。

  * `XDG_CACHE_HOME`
    * 仅可设置单个用于存放特定用户的非必要（缓存）数据的目录（类似于`/var/cache`）。
    * 默认应为`$HOME/.cache`。

  * `XDG_DATA_HOME`
    * 仅可设置单个用于存放特定用户的数据文件的目录（类似于`/usr/share`）。
    * 默认应为`$HOME/.local/share`。

  * `XDG_STATE_HOME`
    * 仅可设置单个用于存放特定用户的状态文件的目录（类似于`/var/lib`）。
    * 默认应为`$HOME/.local/state`。

  * `XDG_RUNTIME_DIR`
    * 用于存放特定用户的非必要数据文件，如Sockets、命名管道等。
    * 不需要提供默认值；如果没有设置也未提供等价物，应该发出警告。
    * 必须由用户拥有，访问模式为`0700`。
    * 文件系统符合OS标准。
    * 必须位于本地文件系统上。
    * 可能会定期清理。
    * 每6小时修改一次或设置粘滞位以确保持久性。
    * 只能在用户登录期间存在。
    * 不应该存储大文件，因为它可能是作为tmpfs挂载的。
    * pam_systemd将其设置为`/run/user/$UID`。

###  系统目录

  * `XDG_DATA_DIRS`
    * 由`:`分隔的目录列表（类似于`PATH`）。
    * 默认应为`/usr/local/share:/usr/share`。

  * `XDG_CONFIG_DIRS`
    * 由`:`分隔的目录列表（类似于`PATH`）。
    * 默认应为`/etc/xdg`。

##  支持

[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：** 目前的完整支持/部分支持/硬编码分割不够详细且可能具有误导性。表格可以合并成一个（增加程序如何与规范工作的字段）或使用不同名称的类别。 (在 [Talk:XDG 基本目录#添加支持类别的描述](</wzh/index.php?title=Talk:XDG_%E5%9F%BA%E6%9C%AC%E7%9B%AE%E5%BD%95&action=edit&redlink=1> "Talk:XDG 基本目录（页面不存在）") 中讨论)

此节旨在记录日益增长的使用[XDG基本目录规范](<https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html>)的软件集，该规范于2003年引入。 这是为了通过列出常见的dotfiles及其支持状态来展示此规范的可行性。 对于那些目前不支持基础目录规范的软件，将演示解决方法以模拟该规范。 

解决方法将限于任何不涉及修补源代码、执行存储在[环境变量](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html> "环境变量")中的代码或编译时选项的方法。 这样做的理由是配置应该能够在系统之间移植，而编译时选项会妨碍这一点。 

希望这将成为识别dotfiles及其来源的信息源。 

###  贡献

贡献时，请确保使用正确的章节。 

任何方法都不应需要代码评估、补丁或编译时选项即可获得支持，任何需要这些的都必须被认为是硬编码的。 此外，如果过程容易出错或困难，也应分类为硬编码。 

  * 第一列应该是指向内部文章的链接、[Template:Pkg](<../zh-cn/Template:%E5%8C%85.html> "Template:Pkg")或[Template:AUR](<../zh-cn/Template:AUR.html> "Template:AUR")。
  * 第二列是项目曾经拥有的任何遗留文件和目录（每行一个），即使它们不再被读取，人们也能找到它们。
  * 在第三列中，尽量找到项目开始使用XDG基本目录的commit或版本以及任何公开讨论，并在接下来的两栏中包括它们（每行两个）。
  * 最后一列应包括任何适当的解决或绕过方法。请确认您的解决方案正确且可行。

###  完整支持

应用程序  | 旧路径  | 采用规范自  | 讨论  | 注释   
---|---|---|---|---  
[act](<https://archlinux.org/packages/?name=act>)包 |  `~/.actrc` |  [1656](<https://github.com/nektos/act/pull/1656>) [2195](<https://github.com/nektos/act/pull/2195>) |  [[1]](<https://github.com/nektos/act/issues/1678>) |  `XDG_CONFIG_HOME/act/actrc` `~/.actrc`（如果存在）会与XDG规范路径下的配置文件合并。   
[aerc](<../zh-cn/Aerc.html> "Aerc") |  |  [fff1664](<https://git.sr.ht/~rjarry/aerc/commit/fff1664>) |  |  `XDG_CONFIG_HOME/aerc/aerc.conf`  
[ALSA](<../zh-cn/ALSA.html> "ALSA") |  `~/.asoundrc` |  [577df36](<https://github.com/alsa-project/alsa-lib/commit/577df365f66ee09579864fc771136e690927b3bf>) [1.2.3](<https://github.com/alsa-project/alsa-lib/releases/tag/v1.2.3>) |  [[2]](<https://github.com/alsa-project/alsa-lib/issues/49>) |  `XDG_CONFIG_HOME/alsa/asoundrc`  
[anaconda](<https://aur.archlinux.org/packages/anaconda/>)AUR |  `~/.conda/.condarc`，`~/.conda/condarc`，`~/.conda/condarc.d/`，`~/.condarc` |  [4.11.0](<https://github.com/conda/conda/blob/main/CHANGELOG.md#4110-2021-11-22>) |  [[3]](<https://conda.io/projects/conda/en/latest/user-guide/configuration/use-condarc.html#searching-for-condarc>) [[4]](<https://github.com/conda/conda/pull/10982>) |   
[Android Studio](<https://developer.android.com/studio/index.html>) |  `~/.AndroidStudioX.X` |  [Android Studio 4.1](<https://developer.android.com/studio/intro/studio-config#file_location>) |  | 
    
    XDG_CONFIG_HOME/Google/AndroidStudioX.X
    XDG_DATA_HOME/Google/AndroidStudioX.X
    XDG_CACHE_HOME/Google/AndroidStudioX.X
    
[Google 的配置文件位置概述](<https://developer.android.com/studio/intro/studio-config#file_location>)中没有提到XDG⸺路径有可能是硬编码的（而不是使用适当的变量）。尽管这种情况不太可能发生，因为Android Studio所基于的Intellij IDEA也正确实现了本规范。   
[Anki](</wzh/index.php?title=Anki&action=edit&redlink=1> "Anki（页面不存在）")（英语：[Anki](<https://wiki.archlinux.org/title/Anki> "en:Anki")） |  `~/Anki`，`~/Documents/Anki` |  |  [[5]](<https://github.com/dae/anki/pull/49>) [[6]](<https://github.com/dae/anki/pull/58>) [[7]](<https://docs.ankiweb.net/files.html>) | 如果旧路径不存在，默认使用`$XDG_DATA_HOME/Anki2`，但可以通过使用`anki -b <anki_dir>`修改。   
[antimicrox](<https://archlinux.org/packages/?name=antimicrox>)包 |  `~/.antimicro`，`~/.antimicrox` |  [edba864](<https://github.com/Antimicrox/antimicrox/commit/edba864>) |  [[8]](<https://github.com/Antimicro/antimicro/issues/5>) |   
[apvlv](<https://aur.archlinux.org/packages/apvlv/>)AUR |  `~/.apvlvrc` |  [[9]](<https://github.com/naihe2010/apvlv/commit/ed0e0112b05b0cafa13ca4e215ee559c82194caf>) |  [[10]](<https://github.com/naihe2010/apvlv/issues/70>) | 现在使用`XDG_CONFIG_HOME/apvlv/apvlvrc`（如果存在）。   
[aria2](<../zh-cn/Aria2.html> "Aria2") |  `~/.aria2` |  [8bc1d37](<https://github.com/tatsuhiro-t/aria2/commit/8bc1d37>) |  [[11]](<https://github.com/tatsuhiro-t/aria2/issues/27>) | 
    
    XDG_CONFIG_HOME/aria2/
    XDG_CACHE_HOME/aria2/
      
[atuin](<https://archlinux.org/packages/?name=atuin>)包 |  `~/.config/atuin` `~/.local/share/atuin` |  [156893d](<https://github.com/ellie/atuin/commit/156893d774b4da5b541fdbb08428f9ec392949a0>) |  | 
    
    XDG_CONFIG_HOME/atuin/config.toml
    XDG_DATA_HOME/atuin/history.db
      
[asunder](<https://archlinux.org/packages/?name=asunder>)包 |  `~/.asunder` `~/.asunder_album_artist` `~/.asunder_album_genre` `~/.asunder_album_title` |  [2.9.0](<https://littlesvr.ca/bugs/show_bug.cgi?id=31>)[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2021-05-17 ⓘ] |  [[12]](<https://littlesvr.ca/bugs/show_bug.cgi?id=52>)[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2021-05-17 ⓘ] | 使用`XDG_CONFIG_HOME/asunder/asunder`代替`~/.asunder`，`XDG_CACHE_HOME/asunder/asunder_album_...`代替其他3个文件。迁移后原文件需要手动删除。   
[audacity](<https://archlinux.org/packages/?name=audacity>)包 |  `~/.audacity-data/` |  [3.2.0](<https://github.com/audacity/audacity/releases/tag/Audacity-3.2.0>) |  [[13]](<https://bugzilla.audacityteam.org/show_bug.cgi?id=2201>) | 如果旧路径不存在，则使用以下新路径： 
    
    XDG_CONFIG_HOME/audacity
    XDG_DATA_HOME/audacity
      
[btop](<https://archlinux.org/packages/?name=btop>)包 |  |  [b5e709d](<https://github.com/aristocratos/btop/commit/b5e709d>) |  |  `XDG_CONFIG_HOME/btop`  
[binwalk](<https://archlinux.org/packages/?name=binwalk>)包 |  `~/.binwalk` |  [2051757](<https://github.com/ReFirmLabs/binwalk/commit/2051757>) |  [[14]](<https://github.com/ReFirmLabs/binwalk/issues/216>) |  `XDG_CONFIG_HOME/binwalk`  
[bitwarden-cli](<https://archlinux.org/packages/?name=bitwarden-cli>)包 |  `~/.config/Bitwarden CLI` |  [1.7.1](<https://github.com/bitwarden/cli/releases/tag/v1.7.1>) |  [[15]](<https://github.com/bitwarden/cli/pull/46>) | 
    
    XDG_CONFIG_HOME/Bitwarden CLI
    XDG_DATA_HOME/audacity
    
`BITWARDENCLI_APPDATA_DIR` 环境变量优先。  目前包含一个包含所有保险库数据的 data.json 文件，因此它应该属于XDG_DATA_HOME。   
[Blender](<../zh-cn/Blender.html> "Blender") |  `~/.blender` |  [4293f47](<https://projects.blender.org/blender/blender/commit/4293f47>) |  [[16]](<https://developer.blender.org/T28943>) |   
[byobu](<https://archlinux.org/packages/?name=byobu>)包 |  `~/.byobu` |  [4.17](<https://launchpad.net/byobu/+milestone/4.17>) |  [[17]](<https://bugs.launchpad.net/byobu/+bug/553105>) |  `XDG_CONFIG_HOME/byobu` 如果旧路径存在或者`XDG_CONFIG_HOME`环境变量未设置，则优先使用旧路径。   
[cabal](<https://www.haskell.org/cabal>) |  `~/.cabal/` |  [9f7dc55](<https://github.com/haskell/cabal/commit/9f7dc55>) [v3.10.1.0](<https://github.com/haskell/cabal/releases/tag/cabal-install-v3.10.1.0>) |  [[18]](<https://github.com/haskell/cabal/issues/680>) |   
[calcurse](<https://archlinux.org/packages/?name=calcurse>)包 |  `~/.calcurse` |  [04162d](<https://github.com/lfos/calcurse/commit/04162d>) |  [[19]](<https://github.com/lfos/calcurse/pull/254>) [[20]](<https://github.com/lfos/calcurse/issues/252>) | 
    
    XDG_CONFIG_HOME/calcurse
    XDG_DATA_HOME/calcurse
    
如果旧路径`~/.calcurse`存在，优先使用。   
[calibre](<https://archlinux.org/packages/?name=calibre>)包 |  |  |  |   
[ccache](<https://archlinux.org/packages/?name=ccache>)包 |  `~/.ccache` |  [4.0](<https://ccache.dev/releasenotes.html#_ccache_4_0>) |  [[21]](<https://github.com/ccache/ccache/issues/191>) | 
    
    XDG_CACHE_HOME/ccache
    XDG_CONFIG_HOME/ccache/ccache.conf
      
[catfish](<https://archlinux.org/packages/?name=catfish>)包 |  `~/.config/catfish` |  [af65ed25](<https://gitlab.xfce.org/apps/catfish/-/commit/af65ed25c5d9bd96647664b5f7d4db50551fed8a>) |  [[22]](<https://gitlab.xfce.org/apps/catfish/-/issues/102>)  
[clangd](<https://clangd.llvm.org/config.html>) |  `~/.clangd` |  [fdf7dcc](<https://github.com/JohnHolmesII/llvm-project/commit/fdf7dcc>)[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2022-09-23 ⓘ] |  [[23]](<https://github.com/clangd/clangd/issues/341>) |  `XDG_CONFIG_HOME/clangd/config.yml` `XDG_CACHE_HOME/clangd` 可以在 `proj/.clangd` 中指定项目特定的配置。 在合理的情况下，会组合配置。如果发生冲突，则用户配置具有最高优先级，其次是内部项目，最后是外部项目。   
[Composer](</wzh/index.php?title=Composer&action=edit&redlink=1> "Composer（页面不存在）")（英语：[Composer](<https://wiki.archlinux.org/title/Composer> "en:Composer")） |  `~/.composer` |  [1.0.0-beta1](<https://github.com/composer/composer/releases/tag/1.0.0-beta1>) |  [[24]](<https://github.com/composer/composer/pull/1407>) |   
crossnote  |  `~/.mume` |  [d714a82](<https://github.com/shd101wyy/crossnote/commit/d714a8229c3a757d52a34eadabefb0795568e37d>) [0.8.13](<https://github.com/shd101wyy/crossnote/archive/refs/tags/0.8.13.tar.gz>) |  [[25]](<https://github.com/shd101wyy/crossnote/pull/234>) |  `$XDG_CONFIG_HOME/mume` 如果旧路径存在，优先使用。   
[ctags](<https://archlinux.org/packages/?name=ctags>)包 (universal-ctags)  |  `~/.ctagsrc`，`~/.ctags.d` |  [68da03a](<https://github.com/universal-ctags/ctags/commit/68da03a946cf532e51d014bc9b76265612da0189>) [8fb0b04](<https://github.com/universal-ctags/ctags/commit/8fb0b0445c396a6a041106b752255e3ebe75533d>) |  [Issue 89](<https://github.com/universal-ctags/ctags/issues/89>) [Pull request 2384](<https://github.com/universal-ctags/ctags/pull/2384>) | 在启动时，Universal-ctags会加载`$XDG_CONFIG_HOME/ctags`目录中文件扩展名为“.ctags”的文件。 请参阅[Ctags Option Files](<https://docs.ctags.io/en/latest/option-file.html>)。   
[cURL](<../zh-cn/CURL.html> "CURL") |  `~/.curlrc` |  [7.73.0](<https://curl.se/changes.html#7_73_0>) |  [[26]](<https://github.com/curl/curl/issues/5829>) |  `XDG_CONFIG_HOME/.curlrc`  
[CUPS](<../zh-cn/CUPS.html> "CUPS") |  `~/.cups/` |  [23b1be6](<https://github.com/OpenPrinting/libcups/pull/45/commits/23b1be68803128ed701d374981c4583bcf9e7bf6>) |  [[27]](<https://github.com/OpenPrinting/cups/issues/10>) |  libcups 在 v3 中添加了 XDG 支持（仍处于测试阶段）。官方存储库中的版本仍然硬编码为 `~/.cups`。   
[dconf](<https://archlinux.org/packages/?name=dconf>)包 |  |  |  |   
[Dolphin 模拟器](<../zh-cn/Dolphin_%E6%A8%A1%E6%8B%9F%E5%99%A8.html> "Dolphin 模拟器") |  `~/.dolphin-emu` |  [a498c68](<https://github.com/dolphin-emu/dolphin/commit/a498c68>) |  [[28]](<https://github.com/dolphin-emu/dolphin/pull/2304>) |   
[dr14_t.meter-git](<https://aur.archlinux.org/packages/dr14_t.meter-git/>)AUR |  |  [7e777ca](<https://github.com/simon-r/dr14_t.meter/commit/7e777ca>) |  [[29]](<https://github.com/simon-r/dr14_t.meter/pull/30>) |  `XDG_CONFIG_HOME/dr14tmeter/`  
[dunst](<https://archlinux.org/packages/?name=dunst>)包 |  |  [78b6e2b](<https://github.com/dunst-project/dunst/commit/78b6e2b>) |  [[30]](<https://github.com/dunst-project/dunst/issues/22>) |  `XDG_CONFIG_HOME/dunst/`  
[Emacs](<../zh-cn/Emacs.html> "Emacs") |  `~/.emacs` `~/.emacs.d/init.el` |  [[31]](<https://git.savannah.gnu.org/cgit/emacs.git/commit/?id=4118297ae2fab4886b20d193ba511a229637aea3>) [27.1](<https://www.gnu.org/savannah-checkouts/gnu/emacs/emacs.html#Releases>) |  |  `XDG_CONFIG_HOME/emacs/init.el` 旧路径优先于 XDG 路径。Emacs 永远不会创建 `XDG_CONFIG_HOME/emacs/`。 26.3 或更早版本的绕过方法：可以更改`HOME`，但它可能会产生意想不到的副作用。   
[fish](<../zh-cn/Fish.html> "Fish") |  |  |  |   
[fltk](<https://archlinux.org/packages/?name=fltk>)包 |  `~/.fltk/` |  [7308bcd](<https://github.com/fltk/fltk/commit/7308bcdb74e34626c6459699cb57371afd7b343b>) |  [[32]](<https://www.fltk.org/str.php?L3370+P0+S0+C0+I0+E0+V%25+Qxdg>) [[33]](<https://github.com/fltk/fltk/issues/79>) | 仅尚未发布（截至 2022 年 7 月 9 日）的 1.4.0 版本支持   
[fontconfig](<../zh-cn/%E5%AD%97%E4%BD%93%E9%85%8D%E7%BD%AE.html> "Fontconfig") |  `~/.fontconfig` `~/.fonts` |  [8c255fb](<https://gitlab.freedesktop.org/fontconfig/fontconfig/-/commit/8c255fb>)，[[34]](<https://gitlab.freedesktop.org/fontconfig/fontconfig/-/commit/437f03299bd1adc9673cd576072f1657be8fd4e0>) |  | 配置位于 `XDG_CONFIG_HOME/fontconfig/fonts.conf` 或 `XDG_CONFIG_HOME/fontconfig/conf.d/`，字体存储在 `XDG_DATA_HOME/fonts/`。   
[fontforge](<https://archlinux.org/packages/?name=fontforge>)包 |  `~/.FontForge` `~/.PfaEdit` |  [e4c2cc7](<https://github.com/fontforge/fontforge/commit/e4c2cc7>) |  [[35]](<https://github.com/fontforge/fontforge/issues/847>) [[36]](<https://github.com/fontforge/fontforge/issues/991>) |   
[freecad](<https://archlinux.org/packages/?name=freecad>)包 |  `~/.FreeCAD` |  [e7e2994ba](<https://github.com/FreeCAD/FreeCAD/commit/e7e2994ba>) [0.20.0](<https://github.com/FreeCAD/FreeCAD/releases/tag/0.20>) |  [[37]](<https://forum.freecad.org/viewtopic.php?f=9&t=63648>) | 默认为 
    
    XDG_CONFIG_HOME/FreeCAD
    XDG_DATA_HOME/FreeCAD
    XDG_CACHE_HOME/FreeCAD
    
旧路径可通过`FreeCAD --keep-deprecated-paths`使用   
[freerdp](<https://archlinux.org/packages/?name=freerdp>)包 |  `~/.freerdp` |  [edf6e72](<https://github.com/FreeRDP/FreeRDP/commit/edf6e72>) |  |   
[Gajim](</wzh/index.php?title=Gajim&action=edit&redlink=1> "Gajim（页面不存在）")（英语：[Gajim](<https://wiki.archlinux.org/title/Gajim> "en:Gajim")） |  `~/.gajim` |  [3e777ea](<https://dev.gajim.org/gajim/gajim/commit/3e777ea>) |  [[38]](<https://dev.gajim.org/gajim/gajim/issues/2149>) |   
[gconf](<https://aur.archlinux.org/packages/gconf/>)AUR |  `~/.gconf` |  [fc28caa](<https://gitlab.gnome.org/Archive/gconf/commit/fc28caa>) |  [[39]](<https://bugzilla.gnome.org/show_bug.cgi?id=674803>)  
[GDB](<../zh-cn/GNU.html#%E5%B7%A5%E5%85%B7%E9%93%BE> "GDB") |  `~/.gdbinit`，`~/.gdb_history` |  [11.1](<https://lists.gnu.org/archive/html/info-gnu/2021-09/msg00007.html>) |  |  `XDG_CONFIG_HOME/gdb/gdbinit`，`export GDBHISTFILE="$XDG_DATA_HOME"/gdb/history`  
[ghidra](<https://archlinux.org/packages/?name=ghidra>)包 |  `~/.ghidra/` |  [3b0aac9](<https://github.com/NationalSecurityAgency/ghidra/commit/3b0aac92d0730bb3eaa25d276d15beeef3f55c23>) |  [[40]](<https://github.com/NationalSecurityAgency/ghidra/issues/908>) |   
[GIMP](<../zh-cn/GIMP.html> "GIMP") |  `~/.gimp-x.y` `~/.thumbnails` |  [60e0cfe](<https://gitlab.gnome.org/GNOME/gimp/commit/60e0cfe>) [483505f](<https://gitlab.gnome.org/GNOME/gimp/commit/483505f>) |  [[41]](<https://bugzilla.gnome.org/show_bug.cgi?id=166643>) [[42]](<https://bugzilla.gnome.org/show_bug.cgi?id=646644>) |   
[Git](<../zh-cn/Git.html> "Git") |  `~/.gitconfig`，`~/.gitignore`，`~/.gitattributes`，`~/.git-credentials`，`~/.gitk` |  [0d94427](<https://github.com/git/git/commit/0d94427>)，[dc79687](<https://github.com/git/git/commit/dc79687>)，[684e40f](<https://github.com/git/git/commit/684e40f>) |  [Git Config](<https://git-scm.com/docs/git-config>)，[Git Attributes](<https://git-scm.com/docs/gitattributes>)，[Git Credentials](<https://git-scm.com/docs/git-credential-store>)，[gitk](<https://git-scm.com/docs/gitk>) |  `XDG_CONFIG_HOME/git/config`，`XDG_CONFIG_HOME/git/ignore`，`XDG_CONFIG_HOME/git/attributes`，`XDG_CONFIG_HOME/git/credentials`，`XDG_CONFIG_HOME/git/gitk`  
[gops](<https://github.com/google/gops>) |  |  [71c4255](<https://github.com/google/gops/commit/71c4255>) |  |   
[gnuplot](<https://en.wikipedia.org/wiki/gnuplot> "wikipedia:gnuplot") |  `~/.gnuplot_history` |  [a5562b1](<https://sourceforge.net/p/gnuplot/gnuplot-main/ci/a5562b1/>) [[43]](<https://sourceforge.net/p/gnuplot/gnuplot-main/merge-requests/12/>) |  |   
[goobook](<https://aur.archlinux.org/packages/goobook/>)AUR |  `~/.goobookrc` |  [3.5](<https://gitlab.com/goobook/goobook/-/blob/master/CHANGES.rst>) |  [[44]](<https://gitlab.com/goobook/goobook/-/merge_requests/11>) |  `XDG_CONFIG_HOME/goobookrc`  
[Godot Engine](<../zh-cn/Godot_Engine.html> "Godot Engine") |  `~/.godot` |  [73049d1](<https://github.com/godotengine/godot/pull/12988/commits/73049d115e190b8c356f0689a9079c3c73cc5765>) [3.0-stable](<https://github.com/godotengine/godot/releases/tag/3.0-stable>) |  [[45]](<https://github.com/godotengine/godot/issues/3513>) |   
[GStreamer](<../zh-cn/GStreamer.html> "GStreamer") |  `~/.gstreamer-0.10` |  [4e36f93](<https://gitlab.freedesktop.org/gstreamer/gstreamer/-/commit/4e36f93>) |  [[46]](<https://bugzilla.gnome.org/show_bug.cgi?id=518597>) |   
[GTK](<../zh-cn/GTK.html> "GTK") 3  |  |  |  |   
[Haskell#Stack](</wzh/index.php?title=Haskell&action=edit&redlink=1> "Haskell（页面不存在）")（英语：[Haskell#Stack](<https://wiki.archlinux.org/title/Haskell#Stack> "en:Haskell")） |  `~/.stack` |  [2.9.3](<https://github.com/commercialhaskell/stack/releases/tag/v2.9.3>) |  [[47]](<https://github.com/commercialhaskell/stack/issues/4243>) | 默认为使用旧目录。使用`export STACK_XDG=1`使其符合规范。 旧方法`export STACK_ROOT="$XDG_DATA_HOME"/stack`仍然有效且优先[[48]](<https://docs.haskellstack.org/en/stable/environment_variables/#stack_xdg>)[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2024-07-30 ⓘ]。   
[helm](<https://archlinux.org/packages/?name=helm>)包 |  `~/.helm` |  [3.0.0](<https://github.com/helm/helm/releases/tag/v3.0.0>) |  |   
[htop](<https://archlinux.org/packages/?name=htop>)包 |  `~/.htoprc` |  [93233a6](<https://github.com/hishamhm/htop/commit/93233a6>) |  |  `XDG_CONFIG_HOME/htop/htoprc`  
[httpie](<https://archlinux.org/packages/?name=httpie>)包 |  `~/.httpie` |  [5af0874](<https://github.com/httpie/httpie/commit/5af0874ed302e9ef79cec97836529ccf353e53f7>) |  [[49]](<https://github.com/httpie/httpie/issues/145>) |   
[hunspell](<https://archlinux.org/packages/?name=hunspell>)包 |  `~/.hunspell_default.` |  |  [[50]](<https://github.com/hunspell/hunspell/pull/637>) |   
[i3](<../zh-cn/I3.html> "I3") |  `~/.i3` |  [7c130fb](<http://code.stapelberg.de/git/i3/commit/?id=7c130fb>) |  |   
[i3blocks](<https://archlinux.org/packages/?name=i3blocks>)包，[i3blocks-git](<https://aur.archlinux.org/packages/i3blocks-git/>)AUR |  |  [[51]](<https://github.com/vivien/i3blocks/commit/a1782404c7d933145b048d0d1872ea40d7a293b6>) |  |   
[i3status](<https://archlinux.org/packages/?name=i3status>)包 |  `~/.i3status.conf` |  [c3f7fc4](<http://code.stapelberg.de/git/i3status/commit/?id=c3f7fc4>) |  |   
[i3status-rust](<https://archlinux.org/packages/?name=i3status-rust>)包 |  |  |  |   
[IdeaVim](<https://github.com/JetBrains/ideavim>) |  `~/.ideavimrc` |  [0.54.1-EAP](<https://github.com/JetBrains/ideavim/pull/212>) |  [[52]](<https://youtrack.jetbrains.com/issue/VIM-664>) |  `XDG_CONFIG_HOME/ideavim/ideavimrc`  
[imagemagick](<https://archlinux.org/packages/?name=imagemagick>)包 |  |  |  |   
[iotop-c](<https://archlinux.org/packages/?name=iotop-c>)包 |  `~/.config/iotop` |  [[53]](<https://github.com/Tomas-M/iotop/commit/cea6d5c7a41f2e7a842d4f244532759142af98b0>) |  [[54]](<https://github.com/Tomas-M/iotop/issues/63>) |   
[Inkscape](<../zh-cn/Inkscape.html> "Inkscape") |  `~/.inkscape` |  [0.47](<https://wiki.inkscape.org/wiki/index.php/Release_notes/0.47#Preferences>) |  [[55]](<https://bugs.launchpad.net/inkscape/+bug/199720>) |   
[ipython](<http://ipython.org>) |  `~/.ipython` |  [8.0.0](<https://ipython.readthedocs.io/en/stable/whatsnew/version8.html#re-added-support-for-xdg-config-directories>) |  [[56]](<https://github.com/ipython/ipython/pull/13224>) |  `$XDG_CONFIG_HOME/ipython`（或当`XDG_CONFIG_HOME`不存在时使用的`~/.config/ipython`）不存在时使用旧路径。   
[iwd](<https://iwd.wiki.kernel.org/>) / iwctl  |  `~/.iwctl_history` |  [d3e00d7f](<https://git.kernel.org/pub/scm/network/wireless/iwd.git/commit/?id=d3e00d7f>) |  |   
[intellij-idea-community-edition](<https://archlinux.org/packages/?name=intellij-idea-community-edition>)包 / [intellij-idea-ultimate-edition](<https://aur.archlinux.org/packages/intellij-idea-ultimate-edition/>)AUR |  `~/.IntelliJIdeaXXXX.X` |  [2020.1](<https://confluence.jetbrains.com/display/IDEADEV/IntelliJ%2BIDEA%2B2020.1%2B%28201.6668.121%2Bbuild%29%2BRelease%2BNotes>) |  [[57]](<https://youtrack.jetbrains.com/issue/IDEA-22407>) | 
    
    XDG_CONFIG_HOME/JetBrains/IntelliJIdeaXXXX.X
    XDG_DATA_HOME/JetBrains/IntelliJIdeaXXXX.X
    XDG_CACHE_HOME/JetBrains/IntelliJIdeaXXXX.X
      
[josm](<https://archlinux.org/packages/?name=josm>)包 |  `~/.josm` |  [11162](<https://josm.openstreetmap.de/changeset/11162/josm>) |  [[58]](<https://josm.openstreetmap.de/ticket/6664>) |   
[jupyter](<https://github.com/jupyter>) |  `~/.jupyter` | 在 5.0 中可选择加入，在 6.0 中可选择退出，在 7.0 中强制使用（[changelog](<https://github.com/jupyter/jupyter_core/blob/f5ab1ac19225c7925282e9c5ae466767b4086361/CHANGELOG.md#migrate-to-standard-platform-directories>)）  |  |  `XDG_CONFIG_HOME/jupyter`  
[Kakoune](</wzh/index.php?title=Kakoune&action=edit&redlink=1> "Kakoune（页面不存在）")（英语：[Kakoune](<https://wiki.archlinux.org/title/Kakoune> "en:Kakoune")） |  |  |  |   
[keynav](<https://aur.archlinux.org/packages/keynav/>)AUR |  `~/.keynavrc` |  |  |  `XDG_CONFIG_HOME/keynav/keynavrc`  
[less](<../zh-cn/Core_utilities.html> "Core utilities") |  `~/.lesshst`，`~/.lesskey` |  [590](<https://www.greenwoodsoftware.com/less/news.590.html>) 完整支持：[600](<https://www.greenwoodsoftware.com/less/news.600.html>)[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2024-07-30 ⓘ] |  [[59]](<https://github.com/gwsw/less/issues/153>) | 在 590 版本中**必须** 设置环境变量`XDG_CONFIG_HOME`和`XDG_DATA_HOME`。600 以后版本不再必要。   
latexmk（[texlive-binextra](<https://archlinux.org/packages/?name=texlive-binextra>)包中）  |  `~/.latexmkrc` |  |  |  `XDG_CONFIG_HOME/latexmk/latexmkrc`  
[lftp](<https://archlinux.org/packages/?name=lftp>)包 |  `~/.lftp` |  [21dc400](<https://github.com/lavv17/lftp/commit/21dc400>) |  [[60]](<https://www.mail-archive.com/lftp@uniyar.ac.ru/msg04301.html>) |   
[lgogdownloader](<https://aur.archlinux.org/packages/lgogdownloader/>)AUR |  `~/.gogdownloader` |  [d430af6](<https://github.com/Sude-/lgogdownloader/commit/d430af6>) |  [[61]](<https://github.com/Sude-/lgogdownloader/issues/4>) |   
[luarocks](<https://archlinux.org/packages/?name=luarocks>)包 |  `~/.luarocks` |  [cd16cdd](<https://github.com/luarocks/luarocks/pull/1298/commits/cd16cdd5f889024f28cc384e3d721a4f4a3261d3>) |  [[62]](<https://github.com/luarocks/luarocks/pull/1298>) | 
    
    XDG_CONFIG_HOME/luarocks
    XDG_CACHE_HOME/luarocks
    
如果旧路径`~/.luarocks`存在，优先使用。   
[mangohud](<https://archlinux.org/packages/?name=mangohud>)包 |  |  [65b90fc](<https://github.com/flightlessmango/MangoHud/commit/65b90fc>) |  [[63]](<https://github.com/flightlessmango/MangoHud/issues/37>) |  `XDG_CONFIG_HOME/MangoHud`  
[mc](<../zh-cn/Midnight_Commander.html> "Mc") |  `~/.mc` |  [1b99570](<https://github.com/MidnightCommander/mc/commit/1b99570>) [0b71156](<https://github.com/MidnightCommander/mc/commit/0b71156>) [ce401d7](<https://github.com/MidnightCommander/mc/commit/ce401d7>) |  [[64]](<https://www.midnight-commander.org/ticket/1851>) |   
[Mercurial](</wzh/index.php?title=Mercurial&action=edit&redlink=1> "Mercurial（页面不存在）")（英语：[Mercurial](<https://wiki.archlinux.org/title/Mercurial> "en:Mercurial")） |  `~/.hgrc` |  [3540200](<https://www.mercurial-scm.org/repo/hg/rev/3540200>) [4.2](<https://www.mercurial-scm.org/wiki/Release4.2>) |  |  `XDG_CONFIG_HOME/hg/hgrc`.   
[mesa](<https://archlinux.org/packages/?name=mesa>)包 |  |  [87ab26b](<https://gitlab.freedesktop.org/mesa/mesa/-/commit/87ab26b>) |  |  `XDG_CACHE_HOME/mesa`  
[milkytracker](<https://archlinux.org/packages/?name=milkytracker>)包 |  `~/.milkytracker_config` |  [eb487c5](<https://github.com/Deltafire/MilkyTracker/commit/eb487c5>) |  [[65]](<https://github.com/Deltafire/MilkyTracker/issues/12>) |   
[mlterm](<../zh-cn/Mlterm.html> "Mlterm") |  `~/.mlterm/` |  [71df071](<https://github.com/arakiken/mlterm/commit/71df0714edc7715524092213516790a24178615b>) |  [[66]](<https://github.com/arakiken/mlterm/issues/42>) |  `XDG_CONFIG_HOME/mlterm/`  
[mozc](</wzh/index.php?title=Mozc&action=edit&redlink=1> "Mozc（页面不存在）")（英语：[mozc](<https://wiki.archlinux.org/title/mozc> "en:mozc")） |  `~/.mozc` |  [91cc1e1](<https://github.com/google/mozc/commit/91cc1e19ef34aeb12888b697fefa52907f1a834d>) |  [[67]](<https://github.com/google/mozc/issues/474>) |   
[mpd](<../zh-cn/MPD.html> "Mpd") |  `~/.mpdconf` |  [87b7328](<https://github.com/MusicPlayerDaemon/MPD/commit/87b7328>) |  |   
[mpv](<../zh-cn/Mpv.html> "Mpv") |  `~/.mpv` |  [cb250d4](<https://github.com/mpv-player/mpv/commit/cb250d4>) |  [[68]](<https://github.com/mpv-player/mpv/pull/864>) |   
[msmtp](</wzh/index.php?title=Msmtp&action=edit&redlink=1> "Msmtp（页面不存在）")（英语：[msmtp](<https://wiki.archlinux.org/title/msmtp> "en:msmtp")） |  `~/.msmtprc` |  [af2f409](<https://github.com/marlam/msmtp-mirror/commit/af2f409>) v1.6.7+  |  |  ` XDG_CONFIG_HOME/msmtp/config`。   
[mutt](<../zh-cn/Mutt.html> "Mutt") |  `~/.mutt` |  [b17cd67](<https://gitlab.com/muttmua/mutt/commit/b17cd67>) |  [[69]](<https://gitlab.com/muttmua/trac-tickets/raw/master/tickets/closed/3207-Conform_to_XDG_Base_Directory_Specification.txt>) |   
[mypaint](<https://archlinux.org/packages/?name=mypaint>)包 |  `~/.mypaint` |  [cf723b7](<https://github.com/mypaint/mypaint/commit/cf723b7>) |  |   
[nano](<../zh-cn/Nano.html> "Nano") |  `~/.nano/` `~/.nanorc` |  [c16e79b](<https://git.savannah.gnu.org/cgit/nano.git/commit/?id=c16e79b>) |  [[70]](<https://savannah.gnu.org/patch/?8523>) |   
[ncmpcpp](<../zh-cn/Ncmpcpp.html> "Ncmpcpp") |  `~/.ncmpcpp` |  [38d9f81](<https://github.com/arybczak/ncmpcpp/commit/38d9f81>) [27cd86e](<https://github.com/arybczak/ncmpcpp/commit/27cd86e>) |  [[71]](<https://github.com/arybczak/ncmpcpp/issues/79>) [[72]](<https://github.com/arybczak/ncmpcpp/issues/110>) | 应设置 `ncmpcpp_directory` 以避免 `~/.ncmpcpp` 中出现 `error.log` 文件。   
[Neovim](<../zh-cn/Neovim.html> "Neovim") |  `~/.nvim` `~/.nvimlog` `~/.nviminfo` |  [1ca5646bb](<https://github.com/neovim/neovim/commit/1ca5646bb>) |  [[73]](<https://github.com/neovim/neovim/issues/78>) [[74]](<https://github.com/neovim/neovim/pull/3198>) |   
[Nestopia UE](<http://0ldsk00l.ca/nestopia/>) |  `~/.nestopia/` |  [610c008](<https://github.com/0ldsk00l/nestopia/commit/d78381198a26a10333128e9bf28bc530a610c008>) [1.51.0](<https://github.com/0ldsk00l/nestopia/releases/tag/1.51.0>) |  [[75]](<https://github.com/0ldsk00l/nestopia/issues/343>) |   
[newsboat](</wzh/index.php?title=Newsboat&action=edit&redlink=1> "Newsboat（页面不存在）")（英语：[newsboat](<https://wiki.archlinux.org/title/newsboat> "en:newsboat")） |  `~/.newsboat` |  [3c57824](<https://github.com/akrennmair/newsbeuter/commit/3c57824>) |  [[76]](<https://github.com/akrennmair/newsbeuter/pull/39>) | 必须手动创建两个目录[[77]](<https://man.archlinux.org/man/newsboat.1#FILES>)： `mkdir -p "$XDG_DATA_HOME"/newsboat "$XDG_CONFIG_HOME"/newsboat`  
[node-gyp](<https://github.com/nodejs/node-gyp>) |  `~/.node-gyp` |  [2b5ce52a](<https://github.com/nodejs/node-gyp/commit/2b5ce52a>) |  [[78]](<https://github.com/nodejs/node-gyp/pull/1570>) |   
[np2kai-git](<https://aur.archlinux.org/packages/np2kai-git/>)AUR |  `~/.config/np2kai` `~/.config/xnp2kai` |  [56a1cc2](<https://github.com/AZO234/NP2kai/commit/56a1cc2>) |  [[79]](<https://github.com/AZO234/NP2kai/pull/50>) |   
[notmuch](<../zh-cn/Notmuch.html> "Notmuch") |  `~/.notmuch-config` |  |  [[80]](<https://notmuchmail.org/pipermail/notmuch/2011/007007.html>) |  `mkdir -p $XDG_CONFIG_HOME/notmuch/default; mv ~/.notmuch-config $XDG_CONFIG_HOME/notmuch/default/config`  
[NSS](<https://developer.mozilla.org/en-US/docs/Mozilla/Projects/NSS>) |  `~/.pki` |  [3.42 (da45424)](<https://hg.mozilla.org/projects/nss/rev/da45424cb9a0b4d8e45e5040e2e3b574d994e254>) |  [[81]](<https://bugzilla.mozilla.org/show_bug.cgi?id=818686>) | 参阅 Chromium 了解现有问题。   
[nteract-bin](<https://aur.archlinux.org/packages/nteract-bin/>)AUR |  |  [4593e72](<https://github.com/nteract/nteract/commit/4593e72>) |  [[82]](<https://github.com/nteract/nteract/issues/180>) [[83]](<https://github.com/nteract/nteract/pull/3870>) |  [无法识别 ipython/jupyter 的绕过方法](<https://github.com/nteract/nteract/issues/4517>)  
[ocaml-utop](<https://aur.archlinux.org/packages/ocaml-utop/>)AUR |  `~/.utop-history` `~/.utoprc` |  [2.13.0](<https://github.com/ocaml-community/utop/releases/tag/2.13.0>) [9729963](<https://github.com/ocaml-community/utop/commit/9729963>) |  [[84]](<https://github.com/ocaml-community/utop/pull/431>) |  `XDG_STATE_HOME/utop/utop-history` `XDG_CONFIG_HOME/utop/utoprc`  
[OfflineIMAP](</wzh/index.php?title=OfflineIMAP&action=edit&redlink=1> "OfflineIMAP（页面不存在）")（英语：[OfflineIMAP](<https://wiki.archlinux.org/title/OfflineIMAP> "en:OfflineIMAP")） |  `~/.offlineimaprc` |  [5150de5](<https://github.com/OfflineIMAP/offlineimap/commit/5150de5>) |  [[85]](<https://github.com/OfflineIMAP/offlineimap/issues/32>) |  `XDG_CONFIG_HOME/offlineimap/config`  
[openal](<https://archlinux.org/packages/?name=openal>)包 |  `~/.alsoftrc` |  [3c90ed9](<https://github.com/kcat/openal-soft/commit/3c90ed95afa1feed70e6c5655cfeec096c00c23b>) |  |  `XDG_CONFIG_HOME/alsoft.conf`  
[opentyrian](<https://aur.archlinux.org/packages/opentyrian/>)AUR |  `~/.opentyrian` |  [39559c3](<https://github.com/opentyrian/opentyrian/commit/39559c3>) |  [[86]](<https://web.archive.org/web/20140815181350/http://code.google.com/p/opentyrian/issues/detail?id=125>) |   
[osc](<https://aur.archlinux.org/packages/osc/>)AUR |  `~/.oscrc` `~/.osc_cookiejar` |  [6bc2d3f](<https://github.com/openSUSE/osc/commit/6bc2d3f939c2518ae555fbf75e3a11cc16fc5302>) [ebcf3de](<https://github.com/openSUSE/osc/commit/ebcf3de6abe1ae142baa5bee4c9867cc1968bad1>) |  [github.com/openSUSE/osc/pull/940](<https://github.com/openSUSE/osc/pull/940>) [github.com/osc/pull/940](<https://github.com/openSUSE/osc/pull/940>) |  `XDG_CONFIG_HOME/osc/oscrc` `XDG_STATE_HOME/osc/cookiejar` 如果旧路径存在，优先使用。   
[pam-u2f](<https://archlinux.org/packages/?name=pam-u2f>)包 |  `~/.config/Yubico/u2f_keys` |  [ad52dd8](<https://github.com/Yubico/pam-u2f/commit/ad52dd82dead525dab94ded1916dcf6334459106>) |  [[87]](<https://github.com/Yubico/pam-u2f/issues/9>) |  `XDG_CONFIG_HOME/Yubico/u2f_keys`  
[pandoc-cli](<https://archlinux.org/packages/?name=pandoc-cli>)包 |  `~/.pandoc/` |  [0bed0ab](<https://github.com/jgm/pandoc/commit/0bed0ab5a308f5e72a01fa9bee76488556288862>) |  [[88]](<https://github.com/jgm/pandoc/issues/3582>) |   
[PCManFM](<../zh-cn/PCManFM.html> "PCManFM") |  `~/.thumbnails` |  [1.3.2](<https://github.com/lxde/libfm/issues/57>) |  |   
[pcsx2](<https://aur.archlinux.org/packages/pcsx2/>)AUR |  `~/.pcsx2` |  [87f1e8f](<https://github.com/PCSX2/pcsx2/commit/87f1e8f>) [a9020c6](<https://github.com/PCSX2/pcsx2/commit/a9020c6>) [3b22f0f](<https://github.com/PCSX2/pcsx2/commit/3b22f0f>) [0a012ae](<https://github.com/PCSX2/pcsx2/commit/0a012ae>) |  [[89]](<https://github.com/PCSX2/pcsx2/issues/352>) [[90]](<https://github.com/PCSX2/pcsx2/issues/381>) |   
[pdfsam](<https://aur.archlinux.org/packages/pdfsam/>)AUR |  `~/.openjfx` |  |  |  `export _JAVA_OPTIONS=-Djavafx.cachedir="$XDG_CACHE_HOME"/openjfx`  
[Pry](<https://pry.github.io/>) |  `~/.pryrc` `~/.pry_history` |  [a0be0cc7](<https://github.com/pry/pry/commit/a0be0cc7b2070edff61c0c7f10fa37fce9b730bd>) [15e1fc92](<https://github.com/pry/pry/commit/15e1fc929ed84c161abc5afc9be73488a41df397>) [e9d1be0e](<https://github.com/pry/pry/commit/e9d1be0e17b294318dbb2f70f74a50486cfa044c>) |  [[91]](<https://github.com/pry/pry/issues/1316>)  
[python-autoimport](<https://aur.archlinux.org/packages/python-autoimport/>)AUR |  `~/.config/autoimport/config.toml` |  [1.2.0](<https://github.com/lyz-code/autoimport/pull/206>) |  [[92]](<https://github.com/lyz-code/autoimport/pull/172>) |  `XDG_CONFIG_HOME/autoimport/config.toml`  
[python-black](<https://archlinux.org/packages/?name=python-black>)包 |  `~/.config/black` |  [21.4b0](<https://github.com/psf/black/pull/1899>) |  [[93]](<https://github.com/psf/black/issues/1577>) |  `XDG_CONFIG_HOME/black`，`XDG_CACHE_HOME/black/<version>/`  
[python-pylint](<https://archlinux.org/packages/?name=python-pylint>)包 |  `~/.pylint.d` |  [2.10](<https://github.com/PyCQA/pylint/pull/4661>) |  [[94]](<https://github.com/PyCQA/pylint/issues/1364>) | 以前需要使用 `export PYLINTHOME="$XDG_CACHE_HOME"/pylint`，全局配置仍然需要：`export PYLINTRC="$XDG_CONFIG_HOME"/pylint/pylintrc`  
[python-pip](<https://archlinux.org/packages/?name=python-pip>)包 |  `~/.pip` |  [6.0](<https://github.com/pypa/pip/blob/548a9136525815dff41acd845c558a0b36eb1c5f/NEWS.rst#60-2014-12-22>) |  [[95]](<https://github.com/pypa/pip/issues/1733>) |   
[python-pipx](<https://archlinux.org/packages/?name=python-pipx>)包 |  `~/.local/pipx` |  [c3d8de9](<https://github.com/pypa/pipx/pull/1001>) |  [[96]](<https://github.com/pypa/pipx/issues/722>) | 为了兼容，pipx 将恢复为 `~/.local/pipx`（如果存在）。使用 [python-platformdirs](<https://archlinux.org/packages/?name=python-platformdirs>)包 实现。   
[python-poetry](<https://archlinux.org/packages/?name=python-poetry>)包 |  `~/.poetry` |  [[97]](<https://github.com/python-poetry/poetry/pull/3706>) |  [[98]](<https://github.com/python-poetry/poetry/issues/2148>) |   
[powershell](<https://aur.archlinux.org/packages/powershell/>)AUR |  |  [6.0](<https://docs.microsoft.com/en-us/powershell/scripting/whats-new/what-s-new-in-powershell-core-60#filesystem>) |  |   
[ppsspp](<https://archlinux.org/packages/?name=ppsspp>)包 |  `~/.ppsspp` |  [132fe47](<https://github.com/hrydgard/ppsspp/commit/132fe47>) |  [[99]](<https://github.com/hrydgard/ppsspp/issues/4623>) |   
[procps-ng](<https://archlinux.org/packages/?name=procps-ng>)包 |  `~/.toprc` |  [af53e17](<https://gitlab.com/procps-ng/procps/commit/af53e17>) |  [[100]](<https://gitlab.com/procps-ng/procps/merge_requests/38>) [[101]](<https://bugzilla.redhat.com/show_bug.cgi?id=1155265>) |   
[pacman](<../zh-cn/Pacman.html> "Pacman") |  `~/.makepkg.conf` |  [80eca94](<https://gitlab.archlinux.org/pacman/pacman/commit/80eca94>) |  [[102]](<https://lists.archlinux.org/archives/list/pacman-dev@lists.archlinux.org/thread/KTD2FW7YKY724UB7PT3GGP5L7TNWZYEP/>) |   
[panda3d](<https://aur.archlinux.org/packages/panda3d/>)AUR |  `~/.panda3d` |  [2b537d2](<https://github.com/panda3d/panda3d/commit/2b537d2>) |  |   
[pnpm](<https://archlinux.org/packages/?name=pnpm>)包 |  `~/.pnpm-store` |  [[103]](<https://github.com/pnpm/pnpm/pull/3873>) [[104]](<https://github.com/pnpm/pnpm/pull/4522>) |  [[105]](<https://github.com/pnpm/pnpm/issues/2574>) |   
[poezio](<https://aur.archlinux.org/packages/poezio/>)AUR |  |  |  |   
[PulseAudio](<../zh-cn/PulseAudio.html> "PulseAudio") |  `~/.pulse` `~/.pulse-cookie` |  [59a8618](<https://gitlab.freedesktop.org/pulseaudio/pulseaudio/-/commit/59a8618>) [87ae830](<https://gitlab.freedesktop.org/pulseaudio/pulseaudio/-/commit/87ae830>) [9ab510a](<https://gitlab.freedesktop.org/pulseaudio/pulseaudio/-/commit/9ab510a>) [4c195bc](<https://gitlab.freedesktop.org/pulseaudio/pulseaudio/-/commit/4c195bc>) |  [[106]](<https://bugzilla.redhat.com/show_bug.cgi?id=845607>) |  [Steam](<../zh-cn/Steam.html> "Steam") 可能仍会创建 `~/.pulse-cookie`。将 `cookie-file = ~/.config/pulse/cookie` 添加到 `/etc/pulse/client.conf` 即可将其删除。   
[pyroom](<https://aur.archlinux.org/packages/pyroom/>)AUR |  |  |  |   
[quodlibet](<https://archlinux.org/packages/?name=quodlibet>)包 |  `~/.quodlibet` | 3.10.0  |  [[107]](<https://github.com/quodlibet/quodlibet/issues/138>) |   
[qutebrowser](</wzh/index.php?title=Qutebrowser&action=edit&redlink=1> "Qutebrowser（页面不存在）")（英语：[qutebrowser](<https://wiki.archlinux.org/title/qutebrowser> "en:qutebrowser")） |  |  |  |   
[qtile](<../zh-cn/Qtile.html> "Qtile") |  |  [fd8686e](<https://github.com/qtile/qtile/commit/fd8686e>) [66d704b](<https://github.com/qtile/qtile/commit/66d704b>) [51cff01](<https://github.com/qtile/qtile/commit/51cff01>) |  [[108]](<https://github.com/qtile/qtile/pull/835>) | 一些可选的栏小部件可以在不兼容的路径中创建文件和目录，但大多数情况下这些仍然是可配置的。   
[rclone](<https://archlinux.org/packages/?name=rclone>)包 |  `~/.rclone.conf` |  [9d36258](<https://github.com/ncw/rclone/commit/9d36258>) |  [[109]](<https://github.com/ncw/rclone/issues/868>) |   
[retroarch](<https://archlinux.org/packages/?name=retroarch>)包 |  |  |  |   
[ripgrep-all](<https://archlinux.org/packages/?name=ripgrep-all>)包 |  `~/.cache/rga` |  [963524b](<https://github.com/phiresky/ripgrep-all/commit/963524bbf5ec861cc1d9d2b57e119eb60125751a>) [v0.10.3](<https://github.com/phiresky/ripgrep-all/releases/tag/v0.10.3>) |  [[110]](<https://github.com/phiresky/ripgrep-all/issues/87>) [[111]](<https://github.com/phiresky/ripgrep-all/issues/102>) [[112]](<https://github.com/phiresky/ripgrep-all/issues/129>) |   
[rr](<https://aur.archlinux.org/packages/rr/>)AUR |  `~/.rr` |  [02e7d41](<https://github.com/mozilla/rr/commit/02e7d41>) |  [[113]](<https://github.com/mozilla/rr/issues/1455>) |   
[RSpec](<https://rspec.info>) |  `~/.rspec` |  [5e395e2](<https://github.com/rspec/rspec-core/commit/5e395e2016f1da19475e6db2817eb26dae828c4c>) |  [[114]](<https://github.com/rspec/rspec-core/issues/1773>) |   
[rTorrent](<../zh-cn/RTorrent.html> "RTorrent") |  `~/.rtorrent.rc` |  [6a8d332](<https://github.com/rakshasa/rtorrent/commit/6a8d332>) |  |   
[RuboCop](<https://www.rubocop.org>) |  `~/.rubocop.yml` |  [6fe5956](<https://github.com/rubocop-hq/rubocop/commit/6fe5956c177ca369cfaa70bdf748b70020a56bf4>) |  [[115]](<https://github.com/rubocop-hq/rubocop/issues/6662>) |   
[Ruby#RubyGems](<../zh-cn/Ruby.html#RubyGems> "Ruby") |  `~/.gem` |  [3.0.0 (5c6269c)](<https://github.com/ruby/ruby/commit/5c6269c>) |  [[116]](<https://github.com/ruby/ruby/pull/2174>) | 
    
    XDG_CONFIG_HOME/gem/gemrc
    XDG_CONFIG_HOME/irb
    XDG_DATA_HOME/gem
    XDG_DATA_HOME/rdoc
      
[sandboxd](<https://github.com/benvan/sandboxd>) |  `~/.sandboxrc` |  [[117]](<https://github.com/benvan/sandboxd/pull/14>) |  [[118]](<https://github.com/benvan/sandboxd/issues/11>) |  `XDG_CONFIG_HOME/sandboxd/sandboxrc`  
[scribus](<https://archlinux.org/packages/?name=scribus>)包 |  `~/.scribus` |  [1.5.3](<https://wiki.scribus.net/canvas/Versione_1.5.3>) |   
[scummvm](<https://archlinux.org/packages/?name=scummvm>)包 |  `~/.scummvmrc` `~/.scummvm/` |  [7d014be](<https://github.com/scummvm/scummvm/commit/7d014be0a2b796175a7ce40a9315603f711b2a30>) |  [[119]](<https://github.com/scummvm/scummvm/pull/656>) | 需要手动迁移数据。 `mkdir "$XDG_CONFIG_HOME"/scummvm/ "$XDG_DATA_HOME"/scummvm` `mv ~/.scummvmrc "$XDG_CONFIG_HOME"/scummvm/scummvm.ini` `mv ~/.scummvm "$XDG_DATA_HOME"/scummvm/saves`  
[sdcv](<https://archlinux.org/packages/?name=sdcv>)包 |  `~/.stardict/` `~/.sdcv_history` |  [958ec35](<https://github.com/Dushistov/sdcv/commit/958ec35>) |  [[120]](<https://github.com/Dushistov/sdcv/issues/51>) |   
[shellcheck](<https://archlinux.org/packages/?name=shellcheck>)包 |  `~/.shellcheckrc` |  [581bcc3](<https://github.com/koalaman/shellcheck/commit/581bcc3907ab98e919a7dd60566810a928c46b95>) |  |  `XDG_CONFIG_HOME/shellcheckrc` 有关更多信息，请参阅[Shellcheck RC 文件](<https://github.com/koalaman/shellcheck/blob/master/shellcheck.1.md#rc-files>)。   
[snes9x](<https://archlinux.org/packages/?name=snes9x>)包 |  `~/.snes9x` |  [93b5f11](<https://github.com/snes9xgit/snes9x/commit/93b5f11>) |  [[121]](<https://github.com/snes9xgit/snes9x/issues/194>) | 默认情况下，配置文件留空，以便用户可以随意填写（通过 GUI 或手动）。   
[spectrwm](</wzh/index.php?title=Spectrwm&action=edit&redlink=1> "Spectrwm（页面不存在）")（英语：[spectrwm](<https://wiki.archlinux.org/title/spectrwm> "en:spectrwm")） |  `~/.spectrwm` |  [a30bbb](<https://github.com/conformal/spectrwm/commit/a30bbb>) |  [[122]](<https://github.com/conformal/spectrwm/pull/153>) |   
[SQLite](<../zh-cn/SQLite.html> "SQLite") |  `~/.sqliterc`，`~/.sqlite_history` |  [3.44.0](<https://github.com/sqlite/sqlite/commit/6e8a33>) |  |  `XDG_CONFIG_HOME/sqlite3/sqliterc`，`export SQLITE_HISTORY=$XDG_DATA_HOME/sqlite_history`  
[Streamlink](<../zh-cn/Streamlink.html> "Streamlink") |  `~/.livestreamerrc` |  [ea80591](<https://github.com/chrippa/livestreamer/commit/ea80591>) |  [[123]](<https://github.com/chrippa/livestreamer/pull/106>) |   
[sublime-text-dev](<https://aur.archlinux.org/packages/sublime-text-dev/>)AUR |  |  [build 4105](<https://www.sublimetext.com/dev>) |  | 在版本 4105 之前，缓存被放置在 `XDG_CONFIG_HOME/sublime-text-3/Cache` 中。   
[surfraw](<../zh-cn/Surfraw.html> "Surfraw") |  `~/.surfraw.conf` `~/.surfraw.bookmarks` |  [3e4591d](<https://gitlab.com/surfraw/Surfraw/commit/3e4591d>) [bd8c427](<https://gitlab.com/surfraw/Surfraw/commit/bd8c427>) [f57fc71](<https://gitlab.com/surfraw/Surfraw/commit/f57fc71>) |  |   
[sway](<../zh-cn/Sway.html> "Sway") |  `~/.sway/config` |  [614393c](<https://github.com/SirCmpwn/sway/commit/614393c>) |  [[124]](<https://github.com/SirCmpwn/sway/issues/5>) |  `XDG_CONFIG_HOME/sway/config`  
[sxhkd](<../zh-cn/Sxhkd.html> "Sxhkd") |  |  |  |   
[systemd](<../zh-cn/Systemd.html> "Systemd") |  |  |  |   
[teeworlds](<https://archlinux.org/packages/?name=teeworlds>)包 |  `~/.teeworlds` |  [[125]](<https://github.com/teeworlds/teeworlds/commit/d2e39d2f50684151490da446156622e69dd84a48>) |  |   
[termite](</wzh/index.php?title=Termite&action=edit&redlink=1> "Termite（页面不存在）")（英语：[termite](<https://wiki.archlinux.org/title/termite> "en:termite")） |  |  |  |   
[tig](<https://archlinux.org/packages/?name=tig>)包 |  `~/.tigrc`，`~/.tig_history` |  [2.2](<https://github.com/jonas/tig/blob/master/NEWS.adoc#tig-22>) |  [[126]](<https://github.com/jonas/tig/issues/513>) |  `~/.local/share/tig`目录必须存在否则将会写入`~/.tig_history`。   
Theming（桌面端）  |  `~/.icons/`，`~/.themes/` |  [[127]](<https://specifications.freedesktop.org/icon-theme-spec/latest/ar01s03.html>) |  |  `XDG_DATA_HOME/icons` `XDG_DATA_HOME/themes` 为了使 Qt 程序、GTK 或 Wayland 上的 Qt 程序使用 `XDG_DATA_HOME/icons` 中的光标，需要配置 [XCURSOR_PATH](<../zh-cn/%E5%85%89%E6%A0%87%E4%B8%BB%E9%A2%98.html#%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F> "光标主题") 环境变量。   
[tmux](<../zh-cn/Tmux.html> "Tmux") |  `~/.tmux.conf` |  [3.1](<https://raw.githubusercontent.com/tmux/tmux/3.1/CHANGES>) |  [[128]](<https://github.com/tmux/tmux/issues/142>) | 3.1 引入了 `~/.config/tmux/tmux.conf` 并在 [3.2](<https://github.com/tmux/tmux/blob/a5f99e14c6f264e568b860692b89d11f5298a3f2/CHANGES#L145>) 添加了 `XDG_CONFIG_HOME/tmux/tmux.conf`  
[tmuxp](</wzh/index.php?title=Tmuxp&action=edit&redlink=1> "Tmuxp（页面不存在）")（英语：[tmuxp](<https://wiki.archlinux.org/title/tmuxp> "en:tmuxp")） |  `~/.tmuxp` |  [1.5.0](<https://tmuxp.git-pull.com/history.html#tmuxp-1-5-0-2018-10-02>) |  [[129]](<https://github.com/tmux-python/tmuxp/pull/404>) |  [1.5.2](<https://tmuxp.git-pull.com/history.html#tmuxp-1-5-2-2019-06-02>)中修复。   
[tmuxinator](<https://aur.archlinux.org/packages/tmuxinator/>)AUR |  `~/.tmuxinator` |  [2636923](<https://github.com/tmuxinator/tmuxinator/pull/511/commits/2636923>) |  [[130]](<https://github.com/tmuxinator/tmuxinator/pull/511>) |   
[Transmission](<../zh-cn/Transmission.html> "Transmission") |  `~/.transmission` |  [b71a298](<https://github.com/transmission/transmission/commit/b71a298>) |  |   
[util-linux](<https://archlinux.org/packages/?name=util-linux>)包 |  |  [570b321](<https://git.kernel.org/pub/scm/utils/util-linux/util-linux.git/commit/?id=570b321>) |  |   
[yapf](<https://archlinux.org/packages/?name=yapf>)包 |  |  [a0b51d2](<https://github.com/google/yapf/pull/1067/commits/a0b51d2>) |  [[131]](<https://github.com/google/yapf/pull/1067>) |  `$XDG_CONFIG_HOME/yapf/style`  
[Uzbl](</wzh/index.php?title=Uzbl&action=edit&redlink=1> "Uzbl（页面不存在）")（英语：[Uzbl](<https://wiki.archlinux.org/title/Uzbl> "en:Uzbl")） |  |  [c6fd63a](<https://github.com/uzbl/uzbl/commit/c6fd63a>) |  [[132]](<https://github.com/uzbl/uzbl/pull/150>) |   
[vim](<../zh-cn/Vim.html> "Vim") |  `~/.vim`，`~/.vimrc`，`~/.viminfo` |  [c9df1fb](<https://github.com/vim/vim/commit/c9df1fb>) |  [[133]](<https://github.com/vim/vim/pull/14182>) |   
[vimb](<https://archlinux.org/packages/?name=vimb>)包 |  |  |  |   
[VirtualBox](<../zh-cn/VirtualBox.html> "VirtualBox") |  `~/.VirtualBox` |  [4.3](<https://www.virtualbox.org/ticket/5099?action=diff&version=7>) |  [[134]](<https://www.virtualbox.org/ticket/5099>) |   
[vis](<https://archlinux.org/packages/?name=vis>)包 |  `~/.vis` |  [68a25c7](<https://github.com/martanne/vis/commit/68a25c7>) [d138908](<https://github.com/martanne/vis/commit/d138908>) |  [[135]](<https://github.com/martanne/vis/pull/303>) |   
[VLC](<../zh-cn/VLC_%E5%AA%92%E4%BD%93%E6%92%AD%E6%94%BE%E5%99%A8.html> "VLC") |  `~/.vlcrc` |  [16f32e1](<https://code.videolan.org/videolan/vlc/-/commit/16f32e1500887c0dcd33cb06ad71759a81a52878>) |  [[136]](<https://trac.videolan.org/vlc/ticket/1267>) |   
[warsow](<https://archlinux.org/packages/?name=warsow>)包 |  `~/.warsow-2.x` |  [98ece3f](<https://github.com/Qfusion/qfusion/commit/98ece3f>) |  [[137]](<https://github.com/Qfusion/qfusion/issues/298>) |   
[WeeChat](</wzh/index.php?title=WeeChat&action=edit&redlink=1> "WeeChat（页面不存在）")（英语：[WeeChat](<https://wiki.archlinux.org/title/WeeChat> "en:WeeChat")） |  `~/.weechat` |  [[138]](<https://github.com/weechat/weechat/commit/70cdf21681d75090c3df9858c9e7ce5a85433856>) [3.2](<https://github.com/weechat/weechat/releases/tag/v3.2>) |  [[139]](<https://github.com/weechat/weechat/issues/1285>) [[140]](<https://specs.weechat.org/specs/001285-follow-xdg-base-dir-spec.html>)[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2023-05-06 ⓘ] | 
    
    XDG_CONFIG_HOME/weechat
    XDG_CACHE_HOME/weechat
    XDG_DATA_HOME/weechat
      
[Wireshark](<../zh-cn/Wireshark.html> "Wireshark") |  `~/.wireshark` |  [b0b53fa](<https://code.wireshark.org/review/gitweb?p=wireshark.git;a=commit;h=b0b53fa>)[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2022-09-23 ⓘ] |  |   
[wxWidgets](<https://wxwidgets.org/>) |  |  [[141]](<https://trac.wxwidgets.org/ticket/17727>) |  |   
[XKB](<https://www.x.org/wiki/XKB/>) |  `~/.xkb` |  |  |   
[Xsettingsd](<../zh-cn/Xsettingsd.html> "Xsettingsd") |  `~/.xsettingsd` |  [b4999f5](<https://github.com/derat/xsettingsd/commit/b4999f5>) |  |   
[xmobar](</wzh/index.php?title=Xmobar&action=edit&redlink=1> "Xmobar（页面不存在）")（英语：[xmobar](<https://wiki.archlinux.org/title/xmobar> "en:xmobar")） |  `~/.xmobarrc` |  [7b0d6bf](<https://github.com/jaor/xmobar/commit/7b0d6bf>)[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2024-07-30 ⓘ] [9fc6b37](<https://github.com/jaor/xmobar/commit/9fc6b37>)[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2024-07-30 ⓘ] [eaccf70](<https://github.com/jaor/xmobar/commit/eaccf70>)[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2024-07-30 ⓘ] |  [[142]](<https://github.com/jaor/xmobar/pull/99>)[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2024-07-30 ⓘ] [[143]](<https://github.com/jaor/xmobar/pull/131>)[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2024-07-30 ⓘ] |  `XDG_CONFIG_HOME/xmobar/xmobarrc`  
[xmonad](<../zh-cn/Xmonad.html> "Xmonad") |  `~/.xmonad/` |  [40fc10b](<https://github.com/xmonad/xmonad/commit/40fc10b>) |  [[144]](<https://github.com/xmonad/xmonad/issues/61>) [[145]](<https://code.google.com/p/xmonad/issues/detail?id=484>) | 所有这些都必须存在，否则它会放弃并回退到 `~/.xmonad/`： 
    
    XDG_CACHE_HOME/xmonad
    XDG_CONFIG_HOME/xmonad
    XDG_DATA_HOME/xmonad
    
或者，它始终尊重 `XMONAD_CACHE_DIR`、`XMONAD_CONFIG_DIR` 和 `XMONAD_DATA_DIR`。   
[xonsh](<https://archlinux.org/packages/?name=xonsh>)包 |  `~/.xonshrc` |  |  [[146]](<https://xon.sh/xonshrc.html>) |  `$XDG_CONFIG_HOME/xonsh/rc.xsh`  
[xournalpp](<https://archlinux.org/packages/?name=xournalpp>)包 |  `~/.xournalpp` |  [20db937f](<https://github.com/xournalpp/xournalpp/commit/20db937f>) [1.1.0](<https://github.com/xournalpp/xournalpp/releases/tag/1.1.0>) |  [[147]](<https://github.com/xournalpp/xournalpp/issues/1101>) [[148]](<https://github.com/xournalpp/xournalpp/pull/1384>)  
[xsel](<https://archlinux.org/packages/?name=xsel>)包 |  `~/.xsel.log` |  [ee7b481](<https://github.com/kfish/xsel/commit/ee7b481>) |  [[149]](<https://github.com/kfish/xsel/issues/10>) |   
[Zim](<../zh-cn/Zim.html> "Zim") |  |  [e42b8b0](<https://github.com/zim-desktop-wiki/zim-desktop-wiki/commit/e42b8b0>) |  | 
    
     $XDG_CONFIG_HOME/zim/preferences.conf
     $XDG_CONFIG_HOME/zim/notebooks.list
      
[zoxide](<https://archlinux.org/packages/?name=zoxide>)包 |  `~/.zo` |  [0.3.0](<https://github.com/ajeetdsouza/zoxide/releases/tag/v0.3.0>) |  [[150]](<https://github.com/ajeetdsouza/zoxide/pull/47>) |   
  
###  部分支持

应用程序  | 旧路径  | 采用规范自  | 讨论  | 注释   
---|---|---|---|---  
[abook](<https://aur.archlinux.org/packages/abook/>)AUR |  `~/.abook` |  |  |  `abook --config "$XDG_CONFIG_HOME"/abook/abookrc --datafile "$XDG_DATA_HOME"/abook/addressbook`  
[ack](<https://archlinux.org/packages/?name=ack>)包 |  `~/.ackrc` |  |  [[151]](<https://github.com/beyondgrep/ack2/issues/516>) |  `export ACKRC="$XDG_CONFIG_HOME/ack/ackrc"`  
[Ansible](</wzh/index.php?title=Ansible&action=edit&redlink=1> "Ansible（页面不存在）")（英语：[Ansible](<https://wiki.archlinux.org/title/Ansible> "en:Ansible")） |  `~/.ansible` |  [2.14](<https://github.com/ansible/ansible/pull/76114>) |  [[152]](<https://github.com/ansible/ansible/issues/52354>) [[153]](<https://github.com/ansible/ansible/issues/68587>) [[154]](<https://github.com/ansible/ansible/issues/75788>) | 
    
    export ANSIBLE_HOME="${XDG_CONFIG_HOME}/ansible"
    export ANSIBLE_CONFIG="${XDG_CONFIG_HOME}/ansible.cfg"
    export ANSIBLE_GALAXY_CACHE_DIR="${XDG_CACHE_HOME}/ansible/galaxy_cache"

[[155]](<https://docs.ansible.com/ansible/latest/reference_appendices/config.html>) 可以通过在适当的 `ansible.cfg` 中设置 `remote_tmp = ${XDG_CONFIG_HOME}/ansible/tmp` 来移动远程的 `~/.ansible/tmp`。[[156]](<https://docs.ansible.com/archive/ansible/2.4/intro_configuration.html#remote-tmp>) [[157]](<https://github.com/ayekat/localdir/issues/7#issuecomment-998286490>)  
[asdf-vm](<https://aur.archlinux.org/packages/asdf-vm/>)AUR |  `~/.asdfrc`，`~/.asdf/` |  |  [[158]](<https://github.com/asdf-vm/asdf/issues/687>) |  `export ASDF_CONFIG_FILE="${XDG_CONFIG_HOME}/asdf/asdfrc"`，`export ASDF_DATA_DIR="${XDG_DATA_HOME}/asdf"`  
[aspell](<../zh-cn/%E8%AF%AD%E8%A8%80%E6%A3%80%E6%9F%A5.html> "Aspell") |  `~/.aspell.conf` |  |  [[159]](<https://github.com/GNUAspell/aspell/issues/560>) | 非常不完整。以下内容重新定位了 `en` 词典，但为了简洁起见，这里没有指定其他可能的词典。`export ASPELL_CONF="per-conf $XDG_CONFIG_HOME/aspell/aspell.conf; personal $XDG_DATA_HOME/aspell/en.pws; repl $XDG_DATA_HOME/aspell/en.prepl"`  
[aws-cli](<https://archlinux.org/packages/?name=aws-cli>)包 |  `~/.aws` |  [1.7.45](<https://github.com/aws/aws-cli/commit/fc5961ea2cc0b5976ac9f777e20e4236fd7540f5>) |  [[160]](<https://github.com/aws/aws-cli/issues/2433>) |  `export AWS_SHARED_CREDENTIALS_FILE="$XDG_CONFIG_HOME"/aws/credentials`，`export AWS_CONFIG_FILE="$XDG_CONFIG_HOME"/aws/config`  
[bash-completion](<https://archlinux.org/packages/?name=bash-completion>)包 |  `~/.bash_completion` |  |  |  `export BASH_COMPLETION_USER_FILE="$XDG_CONFIG_HOME"/bash-completion/bash_completion`  
[bashdb](<https://aur.archlinux.org/packages/bashdb/>)AUR |  `~/.bashdbinit`，`~/.bashdb_hist` |  |  | 就像 [[161]](<https://bashdb.sourceforge.net/bashdb.html#Command-Files>) 中所述，您可以指定一个文件来运行命令。因此，将 init 文件移动到 `XDG_CONFIG_HOME/bashdb/bashdbinit` 并创建一个别名 `alias bashdb='bashdb -x ${XDG_CONFIG_HOME:-$HOME/.config}/bashdb/bashdbinit'`。不幸的是，历史文件是硬编码的 [[162]](<https://sourceforge.net/p/bashdb/code/ci/bash-5.1/tree/lib/hist.sh#l28>)。   
[bazaar](<../zh-cn/Bazaar.html> "Bazaar") |  `~/.bazaar`，`~/.bzr.log` |  [2.3.0](<https://bugs.launchpad.net/bzr/+bug/195397/comments/15>) |  [[163]](<https://bugs.launchpad.net/bzr/+bug/195397>) | 上游错误讨论指出，如果存在 `~/.config/bazaar`，bazaar 将使用它。日志文件 `~/.bzr.log` 可能仍会被写入。   
[bogofilter](<https://archlinux.org/packages/?name=bogofilter>)包 |  `~/.bogofilter` |  [0.7.5](<https://gitlab.com/bogofilter/bogofilter/-/blob/main/bogofilter/NEWS.0#L2760>) |  [[164]](<https://sourceforge.net/p/bogofilter/bugs/110/>) |  `export BOGOFILTER_DIR="$XDG_DATA_HOME"/bogofilter`  
[btpd-git](<https://aur.archlinux.org/packages/btpd-git/>)AUR |  `~/.btpd/` |  |  [[165]](<https://github.com/btpd/btpd/issues/55>) |  `btpd -d "$XDG_DATA_HOME"/.btpd` `HOME="$XDG_DATA_HOME" btcli`  
[bun](<https://aur.archlinux.org/packages/bun/>)AUR |  `~/.bun/` |  |  [[166]](<https://github.com/oven-sh/bun/issues/1678>) | 当明确设置了 `$XDG_CONFIG_HOME`、`$XDG_CACHE_HOME` 和/或 `$XDG_DATA_HOME` 时，Bun 将优先使用它们。或者，可以使用 `export BUN_INSTALL="$XDG_DATA_HOME"/bun` 来设置 `bun` 目录的主位置。   
[calc](<https://archlinux.org/packages/?name=calc>)包 |  `~/.calc_history` |  |  | 
    
    export CALCHISTFILE="$XDG_CACHE_HOME"/calc_history
      
[Rust#Cargo](<../zh-cn/Rust.html#Cargo> "Rust") |  `~/.cargo` |  |  [[167]](<https://github.com/rust-lang/cargo/issues/1734>) [[168]](<https://github.com/rust-lang/rfcs/pull/1615>) [[169]](<https://github.com/rust-lang/cargo/pull/5183>) [[170]](<https://github.com/rust-lang/cargo/pull/148>) |  `export CARGO_HOME="$XDG_DATA_HOME"/cargo`  
[cataclysm-dda](<https://archlinux.org/packages/?name=cataclysm-dda>)包 |  `~/.cataclysm-dda` |  [0.D-1](<https://gitlab.archlinux.org/archlinux/packaging/packages/cataclysm-dda/-/commit/0947de440817c9c418cac615275edbf1cc0abdbb>) |  [[171]](<https://github.com/CleverRaven/Cataclysm-DDA/issues/12315>) | 由于需要编译时选项，属于部分支持。   
[cd-bookmark](<https://github.com/mollifier/cd-bookmark>) |  `~/.cdbookmark` |  |  [[172]](<https://github.com/mollifier/cd-bookmark/issues/3>) |  `export CD_BOOKMARK_FILE=$XDG_CONFIG_HOME/cd-bookmark/bookmarks` 或者使用具有原生 XDG 支持的 fork：[[173]](<https://github.com/erikw/cd-bookmark/>)。   
[cgdb](<https://archlinux.org/packages/?name=cgdb>)包 |  `~/.cgdb` | ［位于 master 分支，但尚未发布］  |  [[174]](<https://github.com/cgdb/cgdb/issues/203>) [[175]](<https://github.com/cgdb/cgdb/blob/master/NEWS>) | 设置 `export CGDB_DIR=$XDG_CONFIG_HOME/cgdb` 并将配置文件移动到 `XDG_CONFIG_HOME/cgdb/cgdbrc`。   
[chez-scheme](<https://aur.archlinux.org/packages/chez-scheme/>)AUR |  `~/.chezscheme_history` |  |  |  `petite --eehistory "$XDG_DATA_HOME"/chezscheme/history`  
chktex in [texlive-binextra](<https://archlinux.org/packages/?name=texlive-binextra>)包 |  `~/.chktexrc` |  |  | 将配置文件移动到 `$XDG_CONFIG_HOME/chktex/.chktexrc`（注意前导点）和 `export CHKTEXRC=$XDG_CONFIG_HOME/chktex`。   
[Chromium](<../zh-cn/Chromium.html> "Chromium") |  `~/.chromium`，`~/.pki` |  [23057](<https://src.chromium.org/viewvc/chrome?revision=23057&view=revision>) |  [[176]](<https://groups.google.com/forum/#!topic/chromium-dev/QekVQxF3nho>) [[177]](<https://code.google.com/p/chromium/issues/detail?id=16976>) [[178]](<https://bugs.chromium.org/p/chromium/issues/detail?id=1038587>) | 故意（根据这些来源）破坏 `~/.config`，向其中写入数百兆字节的**缓存** 数据。完全不支持。 Chromium 由于未正确设置 NSS 而创建了 .pki，尽管 NSS 本身现在允许使用 XDG 规范。这导致其下游无法正常工作（Qt WebEngine 尤其影响了许多情况，例如 KMail 等）   
[cinelerra](<https://www.cinelerra-gg.org/>) |  `~/.bcast5` |  |  [[179]](<https://cinelerra-gg.org/download/CinelerraGG_Manual/Environment_Variables_Custo.html>) |  `export CIN_CONFIG="$XDG_CONFIG_HOME"/bcast5`  
[conky](<../zh-cn/Conky.html> "Conky") |  `~/.conkyrc` |  [00481ee](<https://github.com/brndnmtthws/conky/commit/00481ee9a97025e8e2acd7303d080af1948f7980>) |  [[180]](<https://github.com/brndnmtthws/conky/issues/144>) |  `conky --config="$XDG_CONFIG_HOME"/conky/conkyrc`  
[claws-mail](<https://archlinux.org/packages/?name=claws-mail>)包 |  `~/.claws-mail` |  |  [[181]](<https://lists.claws-mail.org/pipermail/users/2013-April/006087.html>) |  `claws-mail --alternate-config-dir "$XDG_DATA_HOME"/claws-mail`  
[coreutils](<../zh-cn/%E6%A0%B8%E5%BF%83%E5%B7%A5%E5%85%B7.html> "Coreutils") |  `~/.dircolors` |  |  |  `eval $(dircolors "$XDG_CONFIG_HOME"/dircolors)`  
[crawl](<http://www.dungeoncrawl.org/>) |  `~/.crawl` |  |  | 结尾的斜杠是必需的： `export CRAWL_DIR="$XDG_DATA_HOME"/crawl/`  
[clusterssh](<https://archlinux.org/packages/?name=clusterssh>)包 |  `~/.clusterssh/` |  |  |  `alias cssh="cssh --config-file '$XDG_CONFIG_HOME/clusterssh/config'"`
    
    $XDG_CONFIG_HOME/clusterssh/config
    
    extra_cluster_file=$HOME/.config/clusterssh/clusters
    extra_tag_file=$HOME/.config/clusterssh/tags

尽管如此，clusterssh 仍然会创建 `~/.clusterssh/`。   
[CUDA](<../zh-cn/GPGPU.html#CUDA> "CUDA") |  `~/.nv` |  |  |  `export CUDA_CACHE_PATH="$XDG_CACHE_HOME"/nv`  
[dict](</wzh/index.php?title=Dict&action=edit&redlink=1> "Dict（页面不存在）")（英语：[dict](<https://wiki.archlinux.org/title/dict> "en:dict")） |  `~/.dictrc` |  |  |  `dict -c "$XDG_CONFIG_HOME"/dict/dictrc`  
[discord](<../zh-cn/Discord.html> "Discord") |  `${XDG_CONFIG_HOME}/discord` |  |  | 自 0.0.27 版起： 文档未记录，但常用： `export DISCORD_USER_DATA_DIR="${XDG_DATA_HOME}"` 来源：`<discord_system_package_root>/resources/app.asar`  
[Docker](<../zh-cn/Docker.html> "Docker") |  `~/.docker` |  |  |  `export DOCKER_CONFIG="$XDG_CONFIG_HOME"/docker`  
[docker-machine](<https://archlinux.org/packages/?name=docker-machine>)包 |  `~/.docker/machine` |  |  |  `export MACHINE_STORAGE_PATH="$XDG_DATA_HOME"/docker-machine`  
[DOSBox](<../zh-cn/DOSBox.html> "DOSBox") |  `~/.dosbox/dosbox-0.74-2.conf` |  |  [[182]](<https://www.vogons.org/viewtopic.php?t=29599>) |  `dosbox -conf "$XDG_CONFIG_HOME"/dosbox/dosbox.conf`  
[dub](<https://archlinux.org/packages/?name=dub>)包 |  `~/.dub` |  [v1.30.0-beta.1](<https://github.com/dlang/dub/pull/2281>) |  | Dub 使用 `~/.dub` 目录进行用户设置和缓存下载的软件包。该目录只能整体移动，方法是使用 `export DUB_HOME="path/to/new/dub"`。   
[Electrum Bitcoin Wallet](<https://electrum.org>) |  `~/.electrum` |  [c121230](<https://github.com/spesmilo/electrum/commit/c121230>) |  |  `export ELECTRUMDIR="$XDG_DATA_HOME/electrum"`  
[ELinks](</wzh/index.php?title=ELinks&action=edit&redlink=1> "ELinks（页面不存在）")（英语：[ELinks](<https://wiki.archlinux.org/title/ELinks> "en:ELinks")） |  `~/.elinks` |  |  |  `export ELINKS_CONFDIR="$XDG_CONFIG_HOME"/elinks`  
[elixir](<https://archlinux.org/packages/?name=elixir>)包 |  `~/.mix`，`~/.hex` |  [afaf889](<https://github.com/elixir-lang/elixir/commit/afaf889>) |  [[183]](<https://github.com/elixir-lang/elixir/pull/10028>) [[184]](<https://github.com/hexpm/hex/pull/841>) | Elixir 并不完全符合 XDG 规范，只有当 `MIX_XDG` 变量设置为特殊值时，它才会使用 XDG，否则它将默认使用旧路径。 `export MIX_XDG="true"`  
[Elm](<https://elm-lang.org/>) |  `~/.elm` |  |  |  `export ELM_HOME="$XDG_CONFIG_HOME"/elm`  
[factorio](<https://aur.archlinux.org/packages/factorio/>)AUR |  `~/.factorio/` |  |  [[185]](<https://forums.factorio.com/viewtopic.php?t=30585>) [[186]](<https://forums.factorio.com/viewtopic.php?f=5&t=8294>) | Factorio 支持使用配置文件手动指定数据路径：[[187]](<https://wiki.factorio.com/Application_directory#Linux>)
    
    __Game_Install_directory/config-path.cfg
    
    use-system-read-write-data-directories=true
    
    __Game_Install_directory/config/config.ini
    
    [path]
    read-data=__PATH__executable__/../../data
    write-data=.local/share/factorio  
  
[fceux](<https://archlinux.org/packages/?name=fceux>)包 |  `~/.fceux/` |  |  [[188]](<https://github.com/TASEmulators/fceux/issues/412>) |  `export FCEUX_HOME="$XDG_CONFIG_HOME"/fceux`。Fceux 将在 `$FCEUX_HOME` 内创建 `.fceux` 目录。   
[FFmpeg](<../zh-cn/FFmpeg.html> "FFmpeg") |  `~/.ffmpeg` |  |  |  `export FFMPEG_DATADIR="$XDG_CONFIG_HOME"/ffmpeg`  
[flutter](<https://aur.archlinux.org/packages/flutter/>)AUR |  `~/.flutter`，`~/.flutter_settings`，`~/.flutter_tool_state`，`~/.pub-cache` |  |  [[189]](<https://github.com/flutter/flutter/issues/59430>) |   
[fzf-git](<https://aur.archlinux.org/packages/fzf-git/>)AUR |  `~/.fzf.bash`，`~/.fzf.zsh` |  |  [[190]](<https://github.com/junegunn/fzf/pull/1282>) | 如果使用 `--xdg` 调用安装脚本，则 shell init 文件将安装到 `XDG_CONFIG_HOME/fzf`，例如 ` /usr/local/opt/fzf/install --xdg`。   
[emscripten](<https://archlinux.org/packages/?name=emscripten>)包 |  `~/.emscripten`，`~/.emscripten_sanity`，`~/.emscripten_ports`，`~/.emscripten_cache__last_clear` |  |  [[191]](<https://github.com/kripken/emscripten/issues/3624>) |  `export EM_CONFIG="$XDG_CONFIG_HOME"/emscripten/config`，`export EM_CACHE="$XDG_CACHE_HOME"/emscripten/cache`，`export EM_PORTS="$XDG_DATA_HOME"/emscripten/cache`，`emcc --em-config "$XDG_CONFIG_HOME"/emscripten/config --em-cache "$XDG_CACHE_HOME"/emscripten/cache`  
[get_iplayer](<https://aur.archlinux.org/packages/get_iplayer/>)AUR |  `~/.get_iplayer` |  |  |  `export GETIPLAYERUSERPREFS="$XDG_DATA_HOME"/get_iplayer`  
[getmail](</wzh/index.php?title=Getmail&action=edit&redlink=1> "Getmail（页面不存在）")（英语：[getmail](<https://wiki.archlinux.org/title/getmail> "en:getmail")） |  `~/.getmail/getmailrc` |  |  |  `getmail --rcfile="$XDG_CONFIG_HOME/getmail/getmailrc" --getmaildir="$XDG_DATA_HOME/getmail"`  
[ghc](<https://archlinux.org/packages/?name=ghc>)包 |  `~/.ghci` |  [[192]](<https://gitlab.haskell.org/ghc/ghc/-/commit/763d28551de32377a1dca8bdde02979e3686f400>) |  [[193]](<https://ghc.haskell.org/trac/ghc/ticket/6077>) | 上游版本从 9.4.1 开始支持 [[194]](<https://downloads.haskell.org/~ghc/9.4.1/docs/users_guide/9.4.1-notes.html?highlight=xdg>)，但截至 2022-09-24，Arch 软件包为 9.0.2 且尚未更新。   
[ghcup-hs-bin](<https://aur.archlinux.org/packages/ghcup-hs-bin/>)AUR |  `~/.ghcup` |  [[195]](<https://gitlab.haskell.org/haskell/ghcup-hs/-/commit/80603662b4fcc42fd936f45608dc3bc924c7e498>) |  [[196]](<https://gitlab.haskell.org/haskell/ghcup-hs/issues/39>) |  `export GHCUP_USE_XDG_DIRS=true` 环境变量 `GHCUP_USE_XDG_DIRS` 可以设置为任何非空值。请参阅 [[197]](<https://www.haskell.org/ghcup/guide/#xdg-support>)。   
[gliv](<https://aur.archlinux.org/packages/gliv/>)AUR |  `~/.glivrc` |  |  |  `gliv --glivrc="$XDG_CONFIG_HOME"/gliv/glivrc`  
[gnuradio](<https://archlinux.org/packages/?name=gnuradio>)包 |  `~/.gnuradio` |  |  [[198]](<https://github.com/gnuradio/gnuradio/issues/3631>) | GNU Radio： `export GR_PREFS_PATH="$XDG_CONFIG_HOME"/gnuradio` GNU Radio Companion： `export GRC_PREFS_PATH="$XDG_CONFIG_HOME"/gnuradio/grc.conf`  
[GnuPG](<../zh-cn/GnuPG.html> "GnuPG") |  `~/.gnupg` |  |  [[199]](<https://bugs.gnupg.org/gnupg/issue1456>) [[200]](<https://bugs.gnupg.org/gnupg/issue1018>) |  `export GNUPGHOME="$XDG_DATA_HOME"/gnupg`，`gpg2 --homedir "$XDG_DATA_HOME"/gnupg` 请注意，目前使用 systemd 用户单元和基于 socket 的激活无法开箱即用，因为 socket 目录会根据 `$GNUPGHOME` 的哈希值发生变化。您可以使用 `gpgconf --list-dirs socketdir` 获取新的 socket 目录，并必须修改 systemd 用户单元以相应地监听正确的 socket。还必须使用以下 `gpg-agent.service` 插入文件（或以其他方式将 GNUPGHOME 环境变量传递给在 systemd 中运行的代理），否则您可能会遇到“丢失”私钥的问题： 
    
    [Service]
    Environment="GNUPGHOME=%h/.local/share/gnupg"
    
如果您[使用 GPG 作为您的 SSH 代理](<../zh-cn/GnuPG.html#SSH_%E4%BB%A3%E7%90%86> "GnuPG")，请将 `SSH_AUTH_SOCK` 设置为 `gpgconf --list-dirs agent-ssh-socket` 的输出，而不是某些硬编码值。   
[Go](<../zh-cn/Go.html> "Go") |  `~/go` |  [[201]](<https://github.com/golang/go/commit/ca8a055f5cc7c1dfa0eb542c60071c7a24350f76>) |  |  `export GOPATH="$XDG_DATA_HOME"/go`，`export GOMODCACHE="$XDG_CACHE_HOME"/go/mod` 如果未设置 `GOMODCACHE`，则默认为 `$GOPATH/pkg/mod`（参见 [[202]](<https://go.dev/ref/mod#environment-variables>)）。 支持 `GOCACHE`，默认为 `$XDG_CACHE_HOME/go-build`（参见 [[203]](<https://pkg.go.dev/cmd/go#hdr-Build_and_test_caching>)）。   
[Google Earth](<../zh-cn/Google_Earth.html> "Google Earth") |  `~/.googleearth` |  |  | 可以使用 `~/.config/Google/GoogleEarthPlus.conf` 中的 `KMLPath` 和 `CachePath` 选项更改某些路径。   
[gopass](<https://archlinux.org/packages/?name=gopass>)包 |  `~/.password-store` |  |  | 覆盖 `~/.config/gopass/config.yml` 中的设置： 
    
    ~/.config/gopass/config.yml
    
    root:
    path: gpgcli-gitcli-fs+file:///home/<userid>/.config/password-store
      
[gpodder](<https://archlinux.org/packages/?name=gpodder>)包 |  `~/gPodder` |  |  |  `GPODDER_DOWNLOAD_DIR` 用于设置下载文件夹。`GPODDER_HOME` 用于指定配置和数据库文件的存储位置，同时如果未设置 `GPODDER_DOWNLOAD_DIR`，下载的文件也会保存在此目录中。   
[GQ LDAP client](<https://sourceforge.net/projects/gqclient>) |  `~/.gq`，`~/.gq-state` |  [1.51](<https://sourceforge.net/p/gqclient/mailman/message/2053978>) |  |  `export GQRC="$XDG_CONFIG_HOME"/gqrc`，`export GQSTATE="$XDG_DATA_HOME"/gq/gq-state`，`mkdir -p "$(dirname "$GQSTATE")"`  
[Gradle](</wzh/index.php?title=Gradle&action=edit&redlink=1> "Gradle（页面不存在）")（英语：[Gradle](<https://wiki.archlinux.org/title/Gradle> "en:Gradle")） |  `~/.gradle` |  |  [[204]](<https://discuss.gradle.org/t/be-a-nice-freedesktop-citizen-move-the-gradle-to-the-appropriate-location-in-linux/2199>) [[205]](<https://github.com/gradle/gradle/issues/8262>) |  `export GRADLE_USER_HOME="$XDG_DATA_HOME"/gradle`  
[GTK](<../zh-cn/GTK.html> "GTK") 1  |  `~/.gtkrc` |  |  |  `export GTK_RC_FILES="$XDG_CONFIG_HOME"/gtk-1.0/gtkrc`  
[GTK](<../zh-cn/GTK.html> "GTK") 2  |  `~/.gtkrc-2.0` |  |  |  `export GTK2_RC_FILES="$XDG_CONFIG_HOME/gtk-2.0/gtkrc":"$XDG_CONFIG_HOME/gtk-2.0/gtkrc.mine"` 如果使用了 **Lxappearance** ，`~/.gtkrc-2.0` 可能会不断被创建，因为点击“应用”时的定制设置会写入到这个文件。该路径在 Lxappearance 中是硬编码的，但作为一个输出文件，这些设置可以被反复移动到该位置。   
[hledger](<https://archlinux.org/packages/?name=hledger>)包 |  `~/.hledger.journal` |  |  [[206]](<https://github.com/simonmichael/hledger/issues/1081>) |  `export LEDGER_FILE="$XDG_DATA_HOME"/hledger.journal`  
[Houdini](<https://www.sidefx.com/products/houdini/>) |  `~/houdini _MAJOR_._MINOR_)` |  |  [[207]](<https://forums.odforce.net/topic/43138-changing-home-location/>) [[208]](<https://www.sidefx.com/docs/houdini/ref/env.html>) |  `export HOUDINI_USER_PREF_DIR="$XDG_CACHE_HOME"/houdini__HVER__` 这个变量的值必须包含子字符串 `__HVER__`，它将在运行时被替换成当前的 `_MAJOR_._MINOR_` 版本号。   
[imapfilter](<https://aur.archlinux.org/packages/imapfilter/>)AUR |  `~/.imapfilter` |  |  |  `export IMAPFILTER_HOME="$XDG_CONFIG_HOME/imapfilter"`  
[IPFS](</wzh/index.php?title=IPFS&action=edit&redlink=1> "IPFS（页面不存在）")（英语：[IPFS](<https://wiki.archlinux.org/title/IPFS> "en:IPFS")） |  `~/.ipfs` |  |  |  `export IPFS_PATH="$XDG_DATA_HOME"/ipfs`  
[irb](<https://ruby-doc.org/3.2.2/stdlibs/irb/IRB.html>) |  `~/.irbrc` |  |  | 
    
    ~/.profile
    
    $ export IRBRC="$XDG_CONFIG_HOME"/irb/irbrc
    
    "$XDG_CONFIG_HOME"/irb/irbrc
    
    IRB.conf[:SAVE_HISTORY] ||= 1000
    IRB.conf[:HISTORY_FILE] ||= File.join(ENV["XDG_DATA_HOME"], "irb", "history")  
  
[irssi](<../zh-cn/Irssi.html> "Irssi") |  `~/.irssi` |  |  [[209]](<https://github.com/irssi/irssi/pull/511>) |  `irssi --config="$XDG_CONFIG_HOME"/irssi/config --home="$XDG_DATA_HOME"/irssi`  
[isync](</wzh/index.php?title=Isync&action=edit&redlink=1> "Isync（页面不存在）")（英语：[isync](<https://wiki.archlinux.org/title/isync> "en:isync")） |  `~/.mbsyncrc` |  |  [[210]](<https://sourceforge.net/p/isync/feature-requests/14/>) |  `mbsync -c "$XDG_CONFIG_HOME"/isync/mbsyncrc`  
[Java#OpenJDK](<../zh-cn/Java.html#OpenJDK> "Java") |  `~/.java/.userPrefs` |  |  [[211]](<https://bugzilla.redhat.com/show_bug.cgi?id=1154277>) |  `export _JAVA_OPTIONS=-Djava.util.prefs.userRoot="$XDG_CONFIG_HOME"/java`  
[jupyter](<../zh-cn/Jupyter.html> "Jupyter") |  `~/.jupyter` |  [5.0.0rc0](<https://github.com/jupyter/jupyter_core/releases/tag/5.0.0rc0>) |  [[212]](<https://github.com/jupyter/jupyter_core/issues/185>) [[213]](<https://github.com/jupyter/jupyter_core/pull/292>) |  [python-jupyter-core](<https://archlinux.org/packages/?name=python-jupyter-core>)包 < v5.0.0： `export JUPYTER_CONFIG_DIR="$XDG_CONFIG_HOME"/jupyter` v5.0.0 <= [python-jupyter-core](<https://archlinux.org/packages/?name=python-jupyter-core>)包 < v6.0.0：  `export JUPYTER_PLATFORM_DIRS="1"` (see [[214]](<https://github.com/jupyter/jupyter_core/blob/3efd00e5804424198285c63ebc6dc6c085d8c857/jupyter_core/paths.py#L176-L181>))  [python-jupyter-core](<https://archlinux.org/packages/?name=python-jupyter-core>)包 >= v6.0.0：完整支持（通过[python-platformdirs](<https://archlinux.org/packages/?name=python-platformdirs>)包），默认开启   
[k9s](<https://archlinux.org/packages/?name=k9s>)包 |  `~/.k9s` |  [0.20.4](<https://github.com/derailed/k9s/releases/tag/v0.20.4>) |  [[215]](<https://github.com/derailed/k9s/issues/743>) |  `export K9SCONFIG="$XDG_CONFIG_HOME"/k9s`  
[KDE](<../zh-cn/KDE.html> "KDE") |  `~/.kde`，`~/.kde4` |  |  [[216]](<https://userbase.kde.org/KDE_System_Administration/KDE_Filesystem_Hierarchy#KDEHOME>) |  `export KDEHOME="$XDG_CONFIG_HOME"/kde`  
[keychain](<https://archlinux.org/packages/?name=keychain>)包 |  `~/.keychain` |  [[217]](<https://github.com/funtoo/keychain/commit/d43099bcff315d24a2ca31ae83da85e115d22ef6>) |  [[218]](<https://github.com/funtoo/keychain/issues/8>) |  `keychain --absolute --dir "$XDG_RUNTIME_DIR"/keychain`  
[kodi](<https://archlinux.org/packages/?name=kodi>)包 |  `~/.kodi` |  [[219]](<https://github.com/xbmc/xbmc/pull/14460>) |  [[220]](<https://github.com/xbmc/xbmc/pull/6142>) |  `KODI_DATA=$XDG_DATA_HOME/kodi`  
[kscript](<https://aur.archlinux.org/packages/kscript/>)AUR |  `~/.kscript` |  |  [[221]](<https://github.com/holgerbrandl/kscript/issues/323>) |  `export KSCRIPT_CACHE_DIR="$XDG_CACHE_HOME"/kscript`  
[ledger](<../zh-cn/Ledger.html> "Ledger") |  `~/.ledgerrc`，`~/.pricedb` |  |  [[222]](<https://github.com/ledger/ledger/issues/1820>) |  `ledger --init-file "$XDG_CONFIG_HOME"/ledgerrc`  
[Leiningen](</wzh/index.php?title=Leiningen&action=edit&redlink=1> "Leiningen（页面不存在）")（英语：[Leiningen](<https://wiki.archlinux.org/title/Leiningen> "en:Leiningen")） |  `~/.lein`，`~/.m2` |  |  |  `export LEIN_HOME="$XDG_DATA_HOME"/lein` 要更改 Leiningen 使用的 m2 仓库位置，请参阅：[Leiningen#m2 仓库位置](</wzh/index.php?title=Leiningen&action=edit&redlink=1> "Leiningen（页面不存在）")（英语：[Leiningen#m2 repo location](<https://wiki.archlinux.org/title/Leiningen#m2_repo_location> "en:Leiningen")）  
[libdvdcss](<https://archlinux.org/packages/?name=libdvdcss>)包 |  `~/.dvdcss` |  |  [[223]](<https://mailman.videolan.org/pipermail/libdvdcss-devel/2014-August/001022.html>) |  `export DVDCSS_CACHE="$XDG_DATA_HOME"/dvdcss`  
[libice](<https://archlinux.org/packages/?name=libice>)包 |  `~/.ICEauthority` |  |  [[224]](<https://gitlab.freedesktop.org/xorg/lib/libice/issues/2>) |  `export ICEAUTHORITY="$XDG_CACHE_HOME"/ICEauthority` 确保提前设置 `XDG_CACHE_HOME`，使其指向运行 [Xorg](<../zh-cn/Xorg.html> "Xorg") 的用户有写权限的目录。  **不要** 使用 `XDG_RUNTIME_DIR`，因为它是在登录**之后** 才可用的。否则启动 [Xorg](<../zh-cn/Xorg.html> "Xorg") 的显示管理器（如 [GDM](<../zh-cn/GDM.html> "GDM")）将会反复失败。   
[LibreOffice](<../zh-cn/LibreOffice.html> "LibreOffice") |  |  |  [[225]](<https://bugs.documentfoundation.org/show_bug.cgi?id=140039>) | LibreOffice 将所有数据存储在 `$XDG_CONFIG_HOME/libreoffice/4/user/` 目录下，包括运行时文件、用户数据、缓存和扩展。其中一些路径可以在**工具(T) > 选项(O)⋯ > LibreOffice > 路径**中进行更改。   
[libx11](<../zh-cn/Xorg.html> "Xorg") |  `~/.XCompose`，`~/.compose-cache` |  |  |  `export XCOMPOSEFILE="$XDG_CONFIG_HOME"/X11/xcompose`，`export XCOMPOSECACHE="$XDG_CACHE_HOME"/X11/xcompose`  
[ltrace](<https://archlinux.org/packages/?name=ltrace>)包 |  `~/.ltrace.conf` |  |  |  `ltrace -F "$XDG_CONFIG_HOME"/ltrace/ltrace.conf`  
[lynx](<https://archlinux.org/packages/?name=lynx>)包 |  `/etc/lynx.cfg` |  |  |  `export LYNX_CFG="$XDG_CONFIG_HOME"/lynx.cfg`  
[m17n-db](<https://git.savannah.nongnu.org/cgit/m17n/m17n-db.git>) |  `~/.m17n.d` |  |  [[226]](<https://savannah.nongnu.org/bugs/?63056>) |   
[maptool-bin](<https://aur.archlinux.org/packages/maptool-bin/>)AUR |  `~/.maptool-rptools` |  |  [[227]](<https://github.com/RPTools/maptool/issues/2786>) | 
    
    /opt/maptool/lib/app/MapTool.cfg
    
    [JavaOptions]
    -DMAPTOOL_DATADIR=.local/share/maptool-rptools

但是，没有办法改变这个配置文件的位置。   
[maven](<https://archlinux.org/packages/?name=maven>)包 |  `~/.m2` |  |  [[228]](<https://issues.apache.org/jira/browse/MNG-6603>) |  `export MAVEN_OPTS=-Dmaven.repo.local="$XDG_DATA_HOME"/maven/repository` ，`mvn -gs "$XDG_CONFIG_HOME"/maven/settings.xml`并在 [settings.xml](<https://maven.apache.org/settings.html#Simple_Values>) 中根据需要设置 `<localRepository>`  
[Mathematica](<../zh-cn/Mathematica.html> "Mathematica") |  `~/.Mathematica` |  |  |  `export MATHEMATICA_USERBASE="$XDG_CONFIG_HOME"/mathematica`  
[maxima](<https://archlinux.org/packages/?name=maxima>)包 |  `~/.maxima` |  |  |  `export MAXIMA_USERDIR="$XDG_CONFIG_HOME"/maxima`  
[mednafen](<https://archlinux.org/packages/?name=mednafen>)包 |  `~/.mednafen` |  |  |  `export MEDNAFEN_HOME="$XDG_CONFIG_HOME"/mednafen`  
[minikube](<https://archlinux.org/packages/?name=minikube>)包 |  `~/.minikube` |  |  [[229]](<https://github.com/kubernetes/minikube/issues/4109>) |  `export MINIKUBE_HOME="$XDG_DATA_HOME"/minikube` 无论出于什么原因，这会在 `MINIKUBE_HOME` 中创建一个额外的 `.minikube` 目录。   
[mitmproxy](<https://archlinux.org/packages/?name=mitmproxy>)包 |  `~/.mitmproxy` |  |  |  `alias mitmproxy="mitmproxy --set confdir=$XDG_CONFIG_HOME/mitmproxy"`，`alias mitmweb="mitmweb --set confdir=$XDG_CONFIG_HOME/mitmproxy"`  
[MOC](</wzh/index.php?title=MOC&action=edit&redlink=1> "MOC（页面不存在）")（英语：[MOC](<https://wiki.archlinux.org/title/MOC> "en:MOC")） |  `~/.moc` |  |  |  `mocp -M "$XDG_CONFIG_HOME"/moc`，`mocp -O MOCDir="$XDG_CONFIG_HOME"/moc`  
[monero](<https://archlinux.org/packages/?name=monero>)包 |  `~/.bitmonero` |  |  |  `monerod --data-dir "$XDG_DATA_HOME"/bitmonero`  
[most](<https://archlinux.org/packages/?name=most>)包 |  `~/.mostrc` |  |  |  `export MOST_INITFILE="$XDG_CONFIG_HOME"/mostrc`  
[MPlayer](<../zh-cn/MPlayer.html> "MPlayer") |  `~/.mplayer` |  |  |  `export MPLAYER_HOME="$XDG_CONFIG_HOME"/mplayer`  
[mtpaint](<https://archlinux.org/packages/?name=mtpaint>)包 |  `~/.mtpaint` |  |  [[230]](<https://github.com/wjaguar/mtPaint/issues/22>) | 
    
    /etc/mtpaint/mtpaintrc
    
    userINI = ~/.config/mtpaint  
  
[mypy](<https://archlinux.org/packages/?name=mypy>)包 |  `~/.config/mypy/config`，`~/.mypy.ini`，`~/.mypy_cache` |  [v0.670](<https://github.com/python/mypy/pull/6304>) |  [[231]](<https://github.com/python/mypy/issues/6065>) [[232]](<https://github.com/python/mypy/issues/8790>) |  `XDG_CONFIG_HOME/mypy/config`，`export MYPY_CACHE_DIR="$XDG_CACHE_HOME"/mypy`  
[MySQL](<../zh-cn/MySQL.html> "MySQL") |  `~/.mysql_history`，`~/.my.cnf `，`~/.mylogin.cnf` |  |  |  `export MYSQL_HISTFILE="$XDG_DATA_HOME"/mysql_history` `~/.my.cnf` 仅支持 mysql-server，不支持 mysql-client [[233]](<https://dev.mysql.com/doc/refman/8.0/en/option-files.html>) `~/.mylogin.cnf` 不支持。   
[mysql-workbench](<https://archlinux.org/packages/?name=mysql-workbench>)包 |  `~/.mysql/workbench` |  |  | 您可以使用 `--configdir` 标志运行 MySQL Workbench，例如 `mysql-workbench --configdir="$XDG_DATA_HOME/mysql/workbench"`。该目录需要手动创建，因为 MySQL Workbench 默认位置是 `$HOME/.mysql/workbench`。   
[ncurses](<https://archlinux.org/packages/?name=ncurses>)包 |  `~/.terminfo` |  |  | 排除系统路径搜索： `export TERMINFO="$XDG_DATA_HOME"/terminfo`，`export TERMINFO_DIRS="$XDG_DATA_HOME"/terminfo:/usr/share/terminfo`  
[n](<https://github.com/tj/n>) |  `/usr/local/n` |  |  |  `export N_PREFIX=$XDG_DATA_HOME/n`  
[ncmpc](<https://archlinux.org/packages/?name=ncmpc>)包 |  `~/.ncmpc` |  |  |  `ncmpc -f "$XDG_CONFIG_HOME"/ncmpc/config`  
[Netbeans](</wzh/index.php?title=Netbeans&action=edit&redlink=1> "Netbeans（页面不存在）")（英语：[Netbeans](<https://wiki.archlinux.org/title/Netbeans> "en:Netbeans")） |  `~/.netbeans` |  |  [[234]](<https://bz.apache.org/netbeans/show_bug.cgi?id=215961>) |  `netbeans --userdir "${XDG_CONFIG_HOME}"/netbeans`  
[Node.js](<../zh-cn/Node.js.html> "Node.js") |  `~/.node_repl_history` |  |  [[235]](<https://nodejs.org/api/repl.html#repl_environment_variable_options>) |  `export NODE_REPL_HISTORY="$XDG_DATA_HOME"/node_repl_history`  
[npm](<https://archlinux.org/packages/?name=npm>)包 |  `~/.npm`，`~/.npmrc` |  |  [[236]](<https://github.com/npm/cli/issues/654>) |  `export NPM_CONFIG_USERCONFIG=$XDG_CONFIG_HOME/npm/npmrc`
    
    npmrc
    
    prefix=${XDG_DATA_HOME}/npm
    cache=${XDG_CACHE_HOME}/npm
    init-module=${XDG_CONFIG_HOME}/npm/config/npm-init.js
    logs-dir=${XDG_STATE_HOME}/npm/logs
    
如果 Node.js 是通过 [nvm](<https://aur.archlinux.org/packages/nvm/>)AUR 安装的，则 `prefix` 是不必要的（且不受支持）。   
[opam](<https://archlinux.org/packages/?name=opam>)包 |  `~/.opam` |  |  [[237]](<https://github.com/ocaml/opam/issues/3766>) |  `export OPAMROOT="$XDG_DATA_HOME/opam"` 配置和状态数据都存储在 `OPAMROOT` 中，因此该解决方案不完全兼容。   
[PuTTY](</wzh/index.php?title=PuTTY&action=edit&redlink=1> "PuTTY（页面不存在）")（英语：[PuTTY](<https://wiki.archlinux.org/title/PuTTY> "en:PuTTY")） |  `~/.putty/` |  [9952b2d](<https://git.tartarus.org/?p=simon/putty.git;a=commit;h=9952b2d5bd5c8fbac4f5731a805bce10fe4ce47c>) |  | 如果已存在，将使用 `$XDG_CONFIG_HOME/putty`。如果不存在，则创建 `~/.putty`。如果两者都存在，则优先使用 `$XDG_CONFIG_HOME/putty`。已在 0.74 中测试。   
[python-easyocr](<https://aur.archlinux.org/packages/python-easyocr/>)AUR |  `~/.EasyOCR` |  |  |  `export EASYOCR_MODULE_PATH="$XDG_CONFIG_HOME/EasyOCR"`  
[spotdl](<https://aur.archlinux.org/packages/spotdl/>)AUR |  `~/.spotdl` |  [v4.0.6](<https://github.com/spotDL/spotify-downloader/releases/tag/v4.0.6>) ([3929cae](<https://github.com/spotDL/spotify-downloader/commit/3929caed5a2e8c2858a1dc3898ad75be263fdb96>))  |  [[238]](<https://github.com/spotDL/spotify-downloader/issues/1651>) |  `mkdir "$XDG_DATA_HOME"/spotdl`  
[nuget](<https://archlinux.org/packages/?name=nuget>)包 |  `~/.nuget/packages` |  |  [[239]](<https://docs.microsoft.com/en-us/nuget/consume-packages/managing-the-global-packages-and-cache-folders>) |  `export NUGET_PACKAGES="$XDG_CACHE_HOME"/NuGetPackages`  
[NVIDIA](<../zh-cn/NVIDIA.html> "NVIDIA") |  `~/.nv` |  |  | 如果设置则使用 `XDG_CACHE_HOME`，否则不正确地回退到 `~/.nv` 而不是 `~/.cache`。   
[nvidia-settings](<https://archlinux.org/packages/?name=nvidia-settings>)包 |  `~/.nvidia-settings-rc` |  |  [[240]](<https://github.com/NVIDIA/nvidia-settings/issues/30>) |  `nvidia-settings --config="$XDG_CONFIG_HOME"/nvidia/settings`  
[nvm](<https://aur.archlinux.org/packages/nvm/>)AUR |  `~/.nvm` |  |  |  `export NVM_DIR="$XDG_DATA_HOME"/nvm`  
[Octave](<../zh-cn/Octave.html> "Octave") |  `~/octave`，`~/.octave_packages`，`~/.octave_hist` |  |  |  `export OCTAVE_HISTFILE="$XDG_CACHE_HOME/octave-hsts"`，`export OCTAVE_SITE_INITFILE="$XDG_CONFIG_HOME/octave/octaverc"`
    
    $XDG_CONFIG_HOME/octave/octaverc
    
    source /usr/share/octave/site/m/startup/octaverc;
    pkg prefix ~/.local/share/octave/packages ~/.local/share/octave/packages;
    pkg local_list /home/<your username>/.local/share/octave/octave_packages;
    
`local_list` 选项必须给出绝对路径。   
[omnisharp-roslyn-bin](<https://aur.archlinux.org/packages/omnisharp-roslyn-bin/>)AUR |  `~/.omnisharp/` |  [[241]](<https://github.com/OmniSharp/omnisharp-roslyn/commit/e1353fb8ded7070d6e126b0b6030dac5d3d707ea>) |  [[242]](<https://github.com/OmniSharp/omnisharp-roslyn/issues/953>) |  `export OMNISHARPHOME="$XDG_CONFIG_HOME/omnisharp"`  
[openscad](<https://archlinux.org/packages/?name=openscad>)包 |  `~/.OpenSCAD` |  [7c3077b0f](<https://github.com/openscad/openscad/commit/7c3077b0f>) |  [[243]](<https://github.com/openscad/openscad/issues/125>) | 不完全遵守 XDG 基本目录规范，请参阅 [[244]](<https://github.com/openscad/openscad/issues/373>)。 目前它[硬编码](<https://github.com/openscad/openscad/blob/master/src/platform/PlatformUtils-posix.cc#L105>) `~/.local/share`。   
[packettracer](<https://aur.archlinux.org/packages/packettracer/>)AUR |  `~/.packettracer`，`~/packettracer/` |  |  | 具有 GUI 配置来更改 PT 安装目录，`~/packettracer/`（ _选项 > 首选项 > 管理 > 用户文件夹_）。此路径写入文件 `~/.packettracer`。   
[parallel](<https://archlinux.org/packages/?name=parallel>)包 |  `~/.parallel` |  [20170422](<https://git.savannah.gnu.org/cgit/parallel.git/commit/?id=685018f532f4e2d24b84eb28d5de3d759f0d1af1>) |  |  `export PARALLEL_HOME="$XDG_CONFIG_HOME"/parallel`  
[pass](<../zh-cn/Pass.html> "Pass") |  `~/.password-store` |  |  |  `export PASSWORD_STORE_DIR="$XDG_DATA_HOME"/pass`  
[Phive](<https://phar.io>) |  `~/.phive` |  |  [[245]](<https://github.com/phar-io/phive/issues/297>) 以及 [[246]](<https://github.com/phar-io/phive/issues/286>) 和 [[247]](<https://github.com/phar-io/phive/issues/233>) | 从 0.14.5 开始，可以移动整个数据目录。 `export PHIVE_HOME="$XDG_DATA_HOME/phive"`  
[Pidgin](<../zh-cn/Pidgin.html> "Pidgin") |  `~/.purple` |  |  [[248]](<https://developer.pidgin.im/ticket/4911>) |  `pidgin --config="$XDG_DATA_HOME"/purple`  
[platformio-core](<https://archlinux.org/packages/?name=platformio-core>)包 |  `~/.platformio` |  |  [[249]](<https://github.com/platformio/platformio-core/issues/2872>) |  `export PLATFORMIO_CORE_DIR="$XDG_DATA_HOME"/platformio`  
[PostgreSQL](<../zh-cn/PostgreSQL.html> "PostgreSQL") |  `~/.psqlrc`，`~/.psql_history`，`~/.pgpass`，`~/.pg_service.conf` | 9.2  |  [[250]](<https://www.postgresql.org/docs/current/static/app-psql.html>) [[251]](<https://www.postgresql.org/docs/current/static/libpq-envars.html>) |  `export PSQLRC="$XDG_CONFIG_HOME/pg/psqlrc"`，`export PSQL_HISTORY="$XDG_STATE_HOME/psql_history"`，`export PGPASSFILE="$XDG_CONFIG_HOME/pg/pgpass"`，`export PGSERVICEFILE="$XDG_CONFIG_HOME/pg/pg_service.conf"` 必须创建这两个目录：`mkdir "$XDG_CONFIG_HOME/pg" && mkdir "$XDG_STATE_HOME"`  
[PulseAudio](<../zh-cn/PulseAudio.html> "PulseAudio") |  `~/.esd_auth` |  |  | 很可能是由 `module-esound-protocol-unix.so` 模块生成的。可以将其配置为使用不同的位置，但更有意义的是，在 `/etc/pulse/default.pa` 或 `"$XDG_CONFIG_HOME"/pulse/default.pa` 中注释掉此模块。   
[pyenv](<https://archlinux.org/packages/?name=pyenv>)包 |  `~/.pyenv` |  |  [[252]](<https://github.com/pyenv/pyenv/issues/139>) [[253]](<https://github.com/pyenv/pyenv/issues/1789>) |  `export PYENV_ROOT=$XDG_DATA_HOME/pyenv`  
[azure-cli](<https://archlinux.org/packages/?name=azure-cli>)包 |  `~/.azure` |  |  |  `export AZURE_CONFIG_DIR=$XDG_DATA_HOME/azure`  
[python](<../zh-cn/Python.html> "Python") |  `~/.python_history` |  [v3.13](<https://github.com/python/cpython/pull/13208#issuecomment-1877159768>) |  [[254]](<https://bugs.python.org/issue29779>) [[255]](<https://bugs.python.org/issue20886>) [[256]](<https://github.com/python/cpython/pull/13208>) | 自[版本 3.4](<https://bugs.python.org/issue5845>) 起，所有交互式会话的历史记录默认保存到 `~/.python_history`，自 3.13 起，保存到 `PYTHON_HISTORY`。您仍可以像在旧版本中一样自定义此功能（请参阅[此示例](<https://docs.python.org/3/library/readline.html?highlight=readline#example>)），包括[使用自定义路径](<https://bugs.python.org/msg318437>)或[禁用历史记录保存](<https://bugs.python.org/msg265568>)。 [PYTHON_HISTORY](<https://docs.python.org/3.13/using/cmdline.html#envvar-PYTHON_HISTORY>)：`export PYTHON_HISTORY=$XDG_STATE_HOME/python/history` [PYTHONPYCACHEPREFIX](<https://docs.python.org/3/using/cmdline.html#envvar-PYTHONPYCACHEPREFIX>)：`export PYTHONPYCACHEPREFIX=$XDG_CACHE_HOME/python` [PYTHONUSERBASE](<https://docs.python.org/3/using/cmdline.html#envvar-PYTHONUSERBASE>)：`export PYTHONUSERBASE=$XDG_DATA_HOME/python`  
[python-grip](<https://aur.archlinux.org/packages/python-grip/>)AUR |  `~/.grip` |  |  |  `export GRIPHOME="$XDG_CONFIG_HOME/grip"`  
[python-setuptools](<https://archlinux.org/packages/?name=python-setuptools>)包 |  `~/.python-eggs` |  |  |  `export PYTHON_EGG_CACHE="$XDG_CACHE_HOME"/python-eggs`  
[racket](<https://archlinux.org/packages/?name=racket>)包 |  `~/.racketrc`，`~/.racket` |  |  [[257]](<https://github.com/racket/racket/issues/2740>) |  `export PLTUSERHOME="$XDG_DATA_HOME"/racket`  
[rbenv](<https://aur.archlinux.org/packages/rbenv/>)AUR |  `~/.rbenv` |  |  [[258]](<https://github.com/rbenv/rbenv/issues/811>) [[259]](<https://github.com/rbenv/rbenv/issues/1146>) |  `export RBENV_ROOT="$XDG_DATA_HOME"/rbenv`  
[nodenv](<https://aur.archlinux.org/packages/nodenv/>)AUR |  `~/.nodenv` |  |  |  `export NODENV_ROOT="$XDG_DATA_HOME"/nodenv`  
[readline](<../zh-cn/Readline.html> "Readline") |  `~/.inputrc` |  |  |  `export INPUTRC="$XDG_CONFIG_HOME"/readline/inputrc`  
[recoll](<https://archlinux.org/packages/?name=recoll>)包 |  `~/.recoll` |  |  |  `export RECOLL_CONFDIR="$XDG_CONFIG_HOME/recoll"`  
[redis](</wzh/index.php?title=Redis&action=edit&redlink=1> "Redis（页面不存在）")（英语：[redis](<https://wiki.archlinux.org/title/redis> "en:redis")） |  `~/.rediscli_history`，`~/.redisclirc` |  |  |  `export REDISCLI_HISTFILE="$XDG_DATA_HOME"/redis/rediscli_history`，`export REDISCLI_RCFILE="$XDG_CONFIG_HOME"/redis/redisclirc`  
[ripgrep](<https://archlinux.org/packages/?name=ripgrep>)包 |  |  |  [[260]](<https://github.com/BurntSushi/ripgrep/blob/master/GUIDE.md#configuration-file>) |  `export RIPGREP_CONFIG_PATH=$XDG_CONFIG_HOME/ripgrep/config`  
[rlwrap](<https://archlinux.org/packages/?name=rlwrap>)包 |  `~/.*_history` |  |  [[261]](<https://github.com/hanslub42/rlwrap/issues/25>) |  `export RLWRAP_HOME="$XDG_DATA_HOME"/rlwrap`  
[ruby-bundler](<https://archlinux.org/packages/?name=ruby-bundler>)包 |  `~/.bundle` |  [4a120d8](<https://github.com/rubygems/rubygems/commit/4a120d82a730c92c78571bf1819a841ca1ac94a2>) |  [拉取请求 3545](<https://github.com/rubygems/rubygems/pull/3545>) | 
    
    export BUNDLE_USER_CACHE=$XDG_CACHE_HOME/bundle
    export BUNDLE_USER_CONFIG=$XDG_CONFIG_HOME/bundle/config
    export BUNDLE_USER_PLUGIN=$XDG_DATA_HOME/bundle
    
有关更多信息，请参阅 [Bundler: bundle config](<https://bundler.io/v2.5/man/bundle-config.1.html#CONFIGURE-BUNDLER-DIRECTORIES>)。   
[ruby-solargraph](<https://aur.archlinux.org/packages/ruby-solargraph/>)AUR |  `~/.solargraph/cache/` |  |  [[262]](<https://github.com/castwide/solargraph/blob/master/README.md>) |  `export SOLARGRAPH_CACHE=$XDG_CACHE_HOME/solargraph`  
[ruff](<https://archlinux.org/packages/?name=ruff>)包 |  `.ruff_cache` |  |  [[263]](<https://github.com/charliermarsh/ruff/issues/1292>) |  `export RUFF_CACHE_DIR=$XDG_CACHE_HOME/ruff`  
[Rust#Rustup](<../zh-cn/Rust.html#Rustup> "Rust") |  `~/.rustup` |  |  [[264]](<https://github.com/rust-lang-nursery/rustup.rs/issues/247>) |  `export RUSTUP_HOME="$XDG_DATA_HOME"/rustup`  
[sbt](<https://archlinux.org/packages/?name=sbt>)包 |  `~/.sbt` `~/.ivy2` |  |  [[265]](<https://github.com/sbt/sbt/issues/3681>) |  `sbt -ivy "$XDG_DATA_HOME"/ivy2 -sbt-dir "$XDG_DATA_HOME"/sbt`（注意 [[266]](<https://github.com/sbt/sbt/issues/3598>)）   
[SageMath](<../zh-cn/SageMath.html> "SageMath") |  `~/.sage` |  |  |  `export DOT_SAGE="$XDG_CONFIG_HOME"/sage`  
[GNU Screen](<../zh-cn/GNU_Screen.html> "GNU Screen") |  `~/.screenrc` `~/.screen/` |  |  |  `export SCREENRC="$XDG_CONFIG_HOME"/screen/screenrc`，`export SCREENDIR="${XDG_RUNTIME_DIR}/screen"`  
[simplescreenrecorder](<https://aur.archlinux.org/packages/simplescreenrecorder/>)AUR |  `~/.ssr/` |  [0.4.3](<https://github.com/MaartenBaert/ssr/releases/tag/0.4.3>) |  [[267]](<https://github.com/MaartenBaert/ssr/issues/407>) [[268]](<https://github.com/MaartenBaert/ssr/issues/813>) | 仅当已创建时才会使用 `$XDG_CONFIG_HOME/simplescreenrecorder/`，否则默认为 `~/.ssr`。 `mv ~/.ssr "$XDG_CONFIG_HOME"/simplescreenrecorder`  
[singularity-ce](<https://aur.archlinux.org/packages/singularity-ce/>)AUR |  `~/.singularity` |  [3.11.4](<https://github.com/sylabs/singularity/releases/tag/v3.11.4>) |  |  `export SINGULARITY_CONFIGDIR="$XDG_CONFIG_HOME/singularity"`，`export SINGULARITY_CACHEDIR="$XDG_CACHE_HOME/singularity"`  
[spacemacs](<https://www.spacemacs.org/>) |  `~/.spacemacs`，`~/.spacemacs.d` |  [[269]](<https://github.com/syl20bnr/spacemacs/commit/e1eed07c30ea395fb9cfebc8ec3376dcffbace11>) |  [[270]](<https://github.com/syl20bnr/spacemacs/issues/3589>) | 移动 `~/.spacemacs` 文件。 `export SPACEMACSDIR="$XDG_CONFIG_HOME"/spacemacs`，`mv ~/.spacemacs "$SPACEMACSDIR"/init.el` 其他文件需要像 Emacs 一样进行配置。   
[starship](<https://archlinux.org/packages/?name=starship>)包 |  `~/.config/starship`，`~/.cache/starship` |  [[271]](<https://github.com/starship/starship/pull/86>) ([v0.2.0](<https://github.com/starship/starship/releases/tag/v0.2.0>))，[[272]](<https://github.com/starship/starship/pull/1576>) ([v0.45.0](<https://github.com/starship/starship/releases/tag/v0.45.0>))  |  [[273]](<https://github.com/starship/starship/issues/896#issuecomment-952402978>) |  `export STARSHIP_CONFIG="$XDG_CONFIG_HOME"/starship.toml`，`export STARSHIP_CACHE="$XDG_CACHE_HOME"/starship`  
[subversion](<../zh-cn/Subversion.html> "Subversion") |  `~/.subversion` |  |  [[274]](<https://issues.apache.org/jira/browse/SVN-4599>) [[275]](<https://mail-archives.apache.org/mod_mbox/subversion-users/201204.mbox/%3c4F8FBCC6.4080205@ritsuka.org%3e>)[[276]](<https://mail-archives.apache.org/mod_mbox/subversion-dev/201509.mbox/%3C20150917222954.GA20331@teapot%3E>) |  `alias svn="svn --config-dir \"$XDG_CONFIG_HOME\"/subversion"`  
[sudo](<https://archlinux.org/packages/?name=sudo>)包 |  `~/.sudo_as_admin_successful` |  [1.9.6](<https://www.sudo.ws/stable.html#1.9.6>) |  [[277]](<https://github.com/sudo-project/sudo/issues/56>) [[278]](<https://www.sudo.ws/repos/sudo/rev/d77c3876fa95>) | 仅在编译时激活时存在（默认无）。自 1.9.6 起，可以在 /etc/sudoers 中使用 admin_flag 参数。   
[task](<https://archlinux.org/packages/?name=task>)包 |  `~/.task`，`~/.taskrc` |  |  |  `export TASKDATA="$XDG_DATA_HOME"/task`，`export TASKRC="$XDG_CONFIG_HOME"/task/taskrc`}}，[在 2.6 版中完全支持](<https://github.com/GothenburgBitFactory/taskwarrior/pull/2316>)（请注意，$XDG_CONFIG_HOME/task/taskrc **必须** 存在，否则即使设置了 $XDG_CONFIG_HOME，taskwarrior 也会在旧的 $HOME/.taskrc 位置创建示例配置 [[279]](<https://github.com/GothenburgBitFactory/taskwarrior/pull/2316#issuecomment-732821437>)[[280]](<https://github.com/GothenburgBitFactory/taskwarrior/blob/112ac54a57adfb3cc2e6e60dbbb1f5c7d9db3e18/doc/man/task.1.in#L1451>)）   
本地 [TeX Live](<../zh-cn/TeX_Live.html> "TeX Live") TeXmf 树、TeXmf 缓存和配置  |  `~/texmf`，`~/.texlive/texmf-var`，`~/.texlive/texmf-config` |  |  |  `export TEXMFHOME=$XDG_DATA_HOME/texmf`，`export TEXMFVAR=$XDG_CACHE_HOME/texlive/texmf-var`，`export TEXMFCONFIG=$XDG_CONFIG_HOME/texlive/texmf-config`  
[TeXmacs](<https://www.texmacs.org/>) |  `~/.TeXmacs` |  |  |  `export TEXMACS_HOME_PATH=$XDG_STATE_HOME/texmacs`  
[tiptop](<https://aur.archlinux.org/packages/tiptop/>)AUR |  `~/.tiptoprc` |  |  | 这仍然需要 `.tiptoprc` 文件。 `tiptop -W "$XDG_CONFIG_HOME"/tiptop`  
[ruby-travis](<https://aur.archlinux.org/packages/ruby-travis/>)AUR |  `~/.travis/` |  |  [[281]](<https://github.com/travis-ci/travis.rb/issues/219>) |  `export TRAVIS_CONFIG_PATH=$XDG_CONFIG_HOME/travis`  
[uncrustify](<https://archlinux.org/packages/?name=uncrustify>)包 |  `~/.uncrustify.cfg` |  |  |  `export UNCRUSTIFY_CONFIG="$XDG_CONFIG_HOME"/uncrustify/uncrustify.cfg`  
[Unison](<../zh-cn/Unison.html> "Unison") |  `~/.unison` |  |  |  `export UNISON="$XDG_DATA_HOME"/unison`  
[units](<https://aur.archlinux.org/packages/units/>)AUR |  `~/.units_history` |  |  |  `units --history "$XDG_CACHE_HOME"/units_history`  
[urxvtd](</wzh/index.php?title=Rxvt-unicode/%E6%8F%90%E7%A4%BA%E5%92%8C%E6%8A%80%E5%B7%A7&action=edit&redlink=1> "Rxvt-unicode/提示和技巧（页面不存在）")（英语：[rxvt-unicode/Tips and tricks#Daemon-client](<https://wiki.archlinux.org/title/rxvt-unicode/Tips_and_tricks#Daemon-client> "en:rxvt-unicode/Tips and tricks")） |  `~/.urxvt/urxvtd-hostname` |  |  |  `export RXVT_SOCKET="$XDG_RUNTIME_DIR"/urxvtd`  
[Vagrant](</wzh/index.php?title=Vagrant&action=edit&redlink=1> "Vagrant（页面不存在）")（英语：[Vagrant](<https://wiki.archlinux.org/title/Vagrant> "en:Vagrant")） |  `~/.vagrant.d`，`~/.vagrant.d/aliases` |  |  [[282]](<https://www.vagrantup.com/docs/other/environmental-variables.html>) |  `export VAGRANT_HOME="$XDG_DATA_HOME"/vagrant`，`export VAGRANT_ALIAS_FILE="$XDG_DATA_HOME"/vagrant/aliases`  
[vint](<https://archlinux.org/packages/?name=vint>)包 |  `~/.vintrc.yaml`，`.vintrc.yml`，`.vintrc` |  [0f741ac2c](<https://github.com/Vimjas/vint/pull/235/commits/0f741ac2c>) |  [[283]](<https://github.com/Vimjas/vint/pull/235>) | 文档未记录，但代码显示 `$XDG_CONFIG_HOME/.vintrc.yaml` 应该可以工作   
[virtualenv](</wzh/index.php?title=Virtualenv&action=edit&redlink=1> "Virtualenv（页面不存在）")（英语：[virtualenv](<https://wiki.archlinux.org/title/virtualenv> "en:virtualenv")） |  `~/.virtualenvs` |  |  |  `export WORKON_HOME="$XDG_DATA_HOME/virtualenvs"`  
[Visual Studio Code](<../zh-cn/Visual_Studio_Code.html> "Visual Studio Code") |  `~/.vscode-oss/` |  |  [[284]](<https://github.com/Microsoft/vscode/issues/3884>) | 您可以使用 `export VSCODE_PORTABLE="$XDG_DATA_HOME"/vscode`，但该方法未记录在文档中，可能会意外中断。 设置此项会使编辑器在 `$VSCODE_PORTABLE/user-data` 中查找 `.config/Code - OSS` 的内容。  您还可以使用 `--extensions-dir` 标志运行 Visual Studio，例如 `code --extensions-dir "$XDG_DATA_HOME/vscode"`。这已记录在文档中并[有其他用例](<https://github.com/microsoft/vscode/issues/329>)，不大可能意外中断。   
[VSCodium](<https://aur.archlinux.org/packages/VSCodium/>)AUR |  `~/.vscode-oss/` |  |  [[285]](<https://github.com/VSCodium/vscodium/issues/561>) [[286]](<https://github.com/VSCodium/vscodium/issues/671>) | 您可以使用 `--extensions-dir` 标志运行 VSCodium，例如 `vscodium --extensions-dir "$XDG_DATA_HOME/vscode"`。但这不会阻止创建 `~/.vscode-oss/` 目录。   
[w3m](<https://archlinux.org/packages/?name=w3m>)包 |  `~/.w3m` |  [26284ff](<https://github.com/tats/w3m/commit/26284ff62781cbc14ff18593a8251409ca730098>) |  [[287]](<https://sourceforge.net/p/w3m/feature-requests/31/>) [[288]](<https://github.com/tats/w3m/issues/130>) |  `export W3M_DIR="$XDG_STATE_HOME/w3m"`  
[wakatime](<https://archlinux.org/packages/?name=wakatime>)包 |  `~/.wakatime.cfg`，`~/.wakatime.data`，`~/.wakatime.db`，`~/.wakatime.log` |  |  |  `export WAKATIME_HOME="$XDG_CONFIG_HOME/wakatime"` 该目录需要手动创建  `mkdir "$XDG_CONFIG_HOME/wakatime"`  
[wget](<../zh-cn/Wget.html> "Wget") |  `~/.wgetrc`, `~/.wget-hsts` |  |  |  `export WGETRC="$XDG_CONFIG_HOME/wgetrc"` 并将以下内容添加为 wget 的别名：`wget --hsts-file="$XDG_CACHE_HOME/wget-hsts"`，或者使用绝对路径设置 `hsts-file` 变量，因为 wgetrc 不支持环境变量：`echo hsts-file \= "$XDG_CACHE_HOME"/wget-hsts >> "$XDG_CONFIG_HOME/wgetrc"`  
[wine](<../zh-cn/Wine.html> "Wine") |  `~/.wine` |  |  [[289]](<https://bugs.winehq.org/show_bug.cgi?id=20888>) |  [Winetricks](<../zh-cn/Wine.html#Winetricks> "Wine") 使用以下类似 XDG 的位置进行 [WINEPREFIX](<../zh-cn/Wine.html#WINEPREFIX> "Wine") 管理： `mkdir -p "$XDG_DATA_HOME"/wineprefixes`, `export WINEPREFIX="$XDG_DATA_HOME"/wineprefixes/default`  
[x3270](<https://aur.archlinux.org/packages/x3270/>)AUR |  `~/.x3270pro`，`~/.c3270pro` |  |  |  `export X3270PRO="$XDG_CONFIG_HOME"/x3270/config`，`export C3270PRO="$XDG_CONFIG_HOME"/c3270/config` 应用程序还创建了 `~/.x3270connect` 但该目录目前不支持使用 XDG。   
[xbindkeys](</wzh/index.php?title=Xbindkeys&action=edit&redlink=1> "Xbindkeys（页面不存在）")（英语：[xbindkeys](<https://wiki.archlinux.org/title/xbindkeys> "en:xbindkeys")） |  `~/.xbindkeysrc` |  |  |  `xbindkeys -f "$XDG_CONFIG_HOME"/xbindkeys/config`  
[xorg-xauth](<https://archlinux.org/packages/?name=xorg-xauth>)包 |  `~/.Xauthority` |  |  |  `export XAUTHORITY="$XDG_RUNTIME_DIR"/Xauthority` 请注意，[LightDM](<../zh-cn/LightDM.html> "LightDM") 不允许您更改此变量。如果您仍然更改它，您将无法登录。请改用 [startx](<../zh-cn/Xinit.html> "Startx") 或 [配置 LightDM](<https://askubuntu.com/a/961459>)。根据 [[290]](<https://unix.stackexchange.com/a/175331>)，[SLiM](<../zh-cn/SLiM.html> "SLiM") 已硬编码 `~/.Xauthority`。  [SDDM](<../zh-cn/SDDM.html> "SDDM") Xauthority 路径可以在其自己的配置文件中更改，如下所示。不幸的是，它是相对于主目录的。 
    
    /etc/sddm.conf.d/xauth-path.conf
    
    [X11]
    UserAuthFile=.Xauthority

在 Wayland 上，覆盖此设置可能会导致 Xorg 程序无法连接到 Xwayland 服务器。例如，[kwin](<https://archlinux.org/packages/?name=kwin>)包 和 [mutter](<https://archlinux.org/packages/?name=mutter>)包 都使用随机名称，因此无法将其设置为静态值。   
[xinit](<../zh-cn/Xinit.html> "Xinit") |  `~/.xinitrc`，`~/.xserverrc` |  |  [[291]](<https://gitlab.freedesktop.org/xorg/app/xinit/issues/14>) |  `export XINITRC="$XDG_CONFIG_HOME"/X11/xinitrc`，`export XSERVERRC="$XDG_CONFIG_HOME"/X11/xserverrc`  
[xorg-xrdb](<https://archlinux.org/packages/?name=xorg-xrdb>)包 |  `~/.Xresources`，`~/.Xdefaults` |  |  | 最终您 [应该](<https://superuser.com/questions/243914/xresources-or-xdefaults>) 使用 `Xresources`，并且由于这些资源是通过 `xrdb` 加载的，因此您可以指定一个路径，例如 `xrdb -load ~/.config/X11/xresources`。   
[Xorg](<../zh-cn/Xorg.html> "Xorg") |  `~/.xsession`，`~/.xsessionrc`，`~/.Xsession`，`~/.xsession-errors` |  |  | 这些可以作为 Xorg 初始化脚本 (`~/.xinitrc`) 或 Xsession 启动脚本 (通常基于 `/etc/X11/Xsession`) 的一部分添加。 根据您配置 `$XDG_CACHE_HOME` 的位置，您可能需要自行扩展路径。 
    
    # xsession start script
    
    USERXSESSION="$XDG_CACHE_HOME/X11/xsession"
    USERXSESSIONRC="$XDG_CACHE_HOME/X11/xsessionrc"
    ALTUSERXSESSION="$XDG_CACHE_HOME/X11/Xsession"
    ERRFILE="$XDG_CACHE_HOME/X11/xsession-errors"
    
与此表中的大多数其他示例不同，实际的 X11 启动脚本在安装之间会有很大差异。   
[z](<https://archlinux.org/packages/?name=z>)包 |  `~/.z` |  |  [[292]](<https://github.com/rupa/z/issues/267>) |  `export _Z_DATA="$XDG_DATA_HOME/z"`  
[yarn](<https://archlinux.org/packages/?name=yarn>)包 |  `~/.yarnrc`，`~/.yarn/`，`~/.yarncache/`，`~/.yarn-config/` |  [2d454b5](<https://github.com/yarnpkg/yarn/commit/2d454b5>) |  [[293]](<https://github.com/yarnpkg/yarn/pull/5336>) [[294]](<https://github.com/yarnpkg/yarn/issues/2334>) |  `alias yarn='yarn --use-yarnrc "$XDG_CONFIG_HOME/yarn/config"'`  
[zsh](<../zh-cn/Zsh.html> "Zsh") |  `~/.zshrc`，`~/.zprofile`，`~/.zshenv`，`~/.zlogin`，`~/.zlogout`，`~/.histfile`，`~/.zcompdump`，`~/.zcompcache` |  [[295]](<https://www.zsh.org/mla/workers/2013/msg00692.html>) |  |  `export ZDOTDIR=$HOME/.config/zsh` 以避免在主目录中的大多数 [zsh dotfiles](<../zh-cn/Zsh.html#Startup/Shutdown_files> "Zsh")。 
    
    .config/zsh/.zshrc
    
    HISTFILE="$XDG_STATE_HOME"/zsh/history
    # 代码补全文件：使用 XDG 目录
    [ -d "$XDG_CACHE_HOME"/zsh ] || mkdir -p "$XDG_CACHE_HOME"/zsh
    zstyle ':completion:*' cache-path "$XDG_CACHE_HOME"/zsh/zcompcache
    compinit -d "$XDG_CACHE_HOME"/zsh/zcompdump-$ZSH_VERSION

最后，如果您使用 zsh 作为登录 shell，并选择依赖启动文件 `~/.zshenv` **或** `~/.zprofile` **或** `~/.zlogin` 来设置重要的环境变量（例如 `ZDOTDIR`）进行引导，则无法绕过将设置 `ZDOTDIR` 的一个文件放在默认位置。对于上下文，一个例外是，如果您的更广泛的系统配置在此之前设置了 `ZDOTDIR` 环境变量。   
  
###  硬编码

应用程序  | 旧路径  | 讨论  | 注释   
---|---|---|---  
[adb](<../zh-cn/Android_%E8%B0%83%E8%AF%95%E6%A1%A5.html> "Adb") & [Android Studio](<https://developer.android.com/studio/index.html>) |  `~/.android/` |  | 尽管[看起来并非如此](<https://android.googlesource.com/platform/system/core/+/d5fcafaf41f8ec90986c813f75ec78402096af2d%5E%21/>)，adb 将“始终”生成 `~/.android/adbkeys`，尽管它也会尝试 `ADB_VENDOR_KEYS` 中的密钥。   
[aegisub](<https://archlinux.org/packages/?name=aegisub>)包 |  `~/.aegisub/` |  [[296]](<https://github.com/Aegisub/Aegisub/issues/226>) |   
[alpine](</wzh/index.php?title=Alpine&action=edit&redlink=1> "Alpine（页面不存在）")（英语：[alpine](<https://wiki.archlinux.org/title/alpine> "en:alpine")） |  `~/.pinerc`，`~/.addressbook`，`~/.pine-debug[1-4]`，`~/.newsrc`，`~/.mailcap`，`~/.mime.types`，`~/.pine-interrupted-mail` |  |  `alias alpine="alpine -p $XDG_CONFIG_HOME/alpine/pinerc"` 在上面的配置文件中，可以使用 `newsrc-path=` 和 `address-book=` 等选项定制一些位置。   
[aMule](<../zh-cn/AMule.html> "AMule") |  `~/.aMule` |  [[297]](<https://bugs.amule.org/view.php?id=1308>) [[298]](<http://forum.amule.org/index.php?topic=18056>) [[299]](<https://github.com/amule-project/amule/issues/254>) |   
[anthy](<https://osdn.net/projects/anthy/>) |  `~/.anthy` |  [[300]](<https://osdn.net/ticket/browse.php?group_id=14&tid=28397>) |   
[Apache Directory Studio](<https://directory.apache.org/studio/>) |  `~/.ApacheDirectoryStudio` |  |   
[ARandR](<https://christian.amsuess.com/tools/arandr/>) |  `~/.screenlayout` |  [[301]](<https://gitlab.com/arandr/arandr/-/issues/45>) |   
[Arduino](<../zh-cn/Arduino.html> "Arduino") |  `~/.arduino15`，`~/.jssc` |  [不会修复](<https://github.com/arduino/Arduino/issues/3915>) |   
[arduino-cli](<https://archlinux.org/packages/?name=arduino-cli>)包 |  `~.arduino15/` |  [[302]](<https://github.com/arduino/arduino-cli/pull/140>) |  `mv ~/.arduino15 $XDG_CONFIG_HOME/arduino15` 在 arduino-cli.yaml 中指定 Arduino CLI 使用的新目录，如文档[此处](<https://arduino.github.io/arduino-cli/latest/configuration/>)所述。 `alias arduino-cli='arduino-cli --config-file $XDG_CONFIG_HOME/arduino15/arduino-cli.yaml'`  
[ASP.NET Core](<https://dotnet.microsoft.com/en-us/apps/aspnet>) |  `~/.aspnet` |  [[303]](<https://github.com/dotnet/aspnetcore/issues/43278>) |   
[Avidemux](<http://fixounet.free.fr/avidemux/>) |  `~/.avidemux6` |  [[304]](<https://avidemux.org/smif/index.php/topic,19596.0.html>) |   
[Bash](<../zh-cn/Bash.html> "Bash") |  `~/.bashrc`，`~/.bash_history`，`~/.bash_profile`，`~/.bash_login`，`~/.bash_logout` |  [108134](<https://savannah.gnu.org/support/?108134>) [10431](<https://savannah.gnu.org/patch/?10431>) |  `mkdir -p "$XDG_STATE_HOME"/bash` `export HISTFILE="$XDG_STATE_HOME"/bash/history` `bashrc` 可从 `/etc/bash.bashrc` 中的不同位置获取。 对于交互式 shell，请指定 `--init-file <file>` 作为 `~/.bashrc` 的替代。   
[borgmatic](</wzh/index.php?title=Borgmatic&action=edit&redlink=1> "Borgmatic（页面不存在）")（英语：[borgmatic](<https://wiki.archlinux.org/title/borgmatic> "en:borgmatic")） |  `~/.borgmatic/` |  [[305]](<https://projects.torsion.org/borgmatic-collective/borgmatic/issues/562>) | 在您的 `config.yaml` 中设置 `borgmatic_source_directory: ~/.local/state/borgmatic`。这可能会破坏恢复，请参阅讨论。   
[Berkshelf](</wzh/index.php?title=Chef&action=edit&redlink=1> "Chef（页面不存在）")（英语：[Chef](<https://wiki.archlinux.org/title/Chef> "en:Chef")） |  `~/.berkshelf/` |  |   
[chatty](<https://aur.archlinux.org/packages/chatty/>)AUR |  `~/.chatty/` |  [[306]](<https://github.com/chatty/chatty/issues/273>) |   
[cmake](<https://archlinux.org/packages/?name=cmake>)包 |  `~/.cmake/` |  [[307]](<https://gitlab.kitware.com/cmake/cmake/-/issues/22480>) | 用于用户包注册表 `~/.cmake/packages/<package>`，详见 [cmake-packages(7) § User Package Registry](<https://man.archlinux.org/man/cmake-packages.7#User_Package_Registry>) 和 [Package registry wiki 页面](<https://gitlab.kitware.com/cmake/community/wikis/doc/tutorials/Package-Registry>)。看起来像是硬编码的，例如在 [cmFindPackageCommand.cxx](<https://gitlab.kitware.com/cmake/cmake/blob/v3.12.1/Source/cmFindPackageCommand.cxx#L1221>)。   
[cmus](<https://archlinux.org/packages/?name=cmus>)包 |  `~/.config/cmus` |  [[308]](<https://github.com/cmus/cmus/pull/69>) |  [[309]](<https://github.com/cmus/cmus/issues/1283>)  
[Cinnamon](<../zh-cn/Cinnamon.html> "Cinnamon") |  `~/.cinnamon/` |  [[310]](<https://github.com/linuxmint/Cinnamon/issues/7807>) |   
[conan](<https://aur.archlinux.org/packages/conan/>)AUR |  `~/.conan/` |  [[311]](<https://github.com/conan-io/conan/issues/2526>) |  `export CONAN_USER_HOME="$XDG_CONFIG_HOME"` 将设置创建 `.conan/` 的目录。它是 [旨在简化 CI](<https://docs.conan.io/en/latest/reference/env_vars.html#conan-user-home>)，但也可以在这里使用。   
[cryptomator](<https://aur.archlinux.org/packages/cryptomator/>)AUR |  `~/.Cryptomator` |  [[312]](<https://github.com/cryptomator/cryptomator/issues/710>) |   
[cVim](<https://chrome.google.com/webstore/detail/cvim/ihlenndgcmojhcghmfjfneahoeklbjjh>)[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2022-09-23 ⓘ] |  `~/.cvimrc` |  [[313]](<https://github.com/1995eaton/chromium-vim/issues/750>) |   
[darcs](</wzh/index.php?title=Darcs&action=edit&redlink=1> "Darcs（页面不存在）")（英语：[darcs](<https://wiki.archlinux.org/title/darcs> "en:darcs")） |  `~/.darcs/` |  [[314]](<http://bugs.darcs.net/issue2453>) |   
[dart](<https://archlinux.org/packages/?name=dart>)包 |  `~/.dart`，`~/.dart-tool`，`~/.dartServer` |  [[315]](<https://github.com/dart-lang/sdk/issues/41560>) |   
[dbus](<../zh-cn/D-Bus.html> "Dbus") |  `~/.dbus/` |  [[316]](<https://gitlab.freedesktop.org/dbus/dbus/issues/46>) | 考虑使用 [dbus-broker](<https://archlinux.org/packages/?name=dbus-broker>)包，因为它不会创建或使用该目录。   
[devede](<https://archlinux.org/packages/?name=devede>)包 |  `~/.devedeng` |  | 在[此处](<https://gitlab.com/rastersoft/devedeng/blob/f0893b3ff7b14723bd148db35bdfe2d284156d19/src/devedeng/configuration_data.py#L111>)硬编码   
[Dia](<https://wiki.gnome.org/Apps/Dia>) |  `~/.dia/` |  |   
[dig](<https://man.archlinux.org/man/dig.1>) |  `~/.digrc` |  |   
[dotnet-sdk](<https://archlinux.org/packages/?name=dotnet-sdk>)包 |  `~/.dotnet/`，`~/.templateengine` |  [[317]](<https://github.com/dotnet/cli/issues/7569>) |   
[dropbox](<../zh-cn/Dropbox.html> "Dropbox") |  `~/.dropbox/` |  |   
[Eclipse](<../zh-cn/Eclipse.html> "Eclipse") |  `~/.eclipse/` |  [[318]](<https://bugs.eclipse.org/bugs/show_bug.cgi?id=200809>) | 选项 `-Dosgi.configuration.area=@user.home/.config/..` 可覆盖，但必须添加到 `"$ECLIPSE_HOME"/eclipse.ini"` 而不是命令行，这意味着您必须具有对 `$ECLIPSE_HOME` 的写权限。（Arch Linux 在 `/usr/bin/eclipse` 中对 `$ECLIPSE_HOME` 进行硬编码。）   
[emacs-slime](<https://archlinux.org/packages/?name=emacs-slime>)包 |  `~/.slime/` |  [[319]](<https://github.com/slime/slime/issues/610>) [[320]](<https://github.com/slime/slime/pull/787>) |   
[equalx](<https://aur.archlinux.org/packages/equalx/>)AUR |  `~/.equalx/` |  [[321]](<https://bugs.launchpad.net/equalx/+bug/2014460>) |   
[Fetchmail](<https://www.fetchmail.info/>) |  `~/.fetchmailrc` |  |   
[Firefox](<../zh-cn/Firefox.html> "Firefox") |  `~/.mozilla/` |  [[322]](<https://bugzil.la/259356>) [[323]](<https://phabricator.services.mozilla.com/D6995>) |   
[Flatpak](<../zh-cn/Flatpak.html> "Flatpak") |  `~/.var/` |  [[324]](<https://github.com/flatpak/flatpak/issues/46>) [[325]](<https://github.com/flatpak/flatpak.github.io/issues/191>) [不会修复](<https://github.com/flatpak/flatpak/issues/1651>) |   
[freesweep](<https://github.com/rwestlund/freesweep>) |  `~/.sweeprc` |  [[326]](<https://github.com/rwestlund/freesweep/issues/9>) |   
[gftp](<https://aur.archlinux.org/packages/gftp/>)AUR |  `~/.gftp/` |  [[327]](<https://github.com/masneyb/gftp/issues/99#issuecomment-735030824>) | gftp 计划遵循 XDG 规范。   
[gitkraken](<https://aur.archlinux.org/packages/gitkraken/>)AUR |  `~/.gitkraken/` |  [[328]](<https://feedback.gitkraken.com/suggestions/197923/support-for-moving-the-config-directory-on-linux>) |   
[GoldenDict](<../zh-cn/GoldenDict.html> "GoldenDict") |  `~/.goldendict/` |  [[329]](<https://github.com/goldendict/goldendict/issues/151>) |   
[gphoto2](<https://archlinux.org/packages/?name=gphoto2>)包 |  `~/.gphoto` |  [[330]](<https://github.com/gphoto/gphoto2/issues/249>) |   
[gramps](<https://archlinux.org/packages/?name=gramps>)包 |  `~/.gramps/` |  [[331]](<https://gramps-project.org/bugs/view.php?id=8025>) | 2022 支持 XDG 基础目录规范（针对下一版本 Gramps 5.2）⸺补丁 <https://github.com/gramps-project/gramps/pull/1368>  
[groovy](<https://archlinux.org/packages/?name=groovy>)包 |  `~/.groovy/` |  |   
[grsync](<https://archlinux.org/packages/?name=grsync>)包 |  `~/.grsync/` |  [[332]](<https://sourceforge.net/p/grsync/feature-requests/15/>) |   
[google-cloud-cli](<https://aur.archlinux.org/packages/google-cloud-cli/>)AUR |  `~/.gsutil/` |  [[333]](<https://github.com/GoogleCloudPlatform/gsutil/issues/991>) |   
[gtk-recordMyDesktop](<https://recordmydesktop.sourceforge.net/about.php>) |  `~/.gtk-recordmydesktop` |  |   
[hplip](<https://archlinux.org/packages/?name=hplip>)包 |  `~/.hplip/` |  [[334]](<https://bugs.launchpad.net/hplip/+bug/307152>) |   
[hydrogen](<https://archlinux.org/packages/?name=hydrogen>)包 |  `~/.hydrogen/` |  [[335]](<https://github.com/hydrogen-music/hydrogen/issues/643>) |   
[idris](<https://www.idris-lang.org/>) |  `~/.idris` |  [[336]](<https://github.com/idris-lang/Idris-dev/pull/3456>) |   
[itch-setup-bin](<https://aur.archlinux.org/packages/itch-setup-bin/>)AUR |  `~/.itch` |  [不会修复](<https://github.com/itchio/itch/issues/2356>) | 您可以在应用程序设置中移动游戏安装位置。   
[Jmol](<https://sourceforge.net/projects/jmol/>) |  `~/.jmol/` |  [[337]](<https://sourceforge.net/p/jmol/feature-requests/261/>) |   
[lbdb](<https://aur.archlinux.org/packages/lbdb/>)AUR |  `~/.lbdbrc`，`~/.lbdb/` |  [[338]](<https://github.com/RolandRosenfeld/lbdb/blob/eb162aa9da36f699cf821c6487210c7979fcd8ee/TODO#L18>) |   
[llpp](</wzh/index.php?title=Llpp&action=edit&redlink=1> "Llpp（页面不存在）")（英语：[llpp](<https://wiki.archlinux.org/title/llpp> "en:llpp")） |  `~/.config/llpp.conf` |  [[339]](<https://github.com/moosotc/llpp/issues/180>)[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2022-09-23 ⓘ]（存储库已删除）  | 在 [3ab86f0](<https://repo.or.cz/w/llpp.git/commit/3ab86f0>) 中添加，但随后在[旧仓库:e253c9f1](<https://repo.or.cz/w/llpp.git/commit/e253c9f1>)/[新仓库:e253c9f1](<https://github.com/criticic/llpp/commit/e253c9f1ca971b4298cfee889820ad60bded54af>) 中恢复   
[Java](<../zh-cn/Java.html> "Java") OpenJDK  |  `~/.java/fonts` |  [[340]](<https://bugzilla.redhat.com/show_bug.cgi?id=1154277>) |  `export _JAVA_OPTIONS=-Djava.util.prefs.userRoot="$XDG_CONFIG_HOME"/java`  
[Java](<../zh-cn/Java.html> "Java") OpenJFX  |  `~/.java/webview` |  |   
[jgmenu](<https://archlinux.org/packages/?name=jgmenu>)包 |  `~/.jgmenu-lockfile` |  [[341]](<https://github.com/johanmalm/jgmenu/blob/3e48121dc28d06efb23c7901b7e138c2de167a84/src/lockfile.c#L11>) [[342]](<https://github.com/johanmalm/jgmenu/blob/4e45d04502fc5f77392bef0ff33b7bada0cf07d1/src/jgmenu_run#L7>) |   
[jitsi-meet](<https://aur.archlinux.org/packages/jitsi-meet/>)AUR |  `~/Downloads` |  [libjitsi#518](<https://github.com/jitsi/libjitsi/issues/518>) | 下载目录硬编码为 `~/Downloads` 而不是 `XDG_DOWNLOAD_DIR` （来自 [XDG 用户目录](<../zh-cn/XDG_%E7%94%A8%E6%88%B7%E7%9B%AE%E5%BD%95.html> "XDG 用户目录")）。   
[julia](<https://julialang.org/>) |  `~/.juliarc.jl`，`~/.julia_history`，`~/.julia` |  [[343]](<https://github.com/JuliaLang/julia/issues/4630>) [[344]](<https://github.com/JuliaLang/julia/issues/10016>) | 尾随的 `:$JULIA_DEPOT_PATH` 是必需的。请参阅 [[345]](<https://docs.julialang.org/en/v1/manual/environment-variables/#JULIA_DEPOT_PATH>)。 
    
    export JULIA_DEPOT_PATH="$XDG_DATA_HOME/julia:$JULIA_DEPOT_PATH"
    export JULIAUP_DEPOT_PATH="$XDG_DATA_HOME/julia"
      
[kotlin](<https://archlinux.org/packages/?name=kotlin>)包 |  `~/.kotlinc_history` |  | 相关 Konan 问题：[[346]](<https://youtrack.jetbrains.com/issue/KT-40763>)  
[Kubernetes](<../zh-cn/Kubernetes.html> "Kubernetes") |  `~/.kube/` |  [[347]](<https://github.com/kubernetes/kubectl/issues/942>)[[348]](<https://github.com/kubernetes/kubernetes/issues/56402>)[[349]](<https://github.com/kubernetes/kubernetes/issues/115522>) | 
    
    export KUBECONFIG="$XDG_CONFIG_HOME/kube" 
    export KUBECACHEDIR="$XDG_CACHE_HOME/kube"
      
[elan-lean](<https://aur.archlinux.org/packages/elan-lean/>)AUR |  `~/.elan` |  [[350]](<https://github.com/leanprover/elan/issues/75>) |   
[librewolf](<https://aur.archlinux.org/packages/librewolf/>)AUR |  `~/.mozilla` `~/.librewolf` |  [[351]](<https://codeberg.org/librewolf/issues/issues/443>) |   
[lldb](<https://lldb.llvm.org/>) |  `~/.lldb`，`~/.lldbinit` |  |   
[LMMS](<../zh-cn/LMMS.html> "LMMS") |  `~/.lmmsrc.xml` |  [[352]](<https://github.com/LMMS/lmms/issues/5869>) |   
[man-db](<https://archlinux.org/packages/?name=man-db>)包 |  `~/.manpath` |  [[353]](<https://gitlab.com/man-db/man-db/-/issues/39>) |   
[mathomatic](<https://www.mathomatic.org/>) |  `~/.mathomaticrc`，`~/.matho_history` |  | 可以使用 `rlwrap mathomatic -r` 并适当设置 `RLWRAP_HOME` 环境来移动历史记录。   
[MediaWiki](<../zh-cn/MediaWiki.html> "MediaWiki") |  `~/.mweval_history` and `~/.mwsql_history` (if $HOME is defined)  |  | 如果未定义 $HOME：`[MediaWiki]/maintenance/.mweval_history` 和 `[MediaWiki]/maintenance/.mwsql_history`。 由维护脚本 [eval.php](<https://github.com/wikimedia/mediawiki/blob/master/maintenance/eval.php#L99-L100>) 和 [sql.php](<https://github.com/wikimedia/mediawiki/blob/master/maintenance/sql.php#L124-L125>) 生成。   
[Minecraft](<../zh-cn/Minecraft.html> "Minecraft") |  `~/.minecraft/` |  [不会修复](<https://bugs.mojang.com/browse/MCL-2563>) |   
[Minetest](</wzh/index.php?title=Minetest&action=edit&redlink=1> "Minetest（页面不存在）")（英语：[Minetest](<https://wiki.archlinux.org/title/Minetest> "en:Minetest")） |  `~/.minetest/` |  [不会修复](<https://github.com/minetest/minetest/issues/864>) [[354]](<https://github.com/minetest/minetest/issues/8151>) |   
[minicom](<https://archlinux.org/packages/?name=minicom>)包 |  `~/.minirc.dfl` |  | Upstream 在 `~/.config/minicom` 下有一个用于支持配置文件的 TODO 条目。[[355]](<https://salsa.debian.org/minicom-team/minicom/-/blob/fe9ff103/TODO#L27>)  
[Mono](<../zh-cn/Mono.html> "Mono") |  `~/.mono/` |  [[356]](<https://github.com/mono/mono/pull/12764>) |   
[mongodb](<https://www.mongodb.org/>) |  `~/.mongorc.js`，`~/.dbshell` |  [[357]](<https://jira.mongodb.org/browse/DOCS-5652?jql=text%20~%20%22.mongorc.js%22>) |  [这个 Stack Overflow 线程](<https://stackoverflow.com/questions/22348604/the-mongorc-js-is-not-found-but-there-is-one/22349050#22349050>) 建议使用命令行开关 `--norc` 来实现部分解决方法。   
|  `~/.netrc` |  | 与 `~/.ssh` 一样，许多程序都希望此文件在此处。其中包括 curl (`CURLOPT_NETRC_FILE`)、[ftp](</wzh/index.php?title=Ftp&action=edit&redlink=1> "Ftp（页面不存在）") (`NETRC`)、[s-nail](</wzh/index.php?title=S-nail&action=edit&redlink=1> "S-nail（页面不存在）") (`NETRC`) 等项目。虽然其中一些提供了可配置的替代位置，但许多程序没有提供，例如 w3m、wget 和 lftp。   
[nim](<https://archlinux.org/packages/?name=nim>)包 |  `~/.nimble` |  [[358]](<https://github.com/nim-lang/nimble/issues/217>) [[359]](<https://github.com/nim-lang/Nim/issues/11340>) | Nimble 将在启动时 [尝试加载](<https://github.com/nim-lang/nimble/#configuration>) `~/.config/nimble/nimble.ini`，在那里设置 `nimbleDir`。您还必须在 Nim 编译器 [配置文件](<https://nim-lang.org/docs/nimc.html#compiler-usage-configuration-files>) 中更改 `nimblepath`。   
[nmcli](<../zh-cn/NetworkManager.html> "NetworkManager") |  `~/.nmcli-history` |  [[360]](<https://gitlab.freedesktop.org/NetworkManager/NetworkManager/-/issues/64>) | 硬编码为 `g_get_home_dir()`[[361]](<https://developer.gnome.org/glib/stable/glib-Miscellaneous-Utility-Functions.html#g-get-home-dir>) [[362]](<https://gitlab.freedesktop.org/NetworkManager/NetworkManager/-/blob/main/src/nmcli/connections.c#L6598>)  
[Networkmanager-openvpn](</wzh/index.php?title=Networkmanager-openvpn&action=edit&redlink=1> "Networkmanager-openvpn（页面不存在）")（英语：[Networkmanager-openvpn](<https://wiki.archlinux.org/title/Networkmanager-openvpn> "en:Networkmanager-openvpn")） |  `~/.cert/nm-openvpn` |  [[363]](<https://gitlab.gnome.org/GNOME/NetworkManager-openvpn/issues/35>) |   
[nyx](<https://archlinux.org/packages/?name=nyx>)包 |  `~/.nyx` |  | 该项目目前不再维护。   
[ollama](<https://archlinux.org/packages/?name=ollama>)包 |  `~/.ollama` |  [[364]](<https://github.com/jmorganca/ollama/issues/228>) | 可以使用以下命令设置模型位置： `export OLLAMA_MODELS=$XDG_DATA_HOME/ollama/models` 来源：[[365]](<https://github.com/jmorganca/ollama/pull/897>)  
[openshot](<https://archlinux.org/packages/?name=openshot>)包 |  `~/.openshot_qt` |  [[366]](<https://github.com/OpenShot/openshot-qt/issues/2440>) [[367]](<https://github.com/OpenShot/openshot-qt/issues/4477>) |   
[OpenSSH](<../zh-cn/OpenSSH.html> "OpenSSH") |  `~/.ssh` |  [不会修复](<https://web.archive.org/web/20190925004614/https://bugzilla.mindrot.org/show_bug.cgi?id=2050>) | 假定许多 ssh 守护进程和客户端（例如 DropBear 和 OpenSSH）都存在。   
[palemoon](<https://www.palemoon.org/>) |  `~/.moonchild productions` |  [[368]](<https://forum.palemoon.org/viewtopic.php?f=5&t=9639>) |   
[parsec-bin](<https://aur.archlinux.org/packages/parsec-bin/>)AUR |  `~/.parsec` |  |   
[pcsxr](<https://aur.archlinux.org/packages/pcsxr/>)AUR |  `~/.pcsxr` |  | 存在 `-cfg` 标志，但只能相对于 `~/.pcsxr` 进行设置。   
[perf](<https://perf.wiki.kernel.org/index.php/Main_Page>) |  `~/.debug` |  | 硬编码在 [tools/perf/util/config.c](<https://github.com/torvalds/linux/blob/7d42e98182586f57f376406d033f05fe135edb75/tools/perf/util/config.c#L35>)。提交：[[369]](<https://github.com/torvalds/linux/commit/45de34bbe3e1b8f4c8bc8ecaf6c915b4b4c545f8>)  
[perl](</wzh/index.php?title=Perl&action=edit&redlink=1> "Perl（页面不存在）")（英语：[perl](<https://wiki.archlinux.org/title/perl> "en:perl")） |  `~/.cpan`，`~/perl5` |  [[370]](<https://github.com/andk/cpanpm/issues/149>) | Perl5 的 [CPAN](<https://github.com/andk/cpanpm>) 需要 `~/.cpan`  
[phoronix-test-suite](<https://aur.archlinux.org/packages/phoronix-test-suite/>)AUR |  `~/.phoronix-test-suite` |  [[371]](<https://github.com/phoronix-test-suite/phoronix-test-suite/issues/453>) | 部分解决方法：[[372]](<https://github.com/phoronix-test-suite/phoronix-test-suite/blob/ebcde81fcd5cd63956e5f8db5664262b5fd4ceb9/pts-core/pts-core.php#L123>)。   
[PHP](<../zh-cn/PHP.html> "PHP") |  `~/.php_history` |  [[373]](<https://github.com/php/php-src/issues/8546>) | PHP 应用程序可以使用 [readline_read_history](<https://www.php.net/manual/en/function.readline-read-history.php>) ​​和 [readline_write_history](<https://www.php.net/manual/en/function.readline-write-history.php>) ​​读取/写入自定义文件。   
[portfolio-performance-bin](<https://aur.archlinux.org/packages/portfolio-performance-bin/>)AUR |  `~/.PortfolioPerformance/` |  [[374]](<https://github.com/buchen/portfolio/issues/1922>) |   
various [shell](<../zh-cn/%E5%91%BD%E4%BB%A4%E8%A1%8C%E8%A7%A3%E9%87%8A%E5%99%A8.html> "Shell")s and [display manager](<../zh-cn/Display_manager.html> "Display manager")s  |  `~/.profile` |  |   
[psensor](<https://archlinux.org/packages/?name=psensor>)包 |  `~/.psensor` |  [[375]](<https://gitlab.com/jeanfi/psensor/-/issues/38>) |   
[pulumi](<https://archlinux.org/packages/?name=pulumi>)包 |  `~/.pulumi` |  [[376]](<https://github.com/pulumi/pulumi/issues/2534>) |   
[python-tensorflow](<https://archlinux.org/packages/?name=python-tensorflow>)包 |  `~/.keras` |  [[377]](<https://github.com/tensorflow/tensorflow/issues/38831>) | 这个问题是关于 `tf.keras` 模块的。   
[quilt](<https://archlinux.org/packages/?name=quilt>)包 |  `~/.quiltrc` |  | 如果 `~/.quiltrc` 不存在，则返回 `/etc/quilt.quiltrc`。   
[Qt Designer](<https://doc.qt.io/qt-5/qtdesigner-manual.html>) |  `~/.designer` |  [[378]](<https://bugreports.qt.io/browse/QTCREATORBUG-26093>) |   
[R](</wzh/index.php?title=R&action=edit&redlink=1> "R（页面不存在）")（英语：[R](<https://wiki.archlinux.org/title/R> "en:R")） |  `~/.Rprofile`，`~/.Rdata`，`~/.Rhistory` |  | 
    
    R_HOME_USER="$HOME/.config/R"
    R_PROFILE_USER="$HOME/.config/R/profile"
    R_HISTFILE="$HOME/.config/R/history"
      
[RedNotebook](<https://rednotebook.sourceforge.net/>) |  `~/.rednotebook` |  [[379]](<https://github.com/jendrikseipp/rednotebook/issues/404>) |   
[Remarkable](<https://remarkableapp.github.io/linux.html>) |  `~/.remarkable` |  |   
[renderdoc](<https://archlinux.org/packages/?name=renderdoc>)包 |  `~/.renderdoc` |  [不会修复](<https://github.com/baldurk/renderdoc/pull/1741>) |   
[Ren'Py](<https://www.renpy.org/>) |  `~/.renpy` |  [不会修复](<https://github.com/renpy/renpy/issues/1377#issuecomment-370118555>) | 最新版本尊重 `RENPY_PATH_TO_SAVES` 环境变量。因此您可以设置它来更改某些游戏的路径。
    
    export RENPY_PATH_TO_SAVES="$XDG_DATA_HOME/renpy"  
  
[repo](<https://gerrit.googlesource.com/git-repo/>) |  `~/.repoconfig` |  [[380]](<https://bugs.chromium.org/p/gerrit/issues/detail?id=13997>) |   
[rpm](</wzh/index.php?title=Rpm&action=edit&redlink=1> "Rpm（页面不存在）")（英语：[rpm](<https://wiki.archlinux.org/title/rpm> "en:rpm")） |  `~/.rpmrc` `~/.rpmmacros` |  [Backlog](<https://github.com/rpm-software-management/rpm/issues/2153>) | 解决方法是使用 --rcfile 和 --macros，但这会产生副作用。   
[SANE](<../zh-cn/SANE.html> "SANE") |  `~/.sane/` |  |  `scanimage` 在该目录创建一个 `.cal` 文件。   
[sbcl](<https://archlinux.org/packages/?name=sbcl>)包 |  `~/.sbclrc` |  | 
    
    /etc/sbclrc
    
    (require :asdf)
    (setf sb-ext:*userinit-pathname-function*
          (lambda () (uiop:xdg-config-home #P"sbcl/sbclrc")))
    
请注意，这需要 root 权限，并将更改所有用户的 `~/.sbclrc` 位置。可以通过检查 `lambda` 表单中是否存在 `~/.sbclrc` 来缓解此问题。   
[SeaMonkey](<https://www.seamonkey-project.org/>) |  `~/.mozilla/seamonkey` |  [[381]](<https://bugzil.la/726939>) |   
[Signal Desktop](<https://signal.org/>) |  |  [[382]](<https://github.com/signalapp/Signal-Desktop/issues/4975>) | 目前将消息保存在 `~/.config/Signal` 中   
[Snap](<../zh-cn/Snap.html> "Snap") |  `~/snap/` |  [[383]](<https://bugs.launchpad.net/ubuntu/+source/snapd/+bug/1575053>) |   
[Solfege](<https://www.gnu.org/software/solfege/solfege.html>) |  `~/.solfege`, `~/.solfegerc`, `~/lessonfiles` |  [[384]](<https://savannah.gnu.org/bugs/index.php?50251>) |   
[SpamAssassin](<https://spamassassin.apache.org/>) |  `~/.spamassassin` |  |   
[Steam](<../zh-cn/Steam.html> "Steam") |  `~/.steam`, `~/.steampath`, `~/.steampid` |  [[385]](<https://github.com/ValveSoftware/steam-for-linux/issues/1890>) | 许多游戏引擎（Unity 3D、Unreal）都遵循该规范，但个别游戏发行商会对 [Steam Auto-Cloud](<https://www.ctrl.blog/entry/flatpak-steamcloud-xdg>) 中的路径进行硬编码，导致游戏保存同步到错误的目录。   
[stremio](<https://aur.archlinux.org/packages/stremio/>)AUR |  `~/.stremio-server/` |  [[386]](<https://github.com/Stremio/stremio-features/issues/268>) |   
[sts4](<https://github.com/spring-projects/sts4>) |  `~/.sts4` |  [[387]](<https://github.com/spring-projects/sts4/issues/601>) | 传递 JVM 参数 `-Dlanguageserver.boot.symbolCacheDir=$XDG_CACHE_HOME/sts4/symbolCache`  
[python-streamlit](<https://aur.archlinux.org/packages/python-streamlit/>)AUR |  `~/.streamlit` |  [[388]](<https://github.com/streamlit/streamlit/issues/2068>) |   
[sweethome3d](<https://archlinux.org/packages/?name=sweethome3d>)包 |  `~/.eteks/sweethome3d` |  [[389]](<https://sourceforge.net/p/sweethome3d/bugs/1256/>) |   
[python-sympy](<https://archlinux.org/packages/?name=python-sympy>)包 |  `~/.sympy-history` |  [[390]](<https://github.com/sympy/sympy/issues/26363>) |   
[TeamSpeak](</wzh/index.php?title=TeamSpeak&action=edit&redlink=1> "TeamSpeak（页面不存在）")（英语：[TeamSpeak](<https://wiki.archlinux.org/title/TeamSpeak> "en:TeamSpeak")） |  `~/.ts3client` |  |  `export TS3_CONFIG_DIR="$XDG_CONFIG_HOME/ts3client"`  
[terraform](<https://archlinux.org/packages/?name=terraform>)包 |  `~/.terraform.d/` |  [[391]](<https://github.com/hashicorp/terraform/issues/15389>) |   
[texinfo](<https://archlinux.org/packages/?name=texinfo>)包 |  `~/.infokey` |  |  `info --init-file "$XDG_CONFIG_HOME/infokey"`  
[Thunderbird](<../zh-cn/Thunderbird.html> "Thunderbird") |  `~/.thunderbird/` |  [[392]](<https://bugzil.la/735285>) |   
[TigerVNC](<../zh-cn/TigerVNC.html> "TigerVNC") |  `~/.vnc` |  [[393]](<https://github.com/TigerVNC/tigervnc/issues/1195>) |   
[tllocalmgr](<https://gitlab.archlinux.org/remy/texlive-localmanager>) |  `~/.texlive` |  |   
[urlview](<https://aur.archlinux.org/packages/urlview/>)AUR |  `~/.urlview` |  | 改用 fork [urlview-xdg-git](<https://aur.archlinux.org/packages/urlview-xdg-git/>)AUR。Fork 将使用 `XDG_CONFIG_HOME/urlview/config`  
[vale](<https://archlinux.org/packages/?name=vale>)包 |  `~/.vale.ini` |  [不会修复](<https://github.com/errata-ai/vale/issues/152>) |  `vale --config "$XDG_CONFIG_HOME/vale/config.ini"`  
[viber](<https://aur.archlinux.org/packages/viber/>)AUR |  `~/.ViberPC` |  |   
[vimperator](<http://www.vimperator.org/>) |  `~/.vimperatorrc` |  [[394]](<https://web.archive.org/web/20200514081339/http://www.mozdev.org/pipermail/vimperator/2009-October/004848.html>) |  `export VIMPERATOR_INIT=":source $XDG_CONFIG_HOME/vimperator/vimperatorrc"` `export VIMPERATOR_RUNTIME="$XDG_CONFIG_HOME"/vimperator`  
[visidata](<https://archlinux.org/packages/?name=visidata>)包 |  `~/.visidata` |  [[395]](<https://github.com/saulpw/visidata/issues/487>) |   
[wpa_cli](<https://w1.fi/>) |  `~/.wpa_cli_history` |  |   
[wego](<https://aur.archlinux.org/packages/wego/>)AUR |  `~/.wegorc` |  [[396]](<https://github.com/schachmat/wego/issues/116>) |   
[x2goclient](<https://aur.archlinux.org/packages/x2goclient/>)AUR |  `~/.x2goclient` |  |  `alias x2goclient="x2goclient --home=$HOME/.config"`  
[xpdf](<https://archlinux.org/packages/?name=xpdf>)包 |  `~/.xpdfrc` |  |   
[xrdp](<https://aur.archlinux.org/packages/xrdp/>)AUR |  `~/thinclient_drives` |  | 对于目录 `~/thinclient_drives`，您可以考虑编辑 `/etc/xrdp/sesman.ini` 并按照示例配置修改部分 `[Chansrv]`。   
[XVim2](<https://github.com/XVimProject/XVim2>) |  `~/.xvimrc` |  [[397]](<https://github.com/XVimProject/XVim2/issues/389>) |   
[YARD](<https://yardoc.org>) |  `~/.yard` |  [[398]](<https://github.com/lsegal/yard/issues/1230>) | 如果有人想实现它，将会接受 PR。   
[zenmap](<https://nmap.org/zenmap/>) [nmap](<https://archlinux.org/packages/?name=nmap>)包 |  `~/.zenmap` |  [[399]](<https://seclists.org/nmap-dev/2012/q2/163>) [[400]](<https://github.com/nmap/nmap/issues/590>) |   
[zoom](<https://aur.archlinux.org/packages/zoom/>)AUR |  `~/.zoom` |  | 不推荐：设置以下变量会移动 .zoom 的内容，但目录本身始终会创建。此外，它会破坏某些功能，例如无法开始会议。`export SSB_HOME="$XDG_DATA_HOME"/zoom`  
[zotero-bin](<https://aur.archlinux.org/packages/zotero-bin/>)AUR |  `~/.zotero` `~/Zotero` |  [[401]](<https://github.com/zotero/zotero/issues/1203>) |   
  
##  工具

工具 [xdg-ninja](<https://aur.archlinux.org/packages/xdg-ninja/>)AUR 可检测 `$HOME` 中可移动到 XDG 基本目录的不需要的文件/目录。请参阅 [README](<https://github.com/b3nj5m1n/xdg-ninja#xdg-ninja>) 了解示例。 

工具 [boxxy](<https://archlinux.org/packages/?name=boxxy>)包 可用于包装不遵守 XDG 基本目录的应用程序并重定向任何不需要的文件。 

工具 [ephemeral](<https://github.com/danisztls/ephemeral>) 可用于将通常位于 `XDG_CONFIG_HOME` 中的 chromium/electron 缓存链接到 `XDG_CACHE_HOME` 中的位置。 

##  库

C
    [libXDGdirs](<https://github.com/Jorengarenar/libXDGdirs>)
    [libxdg-basedir](<https://github.com/devnev/libxdg-basedir>)
     [C99：Cloudef的简单实现](<https://github.com/Cloudef/chck/tree/master/chck/xdg>).

C++
    [xdg-utils-cxx](<https://github.com/azubieta/xdg-utils-cxx>)
    [xdgpp](<https://sr.ht/~danyspin97/xdgpp>)

Go
    [adrg/xdg](<https://github.com/adrg/xdg>)
     [go-appdir](<https://github.com/ProtonMail/go-appdir>)（弃用，已归档）
     [configdir](<https://github.com/shibukawa/configdir>)（弃用，已归档）
     [kyoh86/xdg](<https://github.com/kyoh86/xdg>)（弃用，已归档）

Haskell
    自 1.2.3.0 [ab9d0810ce](<https://github.com/haskell/directory/commit/ab9d0810ce>) 起正式位于 [directory](<https://hackage.haskell.org/package/directory>)。
    [xdg-basedir](<https://hackage.haskell.org/package/xdg-basedir>)

JVM
    Java、Kotlin、Clojure、Scala⋯⋯
    [directories-jvm](<https://github.com/soc/directories-jvm>)

Perl
    [File-BaseDir](<https://search.cpan.org/dist/File-BaseDir/lib/File/BaseDir.pm>)

Python
    [pyxdg](<https://freedesktop.org/wiki/Software/pyxdg/>)
     [appdirs](<https://github.com/ActiveState/appdirs>)（已废弃）
    [platformdirs](<https://github.com/platformdirs/platformdirs>)

Ruby
    [bkuhlmann/xdg](<https://github.com/bkuhlmann/xdg>)
     [rubyworks/xdg](<https://github.com/rubyworks/xdg>)（弃用，已废弃）

Rust
    [directories-rs](<https://codeberg.org/dirs/directories-rs>)
    [rust-xdg](<https://github.com/whitequark/rust-xdg>)

Swift
    [swift-xdg](<https://github.com/Frizlab/swift-xdg>)

Vala
    通过 [GLib.Environment](<https://valadoc.org/#!api=glib-2.0/GLib.Environment>) 提供内置支持。
    参见 `get_user_cache_dir`、`get_user_data_dir`、`get_user_config_dir` 等。

##  提示与技巧

###  隐藏不需要的目录

对于无法重新定位的目录，某些桌面环境（例如 [KDE](<../zh-cn/KDE.html> "KDE")）允许您隐藏它们： 
    
    $ echo _path_ >> ~/.hidden
    
`_path_` 是文件/目录的路径，相对于 `.hidden` 的父目录。 

##  参见

  * [GNOME Goal: XDG Base Directory Specification Usage](<https://wiki.gnome.org/Initiatives/GnomeGoals/XDGConfigFolders>)
  * [Rob Pike: "Dotfiles" being hidden is a UNIXv2 mistake](<https://web.archive.org/web/20180827160401/plus.google.com/+RobPikeTheHuman/posts/R58WgWwN9jp>)。
  * [systemd-path(1)](<https://man.archlinux.org/man/systemd-path.1>)
  * [file-hierarchy(7)](<https://man.archlinux.org/man/file-hierarchy.7>)
  * [Grawity 关于点文件的注释](<https://github.com/grawity/dotfiles/blob/master/.dotfiles.notes>)。
  * [Grawity 关于环境变量的注释](<https://github.com/grawity/dotfiles/blob/master/.environ.notes>)。
  * [ploum.net: Modify Your Application to use XDG Folders](<https://ploum.net/207-modify-your-application-to-use-xdg-folders/>)。
  * [PCGamingWiki](<https://pcgamingwiki.com/wiki/Home>) 试图记录 Linux PC 游戏是否遵循 XDG 基本目录规范。
