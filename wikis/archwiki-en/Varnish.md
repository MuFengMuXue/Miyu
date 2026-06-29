# Varnish

Varnish Cache is a web application accelerator also known as a caching HTTP reverse proxy. You install it in front of any HTTP server and configure it to cache the contents.

## Installation
Install the  package.

## Customizing Varnish
By default, varnish comes configured in  to use  as the only backend,  is called by the default  file.

You can enable the unit as-is, or override the defaults by editing it.

 Service
 ExecStart=
 ExecStart=/usr/bin/varnishd -j unix,user=nobody -F -a :6081 -T localhost:6082 -f /etc/varnish/default.vcl -S /etc/varnish/secret -s malloc,1G

Also, if you change the configuration file  you will need to reload :

## Manual VCL load
If the previous VCL configuration reload failed, try loading the VCL file manually:

# Connect to the varnish console:
# Load the default VCL. Make sure it has at least one backend:
# Make it active:
# Start the child proccess (optional):
