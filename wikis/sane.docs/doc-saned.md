# NAME

saned - SANE network daemon

# SYNOPSIS

**saned** **\[ -a** *\[ username \]* **\]** **\[ -u** *username* **\]** **\[ -b** *address* **\]** **\[ -p** *port* **\]** **\[ -l \]** **\[ -D \]** **\[ -o \]** **\[ -d** *n* **\]** **\[ -e \]** **\[ -h \]** **\[ -B** *buffer-size* **\]**

# DESCRIPTION

**saned** is the SANE (Scanner Access Now Easy) daemon that allows remote clients to access image acquisition devices available on the local host.

# OPTIONS

**saned** recognises the following options:

**-a** *\[username\]*, **--alone**\[=*username\]*
is equivalent to the combination of **-l -D -u** *username* options. However, *username* is optional and running user will only be set when specified.


**-u** *username*, **--user**=*username*
requests that **saned** drop root privileges and run as the user (and group) associated with *username* after binding.


**-b** *address*, **--bind**=*address*
tells **saned** to bind to the *address* given.


**-p** *port*, **--port=*port***
tells **saned** to listen on the *port* given. A value of 0 tells **saned** to pick an unused port. The default is the **sane-port (6566).**


**-l**, **--listen**
requests that **saned** run in standalone daemon mode. In this mode, **saned** will listen for incoming client connections; **inetd**(8) is not required for **saned** operations in this mode.


**-D**, **--daemonize**
will request **saned** to detach from the console and run in the background.


**-n**, **--allow-network**
allows **saned** to use network scanners. By default this is forbidden to prevent **saned** from contacting itself. When enabled, the configuration of the **sane-net**(5) backend should not mention the address on which **saned** is listening.


**-o**, **--once**
requests that **saned** exits after the first client disconnects. This is useful for debugging.


**-d** *n*, **--debug**=*n*
sets the level of **saned** debug output to *n*. When compiled with debugging enabled, this flag may be followed by a number to request more or less debug info. The larger the number, the more verbose the debug output. E.g., **-d128** will request output of all debug info. A level of 0 produces no output at all. The default value is 2.


**-e**, **--stderr**
will divert **saned** debug output to stderr instead of the syslog default.


**-B**, **--buffer-size=*buffer-size***
specifies the size of the read buffer used for communication with the backend in KB. Default value is 1MB.


**-h**, **--help**
displays a short help message.

# CONFIGURATION

The *saned.conf* configuration file contains both options for the daemon and the access list.

**data_portrange** = *min_port* - *max_port*
Specify the port range to use for the data connection. Pick a port range between 1024 and 65535; don't pick a too large port range, as it may have performance issues. Use this option if your **saned** server is sitting behind a firewall. If that firewall is a Linux machine, we strongly recommend using the Netfilter *nf_conntrack_sane* module instead.

**data_connect_timeout** = *timeout*
Specify the time in milliseconds that **saned** will wait for a data connection. Without this option, if the data connection is not done before the scanner reaches the end of scan, the scanner will continue to scan past the end and may damage it depending on the backend. Specify zero to have the old behavior. The default is 4000ms.

The access list is a list of host names, IP addresses or IP subnets (CIDR notation) that are permitted to use local SANE devices. IPv6 addresses must be enclosed in brackets, and should always be specified in their compressed form. Connections from localhost are always permitted. Empty lines and lines starting with a hash mark (#) are ignored. A line containing the single character \`\`+'' is interpreted to match any hostname. This allows any remote machine to use your scanner and may present a security risk, so this shouldn't be used unless you know what you're doing.

A sample configuration file is shown below:

> \# Daemon options
> data_portrange = 10000 - 10100
> \# Access list
> scan-client.somedomain.firm
> \# this is a comment
> 192.168.0.1
> 192.168.2.12/29
> \[::1\]
> \[2001:db8:185e::42:12\]/64

The case of the host names does not matter, so AHost.COM is considered identical to ahost.com.

# FILES

*/etc/hosts.equiv*
The hosts listed in this file are permitted to access all local SANE devices. Caveat: this file imposes serious security risks and its use is not recommended.

*@CONFIGDIR@/saned.conf*
Contains a list of hosts permitted to access local SANE devices (see also description of **SANE_CONFIG_DIR** below).

*@CONFIGDIR@/saned.users*
If this file contains lines of the form

user:password:backend

access to the listed backends is restricted. A backend may be listed multiple times for different user/password combinations. The server uses MD5 hashing if supported by the client.

# ENVIRONMENT

**SANE_CONFIG_DIR**
This environment variable specifies the list of directories that may contain the configuration file. On \*NIX systems, the directories are separated by a colon (\`:'), under OS/2, they are separated by a semi-colon (\`;'). If this variable is not set, the configuration file is searched in two default directories: first, the current working directory (".") and then in *@CONFIGDIR@*. If the value of the environment variable ends with the directory separator character, then the default directories are searched after the explicitly specified directories. For example, setting **SANE_CONFIG_DIR** to "/tmp/config:" would result in directories *tmp/config*, *.*, and *@CONFIGDIR@* being searched (in this order).

# NOTES

**saned** does *not* provide confidentiality when communicating with clients. If **saned** is exposed directly on the network, other users may be able to intercept scanned images, or learn passwords for connecting to **saned**, with little effort. Client systems should connect to **saned** through a secure tunnel to the server instead.

**saned** is not a trusted program and should not run with root privileges.

Refer to *@DOCDIR@/saned/saned.install.md* for details on configuring **saned** as a service.

# SEE ALSO

**sane**(7), **scanimage**(1), **xscanimage**(1), **xcam**(1), **sane-dll**(5), **sane-net**(5), **sane-"backendname"**(5), **inetd**(8), **xinetd**(8), **systemd**(1)
*http://www.penguin-breeder.org/?page=sane-net*

# AUTHOR

David Mosberger
