# pam_namespace_helper(8)

## Name
pam_namespace_helper — Helper binary that creates home directories

## Synopsis
```
pam_namespace_helper
```

## DESCRIPTION

*pam_namespace_helper* is a helper program for the *pam_namespace* module that sets up a private namespace for a session with polyinstantiated directories. The helper ensures that the namespace mount points exist before they are started to be used for the polyinstantiated directories. Mount points for home directories (lines with \$HOME) are not created.

*pam_namespace_helper* should be run by systemd at system startup. It should also be run by the administrator after defining the polyinstantiated directories but before enabling them.

## SEE ALSO

`pam_namespace(8)`
