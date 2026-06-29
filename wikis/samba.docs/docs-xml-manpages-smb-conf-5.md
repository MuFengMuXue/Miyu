# Docs Xml / Manpages / smb.conf.5

smb.conf

5

Samba

File Formats and Conventions

smb.conf

The configuration file for the Samba suite

# SYNOPSIS

The `smb.conf` file is a configuration file for the Samba suite. `smb.conf` contains runtime configuration information for the Samba programs. The complete description of the file format and possible parameters held within are here for reference purposes.

# HOW CONFIGURATION CHANGES ARE APPLIED

The Samba suite includes a number of different programs. Some of them operate in a client mode, others are server daemons that provide various services to its clients. The `smb.conf` file is processed in the following way:

- The Samba suite's client applications read their configuration only once. Any changes made after start aren't reflected in the context of already running client code.

- The Samba suite's server daemons reload their configuration when requested. However, already active connections do not change their configuration. More detailed information can be found in `smbd(8)` and `winbindd(8)` manual pages.

To request Samba server daemons to refresh their configuration, please use `smbcontrol(1)` utility.

# FILE FORMAT

The file consists of sections and parameters. A section begins with the name of the section in square brackets and continues until the next section begins. Sections contain parameters of the form:

    name = value

The file is line-based - that is, each newline-terminated line represents either a comment, a section name or a parameter.

Section and parameter names are not case sensitive.

Only the first equals sign in a parameter is significant. Whitespace before or after the first equals sign is discarded. Leading, trailing and internal whitespace in section and parameter names is irrelevant. Leading and trailing whitespace in a parameter value is discarded. Internal whitespace within a parameter value is retained verbatim.

