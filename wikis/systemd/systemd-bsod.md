## Name

systemd-bsod.service, systemd-bsod — Displays boot-time emergency log message in full screen

## Synopsis

`systemd-bsod.service`

`/usr/lib/systemd/systemd-bsod` \[OPTIONS...\]

## Description

`systemd-bsod.service` is used to display a blue screen which contains a message relating to a boot failure, including a QR code which can be scanned to get helpful information about the failure.

## Options

The following options are understood by **systemd-bsod**:

`-h`, `--help`  
Print a short help text and exit.

`--version`  
Print a short version string and exit.

`-c`, `--continuous`  
When specified, **systemd-bsod** waits continuously for changes in the journal if it does not find any emergency messages on the initial attempt.

Added in version 255.

`--tty=`  
Specify the TTY to output to. By default, **systemd-bsod** will automatically find a free VT to display the message on. If this option is specified a TTY may be selected explicitly. Use `--tty=/dev/tty` to direct output to the terminal the command is invoked on.

Added in version 256.

## Exit status

On success (displaying the journal message successfully), 0 is returned, a non-zero failure code otherwise.

## See Also

systemd(1)
