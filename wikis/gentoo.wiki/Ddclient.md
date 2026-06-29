[ddclient](https://sourceforge.net/p/ddclient/wiki/Home/) is a tool to update dynamic DNS services like DynDNS or no-ip. It runs as daemon and supports many services.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [no-ip.com]](#no-ip.com)
    -   [[2.2] [Automatic start]](#Automatic_start)
-   [[3] [Removal]](#Removal)
    -   [[3.1] [Unmerge]](#Unmerge)

## [Installation]

### [Emerge]

`root `[`#`]`emerge --ask net-dns/ddclient`

## [Configuration]

The configuration is done in the file [/etc/ddclient/ddclient.conf]. It must not be world or group readable.

### [no-ip.com]

Take a look an example configuration for no-ip.com:

[FILE] **`/etc/ddclient/ddclient.conf`**

    use=web, web=checkip.dyndns.com/, web-skip='IP Address'

    protocol=dyndns2
    server=dynupdate.no-ip.com
    login=your_username (typically your email)
    password=your_password
    your_domain_in_noip.com

### [Automatic start]

To start the ddclient daemon:

`root `[`#`]`rc-service ddclient start`

To have the client start at boot:

`root `[`#`]`rc-update add ddclient default`

## [Removal]

### [Unmerge]

`root `[`#`]`emerge --ask --depclean --verbose net-dns/ddclient`