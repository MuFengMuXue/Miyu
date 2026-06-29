# Fcitx

Fcitx is a lightweight input method framework aimed at providing environment independent language support for Linux. It supports a lot of different languages and also provides many useful non-CJK features.

## Installation
Install the  package.

## Input method engines
Fcitx provides built-in input methods for Chinese Pinyin and table-based input (for example Wubi).

Depending on the language you wish to type, other input method engines are available:

## Chinese
* , fcitx wrapper for Baidu Pinyin IM engine.
*  is a popular Zhuyin input engine for Traditional Chinese based on .
*  uses internet sources to provide input candidates. The selected cloud result will be added to local dictionary. It support all fcitx pinyin input method except .
* , Googlepinyin wrapper for fcitx.
* , based on schemas from the Rime IME project.
* , Sogou input method supporting Jianpin, fuzzy sound, cloud input, English input, and mixed skin.
* , based on . It strikes a good balance between speed and accuracy.

## Japanese
* , a popular Japanese input engine. However, it is not actively developed anymore.
* , based on Mozc, the Open Source Edition of Google Japanese Input.
* , a Japanese Kana Kanji input engine, based on .
* , a Japanese Kana Kanji input engine, based on .

## Other languages
* , for typing Korean hangul, based on .
* , for other languages provided by M17n.
* , for typing Sinhalese.
* , for typing Vietnamese characters.

## Input method module
To obtain a better experience in Qt programs, install ,  or  input method modules as your need. Without these modules, the input method may work on most applications but you may experience input method hang up, preview window screen location error or no preview error.

Applications below do not use GTK/Qt input module:

* Applications use Tk, motif or xlib
* Emacs, Opera, OpenOffice, LibreOffice, Wine, Java, Xterm, urxvt, WPS

## Others
* , light UI for fcitx.
*  adds Cangjie, Zhengma, Boshiamy support.
* , tables for Latex, Emoji and others.
* #GUI configuration tools

Others packages (including git version) are also available in the AUR. All components of fcitx will requires fcitx to restart after install.

## Usage
## Desktop Environment Autostart
If you are using any XDG compatible desktop environment such as KDE, GNOME, Xfce, LXDE, after you re-login, the autostart should work out of the box. If not, run the fcitx executable. To see if fcitx is working correctly, open an application and press  (the default shortcut for switching the input method) to invoke fcitx and input some words.

If fcitx failed to start with your desktop automatically or if you want to change the parameters to start fcitx, configure autostart or edit the  file in your  directory (copy it from  if it does not exist yet).

When other input methods with xim support are also running, fcitx may fail to start due to an xim error. Ensure that no other input methods are running before you start fcitx.

Also please set the following environment variables to prefer IM modules for GTK/Qt applications.

For i3 and Sway users, add  in your configuration file. fcitx5 users should add  instead.

## Set environment variables for IM modules
Set the following environment variables to register the input method modules.

 GTK_IM_MODULE=fcitx
 QT_IM_MODULE=fcitx
 XMODIFIERS=@im=fcitx

Without these variables, applications may fallback to XIM protocol, except for Qt5 applications which do not have XIM support and require an IM module in place.

If fcitx process does not start automatically, you might need to add  in your .
If  does not start, type  after it.

## XIM
Optionally, you can use the X Input Method (XIM) in your GTK and/or Qt programs without installing the above modules in which case you need to change the corresponding lines above as following:

 GTK_IM_MODULE=xim
 QT_IM_MODULE=xim

If you change it in  or , add .

## Configuration
## GUI configuration tools
fcitx provides a KDE configuration module () and a GTK3 configuration tool ().

Run fcitx-config-gtk3 after  is installed. Unset Only Show Current Language if you want to enable an input method for a different language.

Stop fcitx manually before changing configuration, or the change may be lost.

In order to enable spell checking, press  when fcitx is on an input method provided by fcitx-keyboard.

## Input methods configuration
You can add/remove input methods in the GUI tools. Note that the search is case sensitive.

The first set input method is the inactive state, while all the rest will be active states. You generally want the inactive state to be one of the Keyboard options (e.g. "Keyboard - English (US)"). These options just input based on the keyboard layout in the name.

