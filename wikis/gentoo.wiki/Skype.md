**[] Deprecated article**\
\
As of **2025-08-07**, this article is **deprecated (obsolete)**. Contents are [no longer relevant], and are intended for historical reference only!

Skype abandoned by upstream, package is removed.

\
TLDR: **Do not use this article!**

[[]][Wikipedia](https://en.wikipedia.org/wiki/Skype "wikipedia:Skype")

**Skype** is a proprietary application owned by Microsoft for instant messaging, VoIP calls, and video conversations.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Kernel config]](#Kernel_config)
    -   [[1.2] [USE flags]](#USE_flags)
    -   [[1.3] [Emerge]](#Emerge)
    -   [[1.4] [Additional USE flags]](#Additional_USE_flags)
-   [[2] [Troubleshooting]](#Troubleshooting)
    -   [[2.1] [Auto-launching at KDE login]](#Auto-launching_at_KDE_login)
    -   [[2.2] [No video (despite video drivers being installed/loaded)]](#No_video_.28despite_video_drivers_being_installed.2Floaded.29)
        -   [[2.2.1] [Permissions]](#Permissions)
-   [[3] [See also]](#See_also)

## [Installation]

### [Kernel config]

[KERNEL]

    General setup  --->
        -*- Namespaces support  --->
            [*]   User namespace

\

### [USE flags]

Cannot load package information. Is the atom *net-im/skypeforlinux* correct?

### [Emerge]

Install [[[net-im/skypeforlinux]](https://packages.gentoo.org/packages/net-im/skypeforlinux)[]]:

`root `[`#`]`emerge --ask net-im/skypeforlinux`

### [Additional USE flags]

The following settings will need to be in [/etc/portage/package.accept_keywords/skypeforlinux] or some equivalent.

`root `[`#`]`echo "=net-im/skypeforlinux-8.45.0.41 ~amd64" >> /etc/portage/package.accept_keywords/skypeforlinux`

Edit your pinentry usage in this way.

`root `[`#`]`echo ">=app-crypt/pinentry-1.0.0-r2 gnome-keyring" >> /etc/portage/package.use/pinentry`

and then just install the package.

`root `[`#`]`emerge skypeforlinux`

## [Troubleshooting]

### [Auto-launching at KDE login]

For some reason, [KDE](https://wiki.gentoo.org/wiki/KDE "KDE") cannot remember Skype in the session it saves upon log out. This workaround will fool it into saving Skype in the session.

[FILE] **`~/.kde4/Autostart/skype.sh`**

    #!/bin/sh
    skypeforlinux

To make the Skype main window (but not chat windows) go to a desktop or any other features of Window Rules with KDE, use this regular expression under Window Title in the settings window:

[CODE]

    (^[A-Za-z0-9]+\s\-\s)?Skype™(\s\d+\.\d+)?\s\(Beta\)(\sfor\sLinux)?$

### [][No video (despite video drivers being installed/loaded)]

#### [Permissions]

It is possible, that your user does not have privileges to access video device. Example privileges:

`user `[`$`]`ls -al /dev/video0`

    crw-rw----+ 1 root video 81, 0 Nov 25 22:03 /dev/video0

Add each Skype user to the video group:

`root `[`#`]`gpasswd -a larry video`

Where [larry] is substituted for the appropriate username.

## [See also]

-   [Linphone](https://wiki.gentoo.org/wiki/Linphone "Linphone") --- a SIP soft video/phone program.
-   [Mumble](https://wiki.gentoo.org/wiki/Mumble "Mumble") --- an open source, cross platform, low-latency, high quality voice over IP (VoIP) client.