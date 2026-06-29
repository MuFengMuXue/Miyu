# Prosody

From the official website:

:Prosody is a modern XMPP communication server. It aims to be easy to set up and configure, and efficient with system resources. Additionally, for developers it aims to be easy to extend and give a flexible system on which to rapidly develop added functionality, or prototype new protocols.

## Installation
Install the  package.

## Optional dependencies
Prosody has optional dependencies that although not strictly required for its operation, provide useful features.

; TLS/SSL Support (Recommended)
: Allow Prosody to encrypt streams to prevent eavesdropping.
: Requires:
; MySQL/Postgresql Backend
: Allow Prosody to use a MySQL/mariadb/Postgresql backend for better scaling and performance.
: Requires:
; Better Connection Scaling (Recommended)
: Allow Prosody to use libevent to handle a greater number of simultaneous connections.
: Requires:
; Stream Compression
: Allow Prosody to compress client-to-server streams for compatible clients to save bandwidth.
: Requires:

## Configuration
The main configuration file is located at . Information on how to configure Prosody can be found in Prosody's documentation. The syntax of the configuration file can be checked after any changes are made by running:

 # luac -p /etc/prosody/prosody.cfg.lua

No output means the syntax is correct.

## Authentication
The default configuration uses mod_auth_internal_hashed. If you remove the line, it will default to mod_auth_internal_plain.

## Logging
The  package is pre-configured to log to syslog. Thus, by default, Prosody log messages are available in the systemd journal.

## Usage
Start/enable the  systemd service.

Prosody uses the default XMPP ports, 5222 and 5269, for client-to-server and server-to-server communications respectively. Configure your firewall as necessary.

You can manipulate Prosody users by using the  program. To add a user:

 # prosodyctl adduser JID

See  for details.

## Security
## User registration
Prosody supports XMPP's in-band registration standard, which allows users to register with an XMPP client from within their client and change their passwords. While this is convenient for users it does not allow administrators to moderate the registration of new users. As such, the  module is enabled in the default configuration but  is set to . This allows existing users to change their passwords from within their client but does not allow new users to register themselves.

## Stream encryption
Prosody can utilize TLS certificates to encrypt client-to-server communications (if the proper dependencies are installed). See the relevant sections of  to configure Prosody to utilize these certificates.

To require encryption for client-to-server communications add the following to your configuration file:

Similarly, for server-to-server communications you may do:

While requiring client-to-server encryption is generally a good idea, please keep in mind that some popular XMPP services such as Google Talk/Gmail do not support server-to-server encryption.

## Listing users
A simple way to see a list of the registered users is
 # ls -l /var/lib/prosody/*/accounts/*

alternatively, you can download the module mod_listusers.lua, and use it as
 # prosodyctl mod_listusers

## Removal
After normally uninstalling Prosody with pacman, the  and  directories may be left on your filesystem, and you may want to remove them if you do not plan on reinstalling Prosody.

## Tips and tricks
## Components
Prosody supports XMPP components, which provide extra services to clients. Components are either provided internally by special Prosody modules or externally using the protocol specified in XEP-0114.

By default, Prosody will listen for external components. If you do not plan to use any external components with Prosody you can disable this behavior by adding the following your configuration:

{{hc|/etc/prosody/prosody.cfg.lua|2=
component_ports = {}
}}

## Multi-User Chat
A common component used with XMPP servers is Multi-User Chat (MUC), which allows conferences between multiple users. MUC is provided as an internal component with Prosody. To enable MUC add the following to your configuration file:

This will enable the MUC component on host .

## Prosody modules
Prosody Modules is a collection of extra modules not distributed with Prosody. These modules are in various states of development from highly experimental to relatively stable. You should consult a given module's wiki page for more information. An example of an extra module is pastebin, which when loaded will intercept long messages (for example, log file output) and replace them with a link to a pastebin hosted using Prosody's internal HTTP server (provided by the core module, ).

To use an extra module download its raw file(s) from the source browser (when viewing a file, search for the link "View raw file"). Alternatively and likely easier, use Mercurial to clone the entire repository:

 $ hg clone https://hg.prosody.im/prosody-modules/ prosody-modules

Now you can copy the module (and any additional files it needs) to Prosody's module directory at . To enable the module add it to your  list in your  for the host or component you wish to use it for. For example, to use the  module on a MUC component:

{{hc|/etc/prosody/prosody.cfg.lua|2=
Component "conference.example.com" "muc"
    modules_enabled = { "pastebin" }
}}

## Console
The  module provides a telnet console from which administrative operations and queries can be performed. You can connect to the console by issuing:

 $ telnet localhost 5582

You of course need the  program provided by the  package. Use the  command in the console to get usage help.

The console even allows you to execute Lua commands directly on the server by preceding a command with . For example to see if a client connection is compressed:

 > full_sessionsWill return  if the connection is compressed or  if it is not.

## Troubleshooting
One of Prosody's primary design principles is to be simple to use and configure. However, issues can still arise (and likely will as is the case with any complex software). If you encounter a problem there are a variety of steps you can take to narrow down the cause:

; Check for known issues: Look at the [https://prosody.im/doc/release release notes for your Prosody version to see if your issue is listed as a known issue. Also check the issue tracker to see if your issue has already been reported.
; Check configuration syntax: Run  to check for any syntax errors in your configuration file. If there is no output your syntax is fine.
; Check the log: Errors are only logged if there is a critical problem so always address those issues. If you think you have a very low level issue (like protocol compatibility between clients and servers with Prosody) then you can enable the very verbose debug level logging.
; Check permissions: The Prosody package should add a new  user and group to your system and set appropriate permissions, but it is always good to double check. Ensure that  and  are owned by the  user and that the user has appropriate permissions to read and write to those paths and all contained files.
; Check listening ports: When troubleshooting connection issues make sure that Prosody is actually listening for connections. You may do so by running  and making sure that  (port 5222) and  (port 5269) are listed.
; Restart: Like most things, it does not hurt to restart  to see if it resolves an issue.

If you are unable to resolve your issue yourself there are a variety of resources you can use to seek help. In order of immediacy with which you will likely receive help:

# XMPP Conference:
# Mailing List: , web interface
# Arch Forums (for package issues)

## Development
A development packages is maintained for Prosody in the AUR, .  tracks the Mercurial repository tip for Prosody and will always contain the latest code as it is checked in. Both packages are built similarly to the stable package.

## Communication
* Mailing Lists: prosody-dev, prosody-users
* Conference:
* Blog: Prosodical Thoughts
