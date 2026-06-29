# NAME

sane-u12 - SANE backend for Plustek USB flatbed scanners, based on older parport designs

# DESCRIPTION

The **sane-u12** library implements a SANE (Scanner Access Now Easy) backend that provides access to USB flatbed scanners based on Plusteks' ASIC 98003 (parallel-port ASIC) and a GeneSys Logics' USB-parport bridge chip.

# SUPPORTED DEVICES

The backend is able to support some early Plustek USB scanners that based their old parport design around the ASIC 98003 and other rebadged Plustek devices. The following tables will give you a short overview.

If your Plustek scanner has another Product ID, then the device is **NOT** supported by this backend.

Vendor Plustek - ID: 0x07B3

    ----------------------------------------------------------
    Model:                   Vendor-ID:       Product-ID:
    ----------------------------------------------------------
    OpticPro U12             0x07B3           0x0001
    OpticPro U1212           0x07B3           0x0001
    OpticPro UT12            0x07B3           0x0001

Vendor KYE/Genius

    --------------------------------------------------------
    USB Model:               Vendor-ID:       Product-ID:
    --------------------------------------------------------
    ColorPage Vivid III USB  0x07B3           0x0001
    ColorPage HR6 V1         0x0458           0x2004

# CONFIGURATION

To use your scanner with this backend, you need at least two entries in the configuration file *@CONFIGDIR@/u12.conf*

> *\[usb\] vendor-id product-id*
> *device /dev/usbscanner*

*\[usb\]* tells the backend, that the following devicename (here */dev/usbscanner*) has to be interpreted as USB scanner device. If vendor- and product-id has not been specified, the backend tries to detect this by its own. If device is set to *auto* then the next matching device is used.

**The Options:**

option warmup t

> *t* specifies the warmup period in seconds

option lampOff t

> *t* is the time in seconds for switching off the lamps in standby mode

option lOffonEnd b

> *b* specifies the behaviour when closing the backend, 1 --\> switch lamps off, 0 --\> do not change lamp status

See the *u12.conf* file for examples.

**Note:** You have to make sure, that the USB subsystem is loaded correctly and you have access to the device-node. For more details see **sane-usb**(5) manpage. You might use **sane-find-scanner**(1) to check that you have access to your device.

**Note:**
If there's no configuration file, the backend defaults to **device auto**

# FILES

*@CONFIGDIR@/u12.conf*
The backend configuration file

*@LIBDIR@/libsane-u12.a*
The static library implementing this backend.

*@LIBDIR@/libsane-u12.so*
The shared library implementing this backend (present on systems that support dynamic loading).

# ENVIRONMENT

**SANE_CONFIG_DIR**
This environment variable specifies the list of directories that may contain the configuration file. On \*NIX systems, the directories are separated by a colon (\`:'), under OS/2, they are separated by a semi-colon (\`;'). If this variable is not set, the configuration file is searched in two default directories: first, the current working directory (".") and then in *@CONFIGDIR@*. If the value of the environment variable ends with the directory separator character, then the default directories are searched after the explicitly specified directories. For example, setting **SANE_CONFIG_DIR** to "/tmp/config:" would result in directories *tmp/config*, *.*, and *@CONFIGDIR@* being searched (in this order).

**SANE_DEBUG_U12**
If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. Higher debug levels increase the verbosity of the output.

Example: export SANE_DEBUG_U12=10

# SEE ALSO

**sane**(7), **sane-usb**(5), **sane-plustek**(5), **sane-find-scanner**(1), **xscanimage**(1), **scanimage**(1)
*@DOCDIR@/u12/U12.changes*

# CONTACT AND BUG-REPORTS

Please send any information and bug-reports to:
**SANE Mailing List**

Additional info and hints can be obtained from our mailing-List archive at: *http://www.sane-project.org/mailing-lists.html*.

To obtain debug messages from the backend, please set the environment-variable **SANE_DEBUG_U12** before calling your favorite SANE frontend (e.g. **xscanimage**(1)):

*export SANE_DEBUG_U12=20 ; xscanimage*

The value controls the verbosity of the backend.

# KNOWN BUGS & RESTRICTIONS

\* The driver is in alpha state, so please don't expect too much!!!

\* When using libusb, it might be, that the backend hangs. In that case, reconnect the scanner.
