# Ii

IRC it (ii) is:
:a minimalist FIFO and filesystem-based IRC (Internet Relay Chat) client. It creates an IRC directory tree with server, channel and nick name directories. In every directory a FIFO in file and a normal out file is created.

## Installation
Install the  package.

## Configuration
ii is configured via command line options. The default values are  for the main directory, and  for nickname. These can be changed by passing values to ii when run:

 -s server
 -p port
 -u socket (-p option is ignored if this is set)
 -i main.directory
 -n nickname
 -f realname
 -k environmental.variable

ii uses an environmental variable to contain your irc password (i.e., ).

## Usage
For a detailed introduction see the official documentation.

A session manager such as abduco or tmux is recommended. It allows the user to easily disconnect and reconnect to a session.

To start ii, run:

 $ ii

See also .

## Additional functions
ii serves solely as a client for the server. Additional applications will be needed to both read output and write input to ii. In each subdirectory, there will be an output file, "out" and an input file, "in". At a minimum, the output file can be monitored with:

 $ tail -f out

and the input with:

 $ echo "command/message" > in

Another option that allows for a single command to accept ongoing input is:

 $ cp /dev/stdin in

## Commands
ii commands start with a slash and are case sensitive.

{| class="wikitable"
! Command
! Description
|-
|
| mark as away with optional message
|-
|

| join a channel with optional password;
open a private conversation with user and optional opening message
|-
|
| leave channel with optional message
|-
|
| change nickname
|-
|
| quit ii with optional message
|-
|
| set topic of channel
|}

Everything which is not a command will be posted into the channel or to the server. So if you need  just write  as described in RFC:1459 to the server in FIFO.

## SSL/TLS encryption
ii does not support the Transport Layer Security (TLS), and needs a proxy to connect it to a TLS client. An example of this would be with stunnel:

Then use  and  for stunnel to redirect ii to secure connection to the server.

Another option is the use of  for a proxy with ii connecting via UNIX stream socket:

 $ socat UNIX-LISTEN:/tmp/irc.libera.chat OPENSSL:irc.libera.chat:6697
 $ ii -s irc.libera.chat -u /tmp/irc.libera.chat

## Tips and tricks
## Using sed to edit output
Sed can be used to edit  output in ways that make it more readable. Example:

{{bc|
#!/bin/sh
tail -n 55 -f out  sed -u '/-\!-.*has/d;
                          s//\x1bs/\(> >\)\( .*\)/\1\x1b[33m\2\x1b[0m/;
                          s/http[^ >)*/\x1bs/[\"\$\`/\\&/g;
                          s/\(^0-9\{10\}\)\( .*\)/date -d@\1 "+%Y.%m.%d %H.%M.%S""\2"/e'
}}

In this example, the first part of the sed command hides (deletes from the command output) the join, part and quit; the second one adds green color control codes around your nickname; the third one does the same for "highlights" in yellow; the fourth with red on URLs; the penultimate prepares the output of the command before the last one substitutes the UNIX epoch timestamps with a human readable date.
