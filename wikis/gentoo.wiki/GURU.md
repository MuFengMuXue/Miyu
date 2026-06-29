+:-------------------------------------------------------------------------------:+:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:+
| GURU                                                                            |                                                                                                                                                                                                                                                                             |
+---------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Description                                                                     | Ebuild repository entirely maintained by Gentoo users                                                                                                                                                                                                                       |
+---------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [Project email]                       | [guru-devs@gentoo.org](mailto:guru-devs@gentoo.org)                                                                                                                                                                                         |
+---------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [IRC channel] | [[#gentoo-guru](ircs://irc.libera.chat/#gentoo-guru)] ([[webchat](https://web.libera.chat/#gentoo-guru)]) |
+---------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Lead(s)                                                                         | -   [Michał Górny](https://wiki.gentoo.org/wiki/User:MGorny "User:MGorny") (mgorny)\                                                                                                                                                                                        |
|                                                                                 |     *Initiator*                                                                                                                                                                                                                                                             |
|                                                                                 |                                                                                                                                                                                                                                                                             |
|                                                                                 | \                                                                                                                                                                                                                                                                           |
|                                                                                 | No lead election date set                                                                                                                                                                                                                                                   |
+---------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Member(s)                                                                       | -   [Arthur Zamarin](https://wiki.gentoo.org/wiki/User:Arthurzam "User:Arthurzam") (arthurzam)                                                                                                                                                                              |
|                                                                                 | -   [Eli Schwartz](https://wiki.gentoo.org/wiki/User:Eschwartz "User:Eschwartz") (eschwartz)                                                                                                                                                                                |
|                                                                                 | -   [Nowa Ammerlaan](https://wiki.gentoo.org/wiki/User:Nowa "User:Nowa") (Nowa)\                                                                                                                                                                                            |
|                                                                                 |     *Crazy Scientist*                                                                                                                                                                                                                                                       |
|                                                                                 | -   [Viorel Munteanu](https://wiki.gentoo.org/wiki/User:Viorel "User:Viorel") (ceamac)                                                                                                                                                                                      |
+---------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Subproject(s)\                                                                  | (none)                                                                                                                                                                                                                                                                      |
| [(and inherited member(s))]                                             |                                                                                                                                                                                                                                                                             |
+---------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Parent Project                                                                  | [Gentoo](https://wiki.gentoo.org/wiki/Project:Gentoo "Project:Gentoo")                                                                                                                                                                                                      |
+---------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [Project listing](https://wiki.gentoo.org/wiki/Project:Gentoo "Project:Gentoo") |                                                                                                                                                                                                                                                                             |
+---------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

The goal of the GURU project is to create an official repository of new Gentoo packages that are maintained collaboratively by Gentoo users. It follows the tradition of Sunrise project but aims to improve its maintainability by reducing the involvement of Gentoo developers and letting experienced contributors take care of reviewing work of others.

[![](/images/thumb/4/47/GURU.svg/395px-GURU.svg.png)](https://wiki.gentoo.org/wiki/File:GURU.svg)

[](https://wiki.gentoo.org/wiki/File:GURU.svg "Enlarge")

GURU project logo

## Contents

-   [[1] [Disclaimer]](#Disclaimer)
-   [[2] [The regulations]](#The_regulations)
-   [[3] [User roles and responsibilities]](#User_roles_and_responsibilities)
-   [[4] [QA]](#QA)
-   [[5] [Conflict resolution]](#Conflict_resolution)
-   [[6] [Resources]](#Resources)

## [Disclaimer]

Please note that the GURU project is maintained and reviewed entirely by Gentoo users. It is only subject to minimal supervision from individual Gentoo developers, and is not supported by projects such as [Gentoo Security](https://wiki.gentoo.org/wiki/Project:Security "Project:Security"). While our Trusted Contributors do their best to keep GURU safe, it is possible for it to contain vulnerable, badly broken or even malicious software. You are using it on your own responsibility.

## [The regulations]

Every user willing to contribute to the GURU project needs to explicitly agree with the following regulations.

1.  The purpose of GURU project is to maintain a repository that can be reasonably used by Gentoo users. All contributors are responsible for ensuring that the repository is safe to use and free of malicious or severely buggy software.
2.  GURU is an official Gentoo project, and is therefore bound by the official Gentoo policies. In particular, the [Copyright Policy (GLEP 76)](https://www.gentoo.org/glep/glep-0076.html) is binding to all committers.
3.  While following Gentoo ebuild policies and quality standards is recommended, it will not be strictly enforced. More experienced users are encouraged to improve the quality of ebuilds in GURU, and less experienced users are encouraged to learn from those corrections.
4.  Packages in GURU are to have [\~arch] keywords. Stable keywords must not be used.
5.  Packages in GURU are community maintained. While users are encouraged to list themselves as maintainers and take explicit responsibility for their packages, it is acceptable for others to commit improvements to those packages and to commit packages without an explicit maintainer. One should still both aim for consensus and also reach out to the current maintainer or previous folks who touched the ebuild as a courtesy.
6.  At the same time, users are asked to maintain respectful and professional behavior, and to attempt to maintain a good quality of GURU overall.
7.  Users that list themselves as maintainers must use an e-mail address known to bugs.gentoo.org in metadata.xml and keep it up to date in case it changes.
8.  Contributors should refrain from adding packages that they cannot reasonably maintain, due to, for example, the complexity, scope, or quantity of the added work. Adding rough drafts of ebuilds with the hope that someone else will fix them up and no intent of doing so yourself is not acceptable. Adding packages in bulk should be avoided.
9.  Packages in GURU must solve a problem that cannot be reasonably achieved using simpler methods. In other words, there should be some rationale for an ebuild to be an ebuild instead of, for example, a wget script or config snippet.
10. With very few exceptions, such as virtuals or meta-packages, new packages in GURU should have an upstream (meaning SRC_URI should usually be populated). Exceptions must be justified.
11. The primary purpose of GURU is to maintain packages not present in the Gentoo repository. Forking (overriding) actively maintained Gentoo packages into GURU is prohibited. If the package is moved to Gentoo, it should be removed from GURU.
12. News items are permitted in GURU. Before adding a news item, it must be emailed to the gentoo-guru@lists.gentoo.org mailing list and the Trusted Contributors (guru-trusted@gentoo.org) for review and approval.

## [User roles and responsibilities]

GURU notes three classes of users:

-   *Regular contributors* that are permitted to commit to the development (*dev*) branch.
-   *Trusted contributors* that gain additional privilege of merging commits into the reviewed (*master*) branch.
-   *Gentoo developers* who are responsible for handling new user acceptance, enforcement of regulations and taking care of emergencies.

New contributors request access via [filing a bug in GURU product](https://bugs.gentoo.org/enter_bug.cgi?product=GURU&component=Access+requests) and stating their agreement to the regulations. A Gentoo developer grants access to the repository.

Regular contributors perform their work on the development branch. This work is afterwards reviewed by trusted contributors and/or Gentoo developers. They either inform the authors of necessary changes or fix the ebuilds themselves. Whenever the final status is good enough, they merge the changes to the reviewed (master) branch.

The trusted contributor status is granted by Gentoo developers based on previous good work done in GURU. Trusted contributors are generally expected to be responsible for ensuring that the repository is free of malicious or otherwise dangerous code, and for preventing it from reaching the end users via the reviewed branch.

Gentoo developers can join the project at their leisure. Their main role is taking care of technical requests from users, granting trusted contributor privileges and preventing abuse.

## [QA]

While project is maintained and reviewed entirely by Gentoo users, [Tinderbox](https://wiki.gentoo.org/wiki/Project:Tinderbox "Project:Tinderbox") project builds GURU packages on a regular basis to find common mistakes.

## [Conflict resolution]

If an unresolvable disagreement arises between (trusted) contributors or between contributors and users, follow the steps below:

1.  Involve (the other) Trusted Contributors via e-mail to the mailing list or bugs.gentoo.org. If this does not lead to an acceptable resolution then,
2.  Hold a formal vote on bugs.gentoo.org among the Trusted Contributors on how the conflict should be resolved. The issue may be escalated to the Gentoo Developers involved in GURU if this is the conclusion of the vote, or if the involved parties wish to appeal the conclusion of the vote.
3.  If the issue still cannot be resolved via discussion with the Gentoo Developers involved in GURU, then they too will hold a vote to decide how the matter should be resolved,

In this process, the following conditions apply:

1.  A decision to revoke access to the dev or master branch, whether temporarily or permanent, must involve the Gentoo Developers that are a member of the GURU project.
2.  A decision to permanently revoke access to the dev or master branch should be preceded by a formal warning, a preceding temporary suspension of access counts as a warning. Only in extreme cases, such as malevolent behaviour, may this warning be skipped.
3.  To keep track of them, formal warnings and suspensions are noted in the contributor\'s access request bug.
4.  A Trusted Contributor who is the subject of a vote, may not participate in this vote.
5.  Policies and guidelines of the Community Relations project with regards to developer-user conflict apply here as well.

## [Resources]

Technical resources:

-   [repo/proj/guru.git on cgit](https://gitweb.gentoo.org/repo/proj/guru.git): web UI to the repository
-   [open GURU bugs](https://bugs.gentoo.org/buglist.cgi?product=GURU&resolution=---)

Commit feeds:

-   [dev branch](https://cgit.gentoo.org/repo/proj/guru.git/atom/?h=dev)
-   [master branch](https://cgit.gentoo.org/repo/proj/guru.git/atom/)

GURU guides:

-   [Information for End Users](https://wiki.gentoo.org/wiki/Project:GURU/Information_for_End_Users "Project:GURU/Information for End Users")
-   [Information for Contributors](https://wiki.gentoo.org/wiki/Project:GURU/Information_for_Contributors "Project:GURU/Information for Contributors")
-   [Information for Trusted Contributors](https://wiki.gentoo.org/wiki/Project:GURU/Information_for_Trusted_Contributors "Project:GURU/Information for Trusted Contributors")
-   [Information for Gentoo Developers](https://wiki.gentoo.org/wiki/Project:GURU/Information_for_Gentoo_Developers "Project:GURU/Information for Gentoo Developers")

Useful development documentation:

-   [Devmanual --- Gentoo Developer Guide](http://devmanual.gentoo.org)
-   [Proxy-maint project user guide](https://wiki.gentoo.org/wiki/Project:Proxy_Maintainers/User_Guide "Project:Proxy Maintainers/User Guide") (not strictly suited to GURU but contains many useful tips)
-   [GLEP 76: Copyright Policy](https://www.gentoo.org/glep/glep-0076.html) (obligatory)
-   [GLEP 63: Gentoo OpenPGP Policies](https://www.gentoo.org/glep/glep-0063.html) (recommended)
-   [GLEP 66: Gentoo Git Workflow](https://www.gentoo.org/glep/glep-0066.html) (recommended)