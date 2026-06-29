# NAME

lpmove - move a job or all jobs to a new destination

# SYNOPSIS

**lpmove** \[ **-h** *server*\[**:***port*\] \] \[ **-E** \] \[ **-U** *username* \] *job* *destination*
**lpmove** \[ **-h** *server*\[**:***port*\] \] \[ **-E** \] \[ **-U** *username* \] *source* *destination*

# DESCRIPTION

**lpmove** moves the specified *job* or all jobs from *source* to *destination*. *job* can be the job ID number or the old destination and job ID.

# OPTIONS

The **lpmove** command supports the following options:

**-E**
Forces encryption when connecting to the server.

**-U** *username*
Specifies an alternate username.

**-h** *server*\[**:***port*\]
Specifies an alternate server. Note: This option must occur before all others.

# EXAMPLES

Move job 123 from "oldprinter" to "newprinter":


        lpmove 123 newprinter

                or

        lpmove oldprinter-123 newprinter

Move all jobs from "oldprinter" to "newprinter":


        lpmove oldprinter newprinter

# SEE ALSO

**cancel**(1), **lp**(1), **lpr**(1), **lprm**(1),
CUPS Online Help (http://localhost:631/help)

# COPYRIGHT

Copyright © 2020-2024 by OpenPrinting.
