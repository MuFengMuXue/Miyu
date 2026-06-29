# TFTP

The Trivial File Transfer Protocol (TFTP) provides a minimalistic means for transferring files. It is generally used as a part of PXE booting or for updating configuration and firmware on devices which have limited memory such as routers, IP phones and printers.

## Server
There are several TFTP server implementations, some of which are listed below.

## tftp-hpa
Install  and then start .

To modify service parameters edit .

## URL rewriting
This server includes a useful URL rewriting feature via the  option ( in some versions). It allows requests to be altered via regular expressions so the files on the server do not have to match the view the client sees, and different files can be returned to different clients even if they request the same file.

Configure a map by adding  to  and creating a file such as this:

This example file will result in each TFTP request being prefixed with the remote IP address. For example if the machine at 192.168.0.1 requests "boot.bin" and the TFTP server root is  then the file  will be returned (or  if the server is listening on an IPv6 port).

The available map file options are documented in .

## Debugging
The  option can be used to turn on all debugging messages.  This is very useful for diagnosing why a machine will not successfully boot from the network, as the debug messages list all requests for files, whether rewrite rules were used, where the files were read from on the filesystem and whether the request was successful or not.

It is not possible to log messages to stdout/stderr, as only syslog is supported.  This means the messages can be viewed with journalctl or similar.

## atftp
Install  and then start .

To modify service parameters edit .

## uftpd
 is a simple (T)FTP server that can be run from the command line:

 # uftpd -n -o ftp=0,tftp=69 /tmp/tftp

The option  disables the FTP server and only runs TFTP. The server runs in read-only mode by default and passing  allows clients to put files on the server. The  is redundant in the case of default port, but shows a way to select a different one.

## dnsmasq
See dnsmasq#TFTP server.

## Client
## tftp-hpa
Install  and then tftp your day away!

 $ tftp

## atftp
The package  contains both a server and a client with interactive and batch mode. The client binary is  and supports both getting and putting files.

## curl
Standard  has an ability to connect to a TFTP server and upload a file via:

 $ curl -T FILE tftp://HOST

Download a file:

 $ curl -o DESTINATION tftp://HOST/file

Where  is relative to the TFTP root directory.
