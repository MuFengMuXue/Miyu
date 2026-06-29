**Resources**

[[]][Home](https://www.varnish-cache.org/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Varnish_(software) "wikipedia:Varnish (software)")

[![Ohloh Logo](/images/thumb/c/c1/Ohloh-logo.png/30px-Ohloh-logo.png)][Open Hub](https://www.openhub.net/p/varnish)

**Varnish** is a webcache and HTTP accelerator. It can either serve cached content, or retrieve content from a server and cache it. This helps to reduce I/O pressure for web servers that are serving many clients or have many requests.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Files]](#Files)
        -   [[2.1.1] [Global]](#Global)
    -   [[2.2] [Service]](#Service)
        -   [[2.2.1] [OpenRC]](#OpenRC)
        -   [[2.2.2] [systemd]](#systemd)
-   [[3] [Troubleshooting]](#Troubleshooting)
    -   [[3.1] [Verification]](#Verification)

## [Installation]

### [USE flags]

Cannot load package information. Is the atom *www-servers/varnish* correct?

### [Emerge]

Install [[[www-servers/varnish]](https://packages.gentoo.org/packages/www-servers/varnish)[]]

`root `[`#`]`emerge --ask www-servers/varnish`

## [Configuration]

### [Files]

#### [Global]

Configuration is controlled by the [/etc/varnish/default.vcl] file.

[FILE] **`/etc/varnish/example.vcl`**

    #
    # This is an example VCL file for Varnish.
    #
    # It does not do anything by default, delegating control to the
    # builtin VCL. The builtin VCL is called when there is no explicit
    # return statement.
    #
    # See the VCL chapters in the Users Guide at https://www.varnish-cache.org/docs/
    # and https://www.varnish-cache.org/trac/wiki/VCLExamples for more examples.

    # Marker to tell the VCL compiler that this VCL has been adapted to the
    # new 4.0 format.
    vcl 4.0;

    # Default backend definition. Set this to point to your content server.
    backend default

Any traffic pointed at port 8080 will travel through varnish.

### [Service]

#### [OpenRC]

To start varnish immediately:

`root `[`#`]`rc-service varnishd start`

To start varnish at boot:

`root `[`#`]`rc-update add varnishd default`

#### [systemd]

To start varnish on boot:

`root `[`#`]`systemctl enable varnishd`

To start varnish immediately:

`root `[`#`]`systemctl start varnishd`

## [Troubleshooting]

### [Verification]

The [curl] command ([[[net-misc/curl]](https://packages.gentoo.org/packages/net-misc/curl)[]]) can be used to verify that HTTP traffic is successfully traveling through the varnish proxy:

`user `[`$`]`curl -I https://wiki.gentoo.org/wiki`