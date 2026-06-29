This page contains [[changes](https://wiki.gentoo.org/index.php?title=System_time&oldid=1425477&diff=1428620)] which are not marked for translation.

Other languages:

-   [Deutsch](https://wiki.gentoo.org/wiki/System_time/de "System time/de (7% translated)")
-   [English]
-   [español](https://wiki.gentoo.org/wiki/System_time/es "Hora del sistema (75% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/System_time/hu "Rendszeridő (75% translated)")
-   [čeština](https://wiki.gentoo.org/wiki/System_time/cs "System time/cs (0% translated)")
-   [русский](https://wiki.gentoo.org/wiki/System_time/ru "Системное время (99% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/System_time/zh-cn "系统时间 (45% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/System_time/ja "システム時刻 (89% translated)")
-   [한국어](https://wiki.gentoo.org/wiki/System_time/ko "System time/ko (35% translated)")

**Resources**

[[]][System time](https://en.wikipedia.org/wiki/System_time "wikipedia:System time")

[[]][Real-time clock](https://en.wikipedia.org/wiki/Real-time_clock "wikipedia:Real-time clock")

[[]][Time zone](https://en.wikipedia.org/wiki/Time_zone "wikipedia:Time zone")

\
The **system time**, backed by the system clock, is used in Unix systems to keep track of time. It can be set by an onboard hardware clock or by an external time server.

** Important**\
Systems without a functioning Real-Time Clock (RTC) must [set the system clock](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Tools#Suggested:_Time_synchronization "Handbook:AMD64/Installation/Tools"). at every system start, and on regular intervals thereafter. This is also beneficial for systems with a RTC, as the battery could fail, and clock skew can accumulate.

## Contents

-   [[1] [Preface]](#Preface)
    -   [[1.1] [Software clock vs Hardware clock]](#Software_clock_vs_Hardware_clock)
    -   [[1.2] [UTC vs local time]](#UTC_vs_local_time)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Time zone]](#Time_zone)
        -   [[2.1.1] [OpenRC]](#OpenRC)
        -   [[2.1.2] [systemd]](#systemd)
    -   [[2.2] [LC_TIME]](#LC_TIME)
    -   [[2.3] [System clock]](#System_clock)
        -   [[2.3.1] [Time server]](#Time_server)
        -   [[2.3.2] [systemd]](#systemd_2)
    -   [[2.4] [Hardware clock]](#Hardware_clock)
        -   [[2.4.1] [Syncing the hardware clock and system time]](#Syncing_the_hardware_clock_and_system_time)
        -   [[2.4.2] [In-kernel method]](#In-kernel_method)
        -   [[2.4.3] [OpenRC]](#OpenRC_2)
        -   [[2.4.4] [systemd]](#systemd_3)
-   [[3] [Troubleshooting]](#Troubleshooting)
    -   [[3.1] [Dual booting with Windows]](#Dual_booting_with_Windows)
-   [[4] [See also]](#See_also)
-   [[5] [External resources]](#External_resources)
-   [[6] [References]](#References)

## [[] Preface]

### [[] Software clock vs Hardware clock]

The [system clock](https://wiki.gentoo.org/wiki/System_time#System_clock "System time"), provided by the kernel, is the amount of time that has elapsed since the 1 January 1970 00:00:00 UTC [epoch](https://en.wikipedia.org/wiki/Epoch_(computing) "wikipedia:Epoch (computing)"). This is called [Unix time](https://en.wikipedia.org/wiki/Unix_time "wikipedia:Unix time").

The [hardware clock](https://wiki.gentoo.org/wiki/System_time#Hardware_clock "System time") (also known as real-time clock or RTC) is typically a component on the mainboard, which keeps time while the computer is switched off. The accuracy of most RTCs varies, it is typical for them to gain or lose several seconds per day. While adequate for most purposes, systems connected to the Internet usually use Network Time Protocol which achieves accuracy to within a few milliseconds.

In this case, the system will have the slightly incorrect time from the RTC only briefly, with NTP correcting it shortly after networking is established. The RTC can then be corrected, and in this manner will only drift significantly if the machine is left switched off for prolonged periods.

Some systems such as the Raspberry Pi (models up to 4) lack an RTC altogether. As such, these rely on NTP to start up with the correct time automatically.

### [[] UTC vs local time]

System time is always set to local time as determined by the user\'s [time zone](https://wiki.gentoo.org/wiki/System_time#Time_zone "System time"), taking [daylight saving time](https://en.wikipedia.org/wiki/Daylight_saving_time "wikipedia:Daylight saving time") (DST) into account.

The hardware clock can represent either local time or [Coordinated Universal Time](https://en.wikipedia.org/wiki/Coordinated_Universal_Time "wikipedia:Coordinated Universal Time") (UTC). UTC is preferred because it is independent of time zones and DST. Some operating systems (most notably Windows) use local time by default, which can cause conflicts on dual-boot systems. Windows can be reconfigured to use UTC, allowing it to stay in sync with Linux; see section [Dual booting with Windows](https://wiki.gentoo.org/wiki/System_time#Dual_booting_with_Windows "System time").

## [[] Configuration]

### [[] Time zone]

In order to keep time properly, select the proper time zone so the system knows where it is located.

#### [OpenRC]

See [Timezone (AMD64 Handbook)](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Base#Timezone "Handbook:AMD64/Installation/Base").

#### [systemd]

[systemd](https://wiki.gentoo.org/wiki/Systemd "Systemd") comes with the [timedatectl] command to manage the time zone:

To check the current zone:

`user `[`$`]`timedatectl`

To list available zones:

`user `[`$`]`timedatectl list-timezones`

To change the time zone, e.g. for Germany:

`root `[`#`]`timedatectl set-timezone Europe/Berlin`

### [[] LC_TIME]

This [environment variable](https://wiki.gentoo.org/wiki/Localization/Guide#Environment_variables_for_locales "Localization/Guide") defines formatting of dates and times. For more details see [The GNU C Library](https://www.gnu.org/software/libc/manual/html_node/Locale-Categories.html#index-LC_005fTIME)

### [[] System clock]

Typically the system clock time is set up by the hardware clock on boot. Alternatively it is possible to manually set the system clock or use a network time server.

The [date] command can be used to manage the system clock time:

To check the current software clock time:

`user `[`$`]`date`

To set the system clock, e.g. 12:34, May 6, 2016:

`root `[`#`]`date 050612342016`

#### [[] Time server]

See the [Chrony](https://wiki.gentoo.org/wiki/Chrony "Chrony") or [Network Time Protocol](https://wiki.gentoo.org/wiki/Network_Time_Protocol "Network Time Protocol") articles for information concerning the use of time servers.

#### [systemd]

systemd comes with the [timedatectl] command to manage the system clock:

To check the current software clock:

`user `[`$`]`timedatectl`

To set the system clock:

`root `[`#`]`timedatectl set-time "2012-12-17 12:30:59"`

### [[] Hardware clock]

To have a hardware clock, the following kernel options must be activated:

[KERNEL] **Necessary kernel options for a hardware clock**

        Device Drivers --->
          [*] Real Time Clock --->
                [ ]   Set system time from RTC on startup and resume
                [ ]   Set the RTC time based on NTP synchronization
                [*]   /sys/class/rtc/rtcN (sysfs)
                [*]   /proc/driver/rtc (procfs for rtc0)
                [*]   /dev/rtcN (character devices)
                <*>   PC-style 'CMOS'

At runtime, to check the current hardware clock:

`root `[`#`]`hwclock --show`

To set the hardware clock to the current system clock:

`root `[`#`]`hwclock --systohc`

#### [[] Syncing the hardware clock and system time]

Typically the hardware clock is used to setup the system clock on boot. This can be done by the kernel itself or by a boot service (init script). Also on shutdown the kernel or a service can write the software clock to the hardware clock. This aids the system in having the correct time on boot.

#### [[] In-kernel method]

On a sufficiently modern kernel (3.9 or newer), Linux can be configured to handle setting the system time automatically. To do so, enable the **Set system time from RTC on startup and resume** (`CONFIG_RTC_HCTOSYS`) and **Set the RTC time based on NTP synchronization** (`CONFIG_RTC_SYSTOHC`) kernel options:

[KERNEL] **Letting the kernel sync the system clock**

        Device Drivers --->
          [*] Real Time Clock --->
                [*]   Set system time from RTC on startup and resume
                (rtc0)  RTC used to set the system time
                [*]   Set the RTC time based on NTP synchronization
                (rtc0)  RTC used to synchronize NTP adjustment
                [*]   /sys/class/rtc/rtcN (sysfs)
                [*]   /proc/driver/rtc (procfs for rtc0)
                [*]   /dev/rtcN (character devices)
                <*>   PC-style 'CMOS'

The **Set the RTC time based on NTP synchronization** kernel option is currently supported by [chrony](https://wiki.gentoo.org/wiki/Chrony "Chrony")^[\[1\]](#cite_note-1)^, [NTP](https://wiki.gentoo.org/wiki/NTP "NTP") and [OpenNTPD](https://wiki.gentoo.org/wiki/OpenNTPD "OpenNTPD") since version 5.9p1^[\[2\]](#cite_note-2)^.

To check the hardware time was updated, install [[[net-misc/adjtimex]](https://packages.gentoo.org/packages/net-misc/adjtimex)[]] and run:

`root `[`#`]`adjtimex --print | grep status`

Bit 6 of the reported number should be unset (0). More information in [hwclock] man pages (search \'11 minute mode\').

#### [OpenRC]

When using OpenRC the [hwclock] init script can set the system clock on boot and sync system time to the hardware clock on shutdown. The service is enabled by default and should be *disabled* in favor of the above mentioned in-kernel method. The [hwclock] script should *not* be run when using the kernel\'s RTC.

`root `[`#`]`rc-update delete hwclock boot`

** Note**\
It could however happen hwclock being started as dependency of another rc-service, e.g. [sysklogd](https://forums.gentoo.org/viewtopic-t-1069418.html). In this case the rc-service **osclock** should be added to the same runlevel as the dependent rc-service.

If however there is a need for using the OpenRC, set both `clock_hctosys` and `clock_systohc` to `YES` in [/etc/conf.d/hwclock]. By default the service is configured for UTC. To change to local time add `clock="local"`.

[FILE] **`/etc/conf.d/hwclock`Adding hardware clock sync**

    clock_hctosys="YES"
    clock_systohc="YES"
    # clock="local"

Restart the [hwclock] service and have the hardware clock init script run on system boot:

`root `[`#`]`rc-service hwclock restart `

`root `[`#`]`rc-update add hwclock boot `

#### [systemd]

[systemd](https://wiki.gentoo.org/wiki/Systemd "Systemd") can be used to set the system clock on boot. Use [timedatectl] to manage the hardware clock:

To check the current hardware clock:

`user `[`$`]`timedatectl | grep "RTC time"`

To set the hardware clock to the current system clock (in UTC):

`root `[`#`]`timedatectl set-local-rtc 0`

To set the hardware clock to the current system clock (in the local time):

`root `[`#`]`timedatectl set-local-rtc 1`

## [Troubleshooting]

### [[] Dual booting with Windows]

Historically, Unix systems have set their RTC to represent UTC. Other operating system, such as Windows, expect the RTC to represent local time by default.

This can lead to a difficulty when dual-booting: the time being correct on one operating system causes it to be incorrect on the other. When either uses NTP to obtain the time, they then \'correct\' the RTC, only for the situation to revert when the other does the same, seemingly \'fighting\' over the RTC, and resulting in the clock being incorrect by several hours.

To avoid Windows adjusting the hardware clock back to local time, add the following registry entry:

For 64-bit Windows, open [regedit] then browse to [HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\TimeZoneInformation]. Create a new QWORD entry called `RealTimeIsUniversal`, then set its value to `1`. Reboot the system. The clock should now be in UTC time. For 32-bit Windows, follow the 64-bit instructions except use DWORD instead of QWORD.

## [See also]

-   [Network Time Protocol](https://wiki.gentoo.org/wiki/Network_Time_Protocol "Network Time Protocol") --- used to synchronize the [system time] with other devices over the network.
-   [Chrony](https://wiki.gentoo.org/wiki/Chrony "Chrony") --- a versatile implementation of the [Network Time Protocol](https://wiki.gentoo.org/wiki/Network_Time_Protocol "Network Time Protocol") (NTP).
-   [OpenNTPD](https://wiki.gentoo.org/wiki/OpenNTPD "OpenNTPD") --- a lightweight [NTP](https://wiki.gentoo.org/wiki/Network_Time_Protocol "Network Time Protocol") server ported from OpenBSD.

## [External resources]

-   [https://lifehacker.com/5742148/fix-windows-clock-issues-when-dual-booting-with-os-x](https://lifehacker.com/5742148/fix-windows-clock-issues-when-dual-booting-with-os-x) - Dual booting with MS Windows, set RealTimeIsUniversal. Also tested with [Windows 10](https://wiki.gentoo.org/wiki/UEFI_Dual_boot_with_Windows_7/8 "UEFI Dual boot with Windows 7/8").
-   [http://tldp.org/HOWTO/Clock-2.html](http://tldp.org/HOWTO/Clock-2.html) - The Clock Mini-HOWTO.

## [References]

1.  [[[↑](#cite_ref-1)] [[Comparison of NTP implementations](https://chrony.tuxfamily.org/comparison.html), [chrony](https://chrony.tuxfamily.org/), March 1st, 2017. Retrieved on July 11th, 2017.]]
2.  [[[↑](#cite_ref-2)] [OpenNTPD. [OpenNTPD 5.9p1](http://www.openntpd.org/txt/release-5.9p1.txt), [OpenNTPD](http://www.openntpd.org/), March 29th, 2016. Retrieved on July 11th, 2017.]]