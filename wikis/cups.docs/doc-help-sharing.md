# Printer Sharing

This document discusses several ways to configure printer sharing.

The Basics

A "server" is any machine that communicates directly to a printer. A "client" is any machine that sends print jobs to a server for final printing. Clients can also be servers if they communicate directly with any printers of their own.

By default, CUPS uses the Internet Printing Protocol (IPP) to send jobs from a client to a server. When printing to legacy print servers you may also use the Line Printer Daemon (LPD) protocol when printing to older UNIX-based servers or Server Message Block (SMB) when printing to Windows<sup>®</sup> servers.

Clients can automatically discover and access shared printers via DNS Service Discovery (DNS-SD a.k.a. Bonjour<sup>®</sup>). SMB browsing can also be used to manually discover and access shared printers when [Samba](http://www.samba.org/) is installed.

## Configuring the Server

You must enable printer sharing on the server before clients can print through it. The simplest way to do this is to use the [cupsctl(8)](man-cupsctl.html) command on the server:

``` command
cupsctl --share-printers
```

By default, the above command will allow printing from other clients on the same subnet as your server. To allow printing from any subnet, use the following command instead:

``` command
cupsctl --share-printers --remote-any
```

Next, tag each printer that you want to share using the [lpadmin(8)](man-lpadmin.html) command on the server, for example:

``` command
lpadmin -p printer -o printer-is-shared=true
```

You can require authentication for shared printing by setting the policy on each printer, for example:

``` command
lpadmin -p printer -o printer-op-policy=authenticated
```

## Automatic Configuration using IPP

> **Note:**
>
> This method of configuration does not work on macOS 10.7 or later because sandboxed applications do not always have direct network access.

CUPS can be configured to run without a local spooler and send all jobs to a single server. However, if that server goes down then all printing will be disabled. Use this configuration only as absolutely necessary.

The default server is normally the local system ("localhost"). To override the default server create a file named `/etc/cups/client.conf` with a line as follows:

``` example
ServerName server
```

The `server` name can be the hostname or IP address of the default server. If the server is not using the default IPP port (631), you can add the port number at the end like this:

``` example
ServerName server:port
```

The default server can also be customized on a per-user basis. To set a user-specific server create a file named `$HOME/.cups/client.conf` instead. The user `client.conf` file takes precedence over the system one.

Finally, you can set the `CUPS_SERVER` environment variable to override the default server for a single process, for example:

``` command
CUPS_SERVER=server:port firefox https://openprinting.github.io/cups
```

will run the Firefox web browser pointed to the specified server and port. The environment variable overrides both the user and system `client.conf` files, if any.

## Manual Configuration of Print Queues

> **Note:**
>
> This method of configuration does not work on macOS 10.7 or later because sandboxed applications do not always have direct network access.

The most tedious method of configuring client machines is to configure each remote queue by hand using the [lpadmin(8)](man-lpadmin.html) command:

``` command
lpadmin -p printer -E -v ipp://server/printers/printer -m everywhere
```

The `printer` name is the name of the printer on the server machine. The `server` name is the hostname or IP address of the server machine. Repeat the **lpadmin** command for each remote printer you wish to use.
