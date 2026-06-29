# Extensions / Libxt Connlabel

Module matches or adds connlabels to a connection. connlabels are similar to connmarks, except labels are bit-based; i.e. all labels may be attached to a flow at the same time. Up to 128 unique labels are currently supported.

\[**!**\] **--label** **name**
matches if label **name** has been set on a connection. Instead of a name (which will be translated to a number, see EXAMPLE below), a number may be used instead. Using a number always overrides connlabel.conf.

**--set**
if the label has not been set on the connection, set it. Note that setting a label can fail. This is because the kernel allocates the conntrack label storage area when the connection is created, and it only reserves the amount of memory required by the ruleset that exists at the time the connection is created. In this case, the match will fail (or succeed, in case **--label** option was negated).

This match depends on libnetfilter_conntrack 1.0.4 or later. Label translation is done via the **/etc/xtables/connlabel.conf** configuration file.

Example:

    0	eth0-in
    1	eth0-out
    2	ppp-in
    3	ppp-out
    4	bulk-traffic
    5	interactive
