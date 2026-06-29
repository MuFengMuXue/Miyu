**翻译状态：**

  * 本文（或部分内容）译自 [Xmonad](<https://wiki.archlinux.org/title/Xmonad> "arch:Xmonad")，最近一次同步于 2020-08-17，若英文版本有所[更改](<https://wiki.archlinux.org/title/Xmonad?diff=0&oldid=631650>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Xmonad_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[xmonad](<https://xmonad.org/>) 是 X 下的一个平铺[窗口管理器](<../zh-cn/%E7%AA%97%E5%8F%A3%E7%AE%A1%E7%90%86%E5%99%A8.html> "窗口管理器")。窗口会自动排列、无间隙或重叠地平铺在屏幕上，从而最大限度地利用屏幕。窗口管理器功能可通过键盘访问：鼠标操作是可选的。 

Xmonad 使用 [Haskell 语言](<https://haskell.org/>)编写、配置并扩展功能的。用户可以将自定义布局算法、按键绑定和其他扩展功能写在配置文件中。 

布局是动态应用的，并且在每个工作空间上可以使用不同的布局。 Xmonad 完全支持 Xinerama，后者可允许将窗口平铺在多个物理屏幕上。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [xmonad](<https://archlinux.org/packages/?name=xmonad>)包 软件包，其提供了最基本的配置，最好还安装上 [xmonad-contrib](<https://archlinux.org/packages/?name=xmonad-contrib>)包，可获得更有用的桌面配置以及其他平铺算法、配置和脚本等。 

此外，可安装开发版本的 [xmonad-git](<https://aur.archlinux.org/packages/xmonad-git/>)AUR, 其还附带了些额外的依赖；以及同时安装 [xmonad-contrib-git](<https://aur.archlinux.org/packages/xmonad-contrib-git/>)AUR。 

**注意：** 记得在升级 xmonad 后运行 `xmonad --recompile` 命令，否则下次启动寻找共享库时可能会遇到问题。

##  如何启动

用 [xinit](<../zh-cn/Xinit.html> "Xinit") 运行 `xmonad`. 

或者，你也可以在 [display manager](<../zh-cn/Display_manager.html> "Display manager")（SDDM） 的会话菜单中选择 _XMonad_ 。 

请确保在启动 _XMonad_ 之前你已经安装了至少一个默认终端模拟器 [Xterm](</wzh/index.php?title=Xterm&action=edit&redlink=1> "Xterm（页面不存在）")，当然你也可以在这之前修改 _XMonad_ 的配置文件 `~/.xmonad/xmonad.hs` 来指定一个默认的终端，这很重要，否则你将无法在新的窗口管理器下进行任何工作。 

**注意：** 默认情况下， _XMonad_ 之显示一个十字光标， 可以根据这个文章内容来更改默认显示, see [Cursor themes#Change X shaped default cursor](<../zh-cn/Cursor_themes.html#Change_X_shaped_default_cursor> "Cursor themes").

##  配置文件

创建一个配置目录 `~/.xmonad` 和 配置文件 `.xmonad/xmonad.hs` ，然后根据下面的指导编写基础的配置项。 

在更改配置文件 `~/.xmonad/xmonad.hs` 后，使用 Mod+q 快捷键来重新启动 _XMonad_ ，使更改生效。 

**提示：** 默认的 _XMonad_ 的配置在没有 `xmonad.hs` 配置文件的情况下也是十分友好的

因为 xmonad 的配置文件使用的是 _Haskell_ 语言编写，一般人需要自定义定制一个自己的配置文件可能是困难且耗费时间的，以下网站资源是一些关于 xmonad 的详细配置示例参考: 

  * [xmonad wiki](<https://wiki.haskell.org/Xmonad>)
  * [xmonad configuration archive](<https://wiki.haskell.org/Xmonad/Config_archive>)
  * [xmonad FAQ](<https://wiki.haskell.org/Xmonad/Frequently_asked_questions>)
  * Arch Linux [forum thread](<https://bbs.archlinux.org/viewtopic.php?id=40636>)

把更改和自定义内容写入 `~/.xmonad/xmonad.hs` ，XMonad 将会从你的 _def_ 函数中读取相关参数的设定， 

一个编写的 `xmonad.hs` 示例如下: 
    
    import XMonad
    
    main = xmonad def
        { terminal    = "urxvt"  --默认终端
        , modMask     = mod4Mask --快捷前置键, 4是win键，1是alt也是默认的
        , borderWidth = 3        --边框宽度
        }
    
这里只更改了默认终端，快捷前置键和窗口边框的宽度，其他的设置还是 XMonad 的默认值 （默认值从 _Xconfig_ 继承）。 

当配置越来越复杂的时候，可以把参数以赋值的形式传递给 def 函数中的变量，用更容易识别的变量名可以优化配置文件的格式布局，方便自己和其他人查看与维护。 下面是一个简单的例子： 
    
    import XMonad
    
    myTerminal    = "urxvt"
    myModMask     = mod4Mask -- Win key or Super_L
    myBorderWidth = 3
    
    main = do
      xmonad $ def
        { terminal    = myTerminal
        , modMask     = myModMask
        , borderWidth = myBorderWidth
        }
    
Also, order at top level (main, myTerminal, myModMask etc.), or within the {} does not matter in Haskell, as long as imports come first. 

    {
      terminal           = myTerminal,
      focusFollowsMouse  = myFocusFollowsMouse,
      borderWidth        = myBorderWidth,
      modMask            = myModMask,
      -- numlockMask deprecated in 0.9.1
      -- numlockMask        = myNumlockMask,
      workspaces         = myWorkspaces,
      normalBorderColor  = myNormalBorderColor,
      focusedBorderColor = myFocusedBorderColor,
    
      -- key bindings
      keys               = myKeys,
      mouseBindings      = myMouseBindings,
    
      -- hooks, layouts
      layoutHook         = myLayout,
      manageHook         = myManageHook,
      handleEventHook    = myEventHook,
      logHook            = myLogHook,
      startupHook        = myStartupHook
    }
    
The package itself also includes a `xmonad.hs`, which is the latest official example `xmonad.hs` that comes with the **xmonad** Haskell module as an example of how to override everything. This should not be used as a template configuration, but as examples of parts you can pick to use in your own configuration. It is located in an architecture and version dependant directory in `/usr/share/` (e.g. `find /usr/share -name xmonad.hs`). 

### A base desktop configuration

In [xmonad-contrib](<https://archlinux.org/packages/?name=xmonad-contrib>)包 is a better default configuration for average desktop uses. It also helps with problems in some modern programs like Chromium. 

It can be added like so: 
    
    import XMonad
    import XMonad.Config.Desktop
    
    main = xmonad desktopConfig
        { terminal    = "urxvt"
        , modMask     = mod4Mask
        }
    
## Exiting xmonad

To end the current xmonad session, press `Mod+Shift+Q`. By default, `Mod` is the `Alt` key. 

## Tips and tricks

### X-Selection-Paste

The keyboard-centered operation in xmonad can be further supported with a keyboard shortcut for [X-Selection-Paste](<../zh-cn/Keyboard_shortcuts.html#Key_binding_for_X-selection-paste> "Keyboard shortcuts"). 

Also, there exists a function "pasteSelection" in XMonad.Util.Paste that can be bound to a key using a line like: 
    
    xmonad.hs
    
      import XMonad.Util.Paste -- Remember to include this line
      
      -- X-selection-paste buffer
      , ((0, xK_Insert), pasteSelection)

Pressing the "Insert" key will now paste the mouse buffer in the active window. 

### Keyboard shortcuts

Default keyboard shortcuts are listed in the man page of xmonad. 

[![](../File:Tango-inaccurate.png)](<../File:Tango-inaccurate.png>)**本文或本章节的事实准确性存在争议。**

**原因：** `Shift+Insert` pastes the PRIMARY buffer.（在 [Talk:Xmonad](<../zh-cn/Talk:Xmonad.html>) 中讨论）

[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：** Why the 100ms delay? (在 [Talk:Xmonad](<../zh-cn/Talk:Xmonad.html>) 中讨论)

Users who prefer to work with the keyboard rather than the mouse may benefit from a key binding to the paste operation of the middle mouse button. This is especially useful in a keyboard-centered environment. A workflow example is: 

  1. In Firefox, select a string you want to web-search for (with the mouse).
  2. Hit `Ctrl+k` to enter the "search engine" field.
  3. Hit `F9` to paste the buffer, instead of moving the mouse pointer to the field and middle-click to paste.

**注意：**`Shift+Insert` has a similar yet different functionality, see [#Xorg](<#Xorg>): `Shift+Insert` inserts the clipboard buffer, not the x-selection-paste buffer. In some applications, these two buffers are mirrored.

The method suggested here uses the following three packages:: 

  * [xsel](<https://archlinux.org/packages/?name=xsel>)包 to give access to the x-selection-buffer content.
  * [Xbindkeys](</wzh/index.php?title=Xbindkeys&action=edit&redlink=1> "Xbindkeys（页面不存在）") to bind a key-stroke to an action.
  * [xvkbd](<https://aur.archlinux.org/packages/xvkbd/>)AUR to pass the buffer string to the application by emulating keyboard input.

This example binds the x-selection-paste operation to the `F9` key: 
    
    .xbindkeysrc
    
    "xvkbd -no-jump-pointer -xsendevent -text "\D1`xsel`" 2>/dev/null"
        F9
    
The `"\D1"` code prefixes a 100 ms pause to inserting the selection buffer (see the [xvkbd home page](<http://t-sato.in.coocan.jp/xvkbd/>)). 

**注意：** Depending on your X configuration, you may need to drop the `-xsendevent` argument to xvkbd.

The key codes for keys other than `F9` can be determined using `xbindkeys -k`. 

References: 

  * [Pasting X selection (not clipboard) contents with keyboard](<https://unix.stackexchange.com/questions/11889/pasting-x-selection-not-clipboard-contents-with-keyboard>)
  * [xvkbd home page](<http://t-sato.in.coocan.jp/xvkbd/>)

### Targeting unbound keys

If you use xmonad as a stand alone window manager, you can edit the xmonad.hs to add unbound keyboard keys. You just need to find the Xf86 name of the key (such as XF86PowerDown) and look it up in `/usr/include/X11/XF86keysym.h`. It will give you a keycode (like 0x1008FF2A) which you can use to add a line like the following in the keybindings section of your `xmonad.hs`: 
    
    ((0,               0x1008FF2A), spawn "sudo pm-suspend")
    
### Increase the number of workspaces

By default, xmonad uses a set of 9 workspaces. You can change this by changing the **workspaces** parameter: 
    
    xmonad.hs
    
    import XMonad
    import XMonad.Util.EZConfig (additionalKeys)
    
    main=do
      xmonad $ def
        { ...
        , workspaces = myWorkspaces
        , ...
        } `additionalKeys` myAdditionalKeys
    
    myWorkspaces = ["1","2","3","4","5","6","7","8","9"] ++ (map snd myExtraWorkspaces) -- you can customize the names of the default workspaces by changing the list
    
    myExtraWorkspaces = [(xK_0, "0")] -- list of (key, name)
    
    myAdditionalKeys =
        [ -- ... your other hotkeys ...
        ] ++ [
            ((myModMask, key), (windows $ W.greedyView ws))
            | (key, ws) <- myExtraWorkspaces
        ] ++ [
            ((myModMask .|. shiftMask, key), (windows $ W.shift ws))
            | (key, ws) <- myExtraWorkspaces
        ]
    
###  Making room for docks/panels/trays (Xmobar, Tint2, Conky, etc)

Wrap your layouts with avoidStruts from XMonad.Hooks.ManageDocks for automatic dock/panel/trayer spacing: 
    
    import XMonad
    import XMonad.Hooks.ManageDocks
    
    main=do
      xmonad $ docks def
        { ...
        , layoutHook=avoidStruts $ layoutHook def
        , manageHook=manageHook def <+> manageDocks
        , ...
        }
    
If you ever want to toggle the gaps, this action can be added to your key bindings: 
    
    ,((modMask x, xK_b     ), sendMessage ToggleStruts)
    
### Equally sized gaps between windows

If your goal is to have equally sized gaps between individual windows and the screen, the following code will not work as expected: 
    
    layoutHook = spacing 10 $ Tall (1 (3/100) (1/2)) ||| Full
    
This makes each window have its own spacing in each direction. If you have two windows side-by-side, the spacing in the middle will be combined, creating a gap that is twice as large as needed. 

A workaround is to specify both a screen and a window spacing, but only use the top and left margins for the screen and bottom and right margins for the windows. To do this, change the above code into: 
    
     layoutHook = spacingRaw False (Border 10 0 10 0) True (Border 0 10 0 10) True $ Tall (1 (3/100) (1/2)) ||| Full
    
### Using xmobar with xmonad

[![](../File:Merge-arrows-2.png)](<../File:Merge-arrows-2.png>)**本文或本章节可能需要合并到[xmobar](</wzh/index.php?title=Xmobar&action=edit&redlink=1> "Xmobar（页面不存在）")。**

**附注：** Make use of the separate article available（在 [Talk:Xmonad](<../zh-cn/Talk:Xmonad.html>) 中讨论）

**[xmobar](</wzh/index.php?title=Xmobar&action=edit&redlink=1> "Xmobar（页面不存在）")** is a light and minimalistic text-based bar, designed to work with xmonad. To use xmobar with xmonad, you will need two packages in addition to the [xmonad](<https://archlinux.org/packages/?name=xmonad>)包 package. These packages are [xmonad-contrib](<https://archlinux.org/packages/?name=xmonad-contrib>)包 and [xmobar](<https://archlinux.org/packages/?name=xmobar>)包 from the [official repositories](<../zh-cn/Official_repositories.html> "Official repositories"), or you can use [xmobar-git](<https://aur.archlinux.org/packages/xmobar-git/>)AUR from the [AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR") instead of the official [xmobar](<https://archlinux.org/packages/?name=xmobar>)包 package. 

Here we will start xmobar from within xmonad, which reloads xmobar whenever you reload xmonad. 

Open `~/.xmonad/xmonad.hs` in your favorite editor, and choose one of the two following options: 

####  Quick, less flexible

**注意：** There is also [dzen2](<https://archlinux.org/packages/?name=dzen2>)包 which you can substitute for [xmobar](<https://archlinux.org/packages/?name=xmobar>)包 in either case.

Common imports: 
    
    import XMonad
    import XMonad.Hooks.DynamicLog
    
The xmobar action starts xmobar and returns a modified configuration that includes all of the options described in [#More configurable](<#More_configurable>). 
    
    main = xmonad =<< xmobar def { modMask = mod4Mask {- or any other configurations here ... -}}
    
#### More configurable

As of xmonad(-contrib) 0.9, there is a new [statusBar](<https://hackage.haskell.org/package/xmonad-contrib-0.13/docs/XMonad-Hooks-DynamicLog.html#v:statusBar>) function in [XMonad.Hooks.DynamicLog](<https://hackage.haskell.org/package/xmonad-contrib/docs/XMonad-Hooks-DynamicLog.html>). It allows you to use your own configuration for: 

  * The command used to execute the bar
  * The PP that determines what is being written to the bar
  * The key binding to toggle the gap for the bar

The following is an example of how to use it: 
    
    ~/.xmonad/xmonad.hs
    
    -- Imports.
    import XMonad
    import XMonad.Hooks.DynamicLog
    
    -- The main function.
    main = xmonad =<< statusBar myBar myPP toggleStrutsKey myConfig
    
    -- Command to launch the bar.
    myBar = "xmobar"
    
    -- Custom PP, configure it as you like. It determines what is being written to the bar.
    myPP = xmobarPP { ppCurrent = xmobarColor "#429942" "" . wrap "<" ">" }
    
    -- Key binding to toggle the gap for the bar.
    toggleStrutsKey XConfig {XMonad.modMask = modMask} = (modMask, xK_b)
    
    -- Main configuration, override the defaults to your liking.
    myConfig = def { modMask = mod4Mask }
    
#### Verify XMobar config

The template and default xmobarrc contains this. 

At last, open up `~/.xmobarrc` and make sure you have `StdinReader` in the template and run the plugin. E.g. 
    
    ~/.xmobarrc
    
    Config { ...
           , commands = [ Run StdinReader .... ]
             ...
           , template = " %StdinReader% ... "
           }
    
Now, all you should have to do is either to start, or restart, xmonad. 

### Controlling xmonad with external scripts

Here are a few ways to do it, 

  * use the following xmonad extension, [XMonad.Hooks.ServerMode](<https://hackage.haskell.org/package/xmonad-contrib/docs/XMonad-Hooks-ServerMode.html>).

  * simulate keypress events using [xdotool](<https://archlinux.org/packages/?name=xdotool>)包 or similar programs. See this [Ubuntu forums thread](<https://ubuntuforums.org/archive/index.php/t-658040.html>). The following command would simulate the keypress `Super+n`:

    xdotool key Super+n
    
  * [wmctrl](<https://archlinux.org/packages/?name=wmctrl>)包 -If you have desktopConfig or EwmhDesktops configured, this is a very easy to use and standard utility.

### Launching another window manager within xmonad

If you are using [xmonad-git](<https://aur.archlinux.org/packages/xmonad-git/>)AUR, as of January of 2011, you can restart to another window manager from within xmonad. You just need to write a small script, and add stuff to your `~/.xmonad/xmonad.hs`. Here is the script. 
    
    ~/bin/obtoxmd
    
    #!/bin/sh
    openbox
    xmonad
    
And here are the modifications you need to add to your `~/.xmonad/xmonad.hs`: 
    
    ~/.xmonad/xmonad.hs
    
    import XMonad
    --You need to add this import
    import XMonad.Util.Replace
    
    main do
        -- And this "replace"
        replace
        xmonad $ def
        {
        --Add the usual here
        }
    
You also need to add the following key binding: 
    
    ~/xmonad/xmonad.hs
    
    --Add a keybinding as follows:
    ((modm .|. shiftMask, xK_o     ), restart "/home/abijr/bin/obtoxmd" True)
    
Just remember to add a comma before or after and change the path to your actual script path. Now just `Mod+q` (restart xmonad to refresh the configuration), and then hit `Mod+Shift+o` and you should have Openbox running with the same windows open as in xmonad. To return to xmonad you should just exit Openbox. Here is a link to adamvo's `~/.xmonad/xmonad.hs` which uses this setup [Adamvo's xmonad.hs](<https://wiki.haskell.org/Xmonad/Config_archive/adamvo%27s_xmonad.hs>)

### KDE and xmonad

The xmonad wiki has instructions on how to [run xmonad inside KDE](<https://wiki.haskell.org/Xmonad/Using_xmonad_in_KDE>)

It also might be a good idea to set a global keyboard shortcut in KDE to start xmonad in case it is accidentally killed or closed. 

#### Disable plasmashell

You might want to disable plasmashell (the KDE5 thing responsible for desktop background, taskbar, tray, etc.). 
    
      cp /etc/xdg/autostart/plasmashell.desktop ~/.config/autostart/
    
Then edit `~/.config/autostart/plasmashell.desktop` and replace `Exec=plasmashell` with `Exec=`. The result will look like this: 
    
    ~/.config/autostart/plasmashell.desktop
    
    [Desktop Entry]
    Exec=
    Name=Plasma Desktop Workspace
    ... # more stuff
    
### IM Layout for Skype

In orded to create an IM layout for the newer versions of skype, the following code can be used: 
    
    xmonad.hs
    
    myIMLayout = withIM (1%7) skype Grid
        where
          skype = And (ClassName "Skype") (Role "")
    
### Example configurations

Below are some example configurations from fellow xmonad users. Feel free to add links to your own. 

  * brisbin33 :: simple, useful, readable :: [config](<https://github.com/pbrisbin/xmonad-config>) [screenshot](<http://files.pbrisbin.com/screenshots/current_desktop.png>)
  * jelly :: Configuration with prompt, different layouts, twinview with xmobar :: [xmonad.hs](<https://github.com/jelly/dotfiles/tree/master/.xmonad/xmonad.hs>)
  * MrElendig :: Simple configuration, with xmobar :: [xmonad.hs](<https://github.com/MrElendig/dotfiles-alice/blob/master/.xmonad/xmonad.hs>), [.xmobarrc](<https://github.com/MrElendig/dotfiles-alice/blob/master/.xmobarrc>), [screenshot](<http://arch.har-ikkje.net/gfx/ss/2010-09-05-163305_2960x1050_scrot.png>).
  * thayer :: A minimal mouse-friendly config ideal for netbooks :: [configs](<https://wiki.haskell.org/Xmonad/Config_archive/Thayer_Williams%27_xmonad.hs>) [screenshot](<https://wiki.haskell.org/Image:Thayer-xmonad-20110511.png>)
  * vicfryzel :: Beautiful and usable xmonad configuration, along with xmobar configuration, xinitrc, dmenu, and other scripts that make xmonad more usable. :: [git repository](<https://github.com/vicfryzel/xmonad-config>), [screenshot](<https://github.com/vicfryzel/xmonad-config/raw/master/screenshot.png>).
  * vogt :: Check out adamvo's config and many others in the official [Xmonad/Config archive](<https://wiki.haskell.org/Xmonad/Config_archive>)
  * wulax :: Example of using xmonad inside Xfce. Contains two layouts for GIMP. :: [xmonad.hs](<https://gist.github.com/jsjolund/94f6821b248ff79586ba>), [screenshot](<https://i.imgur.com/at9AbOl.png>).
  * alex-courtis :: Clean xmonad, xmobar, media keys, screenshot, j4/dmenu; fonts rendered at the DPI reported by the monitor :: [xmonad.hs](<https://github.com/alex-courtis/arch/blob/ea77edca1a1cd92e87d9c403dae891d03b9ee94e/home/.xmonad/xmonad.hs>), [screenshot](<https://raw.githubusercontent.com/alex-courtis/arch/9e3f16b93f89c328b57a96600da7fd39b81bae8e/ss.png>).

## Troubleshooting

### GNOME 3 and xmonad

[![](../File:Tango-inaccurate.png)](<../File:Tango-inaccurate.png>)**本文或本章节的事实准确性存在争议。**

**原因：** This no longer works with GNOME. It might still work with [GNOME Flashback](<../zh-cn/GNOME_Flashback.html> "GNOME Flashback").（在 [Talk:Xmonad](<../zh-cn/Talk:Xmonad.html>) 中讨论）

With the release of GNOME 3 [custom GNOME sessions](<../zh-cn/GNOME/Tips_and_tricks.html#Custom_GNOME_sessions> "GNOME/Tips and tricks") require additional steps to make GNOME play nicely with xmonad. 

Add an xmonad session file for use by gnome-session (`/usr/share/gnome-session/sessions/xmonad.session`): 
    
    [GNOME Session]
    Name=Xmonad session
    RequiredComponents=gnome-panel;gnome-settings-daemon;
    RequiredProviders=windowmanager;notifications;
    DefaultProvider-windowmanager=xmonad
    DefaultProvider-notifications=notification-daemon

Create a desktop file for GDM (`/usr/share/xsessions/xmonad-gnome-session.desktop`): 
    
    [Desktop Entry]
    Name=Xmonad GNOME
    Comment=Tiling window manager
    TryExec=/usr/bin/gnome-session
    Exec=gnome-session --session=xmonad
    Type=XSession

Create or edit this file (`/usr/share/applications/xmonad.desktop`): 
    
    [Desktop Entry]
    Type=Application
    Encoding=UTF-8
    Name=Xmonad
    Exec=xmonad
    NoDisplay=true
    X-GNOME-WMName=Xmonad
    X-GNOME-Autostart-Phase=WindowManager
    X-GNOME-Provides=windowmanager
    X-GNOME-Autostart-Notify=false

Finally, install [xmonad-contrib](<https://archlinux.org/packages/?name=xmonad-contrib>)包 and create or edit `~/.xmonad/xmonad.hs` to have the following 
    
    import XMonad
    import XMonad.Config.Gnome
    
    main = xmonad gnomeConfig

xmonad should now appear in the list of GDM sessions and also play nicely with gnome-session itself. 

#### Compositing in GNOME and xmonad

Some applications look better (e.g. GNOME Do) when composition is enabled. This, however, is not the case in the default xmonad window manager. To enable it add an additional .desktop file `/usr/share/xsessions/xmonad-gnome-session-composite.desktop`: 
    
    [Desktop Entry]
    Name=Xmonad GNOME (Composite)
    Comment=Tiling window manager
    TryExec=/usr/bin/gnome-session
    Exec=/usr/sbin/gnome-xmonad-composite
    Type=XSession

And create `/usr/sbin/gnome-xmonad-composite` and `chmod +x /usr/sbin/gnome-xmonad-composite`: 
    
    xcompmgr &
    gnome-session --session=xmonad

Now choose "Xmonad GNOME (Composite)" in the list of sessions during login. Reference [xcompmgr(1)](<https://man.archlinux.org/man/xcompmgr.1>) for additional "eye candy". 

### Xfce 4 and xmonad

Use `xfceConfig` instead of `def` after importing `XMonad.Config.Xfce` in `~/.xmonad/xmonad.hs`, e.g. adapting the minimal configuration above: 
    
    import XMonad
    import XMonad.Config.Xfce
    
    main = xmonad xfceConfig
        { terminal    = "urxvt"
        , modMask     = mod4Mask
        }
    
Also add an entry to _Settings > Session and Startup > Application Autostart_ that runs `xmonad --replace`. 

### Missing xmonad-i386-linux or xmonad-x86_64-linux

xmonad should automatically create the `xmonad-i386-linux` file (in `~/.xmonad/`). If this it not the case, grab a configuration file from the [xmonad wiki](<https://wiki.haskell.org/Xmonad/Config_archive>) or create your [own](<https://wiki.haskell.org/Xmonad/Config_archive/John_Goerzen's_Configuration>). Put the `.hs` and all others files in `~/.xmonad/` and run this command from the folder: 
    
    xmonad --recompile
    
Now you should see the file. 

**注意：** A reason you may get an error message saying that xmonad-x86_64-linux is missing is that [xmonad-contrib](<https://archlinux.org/packages/?name=xmonad-contrib>)包 is not installed.

### Problems with Java applications

If you have problems, like Java application Windows not resizing, or menus immediately closing after you click, see [Java#Gray window, applications not resizing with WM, menus immediately closing](<../zh-cn/Java.html#Gray_window,_applications_not_resizing_with_WM,_menus_immediately_closing> "Java"). 

### Empty space at the bottom of gvim or terminals

See [Vim#Empty space at the bottom of gVim windows](<../zh-cn/Vim.html#Empty_space_at_the_bottom_of_gVim_windows> "Vim") for a solution which makes the area match the background color. 

For [rxvt-unicode](<../zh-cn/Rxvt-unicode.html> "Rxvt-unicode"), you can use [rxvt-unicode-patched](<https://aur.archlinux.org/packages/rxvt-unicode-patched/>)AUR. 

You can also configure xmonad to respect size hints, but this will leave a gap instead. See [on Xmonad.Layout.LayoutHints](<https://hackage.haskell.org/package/xmonad-contrib-0.16/docs/XMonad-Layout-LayoutHints.html>). 

###  Chromium/Chrome will not go fullscreen

If Chrome fails to go fullscreen when `F11` is pressed, you can use the [XMonad.Hooks.EwmhDesktops](<https://hackage.haskell.org/package/xmonad-contrib/docs/XMonad-Hooks-EwmhDesktops.html>) extension found in the [xmonad-contrib](<https://archlinux.org/packages/?name=xmonad-contrib>)包 package. Simply add the `import` statement to your `~/.xmonad/xmonad.hs`: 
    
    import XMonad.Hooks.EwmhDesktops
    
and then add `handleEventHook = fullscreenEventHook` to the appropriate place; for example: 
    
    ...
            xmonad $ def
                { modMask            = mod4Mask
                , handleEventHook    = fullscreenEventHook
                }
    ...
    
After a recompile/restart of xmonad, Chromium should now respond to `F11` (fullscreen) as expected. 

###  Multitouch / touchegg

Touchégg polls the window manager for the `_NET_CLIENT_LIST` (in order to fetch a list of windows it should listen for mouse events on.) By default, xmonad does not supply this property. To enable this, use the [XMonad.Hooks.EwmhDesktops](<https://hackage.haskell.org/package/xmonad-contrib/docs/XMonad-Hooks-EwmhDesktops.html>) extension found in the [xmonad-contrib](<https://archlinux.org/packages/?name=xmonad-contrib>)包 package. 

### Keybinding issues with an azerty keyboard layout

Users with a keyboard with azerty layout can run into issues with certain keybindings. Using the [XMonad.Config.Azerty](<https://hackage.haskell.org/package/xmonad-contrib/docs/XMonad-Config-Azerty.html>) module will solve this. 

###  GNOME 3 mod4+p changes display configuration instead of launching dmenu

If you do not need the capability to switch the display-setup in the gnome-control-center, just execute 
    
    dconf write /org/gnome/settings-daemon/plugins/xrandr/active false

as your user, to disable the xrandr plugin which grabs Super+p. 

### Problems with focused border in VirtualBox

A known issue with Virtualbox ([Ticket #6479](<https://www.virtualbox.org/ticket/6479>)) can cause problems with the focused window border. A solution can be found by installing a compositing manager like [xcompmgr](<../zh-cn/Xcompmgr.html> "Xcompmgr") which overrides the incorrect behavior of vboxvideo. 

###  Steam games (Half-Life, Left 4 Dead, …) and xmonad

There seems to be some trouble with xmonad and Source engine based games like Half-Life. If they do not start or get stuck with a black screen, a workaround is to start them in windowed mode. To do so, right click on the game in your Steam library and choose properties, click on launch options and enter [[1]](<https://steamcommunity.com/app/221410/discussions/0/864960353968561426/>): 
    
    -windowed
    
Another solution is to float the window of the game using the manage hook. For example, the following line can be used for Half-Life: 
    
     className =? "hl_linux" --> doFloat
    
This can also be worked around by making xmonad pay attention to EWMH hints and including its fullscreen hook [[2]](<https://hackage.haskell.org/package/xmonad-contrib/docs/XMonad-Hooks-EwmhDesktops.html>): 
    
      main = xmonad $ ewmh def{ handleEventHook =
               handleEventHook def <+> fullscreenEventHook }
    
This has a few other effects and makes it behave more akin to fullscreen apps in other WMs. 

### LibreOffice - focus flicking between main window and dialog

The LibreOffice UI defaults to the gtk engine outside a desktop environment. This may cause problems with some xmonad configurations resulting in focus rapidly flicking between the LibreOffice main window and any open LibreOffice dialog window. Effectively locking the application. In this case the environment variable SAL_USE_VCLPLUGIN can be set to explicitly force LibreOffice to use another UI theme as outlined in [LibreOffice#Theme](<../zh-cn/LibreOffice.html#Theme> "LibreOffice") For instance 
    
      export SAL_USE_VCLPLUGIN=gen lowriter
    
to use the general (QT) UI. 

### Problems with finding shared libraries after update

The xmonad executable is located in `~/.xmonad/`. After upgrading xmonad, an old executable might persist and need in that case be removed for xmonad to compile a new executable. Alternatively use `xmonad --recompile`. 

In the case that `xmonad --recompile` cannot find any modules at all (including `XMonad` itself), try regenerating the package database cache 
    
    sudo ghc-pkg recache
    
###  Broken/missing XMonad.Prompt and window decorations

XMonad by default uses the font `-misc-fixed-*-*-*-*-10-*-*-*-*-*-*-*` [[3]](<https://wiki.haskell.org/Xmonad/Frequently_asked_questions#Tabbed_or_other_decorated_layouts_not_shown>). If this font is missing those windows simply fail to render at all. Easiest fix is to install `(xorg-fonts-misc`. 

## See also

  * [xmonad](<https://xmonad.org/>) \- The official xmonad website
  * [xmonad.hs](<https://wiki.haskell.org/Xmonad/Config_archive/Template_xmonad.hs>) \- Template xmonad.hs
  * [xmonad: a guided tour](<https://xmonad.org/tour.html>)
  * [dzen](</wzh/index.php?title=Dzen&action=edit&redlink=1> "Dzen（页面不存在）") \- General purpose messaging and notification program
  * [dmenu](<../zh-cn/Dmenu.html> "Dmenu") \- Dynamic X menu for the quick launching of programs
  * [平铺式窗口管理器比较](<../zh-cn/%E5%B9%B3%E9%93%BA%E5%BC%8F%E7%AA%97%E5%8F%A3%E7%AE%A1%E7%90%86%E5%99%A8%E6%AF%94%E8%BE%83.html> "平铺式窗口管理器比较") \- Arch wiki article providing an overview of mainstream tiling window managers
  * [Share your xmonad desktop!](<https://bbs.archlinux.org/viewtopic.php?id=94969>)
  * [xmonad hacking thread](<https://bbs.archlinux.org/viewtopic.php?id=40636>)
  * [xmonad-log-applet](<https://github.com/alexkay/xmonad-log-applet>) \- An applet for the GNOME, MATE or xfce panel.