Any line beginning with a semicolon (“;”) or a hash (“\#”) character is ignored, as are lines containing only whitespace.

Any line ending in a “`\`” is continued on the next line in the customary UNIX fashion.

The values following the equals sign in parameters are all either a string (no quotes needed) or a boolean, which may be given as yes/no, 1/0 or true/false. Case is not significant in boolean values, but is preserved in string values. Some items such as create masks are numeric.

# SECTION DESCRIPTIONS

Each section in the configuration file (except for the \[global\] section) describes a shared resource (known as a “share”). The section name is the name of the shared resource and the parameters within the section define the shares attributes.

There are three special sections, \[global\], \[homes\] and \[printers\], which are described under *special sections*. The following notes apply to ordinary section descriptions.

A share consists of a directory to which access is being given plus a description of the access rights which are granted to the user of the service. Some housekeeping options are also specifiable.

Sections are either file share services (used by the client as an extension of their native file systems) or printable services (used by the client to access print services on the host running the server).

Sections may be designated *guest* services, in which case no password is required to access them. A specified UNIX *guest account* is used to define access privileges in this case.

Sections other than guest services will require a password to access them. The client provides the username. As older clients only provide passwords and not usernames, you may specify a list of usernames to check against the password using the `user =` option in the share definition. For modern clients such as Windows 95/98/ME/NT/2000, this should not be necessary.

The access rights granted by the server are masked by the access rights granted to the specified or guest UNIX user by the host system. The server does not grant more access than the host system grants.

The following sample section defines a file space share. The user has write access to the path `/home/bar`. The share is accessed via the share name `foo`:


        /home/bar
        no

The following sample section defines a printable share. The share is read-only, but printable. That is, the only write access permitted is via calls to open, write to and close a spool file. The *guest ok* parameter means access will be permitted as the default guest user (specified elsewhere):


        /var/tmp
        yes
        yes
        yes

# SPECIAL SECTIONS

## The \[global\] section

Parameters in this section apply to the server as a whole, or are defaults for sections that do not specifically define certain items. See the notes under PARAMETERS for more information.

## The \[homes\] section

If a section called \[homes\] is included in the configuration file, services connecting clients to their home directories can be created on the fly by the server.

When the connection request is made, the existing sections are scanned. If a match is found, it is used. If no match is found, the requested section name is treated as a username and looked up in the local password file. If the name exists and the correct password has been given, a share is created by cloning the \[homes\] section.

Some modifications are then made to the newly created share:

- The share name is changed from homes to the located username.

- If no path was given, the path is set to the user's home directory.

If you decide to use a *path =* line in your \[homes\] section, it may be useful to use the %S macro. For example:

    path = /data/pchome/%S

is useful if you have different home directories for your PCs than for UNIX access.

This is a fast and simple way to give a large number of clients access to their home directories with a minimum of fuss.

A similar process occurs if the requested section name is “homes”, except that the share name is not changed to that of the requesting user. This method of using the \[homes\] section works well if different users share a client PC.

The \[homes\] section can specify all the parameters a normal service section can specify, though some make more sense than others. The following is a typical and suitable \[homes\] section:

    no

An important point is that if guest access is specified in the \[homes\] section, all home directories will be visible to all clients *without a password*. In the very unlikely event that this is actually desirable, it is wise to also specify *read only access*.

The *browseable* flag for auto home directories will be inherited from the global browseable flag, not the \[homes\] browseable flag. This is useful as it means setting *browseable = no* in the \[homes\] section will hide the \[homes\] share but make any auto home directories visible.

## The \[printers\] section

This section works like \[homes\], but for printers.

If a \[printers\] section occurs in the configuration file, users are able to connect to any printer specified in the local host's printcap file.

When a connection request is made, the existing sections are scanned. If a match is found, it is used. If no match is found, but a \[homes\] section exists, it is used as described above. Otherwise, the requested section name is treated as a printer name and the appropriate printcap file is scanned to see if the requested section name is a valid printer share name. If a match is found, a new printer share is created by cloning the \[printers\] section.

A few modifications are then made to the newly created share:

- The share name is set to the located printer name

- If no printer name was given, the printer name is set to the located printer name

- If the share does not permit guest access and no username was given, the username is set to the located printer name.

The \[printers\] service MUST be printable - if you specify otherwise, the server will refuse to load the configuration file.

Typically the path specified is that of a world-writeable spool directory with the sticky bit set on it. A typical \[printers\] entry looks like this:

    /var/tmp
    yes
    yes

All aliases given for a printer in the printcap file are legitimate printer names as far as the server is concerned. If your printing subsystem doesn't work like that, you will have to set up a pseudo-printcap. This is a file consisting of one or more lines like this:

    alias|alias|alias|alias...

Each alias should be an acceptable printer name for your printing subsystem. In the \[global\] section, specify the new file as your printcap. The server will only recognize names found in your pseudo-printcap, which of course can contain whatever aliases you like. The same technique could be used simply to limit access to a subset of your local printers.

An alias, by the way, is defined as any component of the first entry of a printcap record. Records are separated by newlines, components (if there are more than one) are separated by vertical bar symbols (`|`).

> [!NOTE]
> On SYSV systems which use lpstat to determine what printers are defined on the system you may be able to use `printcap name = lpstat` to automatically obtain a list of printers. See the `printcap name` option for more details.

# USERSHARES

Starting with Samba version 3.0.23 the capability for non-root users to add, modify, and delete their own share definitions has been added. This capability is called *usershares* and is controlled by a set of parameters in the \[global\] section of the smb.conf. The relevant parameters are :

usershare allow guests
Controls if usershares can permit guest access.

usershare max shares
Maximum number of user defined shares allowed.

usershare owner only
If set only directories owned by the sharing user can be shared.

usershare path
Points to the directory containing the user defined share definitions. The filesystem permissions on this directory control who can create user defined shares.

usershare prefix allow list
Comma-separated list of absolute pathnames restricting what directories can be shared. Only directories below the pathnames in this list are permitted.

usershare prefix deny list
Comma-separated list of absolute pathnames restricting what directories can be shared. Directories below the pathnames in this list are prohibited.

usershare template share
Names a pre-existing share used as a template for creating new usershares. All other share parameters not specified in the user defined share definition are copied from this named share.

To allow members of the UNIX group `foo` to create user defined shares, create the directory to contain the share definitions as follows:

Become root:

    mkdir /usr/local/samba/lib/usershares
    chgrp foo /usr/local/samba/lib/usershares
    chmod 1770 /usr/local/samba/lib/usershares

Then add the parameters

        /usr/local/samba/lib/usershares
        10 # (or the desired number of shares)

to the global section of your `smb.conf`. Members of the group foo may then manipulate the user defined shares using the following commands.

net usershare add sharename path \[comment\] \[acl\] \[guest_ok=\[y\|n\]\]
To create or modify (overwrite) a user defined share.

net usershare delete sharename
To delete a user defined share.

net usershare list wildcard-sharename
To list user defined shares.

net usershare info wildcard-sharename
To print information about user defined shares.

# PARAMETERS

Parameters define the specific attributes of sections.

Some parameters are specific to the \[global\] section (e.g., *security*). Some parameters are usable in all sections (e.g., *create mask*). All others are permissible only in normal sections. For the purposes of the following descriptions the \[homes\] and \[printers\] sections will be considered normal. The letter *G* in parentheses indicates that a parameter is specific to the \[global\] section. The letter *S* indicates that a parameter can be specified in a service specific section. All *S* parameters can also be specified in the \[global\] section - in which case they will define the default behavior for all services.

Parameters are arranged here in alphabetical order - this may not create best bedfellows, but at least you can find them! Where there are synonyms, the preferred synonym is described, others refer to the preferred synonym.

# VARIABLE SUBSTITUTIONS

Many of the strings that are settable in the config file can take substitutions. For example the option “path = /tmp/%u” is interpreted as “path = /tmp/john” if the user connected with the username john.

These substitutions are mostly noted in the descriptions below, but there are some general substitutions which apply whenever they might be relevant. These are:

%U
session username (the username that the client wanted, not necessarily the same as the one they got).

%G
primary group name of %U.

%h
the Internet hostname that Samba is running on.

%m
the NetBIOS name of the client machine (very useful).

This parameter is not available when Samba listens on port 445, as clients no longer send this information. If you use this macro in an include statement on a domain that has a Samba domain controller be sure to set in the \[global\] section `server smb transports = 139`. This will cause Samba to not listen on port 445 and will permit include functionality to function as it did with Samba 2.x.

%L
the NetBIOS name of the server. This allows you to change your config based on what the client calls you. Your server can have a “dual personality”.

%M
the Internet name of the client machine.

%R
the selected protocol level after protocol negotiation. It can be one of CORE, COREPLUS, LANMAN1, LANMAN2, NT1, SMB2_02, SMB2_10, SMB3_00, SMB3_02, SMB3_11 or SMB2_FF.

%d
the process id of the current server process.

%a
The architecture of the remote machine. It currently recognizes Samba (`Samba`), the Linux CIFS file system (`CIFSFS`), OS/2, (`OS2`), Mac OS X (`OSX`), Windows for Workgroups (`WfWg`), Windows 9x/ME (`Win95`), Windows NT (`WinNT`), Windows 2000 (`Win2K`), Windows XP (`WinXP`), Windows XP 64-bit(`WinXP64`), Windows 2003 including 2003R2 (`Win2K3`), and Windows Vista (`Vista`). Anything else will be known as `UNKNOWN`.

%I
the IP address of the client machine.

Before 4.0.0 it could contain IPv4 mapped IPv6 addresses, now it only contains IPv4 or IPv6 addresses.

%J
the IP address of the client machine, colons/dots replaced by underscores.

%i
the local IP address to which a client connected.

Before 4.0.0 it could contain IPv4 mapped IPv6 addresses, now it only contains IPv4 or IPv6 addresses.

%j
the local IP address to which a client connected, colons/dots replaced by underscores.

%T
the current date and time.

%t
the current date and time in a minimal format without colons (YYYYYmmdd_HHMMSS).

%D
name of the domain or workgroup of the current user.

%w
the winbind separator.

%\$(\<envvar\>)
the value of the environment variable \<envar\>.

The following substitutes apply only to some configuration options (only those that are used when a connection has been established):

%S
the name of the current service, if any.

%P
the root directory of the current service, if any.

%u
username of the current service, if any.

%g
primary group name of %u.

%H
the home directory of the user given by %u.

%N
This value is the same as %L.

There are some quite creative things that can be done with these substitutions and other `smb.conf` options.

# NAME MANGLING

Samba supports `name mangling` so that DOS and Windows clients can use files that don't conform to the 8.3 format. It can also be set to adjust the case of 8.3 format filenames.

There are several options that control the way mangling is performed, and they are grouped here rather than listed separately. For the defaults look at the output of the testparm program.

These options can be set separately for each service.

The options are:

case sensitive = yes/no/auto
controls whether filenames are case sensitive. If they aren't, Samba must do a filename search and match on passed names. The default setting of auto allows clients that support case sensitive filenames (Linux CIFSVFS and smbclient 3.0.5 and above currently) to tell the Samba server on a per-packet basis that they wish to access the file system in a case-sensitive manner (to support UNIX case sensitive semantics). No Windows or DOS system supports case-sensitive filename so setting this option to auto is the same as setting it to no for them. Default *auto*.

default case = upper/lower
controls what the default case is for new filenames (ie. files that don't currently exist in the filesystem). Default *lower*. IMPORTANT NOTE: As part of the optimizations for directories containing large numbers of files, the following special case applies. If the options yes, No, and No are set, then the case of *all* incoming client filenames, not just new filenames, will be modified. See additional notes below.

preserve case = yes/no
controls whether new files (ie. files that don't currently exist in the filesystem) are created with the case that the client passes, or if they are forced to be the `default` case. Default *yes*.

short preserve case = yes/no
controls if new files (ie. files that don't currently exist in the filesystem) which conform to 8.3 syntax, that is all in upper case and of suitable length, are created upper case, or if they are forced to be the `default` case. This option can be used with `preserve case = yes` to permit long filenames to retain their case, while short names are lowercased. Default *yes*.

By default, Samba 3.0 has the same semantics as a Windows NT server, in that it is case insensitive but case preserving. As a special case for directories with large numbers of files, if the case options are set as follows, "case sensitive = yes", "case preserve = no", "short preserve case = no" then the "default case" option will be applied and will modify all filenames sent from the client when accessing this share.

# REGISTRY-BASED CONFIGURATION

Starting with Samba version 3.2.0, the capability to store Samba configuration in the registry is available. The configuration is stored in the registry key *`HKLM\Software\Samba\smbconf`*. There are two levels of registry configuration:

1.  Share definitions stored in registry are used. This is triggered by setting the global parameter `registry shares` to “yes” in *smb.conf*.

    The registry shares are loaded not at startup but on demand at runtime by *smbd*. Shares defined in *smb.conf* take priority over shares of the same name defined in registry.

2.  Global *smb.conf* options stored in registry are used. This can be activated in two different ways:

    Firstly, a registry only configuration is triggered by setting registry in the \[global\] section of *smb.conf*. This resets everything that has been read from config files to this point and reads the content of the global configuration section from the registry. This is the recommended method of using registry based configuration.

    Secondly, a mixed configuration can be activated by a special new meaning of the parameter registry in the \[global\] section of *smb.conf*. This reads the global options from registry with the same priorities as for an include of a text file. This may be especially useful in cases where an initial configuration is needed to access the registry.

    Activation of global registry options automatically activates registry shares. So in the registry only case, shares are loaded on demand only.

Note: To make registry-based configurations foolproof at least to a certain extent, the use of `lock directory` and `config backend` inside the registry configuration has been disabled: Especially by changing the `lock directory` inside the registry configuration, one would create a broken setup where the daemons do not see the configuration they loaded once it is active.

The registry configuration can be accessed with tools like *regedit* or *net (rpc) registry* in the key *`HKLM\Software\Samba\smbconf`*. More conveniently, the *conf* subcommand of the `net(8)` utility offers a dedicated interface to read and write the registry based configuration locally, i.e. directly accessing the database file, circumventing the server.

# IDENTITY MAPPING CONSIDERATIONS

In the SMB protocol, users, groups, and machines are represented by their security identifiers (SIDs). On POSIX system Samba processes need to run under corresponding POSIX user identities and with supplemental POSIX groups to allow access to the files owned by those users and groups. The process of mapping SIDs to POSIX users and groups is called *IDENTITY MAPPING* or, in short, *ID MAPPING*.

Samba supports multiple ways to map SIDs to POSIX users and groups. The configuration is driven by the option which allows one to specify identity mapping (idmap) options for each domain separately.

Identity mapping modules implement different strategies for mapping of SIDs to POSIX user and group identities. They are applicable to different use cases and scenarios. It is advised to read the documentation of the individual identity mapping modules before choosing a specific scenario to use. Each identity management module is documented in a separate manual page. The standard idmap backends are tdb (`idmap_tdb(8)`), tdb2 (`idmap_tdb2(8)`), ldap (`idmap_ldap(8)`), rid (`idmap_rid(8)`), hash (`idmap_hash(8)`), autorid (`idmap_autorid(8)`), ad (`idmap_ad(8)`), nss (`idmap_nss(8)`), and rfc2307 (`idmap_rfc2307(8)`).

Overall, ID mapping configuration should be decided carefully. Changes to the already deployed ID mapping configuration may create the risk of losing access to the data or disclosing the data to the wrong parties.

This example shows how to configure two domains with `idmap_rid(8)`, the principal domain and a trusted domain, leaving the default id mapping scheme at tdb.

        [global]
        security = domain
        workgroup = MAIN

        idmap config * : backend        = tdb
        idmap config * : range          = 1000000-1999999

        idmap config MAIN : backend     = rid
        idmap config MAIN : range       = 5000000-5999999

        idmap config TRUSTED : backend  = rid
        idmap config TRUSTED : range    = 6000000-6999999

# EXPLANATION OF EACH PARAMETER

# WARNINGS

Although the configuration file permits service names to contain spaces, your client software may not. Spaces will be ignored in comparisons anyway, so it shouldn't be a problem - but be aware of the possibility.

On a similar note, many clients - especially DOS clients - limit service names to eight characters. `smbd(8)` has no such limitation, but attempts to connect from such clients will fail if they truncate the service names. For this reason you should probably keep your service names down to eight characters in length.

Use of the `[homes]` and `[printers]` special sections make life for an administrator easy, but the various combinations of default attributes can be tricky. Take extreme care when designing these sections. In particular, ensure that the permissions on spool directories are correct.

# VERSION

This man page is part of version of the Samba suite.

# SEE ALSO

`samba(7)`, `smbpasswd(8)`, `smbd(8)`, `nmbd(8)`, `winbindd(8)`, `samba(8)`, `samba-tool(8)`, `smbclient(1)`, `nmblookup(1)`, `testparm(1)`.

# AUTHOR

The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed.
