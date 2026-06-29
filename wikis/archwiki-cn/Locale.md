**翻译状态：**

  * 本文（或部分内容）译自 [Locale](<https://wiki.archlinux.org/title/Locale> "arch:Locale")，最近一次同步于 2022-11-15，若英文版本有所[更改](<https://wiki.archlinux.org/title/Locale?diff=0&oldid=756132>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Locale_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [Environment variables](<../zh-cn/Environment_variables.html> "Environment variables")
  * [Localization](</wzh/index.php?title=Localization&action=edit&redlink=1> "Localization（页面不存在）")

[glibc](<https://archlinux.org/packages/?name=glibc>)包 和应用程序、函数库库使用[区域设置](<https://zh.wikipedia.org/wiki/%E5%8C%BA%E5%9F%9F%E8%AE%BE%E7%BD%AE> "zhwp:区域设置")显示本地化的文字、货币、时间、日期、特殊字符等包含地域属性的内容。 

##  生成区域设置

区域设置的名称通常用 `[language][_TERRITORY][.CODESET][@modifier]` 的格式表示， _language_ 是 [ISO 639 语言代码](<https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes> "w:List of ISO 639-1 codes"), _territory_ 是 [ISO 3166 国家代码](<https://en.wikipedia.org/wiki/ISO_3166-1#Current_codes> "w:ISO 3166-1"), _codeset_ 是[字符集](<https://en.wikipedia.org/wiki/Character_encoding> "w:Character encoding")或 [ISO-8859-1](<https://en.wikipedia.org/wiki/ISO/IEC_8859-1> "w:ISO/IEC 8859-1")、[UTF-8](<https://en.wikipedia.org/wiki/UTF-8> "w:UTF-8") 这样的编码方式。请参考 [setlocale(3)](<https://man.archlinux.org/man/setlocale.3>)。 

要列出所有启用的区域设置，使用： 
    
    $ locale -a
    
启用一个区域设置前，需要先生成它。在 `/etc/locale.gen` 中取消对应的注释，然后执行 _locale-gen_ 。注释掉某行，则会移除对应的区域设置。请启用所有用户都可能使用的区域设置及相关[#变量](<#%E5%8F%98%E9%87%8F>)。 

例如对于使用美式英语和中国简体的用户： 
    
    /etc/locale.gen
    
    ...
    #en_SG ISO-8859-1  
    en_US.UTF-8 UTF-8  
    #en_US ISO-8859-1  
    ...
    #zh_CN.GBK GBK  
    zh_CN.UTF-8 UTF-8  
    #zh_CN GB2312  
    ...
    
编辑完成以后,通过下面的命令生成 Locale： 
    
    # locale-gen
    
**注意：**

  * 每次更新 [glibc](<https://archlinux.org/packages/?name=glibc>)包 时 `locale-gen` 会自动运行。[[1]](<https://github.com/archlinux/svntogit-packages/blob/packages/glibc/trunk/glibc.install#L2>)
  * 建议优先使用 `UTF-8`。[[2]](<https://utf8everywhere.org/>)

##  设置当前区域

想要显示正在使用的 Locale 和相关的环境变量，运行： 
    
    $ locale
    
要使用的区域设置（从前面生成的区域设置中选择）设置在 `locale.conf` 文件中。每一个 `locale.conf` 文件都必须包含一些[环境变量](<../zh-cn/Environment_variables.html> "Environment variables")赋值语句，其格式与 _locale_ 命令输出的格式相同。 

要查看已经生成的区域设置： 
    
    $ localedef --list-archive
    
或者使用 [localectl(1)](<https://man.archlinux.org/man/localectl.1>)： 
    
    $ localectl list-locales
    
###  系统区域设置

要设置整个系统使用的区域设置，需要在 `/etc/locale.conf` 中写入 `LANG` 变量，以下的 _zh_CN.UTF-8_ 应为 `/etc/locale.gen` 中某个未注释条目的**第一列** ： 
    
    locale.conf
    
    LANG=zh_CN.UTF-8

或者使用： 
    
    # localectl set-locale LANG=zh_CN.UTF-8
    
参阅[#变量](<#%E5%8F%98%E9%87%8F>)和 [localectl(1)](<https://man.archlinux.org/man/localectl.1>) 获得更多细节。 

###  在用户会话中覆盖系统区域设置

系统使用的区域设置可以通过用户编辑自己的 `~/$XDG_CONFIG_HOME/locale.conf` (通常为 `~/.config/locale.conf`) 来覆盖。 

这些 `locale.conf` 文件的优先级定义在 `/etc/profile.d/locale.sh` 中。 

**提示：**

  * 设置用户级区域设置 ，能让 `/var/log/` 中的日志以英语输出而在用户环境中使用所选语言。
  * 建立 `/etc/skel/.config/locale.conf` 文件，可以让所有通过 _useradd_ 命令和 `-m` 选项创建的新用户自动拥有一份相应的 `~/.config/locale.conf`。

###  立即启用新设置

`locale.conf` 的变更会在下次登录时生效，要立刻应用新的设置的话，可以运行： 
    
    $ unset LANG
    $ source /etc/profile.d/locale.sh
    
**注意：**`LANG` 变量必须先被 `unset`，否则 `locale.sh` 不会从 `locale.conf` 中更新变量。只有新增的或被修改的命令会被自动更新，从 `locale.conf` 被移除的变量在注销前依然存在。

###  其它用例

和区域设置相关的变量也能像其他的[环境变量](<../zh-cn/Environment_variables.html> "Environment variables")一样传递给其它程序。 

例如在开发和测试某个程序时,可以这样运行： 
    
    $ LANG=C ./my_application.sh
    
类似的，也可以通过设置环境变量让当前 shell 中运行的程序使用特定的区域设置(例如安装系统时)： 
    
    $ export LANG=C
    
##  变量

`locale.conf` 文件支持以下环境变量。 

  * [LANG](<#LANG%EF%BC%9A%E9%BB%98%E8%AE%A4%E7%9A%84%E5%8C%BA%E5%9F%9F%E8%AE%BE%E7%BD%AE>)
  * [LANGUAGE](<#LANGUAGE%EF%BC%9A%E5%90%8E%E5%A4%87%E5%8C%BA%E5%9F%9F%E8%AE%BE%E7%BD%AE>)
  * `LC_ADDRESS`
  * [LC_COLLATE](<#LC_COLLATE%EF%BC%9A%E6%8E%92%E5%BA%8F%E6%A0%BC%E5%BC%8F>)
  * `LC_CTYPE`
  * `LC_IDENTIFICATION`
  * `LC_MEASUREMENT`
  * `LC_MESSAGES`
  * `LC_MONETARY`
  * `LC_NAME`
  * `LC_NUMERIC`
  * `LC_PAPER`
  * `LC_TELEPHONE`
  * [LC_TIME](<#LC_TIME%EF%BC%9A%E6%97%B6%E9%97%B4%E5%92%8C%E6%97%A5%E6%9C%9F%E6%A0%BC%E5%BC%8F>)

[locale(7)](<https://man.archlinux.org/man/locale.7>) 包含了完整 `LC_*` 列表，[locale(5)](<https://man.archlinux.org/man/locale.5>) 包含了详细定义。 

**注意：** 程序在查找本地化相关的变量时遵守[此优先级顺序](<https://www.gnu.org/software/gettext/manual/gettext.html#Locale-Environment-Variables>)。

###  LANG：默认的区域设置

这个变量的值会覆盖掉所有未设置的 `LC_*` 变量的值。 

**提示：** 假设您是西班牙的英语使用者，并且您希望程序根据西班牙的惯例处理数字和日期，仅消息为英语。您可以将 `LANG` 设置为 `es_ES.UTF-8`，并将 `LC_MESSAGES`（用于消息翻译的用户界面）设置为 `en_US.UTF -8`。

###  LANGUAGE：后备区域设置

使用 gettext 翻译的软件会按照 `LANGUAGE` 选择使用的语言。用户通过这个变量指定一个区域设置[列表](<https://www.gnu.org/software/gettext/manual/gettext.html#The-LANGUAGE-variable>)，如果前面的区域设置缺少翻译，会自动使用后面的区域设置显示界面。例如一个澳大利亚用户可能更希望在没有合适的澳大利亚英语翻译时回退到英式英语而不是美式英语： 
    
    locale.conf
    
    LANG=en_AU.UTF-8
    LANGUAGE=en_AU:en_GB:en

**注意：** 很多软件并未将其英文 locale 设置为 `en` 或 `en_US`，而是使用默认 locale `C`。如果在 `LANGUAGE` 中将非英文 locale 设置到 English 之后，例如 `LANGUAGE=en_US:en:es_ES`，那么即使英语字符存在，应用程序可能会选择使用后备 locale. [[3]](<https://bugs.kde.org/show_bug.cgi?id=192019>) 解决方法是强制在英语 locale 后面设置 `C`，例如 `LANGUAGE=en_US:en:C:es_ES`.

###  LC_TIME：时间和日期格式

如果 `LC_TIME` 设置成 `en_US.UTF-8`，日期的格式为 "MM/DD/YYYY"。要使用 ISO 8601 标准的日期格式( "YYYY-MM-DD" ) ,使用： 
    
    locale.conf
    
    LC_TIME=en_DK.UTF-8

[glibc](<https://archlinux.org/packages/?name=glibc>)包 2.29 修复了一个错误，`en_US.UTF-8` 开始如预期般显示 12 小时格式的时间。如果要使用 24 小时制，请使用 `LC_TIME=C.UTF-8`。 

**注意：** 使用此变量来格式化日期不是对程序的强制要求。例如，[date(1)](<https://man.archlinux.org/man/date.1>) 使用其自己的参数来格式化时间，[Firefox](<../zh-cn/Firefox.html> "Firefox") 在版本 57 到 84 之间不支持 `LC_TIME`（[Bug 1429578](<https://bugzilla.mozilla.org/show_bug.cgi?id=1429578>)）。

###  LC_COLLATE：排序格式

这个变量的值决定排序和正则表达式的格式顺序。 

例如将它设置为 `C` 可以让 _ls_ 命令首先列出点开头的文件，然后是大写字母开头的文件和小写字母开头的文件： 
    
    locale.conf
    
    LC_COLLATE=C

另见 [[4]](<https://superuser.com/a/448294>)。 

为了避免潜在的问题，Arch Linux 曾经在 `/etc/profile` 中设置 `LC_COLLATE=C`，这个方法已经过时了。 

###  LC_ALL：测试和排除问题

这个变量的值会覆盖掉 `LANG` 和所有 `LC_*` 变量的值，无论它们是否设置。 如果 `LC_ALL` 设置为`C`, 此变量将覆盖 `LANGUAGE`. 

只有 `LC_ALL` **不能** 出现在 `locale.conf` 文件中：它只能为了测试和排除问题而设置，例如在 `/etc/profile` 中。 

**注意：**`LC_ALL=C.UTF-8` 与 `LC_ALL=C` 不同，不会覆盖 `LANGUAGE`. 请参考 [glibc bug 16621](<https://sourceware.org/bugzilla/show_bug.cgi?id=16621>) 和 [gettext bug 62815](<https://savannah.gnu.org/bugs/?62815>).

##  疑难解答

###  我的终端不支持 UTF-8

这里列出了一些（不是全部）支持 UTF-8 的终端： 

  * gnustep-terminal
  * konsole
  * [mlterm](<../zh-cn/Mlterm.html> "Mlterm")
  * [rxvt-unicode](<../zh-cn/Rxvt-unicode.html> "Rxvt-unicode")
  * [st](<../zh-cn/St.html> "St")
  * [基于 VTE 的终端](<../zh-cn/List_of_applications/Utilities.html#VTE-based> "List of applications/Utilities")
  * [xterm](</wzh/index.php?title=Xterm&action=edit&redlink=1> "Xterm（页面不存在）") \- 启动时使用参数 `-u8`，或者配置资源 `xterm*utf8: 2`。

####  Gnome-terminal / rxvt-unicode 不支持 UTF-8

你必须在 UTF-8 的区域设置下运行它们才会有作用。按照上面的方法启用 `en_US.UTF-8`（或者其它使用 UTF-8 的区域设置）并将它设置成默认区域设置后重启系统。 

###  我的系统的语言还是不对

可能其它文件设置了本该由 `locale.conf`，详见[定义环境变量](<../zh-cn/Environment_variables.html#%E5%AE%9A%E4%B9%89%E5%8F%98%E9%87%8F> "Environment variables")。 

如果使用了桌面环境，可能是被桌面环境修改。例如 [GNOME](<../zh-cn/GNOME.html> "GNOME") 的语言设置会覆盖 `locale.conf` 中的设置。 

[KDE](<../zh-cn/KDE.html> "KDE") Plasma 也通过系统设置修改界面的语言，如果按本文修改后还是原来的区域设置，请[删除](<https://bbs.archlinux.org/viewtopic.php?pid=1435219#p1435219>) `~/.config/plasma-localerc` (之前是：`~/.config/plasma-locale-settings.sh`)。 

如果您正在结合 [accountsservice](<https://archlinux.org/packages/?name=accountsservice>)包 使用显示管理器，请遵循 [Display manager#为用户会话设置语言](<../zh-cn/Display_manager.html#%E4%B8%BA%E7%94%A8%E6%88%B7%E4%BC%9A%E8%AF%9D%E8%AE%BE%E7%BD%AE%E8%AF%AD%E8%A8%80> "Display manager")中的说明。 

[LightDM](<../zh-cn/LightDM.html> "LightDM") 将自动使用 [accountsservice](<https://archlinux.org/packages/?name=accountsservice>)包 来设配置用户的区域设置（如果已安装）。否则，LightDM 将用户会话配置存储在 `~/.dmrc` 中。也可能从那里检索到意料外的的区域设置。 

###  解压文件的编码不正确

老的 Windows 版本 (XP, Vista 和 7) 使用不同的编码方式压缩文件。要解压这些文件，请使用： 
    
    $ unzip -O CP936 _file.zip_
    
##  另见

  * [Gentoo:Localization/Guide](<https://wiki.gentoo.org/wiki/Localization/Guide> "gentoo:Localization/Guide")
  * [Supposedly 2008, or earlier, Gentoo wiki article](<http://wikigentoo.ksiezyc.pl/Locales.htm>)
  * [ICU's interactive collation testing](<https://icu4c-demos.unicode.org/icu-bin/collation.html>)
  * [Free Standards Group Open Internationalisation Initiative](<http://www.openi18n.org/>)
  * [_The Single UNIX Specification_ definition of Locale](<https://pubs.opengroup.org/onlinepubs/007908799/xbd/locale.html>) by The Open Group
  * [Locale environment variables](<https://help.ubuntu.com/community/EnvironmentVariables#Locale_setting_variables>)
