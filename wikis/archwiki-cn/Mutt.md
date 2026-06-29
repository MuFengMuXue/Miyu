**翻译状态：**

  * 本文（或部分内容）译自 [Mutt](<https://wiki.archlinux.org/title/Mutt> "arch:Mutt")，最近一次同步于 2022-06-18，若英文版本有所[更改](<https://wiki.archlinux.org/title/Mutt?diff=0&oldid=733137>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Mutt_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [fdm](</wzh/index.php?title=Fdm&action=edit&redlink=1> "Fdm（页面不存在）")
  * [msmtp](</wzh/index.php?title=Msmtp&action=edit&redlink=1> "Msmtp（页面不存在）")
  * [OfflineIMAP](</wzh/index.php?title=OfflineIMAP&action=edit&redlink=1> "OfflineIMAP（页面不存在）")
  * [isync](</wzh/index.php?title=Isync&action=edit&redlink=1> "Isync（页面不存在）")

[Mutt](<http://www.mutt.org/>) 是一个基于文本的邮件客户端，因其强大的功能而闻名。Mutt 虽然已诞生二十多年了，但仍然是大量高级用户首选的邮件客户端。 

Mutt 主要侧重于作为邮件用户代理（Mail User Agent，MUA），最初是为了查看邮件而编写的。稍后实现的功能（检索、发送和过滤邮件）与其他邮件应用程序相比过于简单，因此用户可能希望使用外部应用程序扩展 Mutt 的功能。 

尽管如此，Arch Linux 的 [mutt](<https://archlinux.org/packages/?name=mutt>)包 软件包在编译时包含了对 IMAP、POP3 和 SMTP 的支持，因此不再需要外部应用程序。 

本文包含如何使用原生 IMAP 发送和检索邮件，以及一套配置，它使用 [OfflineIMAP](</wzh/index.php?title=OfflineIMAP&action=edit&redlink=1> "OfflineIMAP（页面不存在）") 或 [getmail](</wzh/index.php?title=Getmail&action=edit&redlink=1> "Getmail（页面不存在）")（POP3）检索邮件，使用 [procmail](</wzh/index.php?title=Procmail&action=edit&redlink=1> "Procmail（页面不存在）") 过滤邮件（使用 POP3 时），并使用 [msmtp](</wzh/index.php?title=Msmtp&action=edit&redlink=1> "Msmtp（页面不存在）") 发送邮件。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [mutt](<https://archlinux.org/packages/?name=mutt>)包 软件包，或者考虑使用 [#NeoMutt](<#NeoMutt>)。 

可以考虑为 IMAP 配置安装外部帮助程序，例如 [isync](</wzh/index.php?title=Isync&action=edit&redlink=1> "Isync（页面不存在）")、[OfflineIMAP](</wzh/index.php?title=OfflineIMAP&action=edit&redlink=1> "OfflineIMAP（页面不存在）") 或 [msmtp](</wzh/index.php?title=Msmtp&action=edit&redlink=1> "Msmtp（页面不存在）")。 

或者，如果使用 POP3：[getmail](<https://aur.archlinux.org/packages/getmail/>)AUR，[fetchmail](<https://archlinux.org/packages/?name=fetchmail>)包 或 [fdm](<https://archlinux.org/packages/?name=fdm>)包，以及 [procmail](<https://aur.archlinux.org/packages/procmail/>)AUR。 

**注意：** 关于认证配置： 

  * 如果只需要 LOGIN 和 PLAIN，依赖项 [libsasl](<https://archlinux.org/packages/?name=libsasl>)包 已足够
  * 如果想（或必须）使用 CRAM-MD5、GSSAPI 或 DIGEST-MD5，安装 [cyrus-sasl-gssapi](<https://archlinux.org/packages/?name=cyrus-sasl-gssapi>)包 软件包
  * 如果使用 Gmail 作为 SMTP 服务器，则可能需要安装 [cyrus-sasl](<https://archlinux.org/packages/?name=cyrus-sasl>)包 软件包

### NeoMutt

[NeoMutt](<http://www.neomutt.org/>) 项目旨在汇集 Mutt 的所有补丁。它增加了很多[功能](<http://www.neomutt.org/feature.html>)。许多旧的 Mutt 补丁已经被更新、整理和记录。 

虽然 AUR 中有许多不同的 mutt 包，每个都提供了不同的补丁，NeoMutt 计划通过实现合适的编译选项取代它们。 

NeoMutt 可通过 [neomutt](<https://archlinux.org/packages/?name=neomutt>)包 或 [neomutt-git](<https://aur.archlinux.org/packages/neomutt-git/>)AUR（开发版本）软件包安装。 

##  配置

本节包含 [#IMAP](<#IMAP>)、[#POP3](<#POP3>)、[#Maildir](<#Maildir>) 和 [#SMTP](<#SMTP>) 配置。 

Mutt 默认在 6 个位置搜索配置文件：`~/.muttrc`、`~/.mutt/muttrc` 和 `$XDG_CONFIG_HOME/mutt/muttrc`，首先加上 `-MUTT_VERSION` 后缀，然后不加。这之中的任何一个位置都可以。如果决定将初始化文件放在其他地方，使用 `$ mutt -F /path/to/.muttrc`。应当了解 Mutt 配置的一些前提。它的语法非常接近 Bourne Shell。例如，可以获取另一个配置文件的内容： 
    
    source /path/to/other/config/file
    
可以使用变量并将 shell 命令的结果赋值给它。 
    
    set editor=`echo \$EDITOR`
    
此处的 `$` 已被转义，因此在传递给 shell 之前不会被 Mutt 替换。还要注意反引号的使用，因为 bash 语法 `$(...)` 不起作用。Mutt 有很多预定义的变量，但是也可以自己定义变量。用户变量**必须以“my”开头！**
    
    set my_name = "John Doe"
    
### IMAP

####  内置 IMAP 支持

[mutt](<https://archlinux.org/packages/?name=mutt>)包 软件包在编译时已包含 IMAP 支持。最少需要在 muttrc 文件中包含 4 行才能访问邮件。 

##### imap_user
    
    set imap_user=USERNAME
    
**提示：** 接着前一个例子，记住 Gmail 需要完整的邮件地址（这并非标准）：
    
    set imap_user=your.username@gmail.com

##### imap_pass

如果未设置，将提示输入密码。 
    
    set imap_pass=SECRET
    
**提示：** 如果在 Gmail 中启用了双重验证，并且为 Mutt 添加了特定于应用程序的密码，则应使用这个密码，而不是 Gmail 的密码。

##### folder

使用服务器（以及在必要时层次结构中最高的文件夹）而不是包含所有邮件（和文件夹）的本地文件夹。 
    
    set folder=imap[s]://imap.server.domain[:port]/[folder/]
    
你不需要使用 folder，不过它可能会带来方便（例如，如果所有其他的文件夹都在 INBOX 中）。无论在这里把什么设置成文件夹，之后在 Mutt 中都可以通过等号（=）或加号（+）访问。例如： 
    
    set folder=imaps://imap.gmail.com/
    
应当注意的是，对于几个账户，it is best practice to use different folders -- e.g. for _account-hook_ 。如果有几个 Gmail 账户，使用 
    
    set folder=imaps://username@imap.gmail.com/
    
其中账户是 _username@gmail.com_ 。这样将可以区分不同的文件夹，不然会导致认证错误。 

##### spoolfile

spoolfile 就是（未过滤的）邮件到达的文件夹。大多数邮件服务按照常规将其命名为 _INBOX_ 。现在可以使用“=”或“+”代替上面配置的 `folder` 路径。例如： 
    
    set spoolfile=+INBOX
    
##### mailboxes

在此处列出所有应当定期检查是否有新邮件的 IMAP 文件夹： 
    
    mailboxes =INBOX =family
    mailboxes imaps://imap.gmail.com/INBOX imaps://imap.gmail.com/family
    
或者，检查所有订阅的 IMAP 文件夹（等价于通过 `mailboxes` 添加所有的文件夹）： 
    
    set imap_check_subscribed
    
如果想订阅所有的文件夹，这两个版本是等价的。因此第二个方法更方便，但第一个更灵活。此外，更新版本的 Mutt 的默认配置包含一个绑定到“y”键的宏，可以改变到 mailboxes 下列出的任何一个文件夹。 

如果不设置这个变量，默认将使用 _spoolfile_ 。这个变量对 [#Sidebar](<#Sidebar>) 也很重要。 

#####  总结

使用这些选项，就可以启动 Mutt、输入 IMAP 密码并开始阅读邮件了。以下是一个 muttrc 片段（适用于 Gmail），同时还有值得考虑的几行，它们可用于获得更好的 IMAP 支持。 
    
    set folder      = imaps://imap.gmail.com/
    set imap_user   = your.username@gmail.com
    set imap_pass   = your-imap-password
    set spoolfile   = +INBOX
    mailboxes       = +INBOX
    
    # Store message headers locally to speed things up.
    # If hcache is a folder, Mutt will create sub cache folders for each account which may speeds things up even more.
    set header_cache = ~/.cache/mutt
    
    # Store messages locally to speed things up, like searching message bodies.
    # Can be the same folder as header_cache.
    # This will cost important disk usage according to your e-mail amount.
    set message_cachedir = "~/.cache/mutt"
    
    # Specify where to save and/or look for postponed messages.
    set postponed = +[Gmail]/Drafts
    
    # Allow Mutt to open a new IMAP connection automatically.
    unset imap_passive
    
    # Keep the IMAP connection alive by polling intermittently (time in seconds).
    set imap_keepalive = 300
    
    # How often to check for new mail (time in seconds).
    set mail_check = 120

####  外部 IMAP 支持

虽然 Mutt 内置 IMAP 支持，但它并不会下载邮件以供离线使用。可以使用 [OfflineIMAP](</wzh/index.php?title=OfflineIMAP&action=edit&redlink=1> "OfflineIMAP（页面不存在）") 或者 [isync](</wzh/index.php?title=Isync&action=edit&redlink=1> "Isync（页面不存在）") 这样的外部应用程序将邮件下载到本地目录，以便随后由 Mutt 处理。 

考虑使用 [spamassassin](<https://archlinux.org/packages/?name=spamassassin>)包 或 [imapfilter](<https://aur.archlinux.org/packages/imapfilter/>)AUR 这样的应用程序整理邮件。 

### POP3

[mutt](<https://archlinux.org/packages/?name=mutt>)包 软件包在编译时已包含 POP3 支持，可通过 [muttrc(5)](<https://man.archlinux.org/man/muttrc.5>) 中描述的 `pop_*` 变量配置。 

另外，也可以使用外部程序通过 POP3 获取邮件。其中一个流行的选项是使用 [getmail](</wzh/index.php?title=Getmail&action=edit&redlink=1> "Getmail（页面不存在）") 检索邮件，并使用 [procmail](</wzh/index.php?title=Procmail&action=edit&redlink=1> "Procmail（页面不存在）") 过滤邮件。 

### Maildir

Maildir is a generic and standardized format. Almost every MUA is able to handle Maildirs and Mutt's support is excellent. There are just a few simple things that you need to do to get Mutt to use them. Open your muttrc and add the following lines: 
    
    set mbox_type=Maildir
    set folder=~/mail
    set spoolfile=+/
    set header_cache=~/.cache/mutt

This is a minimal Configuration that enables you to access your Maildir and checks for new local Mails in INBOX. This configuration also caches the headers of the eMails to speed up directory-listings. It might not be enabled in your build (but it sure is in the Arch-Package). Note that this does not affect OfflineIMAP in any way. It always syncs all of the directories on a Server. `spoolfile` tells Mutt which local directories to poll for new Mail. You might want to add more Spoolfiles (for example the Directories of Mailing-Lists) and maybe other things. But this is subject to the Mutt manual and beyond the scope of this document. 

### SMTP

Whether you use POP or IMAP to receive mail you will probably still send mail using SMTP. 

#### Folders

There is basically only one important folder here: the one where all your sent e-mails will be saved. 
    
    set record = +Sent
    
Gmail automatically saves sent e-mail to `+[Gmail]/Sent`, so we do not want duplicates. 
    
    unset record
    
#### Native SMTP support

The [mutt](<https://archlinux.org/packages/?name=mutt>)包 package is compiled with SMTP support. 

For example: 
    
    set my_pass='mysecretpass'
    set my_user=myname
    
    set realname = 'Your Real Name'
    set from = your-email-address
    set use_from = yes
    
    set smtp_pass = $my_pass
    set smtp_url=smtps://$my_user@smtp.domain.tld
    set ssl_force_tls = yes

Note that if your SMTP credentials are the same as your IMAP credentials, then you can use those variables: 
    
    set smtp_pass = $imap_pass
    set smtp_url=smtps://$imap_user@smtp.domain.tld

You may need to tweak the security parameters. If you get an error like `SSL routines:SSL23_GET_SERVER_HELLO:unknown protocol`, then your server probably uses the SMTP instead of SMTPS. 
    
    set smtp_url=smtp://$imap_user@smtp.domain.tld

There are other variables that you may need to set. For example for use of STARTTLS: 
    
    set ssl_starttls = yes

**注意：** Setting `ssl_force_tls = yes` is still needed to prevent STARTTLS stripping attacks.

If your server uses the LOGIN authentication method you might need to specify this explicitly, despite the manual's claim that all methods are tried by default: 
    
    set smtp_authenticators = "login"

See [muttrc(5)](<https://man.archlinux.org/man/muttrc.5>) for more information. 

#### External SMTP support

An external SMTP agent such as [msmtp](</wzh/index.php?title=Msmtp&action=edit&redlink=1> "Msmtp（页面不存在）"), [sSMTP](</wzh/index.php?title=SSMTP&action=edit&redlink=1> "SSMTP（页面不存在）") or [opensmtpd](<https://archlinux.org/packages/?name=opensmtpd>)包 can also be used. 

The `sendmail` variable in your `muttrc` determines the program and arguments used to deliver mail in mutt. Any additional arguments must be interpreted by the program as recipient addresses. 

For example, if using [msmtp](</wzh/index.php?title=Msmtp&action=edit&redlink=1> "Msmtp（页面不存在）"): 
    
    muttrc
    
    set realname='Disgruntled Kangaroo'
    
    set sendmail="/usr/bin/msmtp"
    
    set edit_headers=yes
    set folder=~/mail
    set mbox=+mbox
    set spoolfile=+inbox
    set record=+sent
    set postponed=+drafts
    set mbox_type=Maildir
    
    mailboxes +inbox +lovey-dovey +happy-kangaroos

####  从 Mutt 发送邮件

现在，启动 `mutt`： 

You should see all the mail in `~/mail/inbox`. Press `m` to compose mail; it will use the editor defined by your `EDITOR` environment variable. If this variable is not set, you can fix it before starting Mutt: 
    
    $ export EDITOR=your-favorite-editor
    $ mutt
    
You should store the EDITOR value into your shell resource configuration file (such as [bashrc](<../zh-cn/Bash.html#%E9%85%8D%E7%BD%AE%E6%96%87%E4%BB%B6> "Bashrc")). You can also set the editor from Mutt's configuration file: 
    
    .muttrc
    
    set editor=your-favorite-editor

For testing purposes, address the letter to yourself. After you have written the letter, save and exit the editor. You will return to Mutt, which will now show information about your e-mail. Press `y` to send it. 

**警告：** If at this point you press `q` by accident, Mutt will ask you `Postpone this message? ([yes]/no)`. This is really asking whether you want to save the message you just wrote. If you press "n" (perhaps because you want to edit the message again) the message will be permanently deleted. When using Mutt, always remember that "Postpone this message?" really means "Save this message?".

### Multiple accounts

Now you should have a working configuration for one account at least. You might wonder how to use several accounts, since we put everything into a single file. 

Well all you need is to write account-specific parameters to their respective files and source them. All the IMAP/POP3/SMTP configuration for each account should go to its respective folder. 

**警告：** When one account is setting a variable that is not specified for other accounts, you **must unset** it for them, otherwise configuration will overlap and you will most certainly experience unexpected behaviour.

Mutt can handle this thanks to one of its most powerful features: hooks. Basically a hook is a command that gets executed before a specific action. There are several hooks available. For multiple accounts, you must use account-hooks _and_ folder-hooks. 

  * Folder-hooks will run a command before switching folders. This is mostly useful to set the appropriate SMTP parameters when you are in a specific folder. For instance when you are in your work mailbox and you send a e-mail, it will automatically use your work account as sender.
  * Account-hooks will run a command every time Mutt calls a function related to an account, like IMAP syncing. It does not require you to switch to any folder.

Hooks take two parameters: 
    
    account-hook [!]regex command
    folder-hook [!]regex command
    
The regex is the folder to be matched (or not if preceded by the !). The command tells what to do. 

Let us give a full example: 
    
    .muttrc
    
    ## General options
    set header_cache = "~/.cache/mutt"
    set imap_check_subscribed
    set imap_keepalive = 300
    unset imap_passive
    set mail_check = 60
    set mbox_type=Maildir
    
    ## ACCOUNT1
    source "~/.mutt/work"
    # Here we use the $folder variable that has just been set in the sourced file.
    # We must set it right now otherwise the 'folder' variable will change in the next sourced file.
    folder-hook $folder 'source ~/.mutt/work'
    
    ## ACCOUNT2
    source "~/.mutt/personal"
    folder-hook *user@gmail.com/ 'source ~/.mutt/personal'
    folder-hook *user@gmail.com/Family 'set realname="Bob"'
    
    .mutt/work
    
    ## Receive options.
    set imap_user=user@gmail.com
    set imap_pass=****
    set folder = imaps://user@imap.gmail.com/
    set spoolfile = +INBOX
    set postponed = +Drafts
    set record = +Sent
    
    ## Send options.
    set smtp_url=smtps://user:****@smtp.gmail.com
    set realname='User X'
    set from=user@gmail.com
    set hostname="gmail.com"
    set signature="John Doe"
    # Connection options
    set ssl_force_tls = yes
    unset ssl_starttls
    
    ## Hook -- IMPORTANT!
    account-hook $folder "set imap_user=user@gmail.com imap_pass=****"
    
Finally `.mutt/personal` should be similar to `.mutt/work`. 

Now all your accounts are set, start Mutt. To switch from one account to another, just change the folder (`c` key). Alternatively you can use the [sidebar](<#Sidebar>). 

To change folder for different mailboxes you have to type the complete address -- for IMAP/POP3 folders, this may be quite inconvenient -- let us bind some key to it. 
    
    ## Shortcuts
    macro index,pager <f2> '<sync-mailbox><enter-command>source ~/.mutt/personal<enter><change-folder>!<enter>'
    macro index,pager <f3> '<sync-mailbox><enter-command>source ~/.mutt/work<enter><change-folder>!<enter>'
    
With the above shortcuts (or with the sidebar) you will find that changing folders (with `c` by default) is not contextual, _i.e._ it will not list the folders of the current mailbox, but of the one used the last time you changed folders. To make the behaviour more contextual, the trick is to press _=_ or _+_ for current mailbox. You can automate this with the following macro: 
    
    macro index 'c' '<change-folder>?<change-dir><home>^K=<enter>'
    
### Passwords management

Keep in mind that writing your password in `.muttrc` is a security risk. One solution is to always enter the password manually, but this becomes cumbersome. 

#### GPG

An alternative solution is to encrypt your password with [GnuPG](<../zh-cn/GnuPG.html> "GnuPG") in an encrypted file. [Setup your own keypair](<../zh-cn/GnuPG.html#Create_a_key_pair> "GnuPG") if you have not done so already. [Create](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E3%80%81%E5%88%9B%E5%BB%BA%E3%80%81%E7%BC%96%E8%BE%91%E6%96%87%E4%BB%B6> "Create") a file in a [tmpfs](<../zh-cn/Tmpfs.html> "Tmpfs") with the following contents: 
    
    set my_pass = "_password_ "
    
**注意：** Remember that user defined variables **must** start with `my_`.

Then [encrypt](</wzh/index.php?title=Encrypt&action=edit&redlink=1> "Encrypt（页面不存在）") this file, setting yourself as the recipient and move it into an accessible location. In this example the encrypted file resides at $HOME/.my-pwds.gpg. 

In your mutt configuration file add the following before any account: 
    
    source "gpg -dq $HOME/.my-pwds.gpg |"
    
**注意：** At the end of the line above, there is no space between the pipe and the double quote.

This decrypts the file quietly and sets the variable `my_pass` in this example. This can be used in any variable after it has been sourced. For example: 
    
    set imap_pass=$my_pass

If you use external tools like OfflineIMAP and msmtp, you need to set up an agent (e.g. gpg-agent, see [GnuPG#gpg-agent](<../zh-cn/GnuPG.html#gpg-agent> "GnuPG")) to keep the passphrase into cache and thus avoiding those tools always prompting for it. 

#### Pass

You can also use [pass](<../zh-cn/Pass.html> "Pass") to encrypt your passwords easily. Just add the passwords to the given passwords as follows: 
    
    pass add user@domain.tld
    
After that, just add the command `pass show user@domain.tld` in your `muttrc`, for instance: 
    
    set imap_pass=`pass show user@domain.tld`
    
Note the use of the backquotes. Using regular quotes will not work. 

#### Security concern

If `enter-command` is available from the UI, it is possible to see the password unencrypted, which may be undesired if anybody else than you has access to your session while Mutt is running. You may want to disable it for this reason. As a consequence, every command that the user intends to use must be bound to a key in advance, otherwise it will never be accessible. 
    
    .muttrc
    
     bind generic,alias,attach,browser,editor,index,compose,pager,pgp,postpone ':' noop
    
## Tips and tricks

Guides to get you started with using and customizing Mutt: 

  * [My first Mutt](<http://mutt.postle.net/>) (maintained by Bruno Postle)
  * [The Woodnotes Guide to the Mutt Email Client](<https://web.archive.org/web/20201112005521/http://www.therandymon.com/woodnotes/mutt/using-mutt.html>) (maintained by Randall Wood)
  * [The Homely Mutt](<https://stevelosh.com/blog/2012/10/the-homely-mutt>) (by Steve Losh)
  * [Everything You Need To Know To Start Using GnuPG with Mutt](<https://codesorcery.net/old/mutt/mutt-gnupg-howto>) (by Justin R. Miller)
  * [A List of useful programs that often are used in combination with Neomutt](<https://neomutt.org/contrib/useful-programs>)

If you have any Mutt specific questions, feel free to ask in the [IRC channel](<../zh-cn/IRC_channel.html> "IRC channel"). 

### Key bindings

The default key bindings are quite far from the more common Emacs-like or Vi-like bindings. You can customize them to your preference. Mutt has a different set of bindings for the pager, the index, the attachment view, etc. Thus you need to specify which _map_ you want to modify when you bind a key. You can review the list of commands and key bindings from Mutt's help page (default key: `?`). Example of Vi-like bindings: 
    
    muttrc
    
    bind pager j next-line
    bind pager k previous-line
    bind attach,index,pager \CD next-page
    bind attach,index,pager \CU previous-page
    bind pager g top
    bind pager G bottom
    bind attach,index g first-entry
    bind attach,index G last-entry
    
### Composition

####  Encrypt and sign mail (GnuPG)

To start encrypting mail in mutt using [GnuPG](<../zh-cn/GnuPG.html> "GnuPG") copy `/usr/share/doc/mutt/samples/gpg.rc` to your mutt configuration folder (e.g. to `~/.mutt/gpg.rc`). Then [append](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E3%80%81%E5%88%9B%E5%BB%BA%E3%80%81%E7%BC%96%E8%BE%91%E6%96%87%E4%BB%B6> "Append") the following to your mutt configuration file (e.g. `~/.mutt/muttrc`): 
    
    source ~/.mutt/gpg.rc
    
Most encryption options are then available by pressing `p` in the compose view. 

See the `pgp_*` and `crypt_*` options in [muttrc(5)](<https://man.archlinux.org/man/muttrc.5>). 

#### E-mail character encoding

When using Mutt there are two levels where the character sets that must be specified: 

  * The text editor used to write the e-mail must save it in the desired encoding.
  * Mutt will then check the e-mail and determine which encoding is the more appropriate according to the priority you specified in the `send_charset` variable. Default: "us-ascii:iso-8859-1:utf-8".

So if you write an e-mail with characters allowed in ISO-8859-1 (like 'résumé'), but without characters specific to Unicode, then Mutt will set the encoding to ISO-8859-1. 

To avoid this behaviour, set the variable in your `muttrc`: 
    
    set send_charset="us-ascii:utf-8"
    
or even 
    
    set send_charset="utf-8"
    
The first compatible charset starting from the left will be used. Since UTF-8 is a superset of US-ASCII it does not harm to leave it in front of UTF-8, it may ensure old MUA will not get confused when seeing the charset in the e-mail header. 

#### Custom mail headers

One of the greatest thing in Mutt is that you can have full control over your mail header. 

First, make your headers editable when you write e-mails: 
    
    set edit_headers=yes
    
Mutt also features a special function `my_hdr` for customizing your header. Yes, it is named just like a variable, but in fact it is a function. 

You can clear it completely, which you _should_ do when switching accounts with different headers, otherwise they will overlap: 
    
    unmy_hdr *
    
Other variables have also an impact on the headers, so it is wise to clear them before using `my_hdr`: 
    
    unset use_from
    unset use_domain
    unset user_agent
    
Now, you can add any field you want -- even non-standard one -- to your header using the following syntax: 
    
    my_hdr <FIELD>: <VALUE>
    
Note that <VALUE> can be the result of a command. 

Example: 
    
    ## Extra info.
    my_hdr X-Info: Keep It Simple, Stupid.
    
    ## OS Info.
    my_hdr X-Operating-System: `uname -s`, kernel `uname -r`
    
    ## This header only appears to MS Outlook users
    my_hdr X-Message-Flag: WARNING!! Outlook sucks
    
    ## Custom Mail-User-Agent ID.
    my_hdr User-Agent: Every email client sucks, this one just sucks less.
    
#### Signature block

Create a .signature in your home directory. Your signature will be appended at the end of your email. Alternatively you can specify a file in your Mutt configuration: 
    
    set signature="path/to/sig/file"
    
##### Random signature

You can use _fortune_ (package [fortune-mod](<https://archlinux.org/packages/?name=fortune-mod>)包) to add a random signature to Mutt. 

Create a fortune file and then add the following line to your .muttrc: 
    
    set signature="fortune pathtofortunefile|"

Note the pipe at the end. It tells Mutt that the specified string is not a file, but a command. 

#### Compose and send from command line

Man pages will show all available commands and how to use them, but here are a couple of examples. You could use Mutt to send alerts, logs or some other system information, triggered by login through `.bash_profile`, or as a regular [cron](<../zh-cn/Cron.html> "Cron") job. 

Send a message: 
    
    mutt -s "Subject" somejoeorjane@someserver.com < /var/log/somelog
    
Send a message with attachment: 
    
    mutt -s "Subject" somejoeorjane@someserver.com -a somefile < /tmp/sometext.txt
    
#### Compose HTML e-mails

Since Mutt has nothing of a WYSIWIG client, HTML is quite straightforward, and you can do much more than with all WYSIWIG mail clients around since you edit the source code directly. Simply write your mail using HTML syntax. For example: 
    
    This is normal text<br>
    <b>This is bold text</b>
    
Now before sending the mail, use the `edit-type` command (default shortcut `Ctrl+t`), and replace `text/plain` by `text/html`. 

**注意：** HTML e-mails are regarded by many people as useless, cumbersome, and subject to reading issues. Mutt can read HTML mails with a text browser like w3m or lynx, but it has clearly no advantage over a plain-text e-mail. You should avoid writing HTML e-mails when possible.

#### Display another email while composing

A common complaint with Mutt is that when composing a new mail (or reply), you cannot open another mail (i.e. for checking with another correspondent) without closing the current mail (postponing). The following describes a solution: 

First, fire up Mutt as usual. Then, launch another terminal window. Now start a new Mutt with 
    
    mutt -R
    
This starts Mutt in read-only mode, and you can browse other emails at your convenience. It is strongly recommended to always launch a second Mutt in read-only mode, as conflicts will easily arise otherwise. 

**注意：** When changing folders (with `c` or `y`) the read-only mode is not preserved. Instead `Esc c` has to be used.

**提示：** This solution calls for a bit of typing, so it is suitable to bind the following command to a [keyboard shortcut](</wzh/index.php?title=Keyboard_shortcut&action=edit&redlink=1> "Keyboard shortcut（页面不存在）"): 
    
    $TERMINAL -e mutt -R
    
where `$TERMINAL` is your terminal.

###  打印

可以安装 [muttprint](<https://aur.archlinux.org/packages/muttprint/>)AUR 以获得更好的打印质量。在 muttrc 文件中插入： 
    
    set print_command="/usr/bin/muttprint %s -p {PrinterName}"
    
### Viewing content

#### Viewing URLs in a web browser

Your should start by creating a .mutt directory in $HOME if not done yet. There, create a file named macros. Insert the following: 
    
     macro pager \cb <pipe-entry>'urlview'<enter> 'Follow links with urlview'
    
Then install the [urlview](<https://aur.archlinux.org/packages/urlview/>)AUR package. 

Create a .urlview in $HOME and insert the following: 
    
    REGEXP (((http|https|ftp|gopher)|mailto)[.:][^ >"\t]*|www\.[-a-z0-9.]+)[^ .,;\t>">\):]
    COMMAND <your-browser> %s
    
When you read an email on the pager, hitting ctrl+b will list all the urls from the email. Navigate up or down with arrow keys and hit enter on the desired url. Your browser will start and go to the selected site. 

Some browser will require additional arguments to work properly. For example, [Luakit](</wzh/index.php?title=Luakit&action=edit&redlink=1> "Luakit（页面不存在）") will close on Mutt exit. You need to fork it to background, using the `-n` parameter: 
    
    COMMAND luakit -n %s 2>/dev/null
    
The `2>/dev/null` is to make it quiet, i.e. to prevent useless message printing where you do not want them to. 

**注意：** urlview has a few deficiencies (e.g. the inability to handle certain email encodings) and is fairly feature-bare (e.g. it does not provide context for links it finds). There are a couple alternatives that do better. One, which can handle all email encodings and provides link context, is [extract_url](<https://aur.archlinux.org/packages/extract_url/>)AUR. Another, which can also provide link context but cannot handle all email encodings, is [urlscan](<https://archlinux.org/packages/?name=urlscan>)包. Both are drop-in replacements for urlview, though extract_url has features which benefit from additional configuration changes.

#### Viewing HTML

It is possible to pass the html body to an external HTML program and then dump it, keeping email viewing uniform and unobtrusive. Three programs are described here: [lynx](<https://archlinux.org/packages/?name=lynx>)包, [w3m](<https://archlinux.org/packages/?name=w3m>)包 and [elinks](<https://archlinux.org/packages/?name=elinks>)包 (make sure the selected package is [installed](<../zh-cn/Pacman.html> "Pacman")). 

If `~/.mutt/mailcap` does not exist you will need to create it and save the following to it. 
    
    text/html; lynx -assume_charset=%{charset} -display_charset=utf-8 -collapse_br_tags -dump %s; nametemplate=%s.html; copiousoutput
    
or, in case of w3m, 
    
    text/html; w3m -I %{charset} -T text/html; copiousoutput;
    
or, in case of elinks, 
    
    text/html; elinks -dump; copiousoutput;
    
or, in case of elinks (with color support), 
    
    text/html; elinks -dump -dump-color-mode 1; copiousoutput;
    
Edit `~/.muttrc` and add the following, 
    
    set mailcap_path 	= ~/.mutt/mailcap
    
To automatically open HTML messages in lynx, w3m or elinks add this additional line to the muttrc: 
    
    auto_view text/html
    
The beauty of this is, instead of seeing an html body as source or being opened by a separate program, in this case lynx, you see the formatted content directly, and any url links within the email can be displayed with `Ctrl+b`, assuming you have [urlview](<https://aur.archlinux.org/packages/urlview/>)AUR installed. 

If you receive many emails with multiple or alternate encodings Mutt may default to treating every email as html. To avoid this, add the following variable to your ~/.muttrc to have Mutt default to text when available and use w3m/lynx only when no text version is availble in the email: 
    
    alternative_order text/plain text/html
    
Some HTML mails may not display correctly in a text-based web browser. As a fallback solution, you can bind a key to open a graphical browser in such cases. The following macro will open the HTML mail selected from the attachment view in the web browser defined in the environment. (Feel free to adapt the `~/.cache/mutt/` folder). 
    
     macro attach 'V' "<pipe-entry>iconv -c --to-code=UTF8 > ~/.cache/mutt/mail.html<enter><shell-escape>$BROWSER ~/.cache/mutt/mail.html<enter>"
    
If `$BROWSER` is `firefox`, then set `intl.charset.fallback.utf8_for_file` to `true` in `about:config` as described in [[1]](<https://superuser.com/questions/1215064/change-firefox-default-encoding-for-text-files/1319905#1319905>) to ensure non-ASCII characters in the HTML page are displayed correctly. 

#### Filtering the message view

You can restrict the view to e-mails matching a pattern and specific properties with the `limit` command (default shortcut: `l`). 

To view all e-mails containing "foo" in the header, simply write "foo" and you are done. To remove the filter, use the "all" keyword. 

To view all flagged messages, use 
    
    ~F
    
To view all unread messages that are either of size ≥1MB or from johndoe, use 
    
    ~U (~z 1M- | ~f johndoe)
    
All possible patterns are listed in the [official manual](<http://www.mutt.org/doc/manual/#patterns>). 

#### Conversation grouping

The default sort order is by date. Use the `sort-mailbox` command (default key: `o`) to change the sorting option. You can group e-mails by conversation/thread, in which case you can define how to sort threads and how to sort within a thread. 

In the following example, threads are sorted according to the date of their last e-mail. 
    
    muttrc
    
    set sort=threads
    set sort_aux=last-date-received
    
### Configuring editors to work with mutt

#### vim

  * To limit the width of text to 72 characters, edit your .[vim](<../zh-cn/Vim.html> "Vim")rc file and add:

    au BufRead /tmp/mutt-* set tw=72
    
  * Another choice is to use Vim's mail filetype plugin to enable other mail-centric options besides 72 character width. Edit `~/.vim/filetype.vim`, creating it if unpresent, and add:

    augroup filetypedetect
      " Mail
      autocmd BufRead,BufNewFile *mutt-*              setfiletype mail
    augroup END
    
  * To set a different tmp directory, e.g. ~/.tmp, add a line to your muttrc as follows:

    set tmpdir="~/.tmp"
    
  * To reformat a modified text see the Vim context help

    :h 10.7
    
#### GNU nano

[nano](<../zh-cn/Nano.html> "Nano") is another nice console editor to use with Mutt. 

To limit the width of text to 72 characters, edit your .nanorc file and add: 
    
     set fill 72
     set breaklonglines
    
If you do not want to limit the width of text globally, you can pass the column number as an argument to the hard-wrap option in your muttrc file, e.g.: 
    
     set editor="nano -r 72 -b"
    
Also, in muttrc file, you can specify the line to start editing so that you will skip the mail header: 
    
     set editor="nano +7"
    
#### Emacs

Emacs has a _mail_ and a _message_ major mode. To switch to mail-mode automatically when Emacs is called from Mutt, you can add the following to your `.emacs`: 
    
    .emacs
    
    ;; Mutt support.
    (add-to-list 'auto-mode-alist '("/tmp/mutt.*" . mail-mode))
    ;; Neomutt support.
    (add-to-list 'auto-mode-alist '("/tmp/neomutt-" . mail-mode))
    
If you usually run Emacs daemon, you may want Mutt to connect to it. Add this to your `.muttrc`: 
    
    .muttrc
    
    set editor="emacsclient -a \"\" -t"
    
### Display settings

#### Colors

[Append](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E3%80%81%E5%88%9B%E5%BB%BA%E3%80%81%E7%BC%96%E8%BE%91%E6%96%87%E4%BB%B6> "Append") the contents of `/usr/share/doc/mutt/samples/colors.linux` to your .muttrc file, or copy and source it. Then adjust to your liking. 

The actual color each of these settings will produce depends on the colors set in your [~/.Xresources](</wzh/index.php?title=Xresources&action=edit&redlink=1> "Xresources（页面不存在）") file. 

Alternatively, you can source any file you want containing colors (and thus act as a theme file). See [[2]](<https://nongeekshandbook.blogspot.be/2009/03/mutt-color-configuration.html>) for a theme example. 

#### Index Format

Here follows a quick example to put in your `.muttrc` to customize the Index Format, i.e. the columns displayed in the folder view. 
    
    set date_format="%y-%m-%d %T"
    set index_format="%2C | %Z [%d] %-30.30F (%-4.4c) %s"
    
See the [Mutt Reference](<http://www.mutt.org/doc/manual/#index-format>), [strftime(3)](<https://man.archlinux.org/man/strftime.3>) and [printf(3)](<https://man.archlinux.org/man/printf.3>) for more details. 

####  Display recipient instead of sender in "Sent" folder view

By default Mutt uses the `%L` format string in the `index_format` variable, which will display: 

  * "To <list-name>", if an address in the "To:" or "Cc:" header field matches an address defined by the user's `subscribe` command.
  * Otherwise it displays the author name, or recipient name if the message is from you.

If you use multiple email addresses in the same mailbox, make sure to configure the [alternates variable](<https://gitlab.com/muttmua/mutt/wikis/UseCases/MultiAccounts#setting-up-the-addresses-alternates:alternates>), so that Mutt knows which messages were from you. 
    
    muttrc
    
    alternates    ^me@example.COM$ ^me@example.NET$ ^example@archlinux.ORG$
    
#### Variable column width

If you resize the window, the subject might get truncated while there is still unused space left for some fields, like for the sender. You can get the maximum number of columns supported by your terminal (i.e. the width) using a shell call to `tput cols`. With this value, you can set a percentage of the width to fields like Sender and Subject. 

Example using the above folder-hook and a sidebar width of 24: 
    
    muttrc
    
    ## From field gets 30% of remaining space, Subject gets 70%.
    ## Remaining space is the total width minus the other fields (35), minus the sidebar (24)
    set my_index_format_pre='set my_col_from = `echo $((30 * ($(tput cols)-35-24) / 100))`; set my_col_subject = `echo $((70 * ($(tput cols)-35-24) / 100))`; set index_format="%2C | %Z [%d] %-$my_col_from.${my_col_from}'
    set my_index_format_post=' (%-4.4c) %?M?<%M> ?%-$my_col_subject.${my_col_subject}s"'
    
    folder-hook .*[sS]ent.* "$my_index_format_pre"t"$my_index_format_post"
    folder-hook ! .*[sS]ent.* "$my_index_format_pre"F"$my_index_format_post"
    
We _must_ set the variables `my_col_from` and `my_col_from` from within the hooks. Otherwise, the column values will not get re-computed. 

We can add a binding to force re-computing the index format without changing folder: 
    
    muttrc
    
    macro index,pager \CL "<enter-command>$my_index_format_pre"F"$my_index_format_post<enter><redraw-screen>"
    
#### Sidebar

Example settings for a sidebar are in `/usr/share/doc/mutt/samples/sample.muttrc-sidebar`, including keybindings. Copy, edit, and source that file in your mutt configuration file. Be sure to change `set sidebar_visible = yes`. 

[Append](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E3%80%81%E5%88%9B%E5%BB%BA%E3%80%81%E7%BC%96%E8%BE%91%E6%96%87%E4%BB%B6> "Append") the following in order to toggle the sidebar visibility: 
    
    bind index,pager B sidebar-toggle-visible
    
**注意：** You _must_ set the `mailboxes` variables or the `imap_check_subscribed` to tell the sidebar which folder should be displayed. See the [mailboxes](<#mailboxes>) section.

Note that with the `mailboxes` option, folders appear in the order they were set to `mailboxes` if you do not use the `sidebar_sort_method` option. 

**提示：** To add a separator between different mailboxes, add a fake folder to the list of folders For example add: 
    
    mailboxes "+-- My mailbox -----------"

#### Display the index above the pager view

Set the following variable in your `muttrc`: 
    
    set pager_index_lines=10
    
### Contact management

#### Address aliases

_Aliases_ is the way Mutt manages contacts. An alias is **nickname [longname] <address>**. 

  * The **nickname** is what you will type in Mutt to get your contact address. One word only, and should be easy to remember.
  * The **longname** is optional. It may be several words.
  * An **< address>** must be in a valid form (i.e. with an `@`).

It is quite simple indeed. Add this to `.muttrc`: 
    
    set alias_file = "~/.mutt/aliases"
    set sort_alias = alias
    set reverse_alias = yes
    source $alias_file

Explanation: 

  * `alias_file` is the file where the information is getting stored when you add an alias from within Mutt.
  * `sort_alias` specifies which field to use to sort the alias list when displayed in Mutt. Possible values: alias, address.
  * `reverse_alias` if set to yes mutt will display the "personal" name from your aliases in the index menu if it finds an alias that matches the message's sender.
  * `source $alias_file` tells Mutt to read aliases on startup. Needed for auto-completion.

Now all you have to do when prompted `To:` is writing the alias instead of the full address. The beauty of it is that you can auto-complete the alias using `Tab`. Autocompleting a wrong or an empty string will display the full list. You can select the alias as usual, or by typing its index number. 

There are two ways to create aliases: 

  * From Mutt, press `a` when an e-mail of the targetted person if selected.
  * Edit the alias_file manually. The syntax is really simple:

    alias nickname Long Name <my-friend@domain.tld>
    
#### Abook

[abook](<https://aur.archlinux.org/packages/abook/>)AUR is a stand-alone program dedicated to contact management. It uses a very simple text-based interface and contacts are stored in a plain text, human-readable database. Besides the desired contact properties are extensible (birthday, address, fax, and so on). 

Abook is specifically designed to be interfaced with Mutt, so that it can serve as a full, more featured replacement of Mutt internal aliases. If you want to use Abook instead of aliases, remove the aliases configuration in `.muttrc` and add this: 
    
    muttrc
    
    ## Abook
    set query_command= "abook --mutt-query '%s'"
    macro index,pager  a "<pipe-message>abook --add-email-quiet<return>" "Add this sender to Abook"
    bind editor        <Tab> complete-query
    
See the man pages `abook` and `abookrc` for more details and a full configuration sample. 

#### Goobook

Goobook allows you to search your Google contacts from the command line or from within Mutt and can be installed with the [goobook](<https://aur.archlinux.org/packages/goobook/>)AUR or [goobook-git](<https://aur.archlinux.org/packages/goobook-git/>)AUR packages. 

Before using goobook you must configure `~/.goobookrc`. To generate the default template: 
    
    $ goobook config-template > ~/.goobookrc
    
See `~/.goobookrc` for configuration options. At a minimum, you will need to enter your **email** and **password**. 

**注意：** If you have two-step verification enabled with the Google account, you may need to generate an application password. 

In order to authenticate with Google, you must generate a [Client ID and Client secret](<https://github.com/aristosv/google_auth/blob/master/README.md>). See [[3]](<https://gitlab.com/goobook/goobook/-/issues/83>) for details. 

If you want to use Goobook instead of aliases, remove any alias configuration in `.muttrc` and add: 
    
    muttrc
    
    ## GooBook
    set query_command="goobook query '%s'"
    macro index,pager a "<pipe-message>goobook add<return>" "add sender to google contacts"
    bind editor <Tab> complete-query
    
When composing an email message within mutt, `Tab` will now search your Google contacts. While viewing messages `a` will add the sender to Google contacts. 

#### Khard

[khard](<https://archlinux.org/packages/?name=khard>)包 is a command-line addressbook that uses locally-stored carddav address book entries. You can use [vdirsyncer](<https://archlinux.org/packages/?name=vdirsyncer>)包 to sync those with CardDAV servers. 

The integration in mutt is similar to abook, see [khard documentation](<https://khard.readthedocs.io/en/latest/scripting.html#mutt>). 

### Manage multiple sender accounts

If you use multiple sender accounts, you can automatically associate a specific sender account with a recipient. [mutt-vid](<https://aur.archlinux.org/packages/mutt-vid/>)AUR scans sent emails for the most recent "From" details associated with specific recipients, saving these in a file for mutt to source. The next time you email this recipient, mutt will automatically invoke a send-hook with the same email address and real name that you used previously. See mutt-vid's [homepage](<https://gitlab.com/protist/mutt-vid>) for more details. 

### Request IMAP mail retrieval manually

If you do not want to wait for the next automatic IMAP fetching (or if you did not enable it), you might want to fetch mails manually. There is a mutt command `imap-fetch-mail` for that. Alternatively, you could bind it to a key: 
    
    bind index "^" imap-fetch-mail
    
###  Avoiding slow index on large (IMAP) folders due to coloring

Index highlighting by regex is nice, but can lead to slow folder viewing if your regex checks the body of the message. 

Use folder-hook for only highlighting in, for example, the inbox (if you manage to empty your mailbox efficiently): 
    
    folder-hook . 'uncolor index "~b \"Hi Joe\" ~R !~T !~F !~p !~P"'
    folder-hook ""!"" 'color index brightyellow black "~b \"Hi Joe\" ~N !~T !~F !~p !~P"'
    
### Speed up folders switch

Add this to your `.muttrc`: 
    
    set sleep_time = 0

### Archive treated e-mails

When you read an e-mail, you have four choices: Answer it, Flag it, Archive it or Delete it. If you have this in mind, you can keep your inbox slim and fit with this macro (set up for Gmail): 
    
    macro index \' "<tag-pattern>~R !~D !~F<enter>\
    <tag-prefix><save-message>+[Gmail]/All <enter>" \
    "Archive"
    
### Migrating mails from one computer to another

In case you are transfering your mails to a new machine (copy&paste), you probably need to delete the header cache (a file or folder like `~/.cache/mutt` if you followed the above configuration) to make Mutt able to read your migrated E-Mails. Otherwise Mutt may freeze. 

Note that if you had a folder created for you header cache, all mailboxes will have their own cache file, so you can delete caches individually without having to remove everything. 

### Default folder for saving attachments

By default Mutt will save attachments to the folder it was started from. If you want to always set the default destination to `~/attachments`, you can create the following alias, which launches Mutt in this folder: 
    
    alias mutt='cd ~/attachments && mutt'
    
### Pager behavior

Show context lines when going to next page: 
    
    set pager_context=3
    
Stop at the end instead of displaying next mail: 
    
    set pager_stop=yes
    
### Fast reply

By default Mutt will ask to confirm the recipient and the subject when you reply to an e-mail. It will also ask if you want to include the original mail in your answer. If you assume you will always stick to the default values, you can set up Mutt to skip these questions: 
    
    muttrc
    
    set fast_reply=yes
    set include=yes
    
You can still edit the recipient and the subject before sending. 

### Ignore own e-mail addresses from group-reply

Mutt will include your e-mail address(es) in the recipient list when you group-reply to a mail you were CC'ed. You can ask Mutt to ignore some addresses with: 
    
    alternates mail1@server1|mail2@server2|...
    
### IMAP message cache

When using the built-in IMAP support, e-mails are fetched in memory by default. Retrieving a big e-mail several times will download it from your IMAP server that many times. 

Alternatively, you can ask Mutt to store all fetched messages on disk: 
    
    muttrc
    
    set message_cachedir=~/.cache/mutt/messages
    
(The folder must exist.) This will make any future retrieval instantaneous, even with big attachments. 

If you want to purge the cache from its oldest e-mails exceeding a limit of, say, 50MB, you can use a script like the following: 
    
    ~/.mutt/purgecache.sh
    
    #!/bin/sh
    
    ## In KB.
    CACHE_LIMIT=51200
    
    cd "$1" 2>/dev/null
    [ $? -ne 0 ] && exit
    
    [ $(du -s . | cut -f1 -d'	') -lt $CACHE_LIMIT ] && exit
    while IFS= read -r i; do
    	rm "$i"
    	[ $(du -s . | cut -f1 -d'	') -lt $CACHE_LIMIT ] && exit
    done <<EOF
    $(find . -type f -exec ls -rt1 {} +)
    EOF
    
and call it on startup: 
    
    muttrc
    
    set message_cachedir=~/.cache/mutt/messages
    source "~/.mutt/purgecache.sh '$message_cachedir'|"
    
### Open attachments or view HTML email in the background

By default, opening the attachments in the mutt will block mutt. You can edit `~/.mutt/mailcap` to append an `&` so mutt will launch one of the [Default applications](<../zh-cn/Default_applications.html> "Default applications") in the backgroud. Take [xdg-open](<../zh-cn/Xdg-utils.html#xdg-open> "Xdg-open") as an example, 
    
    text/html; xdg-open %s &> /dev/null &; nametemplate=%s.html
    application/*; xdg-open %s &> /dev/null &; 
    image/*; xdg-open %s &> /dev/null &;
    
`&> /dev/null` is used to prevent any error or message from cluttering the mutt terminal window. And `nametemplate=%s.html` is used because chromium refuse to render local files without .html extension as HTML. 

## Troubleshooting

### Backspace does not work in Mutt

This is a common problem with some xterm-like terminals. Two solutions: 

  * Either rebind the key in `.muttrc`

    bind index,pager ^? previous-line
    
Note that `^?` is one single character representing backspace in [caret notation](<https://en.wikipedia.org/wiki/Caret_notation> "wikipedia:Caret notation"). To type in Emacs, use `Ctrl+q Backspace`, in Vim `Ctrl+v Backspace`. 

  * Or fix your terminal:

    $ infocmp > termbs.src
    
Edit `termbs.src` and change `kbs=^H` to `kbs=\177`, then: 
    
    $ tic -x termbs.src
    
### The _change-folder_ function always prompt for the same mailbox

This is not a bug, this is actually an intended behaviour. See the [multiple accounts section](<#Multiple_accounts>) for a workaround. 

###  I cannot change folder when using Mutt read-only (Mutt -R)

This is certainly because you are using macros like this one: 
    
    macro index,pager <f2> '<sync-mailbox><enter-command>source ~/.mutt/personal<enter><change-folder>!<enter>'
    
This macro tells Mutt to sync (which is a write operation) before switching. 

Either use the [sidebar](<#Sidebar>) or set another macro: 
    
    macro index,pager <f3> '<enter-command>source ~/.mutt/personal<enter><change-folder>!<enter>'
    
###  Error sending message, child exited 127 (Exec error.).

This is an SMTP error. It means that mutt does not know how to send the message. You can either try installing sendmail and see if that solves your issue, or you can set the smtp_url variable. If you use gmail, you can add the following to your muttrc to tell mutt to use gmails smtp server. 
    
    set smtp_url=smtps://$imap_user:$imap_pass@smtp.gmail.com
    
Take note of the smtps protocol, it is important. This should solve the problem. 

### Character encoding problems

If you are having problems with character encoding, first read [this section](<https://web.archive.org/web/20160117025625/http://dev.mutt.org/trac/wiki/MuttFaq/Charset>) in the Mutt wiki. 

If Chinese text is still garbled, it may help to decode with GBK even when GB2312 is specified in the header. You can do this with `iconv` by adding the following to your `mailcap` file: 
    
    text/plain; iconv -f gbk -t utf-8 %s; test=echo "%{charset}" | grep -ic "gb2312"; copiousoutput;
    
and enabling it by adding a line to your `.muttrc`: 
    
    auto_view text/plain
    
For HTML emails, you can edit the relevant line of your mailcap by replacing `%{charset}` with `$(echo %{charset} | sed s/gb2312/gbk/I)`, for example: 
    
    text/html; w3m -dump -I $(echo %{charset} | sed s/gb2312/gbk/I) %s; nametemplate=%s.html; copiousoutput
    
### Unable to login with GMail

Gmail disables access from applications it considers less secure, including `mutt`. You can enable access by following the instructions [here](<https://support.google.com/accounts/answer/6010255>)

### Not possible to open too long URLs with urlview

Too long URLs are not parsed correctly, because urlview does not decode text (see [[4]](<https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=127090>)). You can let mutt decode the e-mails instead. Replace the line for opening urlview with the following code: 
    
    macro index \cb "\
    :set my_tmp_pipe_decode=\$pipe_decode\n\
    :set pipe_decode\n\
    |urlview\n\
    :set pipe_decode=\$my_tmp_pipe_decode\n\
    :unset my_tmp_pipe_decode\n" \
    'call urlview to extract URLs out of a message'
    
Another option is to use [urlscan](<https://github.com/firecat53/urlscan>) instead, which gives a text user interface to select the URL and can deal with much stranger text formats. 

##  文档

新手可能会发现很难找到 Mutt 的帮助。实际上大部分主题都涵盖在官方文档中。强烈推荐阅读这些文档。 

  * [官方手册](<http://www.mutt.org/doc/manual/>)。Arch Linux 的 [mutt](<https://archlinux.org/packages/?name=mutt>)包 软件包也在 `/usr/share/doc/mutt/` 安装了 HTML 和纯文本手册。
  * `mutt` 和 `muttrc` 手册页。

##  参见

  * [Mutt 官方网站](<http://www.mutt.org/>)
  * [官方手册](<http://www.mutt.org/doc/manual/>)
  * [The Mutt wiki](<https://gitlab.com/muttmua/mutt/wikis/home/>)
  * [Brisbin's great guide on how to setup different IMAP accounts with Mutt, offlineimap, msmtp](<https://pbrisbin.com/posts/two_accounts_in_mutt/>)
  * [Mutt 快速指南](<https://srobb.net/mutt.html>)
  * [Steve Losh on Mutt, offlineimap, msmtp, notmuch (focused on Gmail)](<https://stevelosh.com/blog/2012/10/the-homely-mutt/>)
