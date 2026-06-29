** Important**\
Metasploit has been removed from the Gentoo ebuild repository by [this commit.](https://gitweb.gentoo.org/repo/gentoo.git/commit/?id=af8f89d9b9f87bff0d3d3176437b3766a0439f4b) However, it might be available from [community (third party) ebuild repositories](http://gpo.zugaina.org/net-analyzer/metasploit)

[] The information in this article is probably **outdated**. You can help the Gentoo community by verifying and [updating this article](https://wiki.gentoo.org/index.php?title=Metasploit&action=edit).

**Resources**

[[]][Home](https://www.metasploit.com/)

[[]][Official documentation](https://weechat.org/doc)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Metasploit_Project "wikipedia:Metasploit Project")

[[]][GitHub](https://github.com/rapid7/metasploit-framework)

The Metasploit Project is a computer security project that provides information about security vulnerabilities and aids in penetration testing and IDS signature development. The framework is maintained by Rapid7 and the community. Its best-known sub-project is the open source Metasploit Framework, a tool for developing and executing exploit code against a remote target machine. Other important sub-projects include the Opcode Database, shellcode archive and related research. The Metasploit Project is well known for its anti-forensic and evasion tools, some of which are built into the Metasploit Framework.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Overlay]](#Overlay)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
-   [[3] [Removal]](#Removal)
    -   [[3.1] [Unmerge]](#Unmerge)
-   [[4] [See also]](#See_also)
-   [[5] [External resources]](#External_resources)

## [Installation]

Rapid7 recommends using the [binary installer](https://www.rapid7.com/products/metasploit/download/editions/) for the desired version. The installer comes with a [guide](https://github.com/rapid7/metasploit-framework/wiki/Nightly-Installers) that aims to help during the installation process. If someone wants to develop and contribute, there\'s a [guide](https://github.com/rapid7/metasploit-framework/wiki/Setting-Up-a-Metasploit-Development-Environment) to set up a development environment.

** Note**\
This guide makes the following assumptions:

-   You have a Debian-based Linux environment
-   You have a user that is not root. In this guide, we\'re using *msfdev*.
-   You have a GitHub account

### [Overlay]

Metasploit is available from the [pentoo](https://repos.gentoo.org/#pentoo) overlay: [https://github.com/pentoo/pentoo-overlay](https://github.com/pentoo/pentoo-overlay)

### [Emerge]

** Warning**\
In the maintainer\'s words: Metasploit is a very delicate package

`root `[`#`]`emerge --ask net-analyzer/metasploit`

## [Usage]

Metasploit comes with its own CLI. For a detailed list of available commands refer to [Offensive Security guide](https://www.offensive-security.com/metasploit-unleashed/msfconsole-commands/).

For a GUI, refer to [Armitage project](http://www.fastandeasyhacking.com/).

## [Removal]

### [Unmerge]

`root `[`#`]`emerge --ask --depclean --verbose net-analyzer/metasploit`

## [See also]

-   [Wireshark](https://wiki.gentoo.org/wiki/Wireshark "Wireshark") --- a free and open-source packet analyzer.
-   [Nmap](https://wiki.gentoo.org/wiki/Nmap "Nmap") --- an open source recon tool used to check for open ports, what is running on those ports, and metadata about the daemons servicing those ports.

## [External resources]

-   [Downloads by version (official)](https://github.com/rapid7/metasploit-framework/wiki/Downloads-by-Version) - Metasploit\'s versions.
-   [Metasploit unleashed](https://www.offensive-security.com/metasploit-unleashed/) - Offensive security\'s Metasploit course.
-   [Rapid7 free tools](https://www.rapid7.com/free-tools) - some free tools from Rapid7
-   [Community\'s documentation](https://community.rapid7.com/community/metasploit/content?filterID=contentstatus%5Bpublished%5D~category%5Bdocumentation%5D) - some comunnity\'s documentation
-   [Armitage](http://www.fastandeasyhacking.com/) - Metasploit front-end UI