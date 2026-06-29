**Resources**

[[]][Home](https://www.harding.motd.ca/autossh/index.html)

[[]][Official documentation](https://www.harding.motd.ca/autossh/README.txt)

AutoSSH is a command that detects when [SSH](https://wiki.gentoo.org/wiki/SSH "SSH") connections drop and automatically reconnects them.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Important tips]](#Important_tips)
    -   [[2.2] [Examples]](#Examples)
-   [[3] [Removal]](#Removal)
    -   [[3.1] [Unmerge]](#Unmerge)
-   [[4] [See also]](#See_also)
-   [[5] [External resources]](#External_resources)

## [Installation]

### [Emerge]

`root `[`#`]`emerge --ask net-misc/autossh`

## [Configuration]

### [Important tips]

The \"-M\" option **is** required, even if you don\'t want to use the monitoring option (in which case, use \"-M 0\").

When using \"-M\"\...

-   Connections are tunnelled. No firewall changes needed for autossh\'s monitoring feature.
-   Ports need to be above 1024 if you are not logging in as root.
-   If you use a password prompt, then autossh will wait for your password when it reconnects, and it won\'t be fully connected until you give that password. So, it is helpful to use a key (instead of password) and ssh-agent.

### [Examples]

1\) Simple login example

`user `[`$`]`autossh -M 0 username@myserver`

2\) More Complex Example

SSH on port 222. Setup a SOCKS proxy on port 9999. Using \"ServerAliveInterval\" and \"ServerAliveCountMax\" as recommended in the autossh README file.

`user `[`$`]`autossh -M 0 -p 222 -N -D 9999 -o "ServerAliveInterval 45" -o "ServerAliveCountMax 2" username@myserver`

3\) Use autossh with sshfs

`user `[`$`]`sshfs -o reconnect,compression=yes,transform_symlinks,ServerAliveInterval=45,ServerAliveCountMax=2,ssh_command='autossh -M 0' username@server:/ /mnt/remote"`

## [Removal]

### [Unmerge]

`root `[`#`]`emerge --ask --depclean --verbose net-misc/autossh`

## [See also]

-   [SCP](https://wiki.gentoo.org/wiki/SCP "SCP") --- an interactive file transfer program, similar to the [copy] command, that copies files over an encrypted SSH transport.
-   [SFTP](https://wiki.gentoo.org/wiki/SFTP "SFTP") --- an interactive file transfer program, similar to [FTP](https://wiki.gentoo.org/wiki/FTP "FTP"), which performs all operations over an encrypted [SSH](https://wiki.gentoo.org/wiki/SSH "SSH") transport.
-   [SSH](https://wiki.gentoo.org/wiki/SSH "SSH") --- the ubiquitous tool for logging into and working on remote machines securely.
-   [SSHFS](https://wiki.gentoo.org/wiki/SSHFS "SSHFS") --- a secure shell client used to mount remote filesystems to local machines.

## [External resources]

-   [https://wiki.openwrt.org/doc/howto/autossh](https://wiki.openwrt.org/doc/howto/autossh) - OpenWRT\'s wiki page on autossh.
-   [https://www.linuxjournal.com/content/autossh-all-your-connection-lost](https://www.linuxjournal.com/content/autossh-all-your-connection-lost) - A short autossh article written by Linux Journal.