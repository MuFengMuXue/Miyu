**Resources**

[[![Gentoo peach graphic](/images/thumb/a/ad/Gentoo-logo-peach.svg/25px-Gentoo-logo-peach.svg.png)](https://wiki.gentoo.org/wiki/Project:Emacs "Project:Emacs")][Project](https://wiki.gentoo.org/wiki/Project:Emacs "Project:Emacs")

[[]][Wikipedia](https://en.wikipedia.org/wiki/Emacs "wikipedia:Emacs")

**Emacs** denominates a class of powerful, extensible, self-documenting text editors. The original implementation was written in 1976 as a set of "**E**ditor **Mac**ro**s**" for the TECO editor. One of the most widely used variants today is [GNU Emacs](https://wiki.gentoo.org/wiki/GNU_Emacs "GNU Emacs").

## Contents

-   [[1] [Available software]](#Available_software)
-   [[2] [Ebuild repository]](#Ebuild_repository)
-   [[3] [See also]](#See_also)
-   [[4] [External resources]](#External_resources)

## [Available software]

There are a number of implementations of Emacs, often lightweight versions, many of which are available in Gentoo. Some of these projects may be feature-complete, without recent releases.

  --------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------
  Name                                                                  Package                                                                                                                                                                                                                                                                                                                                                                                                         Description
  e3                                                                    [[[app-editors/e3]](https://packages.gentoo.org/packages/app-editors/e3)[]]                                                Very tiny editor in ASM with emacs, pico, wordstar, and vi keybindings. Heavily optimized for size and independent of libc or any other libraries.
  EmACT                                                                 [[[app-editors/emact]](https://packages.gentoo.org/packages/app-editors/emact)[]]                                       Fork of Conroy\'s MicroEmacs. Last release in 2009 (as of 2021).
  Ersatz Emacs                                                          [[[app-editors/ersatz-emacs]](https://packages.gentoo.org/packages/app-editors/ersatz-emacs)[]]                  Very minimal imitation of the famous GNU Emacs editor. Last release in 2006 (as of 2021).
  fe                                                                    [[[app-editors/fe]](https://packages.gentoo.org/packages/app-editors/fe)[]]                                                Small and easy to use folding editor with an emacs-like interface. Last release seems to be from 2011 (as of 2021).
  **[GNU Emacs](https://wiki.gentoo.org/wiki/GNU_Emacs "GNU Emacs")**   **[[[app-editors/emacs]](https://packages.gentoo.org/packages/app-editors/emacs)[]]**                                   Powerful, extensible, self-documenting text editor released by the Free Software Foundation. Most popular version of Emacs.
  Hemlock                                                               [[[dev-lisp/cmucl]](https://packages.gentoo.org/packages/dev-lisp/cmucl)[]]                                                Emacs-like editor implemented in Common Lisp with CMUCL, a free implementation of the Common Lisp programming language.
  Jasspa\'s MicroEmacs                                                  [[[app-editors/jasspa-microemacs]](https://packages.gentoo.org/packages/app-editors/jasspa-microemacs)[]]   Emacs editor biased towards UNIX users with a small footprint. Last release in 2009 (as of 2021).
  JED                                                                   [[[app-editors/jed]](https://packages.gentoo.org/packages/app-editors/jed)[]]                                             Powerful editor with emulation of GNU Emacs, among others. Last release in 2009 (as of 2021).
  JEmacs                                                                [[[dev-scheme/kawa]](https://packages.gentoo.org/packages/dev-scheme/kawa)[]]                                             Re-implementation of Emacs, written in a mix of Java, Scheme, and Emacs Lisp that uses Kawa to compile Scheme and ELisp into Java bytecodes.
  JOE                                                                   [[[app-editors/joe]](https://packages.gentoo.org/packages/app-editors/joe)[]]                                             ASCII-Text Screen Editor for UNIX that has some of the key bindings and many of the powerful features of Emacs.
  Jove                                                                  [[[app-editors/jove]](https://packages.gentoo.org/packages/app-editors/jove)[]]                                          Compact, powerful, Emacs-style text-editor. No official release since 1996, but improvements and modifications have been published since.
  µEmacs/PK                                                             [[[app-editors/uemacs-pk]](https://packages.gentoo.org/packages/app-editors/uemacs-pk)[]]                           Enhanced version of MicroEMACS.
  mg                                                                    [[[app-editors/mg]](https://packages.gentoo.org/packages/app-editors/mg)[]]                                                Small, fast, and portable editor for people who can\'t (or don\'t want to) run real Emacs for one reason or another.
  Ng                                                                    [[[app-editors/ng]](https://packages.gentoo.org/packages/app-editors/ng)[]]                                                Emacs like micro editor Ng, based on mg2a. Latest version is beta from 2003.
  QEmacs                                                                [[[app-editors/qemacs]](https://packages.gentoo.org/packages/app-editors/qemacs)[]]                                    Very small but powerful text editor with an Emacs look and feel, and common features. Latest release seems to be from 2013 (as of 2021).
  [XEmacs](https://wiki.gentoo.org/wiki/XEmacs "XEmacs")                [[[app-editors/xemacs]](https://packages.gentoo.org/packages/app-editors/xemacs)[]]                                    Highly customizable open source text editor and application development system. No longer maintained.
  Zile                                                                  [[[app-editors/zile]](https://packages.gentoo.org/packages/app-editors/zile)[]]                                          Text editor development kit that comes with an example implementation of a lightweight Emacs clone.
  --------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------

## [Ebuild repository]

The [Emacs project](https://wiki.gentoo.org/wiki/Project:Emacs "Project:Emacs") runs an [ebuild repository](https://wiki.gentoo.org/wiki/Ebuild_repository "Ebuild repository") for GNU Emacs and XEmacs (see [Project:Emacs/Overlay](https://wiki.gentoo.org/wiki/Project:Emacs/Overlay "Project:Emacs/Overlay")) which contains a number of packages including many VCS builds. To add the repository:

`root `[`#`]`eselect repository enable emacs`

`root `[`#`]`emerge --sync emacs`

Many more Emacs related packages should now be available for installation.

## [See also]

-   [Knowledge Base:Edit a configuration file](https://wiki.gentoo.org/wiki/Knowledge_Base:Edit_a_configuration_file "Knowledge Base:Edit a configuration file")
-   [Text editor](https://wiki.gentoo.org/wiki/Text_editor "Text editor") --- a program to create and edit text files.

## [External resources]

-   [GNU Emacs Reference Card](https://www.gnu.org/software/emacs/refcards/pdf/refcard.pdf) (PDF).
-   [Emacs: The Editor for the Next Forty Years](https://media.emacsconf.org/2019/26.html) by Perry E. Metzger (video).