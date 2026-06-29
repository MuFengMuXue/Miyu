## Name

rofiles-fuse — Use FUSE to create a view where directories are writable, files are immutable

## Synopsis

`rofiles-fuse SRCDIR MNTPOINT`

## Description

Creating a checkout from an OSTree repository by default uses hard links, which means an in-place mutation to any file corrupts the repository and all checkouts. This can be problematic if one wishes to run arbitrary programs against such a checkout. For example, RPM `%post` scripts or equivalent.

In the case where one wants to create a tree commit derived from other content, using **rofiles-fuse** in concert with **ostree commit --link-checkout-speedup** (or the underlying API) can ensure that only new files are checksummed.

## Example: Update an OSTree commit

``` programlisting
# Initialize a checkout and mount
$ ostree --repo=repo checkout somebranch branch-checkout
$ mkdir mnt
$ rofiles-fuse branch-checkout mnt

# Now, arbitrary changes to mnt/ are reflected in branch-checkout
$ echo somenewcontent > mnt/anewfile
$ mkdir mnt/anewdir
$ rm mnt/someoriginalcontent -rf

# Commit and cleanup
$ fusermount -u mnt
$ ostree --repo=repo commit --link-checkout-speedup -b somebranch -s 'Commit new content' --tree=dir=branch-checkout
$ rm mnt branch-checkout -rf
    
```

## See Also

[ostree(1)](man__ostree.md)
