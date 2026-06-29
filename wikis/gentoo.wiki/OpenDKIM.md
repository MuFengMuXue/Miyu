## Contents

-   [[1] [Sharing a local socket with the MTA]](#Sharing_a_local_socket_with_the_MTA)
    -   [[1.1] [Background]](#Background)
    -   [[1.2] [Solution]](#Solution)
    -   [[1.3] [Example]](#Example)
        -   [[1.3.1] [The new way]](#The_new_way)
        -   [[1.3.2] [The old way]](#The_old_way)

## [Sharing a local socket with the MTA]

### [Background]

Using a local socket to communicate *securely* with an MTA requires some subtle configuration. The four security goals achieved are:

1.  Allow OpenDKIM to read the DKIM signing keys.
2.  Allow the MTA to read and write to a shared socket file.
3.  Do **not** allow the MTA to read the DKIM signing keys.
4.  Don\'t allow anyone other than [root] to modify the signing keys.

In recent versions of [[[mail-filter/opendkim]](https://packages.gentoo.org/packages/mail-filter/opendkim)[]], the opendkim daemon runs as the [opendkim] user and group. The signing keys should be,

1.  Located under [/var/lib/opendkim]
2.  Owned by [root], with group [opendkim]
3.  Have mode 640

Taken together, these imply that the [opendkim] group (including the daemon) can read the DKIM signing keys, but not write to them. The problem of the socket is now, essentially: how to share the socket file between the [opendkim] user and the MTA, without allowing the MTA to read the [opendkim] group\'s files? The usual approach here would be to add the MTA to the [opendkim] group, and then allow that group to write to the socket file. However, doing so would allow the MTA to read the DKIM signing keys in this case, and that violates one of our security goals.

### [Solution]

The solution to this problem is to create a new, dedicated group that is used only to control access to the socket. For example, you might

1.  Create a new [dkimsocket] group.
2.  Add the [opendkim] user to the [dkimsocket] group.
3.  Add the MTA to the [dkimsocket] group.
4.  Change the umask in [/etc/opendkim/opendkim.conf] to allow group-write.

This **almost** does what we want, except for one critical pitfall: the socket gets created by the [opendkim] user, and as a result, it gets created with that user\'s primary group, [opendkim]. Since the socket\'s group isn\'t [dkimsocket], our trick has failed! However, all is not lost: we can **change the primary group of the [opendkim] user to [dkimsocket]**, after which the socket will be created with the correct group. With this one crucial modification, everything works as desired.

### [Example]

Below is a step-by-step example of sharing a local socket with Postfix, running as the [postfix] user.

First, edit [/etc/opendkim/opendkim.conf] to specify the name of a local socket. On Gentoo, the local socket should be located under [/run/opendkim], because the permissions on that directory are set correctly at boot time.

[FILE] **`/etc/opendkim/opendkim.conf`**

    #Socket        inet:8891@localhost
    Socket         local:/run/opendkim/opendkim.sock

Then, ensure that the UMask is set correctly in [/etc/opendkim/opendkim.conf] (the ebuild does this on install) so that the socket gets created with group-writable permissions:

[FILE] **`/etc/opendkim/opendkim.conf`**

    UMask 0117

Finally, create and configure the dedicated [dkimsocket] group. [GLEP 81](https://www.gentoo.org/glep/glep-0081.html) changed the way that users and groups are managed on Gentoo.

#### [The new way]

In a local overlay, create an ebuild for the [dkimsocket] group:

[FILE] **`acct-group/dkimsocket/dkimsocket-0.ebuild`**

    # Copyright 1999-2019 Gentoo Authors
    # Distributed under the terms of the GNU General Public License v2

    EAPI=8

    inherit acct-group
    DESCRIPTION="Group used to share the OpenDKIM socket"

    # If you want this to persist across multiple machines, pick a real number!
    ACCT_GROUP_ID="-1"

Then, create newer revisions of the [postfix] and [opendkim] user ebuilds that make use of the new group:

[FILE] **`acct-user/postfix/postfix-0-r4.ebuild`**

    # Copyright 2019 Gentoo Authors
    # Distributed under the terms of the GNU General Public License v2

    EAPI=8

    inherit acct-user

    DESCRIPTION="user for postfix daemon"
    ACCT_USER_ID=207
    ACCT_USER_GROUPS=( postfix mail dkimsocket )

    acct-user_add_deps

[FILE] **`acct-user/opendkim/opendkim-0-r4.ebuild`**

    # Copyright 2019 Gentoo Authors
    # Distributed under the terms of the GNU General Public License v2

    EAPI=8

    inherit acct-user

    DESCRIPTION="User for OpenDKIM"

    ACCT_USER_ID=334
    # dkimsocket goes first, to make it the primary group
    ACCT_USER_GROUPS=( dkimsocket opendkim )

    acct-user_add_deps

Now those two packages will take precedence over the ones in ::gentoo, ensuring that the users on the system are a member of [dkimsocket].

#### [The old way]

Create the [dkimsocket] that will control access to the socket, and add the [postfix] user to it:

`root `[`#`]`groupadd dkimsocket `

`root `[`#`]`usermod --append --groups dkimsocket postfix `

Next, **switch** the primary group of the [opendkim] user to [dkimsocket], and then *append* the [opendkim] group back:

`root `[`#`]`usermod --gid dkimsocket opendkim `

`root `[`#`]`usermod --append --groups opendkim opendkim `

With that, OpenDKIM is ready to start.