# NAME

projects - persistent project root definition

# DESCRIPTION

The */etc/projects* file provides a mapping between numeric project identifiers and those directories which are the roots of the quota tree. Its format is simply:


    # comments are hash-prefixed
    # ...
    10:/export/cage
    42:/var/log

The */etc/projects* file is optional, instead **xfs_quota**(8) can be used with the **-p** argument to specify a project root directly for each operation.

# SEE ALSO

**xfs_quota**(8), **xfsctl**(3), **projid**(5).
