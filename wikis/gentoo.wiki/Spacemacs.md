**Resources**

[[]][Home](http://spacemacs.org/)

[[]][GitHub](https://github.com/syl20bnr/spacemacs)

**Spacemacs** is a sophisticated and polished Emacs set-up focused on ergonomics, mnemonics and consistency.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge Emacs]](#Emerge_Emacs)
    -   [[1.3] [Download and install Spacemacs]](#Download_and_install_Spacemacs)
-   [[2] [Configuration file]](#Configuration_file)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Invocation]](#Invocation)
-   [[4] [See also]](#See_also)
-   [[5] [References]](#References)

## [Installation]

Spacemacs is basically a distribution for Emacs packages - it configures and combines them for a great out-of-box experience.

The installation is done by cloning the Spacemacs configuration files git repository to [\~/.emacs.d/]

First, install [GNU Emacs](https://wiki.gentoo.org/wiki/GNU_Emacs "GNU Emacs") with the correct USE flags:

### [USE flags]

Ensure Emacs is built with the `xft` USE flag^[\[1\]](#cite_note-1)[\[2\]](#cite_note-2)^:

[FILE] **`/etc/portage/package.use`**

    app-editors/emacs xft

### [Emerge Emacs]

Install Emacs, or reinstall if USE flags have been changed:

`root `[`#`]`emerge --ask app-editors/emacs`

### [Download and install Spacemacs]

Spacemacs is installed by cloning a git repository containing Emacs configuration.

First, backup or delete any old configuration files [\~/.emacs.d] and [\~/.emacs], if they already exist:

`user `[`$`]`mv ~/.emacs.d ~/.emacs.d.bak-$(date +%FT%T)`

`user `[`$`]`mv ~/.emacs ~/.emacs.bak-$(date +%FT%T)`

Now that old configs are out of the way, clone the Spacemacs git repository into [\~/.emacs.d]:

`user `[`$`]`git clone https://github.com/syl20bnr/spacemacs ~/.emacs.d`

To finish installing Spacemacs, start Emacs (via menu, a [launcher](https://wiki.gentoo.org/wiki/Recommended_applications#Application_launchers "Recommended applications") or terminal) and follow the install prompt at the bottom of the screen:

`user `[`$`]`emacs`

** Note**\
Once installation has finished, there may be quite a bit of information from the install logs still showing. The simplest thing, when starting off, may be to close Spacemacs and relaunch by following the next section.

## [Configuration file]

Custom configuration and features can be set in the file [\~/.spacemacs], written in [Elisp](https://wiki.gentoo.org/index.php?title=Elisp&action=edit&redlink=1 "Elisp (page does not exist)").

To directly open this file in Spacemacs, press the keys [ESC] -\> [SPACE f e d].

As Emacs (and Spacemacs) is self-documenting, learn about possible configuration options by pressing [SPC h SPC].

## [Usage]

### [Invocation]

Because Spacemacs replaces the main Emacs configuration, by default, simply launch Emacs to open Spacemacs:

`user `[`$`]`emacs`

## [See also]

-   [Emacs](https://wiki.gentoo.org/wiki/Emacs "Emacs") --- a class of powerful, extensible, self-documenting text editors.
-   [Knowledge Base:Edit a configuration file](https://wiki.gentoo.org/wiki/Knowledge_Base:Edit_a_configuration_file "Knowledge Base:Edit a configuration file")
-   [Text editor](https://wiki.gentoo.org/wiki/Text_editor "Text editor") --- a program to create and edit text files.

## [References]

1.  [[[↑](#cite_ref-1)] [Konstantinos Tsardounis. [Unable to use Source Code Pro fonts?](https://github.com/syl20bnr/spacemacs/issues/10162), [Spacemacs GutHub](https://github.com/syl20bnr/spacemacs), January 16th, 2018. Retrieved on March 19th, 2019.]]
2.  [[[↑](#cite_ref-2)] [Wiki authors. [Xft support for GNU Emacs](https://wiki.gentoo.org/wiki/Xft_support_for_GNU_Emacs "Xft support for GNU Emacs"), [Gentoo Wiki](https://wiki.gentoo.org/wiki/Main_Page "Main Page"), July 11th, 2013. Retrieved on March 19th, 2019.]]