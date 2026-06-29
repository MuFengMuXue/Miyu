相关文章

  * [通用第二因素](<../zh-cn/%E9%80%9A%E7%94%A8%E7%AC%AC%E4%BA%8C%E5%9B%A0%E7%B4%A0.html> "通用第二因素")
  * [OATH](</wzh/index.php?title=OATH&action=edit&redlink=1> "OATH（页面不存在）")
  * [dm-crypt/加密整个系统](<../zh-cn/Dm-crypt/%E5%8A%A0%E5%AF%86%E6%95%B4%E4%B8%AA%E7%B3%BB%E7%BB%9F.html> "Dm-crypt/加密整个系统")
  * [PAM](<../zh-cn/PAM.html> "PAM")
  * [GnuPG](<../zh-cn/GnuPG.html> "GnuPG")
  * [KeePass](</wzh/index.php?title=KeePass&action=edit&redlink=1> "KeePass（页面不存在）")
  * [OpenPGP-card-tools](</wzh/index.php?title=OpenPGP-card-tools&action=edit&redlink=1> "OpenPGP-card-tools（页面不存在）")
  * [Smartcards](</wzh/index.php?title=Smartcards&action=edit&redlink=1> "Smartcards（页面不存在）")

**翻译状态：**

  * 本文（或部分内容）译自 [YubiKey](<https://wiki.archlinux.org/title/YubiKey> "arch:YubiKey")，最近一次同步于 2025-02-01，若英文版本有所[更改](<https://wiki.archlinux.org/title/YubiKey?diff=0&oldid=824578>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/YubiKey_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[YubiKey](<https://www.yubico.com>) 是一个小型 [USB 安全令牌](<https://zh.wikipedia.org/wiki/%E5%AE%89%E5%85%A8%E4%BB%A4%E7%89%8C> "zhwp:安全令牌")。取决于型号不同，它可以： 

  * 作为智能卡使用（通过 [CCID 协议](<https://en.wikipedia.org/wiki/CCID_\(protocol\)> "wikipedia:CCID \(protocol\)")）- 可以存储 [PGP](<https://developers.yubico.com/PGP/>) 和 [PIV](<https://developers.yubico.com/PIV/>) 私钥
  * 处理[通用第二因素](<../zh-cn/%E9%80%9A%E7%94%A8%E7%AC%AC%E4%BA%8C%E5%9B%A0%E7%B4%A0.html> "通用第二因素")（U2F）请求
  * 存储和读取约 30 条[开放身份验证](</wzh/index.php?title=Initiative_for_Open_Authentication&action=edit&redlink=1> "Initiative for Open Authentication（页面不存在）")（OATH）凭证
  * 以 Yubico OTP 或 HMAC-SHA1 模式处理[质询-应答请求](<https://en.wikipedia.org/wiki/Challenge%E2%80%93response_authentication> "wikipedia:Challenge–response authentication")
  * 生成[一次性密码](<https://zh.wikipedia.org/wiki/%E4%B8%80%E6%AC%A1%E6%80%A7%E5%AF%86%E7%A2%BC> "zhwp:一次性密码")（OTP）- [基于 AES 的 Yubico 标准](<https://developers.yubico.com/OTP/>).
  * “输入”最长 63 个字符的固定密码

虽然功能丰富，但新版 YubiKey [并不开源](<https://www.yubico.com/blog/secure-hardware-vs-open-source/>)。其它替代品有 [Solo](</wzh/index.php?title=Solo&action=edit&redlink=1> "Solo（页面不存在）")，[TKey](</wzh/index.php?title=Tillitis_TKey&action=edit&redlink=1> "Tillitis TKey（页面不存在）") 和 [Nitrokey](</wzh/index.php?title=Nitrokey&action=edit&redlink=1> "Nitrokey（页面不存在）")。 

##  安装

###  管理工具

  * **YubiKey Manager** — 通过 USB 配置并读取 YubiKey 的 Python 库和命令行工具（`ykman`）。带有可选图形界面。

     <https://developers.yubico.com/yubikey-manager/> || [yubikey-manager](<https://archlinux.org/packages/?name=yubikey-manager>)包，[yubikey-manager-qt](<https://archlinux.org/packages/?name=yubikey-manager-qt>)包

**注意：** 安装后，[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用") `pcscd.service`。

**警告：** 在新的 Arch/python/yubikey-manager 版本上，[yubikey-manager-qt](<https://archlinux.org/packages/?name=yubikey-manager-qt>)包 已经[完全无法使用](<https://github.com/Yubico/yubikey-manager-qt/issues/361>)，且 Yubico [已废弃该工具](<https://github.com/Yubico/yubikey-manager-qt/commit/28dc02d11b081683b59d16d12043aaa3c0a6c75f>)。

  * **YubiKey Personalization** — 通过 OTP USB 配置并读取 YubiKey 的库和工具。比 ykman 更强，但更难用，带有可选图形界面。

     <https://developers.yubico.com/yubikey-personalization/> || [yubikey-personalization](<https://archlinux.org/packages/?name=yubikey-personalization>)包，[yubikey-personalization-gui](<https://archlinux.org/packages/?name=yubikey-personalization-gui>)包

###  认证工具

  * **Yubico PAM** — 使用 Yubico OTP 或质询-应答进行 [PAM](<../zh-cn/PAM.html> "PAM") 用户认证。

     <https://developers.yubico.com/yubico-pam/> || [yubico-pam](<https://archlinux.org/packages/?name=yubico-pam>)包

  * **Yubico PAM-U2F** — 使用 [U2F](<../zh-cn/%E9%80%9A%E7%94%A8%E7%AC%AC%E4%BA%8C%E5%9B%A0%E7%B4%A0.html> "U2F") 进行 [PAM](<../zh-cn/PAM.html> "PAM") 用户认证。

     <https://developers.yubico.com/pam-u2f/> || [pam-u2f](<https://archlinux.org/packages/?name=pam-u2f>)包

  * **Yubico Authenticator for Desktop** — 通过 USB 从 YubiKey 读取 OATH 代码的图形工具。支持新的 OATH 实现（例如 YubiKey NEO 和 4）和旧版基于槽位的实现（例如 YubiKey Standard 和 Edge）。注意：[archlinux/packaging/packages/yubioath-desktop#2](<https://gitlab.archlinux.org/archlinux/packaging/packages/yubioath-desktop/-/issues/2>)

     <https://developers.yubico.com/OATH/YubiKey_OATH_software.html> || [yubioath-desktop](<https://archlinux.org/packages/?name=yubioath-desktop>)包

  * **Yubico Authenticator 6.0+ for Desktop** — Yubico Authenticator 6.0+（6.0 及更高版本）是用于管理 YubiKey 双因素凭证的工具。从 6.0 版本开始，其使用 Flutter 框架完全重写。

     <https://developers.yubico.com/yubioath-flutter/> || [yubico-authenticator-bin](<https://aur.archlinux.org/packages/yubico-authenticator-bin/>)AUR

  * **libfido2** — 客户端侧 U2F 支持，使浏览器可以通过 U2F 协议使用 YubiKey 进行认证。

     <https://developers.yubico.com/libfido2/> || [libfido2](<https://archlinux.org/packages/?name=libfido2>)包

  * **YubiKey 全盘加密** — 使用质询-响应模式创建强 LUKS 密码。支持全盘加密。

     <https://github.com/agherzan/yubikey-full-disk-encryption> || [yubikey-full-disk-encryption](<https://archlinux.org/packages/?name=yubikey-full-disk-encryption>)包

##  输入

YubiKey 接受通过 USB 传入的 API 调用和按钮输入。 

YubiKey 的按钮非常灵敏。根据场景不同，触碰按钮会出现以下效果之一： 

  * 触发固定密码输入或一次性密码（OTP）（短按是槽 1，长按是槽 2）。这是默认行为，很容易会不小心触发。
  * 确认 / 允许功能或访问，LED 会在这时发光提示用户。
  * 插入 / 弹出智能卡

##  输出

YubiKey 会将这些输入转换为输出： 

  * 按键输入（模拟为 USB 键盘），用于输入固定密码和 OTP。（注意，固定密码无法防范键盘窃听器。）
  * 内置 LED： 
    * 插入时闪烁，方便排障
    * 在需要触碰按钮对 API 响应授权时闪烁
  * 通过 USB 发送 API 响应，用于： 
    * 质询-响应请求（使用 Yubico OTP 或 HMAC-SHA1 模式进行计算）
    * U2F 质询-响应请求
    * CCID 智能卡相关请求

##  USB 连接模式

取决于 YubiKey 型号不同，设备提供了最多三种不同的 USB 界面。其中两种实现了 USB HID（人机交互设备）类，第三种是智能卡接口（CCID）。三种接口可以分别被启用或禁用，以控制对应协议。 

以下表格展示了接口对应的协议： 

协议 | 接口   
---|---  
OTP | 键盘 HID   
FIDO | 其它 HID   
PIV | CCID   
OpenPGP | CCID   
OATH | CCID   
  
`ykman` 使用了“模式”一词，将其命名为 OTP、FIDO 和 CCID。 

**注意：** ykman 从 0.6.1（2018-04-16）版本开始将“U2F”改名为“FIDO”。<https://developers.yubico.com/yubikey-manager/Release_Notes.html>

###  获取已启用的模式

对于版本 5 前的 YubiKey： 
    
    $ ykman config mode
    
    Current connection mode is: OTP+FIDO+CCID
    
**注意：**`ykman mode` 命令已被废弃，后续可能会被移除。

对于 YubiKey 5： 
    
    $ ykman info
    
    Device type: YubiKey 5 NFC
    Serial number: XXXXXXXXX
    Firmware version: 5.4.3
    Form factor: Keychain (USB-A)
    Enabled USB interfaces: OTP, FIDO, CCID
    NFC transport is enabled.
    
    Applications    USB     NFC
    FIDO2           Enabled Enabled
    OTP             Enabled Enabled
    FIDO U2F        Enabled Enabled
    OATH            Enabled Enabled
    YubiHSM Auth    Enabled Enabled
    OpenPGP         Enabled Enabled
    PIV             Enabled Enabled
    
###  配置模式

出厂时所有模式都会被启用。要修改配置，请使用如下命令： 
    
    $ ykman mode _[OPTIONS]_ _MODE_
    
  * `_MODE_` 可以是字符串（如 `OTP+FIDO+CCID`）或是简写形式（如 `o+f+c`）。
  * `_MODE_` 也可以是模式编号，编码了数种启用的模式。

以下为模式编号表： 

0 | 仅作为 OTP 设备   
---|---  
1 | 仅作为 CCID 设备   
2 | OTP/CCID 复合设备   
3 | 仅作为 U2F 设备   
4 | OTP/U2F 复合设备   
5 | U2F/CCID 复合设备   
6 | OTP/U2F/CCID 复合设备   
81 | 仅作为 CCID 设备，附带触摸弹出功能   
  
**注意：** 有些范例使用了[无效](<https://github.com/Yubico/yubikey-manager/issues/20#issuecomment-326496204>)的模式编号 86。80 会被忽略掉，并作为编号 6 使用。

选项： 

  * `--touch-eject` \- 按钮将用于插入和弹出智能卡，只在仅 CCID 模式可用，需要禁用 FIDO 和 OTP
  * `--autoeject-timeout _SECONDS_` \- 一定时间后自动弹出智能卡，限制与 `--touch-eject` 相同
  * `--chalresp-timeout _SECONDS_` \- 设置质询-响应超时时间

更多信息请参考 `ykman mode --help`。 

##  一次性密码

该功能的名称有些误导，因为它还包括静态密码和质询-响应功能。 

该功能有两个槽位，可以分别通过短按和长按进行访问。两者都可以被配置为以下功能**之一** ： 

  * Yubico OTP
  * OATH-HOTP
  * OATH-TOTP
  * 质询-响应
  * 固定密码

每个功能在创建时都有多个配置选项，但在创建完成后无法被再次读取。使用 `ykman otp swap` 可以互换槽 1 和槽 2. 

###  出厂配置

对于新出厂的 YubiKey，槽 1 默认配置为 Yubico OTP。该初始 AES 对称密钥同时被存储在 YubiKey 和 Yubico 认证服务器上，这样就可以通过 YubiCloud 进行验证，以在 Yubico 论坛或 <https://demo.yubico.com> 等使用 Yubico OTP 进行认证。 

**警告：** 如果你覆写掉了槽 1 的出厂密钥，就无法再次创建同等信任度的新密钥。出厂生成的 Yubico OTP 凭证以 `CC` 开头，用户生成的凭证以 `VV` 开头。两者在安全和功能性上没有区别，但有的服务只信任 `CC` 开头的凭证。更多信息请参考[该论坛帖子](<https://forum.yubico.com/viewtopic12ca.html?f%3D16&t%3D1960>)。

### Yubico OTP

[Yubico OTP](<https://developers.yubico.com/OTP/>) 基于[对称密钥加密](<https://zh.wikipedia.org/wiki/%E5%B0%8D%E7%A8%B1%E5%AF%86%E9%91%B0%E5%8A%A0%E5%AF%86> "zhwp:对称密钥加密")。具体来说，每个 YubiKey 都包含了该设备独有的 [AES](<https://zh.wikipedia.org/wiki/%E9%AB%98%E7%BA%A7%E5%8A%A0%E5%AF%86%E6%A0%87%E5%87%86> "zhwp:高级加密标准") 密钥，并同时存储在验证服务器上。当被要求输入密码时，YubiKey 将使用如密钥 ID、计数器和随机数等不同字段创建一个令牌，并对结果进行加密。 

然后该 OTP 将被发送到目标系统，之后传到验证服务器上。接着，验证服务器（其同时拥有私钥）会将其解密并验证内容，之后将结果发送到目标系统上，由目标系统决定是否授权。 

####  YubiCloud 和验证服务器

Yubico 提供了被称为 YubiCloud 的验证服务器，提供了免费无限制访问。YubiCloud 记录了所有 YubiKey 的出厂配置，且是 [yubico-pam](<https://archlinux.org/packages/?name=yubico-pam>)包 等的“默认”验证服务。Yubico 还提供了服务器的[开源实现](<https://developers.yubico.com/Software_Projects/Yubico_OTP/YubiCloud_Validation_Servers/>)。 

**注意：** 要验证 Yubico 验证服务器，可以使用： 

  * **HMAC** ：通过 <https://upgrade.yubico.com/getapikey/> 获取一个 HMAC 密钥和 ID
  * **HTTPS** ：验证服务器的证书由 GoDaddy 进行签名，因此默认受 Arch 信任（前提是至少安装了 [ca-certificates](<https://archlinux.org/packages/?name=ca-certificates>)包）。

####  配置和用法

在槽 2 生成新密钥，然后上传到 YubiCloud（会在浏览器中打开）： 
    
    $ ykman otp yubiotp --generate-key --upload 2
    
更多信息请参考 `ykman otp yubiotp --help`。 

####  安全风险

#####  AES 密钥泄漏

可想而知，AES 密钥必须保密，该密钥无法从 YubiKey 上被读取（或者说至少软件上不可行）。密钥同时被存放在验证服务器上，因此必须确保该服务器的安全。 

#####  篡改验证请求/响应

鉴于目标系统依赖于验证服务器，因此攻击方式之一是假冒该服务器。因此，目标系统必须使用 HMAC 或 HTTPS 对验证服务器进行验证。 

###  质询-应答

质询会发送到 YubiKey，然后基于 secret 计算出应答。同一个质询会得出相同的应答。就算有大量的质询-响应对，在没有 secret 的情况下反推计算操作是不可能的。 

这可以被用于： 

  * 事实上的双因素认证：质询被提供给用户，用户必须与密码一起提供正确的响应。双方都需要持有私钥。
  * “半”双因素认证：质询被用作密码，然后服务器会存储正确的响应。该操作与 OTP 不同，且持有正确响应的人都能获得授权；但由于不需要私钥，实现难度较低。

有两种质询-响应算法： 

  * HMAC-SHA1
  * Yubico OTP

你可以使用 [yubikey-personalization-gui](<https://archlinux.org/packages/?name=yubikey-personalization-gui>)包 通过图形界面进行配置，也可以遵循以下步骤： 

####  HMAC-SHA1 算法

将槽 2 配置为质询-响应模式，并生成一个密钥： 
    
    $ ykman otp chalresp --generate 2
    
可以省略掉 `--generate` 并手动指定密钥（参考 `ykman otp chalresp --help`），这么做的好处是可以用同一密钥配置其它备用设备。可以使用 `openssl rand -hex 20` 生成可用密钥。 

####  Yubico OTP 算法

`ykman` 貌似不支持配置 chal-yubico 算法，但可以使用 `ykpersonalize` 进行配置。在槽 2 生成一个随机密钥： 
    
    $ ykpersonalize -2 -ochal-resp -ochal-yubico
    
更多信息请参考 [ykpersonalize(1)](<https://man.archlinux.org/man/ykpersonalize.1>)。 

####  发送质询

可以使用 `ykchalresp -_slot_ _challenge_` 发送质询并获得响应，例如： 
    
    $ ykchalresp -2 _archie_
    
    12a19763be77d75af46fb76f0b737c117fa47205
    
将返回特定于槽 2 的 40 字节 SHA1 哈希值。不同的质询将返回不同的响应。 

###  固定密码

你也可以生成固定密码： 
    
    $ ykman otp static --generate _slot_
    
或者手动提供一个： 
    
    $ ykman otp static _slot_ _password_
    
该命令有多个选项：可以设置密码的长度和字符，也可以设置最后是否会按下确认键。具体选项请参考 `ykman otp static --help`。 

**提示：** Most YubiKeys provide only limited (2) slots to save static passwords. A setup challenge-response slot provides static hash responses for unlimited challenges. While these are numeric and lower alphabet only, the response length provides considerable entropy.

###  模拟 USB 键盘的限制（又称“为什么我的密码看着很弱？”）

为使 YubiKey 与大多数键盘布局兼容，密码默认只能由 ModHex 字母表（`cbdefghijklnrtuv`）、数字 `0-9` 和 `!` 构成。这些字符在大量键盘布局中使用相同的扫描代码，以确保与大多数计算机兼容。 

相关信息可参考 Yubico 提供的[白名单](<https://resources.yubico.com/53ZDUYE6/as/9hccqgx9bwwqq96mhkk8jb4h/Static_Password_Function.pdf>)。 

## OATH

YubiKey 提供了两种 [OATH](</wzh/index.php?title=OATH&action=edit&redlink=1> "OATH（页面不存在）") 实现： 

OATH API：新实现，取决于型号不同，可以存储约 30 个凭证。（YubiKey 4、NEO 及更新版本）
OTP 槽：旧实现，两个 OTP 槽都分别只能存储单个凭证。（所有支持质询-响应的型号都可用）

### OATH API

如果更偏好图形界面，可以使用 [yubioath-desktop](<https://archlinux.org/packages/?name=yubioath-desktop>)包。 

`ykman` 可以通过 `ykman oath uri` 以 URI 形式添加代码。以下为从二维码图片添加凭证的示例： 
    
    $ zbarimg qr_code.png --quiet --raw | xargs ykman oath accounts uri
    
你也可以手动进行添加。配置 TOTP 密钥，并要求触摸按钮后才能生成代码： 
    
    $ ykman oath accounts add --touch _name_ _secret_
    
配置 HOTP 密钥： 
    
    $ ykman oath accounts add --oath-type HOTP _name_ _secret_
    
列出凭证： 
    
    $ ykman oath accounts list
    
生成代码： 
    
    $ ykman oath accounts code _query_
    
所有可用的子命令请参考 `ykman oath --help`。要查看单个命令的选项，请使用 `ykman oath _subcommand_ --help`。 

###  OTP 槽实现

在槽 2 中配置 HOTP： 
    
    $ ykman otp hotp 2 _key_
    
配置 TOTP： 
    
    $ ykman otp chalresp --totp _slot_ _key_
    
生成 HOTP 代码： 
    
    $ ykman otp calculate _slot_
    
生成 TOTP 代码： 
    
    $ ykman otp calculate --totp _slot_
    
另请参考 `ykman otp --help` 和 <https://developers.yubico.com/OATH/> 。 

## U2F

通过 YubiKey 使用[通用第二因素](<../zh-cn/%E9%80%9A%E7%94%A8%E7%AC%AC%E4%BA%8C%E5%9B%A0%E7%B4%A0.html> "通用第二因素") (U2F) 非常简单，不需要对密钥本身进行配置。注意，在部分文档和工具中，该模式也被称作“FIDO”。`ykman` 上的管理配置项比较少： 

  * 设置 PIN 码：`ykman fido access change-pin`
  * 删除单个凭证：`ykman fido credentials delete _QUERY_`
  * 重置所有凭证和 PIN 码：`ykman fido reset`

使用 U2F 进行认证的方法请参考 [U2F](<../zh-cn/%E9%80%9A%E7%94%A8%E7%AC%AC%E4%BA%8C%E5%9B%A0%E7%B4%A0.html> "U2F")。 

另请参考 [WebAuthn](</wzh/index.php?title=WebAuthn&action=edit&redlink=1> "WebAuthn（页面不存在）")。 

##  CCID 智能卡

CCID（芯片卡接口设备）是一个 USB 标准设备类，适用于 USB 智能卡读卡器或类似通过 YubiKey 等通过 USB 连接的安全令牌。HID（人机交互设备）和 CCID 都是 USB 设备类，即它们都位于 USB 标准的同一类别。HID 是类似键盘等计算机外设的标准。在 OTP 和 FIDO 模式下，YubiKey 类似于 USB（HID）键盘；在使用 PIV 应用或作为 OpenPGP 设备时，会切换到 CCID 协议。 

从 2015 年 11 月开始，所有新出厂的 YubiKey 都应默认启用了 CCID 模式[[1]](<https://www.yubico.com/support/knowledge-base/categories/articles/use-yubikey-yubikey-windows-hello-app/>)。Enable at least the CCID mode. Please see [#获取已启用的模式](<#%E8%8E%B7%E5%8F%96%E5%B7%B2%E5%90%AF%E7%94%A8%E7%9A%84%E6%A8%A1%E5%BC%8F>). 

### PIV

从 YubiKey NEO 开始，YubiKey 在芯片中内置了 PIV（个人身份验证）应用。PIV 是一个美国政府标准（FIPS 201），指定了使用 RSA 或 ECC（椭圆曲线密码学）的令牌如何被用于个人电子身份认证。YubiKey NEO 只支持 RSA 加密，后续型号（包括 YubiKey 4 和 5）支持 RSA 和 ECC，具体支持的算法取决于固件。例如，只有 5.7 及更新版本的 YubiKey 支持 RSA 3072、RSA 4096、Ed25519 和 X25519 密钥[[2]](<https://developers.yubico.com/PIV/Introduction/YubiKey_and_PIV.html>)。PIV 令牌的特性是可以保护私钥并在芯片片上执行操作，私钥在安装到令牌上后就无法被导出。私钥也可以通过芯片内置的随机数生成器直接在芯片上生成，在这种情况下，私钥完全不会暴露出芯片外，也无法从令牌上恢复。在使用 PIV 特性时，YubiKey 是作为 CCID 设备工作的。 

###  OpenPGP 智能卡

YubiKey 可以作为标准 OpenPGP 智能卡工作，具体搭配 [GnuPG](<../zh-cn/GnuPG.html> "GnuPG") 进行配置和使用的步骤请参考 [GnuPG#智能卡](<../zh-cn/GnuPG.html#%E6%99%BA%E8%83%BD%E5%8D%A1> "GnuPG")。Yubico 也提供了一些文档：<https://developers.yubico.com/PGP/> 。 

如果你不想使用其它功能（如 U2F 和 OTP），可以将按钮配置为插入和弹出智能卡，也可以配置自动弹出时间。具体信息请参考 [#USB 连接模式](<#USB_%E8%BF%9E%E6%8E%A5%E6%A8%A1%E5%BC%8F>)。 

默认用户 PIN 码是 `123456`，默认管理员密码和 PUK 是 `12345678`。别忘了改掉这三个密码。 

##  用例

本节展示了如何使用 YubiKey 进行多种身份验证，实际上能做到的比这还多。 

###  使用 LUKS 进行全盘加密

有数种实现方案： 

  * **质询-响应** ：将对质询的[响应](<#%E8%B4%A8%E8%AF%A2-%E5%93%8D%E5%BA%94>)用作 LUKS 密钥。质询可被用作双因素认证中的密码，也可为单因素认证以纯文本形式存储。
  * **GnuPG** ：使用 Yubikey 的 [PGP 智能卡](<#CCID_%E6%99%BA%E8%83%BD%E5%8D%A1>)功能，在不需要强密码的同时提供强双因素认证。
  * **FIDO HMAC Secret** ：如果拟定 YubiKey 支持 [U2F](<../zh-cn/%E9%80%9A%E7%94%A8%E7%AC%AC%E4%BA%8C%E5%9B%A0%E7%B4%A0.html> "U2F")，可让其返回对称 secret。

**注意：** 硬盘的加密安全性仅与其最弱的密钥等同。在配置完这几项之一后，考虑移除初始密码或替换为超长密码。

####  常见依赖

  * 一个可启动的 [LUKS 加密](<../zh-cn/Dm-crypt/%E5%8A%A0%E5%AF%86%E6%95%B4%E4%B8%AA%E7%B3%BB%E7%BB%9F.html> "Dm-crypt/加密整个系统")系统，使用 `encrypt` [mkinitcpio](<../zh-cn/Mkinitcpio.html> "Mkinitcpio") 钩子，并有至少一个可用槽位。 
    * [mkinitcpio-ykfde](<https://aur.archlinux.org/packages/mkinitcpio-ykfde/>)AUR 除外，`sd-encrypt` 钩子不受上述任一方案支持。
  * 备份 LUKS header（可选，但建议）

####  质询-应答

完整步骤请参考 [yubikey-full-disk-encryption](<https://archlinux.org/packages/?name=yubikey-full-disk-encryption>)包 的[官方文档](<https://github.com/agherzan/yubikey-full-disk-encryption#usage>)。简单来讲： 

  1. 安装 [yubikey-full-disk-encryption](<https://archlinux.org/packages/?name=yubikey-full-disk-encryption>)包
  2. 配置 `/etc/ykfde.conf`
  3. 注册硬盘：`# ykfde-enroll -d /dev/_DISK_ -s _LUKS_SLOT_`
  4. 在 `encrypt` 钩子前添加 `ykfde` [mkinitcpio 钩子](<../zh-cn/Mkinitcpio.html#%E9%92%A9%E5%AD%90%EF%BC%88HOOKS%EF%BC%89> "Mkinitcpio")
  5. [重新生成 initramfs](<../zh-cn/%E9%87%8D%E6%96%B0%E7%94%9F%E6%88%90_initramfs.html> "重新生成 initramfs")

**注意：** 对于 Plymouth 用户：将 `plymouth-encrypt` 替换为 `ykfde` 钩子。

该方案有数个变种： 

  * 2FA：默认行为，在注册设备和启动时需要将质询作为密码提供.
  * 1FA：在 `ykfde.conf` 中设置 `YKFDE_CHALLENGE`。注意，这是以纯文本保存的，请考虑为该文件禁用非根用户读取权限。
  * [NFC 支持](<https://github.com/agherzan/yubikey-full-disk-encryption#enable-nfc-support-in-ykfde-initramfs-hook-experimental>)（实验性）
  * [待机和唤醒支持](<https://github.com/agherzan/yubikey-full-disk-encryption#enable-ykfde-suspend-service-experimental>)（实验性）在待机时自动锁定加密卷，恢复时解锁

为使配置生效，需要重新生成 initramfs。 

####  基于 systemd 的 initramfs

`sd-encrypt` 钩子的用户可以安装 [mkinitcpio-ykfde](<https://aur.archlinux.org/packages/mkinitcpio-ykfde/>)AUR 或 [mkinitcpio-ykfde-git](<https://aur.archlinux.org/packages/mkinitcpio-ykfde-git/>)AUR，然后遵循[项目文档](<https://github.com/eworm-de/mkinitcpio-ykfde/blob/master/README-mkinitcpio.md>)中的操作描述。具体步骤与 [yubikey-full-disk-encryption](<https://archlinux.org/packages/?name=yubikey-full-disk-encryption>)包 大致类似。 

#### GnuPG encrypted keyfile

One tool to accomplish this is [initramfs-scencrypt](<https://github.com/fuhry/initramfs-scencrypt>); see its docs for complete instructions. Note that as of October 2022 this package is not in the AUR and is not thoroughly tested, though the GitHub repository offers a PKGBUILD. 

The [dm-crypt pages](</wzh/index.php?title=Dm-crypt/%E7%89%B9%E6%AE%8A%E6%83%85%E5%86%B5&action=edit&redlink=1> "Dm-crypt/特殊情况（页面不存在）") offer a few alternatives, though they are mostly links to old forum posts. 

#### HMAC secret extension of FIDO2 protocol

Yet another way of using YubiKey for full disk encryption is to utilize [HMAC Secret Extension](<https://fidoalliance.org/specs/fido-v2.0-id-20180227/fido-client-to-authenticator-protocol-v2.0-id-20180227.html#sctn-hmac-secret-extension>) to retrieve the LUKS password from YubiKey. This can be protected by a passphrase. This functionality requires at least [YubiKey 5 with firmware 5.2.3+](<https://support.yubico.com/hc/en-us/articles/360016649319-YubiKey-5-2-3-Enhancements-to-FIDO-2-Support>). For a passphrase protected solution, install [khefin](<https://aur.archlinux.org/packages/khefin/>)AUR and follow instructions available in [project documentation](<https://github.com/mjec/khefin/wiki/Arch-Linux-LUKS-configuration>). For single factor (optionally PIN-protected) solution and starting with systemd 248, it is possible to use your FIDO2 key as LUKS2 keyslot. Instructions available in the [author's blog post](<https://0pointer.net/blog/unlocking-luks2-volumes-with-tpm2-fido2-pkcs11-security-hardware-on-systemd-248.html>). 

### KeePass

可以为 [KeePass](</wzh/index.php?title=KeePass&action=edit&redlink=1> "KeePass（页面不存在）") 配置 YubiKey 支持，具体步骤请参考 [YubiKey 一节](</wzh/index.php?title=KeePass&action=edit&redlink=1> "KeePass（页面不存在）")。 

###  SSH 密钥

#### CCID

如果你的 YubiKey 支持 CCID 智能卡，可以基于 GPG 或 PIV 密钥将其用作基于硬件的 [SSH 密钥](<../zh-cn/SSH_%E5%AF%86%E9%92%A5.html> "SSH 密钥")。Yubico 提供了详细的文档： 

  * 两者用途和优缺点的[概述](<https://developers.yubico.com/PIV/Guides/Securing_SSH_with_OpenPGP_or_PIV.html>)
  * Instructions for [PGP 认证](<https://developers.yubico.com/PGP/SSH_authentication/index.html>)
  * Instructions for [通过用户证书进行 PIV 认证](<https://developers.yubico.com/PIV/Guides/SSH_user_certificates.html>)
  * Instructions for [通过 #PKCS11 进行 PIV 认证](<https://developers.yubico.com/PIV/Guides/SSH_with_PIV_and_PKCS11.html>)

**注意：** YubiKey 的 PIV 应用默认 PIN 码是 `123456`，你可能会想修改它和默认管理密码。详细信息请参考[设备配置方法](<https://developers.yubico.com/PIV/Guides/Device_setup.html>)。

#### U2F

你也可以通过 YubiKey 的 U2F 功能创建基于硬件的 SSH 密钥。具体步骤请参考 [SSH 密钥#FIDO/U2F](<../zh-cn/SSH_%E5%AF%86%E9%92%A5.html#FIDO/U2F> "SSH 密钥")。 

#### PIV

[yubikey-agent](<https://aur.archlinux.org/packages/yubikey-agent/>)AUR 以 PIV 令牌的显示存储 SSH 密钥。配置步骤请参考 <https://github.com/FiloSottile/yubikey-agent#readme> 。 

###  使用 PAM 进行 Linux 用户认证

[PAM](<../zh-cn/PAM.html> "PAM") 及所有使用 PAM 进行用户验证的软件都可使用 YubiKey 作为用户验证的一环，其中包括 sudo、su、ssh、锁屏、显示管理器及几乎所有 Linux 系统上需要对用户进行验证的地方，灵活的配置项使你可以为整个系统、特定应用或一组应用设定认证需求。例如，你可以在本地会话上用 YubiKey 取代密码，但在远程会话上要求同时使用二者。除了 Arch Wiki 外，建议额外阅读 [pam(8)](<https://man.archlinux.org/man/pam.8>) 和 [pam.conf(5)](<https://man.archlinux.org/man/pam.conf.5>) 来理解工作原理的配置方法。 

有多个模块可用于将 YubiKey 支持的协议集成到 PAM 中： 

  * [pam-u2f](<https://archlinux.org/packages/?name=pam-u2f>)包 \- 通过 FIDO2 标准支持 [#U2F](<#U2F>)。如果你不确定要用哪种，建议用这个 
    * [通用第二因素#用于用户会话认证](<../zh-cn/%E9%80%9A%E7%94%A8%E7%AC%AC%E4%BA%8C%E5%9B%A0%E7%B4%A0.html#%E7%94%A8%E4%BA%8E%E7%94%A8%E6%88%B7%E4%BC%9A%E8%AF%9D%E8%AE%A4%E8%AF%81> "通用第二因素")
    * [Yubico 的官方文档](<https://developers.yubico.com/pam-u2f/>)，提供了支持的模块参数清单
    * Man Page：[pam_u2f(8)](<https://man.archlinux.org/man/pam_u2f.8>), [pamu2fcfg(1)](<https://man.archlinux.org/man/pamu2fcfg.1>)
  * [oath-toolkit](<https://archlinux.org/packages/?name=oath-toolkit>)包 \- 提供 [#OATH](<#OATH>) 一次性密码支持（HOTP 或 TOTP） 
    * [pam_oath](<../zh-cn/Pam_oath.html> "Pam oath")
  * [yubico-pam](<https://archlinux.org/packages/?name=yubico-pam>)包 \- 提供 [#Yubico OTP](<#Yubico_OTP>) 和质询-响应支持。注意，Yubico OTP 模式需要联网到验证服务器，而质询-响应模式没有网络要求 
    * [Yubico 的官方文档](<https://developers.yubico.com/yubico-pam/>)
    * [pam_yubico(8)](<https://man.archlinux.org/man/pam_yubico.8>) \- 注意 `mode` 参数，需要用于配置质询-响应模式

**警告：** 修改 PAM 配置文件需要小心，错误配置会导致系统不再安全，又或是过于安全使得无法通过认证。

PAM 配置超出了本文讨论范围，大致描述如下： 

  * 在用户 home 目录下或中心化创建包含密钥的文件
  * 在对应 PAM 配置文件的合适位置添加一行，格式如下：

       auth [required|sufficient] [module_name].so [module arguments]
    
  * 对于多因素认证使用 `auth required`，单因素认证使用 `auth sufficient`
  * `module_name` \- 例如：`pam_u2f.so`。要获取已安装的模块清单，请执行：`ls /usr/lib/security`
  * 模块配置参数用于如指定密钥位置、模块在认证时使用的方法等操作。

####  SSH 附注

  * Yubico 提供了一些[额外说明](<https://developers.yubico.com/yubico-pam/Yubikey_and_SSH_via_PAM.html>)。虽然是写给旧版 Ubuntu 的，但在最新的 Arch 系统上也可用。
  * 如果你在为远程系统配置使用 YubiKey，需要至少额外提供一个备份 SSH 会话，以免配置失败时被锁在系统外。
  * 检查 `/etc/ssh/sshd_config` 是否包含以下设置。[openssh](<https://archlinux.org/packages/?name=openssh>)包 提供的 `sshd_config` 默认包含以下正确配置。

       ChallengeResponseAuthentication no
       UsePAM yes
    
###  浏览器/网页集成

很多网页服务都开始支持 FIDO 硬件令牌。详细信息请参考 [U2F](<../zh-cn/%E9%80%9A%E7%94%A8%E7%AC%AC%E4%BA%8C%E5%9B%A0%E7%B4%A0.html> "U2F") 和 [WebAuthn](</wzh/index.php?title=WebAuthn&action=edit&redlink=1> "WebAuthn（页面不存在）")，但通常只需要安装 [libfido2](<https://archlinux.org/packages/?name=libfido2>)包，然后就可以[尝试一下](<https://demo.yubico.com/webauthn-technical/registration>)。 

##  小技巧

###  在插入/拔出 YubiKey 时执行操作

例如，如果你想在拔出 YubiKey 时执行操作，可以创建 `/etc/udev/rules.d/80-yubikey-actions.rules` 并添加以下内容： 
    
    ACTION=="remove", ENV{ID_VENDOR}=="Yubico", ENV{ID_VENDOR_ID}=="1050", ENV{ID_MODEL_ID}=="0010|0111|0112|0113|0114|0115|0116|0401|0402|0403|0404|0405|0406|0407|0410", RUN+="_/usr/local/bin/script args_ "
    
注意，有些版本的 YubibKey 可能无法使用该示例，你需要看下 lsusb 的 vendor 和 model ID 及设备描述，也可以用 udevadm 来获取这些信息。如果要改成在插入时执行，需要将 ACTION 中的 remove 改成 add。 

###  在插入时启动 Yubico Authenticator

The authenticator is a long-running GUI process. If run directly in a udev rule, the process would block udev's processing. If forked, udev would unconditionally kill the process after the event handling finishes. Thus you can't start the authenticator from udev rules. However, systemd.device may be used to handle this case. 

与上文类似，创建 `/etc/udev/rules.d/80-yubikey-actions.rules` 并添加以下内容： 
    
    ENV{ID_VENDOR}=="Yubico", ENV{ID_VENDOR_ID}=="1050", ENV{ID_MODEL_ID}=="0010|0111|0112|0113|0114|0115|0116|0401|0402|0403|0404|0405|0406|0407|0410", SYMLINK+="yubikey", TAG+="systemd"
    
然后[创建](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E3%80%81%E5%88%9B%E5%BB%BA%E3%80%81%E7%BC%96%E8%BE%91%E6%96%87%E4%BB%B6> "创建")一个 systemd [用户单元](<../zh-cn/Systemd/%E7%94%A8%E6%88%B7.html> "用户单元")： 
    
    ~/.config/systemd/user/yubioath-desktop.service
    
    [Unit]
    Description=Autostart Yubico Authenticator
    # Uncomment if you want to stop the authenticator when unplugged.
    #StopPropagatedFrom=dev-yubikey.device
    
    [Install]
    WantedBy=dev-yubikey.device
    
    [Service]
    Type=oneshot
    ExecStart=/usr/bin/yubioath-desktop

并将其[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用")。 _systemctl_ 会提示它被添加为不存在单元的 `dev-yubikey.device` 依赖，但对应单元会在 YubiKey 插入时创建。 

##  维护 / 升级

### Installing the OATH Applet for a YubiKey NEO

These steps will allow you to install the OATH applet onto your YubiKey NEO. This allows the use of Yubico Authenticator in the Google Play Store. 

**注意：** These steps are only for NEOs with a firmware version <= 3.1.2. The current generation NEOs (with U2F) come with the OpenPGP applet already installed)

#### Configure the NEO as a CCID device

  1. Install [yubikey-personalization-gui](<https://archlinux.org/packages/?name=yubikey-personalization-gui>)包 ([yubikey-personalization-gui-git](<https://aur.archlinux.org/packages/yubikey-personalization-gui-git/>)AUR).
  2. Add the udev rules and reboot so you can manage the YubiKey without needing to be root
  3. Run `ykpersonalize -m82`, enter `y`, and hit enter.

#### Install the applet

  1. Install [gpshell](<https://aur.archlinux.org/packages/gpshell/>)AUR, [gppcscconnectionplugin](<https://aur.archlinux.org/packages/gppcscconnectionplugin/>)AUR, [globalplatform](<https://aur.archlinux.org/packages/globalplatform/>)AUR, and [pcsclite](<https://archlinux.org/packages/?name=pcsclite>)包.
  2. [启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动") `pcscd.service`.
  3. Download the most recent CAP file from the [ykneo-oath](<https://developers.yubico.com/ykneo-oath/Releases/>) site.
  4. Download `gpinstall.txt` from [GitHub](<https://github.com/Yubico/ykneo-oath/blob/master/gpinstall.txt>).
  5. Edit the line in gpinstall.txt beginning with `install -file` to reflect the path where the CAP file is located.
  6. Open a terminal and run `gpshell _path/to/gpinstall.txt_`.
  7. Ideally, a bunch of text will scroll by and it ends saying something like
         
         Command --> 80E88013D7C000C400BE00C700CA00CA00B400BE00CE00D200D500D700B000DB00C700DF00BEFFFF00BE00E400AC00AE00AE00DB00E700A
         A00EA00ED00ED00ED00BE00EF00F100F400F100F700FA00FF00BE00F700AA01010103010700CA00C400B400AA00F700B400AA00B600C7010C
         010C00AA0140012001B0056810B0013005600000056810E0011006B4B44304B44404B44106B44B4405B443400343B002410636810E06B4B44
         407326810B004B43103441003334002B102B404B3B403BB4003B440076820A4100221024405B4341008B44600000231066820A100
         Wrapped command --> 84E88013DFC000C400BE00C700CA00CA00B400BE00CE00D200D500D700B000DB00C700DF00BEFFFF00BE00E400AC00AE00AE00DB00E700A
         A00EA00ED00ED00ED00BE00EF00F100F400F100F700FA00FF00BE00F700AA01010103010700CA00C400B400AA00F700B400AA00B600C7010C
         010C00AA0140012001B0056810B0013005600000056810E0011006B4B44304B44404B44106B44B4405B443400343B002410636810E06B4B44
         407326810B004B43103441003334002B102B404B3B403BB4003B440076820A4100221024405B4341008B44600000231066820A15D848CB77
         27D0EDA00
         Response <-- 009000
         Command --> 80E60C002107A000000527210108A00000052721010108A000000527210101010003C901000000
         Wrapped command --> 84E60C002907A000000527210108A00000052721010108A000000527210101010003C9010000B4648127914A4C7C00
         Response <-- 009000
         card_disconnect
         release_context

  8. Unplug the NEO and try it with the Yubico Authenticator app.

####  （可选）安装 Yubico Authenticator 桌面客户端

You can get the desktop version of the Yubico Authenticator by installing [yubioath-desktop](<https://archlinux.org/packages/?name=yubioath-desktop>)包. 

While `pcscd.service` is running, run `yubioath-desktop` and insert your YubiKey when prompted. 

##  排障

不论部分功能正常与否，先重启试试，特别是如果上次 YubiKey 能正常使用后更新过系统。 

### YubiKey not acting as HID device

**注意：** These steps are no longer necessary after [systemd since v244](<https://github.com/systemd/systemd/commit/d45ee2f31a8358db0accde2e7c81777cedadc3c2>) added native support for this functionality.

Add udev rule as described in [this article](<https://michaelheap.com/yubikey-on-arch/>): 
    
    /etc/udev/rules.d/10-security-key.rules
    
    KERNEL=="hidraw*", SUBSYSTEM=="hidraw", MODE="0664", GROUP="users", ATTRS{idVendor}=="2581", ATTRS{idProduct}=="f1d0"

Run `udevadm trigger` afterwards. 

###  ykman 无法连接到 YubiKey

如果管理器无法连接到 YubiKey，先检查 `pcscd.service` 或 `pcscd.socket` 是否已经启动。 

###  Error: Failed connecting to YubiKey 5 [OTP+FIDO+CCID]. Make sure the application have the required permissions.

在 `scdaemon` 独占了 YubiKey 控制权的情况下，如果 `ykman` 尝试读取 OATH 凭证，就会出现该报错。[[3]](<https://github.com/Yubico/yubikey-manager/issues/35>)

要修复该问题，可以在 `~/.gnupg/scdaemon.conf` 中为设备配置 `reader-port` 选项。[[4]](<https://support.yubico.com/hc/en-us/articles/360013714479-Troubleshooting-Issues-with-GPG>)

**注意：** 该操作会导致每次 ykman 访问 YubiKey 时 gpgagent 都会提示你解锁 YubiKey。

对于 YubiKey NEO 和 YubiKey 4： 
    
    reader-port Yubico Yubikey
    
对于 YubiKey 5： 
    
    reader-port Yubico Yubi
    
###  无法将 YubiKey 绑定到虚拟机

假设 YubiKey 可用于虚拟机上，该问题是由宿主机上的驱动绑定了设备导致的。要解绑设备，需要在宿主机上通过 [dmesg](<../zh-cn/%E6%A0%B8%E5%BF%83%E5%B7%A5%E5%85%B7.html#%E5%9F%BA%E7%A1%80> "Dmesg") 获取总线和端口信息： 
    
    # dmesg | grep -B1 Yubico | tail -n 2 | head -n 1 | sed -E 's/^\[[^]]+\] usb ([^:]*):.*/\1/'
    
输出的 USB ID 格式为 `X-Y.Z` 或 `X-Y`。接着，在宿主机上使用 `find` 搜索 `/sys/bus/usb/drivers` 来查找哪一个驱动在占用 YubiKey（例如 `usbhid` 或 `usbfs`）： 
    
    $ find /sys/bus/usb/drivers -name "*X-Y.Z*"
    
要解绑 YubiKey，需用到之前获取的信息（例如 `/sys/bus/usb/drivers/_DRIVER_ /X-Y.Z:1.0`）： 
    
    # echo 'X-Y.Z:1.0' > /sys/bus/usb/drivers/_DRIVER_ /unbind
    
###  Error: [key] could not be locally signed or gpg: No default secret key: No public key

在插入 YubiKey 时使用非标准密钥环对密钥进行签名时出现（如 [Pacman](<../zh-cn/Pacman/%E8%BD%AF%E4%BB%B6%E5%8C%85%E7%AD%BE%E5%90%8D.html> "Pacman/软件包签名") 的 `pacman-key --populate` 命令）。解决方法是拔出 YubiKey 后重试。 

###  YubiKey 在 Yubico Authenticator 中消失后又重新出现

这是因为缺少 CCID 驱动，你需要[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [ccid](<https://archlinux.org/packages/?name=ccid>)包。 

### YubiKey core error: timeout

可能是用错槽位了，换一个试试。 
