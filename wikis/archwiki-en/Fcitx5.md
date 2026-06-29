# Fcitx5

Fcitx5 is an input method framework with a lightweight core, offering additional language support via addons. It is the successor to Fcitx.

## Installation
Install the  package.

The  group pulls the main  package, some of #Input method modules, and #Configuration tool.

## Input method modules
Some GUI toolkits provide input method modules support for input method integration in applications. However, they're not always needed, and #Wayland native protocols might show better performance. See #Integration for details.

* Qt5/6: .
* GTK: .
* Qt4: .

## Plugins
For date and time support with , install :  will then input the current time, while  will input the current date.

## Usage
## Integration
Applications need to redirect input events to the input method in order to actually make use of it. The protocol used for such a purpose could be provided by display servers (i.e. Wayland's text-input or Xorg's XIM), or by GUI toolkits' input method modules.

## Wayland
Wayland's native text-input protocol usually yields better results than input method modules. The Wayland frontend of fcitx5 is enabled by default, and GTK/Qt utilize text-input if no other IM module is explicitly specified. Therefore, it's generally recommended to only use #IM modules in Xwayland applications. Additionally, enable #XIM for legacy X11 applications. ===== GNOME =====

GNOME does not support Wayland's input-method protocol, which is required by fcitx5's Wayland frontend to communicate with the compositor and display the popup.  provides support for popups in GNOME Wayland through Kimpanel.

