# NAME

sane-as6e - SANE backend for using the Artec AS6E parallel port interface scanner.

# DESCRIPTION

The **sane-as6e** library implements a SANE (Scanner Access Now Easy) backend that provides access to Artec AS6E flatbed scanner. It requires the **as6edriver** program in order to operate. The **as6edriver** program is not included with the SANE package. It can be found at *http://as6edriver.sourceforge.net*. See the as6edriver documentation for technical information.

The **as6edriver** program must be in the path for executables (**\$PATH**). Especially if you run **saned**(8) (the SANE network scanning daemon), take care to setup the path for **inetd**(8) or **xinetd**(8) correctly or place the program in a directory that is in the path.

# FILES

**as6edriver** - driver program that controls the scanner.

# SEE ALSO

**sane**(7), **as6edriver**(5), **saned**(8), **inetd**(8), **xinetd**(8)
*http://as6edriver.sourceforge.net*

# AUTHOR

Eugene S. Weiss

# EMAIL-CONTACT

*yossarian@users.sourceforge.net*
