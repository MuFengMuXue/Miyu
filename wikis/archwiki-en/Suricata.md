# Suricata

From the project home page:
:Suricata is a high performance Network IDS, IPS and Network Security Monitoring engine. Open Source and owned by a community run non-profit foundation, the Open Information Security Foundation (OISF). Suricata is developed by the OISF and its supporting vendors.

## Installation
Install the  package.

## Configuration
The main configuration file is .

You should change the following parts of the configuration in order to make it run:

   default-log-dir: /var/log/suricata/     # where you want to store log files
   classification-file: /etc/suricata/classification.config
   reference-config-file: /etc/suricata/reference.config
   HOME_NET: "# your local network
   host-os-policy:   ..                    # according to the OS running the ips
   magic-file: /usr/share/file/misc/magic.mgc

## Web interface
You may use Scirius CE [https://github.com/StamusNetworks/scirius or SELKS https://github.com/StamusNetworks/SELKS as web interface for rule management, log analysis, and other sensor management options.

## Starting Suricata
## Manual startup
You may start the suricata service manually with:

## systemd service configuration
To start Suricata automatically at system boot, enable .
