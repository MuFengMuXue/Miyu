# Extensions / Libxt Sctp

This module matches Stream Control Transmission Protocol headers.

\[**!**\] **--source-port**,**--sport** *port*\[**:***port*\]
\[**!**\] **--destination-port**,**--dport** *port*\[**:***port*\]
\[**!**\] **--chunk-types** {**all**\|**any**\|**only**} *chunktype*\[**:***flags*\] \[...\]
The flag letter in upper case indicates that the flag is to match if set, in the lower case indicates to match if unset.

Match types:

all
Match if all given chunk types are present and flags match.

any
Match if any of the given chunk types is present with given flags.

only
Match if only the given chunk types are present with given flags and none are missing.

Chunk types: DATA INIT INIT_ACK SACK HEARTBEAT HEARTBEAT_ACK ABORT SHUTDOWN SHUTDOWN_ACK ERROR COOKIE_ECHO COOKIE_ACK ECN_ECNE ECN_CWR SHUTDOWN_COMPLETE I_DATA RE_CONFIG PAD ASCONF ASCONF_ACK FORWARD_TSN I_FORWARD_TSN

chunk type available flags
DATA I U B E i u b e
I_DATA I U B E i u b e
ABORT T t
SHUTDOWN_COMPLETE T t

(lowercase means flag should be "off", uppercase means "on")

Examples:

iptables -A INPUT -p sctp --dport 80 -j DROP

iptables -A INPUT -p sctp --chunk-types any DATA,INIT -j DROP

iptables -A INPUT -p sctp --chunk-types any DATA:Be -j ACCEPT
