# Extensions / Libxt AUDIT

This target creates audit records for packets hitting the target. It can be used to record accepted, dropped, and rejected packets. See auditd(8) for additional details.

**--type** {**accept**\|**drop**\|**reject**}
Set type of audit record. Starting with linux-4.12, this option has no effect on generated audit messages anymore. It is still accepted by iptables for compatibility reasons, but ignored.

Example:

> iptables -N AUDIT_DROP

> iptables -A AUDIT_DROP -j AUDIT

> iptables -A AUDIT_DROP -j DROP
