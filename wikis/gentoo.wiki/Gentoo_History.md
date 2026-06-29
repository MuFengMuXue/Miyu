This article aims to give a summary of the creation and evolution of the Gentoo project organization\... *so far*.

Gentoo is an ***independent*** *[software distribution](https://en.wikipedia.org/wiki/Software_distribution "wikipedia:Software distribution")* that traces it\'s origins to the end of the 1990\'s.

Gentoo has targeted several \*BSDs in the past, but now is exclusively the **Gentoo Linux** distribution.

**Gentoo [Prefix](https://wiki.gentoo.org/wiki/Prefix "Prefix")** currently makes the distribution available on other operating systems, both [Linux-based](https://wiki.gentoo.org/wiki/Prefix/tested "Prefix/tested") and others, such as [MS Windows](https://wiki.gentoo.org/wiki/Gentoo_in_WSL "Gentoo in WSL"), [Darwin](https://wiki.gentoo.org/wiki/Prefix/Darwin "Prefix/Darwin") (macOS/OS X), [Android](https://wiki.gentoo.org/wiki/Project:Android "Project:Android"), etc.

## Contents

-   [[1] [The birth of Gentoo]](#The_birth_of_Gentoo)
-   [[2] [The Daniel Robbins years 1999--2004]](#The_Daniel_Robbins_years_1999.E2.80.932004)
-   [[3] [The transition to The Gentoo Foundation Inc. 2004]](#The_transition_to_The_Gentoo_Foundation_Inc._2004)
-   [[4] [The rise of the Gentoo Council]](#The_rise_of_the_Gentoo_Council)
-   [[5] [Gentoo organization today]](#Gentoo_organization_today)
-   [[6] [See also]](#See_also)
-   [[7] [References]](#References)

## [The birth of Gentoo]

Not so long ago, in this very galaxy, a Stampede Linux developer called Daniel Robbins (aka drobbins) started a **totally new and independent** distribution around tooling that they created from scratch on their Stampede development box.

Drobbins leveraged the knowledge that they gained from their work on Stampede^[\[1\]](#cite_note-1)^ to create this novel distribution around what they named the **[ebuild](https://wiki.gentoo.org/wiki/Ebuild "Ebuild") system** with the stated goal of *automating everything from unpacking and patching sources; to compilation, installation, and packaging*^[\[2\]](#cite_note-2)^. Development was coordinated through a channel on [IRC](https://wiki.gentoo.org/wiki/IRC "IRC") at *openprojects.net*^[\[3\]](#cite_note-3)^.

The new distribution was code-named *[Enoch](https://wiki.gentoo.org/wiki/FAQ#Why_is_the_letter_.27e.27_in_the_name_of_many_Gentoo-specific_tools_and_functions.3F "FAQ")* but would soon be officially named ***[Gentoo Linux](https://wiki.gentoo.org/wiki/FAQ#How_is_Gentoo_pronounced.2C_and_what_does_it_mean.3F "FAQ")***.

After a brief exploration of FreeBSD, drobbins would breathe new life into these beginnings of the Gentoo project. Taking inspiration from the excellent [BSD Ports](https://en.wikipedia.org/wiki/FreeBSD_Ports "wikipedia:FreeBSD Ports") system, they gave the name **[Portage](https://wiki.gentoo.org/wiki/Portage "Portage")** to what was now a \"next-generation ports system\"^[\[4\]](#cite_note-4)^.

Commits to still-accessible [version control systems](https://wiki.gentoo.org/wiki/Version_control_systems "Version control systems") reference work from **1998**, though further research could still find earlier dates^[\[5\]](#cite_note-5)^. [gentoo.org](https://gentoo.org/) was registered on the 4th October 1999 ^[\[6\]](#cite_note-6)^.

## [][The Daniel Robbins years 1999--2004]

Gentoo\'s copyrights^[\[7\]](#cite_note-7)^, intellectual property, and other assets belonged indirectly to Daniel Robbins (named Gentoo\'s *\"chief architect\"*) through the ownership of [Gentoo Technologies Inc.](https://opencorporates.com/companies/us_nm/2055978), a corporation that controlled the whole project from the founding of Gentoo until drobbins\'s retirement and the creation of the [Gentoo Foundation](https://wiki.gentoo.org/wiki/Foundation:Main_Page "Foundation:Main Page") in 2004^[\[8\]](#cite_note-8)^.

The [Gentoo shop](http://store.gentoo.org/) also belonged to Gentoo Technologies Inc.

During this period, top-level project leads ran the project along with the chief architect. There were fewer formally-democratic processes in place, which may have been a good thing for the pace of development. Gentoo was smaller then and easier for one person to manage.

## [The transition to The Gentoo Foundation Inc. 2004]

The not-for-profit [Gentoo Foundation](https://wiki.gentoo.org/wiki/Foundation:Main_Page "Foundation:Main Page")^[\[9\]](#cite_note-9)^ was formed on [14 May 2004](https://wiki.gentoo.org/wiki/Foundation:Articles_of_Incorporation "Foundation:Articles of Incorporation"). Its purpose was both to legally represent Gentoo, and to be accountable for Gentoo\'s assets, which it inherited from Gentoo Technologies Inc.

Whereas Gentoo Technologies Inc. was managed by Daniel Robbins without the involvement of Gentoo developers, the Foundation would now be composed of developers and major contributors.

The Foundation remained fairly invisible to most developers however, being kept separate from the distribution like Gentoo Technologies Inc. used to be. The top-level project leads, now without a chief architect, continued to be responsible for the technical direction of Gentoo.

## [The rise of the Gentoo Council]

For one reason or another, the de-facto system whereby the top-level project leads were responsible for the technical direction of Gentoo was felt by some to be becoming less effective with the passing of time. A number of proposals beginning with discussions at FOSDEM 2005, were [formulated](https://wiki.gentoo.org/wiki/Project:Council/Metastructure_reform_2005 "Project:Council/Metastructure reform 2005"). One was [selected](https://archives.gentoo.org/gentoo-dev/message/6587be9996ce078315d62ab2b73cfeca) by a ballot of developers and subsequently codified in [GLEP 39](https://www.gentoo.org/glep/glep-0039.html).

The results of the first Council election were announced [on 1 Sept 2005](https://archives.gentoo.org/gentoo-dev/message/3a1042167ebac103b9ffec5261ed6827) and the first Council meeting was held on [15 September 2005](https://archives.gentoo.org/gentoo-dev/message/5dff5c2606b4c79392c51fd4e49dbeab)

Thus [the Council](https://wiki.gentoo.org/wiki/Project:Council "Project:Council") was created later and separately from the Foundation.

## [Gentoo organization today]

The Gentoo Foundation Inc has become even more visible and transparent than in the early years, with it\'s Trustees holding regular monthly meetings in [[#gentoo-trustees](ircs://irc.libera.chat/#gentoo-trustees)] ([[webchat](https://web.libera.chat/#gentoo-trustees)]) since 2008. Members and non-members are welcome to attend. Meeting logs are [published](https://projects.gentoo.org/foundation/2016/) (grouped by year), as are [motions](https://projects.gentoo.org/foundation/motions/).

The Gentoo Foundation Inc. is responsible to its members, and it\'s Trustees are the board responsible for a business. They are required by the laws of New Mexico to hold an Annual General Meeting open to all members.

Foundation members are members who have voted in at least one of the last two Trustee elections and people who have asked to join, showing how they have contributed to Gentoo. Not all developers are Foundation members, membership is opt in, and some Foundation members are not Gentoo developers.

The Council, being directly involved in the management of the Gentoo development process, is generally more visible to the Gentoo community than the Foundation.

The Gentoo Council is responsible to and elected by Gentoo developers (in contrast to the Foundation, which is responsible to it\'s members). Council members are required by their terms of reference ([GLEP 39](https://www.gentoo.org/glep/glep-0039.html)) to hold at least one public meeting per month.

In March 2024, [Gentoo Linux became an SPI associated project](https://www.gentoo.org/news/2024/04/10/SPI-associated-project.html).

## [See also]

-   [Foundation:Main Page](https://wiki.gentoo.org/wiki/Foundation:Main_Page "Foundation:Main Page")
-   [Project:Council](https://wiki.gentoo.org/wiki/Project:Council "Project:Council")
-   [Project:Elections](https://wiki.gentoo.org/wiki/Project:Elections "Project:Elections") --- gather all the people participating in the organization of elections in Gentoo together as well as providing the project with procedures, documentation, and scripts to run those elections.

## [References]

1.  [[[↑](#cite_ref-1)] [[https://web.archive.org/web/20051126223839/https://www.gentoo.org/doc/en/articles/making-the-distro-p1.xml](https://web.archive.org/web/20051126223839/https://www.gentoo.org/doc/en/articles/making-the-distro-p1.xml)]]
2.  [[[↑](#cite_ref-2)] [[https://web.archive.org/web/20101002000636/http://www.gentoo.org/doc/en/articles/making-the-distro-p2.xml](https://web.archive.org/web/20101002000636/http://www.gentoo.org/doc/en/articles/making-the-distro-p2.xml)]]
3.  [[[↑](#cite_ref-3)] [Gentoo has a long history of working with IRC: the Open Projects Network would later become Freenode until what some described as a [\"hostile takeover\"](https://en.wikipedia.org/wiki/Freenode#Ownership_change_and_conflict "wikipedia:Freenode") would [compel Gentoo](https://www.gentoo.org/news/2021/05/26/gentoo-freenode-channels-hijacked.html) to move to [Libera Chat](https://en.wikipedia.org/wiki/Libera_Chat "wikipedia:Libera Chat") - the servers may have changed over the years, but the project remains close to it\'s roots in that respect.]]
4.  [[[↑](#cite_ref-4)] [[https://web.archive.org/web/20101001024709/http://www.gentoo.org/doc/en/articles/making-the-distro-p3.xml](https://web.archive.org/web/20101001024709/http://www.gentoo.org/doc/en/articles/making-the-distro-p3.xml)]]
5.  [[[↑](#cite_ref-5)] []]

    :::::::: cmd-box


    `user `[`$`]`git clone `[`https://anongit.gentoo.org/git/archive/proj/portage-cvs.git`](https://anongit.gentoo.org/git/archive/proj/portage-cvs.git)





    `user `[`$`]`git log --reverse`





    `user `[`$`]`git checkout 8c279bf0b4364a884d902312bc421a963e67f299`





    `user `[`$`]`sed -n '2p' pym/portage.py`





    `user `[`$`]`# Copyright 1998-2000 Daniel Robbins, Gentoo Technologies, Inc.`


    ::::::::
6.  [[[↑](#cite_ref-6)] [Daniel Robbins, Gentoo\'s founder and chief architect or benevolent dictator for life (BDFL), was unable to provide a \"better\" date for when Gentoo was \"officially founded\" when the subject of Gentoo\'s \"birthday\" was researched for the 10th anniversary which was celebrated in 2009]]
7.  [[[↑](#cite_ref-7)] [Before the creation of the Gentoo Foundation, developers were to assign copyright to Gentoo Technologies Inc. The formal [assignment document](https://gitweb.gentoo.org/archive/proj/gentoo.git/tree/xml/htdocs/proj/en/devrel/copyright/assignment.txt?id=c65f28a2b9808b4bc6549ff7efd152adb0a1f9c8) was however only introduced in early 2004, and it was not applied to existing developers, or those that objected.]]
8.  [[[↑](#cite_ref-8)] [[https://archives.gentoo.org/gentoo-dev/message/0d087a4e2fe0864a1cd421029ead3b9e](https://archives.gentoo.org/gentoo-dev/message/0d087a4e2fe0864a1cd421029ead3b9e)]]
9.  [[[↑](#cite_ref-9)] [The Gentoo Foundation Inc. is constrained by the New Mexico Not for Profit Statutes as modified by case law, the [Foundation Bylaws](https://wiki.gentoo.org/wiki/Foundation:Bylaws "Foundation:Bylaws") and the [Foundation Charter](https://wiki.gentoo.org/wiki/Foundation:Main_Page "Foundation:Main Page"). While the Gentoo Foundation Inc. is incorporated as a not-for-profit corporation in the state of New Mexico; it has no 501 tax-exempt status and pays taxes as a normal corporation. Gentoo Technologies Inc. was similarly constrained by the laws of the land but the business management side was handled by Daniel Robbins, Gentoo developers were not involved.]]