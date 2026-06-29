# Arch IRC channels

To use Internet Relay Chat (IRC), you need an IRC client. The installation live environment includes the Irssi client.

You are expected to familiarize yourself with our Code of conduct and General guidelines#IRC before joining any of the official channels. For a list of commonly used abbreviations, see Arch terminology.

## Main channels
This section is about #archlinux, the main Arch Linux support IRC channel, and #archlinux-offtopic, the main Arch Linux social channel, both available on the Libera Chat network. See https://archlinux.org/news/move-of-official-irc-channels-to-liberachat/

The central topic for #archlinux is support and general discussion about Arch Linux.

## Registration
In order to reduce spam, #archlinux and #archlinux-offtopic have the channel mode set to  and . This means you have to be identified via  to be able to join these channels and send messages, respectively. If you are not registered and identified, you will be forwarded to #archlinux-unregistered.

To register with NickServ, follow the Libera Chat FAQ, as well as  when connected to irc.libera.chat:

 /query NickServ HELP REGISTER
 /query NickServ HELP IDENTIFY

## Channel operators
Arch operators are ops in both #archlinux and #archlinux-offtopic. See the list below, or run  on Libera Chat.

If you for some reason need the help of an op, do not be shy to  or  us. Here is the list of ops as of 2021-09-24:

* alad
* BrainDamage
* gehidore / man
* grawity
* jelle
* MrElendig / Mion
* Namarrgon

## Libera Chat group contacts
Group contacts mediate matters between the Libera Chat network staff, Arch Linux staff and Arch Linux users. That includes the management of channels in the #archlinux-* namespace on the Libera Chat network and the assignment of  hostmasks. Please note that only Arch Linux staff are eligible for hostmasks.

* wonder / ioni
* fukawi2
* anthraxx
* dvzrv
* Namarrgon

## Collaborative debugging
When requesting help from an IRC help channel (like #archlinux), it is inappropriate to paste logs into the channel and this may even get you kicked. Use a pastebin instead, you can use phriks factoid  to see which pastebins are acceptable.
Acceptable pastebins usually work without enabling JavaScript. Some require enabling JavaScript for posting from a web browser, which is still acceptable because it does not affect the viewer. They should not display advertising or other disrupting content and should also not require a login. Excellent pastebins usually provide a way to paste output via piping.

An example list of acceptable pastebins:

* https://0x0.st - supports pasting of almost any filetype. May have slightly broken MIME type detection.
* https://paste.rs - supports pasting of images, but MIME type will be off.
* https://bpa.st - good for people who want something graphical.
* https://gist.github.com - useful if you want to also have rendered markdown or multiple files, supports CLI pasting via .

## IRC usage
When first entering the channel, there is no need to say hello and you should turn off your IRC client's Away / Available messages. State the problem you are experiencing and make sure to be verbose and to provide logfiles. It also helps to search for any error messages you are getting first to not waste anybody's time. It is also worth it to search for issues on any of the bugtrackers of the relevant software.
The more helpful and verbose you are, the quicker you are going to receive help.

If this is a problem or question which is very specific to a specific software, consider visiting the dedicated IRC channel for it if there is one. It is more likely to receive a good answer there.

## Output errors/messages to a file
Sometimes it is not possible to pipe the output to a pastebin directly and it should be written into a file before.

 $ application &> application-output.txt

This is useful if pasting logs that contain sensitive data, e.g serial numbers in smartctl output, which have to be manually edited out.

## Other channels
The size of our community led to the creation of multiple IRC channels. To get a list of all channels on irc.libera.chat that contain  in their name, use the command . For further information on how to search channels, see https://libera.chat/guides/findingchannels.

{| class="wikitable sortable"
! Channel
! Topic
|-
| #archlinux-aur
| AUR general discussion
|-
| #archlinux-aurweb
| aurweb development discussion
|-
| #archlinux-bugs
| Bug-centric discussion
|-
| #archlinux-buildbtw
| buildbtw development discussion
|-
| #archlinux-classroom
| A project that develops and hosts classes for the Arch Linux community
|-
| #archlinux-conf
| ArchConf organization and discussion
|-
| #archlinux-devops
| Arch Linux internal infrastructure and devops discussions
|-
| #archlinux-mirrors
| Arch Linux mirror infrastructure and organization
|-
| #archlinux-multilib
| Arch Linux Multilib Project discussion and packaging
|-
| #archlinux-newbie
| A space to learn, try new things, and ask for help without fear of ridicule
|-
| #archlinux-pacman
| Pacman development and discussion
|-
| #archlinux-ports
| Discussion about architecture porting (see RFC!32)
|-
| #archlinux-proaudio
| Discussion about professional audio
|-
| #archlinux-projects
| Projects development and discussion (mkinitcpio, abs, dbscripts, devtools…)
|-
| #archlinux-releng
| Arch Linux Release Engineering discussion (arch-boxes, archiso, archlinux-docker, archlinux-wsl and releng)
|-
| #archlinux-reproducible
| Discussion channel for achieving reproducible builds
|-
| #archlinux-security
| Discussion of security issues within Arch packages
|-
| #archlinux-signstar
| signstar development discussion
|-
| #archlinux-testing
| Discussion channel regarding the testing repositories
|-
| #archlinux-wiki
| Discussion about ArchWiki, its articles and the Arch Linux Forums
|-
| #archlinux-women
| Project discussion for programs/events to encourage women to contribute to Arch Linux and provide space for women to socialize and meet each other. Mostly in English.
|}

## International IRC channels
International discussions are available at the following channels, also located at the irc.libera.chat IRC network, unless stated otherwise.

{| class="wikitable sortable"
! Channel
! Community
|-
| #archlinux-br
| Brazilian
|-
| #archlinux-cn
| Chinese
|-
| #archlinux-cz
| Czech
|-
| #archlinux-de
| German
|-
| #archlinux-dk
| Danish
|-
| #archlinux-es
| Spanish
|-
| #archlinux-fr
| French
|-
| #archlinux-ja
| Japanese
|-
| #archlinux-mx
| Mexican
|-
| #archlinux-nordics
| The Nordics: Danish, Finnish, Norwegian and Swedish
|-
| #archlinux-ph
| Filipino
|-
| #archlinux-pl
| Polish
|-
| #archlinux-pt
| Portuguese
|-
| #archlinux-tr
| Turkish
|-
| #archlinux-ua
| Ukrainian
|-
|}
