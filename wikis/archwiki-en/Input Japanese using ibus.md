# Input Japanese using ibus

This page explains how to get the Japanese input to work using IBus.

If you use SCIM, see Smart Common Input Method platform.

If you use Uim, see Input Japanese using uim.

## Installation
You need the following packages to input Japanese.

* Japanese fonts
* Japanese input method (Kana to Kanji conversion engine)
* Input method framework: ibus

## Japanese fonts
see also Fonts, Font configuration and Localization/Japanese for configuration or more detail.

Recommended Japanese fonts are as follows.

## Sans-serif
* adobe-source-han-sans ||  or
: Open-source OTF fonts developed by Adobe.

## Serif and Sans-serif
* IPA fonts ||
: An open source OTF font set including sans-serif (Gothic) and serif (Mincho) glyphs provided by Information-technology Promotion Agency, Japan (IPA).

If you want to show 2channel Shift JIS art properly, use the following fonts:
* Monapo font (AUR: )

## ibus
Install the  package.

## Input method
## Anthy
Anthy is one of the most popular Japanese input methods in the open source world.

Install  from the official repositories.

## Mozc
See Mozc.

Mozc is a Japanese Input Method Editor (IME) designed for multi-platform such as Chromium OS, Windows, Mac and Linux which originates from Google Japanese Input.

Install  which is available on AUR.

## Settings
## Environment variables
Apply the following environment variables to Xorg:

 GTK_IM_MODULE='ibus'
 QT_IM_MODULE='ibus'
 GLFW_IM_MODULE='ibus'
 XMODIFIERS='@im=ibus'

## Using systemd
If you are using systemd to manage your X session, you will need to set the environment variables in your systemd session rather than an init script.

Lastly, you will need to enable

## ibus preferences
Configure ibus preferences by running:
 $ ibus-setup
which brings forth a GUI.

Navigate to the 'Input Method' tab, click on 'Add', click on 'Japanese' and select your input method.

Now click on the newly added list entry and click on 'Preferences' to configure your input method.

## Anthy preferences
Change 'Input Mode:' from 'Latin' to 'Hiragana'

## After cofiguration
You can run  or restart X to test your settings.

By default  cycles between your input methods

Provided everything went well you should be able to input Japanese in X.
