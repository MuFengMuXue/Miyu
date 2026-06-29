# Emacs

Emacs is an extensible, customizable, self-documenting real-time display editor.

At the core of Emacs lies an Emacs Lisp interpreter, the language in which the majority of Emacs' built-in functionality and extensions are implemented.

GNU Emacs uses GTK as its default X toolkit, though it functions equally well within a CLI environment.

## Installation
Install one of the following packages:

*  - stable release,
*  - without GUI; only run on a terminal emulator,
*  - PGTK enabled,
* Other variants can be searched for, as an example  provides the Lucid (Athena) toolkit in place of GTK.

If you want Emacs spell checking to work, also install  and an aspell language, such as

## Usage
Before launching emacs, you should know how to close it (especially if you run it in a terminal): use the
 key sequence. If you are new to Emacs, it's recommended to work through the official tutorial. To do so, first start Emacs, then select "Tutorial" from the splash screen or press  and then press .

To start Emacs run:

 $ emacs

or, to use it from the console:

 $ emacs -nw

or, for fast loading (no .emacs) and editing within CLI:

 $ emacs -Q -nw

If you installed the nox version,  and  will be the same.

A file name can also be provided to open that file immediately:

 $ emacs filename.txt

## No colors
By default, Emacs starts with a color theme showing hyperlinks in dark blue. To start Emacs on a text terminal without any color theme or scheme:

 $ emacs -nw --color=no

This will cause all text to appear in the foreground color of the terminal — normally white text on a black background, or black text on a white background.

## As a daemon
In order to avoid reloading the Emacs configuration file every time Emacs starts, you can run Emacs as a daemon:

 $ emacs --daemon

You may then connect to the daemon by running:

 $ emacsclient -nc

Which creates a new frame  (use  if you prefer to use it in the terminal) and does not hog the terminal  ().
Note that some programs such as Mutt or Git (for commit messages) wait for the editor to finish, so you cannot use the  parameter.
If your default editor is set to use it, you will have to specify an alternate editor (e.g. ) for those programs.

## As a systemd unit
A systemd unit is included in Emacs 26.1. The unit is installed with Emacs, but it must be enabled as a user unit (not a system-wide) after installing Emacs:

 $ systemctl --user enable --now emacs

After the service is started, Emacs is ready.

If you want to be able to start graphical emacs frames through  on Wayland, a specific drop-in snippet is needed (unless you are running ), as shown in EmacsWiki.

Note that systemd user units do not inherit environment variables from a login shell (like ). See systemd/User#Environment variables for more information.

If you start emacs as a daemon, you may want to set the  and  environment variables to  so that programs that start an editor use emacsclient instead of starting a new full instance of the editor. Programs that use an external editor include email programs (for editing the message), Git (for editing the commit message), and less (the  command for editing the displayed file). Do not use the  () option to emacsclient, since programs typically expect editing to be finished when the editor exits.

It is also recommended to change any GUI start menu entries (or equivalent) for Emacs to point to emacsclient instead of emacs, so that the emacs daemon is used instead of starting a new emacs process.

## Getting help
Emacs has a built-in tutorial which can be accessed by clicking the first link on the splash screen and selecting Help>Emacs Tutorial from the menu or by pressing .

To read the tutorial in a language other than English, use the command , and enter

Emacs is self-documenting by design. As such, a great deal of information is available to determine the name of a specific command or its keybinding, for example. See all contextual help bindings with . You can access the quick help for the Emacs help system with .

Emacs also includes a set of reference cards, useful for beginners and experts alike, see .

## The manuals
If you really want to master Emacs, the most recommended source of documentation remains the official manuals:

* Emacs: the complete Emacs user manual.
* Emacs FAQ.
* Emacs Lisp Intro: if you never used any programming language before.
* Elisp: if you are already familiar with a programming language.

You can access them as HTML documents or PDFs from GNU.org or directly from Emacs itself thanks to the embedded 'info' reader: . Press  to choose a book.

