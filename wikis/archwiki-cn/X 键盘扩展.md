[![](../File:Tango-preferences-desktop-locale-modified.png)](<../File:Tango-preferences-desktop-locale-modified.png>)**这篇文章或章节的[翻译](<../Project:%E8%B4%A1%E7%8C%AE.html#Translating> "Project:Contributing")质量不佳。**

**原因：** 请提供模板的第一个位置参数以概括原因。（在 [Talk:X 键盘扩展#](<../zh-cn/Talk:X_%E9%94%AE%E7%9B%98%E6%89%A9%E5%B1%95.html>) 中讨论）

这个 [X keyboard extension](<https://en.wikipedia.org/wiki/X_keyboard_extension> "wikipedia:X keyboard extension"), or XKB, 定义在X视窗中键盘码被处理的方法，且提供访问内部转译表。他是在X中允许使用多重键盘规划的基本机制。 

这篇文章描述如何修改与创建键盘布局。如果你正查找如何设置你的键盘，看[Xorg/Keyboard configuration](</wzh/index.php?title=Xorg/Keyboard_configuration&action=edit&redlink=1> "Xorg/Keyboard configuration（页面不存在）")

##  预防措施与准备 Precautions and preparations

在X session连线中运用XKB关闭某些键盘上的按键很简单。先确定你有办法不使用你的键盘下终止X连线。 

尽管几率低，改变XKB设置可能挂起或损害X服务器。确定你可以处理他。有某些方法去执行 killall X 或远程重引导会是好主意。 

停止 [xxkb](<https://archlinux.org/packages/?name=xxkb>)包 或任何规划切换程序。 xxkb积极的改变XKB状态，调试两者于同时非好主意。 

##  获得并设置XKB规划

###  使用 rules 文件夹规则资料

看着 `/usr/share/X11/xkb/rules/` 里面的`*.lst`文件或[XKB Homepage](<https://www.x.org/wiki/XKB/>)以获得怎么设置rules档的想法。你自定的设置可以可以运行在`/etc/X11/xorg.conf.d/`。 

例如有可能想重新规划他的 `Caps Lock` 到 `Escape`键: 
    
    90-custom-kbd.conf
    
    Section "InputClass"
        Identifier "keyboard defaults"
        MatchIsKeyboard "on"
    
        Option "XKbOptions" "caps:escape"
    EndSection
    
###  使用按键规划

使用 [xkbcomp(1)](<https://man.archlinux.org/man/xkbcomp.1>) (package [xorg-xkbcomp](<https://archlinux.org/packages/?name=xorg-xkbcomp>)包) 去处理XKB资料。要获得目前的设置，执行 
    
       xkbcomp $DISPLAY output.xkb
    
要上传资料回服务器，执行 
    
       xkbcomp input.xkb $DISPLAY
    
注意下没有`$DISPLAY`参数时xkbcomp将试着去编译.xkb文件进入.xkm档(多数项目没用)，而没有上传任何东西到服务器上。但是这将会检查语法及回报错误。 

一旦布局完成，存文件成 `~/.Xkeymap` 并让 `~/.xinitrc` 在启动时读取他: 
    
       test -f ~/.Xkeymap && xkbcomp ~/.Xkeymap $DISPLAY
    
实际文件名称不重要。注意下不像系统范围的设置会经由`xorg.conf`，这是每位用户按键规划。 还有，当X在运行时改变XKB设置也没问题。 

##  XKB 基本消息

XKB核心是有些单纯，但必须有某些概念他如何运作才开始动手按键规划。 

###  工具与定值

使用[xev](<../zh-cn/%E9%94%AE%E7%9B%98%E8%BE%93%E5%85%A5.html#%E5%9C%A8_Xorg_%E4%B8%AD%E8%AF%86%E5%88%AB%E2%80%9C%E9%94%AE%E7%A0%81%E2%80%9D> "Xev") (package [xorg-xev](<https://archlinux.org/packages/?name=xorg-xev>)包) 去获得keycodes且去检查你的按键规划运作。 
    
    $ xev -event keyboard
    
       KeyPress event, serial 45, synthetic NO, window 0x2200001,
           root 0xad, subw 0x0, time 183176240, (796,109), root:(867,413),
           state 0x1, keycode 21 (keysym 0x2b, plus), same_screen YES,
           XLookupString gives 1 bytes: (2b) "+"
           XmbLookupString gives 1 bytes: (2b) "+"
           XFilterEvent returns: False
    
注意键码21 keycode 21，状态值(state) 0x1 与 按键象征(keysym) 0x2b 又叫 plus 加号。keycode 21 是输入设备提供给 X 的，通常为某种排序的实体按键索引值。 状态值(state) 表示修饰键(modifier keys)，0x01是Shift键。 X随状态值一起送键码给应用程序，以[XKeyEvent(3)](<https://man.archlinux.org/man/XKeyEvent.3>)架构。 按键象征与相对应字符串乃从属端程序[XLookupString(3)](<https://man.archlinux.org/man/XLookupString.3>)使用及随附。 

在状态字段这些比特有预定义名称: `Shift`, `Lock`, `Control`, `Mod1`, `Mod2`, `Mod3`, `Mod4` and `Mod5`, 由低至高。 由此，`Ctrl+Shift`为 0x05，其余如此。(罗技k120键盘 状态值 0x11 Shift按下, 0x14 Control按下, 0x15 `Ctrl+Shift 按下`, 0x18 `Alt 按下`, 0x19 `Alt+ Shift 按下`, 0x1c `Alt+Ctrl 按下`, 0x1d `Ctrl+Alt+Shift 按下`)。从属端应用程序通常仅检查他们需要的比特，故应用程序以一般键盘输入时，`Ctrl+按键`的快捷键键通常没有区别于状态值 `Control` 和 `Control+Mod3`。 

按键象征也是数值型，他们多数有名字，声明于 `/usr/include/X11/keysymdef.h` 随着 `KP_` 前缀。然而，那数值是从属端实际接收。按键象征唯当应用程序预期特定值才重要; 一般就像这些按键 方向键、输入键、退格键、F开头功能键(F1~Fxx)、及各式热键。对其他的按键，特定字符串被使用。 

###  键码转译

XKB通常工作在XLookupString阶段，根据他的内部状态转换输入键码(keycode)成按键象征(keysym)，也就是组群(group)及状态(state)值: 
    
       (keycode, group, state) → keysym
    
组群通常代表"规划布局"， 如同 美式-英文布局 US-English, 法式-AZERTY布局 French-AZERTY, 俄罗斯 Russian, 希腊 Greek 等等。 最多可以有4组群。 

内部中，转译涉及额外步骤： 
    
       (keycode [, group]) → type
       (state, type) → level
       (keycode, group, level) → S[keycode][group][level]
    
随着 `S` 的是转译表 (实际上叫做 `xkb_symbols`, 参考以下叙述). 

类别Type被用来告知哪个修饰键影响哪个按键；特别在这是个方法来减少设置按键 `S` 的第三位阶。 例如，典型的字母数字键仅仅被 `Shift` 影响，所以他的类别被设为 `TWO_LEVEL`，且 
    
       (state, TWO_LEVEL) → level = ((state >> 0) & 0x01) = state & 0x01
    
level为0或1其中之一。因此会是`S[keycode][0..4][0..1]` 而不是 `S[keycode][0..4][0..256]`

###  按键象征与状态值

在X术语中，`a`与`Ctrl+a`意为同样按键象征但不同状态，不过`a` 与 `A`为不同按键象征。 

通常这是XKB调度提供不同按键象征，可是状态值随后被个别应用程序处理。 

同样，状态值在XKB中有些延迟作用，也因此，你必须让 状态值设置优先权给按下但按键 

示例: `Ctrl+h` 可以设置成像 backspace 在 [rxvt](</wzh/index.php?title=Rxvt&action=edit&redlink=1> "Rxvt（页面不存在）") 中(应用程序中设置)。这设置法下 rxvt 将收到按键象征 `h` 及 `Control` 字节以状态值形式，且这值将明显不同于 `Backspace` 的按键象征。或者，XKB可以被用于 `Ctrl+h` 结合产生 `Backspace` 按键象征，以 `Control` 字节；在这案例中， rxwt将看不到任何差异在实体 `Backspace`键及 `h` 与`Ctrl`一起按下时。 使 `Ctrl+h` 组合键产生 `Backspace` 按键象征却没有`Control`字节是XKB的任务，但想实现 `Control+Backspace` 很困难。 

###  触发动作 Actions

按键象征从上层表中获得时可以同时触发某些动作: 
    
       (keysym, state) → action
    
对XKB，setting 或 locking一个修饰键就是一个触发动作，且这亦是任何X服务器中交互 好比切换控制台、中断服务器、移动游标等等。触发动作通常不影响按键象征，且产生按键象征的不是触发动作。 

每个(按键象征 keysym, 按键状态 state)配对只有一个触发动作。 

##  编辑布局设置 Editing the layout

从你的服务器有的任何默认配置文件开始。 只要可以的话，产生一项小变动就马上测试这变动。 

xkbcomp 产生的 .xkb文件为简单文字档。 C++风格注解， // 到一行终止可允许。段落名称--好比在 xkb_keycodes 里的 "name-here" --此处不重要且可以忽略。 

### xkb_keycodes

xkb的键码(keycode)定义。其余的文件不使用数字体键码，只有按键象征按键标签定义于这个段落。 

他是好主意保留这些键码定义。键盘有问题实际上在这里。 

这些按键标签可以随意定。 他们仅用在xkb_symbols 段落。 

### xkb_types

这一段放在xkb_symbols前面，所以先看看，不过先不要产生电动。标准类别依赖许多虚拟修饰键(virtual modifiers)，这些将在后面解释。现在，只要找到你需要的类别。从下列中开始：ONE_LEVEL、 TWO_LEVEL、 ALPHABETIC 。 

ONE_LEVEL 这项值不被修饰键影响；通常他设给 Enter, Space, Escape, F keys, Shift/Alt/Ctrl 键等等。, TWO_LEVEL 与 ALPHABETIC 项值依据 Shift的状态产生不同按键符号。所有字母数字键属于这个类别。ALPHABETIC额外相关于CapsLock。 

类别描述他们自己相当简单。这行 
    
       modifiers= Shift+NumLock+LevelThree;
    
意思是这些键被影响于 按键Shift, NumLock and LevelThree 比特而已。 映射(Map)行像 
    
       map[Shift+LevelThree]= Level4;
    
定义哪个组合键对应哪个位阶值。 程序xkbcomp复制默认值时使用"LevelN"，但简短又方便的"N"也可以用。 

level_name那行不太影响且可以忽略。 

### xkb_compatibility

在所有设置之中 触发动作定义(`interpret`)与键盘上led (`indicator`)。你可以移除资料你没有的或用不到的，像附加数字键触发、鼠标控制或额外的修饰键。 

注意这 `key+AnyOfOrNone(all)` 跟 `key` 等效，但`key`更容易给人读懂。 

看看组群切换(groups switching)如果有必要的话。如果有N个组群的话 `LockGroup(group=N)` 可以用，不然`ISO_Next_Group`/`ISO_Prev_Group`就够了。`LatchGroup` 对非常规设置很有用。 

### xkb_symbols

主要的段落来定义那个按键做什么。语法： 
    
       key <LABL> { [ G1L1, G1L2, G1L3, ... ], [ G2L1, G2L2, G2L3, ... ], ... }
    
`<LABL>` 是按键标签从 xkb_keycodes 段落来的，`GiLj` 组群i位阶j的按键象征。每个组群的按键象征数目必须配合哪个类别的位阶数目定义(`xkbcomp` 将警告你如果项目不存在) 

查看 `/usr/include/X11/keysymdef.h` 可能的按键象征清单。 撇开这些清单，你也可以用 `Unnnn` 给 Unicode 符号加上十六比特码 nnnn, 例如： `U0301` 给组合符号 重音符号。 注意 `a` 与 `U0061` 视为不同地 (目前, 多数应用程序期待 `Ctrl+a`, 不是 `Ctrl+U0061` 因为他们的数字值不一样。) 

按键类别也在这指定，其中像 
    
       key.type = "T1";
       key <...> { ... };
       key <...> { ... };
       key <...> { ... };
       key.type = "T2";
       key <...> { ... };
       key <...> { ... };
    
或单独设给每一个按键: 
    
       key <...> { type = "T", [ .... ], [ .... ] };
    
按键类别可能在不同组群不一样。这很反直觉，但实际上也有很方便的应用。要设置个别组群类别，用这个： 
    
       key <...> { type[1] = "T1", type[2] = "T2", [ ... ], [ ... ] };
    
你可以设置标签让组群使用 
    
       name[1] = "EN";     // group 1
       name[2] = "RU";     // group 2
       name[3] = "UA";     // group 3
    
如果标签在这里启用，xxkb 将显示他。 is what xxkb will show if labels are enabled there. 

这一段落也包含 `modifier_map` 行。 目前先留着这行，或跳去看看后面的虚拟修饰键(Virtual Modifiers)。 

###  xkb_geometry 键盘位置构造

完全不重要的章节描述键盘按键位置构造。可以删除没有任何后果。 

##  基本示例 Basic examples

首先查看你的现存规划档，他很可能包含给许多常见按键的标准定义。 

通过这文字(text) -> "xkb_keycodes { text }" 表示 "text" 应该被加入 xkb_keycodes 段落里。 无论何时，由上下文很清楚地，段落名称被省略了。 (从.xkb档可看到 xkb_keycodes "evdev+aliases(qwerty)" { blabla~ }，引用文件/usr/share/xkb/keycode/里面的 文件evdev 跟 文件aliases 里面段落qwerty 那一段内容) 

###  简易按键分配

启用附加(又叫多媒体)按键: 
    
       xkb_keycodes {
           <VOL-> = 122;       // 數值查看xev
           <VOL+> = 123;
       }
    
       xkb_symbols {
           key.type = "ONE_LEVEL";
           key <VOL-> { [ XF86AudioLowerVolume ] };
           key <VOL+> { [ XF86AudioRaiseVolume ] };
       }
    
Escape键设在 CapsLock键, 通常给 Vim 用户: 
    
       key.type = "ONE_LEVEL";
       key <CAPS> { [ Escape ] };
    
交换按键 Ins 跟 PrintScreen (有案例 他们彼此相反——发生在 Dell笔记电脑按键)： 
    
       key.type = "ONE_LEVEL";
       key <IN?>  { [    Print ] };
       key <PRSC> { [   Insert ] };
    
在某些 HP 笔记本电脑按键，上面那段作用。 相反地， the keycodes他们自己需要被定义： 
    
       partial xkb_keycodes "insert" {
           alias <I118> = <IN?>;
           <INS>  = 218;
           <I218> = 118;
       };
    
改变按键 shift 到粘着按键(sticky key)版: 

取代这行 
    
       key <LFSH> {         [         Shift_L ] };
    
用这 
    
       key <LFSH> {         [         ISO_Level2_Latch ] };
    
你应该也需要加入下面设置到`/usr/share/X11/xkb/compat/basic`
    
       interpret ISO_Level2_Latch+AnyOf(all) {
           useModMapMods=level1;
           action= LatchMods(modifiers=Shift,clearLocks,latchToLock);
       };
       interpret ISO_Level2_Latch+AnyOfOrNone(all) {
           action= LatchMods(modifiers=Shift,clearLocks,latchToLock);
       };
    
###  多重布局 Multiple layouts

对一般字母数字按键，只要加入 第二/第三/第四个中括号 [ ] 段落到按键定义: 
    
       key.type = "ALPHABETIC";
       key <AD01> { [ q, Q ], [ a, A ] };      // QWERTY佈局跟AZERTY(法式鍵盤佈局)
    
       key <AC02> { [        s,        S ],        // 多了兩個西里爾字母 cyrillic 的佈局
                    [    U044B,    U042B ],
                    [    U0456,    U0406 ] };
    
布局切换借着设置启动 触动动作(action) LockGroup 完成: 
    
       interpret ISO_Next_Group { action = LockGroup(group=+1); };
       interpret ISO_Prev_Group { action = LockGroup(group=-1); };
    
通常这意味放置 ISO_Next_Group 与 ISO_Prev_Group 按键象征在在恰当的 组群(group)/位阶(level) 位置。 注意包括的组群，所以此设置如果你有两个组群且敲两次按键，你会回归开始的组群。 

西里尔字切换在两个或以上的布局以专用按键RWIN： 
    
       key.type = "ONE_LEVEL";
       key <RWIN> { [ ISO_Next_Group ] }
    
如果你有更多布局且某些按键要节约，可能最好有个专用键设给每个布局。例如给三重布局： 
    
       key.type = "ONE_LEVEL";
       key <RCTL> { [ ISO_Next_Group ],    // g1: switch to g2
                    [ ISO_Prev_Group ],    // g2: switch back to g1
                    [ ISO_Prev_Group ] };  // g3: switch to g2
    
       key <MENU> { [ ISO_Prev_Group ],    // g1: switch to g3
                    [ ISO_Next_Group ],    // g2: switch to g3
                    [ ISO_Next_Group ] };  // g3: switch back to g1
    
有四个布局，你将很可能得用触发动作 ISO_First_Group 与 ISO_Last_Group。 

同样想法可以被实现以仅仅一个按键借着用类型 TWO_LEVEL type: 
    
       key.type = "TWO_LEVEL";
       key <MENU> { [ ISO_Next_Group, ISO_Prev_Group ],
                    [ ISO_Prev_Group, ISO_Next_Group ],
                    [ ISO_Prev_Group, ISO_Next_Group ] };
    
这方法的 Menu键 设给第二个组群 且 Shift-Menu键 设给第三个组群。要使用按键 Ctrl or Alt 而不是Shift，替代 TWO_LEVEL 用 PC_CONTROL_LEVEL2 或 PC_ALT_LEVEL2 对应的类别。 

切换使用两个修饰键(Shift+Shift, Ctrl+Shift 等等) 可借由使用用某些不同于ONE_LEVEL类别给这些按键。 Shift+Shift 示例: 
    
       key.type = "TWO_LEVEL";
       key <LFSH> { [ Shift_L, ISO_Prev_Group ] };
       key <RTSH> { [ Shift_R, ISO_Next_Group ] };
    
要锁住一个组群(也就是切过去；设成只有你按哪个键那一次时), 使用 LatchGroup 触发动作 一般绑定成 ISO_Group_Latch 按键象征: 
    
       key <RCTL> { [ ISO_Group_Latch ] }
    
调整 ISO_Group_Latch 在xkb_compatibility 那一章节的定义 以使用正确组群： 
    
       interpret ISO_Group_Latch { action = LatchGroup(group=3); };
    
检查 /usr/share/X11/xkb/symbols/group 有更多标准示例。 

###  Caps + hjkl 作为 vim风格方向键

[![](../File:Tango-edit-clear.png)](<../File:Tango-edit-clear.png>)**本文或本章节的语言、语法或风格需要改进。参考：[帮助:风格](<../zh-cn/Help:%E9%A3%8E%E6%A0%BC.html> "Help:风格")**

**原因：** The purpose of this section is not clear.（在[Talk:X 键盘扩展](<../zh-cn/Talk:X_%E9%94%AE%E7%9B%98%E6%89%A9%E5%B1%95.html>)讨论）

如果目标键将用在键盘快捷方式上 产生按键规划时有明确的修饰键在按键按下中是最好的。例如，反白文字用基本键盘(`Shift+Left`)、或改变交谈在多数即时通信软件 (`Alt+Down`) 将不会作用，如果有额外`Caps`修饰键送过去时。不过，额外的修饰键必须提交 如果用户重新绑定一个字母键仅把按键象征放在符号哪个段落。重新绑定也附带许可功能就像 AHK(auto hot key)的blind command。 
    
    types 类别段落 (这行定义位阶映射) 必须包含特定项目例如(此例 hjkl四个字母):
    
  * 当没有修饰键按下，按下字母按键的第一位阶的按键象征被提交 (例如hjkl按键的小写字母)。
  * 当单独Shift键被按下，按下字母按键的第二位阶的按键象征被提交 (hjkl的大写字母).
  * 单独当锁定键(Lock)被按下，按下字母按键的第三位阶的按键象征被提交 (此例hjkl对应的方向键)
  * 当 Shift 与 Lock 被按下，按下字母按键的第三位阶的按键象征被使用 (等同 此例 shift+方向键).

加入这个到你的类别段落最底部 
    
     xkb_types "complete" {
       ...
       type "CUST_CAPSLOCK" {
           modifiers= Shift+Lock;
           map[Shift] = Level2;            //映射 shift鍵 且不含 Lock鍵。 Shift+Alt 也作用，因為 Alt 鍵不在上面那行修飾鍵中，。
           map[Lock] = Level3;
           map[Shift+Lock] = Level3;       //映射 shift and Lock鍵. Shift+Lock+Alt 也作用。
           level_name[Level1]= "Base";
           level_name[Level2]= "Shift";
           level_name[Level3]= "Lock";
       };
     };
    
现在来变更caps键设置从 lock (toggle)键动作去设置成 (press) 按住动作，借着在兼容性那一章节所述来修改已经存在的定义 自 LockMods触发动作 改成 SetMods动作: 

(注意这修改意味你不能再像一般方式使用 capslock键) 
    
     xkb_compatibility "complete" {
       ...
       interpret Caps_Lock+AnyOfOrNone(all) {
           action= SetMods(modifiers=Lock);
       };
       ...
     };
    
最后修改你的符号档如下列。 
    
     xkb_symbols "pc_us_inet(evdev)" {
       ...
       key <AC06> {
           type= "CUST_CAPSLOCK",
           symbols[Group1]= [               h,               H,               Left],
           actions[Group1]= [      NoAction(),      NoAction(),   RedirectKey(keycode=<LEFT>, clearmods=Lock) ]
      };
    
###  额外的象征符号

同一按键可输入更多种字。 

####  构成键 Compose key

简单设置且输入一般Unicode字符很有用。 
    
       key <RALT> { [ Multi_key ] };
    
####  位阶3(Level3)

点子类似 Alt键 or AltGr键 以他们原本的意思: 字母数字按键得到额外字符，借着按住某些修饰按键来用。 

首先，设置修饰键。 
    
       xkb_symbols {
           key <LWIN> { [ISO_Level3_Shift ] };
           modifier_map Mod5 { ISO_Level3_Shift };
       }
    
同样，下面这些应该先在相对应段落被定义好，不过如果没有的话就设置： 
    
       xkb_compatibility {
           interpret ISO_Level3_Shift { action= SetMods(modifiers=Mod5); };
       }
    
       xkb_types {
           type "THREE_LEVEL" {
               modifiers= Shift+Mod5;
               map[Shift]= Level2;
               map[Mod5]= Level3;
               map[Shift+Mod5]= Level3;
               level_name[Level1]= "Base";
               level_name[Level2]= "Shift";
               level_name[Level3]= "Level3";
           };
           type "FOUR_LEVEL" {
               modifiers= Shift+LevelThree;
               map[Shift]= Level2;
               map[LevelThree]= Level3;
               map[Shift+LevelThree]= Level4;
               level_name[Level1]= "Base";
               level_name[Level2]= "Shift";
               level_name[Level3]= "Alt Base";
               level_name[Level4]= "Shift Alt";
           };
       }
    
注记下在xkb_compatibility 和 xkb_types 这段的标准定义有 LevelThree 而不是Mod5。不过只要上面的修饰键映射(modifier_map)使用Mod5，没有实际差别，不管怎样最后你将用Mod5比特。 

现在，按键自定义组群，在这个案例的vi风格游标动作: 
    
       key.type = "THREE_LEVEL";
       key <AC06> { [ h, H,  Left ] };
       key <AC07> { [ j, J,  Down ] };
       key <AC08> { [ k, K,    Up ] };
       key <AC09> { [ l, L, Right ] };
    
如你可能用xev得知，这设置产生Mod5+Left键 而不仅仅是 Left键。 但那也可以的 在多数应用程序忽略他们用不到的状态比特情况下。另一个解决方案，看看 覆盖(Overlays)做法如下。 

###  Meta, Super and Hyper 键

####  真正的修饰键 Real modifiers

某些应用程序 (特别是 emacs) 允许有意的使用更高位的状态比特。他通常假定除了Shift, Ctrl 与 Alt 等这些按键控制比特之外， 还有修饰键叫做 Meta, Super 与 Hyper 存在键盘上。 

从 XKB 观点这意味设置 Mod2, Mod3, Mod4 and Mod5 修饰键比特。因为你所要的是按键自己的比特，没有必要去编辑类别，就像之前 Level3 那个例子。 
    
       xkb_compatibility {
           interpret Super_L { action = SetMods(modifiers=Mod3); };
       }
    
       xkb_symbols {
           key <LWIN> { [ Super_L ] };
           modifier_map Mod3 { Super_L };
       }
    
标准定义在 `xkb_compatibility`之中使用 Super修饰键而不是 Mod3 。你也可保持这样，只要确定有`modifier_map`这行。 

留心在 ModN 和已命名的 Super, Hyper 或甚至 Alt等修饰键 没有严格对应关系。唯一广泛使用的 Mod1；某些应用程序叫他 Meta，某些叫他 Alt。至于其他的，查查特定应用程序如何对待状态比特，可看看下述 虚拟修饰键(Virtual modifiers)。 

####  按键象征追踪 Keysym tracking

至少有一种应用程序(openbox) 已知追踪这些 按键按下KeyPress/KeyRelease按键放开时的事件： Meta_[LR], Super_[LR] 和 Hyper_[LR] 等等按键象征，取代依赖状态值的比特。 在这情况下 
    
       xkb_symbols {
           key <LWIN> { [ Super_L ] };
       }
    
已足够且你可以省略用 `interpret` 与 `modifier_map` 行。 

谈到 Openbox，注意他确实允许两种方法: "S-h" 追踪 Super_[LR] 事件 而 "Mod3-h" 检查相关的状态比特。 

##  预先设置档 Preset configuration

XKB 通常借着指定这几项来设置:XkbTypes/XkbCompat/XkbSymbols, or XkbModel/XkbLayout (+XkbVariant/XkbOptions), or XkbKeymap；文件位置一般在/etc/X11/xorg.conf or /etc/X11/xorg.conf.d/*.conf，像这样： 
    
       Option  "XkbModel"    "thinkpad60"
       Option  "XkbLayout"   "us,sk,de"
       Option  "XkbVariant"  "altgr-intl,qwerty,"
       Option  "XkbOptions"  "grp:menu_toggle,grp_led:caps"
    
这些值定义所有XKB映射(这个可以被xkbcomp转存)。事实上，给xkbcomp的等效.xkb文件可以来自 `setxkbmap -print`： 
    
       setxkbmap -model thinkpad60 -layout us,sk,de -variant altgr-intl,qwerty \
           -option -option grp:menu_toggle -option grp_led:caps -print
    
注意下上面的命令终端输出后 include 已经不一样了。每一段落用的文件从相对应的子目录获取 在`/usr/share/X11/xkb`之中，也就是 
    
       xkb_types { include "complete" };
    
代表 xkbcomp 将找 `/usr/share/X11/xkb/types/complete`。 plus符号表示并行相关，所以 
    
       xkb_keycodes { include "evdev+aliases(qwerty)" };
    
代表 
    
       xkb_keycodes {
           include "evdev";
           include "aliases(qwerty)";
       };
    
括号内可从文件选已命名的段落。 查看 `/usr/share/X11/xkb/keycodes/aliases` 并注意 
    
       xkb_keycodes "qwerty" { ... };
    
这是 `aliases(qwerty)` 部分参考处。 最后，冒号转移布局的一部分到另一个组群。 

不像 XkbTypes/XkbCompat/XkbSymbols/XkbGeometry 的值，都直接地相关 .xkb 文件的段落， XkbModel, XkbLayout and XkbRules 参考额外的 non-xkb 文件 可在下面发现 `/usr/share/X11/xkb/rules/` 这个配合 model 与 layout 值去指定符号(symbols) 和 键盘几何构成(geometry)。 XkbKeymap 参考完整的按键规划。引用 Ivan Pascal 记录得到详细叙述。 

就好像用xkbcomp能达到的，这类设置可以马上完成： 用指令 setxkbmap 不带 -print 选项。 

文件 `/usr/share/X11/xkb` 是好示例来源，特别当他涉及标准键盘功能及非平常的XKB实现(例如 keypad/NumLock 处理)。同样，在前阶段时这些文件你必须编辑以推动你的改变。看看 [X Keyboard Config Rules](<https://www.freedesktop.org/wiki/Software/XKeyboardConfig/Rules>) 在编辑文件之前。 

### xmodmap

尽管有时用在结合预先设置， [xmodmap](<../zh-cn/Xmodmap.html> "Xmodmap") 不直接相关于XKB。 这个工具用不同想法 (pre-XKB) 于键盘代码在X中如何被处理；特别是，xmodmap缺少组群与类别的概念，所以尝试每按键超过一个以上按键象征不太很可能工作。 

通常不建议用 xmodmap，或许对很简单工作是例外。 XKB-compatible 等效于 xmodmap 是 xkbcomp；然而， xkbcomp 缺少 -e 选项(执行表达式)，所以不那么易用。不管怎样，不论何时应该宁愿用 xkbcomp。 

##  指示器 Indicators

如 "keyboard LEDs" 键盘那段落。 指示器命名被使用于搭配在 xkb_keycodes 段落中的实体数目LED。 除此此外，他们不相关。指示器不搭配在任何叫做"virtual"的LED；xkbvleds (package [xorg-xkbutils](<https://archlinux.org/packages/?name=xorg-xkbutils>)包) 可被用于检查他们的状态。 例子： 
    
       xkb_keycodes {
           indicator 1 = "LED1";       // first physical LED
       }
    
指示器是总反映指定部分的 XKB 内部状态。两种通用模式被显示于修饰键状态: 
    
       xkb_compatibility {
           indicator "LED1" { modifiers = Lock; }; // CapsLock indicator
       }
    
或目前组群： 
    
       xkb_compatibility {
           indicator "LED1" { groups = 0x06; };    // "group 2 or group 3 is active"
       }
    
这个值是比特掩码(bitmasks)。对于组群，比特1为组群1，比特2为组群2 后面如此序。 

##  修饰键与类别 Modifiers and types

有时候有必要清除类别区段，也可引入非常用类别。 

类别与修饰键紧密相关，所以很有意义地在做任何类别描述事情前从从修饰键开始。 

决定要用那个比特，他们只有8个。且这些 Shift, Control and Mod1 已广范用在应用程序中，并且 Lock (又叫 CapsLock键) 有预定义意思也可能难于覆盖。然而其余的4个可无碍运用。 

警告： 四个标准类别， ONE_LEVEL, TWO_LEVEL, ALPHABETIC and KEYPAD, 接到特殊对待于 xkbcomp。 他们作用不同只因他们被以作用命名。如果某些修改不如预起作用，试着加入新类别代替。 

###  使用实体修饰键在标准类别 Using real modifiers in standard types

取决于你的基本配置文件而定，可能有许多不常用标准类别像 EIGHT_LEVEL 或 PC_RCONTROL_LEVEL2。 移除他们以避免不需要的作用。 

现在，某些类别使用虚拟修饰键。如果你决定用他们，检查虚拟修饰键如下且略过这一段。 否则，有个好主意是去完全移除他们。检查所需类别，且一是用相对应的实体键取代他们，或相关定义。示例。 
    
       type "KEYPAD" {
           modifiers= Shift+NumLock;
           map[Shift]= Level2;
           map[NumLock]= Level2;
           level_name[Level1]= "Base";
           level_name[Level2]= "Number";
       };
    
如果你用 Mod2 用于 NumLock， 改类别成 
    
       type "KEYPAD" {
           modifiers= Shift+Mod2;
           map[Shift]= Level2;
           map[Mod2]= Level2;
           level_name[Level1]= "Base";
           level_name[Level2]= "Number";
       };
    
如果你不再用 NumLock 修饰键, 改成 
    
       type "KEYPAD" {
           modifiers= Shift;
           map[Shift]= Level2;
           level_name[Level1]= "Base";
           level_name[Level2]= "Number";
       };
    
作的雷同 xkb_compatibility 那段。 一旦修改完成，你应该能移除所有 "virtual_modifiers" 在文件中这行。 

###  切换单一修饰键比特

基本上你只需要按键象征加上有关的解释项(interpretation entry)。例如为了用`LWIN` 切换 Mod5 ，用`ISO_Level3_Shift`设给按键象征： 
    
       xkb_compatibility {
           interpret ISO_Level3_Shift { action = SetMods(modifiers=Mod5); };
       }
    
       xkb_symbols {
           key <LWIN> { [ISO_Level3_Shift ] };
       }
    
撇开 `SetMods`， 你也可以用 `LockMods` 或 `LatchMods`。 `SetMods` 产生通常的 "按住时持续 on while pressed" 修饰按键. `LockMods` 产生 "开/关 on/off" 如同 CapsLock 或 NumLock那样切换。 `LatchMods` 表示 "开启，直到下个按键按下 on until next keypress" 又称粘性修饰键。 

###  修饰键规划 modifier_map

修饰键规划是一张窗体含有映射每个修饰键8位值给至少4个按键： 
    
       modifier_map Mod1 { Alt_L, Alt_R };
    
在核心协议，没有 XKB， 这代表或多或少同样的事 
    
       interpret Alt_L { action = SetMods(modifiers=Mod1); };
       interpret Alt_R { action = SetMods(modifiers=Mod1); };
    
XKB不用修饰键规划他原本的意思。在XKB中，他唯一作用是去用在规划虚拟修饰键(参考下文)。 

然而，这个修饰键规划窗体很容易给客户端访问，且有一个反直觉(但常见)技巧在此： 修饰键规划被用来告知哪个ModX比特是Alt。因为这样，最好有个修饰键规划为如上文 Alt_L 或 Alt_R。除非你有好理由，否则最好设为Mod1。 

##  多键盘 Multiple keyboards

XKB 允许按键规划给单一连接上的唯一实体键盘。 这个特征极度有用于多键盘设置，当键盘是不一样的；想想有个全尺寸USB键盘连接着。 

首先，使用xinput (安装包 [xorg-xinput](<https://archlinux.org/packages/?name=xorg-xinput>)包) 以获得 device IDs: 
    
       AT Translated Set 2 keyboard                id=11   [slave  keyboard (3)]
    
现在， 
    
       xkbcomp -i 11 file.xkb $DISPLAY
    
或 
    
       setxkbmap -device 11 ...
    
将设置按键规划给指定id的键盘而已。顷印XKB设置动作也是： 
    
       xkbcomp -i 11 $DISPLAY file.xkb
    
注意 `xkbcomp -i11`将不给出明确的任何错误消息。确定你有空格在 `-i`后面。 

##  调试 XKB

当按键不照预想工作，第一件事要检查XKB内部状态：修饰键、影响的组群与控制比特。这三个都可以被用来驱动LED灯；使用xkbvleds去检查他们 
    
       indicator "LED1" { modifiers = Lock; };
       indicator "LED2" { groups = 2; };
       indicator "LED3" { controls = audiblebell; };
    
此外 xkbwatch 显示所有 (真实的) 修饰键及他们 固定lock/暂闩住latch 状态. 修饰键也被xev报告。 安装包 Xxkb 可被用来监控影响的组群，但确定two_state模式已关闭。 

在状况解释那段没有作用良好，确定有检查重复的 "interpret" 区块。 最好，试着检查相对应的特定按键象征。查看段落9.2有解释。 

也产生个想法去检查什么是服务器确实收到的，借着下载按键规划 
    
       xkbcomp $DISPLAY out.xkb
    
输出结果结果倾向不同于输入文件，。没有已知地解决方法。 

##  虚拟修饰键 Virtual Modifiers

XKB最让人困扰的部分之一，虚拟修饰键出现于所有标准按键规划档，尽管尽管存在相对次要且大多无用特征。这名词本身非常有误导性，且大多数文件没有进一步帮助。 

所以，首先: 虚拟修饰键不是所有实体修饰键之一。 如果有什么意思，那就是个方法去命名某些实体修饰键。那不是有更多16位而可以用于位阶定义。那是16个可能名称，每个参考到8个修饰键比特之1(有可能某些或没有引用到)。 

实体修饰键比特称为 Shift, Lock, Control 与 Mod1-Mod5。 Alt 不在其中。 虚拟修饰键被介绍为允许表示某键例如 
    
       #define Alt Mod1
    
给应用程序将使用这个消息。 

可以去定义一个有用键盘布局没有定义到任何虚拟修饰键；在标准修饰键中，仅有 Alt/Meta 实际需要如此对待，因为无论如何 Shift 和 Control 是实体修饰键且 NumLock 不常用于修饰键。 

同样，不像大多数按键规划相关的、影响应用程序使用基本的Xlib功能的事物，虚拟修饰键必须被质疑明确使用。不是所有应用程序实际这么做。 

###  定义虚拟修饰键 Defining virtual modifiers

在虚拟修饰键与实体修饰键之间是个定义，以有点奇怪地方式使用按键象征，如同一个介质。因为某些理由在此之后参考XKBproto 。真实修饰键叫做 M 被分配给一个键用： 
    
       modifier_map M { <keysym> };
    
虚拟修饰键 V 可以被分配给一个键用: 
    
       interpret <keysym> { virtualMod = V; };
    
如果一个虚拟修饰键 V 共享于至少一个按键象征给真实修饰键 M ，那就是被绑定给 M 键。 

注意虚拟修饰键命名不在预定义中 且 必须得使用前宣告于 xkb_compatibility 与 xkb_types 段落: 
    
       xkb_compatibility "complete" {
           virtual_modifiers LevelThree,NumLock,Alt;
       }
    
###  按键象征解释 Keysym interpretation

虚拟修饰键可被用 interpret <keysym> 区块如同他们被定义于相对应的实体修饰键。对一个虚拟修饰键 V 不绑定于任何实体修饰键，这代表 
    
       #define V
    
类声明且 
    
       interpret <key> { }
       interpret <key>+V { }
    
此区块将被视为重复。在文件中仅有他们之中最后一项将作用。像这种例子xkbcomp通常会给警告。 

###  客户端侧注记 Client side notes

处理 XKB 虚拟修饰键在客户端侧需要某些非琐碎服务器解译。大多数应用程序只是不操心，附上8个真实修饰键提供在 XKeyEvent.state。 

不过,那是有可能给应用程序获得虚拟修饰键结合按键按下。 Gtk,例如, [gdk-keymap-translate-keyboard-state()](<https://developer-old.gnome.org/gdk2/stable/gdk2-Keyboard-Handling.html#gdk-keymap-translate-keyboard-state>) 那个功能可能有也可能没有被用于特定应用程序。 

某些人可能实现某些事像虚拟修饰键支持，但实际没有。检查Openbox在章节5.3.3.2。关于Alt处理，查看章节 8.3。(备注：搜索不到openbox的文件，待高手补充) 

##  XKB 控制比特

一堆比特标志影响不同方面的XKB功能性。要控制他们， 用 {Set,Latch,Lock} 控制触发动作。 

###  鼠标控制 Mouse control

XKB允许控从键盘制鼠标指针。 档设置适当，他极度有用。 然而，他的可用性依赖许多特定实体键盘的布局规划跟用户喜好上。 

从XKB 观点看这相对简单来实现，修改人只要触发相关动作。 相当完全的实现可被发现于 `/usr/share/X11/xkb/compat/mousekeys`。 

注意那触发动作将不会工作除非 `MouseKeys` 控制比特有设置: 
    
       interpret Pointer_EnableKeys { action= LockControls(controls=MouseKeys); };
    
由于大多数键盘没有专用鼠标控制键， 结合 `MouseKeys` 与 `Overlay` 其中之一的标记可能是好主意。 
    
       interpret Pointer_EnableKeys { action= LockControls(controls=MouseKeys+Overlay1); };
    
这设置允许鼠标游标控制键到适当覆盖区块： 
    
       xkb_keycodes {
           <MUP> = 218;
           <MDWN> = 212;
           <MLFT> = 214;
           <MRHT> = 216;
       }
    
       xkb_symbols {
           key   <UP> { [    Up ], overlay1 = <MUP> };
           key <LEFT> { [  Left ], overlay1 = <MLFT> };
           key <RGHT> { [ Right ], overlay1 = <MRHT> };
           key <DOWN> { [  Down ], overlay1 = <MDWN> };
    
           key <MUP>  { [ Pointer_Up ] };
           key <MDWN> { [ Pointer_Down ] };
           key <MLFT> { [ Pointer_Left ] };
           key <MRHT> { [ Pointer_Right ] };
       }
    
这方法他可能去分配 non-mouse 触发动作到按键来用于控制鼠标， 且因此， 给个例子， 使用修饰按键去产生鼠标按钮事件。 

## Local XKB folder

你可以设置一个 X 来自本机文件的按键规划，用下列命令： 
    
    $ xkbcomp keymap.xkb $DISPLAY
    
这里 `keymap.xkb` 必须有个结构，像 
    
    keymap.xkb
    
    xkb_keymap {
        xkb_keycodes  { ... };
        xkb_types     { ... };
        xkb_compat    { ... };
        xkb_symbols   { ... };
    
        // 下行的键盘按键位置构造项目完全是选择性使用。
        // xkb_geometry  { include "pc(pc104)" };
    };
    
你可以用 _includes_ 从这个文件， 这里 the inclusion 参考自本机文件夹而不是 `/usr/share/X11/xkb`。 为了这个你需要用 `-I/path/` 参数。例如： 
    
    $ xkbcomp -I$HOME/.xkb $HOME/.keymap.xkb $DISPLAY
    
    $HOME/.keymap.xkb
    
    xkb_keymap {
        xkb_keycodes  { include "evdev+aliases(qwerty)" };
        xkb_types     { include "complete" };
        xkb_compat    { include "complete" };
        xkb_symbols   { include "pc+custom+inet(evdev)" };
    };
    
符号档必须有同样命名如同上面例子 `xkb_symbols`的那行。 The symbol file must have the same name as specified in the `xkb_symbols` right above. 
    
    $HOME/.xkb/symbols/custom
    
    partial alphanumeric_keys xkb_symbols "custom" { ... };
    
##  问题排除

###  有个usb键盘 当插拔之后设置消失了 I have an USB keyboard and the settings get lost upon unplugging it

使用 [rules](<#%E4%BD%BF%E7%94%A8_rules_%E8%B3%87%E6%96%99%E5%A4%BE%E8%A6%8F%E5%89%87%E8%B3%87%E6%96%99>) 替代静态按键规划设置会让你更有弹性和长久性按键规划映射那不需手动地(或用脚本script) Using [rules](<#%E4%BD%BF%E7%94%A8_rules_%E8%B3%87%E6%96%99%E5%A4%BE%E8%A6%8F%E5%89%87%E8%B3%87%E6%96%99>) instead of static keymap configuration will give you a more flexible and permanent key mapping that does not need to be reloaded manually (or by a script). 

##  也参考 See also

  * [The XKB Configuration Guide](<https://www.x.org/releases/current/doc/xorg-docs/input/XKB-Config.html>)
  * <https://www.x.org/wiki/XKB>
  * [An Unreliable Guide To XKB Configuration](<https://www.charvolant.org/doug/xkb/html/index.html>)[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2021-11-19 ⓘ].
  * [Ivan Pascal XKB docs](<http://pascal.tsu.ru/en/xkb/>). 最老的与最为人知的指南之一，聚焦许多细节，且解释某些独特的XKB功能。
  * [XKB protocol specification](<https://www.x.org/releases/current/doc/kbproto/xkbproto.pdf>). 全面描述所有XKB功能。极度有用于了解XKB如何工作，在所有东西中包含虚拟修饰键的良好叙述。某些xkbcomp实践极度建议做过，尽管功能被描述于协议等级。
