# Extensions / Libxt Statistic

This module matches packets based on some statistic condition. It supports two distinct modes settable with the **--mode** option.

Supported options:

**--mode** *mode*
Set the matching mode of the matching rule, supported modes are **random** and **nth.**

\[**!**\] **--probability** *p*
Set the probability for a packet to be randomly matched. It only works with the **random** mode. *p* must be within 0.0 and 1.0. The supported granularity is in 1/2147483648th increments.

\[**!**\] **--every** *n*
Match one packet every nth packet. It works only with the **nth** mode (see also the **--packet** option).

**--packet** *p*
Set the initial counter value (0 \<= p \<= n-1, default 0) for the **nth** mode.
