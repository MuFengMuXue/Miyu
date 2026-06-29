Other languages:

-   [English]
-   [español](https://wiki.gentoo.org/wiki/Keychain/es "Keychain (65% translated)")
-   [français](https://wiki.gentoo.org/wiki/Keychain/fr "Keychain (68% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/Keychain/hu "Kulcstartó (100% translated)")
-   [polski](https://wiki.gentoo.org/wiki/Keychain/pl "Keychain/pl (0% translated)")
-   [русский](https://wiki.gentoo.org/wiki/Keychain/ru "Keychain (92% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/Keychain/zh-cn "Keychain (54% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Keychain/ja "Keychain (72% translated)")
-   [한국어](https://wiki.gentoo.org/wiki/Keychain/ko "Keychain/ko (61% translated)")

**Resources**

[[]][Home](https://www.funtoo.org/Keychain)

[[]][Package information](https://packages.gentoo.org/packages/net-misc/keychain)

[[]][GitHub](https://github.com/funtoo/keychain)

[![Ohloh Logo](/images/thumb/c/c1/Ohloh-logo.png/30px-Ohloh-logo.png)][Open Hub](https://www.openhub.net/p/keychain)

This document describes how to use [SSH](https://wiki.gentoo.org/wiki/SSH "SSH") shared keys along with the keychain program. It assumes basic knowledge of public key cryptography.

Keychain is a frontend to [ssh-agent] and [ssh-add], allowing long running sessions and letting the user enter passphases just once. It can also be used to allow scripts access to SSH connections.

## Contents

-   [[1] [Background]](#Background)
    -   [[1.1] [The problem at hand]](#The_problem_at_hand)
    -   [[1.2] [How does public key authentication work?]](#How_does_public_key_authentication_work.3F)
-   [[2] [How to use public key authentication]](#How_to_use_public_key_authentication)
    -   [[2.1] [Generating a key pair]](#Generating_a_key_pair)
    -   [[2.2] [Preparing the server]](#Preparing_the_server)
    -   [[2.3] [Testing the setup]](#Testing_the_setup)
-   [[3] [Making public key authentication convenient]](#Making_public_key_authentication_convenient)
    -   [[3.1] [Typical key management with ssh-agent]](#Typical_key_management_with_ssh-agent)
    -   [[3.2] [Squeezing the last drop of convenience out of ssh-agent]](#Squeezing_the_last_drop_of_convenience_out_of_ssh-agent)
    -   [[3.3] [Using keychain with Plasma 5]](#Using_keychain_with_Plasma_5)
        -   [[3.3.1] [Alternatively use KWallet with kde-plasma/ksshaskpass under Plasma 5]](#Alternatively_use_KWallet_with_kde-plasma.2Fksshaskpass_under_Plasma_5)
-   [[4] [Concluding remarks]](#Concluding_remarks)
    -   [[4.1] [Security considerations]](#Security_considerations)
    -   [[4.2] [Troubleshooting]](#Troubleshooting)
-   [[5] [See also]](#See_also)
-   [[6] [External resources]](#External_resources)

## [Background]

### [The problem at hand]

Having to type in login passwords on each and every system is inconvenient, especially if many systems are being managed. Some administrators might even have a need for a script or cron-job that needs a convenient way to use an ssh connection. Either way, there is a solution to this problem, and it begins with public key authentication.

### [][How does public key authentication work?]

Assume that a client wants to connect to the ssh daemon on a server. The client first generates a key pair and gives the public key to the server. Afterwards, whenever the client attempts to connect, the server sends a challenge that is encrypted with that public key. Only the holder of the corresponding private key (the client) is able to decrypt it, so the correct response leads to successful authentication.

## [How to use public key authentication]

### [Generating a key pair]

The first step is to create a key pair. To do this, use the [ssh-keygen] command:

`user `[`$`]`ssh-keygen`

Accept the default values, and make sure to enter a strong passphrase.

** Warning**\
Be sure to choose a strong passphrase, especially if this key is used for root logins!

After the generation has ended a private key should be located at [\~/.ssh/id_rsa] and a public key in [\~/.ssh/id_rsa.pub]. The public key is now ready to be copied to the remote host.

Adding or changing a passphrase for the private key can be done as follows:

`user `[`$`]`ssh-keygen -p -f ~/.ssh/id_rsa`

### [Preparing the server]

The [\~/.ssh/id_rsa.pub] file needs to be copied over to the server running [sshd]. It has to be added to the [\~/.ssh/authorized_keys] file that belongs the connecting user on the remote server. After [ssh] access to the server has been granted by infrastructure personnel, the following steps can be used to setup automatic login using a public key on the remote server:

`user `[`$`]`ssh-copy-id -i ~/.ssh/id_rsa.pub server_user@server`

[ssh-copy-id] is a wrapper script for these steps. If this wrapper script is unavailable, then the following steps can be used:

`user `[`$`]`scp ~/.ssh/id_rsa.pub server_user@server:~/myhost.pub `

`user `[`$`]`ssh server_user@server "cat ~/myhost.pub >> ~/.ssh/authorized_keys" `

`user `[`$`]`ssh server_user@server "cat ~/.ssh/authorized_keys"`

The output from that last line should show the contents of the [\~/.ssh/authorized_keys] file. Make sure the output looks correct.

### [Testing the setup]

Theoretically, if all went well, and the [sshd] daemon on the server allows it (as this can be configured), [ssh] access without entering a password should now be possible on the server. The private key on the client will still need to be decrypted with the passphrase used previously, but this should not be confused with the password of the user account on the server.

`user `[`$`]`ssh <server_user>@<server>`

It should have asked for a passphrase for [id_rsa], and then grant access via [ssh] as the user `<server_user>` on the server. If not, login as `<server_user>`, and verify that the contents of [\~/.ssh/authorized_keys] has each entry (which is a public key) on a single line. It is also a good idea to check the sshd configuration to make sure that it allows to use public key authorization when available.

At this point, readers might be thinking, \"What\'s the point, I just replaced one password with another?!\" Relax, the next section will show exactly how we can use this to only enter the passphrase once and re-use the (decrypted) key for multiple logins.

## [Making public key authentication convenient]

### [Typical key management with ssh-agent]

The next step is to decrypt the private key(s) once, and gain the ability to ssh freely, without any passwords. That is exactly what the program [ssh-agent] is for.

[ssh-agent] is usually started at the beginning of the X session, or from a shell startup script like [\~/.bash_profile]. It works by creating a UNIX socket, and registering the appropriate environment variables so that all subsequent applications can take advantage of its services by connecting to that socket. Clearly, it only makes sense to start it in the parent process of an X session to use the set of decrypted private keys in all subsequent X applications.

`user `[`$`]`` eval `ssh-agent` ``

** Note**\
This [ssh-agent] will keep keys decrypted until it is killed. To set a lifetime for the keys, use the `-t` argument as described in [man ssh-agent].

When running [ssh-agent], it should output the PID of the running ssh-agent, and also set a few environment variables, namely `SSH_AUTH_SOCK` and `SSH_AGENT_PID`. It should also automatically add [\~/.ssh/id_rsa] to its collection and ask the user for the corresponding passphrase. If other private keys exist which need to be added to the running ssh-agent, use the [ssh-add] command:

`user `[`$`]`ssh-add somekeyfile`

Now for the magic. With the decrypted private key ready, ssh into a (public key configured) server without entering any passwords:

`user `[`$`]`ssh server`

In order to shut down ssh-agent (and as such require entry of the passphrase again later):

`user `[`$`]`ssh-agent -k`

** Note**\
It is possible to have multiple [ssh-agent] processes running, especially when configuring it initially took some effort and trials. These processes can be killed like any other process by running [killall ssh-agent].

To get even more convenience from ssh-agent, proceed to the next section on using keychain. Be sure to kill the running ssh-agent as keychain will handle the [ssh-agent] sessions itself.

### [Squeezing the last drop of convenience out of ssh-agent]

Keychain will allow to reuse an [ssh-agent] between logins, and optionally prompt for passphrases each time the user logs in. Let\'s emerge it first:

`root `[`#`]`emerge --ask net-misc/keychain`

Assuming that was successful, [keychain] can now be used.

Add the following to the shell initialization file ([\~/.bash_profile], [\~/.zshrc], or similar) to enable it:

[FILE] **`~/.bash_profile`Enabling Keychain in Bash**

    keychain ~/.ssh/id_rsa
    . ~/.keychain/$-sh
    . ~/.keychain/$-sh-gpg

[FILE] **`~/.zshrc`Enabling Keychain in zsh**

    keychain ~/.ssh/id_rsa
    . ~/.keychain/$-sh
    . ~/.keychain/$-sh-gpg

** Tip**\
More keys can be appended to the command line as desired. Also, to have it ask for passphrases each time a shell is spawned, add the `--clear` option.

** Note**\
When not using Bash or zsh, check the **EXAMPLES** section of [man keychain] for examples of use in other shells. The idea is to get those commands to run each time a shell is used.

Now test it. First make sure the [ssh-agent] processes from the previous section are killed, then start up a new shell, usually by just logging in, or spawning a new terminal. It should prompt for the password for each key specified on the command line.

All shells opened after that point should reuse the [ssh-agent], allowing to use passwordless SSH connections over and over.

### [Using keychain with Plasma 5]

Plasma 5 users, instead of using [\~/.bash_profile], can let Plasma manage ssh-agent for them. In order to do so, edit [/etc/xdg/plasma-workspace/env/10-agent-startup.sh], which is read during Plasma\'s startup, and [/etc/xdg/plasma-workspace/shutdown/10-agent-shutdown.sh], which is executed during its shutdown.

Here is how one could edit those files:

[FILE] **`/etc/xdg/plasma-workspace/env/10-agent-startup.sh`Editing for Plasma 5**

    SSH_AGENT=true

[FILE] **`/etc/xdg/plasma-workspace/shutdown/10-agent-shutdown.sh`Editing for Plasma 5**

    if [ -n "$" ]; then
      eval "$(ssh-agent -k)"
    fi

Now, all that has to be done is launch a terminal of choice, like [[[kde-apps/konsole]](https://packages.gentoo.org/packages/kde-apps/konsole)[]], and load the right set of keys to use. For example:

`user `[`$`]`keychain ~/.ssh/id_rsa`

The keys will be remembered until the end of the Plasma session (or until the [ssh-agent] process is killed manually).

#### [][Alternatively use KWallet with kde-plasma/ksshaskpass under Plasma 5]

You can also have Plasma automatically ask you for your passphrase upon desktop login. Emerge kde-plasma/ksshaskpass, which will set up an environment variable to use the ksshaskpass application whenever ssh-add is run outside of a terminal. Then create a script as follows, and install it via the Plasma -\> System Settings -\> Startup and Shutdown -\> Autostart.

[FILE] **`~/ssh.sh`Create ssh.sh script**

    #!/bin/sh
    ssh-add < /dev/null

** Note**\
Recent versions of plasma seem to require autostart scripts to have user-only permissions. You may need to `chmod 700 ssh.sh` before adding the script via the Autostart GUI

## [Concluding remarks]

### [Security considerations]

Of course, the use of ssh-agent may add a bit of insecurity to the system. If another user would gain access to a running shell, he could login to all of the servers without passwords. As a result, it is a risk to the servers, and users should be sure to consult the local security policy (if any). Be sure to take the appropriate measures to ensure the security of all sessions.

### [Troubleshooting]

Most of this should work pretty well, but if problems do come up, then the following items might be of assistance.

-   If connecting without [ssh-agent] does not seem to work, consider using ssh with the `-vvv` options to find out what\'s happening. Sometimes the server is not configured to use public key authentication, sometimes it is configured to ask for local passwords anyway! If that is the case, try using the `-o` option with [ssh], or change the server\'s [sshd_config].
-   If connecting with [ssh-agent] or [keychain] does not seem to work, then it may be that the current shell does not understand the commands used. Consult the man pages for ssh-agent and keychain for details on working with other shells.

## [See also]

-   [SSH](https://wiki.gentoo.org/wiki/SSH "SSH") --- the ubiquitous tool for logging into and working on remote machines securely.

## [External resources]

-   [The official Keychain project page](http://www.funtoo.org/Keychain) at Funtoo.org.
-   [IBM developerWorks article series](http://www.funtoo.org/OpenSSH_Key_Management,_Part_1) introducing the concepts behind Keychain.

\

Authorship information[]

This page is based on a document formerly found on [gentoo.org](https://www.gentoo.org/).\
The following people contributed to the original document: **Eric Brown, Marcelo Goes, **\
\
*[Editors: please do **not** add yourself here. Contributions are recorded on each article\'s associated history page, this list is only present to preserve authorship information, as wiki history does not allow for any external attribution.]*