[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Curl&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://curl.se/)

[[]][Official documentation](https://curl.se/docs/)

[[]][Package information](https://packages.gentoo.org/packages/net-misc/curl)

[[]][Wikipedia](https://en.wikipedia.org/wiki/cURL "wikipedia:cURL")

[[]][GitHub](https://github.com/curl/curl)

[[]][Bugs (upstream)](https://github.com/curl/curl/issues)

**curl** is a utility for transferring data to or from a server using URLs. While often used with HTTP, a range of protocols are supported.

In its most basic usage, [curl] sends a request to a server, and prints the response to that request (or an error) on the terminal. An extensive array of options make it a highly flexible tool for fetching content from the network, and diagnosing network services. [curl] allows customization of the sent request and the handling of the response, and can be thought of as a *Swiss-army knife* for request-response based network protocols.

A similar tool is [wget](https://wiki.gentoo.org/wiki/Wget "Wget"), which is included in the [\@system] set on Gentoo systems.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [curl\'ing a web page]](#curl.27ing_a_web_page)
    -   [[2.2] [Following redirect responses]](#Following_redirect_responses)
    -   [[2.3] [Saving files to disk]](#Saving_files_to_disk)
-   [[3] [See also]](#See_also)

## [Installation]

### [USE flags]

### [USE flags for] [net-misc/curl](https://packages.gentoo.org/packages/net-misc/curl) [[]] [A Client that groks URLs]

  ------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+adns`](https://packages.gentoo.org/useflags/+adns)               Add support for asynchronous DNS resolution
  [`+alt-svc`](https://packages.gentoo.org/useflags/+alt-svc)         Enable alt-svc support
  [`+ftp`](https://packages.gentoo.org/useflags/+ftp)                 Enable FTP support
  [`+hsts`](https://packages.gentoo.org/useflags/+hsts)               Enable HTTP Strict Transport Security
  [`+http2`](https://packages.gentoo.org/useflags/+http2)             Enable support for the HTTP/2 protocol
  [`+http3`](https://packages.gentoo.org/useflags/+http3)             Enable HTTP/3 support
  [`+httpsrr`](https://packages.gentoo.org/useflags/+httpsrr)         Enable HTTPS Resource Record support
  [`+imap`](https://packages.gentoo.org/useflags/+imap)               Enable Internet Message Access Protocol support
  [`+openssl`](https://packages.gentoo.org/useflags/+openssl)         Enable openssl ssl backend
  [`+pop3`](https://packages.gentoo.org/useflags/+pop3)               Enable Post Office Protocol 3 support
  [`+psl`](https://packages.gentoo.org/useflags/+psl)                 Enable Public Suffix List (PSL) support. See https://daniel.haxx.se/blog/2024/01/10/psl-in-curl/.
  [`+quic`](https://packages.gentoo.org/useflags/+quic)               Enable support for QUIC (RFC 9000); a UDP-based protocol intended to replace TCP
  [`+smtp`](https://packages.gentoo.org/useflags/+smtp)               Enable Simple Mail Transfer Protocol support
  [`+tftp`](https://packages.gentoo.org/useflags/+tftp)               Enable TFTP support
  [`+websockets`](https://packages.gentoo.org/useflags/+websockets)   Enable websockets support
  [`brotli`](https://packages.gentoo.org/useflags/brotli)             Enable Brotli compression support
  [`debug`](https://packages.gentoo.org/useflags/debug)               Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`ech`](https://packages.gentoo.org/useflags/ech)                   Enable Encrypted Client Hello support
  [`gnutls`](https://packages.gentoo.org/useflags/gnutls)             Enable gnutls ssl backend
  [`gopher`](https://packages.gentoo.org/useflags/gopher)             Enable Gopher protocol support
  [`idn`](https://packages.gentoo.org/useflags/idn)                   Enable support for Internationalized Domain Names
  [`kerberos`](https://packages.gentoo.org/useflags/kerberos)         Add kerberos support
  [`ldap`](https://packages.gentoo.org/useflags/ldap)                 Add LDAP support (Lightweight Directory Access Protocol)
  [`mbedtls`](https://packages.gentoo.org/useflags/mbedtls)           Enable mbedtls ssl backend
  [`rtmp`](https://packages.gentoo.org/useflags/rtmp)                 Enable RTMP Streaming Media support
  [`rustls`](https://packages.gentoo.org/useflags/rustls)             Enable Rustls ssl backend
  [`samba`](https://packages.gentoo.org/useflags/samba)               Add support for SAMBA (Windows File and Printer sharing)
  [`sasl-scram`](https://packages.gentoo.org/useflags/sasl-scram)     Enable snupport for additional SASL SCRAM-SHA authentication methods via net-misc/gsasl
  [`ssh`](https://packages.gentoo.org/useflags/ssh)                   Enable SSH urls in curl using libssh2
  [`ssl`](https://packages.gentoo.org/useflags/ssl)                   Enable crypto engine support (via openssl if USE=\'-gnutls -nss\')
  [`static-libs`](https://packages.gentoo.org/useflags/static-libs)   Build static versions of dynamic libraries as well
  [`telnet`](https://packages.gentoo.org/useflags/telnet)             Enable Telnet protocol support
  [`test`](https://packages.gentoo.org/useflags/test)                 Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`verify-sig`](https://packages.gentoo.org/useflags/verify-sig)     Verify upstream signatures on distfiles
  [`zstd`](https://packages.gentoo.org/useflags/zstd)                 Enable support for ZSTD compression
  ------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-04-16 23:05] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Install [[[net-misc/curl]](https://packages.gentoo.org/packages/net-misc/curl)[]]:

`root `[`#`]`emerge --ask net-misc/curl`

## [Usage]

### [][curl\'ing a web page]

To \"curl\" a web page, call the curl command with the appropriate URL:

`user `[`$`]`curl `[`https://example.com`](https://example.com)

    $ curl https://example.com
    <!doctype html>
    <html>
    <head>
        <title>Example Domain</title>

        <meta charset="utf-8" />
        <meta http-equiv="Content-type" content="text/html; charset=utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <style type="text/css">
        body
        div
        a:link, a:visited
        @media (max-width: 700px)
        }
        </style>
    </head>

    <body>

        <h1>Example Domain</h1>
        This domain is for use in illustrative examples in documents. You may use this
        domain in literature without prior coordination or asking for permission.
        <a href="https://www.iana.org/domains/example">More information...</a>

    </body>
    </html>

### [Following redirect responses]

By default, [curl] returns the first response from the server verbatim. This might not always be desirable, for example if the server returns an `HTTP 3xx` redirect response --- which a browser would usually follow transparently --- [curl] will only retrieve that response and do nothing else.

Use the `--location`(`-L`) option to instruct [curl] to follow redirections with a new request when receiving a redirect response.

** Note**\
This is important when saving the response to disk. If a redirection is received without using `--location`, the saved file would only contain that redirection response (probably a short HTML document) and no error would be emitted. If a [tar] archive was expected, for example, [tar] would complain that the file seemed to be garbage, masking the actual issue that the intended file had not even been fetched.

### [Saving files to disk]

By default, curl writes its output to the terminal. This may surprise users used to the behavior of [wget](https://wiki.gentoo.org/wiki/Wget "Wget"), a similar utility. This is often useful when piping the output of curl to another utility.

** Warning**\
The `-o` and `-O` options will overwrite the destination without prompting.

Files can be saved to disk by specifying the destination file name with the `-output` (`-o`) flag:

`user `[`$`]`curl `[`https://example.com`](https://example.com)` -L -o index.html`

The `--remote-name`(`-O`) option saves the file with the same name as on the server. This is most useful when the URL contains a file name. If the file name can not be determined, such as *default* content where the URL contains no file name, the output is saved as [curl_response].

`user `[`$`]`curl `[`https://example.com/index.html`](https://example.com/index.html)` -OL`

## [See also]

[wget](https://wiki.gentoo.org/wiki/Wget "Wget") --- a robust non-interactive [HTTP](https://en.wikipedia.org/wiki/HTTP "wikipedia:HTTP"), [HTTPS](https://en.wikipedia.org/wiki/HTTPS "wikipedia:HTTPS"), and [FTP](https://en.wikipedia.org/wiki/FTP "wikipedia:FTP") client