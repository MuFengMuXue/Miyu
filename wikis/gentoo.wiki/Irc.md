Other languages:

-   [English]
-   [français](https://wiki.gentoo.org/wiki/IRC/fr "IRC (100% translated)")
-   [italiano](https://wiki.gentoo.org/wiki/IRC/it "IRC/it (100% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/IRC/hu "IRC (100% translated)")
-   [русский](https://wiki.gentoo.org/wiki/IRC/ru "IRC (64% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/IRC/ja "IRC (100% translated)")

**Resources**

[[]][Gentoo IRC channels](https://www.gentoo.org/get-involved/irc-channels/)

[[]][All Gentoo IRC channels](https://www.gentoo.org/get-involved/irc-channels/all-channels.html)

[[]][Guide](https://wiki.gentoo.org/wiki/IRC/Guide "IRC/Guide")

[[]][Wikipedia](https://en.wikipedia.org/wiki/IRC "wikipedia:IRC")

**Internet Relay Chat** (**IRC**) is a stable, mature, text-based chat (instant messaging) system. IRC is one of the primary avenues of communication for those involved at all levels in the [Gentoo project](https://wiki.gentoo.org/wiki/Project:Gentoo "Project:Gentoo").

## Contents

-   [[1] [IRC and Gentoo]](#IRC_and_Gentoo)
-   [[2] [Available software]](#Available_software)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Spam protection]](#Spam_protection)
-   [[4] [External resources]](#External_resources)

## [IRC and Gentoo]

Since chat messages are sent and received almost instantly, IRC allows the Gentoo project to have a very reactive collaboration processes.

There are Gentoo IRC channels for user support. For any issue, a preexisting solution should be sought using a search engine, the [forums](https://forums.gentoo.org/), [mailing lists](https://www.gentoo.org/get-involved/mailing-lists/all-lists.html), and here on the wiki, before asking on a support channel.

** See also**\
See the [support](https://wiki.gentoo.org/wiki/Support "Support") page for tips on how to ask for help with issues with Gentoo.

Most Gentoo subprojects have a specific channel on [Libera Chat](https://libera.chat/) for inter-project communication. Project-related channels are used for: tracking changes to source code, requesting and discussing (new) features, addressing various issues, real-time team meetings, internal support, and communication between Gentoo developers and the community.

There is a bot in many channels called [Willikins](https://wiki.gentoo.org/wiki/Willikins "Willikins") that has some handy functionality.

** Important**\
The [Gentoo IRC channels on Libera Chat](https://www.gentoo.org/get-involved/irc-channels/all-channels.html) have a **[code of conduct](https://wiki.gentoo.org/wiki/Project:Council/Code_of_conduct#Behavior_and_Consequences "Project:Council/Code of conduct")** that should be read and understood by each user before connecting to any channel. See also the [guidelines on the main site](https://www.gentoo.org/get-involved/irc-channels/index.html).

** Important**\
Gentoo IRC channels, like the mailing lists, are [*not*] encrypted; all discussion therein is entirely visible to the public in plain text and is most likely logged by every user present in the channel. It is unwise and unsafe to post private information inside IRC channels.

** Note**\
See the [list of IRC channels](https://www.gentoo.org/get-involved/irc-channels/) managed by the Gentoo project for support, discussion of specific topics, and general chat, but read the above section, and the [code of conduct](https://wiki.gentoo.org/wiki/Project:Council/Code_of_conduct#Behavior_and_Consequences "Project:Council/Code of conduct") first.

** Tip**\
Do not paste long text excerpts, or whole files, to IRC. Use [wgetpaste](https://wiki.gentoo.org/wiki/Wgetpaste "Wgetpaste") if long passages are to be shared.

## [Available software]

The following table contains some of the IRC software available in Gentoo. Discover which client works best by emerging each one or by visiting each homepage:

  -------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ---------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------
  Name                                                                       Package                                                                                                                                                                                                                                                                                                                                                                                                            Homepage                                                                                                               Description
  catgirl                                                                    [[[net-irc/catgirl::guru]](https://gpo.zugaina.org/Overlays/guru/net-irc/catgirl)[]]   [https://git.causal.agency/catgirl/about/](https://git.causal.agency/catgirl/about/)   A TLS-only terminal IRC client
  [HexChat](https://wiki.gentoo.org/wiki/HexChat "HexChat")                  [[[net-irc/hexchat]](https://packages.gentoo.org/packages/net-irc/hexchat)[]]                                                [https://hexchat.github.io/](https://hexchat.github.io/)                               Graphical IRC client based on XChat.
  [Irssi](https://wiki.gentoo.org/wiki/Irssi "Irssi")                        [[[net-irc/irssi]](https://packages.gentoo.org/packages/net-irc/irssi)[]]                                                      [https://irssi.org/](https://irssi.org/)                                               A modular text UI IRC client with IPv6 support.
  ircii                                                                      [[[net-irc/ircii]](https://packages.gentoo.org/packages/net-irc/ircii)[]]                                                      [http://eterna.com.au/ircii/](http://eterna.com.au/ircii/)                             An IRC and ICB client that runs under most UNIX platforms.
  [Konversation](https://wiki.gentoo.org/wiki/Konversation "Konversation")   [[[net-irc/konversation]](https://packages.gentoo.org/packages/net-irc/konversation)[]]                                 [https://konversation.kde.org/](https://konversation.kde.org/)                         User friendly IRC Client based on KDE Frameworks.
  kvirc                                                                      [[[net-irc/kvirc]](https://packages.gentoo.org/packages/net-irc/kvirc)[]]                                                      [http://www.kvirc.net/](http://www.kvirc.net/)                                         A portable IRC client that uses the Qt GUI toolkit.
  [Pidgin](https://wiki.gentoo.org/wiki/Pidgin "Pidgin")                     [[[net-im/pidgin]](https://packages.gentoo.org/packages/net-im/pidgin)[]]                                                      [https://pidgin.im/](https://pidgin.im/)                                               GTK Instant Messenger client.
  Polari                                                                     [[[net-irc/polari]](https://packages.gentoo.org/packages/net-irc/polari)[]]                                                   [https://wiki.gnome.org/Apps/Polari](https://wiki.gnome.org/Apps/Polari)               An IRC client for GNOME
  [Quassel](https://wiki.gentoo.org/wiki/Quassel "Quassel")                  [[[net-irc/quassel]](https://packages.gentoo.org/packages/net-irc/quassel)[]]                                                [https://quassel-irc.org/](https://quassel-irc.org/)                                   Qt5 IRC client supporting a remote daemon for 24/7 connectivity
  Srain                                                                      [[[net-irc/srain::guru]](https://gpo.zugaina.org/Overlays/guru/net-irc/srain)[]]         [https://srain.silverrainz.me/](https://srain.silverrainz.me/)                         Modern, beautiful IRC client written in GTK+ 3
  [WeeChat](https://wiki.gentoo.org/wiki/WeeChat "WeeChat")                  [[[net-irc/weechat]](https://packages.gentoo.org/packages/net-irc/weechat)[]]                                                [https://weechat.org/](https://weechat.org/)                                           Portable and multi-interface (text, web, and GUI) IRC client.
  -------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ---------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------

## [Usage]

** See also**\
See the IRC [guide article](https://wiki.gentoo.org/wiki/IRC/Guide "IRC/Guide") for information on IRC usage.

Learning can be more challenging when starting using a text-mode (CLI) client like [Irssi](https://wiki.gentoo.org/wiki/Irssi "Irssi") or [WeeChat](https://wiki.gentoo.org/wiki/WeeChat "WeeChat"), the [IRC guide](https://wiki.gentoo.org/wiki/IRC/Guide "IRC/Guide") can be particularly helpful with this.

### [Spam protection]

In order to prevent **private message spam** on IRC from unregistered users, one can set **user modes** `+g` or `+R`.

Larry wants to ignore private messages from users who are not identified, but wants to get an information that someone wanted to send a message to Larry. Larry can decide to receive messages with the [/accept] command:

`/mode larry +g`

Larry wants to ignore private messages from users who are not identified totally:

`/mode larry +R`

## [External resources]

-   [https://gentoo.org/get-involved/irc-channels/](https://gentoo.org/get-involved/irc-channels/)
-   [https://www.irchelp.org/](https://www.irchelp.org/) - A site dedicated to helping users understand IRC.
-   [https://libera.chat/](https://libera.chat/) - A next-generation IRC network for free and open source software projects and similarly-spirited collaborative endeavors.
-   [https://libera.chat/guides/usermodes](https://libera.chat/guides/usermodes) - Libera Chat article on user modes\*
-   [https://www.oftc.net/](https://www.oftc.net/) - A stable and effective IRC network that provides collaboration services to members of the free software community in any part of the world.