Some users prefer to read books using 'info' because of its convenient shortcuts, its paragraphs adapting to window width and the font adapted to current screen resolution. Some find it less irritating to the eyes. Finally you can easily copy content from the book to any Emacs buffer, and you can even execute Lisp code snippets directly from the examples.

You may want to read the Info book to know more about it: .
Press  while in info mode for a quick list of shortcuts.

You can read man pages with Emacs with .
Note that man pages for most GNU programs are not as complete as their Info manuals.

## Configuration
One of Emacs's main features is its extensibility and the ease of configuration. Emacs has a built-in customization engine. You can do  which displays a list of customization options. For how to use this interface, see the Easy Customization info node: . You can set customization opens just for one Emacs session or save them into a configuration file so that they are saved across Emacs sessions. Note that this is what the customization interface does if you select Apply and Save.

When Emacs is started, it normally tries to load a Lisp program from an "initialization file", or "init file" for short. This file, if it exists, specifies how to initialize Emacs for you. Emacs looks for your init file at , , , or . See the info node "Init File" for more:

## Tips and tricks
## TRAMP
TRAMP (Transparent Remote Access, Multiple Protocols) is an extension which, as its name suggests, provides transparent access to remote files across a number of protocols. When prompted for a filename, entering a specific form will invoke TRAMP. Some examples:

To prompt for the root password before opening  with root permissions:

 C-x C-f /sudo::/etc/hosts

To connect to 'remotehost' as 'you' via SSH and open the file :

 C-x C-f /ssh:you@remotehost:~/example.txt

The path for TRAMP is typically of the form '/To connect to 'myhost' as 'you' and edit  with sudo:

 /ssh:you@remotehost|sudo:remotehost:/etc/hosts

TRAMP supports much more than the examples above might indicate. For more information refer to the TRAMP info manual, which is distributed with Emacs.

