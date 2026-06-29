# Mozc

From the project's home page:
:Mozc is a Japanese input method editor (IME) designed for multi-platform such as Android OS, Apple OS X, Chromium OS, GNU/Linux and Microsoft Windows. This OpenSource project originates from Google Japanese Input.

The differences between Mozc and Google Japanese Input are described in detail at the project's About Branding page, but in short, Mozc's open-source code does not include Google's extensive word conversion tables (so called "dictionaries"), so its conversion quality is not equivalent to that of Google's branded product. This can be mostly mitigated with custom dictionaries though (see below).

## Installation
## Split vs. integrated packages
As an IME, Mozc has two distinct parts: a server, which does all the work of the conversion, and a set of modules which allow the server to communicate with the system's input method framework and output the result on the screen. A separate module is required for each of IBus, Fcitx5, Fcitx and Emacs.

Some Mozc packages contain only the IMF-specific modules and split the server into a separate  package; this allows for the different modules to be installed side by side, independently from the server itself (which can be useful in a multi-user setup where different users use different IMFs, or when using Emacs).

Other Mozc packages forego this split and instead integrate the server together with the modules. This does have its advantages, but one very notable disadvantage is that it makes it impossible to install additional modules due to file conflicts (because more than one package are competing to provide the server's files).

If for any reason you will be needing more than one IMF module installed at the same time, the solution is to either build the non-split packages yourself and manually resolve the file conflicts, or to only choose from among the packages that split the server from the modules.

## The UT Dictionary
As already mentioned, Mozc's conversion quality is not quite as good as that of Google Japanese Input because it does not include Google's extensive word conversion tables (so called "dictionaries"). A solution exists for that in the form of the UT dictionary, which is a third-party dictionary that enhances Mozc's conversion quality and brings it closer to Google Japanese Input. It achieves that by including thousands of additional words aggregated from several popular online sources (based on page rankings from Google, Yahoo and Wikipedia) and also by integrating a variety of other specialized sources such as the NEologd dictionary, which in the words of its creator contains "neologisms (new words), which are extracted from many language resources on the Web".

## Summary
Install one or more of , ,  and .

When you are asked which flavor of Mozc you wish to use, select either  for the vanilla Mozc or  for the UT-enhanced Mozc.

## Configuration
## IBus
See IBus for more information.

{{Tip|When used with IBus, by default Mozc will launch in Direct (Eisu) input mode, which can be problematic on keyboards that lack the Eisu key. To change this behavior and make Mozc launch in Hiragana input mode instead, edit  and append the following line:

{{hc|~/.config/mozc/ibus_config.textproto|2=
...
}
active_on_launch: True
}}

If that doesn't work:

* Check that  does not exist. If it does (for example because Mozc was upgraded from an older installation), it will take precedence over .
* Run the  command to restart IBus.

More information is available in the Mozc documentation.
}}

Open the IBus configuration tool by running:

 $ ibus-setup

In the Input Method tab, click on Add, and then search for and add the Mozc layout.

You can switch to the new Mozc layout with  (as per the IBus default).

## Fcitx5
See Fcitx5 for more information.

Open the Fcitx5 configuration tool by running:

 $ fcitx5-configtool

In the Input Method tab, add Mozc in the Add Input Method menu. You can set the keyboard shortcut to switch between layouts in Configure global options.
This is different to the normal KDE layout switcher, so one could switch between different layouts mapped to Japanese by Mozc.

Similar to Ibus’ Use system keyboard layout, you can select the layout for Mozc to the left of the remove button. This selects the layout to use before Mozc, so one can use custom layouts mapped correctly to Mozc.

## Emacs
You can use mozc.el (mozc-mode) to input Japanese via LEIM (Library of Emacs Input Method). To use mozc-mode, write the following into your  or some other file for Emacs customizing:
 (require 'mozc)  ; or (load-file "/path/to/mozc.el")
 (setq default-input-method "japanese-mozc")
mozc.el provides "overlay" mode in the styles of showing candidates (from mozc r77) which shows a candidate window in box style close to the point. If you want to use it by default, add the following:
 (setq mozc-candidate-style 'overlay)

 (toggle-input-method) enables and disables use of mozc-mode.

## Disabling XIM
When you are using input method on your desktop and assigning activation/deactivation of input method to C-SPC, you will be not able to use C-SPC/C-@ as set-mark-command on Emacs. To avoid this problem, add the following into your  or . xim will be disabled on Emacs.
 Emacs*UseXIM: false

## Tips and tricks
## Confirming Mozc version which you are using now
Type "ばーじょん" ("version") and convert it while activating Mozc. The version number of Mozc will be shown in the candidate list like follows:

## Launching Mozc tools from command line
The followings are commands to launch Mozc tools:

* Mozc Settings:
* Mozc Dictionary Tool:
* Mozc Word Register:

## Use CapsLock as Eisu_toggle key on ASCII layout keyboard
In all of the preset keymap styles of Mozc, the command Toggle alphanumeric mode on Composition mode is assigned to the  (Eisu_toggle),  or  key, but the ASCII keyboard has none of them.

One solution for it is to use Caps Lock key as Eisu_toggle (Mozc does not recognize the Caps Lock key as of r124). The following is a way to assign Eisu_toggle to  (without any modifier keys) and Caps_Lock to , as on the OADG keyboard layout.

Edit  as follows:
 keycode 66 = Eisu_toggle Caps_Lock
 clear Lock

Then, restart X or run xmodmap to apply the changes immediately:
 $ xmodmap ~/.Xmodmap

## Use underlying Japanese keymap on Non-English/Non-Japanese systems
If you are primarily using a Non-English or Non-Japanese system with a keyboard layout different than QWERTY (e.g. German) and only want to use Japanese as a secondary input language, the key mapping might be based on this main keyboard language. This might be odd, especially if migrating from Windows or MacOS or directly from a Japanese computer.

To change the underlying keyboard layout on Ibus, change the default keymap in  by setting the  key to Japanese (or some other keyboard with QWERTY):

{{hc|~/.config/mozc/ibus_config.textproto|2=
engines {
...
  layout : "jp"
...
}
}}

## Troubleshooting
## Building Mozc fails (process is killed)
If the build process fails with an error message like the following:
 ...
 /bin/sh: line 1:  xxxx killed
 ...
 make: *** error 137
 ...
Make sure you have not run out of memory.

## New version of Mozc does not appear though I upgraded Mozc and restarted X or Input Method Framework (not rebooted)
The old version of Mozc may be still on your memory. Try to kill the existing mozc_server process:
 $ killall mozc_server

## mozc_server becomes defunct
Mozc cannot run in root. Start X in normal user.

## mozc_emacs_helper not found in emacs
When installing mozc.el you need to install a helper program called .

You need to install  for this helper program.

## mozc tool(s) does not launch
It is also possible to launch Mozc tools with log sent directly to console, which is useful for debugging. To enable this, simply append  like this for example:

[https://github.com/google/mozc/issues/438 See also

## Suggestion window is blindingly white in dark mode
Use the following environment variable:

 MOZC_IBUS_CANDIDATE_WINDOW=ibus
