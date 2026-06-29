# Input Japanese using uim

This page explains how to get the Japanese input to work using uim.

If you use SCIM, see Smart Common Input Method platform.

If you use IBus, see IBus.

## Installation
You need the following packages to input Japanese.

* Japanese fonts
* Japanese input method (Kana to Kanji conversion engine)
* Input method framework: uim

## Japanese fonts
see also Fonts and Font configuration for configuration or more detail.

Recommended Japanese fonts are as follows.

## Sans-serif
* adobe-source-han-sans ||  or
: Open-source OTF fonts developed by Adobe.

## Serif and Sans-serif
* IPA fonts ||
: An open source OTF font set including sans-serif (Gothic) and serif (Mincho) glyphs provided by Information-technology Promotion Agency, Japan (IPA).

If you want to show 2channel Shift JIS art properly, use the following fonts:

* Monapo font ()

## uim
Install the  package.

## Input method
## Anthy
Anthy is one of the most popular Japanese input methods in the open source world. However, it has not been maintained for a long time. Debian succeeds it from May 2010.

Install the  package.

## Extra dictionary
Anthy's default dictionary does not include several characters which are not specified on EUC-JP (JIS X 0208) such as "①", "♥", etc. alt-cannadic provides extra dictionaries including those characters.

Get alt-cannadic dictionary and put them under your .
 $ tar jxvf alt-cannadic-091230.tar.bz2
 $ mkdir ~/.anthy/imported_words_default.d (if not exist)
 $ cp alt-cannadic-091230/extra/*.t ~/.anthy/imported_words_default.d/

Please see official wiki for more detail (Japanese).

## Modified Anthy (anthy-ut)
Modified Anthy is a set of patches and huge extended dictionaries which aims to improve the Kana to Kanji conversion quality of original Anthy.

Modified Anthy consists two different upstreams:
* Patched source of Anthy by G-HAL
* Huge extended dictionalies by UTSUMI

## Mozc
Mozc is a Japanese Input Method Editor (IME) designed for multi-platform such as Chromium OS, Windows, Mac and Linux which originates from Google Japanese Input.

Though  adapts to only ibus input method framework, macuim provides uim-mozc plugin.

## Mozc (Vanilla)
Install .

## Registering Mozc
## Google CGI API for Japanese input
Google CGI API for Japanese Input (Google-CGIAPI-Jp) is CGI service to provide Japanese conversion on the Internet by Google. It can be used on web browser. Its conversion engine seems to be equivalent to Google Japanese Input, so conversion quality is probably better than Mozc.

You can use it via uim. Choose "Google-CGIAPI-Jp" on uim-im-switcher-gtk/gtk3/qt4 or uim-pref-gtk/gtk3/qt4.

## Settings
## Environment variables
Autostart the following on Xorg startup:

 export GTK_IM_MODULE='uim'
 export QT_IM_MODULE='uim'
 uim-xim &
 export XMODIFIERS='@im=uim'

## Toolbar utilities
If you want to use UimToolbar utilities which shows and controls uim mode, add one of the followings, too.

## uim-toolbar-gtk/qt
Using toolbar appears as a window.

For GTK 2:
 uim-toolbar-gtk &
For GTK 3:
 uim-toolbar-gtk3 &
For Qt4:
 uim-toolbar-qt4 &

## uim-toolbar-gtk-systray
Using toolbar for system tray.

For GTK 2:
 uim-toolbar-gtk-systray &
For GTK 3:
 uim-toolbar-gtk3-systray &

## Using systemd
If you are using systemd to manage your X session, you will need to set the environment variables in your systemd session rather than an init script.

Lastly, you will need to enable the  and  user units.

## uim preferences
Configure uim preferences by running :
 $ uim-pref-gtk (Or, uim-pref-gtk3/uim-pref-qt4)
which brings forth a GUI.

Choose your preferring input method as 'Default input method'.

You can run  or restart X to test your settings.

Provided everything went well you should be able to input Japanese in X.

## Input Japanese on Emacs
uim provides uim.el the bridge software between Emacs and uim. Here is a sample to use uim on Emacs with utf-8 encoding.

Please see Official wiki for more detail.

## LEIM or minor-mode
You can call uim.el from Emacs in two ways; directly or with the LEIM (Library of Emacs Input Method) framework. Though settings of them are different, basic functions are same. If you want to switch between uim.el and other Emacs IMs frequently, you should use LEIM framework.

## Settings for the minor-mode
If you will be using on minor-mode, write the following settings into your  or some other file for Emacs customizing.

 ;; read uim.el
 (require 'uim)
 ;; uncomment next and comment out previous to load uim.el on-demand
 ;; (autoload 'uim-mode "uim" nil t)

 ;; key-binding for activate uim (ex. C-\)
 (global-set-key "\C-\\" 'uim-mode)

## Settings for the LEIM
If you will be using via LEIM, write the following settings into your  or some other file for Emacs customizing and choose default input method.

 ;; read uim.el with LEIM initializing
 (require 'uim-leim)

 ;; set default IM. Uncomment the one of the followings.
 ;(setq default-input-method "japanese-anthy-utf8-uim")        ; Anthy (UTF-8)
 ;(setq default-input-method "japanese-google-cgiapi-jp-uim")  ; Google-CGIAPI-Jp
 ;(setq default-input-method "japanese-mozc-uim")              ; Mozc

## Preferred character encoding
uim.el uses euc-jp character encoding by default. To set UTF-8 as preferred encodings, add the followings into your  or some other file for Emacs customizing.

 ;; Set UTF-8 as preferred character encoding (default is euc-jp).
 (setq uim-lang-code-alist
       (cons '("Japanese" "Japanese" utf-8 "UTF-8")
            (delete (assoc "Japanese" uim-lang-code-alist)
                    uim-lang-code-alist)))

## Enable inline candidates displaying mode by default
The inline candidates displaying mode displays conversion candidates just below (or above) preedit text vertically instead of echo area. If you want to enable inline candidates displaying mode by default, write as follows.

 ;; set inline candidates displaying mode as default
 (setq uim-candidate-display-inline t)

## Set Hiragana input mode by default
To set Hiragana input mode at activting uim, add the settings like follows:

 ;; Set Hiragana input mode at activating uim.
 (setq uim-default-im-prop '("action_anthy_utf8_hiragana"
                             "action_google-cgiapi-jp_hiragana"
                             "action_mozc_hiragana"))

## Ignoring C-SPC on uim.el
When you are assigning activation/deactivation of input method to C-SPC, C-SPC is stolen to switch input mode by uim.el while it is activated. To prevent the stealing and use for set-mark-command, add the followings into your  or some other file for Emacs customizing.

 (add-hook 'uim-load-hook
           '(lambda ()
              (define-key uim-mode-map nil)
              (define-key uim-mode-map [0 nil)))

## Disabling XIM on Emacs
When you are using input method on your desktop and assigning activation/deactivation of input method to C-SPC, you will be not able to use C-SPC/C-@ as set-mark-command on Emacs. To avoid this problem, add the following into your  or . xim will be disabled on Emacs.

 Emacs*UseXIM: false

## Troubleshooting
## Set the GTK_IM_MODULE variable, but uim still does not work with GTK 2 applications
In case you already set the GTK_IM_MODULE environmental variable, but uim still does not work with GTK 2 applications, you need to specify the location of gtk.immodules, which is created by and can be generated with .

The default location is  for GTK 2.

You can do this with either the GTK_IM_MODULE_FILE variable (not recommended, it causes GTK 3 applications to see incompatible modules) or the im_module_file setting (recommended).

Add the following to  or :

  im_module_file "/etc/gtk-2.0/gtk.immodules"

## Cannot input Japanese on Opera
If you use Opera and cannot input Japanese with uim, try to edit environment variable as follows:
Make sure to add the following to the beginning of /usr/bin/opera.

 export XMODIFIERS='@im=uim'
 export QT_IM_MODULE='xim'

## Cannot type a consonant in Zenkaku mode
If you cannot type a consonant in Zenkaku mode, add the following to your configuration file.

    e.g.  vi ~/.uim.d/customs/custom-google-cgiapi-jp.scm

    (define ja-rk-rule-hoge
    (map
    (lambda (c)
    (list (cons (list c) ()) (list c c c)))
    '("b" "c" "d" "f" "g" "h" "j" "k" "l" "m"
    "p" "q" "r" "s" "t" "v" "w" "x" "y" "z"
    "A" "B" "C" "D" "E" "F" "G" "H" "I" "J" "K" "L" "M"
    "N" "O" "P" "Q" "R" "S" "T" "U" "V" "W" "X" "Y" "Z")))
    (if (symbol-bound? 'ja-rk-rule-hoge)
    (set! ja-rk-rule (append ja-rk-rule-hoge ja-rk-rule)))

## uim-toolbar-gtk-systray: tray icon is crushed
Though some of DE, WM or panel application  may provide only one icon space per application on system-tray/notification-area, uim-toolbar-gtk-systray displays some icons on it by default so those icons are crushed. Choose just one of them to solve it. The steps to display only 'Input mode' icon for example as follows:

# Run .
# Click 'Toolbar' on 'Group' list.
# Take the all checkmarks off.
# Click 'Anthy', 'Anthy (UTF-8)' or 'Mozc' which you are using on 'Group' list.
# Click Edit button in 'Toolbar' box > 'Enable toolbar buttons' line.
# Enable only 'Input mode' and click 'Close' button.
# Click 'OK' button to close uim-pref-gtk.
The tray icon will be displayed "あ" (Hiragana mode) or "ー" (Direct mode).

## I use darker theme, I cannot read the uim mode icons
You can choose icons for darker background (uim 1.6.0 or later).

# Run .
# Click 'Toolbar' on 'Group' list.
# Check 'Use icon for dark background'.
