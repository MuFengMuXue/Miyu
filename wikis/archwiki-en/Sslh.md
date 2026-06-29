# Sslh

sslh is a ssl/ssh multiplexer.

## Installation
Install the  package.

## Configuration
The default configuration file is located at , which supports , , , , , and  protocols.

2 additional configuration files are included in the package:
* , which is a basic configuration file that should provide sensible values for "standard" setup.
* , which is provided as documentation to show what is possible. It should not be used as-is, and probably should not be used as a starting point for a working configuration.

## Usage
Start/enable  or , depending on which option is right for your server:
*  forks a new process for each incoming connection. It is well-tested and very reliable, but incurs the overhead of many processes. If you're going to use  for a "small" setup (less than a dozen SSH connections and a low-traffic HTTPS server), then  is probably the best option for you.
*  uses only one thread, which monitors all connections at once. It is more recent and less tested, but the main process only incurs a 16 byte overhead per connection. However, if it stops then you will lose all non-forked connections, which means you can only upgrade it remotely if the necessary connections are set to fork mode. If you're going to use  on a "medium" setup (a few thousand SSH connections, and another few thousand SSL connections),  will be the most suitable option.
*  is the most recent option, introduced in version 2.0. It's almost functionally identical to , but uses  to scale much higher, making it ideal if you have a very large site (tens of thousands of connections).
