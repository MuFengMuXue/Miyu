This page contains [[changes](https://wiki.gentoo.org/index.php?title=Puppet&oldid=1045832&diff=1347887)] which are not marked for translation.

Other languages:

-   [English]
-   [Türkçe](https://wiki.gentoo.org/wiki/Puppet/tr "Puppet (8% translated)")
-   [français](https://wiki.gentoo.org/wiki/Puppet/fr "Puppet (24% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/Puppet/hu "Puppet (100% translated)")
-   [polski](https://wiki.gentoo.org/wiki/Puppet/pl "Puppet/pl (1% translated)")
-   [русский](https://wiki.gentoo.org/wiki/Puppet/ru "Puppet (73% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Puppet/ja "Puppet (44% translated)")
-   [한국어](https://wiki.gentoo.org/wiki/Puppet/ko "Puppet/ko (7% translated)")

** Warning**\
Perforce is [close-sourcing Puppet against the license](https://www.puppet.com/blog/open-source-puppet-updates-2025), making its future uncertain. There is an attempt to fork Puppet under [OpenVox](https://github.com/OpenVoxProject/puppet) but it has yet to gain any community adoption. Caution is advised before starting new projects with Puppet.

**Resources**

[[]][Home](https://puppetlabs.com/puppet/puppet-open-source)

[[]][Package information](https://packages.gentoo.org/packages/app-admin/puppet)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Puppet_(software) "wikipedia:Puppet (software)")

[![Ohloh Logo](/images/thumb/c/c1/Ohloh-logo.png/30px-Ohloh-logo.png)][Open Hub](https://www.openhub.net/p/puppet)

**Puppet** is a configuration management system written in [Ruby](https://wiki.gentoo.org/wiki/Ruby "Ruby"). It can be used for automating machine deployments.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration and setup]](#Configuration_and_setup)
    -   [[2.1] [Server (Puppetmaster) setup]](#Server_.28Puppetmaster.29_setup)
        -   [[2.1.1] [Setting up the file server]](#Setting_up_the_file_server)
        -   [[2.1.2] [Starting the puppetmaster daemon]](#Starting_the_puppetmaster_daemon)
        -   [[2.1.3] [A simple manifest]](#A_simple_manifest)
    -   [[2.2] [Client configuration]](#Client_configuration)
        -   [[2.2.1] [OpenRC]](#OpenRC)
        -   [[2.2.2] [systemd]](#systemd)
-   [[3] [Other topics]](#Other_topics)
    -   [[3.1] [Manually generating certificates]](#Manually_generating_certificates)
    -   [[3.2] [Refreshing agent certificates]](#Refreshing_agent_certificates)
    -   [[3.3] [Managing slots with puppet]](#Managing_slots_with_puppet)
-   [[4] [See also]](#See_also)
-   [[5] [External resources]](#External_resources)

## [Installation]

Currently, there is no distinction between server and client, so the basic installation procedure is the same for both.

### [USE flags]

### [USE flags for] [app-admin/puppet](https://packages.gentoo.org/packages/app-admin/puppet) [[]] [A system automation and configuration management software]

  ----------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`augeas`](https://packages.gentoo.org/useflags/augeas)           Enable augeas support
  [`diff`](https://packages.gentoo.org/useflags/diff)               Enable diff support
  [`doc`](https://packages.gentoo.org/useflags/doc)                 Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`emacs`](https://packages.gentoo.org/useflags/emacs)             Add support for GNU Emacs
  [`hiera`](https://packages.gentoo.org/useflags/hiera)             Enable hiera support
  [`ldap`](https://packages.gentoo.org/useflags/ldap)               Add LDAP support (Lightweight Directory Access Protocol)
  [`rrdtool`](https://packages.gentoo.org/useflags/rrdtool)         Enable rrdtool support
  [`selinux`](https://packages.gentoo.org/useflags/selinux)         !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`shadow`](https://packages.gentoo.org/useflags/shadow)           Enable shadow support
  [`sqlite`](https://packages.gentoo.org/useflags/sqlite)           Add support for sqlite - embedded sql database
  [`test`](https://packages.gentoo.org/useflags/test)               Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`vim-syntax`](https://packages.gentoo.org/useflags/vim-syntax)   Pulls in related vim syntax scripts
  ----------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-04-06 03:53] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Install [[[app-admin/puppet]](https://packages.gentoo.org/packages/app-admin/puppet)[]]:

`root `[`#`]`emerge --ask app-admin/puppet`

## [Configuration and setup]

Puppet is mainly configured through [/etc/puppet/puppet.conf] in an INI-style format. Comments are marked with a hash sign (`#`).

The configuration file is separated into several sections, or blocks:

-   `[main]` contains settings that act as a default for all parts of Puppet, unless overridden by settings in any of the following sections:
    -   `[master]` is used for settings applying to the Puppetmaster ([puppet master]), or CA tool ([puppet cert])
    -   `[agent]` is used for settings applying to the Puppet agent ([puppet agent])

A more in-depth explanation, as well as a list of further blocks used is available in the [official Puppet documentation](http://docs.puppetlabs.com/guides/configuring.html). Also, there is a [list of all configuration](http://docs.puppetlabs.com/references/stable/configuration.html) options, some of which of course make only sense when applied to either server or client.

### [][Server (Puppetmaster) setup]

The default configuration put by the ebuild into [puppet.conf] can be used as-is. For Puppet 2.7.3, the server-related parts look like this:

[FILE] **`/etc/puppet/puppet.conf`Server-related default configuration**

    [main]
        # The Puppet log directory.
        # The default value is '$vardir/log'.
        logdir = /var/log/puppet

        # Where Puppet PID files are kept.
        # The default value is '$vardir/run'.
        rundir = /var/run/puppet

        # Where SSL certificates are kept.
        # The default value is '$confdir/ssl'.
        ssldir = $vardir/ssl

#### [Setting up the file server]

To be able to send files to the clients, the file server has to be configured. This is done in [/etc/puppet/fileserver.conf]. By default, there are no files being served.

[FILE] **`/etc/puppet/fileserver.conf`Setting the `files` share**

    [files]
        path /var/lib/puppet/files
        allow 192.168.0.0/24

The snippet above sets up a share called `files` (remember this identifier, as it will need to be referenced later), looking for files in [/var/lib/puppet/files] and only available for hosts with an IP from the 192.168.0.0/24 network. Any of the IP addresses, CIDR notation, and host names (including wildcards like `*.domain.invalid`) can be used here. The `deny` command can be used to explicitly deny access to certain hosts or IP ranges.

#### [Starting the puppetmaster daemon]

** Note**\
It is recommended that the Puppetmaster is reachable from the clients using the host name `puppet`. However, the name can be overridden, which of course causes configuration effort.

** Important**\
At this point, the host name as seen from the clients should be the same as the output of [hostname -f]. To achieve this, the [/etc/hosts] file might have to be adjusted, or a new certificate can be created manually as [explained below](#Manually_generating_certificates).

With the basic configuration as well as an initial file server configuration, we can start the Puppetmaster daemon using its OpenRC init script:

`root `[`#`]`rc-service puppetmaster start`

During the first start, Puppet generates an SSL certificate for the Puppetmaster host and places it into the directory configured through the `ssldir` variable, as configured above.

It listens on Port `8140/TCP`, make sure that there are no firewall rules obstructing access from the clients.

#### [A simple manifest]

Manifests, in Puppet\'s terminology, are the files in which the client configuration is specified. The documentation contains a [comprehensive guide](http://docs.puppetlabs.com/guides/language_guide.html) about the manifest markup language.

As a simple example, let\'s create a *message of the day* (motd) file on the client. On the puppetmaster, create a file inside the `files` share created earlier:

[FILE] **`/var/lib/puppet/files/motd`MOTD file on the server**

    Welcome to this Puppet-managed machine!

Then, we have to create the main manifest file in the [manifests] directory. It is called `site.pp`:

[FILE] **`/etc/puppet/manifests/site.pp`Main manifest on the server**

    node default
    }

The `default` *node* (the name for a client) definition is used in case there is no specific `node` statement for the host. We use a `file` resource and want the [/etc/motd] file on our clients to contain the same thing as the `motd` file in the `files` share on the host `puppet`. If the puppetmaster is only reachable using another host name, adapt the `source` URI accordingly.

### [Client configuration]

** Important**\
The client **must** have the **same major and minor version** as the Puppetmaster. Using a 2.7.1 Puppetmaster with 2.7.2 clients is fine, but using 2.6 for the server and 2.7 for clients can cause unexpected issues at any time.

** Note**\
If the puppetmaster is not reachable via `puppet`, set `server=<the hostname>` to the actual host name in [/etc/puppet/puppet.conf] in the `[main]` section.

During the first execution of the Puppet agent, wait for the certificate to be signed by the puppetmaster. To request a certificate, and execute the first configuration run, execute:

`root@client #``puppet agent --test --waitforcert 60`

    info: Creating a new certificate request for client
    info: Creating a new SSL key at /var/lib/puppet/ssl/private_keys/client.pem
    notice: Did not receive certificate

Before the client can connect, authorize the certificate request on the server. The client should appear in the list of nodes requesting a certificate:

`root@server #``puppet cert --list `

    client

Now, we grant the request:

`root@server #``puppet cert --sign client `

The client will check every 60 seconds whether its certificate has already been issued. After that, it continues with the first configuration run:

    info: Caching catalog for client
    info: Applying configuration version '1317317379'
    notice: /Stage[main]//Node[default]/File[/etc/motd]/ensure: defined content as '30ed97991ad6f591b9995ad749b20b00'
    notice: Finished catalog run in 0.05 seconds

When this message pops up, all went well. Now check the contents of the [/etc/motd] file on the client:

`user@client $``cat /etc/motd `

    Welcome to this Puppet-managed machine!

#### [OpenRC]

Start the puppet agent as a daemon and have it launch on boot:

`root@client #``rc-service puppet start `

`root@client #``rc-update add puppet default `

#### [systemd]

Conversely, when running systemd:

`root@client #``systemctl start puppet `

`root@client #``systemctl enable puppet `

## [Other topics]

### [Manually generating certificates]

To manually generate a certificate, use the [puppet cert] utility. It will place all generated certificates into the `ssldir` defined directory as set in the puppet configuration and will sign them with the key of the local Puppet Certificate Authority (CA).

An easy case is the generation of a certificate with **only one Common Name:**

`root `[`#`]`puppet cert --generate host1`

If the certificate has to be valid for **multiple host names**, use the `--certdnsnames` parameter and separate the additional host names with a colon:

`root `[`#`]`puppet cert --generate --certdnsnames puppet:puppet.domain.invalid host1.domain.invalid`

This example will generate a certificate valid for the three listed host names.

### [Refreshing agent certificates]

This is the process used to manually refresh agent certificates.

1.  (on master)

    :::: cmd-box


    `root `[`#`]`puppet cert clean $ `


    ::::
2.  (on agent)

    :::: cmd-box


    `root `[`#`]`rm /etc/puppet/ssl//$.pem`


    ::::

    -   This will cause the Puppet agent to regenerate the CSR with the existing SSL key.
    -   The old certificate is no longer valid, as it was nuked on the master.
    -   When one of the above steps is forgotten, an error will pop up about the certificate mis-matching between agent and master.
    -   To replace the SSL keys (optional):

        :::: cmd-box


        `root `[`#`]`rm /etc/puppet/ssl/_keys/$.pem`


        ::::
3.  (on agent)

    :::: cmd-box


    `root `[`#`]`puppet agent --onetime --no-daemonize --verbose --test --waitforcert 30`


    ::::

    -   When using auto-signing, no further steps are needed.
4.  (on master)

    :::: cmd-box


    `root `[`#`]`puppet cert list $ `


    ::::
5.  Verify that the fingerprint listed in the previous two outputs matches
6.  (on master)

    :::: cmd-box


    `root `[`#`]`puppet cert sign $ `


    ::::
7.  (on agent)

    :::: cmd-box


    `root `[`#`]`puppet agent --onetime --no-daemonize --verbose --test`


    ::::

### [Managing slots with puppet]

While the default portage provider in puppet does support slots there are puppet modules available which also have this functionality.

For instance, with [[[app-admin/puppet]](https://packages.gentoo.org/packages/app-admin/puppet)[]] version 4.6.0 and higher, and/or [[[app-admin/puppet-agent]](https://packages.gentoo.org/packages/app-admin/puppet-agent)[]], the slot functionality is supported like to:

[CODE] **Defining an absent slotted package**

    package

Additional modules are:

-   [puppet-portage](https://github.com/gentoo/puppet-portage)
-   [PortageGT](https://github.com/whatbox/PortageGT)

## [See also]

-   [Puppet module for Gentoo](https://wiki.gentoo.org/wiki/Puppet_module_for_Gentoo "Puppet module for Gentoo")

## [External resources]

-   [Upstream website](http://puppetlabs.com/)
-   [Puppet Wiki](http://projects.puppetlabs.com/projects/puppet/wiki)