# mkhomedir_helper(8)

## Name
mkhomedir_helper — Helper binary that creates home directories

## Synopsis
```
mkhomedir_helper user umask path-to-skel home_mode path-to-vendor-skel
```

## DESCRIPTION

*mkhomedir_helper* is a helper program for the *pam_mkhomedir* module that creates home directories and populates them with contents of the specified skel directory.

The default value of \<umask\> is 0022 and the default value of \<path-to-skel\> is */etc/skel*. The default value of \<home_mode\> is computed from the value of \<umask\>.

\<path-to-vendor-skel\> doesn't have default value. When set to a *path*, home directory will be populated by contents of \<path-to-skel\> first, and then by contents of *path*.

The helper is separated from the module to not require direct access from login SELinux domains to the contents of user home directories. The SELinux domain transition happens when the module is executing the *mkhomedir_helper*.

The helper never touches home directories if they already exist.

## SEE ALSO

`pam_mkhomedir(8)`
