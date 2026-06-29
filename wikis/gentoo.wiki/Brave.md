[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Brave&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://brave.com/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Brave_(web_browser) "wikipedia:Brave (web browser)")

[[]][GitHub](https://github.com/brave/brave-browser)

**Brave** is a web browser focused on privacy, blocking trackers, and advertisements.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Prerequisites]](#Prerequisites)
    -   [[1.2] [Set Portage to use the Brave ebuild repository]](#Set_Portage_to_use_the_Brave_ebuild_repository)
    -   [[1.3] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Screensharing with Pipewire]](#Screensharing_with_Pipewire)
    -   [[2.2] [Using Wayland backend]](#Using_Wayland_backend)
    -   [[2.3] [Policies]](#Policies)
-   [[3] [See also]](#See_also)
-   [[4] [References]](#References)

## [Installation]

### [Prerequisites]

The following must be installed in order for the rest of this article to work properly: [[[app-eselect/eselect-repository]](https://packages.gentoo.org/packages/app-eselect/eselect-repository)[]] and [[[dev-vcs/git]](https://packages.gentoo.org/packages/dev-vcs/git)[]].

Skip the rest of this section if they are already installed.

Install required software:

`root `[`#`]`emerge --ask app-eselect/eselect-repository dev-vcs/git`

### [Set Portage to use the Brave ebuild repository]

Issue the [command](https://wiki.gentoo.org/wiki/Eselect/Repository "Eselect/Repository") to configure the [another-brave-overlay](https://github.com/falbrechtskirchinger/another-brave-overlay) ebuild repository for Portage, then synchronize that repository:

`root `[`#`]`eselect repository enable another-brave-overlay `

`root `[`#`]`emerge --sync another-brave-overlay `

### [Emerge]

Install Brave Stable:

`root `[`#`]`emerge --ask www-client/brave-browser::another-brave-overlay`

Brave Beta:

`root `[`#`]`emerge --ask www-client/brave-browser-beta::another-brave-overlay`

Brave Nightly:

`root `[`#`]`emerge --ask www-client/brave-browser-nightly::another-brave-overlay`

## [Configuration]

Most configuration aspects can be found in the [Chromium article](https://wiki.gentoo.org/wiki/Chromium "Chromium"). Head over there for configuration information.

### [Screensharing with Pipewire]

Change \'WebRTC PipeWire support\' to \'Enabled\' in brave://flags

### [Using Wayland backend]

Change \'Preferred Ozone platform\' to \'Wayland\' in brave://flags

### [Policies]

It is possible to set specific policies for chromium based browsers like Brave. This can be useful especially if the browser should be accessible by users, but the content should be restricted to trusted sites. It can also be configured to restrict the access to specified URIs, like the file:// protocol, to prevent users from surfing the file system.

To set custom policies a JSON file must be created in [/etc/brave/policies/managed/\<filename\>.json]

The JSON file must meet the following structure:^[\[1\]](#cite_note-1)^

[CODE]



An example JSON file could look like this:

[CODE]



This prevents the user from surfing on the file system using the file protocol, incognito mode, blocks the listed URIs and URLs, and the location and notifications. More settings, can be found in the policy list: [https://www.chromium.org/administrators/policy-list-3/](https://www.chromium.org/administrators/policy-list-3/). If configured for other users as a service, it is recommended to block all sites at first and then define the allowed sites, to avoid abuse of the service.

** Note**\
It is important to ensure, that the `<filename>.json` is not writable by non-admin users, to prevent overwriting of the policies by users, which would defeat the purpose of policies! The [chown](https://linux.die.net/man/1/chown) and [chmod](https://linux.die.net/man/1/chmod) commands can be used to change ownership and rights if for any reason the file should be writable by non-admin users.

If the policy was configured properly can be proofed on the special page: brave://policy

Please note that this only blocks the user from visiting specified locations. It does not disable the protocols on the system, so other applications must be configured separately.

\
Additionally, Brave offers some specific policies that allow you to streamline the browser by removing certain features that you might want to disable such as Brave Rewards, Brave Wallet, VPN, AI Chat.

[CODE]



## [See also]

-   [Eselect/Repository](https://wiki.gentoo.org/wiki/Eselect/Repository "Eselect/Repository") --- an [eselect](https://wiki.gentoo.org/wiki/Eselect "Eselect") module for configuring [ebuild repositories](https://wiki.gentoo.org/wiki/Ebuild_repository "Ebuild repository") for [Portage](https://wiki.gentoo.org/wiki/Portage "Portage").

## [References]

1.  [[[↑](#cite_ref-1)] [[https://support.brave.com/hc/en-us/articles/360039248271-Group-Policy](https://support.brave.com/hc/en-us/articles/360039248271-Group-Policy)]]