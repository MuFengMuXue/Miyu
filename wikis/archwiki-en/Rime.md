# Rime

Rime is an input method engine for entering Chinese characters, supporting a wide range of input methods.

The Rime engine itself does not provide a frontend for receiving user input. It must be used with an input method framework such as Fcitx5 or IBus.

## Installation
Install the  package containing the Rime engine, and the integration corresponding with your IMF:

* For Fcitx5, install.
* For Fcitx, install .
* For IBus, install .

## Configuration
In order for Rime to work, input schemas are needed. Schemas are text files that can be created and customized by users. By default, some schemas are installed with  meta package as it is a dependency of .

Alternatively, there are several input schemas available in package repository:

*  - 朙月拼音 Standard Mandarin
*  - 地球拼音 Mandarin with tones
*  - Double pinyin input schemas, include 自然碼雙拼, Double pinyin ABC (智能ABC雙拼), Double pinyin FLYPY (小鶴雙拼), Double pinyin MSPY (MSPY雙拼) and Double pinyin PYJJ (拼音加加雙拼).
*  - 袖珍简化字拼音 Simplified pinyin
*  - 粵語拼音 Cantonese pingjam
*  - 倉頡五代 Cangjie
*  - 速成 Quick
*  - 五筆畫 Stroke
*  - 五筆字型86 Wubi
*  - 上海吳語 wugniu
*  - 注音 bopomofo
*  - Emoji input
*  - 小鶴音形, a derivative of 小鶴雙拼
*  - 雾凇拼音, comes with a large dictionary and other smart functions

Some schema packages provide more than one schemas. For example,  provides 5 schemas including  and . You can check content of each package from Rime GitHub organization.

You can switch input schema at any time by pressing  to trigger the program menu. See #Selecting input method.

## Configuration directory
To customize Rime, you should first create the Rime configuration directory. Assuming you are using :

 $ mkdir ~/.config/ibus/rime

Or if you are using :

 $ mkdir ~/.config/fcitx/rime/

Or if you are using Fcitx5:

 $ mkdir ~/.local/share/fcitx5/rime/

In this directory, create a file named , where you specify your input schema of choice. For example, if you want to be able to type pinyin with tones, you can use the Terra Pinyin input method by adding it to the list of enabled schemas:

The proper names for the installed   schemas can be found in:

Note that the indentation level is important. This file overrides the default configuration, so if you only add Terra Pinyin, it will be the only schema enabled.

## Apply configuration
To make the customizations effective, you need to redeploy. If you have working IBus or Fcitx GUI, you may find a ⟲ (Deploy) button and click it. Alternatively, use the following command, assuming you are using :

 $ rm ~/.config/ibus/rime/default.yaml && ibus-daemon -drx

Or if you are using :

 $ rm ~/.config/fcitx/rime/default.yaml && fcitx-remote -r

Or if you are using :

 $ rm ~/.local/share/fcitx5/rime/default.yaml && fcitx5-remote -r

## Tones
Specifying tones is optional but they are very useful for filtering the list:

 1st tone: -
 2nd tone: /
 3rd tone:  「　【　〔　［
 ] ->　」　】　〕　］
 { ->　『　〖　｛
 } ->　』　〗　｝
 　《　〈　«　‹
 > ->　》　〉　»　›
 @ ->　＠　@　☯
 / ->　／　/　÷
 * ->　＊　*　・　×　※
 % ->　％　%　°　℃
 $ ->　￥　$　€　£　¥
 | ->　・　｜　|　§　¦
 _ -> ——
 \ ->　、　＼　\
 ^ ->　……
 ~ ->　〜　~　～　〰

## Advanced
More advanced examples are provided on the project website (in Chinese).

## Troubleshooting
## ibus-setup set orientation invaild in GNOME environment
See issue #52. Create  with follows:

 style:
   horizontal: true

## Tips and tricks
## Greek letters
Greek characters can be typed by adding the following to  or a custom input scheme file:

For example, with this scheme, the character  is produced by typing .
