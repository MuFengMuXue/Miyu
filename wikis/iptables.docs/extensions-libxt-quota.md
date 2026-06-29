# Extensions / Libxt Quota

Implements network quotas by decrementing a byte counter with each packet. The condition matches until the byte counter reaches zero. Behavior is reversed with negation (i.e. the condition does not match until the byte counter reaches zero).

\[**!**\] **--quota** *bytes*
The quota in bytes.
