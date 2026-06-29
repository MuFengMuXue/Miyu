## Name

org.freedesktop.timesync1 — The D-Bus interface of systemd-timesyncd

## Introduction

systemd-timesyncd.service(8) is a system service that may be used to synchronize the local system clock with a remote Network Time Protocol (NTP) server. This page describes the D-Bus interface.

## The Manager Object

The service exposes the following interfaces on the Manager object on the bus:

``` programlisting
node /org/freedesktop/timesync1 {
  interface org.freedesktop.timesync1.Manager {
    methods:
      SetRuntimeNTPServers(in  as runtime_servers);
    properties:
      readonly as LinkNTPServers = ['...', ...];
      readonly as SystemNTPServers = ['...', ...];
      readonly as RuntimeNTPServers = ['...', ...];
      readonly as FallbackNTPServers = ['...', ...];
      @org.freedesktop.DBus.Property.EmitsChangedSignal("false")
      readonly s ServerName = '...';
      @org.freedesktop.DBus.Property.EmitsChangedSignal("false")
      readonly (iay) ServerAddress = ...;
      @org.freedesktop.DBus.Property.EmitsChangedSignal("const")
      readonly t RootDistanceMaxUSec = ...;
      @org.freedesktop.DBus.Property.EmitsChangedSignal("const")
      readonly t PollIntervalMinUSec = ...;
      @org.freedesktop.DBus.Property.EmitsChangedSignal("const")
      readonly t PollIntervalMaxUSec = ...;
      @org.freedesktop.DBus.Property.EmitsChangedSignal("false")
      readonly t PollIntervalUSec = ...;
      readonly (uuuuittayttttbtt) NTPMessage = ...;
      @org.freedesktop.DBus.Property.EmitsChangedSignal("false")
      readonly x Frequency = ...;
  };
  interface org.freedesktop.DBus.Peer { ... };
  interface org.freedesktop.DBus.Introspectable { ... };
  interface org.freedesktop.DBus.Properties { ... };
};
```

<!-- -->

<!-- -->

<!-- -->

<!-- -->

<!-- -->

<!-- -->

<!-- -->

<!-- -->

<!-- -->

<!-- -->

<!-- -->

<!-- -->

<!-- -->

<!-- -->

Provides information about the manager.

## Examples

**Example 1. Introspect `org.freedesktop.timesync1.Manager` on the bus**

``` programlisting
$ gdbus introspect --system \
  --dest org.freedesktop.timesync1 \
  --object-path /org/freedesktop/timesync1
```

  

## Versioning

These D-Bus interfaces follow the usual interface versioning guidelines.

## See Also

systemd(1), systemd-timesyncd.service(8)