## LSP
[https://github.com/joaotavora/eglot Eglot is a native client for the Language Server Protocol.

Hooks can be loaded at startup:

where  can be replaced by any language name such as  or . For a global application to all languages, use .

## Using Emacs as git mergetool
By default, Git provides support for using Emacs' Emerge mode as a merge tool. However you may prefer the Ediff mode. Unfortunately this mode is not supported by git for technical reasons. There is still a way to use it by evaluating some elisp code upon emacs call.

Note that the command has to be on a single line.
In the above example, we launch a new instance of Emacs. You might want to use emacsclient for quicker startup; it is not recommended though since the Ediff call is not really clean: it could mess with your current Emacs session.

If you want an instant startup you can use the  parameter. If you want to launch Emacs quickly while preserving at least a part of your configuration, you can call Emacs with

 emacs -q -l ~/.emacs-light

where the light configuration file loads only what you need for Ediff.

See kerneltrap.org and stackoverflow for more details on this trick and the Ediff issue.

## Using Caps Lock as Control key
Some users like this behavior to avoid the so-called "emacs pinky".  A nice way to achieve this in GUI desktops (Xorg or Wayland), terminals, and even the console is to use .  Install the package and create this config file:

Then enable and start the keyd service.

## Multiplexing emacs and emacsclient
Opening a new file in the same  requires the use of .  command can be itself wrapped to do the smarter job to open the file if the session exists.

To start session you need to . This snippet will create server in first session of emacs. Add this to your  configuration file.

Shell alias method is not adequate for this since you also need to pass variables or start the independent session of your own. Add this to the  or any rc file of your shell. This will make your  command behave like emacsclient if the argument is passed.

{{bc|
function emacs {
    if  $# -eq 0 ; then
        /usr/bin/emacs # "emacs" is function, will cause recursion
        return
    fi
    args=($*)
    for ((i=0; i  is undefined' ===

Searching about this bug on Google, we find this link: https://lists.gnu.org/archive/html/help-gnu-emacs/2009-05/msg00167.html explaining the problem. The normal way to use accent keys does not work as expected. Trying to accent a word like 'fiancé' will produce the message above.

A way to solve it is just put the line below on your startup file, :

   (require 'iso-transl)

And no, it is not a bug, but a feature of new Emacs versions. Reading the subsequent messages about it on the mail list, we found it :It seems that nothing is loaded automatically because there is a choice betwee iso-transl and iso-acc. Both seem to provide an input method with C-x 8 or Alt- prefix, but what you and I are doing is just pressing a dead key (^, ´, `, ~, ¨) for the accent and then another key to "compose" the accented character. And there is no Alt key used in this! And according to documentation it seems be appropriate for 8-bit encodings, so it should be pretty useless in UTF-8. I reported this bug when it was introduced, but the bug seems to be classified as a feature ... Maybe it's just because the file is auto-loaded though pretty useless.

## C-M-% and some other bindings do not work in emacs nox
This is because terminals are more limited than Xorg. Some terminals may handle more bindings than other, though. Two solutions:

* either use the graphical version,
* or change the binding to a supported one.

Example:

## Emacs hangs
Due to its single-threaded nature, many operations block Emacs. This could happen in a few ways. For example, Emacs may be waiting for input from you (e.g. you have opened the minibuffer in one frame but are trying to work in another). Alternatively, Emacs could be running code that simply takes a while to finish. Or perhaps you have run across a bug. There are several ways of trying to unblock Emacs without killing the Emacs process.

* Try pressing . Depending on what Emacs is doing, you may need to press it multiple times.
* Try pressing .
* From another terminal, run

## Emacs-nox output gets messy
When working in a terminal, the color, indentation, or anything related to the output might become crazy. This is (probably?) because Emacs was sent a special character at some point which may conflict with the current terminal.
If this happens you can do , which will redraw the terminal's display. If this problem happens frequently, you might want to bind the command to a key, e.g. by putting something like:

 (global-set-key (kbd "") 'redraw-display)

in your  file.

Graphical Emacs does not suffer from this issue.

## Weird escaped numbers (utf-8) displaying in emacs terminal
Export these values in your  or :

It can be a source of errors since in Linux distributions the correct values use lowercase utf (e.g. )

To view all available locales use .

## Shift + Arrow keys not working in emacs within tmux
Enable xterm-keys in your tmux configuration:

Because this will break other key combinations, put the following in your emacs config.

See [https://github.com/tmux/tmux/wiki/FAQ#how-do-i-make-modified-function-and-arrow-keys-like-c-up-m-pageup-work-inside-tmux tmux FAQ for details.

## Improper window resizing in KDE
KDE users may observe that the Emacs window does not resize properly, but rather, the resized portion is transparent and mouse clicks are sent to the underlying window. To correct this behavior, change KDE's GTK3 theme to something other than oxygen-gtk. For instance, use the Emacs theme which is included with .

To force Emacs to maximize completely in KDE, click the Emacs icon in the title bar, and select More Actions > Special Window Settings. Then in the Size & Position tab, select Obey geometry restrictions, choose Force in the dropdown menu, and select No from the radio buttons on the right.

## Missing info pages
Sometimes the texinfo dir file can get out of sync and info pages that exist on the system are not available in the info browser. The script below recreates the dir info file, putting all of the system's info pages in it.

    pushd /usr/share/info
    rm -v dir
    for f in *
        do install-info "$f" dir 2>/dev/null
    done
    popd

## Alternatives
There are numerous "smaller" text editors that are, at least on the surface, similar to GNU Emacs. Here are some of them:

*
*
*
*
*
*
*
*
*
*

## Alternative GNU Emacs distributions
An Emacs "distro" is a collection of emacs packages and customizations.  They are easier to install and use than customizing emacs on your own is (but less custom to you).

* Spacemacs - A community-driven Emacs distribution - The best editor is neither Emacs nor Vim, it's Emacs *and* Vim!
* Doom Emacs - An Emacs framework for the stubborn martian hacker
* Witchmacs - The cutest Emacs distribution
* Yukimacs - A GNU/Emacs config built from the ground up (no Spacemacs or Doom Emacs), heavily inspired by Uncle Dave’s Emacs and Witchmacs. It is discouraged now and yukimacs-doom is encouraged instead, which mentioned just below.
* yukimacs-doom - Yukimacs, but Doom.

More: Starter Kits
