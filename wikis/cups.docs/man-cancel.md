# NAME

cancel - cancel jobs

# SYNOPSIS

**cancel** \[ **-h** *hostname\[:port\]* \] \[ **-E** \] \[ **-U** *username* \] \[ **-a** \] \[ **-u** *username* \] \[ **-x** \] \[ *id* \] \[ *destination* \] \[ *destination-id* \]

# DESCRIPTION

The **cancel** command cancels print jobs. If no *destination* or *id* is specified, the currently printing job on the default destination is canceled.

# OPTIONS

The following options are recognized by **cancel**:

**-a**
Cancel all jobs on the named destination, or all jobs on all destinations if none is provided.

**-E**
Forces encryption when connecting to the server.

**-h** *hostname*\[*:port*\]
Specifies an alternate server. Note: This option must occur before all others.

**-U** *username*
Specifies the username to use when connecting to the server.

**-u** *username*
Cancels jobs owned by *username*.

**-x**
Deletes job data files in addition to canceling.

# CONFORMING TO

Unlike the System V printing system, CUPS allows printer names to contain any printable character except SPACE, TAB, "/", or "#". Also, printer and class names are *not* case-sensitive.

# EXAMPLES

Cancel the current print job:


        cancel

Cancel job "myprinter-42":


        cancel myprinter-42

Cancel all jobs:


        cancel -a

# NOTES

The **-a** and **-u*** username* options require administrative access. These restrictions are part of the operation policies defined in the **cupsd.conf**(5) file for the "Cancel-Jobs" and "Cancel-My-Jobs" operations, respectively.

# SEE ALSO

**cupsd.conf**(5), **lp**(1), **lpmove**(8), **lpstat**(1), CUPS Online Help (http://localhost:631/help)

# COPYRIGHT

Copyright © 2020-2024 by OpenPrinting.
