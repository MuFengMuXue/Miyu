# Extensions / Libxt Helper

This module matches packets related to a specific conntrack helper.

\[**!**\] **--helper** *string*
Matches packets related to the specified conntrack helper.

string can be "ftp" for packets related to an FTP session on default port. For other ports, append --portnr to the value, ie. "ftp-2121".

Same rules apply for other conntrack helpers.
