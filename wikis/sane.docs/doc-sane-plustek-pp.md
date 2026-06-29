# NAME

sane-plustek_pp - SANE backend for Plustek parallel port flatbed scanners

# DESCRIPTION

The **sane-plustek_pp** library implements a SANE (Scanner Access Now Easy) backend that provides access to Plustek ASIC 9600\[1/3\] and P9800\[1/3\] based parallel port flatbed scanners.

# SUPPORTED DEVICES

At present, the following scanners should work with this backend:

**PLUSTEK SCANNERS**

    Parallelport Model:    ASIC: Properties:
    ---------------------- ----- ------------------------
    OpticPro PT12          98003 600x1200 dpi 36bit 512Kb
    OpticPro P12           98003 600x1200 dpi 36bit 512Kb
    OpticPro 9636T/12000T  98001 600x1200 dpi 36bit 512Kb
    OpticPro 12000P Turbo  98001 600x1200 dpi 36bit 512Kb
    OpticPro 9636P+/Turbo  98001 600x1200 dpi 36bit 512Kb
    OpticPro 9636P         96003 600x1200 dpi 36bit 128Kb
    OpticPro 12000P/96000P 96003 600x1200 dpi 36bit 128Kb
    OpticPro 1236P         96003 600x1200 dpi 30bit 128Kb
    OpticPro 9600P         96003 600x1200 dpi 30bit 128Kb
    OpticPro 9630P/FBIV    96003 600x1200 dpi 30bit 128Kb
    OpticPro 9630PL (14")  96003 600x1200 dpi 30bit 128Kb
    OpticPro A3I           96003  400x800 dpi 36bit 128Kb
    OpticPro 600P/6000P    96003  300x600 dpi 30bit  32Kb
    OpticPro 4831P         96003  300x600 dpi 30bit  32Kb
    OpticPro 4830P/FBIII   96003  300x600 dpi 30bit  32Kb
    OpticPro 4800P/FBII    96001  300x600 dpi 24bit  32Kb

**PRIMAX SCANNERS**

There are some scanners sold by Primax, but they are in fact Plustek devices. These scanners are also supported. The following table will show the relationship:

    Model:                      Plustek Model:  Remarks:
    --------------------------- --------------  ------------
    Colorado 4800               OpticPro 4800   not tested
    Compact 4800 Direct         OpticPro 600    mov=2
    Compact 4800 Direct 30bit   OpticPro 4830   mov=7
    Compact 9600 Direct 30bit   OpticPro 9630   works

**GENIUS SCANNERS**

The following devices are sold as Genius Scanners, but are in fact Plustek devices. The table will show the relationship:

    Model:                      Remarks:
    --------------------------- ----------------------------
    Colorpage Vivid III V2      Like P12 but has two buttons
                                and Wolfson DAC

**ARIES SCANNERS**

There's one scanner sold as Aries Scanner, but is in fact a Plustek device. The following table will show the relationship:

    Model:                      Plustek Model:  Remarks:
    --------------------------- --------------  ------------
    Scan-It 4800                OpticPro 600    mov=2

**BrightScan SCANNERS**

There's one scanner sold as BrightScan OpticPro Scanner, this is also a rebadged Plustek device. The following table will show the relationship:

    Model:                      Remarks:
    --------------------------- ----------------------------
    BrightScan OpticPro         OpticPro P12

# DEVICE NAMES

This backend's default device is:

> *0x378*

This "default device" will be used if no configuration file can be found. It is the base address of the parallel port on i386 machines.

As the backend supports up to four devices, it is possible to specify them in the configuration file

> *@CONFIGDIR@/plustek_pp.conf*

See this file for examples.

# CONFIGURATION

This section describes the backend's configuration file entries. The file is located at: *@CONFIGDIR@/plustek_pp.conf*

For a proper setup, you will need at least two entries:

> *\[direct\]*
> *device 0x378*

*direct* tells the backend, that the following devicename (here *0x378*) has to be interpreted as parallel port scanner device. In fact it is the address to use. Alternatively you can use */dev/parport0* if the backend has been compiled with libieee1284 support.

Further options:

option warmup t

> *t* specifies the warmup period in seconds

option lampOff t

> *t* is the time in seconds for switching off the lamps in standby mode

option lOffonEnd b

> *b* specifies the behaviour when closing the backend, 1 --\> switch lamps off, 0 --\> do not change lamp status

option mov m

> *m* is the model override switch, which only works in direct mode.
>
> *m* = 0
> default: no override
>
> *m* = 1
> OpticPro 9630PL override (works if OP9630 has been detected) forces legal size (14")
>
> *m* = 2
> Primax 4800Direct override (works if OP600 has been detected) swaps red/green color
>
> *m* = 3
> OpticPro 9636 override (works if OP9636 has been detected) disables backends transparency/negative capabilities
>
> *m* = 4
> OpticPro 9636P override (works if OP9636 has been detected) disables backends transparency/negative capabilities
>
> *m* = 5
> OpticPro A3I override (works if OP12000 has been detected) enables A3 scanning
>
> *m* = 6
> OpticPro 4800P override (works if OP600 has been detected) swaps red/green color
>
> *m* = 7
> Primax 4800Direct 30bit override (works if OP4830 has been detected)

See the *plustek_pp.conf* file for examples.

# PARALLEL PORT MODES

The current driver works best, when the parallel port has been set to EPP-mode. When detecting any other mode such as ECP or PS/2 the driver tries to set to a faster, supported mode. If this fails, it will use the SPP mode, as this mode should work with all Linux supported parallel ports. If in doubt, enter your BIOS and set it to any mode except ECP.

Former Plustek scanner models (4830, 9630) supplied a ISA parallel port adapter card. This card is **not** supported by the driver.

The ASIC 96001/3 based models have sometimes trouble with high resolution modes. If you encounter sporadic corrupted images (parts duplicated or shifted horizontally) kill all other applications before scanning and (if sufficient memory available) disable swapping.

See the *plustek_pp.conf* file for examples.

# FILES

*@CONFIGDIR@/plustek_pp.conf*
The backend configuration file

*@LIBDIR@/libsane-plustek_pp.a*
The static library implementing this backend.

*@LIBDIR@/libsane-plustek_pp.so*
The shared library implementing this backend (present on systems that support dynamic loading).

# ENVIRONMENT

**SANE_CONFIG_DIR**
This environment variable specifies the list of directories that may contain the configuration file. On \*NIX systems, the directories are separated by a colon (\`:'), under OS/2, they are separated by a semi-colon (\`;'). If this variable is not set, the configuration file is searched in two default directories: first, the current working directory (".") and then in *@CONFIGDIR@*. If the value of the environment variable ends with the directory separator character, then the default directories are searched after the explicitly specified directories. For example, setting **SANE_CONFIG_DIR** to "/tmp/config:" would result in directories *tmp/config*, *.*, and *@CONFIGDIR@* being searched (in this order).

**SANE_DEBUG_PLUSTEK_PP**
If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. Higher debug levels increase the verbosity of the output.

Example: export SANE_DEBUG_PLUSTEK_PP=10

# SEE ALSO

**sane**(7), **xscanimage**(1),
*@DOCDIR@/plustek/Plustek-PARPORT.changes*

# CONTACT AND BUG-REPORTS

Please send any information and bug-reports to:
**SANE Mailing List**

Additional info and hints can be obtained from our mailing-List archive at: *http://www.sane-project.org/mailing-lists.html*.

To obtain debug messages from the backend, please set the environment-variable **SANE_DEBUG_PLUSTEK_PP** before calling your favorite SANE frontend (e.g. **xscanimage**(1)):

*export SANE_DEBUG_PLUSTEK_PP=20 ; xscanimage*

The value controls the verbosity of the output.

# KNOWN BUGS & RESTRICTIONS

\* The Halftoning works, but the quality is poor

\* Printers (especially HP models) will start to print during scanning. This in fact is a problem to other printers too, using bidirectional protocol (see www.plustek.com (TAIWAN) page for further details)

\* The driver does not support these manic scalings up to 16 times the physical resolution. The only scaling is done on resolutions between the physical resolution of the CCD-sensor and the stepper motor i.e. you have a 600x1200 dpi scanner and you are scanning using 800dpi, so scaling is necessary, because the sensor only delivers 600dpi but the motor is capable to perform 800dpi steps.

\* On some devices, the pictures seems bluish

*ASIC 98001 based models:*

\* The 300dpi transparency and negative mode does not work correctly.

\* There is currently no way to distinguish a model with and without transparency unit.

\* The scanned images seem to be too dark (P9636T)

*ASIC 96003/1 based models:*

\* 30bit mode is currently not supported.

\* On low end systems under heavy system load the driver may lose data, which can result in picture corruption or cause the sensor to hit the scan bed.

\* The scanning speed on 600x1200 dpi models is slow.

\* The scanning quality of the A3I is poor.
