# V2Ray

V2Ray is the core tool of Project V, which is mainly responsible for the realization of network protocols and functions, and communicates with other Project V.

## Installation
Install the  package.

## Configuration
V2Ray configuration is done with a JSON formatted file. See Config Reference. There are several methods of configuration, please visit V2Ray Beginner's Guide for detail.

## Usage
## From the command line
V2Ray is started with the  command. Run  and  to see its command line help.

## Service management
Start/enable .

## Tips and tricks
## Routing rules
See Routing of V2Ray.

The preset routing rule files are  and  in . They are provided by the  and  packages respectively. These two packages are installed by default as dependencies of .

## Replacing the preset routing rule files
There are ready-made packages for some routing rule files. For example, you can install the  package for @Loyalsoldier/v2ray-rules-dat.

For routing rule files without ready-made packages, you can create packages and install or remove  and  without removing the dependent package and put the routing rule files in the  directory.

## Multiple configs
With multiple configs, it's convenient to achieve things like dropping new inbounds to the config directory without having to touch the master config.

## Rules of multiple configs
* For top-level objects, objects in the latter config file override or supplement the former.
* Inbounds and outbounds are array structures, they have special rules:
** If arrays in the latter config file have 2 or more elements, arrays in the latter config file overwrite the former config file.
** If arrays in the latter config file have only 1 element, overwrite the original element with the same tag; if the element cannot be found:
*** For inbounds, add them to the end.
*** For outbounds, add them to the front; if the name of config file contains , add the outbounds to the end.

## Enable multiple configs with systemd
To enable multiple configs with systemd, you can create the following drop-in file:

## Troubleshooting
## Failed with result 'exit-code'
If you see this error in the log: , it is because V2Ray does not have write permission to /var/log/v2ray/access.log. Use the following command to solve the problem.
 chown -R nobody /var/log/v2ray
