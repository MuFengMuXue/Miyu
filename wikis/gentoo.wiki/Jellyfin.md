**Resources**

[[]][Home](https://jellyfin.org/)

[[]][Official documentation](https://jellyfin.org/docs/)

[[]][Package information](https://packages.gentoo.org/packages/www-apps/jellyfin)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Jellyfin "wikipedia:Jellyfin")

[[]][GitHub](https://github.com/jellyfin/jellyfin)

This article covers installation and management of the **jellyfin** media server.

Jellyfin is an open-source audio and video client/server system that allows managing, playing, and sharing digital media libraries. The Jellyfin server application is multi-platform, and has clients for multiple desktop OSs, smartphones, tablets, smart TVs, games consoles, Chromecasts, DNLA devices, etc. It can also be accessed directly through a web browser.

Jellyfin started as a fork of Emby, which is now mostly closed-source. It can be a networked alternative for Home Theater packages such as [Kodi](https://wiki.gentoo.org/wiki/Kodi "Kodi"), or [media library players](https://wiki.gentoo.org/wiki/Recommended_applications#Audio_players "Recommended applications").

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Emerge]](#Emerge)
    -   [[1.2] [Additional software]](#Additional_software)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Files]](#Files)
    -   [[2.2] [Generating a certificate for HTTPS]](#Generating_a_certificate_for_HTTPS)
        -   [[2.2.1] [Lets Encrypt via Certbot]](#Lets_Encrypt_via_Certbot)
        -   [[2.2.2] [Manual]](#Manual)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Services]](#Services)
        -   [[3.1.1] [OpenRC]](#OpenRC)
        -   [[3.1.2] [systemd]](#systemd)
    -   [[3.2] [Connecting]](#Connecting)
    -   [[3.3] [Updates]](#Updates)
        -   [[3.3.1] [OpenRC]](#OpenRC_2)
        -   [[3.3.2] [systemd]](#systemd_2)
-   [[4] [Removal]](#Removal)
    -   [[4.1] [Unmerge]](#Unmerge)
    -   [[4.2] [Clean up orphaned data directories]](#Clean_up_orphaned_data_directories)

## [[] Installation]

### [[] Emerge]

Install the server package [[[www-apps/jellyfin-bin]](https://packages.gentoo.org/packages/www-apps/jellyfin-bin)[]]:

`root `[`#`]`emerge --ask www-apps/jellyfin-bin`

This package contains a web interface to the library, but may also be used with a dedicated client.

### [[] Additional software]

The community of developers contributing to the Jellyfin project offer a suite of other software which is used in conjunction with the media server. The following are related packages available in the Gentoo ebuild repository:

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------- ------------------------------------------------------------------------------
  Package name                                                                                                                                                                                                                                                                                                                                                                                                                Package description                                                 Additional notes
  [[[media-video/jellyfin-media-player]](https://packages.gentoo.org/packages/media-video/jellyfin-media-player)[]]   Jellyfin Desktop Client based on Plex Media Player                  Package gone without notice. (404)
  [[[media-video/jellyfin-web-bin]](https://packages.gentoo.org/packages/media-video/jellyfin-web-bin)[]]                  Web Client for Jellyfin (binary package)                            N/A
  [[[media-video/jellyfin-web-jmp-bin]](https://packages.gentoo.org/packages/media-video/jellyfin-web-jmp-bin)[]]      Modified Jellyfin Web Client for use inside Jellyfin Media Player   N/A
  media-video/delfin                                                                                                                                                                                                                                                                                                                                                                                                          Jellyfin GTK desktop client                                         in [GURU](https://wiki.gentoo.org/wiki/GURU "GURU") repository
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------- ------------------------------------------------------------------------------

  : Jellyfin related software

## [[] Configuration]

### [[] Files]

**Configuration files:**

-   [/etc/conf.d/jellyfin] - OpenRC\'s configuration file. Adjust as necessary for the running service.
-   [/etc/jellyfin] - Default configuration location for Jellyfin\'s `JELLYFIN_CONFIG_DIR` value.^[\[1\]](#cite_note-1)^

**Cache directories:**

-   [/var/cache/jellyfin] - Default location for Jellyfin\'s `JELLYFIN_CACHE_DIR` value.^[\[2\]](#cite_note-2)^
-

**Data directory:**

-   [/var/lib/jellyfin] - Default data location for Jellyfin\'s `JELLYFIN_DATA_DIR` value.^[\[3\]](#cite_note-3)^ Includes transcodes and library metadata.

**Log directory:**

-   [/var/log/jellyfin] - Default log location for Jellyfin\'s `JELLYFIN_LOG_DIR` value.^[\[4\]](#cite_note-4)^

### [[] Generating a certificate for HTTPS]

If authentication is to be performed over a network (Eg. the jellyfin service is not simply serving localhost, but clients that are across the network) it is important to encrypt the traffic. This protects credentials used to authenticate and the privacy of the data contained in the media library, etc.

#### [[] Lets Encrypt via Certbot]

[[certbot](https://wiki.gentoo.org/wiki/Certbot "Certbot")] can be used to generate a certificate signed by the Let\'s Encrypt public certificate authority. [Upstream has instructions for this](https://jellyfin.org/docs/general/networking/letsencrypt/).

#### [[] Manual]

Manual method implies the certificate is not signed by a public certificate authority; it is self-signed and will be untrusted by all major web browsers. This is to be expected, and does not indicate compromise of the protections afforded by encryption.

OpenSSL can be used to generate a self-signed certificate, which should be in PKCS #12 file format:

`root `[`#`]`mkdir --parents /etc/ssl/jellyfin `

`root `[`#`]`openssl req -x509 -newkey rsa:4096 -keyout jellyfin-key.pem -out jellyfin-cert.pem -days 3650 -noenc # Valid for 10 years `

`root `[`#`]`openssl pkcs12 -export -out jellyfin-keystore.p12 -inkey jellyfin-key.pem -in jellyfin-cert.pem # Enter a strong password to protect the exported PKCS #12 file, it contains the private key! `

`root `[`#`]`chmod 644 /etc/ssl/jellyfin/jellyfin-keystore.p12 # Adds read privs for jellyfin user/group to access `

## [[] Usage]

### [[] Services]

#### [[] OpenRC]

To start and enable the service:

`root `[`#`]`rc-update add jellyfin default`

`root `[`#`]`rc-service jellyfin start`

#### [[] systemd]

To start and enable the service:

`root `[`#`]`systemctl enable --now jellyfin`

### [[] Connecting]

By default the jellyfin service binds to port 8096 on *all* network interfaces (including the loop back address) of the server on which it is running. Interface binding can be changed within the web management portal.

Open localhost:8096 if running from the local server, or \<IP_ADDRESS\>:8096 if running from another host on the LAN. It may be necessary to unblock port 8096 if a firewall rule exists preventing communication.

### [[] Updates]

#### [[] OpenRC]

After package updates, restart the service:

`root `[`#`]`rc-service jellyfin restart`

#### [[] systemd]

After package updates, restart the service:

`root `[`#`]`systemctl daemon-reload # In the event of the jellyfin.service file changing; systemd will warn when this is the case `

`root `[`#`]`systemctl restart jellyfin `

## [[] Removal]

### [[] Unmerge]

`root `[`#`]`emerge --ask --depclean --verbose www-apps/jellyfin-bin`

### [[] Clean up orphaned data directories]

See the cached data directories outlined in the [Files section](#Files) above.

1.  [[[↑](#cite_ref-1)] [[https://jellyfin.org/docs/general/administration/configuration#configuration-directory](https://jellyfin.org/docs/general/administration/configuration#configuration-directory)]]
2.  [[[↑](#cite_ref-2)] [[https://jellyfin.org/docs/general/administration/configuration#cache-directory](https://jellyfin.org/docs/general/administration/configuration#cache-directory)]]
3.  [[[↑](#cite_ref-3)] [[https://jellyfin.org/docs/general/administration/configuration#configuration-directory](https://jellyfin.org/docs/general/administration/configuration#configuration-directory)]]
4.  [[[↑](#cite_ref-4)] [[https://jellyfin.org/docs/general/administration/configuration#log-directory](https://jellyfin.org/docs/general/administration/configuration#log-directory)]]