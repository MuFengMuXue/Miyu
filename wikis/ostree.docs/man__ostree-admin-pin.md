## Name

ostree-admin-pin — Explicitly retain deployment at a given index

## Synopsis

`ostree admin pin` {INDEX}

## Description

Ensures the deployment at `INDEX`, will not be garbage collected by default. This is termed "pinning". If the `-u` option is provided, undoes a pinning operation. `INDEX` can be \>= 0 or one of booted, pending or rollback strings.

## Options

`--unpin`,`-u`  
Undoes a pinning operation.
