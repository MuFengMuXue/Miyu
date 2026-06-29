## Name

journal-upload.conf, journal-upload.conf.d — Configuration files for the journal upload service

## Synopsis

`/etc/systemd/journal-upload.conf`

`/run/systemd/journal-upload.conf`

`/usr/lib/systemd/journal-upload.conf`

`/etc/systemd/journal-upload.conf.d/*.conf`

`/run/systemd/journal-upload.conf.d/*.conf`

`/usr/lib/systemd/journal-upload.conf.d/*.conf`

## Description

These files configure various parameters of systemd-journal-upload.service(8). See systemd.syntax(7) for a general description of the syntax.

## Configuration Directories and Precedence

The default configuration is set during compilation, so configuration is only needed when it is necessary to deviate from those defaults. The main configuration file is loaded from one of the listed directories in order of priority, only the first file found is used: `/etc/systemd/`, `/run/systemd/`, `/usr/local/lib/systemd/` <sup>\[1\]</sup>, `/usr/lib/systemd/`. The vendor version of the file contains commented out entries showing the defaults as a guide to the administrator. Local overrides can also be created by creating drop-ins, as described below. The main configuration file can also be edited for this purpose (or a copy in `/etc/` if it is shipped under `/usr/`), however using drop-ins for local configuration is recommended over modifications to the main configuration file.

In addition to the main configuration file, drop-in configuration snippets are read from `/usr/lib/systemd/*.conf.d/`, `/usr/local/lib/systemd/*.conf.d/`, and `/etc/systemd/*.conf.d/`. Those drop-ins have higher precedence and override the main configuration file. Files in the `*.conf.d/` configuration subdirectories are sorted by their filename in lexicographic order, regardless of in which of the subdirectories they reside. When multiple files specify the same option, for options which accept just a single value, the entry in the file sorted last takes precedence, and for options which accept a list of values, entries are collected as they occur in the sorted files.

When packages need to customize the configuration, they can install drop-ins under `/usr/`. Files in `/etc/` are reserved for the local administrator, who may use this logic to override the configuration files installed by vendor packages. Drop-ins have to be used to override package drop-ins, since the main configuration file has lower precedence. It is recommended to prefix all filenames in those subdirectories with a two-digit number and a dash, to simplify the ordering. This also defines a concept of drop-in priorities to allow OS vendors to ship drop-ins within a specific range lower than the range used by users. This should lower the risk of package drop-ins overriding accidentally drop-ins defined by users. It is recommended to use the range 10-40 for drop-ins in `/usr/` and the range 60-90 for drop-ins in `/etc/` and `/run/`, to make sure that local and transient drop-ins take priority over drop-ins shipped by the OS vendor.

To disable a configuration file supplied by the vendor, the recommended way is to place a symlink to `/dev/null` in the configuration directory in `/etc/`, with the same filename as the vendor configuration file.

## Options

All options are configured in the \[Upload\] section:

`URL=`  
The URL to upload the journal entries to. See the description of `--url=` option in systemd-journal-upload(8) for the description of possible values. There is no default value, so either this option or the command-line option must be always present to make an upload.

Added in version 232.

`ServerKeyFile=`  
SSL key in PEM format.

Added in version 232.

`ServerCertificateFile=`  
SSL CA certificate in PEM format.

Added in version 232.

`TrustedCertificateFile=`  
SSL CA certificate.

Added in version 232.

`NetworkTimeoutSec=`  
When network connectivity to the server is lost, this option configures the time to wait for the connectivity to get restored. If the server is not reachable over the network for the configured time, **systemd-journal-upload** exits. Takes a value in seconds (or in other time units if suffixed with "ms", "min", "h", etc). For details, see systemd.time(7).

Added in version 249.

`Compression=`  
Configures compression algorithm to be applied to logs data before sending. Takes a space separated list of compression algorithms, or "`no`". Supported algorithms are "`zstd`", "`xz`", or "`lz4`". Optionally, each algorithm followed by a colon ("`:`") and its compression level, for example "`zstd:4`". The compression level is expected to be a positive integer. When "`no`" is specified, no compression algorithm will be applied to data to be sent. This option can be specified multiple times. If an empty string is assigned, then all previous assignments are cleared. Defaults to unset, and all supported compression algorithms with their default compression levels are listed.

Example:

``` programlisting
Compression=zstd:4 lz4:2
```

Even when compression is enabled, the initial requests are sent without compression. It becomes effective either if "`ForceCompression=`" is enabled, or the server response contains "`Accept-Encoding`" headers with a list of compression algorithms that contains one of the algorithms specified in this option.

Added in version 258.

`ForceCompression=`  
Takes a boolean value, enforces using compression without content encoding negotiation. Defaults to "`false`".

Added in version 258.

`Header=`  
Specifies an additional HTTP header to be added to each request to a URL. Takes a pair of header name and value separated with a colon("`:`"), e.g. "`Name:Value`". Header name can contain alphanumeric values, "`_`" and "`-`" symbols additionally. This option may be specified more than once, in which case all listed headers will be set. If the same header name is listed more than once, all its unique values will be concatenated with comma. Setting `Header=` to empty string clears all previous assignments.

Example:

``` programlisting
Header=HeaderName: HeaderValue
Header=HeaderName: NewValue
Header=HeaderName: HeaderValue
```

adds "`HeaderName`" header with "`HeaderValue, NewValue`" to each HTTP request.

Added in version 258.

## See Also

systemd-journal-upload.service(8), systemd(1), systemd-journald.service(8)

  

<sup>\[1\]</sup> 💣💥🧨💥💥💣 Please note that those configuration files must be available at all times. If `/usr/local/` is a separate partition, it may not be available during early boot, and must not be used for configuration.