Under Global Config, the Trigger Input Method shortcut will only switch between the inactive and last used active state. The Scroll between Input Methods will by default only scroll between different active states, but can also be set to include the inactive state in the advanced settings. Furthermore, the Scroll between Input Methods shortcut has to be pressed in order, e.g.  will only activate if  is pressed before .

Configuration settings for IME's can be found by setting the keyboard to the desired IME and right-clicking the tray icon.

## Change default UI
Fcitx support kimpanel protocol to provide better desktop integration.

* Gnome-Shell: You can install kimpanel from extensions.gnome.org or , which provides a similar user experience as ibus-gjs.

## Extend pinyin dictionary
Pinyin dictionary is located at . File  is for single characters and file  defines pinyin phrases. To extend them, put your file into  and restart fcitx.

## Skins
You can download skins and extract them to one of the following directories, you can create the directory if it does not exist:

*  for global settings
*  for user settings

## Cloud Pinyin configuration
After installing the  input method, restart fcitx. If you could not find it in configuration GUI, enable advanced settings. The cloud query result will be added to current input method dictionary automatically.

If your network prevents you from accessing Google, change Cloud Pinyin source to Baidu.

The query result from cloud will list as secondary candidate by default and it is configurable. If the result already exists, only one item is shown.

## Tips and tricks
## Shortcut keys
Some commonly used default shortcut keys:

*  - activates the input method
*  - temporarily switches to English
*  - switch between input methods
* / - page forward/backward
*  - Full-width, half-width switching

## Vim
If you often use Fcitx under Vim, you can install the  plugin, or add the following code to . When exiting insert mode, Fcitx is automatically closed, otherwise the reverse:

 "##### auto fcitx  ###########
 let g:input_toggle = 1
 function! Fcitx2en()
    let s:input_status = system("fcitx-remote")
    if s:input_status == 2
       let g:input_toggle = 1
       let l:a = system("fcitx-remote -c")
    endif
 endfunction

 function! Fcitx2zh()
    let s:input_status = system("fcitx-remote")
    if s:input_status != 2 && g:input_toggle == 1
       let l:a = system("fcitx-remote -o")
       let g:input_toggle = 0
    endif
 endfunction

 set ttimeoutlen=150
 "Exit insert mode
 autocmd InsertLeave * call Fcitx2en()
 "Enter insert mode
 autocmd InsertEnter * call Fcitx2zh()
 "##### auto fcitx end ######

## Special symbols
Create , the content of the file is as follows:

  #The first line with "#" is a comment
  #Format: coding symbol
  #Code can only be lowercase letters, after pinyin analysis, the longest is 10 (such as py is 2, pinyin is also 2)
  #Mathematics symbols
  sxfh ＋
  sxfh －
  sxfh ＜
  sxfh ＝
  sxfh ＞
  sxfh ±
  sxfh ×
  sxfh ÷
  sxfh ∈
  sxfh ∏
  sxfh ∑
  sxfh ∕
  sxfh √
  sxfh ∝

Enter a code directly to match the corresponding special symbol.

## Clipboard Access
You can use fcitx to input text in your clipboard (as well as a short clipboard history and primary selection). The default trigger key is . You can change the trigger key as well as other options in the Clipboard addon configure page.

## fcitx-remote
fcitx-remote is a commandline tool that can be used to control the fcitx state. It is installed with the  package.

One option worth elaborating upon here is , which switches to the input method identified by . The correct  for an in use input method can be found by executing fcitx-diagnose, and looking under the "## Input Methods:" section.

## Input special character
See Fcitx5#Input special characters, this content also applies to Fcitx.

## Troubleshooting
## Disable or change Extra key for trigger input method
This setting is under the Global Config tab and defaults to SHIFT Both, meaning that pressing either shift key will immediately change input methods. Although it should only apply when a shift key is pressed individually, it tends to randomly interrupt typing capital letters, selecting text with the keyboard, etc. while using standard keyboard input.

In addition, this setting may revert to default without warning at any time. To ensure fcitx's configuration cannot be modified, you must make the file immutable:  (as the root user).

## Diagnose the problem
If you have problems using fcitx (eg.  fails to work in all applications), then the first thing you should try is to diagnose using .
The output of  should contain the clue to most common problems.
Providing the output of it will also help when you consult other people (eg. in IRC or forums).

