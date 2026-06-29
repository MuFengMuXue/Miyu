# Swift

According to Wikipedia:
: Swift is a general-purpose, multi-paradigm, compiled programming language developed by Apple Inc. and the open-source community. First released in 2014, Swift was developed as a replacement for Apple's earlier programming language Objective-C, as Objective-C had been largely unchanged since the early 1980s and lacked modern language features.

Running Swift-language builds and doing Swift development is possible on Linux.

## Installation
Install  for the released version, which is a repackaged Fedora binary, or  for a native build from source.

For code completion the sourcekit language server protocol, sourcekit-lsp is available, e.g. as plugin to visual studio code, . See below.

## Editing and code completion
Install ,  and make sure that a Swift toolchain providing sourcekit-lsp (e.g.  or ) is installed.

 $ git clone git@github.com:swift-server/vscode-swift.git
 $ cd vscode-swift
 $ npm install
 $ npm run dev-package
 $ code --install-extension swift-lang-*-dev.vsix

## Hello world
The Swift package manager allows to create example programs.

 $ swift package init --type executable
 $ swift run

For a library:

 $ swift package init
 $ swift build

## Read eval print loop, REPL
For details on the swift REPL, see here.
