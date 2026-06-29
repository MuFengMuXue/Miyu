## Name

systemd-journal-gatewayd.service, systemd-journal-gatewayd.socket, systemd-journal-gatewayd — HTTP server for journal events

## Synopsis

`systemd-journal-gatewayd.service`

`systemd-journal-gatewayd.socket`

`/usr/lib/systemd/systemd-journal-gatewayd` \[OPTIONS...\]

## Description

**systemd-journal-gatewayd** serves journal events over the network. Clients must connect using HTTP. The server listens on port 19531 by default. If `--cert=` is specified, the server expects HTTPS connections.

The program is started by systemd(1) and expects to receive a single socket. Use **systemctl start systemd-journal-gatewayd.socket** to start the service, and **systemctl enable systemd-journal-gatewayd.socket** to have it started on boot.

## Options

The following options are understood:

`--cert=`  
Specify the path to a file or `AF_UNIX` stream socket to read the server certificate from. The certificate must be in PEM format. This option switches **systemd-journal-gatewayd** into HTTPS mode and must be used together with `--key=`.

Added in version 198.

`--key=`  
Specify the path to a file or `AF_UNIX` stream socket to read the secret server key corresponding to the certificate specified with `--cert=` from. The key must be in PEM format.

Added in version 198.

`--trust=`  
Specify the path to a file or `AF_UNIX` stream socket to read a CA certificate from. The certificate must be in PEM format.

Added in version 236.

`--system`, `--user`  
Limit served entries to entries from system services and the kernel, or to entries from services of current user. This has the same meaning as `--system` and `--user` options for journalctl(1). If neither is specified, all accessible entries are served.

Added in version 249.

`-m`, `--merge`  
Serve entries interleaved from all available journals, including other machines. This has the same meaning as `--merge` option for journalctl(1).

Added in version 249.

`-D `*`DIR`*, `--directory=`*`DIR`*  
Takes a directory path as argument. If specified, **systemd-journal-gatewayd** will serve the specified journal directory *`DIR`* instead of the default runtime and system journal paths.

Added in version 232.

`--file=`*`GLOB`*  
Takes a file glob as an argument. Serve entries from the specified journal files matching *`GLOB`* instead of the default runtime and system journal paths. May be specified multiple times, in which case files will be suitably interleaved. This has the same meaning as `--file=` option for journalctl(1).

Added in version 249.

`-h`, `--help`  
Print a short help text and exit.

`--version`  
Print a short version string and exit.

## Supported URLs

The following URLs are recognized:

`/boots`  
Returns json-seq (RFC 7464) response containing JSON objects, each one containing boot number, its ID and the timestamps of the first and last message. Boots are returned starting with the latest boot first and use the same schema as **journalctl --list-boots --output json**.

Added in version 258.

`/browse`  
Interactive browsing.

Added in version 197.

`/entries[?option1&option2=value…]`  
Retrieval of events in various formats.

The `Accept:` part of the HTTP header determines the format. Supported values are described below.

The `Range:` part of the HTTP header determines the range of events returned. Supported values are described below.

GET parameters can be used to modify what events are returned. Supported parameters are described below.

Added in version 197.

`/machine`  
Return a JSON structure describing the machine.

Example:

``` programlisting
{ "machine_id" : "8cf7ed9d451ea194b77a9f118f3dc446",
  "boot_id" : "3d3c9efaf556496a9b04259ee35df7f7",
  "hostname" : "fedora",
  "os_pretty_name" : "Fedora 19 (Rawhide)",
  "virtualization" : "kvm",
  …}
```

Added in version 197.

`/fields/`*`FIELD_NAME`*  
Return a list of values of this field present in the logs.

Added in version 197.

## Accept header

`Accept: `*`format`*

Recognized formats:

`text/plain`  
The default. Plaintext syslog-like output, one line per journal entry (like **journalctl --output short**).

Added in version 197.

`application/json`  
Entries are formatted as JSON data structures, one per line (like **journalctl --output json**). See Journal JSON Format for more information.

Added in version 197.

`text/event-stream`  
Entries are formatted as JSON data structures, wrapped in a format suitable for Server-Sent Events (like **journalctl --output json-sse**).

Added in version 229.

`application/vnd.fdo.journal`  
Entries are serialized into a binary (but mostly text-based) stream suitable for backups and network transfer (like **journalctl --output export**). See Journal Export Format for more information.

Added in version 197.

## Range header

`Range: entries=[`*`cursor`*`][[:`*`num_skip`*`]:[`*`num_entries`*`]]`

`Range: realtime=[`*`since`*`]:[`*`until`*`][[:`*`num_skip`*`]:`*`num_entries`*`]`

where *`cursor`* is a cursor string, defaults to the first entry, *`since`* and *`until`* are timestamps (seconds since 1970-01-01 00:00:00 UTC), *`num_skip`* is an integer, *`num_entries`* is an unsigned integer.

Range defaults to all available events.

If *`num_skip`* is negative and no *`cursor`* is given, the last entry will be the reference point.

## URL GET parameters

Following parameters can be used as part of the URL:

`follow`  
wait for new events (like **journalctl --follow**, the number of events returned is not limited, unless *`num_entries`* is specified in the *`Range`* header).

Added in version 197.

`discrete`  
Test that the specified cursor refers to an entry in the journal. Returns just this entry.

Added in version 197.

`boot`  
Limit events to the current boot of the system (like **journalctl -b**).

Added in version 197.

*`KEY`*`=`*`match`*  
Match journal fields. See systemd.journal-fields(7).

Added in version 197.

## Examples

Retrieve events from this boot from local journal in Journal Export Format:

``` programlisting
curl --silent -H'Accept: application/vnd.fdo.journal' \
       'http://localhost:19531/entries?boot'
```

Listen for core dumps:

``` programlisting
curl 'http://localhost:19531/entries?follow&MESSAGE_ID=fc2e22bc6ee647b6b90729ab34a250b1'
```

## See Also

systemd(1), journalctl(1), systemd.journal-fields(7), systemd-journald.service(8), systemd-journal-remote.service(8), systemd-journal-upload.service(8)
