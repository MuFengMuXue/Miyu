# Micro

micro is a terminal-based text editor that aims to be easy to use and intuitive, while taking advantage of the full capabilities of modern terminals. It is shipped as a single, static binary with no dependencies.

As the name suggests, micro aims to be a successor to the nano editor, as it is easy to install and use, but micro also strives to be pleasant to use on a daily basis.

## Installation
Install the  package.

## Configuration
Micro uses  or  as its configuration directory. If these variables are not set, it defaults to .
The main settings are defined in the  file. You can find all available options here.

## Syntax highlighting
The colorscheme can be changed via the configuration file or from the micro command line. To do this, press  and type the command

## Plugins
To install a plugin, use the command  inside micro. To remove one, use . The plugin help guide is available by running the command .

## Tips and tricks
## Replace vi with micro
To replace  with  as the default text editor for commands such as visudo, set the  and  environment variables:

 export VISUAL=micro
 export EDITOR=micro
