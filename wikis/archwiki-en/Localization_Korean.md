# Localization/Korean

This article describes how to set up a Korean language environment. It does not cover setting up Korean input on a tty.

## Fonts
*  - Korean OpenType/CFF fonts
*  - Google Noto CJK fonts
*  - Source Han Sans customized by Spoqa
*  - Collection of Korean TrueType fonts
*  - D2Coding fixed width TrueType font made by Naver
*  - Nanum series TrueType fonts
*  - Nanum series fixed width TrueType fonts
* / - Korean TrueType/OpenType fonts by Korea Publisher Society
* / - Multilingual (Korean, Yethangul, Chinese extended, Japanese, Latin extended, Cyrillic, Arabic, Hebrew, Devanagari) TrueType/OpenType fonts by Korea Publisher Society
*  - Pretendard, a Korean sans-serif font with Latin characters similar to Inter () and Apple's San Francisco

## Locale
You should have  enabled in . It is recommended that you always use a  locale rather than the  locale. For more information, read locale.

## Input methods
The following input methods are available for Korean:

*  for Fcitx5
*  for IBus
*  for SCIM
* uim-byeoru of uim
* Nimf
* #Nabi

## Configuration
## Fcitx5
Fcitx5 is a modern Chinese/Japanese/Korean input method. Install the  and  packages for Korean input and configuration respectively.

After installing Fcitx5-im, run , select Add Input Method -> Deselect "Show Only Current Language" and add Hangul.

Lastly, add the following to  for Fcitx5 to work across almost all apps:

 GTK_IM_MODULE=fcitx
 QT_IM_MODULE=fcitx
 XMODIFIERS=@im=fcitx

## Nabi
Nabi is a standalone Korean input method, developed by Choe Hwanjin, offering many unique features, such as Yethangul support.

Install the  package.

Once you have finished the installation, add the following to xprofile, xinitrc, or :

 export XIM=nabi
 export XIM_ARGS=
 export XIM_PROGRAM="nabi"
 export XMODIFIERS="@im=nabi"
 export GTK_IM_MODULE=xim
 export QT_IM_MODULE=xim

Once you restart the X session, nabi will autostart by default. The default Korean keyboard layout is Dubeolsik(두벌식). If you need a different Korean keyboard layout (e.g. Sebeolsik or Dubeolsik Yetgul), click on the system tray icon of nabi, and select a input method from the menu that pops up.

## scim-hangul
Install .

Now add the following to the user's , , or :

 export XMODIFIERS=@im=SCIM
 export GTK_IM_MODULE="xim"
 export QT_IM_MODULE="scim"
 scim -d

## uim-byeoru
Follow the instructions in User:Isaac914/uim to install uim and to get it running.  Return to this section after uim is installed and running as the default input method.

Open the uim preferences window by running :

 $ uim-pref-gtk (Or, uim-pref-gtk3/uim-pref-qt4)

Within global settings, check on the Specify default IM checkbox. Then, set Byeoru as default. You may also want to disable input methods that you do not plan on using by clicking on the 'edit' button. If you want to quickly switch between Korean and other languages (other than English), check the enable IM switching by hotkey checkbox, and set a hotkey to switch between enabled IMEs.

When you are done with the global preferences, find Byeoru in the tree menu on the left side of the preferences window. From there, you can set the Korean keyboard layout you want to use (e.g. ), specify the korean/Hanja dictionary that Byeoru will use, and other miscellaneous settings. Then, click on Byeoru Keybinding 1 in the tree menu. Set the hotkey you want to use to enable/disable Byeoru. Most Korean users use  or .

If all went properly, you should now be able to use UIM-byeoru to type in Korean.

## Troubleshooting
;IBus:As of November 2014, IBus sometimes does not recognize user-set hotkeys for IM switching. This means that you may need to click on the IBus systray icon every time to want to switch input methods.

;uim:uim-byeoru may cause Opera to crash.

;scim: scim-hangul, as of November 2014, has issues with Google Chrome and Chromium web browsers. With the default environment variables, you cannot input Korean in Google Chrome or Chromium. scim also causes problems in Gedit as of November 2014. When scim-hangul is active, pressing  does not work properly. A workaround for both these issues will be explained in #scim-hangul. However, even with this workaround applied, Chrome/Chromium users may find that the preedit string disappears when the spacebar or any other modifier key is pressed. There is currently no known workaround for this issue.

;fcitx:Fcitx-hangul has issues with Google Chrome and Chromium. Some users have reported that fcitx only recognizes Google Chrome/Chromium's URL bar as an input window only after their themes have been changed.

;nabi:  is a standalone Korean input method that is being developed by Choehwanjin. Nabi provides many unique features, such as Yethangul support. If you only need to use Korean and English input, you may want to install nabi. Currently, nabi causes an issue with chromium. When you press the spacebar, the preedit string will be placed after the space, causing your input to look like this:

## Libreoffice
In some cases, Libreoffice will not take Korean input from any input method. To resolve this issue, try adding  to , , or .

## Tips and tricks
## Using the Right alt key to switch input methods
## On X11
You can use the right  key (e.g. '한/영키') to switch between Input methods if you are using uim, scim, or nabi. To do this, add the following lines after the environment variables that start your input method:

Then, in the settings of your input method, add the right  key as a hotkey to switch IMEs. The right  key has been remapped to a non-modifier key called "Hangul". The script above also allows you to use the right  key (e.g. '한자키') to activate Hanja input. The right  key should also have been remapped to "Hangul_Hanja". Add this key as a Hanja hotkey within the settings of your input method. If adding that to your  or  file did not work, create a script containing those four lines and set it to auto execute when your desktop environment starts up.

## On Wayland
On Wayland,  does not work because it is only intended for X11. Instead,  can be configured to map the keys instead.

Then enable the .
