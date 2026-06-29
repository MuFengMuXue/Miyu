**翻译状态：**

  * 本文（或部分内容）译自 [Kanshi](<https://wiki.archlinux.org/title/Kanshi> "arch:Kanshi")，最近一次同步于 2025-05-15，若英文版本有所[更改](<https://wiki.archlinux.org/title/Kanshi?diff=0&oldid=833978>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Kanshi_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [Sway](<../zh-cn/Sway.html> "Sway")

[kanshi](<https://gitlab.freedesktop.org/emersion/kanshi>) 可以在热插拔时自动启用和禁用显示输出的配置文件。例如，当有扩展屏幕时，kanshi 可以自动关闭笔记本内置屏幕。 

这是 [autorandr](<https://github.com/phillipberndt/autorandr>) 等工具在 Wayland 上的等效替代品。kanshi 可在支持 wlr-output-management 协议的 Wayland 混成器上使用 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")正式版本 [kanshi](<https://archlinux.org/packages/?name=kanshi>)包 或开发版本 [kanshi-git](<https://aur.archlinux.org/packages/kanshi-git/>)AUR。 

##  配置

###  基础配置

创建 kanshi 配置文件： 
    
    ~/.config/kanshi/config
    
    profile {
    	output LVDS-1 disable
    	output "Some Company ASDF 4242" mode 1600x900 position 0,0
    }
    
    profile {
    	output LVDS-1 enable scale 2
    }

每个配置（profile）都由括号分隔，其包含几个输出指令（语法类似 [sway-output(5)](<https://man.archlinux.org/man/sway-output.5>)）。当一个配置所列的所有输出（output）都已连接时，该配置就会启用。 

**提示：** 可以使用 `swaymsg -t get_outputs` 命令获取输出名称列表和其它信息。 

###  进阶配置

为了易于管理多种配置 _（如“仅笔记本内置屏幕”、“在家连接一个扩展屏”、“工作时连接两个扩展屏”等配置）_ ，您可定义配置里使用的输出的默认行为并为其分配别名。默认行为会应用到所有提到该输出的配置中。更多信息参见 [kanshi(5)](<https://man.archlinux.org/man/kanshi.5>)。 
    
    ~/.config/kanshi/config
    
    output "Dell Inc. DELL S2721DGF G52TR83" {
      mode 2560x1440@165.08
      position 1280,0
      scale 2
      alias $HOME_1
    }
    
    output "LG Display 0x058B Unknown" {
      mode 2560x1440@59.99800
      position 0,0
      scale 2
      alias $INTERNAL
    }
    
    profile home_1 {
      output $INTERNAL disable
      output $HOME_1 enable
    }

注意 _$INTERNAL_ 输出的名称的第三段是 _UNKNOWN_ 。这是因为 kanshi 需要三个字段（制造商，型号，序列号）都被填充，如果缺少一个则需要使用 _UNKNOWN_ 代替。 

您可使用 [hyprctl monitors](<https://wiki.hyprland.org/Configuring/Using-hyprctl/>) 等命令查询这些字段，其会输出这三个字段： 
    
    hyprctl monitors
    
    make: LG Display
    model: 0x058B
    serial:

您还可以让您的工作流与 kanshi 进一步集成，使用 _exec_ 以在配置启用时执行命令： 
    
    ~/.config/kanshi/config
    
    profile home_1 {
      output $INTERNAL disable
      output $HOME_1 enable
      exec uwsm app -- $HOME/.config/hypr/scripts/move-workspaces.sh "LG Display 0x058B"
    }

##  使用

执行命令： 
    
    $ kanshi
    
自动用法参见[#使用 systemd 管理 kanshi](<#%E4%BD%BF%E7%94%A8_systemd_%E7%AE%A1%E7%90%86_kanshi>)。 

##  提示和技巧

###  使用 systemd 管理 kanshi

按照 [Sway#使用 systemd 管理仅用于 Sway 的守护程序](<../zh-cn/Sway.html#%E4%BD%BF%E7%94%A8_systemd_%E7%AE%A1%E7%90%86%E4%BB%85%E7%94%A8%E4%BA%8E_Sway_%E7%9A%84%E5%AE%88%E6%8A%A4%E7%A8%8B%E5%BA%8F> "Sway")创建并启动 `~/.config/systemd/user/sway-session.target`（如果尚未创建）。 

创建 `kanshi.service` 文件： 
    
    ~/.config/systemd/user/kanshi.service
    
    [Unit]
    Description=Dynamic output configuration for Wayland compositors
    Documentation=<https://gitlab.freedesktop.org/emersion/kanshi>
    BindsTo=sway-session.target
    
    [Service]
    Type=simple
    ExecStart=/usr/bin/kanshi
    
    [Install]
    WantedBy=sway-session.target

[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用")该[用户单元](<../zh-cn/Systemd/%E7%94%A8%E6%88%B7.html> "用户单元")。其仅会在 Sway 运行时激活并在 Sway 停止时停用。 

##  疑难解答

###  唤醒后外置屏幕工作区编号从 2 开始

若您参照[上文](<#%E9%85%8D%E7%BD%AE>)配置，当第二块屏幕连接到计算机时，第一块屏幕被禁用，第二块屏幕从 1 开始编号工作区，您首次接入屏幕或开机后应当是这种状况。但从睡眠唤醒后，这个数字可能会变成 2。欲解决，只需将第一个工作区移动到第二块屏幕，向 kanshi 配置文件中添加配置命令： 
    
    ~/.config/kanshi/config
    
    profile {
    	output LVDS-1 disable
    	output "Some Company ASDF 4242" mode 1600x900 position 0,0
    	# 以下这条就是添加的命令（别忘了更新输出名称）：
    	exec swaymsg workspace 1, move workspace to HDMI-A-1
    }
    
    profile {
    	output LVDS-1 enable scale 2
    }

##  另请参阅

  * [源码和文档](<https://gitlab.freedesktop.org/emersion/kanshi>)
