**Resources**

[[]][Home](https://nodejs.org/en)

[[]][Official documentation](https://nodejs.org/en/docs)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Node.js "wikipedia:Node.js")

[[]][GitHub](https://github.com/nodejs/node)

[[]][[#node.js](ircs://irc.libera.chat/#node.js)] ([[webchat](https://web.libera.chat/#node.js)])

[[]][Blog](https://nodejs.org/en/blog)

**Node.js** is a cross platform, open source, JavaScript server environment.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [npm]](#npm)
-   [[2] [Standalone Node.js server]](#Standalone_Node.js_server)
    -   [[2.1] [SELinux policy]](#SELinux_policy)
        -   [[2.1.1] [Policy installation]](#Policy_installation)
        -   [[2.1.2] [Policy usage]](#Policy_usage)
        -   [[2.1.3] [Policy removal]](#Policy_removal)
    -   [[2.2] [Port redirection]](#Port_redirection)
        -   [[2.2.1] [iptables]](#iptables)
        -   [[2.2.2] [nftables]](#nftables)
    -   [[2.3] [HTTPS]](#HTTPS)
        -   [[2.3.1] [Certificate issuance (Let\'s Encrypt)]](#Certificate_issuance_.28Let.27s_Encrypt.29)
        -   [[2.3.2] [Certificate usage]](#Certificate_usage)
    -   [[2.4] [Node.js as a reverse proxy for Forgejo\\Gitea (or anything else)]](#Node.js_as_a_reverse_proxy_for_Forgejo.5CGitea_.28or_anything_else.29)
-   [[3] [Web application daemons with nginx and monit]](#Web_application_daemons_with_nginx_and_monit)
    -   [[3.1] [Packages]](#Packages)
    -   [[3.2] [Configure Monit]](#Configure_Monit)
    -   [[3.3] [Configure Nginx]](#Configure_Nginx)
-   [[4] [Web application with openrc runscript]](#Web_application_with_openrc_runscript)
-   [[5] [References]](#References)

## [Installation]

### [USE flags]

### [USE flags for] [net-libs/nodejs](https://packages.gentoo.org/packages/net-libs/nodejs) [[]] [A JavaScript runtime built on Chrome\'s V8 JavaScript engine]

  ------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+icu`](https://packages.gentoo.org/useflags/+icu)                 Enable ICU (Internationalization Components for Unicode) support, using dev-libs/icu
  [`+inspector`](https://packages.gentoo.org/useflags/+inspector)     Enable V8 inspector
  [`+npm`](https://packages.gentoo.org/useflags/+npm)                 Enable NPM package manager
  [`+snapshot`](https://packages.gentoo.org/useflags/+snapshot)       Enable snapshot creation for faster startup
  [`+ssl`](https://packages.gentoo.org/useflags/+ssl)                 Add support for SSL/TLS connections (Secure Socket Layer / Transport Layer Security)
  [`+system-icu`](https://packages.gentoo.org/useflags/+system-icu)   Use system dev-libs/icu instead of the bundled version
  [`+system-ssl`](https://packages.gentoo.org/useflags/+system-ssl)   Use system OpenSSL instead of the bundled one
  [`corepack`](https://packages.gentoo.org/useflags/corepack)         Enable the experimental corepack package management tool
  [`debug`](https://packages.gentoo.org/useflags/debug)               Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`doc`](https://packages.gentoo.org/useflags/doc)                   Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`lto`](https://packages.gentoo.org/useflags/lto)                   Enable Link-Time Optimization (LTO) to optimize the build
  [`pax-kernel`](https://packages.gentoo.org/useflags/pax-kernel)     Enable building under a PaX enabled kernel
  [`test`](https://packages.gentoo.org/useflags/test)                 Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  ------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-05 17:49] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [npm]

Node.js has a [USE flag](https://wiki.gentoo.org/wiki/USE_flag "USE flag") to include npm, the Node.js package manager. [npm] is necessary to install a Node.js application\'s dependencies, which are defined in a file named `package.json`. The USE can be disabled if [npm] is not necessary locally, or prefer to only install an alternative, for example, [[[sys-apps/yarn]](https://packages.gentoo.org/packages/sys-apps/yarn)[]].

[npm] and [[[sys-apps/yarn]](https://packages.gentoo.org/packages/sys-apps/yarn)[]] are what\'s known as [application-level package managers](https://wiki.gentoo.org/wiki/Application_level_package_management "Application level package management"). They can install packages in one of two modes:

-   Local (the default). Packages are installed in the working directory of the Node.js project being worked on. This is the generally preferred way of working with Node.js projects and dependencies.
-   Global (enabled by the `--global` option). Packages are installed in a system-wide location and available for all projects and from the command line outside of a Node.js project.

** Warning**\
By default, `npm --global` will require root privileges, and install packages into system directories managed by [Portage](https://wiki.gentoo.org/wiki/Portage "Portage"). As discussed in [Application level package management](https://wiki.gentoo.org/wiki/Application_level_package_management "Application level package management"), this **should not be done**.

As a workaround, the [environment variable](https://wiki.gentoo.org/index.php?title=Environment_variable&action=edit&redlink=1 "Environment variable (page does not exist)") `NPM_CONFIG_PREFIX` can be used to override to install \"global\" packages in the user\'s home directory:

[FILE] **`~/.config/bash/bashrc`**

    export NPM_CONFIG_PREFIX=$HOME/.local/

See also [https://docs.npmjs.com/resolving-eacces-permissions-errors-when-installing-packages-globally#manually-change-npms-default-directory](https://docs.npmjs.com/resolving-eacces-permissions-errors-when-installing-packages-globally#manually-change-npms-default-directory)

## [Standalone Node.js server]

** Warning**\
Node.js and Express.js suggest to run Node.js behind a **reverse proxy** to mitigate **DoS attacks** and improve **performance**. ^[\[1\]](#cite_note-1)[\[2\]](#cite_note-2)[\[3\]](#cite_note-3)^ This section goes against these recommendations and even includes an example of using Node.js itself as a reverse proxy. Not following these recommendations is allowed if the server will not be public. With caution, the methods provided here can be used for small homelab projects. It is also important to understand that reverse proxies are not a panacea. They may contain vulnerabilities that could lead to the execution of arbitrary code (e.g. [[[bug #CVE-2021-23017]](https://bugs.gentoo.org/show_bug.cgi?id=CVE-2021-23017)[]]) or root privilege escalation (e.g. [[[bug #CVE-2016-1247]](https://bugs.gentoo.org/show_bug.cgi?id=CVE-2016-1247)[]]). Not using reverse proxies limits the attack vector to Node.js only.

Node.js can be run as a standalone HTTP server. It does not require root privileges and can be accessed from the Internet, for example on port 3000.

To launch the [official example](https://nodejs.org/en/learn/getting-started/introduction-to-nodejs), the `hostname` (a variable in the example) must be set to a public IPv6 or IPv4 address (`localhost` will not work). The modified example can be executed from the user space as following:

`user `[`$`]`node modified-downloaded-example.js`

The only problem is the inability to connect to [well-known ports](https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers#Well-known_ports "wikipedia:List of TCP and UDP port numbers") (e.g. 80) from unprivileged user space. But this problem can be solved with [port redirection](#Port_redirection).

### [SELinux policy]

** Warning**\
The policy provided in this section is not official. Review the policy before using it.

As of December 2, 2024, the Node.js package does not come with a [SELinux](https://wiki.gentoo.org/wiki/SELinux "SELinux") policy, so creating a custom policy is required. The following custom policy assumes that Node.js will be executed from unprivileged user space. The policy was tested with Nodejs v. 22.7.0 on the `default/linux/arm64/23.0/musl/hardened/selinux` profile.

[FILE] **`nodejs.te`**

    # License: 0BSD

    policy_module(nodejs, 1.0)

    gen_require(`
      attribute file_type, non_security_file_type, non_auth_file_type;
      role user_r;
      type user_t;
      type node_t;
      type cert_t;
      type sshd_t;
      type user_devpts_t;
      type ntop_port_t;
      type unreserved_port_t;
    ')

    ##
    # Type declarations.
    #
    type nodejs_t;
    type nodejs_exec_t;
    type nodejs_www_t;
    domain_type(nodejs_t)
    domain_entry_file(nodejs_t, nodejs_exec_t)
    typeattribute nodejs_www_t file_type, non_security_file_type, non_auth_file_type;

    ##
    # Domain transition (user_t -> nodejs_t).
    #
    domtrans_pattern(user_t, nodejs_exec_t, nodejs_t)
    role user_r types nodejs_t;
    allow user_t nodejs_exec_t:file mmap_exec_file_perms;

    ##
    # Static files.
    #
    allow nodejs_t nodejs_www_t:file read_file_perms;
    allow nodejs_t nodejs_www_t:dir search_dir_perms;

    ##
    # Node.js requirements.
    #
    allow nodejs_t self:process ;
    allow nodejs_t self:fifo_file rw_file_perms;
    allow nodejs_t self:tcp_socket server_stream_socket_perms;
    allow nodejs_t node_t:tcp_socket node_bind;
    allow nodejs_t ntop_port_t:tcp_socket name_bind;
    # OpenSSL
    allow nodejs_t cert_t:dir search;
    allow nodejs_t cert_t:file read_file_perms;
    # PTY
    allow nodejs_t sshd_t:fd use;
    allow nodejs_t user_devpts_t:chr_file rw_inherited_file_perms;

    ##
    # Optional
    #
    allow nodejs_t unreserved_port_t:tcp_socket name_bind;

** Important**\
Delete the following lines if there are no plans to use Node.js on ports other than `3000`:

`type unreserved_port_t;` and

`allow nodejs_t unreserved_port_t:tcp_socket name_bind;`

[FILE] **`nodejs.fc`**

    /usr/bin/node -- gen_context(system_u:object_r:nodejs_exec_t)

#### [Policy installation]

To compile and install the policy module, run the commands:

`root `[`#`]`make -f /usr/share/selinux/strict/include/Makefile nodejs.pp`

`root `[`#`]`semodule --install nodejs.pp`

#### [Policy usage]

The policy requires that all files that should be accessible to Node.js be labeled as `nodejs_www_t`.

For example, if the project is stored in the [/opt/website] directory, the following command can be used:

`root `[`#`]`chcon --recursive --type nodejs_www_t /opt/website`

#### [Policy removal]

To remove the policy, run the command:

`root `[`#`]`semodule --remove nodejs`

### [Port redirection]

This section describes a way to redirect ports using the legacy [iptables](https://wiki.gentoo.org/wiki/Iptables "Iptables") approach or the modern [nftables](https://wiki.gentoo.org/wiki/Nftables "Nftables") approach. Choose one.

#### [iptables]

The redirection requires the following option to be enabled in the kernel:

[KERNEL] **Enable redirections**

    [*] Networking support  --->
      --- Networking support
        Networking options  --->
          [*] Network packet filtering framework (Netfilter)  --->
            --- Network packet filtering framework (Netfilter)
              Core Netfilter Configuration  --->
                [*] REDIRECT target support

** Important**\
The examples below assume that the server is running on a public IPv6 address. For an IPv4 address use `iptables` instead of `ip6tables`, the syntax is the same. IPv4 and IPv6 have separate NAT tables.

Assuming the Node.js server is running on port 3000, run the following command to redirect port 80 to 3000:

`root `[`#`]`ip6tables --table nat --append PREROUTING --protocol tcp --dport 80 --jump REDIRECT --to-port 3000`

The server should be immediately accessible via port 80.

** Note**\
The created rule will disappear after a reboot.

To see the modified NAT table, run the command:

`root `[`#`]`ip6tables --table nat --list`

    Chain PREROUTING (policy ACCEPT)
    target     prot opt source               destination
    REDIRECT   tcp  --  anywhere             anywhere             tcp dpt:http redir ports 3000

    Chain INPUT (policy ACCEPT)
    target     prot opt source               destination

    Chain OUTPUT (policy ACCEPT)
    target     prot opt source               destination

    Chain POSTROUTING (policy ACCEPT)
    target     prot opt source               destination

To remove the added rule (to change the port or because of a mistake), run the command:

** Important**\
Make sure the rule is the first (`1`) in the `PREROUTING` chain, otherwise specify the correct number.

`root `[`#`]`ip6tables --table nat --delete PREROUTING 1`

#### [nftables]

The redirection requires the following options to be enabled in the kernel:

[KERNEL] **Enable redirections**

    [*] Networking support  --->
      --- Networking support
        Networking options  --->
          [*] Network packet filtering framework (Netfilter)  --->
            --- Network packet filtering framework (Netfilter)
              Core Netfilter Configuration  --->
                [*] Netfilter nf_tables support
                [*]   Netfilter nf_tables redirect support
                [*]   Netfilter nf_tables nat module

[KERNEL] **IPv6**

    [*] Networking support  --->
      --- Networking support
        Networking options  --->
          [*] Network packet filtering framework (Netfilter)  --->
            --- Network packet filtering framework (Netfilter)
              IPv6: Netfilter Configuration  --->
                [*] IPv6 nf_tables support

[KERNEL] **IPv4**

    [*] Networking support  --->
      --- Networking support
        Networking options  --->
          [*] Network packet filtering framework (Netfilter)  --->
            --- Network packet filtering framework (Netfilter)
              IP: Netfilter Configuration  --->
                [*] IPv4 nf_tables support

** Important**\
The examples below assume that the server is running on a public IPv6 address. For an IPv4 address use `inet` or `ip` instead of `ip6`

Create the NAT table and chain:

`root `[`#`]`nft add table ip6 nat`

`root `[`#`]`nft add chain ip6 nat prerouting ''`

Redirect port `80` to port `3000`:

`root `[`#`]`nft add rule ip6 nat prerouting tcp dport 80 counter redirect to 3000`

The server should be immediately accessible via port 80.

** Note**\
The created rule will disappear after a reboot.

To see the prerouting chain, run the command:

`root `[`#`]`nft --handle list chain ip6 nat prerouting`

    table ip6 nat
    }

To remove the added rule (to change the port or because of a mistake), run the command:

** Important**\
Make sure the rule is matched as `# handle 2` in the above output, otherwise specify the correct number.

`root `[`#`]`nft delete rule ip6 nat prerouting handle 2`

### [HTTPS]

This section relies on [Express.js](https://expressjs.com/en/starter/installing.html) because it provides a simple way to host static files that appear dynamically. All paths match the [acme-tiny configuration guide](https://wiki.gentoo.org/wiki/Let%27s_Encrypt#acme-tiny "Let's Encrypt"), but there are no strict requirements, the files can be anywhere.

#### [][Certificate issuance (Let\'s Encrypt)]

First, it is necessary to create and run a server script that will host the Let\'s Encrypt token for the [HTTP-01 challenge](https://letsencrypt.org/docs/challenge-types/#http-01-challenge):

[FILE] **`http-server.js`**

    const express = require('express');

    const PORT = 3000;
    const ACME_CHALLENGE_PATH = '/var/www/localhost/acme-challenge';
    const app = express();

    app.use('/.well-known/acme-challenge', express.static(ACME_CHALLENGE_PATH));

    app.listen(PORT);

Then redirect port `80` to port `3000` as described [above](#Port_redirection). Install acme-tiny as described [here](https://wiki.gentoo.org/wiki/Let%27s_Encrypt#acme-tiny_.28optional.29 "Let's Encrypt") and issue the certificate as described [here](https://wiki.gentoo.org/wiki/Let%27s_Encrypt#acme-tiny "Let's Encrypt").

#### [Certificate usage]

Once the certificate has been issued, the server script needs to be replaced with this one:

[FILE] **`https-server.js`**

    const fs = require('node:fs');
    const https = require('node:https');
    const express = require('express');

    const PORT = 3000;
    const CERTIFICATE_PATH = '/var/lib/letsencrypt/chained.pem';
    const PRIVATE_KEY_PATH = '/var/lib/letsencrypt/domain.key';
    const app = express();

    const options = ;

    https.createServer(options, app).listen(PORT);

Redirect port `443` to `3000` as described [above](#Port_redirection). The connection should now be encrypted. The above script doesn\'t actually require Express.js anymore, but it\'s left as an example, an example of pure Node.js can be found [here](https://nodejs.org/api/https.html#httpscreateserveroptions-requestlistener). The ACME challenge is not required either, even for renewals.

### [][Node.js as a reverse proxy for Forgejo\\Gitea (or anything else)]

The simplest way to set up a reverse proxy is to use [Express.js](https://expressjs.com/en/starter/installing.html) with [express-http-proxy](https://github.com/villadora/express-http-proxy).

The following example shows a way to redirect all requests coming to `http://<DOMAIN>/projects` to [Forgejo](https://wiki.gentoo.org/wiki/Forgejo "Forgejo") (or [Gitea](https://wiki.gentoo.org/wiki/Gitea "Gitea")). The example assumes that port `80` is redirected to port `3000` as described [above](#Port_redirection).

The minimal Forgejo [configuration](https://forgejo.org/docs/latest/admin/config-cheat-sheet/):

[FILE] **`<Forgejo\Gitea root directory>/custom/conf/app.ini`**

    [server]
    ROOT_URL = http://<DOMAIN GOES HERE>/projects/
    HTTP_PORT = 3001

** Note**\
Replace `http://` with `https://` if HTTPS is used.

The minimal HTTP server:

[FILE] **`server.js`**

    const express = require('express');
    const proxy = require('express-http-proxy');

    const PORT = 3000;
    const app = express();

    app.use('/projects', proxy('localhost:3001'));

    app.listen(PORT);

To use HTTPS, just inject the following lines in the script provided [here](#Certificate_usage):

[CODE]

    const proxy = require('express-http-proxy');
    app.use('/projects', proxy('localhost:3001'));

## [Web application daemons with nginx and monit]

This section will walk through installing Node.js behind nginx and using Monit to keep Node instances alive. Since Node.js is a single-process application, the goal is to launch multiple instances of the application and load balance using nginx.

### [Packages]

Use [[[app-admin/monit]](https://packages.gentoo.org/packages/app-admin/monit)[]] for spawning Node.js servers.

`root `[`#`]`emerge --ask monit nginx nodejs`

### [Configure Monit]

[FILE] **`/etc/monit.d/nodejs-server`Auto restart NodeJS App**

    check process nodejs-server with pidfile /run/nodejs-server.pid
        start program = "/bin/bash -c 'rc-service nodejs-server start'"
        stop program  = "/bin/bash -c 'rc-service nodejs-server stop'"

### [Configure Nginx]

[FILE] **`/etc/nginx/nginx.conf`Nginx Config**

    http

        server
        }
    }

## [Web application with openrc runscript]

[FILE] **`/etc/init.d/nodejs-server`Sample init.d file for a Node.js daemon**

    #!/sbin/openrc-run

    user="nobody"
    group="nobody"
    command="/usr/bin/node"
    directory="/opt/$"
    command_args="httpd.js"
    command_user="$:$"
    command_background="yes"
    pidfile="/run/$.pid"
    output_log="/var/log/$.log"
    error_log="$"

    depend()

## [References]

1.  [[[↑](#cite_ref-1)] [[https://nodejs.org/en/learn/getting-started/security-best-practices](https://nodejs.org/en/learn/getting-started/security-best-practices)]]
2.  [[[↑](#cite_ref-2)] [[https://expressjs.com/en/advanced/best-practice-security.html](https://expressjs.com/en/advanced/best-practice-security.html)]]
3.  [[[↑](#cite_ref-3)] [[https://expressjs.com/en/advanced/best-practice-performance.html](https://expressjs.com/en/advanced/best-practice-performance.html)]]