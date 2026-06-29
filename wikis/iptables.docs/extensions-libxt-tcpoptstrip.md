# Extensions / Libxt TCPOPTSTRIP

This target will strip TCP options off a TCP packet. (It will actually replace them by NO-OPs.) As such, you will need to add the **-p tcp** parameters.

**--strip-options** *option*\[**,***option*...\]
Strip the given option(s). The options may be specified by TCP option number or by symbolic name. The list of recognized options can be obtained by calling iptables with **-j TCPOPTSTRIP -h**.
