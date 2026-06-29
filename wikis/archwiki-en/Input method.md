# Input method

From Wikipedia:Input method:

:An input method (or input method editor, commonly abbreviated as IME) is an operating system component or program that enables users to generate characters not natively available on their input devices by using sequences of characters (or mouse operations) that are natively available on their input devices. Using an input method is usually necessary for languages that have more graphemes than there are keys on the keyboard.

In simpler words, an IME is an application that allows us to use Latin characters in order to type non-Latin characters.

Some IMEs do this through a process called romanization, which is the transliteration of non-Latin language sounds into the Latin equivalents that most closely resemble them. As an example, the Japanese written word for "sake" or "rice wine" is , also written as , and romanized as "sake". The IME's role is to act as a middleman between the keyboard and the input fields, so that when we type "sake" it will intercept the keyboard's input, replace "sake" with  or  (as chosen by users) and type the native characters for us instead of the keys we pressed.

There are also IMEs that do not make use of romanization. One of the most prominent ones, Cangjie, does so by decomposing Chinese characters into their radicals, matching these radicals to a second set of its own internal radicals, and finally matching these internal radicals to the Latin characters. As an example, the Chinese written word for "wine" is also , which consists of the radicals , , ,  and . Cangjie matches these radicals to the internal radicals , , ,  and , and then matches these to the Latin characters ; this means that when we type "emcw", Cangjie will intercept the keyboard's input, replace "emcw" with , and type that character on the screen.

## Input method framework
Most IMEs work as part of an input method framework (commonly abbreviated as IMF), which is an application that allows the user to easily switch between different IMEs. In fact, this is the exact same application that many of us unknowingly use everyday to switch between the different Latin keyboard layouts (e.g. English, Spanish, German, etc).

The most common IMF is IBus (often used in GTK-based environments like GNOME), followed by Fcitx5 (mostly used in Qt-based environments like KDE), Scim, Fcitx, and Uim. Very uncommon ones include Gcin, Nimf and Hime. Additionally, Emacs is a very popular text editor that has its own internal IMF.

See also Wikipedia:List of input methods for Unix platforms.

## List of available input method editors
The following table shows the IMEs for various languages currently available in the Arch repositories and the AUR.

Other following main complex scripts of China (non-Han Chinese languages), are included in Fcitx5 in Chinese languages category. They are not available in iBus:  Manchu and Xibe (Tungustic languages, Mongolian script), and Galik extension and Todo variant. Uygur (Turkic language, Arabic script, no method of old-Uygur script). there is no Kazakh/Kirgiz method, Uygur one should work, Kazakhstan and Mongolia use Cyrillic for Kazakh and Kyrgyzstan use cyrillic too for Kyrgyz).

{| class="wikitable" style="text-align:center;"
|-
! style="background:var(--background-color-neutral,#eaecf0);color:inherit;background:linear-gradient(to top right,var(--background-color-neutral,#eaecf0) 49%,var(--border-color-base,#a2a9b1) 49.5%,var(--border-color-base,#a2a9b1) 50.5%,var(--background-color-neutral,#eaecf0) 51%);line-height:1.2;padding:0.1em 0.4em;"|IMFIME
! Fcitx5 !! Fcitx !! IBus !! Uim !! Emacs !! Scim !! Hime !! Gcin !! Nimf
|-
! colspan=10| Chinese
|-
| Rime
|
|
|
|
|
|
|
|
| built-in
|-
| Pinyin[https://github.com/libpinyin/libpinyin Libpinyin
|
| built-in
|  (replaces the older )
|
|
|
|
|
| built-in
|-
| Zhuyin
|
|
|
|
|
|
|
|
| built-in
|-
| CangjieSuchengSmartCangjie
|
|
|
|
|
|
|
|
|
|-
| Wubi
| built-in
| built-in
|
| built-in
|
|
|
|
|
|-
| SunPinyin
|
|
|
|
|
|
|
|
|
|-
! colspan=10| Japanese
|-
| Mozc
| ,
|
|
|
|
|
|
|
|
|-
| Anthy
|
|
|
| built-in
|
|
| built-in
| built-in
| built-in
|-
| SKK
|
|
|
| built-in
|
|
|
|
|
|-
| KKC
|
|
|
|
|
|
|
|
|
|-
! colspan=10| Korean
|-
| Libhangul
|
|
|
| built-in
|
|
|
|
| built-in
|-
! colspan=10| Vietnamese
|-
| UniKey
|
|
|
|
|
|
|
|
|
|-
| Bamboo
|
|
|
|
|
|
|
|
|
|-
| Lotus
|
|
|
|
|
|
|
|
|
|-
! colspan=10| Indic
|-
| Avro (Bangla)
|
|
|
|
|
|
|
|
|
|-
| Helakuru (Sinhala)
|
|
|
|
|
|
|
|
|
|-
| m17n
|
|
|
|
|
|
|
|
|
|-
| OpenBangla Keyboard (Bangla)
|
|
|
|
|
|
|
|
|
|-
| Sayura (Sinhala)
|
|
|
|
|
|
|
|
|
|-
| Varnam
|
|
|
|
|
|
|
|
|
|-
! colspan=10| Mongol bichig (Mongolian Script, not Cyrillic)
|-
| Mongolian|Script
| in prefs, Chinese => Mongolian （bichig)
|
|
|
|
|
|
|
|
|-
! colspan=10| Tibetan
|-
| 3 main methods ewts, tcrc, wylie
| in prefs, Chinese => Tibetan, or +
|
| +
|
|
|
|
|
|
|}

## Configuration
In order for your desktop environment to properly register an installed input method framework as available and assign it to handle user input, a set of environment variables must be configured accordingly.

## Fcitx5
See Fcitx5#Integration for more information.

## Fcitx
See Fcitx for more information.

 GTK_IM_MODULE=fcitx
 QT_IM_MODULE=fcitx
 XMODIFIERS=@im=fcitx

## IBus
See IBus for more information.

 GTK_IM_MODULE=ibus
 QT_IM_MODULE=ibus
 XMODIFIERS=@im=ibus

## Uim
See Uim for more information.

 GTK_IM_MODULE=uim
 QT_IM_MODULE=uim
 XMODIFIERS=@im=uim

## Emacs
According to this Fcitx wiki entry, "in some case, including emacs and java. Emacs has a historical bug, that under en_US.UTF-8 or similar locale, it will never use XIM (Though emacs is a gtk app, it use XIM). The only way to walkaround this is to use LC_CTYPE to fix this."

## Scim
See Scim for more information.

 GTK_IM_MODULE=scim
 QT_IM_MODULE=scim
 XMODIFIERS=@im=scim

## Xim
 GTK_IM_MODULE=xim
 QT_IM_MODULE=xim
