# HAproxy

HAProxy is a free, very fast and reliable solution offering high availability, load balancing, and proxying for TCP and HTTP-based applications. It is particularly suited for very high traffic web sites and powers quite a number of the world's most visited ones. Over the years it has become the de-facto standard opensource load balancer, is now shipped with most mainstream Linux distributions, and is often deployed by default in cloud platforms.

## Installation
Install the  package.

## Running
Enable . HAProxy's configuration can be reloaded live by reloading  as root.

## Configuration
An example configuration is available in . Edit it to suit your needs, and then start .

## General configuration
## ACLs
HAProxy supports ACLs, which can be used to test conditions and perform a given action based on the results of those tests. A typical ACL would be written as follows:

In this case, the ACL is matched if the user's request path begins with .

## Backends
In HAProxy terminology, backends are a server or set of servers that will receive forwarded requests. Backends can balance load based on several load balancing algorithms, including:

* Round-robin
* Static round-robin (also known as weighted round-robin)
* Least connections

An example backend may be written as follows:

## Frontends
Frontends are used to define how requests should be forwarded to backends. They consist of the following:

* IP addresses and ports
* ACLs
* use_backend rules

## Health checks
When a backend is declared with the  option, HAProxy will check on startup and on scheduled intervals if the backend is available to process forwarded requests. If a backend fails the health check, it will be removed from rotation until it is deemed to be healthy again, i.e. it passes the health check.

By default, HAProxy will attempt to establish a TCP connection to the backend to determine healthiness.

If a large number of backends are declared with the  option, HAProxy will query all of them on startup, which may delay startup time.

## Logging with systemd
To configure HAproxy to use systemd  compatibility socket add the following to your configuration file under the  section.

 log /dev/log local0 info

If you use the  option in your global configuration, you need to bind the socket into the chroot.

For this we will use a  unit. Generate the unit name with:

 # systemd-escape --suffix=mount --path /var/lib/haproxy/dev/log

We want mount  into the chroot, but just after journald came up. Create a replacement unit file:

With the mount file created it is time to expand the original service unit so it mounts up everything correctly. Use a drop-in file for  and add:

## Performing TLS/SSL termination
In order to use haproxy as a TLS terminator you have to set inside your  section

 bind :80
 bind :443 ssl crt /path/to/combined/cert

## Redirecting HTTP to HTTPS
Set in your  section

 redirect scheme https code 301 if !{ ssl_fc }

## Virtual host like configuration
Suppose you have two backends:  and  and each should handle requests only for a specific domain.
In order to perform this in your  section you can configure

 use_backend foo-backend if { hdr(host) -i foo.example.com || hdr(host) -i www.foo.example.com }
 use_backend bar-backend if { hdr(host) -i bar.example.com || hdr(host) -i www.bar.example.com }
