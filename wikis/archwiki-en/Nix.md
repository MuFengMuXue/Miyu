# Nix

Nix is a purely functional package manager that aims to make package management reproducible, declarative and reliable.

## Installation
Install the  package.

## Configuration
To have the Nix daemon launched at boot time, enable .

Add a channel and update it.

 $ nix-channel --add https://channels.nixos.org/nixpkgs-unstable
 $ nix-channel --update

## Usage
With the shell configured, the following should install hello into your updated PATH:

 $ nix-env -iA nixpkgs.hello

The binary itself will be located at .

Run  and make sure it is in the right PATH. If it works, you can remove it:

 $ nix-env --uninstall hello

Or you can check the list of installed programs:

 $ nix-env --query

You can also list generations:

 $ nix-env --list-generations

See  for more detailed information.

## Tips and tricks
## Declarative management of software installation and configuration
Home Manager provides a system for managing a user environment with Nix.

It lets you
* install software declaratively in your user profile, rather than using
* manage dotfiles in the home directory of your user.

See Home Manager Manual and the Nixos Wiki page for the installation and configuration guide.

## Max jobs
By default, nix only uses one builder. The following will allow nix to use as many jobs as the number of CPUs:

## Graphical acceleration
To run OpenGL and Vulkan applications, use NixGL.

## Desktop integration
For integrating Nix applications with your desktop environment, add the  directory to your , for instance using .

## Zsh integration for nix-shell
 starts Bash by default.  lets you use Zsh as the default shell in a  environment. Some prompt plugins such as  and  provide a  indicator.

## Command completion
## Zsh
 provides Zsh completions for nix commands such as  and .

## Troubleshooting
## Too many open files
Some builds may run into an error such as:

 error: opening directory '/nix/store/...': Too many open files

Edit  and increase the file limit:

 LimitNOFILE=65536

## Warning message about root user channels
If you get this error while using Nix:

 warning: Nix search path entry '/nix/var/nix/profiles/per-user/root/channels' does not exist, ignoring

The root user will need to update their channels:

 # nix-channel --update

## Sandbox build issues
## Other sandbox issues
The issue is known upstream: [https://github.com/NixOS/nix/issues/2311 #2311, #3000, and #4636.

The most common fix is to disable sandboxing in the configuration file:

Then restart the .

## Locale warnings
The Nixos wiki recommends running . Alternatively, export the environment variable .
