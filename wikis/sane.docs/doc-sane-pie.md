# NAME

sane-pie - SANE backend for PIE, Devcom and AdLib SCSI flatbed scanners

# DESCRIPTION

The **sane-pie** library implements a SANE (Scanner Access Now Easy) backend that provides access to PIE, Devcom and AdLib SCSI flatbed scanners.
At present, the following scanners should work with this backend:

    Model:                  Status
    ----------------------  ------
    Devcom 9636PRO          OK
    Devcom 9636S            Untested
    Devcom 9630S            Untested
    ScanAce 1236S           Untested
    ScanAce 1230S           Untested
    ScanAce II              Untested
    ScanAce III             OK
    ScanAce Plus            Untested
    ScanAce II Plus         Untested
    ScanAce III Plus        Untested
    ScanAce V               Untested
    ScanAce ScanMedia       Untested
    ScanAce ScanMedia II    Untested
    ScanAce 630S            Untested
    ScanAce 636S            Untested
    JetScan 630             OK
    JetScan 636PRO          Untested

# FILES

*@CONFIGDIR@/pie.conf*
The backend configuration file

*@LIBDIR@/libsane-pie.a*
The static library implementing this backend.

*@LIBDIR@/libsane-pie.so*
The shared library implementing this backend (present on systems that support dynamic loading).

# SEE ALSO

**sane**(7)

# CONTACT AND BUG-REPORTS

Please send any information and bug-reports to:
Simon Munton \<*simon@munton.demon.co.uk*\>
