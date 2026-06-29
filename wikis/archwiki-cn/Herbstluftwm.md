**翻译状态：**

  * 本文（或部分内容）译自 [Herbstluftwm](<https://wiki.archlinux.org/title/Herbstluftwm> "arch:Herbstluftwm")，最近一次同步于 2024-07-16，若英文版本有所[更改](<https://wiki.archlinux.org/title/Herbstluftwm?diff=0&oldid=775335>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Herbstluftwm_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[Herbstluftwm](<https://herbstluftwm.org/>)是一个使用 Xlib 的手动 X11 窗口管理器。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [herbstluftwm](<https://archlinux.org/packages/?name=herbstluftwm>)包 包或 [herbstluftwm-git](<https://aur.archlinux.org/packages/herbstluftwm-git/>)AUR （开发版本）。 

##  启动

###  从 TTY 启动

用 [xinit](<../zh-cn/Xinit.html> "Xinit") 启动 `herbstluftwm`。 

###  作为桌面环境启动

[herbstluftwm](<https://archlinux.org/packages/?name=herbstluftwm>)包 包含可以启动窗口管理器的 `herbstluftwm.desktop` 作为 [Xsession](</wzh/index.php?title=Xsession&action=edit&redlink=1> "Xsession（页面不存在）")。 

###  从其他窗口管理器启动

如果已经启动了一个窗口管理器会话，可以用 `herbstluftwm --replace` 替换掉原窗口管理器。 

##  第一步

阅读 [herbstluftwm(1)](<https://man.archlinux.org/man/herbstluftwm.1>) 和 [herbstclient(1)](<https://man.archlinux.org/man/herbstclient.1>) 手册页，它们包含很多对配置选项和有效值的解释。 

##  配置

复制 `/etc/xdg/herbstluftwm/autostart` 到`~/.config/herbstluftwm/autostart`。可以按需修改文件。 保证 autostart 文件可执行，否则键绑定极有可能失效！ 

Herbstluftwm 的配置可以用 `herbstclient reload` 即时更新 （见 [#Commands](<#Commands>)）。每次 reload 配置时 Autostart 脚本都会被调用，所以它一般会先恢复所有配置到默认值。 

###  多显示器支持

Herbstluftwm 支持多个显示器 as a virtual concept；Herbstluftwm 中，显示器信息不必与 xrandr 报告的真实监视器配置相匹配。它带来了很大的灵活性，让用户可以更好地控制显示器的布置。可以使用 `herbstclient detect_monitors` 自动适应物理设置，或者通过手册了解如何添加、移除、调整和移动显示器。多监视器设置中的标记不为某个监视器 "拥有"。这意味着当一个监视器切换到另一个监视器中激活的标记时，两个监视器将交换标记。 

##  命令

Herbstclient 很强大，因为它能让你通过命令行完全控制窗口管理器。 

Herbstclient 的参数支持 Tab 补全。用 `herbstclient list_commands` 查看所有参数。 

现在如果传给 Herbstclient 的参数有误，Herbstclient 不会打印错误信息，指挥以非零值退出。如果不通过其他方式显示返回值（比如用`$SHELL-prompt`），可能需要用 `echo $?` 打印返回值。 

##  脚本和钩子

The main way to control herbstluftwm is though commands to herbstclient. Since herbstclient can be called from any script, you have great flexibility in controlling herbstluftwm this way. Furthermore, you can listen to window management events and react to them accordingly. 

Herbstluftwm includes a number of example scripts: `/usr/share/doc/herbstluftwm/examples/` or <https://github.com/herbstluftwm/herbstluftwm/tree/master/scripts>

### Script to switch to the next empty tag

The following python script allows you to switch to the (next or previous) (full or empty) tag. Call it with the arguments (+1 or -1) and (full or empty). For example, if you save the script to herbst-move.py, then 
    
    python3 herbst-move.py +1 full
    
will move you to the next full tag. I use the following key bindings. 
    
    hc keybind $Mod-Left  spawn herbst-move.py -1 empty
    hc keybind $Mod-Right spawn herbst-move.py +1 empty
    hc keybind $Mod-Up spawn herbst-move.py -1 full
    hc keybind $Mod-Down spawn herbst-move.py +1 full
    
And here is the script. 
    
    #!/usr/bin/env python3
    def run(*cmd):
        from subprocess import Popen, PIPE
        proc = Popen(cmd, shell=False, stderr=PIPE, stdout=PIPE)
        return proc.stdout.read()
    
    import sys
    tag_offset, mode = sys.argv[1:]
    tag_offset = int(tag_offset)
    if mode == 'full':
        ch = {'.'}
    elif mode == 'empty':
        ch = {':', '!'}
    else:
        raise Exception('Unknown type ' + mode)
    tag_list = run('herbstclient', 'tag_status', '0').strip().decode('ascii').split('\t')
    tag_curr = int(run('herbstclient', 'attr', 'tags.focus.index').strip())
    tag_next = (tag_curr + tag_offset) % len(tag_list)
    while (tag_next != tag_curr) and (tag_list[tag_next][0] in ch):
        tag_next = (tag_next + tag_offset) % len(tag_list)
    if tag_next != tag_curr:
        run('herbstclient', 'use_index', str(tag_next))
    
###  Script to cycle though paddings (or other settings)

Here is a ruby script to cycle through a set of paddings, although you can modify it to cycle though any collection of settings. The script knows the previous layout by looking for the presence of two dummy files in /tmp. 
    
    #!/usr/bin/ruby
    
    file1 = "/tmp/herbst-padding-1"
    file2 = "/tmp/herbst-padding-2"
    
    pad1 = 'pad 0 0 0 0 0'
    pad2 = 'pad 0 0 20 0 200'
    pad3 = 'pad 0 0 0 0 150'
    
    files = [file1, file2].map{|f| File.exist? File.expand_path(f)}
    
    if files == [false, false]  # 0 files
      system "herbstclient #{pad2}"
      system "touch #{file1}"
    elsif files == [true, false]  # 1 file
      system "herbstclient #{pad1}"
      system "touch #{file2}"
    else           # 2 files
      system "herbstclient #{pad3}"
      system "rm #{file1} #{file2}"
    end
    
### Script to change decoration per-tag

The following Perl script demonstrates how to use hooks to react to window management events. It can be called in autostart (with backgrounding). 
    
    #!/usr/bin/perl
    # This script watches for tag changes and gives visual feedback
    
    ## Configuration (fill with your tag names)
    my %colors = (
    	main => '#DD0000',
    	devel => '#13B8E0',
    	write => '#96E013',
    	admin => '#C713E0'
    );
    
    ## Apply tag color
    # Right now we change the active window's border color to the tag's color.
    sub redecorate
    {
    	my ($foo, $activity) = @_;
    	system("herbstclient", "set", "window_border_active_color",
    		"$colors{$activity}");
    }
    
    ## main routine
    use v5.20;
    
    # set up a pipe for reading hooks
    open HOOKS, "herbstclient -i '(tag_changed|reload)'|"
    	or die "can't fork: $!";
    # process incoming messages
    OUTER:
    while (<HOOKS>) {
    	chomp;
    	for ($_) {
    		redecorate(split(/\t/)) when /^tag_changed/;
    		last OUTER when /^reload/; # quit on reload
    	}
    }
    close HOOKS or die "unfinished love story: $! $?"; # happens on hlwm crash
    
## Troubleshooting

  * After installing, `$mod+enter` keybind does not start a terminal: the herbstluftwm autostart configuration file uses the xterm terminal by default. Make sure [xterm](<https://archlinux.org/packages/?name=xterm>)包 is [install](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "Install")ed or edit the autostart file to use a different terminal.
  * To log out of herbstluftwm, use the command `herbstclient quit` or the default keybind of `$mod+shift-q`

## See also

  * [The herbstluftwm homepage](<https://herbstluftwm.org>)
  * [Arch Linux BBS thread](<https://bbs.archlinux.org/viewtopic.php?id=128646>)
  * `/usr/share/doc/herbstluftwm/examples/` \- various scripts
  * `/usr/share/doc/herbstluftwm/BUGS` \- bugs
  * [A herbstluftwm thread on the CrunchBang Forums](<https://crunchbang.org/forums/viewtopic.php?pid=204358%23p204358#p204358k>)
  * **Screenshots and configuration files:** [on Arch Linux Forum](<https://bbs.archlinux.org/viewtopic.php?id=133557>), [on DotShare.it](<http://dotshare.it/category/wms/herbstluft/>)
  * `#herbstluftwm` \- IRC channel at irc.libera.chat
  * [User git repository #1](<https://github.com/ypnos/hlwm>) with autostart written in Perl and a few custom scripts
  * [User git repository #2](<https://github.com/ylixir/hlwm-config>) with autostart and panel written in Python
  * [Github Discussions](<https://github.com/herbstluftwm/herbstluftwm/discussions>)
  * [Herbstluftwm Subreddit](<https://www.reddit.com/r/herbstluftwm/>)
