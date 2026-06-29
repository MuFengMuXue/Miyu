# Wpa Supplicant / Doc / Docbook / Wpa Passphrase

07 August 2019


     wpa_passphrase
     8


wpa_passphrase


Generate a WPA PSK from an ASCII passphrase for a SSID


       wpa_passphrase
        ssid
        passphrase


Overview


 wpa_passphrase  pre-computes PSK entries for
    network configuration blocks of a
     wpa_supplicant.conf  file. An ASCII passphrase
    and SSID are used to generate a 256-bit PSK.


Options


ssid


The SSID whose passphrase should be derived.


passphrase


The passphrase to use. If not included on the command line,
	  passphrase will be read from standard input.


See Also


	 wpa_supplicant.conf
	 5


	 wpa_supplicant
	 8


Legal


wpa_supplicant is copyright (c) 2003-2022,
    Jouni Malinen  j@w1.fi  and
    contributors.
    All Rights Reserved.


This program is licensed under the BSD license (the one with
    advertisement clause removed).
