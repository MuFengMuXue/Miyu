# Wireshark

Wireshark is a free and open-source packet analyzer. It is used for network troubleshooting, analysis, software and communications protocol development, and education.

## Installation
Install the  package for the Wireshark GUI or  for just the  CLI.

 is an alternative terminal UI.

## Capturing privileges
Do not run Wireshark as root; it is insecure. Wireshark has implemented privilege separation, which means that the Wireshark GUI (or the tshark CLI) can run as a normal user while the dumpcap capture utility runs as rootThe  install script sets packet capturing capabilities on the  executable.

 can only be executed by root and members of the  group, so to use Wireshark as a normal user, you have to add your user to the  user group.

## A few capturing techniques
There are a number of different ways to capture exactly what you are looking for in Wireshark, by applying [https://gitlab.com/wireshark/wireshark/-/wikis/CaptureFilters capture filters or display filters.

## Filtering TCP packets
If you want to see all the current TCP packets, type  into the Filter bar or in the CLI, enter:

 $ tshark -f "tcp"

## Filtering UDP packets
If you want to see all the current UDP packets, type  into the Filter bar or in the CLI, enter:

 $ tshark -f "udp"

## Filter packets to a specific IP address
To observe traffic around a specific address, say , there are a few filter options. Note that IPv6 addresses can be filtered similarly but using  instead of .

*  shows all traffic sent to a that address.
*  shows all traffic sent from that address.
*  shows all traffic both sent to and sent from that address.
*  shows all traffic not sent either to or from that address.

## Filter packets to IPv4 LAN
To only see LAN traffic and no internet traffic use this display filter to show traffic on private network addresses.

 (ip.src==10.0.0.0/8 AND ip.dst==10.0.0.0/8) OR (ip.src==172.16.0.0/12 AND ip.dst==172.16.0.0/12) OR (ip.src==192.168.0.0/16 and ip.dst==192.168.0.0/16)

## Filter packets by port
See all traffic on specific TCP or UDP ports via  or  respectively.

 tcp.port == 80

## Headless capturing with dumpcap
dumpcap is part of Wireshark and can be used for capturing packets without the GUI. Used in combination with tmux will allow the capture of packets in a detached session.

To see all dumpcap options, use the  flag.

The following example will provide a ringbuffer capture. It captures twenty  files of 100MB each, replacing the oldest file with the twenty-first file and so on… This allows a continuous capture without exhausting disk space.

 # dumpcap -i 1 -b filesize:100000 -b files:20 -w mycapture.pcapng

*  − interface number (listed from )

*  − file size in kB before starting a new  file

*  − the number of files to capture before overwriting the oldest

*  − write the output to the file
