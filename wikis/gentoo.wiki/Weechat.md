**Resources**

[[]][Home](https://weechat.org/)

[[]][Official documentation](https://weechat.org/doc)

[[]][Package information](https://packages.gentoo.org/packages/net-irc/weechat)

[[]][Wikipedia](https://en.wikipedia.org/wiki/WeeChat "wikipedia:WeeChat")

[[]][GitHub](https://github.com/weechat/weechat)

[[]][[#weechat](ircs://irc.libera.chat/#weechat)] ([[webchat](https://web.libera.chat/#weechat)])

**WeeChat** is a light, extensible, actively maintained, well documented, highly featured text-mode [IRC](https://wiki.gentoo.org/wiki/IRC "IRC") client. WeeChat natively runs through ncurses for the text-mode interface, however for user convenience many \'remote\' interfaces (GUIs) are available to relay WeeChat data to more accessible mediums (Android phones, Web interfaces, X GUIs, and more).

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Add IRC server]](#Add_IRC_server)
    -   [[2.2] [SASL authentication]](#SASL_authentication)
    -   [[2.3] [Running a command when connecting to a server]](#Running_a_command_when_connecting_to_a_server)
    -   [[2.4] [Securing passwords]](#Securing_passwords)
    -   [[2.5] [Auto-join channels]](#Auto-join_channels)
    -   [[2.6] [Fast set]](#Fast_set)
        -   [[2.6.1] [Example usage]](#Example_usage)
    -   [[2.7] [Smart filter]](#Smart_filter)
    -   [[2.8] [Scripts]](#Scripts)
    -   [[2.9] [Plugins]](#Plugins)
    -   [[2.10] [Hardening]](#Hardening)
        -   [[2.10.1] [CTCP]](#CTCP)
        -   [[2.10.2] [Part and quit messages]](#Part_and_quit_messages)
    -   [[2.11] [Relay]](#Relay)
        -   [[2.11.1] [Adding a relay]](#Adding_a_relay)
        -   [[2.11.2] [Adding an encrypted relay]](#Adding_an_encrypted_relay)
        -   [[2.11.3] [Time-based One-Time Password (TOTP)]](#Time-based_One-Time_Password_.28TOTP.29)
        -   [[2.11.4] [Remote interfaces]](#Remote_interfaces)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Invocation]](#Invocation)
    -   [[3.2] [screen]](#screen)
    -   [[3.3] [tmux]](#tmux)
-   [[4] [Upgrades]](#Upgrades)
-   [[5] [Troubleshooting]](#Troubleshooting)
    -   [[5.1] [Mouse usage]](#Mouse_usage)
-   [[6] [Removal]](#Removal)
    -   [[6.1] [Unmerge]](#Unmerge)
    -   [[6.2] [Configuration and logs]](#Configuration_and_logs)
-   [[7] [See also]](#See_also)
-   [[8] [External resources]](#External_resources)
-   [[9] [References]](#References)

## [Installation]

### [USE flags]

### [USE flags for] [net-irc/weechat](https://packages.gentoo.org/packages/net-irc/weechat) [[]] [Portable and multi-interface IRC client]

  ----------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`+alias`](https://packages.gentoo.org/useflags/+alias)           Enable plugin for alias control
  [`+buflist`](https://packages.gentoo.org/useflags/+buflist)       Enable buflist plugin
  [`+charset`](https://packages.gentoo.org/useflags/+charset)       Enable encoding conversions
  [`+exec`](https://packages.gentoo.org/useflags/+exec)             Enable exec plugin
  [`+fifo`](https://packages.gentoo.org/useflags/+fifo)             Enable FIFO support (sh pipes)
  [`+fset`](https://packages.gentoo.org/useflags/+fset)             Enable fast set plugin
  [`+irc`](https://packages.gentoo.org/useflags/+irc)               Enable IRC protocol support
  [`+logger`](https://packages.gentoo.org/useflags/+logger)         Enable support for logging
  [`+perl`](https://packages.gentoo.org/useflags/+perl)             Add optional support/bindings for the Perl language
  [`+python`](https://packages.gentoo.org/useflags/+python)         Add optional support/bindings for the Python language
  [`+relay`](https://packages.gentoo.org/useflags/+relay)           Enable relay plugin (experimental)
  [`+scripts`](https://packages.gentoo.org/useflags/+scripts)       Build infrastructure for scripting
  [`+spell`](https://packages.gentoo.org/useflags/+spell)           Add dictionary support
  [`+trigger`](https://packages.gentoo.org/useflags/+trigger)       Enable trigger plugin
  [`+typing`](https://packages.gentoo.org/useflags/+typing)         Enable typing plugin
  [`+xfer`](https://packages.gentoo.org/useflags/+xfer)             Enable xfer plugin support
  [`+zstd`](https://packages.gentoo.org/useflags/+zstd)             Enable support for ZSTD compression
  [`doc`](https://packages.gentoo.org/useflags/doc)                 Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`enchant`](https://packages.gentoo.org/useflags/enchant)         Enable spell checker plugin via Enchant instead of GNU Aspell
  [`guile`](https://packages.gentoo.org/useflags/guile)             Add support for the guile Scheme interpreter
  [`lua`](https://packages.gentoo.org/useflags/lua)                 Enable Lua scripting support
  [`nls`](https://packages.gentoo.org/useflags/nls)                 Add Native Language Support (using gettext - GNU locale utilities)
  [`relay-api`](https://packages.gentoo.org/useflags/relay-api)     Enable json API support for the relay plugin (experimental)
  [`ruby`](https://packages.gentoo.org/useflags/ruby)               Add support/bindings for the Ruby language
  [`selinux`](https://packages.gentoo.org/useflags/selinux)         !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`tcl`](https://packages.gentoo.org/useflags/tcl)                 Add support the Tcl language
  [`test`](https://packages.gentoo.org/useflags/test)               Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`verify-sig`](https://packages.gentoo.org/useflags/verify-sig)   Verify upstream signatures on distfiles
  ----------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-01-27 08:03] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Install WeeChat:

`root `[`#`]`emerge --ask net-irc/weechat`

## [Configuration]

An *excellent* [quick start guide](https://weechat.org/files/doc/stable/weechat_quickstart.en.html) can be found on WeeChat\'s website. The official guide should be followed for the most up to date configuration instructions. Head over there and read the guide. When finished return here if necessary for further instructions.

### [Add IRC server]

To be able to chat on IRC, the client must be connected to an IRC server. For this section, the libera server network will be used as an example.

At the IRC input box, add the libera server:

`/server add libera irc.libera.chat/6697 -ssl -username=larry -ssl -ssl_verify`

if using znc^[\[1\]](#cite_note-1)^, do this:

`/server add BNC my.bouncer.net/6697 -tls -username=username/network -password=password -autoconnect`

Connect to the server:

`/connect libera`

For WeeChat 4.0 and later, use -tls^[\[2\]](#cite_note-2)^ instead of -ssl:

`/server add libera irc.libera.chat/6697 -tls -username=larry`

The option [-tls_verify] is on by default.^[\[3\]](#cite_note-3)^

### [SASL authentication]

** Note**\
By default, some passwords are hidden behind asterisks. More options can be added under \'irc.look.nicks hide password\' for different services to mask the password (ex. nickbot).

If SASL is available on the server, it is possible to use it for authentication (the user will be identified before joining channels).

Set the username for the server, substituting `larry` in the example below with the appropriate username:

`/set irc.server.libera.sasl_username "larry"`

Set the password for the server, substituting `xxxxxxxx` in the example below with the appropriate password:

`/set irc.server.libera.sasl_password "xxxxxxxx"`

### [Running a command when connecting to a server]

It is possible to run a command automatically upon connecting to server. Use the [/set irc.server.libera.command] command to set up commands to run on connection.

For example, to authenticate with nickserv on connection (necessary only when not using SASL for authentication). Substitute `xxxxxxxx` in the example below with the appropriate password:

`/set irc.server.libera.command "/msg nickserv identify xxxxxxxx"`

** Tip**\
Multiple commands command can be separated with a `;` (semi-colon).

### [Securing passwords]

It is possible to protect passwords in configuration files to keep secure from prying eyes.

The first step to protect passwords is to setup a passphrase with the [/secure passphrase] command:

`/secure passphrase <this is my secret passphrase>`

Then add a secured data with the libera password:

`/secure set libera_password xxxxxxx`

Then use `$` instead of the password in the IRC options mentioned above, for example:

`/set irc.server.libera.sasl_password "$"`

### [Auto-join channels]

To auto-join specific channels when connecting to server, configure WeeChat to automatically update the autojoin option when joining or leaving channels with the following command:

`/set irc.server_default.autojoin_dynamic on`

Todo: [ **Todo:**]

-   Make section independent of external guide

\

After making it through step 7 in the [WeeChat quick start guide](https://weechat.org/files/doc/stable/weechat_quickstart.en.html) Libera.Chat *should* be added as the server.

Custom channels can be automatically joined each time WeeChat is opened by running the following command inside the WeeChat client. For example, to add [[#gentoo](ircs://irc.libera.chat/#gentoo)] ([[webchat](https://web.libera.chat/#gentoo)]) and [[#gentoo-chat](ircs://irc.libera.chat/#gentoo-chat)] ([[webchat](https://web.libera.chat/#gentoo-chat)]) channels to the auto-join list each time [weechat] starts:

`/set irc.server.libera.autojoin "#gentoo,#gentoo-chat"`

Add or subtract more more channels to the comma separated list as desired. Everyone has their own channels interests!

### [Fast set]

The \"fast set\" plugin displays a list of options in a buffer, and helps to set WeeChat and plugin options.

#### [Example usage]

Show IRC options changed:

`/fset d:irc.*`

Show all options with \"nicklist\" in name:

`/fset nicklist`

Show how all values which contain \"red\":

`/fset =red`

Show all values which are exactly \"red\":

`/fset ==red`

### [Smart filter]

A new smart filter for IRC join/part/quit message has been added. It is disabled by default (to see all join/part/quit by default).

When a nick spoke on channel during past X minutes (where X is delay irc.look.smart_filter_delay), its join/part/quit will be displayed by default. Otherwise, if nick did not speak for a long time, all join/part/quit messages will be tagged with \"irc_smart_filter\". Define a filter on this tag to hide join/part/quit from users that are not speaking on channel, in the example below delay is set to 5 min:

`/set irc.look.smart_filter on `

`/filter add irc_smart * irc_smart_filter * `

`/set irc.look.smart_filter_delay 5 `

### [Scripts]

Todo: [ **Todo:**]

-   Provide more context of what is being done here, and maybe a lead-in on what scripts are.

\

Enable download of files from the scripts repository when the /script command is used (list of scripts and scripts themselves); the list of scripts is downloaded from the URL specified in the option script.scripts.url; WeeChat will sometimes download again the list of scripts when using the /script command, even if no script is installed:

`/set script.scripts.download_enabled on`

List collections of WeeChat scripts written by external contributors, which can be installed directly in WeeChat

`/script`

### [Plugins]

Plugins for WeeChat can be added and removed via USE flags. See the [USE flags](#USE_flags) section above for a list of available plugins.

### [Hardening]

Occasionally spammers/trolls will attempt to scrape IRC networks for any relevant information they can find exposed about the IRC connection. Those concerned about hardening can restrict WeeChat to not provide specific details concerning their use.

These options can be set by hand in the [\~.weechat/irc.conf] file.

#### [CTCP]

To block CTCP requests [set an empty string](https://weechat.org/files/doc/stable/weechat_user.en.html#irc_ctcp_replies):

`/set irc.ctcp.version ""`

#### [Part and quit messages]

The [part](https://weechat.org/files/doc/stable/weechat_user.en.html#option_irc.server_default.msg_part) and [quit](https://weechat.org/files/doc/stable/weechat_user.en.html#option_irc.server_default.msg_quit) messages can contain custom text:

`/set irc.server_default.msg_part "Ciao!" `

`/set irc.server_default.msg_quit "Connection severed." `

Alternatively, these messages can be nullified in order to not share any information when leaving a channel or disconnecting from a network:

`/set irc.server_default.msg_part "Ciao!" `

`/set irc.server_default.msg_quit "Connection severed." `

### [Relay]

#### [Adding a relay]

In order to use remote interfaces, WeeChat needs to be configured as a relay. Substitute `` with a specific port above 1024, port 9001 is suggested for this purpose:

`/relay add weechat `

Next set the password for the relay:

`/set relay.network.password `

#### [Adding an encrypted relay]

An encrypted relay will ensure communications go directly between a browser and WeeChat relay, resulting in a greater level of privacy. All settings will be saved locally in the browser between sessions. [Let\'s Encrypt](https://wiki.gentoo.org/wiki/Let%27s_Encrypt "Let's Encrypt") can be used to make the process of certificate creation and renewal easier.

`root `[`#`]`mkdir -p ~/.config/weechat/tls `

`root `[`#`]`openssl req -nodes -newkey rsa:2048 -keyout relay.pem -x509 -days 3650 -out ~/.config/weechat/tls/relay.pem `

Configure Let\'s Encrypt and obtain the certificate:

`root `[`#`]`certbot certonly --standalone -d <domain> `

`root `[`#`]`install -d -m 0755 -o username -g username ~/.config/weechat/tls/ `

`root `[`#`]`mkdir -p ~/.weechat/tls `

`root `[`#`]`cat /etc/letsencrypt/live/<domain>/.pem > ~/.config/weechat/tls/relay.pem `

`root `[`#`]`chown -R username:username ~/.config/weechat/tls/`

Then in WeeChat:

`/relay add ssl.irc.freenode 8001 `

`/relay add ssl.weechat 9001 `

`/relay sslcertkey `

WeeChat will now serve clients on these ports using SSL. One can connect to the computer with the WeeChat relay by setting up a self-hosted relay or visiting [https://glowing-bear.org](https://glowing-bear.org) and chatting directly from a web browser.

#### [][Time-based One-Time Password (TOTP)]

TOTP (Time-based One-Time Password) support has been added in WeeChat, which can now generate and check TOTP validity.

A TOTP is generated with:

-   The secret (encoded in base 32),
-   The time (by default 0, which is the current time),
-   The number of digits (4 to 10 digits are supported, 6 is the default and recommended value).

`/secure set relay_totp_secret xxxxx `

`/set relay.network.totp_secret "$" `

If the password is valid and that TOTP is valid for the current time, the authentication is successful.

It is also possible to generate or validate TOTP with two new infos within WeeChat:

-   totp_generate: generate a TOTP
-   totp_validate: validate a TOTP

For example to show the value of TOTP for the secret *secretbase32*, current time, with 6 digits

`/eval -n $ `

#### [Remote interfaces]

The following remote interfaces are available:

-   [Glowing Bear](https://www.glowing-bear.org/) - A web frontend for WeeChat. See the [Glowing Bear Guide](https://wiki.gentoo.org/wiki/WeeChat/Glowing_Bear_Guide "WeeChat/Glowing Bear Guide") for hosting Glowing Bear on Gentoo.
-   [QWeeChat](https://weechat.org/download/devel/) - A Qt interface for WeeChat.
-   [WeeChat Android](https://play.google.com/store/apps/details?id=com.ubergeek42.WeechatAndroid) - Only works on Android phones. Simply download the application from the Google Play Store and get started!
-   [Emacs](https://github.com/the-kenny/weechat.el) - A weird emacs thing.
-   [WeeCloud](https://github.com/eirikb/weecloud) - A WeeChat client written in javascript.

Each remote interface has a unique setup. Not all of the clients available in the list above may be operational. Glowing Bear is probably the most tested of the bunch.

## [Usage]

It is common for many text-mode IRC client users to run the clients on a system that is always on always connected to the internet. This make it possible to never miss a mention or a message. Like most command-line programs, [weechat] will run all the time if opened in a [[screen](https://wiki.gentoo.org/wiki/Screen "Screen")] or a [[tmux](https://wiki.gentoo.org/wiki/Tmux "Tmux")] session which is then detached. This is currently the ideal method for staying connected to IRC networks continuously.

### [Invocation]

`user `[`$`]`weechat --help`

    WeeChat 3.8 Copyright (C) 2003-2023, compiled on Mar 28 2023 16:05:07
    Developed by Sébastien Helleu <flashcode@flashtux.org> - https://weechat.org/

    Usage: weechat [option...] [plugin:option...]

      -a, --no-connect         disable auto-connect to servers at startup
      -c, --colors             display default colors in terminal
      -d, --dir          force a single WeeChat home directory
                               or 4 different directories separated by colons (in this order: config, data, cache, runtime)
                               (environment variable WEECHAT_HOME is read if this option is not given)
      -t, --temp-dir           create a temporary WeeChat home directory and delete it on exit
                               (incompatible with option "-d")
      -h, --help               display this help
      -l, --license            display WeeChat license
      -p, --no-plugin          don't load any plugin at startup
      -P, --plugins   load only these plugins at startup
                               (see /help weechat.plugin.autoload)
      -r, --run-command <cmd>  run command(s) after startup;
                               many commands can be separated by semicolons and are evaluated,
                               this option can be given multiple times
      -s, --no-script          don't load any script at startup
          --upgrade            upgrade WeeChat using session files (see /help upgrade in WeeChat)
      -v, --version            display WeeChat version
      plugin:option            option for plugin (see man weechat)

    Debug options (for tools like valgrind, DO NOT USE IN PRODUCTION):
          --no-dlclose         do not call function dlclose after plugins are unloaded
          --no-gnutls          disable init/deinit of gnutls
          --no-gcrypt          disable init/deinit of gcrypt

### [screen]

Open [screen] using the following command:

`user `[`$`]`screen -t weechat`

After [weechat] is configured press [Ctrl]+[a] to enter *Command Mode* and then [d] to detach from the [screen] session. It can be re-attached to later by running:

`user `[`$`]`screen -ls`

To list the currently running sessions and then entering:

`user `[`$`]`screen -r <session>`

Where `<session>` is a weird, crazy string.

For additional information on how to use [screen] visit the [screen article](https://wiki.gentoo.org/wiki/Screen "Screen").

### [tmux]

To open a new [tmux] session for [weechat], the following command can be used:

`user `[`$`]`tmux new-session -s weechat weechat`

To start it as a daemon, use:

`user `[`$`]`tmux new-session -d -s weechat weechat`

To attach to the session (if started as a daemon), run:

`user `[`$`]`tmux attach-session -t weechat`

This can be executed on login using:

[FILE] **`~/.bashrc`Start weechat on shell login**

    if [[ $(ps -ef | grep -c tmux) -eq 1 ]] || ([[ $(ps -ef | grep -c tmux) -ne 1 ]] && ! tmux has-session -t weechat) ; then
        echo "Starting weechat tmux session"
        tmux new-session -d -s weechat weechat
    fi

After [weechat] has been configured, disconnect from the session by using [Ctrl]+[b] and then press [d] to detach.

In order to reconnect to the [tmux] session that is running (which was titled *weechat*) issue:

`user `[`$`]`tmux attach-session -t weechat`

For additional information on how to use [tmux] visit the [tmux article](https://wiki.gentoo.org/wiki/Tmux "Tmux").

## [Upgrades]

After emerging updates, [weechat] can be \'in-place\' upgraded without losing the currently open buffer list. This is performed by running the following command inside the weechat client:

`weechat``/upgrade`

See the [upstream user guide](https://weechat.org/files/doc/stable/weechat_user.en.html#command_weechat_upgrade) for more additional details.

## [Troubleshooting]

### [Mouse usage]

Mouse usage is not enabled by default. To enable it (at startup):

`/set weechat.look.mouse on`

`/mouse enable`

## [Removal]

### [Unmerge]

Remove WeeChat:

`root `[`#`]`emerge --ask --depclean --verbose net-irc/weechat`

### [Configuration and logs]

** Important**\
This will delete all message history and any saved settings.

After unmerging, for a full clean-up, be sure to remove old logs and individual user configuration from their default location in each [weechat] user\'s home directory:

`user `[`$`]`rm -rf ~/.config/weechat/`

`user `[`$`]`rm -rf ~/.local/share/weechat/logs/`

## [See also]

-   [IRC/Guide](https://wiki.gentoo.org/wiki/IRC/Guide "IRC/Guide") --- provides a broad overview of concepts related to IRC.
-   [Irssi](https://wiki.gentoo.org/wiki/Irssi "Irssi") --- a powerful text-mode IRC client for connecting to internet relay chat (IRC) networks.
-   [Quassel](https://wiki.gentoo.org/wiki/Quassel "Quassel") --- a daemon/headless IRC client written in C++ that supports 24/7 connectivity.

## [External resources]

-   [FAQ (official)](https://weechat.org/files/doc/weechat_faq.en.html) - A list of Frequently Asked Questions concerning WeeChat.
-   [Quick Start guide (official)](https://weechat.org/files/doc/stable/weechat_quickstart.en.html) - WeeChat\'s excellent little Quick Start guide. It covers all the steps needed in order to connect to an IRC server, set up a nick name, etc. It\'s well worth the 5 minute read time.
-   [User\'s guide (official)](https://weechat.org/files/doc/stable/weechat_user.en.html) - An in-depth user guide. Helpful for those who desired to become deeply familiar with WeeChat. It is also helpful as reference material.
-   [Scripting guide (official)](https://weechat.org/files/doc/stable/weechat_scripting.en.html)
-   [Plugin API reference (official)](https://weechat.org/files/doc/stable/weechat_plugin_api.en.html) - Want to write a remote interface (front end) for WeeChat? This is one of the articles for that.
-   [Relay protocol (official)](https://weechat.org/files/doc/stable/weechat_relay_protocol.en.html) - This is another article that will need to be covered in order to write a remote interface (front end) for WeeChat.
-   [Developer\'s guide (official)](https://weechat.org/files/doc/stable/weechat_dev.en.html) - Want to develop WeeChat itself? Reading this guide will help with that goal.

## [References]

1.  [[[↑](#cite_ref-1)] [[https://wiki.znc.in/Weechat#Connecting_to_ZNC](https://wiki.znc.in/Weechat#Connecting_to_ZNC)]]
2.  [[[↑](#cite_ref-2)] [[https://libera.chat/guides/weechat](https://libera.chat/guides/weechat)]]
3.  [[[↑](#cite_ref-3)] [[https://www.weechat.org/files/doc/stable/weechat_user.en.html#irc_tls_certificates](https://www.weechat.org/files/doc/stable/weechat_user.en.html#irc_tls_certificates)]]