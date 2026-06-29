**翻译状态：**

  * 本文（或部分内容）译自 [Arch IRC channels](<https://wiki.archlinux.org/title/Arch_IRC_channels> "arch:Arch IRC channels")，最近一次同步于 2016-06-27，若英文版本有所[更改](<https://wiki.archlinux.org/title/Arch_IRC_channels?diff=0&oldid=439070>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Arch_IRC_channels_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

**注意：** 此页面上的内容可能不是最新的，请首先参阅 ArchWiki 上的 [Arch IRC channels](<https://wiki.archlinux.org/title/Arch_IRC_channels> "arch:Arch IRC channels") 。

相关文章

  * [ArchWiki:IRC](</wzh/index.php?title=Project:IRC&action=edit&redlink=1> "Project:IRC（页面不存在）")
  * [International communities](<../zh-cn/International_communities.html> "International communities")
  * [phrik](</wzh/index.php?title=Phrik&action=edit&redlink=1> "Phrik（页面不存在）")

##  官方频道

这篇条目介绍 Arch Linux 的[IRC](<https://zh.wikipedia.org/wiki/IRC> "zhwp:IRC") 主要支持频道 **#archlinux** , 主要的交流频道 **#archlinux-offtopic** 。（都在 [Libera Chat](<https://libera.chat/>) 上） 

**#archlinux** 频道的主要话题是有关 Arch Linux 的支持和总体讨论。频道规则请查看[Code of conduct](</wzh/index.php?title=Code_of_conduct&action=edit&redlink=1> "Code of conduct（页面不存在）") 和 [General guidelines#IRC](<../zh-cn/General_guidelines.html#IRC> "General guidelines")，常用的缩略语请参看[Arch terminology](<../zh-cn/Arch_terminology.html> "Arch terminology") 和 [IRC Jargon](<http://www.ircbeginner.com/ircinfo/abbreviations.html>)。 

你需要一个IRC客户端才能加入讨论频道。可用的IRC客户端列表请查看[List of applications/Internet#IRC clients](<../zh-cn/List_of_applications/Internet.html#IRC_clients> "List of applications/Internet") 和 [Wikipedia:Comparison of Internet Relay Chat clients](<https://en.wikipedia.org/wiki/Comparison_of_Internet_Relay_Chat_clients> "wikipedia:Comparison of Internet Relay Chat clients")。[安装环境](<../zh-cn/Installation_guide.html> "Installation guide")中可以使用 [irssi](<../zh-cn/Irssi.html> "Irssi") 。 

###  用户名注册

**#archlinux** 和**archlinux-offtopic** 当前的频道模式为`+r`和`+q $~a`。这意味着你必须通过`NickServ`的身份验证才能加入个别的频道，发送消息。做这个是为了过滤垃圾信息的骚扰。 

需要使用NickServ注册，请参照[libera FAQ](<https://libera.chat/guides/registration>)，当连接上了 _irc.libera.chat_ 使用`NickServ help`： 
    
    /query nickserv help register
    /query nickserv help identify
    
如果你并没有进行用户注册和验证，你会被转到**#archlinux-unregisterd** 频道。用`msg chanserv access #archlinux list`指令能得到可以帮助你的人的列表，或者加入#liberachat频道，在那里提问。 

**注意：**

  * 如果`/query`在你的客户端不起作用，你可以试着用`/quote nickserv <command>`或`/msg nickserv <command>`。
  * 有些客户端会在你通过NickServ验证之前就尝试自动加入频道， 你需要开启SASL来解决这个问题。查看你的IRC客户端文档或者在[SASL page](<https://libera.chat/guides/sasl>)上寻找教程来实现它。

###  频道管理员

**注意：** Arch的管理员在**#archlinux** 和**#archlinux-offtopic** 都具有管理员身份。查看下面的列或者在liberachat上用`/msg phrik listops`指令。

需要管理员的协助? 别犹豫，直接 `/query` 或者 `/msg` 吧。截止到 2019-12-18 , 操作员有这些: 

  * alad
  * amcrae
  * falconindy
  * gehidore / man
  * grawity
  * heftig
  * jelle
  * MrElendig / Mion
  * Namarrgon
  * tigrmesh / tigr
  * wonder / ioni

###  其它频道

The size of our community led to the creation of multiple IRC channels. To get a list of all channels on **[irc.libera.chat](<ircs://irc.libera.chat>)** that contain `archlinux` in their name, use the command `/query alis list *archlinux*`. 

Channel  | Description   
---|---  
[#archlinux64](<ircs://irc.libera.chat/archlinux64>) | x86_64 specific discussion channel, mostly in English   
[#archlinux-aur](<ircs://irc.libera.chat/archlinux-aur>) |  [AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR") general discussion   
[#archlinux-aurweb](<ircs://irc.libera.chat/archlinux-aurweb>) |  [aurweb](<https://gitlab.archlinux.org/archlinux/aurweb>) development discussion   
[#archlinux-bugs](<ircs://irc.libera.chat/archlinux-bugs>) | Bug-centric discussion   
[#archlinux-classroom](<ircs://irc.libera.chat/archlinux-classroom>) | A project that develops and hosts classes for the Arch Linux community.   
[#archlinux-devops](<ircs://irc.libera.chat/archlinux-devops>) | Arch Linux internal infrastructure and devops discussions.   
[#archlinux-multilib](<ircs://irc.libera.chat/archlinux-multilib>) | Arch Linux Multilib Project discussion and packaging   
[#archlinux-newbie](<ircs://irc.libera.chat/archlinux-newbie>) | A space to learn, try new things, and ask for help without fear of ridicule.   
[#archlinux-pacman](<ircs://irc.libera.chat/archlinux-pacman>) |  [Pacman](<../zh-cn/Pacman.html> "Pacman") development and discussion   
[#archlinux-projects](<ircs://irc.libera.chat/archlinux-projects>) | Projects development and discussion (mkinitcpio, abs, dbscripts, devtools, ...)   
[#archlinux-reproducible](<ircs://irc.libera.chat/archlinux-reproducible>) | Discussion channel for achieving reproducible builds.   
[#archlinux-security](<ircs://irc.libera.chat/archlinux-security>) | Discussion of security issues within Arch packages.   
[#archlinux-testing](<ircs://irc.libera.chat/archlinux-testing>) | Discussion channel regarding the testing repositories.   
[#archlinux-wiki](<ircs://irc.libera.chat/archlinux-wiki>) | Discussion about [ArchWiki](<../Project:%E5%85%B3%E4%BA%8E.html> "ArchWiki"), its articles and the [Arch Linux Forums](<https://bbs.archlinux.org/>).   
[#archlinux-women](<ircs://irc.libera.chat/archlinux-women>) | Discussing gender and equality, mostly in English.   
[#archlinux-proaudio](<ircs://irc.libera.chat/archlinux-proaudio>) | Discussion of [Arch Linux 专业音频](<../zh-cn/%E4%B8%93%E4%B8%9A%E9%9F%B3%E9%A2%91.html> "专业音频"). Users also in the unofficial #archaudio   
  
##  其它语言的 IRC 频道

International discussions are available at the following channels, also located at the [irc.libera.chat](<ircs://irc.libera.chat>) IRC network, unless stated otherwise. 

Channel  | Description   
---|---  
[#archlinux-za](<ircs://irc.libera.chat/archlinux-za>) | Discussion (Afrikaans, English)   
[#archlinux-br](<ircs://irc.libera.chat/archlinux-br>) | Discussion (Brazilian)   
[#archlinux-cr](<ircs://irc.libera.chat/archlinux-cr>) | Discussion (Costa Rica)   
[#archlinux.cz](<ircs://irc.libera.chat/archlinux.cz>) | Discussion (Czech)   
[#archlinux.dk](<ircs://irc.libera.chat/archlinux.dk>) | Discussion (Danish)   
[#archlinux.fi](<ircs://irc.libera.chat/archlinux.fi>) | Discussion (Finnish)   
[#archlinux-fr](<ircs://irc.libera.chat/archlinux-fr>) | Discussion (French)   
[#archlinux-gaelic](<ircs://irc.libera.chat/archlinux-gaelic>) | Discussion (Gaelic)   
[#archlinux.de](<ircs://irc.libera.chat/archlinux.de>) | Discussion (German)   
[#archlinux-greece](<ircs://irc.libera.chat/archlinux-greece>) | Discussion (Greek)   
[#archlinux-il](<ircs://irc.libera.chat/archlinux-il>) | Discussion (Hebrew)   
[#archlinux.hu](<ircs://irc.libera.chat/archlinux.hu>) | Discussion (Hungarian)   
[#archlinux-it](<ircs://irc.libera.chat/archlinux-it>) | Discussion (Italian); also on **[irc.azzurra.org#archlinux](<ircs://irc.azzurra.org/archlinux>)**  
[#archlinux-nordics](<ircs://irc.libera.chat/archlinux-nordics>) | Discussion (the nordics: Danish, Finnish, Norwegian and Swedish)   
[#archlinux-kr](<ircs://irc.libera.chat/archlinux-kr>) | Discussion (Korean)   
[#archlinux-ir](<ircs://irc.libera.chat/archlinux-ir>) | Discussion (Persian)   
[#archlinux.org.pl](<ircs://irc.libera.chat/archlinux.org.pl>) | Discussion (Polish)   
[#archlinux-pt](<ircs://irc.libera.chat/archlinux-pt>) | Discussion (Portuguese)   
[#archlinux.ro](<ircs://irc.libera.chat/archlinux.ro>) | Discussion (Romanian)   
[#archlinux-ru](<ircs://irc.libera.chat/archlinux-ru>) | Discussion (Russian); also on **[irc.mibbit.net#archlinux-ru](<irc://irc.mibbit.net/archlinux-ru>)**  
[#archlinux-rs](<ircs://irc.libera.chat/archlinux-rs>) | Discussion (Serbian)   
[#archlinux-es](<ircs://irc.libera.chat/archlinux-es>) | Discussion (Spanish)   
[#archlinux.se](<ircs://irc.libera.chat/archlinux.se>) | Discussion (Swedish)   
[#archlinux-tr](<ircs://irc.libera.chat/archlinux-tr>) | Discussion (Turkish)   
[#archlinux-ve](<ircs://irc.libera.chat/archlinux-ve>) | Discussion (Venezuela)   
[#archlinuxvn](<ircs://irc.libera.chat/archlinuxvn>) | Discussion (Vietnamese, Tiếng Việt) 
