# Docs Xml / Manpages / testparm.1

testparm

1

Samba

User Commands

testparm

check an smb.conf configuration file for internal correctness

testparm

-s\|--suppress-prompt

-v\|--verbose

-?\|--help

--usage

-d\|--debuglevel=DEBUGLEVEL

--debug-stdout

config filename

hostname hostIP

# DESCRIPTION

This tool is part of the `samba(7)` suite.

`testparm` is a very simple test program to check an `smbd(8)` configuration file for internal correctness. If this program reports no problems, you can use the configuration file with confidence that `smbd` will successfully load the configuration file.

Note that this is *NOT* a guarantee that the services specified in the configuration file will be available or will operate as expected.

If the optional host name and host IP address are specified on the command line, this test program will run through the service entries reporting whether the specified host has access to each service.

If `testparm` finds an error in the `smb.conf` file it returns an exit code of 1 to the calling program, else it returns an exit code of 0. This allows shell scripts to test the output from `testparm`.

# OPTIONS

-s\|--suppress-prompt
Without this option, `testparm` will prompt for a carriage return after printing the service names and before dumping the service definitions.

-v\|--verbose
If this option is specified, testparm will also output all options that were not used in `smb.conf(5)` and are thus set to their defaults.

--parameter-name parametername
Dumps the named parameter. If no section-name is set the view is limited by default to the global section. It is also possible to dump a parametrical option. Therefore the option has to be separated by a colon from the parametername.

--section-name sectionname
Dumps the named section.

--show-all-parameters
Show the parameters, type, possible values.

-l\|--skip-logic-checks
Skip the global checks.

configfilename
This is the name of the configuration file to check. If this parameter is not present then the default `smb.conf(5)` file will be checked.

hostname
If this parameter and the following are specified, then `testparm` will examine the `hosts allow` and `hosts deny` parameters in the `smb.conf(5)` file to determine if the hostname with this IP address would be allowed access to the `smbd` server. If this parameter is supplied, the hostIP parameter must also be supplied.

hostIP
This is the IP address of the host specified in the previous parameter. This address must be supplied if the hostname parameter is supplied.

# FILES

`smb.conf(5)`
This is usually the name of the configuration file used by `smbd(8)`.

# DIAGNOSTICS

The program will issue a message saying whether the configuration file loaded OK or not. This message may be preceded by errors and warnings if the file did not load. If the file was loaded OK, the program then dumps all known service details to stdout.

For certain use cases, SMB protocol requires use of cryptographic algorithms which are known to be weak and already broken. DES and ARCFOUR (RC4) ciphers and the SHA1 and MD5 hash algorithms are considered weak but they are required for backward compatibility. The testparm utility shows whether the Samba tools will fall back to these weak crypto algorithms if it is not possible to use strong cryptography by default. In FIPS mode weak crypto cannot be enabled.

# VERSION

This man page is part of version of the Samba suite.

# SEE ALSO

`smb.conf(5)`, `smbd(8)`

# AUTHOR

The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed.
