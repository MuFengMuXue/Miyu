# GPS

There is a variety of Global Positioning System (GPS) hardware receivers supported in Arch Linux:

* Bluetooth GPS adapters
* USB GPS adapters (internal or external)
* WWAN-integrated adapters (some Laptop/HP EliteBook modules for example)
* Smartphones are able to relay GPS data over USB or Bluetooth with additional software

## Drivers
Usually a GPS device is presented as a serial device and the kernel uses a standard driver, but in some cases the drivers such as  or  need to be installed.

## Interfaces
GPS does not have a very unified interfacing and configuration in Linux. The raw GPS data is printed on the serial device and programs interpret the location by themselves, occupying the device in the process. Sharing the GPS adapter to multiple applications is possible with .

## GPSD
GPSD is a daemon to query the serial GPS device and make its output available on a TCP server. It is the most standard GPS interface in Linux and GPS-aware applications usually support it.

## ModemManager
ModemManager is a Linux WWAN modem support package which interfaces with NetworkManager. It also supports querying GPS coordinates from GPS-enabled WWAN cards and it even displays the location in the . The most important commands are:

## View locationing capabilities
 # mmcli -m 0 --location-status

## Enable GPS
 # mmcli -m 0 --location-enable-gps-raw --location-enable-gps-nmea

## Display location
 # watch mmcli -m 0 --location-get

## Disable GPS
 # mmcli -m 0 --location-disable-gps-raw --location-disable-gps-nmea

## Clients
The  package provides , a simple console-based client for showing the current GPS device status.

## Time Synchronization
See Network Time Protocol daemon#Using ntpd with GPS
