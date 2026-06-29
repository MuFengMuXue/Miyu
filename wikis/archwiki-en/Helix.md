# Helix

Helix is a modal text editor written in Rust and inspired by Neovim and Kakoune. It implements changes to the traditional Vim workflow similar to Kakoune's, like selection-based editing and multi-cursor support. Helix bundles and enables many features out of the box. It does have adding custom language support and #Plugins support.

## Installation
Install the  package.

## Configuration
Helix reads an optional  configuration file. See this page of the official documentation for a list of available options.

## Usage
For a basic overview on how to use helix, follow the helix tutorial by running either helix --tutor or :tutor.

## Syntax highlighting
To enable syntax highlighting for many programming languages:
install an lsp
then edit  to include it

## Indentation
Helix will detect the indentation used in the file, or otherwise defaults to the language indentation configured in languages.toml, with a fallback to tabs if it is not specified.

example:

 name = "javascript"
 indent = { tab-width = 4, unit = "    " }

## Using the mouse
helix has the ability to make use of the mouse already set to true by default,
To disable this feature, add this line into :

 mouse = false

## Tips and tricks
## Line numbers
By default absolute line numbers are shown, relative numbers can be enabled with  or in the config .

Jumping to a specific line is possible with  or .

## Spell checking
Helix has the ability to do spell checking, enable by installing a tree-sitter package

## True color support
True color support is enabled by default

## Language Server Protocol
Helix contains a built-in Language Server Protocol client.
To enable it, follow the wiki

See Language Server Protocol for a list of Arch packages.

## Plugins
As of march 2026, the plugin system hasn't been merged into mainline, you can try this fork at .

Adding plugins to Helix can increase your productivity by extending Helix features. Plugins can alter Helix UI, add new commands, enable code completion support, integrate other programs and utilities with Helix, add support for additional languages and more.
