# Extensions / Libxt String

This module matches a given string by using some pattern matching strategy. It requires a linux kernel \>= 2.6.14.

**--algo** {**bm**\|**kmp**}
Select the pattern matching strategy. (bm = Boyer-Moore, kmp = Knuth-Pratt-Morris)

**--from** *offset*
Set the offset from which it starts looking for any matching. If not passed, default is 0.

**--to** *offset*
Set the offset up to which should be scanned. That is, byte *offset* (counting from 0) is the last one that is scanned and the maximum position of *pattern*'s last character. If not passed, default is the packet size.

\[**!**\] **--string** *pattern*
Matches the given pattern.

\[**!**\] **--hex-string** *pattern*
Matches the given pattern in hex notation.

**--icase**
Ignore case when searching.

Examples:
> \# The string pattern can be used for simple text characters.
> iptables -A INPUT -p tcp --dport 80 -m string --algo bm --string 'GET /index.html' -j LOG

\# The hex string pattern can be used for non-printable characters, like \|0D 0A\| or \|0D0A\|.
iptables -p udp --dport 53 -m string --algo bm --from 40 --to 57 --hex-string '\|03\|www\|09\|netfilter\|03\|org\|00\|'

Note: Since Boyer-Moore (BM) performs searches for matches from right to left and the kernel may store a packet in multiple discontiguous blocks, it's possible that a match could be spread over multiple blocks, in which case this algorithm won't find it.

If you wish to ensure that such thing won't ever happen, use the Knuth-Pratt-Morris (KMP) algorithm instead. In conclusion, choose the proper string search algorithm depending on your use-case.

For example, if you're using the module for filtering, NIDS or any similar security-focused purpose, then choose KMP. On the other hand, if you really care about performance — for example, you're classifying packets to apply Quality of Service (QoS) policies — and you don't mind about missing possible matches spread over multiple fragments, then choose BM.
