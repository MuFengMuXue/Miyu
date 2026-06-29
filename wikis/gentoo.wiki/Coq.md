**Resources**

[[]][Home](https://coq.inria.fr/)

[[]][Official documentation](https://coq.inria.fr/documentation)

[[]][Package information](https://packages.gentoo.org/packages/sci-mathematics/coq)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Coq "wikipedia:Coq")

[[]][GitHub](https://github.com/coq/coq)

[[]][Bugs (upstream)](https://github.com/coq/coq/issues/)

[[]][[#coq](ircs://irc.libera.chat/#coq)] ([[webchat](https://web.libera.chat/#coq)])

**Coq** is a formal proof management system, for formalizing and machine-checking proof written in [Ocaml](https://en.wikipedia.org/wiki/OCaml "wikipedia:OCaml"). Coq is based on the Calculus of Inductive Constructions.^[\[1\]](#cite_note-1)^ From the official website

> It (Coq, red.) provides a formal language to write mathematical definitions, executable algorithms and theorems together with an environment for semi-interactive development of machine-checked proofs.^[\[2\]](#cite_note-2)^

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Emerge]](#Emerge)
-   [[2] [User interfaces]](#User_interfaces)
    -   [[2.1] [VSCode]](#VSCode)
    -   [[2.2] [Emacs]](#Emacs)
    -   [[2.3] [Vim/Neovim]](#Vim.2FNeovim)
-   [[3] [Further reading]](#Further_reading)

## [Installation]

### [USE flags for] [sci-mathematics/coq](https://packages.gentoo.org/packages/sci-mathematics/coq) [[]] [Coq/Rocq is a proof assistant written in O\'Caml]

  --------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+ocamlopt`](https://packages.gentoo.org/useflags/+ocamlopt)               Enable ocamlopt support (ocaml native code compiler) \-- Produces faster programs (Warning: you have to disable/enable it at a global scale)
  [`debug`](https://packages.gentoo.org/useflags/debug)                       Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`doc`](https://packages.gentoo.org/useflags/doc)                           Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`gui`](https://packages.gentoo.org/useflags/gui)                           Enable support for a graphical user interface
  [`native-compiler`](https://packages.gentoo.org/useflags/native-compiler)   Enable \"native_compute\" and compile the Coq Standard Library
  [`test`](https://packages.gentoo.org/useflags/test)                         Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  --------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-03-31 19:52] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Coq can be installed from the official gentoo repositories.

`root `[`#`]`emerge --ask sci-mathematics/coq`

## [User interfaces]

Coq supports multiple user interfaces, such as VSCode, [Emacs](https://wiki.gentoo.org/wiki/Emacs "Emacs"), [Vim](https://wiki.gentoo.org/wiki/Vim "Vim")/[Neovim](https://wiki.gentoo.org/wiki/Neovim "Neovim") as well as its own [CoqIDE](https://wiki.gentoo.org/index.php?title=CoqIDE&action=edit&redlink=1 "CoqIDE (page does not exist)").

### [VSCode]

Users of Visual Studio Code can use the VsCoq extention which is currently maintained by the coq-community.^[\[3\]](#cite_note-3)^

### [Emacs]

Users of Emacs can use the major Coq mode [Proof General](https://proofgeneral.github.io/) and extend that with the minor Coq mode [Company-Coq](https://github.com/cpitclaudel/company-coq).

### [][Vim/Neovim]

Users of Vim/Neovim can use the [Coqtail](https://github.com/whonore/Coqtail) plugin.

## [Further reading]

For a thorough introduction to logic in Coq see the free e-book [Logical Foundation](https://softwarefoundations.cis.upenn.edu/lf-current/index.html) from the University of Pennsylvania.

1.  [[[↑](#cite_ref-1)] [[https://coq.inria.fr/about-coq](https://coq.inria.fr/about-coq)]]
2.  [[[↑](#cite_ref-2)] [[https://coq.inria.fr/](https://coq.inria.fr/)]]
3.  [[[↑](#cite_ref-3)] [[https://coq.inria.fr/user-interfaces.html](https://coq.inria.fr/user-interfaces.html)]]