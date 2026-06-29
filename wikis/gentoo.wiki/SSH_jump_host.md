SSH jump hosts are employed as an alternative to [SSH tunneling](https://wiki.gentoo.org/wiki/SSH_tunneling "SSH tunneling") to access internal machines through a gateway.

The idea is to use ProxyCommand to automatically execute the [ssh] command on remote host to jump to the next host and forward all traffic through.

## Contents

-   [[1] [Prerequisites]](#Prerequisites)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Single jump]](#Single_jump)
    -   [[2.2] [Multiple jump]](#Multiple_jump)
    -   [[2.3] [Static jump host list]](#Static_jump_host_list)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Single jump]](#Single_jump_2)
    -   [[3.2] [Multiple jump]](#Multiple_jump_2)
    -   [[3.3] [Dynamic jump host list]](#Dynamic_jump_host_list)
    -   [[3.4] [Tips]](#Tips)
-   [[4] [See also]](#See_also)
-   [[5] [External resources]](#External_resources)

## [Prerequisites]

-   SSH access to the gateway machine and the internal one.
-   Gateway machine has Netcat installed.

## [Configuration]

### [[] Single jump]

`ProxyJump` hosts can be defined inside each user\'s SSH [config] file.

[FILE] **`~/.ssh/config`ProxyJump Example**

    ### First jump host. Directly reachable
    Host betajump
      HostName jumphost1.example.org

    ### Host to jump to via jumphost1.example.org
    Host behindbeta
      HostName behindbeta.example.org
      ProxyJump  betajump

See the corresponding single jump section under Usage below.

### [[] Multiple jump]

The same syntax can be used to make jumps over multiple machines:

[FILE] **`~/.ssh/config`Add this text**

    ### First jump host. Directly reachable
    Host alphajump
      HostName jumphost1.example.org

    ### Second jumphost. Only reachable via jumphost1.example.org
    Host betajump
      HostName jumphost2.example.org
      ProxyJump alphajump

    ### Host only reachable via alphajump and betajump
    Host behindalphabeta
      HostName behindalphabeta.example.org
      ProxyJump betajump

See the corresponding multiple jump section under Usage below.

`user `[`$`]`ssh behindalphabeta`

### [Static jump host list]

Static jump host list means, that the jump host(s) are known and can be defined before initiating the first ssh connection. Therefore a static jump host \'routing\' can be defined in the user\'s [\~/.ssh/config] file. The advantage in comparison to the dynamic jump host option is, that you don\'t have to provide the .ssh config on jump hosts between your machine and all the other jump hosts between you and the final host you want to jump to.

## [Usage]

### [[] Single jump]

`user `[`$`]`ssh behindalpha`

If usernames on machines differ, specify them by modifying the correspondent `ProxyJump` line:

[FILE] **`~/.ssh/config`Modify correspondent ProxyCommand**

    ProxyJump  otheruser@behindalpha

It works with the [scp] command, too:

`user `[`$`]`scp filename behindalphabeta:~/`

** Note**\
The colon and path at the end is needed so that [scp] recognizes it as remote.

### [[] Multiple jump]

The same syntax can be used to make jumps over multiple machines:

`user `[`$`]`ssh -J user1@host1:port1,user2@host2:port2 user3@host3`

### [Dynamic jump host list]

The `-J` option can be used to jump through a host:

`user `[`$`]`ssh -J host1 host2`

If usernames or ports on machines differ, specify them:

`user `[`$`]`ssh -J user1@host1:port1 user2@host2 -p port2`

### [Tips]

To ease the connecting even further:

-   Set these commands as [shell aliases](https://en.wikipedia.org/wiki/Alias_(command) "wikipedia:Alias (command)")
-   To avoid typing passwords use [OpenSSH keys](https://wiki.gentoo.org/wiki/SSH#Passwordless_authentication "SSH")

## [See also]

-   [SSH](https://wiki.gentoo.org/wiki/SSH "SSH") --- the ubiquitous tool for logging into and working on remote machines securely.

## [External resources]

-   [SSH through jump hosts](https://glandium.org/blog/?p=308)
-   [[[net-misc/connect]](https://packages.gentoo.org/packages/net-misc/connect)[]] --- [SSH Proxy Command \-- connect.c](https://bitbucket.org/gotoh/connect/wiki/Home)