Pour un chiffrement complet du disque, il convient d\'utiliser un disque de démarrage séparé : le chiffrement intégral du disque peut être utilisé pour préserver l\'intégrité et la confidentialité des données. [dm-crypt](https://wiki.gentoo.org/wiki/Dm-crypt "Dm-crypt") peut être utilisé pour configurer les disques afin de les chiffrer avec LUKS ou d\'autres formats. Cet article est un guide qui explique comment configurer un disque pour le chiffrer en utilisant LUKS et btrfs.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Emerge]](#Emerge)
    -   [[1.2] [Logiciels supplémentaires]](#Logiciels_suppl.C3.A9mentaires)
-   [[2] [Préparation du système]](#Pr.C3.A9paration_du_syst.C3.A8me)
-   [[3] [Préparation du disque]](#Pr.C3.A9paration_du_disque)
    -   [[3.1] [Formatage du système racine]](#Formatage_du_syst.C3.A8me_racine)
    -   [[3.2] [Phrase de passe sécurisée de l\'en-tête LUKS]](#Phrase_de_passe_s.C3.A9curis.C3.A9e_de_l.27en-t.C3.AAte_LUKS)
        -   [[3.2.1] [Ajout d\'une phrase de passe à un volume à l\'aide de fichiers de clés sécurisées GPG]](#Ajout_d.27une_phrase_de_passe_.C3.A0_un_volume_.C3.A0_l.27aide_de_fichiers_de_cl.C3.A9s_s.C3.A9curis.C3.A9es_GPG)
    -   [[3.3] [En-tête sécurisé du fichier de clé]](#En-t.C3.AAte_s.C3.A9curis.C3.A9_du_fichier_de_cl.C3.A9)
        -   [[3.3.1] [Création d\'un fichier de clé de base]](#Cr.C3.A9ation_d.27un_fichier_de_cl.C3.A9_de_base)
        -   [[3.3.2] [Fichier de clés symétriquement chiffrées GPG]](#Fichier_de_cl.C3.A9s_sym.C3.A9triquement_chiffr.C3.A9es_GPG)
        -   [[3.3.3] [Fichier de clé GPG à chiffrement asymétrique]](#Fichier_de_cl.C3.A9_GPG_.C3.A0_chiffrement_asym.C3.A9trique)
        -   [[3.3.4] [luksFormat en utilisant un fichier de clé]](#luksFormat_en_utilisant_un_fichier_de_cl.C3.A9)
        -   [[3.3.5] [luksFormat en utilisant un fichier de clé protégé par GPG]](#luksFormat_en_utilisant_un_fichier_de_cl.C3.A9_prot.C3.A9g.C3.A9_par_GPG)
    -   [[3.4] [Sauvegarde de l\'en-tête LUKS]](#Sauvegarde_de_l.27en-t.C3.AAte_LUKS)
-   [[4] [Préparation du système de fichiers]](#Pr.C3.A9paration_du_syst.C3.A8me_de_fichiers)
    -   [[4.1] [Ouvrir le volume LUKS]](#Ouvrir_le_volume_LUKS)
    -   [[4.2] [Formatage des systèmes de fichiers]](#Formatage_des_syst.C3.A8mes_de_fichiers)
        -   [[4.2.1] [Création de sous-volumes btrfs optionnels]](#Cr.C3.A9ation_de_sous-volumes_btrfs_optionnels)
-   [[5] [Configuration de l\'initramfs]](#Configuration_de_l.27initramfs)
    -   [[5.1] [Extraction de l\'initramfs]](#Extraction_de_l.27initramfs)
    -   [[5.2] [Intégration de l\'initramfs]](#Int.C3.A9gration_de_l.27initramfs)
-   [[6] [Installation de Gentoo]](#Installation_de_Gentoo)
    -   [[6.1] [Monter la partition racine]](#Monter_la_partition_racine)
    -   [[6.2] [Configuration de fstab]](#Configuration_de_fstab)
    -   [[6.3] [Finalisation de l\'installation de Gentoo]](#Finalisation_de_l.27installation_de_Gentoo)
-   [[7] [Informations complémentaires]](#Informations_compl.C3.A9mentaires)
    -   [[7.1] [Astuces pour les SSD]](#Astuces_pour_les_SSD)
-   [[8] [Voir également]](#Voir_.C3.A9galement)

## [Installation]

### [Emerge]

`root `[`#`]`emerge --ask sys-fs/cryptsetup`

### [][Logiciels supplémentaires]

Si vous utilisez GPG pour sécuriser davantage les fichiers de clé :

`root `[`#`]`emerge --ask app-crypt/gnupg`

## [][Préparation du système]

** Important**\
Le noyau doit être configuré conformément à : [Dm-crypt: Configuration du noyau](https://wiki.gentoo.org/wiki/Dm-crypt#Kernel_Configuration "Dm-crypt").

Si cette opération est effectuée dans le cadre d\'une nouvelle installation de Gentoo, la procédure d\'installation peut être suivie jusqu\'à l\'étape suivante : [Handbook:AMD64/Full/Installation/fr#Designing_a_partition_scheme](https://wiki.gentoo.org/wiki/Handbook:AMD64/Full/Installation/fr#Designing_a_partition_scheme "Handbook:AMD64/Full/Installation/fr")

Si vous convertissez un système existant à une configuration chiffrée, il faut soit ajouter du stockage, soit utiliser cette procédure pour créer de nouvelles partitions en utilisant l\'espace libre, où les données peuvent ensuite être copiées après la création.

Selon le type de disque, il peut être difficile, voire impossible, d\'écraser véritablement les parties du disque où se trouvent des données non chiffrées, mais déréférencées. Il est préférable de procéder à un effacement sécurisé à l\'aide du micrologiciel du disque avant de le réutiliser.

** Warning**\
Selon le type de disque, il peut être difficile, voire impossible, d\'écraser véritablement les parties du disque où se trouvent des données non chiffrées, mais déréférencées. Il est préférable de procéder à un effacement sécurisé à l\'aide du micrologiciel du disque avant de le réutiliser.

** Tip**\
Si vous migrez une installation existante vers un système de fichiers racine chiffré, la partition du chargeur d\'amorçage existante n\'a pas besoin d\'être modifiée (sauf si vous le souhaitez), mais la configuration du chargeur d\'amorçage devra être modifiée pour démarrer à partir des nouvelles partitions chiffrées.

## [][Préparation du disque]

** Important**\
Le partitionnement n\'implique généralement pas la modification des données contenues dans les partitions. Si un disque est re-partitionné puis chiffré, les anciennes données peuvent rester sous une forme non chiffrée jusqu\'à ce qu\'elles soient écrasées.

** Note**\
Les périphériques de stockage modernes **risquent de ne pas** être correctement effacés avec une commande du type [dd if=/dev/urandom of=/dev/sdX].

** See also**\
Pour plus d\'informations, voir : [Secure wipe](https://wiki.gentoo.org/wiki/Secure_wipe "Secure wipe").

Cet exemple utilise GPT comme table de partitions et GRUB comme chargeur de démarrage. fdisk est utilisé comme outil de partitionnement, mais n\'importe quel utilitaire de partitionnement fonctionnera.

** See also**\
Pour plus d\'informations sur GPT et EFI, voir [Disques (AMD64 Handbook)](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Disks/fr "Handbook:AMD64/Installation/Disks/fr").

Pour un chiffrement complet du disque, il convient d\'utiliser un disque de démarrage séparé :

[CODE]

    '"`UNIQ--pre-00000002-QINU`"'

** Tip**\
N\'importe quel système de fichiers peut être utilisé pour le système de fichiers racine, mais c\'est [btrfs](https://wiki.gentoo.org/wiki/Btrfs "Btrfs") qui est utilisé ici. Dans la plupart des cas, FAT32 doit être utilisé pour les partitions EFI/boot.

** Tip**\
L\'utilisation d\'un périphérique de stockage externe, tel qu\'une clé USB, peut s\'avérer judicieuse comme disque de démarrage, puisqu\'il peut être facilement retiré une fois le système démarré, et débogué plus facilement qu\'un disque interne.

** Note**\
La taille de la partition EFI est quelque peu importante, certains appareils ne démarreront pas avec des partitions trop petites (typiquement à cause de la taille des secteurs^[\[1\]](#cite_note-1)^), un minimum de **512MB** convient généralement.

### [][Formatage du système racine]

Pour créer une disposition de partitions avec fdisk, commencez par créer une nouvelle table de partitions sur le disque racine, [/dev/nvme0n1] :

`root `[`#`]`fdisk /dev/nvme0n1`

    Welcome to fdisk (util-linux 2.38.1).
    Changes will remain in memory only, until you decide to write them.
    Be careful before using the write command.

    Device does not contain a recognized partition table.
    Created a new DOS disklabel with disk identifier 0x81391dbc.

    Command (m for help): g
    Created a new GPT disklabel (GUID: 8D91A3C1-8661-2940-9076-65B815B36906).

Une fois la table de partition créée, une nouvelle partition du disque peut être créée en utilisant **n** en acceptant les valeurs par défaut :

`Command (m for help):``n`

    Partition number (1-128, default 1):
    First sector (2048-1953525134, default 2048):
    Last sector, +/-sectors or +/-size (2048-1953525134, default 1953523711):

    Created a new partition 1 of type 'Linux filesystem' and of size 931.5 GiB.

Enfin, les modifications peuvent être écrites avec **w** :

`Command (m for help):``w`

    The partition table has been altered.
    Calling ioctl() to re-read partition table.
    Syncing disks.

** Note**\
Cette partition pourrait être créée pour occuper l\'ensemble du périphérique.

Enfin, les propriétés de l\'**ESP** peuvent être définies à l\'aide de **t** :

`Command (m for help):``t`

    Selected partition 1
    Partition type or alias (type L to list all): 1
    Changed type of partition 'Linux filesystem' to 'EFI System'.

** Tip**\
Des Informations d\'utilisation plus avancées sont disponibles dans [man cryptsetup-luksFormat].

** Important**\
Ne spécifiez des arguments comme **\--cipher** que si vous êtes certain qu\'ils améliorent la sécurité au-delà des valeurs par défaut.

### [][Phrase de passe sécurisée de l\'en-tête LUKS]

La façon la plus simple de configurer un volume chiffré est d\'utiliser :

`root `[`#`]`cryptsetup luksFormat --key-size 512 /dev/nvme0n1p1`

    WARNING!
    ========
    This will overwrite data on /dev/nvme0n1p1 irrevocably.

    Are you sure? (Type 'yes' in capital letters):
    YES
    Enter passphrase for /dev/sda2:

** Note**\
Pour plus de sécurité, la taille de la clé peut être augmentée à 512 bits avec **\--key-size 512**.

** Warning**\
Un fichier de clé est généralement considéré comme plus sûr qu\'un mot de passe, mais il doit être protégé par un mot de passe. Un assaillant doit *posséder* le key file et *connaître* le mot de passe pour briser le chiffrement du disque.

** Tip**\
Luks peut permettre l\'utilisation de plusieurs fichiers de clé/mots de passe pour déchiffrer une partition. Si le mot de passe est utilisé à des fins de récupération, envisagez d\'utiliser une **phrase de passe** longue et de l\'écrire, ou de la stocker hors ligne.

#### [][Ajout d\'une phrase de passe à un volume à l\'aide de fichiers de clés sécurisées GPG]

La clé peut être déchiffrée vers ce tuyau :

`root `[`#`]`mkfifo key_pipe`

Une phrase de passe peut ensuite être ajoutée avec :

`root `[`#`]`gpg --decrypt key_file > key_pipe &`

Le pipe nommé peut être effacé avec :

`root `[`#`]`cryptsetup luksAddKey --key-file key_pipe /dev/nvme0n1p1`

Le pipe nommé peut être effacé avec :

`root `[`#`]`rm key_pipe`

### [][En-tête sécurisé du fichier de clé]

** Important**\
Les key files doivent être stockés ailleurs que dans les appareils qu\'ils chiffrent. Un fichier de clé est un facteur de sécurité relatif à la possession, tandis que les mots de passe ou les phrases de passe sont des facteurs relatifs à la connaissance. À quoi sert une serrure si les clés y sont attachées ?

** Warning**\
Prenez grand soin de ce fichier de clé, car s\'il est perdu, toute la partition chiffrée sera inaccessible, et s\'il est volé, les données ne seront plus en sécurité. Si elles sont écrites sur un support non chiffré ou transmises sur un réseau malveillant, elles ne peuvent être considérées comme sûres.

** Tip**\
L\'utilisation de [GnuPG](https://wiki.gentoo.org/wiki/GnuPG "GnuPG") pour chiffrer le fichier de clé peut contribuer à le sécuriser, en y ajoutant un facteur de *connaissance*.

#### [][Création d\'un fichier de clé de base]

Un fichier de clé basique peut être créé avec *dd* et [/dev/urandom] :

`/tmp/ #``dd bs=8388608 count=1 if=/dev/urandom of=crypt_key.luks`

    1+0 records in
    1+0 records out
    8388608 bytes (8.4 MB, 8.0 MiB) copied, 0.014407 s, 582 MB/s

** Tip**\
**cryptsetup \--help** indique la taille de la clé intégrée et la limite de la taille des caractères. La valeur par défaut est **8388608**, ou *8192 \* 1024* (*2\^23*).

#### [][Fichier de clés symétriquement chiffrées GPG]

Pour une plus grande sécurité, le fichier de clé peut être immédiatement chiffré avec [GnuPG](https://wiki.gentoo.org/wiki/GnuPG "GnuPG").

** Warning**\
Le chiffrement symétrique utilisant un mot de passe, est une méthode simple qui fonctionne sur la plupart des systèmes, mais qui est vulnérable au keylogging, de la même manière que la protection basée sur un simple mot de passe ou une phrase de passe.

** Important**\
Si vous utilisez l\'ISO d\'installation de Gentoo, il peut être nécessaire d\'exécuter

`root `[`#`]`export GPG_TTY=$(tty)`

pour chiffrer les données GPG directement à partir de **stdout**. Alternativement, **\--pinentry-mode loopback** peut être ajouté comme argument pour utiliser stdin pinentry, cependant, cela ne valide pas l\'entrée.

`/media/sda1/ #``dd bs=8388608 count=1 if=/dev/urandom | gpg --symmetric --cipher-algo AES256 --output crypt_key.luks.gpg`

    1+0 records in
    1+0 records out
    8388608 bytes (8.4 MB, 8.0 MiB) copied, 7.50139 s, 1.1 MB/s

#### [][Fichier de clé GPG à chiffrement asymétrique]

Un fichier de clé peut être protégé à l\'aide de la cryptographie à clé publique en utilisant une carte à puce telle qu\'une [YubiKey](https://wiki.gentoo.org/wiki/YubiKey "YubiKey"). [Ce guide du GPG YubiKey](https://wiki.gentoo.org/wiki/YubiKey/GPG "YubiKey/GPG") peut être utilisé pour générer des clés [GPG](https://wiki.gentoo.org/wiki/GnuPG "GnuPG") sur une YubiKey. Une fois les clés publiques chargées, les clés peuvent être chiffrées avec pour destinataire le détenteur de la clé :

`/media/sda1/ #``dd bs=8388608 count=1 if=/dev/urandom | gpg --recipient larry@gentoo.org --output crypt_key.luks.gpg --encrypt`

    1+0 records in
    1+0 records out
    8388608 bytes (8.4 MB, 8.0 MiB) copied, 7.50139 s, 1.1 MB/s

** Important**\
Dracut doit être configuré pour utiliser la clé publique correspondante, ce qui est expliqué dans la section Dracut.

Au démarrage, assurez-vous que la carte à puce est insérée. Dracut demandera le code PIN et, selon la configuration, il se peut qu\'il faille taper sur l\'appareil pour terminer la détection de présence.

#### [][luksFormat en utilisant un fichier de clé]

Pour sécuriser la partition avec un fichier de clé simple :

`/media/sda1/ #``cryptsetup --key-size 512 luksFormat /dev/nvme0n1p1 crypt_key.luks`

    WARNING!
    ========
    This will overwrite data on /dev/nvme0n1p1 irrevocably.

    Are you sure? (Type 'yes' in capital letters): YES

Pour ajouter ce fichier de clé à une partition déjà chiffrée :

`/media/sda1/ #``cryptsetup luksAddKey /dev/nvme0n1p1 crypt_key.luks`

    Enter any existing passphrase:

#### [][luksFormat en utilisant un fichier de clé protégé par GPG]

Pour sécuriser la partition à l\'aide d\'un fichier de clé protégé par GPG :

`/media/sda1/ #``gpg --decrypt crypt_key.luks.gpg | cryptsetup luksFormat --key-size 512 /dev/nvme0n1p1 -`

    gpg: AES256.CFB encrypted data
    WARNING!
    ========
    This will overwrite data on /dev/nvme0n1p1 irrevocably.

    Are you sure? (Type 'yes' in capital letters): YES

Pour ajouter le fichier de clé chiffré par GPG à une partition déjà chiffrée, il faut utiliser des tubes nommés afin d\'éviter de déchiffrer la clé sur le disque, car gpg et cryptsetup attendent tous deux des entrées provenant de stdin :

`/media/sda1/ #``mkfifo crypt_key`

`/media/sda1/ #``mkfifo cryptsetup_pass`

Une fois les fichiers créés, la clé doit être déchiffrée dans crypt_key, et la phrase de passe de récupération doit être transmise à cryptsetup_pass :

`/media/sda1/ #``gpg --decrypt crypt_key.luks.gpg > crypt_key &`

`/media/sda1/ #``read -s -r -p 'LUKS passphrase: ' CRYPT_PASS; echo "$CRYPT_PASS" > cryptsetup_pass &`

Enfin, **cat** peut être utilisé pour transmettre ces informations à **cryptsetup** :

`/media/sda1/ #``cat cryptsetup_pass crypt_key | cryptsetup luksAddKey /dev/nvme0n1p1 -`

    gpg: AES256.CFB encrypted data
    gpg: encrypted with 1 passphrase
    [1]-  Done                    read -s -r -p 'LUKS passphrase: ' CRYPT_PASS; echo "$CRYPT_PASS" > cryptsetup_pass
    [2]+  Done                    gpg -d crypt_key.luks.gpg > crypt_key

** Tip**\
L\'état de la clé LUKS peut être vérifié avec **cryptsetup luksDump **, par exemple **cryptsetup luksDump /dev/nvme0n1p1**.

** Note**\
Les tubes nommés peuvent maintenant être supprimés.

### [][Sauvegarde de l\'en-tête LUKS]

** Important**\
N\'oubliez pas cette étape, les clés/mots de passe sont utilisés pour décrypter l\'en-tête LUKS, si celui-ci est détruit pour une raison quelconque, les données restantes ne pourront être récupérées qu\'avec le fichier d\'en-tête.

Les en-têtes peuvent être sauvegardés avec :

`root `[`#`]`cryptsetup luksHeaderBackup /dev/nvme0n1p1 --header-backup-file crypt_headers.img`

## [][Préparation du système de fichiers]

Une fois le volume LUKS créé, il doit être mappé pour que les systèmes de fichiers sous-jacents puissent être créés.

### [Ouvrir le volume LUKS]

Le dispositif chiffré doit être ouvert et mappé avant de pouvoir être utilisé, ce qui peut être fait avec :

`root `[`#`]`cryptsetup luksOpen /dev/nvme0n1p1 crypt`

En cas d\'utilisation d\'un fichier clé :

`/media/sda1/ #``cryptsetup --key-file=crypt_key.luks open /dev/nvme0n1p1 crypt`

Si vous utilisez un fichier de clés chiffrées GPG :

`/media/sda1/ #``gpg --decrypt crypt_key.luks.gpg | cryptsetup --key-file=- open /dev/nvme0n1p1 crypt`

** Note**\
Cette commande ouvre [/dev/nvme0n1p1] et le place sous [/dev/mapper/] **crypt**.

### [][Formatage des systèmes de fichiers]

Créez un système de fichiers pour [/dev/sda1], la partition de démarrage qui contiendra les fichiers GRUB et le noyau. Cette partition est lue par l\'UEFI. La plupart des cartes mères ne peuvent lire qu\'un système de fichiers [FAT32](https://wiki.gentoo.org/wiki/FAT "FAT") :

`root `[`#`]`mkfs.vfat -F32 /dev/sda1`

Pour créer le système de fichiers racine [btrfs](https://wiki.gentoo.org/wiki/Btrfs "Btrfs") sur la partition LUKS :

`root `[`#`]`mkfs.btrfs -L rootfs /dev/mapper/crypt`

** Note**\
Les étiquettes sont facultatives, mais utiles. Elles permettent un montage facile sans UUID.

#### [][Création de sous-volumes btrfs optionnels]

Pour créer des sous-volumes pour [/etc], [/home] et [/var], le système de fichiers doit d\'abord être monté :

`root `[`#`]`mount LABEL=rootfs /mnt/gentoo`

Chaque sous-volume peut ensuite être créé :

`root `[`#`]`btrfs subvolume create /mnt/gentoo/etc `

`root `[`#`]`btrfs subvolume create /mnt/gentoo/home `

`root `[`#`]`btrfs subvolume create /mnt/gentoo/var`

## [][Configuration de l\'initramfs]

Un initramfs doit être utilisé pour déchiffrer et monter la partition racine. Cela peut être réalisé en utilisant un initramfs personnalisé minimal, en utilisant quelques commandes, ou en utilisant un outil comme dracut pour déchiffrer en utilisant des paramètres passés dans la ligne de commande du noyau. Dracut

** Important**\
Cette configuration doit être effectuée en mode chroot, ou sur un système live.

Les modules suivants doivent être ajoutés à la directive add_dracutmodules dans le fichier /etc/dracut.conf :

[FILE] **`/etc/dracut.conf`Composants minimaux requis pour déchiffrer les volumes LUKS à l\'aide de dracut**

    add_dracutmodules+=" crypt dm rootfs-block "

** Important**\
L\'espacement des directives de configuration de Dracut est très important. Assurez-vous qu\'il n\'y a pas d\'espace entre *add_dracutmodules* et *+=\"*, les paramètres dans *add_dracutmodules* doivent être encadrés par des espaces.

Si des clés GPG sont utilisées, le module suivant doit également être ajouté : **crypt-gpg**

[FILE] **`/etc/dracut.conf`Composants minimum nécessaires pour déchiffrer les volumes LUKS à l\'aide de dracut**

    add_dracutmodules+=" crypt crypt-gpg dm rootfs-block "

** Important**\
Si une carte à puce est utilisée pour stocker les clés privées d\'un fichier de clés chiffrées GPG, le fichier [/etc/dracut.conf.d/crypt-public-key.gpg] doit être configuré pour contenir la clé publique correspondante..

Dracut peut être configuré pour être construit avec la configuration pour LUKS codée en dur, les informations sur le premier disque doivent être obtenues :

`root `[`#`]`lsblk -o name,uuid`

    NAME        UUID
    sda
    └─sda1      BDF2-0139
    nvme0n1
    └─nvme0n1p1 4bb45bd6-9ed9-44b3-b547-b411079f043b
      └─crypt   cb070f9e-da0e-4bc5-825c-b01bb2707704

[FILE] **`/etc/dracut.conf`Paramètres cmdline intégrés pour le déchiffrage de rootfs**

    kernel_cmdline+=" rd.luks.uuid=4bb45bd6-9ed9-44b3-b547-b411079f043b rd.luks.key=/crypt_key.luks.gpg:UUID=BDF2-0139 "

Si vous utilisez systemd comme init, vous devez également ajouter l\'use flag **cryptsetup** :

[FILE] **`/etc/portage/package.use/systemd`**

    sys-apps/systemd cryptsetup

Et faire un rebuild :

`root `[`#`]`emerge --ask --newuse sys-apps/systemd`

Une fois Dracut configuré, un nouveau fichier initramfs peut être généré en exécutant :

`root `[`#`]`dracut`

** Important**\
Par défaut, Dracut écrit le fichier dans le répertoire [/boot], qui doit être monté.

If the initramfs is being generated for a kernel other than the currently active one, **\--kver** must be used:

`root `[`#`]`dracut --kver 6.1.28-gentoo `

Cela peut se produire dans une situation où la version du noyau dans le CD Gentoo Live diffère de la version émergée de sys-kernel/gentoo-sources dans le processus de compilation du noyau.

** Tip**\
Les versions disponibles du noyau peuvent être trouvées à l\'aide de **ls /lib/modules**.

Dracut a maintenant généré un initramfs, mais la configuration n\'est pas terminée. Les paramètres de la ligne de commande doivent être définis, soit en les ajoutant manuellement au noyau, soit en les configurant dans le bootloader.

** Tip**\
La plupart des paramètres de dracut sont décrits dans **man dracut.cmdline**.

#### [][Extraction de l\'initramfs]

Il est possible d\'utiliser **dracut** pour générer une image *initramfs*, puis de l\'extraire pour l\'intégrer au noyau.

`/usr/src/initramfs #``/usr/lib/dracut/skipcpio /boot/initramfs-6.1.28-gentoo-initramfs.img | zcat | cpio -ivd`

#### [][Intégration de l\'initramfs]

Une fois l\'*initramfs* extrait dans [/usr/src/initramfs], le noyau peut être configuré pour l\'intégrer :

[KERNEL] **Intégration l\'initramfs dans le noyau**

    General Setup --->
    [*] Initial RAM filesystem and RAM disk (initramfs/initrd) support
        (/usr/src/initramfs) Initramfs source file(s)
    [*]   Support initial ramdisk/ramfs compressed using gzip

Équivalent en .config :

[CODE] **Configuration de .config pour un initramfs intégré**

    CONFIG_INITRAMFS_SOURCE="/usr/src/initramfs"
    CONFIG_INITRAMFS_ROOT_UID=0
    CONFIG_INITRAMFS_ROOT_GID=0
    CONFIG_RD_GZIP=y
    CONFIG_INITRAMFS_COMPRESSION_GZIP=y

Avec cette configuration, le noyau intégrera automatiquement ce qui existe sous [/usr/src/initramfs] dans le noyau lorsqu\'il est construit, et tentera de l\'utiliser au démarrage. Ceci est particulièrement utile pour un démarrage [Secure Boot](https://wiki.gentoo.org/wiki/Secure_Boot "Secure Boot").

** Important**\
Si vous utilisez cette méthode avec **GRUB**, assurez-vous de supprimer ou de déplacer **dracut** et de générer l\'image *initramfs* pour éviter que **grub-mkconfig** ne soit confondu.

## [Installation de Gentoo]

Si cette procédure est suivie lors d\'une installation Gentoo (à la place de [Handbook:AMD64/Full/Installation/fr#Designing_a_partition_scheme](https://wiki.gentoo.org/wiki/Handbook:AMD64/Full/Installation/fr#Designing_a_partition_scheme "Handbook:AMD64/Full/Installation/fr") via [Handbook:AMD64/Full/Installation/fr#Monter_la_partition_racine](https://wiki.gentoo.org/wiki/Handbook:AMD64/Full/Installation/fr#Monter_la_partition_racine "Handbook:AMD64/Full/Installation/fr")), les étapes suivantes peuvent être utilisées pour monter la partition créée, afin de poursuivre l\'installation.

### [Monter la partition racine]

Le volume logique du système de fichiers racine peut être monté à cet emplacement créé avec :

`root `[`#`]`mount LABEL=rootfs /mnt/gentoo`

### [Configuration de fstab]

    fstab  .

** Important**\
Le bon fichier *fstab* doit être édité, si cela est fait avant le chrootage, assurez-vous que le bon chemin est utilisé. Plus d\'informations sont disponibles dans [la partie système de fichiers du guide d\'installation](https://wiki.gentoo.org/wiki/Handbook:AMD64/Full/Installation/fr#Informations_sur_le_syst.C3.A8me_de_fichiers "Handbook:AMD64/Full/Installation/fr").

Pour un montage cohérent des volumes, les étiquettes et les UUID doivent être utilisés. Les périphériques de bloc et les ID de partition qui leur sont associés peuvent être visualisés à l\'aide de :

`root `[`#`]`lsblk -o name,uuid`

    NAME        UUID
    sda
    └─sda1      BDF2-0139
    nvme0n1
    └─nvme0n1p1 4bb45bd6-9ed9-44b3-b547-b411079f043b
      └─crypt   cb070f9e-da0e-4bc5-825c-b01bb2707704

Une fois les UUID et les labels des partitions identifiés, le fichier [/etc/fstab](https://wiki.gentoo.org/wiki/Fstab "Fstab") peut être modifié pour ajouter les montages appropriés :

[FILE] **`/mnt/gentoo/etc/fstab`**

    '"`UNIQ--pre-00000021-QINU`"'

** Note**\
Les sous-volumes étant créés à l\'endroit où ils seraient montés, ils n\'ont pas besoin d\'entrées fstab.

### [][Finalisation de l\'installation de Gentoo]

** Important**\
Le guide d\'installation général devrait s\'appliquer. Quelques considérations doivent être faites, le système de fichiers RAM initial doit être construit avec le support du déchiffrage de la partition racine, et la ligne de commande du noyau doit être configurée pour passer des paramètres à l\'initramfs si nécessaire.

A ce stade, l\'installation de Gentoo peut être poursuivie normalement : [Installation d\'une archive tar](https://wiki.gentoo.org/wiki/Handbook:AMD64/Full/Installation/fr#Installation_d.27une_archive_tar "Handbook:AMD64/Full/Installation/fr")

## [][Informations complémentaires]

### [Astuces pour les SSD]

** Warning**\
L\'utilisation de disques SSD et de disques hybrides sacrifie une partie de la sécurité cryptographique au profit de l\'amélioration de la vitesse et de la réduction de la consommation d\'énergie. Voir les [https://gitlab.com/cryptsetup/cryptsetup/-/wikis/FrequentlyAskedQuestions](https://gitlab.com/cryptsetup/cryptsetup/-/wikis/FrequentlyAskedQuestions) FAQ de cryptsetup pour plus de détails. Prévoyez la dégradation du disque et la perte d\'espace au fil du temps. Avec ou sans trim, la destruction physique du disque est nécessaire. Il n\'y a aucune garantie que l\'écrasement modifie réellement les bits dans les puces de mémoire du disque. Il ne s\'agit pas d\'un problème de cryptsetup, de LUKS ou du noyau, mais d\'un problème causé par les algorithmes spécifiques au micrologiciel, au matériel, au vendeur et au modèle.

Le [trim](https://en.wikipedia.org/wiki/Trim_(computing) "wikipedia:Trim (computing)") SSD permet à un système d\'exploitation d\'indiquer à un lecteur à semi-conducteurs (SSD) quels blocs de données ne sont plus considérés comme utilisés et peuvent être effacés en interne. Le fonctionnement de bas niveau des disques SSD étant très différent de celui des disques durs, la façon dont les systèmes d\'exploitation traitent habituellement les opérations telles que les suppressions et les formatages a entraîné une dégradation progressive imprévue des performances des opérations d\'écriture sur les disques SSD. Le trim permet au disque SSD de gérer plus efficacement la collecte des données résiduelles, ce qui ralentirait les futures opérations d\'écriture sur les blocs concernés. Pour activer le découpage du SSD du système de fichiers racine crypté sur LVM, modifiez le fichier /etc/default/grub si vous utilisez genkernel :

[FILE] **`/etc/default/grub`**

    GRUB_CMDLINE_LINUX="...root_trim=yes"

Si vous utilisez dracut pour générer les intiramfs, utilisez :

[FILE] **`/etc/default/grub`**

    GRUB_CMDLINE_LINUX="...rd.luks.allow-discards"

Si vous utilisez initramfs basé sur un système utilisant systemd, utilisez :

[FILE] **`/etc/default/grub`**

    GRUB_CMDLINE_LINUX="...rd.luks.options=discard"

Cela indiquera au noyau d\'activer trim sur la racine. Modifiez le fichier de configuration [/etc/lvm/lvm.conf] :

[FILE] **`/etc/lvm/lvm.conf`**

    issue_discards = 1

Cela notifiera à la couche LVM d\'activer trim sur les disques SSD. Lors de l\'utilisation de disques SSD et de l\'UEFI-boot, la séquence de démarrage peut être trop rapide. Lorsque vous entrez la phrase d\'authentification correcte, le noyau se plaindra de modules manquants ou de l\'absence de périphérique racine. Essayez d\'ajouter `rootdelay=3` à `GRUB_CMDLINE_LINUX_DEFAULT` dans [/etc/default/grub], ou ajoutez-le directement en mode édition du menu GRUB lors du démarrage.

## [][Voir également]

-   [Rootfs encryption](https://wiki.gentoo.org/wiki/Rootfs_encryption "Rootfs encryption")
-   [Dm-crypt](https://wiki.gentoo.org/wiki/Dm-crypt "Dm-crypt")
-   [Dm-crypt full disk encryption](https://wiki.gentoo.org/wiki/Dm-crypt_full_disk_encryption "Dm-crypt full disk encryption")

1.  [[[↑](#cite_ref-1)] [[https://www.ctrl.blog/entry/esp-size-guide.html](https://www.ctrl.blog/entry/esp-size-guide.html)]]