## Emacs
If your  is English, you may not be able to use input method in emacs due to an old emacs bug. You can set your  to something else such as  before emacs starts to get rid of this problem.

Note that the corresponding locale should be generated on your your system.

The default fontset will use `-*-*-*-r-normal--14-*-*-*-*-*-*-*' as basefont (in ), if you do not have one matched (like terminus or 75dpi things, you can look the output of `xlsfonts'), XIM can not be activated. According to [https://fcitx-im.org/wiki/FAQ#Emacs FAQ and Fonts, it is likely that  is the one that should be installed since  no longer provides the required fontset.

## Emacs Daemon
If you are using emacs daemon/client mode,  should be set when starting the daemon. For example, by running emacs daemon with .

If starting emacs daemon from systemd, set  in the unit file.

( may need to be set explicitly here as systemd does not load . Check the  variable in emacs to verify both variables are set correctly.)

## Ctrl+Space fail to work in GTK programs
This problem sometimes happens especially when the locale is set as English. Please make sure your  is set correctly.

See also FAQ

If you have set the  environment variables to fcitx but cannot activate fcitx, please check if you have installed the corresponding input method modules.

Some programs can only use xim, if you are using these programs, please make sure your  is set properly and be aware of the problems you may have. These programs include all programs that are not using GTK or Qt (e.g. programs that use tk, motif, or xlib directly), emacs, opera, openoffice, libreoffice.

If you cannot enable fcitx in gnome-terminal under Gnome and the above way does not work, try:

 $ gsettings set org.gnome.settings-daemon.plugins.xsettings overrides "{'Gtk/IMModule':}"

## Buildin Chinese Pinyin Default NOT ACTIVE
If your locale is , fcitx did NOT enable the buildin Chinese Pinyin input method by default. There is only  input method enabled. You can get a notice by  command like this:

    ## Input Methods:
        1.  Found 1 enabled input methods:
                fcitx-keyboard-us
        2.  Default input methods:
            **You only have one input method enabled, please add a keyboard input method as the first one and your main input method as the second one.**

Then you should add  or  input method to actived input methods by the GUI configure tool.

## fcitx and KDE
For some reasons, KDE does not handle keyboard layouts properly. For example, if you switch from US (English) to LT (Lithuanian), all numbers on the keyboard should produce Lithuanian letters, but they still produce numbers as the output. This can be fixed by these steps:

# Turn off fcitx if it is running in the background.
# Disable stuff related to KDE:
## At System settings > Input devices > Layouts (tab) make sure that Configure layouts is unchecked.
## At System settings > Input devices > Advanced (tab) make sure that Configure keyboard options is unchecked.
# Start fcitx to start it. You can close the terminal - fcitx will still be running in the background.
# Set up your needed layouts (right click on the system tray icon, then Configure).
# Right click on the system tray icon, then Exit

At this point you should have working layouts, native KDE layouts switch icon should appear and you can switch them by mouse scroll or click on it.

## Input method switched to English unintentionally
For instance, in XMind, when the user presses  to create a node, input method is always switched to English, and has to be switched back to Chinese manually.

To fix this issue, open the fcitx GUI configuration tool (provided by ), switch to tab Global Config, in dropdown menu Share State Among Window, select PerProgram or All.

## xmodmap settings being overwritten
fcitx controls keyboard layout, so your xmodmap settings will be overwritten.
Since 4.2.7, Fcitx will try to load  if it exists.

For more details on how you can save your xmodmap changes see FAQ

## Fcitx and setxkbmap
If you are using setxkbmap for another language, then (as per above) fcitx can overwrite them and even prevent from switching to that language in certain applications (e.g. QuteBrowser).

If you would like to prevent that and manage your xmodmap layouts independently from fcitx then follow these steps:
# Open the fcitx GUI configuration tool (provided by )
# Switch to tab Addon
# Select Advanced
# Search for xkb#
# Select X Keyboards Integration
# Click Configure
# Unselect Allow to Override System XKB Settings
# Click OK

## Fcitx preedit box is too small with HiDPI
See HiDPI#Fcitx
