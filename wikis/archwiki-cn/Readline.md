[![](../File:Tango-preferences-desktop-locale.png)](<../File:Tango-preferences-desktop-locale.png>)**本文或本节需要[翻译](<../Project:Contributing_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\).html#%E7%BF%BB%E8%AF%91> "Project:Contributing \(简体中文\)")。要贡献翻译，请访问[简体中文翻译团队](<../Project:%E7%BF%BB%E8%AF%91%E5%9B%A2%E9%98%9F.html> "Project:翻译团队")。**

**附注：** 翻译未完成（在 [Talk:Readline#](<../zh-cn/Talk:Readline.html>) 中讨论）

[Readline](<https://www.gnu.org/software/readline/>) 是来自 [GNU Project](<../zh-cn/GNU_Project.html> "GNU Project") 的库，[Bash](<../zh-cn/Bash.html> "Bash") 和其他命令行界面的程序使用它在命令行编辑和交互。详情请参阅 [readline(3)](<https://man.archlinux.org/man/readline.3>)。 

##  安装

[readline](<https://archlinux.org/packages/?name=readline>)包 包很可能已作为 [Bash](<../zh-cn/Bash.html> "Bash") 的依赖安装。 

##  编辑模式

Readline 默认使用 [Emacs](<../zh-cn/Emacs.html> "Emacs") 风格的快捷键与命令行交互。不过，[vi](<../zh-cn/Vi.html> "Vi") 风格的编辑界面也受支持，但需要将以下内容添加到 `~/.inputrc`： 
    
    ~/.inputrc
    
    set editing-mode vi

或者，要只为 [Bash](<../zh-cn/Bash.html> "Bash") 设置，你可将以下内容添加到 `~/.bashrc`： 
    
    ~/.bashrc
    
    set -o vi

###  提示中的模式指示符

Vi 风格的编辑有两种模式：命令模式和插入模式。你可通过添加以下命令显示当前的模式： 
    
    ~/.inputrc
    
    set show-mode-in-prompt on
    
这将在你的提示中显示模式（默认是 `(cmd)`/`(ins)`），显示的内容可通过 `vi-ins-mode-string` 和 `vi-cmd-mode-string` 变量自定义。 

###  为每个模式指定不同的光标样式

你可以使用["\1 .. \2" 转义符](<https://www.gnu.org/software/bash/manual/html_node/Readline-Init-File-Syntax.html#index-vi_002dcmd_002dmode_002dstring>)为每个模式指定不同的光标样式： 
    
    ~/.inputrc
    
    set vi-ins-mode-string \1\e[6 q\2
    set vi-cmd-mode-string \1\e[2 q\2
    
这将在命令模式中显示方块形状的光标，在插入模式中显示竖线形状的光标。注意，你必须先启用模式指示符（见[#提示中的模式指示符](<#%E6%8F%90%E7%A4%BA%E4%B8%AD%E7%9A%84%E6%A8%A1%E5%BC%8F%E6%8C%87%E7%A4%BA%E7%AC%A6>)）。 

Virtual Console 使用不同的转义代码，因此你应先检查使用的是哪种终端： 
    
    ~/.inputrc
    
    $if term=linux
    	set vi-ins-mode-string \1\e[?0c\2
    	set vi-cmd-mode-string \1\e[?8c\2
    $else
    	set vi-ins-mode-string \1\e[6 q\2
    	set vi-cmd-mode-string \1\e[2 q\2
    $endif

详情请参阅 [software cursor for VGA](<https://docs.kernel.org/admin-guide/vga-softcursor.html>)。 

## Fast word movement

[Xterm](</wzh/index.php?title=Xterm&action=edit&redlink=1> "Xterm（页面不存在）") [默认](<https://stackoverflow.com/a/7783928>)支持使用 `Ctrl+Left` 和 `Ctrl+Right` 在单词间移动。要在其他终端模拟器中实现这一效果，先找到正确的[终端代码](<https://wiki.bash-hackers.org/scripting/terminalcodes>)，然后在 `~/.inputrc` 中绑定到 `backward-word` 和 `forward-word`。 

例如，对于 [urxvt](<../zh-cn/Rxvt-unicode.html> "Urxvt")： 
    
    ~/.inputrc
    
    "\e[1;5D": backward-word
    "\e[1;5C": forward-word

##  历史

通常，无论你输入了什么，按向上箭头都会出现上一次输入的命令。然而，用户可能会觉得只显示匹配刚刚输入的内容的命令更实用。 

例如，假设输入了以下命令： 

  * `ls /usr/src/linux-2.6.15-ARCH/kernel/power/Kconfig`
  * `who`
  * `mount`
  * `man mount`

此时，当输入 `ls` 并按向上箭头，输入将会被替换为 `man mount`。如果你使用了历史搜索功能，那么只有过去以 `ls`（当前的输入）开头的命令会被显示，在这里就是 `ls /usr/src/linux-2.6.15-ARCH/kernel/power/Kconfig`。 

要启用历史搜索功能，只需把以下内容加入到 `/etc/inputrc` 或者 `~/.inputrc`： 
    
    "\e[A": history-search-backward
    "\e[B": history-search-forward
    
如果你使用 vi 模式，添加以下内容到 `~/.inputrc`（来自[这个帖子](<https://bbs.archlinux.org/viewtopic.php?pid=428760#p428760>)）： 
    
    set editing-mode vi
    $if mode=vi
    set keymap vi-command
    # these are for vi-command mode
    "\e[A": history-search-backward
    "\e[B": history-search-forward
    j: history-search-forward
    k: history-search-backward
    set keymap vi-insert
    # these are for vi-insert mode
    "\e[A": history-search-backward
    "\e[B": history-search-forward
    $endif
    
如果你选择将这些内容添加到 `~/.inputrc`，那建议你同时在文件的开始添加以下内容，以避免像[这样](<https://bbs.archlinux.org/viewtopic.php?id=112537>)的怪事： 
    
    $include /etc/inputrc
    
Alternatively, one can use reverse-search-history (incremental search) by pressing `Ctrl+R`, which does not search based on previous input but instead jumps backwards in the history buffer as commands are typed in a search term. Pressing `Ctrl+R` again during this mode will display the previous line in the buffer that matches the current search term, while pressing `Ctrl+G` (abort) will cancel the search and restore the current input line. So in order to search through all previous `mount` commands, press `Ctrl+R`, type 'mount' and keep pressing `Ctrl+R` until the desired line is found. 

The forward equivalent to this mode is called forward-search-history and is bound to `Ctrl+S` by default. Beware that most terminals override `Ctrl+S` to suspend execution until `Ctrl+Q` is entered. (This is called XON/XOFF flow control). For activating forward-search-history, either disable flow control by issuing: 
    
    $ stty -ixon
    
或者在 `inputrc` 中使用不同的键。例如，要使用默认未绑定的 `Alt+S`： 
    
    "\es": forward-search-history
    
## Faster completion

When performing tab completion, a single tab attempts to partially complete the current word. If no partial completions are possible, a double tab shows all possible completions. 

The double tab can be changed to a single tab by setting: 
    
    ~/.inputrc
    
    set show-all-if-unmodified on
    
Or you can set it such that a single tab will perform both steps: partially complete the word _and_ show all possible completions if it is still ambiguous: 
    
    ~/.inputrc
    
    set show-all-if-ambiguous on
    
## Colorized completion

You can enable coloring of completion of filenames with the `colored-stats` option. You can also color the identical prefix of completion-lists with `colored-completion-prefix`. For example: 
    
    ~/.inputrc
    
    # Color files by types
    # Note that this may cause completion text blink in some terminals (e.g. xterm).
    set colored-stats On
    # Append char to indicate type
    set visible-stats On
    # Mark symlinked directories
    set mark-symlinked-directories On
    # Color the common prefix
    set colored-completion-prefix On
    # Color the common prefix in menu-complete
    set menu-complete-display-prefix On
    
##  宏

Readline also supports binding keys to keyboard macros. For simple example, run this command in Bash: 
    
    bind '"\ew": "\C-e # macro"'
    
or add the part within single quotes to inputrc: 
    
    "\ew": "\C-e # macro"
    
Now type a line and press `Alt`+`W`. Readline will act as though `Ctrl+E` (end-of-line) had been pressed, appended with '` # macro`'. 

Use any of the existing keybindings within a readline macro, which can be quite useful to automate frequently used idioms. For example, this one makes `Ctrl+Alt+L` append "| less" to the line and run it (`Ctrl+M` is equivalent to `Enter`): 
    
    "\e\C-l": "\C-e | less\C-m"
    
The next one prefixes the line with 'yes |' when pressing `Ctrl+Alt+Y`, confirming any yes/no question the command might ask: 
    
    "\e\C-y": "\C-ayes | \C-m"
    
This example wraps the line in `su -c ''`, if `Alt+S` is pressed: 
    
    "\es": "\C-a su -c '\C-e'\C-m"
    
This example prefixes the line with `sudo `, if `Alt+S` is pressed. It is safer because it will not input the `Enter` key. 
    
    "\es": "\C-asudo \C-e"
    
As a last example, quickly send a command in the background with `Ctrl+Alt+B`, discarding all of its output: 
    
    "\e\C-b": "\C-e > /dev/null 2>&1 &\C-m"
    
##  禁用 control 回显

Readline 使得终端在按下 `Ctrl+C` 后回显 `^C`。要禁用，只需将以下内容添加到 `~/.inputrc`： 
    
    set echo-control-characters off
    
##  参阅

  * [vi readline 编辑速查表](<https://www.catonmat.net/download/bash-vi-editing-mode-cheat-sheet.pdf>)
  * [emacs readline 编辑速查表](<https://www.catonmat.net/download/readline-emacs-editing-mode-cheat-sheet.pdf>)
