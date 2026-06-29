# Ledger

Ledger is a powerful, double-entry accounting system that is accessed from the UNIX command-line. Ledger, begun in 2003, is written by John Wiegley and released under the BSD license.

## Installation
There are several ports of ledger to various languages. Install one of:

* : the original implementation,
* : a port to haskell, which is also popular.

## Usage
The online documentation contains a tutorial to help new users get started.

Emacs users may be interested in using ledger-mode. ledger-mode is available on MELPA and comes with info, accessible via .

## Tips and tricks
## Assign commodity during ledger convert
By default, ledger does not assign a commodity when it converts from csv files to ledger format. To have it assign a currency when one is missing, you can make a currency the default commodity of a ledger file by adding something like this to the file:
