**Secure Boot** est un renforcement de la sécurité du processus de pré-amorçage d\'un système [UEFI](https://wiki.gentoo.org/wiki/UEFI "UEFI"). Lorsqu\'il est activé, le micrologiciel UEFI vérifie la signature de chaque composant utilisé dans le processus de démarrage. Il en résulte des fichiers de démarrage facilement lisibles, mais inviolables.

## Contents

-   [[1] [Introduction]](#Introduction)
    -   [[1.1] [Cryptographie]](#Cryptographie)
    -   [[1.2] [Composants]](#Composants)
    -   [[1.3] [Formats de clés]](#Formats_de_cl.C3.A9s)
    -   [[1.4] [Implémentation]](#Impl.C3.A9mentation)
        -   [[1.4.1] [Stockage des clés]](#Stockage_des_cl.C3.A9s)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [USE flags]](#USE_flags)
    -   [[2.2] [Emerge]](#Emerge)
-   [[3] [Génération de nouvelles clés]](#G.C3.A9n.C3.A9ration_de_nouvelles_cl.C3.A9s)
    -   [[3.1] [Génération d\'un UUID]](#G.C3.A9n.C3.A9ration_d.27un_UUID)
    -   [[3.2] [Création de clé à protection asymétrique par lots]](#Cr.C3.A9ation_de_cl.C3.A9_.C3.A0_protection_asym.C3.A9trique_par_lots)
    -   [[3.3] [Création manuelle de clés]](#Cr.C3.A9ation_manuelle_de_cl.C3.A9s)
    -   [[3.4] [Création des nouvelles listes de signatures]](#Cr.C3.A9ation_des_nouvelles_listes_de_signatures)
        -   [[3.4.1] [Création par lots]](#Cr.C3.A9ation_par_lots)
        -   [[3.4.2] [Création manuelle]](#Cr.C3.A9ation_manuelle)
    -   [[3.5] [Création du fichier DER (optionnel)]](#Cr.C3.A9ation_du_fichier_DER_.28optionnel.29)
-   [[4] [Préparation des clés]](#Pr.C3.A9paration_des_cl.C3.A9s)
    -   [[4.1] [Combinaison des Signature Lists]](#Combinaison_des_Signature_Lists)
        -   [[4.1.1] [Concaténation par lots]](#Concat.C3.A9nation_par_lots)
        -   [[4.1.2] [Concaténation manuelle]](#Concat.C3.A9nation_manuelle)
        -   [[4.1.3] [Copie de la Platform Key]](#Copie_de_la_Platform_Key)
    -   [[4.2] [Signature des Signature Lists]](#Signature_des_Signature_Lists)
        -   [[4.2.1] [Platform Key]](#Platform_Key)
            -   [[4.2.1.1] [Clé de réinitialisation]](#Cl.C3.A9_de_r.C3.A9initialisation)
        -   [[4.2.2] [Key Exchange Keys]](#Key_Exchange_Keys)
        -   [[4.2.3] [Signature Databases]](#Signature_Databases)
-   [[5] [Installation des clés]](#Installation_des_cl.C3.A9s)
    -   [[5.1] [Installation de la Key Exchange Key]](#Installation_de_la_Key_Exchange_Key)
    -   [[5.2] [Installation des Database Keys]](#Installation_des_Database_Keys)
    -   [[5.3] [Installation de la Platform Key]](#Installation_de_la_Platform_Key)
-   [[6] [Signature des fichiers de boot]](#Signature_des_fichiers_de_boot)
    -   [[6.1] [Signature]](#Signature)
        -   [[6.1.1] [Création d\'une entrée dans le gestionnaire de démarrage EFI]](#Cr.C3.A9ation_d.27une_entr.C3.A9e_dans_le_gestionnaire_de_d.C3.A9marrage_EFI)
    -   [[6.2] [Vérification des signatures]](#V.C3.A9rification_des_signatures)
    -   [[6.3] [Liste des signatures]](#Liste_des_signatures)
-   [[7] [Vérification de l\'état de Secure Boot]](#V.C3.A9rification_de_l.27.C3.A9tat_de_Secure_Boot)
    -   [[7.1] [efivar]](#efivar)
        -   [[7.1.1] [Liste des variables]](#Liste_des_variables)
-   [[8] [Réinitialisation de la Platform Key]](#R.C3.A9initialisation_de_la_Platform_Key)
-   [[9] [Voir également]](#Voir_.C3.A9galement)
-   [[10] [References]](#References)

## [Introduction]

La mise en place de Secure Boot peut améliorer de manière significative la sécurité d\'un système. L\'intégrité de la chaîne de démarrage est extrêmement importante. Si un code malveillant parvient à interférer avec le processus d\'amorçage, de nombreuses autres mesures de sécurité sont neutralisées. Cet article explique en détail comment interagir avec le processus de démarrage sécurisé. Pour faire fonctionner le système de démarrage sécurisé, un programme comme [[[app-crypt/sbctl]](https://packages.gentoo.org/packages/app-crypt/sbctl)[]] peut être utilisé.

### [Cryptographie]

Le système UEFI Secure Boot utilise généralement **RSA-2048** et **sha256** pour effectuer la *cryptographie à clé publique*.

** Note**\
Certaines implémentations de l\'UEFI peuvent prendre en charge d\'autres algorithmes et tailles de clés.

Les clés publiques de Secure Boot doivent être stockées au format **X.509**.

** Important**\
Les clés privées utilisées pour signer les fichiers de démarrage doivent être conservées en toute sécurité. En cas de fuite, elles pourraient être utilisées pour signer des fichiers de démarrage malveillants.

### [Composants]

Secure Boot met généralement en œuvre les clés et listes suivantes ^[\[1\]](#cite_note-1)[\[2\]](#cite_note-2)[\[3\]](#cite_note-3)^ :

-   **PK** - *Platform Key* - Composée de deux parties, *PKpub* (la clé publique) et *PKpriv* (la clé privée), utilisé pour signer la KEK.
-   **KEK** - *Key Exchange Key* - Clé utilisée pour signer la base de données des *signatures* et des *signatures interdites* ; il peut y en avoir plusieurs.
-   **db** - *Signature Database)* - Contient des listes de clés publiques, de signatures et de hachages autorisés dans la chaîne de démarrage.
-   **dbx** - *Forbidden Signature Database* - Le contraire de la base de données des signatures, des clés publiques, des signatures et des hachages qui ne devraient jamais être autorisés à démarrer.

** Important**\
Une seule *clé de plate-forme* peut être utilisée sur un système, chaque autre type étant en fait une liste ou une \"*base de données*\". Il est courant d\'inclure la *Clé d\'échange de clés*, du fabricant de l\'appareil, et parfois celle de Microsoft. Sur certains appareils, la suppression de l\'une ou l\'autre de ces clés peut désactiver toute sortie vidéo..

### [][Formats de clés]

Plusieurs formats et extensions de clés sont utilisés avec Secure Boot :

-   **.key** - *PEM* - Utilisé pour les clés privées.
-   **.crt** - *PEM* - Utilisé pour les clés publiques.
-   **.cer** - *DER* - Utilisé pour les clés publiques.
-   **.esl** - *EFI Signature List* - Utilisé par l\'EFI, un ensemble de clés publiques et de hachages..
-   **.auth** - *Signed EFI Signature List* - Utilisé par l\'EFI, forme signée d\'un esl.

### [][Implémentation]

La solidité de Secure Boot dépend de sa mise en œuvre. L\'UEFI doit être protégée par des mots de passe, faute de quoi un pirate pourrait simplement désactiver le système Secure Boot et le contourner. En outre, un stockage de clés faible peut rendre inutiles toutes les protections fournies par Secure Boot.

La sécurité physique joue un rôle important dans le bon fonctionnement du système Secure Boot. Même si un mot de passe administrateur est défini pour le micrologiciel d\'un système, la réinitialisation du CMOS en retirant la batterie ou en utilisant un cavalier/bouton sur la carte mère réinitialisera souvent les mots de passe. En outre, le mot de passe UEFI de certains ordinateurs portables peut être facilement réinitialisé.

#### [][Stockage des clés]

Secure Boot stocke les clés publiques et les listes de signatures, généralement dans la NVRAM de la carte mère. Cette région de la mémoire est généralement lisible une fois le système démarré, mais ne peut être écrite qu\'à l\'aide du micrologiciel EFI. Par exemple, **efibootmgr** est utilisé pour ajuster l\'ordre de démarrage lorsque le système est en cours d\'exécution. La mémoire des clés Secure Boot est généralement en lecture seule et, selon l\'implémentation, les variables ne peuvent être écrites qu\'une seule fois en mode configuration. Les microprogrammes UEFI peuvent prendre en charge la mise à jour en utilisant correctement les fichiers .auth, mais cela n\'est pas universel.

** Warning**\
Certains UEFI permettent le chargement de clés inappropriées/sécurisées, telles que des clés *db* et *KEK* qui ne correspondent pas, ou le chargement *esl* sans autorisation lors de la configuration de l\'UEFI.

## [Installation]

### [USE flags]

### [USE flags for] [app-crypt/efitools](https://packages.gentoo.org/packages/app-crypt/efitools) [[]] [Tools for manipulating UEFI secure boot platforms]

  --------------------------------------------------------- -----------------------------------------------------------------------------------------------------
  [`static`](https://packages.gentoo.org/useflags/static)   !!do not set this during bootstrap!! Causes binaries to be statically linked instead of dynamically
  --------------------------------------------------------- -----------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-02-14 09:04] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [USE flags for] [app-crypt/sbsigntools](https://packages.gentoo.org/packages/app-crypt/sbsigntools) [[]] [Utilities for signing and verifying files for UEFI Secure Boot]

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-03-22 00:28] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [USE flags for] [dev-libs/openssl](https://packages.gentoo.org/packages/dev-libs/openssl) [[]] [Robust, full-featured Open Source Toolkit for the Transport Layer Security (TLS)]

  ----------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------
  [`+asm`](https://packages.gentoo.org/useflags/+asm)                           Enable using assembly for optimization
  [`+quic`](https://packages.gentoo.org/useflags/+quic)                         Enable support for QUIC (RFC 9000); a UDP-based protocol intended to replace TCP
  [`fips`](https://packages.gentoo.org/useflags/fips)                           Enable FIPS provider
  [`ktls`](https://packages.gentoo.org/useflags/ktls)                           Enable support for Kernel implementation of TLS (kTLS)
  [`rfc3779`](https://packages.gentoo.org/useflags/rfc3779)                     Enable support for RFC 3779 (X.509 Extensions for IP Addresses and AS Identifiers)
  [`sctp`](https://packages.gentoo.org/useflags/sctp)                           Support for Stream Control Transmission Protocol
  [`static-libs`](https://packages.gentoo.org/useflags/static-libs)             Build static versions of dynamic libraries as well
  [`test`](https://packages.gentoo.org/useflags/test)                           Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`tls-compression`](https://packages.gentoo.org/useflags/tls-compression)     Enable support for discouraged TLS compression
  [`vanilla`](https://packages.gentoo.org/useflags/vanilla)                     Do not add extra patches which change default behaviour; DO NOT USE THIS ON A GLOBAL SCALE as the severity of the meaning changes drastically
  [`verify-sig`](https://packages.gentoo.org/useflags/verify-sig)               Verify upstream signatures on distfiles
  [`weak-ssl-ciphers`](https://packages.gentoo.org/useflags/weak-ssl-ciphers)   Build support for SSL/TLS ciphers that are considered \"weak\"
  ----------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-04-18 23:14] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

Sur les paquets avec l\'USE flag global de `secureboot`, ce flag peut être activé pour signer automatiquement tous les exécutables EFI installés par le paquet. Lorsque cette option est activée, les variables d\'environnement `SECUREBOOT_SIGN_KEY` et `SECUREBOOT_SIGN_CERT` doivent être utilisées pour spécifier la clé (ou le pkcs11 URI) et le certificat à utiliser pour la signature.

[FILE] **`/etc/portage/make.conf`make.conf**

    SECUREBOOT_SIGN_KEY="..."
    SECUREBOOT_SIGN_CERT="..."

Outre le noyau lui-même, les modules du noyau doivent également être signés pour démarrer avec succès lorsque l\'option Secure Boot est activée. À cette fin, l\'use flag global `modules-sign` peut être utilisé en plus des variables d\'environnement `MODULES_SIGN_KEY` et `MODULES_SIGN_HASH`.

### [Emerge]

`root `[`#`]`emerge --ask app-crypt/efitools`

`root `[`#`]`emerge --ask app-crypt/sbsigntools`

`root `[`#`]`emerge --ask dev-libs/openssl`

Sauvegarde des clés existantes

** Warning**\
Le fait de mettre le système en *mode de configuration* supprime toutes les clés présentes, des sauvegardes doivent être effectuées avant d\'entrer en *mode de configuration*.

**efi-readvar** peut être utilisé pour afficher le contenu **public** de la base de données des signatures UEFI.

Les clés peuvent être sauvegardées en utilisant :

`~/secure_boot/factory_config $``for key_type in PK KEK db dbx; do efi-readvar -v $key_type -o $.esl; done`

Il est également possible d\'enregistrer manuellement chaque var en utilisant :

`~/secure_boot/factory_config $``efi-readvar -v PK -o PK.esl`

`~/secure_boot/factory_config $``efi-readvar -v KEK -o KEK.esl`

`~/secure_boot/factory_config $``efi-readvar -v db -o db.esl`

`~/secure_boot/factory_config $``efi-readvar -v dbx -o dbx.esl`

** Tip**\
Veillez à ce que ces clés soient stockées de manière à ce que leur origine soit claire. Ce guide les place dans un répertoire séparé, elles seront utilisées plus tard.

## [][Génération de nouvelles clés]

OpenSSL peut être utilisé pour générer les clés de Secure Boot.

Au minimum, les clés **PK**, **KEK** et **db** doivent être créées. Chacune de ces clés peut être créée de la même manière.

** Important**\
Lors de la génération des clés, assurez-vous qu\'elles ne sont pas écrites sur un support non chiffré ou dans un endroit facilement accessible. Chiffrer les fichiers de clés privées est une étape facultative, mais qui renforce considérablement la sécurité.

** Note**\
Le processus de renouvellement des clés de Secure Boot étant assez lourd, une période d\'expiration de 10 ans est généralement utilisée ; elle peut être réduite ou prolongée, mais doit être renouvelée lorsque les clés expirent.

** Note**\
Les entrées dans les *listes de signatures EFI* doivent recevoir un *GUID* (*UUID*), qui doit être unique, mais qui peut être tout ce qui correspond à ce format. L\'*UUID* choisi ne doit pas nécessairement être le même pour tous les composants, mais cette pratique peut aider à l\'organisation.

### [][Génération d\'un UUID]

Pour générer un *UUID* avec **uuidgen**, et l\'écrire dans [uuid.txt] :

** Note**\
**uuidgen** utilise par défaut [/dev/random] si possible.

### [][Création de clé à protection asymétrique par lots]

Pour créer un fichier chiffré GPG pour chaque type de clé (*PK*, *KEK*, *db*, *dbx*) :

`~/secure_boot/custom_config $``mkfifo key_pipe & sleep 1 && for key_type in PK KEK db dbx; do openssl req -new -x509 -newkey rsa:2048 -subj "/CN=Larry's $" -keyout key_pipe -out $.crt -days 9999 -nodes -sha256 & gpg --output $.key.gpg --recipient larry@gentoo.org --encrypt < key_pipe ; done ; rm key_pipe`

Cela équivaut à :

`~/secure_boot/custom_config $``mkfifo key_pipe &`

`~/secure_boot/custom_config $``openssl req -new -x509 -newkey rsa:2048 -subj "/CN=Larry's PK" -keyout key_pipe -out PK.crt -days 9999 -nodes -sha256 &`

`~/secure_boot/custom_config $``gpg --output PK.key.gpg --recipient larry@gentoo.org --encrypt < key_pipe`

`~/secure_boot/custom_config $``openssl req -new -x509 -newkey rsa:2048 -subj "/CN=Larry's KEK" -keyout key_pipe -out KEK.crt -days 9999 -nodes -sha256 &`

`~/secure_boot/custom_config $``gpg --output KEK.key.gpg --recipient larry@gentoo.org --encrypt < key_pipe`

`~/secure_boot/custom_config $``openssl req -new -x509 -newkey rsa:2048 -subj "/CN=Larry's db" -keyout key_pipe -out db.crt -days 9999 -nodes -sha256 &`

`~/secure_boot/custom_config $``gpg --output db.key.gpg --recipient larry@gentoo.org --encrypt < key_pipe`

`~/secure_boot/custom_config $``openssl req -new -x509 -newkey rsa:2048 -subj "/CN=Larry's dbx" -keyout key_pipe -out dbx.crt -days 9999 -nodes -sha256 &`

`~/secure_boot/custom_config $``gpg --output dbx.key.gpg --recipient larry@gentoo.org --encrypt < key_pipe`

`~/secure_boot/custom_config $``rm key_pipe`

### [][Création manuelle de clés]

Pour créer une paire de clés *Platform Key* sans protéger le *PKpriv* :

`~/secure_boot/custom_config $``openssl req -new -x509 -newkey rsa:2048 -subj "/CN=Larry's Platform Key" -keyout PK.key -out PK.crt -days 9999 -nodes -sha256`

** Note**\
Le *Common Name* sélectionné pour le certificat peut être quelconque, mais doit être descriptif.

Pour que GPG chiffre immédiatement le PKpriv afin d\'assurer une protection supplémentaire, il est possible d\'utiliser un tube nommé :

** Note**\
Le **destinataire** doit correspondre à la clé utilisée pour crypter les fichiers clés. L\'option **-c** peut être utilisée à la place pour chiffrer symétriquement les fichiers créés.

`~/secure_boot/custom_config $``mkfifo key_pipe & sleep 1; openssl req -new -x509 -newkey rsa:2048 -subj "/CN=Larry's Platform Key" -keyout key_pipe -out PK.crt -days 9999 -nodes -sha256 & gpg --output PK.key.gpg --recipient larry@gentoo.org --encrypt < key_pipe && rm key_pipe`

** Note**\
Cette opération prend une seconde, parce qu\'il y a un risque que le tube nommé ne soit pas créé au moment où openssl tente de générer les clés.

Ce processus peut être répété pour la *Key Exchange Key* (**KEK**), la *Signature Database Key* (**db**) et, éventuellement, la *Forbidden Signature Database Key* (**dbx**).

### [][Création des nouvelles listes de signatures]

**cert-to-efi-list** peut être utilisé pour créer un fichier *.esl* à l\'aide d\'un fichier *.crt*. Cette liste de signatures peut ensuite être signée à l\'aide de **sign-efi-sign-list** et de la clé privée. Pour effectuer ces actions sur la *Platform Key* qui a été chiffrée par GPG :

#### [][Création par lots]

Ce processus peut être effectué par lots :

`~/secure_boot/custom_config $``for key_type in PK KEK db dbx; do cert-to-efi-sig-list -g $(< uuid.txt) $.crt $.esl; done`

#### [][Création manuelle]

La *Signing List* pour la *Platform Key* peut être créée à l\'aide de :

`~/secure_boot/custom_config $``cert-to-efi-sig-list -g $(< uuid.txt) PK.crt PK.esl`

** Note**\
Cette opération prend [PK.crt] en entrée et génère [PK.esl] en sortie. À ce stade, rien n\'est signé.

Ce processus doit être répété pour chaque autre type de clé utilisé.

### [][Création du fichier DER (optionnel)]

Pour créer un fichier *DER* (*.cer*) pour chacune des clés générées :

`~/secure_boot/custom_config $``for key_type in `[`PK KEK db dbx`]`; do openssl x509 -outform `[`DER`]` -in $.crt -out $.`[`cer`]` ; done`

## [][Préparation des clés]

Une fois les nouvelles clés créées, elles doivent être combinées avec les clés existantes, formatées et signées pour être utilisées.

### [Combinaison des Signature Lists]

Les *Signature Lists* créées ne sont pas remplies, il est souvent judicieux de commencer par utiliser les clés d\'usine, qui peuvent être supprimées ultérieurement si nécessaire.

** Important**\
Certains systèmes nécessitent le chargement de pilotes GPU signés avec des clés d\'usine. Si Secure Boot est activé, mais que la validation échoue pour ces fichiers, la sortie graphique sera interrompue. Dans ce cas, Secure Boot devra être désactivé sans en-tête pour restaurer le système.

#### [][Concaténation par lots]

Pour concaténer toutes les nouvelles et anciennes *Signature Lists* :

`~/secure_boot $``for key_type in `[`KEK db dbx`]`; do cat factory_config/$.esl custom_config/$.esl > $.esl; done`

#### [][Concaténation manuelle]

Les Signature Lists KEK peuvent être concaténées avec :

`~/secure_boot $``cat `[`factory_config`]`/KEK.esl `[`custom_config`]`/KEK.esl > KEK.esl`

Ce processus peut être répété pour les *Signature Lists* **db** et **dbx**.

#### [Copie de la Platform Key]

Pour des raisons d\'organisation, la nouvelle *Platform Key* doit être copiée dans le répertoire actuel :

`~/secure_boot $``cp custom_config/PK.esl .`

### [Signature des Signature Lists]

Une fois les *Signature Lists* finalisées, elles doivent être signées :

#### [Platform Key]

Les Signature List PK signées peut être créée avec :

`~/secure_boot/ $``mkfifo key_pipe & sleep 1 && gpg --decrypt custom_config/PK.key.gpg > key_pipe & sign-efi-sig-list -k key_pipe -c custom_config/PK.crt `[`PK`]` PK.esl PK.auth ; rm key_pipe`

##### [][Clé de réinitialisation]

Si un fichier vide est passé comme fichier *esl*, il crée un fichier *auth* qui peut être inséré dans l\'emplacement de la *Platform Key*, ce qui désactive la *Platform Key*.

** Note**\
Ce fichier est littéralement un fichier vide signé avec la *Platform Key*. Lorsqu\'il est chargé dans l\'emplacement **PK**, comme il est valablement signé, il en efface le contenu, ce qui désactive le *Secure Boot*.

`~/secure_boot/ $``rm -f noPK.esl `

`~/secure_boot/ $``touch noPK.esl `

`~/secure_boot/ $``mkfifo key_pipe `

`~/secure_boot/ $``mkfifo nopk_pipe `

`~/secure_boot/ $``gpg --decrypt custom_config/PK.key.gpg > key_pipe & sign-efi-sig-list -k key_pipe -c custom_config/PK.crt PK `[`noPK`]`.esl nopk_pipe & `

`~/secure_boot/ $``gpg --recipient larry@gentoo.org --output noPK.auth.gpg --encrypt < nopk_pipe `

`~/secure_boot/ $``rm nopk_pipe `

`~/secure_boot/ $``rm key_pipe`

#### [Key Exchange Keys]

** Important**\
La *KEK* est signée à l\'aide du *PK*.

La *Signature List* **KEK** signée peut être créée avec :

`~/secure_boot/ $``mkfifo key_pipe & sleep 1 && gpg --decrypt custom_config/`[`PK`]`.key.gpg > key_pipe & sign-efi-sig-list -a -k key_pipe -c custom_config/`[`PK`]`.crt `[`KEK`]` KEK.esl KEK.auth ; rm key_pipe`

#### [Signature Databases]

La db et la dbx sont signées avec la KEK.

Enfin, ce processus doit être utilisé avec les *Signature Lists* **db** et **dbx** :

`~/secure_boot/ $``mkfifo key_pipe & sleep 1 && for db_type in `[`db dbx`]`; do gpg --decrypt custom_config/`[`KEK`]`.key.gpg > key_pipe & sign-efi-sig-list -k key_pipe -c custom_config/`[`KEK`]`.crt `[`$db_type`]` $.esl $.auth ; done ; rm key_pipe`

## [][Installation des clés]

Sur la plupart des systèmes, les clés et les listes de signatures peuvent être installées avec **efi-updatevar**. Si ce n\'est pas possible, les clés doivent être chargées à l\'aide de l\'UEFI.

Avant d\'installer les clés, le système doit être mis en *mode de configuration*. Ce processus diffère largement d\'un système à l\'autre, mais il existe généralement une option sous l\'onglet *Sécurité* qui permet de désactiver le démarrage sécurisé, d\'effacer les clés et d\'entrer en mode de configuration.

** Important**\
*Le mode configuration* est quitté une fois que la *Platform Key* a été écrite. Le passage en *mode utilisateur* n\'active pas le *Secure Boot*.

Les entrées autres que la *Platform Key* peuvent être installées à l\'aide des fichiers *.esl* en *mode configuration*.}}

** Note**\
Lors de l\'installation de fichiers *esl*, le paramètre **-e** doit être utilisé.

### [Installation de la Key Exchange Key]

En *mode configuration*, le **KEK** peut être installé avec le fichier *.auth* ou *.esl* :

`~/secure_boot/ $``sudo efi-updatevar -e -f KEK.esl `[`KEK`]

En *mode utilisateur*, la **KEK** peut être installée avec une *KEK.auth* valide :

`~/secure_boot/ $``sudo efi-updatevar -f KEK.auth `[`KEK`]

### [Installation des Database Keys]

En *mode configuration*, les fichiers **db** et **dbx** peuvent être installés soit avec le fichier *.auth*, soit avec le fichier *.esl* :

`~/secure_boot/ $``for db_type in `[`db dbx`]`; do sudo efi-updatevar -e -f $.esl `[`$db_type`]`; done`

En *mode utilisateur*, la **KEK** peut être installé avec une *KEK.auth* valide :

`~/secure_boot/ $`` for db_type in `[`db dbx`]`; do sudo efi-updatevar -f $.auth `[`$db_type`]`; done`

### [Installation de la Platform Key]

En *mode configuration*, la **PK** peut être installée avec :

`~/secure_boot/ $``sudo efi-updatevar -f PK.auth `[`PK`]

L\'exécution réussie de cette commande permet de quitter le mode configuration et d\'entrer dans le mode utilisateur.

## [Signature des fichiers de boot]

Avant d\'activer *Secure Boot*, tous les fichiers de démarrage doivent être signés avec la clé **db**.

** Tip**\
La façon la plus simple de démarrer avec Secure Boot est d\'utiliser un noyau [EFI stub](https://wiki.gentoo.org/wiki/EFI_stub "EFI stub"), de sorte qu\'un seul fichier doit être signé.

### [Signature]

Utilisation avancée, avec des clés chiffrées GPG :

`~/secure_boot/ $``mkfifo key_pipe & sleep 1 && gpg --decrypt custom_config/`[`db.key.gpg`]` > key_pipe & sudo sbsign --key `[`key_pipe`]` --cert custom_config/`[`db.crt`]` --output /boot/signed-vmlinuz /boot/vmlinuz; rm key_pipe`

** Note**\
Dans ce cas, sudo n\'est nécessaire que pour écrire dans [/boot].

Utilisation de base avec une clé privée **db** non chiffrée :

`~/secure_boot/ $``sudo sbsign --key custom_config/`[`db.key`]` --cert custom_config/`[`db.crt`]` --output /boot/signed-vmlinuz /boot/vmlinuz`

[`#`]`efibootmgr --disk /dev/sda --create --label "Signed Gentoo 6.3.4" --loader vmlinuz-6.3.4-gentoo-r1-initramfs.signed`

** Tip**\
L\'étiquette est destinée à l\'utilisateur et doit être descriptive.

### [][Vérification des signatures]

Les fichiers signés à l\'aide de ce processus peuvent être vérifiés avec :

`~/secure_boot/ $`` sbverify --cert custom_config/db.crt /boot/vmlinuz-6.3.4-gentoo-r1-initramfs.signed`

Signature verification OK

### [Liste des signatures]

Les signatures peuvent être listées en utilisant :

`user `[`$`]`sbverify --list /boot/vmlinuz-6.3.4-gentoo-r1-initramfs.signed`

    signature 1
    image signature issuers:
     - /CN=Larry's db
    image signature certificates:
     - subject: /CN=Larry's db
       issuer:  /CN=Larry's db

## [][Vérification de l\'état de Secure Boot]

Lorsque l\'option Secure Boot est activée, **dmesg** devrait indiquer :

`root `[`#`]` dmesg | grep -i "secure"`

\[ 0.010667\] Secure boot enabled

[od] peut être utilisé pour lire l\'état de *Secure Boot* dans [/sys/firmware/efi/efivars/] :

** Important**\
L\'UUID peut être différent, mais le paramètre doit commencer par **SecureBoot-**.

`user `[`$`]`od --address-radix n --format x1 /sys/firmware/efi/efivars/SecureBoot-8be4df61-93ca-11d2-aa0d-00e098032b8c`

06 00 00 00 01

Une valeur de 1 dans la dernière partie indique que *Secure Boot* est activé dans les *variables EFI*.

** Note**\
**\--address-radix n** supprime le formatage de la sortie et n\'affiche que les données. **\--format x1** formate les données de sortie en hexadécimal.

### [efivar]

efivar peut être utilisé pour lire et modifier les valeurs des variables EFI :

#### [Liste des variables]

Le paramètre **\--list** peut être utilisé pour lire les variables *EFI* actuelles.

** Note**\
Le format de sortie est *-name* et l\'UUID est essentiellement ignoré.

`user `[`$`]`efivar --list | grep -i secure`

    aa1305b9-01f3-4afb-920e-c9b979a852fd-SecureBootData
    8be4df61-93ca-11d2-aa0d-00e098032b8c-SecureBoot
    59d1c24f-50f1-401a-b101-f33e0daed443-SecureBootEnforce
    382af2bb-ffff-abcd-aaee-cce099338877-SecureFlashInfo
    59d1c24f-50f1-401a-b101-f33e0daed443-AdministerSecureBoot

Vérification de l\'état de Secure Boot

L\'état de Secure Boot peut être vérifié avec :

`user `[`$`]`efivar --print --name 8be4df61-93ca-11d2-aa0d-00e098032b8c-SecureBoot`

    Name: "SecureBoot"
    Attributes:
        Boot Service Access
        Runtime Service Access
    Value:
    00000000  01                                                |.               |

Une sortie de 1 indique que Secure Boot est activé.

## [][Réinitialisation de la Platform Key]

L\'utilisation d\'un *noPK.auth*, pour mettre à jour le **PK**, le désactive :

`~/secure_boot/ $``mkfifo auth_pipe & sleep 1 && gpg --decrypt noPK.auth.gpg > auth_pipe & sudo efi-updatevar -f auth_pipe PK`

## [][Voir également]

-   [Chiffrement_intégral_du_disque_à_partir_de_zéro_simplifié](https://wiki.gentoo.org/wiki/Chiffrement_int%C3%A9gral_du_disque_%C3%A0_partir_de_z%C3%A9ro_simplifi%C3%A9 "Chiffrement intégral du disque à partir de zéro simplifié")
-   [Security_Handbook/Boot_Path_Security](https://wiki.gentoo.org/wiki/Security_Handbook/Boot_Path_Security "Security Handbook/Boot Path Security") --- boot path security.
-   [Trusted_Boot](https://wiki.gentoo.org/wiki/Trusted_Boot "Trusted Boot")
-   [Trusted_Platform_Module](https://wiki.gentoo.org/wiki/Trusted_Platform_Module "Trusted Platform Module") --- The **Trusted Platform Module**, or **TPM** for short, is a secure, isolated, cryptographic processor that is typically built into most modern computers.
-   [Unified_Kernel_Image](https://wiki.gentoo.org/wiki/Unified_Kernel_Image "Unified Kernel Image") --- a single executable which can be [booted directly from UEFI firmware](https://wiki.gentoo.org/wiki/EFI_stub "EFI stub"), or automatically sourced by boot-loaders with little or no configuration.

## [[] References]

1.  [[[↑](#cite_ref-1)] [[https://www.rodsbooks.com/efi-bootloaders/controlling-sb.html](https://www.rodsbooks.com/efi-bootloaders/controlling-sb.html)]]
2.  [[[↑](#cite_ref-2)] [[https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/windows-secure-boot-key-creation-and-management-guidance?view=windows-11](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/windows-secure-boot-key-creation-and-management-guidance?view=windows-11)]]
3.  [[[↑](#cite_ref-3)] [[https://wiki.archlinux.org/title/Unified_Extensible_Firmware_Interface/Secure_Boot](https://wiki.archlinux.org/title/Unified_Extensible_Firmware_Interface/Secure_Boot)]]