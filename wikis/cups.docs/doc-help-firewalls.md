# Firewalls

This help document describes the ports that CUPS uses so that firewall administrators can allow traffic used for printing.

## Ports Used for Printer Sharing

Table 1 lists the ports that are used for IPP printer sharing via CUPS.


| (Destination) Port | TCP/UDP | Direction | Description |
|----|----|----|----|
| 53 (DNS) | TCP/UDP | OUT | Domain Name System lookups and service registrations. |
| 631 (IPP/IPPS) | TCP | IN | Internet Printing Protocol requests and responses (print jobs, status monitoring, etc.) |
| 5353 (mDNS) | UDP | IN+OUT | Multicast DNS lookups and service registrations. |

Table 1: Ports Used for IPP Printer Sharing


Table 2 lists the ports that are used for SMB (Windows) printer sharing, typically via the Samba software.


| (Destination) Port(s) | TCP/UDP | Direction | Description |
|----|----|----|----|
| 137 (WINS) | UDP | IN+OUT | Windows Internet Naming Service (name lookup for SMB printing). |
| 139 (SMB) | TCP | IN | Windows SMB printing. |
| 445 (SMBDS) | TCP | IN+OUT | Windows SMB Domain Server (authenticated SMB printing). |

Table 2: Ports Used for SMB Printer Sharing


## Ports Used for Network Printers

Table 3 lists the ports for outgoing network traffic that are used for network printers.

> **Notes:**
>
> 1.  DNS and mDNS are used for all printing protocols except SMB.
> 2.  SNMP is used to provide status and supply level information for AppSocket and LPD printers.


| (Destination) Port(s) | TCP/UDP | Description |
|----|----|----|
| 53 (DNS) | TCP/UDP | Domain Name System lookups. |
| 137 (WINS) | UDP | Windows Internet Naming Service (name lookup for SMB printing). |
| 139 (SMB) | TCP | Windows SMB printing. |
| 161 (SNMP) | UDP | SNMP browsing (broadcast) and status monitoring (directed to printer IP address). |
| 443 (IPPS) | TCP | Internet Printing Protocol requests and responses (print jobs, status monitoring, etc.) |
| 445 (SMBDS) | TCP | Windows SMB Domain Server (authenticated SMB printing). |
| 515 (LPD) | TCP | Line Printer Daemon (LPD/lpr) print job submission and status monitoring. |
| 631 (IPP/IPPS) | TCP | Internet Printing Protocol requests and responses (print jobs, status monitoring, etc.) |
| 5353 (mDNS) | UDP | Multicast DNS lookups. |
| 9100-9102 | TCP | Raw print data stream (AppSocket/JetDirect). |

Table 3: Outgoing Ports Used for Network Printers
