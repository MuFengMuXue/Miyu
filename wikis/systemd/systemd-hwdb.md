## Name

systemd-hwdb — hardware database management tool

## Synopsis

`systemd-hwdb [``options``] update`

`systemd-hwdb [``options``] query `*`modalias`*

## Description

**systemd-hwdb** expects a command and command specific arguments. It manages the binary hardware database.

## Options

`--usr`  
Generate in /usr/lib/udev instead of /etc/udev.

Added in version 219.

`-r`, `--root=`*`PATH`*  
Alternate root path in the filesystem.

Added in version 219.

`-s`, `--strict`  
When updating, return non-zero exit value on any parsing error.

Added in version 239.

`-h`, `--help`  
Print a short help text and exit.

### systemd-hwdb \[*`options`*\] update

Update the binary database.

### systemd-hwdb \[*`options`*\] query *`MODALIAS`* 

Query database and print result.

## See Also

systemd(1) hwdb(7)
