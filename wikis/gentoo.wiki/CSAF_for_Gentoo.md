This page collects the required information for a possible migration from [GLSA](https://wiki.gentoo.org/wiki/GLSA "GLSA") to CSAF

## Contents

-   [[1] [Comparison of CSAF and GLSA]](#Comparison_of_CSAF_and_GLSA)
-   [[2] [Who uses CSAF already?]](#Who_uses_CSAF_already.3F)
-   [[3] [Steps for a migration]](#Steps_for_a_migration)
-   [[4] [Important tools]](#Important_tools)
-   [[5] [Ideas]](#Ideas)

## [Comparison of CSAF and GLSA]

  -------------------------------------------------------- ----------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------
  Aspect                                                   GLSA                                CSAF
  standardization                                          Gentoo-specific                     International standard
  Announce that Gentoo is not affected by a specific CVE   Not implemented                     Implemented with VEX
  File format                                              XML                                 JSON
  File structure                                           individual files                    one large file
  Automation                                               Manual processing                   Automated processing
  Location                                                 Gentoo website, ebuild repository   [https://gentoo.org/.well-known/csaf-feed-tlp-white.json](https://gentoo.org/.well-known/csaf-feed-tlp-white.json)
  Integration                                              glsa-check                          many tools
  Accessibility                                            needs individual solutions          due to standardization and wide spread it is easy to add multi language support and support for blind users
  -------------------------------------------------------- ----------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------

  : Caption text

## [][Who uses CSAF already?]

Just a few examples, of projects related or similar to Gentoo

-   Redhat ([https://redhat.com/.well-known/security.txt](https://redhat.com/.well-known/security.txt) [https://access.redhat.com/security/data](https://access.redhat.com/security/data))
-   Oracle Linux
-   Suse ([https://www.suse.com/de-de/support/security/csaf/](https://www.suse.com/de-de/support/security/csaf/))
-   Intel ([https://www.intel.com/content/www/us/en/security-center/default.html](https://www.intel.com/content/www/us/en/security-center/default.html))

## [Steps for a migration]

Request for a migration [[[bug #946870]](https://bugs.gentoo.org/show_bug.cgi?id=946870)[]]. GLSA and CSAF can be provided in parallel. There is no interference.

-   create a security.txt without OpenPGP signature for a start [[[bug #688380]](https://bugs.gentoo.org/show_bug.cgi?id=688380)[]]
-   test if the security.txt was setup properly ([https://internet.nl/site/gentoo.org/](https://internet.nl/site/gentoo.org/))
-   add the link to the CSAF JSON file to the security.txt
-   create first advisories with secvisogram
-   write converter to convert old GLSA to CSAF
-   optionally add OpenPGP

## [Important tools]

-   Secvisogram: Edit the whole CSAF locally in the browser [https://github.com/secvisogram/secvisogram](https://github.com/secvisogram/secvisogram)
-   CSAF Specification: [https://csaf.io/](https://csaf.io/)
-   CSAF Tools [https://oasis-open.github.io/csaf-documentation/tools.html](https://oasis-open.github.io/csaf-documentation/tools.html)
-   Slides explaining the benefit of CSAF [https://rg-rhein-main.gi.de/fileadmin/GI/Hauptseite/Netzwerk/Regionalgruppen/20220830_CSAF_BSI.pdf](https://rg-rhein-main.gi.de/fileadmin/GI/Hauptseite/Netzwerk/Regionalgruppen/20220830_CSAF_BSI.pdf)

## [Ideas]

-   Possible project for the Google Summer of Code
-   Discussion on new GLSA schama: [https://archives.gentoo.org/gentoo-dev/?q=%5BRFC%5D+A+new+GLSA+schema](https://archives.gentoo.org/gentoo-dev/?q=%5BRFC%5D+A+new+GLSA+schema)