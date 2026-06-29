**翻译状态：**

  * 本文（或部分内容）译自 [GDM](<https://wiki.archlinux.org/title/GDM> "arch:GDM")，最近一次同步于 2025-02-09，若英文版本有所[更改](<https://wiki.archlinux.org/title/GDM?diff=0&oldid=824318>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/GDM_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [GNOME](<../zh-cn/GNOME.html> "GNOME")
  * [显示管理器](<../zh-cn/%E6%98%BE%E7%A4%BA%E7%AE%A1%E7%90%86%E5%99%A8.html> "显示管理器")

来自[GDM - GNOME显示管理器](<https://wiki.gnome.org/Projects/GDM>)：“GNOME显示管理器（GDM）是一个管理图形显示服务并处理图形用户登录的程序。 

[显示管理器](<../zh-cn/%E6%98%BE%E7%A4%BA%E7%AE%A1%E7%90%86%E5%99%A8.html> "显示管理器")为[X Window System](<../zh-cn/Xorg.html> "Xorg")和[Wayland](<../zh-cn/Wayland.html> "Wayland")提供图形登录提示。 

##  安装

可通过安装[gdm](<https://archlinux.org/packages/?name=gdm>)包来安装GDM，或作为[gnome](<https://archlinux.org/groups/x86_64/gnome/>)包组的一部分安装。 

##  启动

若要开机启动GDM，[启用](<../zh-cn/Systemd.html#%E4%BD%BF%E7%94%A8%E5%8D%95%E5%85%83> "Systemd")`gdm.service`。 

###  自动启动应用

欲使程序于登录后自动启动，请参照 [Autostarting#On desktop environment startup](<../zh-cn/%E8%87%AA%E5%8A%A8%E5%90%AF%E5%8A%A8.html#On_desktop_environment_startup> "Autostarting") 中适用您的桌面环境的指示。 

##  配置

**注意：** 下面列出的大多数配置选项都可以使用 [gdm-settings](<https://aur.archlinux.org/packages/gdm-settings/>)AUR GUI 应用程序轻松设置。

###  登录页面背景图片

[![](../File:Tango-inaccurate.png)](<../File:Tango-inaccurate.png>)**本文或本章节的事实准确性存在争议。**

**原因：** 配置不是持久的，更改在 GNOME Shell 更新后会被撤销。建议：重写以使用“用户主题”GNOME 扩展。（在 [Talk:GDM](<../zh-cn/Talk:GDM.html>) 中讨论）

**注意：**

  * 自GNOME 3.16开始，GNOME Shell主题被存储为二进制文件（gresource）。
  * 在 [gnome-shell](<https://archlinux.org/packages/?name=gnome-shell>)包 的后续升级中，这个变动会被重写。

首先，您需要将现有的 GNOME Shell 主题解压到您的主目录中的一个目录中。 您可以使用以下脚本执行此操作： 
    
    extractgst.sh
    
    #!/bin/sh
    gst=/usr/share/gnome-shell/gnome-shell-theme.gresource
    workdir=${HOME}/shell-theme
    
    for r in `gresource list $gst`; do
    	r=${r#\/org\/gnome\/shell/}
    	if [ ! -d $workdir/${r%/*} ]; then
    	  mkdir -p $workdir/${r%/*}
    	fi
    done
    
    for r in `gresource list $gst`; do
            gresource extract $gst $r >$workdir/${r#\/org\/gnome\/shell/}
    done

主题文件应当已提取到创建的目录中。现在将您想要的背景图像复制到此目录。 

接下来，您需要在目录中创建一个文件，内容如下： 
    
    gnome-shell-theme.gresource.xml
    
    <?xml version="1.0" encoding="UTF-8"?>
    <gresources>
      <gresource prefix="/org/gnome/shell/theme">
        <file>calendar-today.svg</file>
        <file>calendar-today-light.svg</file>
        <file>checkbox.svg</file>
        <file>checkbox-focused.svg</file>
        <file>checkbox-off-focused-light.svg</file>
        <file>checkbox-off-focused.svg</file>
        <file>checkbox-off-light.svg</file>
        <file>checkbox-off.svg</file>
        <file>gnome-shell.css</file>
        <file>gnome-shell-high-contrast.css</file>
        <file>gnome-shell-start.svg</file>
        <file>pad-osd.css</file>
        <file>process-working.svg</file>
        <file>toggle-off.svg</file>
        <file>toggle-off-hc.svg</file>
        <file>toggle-off-light.svg</file>
        <file>toggle-on.svg</file>
        <file>toggle-on-hc.svg</file>
        <file>toggle-on-light.svg</file>
        <file>workspace-placeholder.svg</file>
        <file>**filename** </file>
      </gresource>
    </gresources>

将 **filename** 替换为背景图像的文件名，或移除此行后用16位色彩值替代。 

现在，打开 `gnome-shell.css` 文件并更改 `#lockDialogGroup` 定义如下： 
    
    #lockDialogGroup {
      background: url(**filename**);
      background-size: **width** px **height** px;
      background-repeat: no-repeat;
    }
    
将 `background-size` 设置为GDM使用的分辨率, 这可能不一定是图像的分辨率。显示分辨率列表见[Display resolution](<https://en.wikipedia.org/wiki/Display_resolution#Computer_monitors> "wikipedia:Display resolution")。同样，将 **filename** 替换为背景图像的文件名。 

如果您仅想改变背景颜色，请调整 `#lockDialogGroup` 的定义，如下： 
    
    #lockDialogGroup {
      background-color: #**color** ;
    }
    
这里 **color** 是作为背景的十六进制编码的新颜色。 

最后，使用以下命令编译主题： 
    
    $ glib-compile-resources gnome-shell-theme.gresource.xml
    
然后将生成的 `gnome-shell-theme.gresource` 文件复制到 `/usr/share/gnome-shell` 目录下。 

然后重启 `gdm.service` (注意：重启而不是退出) ，它就会使用您想要的背景图片了。 

更多信息见[此贴](<https://bbs.archlinux.org/viewtopic.php?id=197036>)。一个自动执行以上步骤的 shell 脚本在 [DimaZirix's github repository](<https://github.com/DimaZirix/fedora-gdm-wallpaper>) 上可用。 

###  dconf配置

一些 GDM 设置存储在 [dconf](</wzh/index.php?title=Dconf&action=edit&redlink=1> "Dconf（页面不存在）") 数据库中。可以通过将 _keyfiles_ 添加到 `/etc/dconf/db/gdm.d` 目录，然后以root身份运行 `dconf update` 重新编译GDM数据库来配置它们，或者通过登录系统上的GDM用户并使用"gsettings" 命令直接更改设置。需要一个 GDM 配置文件 - 这必须手动创建，因为它不再向上游发送，见下文： 
    
    /etc/dconf/profile/gdm
    
    user-db:user
    system-db:gdm
    file-db:/usr/share/gdm/greeter-dconf-defaults
    
对于后一种方法，您可以用以下命令尝试登入 GDM 用户： 
    
    # machinectl shell gdm@ /bin/bash
    
####  登录页面的logo

创建以下密钥文件： 
    
    /etc/dconf/db/gdm.d/02-logo
    
    [org/gnome/login-screen]
    logo='_/path/to/logo.png_ '

然后重新编译 GDM 数据库。 

或者，作为 GDM 用户执行以下操作来更改 logo： 
    
    [gdm]$ dbus-launch gsettings set org.gnome.login-screen logo '_/path/to/logo.png_ '
    
要禁用 logo，可以将值设置为空字符串： 
    
    [gdm]$ dbus-launch gsettings set org.gnome.login-screen logo ''
    
####  更改光标主题

GDM会忽略 [GNOME](<../zh-cn/GNOME.html> "GNOME") 光标主题设置，也忽略根据 [XDG_规范](<../zh-cn/Cursor_themes.html#XDG_%E8%A7%84%E8%8C%83> "Cursor themes")设置的光标主题。若要更改GDM使用的光标，请创建以下密钥文件： 
    
    /etc/dconf/db/gdm.d/10-cursor-settings
    
    [org/gnome/desktop/interface]
    cursor-theme='_theme-name_ '

然后重新编译GDM database，或作为GDM用户执行以下操作： 
    
    [gdm]$ dbus-launch gsettings set org.gnome.desktop.interface cursor-theme '_theme-name_ '
    
####  更改图标主题

可以使用相同的方法来更改图标主题。 创建以下密钥文件： 
    
    /etc/dconf/db/gdm.d/11-icon-settings
    
    [org/gnome/desktop/interface]
    icon-theme='_theme-name_ '

然后，重新编译 GDM 数据库。 或者，执行以下命令临时作为 GDM 用户更改图标主题： 
    
    [gdm]$ dbus-launch gsettings set org.gnome.desktop.interface icon-theme '_theme-name_ '
    
####  在登录页面显示大字体

单击屏幕右上角的辅助功能图标（一个白色圆圈，中间有一个人的轮廓），然后选中 _大号文本_ 选项。 

要设置特定的缩放比例，可以创建以下密钥文件（以1.25为例）： 
    
    /etc/dconf/db/gdm.d/03-scaling
    
    [org/gnome/desktop/interface]
    text-scaling-factor='_1.25_ '

然后重新编译GDM database，或作为GDM用户执行以下操作： 
    
    [gdm]$ dbus-launch gsettings set org.gnome.desktop.interface text-scaling-factor '_1.25_ '
    
####  关闭声音

此调整禁用在登录屏幕上（通过键盘）调整系统音量时听到的声音反馈。 

创建以下密钥文件： 
    
    /etc/dconf/db/gdm.d/04-sound
    
    [org/gnome/desktop/sound]
    event-sounds=false

然后重新编译GDM database，或作为GDM用户执行以下操作： 
    
    [gdm]$ dbus-launch gsettings set org.gnome.desktop.sound event-sounds 'false'
    
####  更改电源按钮行为

**注意：**

  * 对于电源键的设置 [logind 设置](<../zh-cn/Power_management.html#ACPI_%E4%BA%8B%E4%BB%B6> "Power management") 已被 GNOME Settings Daemon 覆盖。 [[1]](<https://bugzilla.gnome.org/show_bug.cgi?id=755953#c4>)
  * 自从 GDM 3.18起，电源键不能被设置为交互式 (_interactive_). [[2]](<https://bugzilla.gnome.org/show_bug.cgi?id=753713#c6>)
  * 在某些情况下，这条设置会被忽略，而采用硬编码产生的的默认值。[[3]](<https://bugzilla.gnome.org/show_bug.cgi?id=755953#c17>)

**警告：** 请注意， [acpid](<../zh-cn/Acpid.html> "Acpid") 守护进程也会控制“电源键”和“休眠键”相关事件。同时运行两套系统可能导致意外的结果。

创建如下的 keyfile: 
    
    /etc/dconf/db/gdm.d/05-power
    
    [org/gnome/settings-daemon/plugins/power]
    power-button-action='_action_ '

然后重新编译GDM database，或作为GDM用户并执行以下操作： 
    
    [gdm]$ dbus-launch gsettings set org.gnome.settings-daemon.plugins.power power-button-action '_action_ '
    
这里 _action_ 可以是 `nothing`, `suspend` 或 `hibernate` 其中之一。 

####  开启触摸板轻触以点击

GDM（和GNOME）中默认关闭轻触以点击，但可以使用dconf设置开启它。 

**注意：** 如果想要在X下这么做，必须先正确配置X服务器的访问权限，见 [#配置X服务器的访问权限](<#%E9%85%8D%E7%BD%AEX%E6%9C%8D%E5%8A%A1%E5%99%A8%E7%9A%84%E8%AE%BF%E9%97%AE%E6%9D%83%E9%99%90>)。

若要启用轻触以点击，创建以下keyfile： 
    
    /etc/dconf/db/gdm.d/06-tap-to-click
    
    [org/gnome/desktop/peripherals/touchpad]
    tap-to-click=true

然后重新编译GDM database，或作为GDM用户执行以下操作： 
    
    [gdm]$ dbus-launch gsettings set org.gnome.desktop.peripherals.touchpad tap-to-click 'true'
    
####  开启或关闭无障碍菜单

[![](../File:Tango-view-refresh-red.png)](<../File:Tango-view-refresh-red.png>)**本文或本节内容已经过时。**

**原因：** 对于 GDM 43，以下配置 keyfile 无效，尽管官方文档仍然这样说明[[4]](<https://help.gnome.org/admin/gdm/3.26/configuration.html.en#accessibilityconfiguration>)。请使用 `org.gnome.desktop.a11y.applications screen-keyboard-enabled true` key。 (在[Talk:GDM](<../zh-cn/Talk:GDM.html>)讨论)

若要禁用或启用无障碍菜单，创建以下 keyfile： 
    
    /etc/dconf/db/gdm.d/07-accessibility
    
    [org/gnome/desktop/interface]
    toolkit-accessibility='_boolean_ '

然后重新编译GDM database，或作为GDM用户执行以下操作： 
    
    [gdm]$ dbus-launch gsettings set org.gnome.desktop.interface toolkit-accessibility '_boolean_ '
    
当key的值为`false`时，无障碍菜单默认关闭；`true`则开启。 

####  在 GDM 上启用夜间模式

欲启用[夜间模式](<../zh-cn/GNOME.html#%E5%A4%9C%E9%97%B4%E6%A8%A1%E5%BC%8F> "GNOME")，运行 
    
    [gdm]$ dbus-launch gsettings set org.gnome.settings-daemon.plugins.color night-light-enabled true

###  键盘布局

GDM 需要 `/etc/vconsole.conf` 中设置 `XKBLAYOUT` 参数；如果没有设置，它将默认使用标准的 `us`（qwerty）布局，即不会遵循 `KEYMAP` 中设置的值。 

一种普遍适用的方法是使用 `localectl --no-convert set-x11-keymap [keymap]`：详情参见 [Keyboard configuration in Xorg#Setting keyboard layout](</wzh/index.php?title=Keyboard_configuration_in_Xorg&action=edit&redlink=1> "Keyboard configuration in Xorg（页面不存在）")。 

**警告：** 使用 `localectl set-x11-keymap` 而不带 `--no-convert` 也会改变 `KEYMAP=` 的值，如果使用包含重音字符的密码短语[加密整个系统](</wzh/index.php?title=Dm-crypt/Encrypting_an_entire_system&action=edit&redlink=1> "Dm-crypt/Encrypting an entire system（页面不存在）")，可能会导致系统无法启动。参见 [systemd issue #34967](<https://github.com/systemd/systemd/issues/34967>)。

###  更改语言

系统语言将应用于 GDM。如果系统有多个用户，则可以为 GDM 设置与系统语言不同的语言。在这种情况下，首先请确保安装了 [gnome-control-center](<https://archlinux.org/packages/?name=gnome-control-center>)包。然后，启动 _gnome-control-center_ 并选择“区域和语言”。在标题栏中，选中 _登录屏幕_ 切换按钮。最后，单击 _语言_ 并从列表中选择您的语言。系统将提示您输入 root 密码。请注意，除非系统上存在多个用户，否则标题栏中的“登录屏幕”按钮将不可见 [[5]](<https://bugzilla.gnome.org/show_bug.cgi?id=741500>)。 

**提示：** 添加 2 种不同的输入语言后，注销。然后选择您的默认语言，GDM 将在第二个选项被删除后记住您的选择。

###  用户与登录

####  自动登录

**警告：** 不要尝试对由 [systemd-homed](<../zh-cn/Users_and_groups.html#%E7%94%A8%E6%88%B7%E7%BB%84%E7%AE%A1%E7%90%86> "Users and groups") 管理的用户执行此操作。 这是目前 [未解决](<https://github.com/systemd/systemd/issues/20844>) 的漏洞，并且会使 GDM 崩溃。

将以下内容添加至`/etc/gdm/custom.conf`以开启自动登录（将 _username_ 替换为您的用户名）： 
    
    /etc/gdm/custom.conf
    
    # Enable automatic login for user
    [daemon]
    AutomaticLogin=_username_
    AutomaticLoginEnable=True

**提示：** 如果在添加这些行后 GDM 失败，请从 TTY 中将它们注释掉。

或延迟自动登录： 
    
    /etc/gdm/custom.conf
    
    [daemon]
    TimedLoginEnable=true
    TimedLogin=_username_
    TimedLoginDelay=1

您可以设置用于自动登录的会话（将 `gnome-xorg` 替换为所需的会话）： 
    
    /var/lib/AccountsService/users/_username_
    
    XSession=gnome-xorg

####  免密登录

如果您想绕过 GDM 中的密码提示，只需在 `/etc/pam.d/gdm-password` 的第一行添加以下行： 
    
    auth sufficient pam_succeed_if.so user ingroup nopasswdlogin
    
然后，将 `nopasswdlogin` 组加入您的系统。详见[用户组](<../zh-cn/Users_and_groups.html#%E7%94%A8%E6%88%B7%E7%BB%84%E7%AE%A1%E7%90%86> "Users and groups")以获得组的描述和组管理相关命令 。 

现在，把您的用户加入 `nopasswdlogin` 组，然后您只需点击您的用户名以登录。 

**警告：**

  * **不要** 对**root** 账户这么做。
  * 您将无法在使用 GDM 登录时更改会话类型。 如果您想更改默认会话类型，您首先需要从 `nopasswdlogin` 组中删除您的用户。

####  禁用指纹登录

当使用[指纹](<../zh-cn/Fprint.html> "Fprint")登录时，它不会解锁密钥环，因此您仍然会被提示输入密钥环密码。您可能希望禁用登录并保留指纹以解锁会话。为此，只需为 GDM 用户禁用指纹。 

临时以 GDM 用户身份执行以下命令并更改此设置： 
    
    [gdm]$ dbus-launch gsettings set org.gnome.login-screen enable-fingerprint-authentication false
    
####  多个会话的无密码关闭

GDM 使用 polkit 和 logind 来获得关机权限。 当多个用户登录时，您可以通过设置以关闭系统： 
    
    /etc/polkit-1/localauthority.conf.d/org.freedesktop.logind.policy
    
    <?xml version="1.0" encoding="UTF-8"?>
    <!DOCTYPE policyconfig PUBLIC
     "-//freedesktop//DTD PolicyKit Policy Configuration 1.0//EN"
     "http://www.freedesktop.org/software/polkit/policyconfig-1.dtd">
    
    <!--
    Policy definitions for logind
     -->
    
    <policyconfig>
    
      <action id="org.freedesktop.login1.power-off-multiple-sessions">
        <description>Shutdown the system when multiple users are logged in</description>
        <message>System policy prevents shutting down the system when other users are logged in</message>
        <defaults>
          <allow_inactive>yes</allow_inactive>
          <allow_active>yes</allow_active>
        </defaults>
      </action>
    
    </policyconfig>
    
您可以找到所有可用的 logind 选项（比如，reboot-multiple-sessions，即重启多用户会话）在 [org.freedesktop.login1(5)](<https://man.archlinux.org/man/org.freedesktop.login1.5>) 中。 

####  在GDM中开启root登录

我们并不建议您以 root 登录，但如果必要，请编辑 `/etc/pam.d/gdm-password` 并在行 `auth required pam_deny.so` 前添加以下行： 
    
    /etc/pam.d/gdm-password
    
    auth            sufficient      pam_succeed_if.so uid eq 0 quiet
    
这个文件应当看起来如下： 
    
    /etc/pam.d/gdm-password
    
    ...
    auth            sufficient      pam_succeed_if.so uid eq 0 quiet
    auth            sufficient      pam_succeed_if.so uid >= 1000 quiet
    auth            required        pam_deny.so
    ...

重启 GDM 后，您可以用 root 身份登录。 

####  在登录列表中隐藏用户

gdm 用户列表的用户由 [[6]](<https://www.freedesktop.org/wiki/Software/AccountsService/AccountsService>)[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2022-09-17 ⓘ] 收集。 它会自动隐藏系统用户（UID < 1000）。 要从登录列表中隐藏普通用户，请创建或编辑一个以用户命名的文件，并将其保存在 `/var/lib/AccountsService/users/` 中，随之隐藏该文件。文件至少应包含： 
    
    /var/lib/AccountsService/users/_username_
    
    [User]
    SystemAccount=true

####  通过 RDP 的远程登录

**注意：** 当前只能创建无显示器的远程会话。

**注意：** 一次只能存在一个图形化会话。若另一个图形化会话存在，尝试创建新图形化会话会杀死它。

#####  通过图形化接口

可在 Gnome 设置程序中找到“系统>远程桌面>远程登录”来图形化地配置远程登录。 

#####  通过终端接口

**注意：** 要生效，Gnome 远程桌面同时要求 TLS 证书和凭证。除非预先设置过，否则两者都不存在，需要手动设置。

要显示当前状态和凭证，可采用以下命令： 
    
    # grdctl --system status --show-credentials
    
要设置凭证： 
    
    # grdctl --system rdp set-credentials _rdp_login_ _rdp_password_
    
要生成新的 TLS 密钥和证书： 
    
    # winpr-makecert3 -rdp -path /etc/gnome-remote-desktop -n rdp-tls
    
若省略了 `-n rdp-tls` 部分，就会使用 _hostname_ 作为名字。 

要设置新的 TLS 密钥和证书： 
    
    # grdctl --system rdp set-tls-key /etc/gnome-remote-desktop/rdp-tls.key
    # grdctl --system rdp set-tls-cert /etc/gnome-remote-desktop/rdp-tls.crt
    
最终，启用远程登录： 
    
    # grdctl --system rdp enable
    
###  设置默认显示器

一些[桌面环境](<../zh-cn/%E6%A1%8C%E9%9D%A2%E7%8E%AF%E5%A2%83.html> "桌面环境")将显示设置保存在 `~/.config/monitors.xml`。 _xrandr_ 命令基于该文件内容生成信息。在GDM中类似内容保存在`/var/lib/gdm/.config/monitors.xml`。 

若有显示器设置（例如朝向，缩放，主屏幕等等）信息记录于`~/.config/monitors.xml`中，并且想要让这些设置用于GDM： 
    
    # cp ~/.config/monitors.xml /var/lib/gdm/.config/
    
要在每次启动时自动重新配置显示器设置，为 `gdm.service` 使用 [Systemd#附加配置片段](<../zh-cn/Systemd.html#%E9%99%84%E5%8A%A0%E9%85%8D%E7%BD%AE%E7%89%87%E6%AE%B5> "Systemd")： 
    
    /etc/systemd/system/gdm.service.d/override.conf
    
    [Service]
    ExecStartPre=/bin/cp /home/_user_ /.config/monitors.xml /var/lib/gdm/.config/monitors.xml

`monitors.xml`文件中屏幕旋转和缩放的部分内容如下： 
    
    <monitors version="2">
      <configuration>
        <logicalmonitor>
          ...
          <scale>2</scale>
          ...
          <transform>
            <rotation>right</rotation>
            <flipped>no</flipped>
          </transform>
          ...
        </logicalmonitor>
      </configuration>
    </monitors>
    
必须登出才能使更改生效，因为GDM不遵守`xorg.conf`。 

**注意：**

  * 如果在Wayland下使用GDM，则必须使用在Wayland下创建的`monitors.xml`。详见[GDM bug 224](<https://gitlab.gnome.org/GNOME/gdm/issues/224>)。也可以强制让GDM [#使用Xorg后端](<#%E4%BD%BF%E7%94%A8Xorg%E5%90%8E%E7%AB%AF>)，并使用在Xorg下创建的`monitors.xml`。
  * 如果您使用 [fractional scaling (分数缩放)](<../zh-cn/HiDPI.html#Fractional_scaling> "HiDPI")，您需要为用户 `gdm` 启用它：

     [gdm]$ dbus-launch gsettings set org.gnome.mutter experimental-features "['scale-monitor-framebuffer']"
    
###  配置X服务器的访问权限

您可以使用 `xhost` 命令来配置 X 服务器的访问权限。 

例如，要授予 GDM 访问 X 服务器的权限，请使用以下命令： 
    
    # xhost +SI:localuser:gdm

##  疑难解答

###  Wayland 与 NVIDIA 专有驱动

要在 GDM 中使用带有 [NVIDIA](<../zh-cn/NVIDIA.html> "NVIDIA") 驱动程序的 Wayland，您必须满足以下三个条件： 

  * 启用 [DRM KMS](<../zh-cn/NVIDIA.html#DRM_%E5%86%85%E6%A0%B8%E7%BA%A7%E6%98%BE%E7%A4%BA%E6%A8%A1%E5%BC%8F%E8%AE%BE%E7%BD%AE> "NVIDIA")；

  * [配置 Wayland](<../zh-cn/Wayland.html#%E7%B3%BB%E7%BB%9F%E9%9C%80%E6%B1%82> "Wayland")；

  * 遵循 [NVIDIA/Tips and tricks#Preserve video memory after suspend](</wzh/index.php?title=NVIDIA/Tips_and_tricks&action=edit&redlink=1> "NVIDIA/Tips and tricks（页面不存在）")。

从 GDM 42 和 NVIDIA 驱动程序 510 开始，GDM 默认为 Wayland。 对于较旧的 NVIDIA 驱动程序（版本 470 和 510 之间），GDM 具有依赖于芯片组的 [udev 规则](<https://gitlab.gnome.org/GNOME/gdm/-/blob/main/data/61-gdm.rules.in>)使用 Xorg 而不是 Wayland。 要强制启用 Wayland，**不** 遵循上述三个常规步骤，请通过创建以下符号链接来覆盖这些规则： 
    
    # ln -s /dev/null /etc/udev/rules.d/61-gdm.rules
    
**注意：** 此命令之所以有效，是因为 `/etc/udev/rules.d/` 中的规则会覆盖 `/usr/lib/udev/rules.d/` 中的规则（参见 [Udev#About udev rules](<../zh-cn/Udev.html#About_udev_rules> "Udev")）。 建议修改 `/etc/` 中的文件，而非 `/usr/` 中的文件，也是因为 `/etc/` 中的文件由 [pacman](<../zh-cn/Pacman.html> "Pacman") 管理。

如果出现黑屏而不是 GDM，请尝试在计算机的 BIOS 设置中禁用集成显卡。 

一些情况下，GNOME 无法启动，将控制权转回 GDM，最终导致登录页面重复出现。您可以尝试设置以下环境变量，参考[BBS#2126478](<https://bbs.archlinux.org/viewtopic.php?pid=2126478>)： 
    
    /etc/environment
    
    MUTTER_DEBUG_KMS_THREAD_TYPE=user

###  注销失败

如果 GDM 在启动时正常启动，但在多次尝试注销后失败，请尝试将此行添加到 `/etc/gdm/custom.conf` 的守护程序部分： 
    
    GdmXserverTimeout=60
    
###  无 root 的 Xorg

见[Xorg#没有 root 权限的 Xorg](<../zh-cn/Xorg.html#%E6%B2%A1%E6%9C%89_root_%E6%9D%83%E9%99%90%E7%9A%84_Xorg> "Xorg")。 

###  使用Xorg后端

默认使用 [Wayland](<../zh-cn/Wayland.html> "Wayland") 后端，只有在 Wayland 后端无法启动时才使用 [Xorg](<../zh-cn/Xorg.html> "Xorg") 后端。在以下情况下，您可能希望使用 Xorg 后端： 

  * GDM [崩溃](<https://bbs.archlinux.org/viewtopic.php?pid=1869534#p1869534>)

要默认使用 Xorg 后端，请在 `/etc/gdm/custom.conf` 中将以下行取消注释： 
    
    #WaylandEnable=false
    
###  没有完全卸载 GDM

删除 [gdm](<https://archlinux.org/packages/?name=gdm>)包 后，[systemd](<../zh-cn/Systemd.html> "Systemd") 可能会报告以下内容： 
    
    user 'gdm': directory '/var/lib/gdm' does not exist
    
要删除此警告，请以 root 身份登录并[删除私有用户](<../zh-cn/Users_and_groups.html#%E5%85%B6%E4%BB%96%E7%94%A8%E6%88%B7%E7%AE%A1%E7%90%86%E7%A4%BA%E4%BE%8B> "Users and groups") `gdm` 然后[删除组](<../zh-cn/Users_and_groups.html#%E7%94%A8%E6%88%B7%E7%BB%84%E7%AE%A1%E7%90%86> "Users and groups") `gdm`： 

验证 `gdm` 是否已通过具有 root 权限的 `pwck` 和 `grpck` 成功删除。 解决这个问题 ，您可能需要仔细检查[无主文件](<../zh-cn/Pacman/Tips_and_tricks.html#Identify_files_not_owned_by_any_package> "Pacman/Tips and tricks")是否保留 _gdm_ 。 

###  GDM自动挂起（GNOME 3.28）

GDM 使用单独的 dconf 数据库来控制电源管理。要应用用户的电源设置，请将它们复制到 GDM 的 dconf 数据库： 
    
    $ IFS=$'\n'; for x in $(sudo -u _username_ gsettings list-recursively org.gnome.settings-daemon.plugins.power); do eval "sudo -u gdm dbus-launch gsettings set $x"; done; unset IFS
    
这里 `_username_` 是您的用户名。 

欲仅禁用 AC 上的自动挂起，运行： 
    
    [gdm]$ dbus-launch gsettings set org.gnome.settings-daemon.plugins.power sleep-inactive-ac-type 'nothing'
    
（要同时禁用电池自动挂起，请使用 `battery` 而不是 `ac` 运行命令。） 

重新启动 GDM 以激活您的更改。 

###  GDM 忽略了 Wayland，默认使用 X.Org

Wayland 需要运行内核模式设置 (KMS) 才能工作，并且在某些机器上 GDM 进程比 KMS 更早启动，导致 GDM 无法看到 Wayland 并且只能使用 X.Org。 这可能会导致您的日志中显示如下消息： 
    
    gnome-shell[569]: Failed to open gpu '/dev/dri/card0': GDBus.Error:org.freedesktop.DBus.Error.AccessDenied: Operation not permitted
    gnome-shell[569]: Failed to create backend: No GPUs found
    systemd[505]: org.gnome.Shell@wayland.service: Failed with result 'protocol'.
    systemd[505]: Failed to start GNOME Shell on Wayland.
    
或者，同样的问题可能会导致 GDM 不出现或监视器仅显示 TTY 输出。 

您可以通过[尽早启动 KMS（缺失中文翻译）](<../zh-cn/Kernel_mode_setting.html#Early_KMS_start> "Kernel mode setting")来解决这个问题。您可能还希望仅验证在 GDM 配置中启用了 Wayland,（[见上文](<#%E4%BD%BF%E7%94%A8Xorg%E5%90%8E%E7%AB%AF>)）。 

此外，如果您使用 [NVIDIA](<../zh-cn/NVIDIA.html> "NVIDIA") 驱动程序，Wayland 会话可能会被 [udev](<../zh-cn/Udev.html> "Udev") 规则阻止（请参阅 [GNOME#Wayland 会话](<../zh-cn/GNOME.html#Wayland_%E4%BC%9A%E8%AF%9D> "GNOME")下的注释）。 这可能会导致如下消息： 
    
    systemd[1022]: Condition check resulted in GNOME Shell on Wayland being skipped.
    systemd[1022]: org.gnome.Shell@wayland.service: Skipped due to 'exec-condition'.
    systemd[1022]: org.gnome.Shell@wayland.service: Control process exited, code=exited, status=2/INVALIDARGUMENT
    
请参阅 [#Wayland与NVIDIA专有驱动](<#Wayland%E4%B8%8ENVIDIA%E4%B8%93%E6%9C%89%E9%A9%B1%E5%8A%A8>)作为解决方法。 

###  当存在 NVIDIA (e)GPU 时，AMD 或 Intel GPU 上出现黑屏

起初，在没有 NVIDIA 设备的情况下，GDM 可以在 Wayland 上正常启动和工作。但一旦插入 NVIDIA eGPU（或由于其他原因加载 `nvidia` 模块），GDM 就会停止工作。该问题的一个典型表现是在注销和 GDM 重新启动时出现黑屏，并在 GDM 的日志中显示以下消息（通过以 root 身份运行 `journalctl -u gdm -b` 访问）： 
    
    Gdm: Child process -<some PID> was already dead.
    
解决方法同[上所描述](<#GDM_%E5%BF%BD%E7%95%A5%E4%BA%86_Wayland%EF%BC%8C%E9%BB%98%E8%AE%A4%E4%BD%BF%E7%94%A8_X.Org>): 防止 `/usr/lib/gdm-disable-wayland` 在 `nvidia` 模块加载时运行。 

请注意，一旦 `/usr/lib/gdm-disable-wayland` 运行，Wayland 上的 GDM 将不再工作。这是因为 `WaylandEnable=false` 已写入 `/run/gdm/custom.conf`，它会覆盖 `/etc/gdm/custom.conf`。要在不重新启动系统的情况下解决此问题，请删除 `/run/gdm/custom.conf`，然后重新启动 GDM。 

###  无法启用 GDM

参见 [systemd/FAQ#Failure to enable unit due to preexisting symlink](<../zh-cn/Systemd/FAQ.html#Failure_to_enable_unit_due_to_preexisting_symlink> "Systemd/FAQ")。 

##  另见

  * [GDM 参考手册](<https://help.gnome.org/admin/gdm/stable/index.html.en>)
