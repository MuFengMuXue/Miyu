# Zeitgeist

Zeitgeist is a service which logs user activities and events, anywhere from files opened to websites visited or conversations held via email and more. It makes this information readily available for other applications to use in the form of timelines and statistics. See the Wikipedia article for a more detailed description of Zeitgeist itself.

## Installation
Install the  package, which includes the daemon and the datahub. The daemon receives metadata from data sources, and provides them to applications using D-Bus. The datahub provides passive plugins which insert events into Zeitgeist.

To configure what gets logged by Zeitgeist, install  which provides a graphical user interface where you can filter out specific folders, file types, and applications.

To monitor and inspect Zeitgeist's log at a low level, install  which provides a graphical user interface where you can see the events logged in real-time just like Wireshark.

## Data providers
The following applications are just a few examples of software able to send metadata to Zeitgeist. In some cases this functionality must be enabled manually.

*
*
*
* Zim

## Applications
The following applications can be used to browse or search for recent activity using the Zeitgeist engine:

*
*
*
