# Localization/Japanese

This article describes how to set up a Japanese language environment and input method. It only covers the general and recommended cases . For full details on alternatives (e.g. Japanese input on tty or less common input method frameworks), see their respective It does not cover setting up Japanese input on the console/tty.

## Fonts
To display Japanese characters, a Japanese (or Chinese) font must be installed. If text appears as gibberish on your screen, ensure you have an appropriate Japanese (Chinese can also suffice) font installed on your system.

Some recommended Japanese fonts are as follows (see Fonts or Font configuration for more fonts or their configuration):

*  - Japanese OpenType/CFF fonts, style Gothic (sans-serif).
*  - Japanese OpenType/CFF fonts, style Mincho (serif).
*  - Google Noto CJK fonts.
*  - Formal style Japanese Gothic (sans-serif) and Mincho (serif) fonts set; one of the highest quality open source font. Default of openSUSE-ja.
*  - An updated version of ipafont.
*  - Japanese Kanji font set. The official successor to  (serif).
*  - Japanese free TrueType font. This is outdated and not maintained any more, but may be defined as a fallback font on several environments.
*  - Japanese TrueType font obtained by mixing MPLUS and Open Sans
*  - Japanese fonts to show 2channel Shift JIS art properly.
*  - Modern Gothic style Japanese outline fonts. It includes all of Japanese Hiragana/Katakana, Basic Latin, Latin-1 Supplement, Latin Extended-A, IPA Extensions and most of Japanese Kanji, Greek, Cyrillic, Vietnamese with 7 weights (proportional) or 5 weights (monospace).
*  - Japanese Gothic fonts. Default of Debian/Fedora/Vine Linux
*  - KanjiStrokeOrders font that indicates the stroke order of characters.

## Locale
See locale for details.

Locales are used to correctly display regional or language/locale-specific standards. To ensure the Japanese locale is enabled, confirm that  is in the output of:

 $ locale -a

To enable the Japanese locale, uncomment  in :

Afterwards, regenerate your locale:

 # locale-gen

## Japanese Input
To type Japanese characters using a Western keyboard, an input method (or input method editor (IME)) is required to convert rōmaji into kana or kanji.Wikipedia:Romanization of Japanese To conveniently switch between different IMEs (e.g. to switch between English and Japanese input), IMEs often function as part of an Input Method Framework (IMF) to enable easily switching between different keyboard layouts.

## Input Method Framework (IMF)
The most common IMFs are IBus (more common for GTK-based environments) and Fcitx5 (more common for Qt-based environments), which support all available Japanese IMEs. For a full overview of IMFs and supported IMEs, see this table. This article only briefly covers installation and configuration of #Fcitx5 and #IBus.

## Fcitx5
In most cases, installing the  group suffices. For full details and instructions, see Fcitx5#Installation.

To enable Fcitx5, configure at least the following environment variables:

Best per user option might be to  them in your personal ~/.bash_profile.

## IBus
Install the  package. See IBus#Installation for more information.

## Input Method Editor (IME)
Both Fcitx5 and IBus support all available Japanese IMEs. Follow the instructions for installing the IME of your choosing. If in doubt, #Mozc is a good recommendation.

## Mozc
From the project's home page:

:Mozc is a Japanese input method editor (IME) designed for multi-platform such as Android OS, Apple OS X, Chromium OS, GNU/Linux and Microsoft Windows. This OpenSource project originates from Google Japanese Input.

Install the Mozc version for the IMF of your choosing (e.g.  for Fcitx5 or  for IBus support).

## Anthy
Anthy is supported or built into most IMFs, though it is effectively dead.

Install the Anthy version for the IMF of your choosing (e.g.  for Fcitx5 or  for IBus support).

To be able to switch between the input methods add "Anthy" as such within the configuration menu. Shortcuts and behavior are able to be altered within the configuration menu of the addons.

Standard shortcut to switch between ひらがな(Hiragana), カタカナ(Katakana) and Romaji (roman alphabet) is . While typing the word written appears underlined. Hit  two times to list alternative writings and Kanjis.

## SKK (libskk)
Simple Kana to Kanji (SKK) is a basic kana to kanji conversion method based on Emacs. It was designed by Dr. Masahiko Sato (Professor Emeritus, Kyoto University) (old link) and created in 1987.A unique feature of SKK is that it converts words one by one (single-word conversion), without analysing syntax or grammar.

Install the libskk version for the IMF of your choosing (e.g.  for Fcitx5 or  for IBus support).

## KKC (libkkc)
From the project's [https://github.com/ueno/libkkc GitHub page:

:libkkc provides a converter from Kana-string to Kana-Kanji-mixed-string. It was named after kkc.el in GNU Emacs, a simple Kana Kanji converter, while libkkc tries to convert sentences in a bit more complex way using N-gram language models.

Install the libkkc version for the IMF of your choosing (e.g.  for Fcitx5 or  for IBus support).

## Google CGI API for Japanese Input
Available IM frameworks: uim

Google CGI API for Japanese Input (Google-CGIAPI-Jp) is CGI service to provide Japanese conversion on the Internet by Google. It can be used on web browser. Its conversion engine seems to be equivalent to Google Japanese Input, so conversion quality is probably better than Mozc.

You can use it via uim. Choose "Google-CGIAPI-Jp" on uim-im-switcher-gtk/gtk3/qt4 or uim-pref-gtk/gtk3/qt4.
