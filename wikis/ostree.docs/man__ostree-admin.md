## Name

ostree-admin — Use one of the ostree admin commands

## Synopsis

`ostree admin` {SUBCOMMAND}

## Description

Use ostree admin subcommands.

## Subcommands

- **cleanup**

- **config-diff**

- **deploy**

- **init-fs**

- **instutil**

- **os-init**

- **pin**

- **post-copy**

- **set-origin**

- **status**

- **switch**

- **undeploy**

- **unlock**

- **upgrade**

View manpages for each admin subcommand using, for example:

**\$ man ostree-admin cleanup**

## Options

`--help`, `-h`  
Usage help

`--sysroot`="PATH"  
Creates a new OSTree sysroot at PATH

`--print-current-dir`  
Prints the full path to the deployment directory for the currently active deployment in the specified sysroot to standard out. This is incompatible with specifying a subcommand.
