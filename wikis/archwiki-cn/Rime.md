**翻译状态：**

  * 本文（或部分内容）译自 [Rime](<https://wiki.archlinux.org/title/Rime> "arch:Rime")，最近一次同步于 2025-02-18，若英文版本有所[更改](<https://wiki.archlinux.org/title/Rime?diff=0&oldid=827237>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Rime_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

**[Rime](<https://rime.im>)** （中州韵输入法引擎）是一款支持多种输入方案的输入法引擎。 

Rime 本身没有用于处理用户输入的前端，需要配合输入法框架才能使用，比如 [Fcitx5](<../zh-cn/Fcitx_5.html> "Fcitx5") 或 [IBus](<../zh-cn/IBus.html> "IBus")。 

**注意：**[Fcitx5](<../zh-cn/Fcitx_5.html> "Fcitx5") 和 [Fcitx](<../zh-cn/Fcitx.html> "Fcitx") 是两个不同的软件包。Fcitx 处于维护模式，建议使用 Fcitx5。自 2021 年以来，[fcitx-im](<https://fcitx-im.org/>) 的官方页面已指向 Fcitx5。由于官方软件包尚未重命名以反映这一变化，请特别注意。

##  安装

分别安装提供 Rime 输入引擎的 [librime](<https://archlinux.org/packages/?name=librime>)包 和所使用输入法对应的集成： 

  * 若使用 [Fcitx5](<../zh-cn/Fcitx_5.html> "Fcitx5") ，安装 [fcitx5-rime](<https://archlinux.org/packages/?name=fcitx5-rime>)包；
  * 若使用 [Fcitx](<../zh-cn/Fcitx.html> "Fcitx") ，安装 [fcitx-rime](<https://archlinux.org/packages/?name=fcitx-rime>)包；
  * 若使用 [IBus](<../zh-cn/IBus.html> "IBus") ，安装 [ibus-rime](<https://archlinux.org/packages/?name=ibus-rime>)包。

##  配置

Rime 需要输入方案才能工作，用户可以定制输入方案。默认情况下，一些方案随着 [librime-data](<https://archlinux.org/packages/?name=librime-data>)包 元软件包一起安装，因为它是 [librime](<https://archlinux.org/packages/?name=librime>)包 的依赖项。 

另外，在软件仓库中有几个可用的官方输入方案： 

  * [rime-luna-pinyin](<https://archlinux.org/packages/?name=rime-luna-pinyin>)包 \- 朙月拼音
  * [rime-terra-pinyin](<https://archlinux.org/packages/?name=rime-terra-pinyin>)包 \- 地球拼音
  * [rime-double-pinyin](<https://archlinux.org/packages/?name=rime-double-pinyin>)包 \- 基于朙月拼音的双拼输入，包含自然码、MSPY、智能 ABC、小鹤双拼、拼音加加等
  * [rime-pinyin-simp](<https://archlinux.org/packages/?name=rime-pinyin-simp>)包 \- 袖珍简化字拼音
  * [rime-cantonese](<https://archlinux.org/packages/?name=rime-cantonese>)包 \- 粤语拼音
  * [rime-cangjie](<https://archlinux.org/packages/?name=rime-cangjie>)包 \- 仓颉五代
  * [rime-quick](<https://archlinux.org/packages/?name=rime-quick>)包 \- 速成
  * [rime-stroke](<https://archlinux.org/packages/?name=rime-stroke>)包 \- 五笔画（笔画输入法）
  * [rime-wubi](<https://archlinux.org/packages/?name=rime-wubi>)包 \- 五笔字型86
  * [rime-wugniu](<https://archlinux.org/packages/?name=rime-wugniu>)包 \- 上海吴语
  * [rime-bopomofo](<https://archlinux.org/packages/?name=rime-bopomofo>)包 \- 注音
  * [rime-emoji](<https://archlinux.org/packages/?name=rime-emoji>)包 \- Emoji 表情符号输入
  * [rime-flypy](<https://aur.archlinux.org/packages/rime-flypy/>)AUR \- 小鹤音形
  * [rime-ice-git](<https://aur.archlinux.org/packages/rime-ice-git/>)AUR 或 [rime-ice-git](<https://github.com/archlinuxcn/repo/tree/master/archlinuxcn/rime-ice-git>)[CNRepo](<../zh-cn/Arch_Linux_%E4%B8%AD%E6%96%87%E7%A4%BE%E5%8C%BA%E4%BB%93%E5%BA%93.html> "Arch Linux 中文社区仓库") \- [雾凇拼音](<https://github.com/iDvel/rime-ice>), 自带大词库和其他智能功能

一些软件包提供不止一种输入方案，如 [rime-luna-pinyin](<https://archlinux.org/packages/?name=rime-luna-pinyin>)包 就提供了包括 `luna_pinyin` 和 `luna_pinyin_fluency` 在内的五种输入方案。 

使用 Rime 时，默认可以按 `F4` 或 `Ctrl+`` 切换输入法，详见[#选择输入方案](<#%E9%80%89%E6%8B%A9%E8%BE%93%E5%85%A5%E6%96%B9%E6%A1%88>)。 

###  配置目录

若要自定义 Rime，请先根据使用的输入法创建 Rime 的配置文件夹： 

若使用 [ibus-rime](<https://archlinux.org/packages/?name=ibus-rime>)包： 
    
    $ mkdir ~/.config/ibus/rime
    
若使用 [fcitx-rime](<https://archlinux.org/packages/?name=fcitx-rime>)包： 
    
    $ mkdir ~/.config/fcitx/rime/
    
若使用 [fcitx5-rime](<https://archlinux.org/packages/?name=fcitx5-rime>)包： 
    
    $ mkdir ~/.local/share/fcitx5/rime/
    
在文件夹中创建 `default.custom.yaml` 文件，以指定可选的输入法。例如，若要按声调输入拼音，添加下列内容以使用地球拼音： 
    
    default.custom.yaml
    
    patch:
      schema_list:
        - schema: terra_pinyin
    
添加内容时请注意行首缩进。此文件会覆盖默认的配置文件，若只在文件中添加地球拼音，则只能用地球拼音。 

###  应用配置

请重新部署输入法以使自定义生效。如果使用图形界面的 IBus 或 Fcitx，请点击 ⟲（重新部署）按钮。也可以使用命令行重新部署： 

若使用 [ibus-rime](<https://archlinux.org/packages/?name=ibus-rime>)包： 
    
    $ rm ~/.config/ibus/rime/default.yaml && ibus-daemon -drx
    
若使用 [fcitx-rime](<https://archlinux.org/packages/?name=fcitx-rime>)包： 
    
    $ rm ~/.config/fcitx/rime/default.yaml && fcitx-remote -r
    
若使用 [fcitx5-rime](<https://archlinux.org/packages/?name=fcitx5-rime>)包: 
    
    $ rm ~/.local/share/fcitx5/rime/default.yaml && fcitx5-remote -r
    
###  声调过滤

注意：可以选择声调以过滤候选列表，对应按键如下： 
    
    一声： -
    二声： /
    三声： <
    四声： \
    
例如，若要打出拼音为 `hǎo` 的字，输入 `hao<` 即可。 

###  候选项个数

Rime 默认只会列出 5 个候选项，可以修改 `"menu/page_size"` 的值以改变列出候选项的数量： 
    
    default.custom.yaml
    
    patch:
         "menu/page_size": 9
    
##  使用

###  选择输入方案

使用 Rime 时，默认可以按 `F4` 或 `Ctrl+`` 调整基础设置。显示的设置项如下： 
    
    1.　 _输入法名称_
    2. 中文　－›　西文
    3. 全角　－›　半角
    4. 漢字　－›　汉字
    ...
    
第一项会显示输入方案的名称，可以在其中切换已启用的不同输入方案。 

第二项可以切换中文/英文输入。 

第三项可以切换全角/半角标点。 

第四项可以切换简体/繁体输入。 

其他选项取决于当前使用的输入方案。 

###  自定义输入方案

通过覆盖某一输入方案的默认选项，可以不用每次打开菜单。 

这需要创建一个 `custom` 文件（定制文件）来覆盖 `scheme` 文件（方案定义）中的选项。 

####  例子

下文以更改地球拼音的默认选项从“繁体中文”到“简体中文”为例。 

该输入方案由 [rime-terra-pinyin](<https://archlinux.org/packages/?name=rime-terra-pinyin>)包 在 `/usr/share/rime-data/build/terra_pinyin.schema.yaml` 提供。 

根据输入方案定义里的 `switches` 段： 
    
    switches:
      - name: ascii_mode
        reset: 0
        states: ["中文", "西文"]
      - name: full_shape
        states: ["半角", "全角"]
      - name: simplification
        states: ["汉字", ]
      - name: ascii_punct
        states: ["。，", "．，"]
    
这一段是地球拼音所提供的选项菜单（由 `F4` 或者 `Ctrl+`` 打开）。对于不同的输入方案，配置文件可能会有所不同。 

在 Rime 的 [#配置目录](<#%E9%85%8D%E7%BD%AE%E7%9B%AE%E5%BD%95>)中，创建地球拼音的定制文件： 
    
    terra_pinyin.custom.yaml
    
    patch:
      switches:
        - name: simplification
          reset: 1
    
`name` 项匹配方案定义中的 `switches` 列表的对应选项。 `reset: 1` 指 Rime 总是会重设该项为第二个选项 (下标 1，即 `"汉字"`). 

[#应用配置](<#%E5%BA%94%E7%94%A8%E9%85%8D%E7%BD%AE>)以加载定制文件。 

Rime 提供了多种通过 YAML 来进行此类自定义的方法，更多案例可在 [#进阶内容](<#%E8%BF%9B%E9%98%B6%E5%86%85%E5%AE%B9>)查看。 

###  中文标点

按下列各键输入不同的符号： 
    
    [ -> 「　【　〔　［
    ] ->　」　】　〕　］
    { ->　『　〖　｛
    } ->　』　〗　｝
    < ->　《　〈　«　‹
    > ->　》　〉　»　›
    @ ->　＠　@　☯
    / ->　／　/　÷
    * ->　＊　*　・　×　※
    % ->　％　%　°　℃
    $ ->　￥　$　€　£　¥
    | ->　・　｜　|　§　¦
    _ -> ——
    \ ->　、　＼　\
    ^ ->　……
    ~ ->　〜　~　～　〰
    
###  进阶内容

若要查看详细的 Rime 定制指南，见 <https://github.com/rime/home/wiki/CustomizationGuide> 。 

##  疑难解答

###  GNOME 环境下，ibus-setup 无法更改候选方向

见 [issue #52](<https://github.com/rime/ibus-rime/issues/52>)。 创建 `~/.config/ibus/rime/build/ibus_rime.yaml` 并写入以下内容: 
    
    style:
      horizontal: true
    
##  技巧

###  输入希腊字母

若想输入希腊字母，请在 `luna_pinyin.custom.yaml` 或自定义输入方案文件中追加以下内容： 
    
    luna_pinyin.custom.yaml
    
    recognizer:
      patterns:
        # Use / as the identifier here
        # You can freely replace your favorite identifiers (such as: `~, .\; etc., characters that need not be displayed directly on the screen)
        # Replace the / before the Greek letter at the same time
        punct: "^/([0-9]0?|[A-Za-z]+)$"
    punctuator:
      symbols:
        # Here, the letter name is used as the code of the Greek letter, and you can replace it with your favorite code as needed.
        # For example, if you want to use a as the alpha code
        # just replace the alpha below with a
        "/alpha": ["Α", "α"]
        "/beta": ["Β", "β"]
        "/gamma": ["Γ", "γ"]
        "/delta": ["Δ", "δ"]
        "/epsilon": ["Ε", "ε"]
        "/zeta": ["Ζ", "ζ"]
        "/eta": ["Η", "η"]
        "/theta": ["Θ", "θ"]
        "/iota": ["Ι", "ι"]
        "/kappa": ["Κ", "κ"]
        "/lambda": ["Λ", "λ"]
        "/mu": ["Μ", "μ"]
        "/nu": ["Ν", "ν"]
        "/xi": ["Ξ", "ξ"]
        "/omicron": ["Ο", "ο"]
        "/pi": ["Π", "π"]
        "/rho": ["Ρ","ρ"]
        "/sigma": ["Σ", "σ", "ς"]
        "/tau": ["Τ", "τ"]
        "/upsilon": ["Υ", "υ"]
        "/phi": ["Φ", "φ"]
        "/chi": ["Χ", "χ"]
        "/psi": ["Ψ", "ψ"]
        "/omega": ["Ω", "ω"]
    
在此输入配置下，输入 `/alpha` 即会出现候选词 `α` 。 

##  参见

  * [官方网站](<https://rime.im/>)
  * [GitHub wiki](<https://github.com/rime/home/wiki>)
