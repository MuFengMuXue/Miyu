**翻译状态：**

  * 本文（或部分内容）译自 [Firejail](<https://wiki.archlinux.org/title/Firejail> "arch:Firejail")，最近一次同步于 2023-01-02，若英文版本有所[更改](<https://wiki.archlinux.org/title/Firejail?diff=0&oldid=760357>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Firejail_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [安全](<../zh-cn/%E5%AE%89%E5%85%A8.html> "安全")
  * [AppArmor](<../zh-cn/AppArmor.html> "AppArmor")

[Firejail](<https://firejail.wordpress.com/>) 是一个易于使用的 SUID 沙盒程序，它通过使用 Linux 命名空间、seccomp-bpf 和 Linux 功能来限制不受信任的应用程序的运行环境以降低安全漏洞被利用的风险。 

**警告：** 运行不受信任的代码永远不安全，沙盒并不能挽救这个局面。

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [firejail](<https://archlinux.org/packages/?name=firejail>)包 或者 [firejail-git](<https://aur.archlinux.org/packages/firejail-git/>)AUR 包. 还有可以与 Firejail 一起使用的 GUI 应用程序, [firetools](<https://archlinux.org/packages/?name=firetools>)包. 

**注意：** 有关 Arch Linux 内核中的 [user_namespaces(7)](<https://man.archlinux.org/man/user_namespaces.7>) 支持的信息，请参阅 [Security#Sandboxing applications](<../zh-cn/%E5%AE%89%E5%85%A8.html#Sandboxing_applications> "Security"). [Firejail即使被禁用也可以使用](<https://github.com/netblue30/firejail/issues/1842#issuecomment-376642039>)。

**警告：** 虽然上游正在逐步采用白名单（参见`/etc/firejail/firefox.profile`），但大多数提供的配置文件仍然严重依赖黑名单。这意味着，任何没有被配置文件明确禁止的东西都会被应用程序访问。例如，如果你在`/mnt/btrfs`中有 btrfs 快照，沙盒里的程序可能被禁止访问`$HOME/.ssh`，但仍能访问`/mnt/btrfs/@some-snapshot/$HOME/.ssh`。请确保检查您的配置文件。见[#测试配置文件](<#%E6%B5%8B%E8%AF%95%E9%85%8D%E7%BD%AE%E6%96%87%E4%BB%B6>)。

##  配置

大多数用户不需要任何自定义配置，并且可以继续 [#使用方法](<#%E4%BD%BF%E7%94%A8%E6%96%B9%E6%B3%95>). 

Firejail 使用配置文件为其中执行的每个应用程序设置安全保护 - 您可以在 `/etc/firejail/_application_.profile` 中找到默认配置文件. 如果您需要为未包含的应用程序自定义配置文件，或者希望修改默认值, 您可以在 `~/.config/firejail/` 目录中放置新规则或默认值副本. 一个应用程序可能有多个自定义配置文件，并且您可以在多个应用程序之间共享同一个配置文件. 

如果 firejail 没有特定应用程序的配置文件，它会使用其限制性的系统范围默认配置文件。如果没有事先创建自定义且限制较少的配置文件，这可能会导致应用程序无法按预期运行。 

参阅 [firejail-profile(5)](<https://man.archlinux.org/man/firejail-profile.5>)。 

##  使用方法

要使用 firejail 对该应用程序的默认保护（默认配置文件）执行应用程序，请执行以下命令 : 
    
    $ firejail <应用程序名称>
    
一次性添加到默认配置文件可以作为命令行选项添加（参见 [firejail(1)](<https://man.archlinux.org/man/firejail.1>)）。 例如，要执行带有 seccomp 保护的 _okular_ ，请执行以下命令 : 
    
    $ firejail --seccomp okular
    
您可以为单个程序定义多个非默认配置文件。 创建配置文件后，您可以通过执行来使用它 : 
    
    $ firejail --profile=/absolute/path/to/profile <program name>
    
###  默认配置使用 Firejail

默认情况下将 Firejail 用于具有配置文件的所有应用程序 , [使用 sudo 运行 firecfg 工具](<https://github.com/netblue30/firejail/wiki/Frequently-Asked-Questions#a-program-isnt-firejailed>): 
    
    $ sudo firecfg
    
这将在`/usr/local/bin`中创建指向`/usr/bin/firejail`，用于 Firejail 有默认或自定配置文件的程序的符号链接。请注意，[firecfg(1)](<https://man.archlinux.org/man/firecfg.1>) 只与`/etc/firejail/firecfg.config`中列出的程序建立符号链接。某些命令行界面的程序是不存在的，例如 _tar_ 、 _curl_ 和 _git_ 。这些程序需要手动建立符号链接。请参阅 [Profiles not in firecfg #2507](<https://github.com/netblue30/firejail/issues/2507>) 了解为什么不包括这些程序。 _firecfg_ 还将当前用户加入 Firejail 用户访问数据库，并检查`/usr/share/applications/*.desktop`文件是否包含相应可执行文件的完整路径，然后删除完整路径并将其复制到`~/.local/share/applications/`。这确保了`/usr/local/bin`中的符号链接将被使用，从而防止 Firejail 被绕过。如果您的系统中没有安装 [sudo](<../zh-cn/Sudo.html> "Sudo")，请以 root 身份执行： 
    
    # firecfg
    
以及以一般用户执行： 
    
    $ firecfg --fix
    
以修复 _.desktop_ 文件 

在某些情况下，您可能需要手动修改`~/.local/share/applications/`中 ".desktop " 文件的`Exec=`行，以直接调用 Firejail。 

**提示：** 可使用 [pacman hook](<../zh-cn/Pacman_hook.html> "Pacman hook")来在 [pacman](<../zh-cn/Pacman.html> "Pacman") 操作中自动运行 _firecfg_ 。 
    
    /etc/pacman.d/hooks/firejail.hook
    
    [Trigger]
    Type = Path
    Operation = Install
    Operation = Upgrade
    Operation = Remove
    Target = usr/bin/*
    Target = usr/local/bin/*
    Target = usr/share/applications/*.desktop
    
    [Action]
    Description = Configure symlinks in /usr/local/bin based on firecfg.config...
    When = PostTransaction
    Depends = firejail
    Exec = /bin/sh -c 'firecfg >/dev/null 2>&1'

要手动链接各个应用程序，请执行以下操作： 
    
    # ln -s /usr/bin/firejail /usr/local/bin/_application_
    
**注意：**

  * `/usr/local/bin` must be set before `/usr/bin` and `/bin` in the `PATH` [environment variable](<../zh-cn/Environment_variable.html> "Environment variable").
  * To run a symbolic program with custom Firejail setting, simple prefix _firejail_ as seen in [#使用方法](<#%E4%BD%BF%E7%94%A8%E6%96%B9%E6%B3%95>).
  * For a daemon, you will need to overwrite the systemd unit file for that daemon to call firejail, see [systemd#Editing provided units](<../zh-cn/Systemd.html#Editing_provided_units> "Systemd").
  * Symbolic links to _gzip_ and _xz_ interfere with _makepkg_ 's ability to preload `libfakeroot.so`. See [BBS#230913](<https://bbs.archlinux.org/viewtopic.php?id=230913>).

### Use with hardened_malloc

[hardened_malloc](<https://aur.archlinux.org/packages/hardened_malloc/>)AUR is a hardened implementation of glibc's `malloc()` allocator, originally written for Android but extended for use on the desktop. While not integrated into glibc yet, it can be used selectively with `LD_PRELOAD`. The proper way to launch an application within firejail using hardened_malloc is demonstrated below. To make it permanent, you would need to create your own entry in /usr/local/bin for the desired application.__
    
    $ firejail --env=LD_PRELOAD='/usr/lib/libhardened_malloc.so' /usr/bin/firefox
    
Alternatively, add the following to a custom profile: 
    
    env LD_PRELOAD='/usr/lib/libhardened_malloc.so'
    
The various environment variables and settings that can be used to tune hardened_malloc can be found on its [github page](<https://github.com/GrapheneOS/hardened_malloc>). 

### Enable AppArmor support

Since 0.9.60-1, Firejail has supported more direct integration with AppArmor through a generic AppArmor profile. During installation, the profile, `firejail-default`, is placed in `/etc/apparmor.d` directory, and needs to be loaded into the kernel by running the following command as root: 
    
    # apparmor_parser -r /etc/apparmor.d/firejail-default
    
See [firejail(1) § APPARMOR](<https://man.archlinux.org/man/firejail.1#APPARMOR>). 

Local customizations of the apparmor profile are supported by editing the file `/etc/apparmor.d/local/firejail-local`

AppArmor is already enabled for a [large number](<https://github.com/netblue30/firejail#profile-statistics>) of Firejail profiles. There are several ways to enable [AppArmor](<../zh-cn/AppArmor.html> "AppArmor") confinement on top of a Firejail security profile: 

  * Pass the `--apparmor` flag to Firejail in the command line, e.g. `$ firejail --apparmor firefox`
  * Use a custom profile and add the `apparmor` command.
  * Enable Apparmor globally in `/etc/firejail/globals.local` and disable as needed through the use of `ignore apparmor` in `/etc/firejail/<ProgramName>.local`.

Note that enabling AppArmor by above methods **always** means that `/etc/apparmor.d/firejail-default` is used. If you rather want to use a _specific_ AppArmor profile for an application, you have to use the above mentioned `ignore apparmor` command. However, that is [not recommended](<https://github.com/netblue30/firejail/wiki/Frequently-Asked-Questions#how-does-it-compare-with-apparmor>), as using both Firejail and AppArmor for the same applications often creates problems. 

### Verifying Firejail is being used
    
    $ firejail --list
    
A more comprehensive output is produced by 
    
    $ firejail --tree
    
## Creating custom profiles

### Whitelists and blacklists

**Blacklists** are heavily used in various `/etc/firejail/*.inc` files which are included in most profiles. Blacklists are permissive: 

  * Deny access to a directory or file and permit everything else: `blacklist <directory/file>`
  * Disable/undo/ignore blacklisting a directory or file already blacklisted, e.g., in an _*.inc_ file: `noblacklist <directory/file>`

The order in which they appear in a profile is important: _noblacklist_ directives must be added **above** _blacklist_ directives. 

**Whitelists** block everything what is not _explicitly_ whitelisted. They should not be used in profiles for applications that need access to random locations (e.g., text editors, image viewers/editors). 

  * Allow access to a directory or file and forbid everything else: `whitelist <directory/file>`
  * Disable/undo/ignore whitelisting a directory or file already whitelisted, e.g., in an _*.inc_ file: `nowhitelist <directory/file>`

The order in which they appear in a profile is important: _nowhitelist_ directives must be added **above** _whitelist_ directives. 

Whitelisting is always done before blacklisting. As mentioned, a _whitelist_ directive blacklists everything else. A _blacklist_ directive is therefore a fallback if there are no _whitelist_ directives or if a _whitelist_ directive is too permissive. 

_(no)blacklist_ and _(no)whitelist_ directives are often used in combination. Example: `/etc/firejail/disable-programs.inc` (which is included in all profiles) contains the directive: 
    
    blacklist ${HOME}/.mozilla
    
in order to block access to that directory for all applications sandboxed by Firejail. `/etc/firejail/firefox.profile` must disable this directive **and** must add a _whitelist_ directive to allow access to that directory (as the Firefox profile is a whitelisted profile): 
    
    noblacklist ${HOME}/.mozilla
    whitelist ${HOME}/.mozilla
    
### Profile writing

The basic process is: 

  1. Copy `/usr/share/doc/firejail/profile.template` to `/etc/firejail/` or `~/.config/firejail/` and rename it to `_ProfileName_.profile` where _ProfileName_ should match the name of the executable to be sandboxed
  2. Change the line `include PROFILE.local` to `include ProfileName.local`
  3. Gradually comment/uncomment the various options while checking at each stage that the application runs inside the new sandbox. Do not change the order of the sections in that template.
  4. Detailed explanations of the possible options for a Firejail profile can be found in the [firejail-profile(5)](<https://man.archlinux.org/man/firejail-profile.5>) man page
  5. Test the profile for security holes, see [#Testing profiles](<#Testing_profiles>)

If you want to create a whitelisted profile (i.e. a profile which contains _whitelist_ directives) you can [build a whitelist](<https://firejail.wordpress.com/documentation-2/building-custom-profiles/#whitelisted>) of permitted locations by executing 
    
    $ firejail --build _application_
    
Keep in mind that a whitelisted profile is problematic for applications that need to access random locations (like text editors or file managers). 

**注意：**

  * The idea is to be as restrictive as possible, while still maintaining usability. This may involve sacrificing potentially dangerous functionality and a change in cavalier work habits.
  * By default, seccomp filters work on a blacklist (which can be found in `/usr/share/doc/firejail/syscalls.txt`). It is possible to use `seccomp.keep` to build a custom whitelist of filters for an application. [[1]](<https://firejail.wordpress.com/documentation-2/seccomp-guide/>). A convenient way to automate these steps is to execute `/usr/lib/firejail/syscalls.sh`. If the application is still broken because of missing syscalls, you should follow the instructions at the bottom of `/usr/share/doc/firejail/syscalls.txt`.

#### Persistent local customisation

The standard profile layout includes the capability to make persistent local customisations through the inclusion of `.local` files[[2]](<https://github.com/netblue30/firejail/wiki/Creating-overrides>). Basically, each officially supported profile contains the lines `include ProgramName.local` and `include globals.local`. These _*.local_ files might be located in `/etc/firejail` or in `~/.config/firejail`. Since the order of precedence is determined by which is read first, this makes for a very powerful way of making local customisations. For example, with reference [this firejail question](<https://github.com/netblue30/firejail/issues/1510#issuecomment-326443650>), to globally enable Apparmor and disable Internet connectivity, one could simply create/edit `/etc/firejail/globals.local` to include the lines 
    
    # enable Apparmor and disable Internet globally
    net none
    apparmor
    
Then, to allow, for example, "curl" to connect to the internet, yet still maintain its apparmor confinement, one would create/edit `/etc/firejail/curl.local` to include the lines. 
    
    # enable internet for curl
    ignore net
    
Since `curl.local` is read before `globals.local`, `ignore net` overrides `net none`, and, as a bonus, the above changes would be persistent across future updates. 

### Testing profiles

In order to test and audit a Firejail profile you may find the following to be useful: 

  1. `firejail --debug $Program > $PathToOutputFile` Gives a detailed breakdown of the sandbox
  2. `firejail --debug-blacklists $Program` and `firejail --debug-whitelists $Program` show the blacklisted and whitelisted directories and files for the current profile.
  3. `firejail --debug-caps` gives a list of caps supported by the current Firejail software build. This is useful when building a [caps whitelist](<https://l3net.wordpress.com/2015/03/16/firejail-linux-capabilities-guide/>).
  4. `firejail --help` for a full list of `--debug` options
  5. `firemon PID` monitors the running process. See `firemon --help` for details
  6. Executing `sudo jailcheck` tests running sandboxes. See the [jailcheck(1)](<https://man.archlinux.org/man/jailcheck.1>) man page for details.
  7. [checksec](<https://archlinux.org/packages/?name=checksec>)包 may also be useful in testing which standard security features are being used

## Firejail with Xorg

[![](../File:Tango-inaccurate.png)](<../File:Tango-inaccurate.png>)**本文或本章节的事实准确性存在争议。**

**原因：** Why does sandboxing X11 require DNS?（在 [Talk:Firejail](<../zh-cn/Talk:Firejail.html>) 中讨论）

On [Xorg](<../zh-cn/Xorg.html> "Xorg") any program can listen to all keyboard input and record all screens. The purpose of sandboxing X11 is to restrict this behavior, which is especially problematic for complex programs working with potentially malicious input like browsers. 

[Xephyr](<../zh-cn/Xephyr.html> "Xephyr") and [Xpra](</wzh/index.php?title=Xpra&action=edit&redlink=1> "Xpra（页面不存在）") allow you to sandbox Xorg. Although Xpra provides full clipboard support, it is recommended to use Xephyr due to the very notable and permanent lag with nested X11 sessions. 

For a complete setup with (not ideal) clipboard support (clipboard is still always shared), see [Sakaki's Gentoo guide](<https://wiki.gentoo.org/wiki/User:Sakaki/Sakaki%27s_EFI_Install_Guide/Sandboxing_the_Firefox_Browser_with_Firejail#Graphical_Isolation_via_Xephyr> "gentoo:User:Sakaki/Sakaki's EFI Install Guide/Sandboxing the Firefox Browser with Firejail"), especially the [section about the clipboard and automatic rescaling](<https://wiki.gentoo.org/wiki/User:Sakaki/Sakaki%27s_EFI_Install_Guide/Sandboxing_the_Firefox_Browser_with_Firejail#Setting_Up_Clipboard_Sharing_and_Display_Rescaling_for_Xephyr> "gentoo:User:Sakaki/Sakaki's EFI Install Guide/Sandboxing the Firefox Browser with Firejail"). 

Alternatively, if clipboard support is not needed but windows need to be managed, install a standalone [window manager](<../zh-cn/Window_manager.html> "Window manager") such as [Openbox](<../zh-cn/Openbox.html> "Openbox"). 

`xephyr-screen _Width_ x _Height_` can be set in `/etc/firejail/firejail.config` where `_Width_` and `_Height_` are in pixels and based on your screen resolution. 

To open the sandbox: 
    
    $ firejail --x11 --net=_device_ openbox
    
`_device_` is your active [network interface](</wzh/index.php?title=Network_interface&action=edit&redlink=1> "Network interface（页面不存在）"), which is needed to ensure that DNS works. Then right click and select your applications to run. 

**注意：** If you use [Unbound](<../zh-cn/Unbound.html> "Unbound"), [dnsmasq](<../zh-cn/Dnsmasq.html> "Dnsmasq"), [Pdnsd](</wzh/index.php?title=Pdnsd&action=edit&redlink=1> "Pdnsd（页面不存在）") or any other local resolver on 127.0.0.1, you would leave `--net=_device_` out of the command as DNS should work automatically.

See the [Firejail Wordpress site](<https://firejail.wordpress.com/documentation-2/x11-guide/#configurexephyr>) for a simpler guide. 

According to the guide: 

    The sandbox replaces the regular X11 server with Xpra or Xephyr server. This prevents X11 keyboard loggers and screenshot utilities from accessing the main X11 server.

Note that the statement: 

    The only way to disable the abstract socket `@/tmp/.X11-unix/X0` is by using a network namespace. If for any reasons you cannot use a network namespace, the abstract socket will still be visible inside the sandbox. Hackers can attach keylogger and screenshot programs to this socket.

is incorrect, [xserverrc](<../zh-cn/Xinit.html#xserverrc> "Xinit") can be edited to `-nolisten local`, which disables the abstract sockets of X11 and helps isolate it. 

### Sandboxing a browser

[Openbox](<../zh-cn/Openbox.html> "Openbox") can be configured to start a certain browser at startup. `_program_.profile` is the respective profile contained in `/etc/firejail`, and `--startup "_command_ "` is the command line used to start the program. For example, to start Chromium in the sandbox: 
    
    $ firejail --x11 --profile=/etc/firejail/chromium.profile openbox --startup "chromium"
    
## Tips and tricks

### Hardening Firejail

The security risk of Firejail being a SUID executable can be mitigated by adding the line 
    
    force-nonewprivs yes
    
to `/etc/firejail/firejail.config`. However, this can break specific applications. On Arch Linux, VirtualBox doesn't start anymore. With the [linux-hardened](<https://archlinux.org/packages/?name=linux-hardened>)包 kernel Wireshark and Chromium-based browsers are also affected. 

Further hardening measures include creating a special firejail group with adding the user to that group and changing the file mode for the firejail executable. For details see [here](<https://firejail.wordpress.com/documentation-2/basic-usage/#suid>). 

### Paths containing spaces

If you need to reference, whitelist, or blacklist a directory within a custom profile, such as with [palemoon](<https://aur.archlinux.org/packages/palemoon/>)AUR, you must do so using the absolute path, without encapsulation or escapes: 
    
    /home/user/.moonchild productions
    
### Private mode

Firejail also includes a one time private mode, in which no mounts are made in the chroots to your home directory. In doing this, you can execute applications without performing any changes to disk. For example, to execute okular in private mode, do the following: 
    
    $ firejail --seccomp --private okular
    
### Experimental improved tools

Some of the Firejail developers recognized issues with the tools it ships with and made their own, improved versions of them. 

**警告：** As stated in some of the projects descriptions, these tools might be experimental.

  * [firecfg.py](<https://github.com/rusty-snake/firecfg.py>), an improved version of `firecfg`.
  * [fjp](<https://github.com/rusty-snake/fjp>), a tool to interact with Firejail profiles.
  * [firejail-handler-http](<https://github.com/glitsj16/firejail-handler-http>), which helps with opening HTTP(S) links properly when sandboxing applications.
  * [firejail-handler-extra](<https://github.com/glitsj16/firejail-handler-extra>), like above but handles other protocols.

##  疑难解答

Firejail 可能很难调试。配置错误或其他不合适设置的症状包括随机分段故障、应用程序挂起和简单的错误信息。 

有些应用程序比其他应用程序更难沙箱化。例如，[网络浏览器](<../zh-cn/%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F%E5%88%97%E8%A1%A8/%E4%BA%92%E8%81%94%E7%BD%91.html#%E7%BD%91%E7%BB%9C%E6%B5%8F%E8%A7%88%E5%99%A8> "网络浏览器")和 [Electron](</wzh/index.php?title=Electron&action=edit&redlink=1> "Electron（页面不存在）") 应用程序往往比其他应用程序需要更多的故障排除，因为可能出错的地方很多。首先查看 [FAQ](<https://github.com/netblue30/firejail/wiki/Frequently-Asked-Questions>) 与 [open issues](<https://github.com/netblue30/firejail/issues>) 是至关重要的，因为调试可能需要相当长的时间。 

**提示：** 另请参阅[上游维基](<https://github.com/netblue30/firejail/wiki>)，尤其是其中有关[调试 Firejail](<https://github.com/netblue30/firejail/wiki/Debugging-Firejail>) 的页面。

###  移除 Firejail 的符号链接

要移除 Firejail 创建的符号链接（例如重置为默认值）： 
    
    # firecfg --clean
    
如果您不想在特定应用程序中使用 Firejail（例如，因为您更喜欢使用 AppArmor 对其进行限制），则必须手动删除相关的符号链接： 
    
    # rm /usr/local/bin/_application_
    
由于后续执行 _firecfg_ 时会重新添加已删除的符号链接，因此应在 `/etc/firejail/firecfg.config` 中对相应应用程序进行注释。 

验证 Firejail 是否仍然覆盖[桌面项](<../zh-cn/%E6%A1%8C%E9%9D%A2%E9%A1%B9.html> "桌面项")的任何残留内容。 

### PulseAudio

**注意：** 使用 PulseAudio 9.0 或更高版本应该可以解决这个问题。

如果 Firejail 会导致沙盒应用程序出现 [PulseAudio](<../zh-cn/PulseAudio.html> "PulseAudio") 有关问题[[3]](<https://github.com/netblue30/firejail/wiki/Frequently-Asked-Questions#pulseaudio-7080-issue>)，可以使用以下命令： 
    
    $ firecfg --fix-sound
    
此命令会为 _当前_ 用户创建一个自定义 `~/.config/pulse/client.conf` 文件，其中包含 `enable-shm = no` 和其他可能的变通方法。 

### hidepid

如果系统使用 [hidepid](</wzh/index.php?title=Hidepid&action=edit&redlink=1> "Hidepid（页面不存在）") [内核参数](<../zh-cn/%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0.html> "内核参数")，Firemon 只能以 root 身份运行。这将导致 Firetools GUI 错误报告 "Capabilities"、"Protocols" 和 "Seccomp"[[4]](<https://github.com/netblue30/firejail/issues/1564>) 的状态等问题。 

###  Nvidia 专有驱动程序

一些用户报告（例如 [[5]](<https://github.com/netblue30/firejail/issues/1753>)、[[6]](<https://github.com/netblue30/firejail/issues/879>) 或 [[7]](<https://github.com/netblue30/firejail/issues/841>)）称，在使用 Firejail 和 [NVIDIA](<../zh-cn/NVIDIA.html> "NVIDIA") 专有图形驱动程序时会出现问题。通常禁用应用程序的 `noroot` 选项即可解决这一问题。Firejail 选项。 

###  \--net 选项和 Linux 内核 >= 4.20.0

在使用 linux >= 4.20.0 时，firejail 0.5.96 存在一个错误，请参见 [[8]](<https://github.com/netblue30/firejail/issues/2314>) 和 [[9]](<https://github.com/netblue30/firejail/pull/2327>)。 

错误信息示例： 
    
    $ firejail --noprofile --net=eth0 ls
    Parent pid 8521, child pid 8522
    Error send: arp.c:182 arp_check: Invalid argument
    Error: proc 8521 cannot sync with peer: unexpected EOF
    Peer 8522 unexpectedly exited with status 1
    
###  警告： 无法使用 AppArmor 限制应用程序

[![](../File:Merge-arrows-2.png)](<../File:Merge-arrows-2.png>)**本文或本章节可能需要合并到[#启用 AppArmor 支持](<#%E5%90%AF%E7%94%A8_AppArmor_%E6%94%AF%E6%8C%81>)。**

**附注：** 应在前文中明确说明启用 AppArmor 的要求。请注意，Manjaro 的引用是不相关的。（在 [Talk:Firejail](<../zh-cn/Talk:Firejail.html>) 中讨论）

对于某些应用程序（如 [Firefox](<../zh-cn/Firefox.html> "Firefox") [[10]](<https://archived.forum.manjaro.org/t/firejail-apparmor-needs-kernel-patch/97700/3>)）启动 Firejail 时可能会出现以下警告： 
    
    Warning: Cannot confine the application using AppArmor.
    Maybe firejail-default AppArmor profile is not loaded into the kernel.
    As root, run "aa-enforce firejail-default" to load it.
    
运行建议的命令时，您可能会看到 
    
    ERROR: Cache read/write disabled: interface file missing. (Kernel needs AppArmor 2.4 compatibility patch.)
    
这意味着 [AppArmor](<../zh-cn/AppArmor.html> "AppArmor") 未作为内核参数启用，因此必须根据 [AppArmor#安装](<../zh-cn/AppArmor.html#%E5%AE%89%E8%A3%85> "AppArmor")进行设置。 

###  /usr/bin/patch: **** Can't open patch file

这意味着 `PKGBUILD` 会使用 `patch` 和 `-i` 参数，因此需要在 `/etc/makepkg.conf` 中为 `$SRCDEST` 列出白名单。 

用 `$SRCDEST` 的值创建 [覆盖](<#Persistent_local_customisation>) `patch.local`： 
    
    whitelist _/path/to/makepkg/sources_
    
将 `PKGBUILD` 改为使用 `stdin` 也同样有效： 
    
    patch -p1 < ../_file.patch_
    
###  使用 AMDGPU 启动图形应用程序时挂起

当使用 AMDGPU 且 Mesa >= 19.3.4 时，某些图形应用程序（如 Firefox 和 mpv）会在启动时挂起。请参见 [[11]](<https://github.com/netblue30/firejail/issues/3219>)。该问题已在上游 [fixed](<https://github.com/netblue30/firejail/pull/3301>) 解决，因此 [firejail-git](<https://aur.archlinux.org/packages/firejail-git/>)AUR 应可正常工作。或者，为所有受影响的应用程序在 `etc/firejail` 中的配置文件中添加 `seccomp !kcmp`。如果它们已经有了 `seccomp` 语句，则可以将其连接为逗号分隔的列表，例如 `seccomp !chroot,!kcmp` 。 

###  守护进程/后台进程挂起

有一个[已知问题](<https://github.com/netblue30/firejail/issues/3491>)会阻止进程守护进程化。除了不使用 Firejail 对受影响的应用程序进行沙箱化之外，目前没有其他解决方案。因为这是 Firejail 内部的一个错误，任何配置都无法解决这个问题。幸运的是，问题中提到的应用程序通常没有很大的攻击面，因此在没有沙箱的情况下运行它们的风险相对较低。 

##  参见

  * [Firejail GitHub 项目页面](<https://github.com/netblue30/firejail>)
  * [bubblewrap](<../zh-cn/Bubblewrap.html> "Bubblewrap")，一个 Firejail 的最小替代方案
