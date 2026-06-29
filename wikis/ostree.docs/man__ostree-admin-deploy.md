## Name

ostree-admin-deploy — Checkout a revision as the new default deployment

## Synopsis

`ostree admin deploy` \[OPTIONS...\] {REFSPEC}

## Description

Takes a commit or revision REFSPEC, and queues the new deployment as default upon reboot.

## Options

`--stateroot`="STATEROOT"  
Use a different operating system stateroot than the current one.

`--os`="STATEROOT"  
Alias for `--stateroot`.

`--origin-file`="FILENAME"  
Use FILENAME as the origin, which is where OSTree will look for updated versions of the tree.

`--retain`  
Do not delete previous deployment.

`--retain-pending`  
Do not delete pending deployments.

`--retain-rollback`  
Do not delete rollback deployments.

`--not-as-default`  
Append rather than prepend new deployment.

`--lock-finalization`  
The deployment will not be "finalized" by default on shutdown; to later queue it, use `ostree admin lock-finalization --unlock`.

`--karg-proc-cmdline`  
Import current /proc/cmdline.

`--karg`="NAME=VALUE"  
Set kernel argument, like root=/dev/sda1; this overrides any earlier argument with the same name.

`--karg-append`="NAME=VALUE"  
Append kernel argument; useful with e.g. console= that can be used multiple times.

`--karg-delete`="NAME=VALUE"  
Delete kernel argument if exists, can be used multiple times.

## Example

**\$ ostree admin status**

``` programlisting
        * gnome-ostree 67e382b11d213a402a5313e61cbc69dfd5ab93cb07.0
            origin refspec: gnome-ostree/buildmain/x86_64-runtime
          gnome-ostree ce19c41036cc45e49b0cecf6b157523c2105c4de1ce3.0
            origin refspec: gnome-ostree/buildmain/x86_64-runtime
```

**\$ ostree admin deploy gnome-ostree/buildmain/x86_64-runtime**

``` programlisting
        ostadmin: Creating deployment /ostree/deploy/gnome-ostree/deploy/7e382b11d213a402a5313e61cbc69dfd5ab93cb07.1
        ostadmin: Processing /etc: 3 modified, 0 removed, 29 added
        Transaction complete: bootconfig swap: no deployment count change: 0)
```

**\$ ostree admin status**

``` programlisting
          gnome-ostree 67e382b11d213a402a5313e61cbc69dfd5ab93cb07.1
            origin refspec: gnome-ostree/buildmain/x86_64-runtime
        * gnome-ostree 67e382b11d213a402a5313e61cbc69dfd5ab93cb07.0
            origin refspec: gnome-ostree/buildmain/x86_64-runtime
```
