**Resources**

[[]][Network Time Protocol](https://en.wikipedia.org/wiki/Network_Time_Protocol "wikipedia:Network Time Protocol")

*Not to be confused with [the ntp package](https://wiki.gentoo.org/wiki/Ntp "Ntp").*

The Network Time Protocol (NTP) is used to synchronize the [system time](https://wiki.gentoo.org/wiki/System_time "System time") with other devices over the network. This happens in a client-server model.

## Contents

-   [[1] [Implementations]](#Implementations)
-   [[2] [Sync system clock on boot]](#Sync_system_clock_on_boot)
-   [[3] [See also]](#See_also)
-   [[4] [External resources]](#External_resources)

## [Implementations]

Following implementations of the Network Time Protocol are currently available:

  ---------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------
  Name                                                                         Package                                                                                                                                                                                                                                                                                                                                                                           Description
  [chrony](https://wiki.gentoo.org/wiki/Chrony "Chrony")                       [[[net-misc/chrony]](https://packages.gentoo.org/packages/net-misc/chrony)[]]               Versatile implementation of the Network Time Protocol.
  clockspeed                                                                   [[[net-misc/clockspeed]](https://packages.gentoo.org/packages/net-misc/clockspeed)[]]   Simple Network Time Protocol (NTP) client.
  [ntp](https://wiki.gentoo.org/wiki/Ntp "Ntp")                                [[[net-misc/ntp]](https://packages.gentoo.org/packages/net-misc/ntp)[]]                        Suite of tools utilizing Network Time Protocol.
  ntpsec                                                                       [[[net-misc/ntpsec]](https://packages.gentoo.org/packages/net-misc/ntpsec)[]]               NTP reference implementation, refactored.
  [openntpd](https://wiki.gentoo.org/wiki/Openntpd "Openntpd")   [[[net-misc/openntpd]](https://packages.gentoo.org/packages/net-misc/openntpd)[]]         Lightweight NTP server ported from OpenBSD.
  sntpd                                                                        [[[net-misc/sntpd]](https://packages.gentoo.org/packages/net-misc/sntpd)[]]                  NTP (RFC-1305 and RFC-4330) client and server for unix(like) systems.
  ---------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------

## [Sync system clock on boot]

It is important for most systems to keep accurate time, so it is usual to set up an NTP time synchronization solution to adjust system time on boot. This can be essential for some systems that do not have an [RTC](https://wiki.gentoo.org/wiki/System_time#Software_clock_vs_Hardware_clock "System time").

The handbook gives an example of an easy way to [setup time synchronization](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Tools#Suggested:_Time_synchronization "Handbook:AMD64/Installation/Tools").

## [See also]

-   [Pi4 Stratum 1 Time Server](https://wiki.gentoo.org/wiki/Pi4_Stratum_1_Time_Server "Pi4 Stratum 1 Time Server") --- setting up a [Raspberry Pi 4/5](https://wiki.gentoo.org/wiki/Raspberry_Pi4_64_Bit_Install "Raspberry Pi4 64 Bit Install") as a Stratum 1 Time Server
-   [System time](https://wiki.gentoo.org/wiki/System_time "System time") --- is used in Unix systems to keep track of time.

## [External resources]

-   [RFC 5905 - Network Time Protocol Version 4: Protocol and Algorithms Specification](https://tools.ietf.org/html/rfc5905)
-   [RFC 5907 - Definitions of Managed Objects for Network Time Protocol Version 4 (NTPv4)](https://tools.ietf.org/html/rfc5907)
-   [RFC 5908 - Network Time Protocol (NTP) Server Option for DHCPv6](https://tools.ietf.org/html/rfc5908)
-   [RFC 7164 - RTP and Leap Seconds](https://tools.ietf.org/html/rfc7164)
-   [RFC 7822 - Network Time Protocol Version 4 (NTPv4) Extension Fields](https://tools.ietf.org/html/rfc7822)
-   [RFC 8573 - Message Authentication Code for the Network Time Protocol](https://tools.ietf.org/html/rfc8573)
-   [RFC 9109 - Network Time Protocol Version 4: Port Randomization](https://tools.ietf.org/html/rfc9109)