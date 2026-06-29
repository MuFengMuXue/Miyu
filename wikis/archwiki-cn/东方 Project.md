**翻译状态：**

  * 本文（或部分内容）译自 [Touhou](<https://wiki.archlinux.org/title/Touhou> "arch:Touhou")，最近一次同步于 2025-01-16，若英文版本有所[更改](<https://wiki.archlinux.org/title/Touhou?diff=0&oldid=808668>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Touhou_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[东方Project](<https://zh.wikipedia.org/wiki/%E6%9D%B1%E6%96%B9Project> "zhwp:东方Project") 是一种[弹幕游戏](<https://baike.baidu.com/item/%E5%BC%B9%E5%B9%95%E5%B0%84%E5%87%BB%E6%B8%B8%E6%88%8F/8682817?fr=aladdin>)(在西方又被叫做 "bullet-hell shooters") 

东方Project (Touhou Project) 是一个弹幕类游戏系列的合称。 弹幕类游戏是一种2D射击类游戏，大多由美丽且难度极大的弹幕组成。 东方Project作为现在最多同人作品的射击游戏，现在已经渗透到各个领域，比如说Linux这个与任何一款Windows游戏八杆子打不着的地方… 

虽然东方Project系列的原作游戏难度较大，但同时也是一个让人上瘾的游戏。 

本页的目标是帮助Arch Linux用户安装东方本作及其它与东方相关的包。 

##  安装

PC-98上的游戏可以使用 Linux-native X Neko Project II emulator ([xnp2](<https://aur.archlinux.org/packages/xnp2/>)AUR)来运行。 

以下的AUR包都需要[Wine](<../zh-cn/Wine.html> "Wine")来运行(以及[Timidity++](<../zh-cn/Timidity++.html> "Timidity++")来播放MIDI音乐).有一个基于python的引擎正在开发中，并会用来代替wine。在AUR中的游戏都是免费试用版。你可以简单的用完整版把试用版换掉（如果你有完整版的话）。 

下面是已经在AUR中打包好的软件包： 

  * th6:东方红魔乡 〜 the Embodiment of Scarlet Devil.——[th06-demo-wine](<https://aur.archlinux.org/packages/th06-demo-wine/>)AUR 或 [th06-demo-pytouhou](<https://aur.archlinux.org/packages/th06-demo-pytouhou/>)AUR
  * th7:东方妖妖梦 〜 Perfect Cherry Blossom.——[th07](<https://aur.archlinux.org/packages/th07/>)AUR
  * th8:东方永夜抄 〜 Imperishable Night.——[th08](<https://aur.archlinux.org/packages/th08/>)AUR

我们需要帮助[打包](</wzh/index.php?title=Wine_PKGBUILD_Guidelines&action=edit&redlink=1> "Wine PKGBUILD Guidelines（页面不存在）")更多的东方游戏到[AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR")中。以下是一些尚未打包到AUR中，但有免费版放出，需要有人进行打包的： 

  * th7.5:东方萃梦想 〜 Immaterial and Missing Power
  * th9:东方花映冢 〜 Phantasmagoria of Flower View
  * th10:东方风神录 〜 Mountain of Faith
  * th10.5:东方绯想天 〜 Scarlet Weather Rhapsody
  * th11:东方地灵殿 〜 Subterranean Animism
  * th12:东方星莲船 〜 Undefined Fantastic Object
  * th13:东方神灵庙 〜 Ten Desires
  * th13.5:东方心绮楼 〜 Hopeless Masquerade.
  * th14:东方辉针城 〜 Double Dealing Character
  * th14.5:东方深秘录 〜 Urban Legend in Limbo
  * th15:东方绀珠传 〜 Legacy of Lunatic Kingdom
  * th15.5:东方凭依华 〜 Antinomy of Common Flowers
  * th16:东方天空璋 〜 Hidden Star in Four Seasons
  * th17:东方鬼形兽 〜 Wily Beast and Weakest Creature
  * th18:东方虹龙洞 〜 Unconnected Marketeers

###  Python引擎

[Linkmauve](<https://linkmauve.fr/doc/touhou/>) 制作了一个实验性质的基于python的游戏引擎。现在这个引擎还不稳定， 和正式作比起来更像是一个目标。参考 [pytouhou-hg](<https://aur.archlinux.org/packages/pytouhou-hg/>)AUR 和 [th06-demo-data](<https://aur.archlinux.org/packages/th06-demo-data/>)AUR。 

##  其它信息

###  安装完整版游戏

如果你有永夜抄或者妖妖梦的完整版的话，你可以放到你的主文件夹或者overlay里。这样就能在liveCD/磁盘里安装了。 

**注意：**`.th08` 是东方永夜抄的 wineprefix 文件夹，而`.th07` 东方妖妖梦的文件夹。

  1. 找到完整游戏的文件夹
  2. 在主文件夹(/home)下查看隐藏文件并找到“.th08”和“.th07”这2个文件夹
  3. 把完整游戏文件复制到隐藏文件(“.th08”和“.th07”)
  4. 运行游戏

###  MIDI 音源

试用版只提供MIDI文件，所以你需要安装 [timidity++](<https://archlinux.org/packages/?name=timidity%2B%2B>)包 和一些音源 ([freepats-general-midi](<https://archlinux.org/packages/?name=freepats-general-midi>)包)。 

然后再把下面几行加入 Timidity++ 的配置文件中去： 
    
    /etc/timidity++/timidity.cfg
    
    dir /usr/share/timidity/freepats
    source /etc/timidity++/freepats/freepats.cfg
    
请记住要在玩游戏之前[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动") `timidity.service` [用户单元](<../zh-cn/Systemd/%E7%94%A8%E6%88%B7.html> "用户单元")。 

###  Windows时代游戏中的音频

如果你发现你在任何Windows时代或以后的游戏(>=th06)没有音频，请确保安装[lib32-alsa-lib](<https://archlinux.org/packages/?name=lib32-alsa-lib>)包和[lib32-alsa-plugins](<https://archlinux.org/packages/?name=lib32-alsa-plugins>)包，并重新检查你的配置（在winecfg）。此外，设置游戏中的音频为“WAV”模式。 

##  Steam版本

你可以在[这个列表](<https://store.steampowered.com/curator/42231740-Touhou-Official-Games-Info/list/93128>)中找到Steam上可用的东方游戏。 

### thcrap

[Touhou Community Reliant Automatic Patcher](<https://www.thpatch.net/>) (thcrap) 主要用于促进[东方Project](<https://en.wikipedia.org/wiki/Touhou_Project> "wikipedia:Touhou Project")游戏的自更新、多语言翻译，在[Touhou Patch Center](<https://thpatch.net/>)上，但理论上可以用于这些游戏的任何其他补丁，而不需要通过该网站。 

使用thcrap启动东方游戏的最简单方法是使用[thcrap-steam-proton-wrapper](<https://github.com/tactikauan/thcrap-steam-proton-wrapper>)脚本。 

  * 从Steam下载你购买的游戏。

  * [安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [thcrap-steam-proton-wrapper-git](<https://aur.archlinux.org/packages/thcrap-steam-proton-wrapper-git/>)AUR。对于[Flatpak](<../zh-cn/Flatpak.html> "Flatpak")版本的Steam，请从 _Flathub_ 安装`com.valvesoftware.Steam.Utility.thcrap_steam_proton_wrapper`。
  * 更改你的东方游戏启动选项。右键点击Steam库中的东方游戏，然后点击 _属性_ 。在 _常规_ 选项卡下，更改 _启动选项_ 为

    thcrap_proton -c _en.js_ -- %command%
    
查看[手册](<https://github.com/tactikauan/thcrap-steam-proton-wrapper>)以使用其他语言启动东方游戏。 

  * 第一次启动游戏时，它会要求你安装thcrap。
  * 之后，它会更新thcrap并启动游戏。当thcrap窗口出现时，建议你在设置中取消选中 _在后台保持更新程序运行_ ，以便在你退出时Steam可以正确关闭游戏。

### thprac

[thprac](<https://github.com/touhouworldcup/thprac>) 是一个练习工具。添加`-p`选项将安装并使用thprac启动东方游戏。 
    
    thcrap_proton -p -c en.js -- %command%
    
### vpatch

**注意：** Vsync Patches (vpatch) 仅适用于原始磁盘中的可执行文件。你需要一个来自原始磁盘的`.exe`文件，而不是Steam版本。参见[这个](<https://en.touhouwiki.net/wiki/Purchasing_Guide>)购买指南。

Vsync补丁减少了输入延迟（按下按钮时游戏响应更快）。 

  * 从[touhouwiki](<https://en.touhouwiki.net/wiki/Game_Tools_and_Modifications#Vsync_Patches>)下载补丁。

  * 将`vpatch.exe`、`vpatch.ini`和`vpatch_thxx.dll`复制到你的游戏目录`~/.local/share/Steam/steamapps/common/thxx/`（或`~/.var/app/com.valvesoftware.Steam/data/Steam/steamapps/common/thxx/`对于Flatpak版本的Steam）。

  * 使用你喜欢的文本编辑器打开游戏目录中的`vpatch.ini`。我们将更改窗口大小。对于TH10，默认窗口非常小。首先，在`[Window]`部分下设置`enabled = 1`。如果使用4K显示器，设置 _Width = 2667_ 和 _Height = 2000_ 。如果使用1080p显示器，设置 _Width = 1280_ 和 _Height = 960_ 。基于[这个](<https://steamcommunity.com/sharedfiles/filedetails/?id=2196860604>)教程。要修复Th10 Marisa B 3.xx的功率错误，请在`[Option]`部分添加`BugFixTh10Power3 = 1`。

  * 备份原始的Steam可执行文件`~/.local/share/Steam/steamapps/common/thxx/thxx.exe`。这是为了方便，你总是可以使用Steam中的 _验证本地文件_ 来恢复它。

  * 将`~/.local/share/Steam/steamapps/common/thxx/thxx.exe`替换为你从原始磁盘合法获得的文件。

  * 将Steam游戏启动选项更改为

    thcrap_proton -v -c en.js -- %command%
    
     `-v`标志让Steam运行`vpatch.exe`。

##  相关链接

  * [THBwiki上的东方Project](<https://thwiki.cc/%E6%9D%B1%E6%96%B9Project>)
  * [萌娘百科上的东方Project](<https://zh.moegirl.org.cn/%E4%B8%9C%E6%96%B9Project>)
  * [维基百科上的东方Project](<https://zh.wikipedia.org/wiki/%E4%B8%9C%E6%96%B9Project> "zhwp:东方Project")
  * [东方Project在LINUX运行](<https://zh.touhouwiki.net/wiki/%E4%BA%8ELinux%E8%BF%90%E8%A1%8C>)
  * [在Linux和MacOS X上运行东方游戏](<https://en.touhouwiki.net/wiki/Running_in_Linux_and_MacOS_X>)
  * [Wine PKGBUILD Guidelines](</wzh/index.php?title=Wine_PKGBUILD_Guidelines&action=edit&redlink=1> "Wine PKGBUILD Guidelines（页面不存在）")
  * [如何在Steam Deck上使用thcrap（Touhou Community Reliant Automatic Patcher）](<https://www.reddit.com/r/touhou/comments/yypp3q/how_to_use_thcrap_touhou_community_reliant/>)
  * [[WIN/LINUX] 使用ThCRAP的英文补丁，加上V-Sync补丁，全部在Steam内完成](<https://steamcommunity.com/sharedfiles/filedetails/?id=2196860604>)
