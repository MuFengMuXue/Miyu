# Lean

The Lean theorem prover is a proof assistant developed principally by Leonardo de Moura at Amazon. The Lean mathematical library—mathlib—is a community-driven effort to build a unified library of mathematics formalized in the Lean proof assistant.

## Installation
## Lean 4 using elan
elan is a tool to manage installs of the Lean theorem prover. It facilitates maintaining several concurrent versions of Lean.

In addition, as Lean 4 is under heavy development, using it often requires installing nightly builds, which is made easy using elan.

elan installs Lean in subdirectories of , and does not require root access.

Install the  package.

To install the latest stable version of Lean 4, use

 $ elan toolchain install leanprover/lean4:stable

However, many applications (including using mathlib4) require development versions of Lean 4. For instance, the build of Lean that mathlib4 is using can be found in the file To install the desired build, run

 $ elan toolchain install leanprover/lean4:build

where  should be replaced with the desired build.

The installed versions of Lean can be listed with

 $ elan show

and a default can be selected with

 $ elan default build

When using Lean 4, the default build can be overridden for a given project by -ing to the project directory and creating a file

Replace  with the appropriate build identifier.

To get the path to an executable in the current Lean build, use

 $ elan which name_of_executable

## Lean 3 via the AUR
Install  or .

To install mathlib, you must first install , which will install 'leanproject'.

To install mathlib, you must create a Lean project:

 $ cd /path/to/project
 $ leanproject new name_of_project

which will download mathlib to .

## Project management
In this section, we will describe how to create and contribute to Lean 4 projects, including mathlib4.

## Structure of a project
A Lean 4 project will contain several files that are used to manage the project.
* : contains information on how to build the project, as well as a list of dependencies.
* : a single-line file specifying the build to be used for the project.
* : an automatically generated file that contains information on the specific version of each of the installed dependencies. If you have a  file, running  will download the versions of the dependencies specified in . This is useful to avoid incompatible dependency versions.
*  (or, in earlier versions of Lean 4, ): this is where dependencies are installed.
* : directory where built files are stored.
* Lean files, containing the Lean code.

## Creating a project
To create a project, install elan and a Lean build, as described in the Lean 4 using elan section above.
Next, run
 $ lake new path/to/project
This will create a default  and  file.

This will not download mathlib, which you may want to do. [https://github.com/leanprover-community/mathlib4 Mathlib is the official math library of the Lean project, and contains a lot of definitions, lemmas and theorems that you may need for your project. If you want to add mathlib to your project, you must add it as a dependency in the lakefile. See below for details.

## Managing a project
If you are working with an existing project, for instance one you have downloaded from the internet (e.g. github), you do not need to install Lean separately, as long as you have elan installed, see the Lean 4 using elan section above. As long as the appropriate  file is present in the project, you can simply run
 $ lake update
which will download the required version of Lean, as well as all the dependencies for the project.

Dependencies can be added by editing the  file.
For example, to add mathlib as a dependency, add the following

to . Next run
 $ curl https://raw.githubusercontent.com/leanprover-community/mathlib4/master/lean-toolchain -o lean-toolchain
 $ lake update
to download mathlib, and
 $ lake exe cache get
to download the pre-compiled library (see section Caches and oleans below).

## Contributing to Mathlib
If you wish to participate in the ongoing effort to formalize much of mathematics, you may want to make contributions to Mathlib, which is the official math library of the Lean project.

To do so, you will first need to download mathlib:
 $ git clone https://github.com/leanprover-community/mathlib4.git
and  to the downloaded directly and run
 $ lake update
 $ lake exe cache get

If you wish to submit your work, you will need to get a branch on the mathlib Git server, and submit a pull request. To get a branch, contact the community on the leanprover Zulip chat, introduce yourself and your project, and ask for a branch.

## Automatically generating documentation
It is possible to automatically generate documentation, in the same style as the mathlib documentation. This is done using the doc-gen4 package. To install it, add it to your :

(the  part of the code ensures that the doc can only be built when running  with , as below, so as to avoid generating the doc when merely trying to build the package) and download it:
 $ lake -Kenv=dev update
The documentation can be generated using
 $ lake -Kenv=dev build NameOfProject:docs
where NameOfProject should be replaced by the name of your project. This will generate the documentation and place it in the  directory. You can then navigate through the documentation by opening  in a browser.

The documentation also includes a search function. To search for a term in the documentation, use
 file:///path/to/doc/find/index.html?pattern='search_term'#doc

## Text editors
## Using Lean with Emacs
## Install lean-mode
To use Lean with emacs, you must install the lean4-mode package which is currently not available on MELPA and must be installed manually (there is also the lean3-mode package for lean3).

## Automatic unicode input
Lean uses unicode symbols as part of its language.
 can handle this input easily by translating standard text to unicode characters, for instance, typing  will resolve to the unicode character .
To do this, the  input method needs to be selected.
This can be done automatically by adding the following to your Emacs configuration file:

## Viewing goal in separate buffer
Keeping track of the "goal" is very useful when writing proofs in Lean.
The goal can be seen directly in emacs using the  keybinding, which will open a new buffer in which the goal is shown.
This buffer can also be opened automatically when editing a  file by adding:

to your Emacs configuration file.

## Using Lean with Neovim
## Install lean.nvim
To use Lean with Neovim, you must install the lean.nvim plugin. This can be done easily using vim-plug byadding the following to your Neovim Configuration file:

open nvim, and type

 :PlugInstall

If you are using Lean 3, you will also need to install . (The language server is built into Lean 4, so it is not necessary for Lean 4 installs).

Next, create a configuration file at :

{{hc|$XDG_CONFIG_HOME/nvim/plugin/lean.lua|require('lean').setup{
 abbreviations  { builtin  true },
 mappings  true,
}
}}

 enables abbreviating unicode characters, and  enables a number of useful keybindings, see https://github.com/Julian/lean.nvim/ for a full list.
More configuration options are available at https://github.com/Julian/lean.nvim/.

## Tips and tricks
## Caches and oleans
In order to use the theorems and lemmas in mathlib, mathlib needs to be built (i.e. compiled).
This is a long process.
To avoid this, the mathlib community provides a repository of pre-compiled mathlib files (also called "oleans").
To download them using Lean 4, use

 $ lake exe cache get

and using Lean 3, use

 $ leanproject get-cache

## Documentation
A good resource to learn theorem proving in Lean 4 is Of particular note, a succinct "cheatsheet" for useful commands for theorem proving in Lean 4 is available from [https://leanprover-community.github.io/papers/lean-tactics.pdf.

The documentation for mathlib in Lean 4 is available at Since the documentation is still rather sparse, it is often more productive to address questions to the lean community directly.
The most popular forum for this is the [https://leanprover.zulipchat.com leanprover Zulip chat.