## KDE Plasma
Plasma on Wayland requires the input method process to be invoked by KWin.[https://fcitx-im.org/wiki/Using_Fcitx_5_on_Wayland#KDE_Plasma To achieve that, quit any running Fcitx 5 process, head to System Settings > Input & Output > Keyboard > Virtual Keyboard, then select Fcitx 5.

## Wayfire
Enable the input-method-v1 plugin and add fcitx5 to the autostart commands.

Due to Wayfire partially supporting text-input-v1, for software that supports text-input-v1 but not text-input-v3, see #Software using Wayland input protocol cannot obtain Wayland popup window.

For Qt6 software, which currently defaults to text-input-v1 but supports text-input-v3, an other workaround is using  but you may encounter other bugs.

## IM modules
Set the following environment variablesglobally if using X11 or for each Xwayland application if using a Wayland compositor with text-input support.

 GTK_IM_MODULE=fcitx
 QT_IM_MODULE=fcitx

Alternatively, write  for GTK3 and  for GTK2 into the configuration files in GTK#Configuration to make GTK applications running under X11/Xwayland use the IM module without affecting Wayland-native GTK applications.

If your locale is , and your GTK2 application cannot activate fcitx5, you can set  specifically for it.

## XIM
For generic X11 applications, enable XIM support through the following environment variable:

 XMODIFIERS=@im=fcitx

## Autostart
If your desktop environment implements XDG Autostart, see Autostarting#On desktop environment startup.

See Autostarting#On Xorg startup or Autostarting#On window manager startup depending on your needs.

## Dictionaries
## Chinese
For the Chinese input method of Fcitx5, several dictionaries are currently available:

* : A dictionary created by felixonmars based on Chinese Wikipedia. Applicable to Pinyin input method.
* : A dictionary for Rime input method.
*  : A dictionary created by outloudvi based on Moegirlpedia.
* : A dictionary for Rime input method.
* [https://github.com/cathaysia/fcitx5_dicts/releases/tag/0.0.1 cedict: A dictionary converted from cedict dictionary.

## Custom dictionary
Generally speaking, since  supports importing the Sogou dictionary, there is no need to customize dictionaries to a large extent, but  still provides related tools (i.e. ).

The original dictionary file is a text file, its format is: . To convert it:

 $ libime_pinyindict dictionary.txt dictionary.dict

The custom dictionary file can be placed in

## Configuration
## Configuration tool
The configuration file of  is located at . Although you can use a text editor to edit the configuration file, you might find a GUI configuration tool much more convenient, so install the  package.

## Disable overriding XKB settings
By default Fcitx5 overrides X keyboard settings. (The ones you can set with  command or graphical tools provided by desktop environments.) If you do not want that, run  and uncheck Addons > XCB > Allow Overriding System XKB Settings.

## Themes and appearance
## Themes
The number of default themes is limited, you can find more themes on GitHub.

*
*
*
*
*

## Enable single-line mode
In the settings of the Pinyin input method (or Rime input method), enable Show preedit within application to enable single-line mode.

## Use fullwidth punctuation after latin letter or number
By default Fcitx5 uses halfwidth punctuation after latin letter or number. If you want to use fullwidth punctuation instead, run  and uncheck Configure addons > Punctuation > Half width punctuation after latin letter or number.

## Troubleshooting
## Diagnose problems
If you have problems using fcitx5, e.g. if  fails to activate input method in some applications, try to diagnose the current environment using , whose output should contain clues for the most common problems.

## Fcitx5 single-line mode not working in some applications
If the single-line mode does not work in GTK applications such as Firefox, install

The single-line mode is unsupported by WPS Officeand Sublime Text[https://github.com/fcitx/fcitx5/issues/60.

## Fcitx5 is not working in JetBrains IDEs
Please verify that your system locale is correct and well generated, as an incorrect locale will prevent Fcitx5 from working correctly in JetBrains IDEs.

## Emoji show abnormally in the candidate box
Confirm you have a font with emoji support installed (such as ). Disable anti-aliasing for the chosen emoji font (such as Noto Color Emoji) as explained in Font configuration#Anti-aliasing and Font configuration#Custom settings for certain fonts or font styles.

## Fcitx5 not available in RStudio
Run the following command:

 $ strings /usr/lib/rstudio/lib/libQt5Core.so.5 | grep "Qt 5"

Find out the version of the Qt library, use this version to recompile  in , and put it into  directory.

## Fcitx5 not available on Steam and Dota 2
The IME can be activated on Steam Big Screen mode and Dota 2 by using  instead of . === Fcitx5 not available in Chromium running on Wayland ===

See Chromium#Native Wayland support.

## Candidate popup misaligned in HiDPI mode of GTK environments
If the position of your candidate popup is not anchored at your cursor position, install .

## Fcitx5 right alt key not working with Electron applications
If a non-system keyboard is used by an application (e.g. Discord, Element, etc.), the application may handle the  before the input method can. This results in some input methods failing in specific applications. One solution is to add another input method group, setting the system layout to correspond to this keyboard. For example, to type Polish letters like  on a QWERTY keyboard with English as your primary system keyboard, you can use the Fcitx5 Configuration GUI to:

# Click the Add Group plus button.
# Select this group in the dropdown and now add your input method (the keyboard, e.g. Keyboard - Polish).
# Use Select system keyboard layout to pick the one that matches this input method, and apply changes.

See comments from the Fcitx5 developers if you need another solution. [https://github.com/fcitx/fcitx5/issues/740

## Software using Wayland input protocol cannot obtain Wayland popup window
Software using the Wayland input protocols (such as wezterm and GTK software if the environment variable is set to ) may have issues with text-input-v3 support.

Regarding Qt and GTK software support for Wayland, according to the fcitx5 developer: Qt has text-input-v2 support. If QT_IM_MODULE is empty, it can be used, but there are some minor problems with pre-editing. In addition, for the current version of Wayland input method protocol, Wayland can only have one global input context. So now if you want to use the "per-application" input status supported by Fcitx 5, it may be a problem. However, there is a benefit to using Qt's text input protocol, which is that the input window will not flicker visually.
: Gtk has text-input-v3 support, but its pre-editing style is poor, with bold fonts highlighted. In addition, its text support is weak. So now, if you want to have all the Fcitx features, using  may still be a good choice.

In summary, for [https://fcitx-im.org/wiki/Using_Fcitx_5_on_Wayland#Gtk3_.2F_Gtk4 GTK3/GTK4 and Qt5/Qt6 you may still want to set the respective environment variables if you encounter issues without them.

## Tips and tricks
## Customizing traditional and simplified Chinese conversion
Some IMEs assume Simplified Chinese by default, resulting in incorrect characters being displayed when using Traditional input, e.g. 爲什麼 instead of 為什麼. To fix this, the usage of the  can be customized.

To configure conversion, set  to one of the following values:
* s2t - Simplified to Traditional (OpenCC) (this is the default and probably not what you are looking for)
* s2tw - Simplified to Traditional (Taiwan)
* s2twp - Simplified to Traditional (Taiwan) with Taiwanese idiom
* s2hk - Simplified to Traditional (Hong Kong)

To configure the reverse, set  to one of the following values:
* t2s - Traditional (OpenCC) to Simplified (OpenCC) (this is the default and probably not what you are looking for)
* tw2s - Traditional (Taiwan) to Simplified (OpenCC)
* tw2sp - Traditional (Taiwan) to Simplified (OpenCC) with Mainland Chinese idiom
* t2hk - Traditional (OpenCC) to Hong Kong variant
* t2tw - Traditional (OpenCC) to Taiwan Standard
* tw2t - Traditional (Taiwan) to Traditional (OpenCC)
* hk2s - Traditional (Hong Kong) to Simplified (OpenCC)
* hk2t - Traditional (Hong Kong) to Traditional Chinese (OpenCC)
* t2jp - Traditional (Kyūjitai) to New Japanese Kanji (Shinjitai)
* jp2t - New Japanese Kanji (Shinjitai) to Traditional (Kyūjitai)

Up to date list here: OpenCC

## View the Unicode encoding of selected characters
* If you want to view the Unicode encoding of the selected text in a text editor, then directly select the text, and then use the shortcut keys  to view the encoding of the selected text.
* If you want to view the Unicode encoding of some text in a non-editable area (such as this wiki), you need to first copy the text to the clipboard, then click on any editable area (such as the search box), and then use the shortcut keys  to view the encoding of the text in the clipboard.

## Input special characters
In general, for some simple symbols, such as , , , , etc., you can enter them through Configuring compose key, but for more special symbols, such as , , , etc., you Either customize , or use Fcitx5's Unicode function to achieve.

Take  as an example:

Position the cursor in any input box, and then press , and then enter , you will see a variety of , other special characters are similar here.

## Switching halfwidth and fullwidth punctuation
For , fullwidth punctuation is used by default, one may use  to switch between halfwidth and fullwidth punctuation.

## Automatically switch input methods in vim
It is recommended to use the fcitx.vim plugin. This plugin will keep different buffer-specific input method states in their respective insert modes.

For a simple solution, you can append the code to : If you are using , then append the above code to .

If you are using Vim9, then the code should be

If you are using VSCodeVim, add the following snippet into your configuration file:

 "vim.autoSwitchInputMethod.enable": true,
 "vim.autoSwitchInputMethod.defaultIM": "1",
 "vim.autoSwitchInputMethod.obtainIMCmd": "/usr/bin/fcitx5-remote",
 "vim.autoSwitchInputMethod.switchIMCmd": "/usr/bin/fcitx5-remote -t {im}",

## Pinyin input method
## Import Sogou dictionary
* For KDE users, you can import Sogou dictionary through Settings > Regional Settings > Input Method > Pinyin > Dictionary > Import.
* For users who use , you need to manually open the software "Fcitx5 Configuration" and manually configure it in the Pinyin input method.
* Alternatively, scel2org5 (from ) allows the conversion.

You can import local dictionaries or browse and import online dictionaries.

## Cloud Pinyin
On the settings page of the Pinyin input method, you can enable Cloud Pinyin. But if you need to change the default backend of Cloud Pinyin, you need to change it in the global settings of . Provided backends are , , .

## Stroke Filter
Set the shortcut key after the "stroke filter" of the pinyin input method you set (the default is )
Then after entering the text, press the shortcut key, the words stroke filter will appear in the candidate box of the input method, and the words can be filtered by strokes. The specific rules are: h horizontal stroke, s vertical stroke, p left-falling stroke, n right-falling stroke, z turning stroke.

By default, the stroke filter is to filter the first character of a sentence, but you can switch between different characters in a sentence by using determining characters by word.

For example, to perform stroke filtering on the third character in the word 中华人民共和国, you can press  twice in a row after enabling stroke filtering to let  perform stroke filtering on it.

## RIME/Zhongzhou rhyme
## Import dictionary
Take importing dictionary  and  as an example.

1. Change the  file (take  as an example, and modify the name of the other input schemes)

2. Create a new  file

## Fuzzy sound settings
Please comment (#) or delete unnecessary fuzzy sounds as needed. If you need to add other fuzzy sounds, please refer to [https://gist.github.com/2320943 Mingyue Pinyin fuzzy sound custom template

If the  file does not exist

If the file exists, paste the part below  to the end of the file (there is only one  in )

## Special symbols
Import the  dictionary in the rime-dict project to input Greek letters, some mathematical symbols and Emoji expressions in Pinyin.

Example:

* Greek letters: input  to output

* Mathematical symbols: input  to output

* Special symbols: Input  to output

* Serial number: input  to output

* Emoji expression: Input  to output

## Load librime-lua plugin
If you want to load the librime-lua plugin, you must add the  module in the Rime input method settings of the fcitx configuration tool.
