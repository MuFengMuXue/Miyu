This page contains [[changes](https://wiki.gentoo.org/index.php?title=Email&diff=1415629)] which are not marked for translation.

**Resources**

[[]][[#email](ircs://irc.libera.chat/#email)] ([[webchat](https://web.libera.chat/#email)])

[[]][[alt.comp.apps.email](news:alt.comp.apps.email) ([weblink](https://www.novabbs.com/devel/thread.php?group=alt.comp.apps.email))]

[[]][r/email](https://reddit.com/r/email)

[[]][r/selfhosted](https://reddit.com/r/selfhosted)

**Email** (sometimes **E-Mail**) is a federated protocol for sending and receiving long-form electronic mail messages and documents over a computer network. The first email message was sent via [SNDMSG] in 1971 over the fledgling ARPANET network, the historical antecedent to the Internet. At that time ARPANET was a closed system; email did not gate to other networks. Somewhat later, in 1979, the Unix-to-Unix Copy ([UUCP](https://wiki.gentoo.org/index.php?title=UUCP&action=edit&redlink=1 "UUCP (page does not exist)")) network was created as a means to link all Unix users together over a common medium. This network permitted the open exchange of email and files between users. It wasn\'t until until 1983 when UUCP was connected to ARPANET that either network gated to anywhere outside their own networks. It was this interconnectivity between ARPANET and UUCPNET that was a major factor in the rise of the decentralized social media network [Usenet](https://wiki.gentoo.org/wiki/Usenet "Usenet") that persists to this day. Even so, from the 1970\'s through to the early 1980\'s proprietary email-like messaging systems were somewhat common in large network installations. Even [bulletin board system](https://en.wikipedia.org/wiki/Bulletin_board_system "wikipedia:Bulletin board system") SysOps (administrators) got into the email game with FidoNet in 1983.

Modern email networks chiefly rely on a set of standard protocols for communications, primarily Simple Mail Transfer Protocol (SMTP) for sending email and Internet Message Access Protocol (IMAP) receiving it. During the dial-up era Post Office Protocol (POP3) was a common protocol for receiving email from a server but suffered from limitations and was displaced by IMAP.

Additionally, proprietary Microsoft non-standards for email message exchange exist but are little used outside of the Windows and Microsoft Exchange world: Messaging Application Programming Interface (MAPI) and Exchange Web Services (EWS) the newer one. The latter is set to displace the former.

## Contents

-   [[1] [Email Software on Gentoo]](#Email_Software_on_Gentoo)
    -   [[1.1] [Email Terminology]](#Email_Terminology)
    -   [[1.2] [A Brief History of Email]](#A_Brief_History_of_Email)
-   [[2] [Understanding How Email Works]](#Understanding_How_Email_Works)
    -   [[2.1] [Anti-spam measures affecting sending of email]](#Anti-spam_measures_affecting_sending_of_email)
-   [[3] [Email Delivery Protocols]](#Email_Delivery_Protocols)
    -   [[3.1] [SMTP]](#SMTP)
-   [[4] [Email Retrieval Protocols]](#Email_Retrieval_Protocols)
    -   [[4.1] [POP3]](#POP3)
    -   [[4.2] [IMAP]](#IMAP)
-   [[5] [Less Common Email Protocols]](#Less_Common_Email_Protocols)
    -   [[5.1] [Protocols Extended from SMTP]](#Protocols_Extended_from_SMTP)
        -   [[5.1.1] [Proton Mail]](#Proton_Mail)
        -   [[5.1.2] [Winlink]](#Winlink)
    -   [[5.2] [Non-SMTP Dervied Protocols]](#Non-SMTP_Dervied_Protocols)
        -   [[5.2.1] [FidoNet]](#FidoNet)
        -   [[5.2.2] [Packet Mail]](#Packet_Mail)
        -   [[5.2.3] [UUCP]](#UUCP)
-   [[6] [Commonly Gated or Bridged Protocols]](#Commonly_Gated_or_Bridged_Protocols)
    -   [[6.1] [Git]](#Git)
    -   [[6.2] [Network News Transfer Protocol (NNTP)]](#Network_News_Transfer_Protocol_.28NNTP.29)
    -   [[6.3] [Short Message Service (SMS) Text]](#Short_Message_Service_.28SMS.29_Text)
-   [[7] [Attachments]](#Attachments)
    -   [[7.1] [Uuencoding]](#Uuencoding)
    -   [[7.2] [MIME]](#MIME)
-   [[8] [Encryption]](#Encryption)
    -   [[8.1] [TLS]](#TLS)
    -   [[8.2] [PGP]](#PGP)
-   [[9] [Troubleshooting]](#Troubleshooting)
-   [[10] [See also]](#See_also)
-   [[11] [External resources]](#External_resources)
-   [[12] [References]](#References)

## [Email Software on Gentoo]

  ----------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Name                                                        Package                                                                                                                                                                                                                                                                                                                                                                                                   Description
  Email Clients
  [aerc](https://wiki.gentoo.org/wiki/Aerc "Aerc")            [[[mail-client/aerc]](https://packages.gentoo.org/packages/mail-client/aerc)[]]                                    Email client for your terminal.
  alot                                                        [[[mail-client/alot]](https://packages.gentoo.org/packages/mail-client/alot)[]]                                    Experimental terminal UI for [[[net-mail/notmuch]](https://packages.gentoo.org/packages/net-mail/notmuch)[]] written in Python.
  alpine                                                      [[[mail-client/alpine]](https://packages.gentoo.org/packages/mail-client/alpine)[]]                              An easy to use text-based based mail and news client.
  balsa                                                       [[[mail-client/balsa]](https://packages.gentoo.org/packages/mail-client/balsa)[]]                                 Email client for GNOME.
  bower                                                       [[[mail-client/bower]](https://packages.gentoo.org/packages/mail-client/bower)[]]                                 Curses terminal client for the Notmuch email system.
  clawsker                                                    [[[mail-client/clawsker]](https://packages.gentoo.org/packages/mail-client/clawsker)[]]                        Applet to edit Claws Mail\'s hidden preferences.
  claws-mail                                                  [[[mail-client/claws-mail]](https://packages.gentoo.org/packages/mail-client/claws-mail)[]]                  An email client (and news reader) based on GTK+.
  evolution                                                   [[[mail-client/evolution]](https://packages.gentoo.org/packages/mail-client/evolution)[]]                     Integrated mail, address book and calendaring functionality.
  geary                                                       [[[mail-client/geary]](https://packages.gentoo.org/packages/mail-client/geary)[]]                                 A lightweight, easy-to-use, feature-rich email client.
  hap                                                         [[[mail-client/hap]](https://packages.gentoo.org/packages/mail-client/hap)[]]                                       A terminal mail notification program (replacement for [biff]).
  kube                                                        [[[mail-client/kube]](https://packages.gentoo.org/packages/mail-client/kube)[]]                                    Mail client based on KDE Frameworks.
  mailx                                                       [[[mail-client/mailx]](https://packages.gentoo.org/packages/mail-client/mailx)[]]                                 A terminal-based mail program, which is used to send mail via shell scripts.
  mailx-support                                               [[[mail-client/mailx-support]](https://packages.gentoo.org/packages/mail-client/mailx-support)[]]         Provides lockspool utility.
  [mutt](https://wiki.gentoo.org/wiki/Mutt "Mutt")            [[[mail-client/mutt]](https://packages.gentoo.org/packages/mail-client/mutt)[]]                                    A small but very powerful text-based mail client.
  mutt-wizard                                                 [[[mail-client/mutt-wizard]](https://packages.gentoo.org/packages/mail-client/mutt-wizard)[]]               A system for automatically configuring neomutt and isync.
  [neomutt](https://wiki.gentoo.org/wiki/Mutt "Mutt")         [[[mail-client/neomutt]](https://packages.gentoo.org/packages/mail-client/neomutt)[]]                           A small but very powerful text-based mail client.
  roundcube                                                   [[[mail-client/roundcube]](https://packages.gentoo.org/packages/mail-client/roundcube)[]]                     A browser-based multilingual IMAP client with an application-like user interface.
  s-nail                                                      [[[mail-client/s-nail]](https://packages.gentoo.org/packages/mail-client/s-nail)[]]                              Enhanced mailx-compatible mail client based on Heirloom mailx (nail).
  thunderbird                                                 [[[mail-client/thunderbird]](https://packages.gentoo.org/packages/mail-client/thunderbird)[]]               Thunderbird Mail Client.
  thunderbird-bin                                             [[[mail-client/thunderbird-bin]](https://packages.gentoo.org/packages/mail-client/thunderbird-bin)[]]   Thunderbird Mail Client (binary).
  Email Servers (MTA\'s)
  courier                                                     [[[mail-mta/courier]](https://packages.gentoo.org/packages/mail-mta/courier)[]]                                    An MTA designed specifically for maildirs.
  esmtp                                                       [[[mail-mta/esmtp]](https://packages.gentoo.org/packages/mail-mta/esmtp)[]]                                          User configurable relay-only Mail Transfer Agent with a sendmail-like syntax.
  exim                                                        [[[mail-mta/exim]](https://packages.gentoo.org/packages/mail-mta/exim)[]]                                             A highly configurable, drop-in replacement for sendmail.
  msmtp                                                       [[[mail-mta/msmtp]](https://packages.gentoo.org/packages/mail-mta/msmtp)[]]                                          An SMTP client and SMTP plugin for mail user agents such as Mutt.
  netqmail                                                    [[[mail-mta/netqmail]](https://packages.gentoo.org/packages/mail-mta/netqmail)[]]                                 qmail --- a secure, reliable, efficient, simple message transfer agent.
  notqmail                                                    [[[mail-mta/notqmail]](https://packages.gentoo.org/packages/mail-mta/notqmail)[]]                                 Collaborative open-source successor to qmail.
  nullmailer                                                  [[[mail-mta/nullmailer]](https://packages.gentoo.org/packages/mail-mta/nullmailer)[]]                           Simple relay-only local mail transport agent.
  opensmtpd                                                   [[[mail-mta/opensmtpd]](https://packages.gentoo.org/packages/mail-mta/opensmtpd)[]]                              Lightweight but featured SMTP daemon from OpenBSD.
  [postfix](https://wiki.gentoo.org/wiki/Postfix "Postfix")   [[[mail-mta/postfix]](https://packages.gentoo.org/packages/mail-mta/postfix)[]]                                    A fast and secure drop-in replacement for sendmail.
  proton-mail-bridge                                          [[[mail-mta/proton-mail-bridge]](https://packages.gentoo.org/packages/mail-mta/proton-mail-bridge)[]]   Serves ProtonMail to IMAP/SMTP clients.
  qpsmtpd                                                     [[[mail-mta/qpsmtpd]](https://packages.gentoo.org/packages/mail-mta/qpsmtpd)[]]                                    qpsmtpd is a flexible smtpd daemon written in Perl.
  sendmail                                                    [[[mail-mta/sendmail]](https://packages.gentoo.org/packages/mail-mta/sendmail)[]]                                 Widely-used Mail Transport Agent (MTA).
  ssmtp                                                       [[[mail-mta/ssmtp]](https://packages.gentoo.org/packages/mail-mta/ssmtp)[]]                                          Extremely simple MTA to get mail off the system to a Mailhub.
  Exotic Email Servers
  serialmail                                                  [[[net-mail/serialmail]](https://packages.gentoo.org/packages/net-mail/serialmail)[]]                           A serialmail is a collection of tools for passing mail across serial links.
  taylor-uucp                                                 [[[net-misc/taylor-uucp]](https://packages.gentoo.org/packages/net-misc/taylor-uucp)[]]                        Taylor UUCP protocol stack, typically for routing messages over serial lines or radio links.
  Additional Email Security Tools
  clamav                                                      [[[app-antivirus/clamav]](https://packages.gentoo.org/packages/app-antivirus/clamav)[]]                        Clam Anti-Virus Scanner.
  gnupg                                                       [[[app-crypt/gnupg]](https://packages.gentoo.org/packages/app-crypt/gnupg)[]]                                       The GNU Privacy Guard, a GPL OpenPGP implementation.
  pius                                                        [[[app-crypt/pius]](https://packages.gentoo.org/packages/app-crypt/pius)[]]                                          A tool for signing and emailing all UIDs on a set of PGP keys.
  stunnel                                                     [[[net-misc/stunnel]](https://packages.gentoo.org/packages/net-misc/stunnel)[]]                                    A TLS/SSL Port Wrapper.
  tor                                                         [[[net-vpn/tor]](https://packages.gentoo.org/packages/net-vpn/tor)[]]                                                   Anonymizing overlay network for TCP.
  ----------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [Email Terminology]

-   *EWS* --- Exchange Web Services Microsoft\'s non-standard alternative communications protocol for communicating with Microsoft Exchange Servers in lieu of IMAP. EWS is a SOAP-based XML protocol.
-   *Email Attachment* --- a binary file encoded as text and appended to the body of an email message. Typical encoding schemes include Unix-to-Unix Encoding and MIME.
-   *Email Client* --- end user software used to access an email account. See also MUA.
-   *Email Server* --- server-side software used to receive and store email messages on behalf of a recipient.
-   *Email Spoofing* --- the practice of forging email headers, typically to misrepresent the sender of the message.
-   *Federation* --- a protocol architecture that allows multiple independent implementations over disparate networks to communicate.
-   *GPG* --- GNU Privacy Guard an implementation of the OpenPGP standard.
-   *IMAP* --- Internet Message Access Protocol the dominant protocol for receiving email over persistent Internet connections. Typically, messages stay resident server-side.
-   *MAPI* --- Messaging Application Programming Interface Microsoft\'s non-standard communications protocol for communicating with Exchange Servers.
-   *MBOX* --- a plain text file format for storing electronic mail and Usenet messages.
-   *MDA* --- Mail Delivery Agent: The mail server component that accepts email on behalf of the recipient and places it in the recipient\'s mailbox.
-   *MSA* --- Mail Submission Agent: the email server component that accepts initial receipt of an email from the Mail User Agent.
-   *MTA* --- Mail Transfer Agent: the email server component that transfers or relays email the email server on the intended recipient\'s domain.
-   *MUA* --- Mail User Agent: user facing software for the composition and initial transmission or final delivery of an email.
-   *PGP* --- Pretty Good Privacy: a standard for encrypting the content of email messages in transit and at rest. As an unavoidable technical limitations headers --- which can be used to infer who is communicating with whom --- cannot be encrypted.
-   *POP3* --- Post Office Protocol version 3, a email drop protocol typically used for retrieving email over intermittent data links. Typically the emails are deleted server-side after delivery.
-   *Phishing* --- email with a malicious link or payload intended to compromise the recipient\'s system for a malicious purpose.
-   *Plain Text Email* --- Email composed entirely of ASCII characters or Unicode glyphs and absent any markup language.
-   *Rich Text Email* --- an email body composed of HTML.
-   *SMIME* --- Secure/Multipurpose Internet Mail Extensions is a standard for signing and encrypting MIME data in transit and at rest. As an unavoidable technical limitations headers --- which can be used to infer who is communicating with whom --- cannot be encrypted.
-   *SMTP* --- Simple Mail Transfer Protocol the predominant email transmission protocol.
-   *Self-Hosting* --- The difficult but not impossible task of operating one\'s own *personal* email server infrastructure independent of a third party provider.
-   *Spam* --- unsolicited email of a commercial nature.
-   *Spear Phishing* --- email with a malicious link or payload intended to compromise *a targeted individual\'s* system for a malicious purpose.
-   *TLS* --- Transport Layer Security: a means of securing email from prying eyes or modification in transit.
-   *Tracking Pixel* --- the use of uniquely named embedded images to track the behavior of an email recipient\'s behavior either for marketing or malicious purposes.
-   *[Usenet](https://wiki.gentoo.org/wiki/Usenet "Usenet")* --- the distributed message store and social network \"cousin\" of Email.

### [A Brief History of Email]

Email as a technology is surprisingly old. It predates the modern Internet and shares a lot of history with the [Usenet](https://wiki.gentoo.org/wiki/Usenet "Usenet") social network. Indeed, the modern SNMP protocol and Usenet\'s NNTP protocol are similar if far from identical.

At its heart, email is a text-only protocol with additional technologies grafted onto it. The first emails were text only and assumed a roughly 80×25 screen for all users. This disadvantaged some very early home computer users who had systems that were only capable of 40×25 (or worse) except on services that specifically catered to such users. Users often did not stay connected to electronic networks indefinitely, this was prohibitively expensive: early pre-Internet online services charged by the minute in addition to any long distance calling charges dial-up users would incur.

Thus messages were composed offline and later sent in bulk, often in the middle of the night when telephone rates were less expensive. As email messages were basically long-form text messages that roughly corresponded to handwritten letters in length, even slow dial-up modems could transfer messages at reasonable speeds. The now ubiquitous email attachment originated as a hack but this usage quickly spread resulting in much longer connection times to send or receive some messages.

Eventually, large corporate email networks evolved. These were \"always on\" --- but had the twin disadvantages of not reaching users that were out of the office and occasionally experiencing significant message handling delays when communicating with external networks. Improvements in underlying infrastructure eventually made email transmission delays far less common. The rise of the smartphone meant that email could reach just about anyone at any time, fundamentally changing the way people related to the once niche service.

  --------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  1970\'s   Humble Beginnings
  1971      [SNDMSG] an experimental message and file transfer command was used by Ray Tomlinson to send the first email over ARPANET, the Internet\'s historical antecedent.
  1972      The UNIX mail program was developed.
  1978      The pre-Internet online service CompuServe begins offering an electronic interoffice memo service; the first computerized builitin board systems (BBS) were built. The first known spam email is sent over ARPANET.
  1979      [delivermail] the predecessor to [sendmail] shipped with BSD 4.0. Unix-to-Unix Copy (UUCP) is developed for email over telephone lines and serial links.
  1980\'s   Early Dial-Up Era and Electronic Builtin Boards
  1980      SMTP (Simple Mail Transfer Protocol) was proposed but not implemented. The distributed message board [Usenet](https://wiki.gentoo.org/wiki/Usenet "Usenet") was deployed, it remains the oldest electronic social network and much of its history parallel\'s that of electronic mail.
  1981      CompuServe attempts to trademark the term EMAIL but abandons the application.
  1983      SMTP (Simple Mail Transfer Protocol) was first implemented, it would eventually become the dominant email messaging standard.
  1984      FidoNet is released, allowing BBS systems to send email. The network slowly goes global. The Post Office Protocol (POP) protocol was developed to enable dial up users to briefly connect to a mail-drop server to retrieve messages in bulk and disconnect.
  1985      Quantum Link (or Q-Link) launches providing pre-Internet online services, including email services tailored to 40×25 displays, for Commodore 64 and Commodore 128 users. *Habitat*, the first massively multiplayer online role-playing game (MMORPG) would see a beta release on the platform the following year.
  1988      The Internet Message Access Protocol (IMAP) protocol was developed, it would eventually supersede POP --- by then POP3 --- for most applications. Microsoft\'s first proprietary email client is released.
  1989      Quantum Link changes its name to America Online (AOL) and pivots to the PC market. It straddles the line between its pre-Internet a online service roots and the modern Internet. The sound of \"You\'ve Got Mail\" becomes a cultural touchstone.
  1990\'s   The Late Dial-Up Era and the Early Modern Internet
  1990      The first web server is developed at CERN by Tim Berners-Lee.
  1991      Pretty Good Privacy (PGP) is developed by Philip R. Zimmermann as a tool to cryptographically secure and validate the contents of emails. US intelligence services are not amused, and Zimmermann is relentlessly investigated for what they view as Arms Export Control Act violations.
  1992      Users begin experimenting with techniques for encoding binaries as text and attaching them to the bodies of email and Usenet messages, Unix-to-Unix encoding becomes he *de facto* standard for email attachments.
  1994      The first experimental webmail server, [PTG MAIL-DAEMON], is deployed. The first large scale spam campaigns begin, flooding email networks and [Usenet](https://wiki.gentoo.org/wiki/Usenet "Usenet") alike.
  1995      The console email program [[mutt](https://wiki.gentoo.org/wiki/Mutt "Mutt")] is released. Philip R. Zimmermann publishes, in cooperation with MIT Press, publishes the source code of PGP in printed volumes which are exported outside the US, which are then scanned, corrected for OCR errors, and compiled by cryptography activists. Secure Socket Layer (SSL), later known as Transport Layer Security (TLS), is released the same year.
  1996      Hotmail, among the first widely popular webmail services, is launched. Mail Abuse Prevention System (MAPS), the first anti-spam product, launches the same year. Multipurpose Internet Mail Extensions (MIME) becomes a standard and quickly displaces UUE as the preferred email attachment mechanism.
  1997      The first release of Microsoft Outlook email and calendaring application, it is now ubiquitous in corporate environments.
  1999      The BlackBerry 850 is released, ushering in the smartphone era, email begins to migrate away from a presumed 80×25 display to reflowable text that is readable in any aspect ratio. Hushmail, the first popular end-to-end encrypted email service is launched. Its use remains popular among organizations requiring HIPPA compliance.
  2000\'s   Email and the Rise of the Smartphone
  2000      [ILOVEYOU](https://en.wikipedia.org/wiki/ILOVEYOU "wikipedia:ILOVEYOU"), the first major computer virus designed to propagate via email is released and quickly goes global. The virus is written in VBScript and exploits vulnerabilities in Microsoft Outlook in order to propagate.
  2001      The first release of Spam Assassin, meant to curb the growing tide of spam messages on email networks.
  2003      Mozilla Thunderbird is released.
  2004      Sender Policy Framework (SPF) DNS records were developed as a tool to curb forged email messages. Gmail is launched.
  2007      The iPhone is released, it is the first wildly popular smartphone for the masses. The trend towards reflowable text and HTML email quickly accelerates. It is discovered that Hushmail\'s application is able to capture user encryption passphrases allowing for later decryption of messages.
  2010\'s   The Twenty Tens
  2010      Under pressure from users seeking increased security in the aftermath of the Edward Snowden leaks, email providers quickly pivot to enforcing TLS security for all email exchanges. This protects email in transit from passive surveillance but does nothing to secure email \"at rest\" stored in a user\'s inbox. Winlink quickly becomes the dominant form of email message handling over amateur radio (ham) bands, significantly improving radio amateurs ability to support humanitarian relief efforts during hurricanes and other disasters.
  2014      The Switzerland based Proton Mail service is launched, providing end-to-end encryption of email messages. The service uses its own protocol internally, but released proton-bridge to allow SMTP clients to connect securely. Both the protocol and the bridge are open source and publicly documented.
  2017      A small number of [Tor](https://wiki.gentoo.org/wiki/Tor "Tor")-based email services begin to emerge; Proton Mail announces the availability of email via its Tor node.
  --------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## [Understanding How Email Works]

A modern email address, as specified in the SMTP standard, has a few different parts. Given: `bob@gentoo.org`:

-   ***bob*** is the name of the user account.
-   ***@*** demarkates the user part of the email address from the server name.
-   ***gentoo*** is the public facing name of the email server.
-   ***.org*** is the top-level domain to which the server *gentoo* belongs.

All public facing email servers must have globally unique names, the use of higher level domain names helps make that possible. Thus `gentoo.org` and `gentoo.net` are different servers.

SMTP is not the only standard for email addresses, even in the modern era, but it is far and away the most common. This standard is what the Internet uses natively. Bidirectional communication with email addresses that do not conform to this standard are *usually* possible to and from the public Internet, provided some gateway is available to mediate between the disparate protocols.

In simple terms, when an email is created it is a plain text file with some additional markup. There are two main parts to the message: the headers and the body. The headers contain the subject line, the email of the intended recipient, and several bits of housekeeping required by the mail server. Attachments, if any, are encoded as text using a standard encoding, typically [base64] or (rarely) [uuencode]. An email client, or web portal emulating an email client, is used for email composition.

Let\'s assume Alice wants to send Bob an email inviting him to a sporting event next week.

Alice opens her mail client locally on her Gentoo Linux workstation and composes a message. Once Alice instructs the mail client to send the message, several things happen:

**Communication Between Alice and her Email Server**

1.  Alice\'s email client performs a DNS lookup of her email server it finds the MX record and reaches out to the specified server.
2.  Alice\'s email server accepts a connection over SMTP. Typically the session is encrypted with TLS.
3.  Alice\'s email server confirms she\'s a valid user and then accepts the message.
4.  Once Alice\'s mail exchange server has the message it may perform additional checks: has Alice\'s IP been used to send spam recently? Does the email contain a possibly malicious attachment, etc?

**Communication Between the Sending and Receiving Email Servers**

1.  Once Alice\'s mail exchange server satisfied there is nothing fishy about the message, sends the message to the Mail Transfer Agent (MTA).
2.  Alice\'s Mail Transfer Agent performs a DNS lookup for Bob\'s email server and checks the MX record.
3.  It then establishes an SMTP connection, again typically secured with TLS, and advises that it has a message for Bob.
4.  Bob\'s email server check\'s to see if Bob is indeed a valid user on the server. If so, it accepts the message.
5.  Once Bob\'s server accepts the message it performs a number of checks. If Bob\'s email sever has never heard of Alice\'s it will likely \"call back\" to her mail server and confirm she is a valid user.
6.  Bob\'s server may check for signs of spam, malicious code, etc. its end as well.
7.  Assuming the message passes all of its checks, the email is delivered to Bob\'s inbox.

**Communication Between the Receiving Email Server and Bob**

1.  Bob\'s smartphone polls his email server every few minutes to see if he has a message. These polls are performed over the IMAP protocol, typically secured by TLS.
2.  Bob\'s email client sees the new message and, to conserve data usage, only pulls down a copy of the headers.
3.  Bob\'s smartphone chimes indicating he has a message.
4.  Bob opens his smartphone\'s email client and sees Alice\'s message in his inbox.
5.  Bob taps the message and his email client pulls down a full copy of the message using the IMAP protocol, again typically secured via TLS.

To keep things simple, the specifics of spam and malware prevention have been glossed over to a great extent, as was the possibility of one or more intermediate SMTP relay servers handling the message in transit prior to delivery. This is the process of sending and reciving email in the modern age boiled down to its essence. To avoid clouding the basics, optional but semi-common security tools that enable message and attachment encryption prior to sending were not modeled.

### [Anti-spam measures affecting sending of email]

Email involves two distinct FROM fields defined in two separate email specifications, [RFC5231](https://www.rfc-editor.org/rfc/rfc5321) (\"Simple Mail Transfer Protocol\", SMTP) and [RFC5322](https://www.rfc-editor.org/rfc/rfc5322) (\"Internet Message Format\"). The first FROM, referred to variously as [RFC5321.MailFrom], [envelope FROM], or [bounce address], is the one used by SMTP when transferring mail between mail servers. The second FROM, referred to as [RFC5322.From] or [header FROM], is the one visible to end-users as the \'From:\' header of an email.

-   SPF: [Sender Policy Framework](https://en.wikipedia.org/wiki/Sender_Policy_Framework). Used to check whether the sending mail server to authorized to send mail from the sender\'s domain.
-   DKIM: [DomainKeys Identified Mail](https://en.wikipedia.org/wiki/DomainKeys_Identified_Mail). Used to digitally sign the \'header FROM\' (and possibly other header fields as well). Receivers verify the signature via a specific Resource Record in DNS. DKIM can create issues when sending mail to mailing lists.^[\[1\]](#cite_note-1)^
-   DMARC: [Domain-based Message Authentication, Reporting and Conformance](https://en.wikipedia.org/wiki/DMARC). Used to check whether the envelope FROM aligns with the header FROM.
-   IP Address Reputation: tracks whether an IP address has been used in the past to send SPAM messages among several other factors.

At one point the political consensus among email providers was that \"positive delivery\" was a good thing and that it was sufficient to mark an incoming message as SPAM. This would ensure that an email incorrectly market as suspicious would still reach its intended recipient\'s SPAM folder if nothing else. With the rise of highly sophisticated SPAM campaigns those days are long over. Very well known email providers --- Google, Microsoft, Apple, Major ISP\'s, etc. --- are effectively privileged senders and smaller email providers are disadvantaged to varying degrees. The net result is that it can be difficult for a single individual or small group to self-host their email services.

## [Email Delivery Protocols]

### [SMTP]

-   Year Created: 1981
-   Address Pattern: [\<user\>@\<domain\>.\<tld\>]
-   Example Address: [larry@gentoo.org]
-   Community Support: [r/email](https://reddit.com/r/email)

SMTP is far and away the most common email delivery protocol. Even though the SMTP protocol dominates as the email transmission of choice, several other protocols do exist and are still used in niche applications even in the present day.

## [Email Retrieval Protocols]

### [POP3]

### [IMAP]

## [Less Common Email Protocols]

### [Protocols Extended from SMTP]

#### [Proton Mail]

-   Website: [https://proton.me](https://proton.me)
-   Year Created: 2014
-   Address Pattern: [\<user\>@proton.me], or [\<user\>@protonmail.com]
-   Example Address: [larry@proton.me]
-   Community Support:
    -   Reddit: [r/ProtonMail](https://reddit.com/r/ProtonMail)

**How an SMTP user routes email to Proton Mail:** Any SMTP-based email user can send email to the [proton.me] domain as normal. No special action is required.

**How a Proton Mail routes Email to Third Parties:** Proton Mail is an SMTP-based email provider that enforces PGP encryption between parties in a zero knowledge way to enforce *encryption at rest*. The keys are never known to the provider and the user\'s password decrypts the keys client-side.

To send to a non Proton Account there two options:

1.  An unencrypted message can be sent. In this case, no special action is required. From the perspective of both users there is no difference in experience. The message is handled identically to a less privacy enforcing email provider.
2.  A secure message can be sent to the non-Proton Mail account. In this case the non-Proton email user gets a minimal email message indicating a secure message has arrived for them. This message originates from the [proton.me] domain and includes a hyperlink to the actual message. A password must be provided for authentication. Upon successful authentication the message is decrypted in a secure web portal. The message is decrypted client-side.

**Description:** Proton uses SMTP internally in a way that systematically enforces PGP encryption between sender and recipient in a manner that is transparent to the user. Proton Mail is end-to-end encrypted by default and protected by strong Swiss privacy laws. When communicating between Proton Mail accounts only the sender and recipient account names and the sender IP address are known to the provider. This is just enough information to route the message and prevent bad actors from abusing the system and nothing more.

Unlike most email providers, Proton Mail is [Tor](https://wiki.gentoo.org/wiki/Tor "Tor") friendly and a dedicated [.onion] instance is provided for added anonymity if desired.

A dedicated web-based interface and mobile app are available from Proton Mail. Proton Bridge allows anyone to use a traditional SMTP-based email client which passes the message to Proton Mail over the far more secure Proton Mail protocol. Officially, major email clients such as [Thunderbird](https://wiki.gentoo.org/wiki/Thunderbird "Thunderbird") are supported. Terminal-based email clients such as [Mutt](https://wiki.gentoo.org/wiki/Mutt "Mutt") and [Alpine](https://wiki.gentoo.org/index.php?title=Alpine&action=edit&redlink=1 "Alpine (page does not exist)") are not officially supported but users report few if any difficulties in configuring their preferred email clients for Proton Mail use.

#### [Winlink]

-   Website: [https://winlink.org/](https://winlink.org/)
-   Year Created: 1997
-   Address Pattern: [\<ham-radio-callsign\>@winlink.org]
-   Example Addess: [w1aw@winlink.org]
-   Known SMTP Gateways: [winlink.org].
-   Community Support:
    -   Reddit: [r/amateurradio](https://reddit.com/r/amateurradio)
    -   IRC: [[#hamradio](ircs://irc.libera.chat/#hamradio)] ([[webchat](https://web.libera.chat/#hamradio)])
    -   IRC: [[#hamradio-social](ircs://irc.libera.chat/#hamradio-social)] ([[webchat](https://web.libera.chat/#hamradio-social)])
    -   Usenet: [[rec.radio.amateur.moderated](news:rec.radio.amateur.moderated) ([weblink](https://www.novabbs.com/devel/thread.php?group=rec.radio.amateur.moderated))]
    -   Usenet: [[rec.radio.amateur.misc](news:rec.radio.amateur.misc) ([weblink](https://www.novabbs.com/devel/thread.php?group=rec.radio.amateur.misc))]

**How an Internet Email sends a message to a Winlink Email Address:** The Internet-based email address must have previously received a message from his intended recipient. After having done so, he may reply or initiate a new message entirely. However, the sender must --- among several prohibitions --- scrupulously avoid obscenity and any attempts at commerce.

**How a Winlink Email user sends a message to an Internet Email Address:** The Winlink user composes a message with the Internet-based email address listed in the \"To:\" field. The Winlink network gates to the public Internet.

**Description:** Winlink is for sending email via [ham radio](https://en.wikipedia.org/wiki/Amateur_radio "wikipedia:Amateur radio") (ham radio) and is heavily used by service groups such as [ARES](https://en.wikipedia.org/wiki/Amateur_Radio_Emergency_Service "wikipedia:Amateur Radio Emergency Service") and [RACES](https://en.wikipedia.org/wiki/Radio_Amateur_Civil_Emergency_Service "wikipedia:Radio Amateur Civil Emergency Service") in support of [FEMA](https://en.wikipedia.org/wiki/FEMA "wikipedia:FEMA") operations. In the event of a nation-state level Internet outage, the network can act as a \"post-apocalyptic Internet\" of sorts and relay messages globally using only HF and UHF/VHF connected nodes. The Winlink network uses a heavily modified SMTP infrastructure with several custom extensions. Intentionally obscuring the meaning of messages is illegal, so TLS or PGP encryption is not allowed. Only licensed ham radio operators can initiate messages from Winlink, however non-hams may reply to a previously sent message. The act of replying whitelists the non-Winlink sender\'s address for future correspondence. FCC (or national equivalent) rules forbidding obscenity and commerce apply. Due to bandwidth limitations most messages are sent over HF at no more than 300 baud. Consequently, message sizes are capped at 128kB.

**Common Issues:**

-   **Advertisements in the signature block:** Many Internet users have antivirus advertisements buried in their signature block. As commerce is forbidden over amateur radio bands. Emailing from the Internet to Winlink with such a signature will likely get flagged and bounced back to the sender; this is an *extremely common* oversight.
-   **Attempting to send an email larger than 128kB:** Message larger than 128kB will get bounced back to the sender. Winlink emails are typically UTF-8 text. HTML is rare and when it is used it\'s in a minimal style to keep message sizes down. Unfortunately, modern HTML email can be quite large. An empty Google Gmail message starts at about 5kB. Internet-based email senders should use plain text email messages if possible. Additionally, it\'s a good idea to keep messages short and avoid unnecessary file attachments to prevent bounces. If file attachments are unavoidable, compress them.
-   **Swearing or using crude terms:** A message containing one or more expletives will likely get bounced back to the sender. Such language is not permitted over the air.
-   **Having a name like \"Dick Jones\":** Occasionally a portion of a user\'s name may contain a [regular expression](https://en.wikipedia.org/wiki/regular_expression "wikipedia:regular expression") match for a strong expletive or crude anatomical term. When that happens messages are sometimes inappropriately flagged as obscene and not delivered. Most people end up contacting Winlink support directly to resolve the issue.

### [Non-SMTP Dervied Protocols]

#### [FidoNet]

-   Website: [https://www.fidonet.org/](https://www.fidonet.org/)
-   Year Created: 1983
-   Address Pattern: [\<zone\>:\<net\>/\<node\>\[\<.point\>\]]
-   Example Address: [larry@1:33/108.0]
-   Known SMTP Gateways: [fidonet.org]
-   Community Support: [r/fidonet](https://reddit.com/r/fidonet) and #fidonet on irc.icq.com.

**How an SMTP user routes email to FidoNet:** The email address has to be rewritten as [\<name\>@p\.f\<node\>.n\<net\>.z\<zone\>.fidonet.org]. So, the user Larry with an email of [larry@1:33/108.0] would be rewritten as [larry@p0.f108.n33.z1.fidonet.org].

**How a FidoNet user routes email to SMTP:** Most FidoNet nodes will recognize an domain-style SMTP email address when they see it and route it to [fidonet.org] which will gate it to the Internet.

**Description:** FidoNet is still in use by BBS system administrators today. FidoNet was formerly used in ham radio until displaced by Winlink in the late 1990\'s and early 2000\'s.

#### [Packet Mail]

-   Website: [Tucson Amateur Packet Radio](https://tapr.org/)
-   Year Created: 1994
-   Address Pattern: [\<USER-CALL-SIGN\>@\<BBS-CALL-SIGN\>.\[#\<GEOGRAPHIC-AREA\>\]\<STATE-PROVINCE\>.\<COUNTRY\>.\<CONTINENT\>\[.WW\]]
-   Example Address: [K0LCOW@W1AW.CT.USA.NOAM]
-   Known SMTP Gateways: Unknown
-   Community Support: [r/amateurradio](https://reddit.com/r/amateurradio).

<!-- -->

-   **How an Internet Email sends a message to a Packet Mail Email Address:** The Internet-based email address must have access to an email server that can act as a gateway and probably has to be on a whitelist as well. The precise semantics may be gateway specific but the following is relatively common: typically the Packet Mail email address must be rewritten. A common scheme is something like [\<RECIPIENT-CALL-SING\>+\<SENDER-CALL-SIGN\>!\<PAKET-BBS-CALL-SIGN\>@\<SOME-GATEWAY\>.\<TLD\>] in order to transit the SMTP portion of the journey to the sender.

Sending NTS radiograms this way may or may not be supported by the gateway. The best alternative is to either send the radiogram via Winlink to a [Radio Relay International](https://radiorelay.org/) NTS Gateway or to use the [NTS 2.0 Radiogram web portal](https://nts2.arrl.org/radiogram/) to originate the NTS message.

-   **How a Packet Mail Email user sends a message to an Internet Email Address:** The Packet Mail user composes a message with the Internet-based email address listed in the \"To:\" field. This can typically only be done if the Packet Mail BBS node directly supports sending messages out over the public Internet via SMTP.

**Description:** Modern packet mail addressing and routing rules were developed by TAPR BBS and is still in use today by ham radio operators all over the world. Unlike SMTP-style addresses, packet mail addresses use the x.3.4 hierarchical address protocol. This has the advantage of not relying on DNS infrastructure for name resolution. Unfortunately, this has the disadvantage that valid packet mail addresses often include characters that are not valid for SMTP which complicates any efforts to allow bidirectional communication from a normal Internet facing SMTP email user and a packet mail user.

If the packet station receiving the message from the sender knows how to reach the home packet station of the message recipient, the message will be queued for delivery to that station. If on the other hand it has no idea how to reach that station directly, it will forward the message to a node it knows in the [\<#GEOGRAPHIC-AREA\>]. Failing that, it will walk the hierarchy until it gets to a node that either is a member of that hierarchy or knows how to reach it. With rare exceptions (see below) the top of the hierarchy is assumed to be \"World Wide\" [.WW]. Once an email message has been passed, the message will hop from one node to the next either via AX.25 over ham radio bands or, given an Internet connected node, AX.25 over IP (AXIP) until it reaches the destination packet node.

There are a few edge-cases when dealing with hierarchical address protocol:

1.  Objects in outer space.
2.  [National Traffic System](https://en.wikipedia.org/wiki/National_Traffic_System "wikipedia:National Traffic System") (NTS) messages in [ARRL Radiogram](https://en.wikipedia.org/wiki/ARRL_Radiogram "wikipedia:ARRL Radiogram") format.

A packet node in earth orbit might have an address that ends in [AMSAT] instead. NTS radiograms are typically addressed as \<ZIP-CODE\>@NTS\<TWO-LETTER-STATE\> with no dot between \"NTS\" and the two letter state code and nothing higher in the hierarchy following after.

All though Packet Mail and Winlink are both commonly used in Ham radio, all of this is entirely different from Winlink. Each has its own separate infrastructure. Winlink is email only and uses a heavily customized extension of SMTP. On the other hand, Packet Mail does not use SMTP and has equal support for both email functionality and [Usenet](https://wiki.gentoo.org/wiki/Usenet "Usenet")-like bulletins. Some nodes are configured to pass messages out from packet nodes to Winlink but the reply address is nearly always rewritten as a Winlink address so the packet user must check Winlink for message replies.

#### [UUCP]

-   Website: [https://uu.net](https://uu.net) (defunct)
-   Year Created: 1979
-   Address Pattern: [\<well-known-host\>!\<next-hop\>!\<hostname\>!\<user\>\[\<.UUCP\>\]]
-   Example Addess: [gentoo!larry.UUCP]
-   Known SMTP Gateways: [uunet.uu.net] or [uucp.uu.net] (working?); [uucpssh.net] (defunct, circa 2008).
-   Community Support: [[comp.mail.uucp](news:comp.mail.uucp) ([weblink](https://www.novabbs.com/devel/thread.php?group=comp.mail.uucp))], [r/sysadmin](https://reddit.com/r/sysadmin) and [#Fidonet] on [newnet.net:6697].

**How an SMTP user routes email to UUCP:** Emails from a UUCP network outbound to SMTP take the form of [\<user\>%\<domain\>@uunet.uu.net]. So, a user, Alice, attempting to reach Larry the Cow from an SMTP network to his UUCP email address [gentoo!larry.UUCP], network would send an email to [larry%gentoo@uunet.uu.net] which is a known SMTP-UUCP gateway.

**How a UUCP user routes email to SMTP:** Emails from UUCP outbound to an SMTP network use the pattern [\<domain\>!\<server\>!\<user\>]. So if Larry emails Alice [alice@gentoo.org] he would send the email to [org!gentoo!alice] and his email gateway would do the rest.

**Description:** Email addresses specified the names of adjacent machines using a *bang-path* ending in the pseudo-domain [.UUCP]. This was the standard long before DNS-based hostname lookup. Each link was specified manually by name. If a server went down the path could break and messages could be delivered late or not at all. Sometimes due to maintenance issues, users had to get creative and find an alternate route to a desired contact. UUCP is still used for messaging over intermittently available serial lines or radio links where TCP/IP or ax.25 prove impractical. The [[[net-misc/taylor-uucp]](https://packages.gentoo.org/packages/net-misc/taylor-uucp)[]] is perhaps the most commonly available UUCP implementation on Linux.

## [Commonly Gated or Bridged Protocols]

### [Git]

-   Website: [https://git-scm.com/](https://git-scm.com/)
-   Year Created: 2005
-   Address Pattern: Typically, `<org>/<repository>@<domain>.<tld> <filename>.patch` or similar.
-   Example Address: `larry_cow/project-foo@lists.sr.ht`
-   Community Support:
    -   [https://git-scm.com/community](https://git-scm.com/community)
    -   [https://git-send-email.io](https://git-send-email.io)
    -   `#git` on libera.chat.

**How an Email user routes email to a Git repository:** The [git send-email] command is used. Something like [git send-email \--to=\"larry_cow/project-foo@lists.sr.ht\" HEAD\^] is typical. The exact details differ somewhat between git providers.

**How a Git repository sends messages to an Email Address:** Typically, the git provider has its own email infrastructure which sends updates out to a registered user\'s email address.

**Description:** Git was originally designed for collaboration via email. As a consequence, it is a core feature of git. Later git providers produced web-based portals in lieu of an email-centric approach to git project management. [GitHub](https://github.com/) and [GitLab](https://gitlab.com) are two famous examples. Some git providers, notably [SourceHut](https://sr.ht/), buck this trend and manage git projects in an email-centric manner.

In order to be able to manage remote git projects effectively via email some configuration steps are required by the git user.

First, the [[[dev-vcs/git]](https://packages.gentoo.org/packages/dev-vcs/git)[]] needs to be installed:

`root `[`#`]`emerge --ask dev-vcs/git`

Then ensure that [git config] has at least minimal user information:

`user `[`$`]`git config --global user.email "you@youremailserver.org"`

`user `[`$`]`git config --global user.name "Your Name"`

Second, SMTP email information needs to be added to [\~/.gitconfig]:

[FILE] **`~/.gitconfig`**

    [sendemail]
        smtpserver = mail.youremailserver.org
        smtpuser = you@youremailserver.org
        smtpencryption = ssl
        smtpserverport = 465

Third, after performing a [git commit] send the patch from [git]:

`user `[`$`]`git send-email --to="myorg/myproject@mygitprovider.org" HEAD^`

**Common Issues:**

-   Trying to send patch emails via something other than [git send-email] will not work. Please do not try it. Stick to git\'s native email mechanism.

### [][Network News Transfer Protocol (NNTP)]

-   Website: [https://www.big-8.org/](https://www.big-8.org/) (*de facto*)
-   Year Created: 1983
-   Address Pattern: [\<group\>-\<name\>@\<nntpgateway\>.\<tld\>]
-   Example Addess: [alt-os-linux-gentoo@hypotheticalgw.gentoo.org]
-   Known SMTP-NNTP Gateways: N/A, locally deployed.
-   Community Support:
    -   Reddit: [r/r/usenet](https://reddit.com/r/r/usenet)
    -   Usenet: [[alt.fan.usenet](news:alt.fan.usenet) ([weblink](https://www.novabbs.com/devel/thread.php?group=alt.fan.usenet))]
    -   Usenet: [[news.software.readers](news:news.software.readers) ([weblink](https://www.novabbs.com/devel/thread.php?group=news.software.readers))]
    -   Usenet: [[news.admin.peering](news:news.admin.peering) ([weblink](https://www.novabbs.com/devel/thread.php?group=news.admin.peering))]

**How an Email user routes email to Usenet:** The typical pattern is to replace all dots in the Usenet newsgroup path with hyphens and affix the gateway domain. So, [alt.os.linux.gentoo] becomes [alt.os.linux.gentoo@\<smtp-to-nntp-gateway\>.\<tld\>].

**How a Usenet user routes email to an Email Address:** Reply by SMTP, most users have their email addresses in the headers.

**Description:** Usenet newsgroup traffic travels over NNTP protocol. Many institutions have historically provided email gateways to Usenet for convenience. Some gateways doubtless still exist. Most good email clients worthy of the name have native NNTP support anyway, all but eliminating the need for such gateways.

### [][Short Message Service (SMS) Text]

-   Year Created: 1992
-   Address Pattern: [\<10-digit-telephone-number\>@\<carrier-sms-gateway\>.\<tld\>].
-   Example Address: 5551234567@txt.att.net
-   Known SMTP-SMS Gateways: See [List Of Email-To-SMS Addresses](https://avtech.com/articles/138/list-of-email-to-sms-addresses/).
-   Community Support: N/A.

**How an Email user sends a message to an SMS Text Enabled Number:** Simply send an email to a known mobile phone number, typically without the country code, followed by the at symbol (`@`) and the appropriate domain. See [this list](https://avtech.com/articles/138/list-of-email-to-sms-addresses/) for details.

**Description:** SMS text traffic is digital and all major mobile phone carriers provide bidirectional communication with email addresses over text. This can be used by automation or to avoid the fees associated with sending SMS texts internationally.

**Common Issues:**

-   Messages in excess of 160 characters (ASCII) or 70 glyphs (Unicode) --- subject line included --- are converted to Multimedia Messaging Service (MMS) messages. Most carriers limit total MMS message size to around 5,000 bytes. Messages larger than this are usually delivered but truncated.
-   Unicode characters may not display correctly in an SMS text messaging application. Further, Unicode glyphs will necessarily consume more bytes than simple ASCII text.

## [Attachments]

### [Uuencoding]

### [MIME]

## [Encryption]

### [TLS]

### [PGP]

## [Troubleshooting]

## [See also]

-   [Mailfiltering Gateway](https://wiki.gentoo.org/wiki/Mailfiltering_Gateway "Mailfiltering Gateway") --- provides step-by-step instructions for installing spam fighting technologies for Postfix.
-   [Usenet](https://wiki.gentoo.org/wiki/Usenet "Usenet") --- a federated and decentralized worldwide Internet forum and the world\'s oldest digital social network

## [External resources]

-   [UsePlainText.email](https://useplaintext.email/) --- a site dedicated to promoting the security and accessibility benefits of email as a text only format to the exclusion of HTML-based messages.
-   [Anti-Spam techniques](https://en.wikipedia.org/wiki/Anti-spam_techniques "wikipedia:Anti-spam techniques") --- a Wikipedia article detailing anti-spam techniques.

## [References]

1.  [[[↑](#cite_ref-1)] [[RFC7960, \"Interoperability Issues between Domain-based Message Authentication, Reporting, and Conformance (DMARC) and Indirect Email Flows\", Section 3.2.3, \"Mailing Lists\"](https://datatracker.ietf.org/doc/html/rfc7960#section-3.2.3)]]

\