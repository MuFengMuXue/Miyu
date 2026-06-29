[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Eduroam&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://eduroam.org/)

[[]][Official documentation](https://eduroam.org/about/connect-yourself/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/eduroam "wikipedia:eduroam")

[[]][GitHub](https://github.com/GEANT/CAT)

This article will describe how to configure Gentoo to connect to **eduroam**. eduroam (*edu*cation *roam*ing) is an international [Wi-Fi](https://wiki.gentoo.org/wiki/Wifi "Wifi") service based on [802.1x](https://en.wikipedia.org/wiki/IEEE_802.1X "wikipedia:IEEE 802.1X") for users at many educational institutions.^[\[1\]](#cite_note-1)^. There is a map available to see where eduroam networks exist.^[\[2\]](#cite_note-2)^

## Contents

-   [[1] [Configuration]](#Configuration)
    -   [[1.1] [Configuration assistant tool]](#Configuration_assistant_tool)
    -   [[1.2] [NetworkManager (nmcli)]](#NetworkManager_.28nmcli.29)
        -   [[1.2.1] [Troubleshooting]](#Troubleshooting)
        -   [[1.2.2] [Roam.fi]](#Roam.fi)
    -   [[1.3] [IWD]](#IWD)
    -   [[1.4] [KDE Plasma settings]](#KDE_Plasma_settings)
-   [[2] [Site-specific tips]](#Site-specific_tips)
    -   [[2.1] [University of Bristol]](#University_of_Bristol)
    -   [[2.2] [Technical University of Łódź]](#Technical_University_of_.C5.81.C3.B3d.C5.BA)
    -   [[2.3] [Umeå University]](#Ume.C3.A5_University)
-   [[3] [See also]](#See_also)
-   [[4] [External resources]](#External_resources)
-   [[5] [References]](#References)

## [Configuration]

### [Configuration assistant tool]

The eduroam Configuration Assistant Tool (CAT) collects information about RADIUS/EAP deployments and generates secure installation programs for a range of popular PC and smartphone platforms.^[\[3\]](#cite_note-3)^ The installer can be downloaded at [cat.eduroam.org](https://cat.eduroam.org/). On Linux, it supports PEAP-MSCHAPv2, TLS, TTLS-MSCHAPv2, TTLS-PAP, and Managed IdP.^[\[4\]](#cite_note-4)^ The CAT installer primarily supports NetworkManager, but can also be used to generate standalone configuration files for use with [wpa_supplicant](https://wiki.gentoo.org/wiki/Wpa_supplicant "Wpa supplicant") and [iwd](https://wiki.gentoo.org/wiki/Iwd "Iwd").

** Note**\
Not all organizations may have a CAT profile.

### [][NetworkManager (nmcli)]

** Important**\
Be careful about storing passwords in configuration files, especially on multi-user systems. Follow standard best practices and don\'t reuse passwords.

nmcli can be used to manually establish eduroam connections with [NetworkManager](https://wiki.gentoo.org/wiki/NetworkManager "NetworkManager"). The connection-specific configuration files are stored in [/etc/NetworkManager/system-connections/].

[FILE] **`eduroam-setup.sh`**

    #!/bin/bash

    CONNAME="eduroam"
    USERNAME="firstname.surname@tuni.fi"
    PASSWORD=""

    nmcli connection add type wifi con-name $CONNAME        \
            connection.permissions $LOGNAME                 \
            802-11-wireless.ssid $CONNAME                   \
            802-11-wireless-security.key-mgmt wpa-eap       \
            802-11-wireless-security.group ccmp,tkip        \
            802-11-wireless-security.pairwise ccmp          \
            802-11-wireless-security.proto rsn              \
            802-1x.altsubject-matches DNS:wifi.tuni.fi      \
            802-1x.anonymous-identity anonymous@tuni.fi     \
            802-1x.eap peap                                 \
            802-1x.identity $USERNAME                       \
            802-1x.password $PASSWORD                       \
            802-1x.phase2-auth mschapv2                     \
            ipv4.method auto                                \
            ipv6.addr-gen-mode stable-privacy               \
            ipv6.method auto

The above is specific to Tampere University in Finland. Configuration may differ across institutions, especially parameters like `802-1x.altsubject-matches DNS:wifi.tuni.fi` and `802-1x.anonymous-identity anonymous@tuni.fi`.

#### [Troubleshooting]

On [systemd](https://wiki.gentoo.org/wiki/Systemd "Systemd") profiles, a conflict may arise between NetworkManager and [systemd-networkd](https://wiki.gentoo.org/wiki/Systemd/systemd-networkd "Systemd/systemd-networkd").service which results in eduroam connections continually disconnecting after a short time and then reconnecting. In order to ensure that only NetworkManager is managing the eduroam connection, run

`root `[`#`]`systemctl stop systemd-networkd.service`

and

`root `[`#`]`systemctl disable systemd-networkd.service`

unless this service is needed for something else.

#### [Roam.fi]

[https://www.roam.fi/](https://www.roam.fi/) is a similar networking project like *eduroam* in Finland. The above script works also for *roam.fi*, only the SSID is different. Please set the variable `CONNAME="roam.fi"`.

### [IWD]

This section details eduroam configuration for standalone iwd network management.

** Important**\
See the [iwd#iwd native](https://wiki.gentoo.org/wiki/Iwd#iwd_native "Iwd") article for details on configuring iwd standalone.

Run the CAT installer with the `--iwd_conf` option:

`root `[`#`]`./eduroam-linux-<your-org>.py --iwd_conf`

This will generate a [eduroam.8021x] file in the current directory. Move it to the runtime directory (see also [man 5 iwd.network]):

`root `[`#`]`mv eduroam.8021x /var/lib/iwd/`

Provided that the username and password are correct, connecting with eduroam should now work.

** Tip**\
Some institutions use alternative EAP methods, like Tunneled TLS (TTLS). These require their own configuration values which can be found in [the Documentation](https://iwd.wiki.kernel.org/networkconfigurationsettings)

### [KDE Plasma settings]

Below are screenshots from [KDE](https://wiki.gentoo.org/wiki/KDE "KDE") Plasma desktop environment system settings for eduroam wi-fi configuration.

-   ::::::
    ::::
    :::
    [![](/images/thumb/f/f7/KDE_Plasma_eduroam_general_configuration.png/300px-KDE_Plasma_eduroam_general_configuration.png)](https://wiki.gentoo.org/wiki/File:KDE_Plasma_eduroam_general_configuration.png)
    :::
    ::::

    ::: gallerytext
    General configuration
    :::
    ::::::

-   ::::::
    ::::
    :::
    [![](/images/thumb/7/73/KDE_Plasma_eduroam_wi-fi.png/300px-KDE_Plasma_eduroam_wi-fi.png)](https://wiki.gentoo.org/wiki/File:KDE_Plasma_eduroam_wi-fi.png)
    :::
    ::::

    ::: gallerytext
    Wi-Fi settings
    :::
    ::::::

-   ::::::
    ::::
    :::
    [![](/images/thumb/c/c6/KDE_Plasma_eduroam_wi-fi_security.png/300px-KDE_Plasma_eduroam_wi-fi_security.png)](https://wiki.gentoo.org/wiki/File:KDE_Plasma_eduroam_wi-fi_security.png)
    :::
    ::::

    ::: gallerytext
    Wi-Fi security settings. Cyan dots indicate settings which probably vary from one institution to another.
    :::
    ::::::

-   ::::::
    ::::
    :::
    [![](/images/thumb/a/a2/KDE_Plasma_eduroam_ipv4.png/300px-KDE_Plasma_eduroam_ipv4.png)](https://wiki.gentoo.org/wiki/File:KDE_Plasma_eduroam_ipv4.png)
    :::
    ::::

    ::: gallerytext
    IPv4 settings
    :::
    ::::::

-   ::::::
    ::::
    :::
    [![](/images/thumb/d/d8/KDE_Plasma_eduroam_ipv6.png/300px-KDE_Plasma_eduroam_ipv6.png)](https://wiki.gentoo.org/wiki/File:KDE_Plasma_eduroam_ipv6.png)
    :::
    ::::

    ::: gallerytext
    IPv6 settings
    :::
    ::::::

## [Site-specific tips]

For institution-specific guidance, please contact the institution\'s support team. Some tips have been proposed here, and may be useful for some individual users.

### [University of Bristol]

The University of Bristol [has pages](https://www.wireless.bris.ac.uk/eduroam/instructions/) on configuring eduroam using NetworkManager, wpa_supplicant, netctl and more.

### [][Technical University of Łódź]

The Technical University of Łódź (Politechnika Łódzka) does not provide any official guidance on how to configure eduroam.^[\[5\]](#cite_note-5)^

** Note**\
If NetworkManager isn\'t [compiled with iwd](https://packages.gentoo.org/useflags/iwd) support, it won\'t even see the network.

Below is a config that allowed at least one student to use NetworkManager to connect to eduroam.

1.  Download the `tuLodzPem.pem` file from [the University CA\'s site](https://ca.p.lodz.pl/tulodz/) and save it to `/etc/ca-certificates/trust-source/`
2.  Copy this file to `/var/lib/iwd/eduroam.8021x` and replace the stuff \[in brackets\]

[FILE] **`/var/lib/iwd/eduroam.8021x`**

    [Security]
    EAP-Method=PEAP
    EAP-Identity=[student_id]@edu.p.lodz.pl
    EAP-PEAP-CACert=/etc/ca-certificates/trust-source/tuLodzRoot.pem
    EAP-PEAP-ServerDomainMask=*.p.lodz.pl
    EAP-PEAP-Phase2-Method=MSCHAPV2
    EAP-PEAP-Phase2-Identity=[student_id]@edu.p.lodz.pl
    EAP-PEAP-Phase2-Password=[password]

This should work already. However just to be safe go to `nmtui` and check the eduroam connection. Once you save it the file above should begin with `# Auto-generated from NetworkManager connection "eduroam"`.

### [][Umeå University]

Umeå University has official guidance for setting up Eduroam through Ubuntu, which can be found on [their website](https://manual.umu.se/en/install-eduroam-manually) under the \"Ubuntu\" tab. The instructions there can be applied to Gentoo, for example using NetworkManager and `nmtui`. To note, the institution uses TLS 1.0 for authentication rather than EAP (even though the authentication domain is `eap.ad.umu.se`), meaning logging in to download a user and root certificate from the website before setting the connection up is required.

## [See also]

-   [Category:Network_management](https://wiki.gentoo.org/wiki/Category:Network_management "Category:Network management")
-   [iwd](https://wiki.gentoo.org/wiki/Iwd "Iwd") --- a wireless daemon intended to replace wpa_supplicant
-   [resolv.conf](https://wiki.gentoo.org/wiki/Resolv.conf "Resolv.conf") --- used to configure hostname resolution.
-   [WireGuard](https://wiki.gentoo.org/wiki/WireGuard "WireGuard") --- a modern, simple, and secure VPN that utilizes state-of-the-art cryptography.
-   [wpa_supplicant](https://wiki.gentoo.org/wiki/Wpa_supplicant "Wpa supplicant") --- an app for [Wi-Fi](https://wiki.gentoo.org/wiki/Wi-Fi "Wi-Fi") authentication

## [External resources]

-   [https://unix.stackexchange.com/questions/145366/how-to-connect-to-an-802-1x-wireless-network-via-nmcli](https://unix.stackexchange.com/questions/145366/how-to-connect-to-an-802-1x-wireless-network-via-nmcli) --- How to connect to an 802.1x wireless network via nmcli
-   [eduroam Privacy Notice](https://eduroam.org/eduroam-privacy-notice/)
-   [https://monitor.eduroam.org/](https://monitor.eduroam.org/) - eduroam services status
-   [CAT Diagnostics](https://cat.eduroam.org/diag/diag.php)
-   [RITlug eduroam Guide](https://wiki.ritlug.com/eduroam/)

## [References]

1.  [[[↑](#cite_ref-1)] [[https://en.wikipedia.org/wiki/Eduroam](https://en.wikipedia.org/wiki/Eduroam)]]
2.  [[[↑](#cite_ref-2)] [[https://eduroam.org/where/](https://eduroam.org/where/)]]
3.  [[[↑](#cite_ref-3)] [[https://eduroam.org/configuration-assistant-tool-cat/](https://eduroam.org/configuration-assistant-tool-cat/)]]
4.  [[[↑](#cite_ref-4)] [[https://cat.eduroam.org/](https://cat.eduroam.org/) (About → About eduroam CAT)]]
5.  [[[↑](#cite_ref-5)] [[https://uci.p.lodz.pl/node/261](https://uci.p.lodz.pl/node/261)]]