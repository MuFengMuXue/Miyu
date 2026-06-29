# NAME

sane-kvs40xx - SANE backend for Panasonic KV-S40xxC USB/SCSI ADF scanners.

# DESCRIPTION

The **sane-kvs40xx** library implements a SANE (Scanner Access Now Easy) backend which provides access to the Panasonic KV-S40xxC and KV-S70xxC scanners.

# KNOWN ISSUES

This document was written by the SANE project, which has no information regarding the capabilities or reliability of the backend. All information contained here is suspect.

The backend uses pthreads directly, and so requires pthreads to be enabled.

# CREDITS

The backend was written by Panasonic Russia Ltd.

The backend was ported to sane-backends 1.0.23 and downgraded to C89 by m. allan noah.

# SEE ALSO

**sane**(7), **sane-usb**(5), **sane-scsi**(5)

# AUTHOR

m\. allan noah: \<*kitno455 a t gmail d o t com*\>
