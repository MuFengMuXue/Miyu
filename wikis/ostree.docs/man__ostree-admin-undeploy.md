## Name

ostree-admin-undeploy — Delete deployment at a given index

## Synopsis

`ostree admin undeploy` {INDEX}

## Description

Deletes the deployment at INDEX. INDEX must be in range and not reference the currently booted deployment.

## Example

**\$ ostree admin status**

``` programlisting
        * gnome-ostree 67e382b11d213a402a5313e61cbc69dfd5ab93cb07.0
            origin refspec: gnome-ostree/buildmain/x86_64-runtime
          gnome-ostree ce19c41036cc45e49b0cecf6b157523c2105c4de1c.0
            origin refspec: gnome-ostree/buildmain/x86_64-runtime
```

**\$ ostree admin undeploy 1**

``` programlisting
        Transaction complete; bootconfig swap: no deployment count change: -1)
        Freed objects: 326.5 kB
        Deleted deployment ce19c41036cc45e49b0cecf6b157523c2105c4de1c.0
```

**\$ ostree admin status**

``` programlisting
        * gnome-ostree 67e382b11d213a402a5313e61cbc69dfd5ab93cb07.0
            origin refspec: gnome-ostree/buildmain/x86_64-runtime
```
