**翻译状态：**

  * 本文（或部分内容）译自 [Thunderbird](<https://wiki.archlinux.org/title/Thunderbird> "arch:Thunderbird")，最近一次同步于 2025-05-04，若英文版本有所[更改](<https://wiki.archlinux.org/title/Thunderbird?diff=0&oldid=831447>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Thunderbird_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [Firefox](<../zh-cn/Firefox.html> "Firefox")

[Thunderbird](<https://www.thunderbird.net/zh-CN/>)（雷鸟）是一款开源的电子邮件、新闻和聊天客户端，曾由 Mozilla（谋智网络）基金会开发。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [thunderbird](<https://archlinux.org/packages/?name=thunderbird>)包 包。如果需要，请安装[语言包](<https://archlinux.org/packages/?q=thunderbird-i18n>)。 

其它版本包括： 

  * **Thunderbird Beta 版** — 具有相对稳定的前沿功能。

     <https://www.thunderbird.net/zh-CN/thunderbird/all> || [thunderbird-beta-bin](<https://aur.archlinux.org/packages/thunderbird-beta-bin/>)AUR

  * **Thunderbird 每日版** — 通过每日构建体验最新的创新（适用于愿意处理潜在问题的用户）。

     <https://www.thunderbird.net/zh-CN/thunderbird/all> || [thunderbird-nightly-bin](<https://aur.archlinux.org/packages/thunderbird-nightly-bin/>)AUR

  * **Betterbird** — Betterbird 是 Mozilla Thunderbird 的优化版本，可以说是加强版的 Thunderbird。

     <https://www.betterbird.eu> || [betterbird-bin](<https://aur.archlinux.org/packages/betterbird-bin/>)AUR

关于过去和未来的版本概览，可以参见 [MozillaWiki:Releases](<https://wiki.mozilla.org/Releases> "mozillawiki:Releases")。 

##  隐私安全

  * Thunderbird 会在 HELO/ELHO SMTP 命令中将系统的内部 IP 地址作为参数发送给配置好的 SMTP 服务器。这个值可以通过设置 `mail.smtpserver.default.hello_argument` 为例如 `localhost` 来覆盖，但这样做可能会增加发送邮件的垃圾邮件评分。详情请参见 [[1]](<https://kb.mozillazine.org/Replace_IP_address_with_name_in_headers>) 和 [[2]](<https://kb.mozillazine.org/Mail_and_news_settings>)。
  * 要隐藏 Thunderbird 的[用户代理字符串（UA）](<https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Headers/User-Agent/Firefox>)，可以将 `mailnews.headers.useMinimalUserAgent` 设置为 `false` 并在[#配置编辑器](<#%E9%85%8D%E7%BD%AE%E7%BC%96%E8%BE%91%E5%99%A8>)中创建一个新的空的 `general.useragent.override` 字符串条目。
  * JavaScript 在消息内容中被禁用，但在 RSS 新闻源中默认启用。要禁用它，请在[#配置编辑器](<#%E9%85%8D%E7%BD%AE%E7%BC%96%E8%BE%91%E5%99%A8>)中将 `javascript.enabled` 设置为 `false`。

**注意：**

  * 将 `javascript.enabled` 设置为 `false` 会在 OAuth 对话框中也禁用 JavaScript。
  * 将 `general.useragent.override` 设置为空字符串已知会导致 Duo MFA 出现问题。详情请参见 [web-bugs#104558](<https://github.com/webcompat/web-bugs/issues/104558>)。

##  插件与扩展

插件需要使用软件包管理器[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")。扩展可以通过附加组件管理器安装，部分也可以用软件包管理器[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")。 

  * **Birdtray** — 通过 [X](<../zh-cn/Xorg.html> "X") 服务器在系统托盘显示新邮件通知的插件，无需安装扩展。可使用系统托盘图标运行 Thunderbird。

     <https://github.com/gyunaev/birdtray> || [birdtray](<https://aur.archlinux.org/packages/birdtray/>)AUR

  * **SysTray-X** — 系统托盘扩展。类似于 FireTray，但适用于 Thunderbird 68+ 版本，需要同时安装插件和相应扩展才能工作。适用于 [X11](<../zh-cn/Xorg.html> "X11") 桌面。

     <https://github.com/Ximi1970/systray-x> || [systray-x-common](<https://archlinux.org/packages/?name=systray-x-common>)包 或 [systray-x-kde](<https://archlinux.org/packages/?name=systray-x-kde>)包

  * **SOGo Connector** — 让你能够通过 CardDAV 同步通讯录。

     <https://sogo.nu/download.html#/frontends> || [thunderbird-sogo-connector-bin](<https://aur.archlinux.org/packages/thunderbird-sogo-connector-bin/>)AUR

  * **Cardbook** — 基于 CARDDav 和 VCARD 标准的 Thunderbird 新通讯录。

     [Cardbook AMO](<https://addons.thunderbird.net/thunderbird/addon/cardbook/>) ||

###  OpenPGP：签名与加密

从 Thunderbird 78.2.1 版本开始，此功能已经集成到 Thunderbird 中。此前，这一功能是由 Enigmail 插件提供的，但该插件不兼容 Thunderbird 78+ 版本。要将密钥从 Enigmail 迁移到 Thunderbird，并了解目前支持的功能，请参阅[在 Thunderbird 中使用 OpenPGP——怎么做以及问题解答](<https://support.mozilla.org/zh-CN/kb/thunderbird-openpgp>)。在迁移前，请确保为主密码使用了一个强密码短语。否则，私钥将无法得到妥善保护。 

##  提示与技巧

###  配置编辑器

可以通过点击**≡菜单 > 设置 > 常规**并点击页面底部的**配置编辑器…(C)** 按钮来扩展配置 Thunderbird。 或者，如果启用了菜单栏，则可以通过点击菜单栏的**编辑(E) > 设置(E) > 常规**找到配置编辑器按钮。 

###  设置默认浏览器

Thunderbird 使用由 [XDG MIME Applications](<../zh-cn/XDG_MIME_Applications.html> "XDG MIME Applications") 定义的默认浏览器。这通常由[桌面环境](<../zh-cn/%E6%A1%8C%E9%9D%A2%E7%8E%AF%E5%A2%83.html> "桌面环境")（例如 [GNOME](<../zh-cn/GNOME.html> "GNOME") 的控制中心：**详细信息 > 默认应用程序 > Web**）进行修改。 

这可以通过在[#配置编辑器](<#%E9%85%8D%E7%BD%AE%E7%BC%96%E8%BE%91%E5%99%A8>)中设置 `network.protocol-handler.warn-external` 来覆盖。 

如果以下所有设置都为 `false`（默认），则将其设置为 `true`，当您点击链接时，Thunderbird 将询问您要使用哪个应用程序（记得也要勾选**“一律使用此应用程序打开⋯⋯链接”** ）。 
    
    network.protocol-handler.warn-external.http
    network.protocol-handler.warn-external.https
    
###  纯文本模式与字体统一性

纯文本模式允许您在不使用 HTML 渲染的情况下查看所有电子邮件，可在菜单栏（可通过 `Alt` 键打开）的**查看(E) > 消息显示方式(B)** 中启用。默认情况下，它使用[等宽字体](<https://zh.wikipedia.org/wiki/%E7%AD%89%E5%AE%BD%E5%AD%97%E4%BD%93> "zhwp:等宽字体")，但字体大小仍然继承自原始系统字体配置设置。以下示例将使用 10 像素大小的 Ubuntu Mono 字体覆盖默认设置（可在 [ttf-ubuntu-font-family](<https://archlinux.org/packages/?name=ttf-ubuntu-font-family>)包 中找到）。 

请记得运行 `fc-cache -fv` 来更新系统字体缓存。更多信息请参见[字体配置](<../zh-cn/%E5%AD%97%E4%BD%93%E9%85%8D%E7%BD%AE.html> "字体配置")。 
    
    ~/.config/fontconfig/fonts.conf
    
    <?xml version="1.0"?>
    <!DOCTYPE fontconfig SYSTEM "fonts.dtd">
    <fontconfig>
      <match target="pattern">
        <test qual="any" name="family">
          <string>monospace</string>
        </test>
        <edit name="family" mode="assign" binding="same">
          <string>Ubuntu Mono</string>
        </edit>
        <!-- 对于 Thunderbird，将默认字体大小降低到 10，以实现统一性 -->
        <edit name="pixelsize" mode="assign">
          <int>10</int>
        </edit>
      </match>
    </fontconfig>
    
###  迁移个人资料到另一系统

**提示：**[ImportExportTools NG](<https://addons.thunderbird.net/thunderbird/addon/importexporttools-ng/>) 扩展提供了导出和导入配置文件夹选项。

在开始导入或导出任务之前，请完整备份 `~/.thunderbird` 配置文件夹： 
    
    $ cp -R ~/.thunderbird _/到/备份文件夹/_
    
通过迁移，您只需将当前的 Thunderbird 配置文件复制到另一台电脑或新的 Thunderbird 安装中： 

  1. 在目标电脑上安装 Thunderbird。
  2. 启动 Thunderbird 不做任何操作然后退出它。
  3. 从备份文件夹复制配置文件内容到目标配置文件夹：
         
         $ cp -R _/到/备份文件夹/_.thunderbird/<_原随机数_ >.default-release/* ~/.thunderbird/<_新生成随机数_ >.default-release/

###  导出和导入

在开始导入或导出任务之前，请完整备份 `~/.thunderbird` 配置文件夹： 
    
    $ cp -R ~/.thunderbird _/到/备份文件夹/_
    
如果你的账户出现问题或者你想合并两个不同的 Thunderbird 安装，你可以为这两个 Thunderbird 安装都安装 [ImportExportTools NG](<https://addons.thunderbird.net/thunderbird/addon/importexporttools-ng/>) 插件，然后只需将你所有的数据导出并导入到新的安装中。 

###  更改默认排序顺序

Thunderbird（至少到版本 31.4.0-1）按日期对邮件进行排序，默认将最早的邮件放在顶部，并且没有线程化显示。虽然这可以按每个文件夹进行更改，但更简便的方法是设置一个合理的默认值，如这里所述 [[3]](<https://superuser.com/questions/13518/change-the-default-sorting-order-in-thunderbird>)。 

在[#配置编辑器](<#%E9%85%8D%E7%BD%AE%E7%BC%96%E8%BE%91%E5%99%A8>)中设置以下偏好： 
    
    mailnews.default_sort_order = 2 _（降序）_
    mailnews.default_view_flags = 1 _（线程化视图）_
    
###  邮件目录（Maildir）支持

默认的消息存储格式是 mbox。要启用 Maildir 的使用，请参阅 [MozillaWiki:Thunderbird/Maildir](<https://wiki.mozilla.org/Thunderbird/Maildir> "mozillawiki:Thunderbird/Maildir")。基本方式是在[#配置编辑器](<#%E9%85%8D%E7%BD%AE%E7%BC%96%E8%BE%91%E5%99%A8>)中设置以下偏好： 
    
    mail.serverDefaultStoreContractID = @mozilla.org/msgstore/maildirstore;1
    
至少到版本 31.4.0-1 存在一些限制：只支持`tmp` 和 `cur` 目录。` new` 目录被完全忽略。邮件的已读状态存储在一个单独的 .msf 文件中，因此最初所有使用 Maildir 的本地邮件即使位于 `cur` 目录中也会被标记为未读。现在也可以在常规用户界面中更改此设置：转到**≡菜单 > 设置 > 常规 > 索引 > 新账户的消息存储类型：(T)** 并选择**为每条消息新建文件（maildir）** 。 

###  拼写检查

安装 [hunspell](<../zh-cn/%E8%AF%AD%E8%A8%80%E6%A3%80%E6%9F%A5.html> "Hunspell") 和 hunspell 语言词典，然后重启 Thunderbird。 

请参阅 Firefox 文章中的[如何设置默认拼写检查语言](<../zh-cn/Firefox.html#Firefox_%E4%B8%8D%E8%AE%B0%E4%BD%8F%E9%BB%98%E8%AE%A4%E6%8B%BC%E5%86%99%E6%A3%80%E6%9F%A5%E8%AF%AD%E8%A8%80> "Firefox")。 

###  原生通知

确保在[#配置编辑器](<#%E9%85%8D%E7%BD%AE%E7%BC%96%E8%BE%91%E5%99%A8>)中的 `mail.biff.use_system_alert` 设置为 `true`（默认）。这个选项意味着对于这些较新版本的 Thunderbird，不需要扩展（例如 Gnome 集成）来实现原生通知。 

可能还需要安装[通知服务器](</wzh/index.php?title=%E6%A1%8C%E9%9D%A2%E9%80%9A%E7%9F%A5&action=edit&redlink=1> "桌面通知（页面不存在）")（英语：[Desktop notifications#Notification servers](<https://wiki.archlinux.org/title/Desktop_notifications#Notification_servers> "en:Desktop notifications")）。 

###  系统托盘（tray）

可以在[Thunderbird#配置编辑器](<#%E9%85%8D%E7%BD%AE%E7%BC%96%E8%BE%91%E5%99%A8>)中将`mail.biff.show_tray_icon_always`和`mail.minimizeToTray`条目设置为`true`，以部分性实现托盘插件的功能。但是很遗憾，根据[bugzilla#1942125](<https://bugzilla.mozilla.org/show_bug.cgi?id=1942125>)和[bugzilla#1627479](<https://bugzilla.mozilla.org/show_bug.cgi?id=1627479>)，`mail.minimizeToTray`目前并没有在linux下的Thunderbird实装，。可以安装[Minimize on Close](<https://addons.thunderbird.net/zh-CN/thunderbird/addon/minimize-on-close/>)插件并通过修改插件文件里面`manifest.json`的`strict_max_version`限定的最高版本号安装来替代`mail.minimizeToTray`选项。如果需要其他系统托盘的功能，请自行查阅实现了相关功能的插件。 

[Betterbird的FAQ页面](<https://www.betterbird.eu/faq/index.html>)标明了他们完整的实现系统托盘的所有功能。 

###  声音提示

Thunderbird 可以配置为在接收到新邮件和日历提醒时播放声音。这需要 [libcanberra](<https://archlinux.org/packages/?name=libcanberra>)包。 

###  主题调整

Thunderbird 应该遵循系统上定义的 [GTK#主题](<../zh-cn/GTK.html#%E4%B8%BB%E9%A2%98> "GTK")。然而，为了达到完全一致的效果，调整是非常必要的。该调整对于深色主题尤其有益，使电子邮件正文的颜色与主题一致： 

  1. 转到**≡菜单 > 设置 > 常规**
  2. 找到**字体和颜色** 一栏
  3. 点击**颜色…(C)** 按钮
  4. 勾选**使用系统颜色(S)**
  5. 将**使用我在上面选择的颜色覆盖内容指定的颜色(O)** 选项设置为**一律** 或**仅在使用高对比度主题时**

进一步的定制可以通过创建和编辑一个 `userChrome.css` 文件来实现。请参阅 [Firefox/Tweaks#通用用户界面 CSS 设置](<../zh-cn/Firefox/%E5%BE%AE%E8%B0%83.html#%E9%80%9A%E7%94%A8%E7%94%A8%E6%88%B7%E7%95%8C%E9%9D%A2_CSS_%E8%AE%BE%E7%BD%AE> "Firefox/Tweaks")和 [MozillaZine 的 userChrome.css 页面](<https://kb.mozillazine.org/UserChrome.css>)。 

###  键盘快捷键

Thunderbird [遗憾地缺乏](<https://bugzilla.mozilla.org/show_bug.cgi?id=615957>)一种简单的方法来禁用单键快捷键（如按下 `a` 键会归档消息）。[tbkeys-lite](<https://addons.thunderbird.net/thunderbird/addon/tbkeys-lite/>) 扩展提供了一种编辑和删除这类快捷键的方式，并且适用于 Thunderbird 68.0 及以上版本。 

###  使用外部 GnuPG 进行 OpenPGP 加密

从版本 78.1 开始，Thunderbird 现在集成了以前由 Enigmail 等插件提供的 OpenPGP 支持。在更新后首次启动时，它会提示你将现有的 Enigmail 密钥迁移到 Thunderbird 中。如果你不想将私钥存储在 Thunderbird 内部，你可以使用外部 GnuPG 安装与 Thunderbird 结合来保证你的密钥安全或使用智能卡。 

查看存储在 Thunderbird 内的任何 OpenPGP 密钥： 

  1. 转到**菜单栏 > 工具(T) > OpenPGP 密钥管理器**
  2. 关闭**查看(V) > 显示来自其他人的密钥(O)** 以便更好地查看自己的密钥。私钥将以粗体显示。
  3. 查看现有密钥（也可通过此方法删除）。
  4. 通过**文件(F) > 从文件导入公钥(I)** 导入任何想要使用的外部私钥的公钥。参见 [GnuPG#导出公钥](<../zh-cn/GnuPG.html#%E5%AF%BC%E5%87%BA%E5%85%AC%E9%92%A5> "GnuPG")。

启用 Thunderbird 中的外部 GnuPG 支持： 

  1. 确保你有[相关密钥可用](<../zh-cn/GnuPG.html#%E6%9F%A5%E7%9C%8B%E5%AF%86%E9%92%A5> "GnuPG")或[创建相关密钥](<../zh-cn/GnuPG.html#%E5%88%9B%E5%BB%BA%E5%AF%86%E9%92%A5%E5%AF%B9> "GnuPG")。
  2. 打开[#配置编辑器](<#%E9%85%8D%E7%BD%AE%E7%BC%96%E8%BE%91%E5%99%A8>)
  3. 搜索 `mail.openpgp.allow_external_gnupg` 并将其值设置为 `true`
  4. 转到**≡菜单 > 账户设置**并选择你要使用的账户。
  5. 点击**管理标识…(M)** 并选择要编辑的身份。
  6. 点击**编辑…(E) > 端到端加密 > 添加密钥…(A)**。
  7. 选择**通过GnuPG使用您的外部密钥（例如：智能卡）** 并粘贴来自 GnuPG 的密钥 ID。

**注意：** 密钥 ID 是主密钥指纹的最后 16 个字符。

有关进一步的说明和专业配置，请参阅 [MozillaWiki:Thunderbird:OpenPGP:Smartcards](<https://wiki.mozilla.org/Thunderbird:OpenPGP:Smartcards> "mozillawiki:Thunderbird:OpenPGP:Smartcards")。 

### Wayland

从版本 128 开始，Thunderbird 默认使用 [Wayland](<../zh-cn/Wayland.html> "Wayland") 而非 XWayland，且无需任何配置。旧版 Thunderbird 则需通过设置[环境变量](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html> "环境变量")来启用 [Wayland](<../zh-cn/Wayland.html> "Wayland") 模式。 
    
    $ MOZ_ENABLE_WAYLAND=1 thunderbird
    
### Tor

要通过 Tor 网络路由到服务器的连接，必须相应地设置代理设置。 

  1. 确保你已经安装了 [tor](<https://archlinux.org/packages/?name=tor>)包 并且进程正在运行。
  2. 在 Thunderbird 中转到**≡菜单 > 设置 > 常规**。在**网络与磁盘空间 > 连接**部分，点击**设置…(S)** 按钮。
  3. 选择**手动配置代理(M)** ，在**SOCKS 主机栏** 输入`localhost`，端口使用`9050`（9050 是默认端口；可以在 /etc/tor/torrc 中进行不同配置）。勾选下方**使用 SOCKS v5 时 DNS 经过代理** 。

##  问题解决

###  LDAP 导致程序崩溃

在配置为使用 LDAP 获取用户信息的系统上会出现 [LDAP 冲突（Bugzilla#292127）](<https://bugzilla.mozilla.org/show_bug.cgi?id=292127>)。一个可能的[解决方案](<https://bugzilla.mozilla.org/show_bug.cgi?id=292127#c7>)是重命名冲突的捆绑 LDAP 库。 

###  错误：传入服务器已存在

如果你想重新安装一个之前删除过的具有相同账户数据的账户，可能会弹出 “传入服务器已存在”。详细情况请参阅 [Bugzilla#1121151](<https://bugzilla.mozilla.org/show_bug.cgi?id=1121151>)。不幸的是，如果你遇到这个错误，你现在只能清理后重新安装 Thunderbird： 

  1. 备份你当前的配置文件：
         
         $ cp -R ~/.thunderbird /to/backup/folder/

  2. 通过插件（如本页面的[#导出和导入](<#%E5%AF%BC%E5%87%BA%E5%92%8C%E5%AF%BC%E5%85%A5>)部分所述）导出所有账户、日历和订阅。
  3. 关闭 Thunderbird
  4. 删除你当前的所有 Thunderbird 数据 `rm -R ~/.thunderbird/`。
  5. 启动 Thunderbird
  6. 创建你的邮件账户、订阅和日历（空）。
  7. 安装 [ImportExportTools NG](<https://addons.thunderbird.net/thunderbird/addon/importexporttools-ng/>) 插件
  8. 导入所有数据。

###  接收新邮件时 Thunderbird 界面冻结

如果 Thunderbird 配置为在接收新邮件或启动时显示通知，而缺少通知守护进程可能会导致界面冻结（白屏）数秒。你可以通过禁用通知或安装一个[通知服务器](</wzh/index.php?title=%E6%A1%8C%E9%9D%A2%E9%80%9A%E7%9F%A5&action=edit&redlink=1> "桌面通知（页面不存在）")（英语：[Desktop notifications#Notification servers](<https://wiki.archlinux.org/title/Desktop_notifications#Notification_servers> "en:Desktop notifications")）来解决这个问题。 

###  不遵守 LC_TIME 环境变量

Thunderbird 应该使用 `LC_TIME` 环境变量来进行本地化，但在所有上下文中可能并不总是如此。一些问题可以通过设置**≡菜单 > 设置 > 常规 > 语言与外观 > 日期和时间格式**为**区域设置语言区域** 来缓解，这一设置是在 Thunderbird 56 版本中引入的。 

从版本 60 开始，Gecko 开始使用 [CLDR 项目](<https://cldr.unicode.org/>)进行本地化，包括日期时间格式化，CLDR 使用的设置与大多数其他基于 `LC_TIME` 的软件不同。有一个 [Bug 报告](<https://bugzilla.mozilla.org/show_bug.cgi?id=1426907>)记录了这个问题，并包含了一些效果不一的变通方法。要在 Thunderbird 中实现 ISO-8601 格式的日期并让星期一作为星期开始，可以使用 `LC_TIME=lt_LT thunderbird` 启动 Thunderbird。 

从 Thunderbird 版本 91 开始，可以设置一些偏好来使 Thunderbird 符合 ISO-8601。大多数程序可以通过将你的区域语言设置为 `en_DK` 来设置为 ISO-8601，但默认情况下 Thunderbird 忽略区域语言偏好。详情请参见 [[4]](<https://support.mozilla.org/en-US/kb/customize-date-time-formats-thunderbird>)。 

###  使用 OAuth2 与 G Suite 账户时出现“连接到服务器 imap.gmail.com 时认证失败”错误

有时，Thunderbird 在使用 G Suite 账户登录时会出现“连接到服务器 imap.gmail.com 时认证失败”的错误。这可以通过在[#配置编辑器](<#%E9%85%8D%E7%BD%AE%E7%BC%96%E8%BE%91%E5%99%A8>)中将 `general.useragent.compatMode.firefox` 设置为 `true` 来修复，然后再次进行认证。 

###  Outlook 365 SMTP 使用 OAuth2 认证失败

显然，默认情况下，Outlook 365 账户的 SMTP 认证是禁用的。请使用 Microsoft 365 管理中心来启用它。参见[为特定邮箱启用 SMTP 身份验证](<https://learn.microsoft.com/zh-cn/exchange/clients-and-mobile-in-exchange-online/authenticated-client-smtp-submission#enable-smtp-auth-for-specific-mailboxes>)。 

###  难以使用 Thunderbird 访问 Outlook 365 账户

Thunderbird 102.7.0 版本中对 OAuth2 实现进行了更改，这影响到了对 Outlook 365 账户的访问（参见 [[5]](<https://www.thunderbird.net/en-US/thunderbird/102.7.0/releasenotes/>) 和 [[6]](<https://bugzilla.mozilla.org/show_bug.cgi?id=1810760>)）。受影响的用户应直接升级到 102.7.1 或更高版本。 

###  无法登录 Outlook 365 账户

如果在被重定向到机构的登录页面后，输入凭证并点击登录按钮，又被重定向回相同的登录页面，可以尝试以下操作： 

  1. 通过**菜单栏 > 工具(T) > 清除最近历史记录…(H)** 清除 Cookie 和缓存，在**要清除的时间范围：(T)** 中选择**全部** ，在**历史记录** 中勾选**浏览历史记录(B)** 、**Cookie** 和**缓存(A)** ，点击**立即清空** 。
  2. 在**≡菜单 > 设置 > 隐私与安全**的**网页内容** 部分勾选**接受站点的 Cookie(A)** 来启用 Cookie。
