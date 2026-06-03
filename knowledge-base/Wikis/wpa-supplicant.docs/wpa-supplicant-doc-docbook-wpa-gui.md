# Wpa Supplicant / Doc / Docbook / Wpa Gui

07 August 2019


     wpa_gui
     8


wpa_gui


WPA Graphical User Interface


       wpa_gui
       -p  path to ctrl sockets
       -i  ifname
       -m  seconds
       -t
       -q


Overview


wpa_gui is a QT graphical frontend program for interacting
    with wpa_supplicant. It is used to query current status, change
    configuration and request interactive user input.


wpa_gui supports (almost) all of the interactive status and
    configuration features of the command line client, wpa_cli. Refer
    to the wpa_cli manpage for a comprehensive list of the
    interactive mode features.


Command Arguments


-p path


Change the path where control sockets should
	be found.


-i ifname


Specify the interface that is being
	configured. By default, choose the first interface found with
	a control socket in the socket path.


-m seconds


Set the update interval in seconds for the signal
	strength meter. This value must be a positive integer, otherwise
	meter is not enabled (default behavior).


-t


Start program in the system tray only (if the window
	manager supports it). By default the main status window is
	shown.


-q


Run program in the quiet mode - do not display tray
	icon pop-up messages.


See Also


	 wpa_cli
	 8


	 wpa_supplicant
	 8


Legal


wpa_supplicant is copyright (c) 2003-2022,
    Jouni Malinen  j@w1.fi  and
    contributors.
    All Rights Reserved.


This program is licensed under the BSD license (the one with
    advertisement clause removed).
