**[] Deprecated article**\
\

This article is **deprecated (obsolete)**. Contents are [no longer relevant], and are intended for historical reference only!

\
TLDR: **Do not use this article!**

** Important**\
[split-usr] configurations are no longer typical and can cause issues. It is recommended to migrate [split-usr] system to [merged-usr] profile.

The [split-usr] or [split [/usr]] layout refers to the legacy layout, where [/bin], [/sbin], [/lib], and [/lib64] are independent directories, separate from [/usr/bin], [/usr/sbin], [/usr/lib] and [/usr/lib64]. The opposite (now typical) configuration is the [merged-usr] layout, where the contents of the directories under [/] are migrated to [/usr] and the directories are replaced with symlinks to their [/usr] counterparts.

Splitting binaries and libraries between root and [/usr] was historically common to enable spreading disk usage across multiple drives. With modern disk sizes and file systems, this is not typically an issue.

In modern systems, [split-usr] can cause incompatibility issues, e.g. when a script calls on [/bin/bash] when bash is located under [/usr/bin/bash] or the inverse. Starting from systemd-255, [merged-usr] layout is **mandatory** for systemd [profiles](https://wiki.gentoo.org/wiki/Profile_(Portage) "Profile (Portage)")^[\[1\]](#cite_note-1)^.

## Contents

-   [[1] [Quirks]](#Quirks)
    -   [[1.1] [elogind with Dracut]](#elogind_with_Dracut)
-   [[2] [See also]](#See_also)
-   [[3] [References]](#References)

## [Quirks]

### [elogind with Dracut]

The path to fully support [elogind on Dracut](https://wiki.gentoo.org/wiki/Dracut#Elogind "Dracut") with [split-usr] layout starting from sys-auth/elogind-255.5 is:

[FILE] **`/etc/dracut.conf.d/elogind.conf`**

    install_items+=" /usr/lib/elogind/elogind-uaccess-command "

## [See also]

-   [Merge-usr](https://wiki.gentoo.org/wiki/Merge-usr "Merge-usr") --- a script which may be used to migrate a system from the legacy \"[split-usr]\" layout to the newer \"merged-usr\" layout as well as the \"sbin merge\".

## [References]

1.  [[[↑](#cite_ref-1)] [[/usr merge for systemd users](https://www.gentoo.org/support/news-items/2022-12-01-systemd-usrmerge.html)]]