# Scp

copies files between hosts on a network.

uses the SFTP protocol over an

connection for data transfer, and uses the same authentication and provides the same security as a login session.

will ask for passwords or passphrases if they are needed for authentication.

The

and

may be specified as a local pathname, a remote host with optional path in the form

or a URI in the form

Local file names can be made explicit using absolute or relative pathnames to avoid

treating file names containing

as host specifiers.

When copying between two remote hosts, if the URI format is used, a

cannot be specified on the

if the

option is used.

The options are as follows:

Copies between two remote hosts are transferred through the local host. This mode is the default, but see also the

option for copying data directly between two remote hosts. Note that when using the legacy SCP protocol (via the

flag), this option selects batch mode for the second host as

cannot ask for passwords or passphrases for both hosts.

Forces

to use IPv4 addresses only.

Forces

to use IPv6 addresses only.

Allows forwarding of

to the remote system. The default is not to forward an authentication agent.

Selects batch mode (prevents asking for passwords or passphrases).

Compression enable. Passes the

flag to

to enable compression.

Selects the cipher to use for encrypting the data transfer. This option is directly passed to

Connect directly to a local SFTP server program rather than a remote one via

This option may be useful in debugging the client and server.

Specifies an alternative per-user configuration file for

This option is directly passed to

Selects the file from which the identity (private key) for public key authentication is read. This option is directly passed to

Connect to the target host by first making an

connection to the jump host described by

and then establishing a TCP forwarding to the ultimate destination from there. Multiple jump hops may be specified separated by comma characters. This is a shortcut to specify a

configuration directive. This option is directly passed to

Limits the used bandwidth, specified in Kbit/s.

Use the legacy SCP protocol for file transfers instead of the SFTP protocol. Forcing the use of the SCP protocol may be necessary for servers that do not implement SFTP, for backwards-compatibility for particular filename wildcard patterns and for expanding paths with a

prefix for older SFTP servers.

Can be used to pass options to

in the format used in

This is useful for specifying options for which there is no separate

command-line flag. For full details of the options listed below, and their possible values, see

Specifies the port to connect to on the remote host. Note that this option is written with a capital

because

is already reserved for preserving the times and mode bits of the file.

Preserves modification times, access times, and file mode bits from the source file.

Quiet mode: disables the progress meter as well as warning and diagnostic messages from

Copies between two remote hosts are transferred through the local host by default. This option instead copies between two remote hosts by connecting to the origin host and executing

there. This requires that

running on the origin host can authenticate to the destination host without requiring a password.

Recursively copy entire directories. Note that

follows symbolic links encountered in the tree traversal.

Name of

to use for the encrypted connection. The program must understand

options.

Disable strict filename checking. By default when copying files from a remote host to a local directory

checks that the received filenames match those requested on the command-line to prevent the remote end from sending unexpected or unwanted files. Because of differences in how various operating systems and shells interpret filename wildcards, these checks may cause wanted files to be rejected. This option disables these checks at the expense of fully trusting that the server will not send unexpected filenames.

Verbose mode. Causes

and

to print debugging messages about their progress. This is helpful in debugging connection, authentication, and configuration problems.

Specify an option that controls aspects of SFTP protocol behaviour. The valid options are:

Controls how many concurrent SFTP read or write requests may be in progress at any point in time during a download or upload. By default 64 requests may be active concurrently.

Controls the maximum buffer size for a single SFTP read/write operation used during download or upload. By default a 32KB buffer is used.

is based on the rcp program in

source code from the Regents of the University of California.

Since OpenSSH 9.0,

has used the SFTP protocol for transfers by default.

The legacy SCP protocol (selected by the

flag) requires execution of the remote user's shell to perform

pattern matching. This requires careful quoting of any characters that have special meaning to the remote shell, such as quote characters.
