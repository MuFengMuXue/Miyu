相关文章

  * [窗口管理器](<../zh-cn/%E7%AA%97%E5%8F%A3%E7%AE%A1%E7%90%86%E5%99%A8.html> "窗口管理器")

**翻译状态：**

  * 本文（或部分内容）译自 [EXWM](<https://wiki.archlinux.org/title/EXWM> "arch:EXWM")，最近一次同步于 2025-02-14，若英文版本有所[更改](<https://wiki.archlinux.org/title/EXWM?diff=0&oldid=827061>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/EXWM_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

EXWM 是一款基于 [Emacs](<../zh-cn/Emacs.html> "Emacs") 的[窗口管理器](<../zh-cn/%E7%AA%97%E5%8F%A3%E7%AE%A1%E7%90%86%E5%99%A8.html> "窗口管理器")。 

##  安装

确保已安装 [emacs](<https://archlinux.org/packages/?name=emacs>)包。还需要 [xorg-xinit](<https://archlinux.org/packages/?name=xorg-xinit>)包。 

在 Emacs 中安装 EXWM： `M-x package-install RET exwm RET`。 

编辑 [xinitrc](<../zh-cn/Xinit.html#xinitrc> "Xinitrc") 并添加： 
    
    exec emacs
    
在 emacs 初始化（init）文件中添加 
    
    (require 'exwm)
    (require 'exwm-config)
    (exwm-config-example)
    
以使用默认设置。如果想使用自己的设置，请使用 `(exwm-enable)` 而不是 `(exwm-config-example)` （也无需 `(require 'exwm-config)`）。 

还可以在服务器模式下启动 emacs，并通过命令行启动 EXWM。请参见 <https://github.com/ch11ng/exwm/issues/284> 。 

##  配置

EXWM 是一个完整的 X 窗口管理器，因此 Emacs 可以管理浏览器、vlc 等 X 窗口。您可以使用所有正常的 Emacs 窗口命令来控制窗口的位置。在 X 窗口（即非“正常”的 Emacs 缓冲区）中，有些命令会被 EXWM 捕捉，而不会传递给程序。这些键值存储在 `exwm-input-prefix-keys` 中。此外，您也可以通过自定义 `exwm-input-global-keys` 来设置全局命令。如果您不使用自定义功能，而希望在 elisp 中设置 `exwm-input-global-keys` ，请注意可能需要重启 EXWM（并在启用 exwm 之前设置 `exwm-input-global-keys`）。或者，你也可以尝试使用 ["or emacs" blog](<https://oremacs.com/2015/01/17/setting-up-ediff/>) 中的 `cset` 宏，它可以在不重启 EXWM 的情况下重新定义 `exwm-input-global-keys`。要使用 s-& 作为启动程序（如 firefox）的快捷键，可以这样做： 
    
    (setq exwm-input-global-keys `(,(kbd "s-&") .
                                   (lambda (command)
                                     (interactive (list (read-shell-command "$ ")))
                                     (start-process-shell-command command nil command))))
    
###  多显示器

EXWM 可以通过（可选）`exwm-randr` 软件包处理多显示器问题。在调用 `(exwm-enable)` 之前，您需要安装 [xrandr](<../zh-cn/Xrandr.html> "Xrandr") 并在 emacs 配置文件中启用 exwm-randr。您需要调整 “DP-1” 和 “DP-2” 的值，使其与您电脑使用的值一致；在命令行中调用 `xrandr` 不带参数，即可查看可用输出。 
    
    (require 'exwm-randr)
    (setq exwm-randr-workspace-output-plist '(1 "DP-1"))
    (add-hook 'exwm-randr-screen-change-hook
              (lambda ()
                (start-process-shell-command
                 "xrandr" nil "xrandr --output DP-1 --right-of DP-2 --auto")))
    (exwm-randr-enable)
    
###  系统托盘

EXWM 支持系统托盘，但默认情况下并未启用。要启用它，请在 dotemacs 文件中的 `(exwm-enable)` 前添加以下内容： 
    
    (require 'exwm-systemtray)
    (exwm-systemtray-mode 1)
    
之后可能需要调整高度；可以使用 `exwm-systemtray-height` 变量进行调整。 

##  嵌入 LXDE

EXWM 可以代替 openbox，让您仍然可以使用 [LXDE](<../zh-cn/LXDE.html> "LXDE") 会话管理工具。 

在这样做之前，请确保已为 emacs 设置好运行 EXWM 的启动文件（见上文） 

_lxsession_ 使用`~/.config/lxsession/LXDE/desktop.conf`中定义的[窗口管理器](<../zh-cn/%E7%AA%97%E5%8F%A3%E7%AE%A1%E7%90%86%E5%99%A8.html> "窗口管理器")。(默认情况下使用[Openbox](<../zh-cn/Openbox.html> "Openbox")）。如果该文件不存在，则会在 `/etc/xdg/lxsession/LXDE/desktop.conf` 中搜索。 

用 emacs 替换任一文件中的 `openbox-lxde`： 
    
    [Session]
    window_manager=emacs
    
### lxsession-logout

您可以在 emacs 中创建以下函数，以便在 LXDE 会话中干净利落地注销、关机或重启： 
    
    (defun exwm-logout ()
      (interactive)
      (recentf-save-list)
      (save-some-buffers)
      (start-process-shell-command "logout" nil "lxsession-logout"))
    
该功能会将最近的历史记录存储到磁盘中，提示您保存、丢弃或更改未保存缓冲区中的更改，然后启动注销管理器。你可以将此功能绑定到 emacs 中的任意键上。 

##  疑难解答

###  火狐浏览器屏幕撕裂

在某些程序中，特别是 Firefox 中，您可能会遇到屏幕撕裂现象。您可以试试 

  * 在首选项 > 高级 > 使用平滑滚动中关闭平滑滚动。
  * 安装（并激活）[Compton](<../zh-cn/Picom.html> "Compton") 或其他合成管理器：[Xorg#合成](<../zh-cn/Xorg.html#%E5%90%88%E6%88%90> "Xorg")。

###  令人困惑的缓冲区名称

您可能会看到缓冲区名称被命名为 “*EXWM*”。EXWM 允许缓冲区自行命名。要允许缓冲区自行命名，请在 dotemacs 中添加以下内容： 
    
    ;; Make buffer name more meaningful
    (add-hook 'exwm-update-class-hook
              (lambda ()
              (exwm-workspace-rename-buffer exwm-class-name)))
    
##  参见

  * [EXWM 维基](<https://github.com/emacs-exwm/exwm/wiki>)
