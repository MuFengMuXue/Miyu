# Wpa Supplicant / Doc / Docbook / Eapol Test

07 August 2019


     eapol_test
     8


eapol_test


EAP peer and RADIUS client testing


       eapol_test
       -nWS
       -c config file
       -a server IP address
       -A client IP address
       -p UDP port
       -s shared secret
       -r re-authentications
       -t timeout
       -C Connect-Info
       -M MAC address
       -o file
       -N attr spec


       eapol_test scard


       eapol_test sim
       PIN
       num triplets


Overview


eapol_test is a program that links together the same EAP
    peer implementation that wpa_supplicant is using and the RADIUS
    authentication client code from hostapd. In addition, it has
    minimal glue code to combine these two components in similar
    ways to IEEE 802.1X/EAPOL Authenticator state machines. In other
    words, it integrates IEEE 802.1X Authenticator (normally, an
    access point) and IEEE 802.1X Supplicant (normally, a wireless
    client) together to generate a single program that can be used to
    test EAP methods without having to setup an access point and a
    wireless client.


The main uses for eapol_test are in interoperability testing
    of EAP methods against RADIUS servers and in development testing
    for new EAP methods. It can be easily used to automate EAP testing
    for interoperability and regression since the program can be run
    from shell scripts without require additional test components apart
    from a RADIUS server. For example, the automated EAP tests described
    in eap_testing.txt are implemented with eapol_test. Similarly,
    eapol_test could be used to implement an automated regression
    test suite for a RADIUS authentication server.


As an example:


eapol_test -ctest.conf -a127.0.0.1 -p1812 -ssecret -r1


tries to complete EAP authentication based on the network
    configuration from test.conf against the RADIUS server running
    on the local host. A re-authentication is triggered to test fast
    re-authentication. The configuration file uses the same format for
    network blocks as wpa_supplicant.


Command Arguments


-c configuration file path


A configuration to use.  The configuration should
	use the same format for network blocks as wpa_supplicant.


-a AS address


IP address of the authentication server.  The
	default is '127.0.0.1'.


-A client address


IP address of the client.  The default is to
	select an address automatically.


-p AS port


UDP port of the authentication server. The
	default is '1812'.


-s AS secret


Shared secret with the authentication server.
	The default is 'radius'.


-r count


Number of reauthentications.


-t timeout


Timeout in seconds. The default is 30.


-C info


RADIUS Connect-Info.  The default is
	'CONNECT 11Mbps 802.11b'.


-M mac address


Client MAC address (Calling-Station-Id).  The
	default is '02:00:00:00:00:01'.


-o file


Location to write out server certificate.


-N attr spec


Send arbitrary attribute specific by
	attr_id:syntax:value, or attr_id alone.  attr_id should be the numeric
	ID of the attribute, and syntax should be one of 's' (string),
	'd' (integer), or 'x' (octet string). The value is the attribute value
	to send.  When attr_id is given alone, NULL is used as the attribute
	value.  Multiple attributes can be specified by using the option
	several times.


-n


Indicates that no MPPE keys are expected.


-W


Wait for a control interface monitor before starting.


-S


Save configuration after authentication.


See Also


	 wpa_supplicant
	 8


Legal


wpa_supplicant is copyright (c) 2003-2022,
    Jouni Malinen  j@w1.fi  and
    contributors.
    All Rights Reserved.


This program is licensed under the BSD license (the one with
    advertisement clause removed).
