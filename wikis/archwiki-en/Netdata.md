# Netdata

netdata is a system for distributed real-time performance and health monitoring. netdata is created by the group that also created FireHOL and FireQOS.

netdata is designed to permanently run on all systems (physical and virtual servers, containers, IoT devices), without disrupting their core function.

Netdata allows to create dashboards of multiple servers, which stream on the fly the data from them to the browser. This functionality is called cloud and available through their website. This service is free of charge.

## Installation
Install the  package. The installation package includes go.d.plugin.

Start/enable the  service.

## Configuration
Netdata reads its configuration file from . This configuration file is not needed by default. Netdata works with the default settings without it, but it does allow you to adapt the general behavior of Netdata. You can find all these settings (and their default values) by accessing the http://localhost:19999/netdata.conf URL.

The plugins folders is at  and their configuration at .

## Enable cloud connection
The old way to connect to Netdata Cloud () was deprecated in favor of the "kickstart" script that is not provided as part of the Netdata package. As such, the way to get the connection online is:

# Make sure the  package is installed and the  systemd service is running already. Otherwise the script may try to make changes to your system outside the package manager.
# Go to the Netdata Cloud dashboard and copy the "kickstart" command (with claim tokens etc) for adding a new node.
# Add the  argument to the command line before running it.

The node should then show up in the dashboard but upgrades will be managed by Pacman as per usual.

## Disable cloud integration
To hide all Netdata Cloud advertisements and connection attempts:

If the  folder does not exist (which is the case if Netdata was just installed without starting it for the first time), create it:

 # mkdir -p /var/lib/netdata/cloud.d
 # chown -R netdata:netdata /var/lib/netdata

## Behind a web server
netdata can be run behind another web server (proxy) and you can configure it accordingly. The netdata documentation has examples for Apache, Nginx, lighttpd, haproxy and caddy.

## Built-in web server
netdata is accessible at http://localhost:19999/ by default.

To enable remote IPv4 () and IPv6 () access, edit :

 bind to = 0.0.0.0 [::

## Telemetry
Netdata collects anonymous usage information through its own infrastructure and via PostHog by default. To opt out of this telemetry functionality, create the following configuration file:

 # touch /etc/netdata/.opt-out-from-anonymous-statistics

More details on the data gathered can be found here.

## Optimization
netdata can be optimized for different scenarios.https://learn.netdata.cloud/docs/netdata-agent/configuration/how-to-optimize-the-netdata-agent-s-performance
