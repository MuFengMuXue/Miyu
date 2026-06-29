# NAME

sane-net - SANE network backend

# DESCRIPTION

The **sane-net** library implements a SANE (Scanner Access Now Easy) backend that provides access to image acquisition devices through a network connection. This makes it possible to control devices attached to a remote host and also provides a means to grant users access to protected resources.

# DEVICE NAMES

This backend expects device names of the form:

> *host*:*device*

Where *host* is the name (or IP address) of the (remote) host and *device* is the name of the device on this host that should be addressed. If the device name does not contain a colon (:), then the entire string is treated as the *device* string for the default host. The default host is the host listed last in the configuration file (see below).

An IPv6 address can be specified enclosed in square brackets:

> *\[::1\]*:*device*

# CONFIGURATION

The *net.conf* file contains both backend options and a list of host names (or IP addresses) that should be contacted for scan requests. Anything that isn't one of the options listed below will be treated as an host name.

**connect_timeout = nsecs**
Timeout (in seconds) for the initial connection to the **saned**(8) server. This will prevent the backend from blocking for several minutes trying to connect to an unresponsive **saned**(8) host (network outage, host down, ...). The environment variable **SANE_NET_TIMEOUT** can also be used to specify the timeout at runtime.

Empty lines and lines starting with a hash mark (#) are ignored. Note that IPv6 addresses in this file do not need to be enclosed in square brackets. A sample configuration file is shown below:

> scan-server.somedomain.firm
> 192.168.0.1
> \# this is a comment
> localhost
> ::1

The above list of hosts can be extended at run-time using environment variable **SANE_NET_HOSTS**. This environment variable is a colon-separated list of hostnames or IP addresses that should be contacted in addition to the hosts mentioned in the configuration file. For example, a user could set the environment variable to the string:

> new.scanner.com:\[::1\]:192.168.0.2:scanner.univ.edu

To request that hosts *new.scanner.com* , *\[::1\]* , *192.168.0.2* and *scanner.univ.edu* are contacted in addition to the hosts listed above.

For this backend to function properly, it is also necessary to define the **sane-port** service in */etc/services* using a line of the following form:

> sane-port 6566/tcp \# SANE network scanner daemon

# FILES

*@CONFIGDIR@/net.conf*
The backend configuration file (see also description of **SANE_CONFIG_DIR** below).

*@LIBDIR@/libsane-net.a*
The static library implementing this backend.

*@LIBDIR@/libsane-net.so*
The shared library implementing this backend (present on systems that support dynamic loading).

# ENVIRONMENT

**SANE_CONFIG_DIR**
This environment variable specifies the list of directories that may contain the configuration file. On \*NIX systems, the directories are separated by a colon (\`:'), under OS/2, they are separated by a semi-colon (\`;'). If this variable is not set, the configuration file is searched in two default directories: first, the current working directory (".") and then in *@CONFIGDIR@*. If the value of the environment variable ends with the directory separator character, then the default directories are searched after the explicitly specified directories. For example, setting **SANE_CONFIG_DIR** to "/tmp/config:" would result in directories *tmp/config*, *.*, and *@CONFIGDIR@* being searched (in this order).

**SANE_NET_HOSTS**
A colon-separated list of host names or IP addresses to be contacted by this backend.

**SANE_NET_TIMEOUT**
Number of seconds to wait for a response from the **saned**(8) server for the initial connection request.

**SANE_DEBUG_NET**
If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. E.g., a value of 128 requests all debug output to be printed. Smaller levels reduce verbosity.

# BUGS

If **saned**(8) has timed out, the net backend may loop with authorization requests.

# SEE ALSO

**sane**(7), **saned**(8), **sane-dll**(5), **scanimage**(1)

*http://www.penguin-breeder.org/?page=sane-net*

# AUTHOR

David Mosberger and Andreas Beck
