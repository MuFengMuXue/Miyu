[Translate this page](//wiki.manjaro.org/index.php?title=Special:Translate&group=page-How-to+verify+GPG+key+of+official+.ISO+images&language=en&action=page&filter= "Special:Translate")

Other languages:

[English](//wiki.manjaro.org/index.php?title=How-to_verify_GPG_key_of_official_.ISO_images "How-to verify GPG key of official .ISO images (100% translated)") • ‎[português do Brasil](//wiki.manjaro.org/index.php?title=How-to_verify_GPG_key_of_official_.ISO_images/pt-br "Como verificar a chave GPG de imagens .ISO oficiais (100% translated)") • ‎[русский](//wiki.manjaro.org/index.php?title=How-to_verify_GPG_key_of_official_.ISO_images/ru "Как проверить GPG-ключ официальных образов .ISO (100% translated)")

## Contents

-   [[1] [Verifying GPG key of official .ISO images]](#Verifying_GPG_key_of_official_.ISO_images)
-   [[2] [Links]](#Links)

# [Verifying GPG key of official .ISO images]

**1.** Download an ISO file and the corresponding .sig file from the official sources (see Download Manjaro below).

**2.** Install GPG and wget using a Manjaro package manager (pamac or pacman):

      pamac install gnupg wget

**3.** Next, you have 2 possible ways to import Manjaro\'s keys. Choose one of them:

Download all keys from the Manjaro Developers from GitLab:

    wget gitlab.manjaro.org/packages/core/manjaro-keyring/-/raw/master/manjaro.gpg

Next, import all the keys in the downloaded .gpg file into your gnupg keyring:

    gpg --import manjaro.gpg

If you do not trust GitLab, import the Manjaro Build Server\'s GPG key to your system (afterwards, select the key by entering its number and pressing ENTER):

    gpg --keyserver keyserver.ubuntu.com --search-keys Manjaro Build Server

**4.** Finally, verify if the .iso image file was built by the Manjaro Build Server, Philip Müller or one of the other Manjaro Developers:

    gpg --verify manjaro-ISO-image.iso.sig manjaro-ISO-image.iso

Compare the key which was used to sign the .iso file with the corresponding developer key.

Check whether the .ISO was verified by Philip Müller\'s GPG key, another Manjaro Developer\'s key, or the Manjaro Build Server key which you have imported to your system. If this is the case, you can be sure that your .iso is official.

# [Links]

-   **[Download Manjaro](//wiki.manjaro.org/index.php?title=Download_Manjaro "Download Manjaro")**
-   **[Check a Downloaded ISO Image For Errors](//wiki.manjaro.org/index.php?title=Check_a_Downloaded_ISO_Image_For_Errors "Check a Downloaded ISO Image For Errors")**
-   **[Burn an ISO File](//wiki.manjaro.org/index.php?title=Burn_an_ISO_File "Burn an ISO File")**
-   **[Installation Guides](//wiki.manjaro.org/index.php?title=Installation_Guides "Installation Guides")**