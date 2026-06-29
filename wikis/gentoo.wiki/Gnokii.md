**Resources**

[[]][Home](http://gnokii.org)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Gnokii "wikipedia:Gnokii")

**gnokii** is a modem and fax driver for mobile phones.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Set PIN to work with gnokii]](#Set_PIN_to_work_with_gnokii)
    -   [[3.2] [Sending SMS]](#Sending_SMS)
    -   [[3.3] [Write calendar notes]](#Write_calendar_notes)

## [Installation]

### [USE flags]

### [USE flags for] [app-mobilephone/gnokii](https://packages.gentoo.org/packages/app-mobilephone/gnokii) [[]] [User space driver and tools for use with mobile phones]

  ----------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+pcsc-lite`](https://packages.gentoo.org/useflags/+pcsc-lite)   Enable smartcard support with sys-apps/pcsc-lite
  [`X`](https://packages.gentoo.org/useflags/X)                     Add support for X11
  [`bluetooth`](https://packages.gentoo.org/useflags/bluetooth)     Enable Bluetooth Support
  [`debug`](https://packages.gentoo.org/useflags/debug)             Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`ical`](https://packages.gentoo.org/useflags/ical)               Enable support for dev-libs/libical
  [`irda`](https://packages.gentoo.org/useflags/irda)               Enable infrared support
  [`mysql`](https://packages.gentoo.org/useflags/mysql)             Add mySQL Database support
  [`nls`](https://packages.gentoo.org/useflags/nls)                 Add Native Language Support (using gettext - GNU locale utilities)
  [`postgres`](https://packages.gentoo.org/useflags/postgres)       Add support for the postgresql database
  [`sms`](https://packages.gentoo.org/useflags/sms)                 Enable SMS support (build smsd)
  [`usb`](https://packages.gentoo.org/useflags/usb)                 Add USB support to applications that have optional USB support (e.g. cups)
  ----------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-12-19 09:51] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask app-mobilephone/gnokii`

## [Configuration]

Edit the [/etc/gnokiirc] file:

[FILE] **`/etc/gnokiirc`**

    [global]
    port = /dev/ttyUSB0
    model = AT
    initlength = default
    connection = serial
    use_locking = yes
    serial_baudrate = 19200
    smsc_timeout = 10

    [gnokiid]
    bindir = /usr/sbin/

    [connect_script]
    TELEPHONE = 12345678

    [disconnect_script]

    [logging]
    debug = on

    rlpdebug = off
    xdebug = off

Setup save the password for PIN login

[FILE] **`/etc/sms-pin`**

    ABORT BUSY
    ABORT ERROR
    ABORT 'NO CARRIER'
    REPORT CONNECT
    TIMEOUT 10
    # Set your pin here
    "" "AT+CPIN=0000

## [Usage]

### [Set PIN to work with gnokii]

/usr/sbin/chat is part of [[[net-dialup/ppp]](https://packages.gentoo.org/packages/net-dialup/ppp)[]].

`root `[`#`]`/usr/sbin/chat -V -f /etc/sms-pin >> /dev/ttyUSB0 < /dev/ttyUSB0`

An other way is just using gnokii:

`user `[`$`]`gnokii --entersecuritycode PIN`

Show the PIN status:

`user `[`$`]`gnokii --getsecuritycodestatus | grep PIN`

### [Sending SMS]

`user `[`$`]`echo "test" | gnokii --sendsms +land_and_telephonenumber`

### [Write calendar notes]

[FILE] **`gnokii-import.sh`**

    #!/bin/bash
    #########################################################
    # gnokii ical import script to fix buggy write mode     #
    # don't forget to use "irattach irda0 -s" if using ira  #
    #########################################################
    read -p "Please give path and file name: " file

    declare -i a
    a=$(grep -ir "SUMMARY:" $file | wc -l) # count the entries

    for i in `seq 1 $a`;do
    echo $i
    gnokii --writecalendarnote $file $i
    sleep 1 # wait a second before the next entry is written
    done

[FILE] **`cal.ical`**

    BEGIN:VCALENDAR
    VERSION:1.0
    BEGIN:VEVENT
    CATEGORIES:MISCELLANEOUS
    SUMMARY:09:00-18:00h New calendar entry
    DTSTART:20080415T210000
    DTEND:20080415T210000
    DALARM:20080414T210000
    END:VEVENT
    END:VCALENDAR

`user `[`$`]`gnokii-import.sh`

`user `[`$`]`cal.ica`