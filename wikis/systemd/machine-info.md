## Name

machine-info — Local machine information file

## Synopsis

`/etc/machine-info`

## Description

The `/etc/machine-info` file contains machine metadata.

The format of `machine-info` is a newline-separated list of environment-like shell-compatible variable assignments, ignoring comments and empty lines. It is possible to source the configuration from shell scripts, however, beyond mere variable assignments no shell features are supported, allowing applications to read the file without implementing a shell compatible execution engine. See os-release(5) for a detailed description of the format.

`/etc/machine-info` contains metadata about the machine that is set by the user or administrator. The settings configured here have the highest precedence. When not set, appropriate values may be determined automatically, based on the information about the hardware or other configuration files. It is thus completely fine for this file to not be present.

You may use hostnamectl(1) to change the settings of this file from the command line.

## Options

The following machine metadata parameters may be set using `/etc/machine-info`:

### Machine Information

`PRETTY_HOSTNAME=`  
A pretty human-readable UTF-8 machine identifier string. This should contain a name like "`Lennart's Laptop`" which is useful to present to the user and does not suffer by the syntax limitations of internet domain names. If possible, the internet hostname as configured in `/etc/hostname` should be kept similar to this one. Example: if this value is "`Lennart's Computer`" an Internet hostname of "`lennarts-computer`" might be a good choice. If this parameter is not set, an application should fall back to the Internet hostname for presentation purposes.

`ICON_NAME=`  
An icon identifying this machine according to the XDG Icon Naming Specification. If this parameter is not set, an application should fall back to "`computer`" or a similar icon name.

`CHASSIS=`  
The chassis type. Currently, the following chassis types are defined: "`desktop`", "`laptop`", "`convertible`", "`server`", "`tablet`", "`handset`", "`watch`", and "`embedded`", as well as the special chassis types "`vm`" and "`container`" for virtualized systems that lack an immediate physical chassis.

Note that most systems allow detection of the chassis type automatically (based on firmware information or suchlike). This setting should only be used to override a misdetection or to manually configure the chassis type where automatic detection is not available.

Added in version 197.

`DEPLOYMENT=`  
Describes the system deployment environment. One of the following is suggested: "`development`", "`integration`", "`staging`", "`testing`", "`production`".

Added in version 216.

`LOCATION=`  
Describes the system location if applicable and known. Takes a human-friendly, free-form string. This may be as generic as "`Berlin, Germany`" or as specific as "`Left Rack, 2nd Shelf`".

Added in version 216.

`HARDWARE_VENDOR=`  
Specifies the hardware vendor. If unspecified, the hardware vendor set in DMI or hwdb(7) will be used.

Added in version 251.

`HARDWARE_MODEL=`  
Specifies the hardware model. If unspecified, the hardware model set in DMI or hwdb(7) will be used.

Added in version 251.

`HARDWARE_SKU=`  
Specifies the hardware SKU (Stock-Keeping Unit). If unspecified, the hardware SKU set in DMI will be used.

Added in version 258.

`HARDWARE_VERSION=`  
Specifies the hardware version. If unspecified, the hardware version set in DMI will be used.

Added in version 258.

### Custom Fields

Operating system vendors and systemd administrators may extend the file format and introduce new fields. It is highly recommended to prefix new fields with an OS-specific name in order to avoid name clashes. Applications reading this file must ignore unknown fields.

Example: "`_LOCAL_EMERGENCY_CONTACT="user@example.org"`".

## Example

``` programlisting
PRETTY_HOSTNAME="Lennart's Tablet"
ICON_NAME=computer-tablet
CHASSIS=tablet
DEPLOYMENT=production
```

## See Also

systemd(1), os-release(5), hostname(5), machine-id(5), hostnamectl(1), systemd-hostnamed.service(8)
