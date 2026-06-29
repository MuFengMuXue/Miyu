# Julia

Julia is a high-level, high-performance dynamic programming language for numerical computing. It provides a sophisticated compiler, distributed parallel execution, numerical accuracy, and an extensive mathematical function library.

## Installation
You can install one of three packages:

* The  package.
:
*  provides official builds compiled against patched LLVM libs.
*  provides a binary manager, similar to rustup, that allows to use different versions of Julia.

## Troubleshooting
If you get the following error while using  with ,

 WARNING: You are using Matplotlib 0.0.0, which is no longer officialy supported by the Plots community. To ensure smooth Plots.jl integration update your Matplotlib library to a version >= 2.0.0

first install  and . Then, install VersionParsing.jl with  within the Julia promptand restart Julia.

## Integration with editors
## Vim
## Syntax highlighting and more
[https://github.com/JuliaEditorSupport/julia-vim julia-vim

## Linting
The julialint plugin combined with the Lint.jl package can provide linting.

## REPL vim bindings
The VimBindings.jl package provides vim emulation within the Julia REPL.

## Emacs
## Syntax highlighting
julia-emacs.

## Linting
lsp-julia: provides linting using the LSP protocol.

## REPL integration
julia-repl: for interacting with a Julia REPL running inside Emacs.
