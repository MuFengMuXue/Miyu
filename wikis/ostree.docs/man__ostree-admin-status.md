## Name

ostree-admin-status — List deployments

## Synopsis

`ostree admin status`

## Description

Lists the deployments available to be booted into. Includes osname, the checksum followed by the deploy serial, and the refspec. An asterisk indicates the current booted deployment.

## Options

`--sysroot`="PATH"  
Create a new OSTree sysroot at PATH

`-V, --verify`  
Print the commit verification status

`--json`  
Output in JSON format.

`-S, --skip-signatures`  
Skip signatures in output

`-D, --is-default`  
Output the string `default` if the default deployment is the booted one, `not-default` if we are booted in a non-default deployment (e.g. the user interactively chose a different entry in the bootloader menu, or the bootloader rolled back automatically, etc.). If we are not in a booted OSTree system, an error is returned.

`-v, --verbose`  
Print debug information during command processing

`--version`  
Print version information and exit

## Example

**\$ ostree admin status**

``` programlisting
        * gnome-ostree 67e382b11d213a402a5313e61cbc69dfd5ab93cb07.0
            origin refspec: gnome-ostree/buildmain/x86_64-runtime
          gnome-ostree ce19c41036cc45e49b0cecf6b157523c2105c4de1c.0
            origin refspec: gnome-ostree/buildmain/x86_64-runtime
```
