**翻译状态：**

  * 本文（或部分内容）译自 [Spacemacs](<https://wiki.archlinux.org/title/Spacemacs> "arch:Spacemacs")，最近一次同步于 2025-10-14，若英文版本有所[更改](<https://wiki.archlinux.org/title/Spacemacs?diff=0&oldid=845810>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Spacemacs_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[![](../File:Tango-preferences-desktop-locale.png)](<../File:Tango-preferences-desktop-locale.png>)**本文或本节需要[翻译](<../Project:Contributing_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\).html#%E7%BF%BB%E8%AF%91> "Project:Contributing \(简体中文\)")。要贡献翻译，请访问[简体中文翻译团队](<../Project:%E7%BF%BB%E8%AF%91%E5%9B%A2%E9%98%9F.html> "Project:翻译团队")。**

**附注：** 全文需要翻译（在 [Talk:Spacemacs#](<../zh-cn/Talk:Spacemacs.html>) 中讨论）

[Spacemacs](<https://en.wikipedia.org/wiki/Spacemacs> "wikipedia:Spacemacs") 是一款基于 [Emacs](<../zh-cn/Emacs.html> "Emacs") 构建、采用 [Vim](<../zh-cn/Vim.html> "Vim") 按键绑定方案的可扩展文本编辑器。该项目旨在融合 Vim 与 Emacs 编辑器的优势，取其精华。Spacemacs 的发行版基于社区驱动的 [Emacs](<../zh-cn/Emacs.html> "Emacs") 配置，不仅大幅扩展了 Emacs 的默认行为，更增添了诸多额外功能。 

##  安装

###  安装 Emacs

Spacemacs 是基于 Emacs 构建的，因此我们需要先安装 Emacs。 

  * [安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [Emacs](<../zh-cn/Emacs.html> "Emacs") 包

###  备份旧的 Emacs 配置 (可选)

若您曾使用过Emacs，请务必备份之前的配置文件。 
    
    $ mv ~/.emacs.d ~/.emacs.d.bak && mv ~/.emacs ~/.emacs.bak
    
###  安装 Spacemacs

要安装 Spacemacs，我们需要从 GitHub 克隆一个实际配置，并完全替换 Emacs 的配置。 
    
    $ git clone <https://github.com/syl20bnr/spacemacs> ~/.emacs.d
    
**注意：** 此命令应从您的用户账户运行。

###  安装 Adobe Source Pro fonts (可选)

Spacemacs 默认使用的字体是 Source Code Pro by Adobe. 若需使用该字体，建议在系统中安装。 

  * [安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [adobe-source-code-pro-fonts](<https://archlinux.org/packages/?name=adobe-source-code-pro-fonts>)包

如果未找到指定字体，则回落到一个可用字体。 

### Remove Emacs configuration file

Backup (if required) and remove the ~/.emacs file if you have not already. Otherwise Spacemacs will not load since that file prevents Emacs from loading the proper initialization file. You can do this by either renaming it through: 
    
    $ mv ~/.emacs ~/.emacs.bak
    
Or you can just remove it without backing it up: 
    
    $ rm ~/.emacs
    
### Run Spacemacs for the first time

Now it is time to launch Spacemacs. 
    
    $ emacs
    
For the first time you will be asked for features that should be installed. All the choices are alternatives, so something should be selected in any case. This choices affects some Spacemacs behavior and hotkeys. It is recommended to choose default values, just hitting **Enter**. Defaults are pretty optimized and you can always change them later. 

**提示：** Most default packages offers more features than the alternatives. However, you can find the other variants more useful in some cases (i.e performance and some special features).

When you finish with the questions, Spacemacs will download and install all the required packages. It may take a few minutes. Spacemacs may seems frozen at this time, but it is okay. 

## Running Spacemacs

To start spacemacs simply run: 
    
    $ emacs
    
Spacemacs will be ready to work when there are no '...' operations in the bottom bar would be displayed. 

**注意：** If startup time exceeds 10 seconds, refer to the troubleshooting part below.

### Daemon mode

Spacemacs can also be launched in a daemon mode. Daemon mode allows to initialize editor once, and connect to it later, without re-reading configuration file. It can be useful, when you have massive configuration file, so the initialization sequence would be completed only once. You would be able to connect immediately any time later then. 

To run Spacemacs in daemon mode: 
    
    $ emacs --daemon=instance1
    
Then you can connect to `instance1` later, using **emacsclient** : 
    
    $ emacsclient -nc -s instance1
    
**提示：** You can run multiple daemons with different names

### systemd module

[![](../File:Tango-edit-clear.png)](<../File:Tango-edit-clear.png>)**本文或本章节的语言、语法或风格需要改进。参考：[帮助:风格](<../zh-cn/Help:%E9%A3%8E%E6%A0%BC.html> "Help:风格")**

**原因：** Written like a blog, violates [Help:Style#Language register](<../zh-cn/Help:%E9%A3%8E%E6%A0%BC.html#Language_register> "Help:Style").（在[Talk:Spacemacs](<../zh-cn/Talk:Spacemacs.html>)讨论）

You may want to create a systemd module to run the emacs daemon. Note, due to security concerns stemming from community ELPA packages among other reasons, running the daemon as a user-privileged systemd user module is recommend as described here. 

Create an emacs user systemd service file such as: 
    
    .config/systemd/user/emacs.service
    
    [Unit]
    Description=Emacs text editor
    Documentation=info:emacs man:emacs(1) <https://gnu.org/software/emacs/>
    
    [Service]
    Type=forking
    ExecStart=/usr/bin/emacs --daemon=instance1
    ExecStop=/usr/bin/emacsclient --eval "(kill-emacs)"
    Restart=on-failure
    
    [Install]
    WantedBy=default.target

Edit your Emacs/Spacemacs desktop file as the following. Please note the changes to Exec. The rest is just nice aesthetics. 
    
    /usr/share/applications/emacs.desktop
    
    [Desktop Entry]
    Name=Spacemacs
    GenericName=Text Editor
    Comment=Edit text
    MimeType=text/english;text/plain;text/x-makefile;text/x-c++hdr;text/x-c++src;text/x-chdr;text/x-csrc;text/x-java;text/x-moc;text/x-pascal;text/x-tcl;text/x-tex;application/x-shellscript;text/x-c;text/x-c++;
    Exec=emacsclient -nc -s instance1 %F
    Icon=/home/[!!! YOUR USER NAME HERE !!!]/.emacs.d/assets/spacemacs.svg
    Type=Application
    Terminal=false
    Categories=Development;TextEditor;
    StartupWMClass=Emacs
    Keywords=Text;Editor;

Then do a [daemon-reload](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Daemon-reload") and [start](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Start") the `emacs.service` [user unit](<../zh-cn/User_unit.html> "User unit"). 

Check to make sure no errors occured. If you have already been mucking around with emacs running as a daemon and get errors, I recommend [enabling](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Enabling") the user emacs service we just made and reboot. It happened to resolve my issues. It might also be useful to check your user `emacs.service` [unit status](</wzh/index.php?title=Unit_status&action=edit&redlink=1> "Unit status（页面不存在）"). Then, if successful, [enable](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Enable") the [user unit](<../zh-cn/User_unit.html> "User unit") for persistence. 

Upon completion, you may start emacs via your DE launcher and enjoy significantly reduced loading times, however emacs still does not instantly open on even very powerful systems. You may also alias the following command if you prefer. "instance1" may also be renamed as well but be sure to match the daemon's name in the service file as well. 
    
    $ emacsclient -nc -s instance1
    
## Usage

Using Spacemacs may be tricky for the first time, especially for complete beginners. However, your efforts will be rewarded. Only a few key concepts are required to perform basic tasks. 

You can always exit Spacemacs by typing **:q[Enter]**

### Built-in Tutorial

You can always run Spacemacs built-in tutorial by pressing `SPC h T` when in Spacemacs. 

### Basic Concepts

#### Prerequisites

In order to explain the basic concepts we need some text to play with. Let us generate it first. Please, do not mind if the commands are unclear right now, you do not need to know them at the moment. 

  1. Run Spacemacs
  2. Press `SPC b N` to create new empty buffer
  3. Press `9 SPC i l l` to insert some text

You should see nine lines of generated text as the result. Use them to experiment with the commands described in the next sections. 

**注意：** When the **SPC** key sequence is used, you need to press the keys one after another. So you press **SPACE** key, followed by **b** , followed by **N**. Uppercase letters should be entered with shift key, for example **N** is **Shift+n**. So the final sequence would be **SPACE** , **b** , **Shift+n**

**提示：** When you press SPC key, the help menu appears at the bottom. You can inspect available commands there.

Now we can move closer to a concept named **states**. 

#### Editor states

The major difference between Spacemacs and regular text editor is **states**. Each state changes the way how the editor works. For example, there is an **insert state** , where you are able to enter text (like in a regular text editor), and there is a **normal state** , where all your key presses are used as commands, without changing the actual text. Only one state can be active at a time. Switching between the states is the key skill to use Spacemacs successfully. 

The current editor state is displayed in the left bottom corner. It has the form of a colored rectangle with text "1" (by default). The color describes the current state. There are a lot of states, but only a few of them are used regularly: 

  * Orange. This is **normal state**. Used for entering commands and text navigation.
  * Green. This is **insert state**. Used for text input.
  * Grey. This is **visual state**. Used for selecting chunks of text and controlling them.

You can also check the cursor color for the current state. 

**注意：** In order to use Spacemacs you will need to know at least **normal** and **insert** state.

##### Normal state

Normal state is used for text navigation and running commands. You cannot directly enter text in this mode. Instead, you are able to quickly navigate and make any sort of corrections there. Normal state is the default state and its color is **orange**. 

You can always return to normal state by pressing `ESC` key or `fd` key sequence if you accidentally leave it. 

**注意：** Commands listed below are not complete, there are lots more. You can check the additional documentation to find commands that are useful to you.

**注意：** Nobody can learn this commands in one go. Just take a few of them and master them. Only a small subset of commands is required to get you started.

###### Navigation

For basic navigation, the following keys are used: 

  * `h` \- move cursor by one symbol left
  * `j` \- move cursor by one line down
  * `k` \- move cursor by one line up
  * `l` \- move cursor by one symbol right

It is also possible to navigate between words or even sentences with a single key: 

  * `w` \- move to next word (beginning)
  * `b` \- move to previous word (beginning)
  * `(` \- move to the beginning of current sentence
  * `)` \- move to the beginning of next sentence
  * `^` \- move to beginning of line
  * `$` \- move to the end of line

To scroll the pages, use the following commands: 

  * `Ctrl+f` \- move one page down
  * `Ctrl+b` \- move one page up
  * `gg` \- goto first line of the document
  * `G` \- goto last line of the document

You can also use numbers with commands, so they would repeat **n** times: 

  * `5j` \- move cursor five lines down
  * `7w` \- move cursor seven words forward
  * `3 Ctrl+f` \- move three pages down
  * `20gg` \- move cursor to line with number 20

**提示：** Numeric arguments are widely used in the Spacemacs world.

There are a lot of commands to be uncovered. Basically, you can navigate between everything in Spacemacs, thanks to **Vim-like** flow. Check the additional resources to get the details. 

###### Text manipulation

You can modify text with the following commands: 

  * `x` \- cut the symbol under cursor
  * `dw` \- cut the word under cursor
  * `dd` \- cut the line under cursor
  * `yw` \- copy (yank) the word under cursor
  * `yd` \- copy (yank) the line under cursor
  * `p` \- paste copied/cut text
  * `r _a_` \- replace the symbol under cursor to _a_

You can also use numeric arguments there. 

######  Undo/Redo

You can undo and redo changes with the following commands: 

  * `u` \- undo last change
  * `Ctrl+r` \- redo last change

##### Insert state

Insert state is used for the text input. It is very close to regular editor behavior. However, the ability to modify text is limited. You will need to switch back to the **normal state** in order to make corrections. The color of insert state is **green**. 

###### Entering

To enter the insert state, press `i` from the **normal state**. Your cursor will change to being a green thin line. Now you can type something. When you are done, just leave the insert state by pressing `ESC` key or `fd` key sequence. 

There are a lot of ways to enter insert mode. The difference, however, is only related to the initial cursor position. It is enough to know just the `i` hotkey for the first time. But there are also others and they will be very useful once you master them: 

  * `i` \- enter insert mode before the cursor
  * `a` \- enter insert mode after the cursor
  * `I` \- enter insert mode at the beginning of the line
  * `A` \- enter insert mode at the end of the line
  * `o` \- enter insert mode at next line
  * `O` \- enter insert mode at previous line

###### Leaving

To leave the insert state press `ESC` key or `fd` key sequence. You will return to **normal state** and cursor will change to orange. 

##### Visual state

This state used for visual text selection. It allows to select text chunks and cut/copy them. The state color is **grey**. 

To enter visual state press `v` hotkey from the **normal mode**. Then you can navigate around using normal mode hotkeys with only one difference: text selection. Cursor movements would select text, based on initial cursor position, and you can `y`ank (copy) or `d`elete it later. Remember, that you can use commands like `ve` or `v(` to quickly select words or sentences. Check the `Normal state: Navigation` section to get the idea. 

You can also press `V` to quickly select the whole line. 

###### Visual block state

Visual block state is more powerful version of visual state. It allows to select text in columns. It is similar to multi-cursor concept on regular editors and IDEs. This state can be entered by pressing `Ctrl+v` hotkey. Then you can navigate with `h j k l` keys to see the difference. 

There is lots of stuff that can be done in visual block state. Refer to the additional resources for this information. This feature is called **vim visual block mode** in Vim parlance. 

####  Buffers (Tabs)

Text in Spacemacs is located in areas called buffers. They are very similar to regular editor tabs. You can switch between buffers and create new ones. Buffers are also used by the editor itself to store some information you can inspect later. 

##### Navigation

To show the list of current buffers press `SPC b b`. You will see a new window at the bottom. This is the place where you can inspect, filter, and navigate buffers. Some buffers already exist there, like *Messages* and *scratch*. They are created by the editor and contain some useful information. 

The first thing you can do with the bottom window is to type anything into the `pattern` field. This will filter buffers. If there are no buffers left after the filtering, you can create a new one by simply pressing "Enter" after your input. The new buffer will be created and opened. 

You can also open any buffer by hand. Press `Ctrl+**j**` or `Ctrl+**k**` to navigate between the lines. Then press `Ctrl+**l**` or `Enter` to confirm your choice. The selected buffer will be opened. 

**提示：** Remember `h j k l` keys? They are widely used for navigation. In some cases we need to use modifier keys like `Ctrl`. That allows to input and navigate at the same time. 

You can also use some hotkeys from **normal state** to control buffers: 

  * `SPC b b` \- list buffers
  * `SPC TAB` \- switch to last viewed buffer
  * `SPC b n` \- switch to next buffer (one forward)
  * `SPC b p` \- switch to previous buffer (one backward)
  * `SPC f s` \- save the current buffer to file
  * `SPC b d` \- close current buffer

**提示：** If you want to save a new buffer, you should choose a file for it. Refer to the next section for details.

#### Files

Spacemacs provides two options for file navigation: inline navigation and built-in file manager. Inline navigation is used in Spacemacs confirmation dialogs and it is very similar to the shell one. Build-in file manager is more user-friendly and allows to check the file details. Learning the basics of each is the essential key of mastering Spacemacs. 

There also advanced options available, like more powerful file manager and file tree. They are covered in `Advanced` section. 

#####  Inline (Helm)

Inline navigation available with `SPC f f` hotkey. It uses the window very similar to buffer-navigation one. You can filter and select files there. Just type anything to narrow results, or press `Ctrl+j` or `Ctrl+k` for moving the line down and up. Press `Ctrl+l` to open file or directory, and press `Ctrl+h` for going backward. Press `TAB` to autocomplete the input. 

#####  File manager (Dired)

If you need more visual method, run built-in file manager by pressing `SPC a d` `Enter`. You can navigate, using `Ctrl`+`h j k l` keys, and press `Enter` to enter directories and open files. 

There are some hotkeys available (refer to dired documentation for more): 

  * `q` \- quit dired
  * `R` \- rename file
  * `C` \- copy file
  * `+` \- create new directory

**提示：** If you need more powerful file manager, check Ranger in `Advanced` section. It provides more features and can be the best replacement for Dired when you master it.

##### Exiting

Exiting the editor can be achieved with `SPC q` this will show the multiple exiting methods. 

Some available are: 

  * `SPC qf` Quit current frame - good for emacsclient frames
  * `SPC qq` Quit emacs Kill-emacs
  * `SPC qr` Quit emacs and restart resuming layouts
  * `SPC qR` Quit emacs and restart
  * `SPC qd` Quit emacs and restart with --debug-init

### Advanced concepts

At this step you are able to open files, make changes and save them successfully. Half the way is done, and now you can choose what to master next. There are some sections you may be interested. 

#### Layers

Layers are one of the strongest features in Spacemacs. Layer is a set of packages and configuration options that greatly extends editor functionality in some way. There are layers for different programming languages, for example, or layers, providing additional tools (like IRC messaging, or integrated web browser). The full list of layers can be found at [Layers](<https://www.spacemacs.org/layers/LAYERS.html>) documentation page. 

Some layers are already shipped with Spacemacs, the others can be added manually. To do this, open Spacemacs configuration file (`SPC f e d`), and find `dotspacemacs-configuration-layers` section there. Then simply add selected layer to the list and restart Spacemacs. It will download all the required files on the next start. 

Spacemacs will also offer you to install a new layer when you open a file with an already known extension. For example, if you open a `.html` file, the installation of the `html` layer is offered. 

You can customize layer behaviour by overriding some layer-specific variables in your Spacemacs configuration file. Check the appropriate layer documentation to get the details. 

#### File Navigation

There are some additional tools for file navigation. They may greatly increase the way you use Spacemacs on a daily basis. 

#####  File tree (Neotree)

You can run file tree by pressing `SPC f t`. New window opens, accessible with `SPC 0`. Standard `h j k l` navigation is available there. You can change root folder with `R` and toggle hidden files with `s`. Create new files with `c` and rename the old ones with `r`. Check [Neotree](<https://github.com/syl20bnr/spacemacs/blob/master/doc/DOCUMENTATION.org#neotree-file-tree>) documentation for the details. 

**提示：** If you need to change the root to higher one, just press `R` while on the current root path (first line of the window). Inline file navigation opens, just go backward with `H` as far as you need and select `.` directory then

#####  File manager (Ranger)

If you need a full-featured file manager then Ranger may be the best choice. A lot of useful features are available there, like an instant `h j k l` navigation, inline file preview and ability to manipulate files. It also improves default Dired behaviour (`SPC a d`) a bit. Install `ranger` layer and run it with `SPC a r`. Check [Ranger](<https://github.com/syl20bnr/spacemacs/tree/master/layers/%2Btools/ranger>) documentation for the details. Along with customization options, there are a lot of useful hotkeys. 

**注意：** If you have issues opening Ranger, try to close Neotree first

#### Windows

Spacemacs allows you to split the screen into the separate windows. Each window has a personal number and can be accessed with `SPC _n_` hotkey, where the `_n_` is a selected number. Windows can be splitted individually, so it gives an ability to create complex layouts. 

Some of windows hotkeys are presented below. Check the inline help (`SPC w`) to get more. 

  * `SPC w 3` \- focus window with number 3
  * `SPC w s` \- split window horizontally
  * `SPC w v` \- split window vertically
  * `SPC w d` \- delete window
  * `SPC w u` \- undo last window action
  * `SPC w m` \- toggle window fullscreen
  * `SPC w .` \- enter window transient state

**提示：** Transient state allows you to play with window settings, like their order and proportions. Just enter it and all the available options will be displayed.

[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：** Expand with additional daily-used emacs/spacemacs features. (在 [Talk:Spacemacs](<../zh-cn/Talk:Spacemacs.html>) 中讨论)

## Configuration

[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：** Expand with short description of Spacemacs configuration file. (在 [Talk:Spacemacs](<../zh-cn/Talk:Spacemacs.html>) 中讨论)

## Troubleshooting

### Slow startup time

If startup time exceeds 10 seconds, there may be a problem with `exec-path-from-shell` module. It can be safely disabled on linux systems. Complete the following steps: 

  1. Open Spacemacs configuration file by pressing `SPC f e d`
  2. Find `dotspacemacs-excluded-packages` section
  3. Add `exec-path-from-shell` module here, so the final entry would be like `dotspacemacs-excluded-packages '(exec-path-from-shell)`
  4. Save changes with `SPC f s` and restart Spacemacs

### Incorrect minor mode icon fonts

If you see 24ba 24c0 symbols instead of ⒺⓀ or they are too ugly, then you have to install a good unicode fallback font for these symbols, or disable them by setting `dotspacemacs-mode-line-unicode-symbols` to `nil`. 

**提示：** A nice fallback unicode font for Spacemacs is [ttf-symbola](<https://aur.archlinux.org/packages/ttf-symbola/>)AUR
