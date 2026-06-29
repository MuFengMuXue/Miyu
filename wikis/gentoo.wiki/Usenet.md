*Not to be confused with [RSS news feeds](https://wiki.gentoo.org/wiki/RSS "RSS").*

*Not to be confused with [Email mailing lists](https://wiki.gentoo.org/wiki/Email "Email").*

**Resources**

[[]][Home](https://www.big-8.org)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Usenet "wikipedia:Usenet")

[[]][[#usenet](ircs://irc.libera.chat/#usenet)] ([[webchat](https://web.libera.chat/#usenet)])

[[]][[alt.fan.usenet](news:alt.fan.usenet) ([weblink](https://www.novabbs.com/devel/thread.php?group=alt.fan.usenet))]

[[]][[news.software.readers](news:news.software.readers) ([weblink](https://www.novabbs.com/devel/thread.php?group=news.software.readers))]

[[]][[news.groups.proposals](news:news.groups.proposals) ([weblink](https://www.novabbs.com/devel/thread.php?group=news.groups.proposals))]

[[]][[news.admin.peering](news:news.admin.peering) ([weblink](https://www.novabbs.com/devel/thread.php?group=news.admin.peering))]

[[]][[alt.free.newsservers](news:alt.free.newsservers) ([weblink](https://www.novabbs.com/devel/thread.php?group=alt.free.newsservers))]

[[]][r/usenet](https://reddit.com/r/usenet)

**Usenet** is a federated and decentralized worldwide Internet forum and the world\'s oldest digital social network. Usenet has been in continuous operation since 1979. It is among the oldest federated network services of any kind, likely second only to e-mail, which itself was invented in 1971. Usenet was initially created by two Duke University graduate students as an experiment, but it very quickly grew beyond the confines of Duke University. News is and has been distributed by various transports, some of them improvised. For much of its history, Usenet used the Unix-to-Unix Copy ([UUCP](https://wiki.gentoo.org/index.php?title=UUCP&action=edit&redlink=1 "UUCP (page does not exist)")) protocol to pass traffic between nodes. This was done primarily over landline telephones but other means of passing message traffic between servers have been improvised over the years. With the rise of the Internet and TCP/IP networking, Usenet primarily accepts traffic via the Network News Transfer Protocol ([NNTP](https://wiki.gentoo.org/index.php?title=NNTP&action=edit&redlink=1 "NNTP (page does not exist)")). Perhaps because of its simplicity Usenet readily accepted traffic gated from other networks. It is most likely that this flexibility together with its distributed nature enabled it to long outlive multiple precursors to the modern Internet.

At its heart, Usenet is an extremely delay tolerant store-and-forward network for passing messages between nodes. The propagation model ensures *eventual consistency* between servers. Because all content is shared with all members of the network, content is difficult to remove. This is a blessing and a curse. On the one hand it makes Usenet censorship resistant. On the other hand individual Usenet server operators purge undesired messages only from their own systems. Message types advising the rest of the network to delete a given file do exist, but the protocol does not require remote servers act on them. Consequently, removing illicit content from a single Usenet server is a simple task, but purging it from the entire network is another matter.

Unexpectedly, large snapshots of Usenet message history have appeared on the Internet. Some of them are organized and searchable. This has been a boon to Internet historians.

## Contents

-   [[1] [Gentoo Newsgroups on Usenet]](#Gentoo_Newsgroups_on_Usenet)
-   [[2] [Netnews Software on Gentoo]](#Netnews_Software_on_Gentoo)
-   [[3] [Understanding Usenet and Netnews]](#Understanding_Usenet_and_Netnews)
    -   [[3.1] [Google Groups Compared to Usenet]](#Google_Groups_Compared_to_Usenet)
    -   [[3.2] [Usenet Compared to Email]](#Usenet_Compared_to_Email)
    -   [[3.3] [Usenet Compared to BitTorrent]](#Usenet_Compared_to_BitTorrent)
    -   [[3.4] [Usenet Compared to Centralized Social Media Sites]](#Usenet_Compared_to_Centralized_Social_Media_Sites)
    -   [[3.5] [Usenet Compared to Anonymity Networks]](#Usenet_Compared_to_Anonymity_Networks)
    -   [[3.6] [Usenet Terminology]](#Usenet_Terminology)
    -   [[3.7] [An Overview of Usenet History]](#An_Overview_of_Usenet_History)
-   [[4] [Troubleshooting]](#Troubleshooting)
    -   [[4.1] [How do I get a Usenet account?]](#How_do_I_get_a_Usenet_account.3F)
    -   [[4.2] [How do I propose a new Usenet newsgroup?]](#How_do_I_propose_a_new_Usenet_newsgroup.3F)
    -   [[4.3] [How do I run a local Usenet server?]](#How_do_I_run_a_local_Usenet_server.3F)
    -   [[4.4] [How do I link to Usenet or other Netnews Service from the Web?]](#How_do_I_link_to_Usenet_or_other_Netnews_Service_from_the_Web.3F)
    -   [[4.5] [Someone insulted me on Usenet]](#Someone_insulted_me_on_Usenet)
    -   [[4.6] [How do I set fonts or insert emojis?]](#How_do_I_set_fonts_or_insert_emojis.3F)
    -   [[4.7] [What\'s with all the \"dead\" Newsgroups?]](#What.27s_with_all_the_.22dead.22_Newsgroups.3F)
    -   [[4.8] [How do I become a Usenet newsgroup moderator?]](#How_do_I_become_a_Usenet_newsgroup_moderator.3F)
    -   [[4.9] [How do I get an authoritative list of ALL Usenet Newsgroups?]](#How_do_I_get_an_authoritative_list_of_ALL_Usenet_Newsgroups.3F)
    -   [[4.10] [Are there mobile Usenet newsreaders for smartphones and tablets?]](#Are_there_mobile_Usenet_newsreaders_for_smartphones_and_tablets.3F)
    -   [[4.11] [Is Usenet part of the Fediverse?]](#Is_Usenet_part_of_the_Fediverse.3F)
-   [[5] [See also]](#See_also)
-   [[6] [External resources]](#External_resources)

## [Gentoo Newsgroups on Usenet]

  --------------------------------------------------------------------------------------- ----------- ----------------------------------------------------------------------------------------------------------------------
  Newsgroup                                                                               Moderated   Description
  [`alt.os.linux.gentoo`](news:alt.os.linux.gentoo)       No          Gentoo Linux support and discussion newsgroup.
  [`linux.gentoo.announce`](news:linux.gentoo.announce)   Yes         Mirrors [gentoo-announce@lists.gentoo.org](mailto:gentoo-announce@lists.gentoo.org).
  [`linux.gentoo.dev`](news:linux.gentoo.dev)             Yes         Mirrors [gentoo-dev@lists.gentoo.org](mailto:gentoo-dev@lists.gentoo.org).
  [`linux.gentoo.user`](news:linux.gentoo.user)           Yes         Mirrors [gentoo-user@lists.gentoo.org](mailto:gentoo-user@lists.gentoo.org).
  [`linux.gentoo.user.de`](news:linux.gentoo.user.de)     Yes         Mirrors [gentoo-user-de@lists.gentoo.org](mailto:gentoo-user-de@lists.gentoo.org).
  [`linux.gentoo.user.es`](news:linux.gentoo.user.es)     Yes         Mirrors [gentoo-user-es@lists.gentoo.org](mailto:gentoo-user-es@lists.gentoo.org).
  [`linux.gentoo.user.fr`](news:linux.gentoo.user.fr)     Yes         Mirrors [gentoo-user-fr@lists.gentoo.org](mailto:gentoo-user-fr@lists.gentoo.org).
  [`linux.gentoo.user.id`](news:linux.gentoo.user.id)     Yes         Mirrors [gentoo-user-id@lists.gentoo.org](mailto:gentoo-user-id@lists.gentoo.org).
  [`linux.gentoo.user.kr`](news:linux.gentoo.user.kr)     Yes         Mirrors [gentoo-user-kr@lists.gentoo.org](mailto:gentoo-user-kr@lists.gentoo.org).
  [`linux.gentoo.user.pl`](news:linux.gentoo.user.pl)     Yes         Mirrors [gentoo-user-pl@lists.gentoo.org](mailto:gentoo-user-pl@lists.gentoo.org).
  --------------------------------------------------------------------------------------- ----------- ----------------------------------------------------------------------------------------------------------------------

## [Netnews Software on Gentoo]

Netnews servers are designed around a client-server relationship model. Netnews servers exchange messages with peers until consistency is achieved across the network. Clients, called Newsreaders, access the messages stored on a remote server.

  ----------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Name                                                                    Package                                                                                                                                                                                                                                                                                                                                                                                       Description
  Netnews Servers
  inn                                                                     [net-nntp/inn](https://gitweb.gentoo.org/repo/proj/guru.git/tree/net-nntp/inn) ([GURU](https://wiki.gentoo.org/wiki/GURU "GURU"))                                                                                                                                                                                                               A scalable Netnews server analogous to [postfix](https://wiki.gentoo.org/wiki/Postfix "Postfix").
  leafnode                                                                [[[net-nntp/leafnode]](https://packages.gentoo.org/packages/net-nntp/leafnode)[]]                     A Netnews server designed for small sites.
  Newsreaders --- Graphical
  claws mail                                                              [[[mail-client/claws-mail]](https://packages.gentoo.org/packages/mail-client/claws-mail)[]]      An email client and news reader based on GTK+.
  evolution                                                               [[[mail-client/evolution]](https://packages.gentoo.org/packages/mail-client/evolution)[]]         Integrated mail, newsreader, addressbook, and calendaring application.
  gnus                                                                    [[[app-xemacs/gnus]](https://packages.gentoo.org/packages/app-xemacs/gnus)[]]                           The Gnus Newsreader and Mailreader for xemacs.
  pan                                                                     [net-nntp/pan](https://gitweb.gentoo.org/repo/proj/guru.git/tree/net-nntp/pan) ([GURU](https://wiki.gentoo.org/wiki/GURU "GURU"))                                                                                                                                                                                                               A graphical newsreader for GNOME with full support for text and binary content.
  seamonkey                                                               [[[www-client/seamonkey]](https://packages.gentoo.org/packages/www-client/seamonkey)[]]            Seamonkey Web Browser, Email, and Newsreader.
  [thunderbird](https://wiki.gentoo.org/wiki/Thunderbird "Thunderbird")   [[[mail-client/thunderbird]](https://packages.gentoo.org/packages/mail-client/thunderbird)[]]   An email client with a built-in graphical Newsreader.
  Newsreaders --- Terminal
  alpine                                                                  [[[mail-client/alpine]](https://packages.gentoo.org/packages/mail-client/alpine)[]]                  An easy to use text-based based mail and netnews client.
  [mutt](https://wiki.gentoo.org/wiki/Mutt "Mutt")                        [[[mail-client/mutt]](https://packages.gentoo.org/packages/mail-client/mutt)[]]                        A small but very powerful text-based mail and netnews client.
  [neomutt](https://wiki.gentoo.org/wiki/Mutt "Mutt")                     [[[mail-client/neomutt]](https://packages.gentoo.org/packages/mail-client/neomutt)[]]               A small but very powerful text-based mail and netnews client.
  newspost                                                                [[[net-nntp/newspost]](https://packages.gentoo.org/packages/net-nntp/newspost)[]]                     A usenet binary autoposter for Linux.
  nzbget                                                                  [[[net-nntp/nzbget]](https://packages.gentoo.org/packages/net-nntp/nzbget)[]]                           A command-line based binary newsgrabber supporting [.nzb] files.
  sabnzbd                                                                 [[[net-nntp/sabnzbd]](https://packages.gentoo.org/packages/net-nntp/sabnzbd)[]]                        Binary newsgrabber with web-interface.
  slrn                                                                    [[[net-nntp/slrn]](https://packages.gentoo.org/packages/net-nntp/slrn)[]]                                 The classic text-based newsreader, akin to [[mutt](https://wiki.gentoo.org/wiki/Mutt "Mutt")].
  tin                                                                     [[[net-nntp/tin]](https://packages.gentoo.org/packages/net-nntp/tin)[]]                                    A threaded NNTP and spool-based Newsreader.
  Netnews Gateways
  suck                                                                    [[[net-nntp/suck]](https://packages.gentoo.org/packages/net-nntp/suck)[]]                                 Grab news from a remote NNTP server and feed them to another.
  Common Tools
  sharutils                                                               [[[app-arch/sharutils]](https://packages.gentoo.org/packages/app-arch/sharutils)[]]                  Tools to deal with shar archives and [uuencode] files.
  yydecode                                                                [[[net-news/yydecode]](https://packages.gentoo.org/packages/net-news/yydecode)[]]                     A decoder for yENC format, popular on Usenet.
  ----------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## [Understanding Usenet and Netnews]

### [Google Groups Compared to Usenet]

** Note**\
Google has advised: \"Effective February 22, 2024, Google Groups will no longer support new Usenet content. Posting and subscribing will be disallowed, and new content from Usenet peers will not appear. Viewing and searching of historical data will still be supported as it is done today.\"

Google Groups partially federates with Usenet under the hood, restricted to text-only news groups (as is common for free Usenet providers).

**Google Groups is not Usenet**:

-   Native Google groups do not propagate over Usenet, they\'re unique to Google.
-   Google blocks access to some groups that are perfectly accessible via a normal Usenet account.
-   Ironically for a search engine company, the advanced search feature (which used to search all of Usenet) no longer works.

### [Usenet Compared to Email]

**Like [email](https://wiki.gentoo.org/wiki/Email "Email")**, each Usenet server is may accept or reject traffic as it sees fit but there is no individual or group in charge of the entire network. Messages pass from a Usenet poster to a Netnews server, just as with email, but the messages then propagate to the *entire network* and not to some specified recipient(s) on the network. Just as email users need a software client to access email, a Newsreader is required to access messages on Usenet. The newsreader may be locally installed or it may be a web portal. Messages are fundamentally text files, the inclusion of binary files is ultimately a hack.

Due to the distributed nature of both email and Usenet, some amount of spam is inevitable. Message retention policies and capacity may differ from one Usenet provider to another. Some Usenet servers may not store messages at all and simply act as a relay to pass message to the rest of the network. Some messages may be rejected because it contains attachments or because it is too large. Just like spam blacklists in an email context, in the case of a severely misbehaving news server other servers may block all traffic originating from that server.

Just as an email provider may suspend an individual\'s account for violating its terms of service, a Usenet administrator may do the same. Because Usenet is federated a banned user may simply switch to another Usenet provider and return to the network. Further, is technically possible for an individual to self-host an Netnews and participate with the rest of the network. As a practical matter most people who do this reject messages from most groups dedicated to sharing binaries. Fully federating with Usenet including binaries groups easily consumes 1--2 tara*bytes* --- that\'s *bytes* not *bits* --- of bandwidth per day.

Just as with email conversations, Usenet conversations are threaded to make them easy to follow. While email has a symmetrical relationship to privacy: anyone can see who is sending to whom Usenet has an asymmetrical relationship to it. Anyone can see who is posting but tracking down everyone who may have accessed a given message is effectively impossible. Obfuscation of a sender\'s identity technically possible under some conditions but this not an inherent feature of the Network News Transfer Protocol itself.

Encryption of message contents and digital message signing are possible with Usenet, just as they are with email, neither protocols enforce this as a requirement. Both Usenet\'s NNTP traffic and email\'s SNMP traffic are typically secured in transit with TLS encryption. Both protocols require messages to have headers and both protocols have evolved formally (by [RFC](https://en.wikipedia.org/wiki/Request_for_Comments "wikipedia:Request for Comments")) and informally through the use of X-headers to accommodate new features. Just as with a post to a public email list, your Usenet post history may live far longer than you expect and may lead to later embarrassment.

**Unlike email**, assuming full federation, all servers eventually receive a copy of all messages passing through the Usenet network. Hence [John Gilmore](https://en.wikipedia.org/wiki/John_Gilmore_(activist) "wikipedia:John Gilmore (activist)")\'s famous adage, \"The Net interprets censorship as damage and routes around it.\" Unlike mail server host names, the names of newsgroups do not exist as DNS records; consequently, they are immune to DNS take-down requests. While most likely stored in a database now, Usenet hierarchies were originally simple directory entries in a news server\'s file system.

Unlike modern email, messages are generally stored as plain text and do not contain HTML markup. Some people do write their messages in the style of a lightweight markup language, such as Markdown, but the message format does not enforce this. Unfortunately, Usenet missed out on the mobile computing revolution of the past decade or so. As a result, Usenet apps for smartphones are almost unheard of but due to the rise in interest in federated social media platforms this may well change in the near future.

### [Usenet Compared to BitTorrent]

**Like BitTorrent,** Usenet can technically be used to share files. Unfortunately it was not designed for this sort of an application and the inclusion of attachments in Usenet messages is an inefficient hack. Binaries [encoded as text](https://en.wikipedia.org/wiki/Binary-to-text_encoding "wikipedia:Binary-to-text encoding") take up significantly more space than raw binaries stored directly on a file system. Email suffers from this problem as well. Worse, by default all messages are shared with all nodes on the network. As a consequence, every file uploaded to Usenet there are thousands of redundant copies of it spread across the network. Given that demand for a specific file is not distributed evenly at a global scale almost none of the redundant copies will ever be accessed by a human being on the network. Nevertheless, it\'s impossible to stop people from uploading attachments to Usenet as this would just create an arms race as posters find ever more clever ways to disguise binary data from whatever filter is setup to stop it. Like any other tool, Usenet\'s file sharing capability may be used for licit or illicit purposes by the user.

**Unlike BitTorrent,** Usenet traffic is not peer-to-peer, it\'s much more like email in that messages between servers before reaching individual subscribers via their newsreaders. As a consequence of this architecture, users who merely access preexisting content already stored on the network are not simultaneously sharing it themselves.

### [Usenet Compared to Centralized Social Media Sites]

**Like centralized social media sites,** such as Facebook or Reddit many people use the service for different reasons. Some people want to chat with others regarding common interests. Others are looking for honest reviews of products and services. Still more are looking for community technical support, etc.

Usenet newsgroups are akin to subreddits, most have a niche, and all have unique names like [[comp.mail.mutt](news:comp.mail.mutt) ([weblink](https://www.novabbs.com/devel/thread.php?group=comp.mail.mutt))] or [[comp.lang.python](news:comp.lang.python) ([weblink](https://www.novabbs.com/devel/thread.php?group=comp.lang.python))]. Just like Reddit, there is some amount of overlap with respect to similarly named groups, this may cause confusion at first. Also, because anyone can post, misinformation can spread quickly and posts that are popular may or may not be as well informed as they seem to be. Such is the nature of the Internet more generally.

**Unlike centralized social media sites,** with the exception of those who have interacted with Usenet, perhaps unknowingly, via [Google Groups](https://en.wikipedia.org/wiki/Google_Groups "wikipedia:Google Groups") connecting to Usenet via an intermediary web portal or smartphone app is rare. To be fair, increased interest in federated and self-hosted applications is starting to change this.

There is no mechanism to vote on posts, no concept of poster \"karma\" and no profiles or avatars. There are *some parts* of Usenet are moderated but the vast majority of newsgroups are unmoderated. That said, all Usenet servers have a mechanism to report egregious violations of their terms of service. However, attempting to use that mechanism as a \"super down-vote\" instead of its intended purpose is unlikely to be well received. As a class, Usenet and its server administrators take a *dim view* of attempts at viewpoint censorship.

Due to this ethos and the federated nature of Usenet deplatforming someone for unpopular, heterodox, or even condemnable views verges on the impossible. The server administrator can block bad actor\'s accounts, delete spam messages, or in severe cases their server of origin, but that account or server can still participate with the rest of the network. Most modern newsreaders have a *ignore post from specified addresses* feature. In these respects, Usenet and its moderation mechanisms are much closer to those of the modern [Fediverse](https://en.wikipedia.org/wiki/Fediverse "wikipedia:Fediverse").

### [Usenet Compared to Anonymity Networks]

**Like many anonymity networks,** content is spread around the globe in many jurisdictions frustrating efforts to exercise information or viewpoint censorship. Usenet traffic can [gate](https://en.wikipedia.org/wiki/https://en.wikipedia.org/wiki/Gateway_(telecommunications) "wikipedia:https://en.wikipedia.org/wiki/Gateway (telecommunications)") to other networks or [encapsulate](https://en.wikipedia.org/wiki/https://en.wikipedia.org/wiki/Encapsulation_(computer_programming) "wikipedia:https://en.wikipedia.org/wiki/Encapsulation (computer programming)") within other protocols, as it has done over the course of its history, to pass traffic if a hostile ISP or other actor manages to block Usenet access directly. Consequently, simply blocking the relevant TCP ports nation wide will be \"perceived as damage\" by the Usenet network and ultimately \"routed around\" in a manner not entirely dissimilar to the Tor network.

**Unlike many anonymity networks,** posters on the network are not anonymized by default and it\'s very likely that a Usenet server knows who its customers are, and can provide personally identifiable information if compelled to do so. However, the reader is only exposed to his local Usenet provider but the poster may be exposed to some degree to the entire network. While it is virtually impossible to uncover the identity of *every person* who accessed a given Usenet post, it\'s unlikely to be difficult to unmask at least some of them. The poster may limited exposure by simply encrypting a post. However, the post\'s headers remain in clear text and likely reveal the path the message traveled from its server of origin to the rest of the network. So, achieving full anonymity for both poster and reader is more difficult than on Tor without taking additional steps.

Tor is a low-latency anonymity network intended to handle real-time traffic. Usenet\'s traffic model does not require anything like real time communication. As a result, the Usenet network can even be accessed indirectly by removable media --- in a bidirectional manner --- something Tor cannot realistically do.

Access to Usenet text articles over Tor is possible but ***accessing large binary files over Tor strongly discouraged*** due to bandwidth limitations of the network. All Tor nodes are run by volunteers and bandwidth on the network is nearly always at a premium. Most VPN providers have ample bandwidth for to support downloads, Tor does not.

### [Usenet Terminology]

-   *Big 8* --- The major Usenet hierarchies of which there were originally seven: [comp.\*], [misc.\*], [news.\*], [rec.\*], [sci.\*], [soc.\*], [talk.\*]. The eighth, [alt.\*], was eventually added later.
-   *Cross posting* --- posting identical or near identical messages in multiple newsgroups.
-   *Eternal September* --- September circa 1993, when ISP\'s begin marketing Usenet access to new users. These users, unaccustomed to the civil norms of Usenet up to this point begin behaving badly in ways now common to social networks.
-   *Flaming* --- the act of posting *ad hominem* attacks, typically including vulgar language and insults.
-   *Kill file* --- Client-side files with exclusion patterns to filter out Spam by sender, subject, domain, etc.
-   *Indexer* --- a centralized Usenet search engine.
-   *Lurker* --- someone who reads Usenet but does not post, inherited from [BBS](https://en.wikipedia.org/wiki/Bulletin_board_system "wikipedia:Bulletin board system") slang.
-   *Newsreader* --- A News client, akin to an email client.
-   *Netnews* --- newsgroups as a medium of information exchange generally, including private instances.
-   *Netiquette* --- Norms of etiquette and expected behavior on Usenet.
-   *Newsgroup* --- A directory-like group where related messages are stored, akin to a subreddit.
-   *News server* --- any server that provides Network News messaging, even if it is not gated to Usenet.
-   *NNSP* --- NetNews Server Protocol for *bulk* transfer of messages between news servers, typically over tcp/433 (clear text) or tcp/563 (TLS).
-   *NNTP* --- NetNews Transmission Protocol the most common means by which Usenet traffic propagates to other servers or to individual Newsreaders, typically over tcp/119 (clear text) or tcp/563 (TLS).
-   *Request for Discussion (RFD)* --- a proposal for creating a new Usenet newsgroup.
-   *Sock Puppet* --- A user with multiple accounts often used to start arguments or shill for a given cause.
-   *Spam* --- unsolicited email of a commercial nature.
-   *Sporgery* --- A portmanteau of the words *spam* and *forgery* referring to the disruptive act of flooding a newsgroup with fake articles.
-   *Spotnet* --- a decentralized alternative to indexers.
-   *Usenet* --- The largest global Network News implementation.
-   *Usenet Death Penalty* --- a melodramatic way of referring to an individual who has had their Usenet access temporarily or permanently revoked by a server. This is rarely done because a user can simply move to another Usenet provider. This term can also be applied to news servers that have been blacklisted by other server operators, typically for originating large amounts of spam messages.
-   *UUCP* --- Unix-to-Unix Copy a network protocol originally intended for routing traffic over land line telephone circuits or serial cable links. Though rare, the protocol is still occasionally used for data transmission over long distance low baud rate radio links when TCP/IP or x.25 are deemed to present too much overhead.

### [An Overview of Usenet History]

Despite its age, Netnews in general and Usenet in particular is far more resilient and flexible than many modern distributed services. It can deal with delays and inconsistencies that would bring just about any other service to its knees. To get a feel for just how resilient the service is and how many disparate networks it has spanned over the decades, it\'s important to understand a bit about Usenet\'s history.

  --------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Year      Historical Context
  1970\'s   Relevant Prehistory
  1971      The first email is sent over the fledgling [ARPANET](https://en.wikipedia.org/wiki/ARPANET "wikipedia:ARPANET"), ancestor to the modern Internet. The first wireless packet radio network, [ALOHAnet](https://en.wikipedia.org/wiki/ALOHAnet "wikipedia:ALOHAnet"), comes online the same year.
  1975      ARPANET, deployed experimentally in 1969, is declared fully operational by the US Defense Department. Some prestigious US universities have access to ARPANET, most do not.
  1978      The world\'s first computerized [bulletin board system](https://en.wikipedia.org/wiki/Computerized_Bulletin_Board_System "wikipedia:Computerized Bulletin Board System") (BBS) is built in Chicago, Illinois is connected to the outside world via telephone land lines. UCB connects [Berknet](https://en.wikipedia.org/wiki/Berknet "wikipedia:Berknet") to ARPANET and UUCPNet the same year.
  1979      Two Duke University graduate students concieve of a \"Unix Users Network\" (Usenet) as a \"poor man\'s ARPANET.\"
  1980\'s   From Student Project to Global Network
  1980      The first public Usenet servers are deployed with [Unix-to-Unix Copy](https://wiki.gentoo.org/index.php?title=UUCP&action=edit&redlink=1 "UUCP (page does not exist)") (UUCP) and homemade 300-baud modems.
  1981      California at Berkeley joins Usenet and message traffic begins to pass between Usenet and ARPANET.
  1982      Usenet coverage spans the entire the North American continent for the first time.
  1983      The first [amateur radio](https://en.wikipedia.org/wiki/Amateur_radio "wikipedia:Amateur radio") (ham radio) packet network to Usenet gateway is established in New Jersey. The first European Usenet server appears in the Netherlands. The University of Sidney, Australia begins receiving a [weekly Airmail](https://article.olduse.net/467@sdchema.UUCP) of Usenet traffic dumped to magnetic tape. Richard Stallman [announces the GNU project](https://article.olduse.net/771@mit-eddie.UUCP).
  1984      [FidoNet](https://en.wikipedia.org/wiki/FidoNet "wikipedia:FidoNet") a decentralized system for passing messages among computer bulletin boards systems (BBSs) to share email (netmail) and forum posts (echomail) is created. It too is built around a delay tolerant design and a store-and-forward architecture conceptually similar to Usenet.
  1985      The total number of Usenet servers exceeds 1,000 for the first time. The FidoNet BBS node count reaches 600, it is now a global email network capable of supporting email and forum posts with file attachments. Some FidoNet nodes begin to gateway Usenet traffic via UUCP.
  1987      The (then few) high bandwidth Usenet servers push the \"[Great Renaming](https://en.wikipedia.org/wiki/Great_Renaming "wikipedia:Great Renaming")\" onto Usenet. The core [fa.\*] (from ARPANET), [mod.\*] (moderated), and [net.\*] (unmoderated) groups are migrated to [comp.\*], [misc.\*], [news.\*], [rec.\*], [sci.\*], [soc.\*], [talk.\*] and [alt.\*].
  1988      The total number of Usenet servers well exceeds 10,000 with 4Mbit/day in user traffic.
  1989      To the surprise of users in the West, Soviet Russia establishes an [Akademset](https://en.wikipedia.org/wiki/Akademset "wikipedia:Akademset") (Академсеть) network gateway to Usenet over [x.25](https://en.wikipedia.org/wiki/X.25 "wikipedia:X.25") links for the first time; China soon follows. The [Commodore 64](https://en.wikipedia.org/wiki/Commodore_64 "wikipedia:Commodore 64")-only pre-Internet online service [Quantum Link](https://en.wikipedia.org/wiki/Quantum_Link "wikipedia:Quantum Link") changes its name to [America Online](https://en.wikipedia.org/wiki/AOL "wikipedia:AOL") and begins its pivot towards the 32-bit PC and Mac market. This move will have an enormous impact on Usenet in the years to come.
  1990\'s   Eternal September, Flame Wars, and Spam
  1990      Usenet reaches its pre-World Wide Web peak of a maximum estimated user base of \~500,000 subscribers, mostly academics, scholars, journalists and other professionals. ARPANET ceases operation.
  1991      Tim Berners-Lee announces the World Wide Web on [[alt.hypertext](news:alt.hypertext) ([weblink](https://www.novabbs.com/devel/thread.php?group=alt.hypertext))], Linus Torvalds [announces Linux](https://groups.google.com/group/comp.os.minix/msg/b813d52cbc5a044b?dmode=source) on [[comp.os.minix](news:comp.os.minix) ([weblink](https://www.novabbs.com/devel/thread.php?group=comp.os.minix))] the same year.
  1992      Roughly 60% of Usenet traffic propagates over the Internet via the NNTP protocol UUCP traffic constitutes the remaining 40%. There was very likely some degree of overlap, some nodes are known to have encapsulated UUCP over TCP/IP.
  1993      [America Online](https://en.wikipedia.org/wiki/AOL "wikipedia:AOL") and other ISP\'s begin providing free Usenet access to their subscribers, [Eternal September](https://en.wikipedia.org/wiki/Eternal_September "wikipedia:Eternal September") begins.
  1994      With the influx of new users, the culture of Usenet begins to shift away from professionalism and polish. Flamewars begin, and spam begins to plague the network. The first known commercial SPAM message is sent, advertising legal services an (unrelated) deluge of spam hits Usenet later that same year. More spam follows, *a lot more*.
  1995      America Online shutters the last vestiges of its Quantum Link online service. The service would eventually be resurrected as [QuantumLink Reloaded](https://quantumlink.net/) by retrocomputing enthusiasts in the early 2010\'s.
  1996      The BBS email network FidoNet reaches its peak, the same year the Internet begins to go mainstream.
  1997      Usenet traffic between peers reaches 8Gbit/day.
  2000\'s   \"*Arrr ye matey!*\" --- Piracy Explodes, Regular Users Begin to Leave
  2001      The Bittorrent protocol is created, it sees heavy use among technologists and software/content pirates alike.
  2002      Gentoo Linux is announced.
  2003      Gentoo newsgroups [[alt.os.linux.gentoo](news:alt.os.linux.gentoo) ([weblink](https://www.novabbs.com/devel/thread.php?group=alt.os.linux.gentoo))] begins and [[linux.gentoo.user](news:linux.gentoo.user) ([weblink](https://www.novabbs.com/devel/thread.php?group=linux.gentoo.user))], etc. begin to see regular traffic.
  2006      In response to privacy and network throttling concerns, third party Usenet providers begin to transition from unencrypted NNTP to NNTP over TLS (NNTPS).
  2008      Facebook becomes the dominant centralized social media platform. PC Magazine declares Usenet dead. Google buys Deja News and [Google Groups](https://en.wikipedia.org/wiki/Google_Groups "wikipedia:Google Groups") begins acting as a Usenet archive and web-based front end.
  2009      Major ISP\'s begin to abandon free access to Usenet for their subscriber base, citing bandwidth concerns due to Tbit/day traffic required to keep the network in sync among other concerns.
  2010\'s   Major Technology Companies, ISP\'s Start Dropping Usenet
  2010      To evade peer-to-peer file sharing lawsuits, pirates begin shifting from BitTorrent, hastening ISP divestment. Paid Usenet service providers proliferate and text-only Usenet traffic begins to fall off.
  2013      Microsoft stops using passing traffic to [microsoft.\*] newsgroups. Gentoo mailing list traffic stops gating to Usenet, general support traffic remains on [[alt.os.linux.gentoo](news:alt.os.linux.gentoo) ([weblink](https://www.novabbs.com/devel/thread.php?group=alt.os.linux.gentoo))].
  2020\'s   Discontent with Centralized Social Media Grows
  2020      Several open source decentralized social networks, begun in the previous decade, see traction outside of the technology community. After a long period of dormancy, [Big 8](https://www.big-8.org) board is reestablished.
  2022      Discontent with Twitter drives many users to [Mastodon](https://en.wikipedia.org/wiki/Mastodon_(social_network) "wikipedia:Mastodon (social network)") and other federated alternatives collectively known as the [Fediverse](https://en.wikipedia.org/wiki/Fediverse "wikipedia:Fediverse"). Usenet traffic reaches an average of 172Tbit/day among full nodes.
  2023      Discontent with [Reddit](https://en.wikipedia.org/wiki/Reddit "wikipedia:Reddit") causes some users to explore Usenet as a decentralized alternative, text-only Usenet providers see a modest increase subscribers. The first new newsgroup in the Big 8 hierarchy in many years is established: [[comp.infosystems.gemini](news:comp.infosystems.gemini) ([weblink](https://www.novabbs.com/devel/thread.php?group=comp.infosystems.gemini))] which is soon followed by newsgroups for the [Rust](https://wiki.gentoo.org/wiki/Rust "Rust") and [Go](https://wiki.gentoo.org/wiki/Go "Go") programming languages.
  --------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## [Troubleshooting]

### [][How do I get a Usenet account?]

A good first step is to contact your ISP. Though not as common as it once as, some ISP\'s still offer their subscribers free access to Usenet. The more subscribers that use their own ISP\'s Usenet infrastructure the more incentive the ISP has to maintain it.

If that fails, the Big 8 provides a list of major [Usenet Service Providers](https://www.big-8.org/wiki/News_service_providers). Some are free text-only providers while others cost money but offer unfettered access to Usenet, including binaries groups. Additionally, the [r/usenet](https://reddit.com/r/usenet) subreddit maintains a large and [heavily annotated list of providers](https://www.reddit.com/r/usenet/wiki/providers/) on their wiki. This list can be especially useful if geographic proximity to the Usenet provider is desirable.

As a last ditch effort, new Usenet providers advertise themselves on [[alt.free.newsservers](news:alt.free.newsservers) ([weblink](https://www.novabbs.com/devel/thread.php?group=alt.free.newsservers))] fairly regularly. Your mileage may vary with these providers.

### [][How do I propose a new Usenet newsgroup?]

Start a Request for Discussion (RFD) on [[news.groups.proposals](news:news.groups.proposals) ([weblink](https://www.novabbs.com/devel/thread.php?group=news.groups.proposals))] containing the following:

-   Proposed Newsgroup name.
-   A checkgroups file entry.
-   Moderation status.
-   If moderated, the email address of at least one moderator.

There are numerous existing Requests for Discussion in that group which can be used as a template to formulate a new request.

### [][How do I run a local Usenet server?]

First, if all you want to do is have your own NNTP server and your own set of newsgroups separate from the Usenet network that is entirely viable and is referred to as a private NetNews server. Many institutions have (or once had) just such an NNTP server configuration. The package, [[[net-nntp/leafnode]](https://packages.gentoo.org/packages/net-nntp/leafnode)[]] is a popular option for setups like this. In a private NetNews deployment, internal NNTP servers may peer with themselves for redundancy, but no external peering arrangement is made with the global Usenet infrastructure.

Second, understand that peering with Usenet is different than configuring a newsreader. A newsreader only uses tiny amounts of bandwidth to send and receive Usenet posts. A netnews server configured to mirror the whole of Usenet will consume mind-boggling amounts of bandwidth and storage, on the order of nearly 200Tbit/day! That\'s not a bandwidth bill most people can afford, so be careful.

Assuming you\'re configuring a text-only Usenet server:

The first thing you\'ll want to do is configure your netnews server to reject binaries groups in order to make the bandwidth manageable. At a *bare minimum* this means blocking groups with the word [binaries] in the path. Some text only providers block the top level [alt] hierarchy as well, on account of its reputation for spam but others do not.

Alternatively, if your server supports it, consider a whitelisting approach. Eternal September maintains a known-good list of [text-only hierarchies](https://www.eternal-september.org/hierarchies.php). Even so, at least a few binary posts are likely to slip through. Depending upon the sophistication of your netnews server you may also be able to filter content at the message level. There are filters that drop messages containing UUE, MIME, BASE64, or yENC encoded payloads.

That done, you\'ll want to post a message to [[news.admin.peering](news:news.admin.peering) ([weblink](https://www.novabbs.com/devel/thread.php?group=news.admin.peering))] requesting peers. If you\'re a *leaf node* --- you do not intend to allow others connect to your server for the purpose of bulk message transfer --- you\'ll want to specify that in your message.

Most likely, you\'ll get several responses. The two most common ports for the bulk transfer of Usenet traffic are tcp/433 (NNSP) for clear text message transfer and tcp/563 (NNSPS) for TLS encrypted message transfer.

### [][How do I link to Usenet or other Netnews Service from the Web?]

Hyperlinks to Netnews are valid *href* tags in (x)HTML. The protocol indicator for Netnews is simply **[news:]** by itself, this is a widely supported RFC standard not a custom protocol handler. To link to Usenet simply follow the colon with a newsgroup name or a message ID. Note: as we\'re not specifying a specific server that should provide access to the content a [//] does NOT follow the colon.

***HTML to Hyperlinks Directly to Usenet***

-   To link to Usenet newsgroup via hyperlink the link syntax is: [news:\<dotted.group.name\>]. The web browser will launch the user\'s default Newsreader and show the contents of the specified newsgroup.
-   To link to specific Usenet post via hyperlink the link syntax is: [news:\<message_id\>]. The web browser will launch the user\'s default Newsreader and show the contents of the specified message. This value is taken from the `Message-ID:` entry in a Usenet\'s message\'s header.

***HTML and Links to a Specific Netnews Server***

Private Netnews servers that do not federate with the wider Usenet exist. There are often internal Netnews servers belonging to large institutions, most commonly academic ones. This is not unusual, it\'s no different from a large organization hosting its own internal email infrastructure with limits on what messages may pass to or from the outside world.

-   To link to newsgroup on a specific netnews server via hyperlink the link syntax is: [nntp://\<hostname\>\[\<:port\>\]/\<groupname\>]. the web browser will launch the user\'s default Newsreader and show the contents of the specified newsgroup.
-   To link to a specific message within a newsgroup on a specific netnews server via hyperlink the link syntax is: [nntp://\<hostname\>\[\<:port\>\]/\<groupname\>/\<message-id\>]. The web browser will launch the user\'s default Newsreader and show the contents of the specified newsgroup. The use of [news://] is valid in place of [nntp], because a specific server is specified.

Unfortunately, most browsers do not support [nntps://] as clickable hyperlinks. Newsreaders themselves typically default to NNTP over TLS, so it\'s not much of a security issue anymore. Alternatively, the use of [news://] is valid in place of [nntp://], because a specific server is specified.

***HTML to Hyperlinks a Usenet Archive on the Web***

Several large archives of Usenet messages exist, some of them going all the way back to 1980! Unfortunately no Usenet archive is anywhere near 100% complete. Every single Usenet web portal has issues. No one could have anticipated the historical significance of this content. The most common issues are:

1.  The archive only covers a specific time period.
2.  The content is archived but not easily searchable.
3.  There are gaps in the archive\'s content.
4.  The archive may not be in sync with modern Usenet.
5.  The archive may only be partially in sync modern Usenet, messages may simply seem to stop.

***Google Groups Usenet Archive***

** Note**\
Google has advised: \"Effective February 22, 2024, Google Groups will no longer support new Usenet content. Posting and subscribing will be disallowed, and new content from Usenet peers will not appear. Viewing and searching of historical data will still be supported as it is done today.\"

[Google Groups](https://groups.google.com) federates with Usenet. It has both current and historical content. Because it is live and anyone with a Google account can contribute this is what the `}` template links to. The link structure has changed several times over the years and it\'s a bit different than other providers:

-   To link to a specific Usenet newsgroup: [https://groups.google.com/g/*\<usenet.newsgroup.name\>*].
-   To link to a specific thread within a newsgroup: [https://groups.google.com/g/*\<usenet.newsgroup.name\>*/c/*\<message-first-message-in-thread\>*].
-   To link to a specific reply within a newsgroup thread: [https://groups.google.com/g/*\<usenet.newsgroup.name\>*/c/*\<message-first-message-in-thread\>*/m/*\<message-id-of-specific-reply\>*].

While it\'s much easier to find live Usenet content via the Google Groups web interface, it\'s not really possible to see Usenet\'s message\'s full header. Changes its URL structure every few years making long-term links directly to messages problematic. Also, Google has been known to be somewhat heavy-handed in blocking content to some groups for spam or other content issues. There is an [appeals process](https://support.google.com/a/thread/7543247/accessing-a-newsgroup-that-has-been-blocked?hl=en) if a Usenet group has been blocked from view by the Google groups portal. Google blocking a Usenet group from its portal has no effect on the Usenet network itself. A real Usenet reader will be able to access a blocked group without issue.

***Usenet Archives.com***

[Usenet Archives.com](https://www.usenetarchives.com/) is large and easy to link to. This is what the `}` template used to link to. Its archive goes all the way back to 1979/1970 but there gaps in content coverage. The web interfaces does a very good job of using CSS typography which makes the content quite readable on modern devices. The problem is new content is very hit-and-miss. Many groups just seem to stop around 2013 or so.

-   To link to a specific newsgroup: [https://www.usenetarchives.com/threads.php?id=*\<usenet.newsgroup.name\>*].
-   To link to a specific post: [https://www.usenetarchives.com/view.php?id=*\<usenet.newsgroup.name\>*&mid=*\<message_id\>*].

***Olduse.net***

[Olduse.net](https://olduse.net) is as much interactive art project as it is historical archive. The site archives only the first 10 years of Usenet\'s history. It\'s primarily intended to allow people to experience Usenet on \"tape delay\" decades back. The site loosely simulates a [VT220](https://en.wikipedia.org/wiki/VT220 "wikipedia:VT220") terminal\'s look in feel via careful font selection and CSS. It\'s possible to link directly to a post within the archive\'s time period. The syntax is: [https://article.olduse.net/*\<message_id\>*].

***Archive.org***

Archive.org has a large collection of [Usenet archives](https://archive.org/details/usenet). Most of these are in [[.mbox](https://en.wikipedia.org/wiki/Mbox "wikipedia:Mbox")] format. These collections aren\'t directly searchable or likable. Taken together (and sufficiently de-duplicated) these could be used to build a new purpose-built Usenet archive.

### [Someone insulted me on Usenet]

You\'ll live. Usenet is technically censorship resistant and culturally very much in favor of freedom of speech and expression.

### [][How do I set fonts or insert emojis?]

Usenet messages are plain text, just like email was originally. Some graphical newsreaders have rendering engines that can do a beautify the typography of the message, but it\'s still text.

Emoticons can be inserted manually if they exist in the [emoticons Unicode block](https://en.wikipedia.org/wiki/Emoticons_(Unicode_block) "wikipedia:Emoticons (Unicode block)"). While all modern newsreaders support Unicode, these may or may not render appropriately due to font issues or the like. The best solution is to use [well-known ASCII emoticons](https://en.wikipedia.org/wiki/List_of_emoticons "wikipedia:List of emoticons").

### [][What\'s with all the \"dead\" Newsgroups?]

First, web-based portals into Usenet are incomplete. This is true of any *historical* Usenet archive. Unfortunately, this includes [UsenetArchives.com](https://usenetarchives.com/), which provides `}` with its weblink functionality. The only way to get an accurate live picture of Usenet is to get a Usenet account somewhere and look around with a real Newsreader.

Second, once a newsgroup is established it\'s rarely if ever pruned from the hierarchy. Groups with no new content in them aren\'t really dead though. Anyone with a Usenet account can post to the majority of groups at any time. Throughout its history Usenet has seen many newsgroups go dormant only to later revive. More than one group has been restarted simply by posting new content. It\'s impossible to see who might be subscribed and might be willing to reply to new questions.

Third, there are a number of moderated groups that have lost all of their moderators. In practice, this means that it is no longer possible to post new content to such groups. Sometimes these groups remain visible with Usenet providers \"frozen in time\" indefinitely. Other providers may drop the group after a *very* long period of inactivity, typically on the order of a decade or more.

Forth, it should be noted that --- while difficult --- it\'s not impossible to revive a moderated group that has been abandoned. The Big 8 has a [Changing the Moderation Status of Existing Groups](https://www.big-8.org/wiki/Changing_the_Moderation_Status_of_Existing_Groups) procedure document. The moderated group would either need new moderators --- nearly always from the existing contributors --- or it would need to become unmoderated. Once the migration to a new moderation status is approved and implemented new content can flow to the formerly abandoned group.

### [][How do I become a Usenet newsgroup moderator?]

The [*NetNews Moderator\'s Handbook*](https://web.archive.org/web/20080510141028/http://www.landfield.com/usenet/moderators/handbook/modtoc.html) is considered the go-to document for understanding Usenet moderation.

Additionally, the much shorter [*Pitfalls of Newsgroup Moderation*](https://www.eyrie.org/~eagle/faqs/mod-pitfalls.html) includes a lot of information most Usenet moderators wished the knew before they started.

### [][How do I get an authoritative list of ALL Usenet Newsgroups?]

It doesn\'t exist.

The [Internet Systems Consortium](https://www.isc.org/) (ISC) maintains a [newsgroup list](https://downloads.isc.org/pub/usenet/CONFIG/newsgroups.bz2). In theory, this list should constitute the entirety of Usenet\'s newsgroup hierarchy. In practice, Usenet providers often filter out groups for a number of reasons, including but not limited to:

1.  The newsgroup is known to contain excessive amounts of spam.
2.  A moderated newsgroup has lost all of its moderators, so no new content can be posted to the group.
3.  The newsgroup contains excessive amounts of binary data which can cause bandwidth issues for the Usenet provider.
4.  The newsgroup has reputation for containing content that is illegal in the jurisdiction of the Usenet provider.
5.  The newsgroup may be local to a specific Usenet server instance.

### [][Are there mobile Usenet newsreaders for smartphones and tablets?]

Every so often a newsreader will get pushed to an app store only to quickly get abandoned; none are open source. Those few mobile newsreaders that do exist are inevitably low quality and focus on Usenet as a source for pirated content. This is an unfortunate state of affairs.

If you have mobile development skills, you are absolutely encouraged to produce a quality open source Usenet newsreader reader. The market exists, it\'s just not a huge market at present. Given the increased push for a return to a more decentralized Internet, releasing a high quality open source mobile newsreader might change all that.

A few people have been known to use [termux](https://termux.dev/en/) to accomplish this. Basically, this amounts to launching the termux terminal on and Android device and using it to connect to a remote Linux machine via SSH, and then running a newsreader remotely. This results in a suboptimal experience to put it lightly. A tablet user might not have too much difficulty, but a smartphone user will no doubt find the amount of pinch-zooming required to get through even a single message to be quite aggravating.

### [][Is Usenet part of the Fediverse?]

Technically, no; but that will probably change.

\"The [Fediverse](https://en.wikipedia.org/wiki/Fediverse "wikipedia:Fediverse")\" isn\'t simply slang for any federated social network. To be considered part of the Fediverse a node must either communicate via the [ActivityPub](https://en.wikipedia.org/wiki/ActivityPub "wikipedia:ActivityPub") protocol natively or pass messages to and from its native protocol and ActivityPub.

By that definition, Usenet is not part of the Fediverse\... at least not yet.

That seems to be changing for two reasons:

1.  [Illuminant](https://illuminant.asjo.org/) is an ActivityPub-NNTP gateway server that communicates wtih NetNews clients over NNTP locally, but all remote peers are ActivityPub instances. Thus, anyone with a NetNews client can participate in the Fediverse but traffic is not passed between the Fediverse and Usenet directly or indirectly.
2.  There is active discussion underway about the possibility of ActivityPub federating with Usenet in support of the Reddit-clone [Lemmy](https://join-lemmy.org/). See [ActivityPub Should Support Federating with Usenet](https://codeberg.org/fediverse/fediverse-ideas/issues/46).

Most likely Usenet will become part of the Fediverse eventually.

## [See also]

-   [Email](https://wiki.gentoo.org/wiki/Email "Email") --- a federated protocol for sending and receiving long-form electronic mail messages and documents over a computer network.
-   [Fediverse](https://wiki.gentoo.org/wiki/Fediverse "Fediverse") --- a federated and decentralized worldwide Internet-based social network built upon the [ActivityPub](https://en.wikipedia.org/wiki/ActivityPub "wikipedia:ActivityPub") protocol.
-   [Gemini](https://wiki.gentoo.org/wiki/Gemini "Gemini") --- a lightweight application-layer Internet protocol for accessing remote documents.
-   [I2P](https://wiki.gentoo.org/wiki/I2P "I2P") --- an anonymous network, similar to [Tor](https://wiki.gentoo.org/wiki/Tor "Tor").
-   [News feed](https://wiki.gentoo.org/wiki/News_feed "News feed") --- a computer-readable data format for content updates.
-   [Terminal productivity software](https://wiki.gentoo.org/wiki/Terminal_productivity_software "Terminal productivity software") --- applications designed to run within the constraints of a text-based terminal window that are typically associated with GUI-based office productivity software
-   [Tor](https://wiki.gentoo.org/wiki/Tor "Tor") --- an onion routing Internet anonymity system.

## [External resources]

-   [*NetNews Moderator\'s Handbook*](https://web.archive.org/web/20080510141028/http://www.landfield.com/usenet/moderators/handbook/modtoc.html)
-   [*Pitfalls of Newsgroup Moderation*](https://www.eyrie.org/~eagle/faqs/mod-pitfalls.html).
-   [Telehack a web-based ARPANET simulator](https://telehack.com/) with historical Usenet archives.
-   [Usenet Archives](https://www.usenetarchives.com/) a searchable Usenet archive with messages as far back as 1980 that also occasionally includes some recent Usenet traffic.
-   [Big 8 Wiki: Usenet Service Providers](https://www.big-8.org/wiki/News_service_providers)
-   [Rocksolid Light](https://gitlab.com/rslight-public/rocksolid-light) a web based newsreader with a [PHPBB](https://www.phpbb.com/) look and feel with [NovaBBS](https://www.novabbs.com/) being it\'s most well-known instance.
-   [Olduse.net](https://olduse.net/) --- interactive art that replays Usenet messages in a web browser from the first 10 years of the network\'s existence. The page is designed to resemble a CRT terminal with a phosphor display.
-   [Protocols, Not Platforms: A Technological Approach to Free Speech](https://knightcolumbia.org/content/protocols-not-platforms-a-technological-approach-to-free-speech) --- an influential article that helped spur the modern decentralized social media phenomenon.
-   [Usenet, the OG social network, rises again like a text-only phoenix](https://www.theregister.com/2023/08/30/usenet_revival/) --- a 2023 article on Usenet\'s recent resurgence.