**翻译状态：**

  * 本文（或部分内容）译自 [Pam oath](<https://wiki.archlinux.org/title/Pam_oath> "arch:Pam oath")，最近一次同步于 2022-11-20，若英文版本有所[更改](<https://wiki.archlinux.org/title/Pam_oath?diff=0&oldid=757620>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Pam_oath_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [OATH](</wzh/index.php?title=OATH&action=edit&redlink=1> "OATH（页面不存在）")
  * [Google Authenticator](<../zh-cn/Google_Authenticator.html> "Google Authenticator")
  * [YubiKey](<../zh-cn/YubiKey.html> "YubiKey")

[OATH Toolkit](<https://www.nongnu.org/oath-toolkit/index.html>) 为认证系统提供一次性密码（OTP）组件。它包含一个 PAM 认证模块，支持的技术包括基于消息的 [HOTP 算法](<https://en.wikipedia.org/wiki/HMAC-based_One-time_Password_Algorithm> "w:HMAC-based One-time Password Algorithm") ([RFC 4226](<https://tools.ietf.org/html/rfc4226> "rfc:4226")）和基于时间的 [TOTP 算法](<https://en.wikipedia.org/wiki/Time-based_One-time_Password_Algorithm> "w:Time-based One-time Password Algorithm") ([RFC 6328](<https://tools.ietf.org/html/rfc6328> "rfc:6328")）。OTP 生成器应用程序可用于 Android、iOS、Blackberry 和其他设备。与 [Google Authenticator](<../zh-cn/Google_Authenticator.html> "Google Authenticator") 类似，该认证机制整合在 Linux [PAM](<../zh-cn/PAM.html> "PAM") 系统中。本指南展示该机制的安装和配置。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [oath-toolkit](<https://archlinux.org/packages/?name=oath-toolkit>)包。 

##  设置OATH

OATH 种子是一个十六进制数字，每个用户应该唯一。为了给一个用户生成一个新的种子，可以使用下面的命令： 
    
    $ openssl rand -hex 10
    
    12345678909876543210
    
**注意：** 本文中上述输出种子是作为例子使用，**不要** 直接使用。

每个用户需要有一个 OATH，并在配置文件 `/etc/users.oath` 中链接到它。使用[根用户](<../zh-cn/%E7%94%A8%E6%88%B7%E5%92%8C%E7%94%A8%E6%88%B7%E7%BB%84.html#%E6%A6%82%E8%A7%88> "根用户")创建该文件并插入用户种子： 

**提示：** 在一个终端登录到具有root用户权限的会话中，并在另一个终端中修改 PAM 配置。这样，如果 PAM 设置出现问题，你仍然有一个账户登录并修复，这在远程连接时特别有用。
    
    /etc/users.oath
    
    # Option User Prefix Seed
    HOTP/T30/6 _user_ - _12345678909876543210_
    
**警告：** 不要设置 T 大于60，否则会有报错：（OATH_UNKNOWN_USER: 无法找到用户的信息）。

如果需要 HOTP，请使用此配置： 
    
    /etc/users.oath
    
    # Option User Prefix Seed
    HOTP _user_ - _12345678909876543210_
    
确保该文件只能由 Root 用户访问： 
    
    # chmod 600 /etc/users.oath
    # chown root /etc/users.oath
    
##  设置 PAM

要想只为某个特定的服务启用 OATH，比如 [OpenSSH](<../zh-cn/OpenSSH.html> "OpenSSH")，可以编辑 `/etc/pam.d/sshd` 文件，并在文件开头添加以下一行： 
    
    auth	  sufficient pam_oath.so usersfile=/etc/users.oath window=30 digits=6
    
如果只输入正确的 OATH 代码即可认证通过。如果使用下面这行，可以把 OATH 作为一个要求，并让 PAM 堆栈的其他部分得到处理： 
    
    auth	  required pam_oath.so usersfile=/etc/users.oath window=30 digits=6
    
为了让 SSH 登录工作，确保这些选项在文件中启用 `/etc/ssh/sshd_config`： 
    
    ChallengeResponseAuthentication yes
    UsePAM yes
    
[重启](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "重启") `sshd.service` 来启用这些更改。 

如果想强制 OATH 请求-响应，即使有一个有效的公钥认证和密码认证，把以下内容加入到 `/etc/ssh/sshd_config`： 
    
    AuthenticationMethods publickey,keyboard-interactive:pam
    KbdInteractiveAuthentication yes
    PasswordAuthentication yes
    
**提示：** 用于本地登录，编辑 `/etc/pam.d/login` 即可。

##  使用 OATH 密码登录

对于用 TOTP 登录的情况： 
    
    $ oathtool -v --totp -d 6 _12345678909876543210_
    
**警告：** 当 TOTP 模式设置为 `SHA512` 会有一处程序错误，但开发者没有修复。参见 [Gitlab 的公开问题](<https://gitlab.com/oath-toolkit/oath-toolkit/issues/8>)。

对于用 HOTP 登录的情况： 
    
    $ oathtool -v -d 6 _12345678909876543210_
    
将` _12345678909876543210_`替换为用户对应的种子。将输出类似如下内容： 
    
    Hex secret: 1ab4321412aebc
    Base32 secret: DK2DEFASV26A====
    Digits: 6
    Window size: 0
    Start counter: 0x0 (0)
    
    820170
    
最后一串数字即可现在用于登录的代码，但 Base32 密钥更加有趣，因为可转换成 QR 码方便转移密钥。安装 [qrencode](<https://archlinux.org/packages/?name=qrencode>)包 并运行以下命令转换： 
    
    $ qrencode -o _user_.png 'otpauth://totp/_user_ @_machine_?secret=_DK2DEFASV26A====_
    
相应改变 _用户_ 、 _机器_ 和` _DK2DEFASV26A====_`。一旦完成，可以用你喜欢的图像显示程序来显示 QR 码。另外，也可以用以下方法在终端上直接生成 QR 码： 
    
    $ qrencode -t UTF8 'otpauth://totp/_user_ @_machine_?secret=_DK2DEFASV26A===='_
    
使用 [Aegis Authenticator](<https://f-droid.org/packages/com.beemdevelopment.aegis/>) 或 [FreeOTP+](<https://f-droid.org/packages/org.liberty.android.freeotpplus/>)，然后对该 `_user_.png`（或类似 ASCII-art 的图像）截图，并在需要时让它显示 OTP 密码，这样十分方便。 

**注意：** 你的用户密匙是这个系统中最重要的信息。一旦设置手机来提供 OTP，它就会有这个密钥，` _user_.png` 文件中的 QR 码也有这个密钥。需要特别注意这个文件，它应该只存储在加密的媒介上（你的手机需要使用加密，以达到任何合理的安全水平）。如果没有，可以限制在像三星 Knox 这样的沙盒中，以防止第三方应用程序潜在地访问它们。

##  参见

  * [使用 pam_oath 和 Google Authenticator 的双因素时间（TOTP）SSH 认证](<https://spod.cx/blog/two-factor-ssh-auth-with-pam_oath-google-authenticator.shtml>)
  * [pam_oath 手册](<https://www.nongnu.org/oath-toolkit/pam_oath.html>)
