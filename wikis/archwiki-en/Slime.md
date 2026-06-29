# Slime

SLIME (Superior Lisp Interaction Mode for Emacs) provides a development environment for Common Lisp in Emacs. This article assumes that SBCL will be used. It can be replaced with other implementations, e.g. CMUCL, ECL, CLISP.

## Installation
Install  and your preferred Common Lisp implementation. Alternatively, SLIME can be installed via .

## Configuration
To make use of SLIME, add the following lines to your init file:

 (setq inferior-lisp-program "/path/to/lisp-executable")
 (add-to-list 'load-path "/usr/share/emacs/site-lisp/slime/")
 (require 'slime)
 (slime-setup)

Then run  from within emacs.

Alternatively, for a fancier SLIME setup, you can change the above lines to:

 (setq inferior-lisp-program "/path/to/lisp-executable")
 (add-to-list 'load-path "/usr/share/emacs/site-lisp/slime/")
 (require 'slime)
 (slime-setup '(slime-fancy))

## Resources
* The Common Lisp wiki
* Practical Common Lisp
* Structure and Interpretation of Computer Programs
* Paul Graham's Lisp resources.
