In order to aid new community members and harden concepts for existing ones, this article aims to serve as a location to collect terms, definitions, acronyms, colloquialisms, expressions, and all other types of jargon known to the Gentoo community.

As with any unique distribution with a storied history, specific colloquialisms such as \"Portage tree\", or deprecated terminology such as \"Herds\" have influenced conversation in the Gentoo community. These are the types of community-specific terminology that this article will try to document.

[   Note to editors] []

If possible, entries under each section should list a link or other type of authoritative upstream citation. Archive.org links are welcome, but only if necessary (example: when citing information from the original Gentoo.org site).

\

Please focus on the not-so-common abbreviations which are important in the Gentoo universe. Well-known general abbreviations like CPU or SCSI would not fit here.

## Contents

-   [[1] [Abbreviations]](#Abbreviations)
-   [[2] [Terminology and jargon]](#Terminology_and_jargon)
-   [[3] [Deprecated terminology]](#Deprecated_terminology)

## [Abbreviations]

  -------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Short form                                         Long form                                                                                                                           Explanation
  ABI                                                Application Binary Interface                                                                                                        [Application binary interface](https://wiki.gentoo.org/wiki/Application_binary_interface "Application binary interface")
  API                                                Application Programming interface                                                                                                   [wikipedia:API](https://en.wikipedia.org/wiki/Application_programming_interface "wikipedia:Application programming interface")
  AT                                                 Arch Testers                                                                                                                        [Project:AMD64 Arch Testers](https://wiki.gentoo.org/wiki/Project:AMD64_Arch_Testers "Project:AMD64 Arch Testers"), [Project:X86_Arch_Testers](https://wiki.gentoo.org/wiki/Project:X86_Arch_Testers "Project:X86 Arch Testers"), [Project:SPARC/Arch tester](https://wiki.gentoo.org/wiki/Project:SPARC/Arch_tester "Project:SPARC/Arch tester"), [Project:Alpha/Arch tester](https://wiki.gentoo.org/wiki/Project:Alpha/Arch_tester "Project:Alpha/Arch tester")
  BGO/bgo/b.g.o                                      bugs.gentoo.org                                                                                                                     [Gentoo Bugtracker](https://bugs.gentoo.org)^[\[1\]](#cite_note-unofficial-1)^
  CI                                                 Continuous Integration                                                                                                              [wikipedia:CI](https://en.wikipedia.org/wiki/Continuous_integration "wikipedia:Continuous integration")
  CLA                                                Contributor License Agreement                                                                                                       [wikipedia:CLA](https://en.wikipedia.org/wiki/Contributor_License_Agreement "wikipedia:Contributor License Agreement")
  CLI                                                Command Line Interface                                                                                                              [The Command Line Interface](https://wiki.gentoo.org/wiki/Shell#The_Command_Line_Interface "Shell")
  CoC                                                Code of Conduct                                                                                                                     [Project:Council/Code of conduct](https://wiki.gentoo.org/wiki/Project:Council/Code_of_conduct "Project:Council/Code of conduct")
  ComRel                                             Community Relations                                                                                                                 [Project:ComRel](https://wiki.gentoo.org/wiki/Project:ComRel "Project:ComRel")
  [EAPI](https://wiki.gentoo.org/wiki/EAPI "EAPI")   Ebuild API                                                                                                                          The term [ebuild API](https://devmanual.gentoo.org/eclass-reference/ebuild/) was [invented on the gentoo-dev mailing list](https://archives.gentoo.org/gentoo-dev/message/881f6757d8ed8d0e395359c3832a6073)
  GGO/ggo/g.g.o                                      gitweb.gentoo.org                                                                                                                   [Official Gentoo git repositories](https://gitweb.gentoo.org) for [Gentoo development](https://wiki.gentoo.org/wiki/Category:Gentoo_development "Category:Gentoo development")
  GH                                                 GitHub                                                                                                                              GitHub hosts the [official mirror](https://github.com/gentoo) of Gentoo git repositories ^[\[1\]](#cite_note-unofficial-1)^
  GLEP                                               Gentoo Linux Enhancement Proposal                                                                                                   [Project:GLEP](https://wiki.gentoo.org/wiki/Project:GLEP "Project:GLEP")
  GLSA                                               Gentoo Linux Security Advisories                                                                                                    [GLSA](https://wiki.gentoo.org/wiki/GLSA "GLSA")
  HB                                                 The Gentoo handbook                                                                                                                 [Handbook:Main Page](https://wiki.gentoo.org/wiki/Handbook:Main_Page "Handbook:Main Page")
  IOMMU                                              Input--output memory management unit                                                                                                [wikipedia:IOMMU](https://en.wikipedia.org/wiki/Input%E2%80%93output_memory_management_unit)
  LTO                                                Link Time Optimization                                                                                                              [LTO](https://wiki.gentoo.org/wiki/LTO "LTO")
  m-n                                                maintainer needed                                                                                                                   As in \"this package is set to *maintainer needed* status\"^[\[1\]](#cite_note-unofficial-1)^
  PGO                                                Profile Guided Optimization                                                                                                         [Profile Guided Optimization](https://wiki.gentoo.org/wiki/GCC_optimization#Profile_Guided_Optimization_.28PGO.29 "GCC optimization")
  p.g.o                                              packages.gentoo.org                                                                                                                 [packages.gentoo.org](https://wiki.gentoo.org/wiki/Packages.gentoo.org "Packages.gentoo.org") website providing information about packages in the current Gentoo ebuild repository
  PIC                                                Position-Independent Code                                                                                                           [wikipedia:PIC](https://en.wikipedia.org/wiki/Position-independent_code "wikipedia:Position-independent code")
  PIE                                                Position-Independent Executables                                                                                                    a security hardening technique; [wikipedia:PIE](https://en.wikipedia.org/wiki/Position-independent_code "wikipedia:Position-independent code")
  PM                                                 Package Manager                                                                                                                     [wikipedia:PM](https://en.wikipedia.org/wiki/Package_manager "wikipedia:Package manager")
  PMASKED                                            package masked (listed in packages.mask)                                                                                            [PMASKED in bug tickets](https://bugs.gentoo.org/buglist.cgi?keywords=PMASKED&resolution=---)^[\[1\]](#cite_note-unofficial-1)^
  PMS                                                Package Manager Specification                                                                                                       [Package Manager Specification](https://wiki.gentoo.org/wiki/Package_Manager_Specification "Package Manager Specification"), see also [Project:Package Manager Specification](https://wiki.gentoo.org/wiki/Project:Package_Manager_Specification "Project:Package Manager Specification") and [latest HTML rendering](https://dev.gentoo.org/~ulm/pms/head/pms.html).
  PR                                                 Pull Request                                                                                                                        [Project:GitHub/Pull_requests](https://wiki.gentoo.org/wiki/Project:GitHub/Pull_requests "Project:GitHub/Pull requests"), [Creating_GitHub_Pull_Requests](https://wiki.gentoo.org/wiki/Creating_GitHub_Pull_Requests "Creating GitHub Pull Requests"), [Gentoo_git_workflow](https://wiki.gentoo.org/wiki/Gentoo_git_workflow "Gentoo git workflow") ^[\[1\]](#cite_note-unofficial-1)^
  p-m                                                Proxy Maintainer                                                                                                                    [Project:Proxy Maintainers](https://wiki.gentoo.org/wiki/Project:Proxy_Maintainers "Project:Proxy Maintainers")
  QA                                                 Quality assurance                                                                                                                   [Project:Quality Assurance](https://wiki.gentoo.org/wiki/Project:Quality_Assurance "Project:Quality Assurance")
  SLOT                                               SLOTs allow multiple versions of a package to be installed                                                                          [SLOT](https://wiki.gentoo.org/wiki/SLOT "SLOT")
  SOB                                                Signed Off By                                                                                                                       \...
  stablereq                                          Stabilization Request                                                                                                               [Stable request](https://wiki.gentoo.org/wiki/Stable_request "Stable request")
  VDB                                                [/var/db/pkg] - database of installed packages   [/var/db/pkg](https://wiki.gentoo.org/wiki//var/db/pkg "/var/db/pkg") ^[\[1\]](#cite_note-unofficial-1)^
  -------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## [Terminology and jargon]

According to Wikipedia, [jargon](https://en.wikipedia.org/wiki/jargon "wikipedia:jargon") is the specialized terminology associated with a particular field or area of activity. In Gentoo, this means terms such as [Portage](https://wiki.gentoo.org/wiki/Portage "Portage"), [ebuild repository](https://wiki.gentoo.org/wiki/Ebuild_repository "Ebuild repository"), [Profiles](https://wiki.gentoo.org/wiki/Profile_(Portage) "Profile (Portage)"), and others that are not quickly or easily understood by [etymology](https://en.wikipedia.org/wiki/etymology "wikipedia:etymology") alone.

Ebuild repository

<!-- -->

emerge

<!-- -->

dist kernel\
dk

Gentoo ebuild repository

Gentoo repository

Gentoo repo

<!-- -->

gentoo.git

<!-- -->

[Meta ebuild](https://wiki.gentoo.org/wiki/Meta_ebuilds "Meta ebuilds")

Meta package

<!-- -->

p.use

p.a_k

p.mask

<!-- -->

[Portage](https://wiki.gentoo.org/wiki/Portage "Portage")

<!-- -->

[Tinderbox](https://zwiebeltoralf.de/tinderbox.html)

<!-- -->

Upstream

## [Deprecated terminology]

These terms were once more common, but because of the evolution of Gentoo over the years they are now rarely used or no longer applicable. They are listed here for historical reasons and because they may still be encountered in content that has not been kept up to date.

[Genkernel](https://wiki.gentoo.org/wiki/Genkernel "Genkernel")\
gk

<!-- -->

Gentoo tree

Portage tree

rsync tree

\"the tree\"

<!-- -->

Herd

1.  [[↑ ^[1.0](#cite_ref-unofficial_1-0)^ ^[1.1](#cite_ref-unofficial_1-1)^ ^[1.2](#cite_ref-unofficial_1-2)^ ^[1.3](#cite_ref-unofficial_1-3)^ ^[1.4](#cite_ref-unofficial_1-4)^ ^[1.5](#cite_ref-unofficial_1-5)^] [This abbreviation is not official, but very often used in chats.]]