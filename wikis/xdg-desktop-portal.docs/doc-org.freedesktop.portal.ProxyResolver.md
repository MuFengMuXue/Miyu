# Proxy Resolver

## Description

Proxy information

The ProxyResolver interface provides network proxy information to sandboxed applications. It is not a portal in the strict sense, since it does not involve user interaction. Applications are expected to use this interface indirectly, via a library API such as the GLib GProxyResolver interface.

This documentation describes version 1 of this interface.

## Properties

### org.freedesktop.portal.ProxyResolver:version

    version readable u

## Methods

### org.freedesktop.portal.ProxyResolver.Lookup

    Lookup (
      IN uri s,
      OUT proxies as
    )

Looks up which proxy to use to connect to `uri`. The returned proxy uri are of the form `protocol://[user[:password] AT host:port`. The protocol can be `http`, `rtsp`, `socks` or another proxying protocol. `direct://` is used when no proxy is needed.

uri  
A URI, as described in RFC 3986, of the destination to connect to

proxies  
List of proxy uris
