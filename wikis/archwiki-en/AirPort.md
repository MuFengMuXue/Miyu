# AirPort

From Wikipedia:
:AirPort is the name given to a series of Apple products using the (Wi-Fi) protocols (802.11b, 802.11g, 802.11n and 802.11ac). These products comprise a number of wireless routers and wireless cards. The AirPort Extreme name was originally intended to signify the addition of the 802.11g protocol to these products.

Apple sells a number of AirPort models: AirPort Express, AirPort Extreme, and AirPort Time Capsule. The AirPort Time Capsule is essentially the AirPort Extreme, but with a 2-3 TB hard drive added, depending on which model you buy. All AirPort models have the ability to share printers on the network (through the USB port), and all AirPort models support up to 50 users.

## Configuration
Traditionally, AirPort base stations can be configured two ways, both of which require applications from Apple - AirPort base stations do not have web interfaces, unlike most routers. The first is using the desktop application, which is shipped with all Macs as a part of macOS and can be downloaded separately for Windows. There is no GNU/Linux version.

The second way is to use the AirPort Utility app on an iOS device. If you or a friend has an iPod Touch, iPhone, or iPad lying around, this is probably the most hassle-free way to configure your AirPort base station.

If that is not an option, you basically have two things to try: either run the desktop version of AirPort Utility in Wine, or use .

## Music streaming
If you want to emulate the AirPort Express, take a look at Shairport Sync. If you wish to use the music streaming feature of AirPort Express base stations, look for "raop" in the AUR.

## Printing
Scan the Airport Express station to determine which port is used for printing.

Note the port of the jetdirect service, and use a printer URI of socket://, followed by your station IP address, a colon, and the jetdirect port number.

See CUPS for more information.
