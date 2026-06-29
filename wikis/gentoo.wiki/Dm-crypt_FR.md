**Resources**

[[]][Home](https://gitlab.com/cryptsetup/cryptsetup)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Dm-crypt_(FR) "wikipedia:Dm-crypt (FR)")

**dm-crypt** est un système de chiffrement de disque utilisant le framework de l\'API cryptographique du noyau et le sous-système de mappeur de périphériques. Avec dm-crypt, les administrateurs peuvent chiffrer des disques entiers, des volumes logiques, des partitions, mais aussi des fichiers individuels.

Le sous-système dm-crypt prend en charge la structure *LUKS (Linux Unified Key Setup)*, qui permet à plusieurs clés d\'accéder aux données chiffrées, ainsi que de manipuler les clés (comme les modifier, ajouter des phrases de passe supplémentaires, etc.) Bien que dm-crypt prenne également en charge des configurations non LUKS, cet article se concentrera sur la fonctionnalité LUKS, principalement en raison de sa flexibilité, de sa facilité de gestion et de son large support au sein de la communauté.

## Contents

-   [[1] [Configuration]](#Configuration)
    -   [[1.1] [Configuration du noyau]](#Configuration_du_noyau)
    -   [[1.2] [Installation de cryptsetup]](#Installation_de_cryptsetup)
-   [[2] [Espace de stockage chiffré]](#Espace_de_stockage_chiffr.C3.A9)
    -   [[2.1] [Benchmark]](#Benchmark)
    -   [[2.2] [Fichier de clé ou phrase de passe]](#Fichier_de_cl.C3.A9_ou_phrase_de_passe)
    -   [[2.3] [Création d\'une plateforme de stockage chiffrée]](#Cr.C3.A9ation_d.27une_plateforme_de_stockage_chiffr.C3.A9e)
        -   [[2.3.1] [Démarrage avec chiffrement intégral du disque]](#D.C3.A9marrage_avec_chiffrement_int.C3.A9gral_du_disque)
    -   [[2.4] [Ouverture du stockage chiffré]](#Ouverture_du_stockage_chiffr.C3.A9)
    -   [[2.5] [Fermeture du stockage chiffré]](#Fermeture_du_stockage_chiffr.C3.A9)
-   [[3] [Manipulation des clés LUKS]](#Manipulation_des_cl.C3.A9s_LUKS)
    -   [[3.1] [Liste des emplacements]](#Liste_des_emplacements)
    -   [[3.2] [Suppression d\'un fichier de clé ou d\'une phrase de passe]](#Suppression_d.27un_fichier_de_cl.C3.A9_ou_d.27une_phrase_de_passe)
    -   [[3.3] [Vider un emplacement]](#Vider_un_emplacement)
-   [[4] [Automatiser le montage des systèmes de fichiers chiffrés]](#Automatiser_le_montage_des_syst.C3.A8mes_de_fichiers_chiffr.C3.A9s)
    -   [[4.1] [Configuration de dm-crypt]](#Configuration_de_dm-crypt)
    -   [[4.2] [Configuration de fstab]](#Configuration_de_fstab)
    -   [[4.3] [Ajout de l\'initscript à bootlevel]](#Ajout_de_l.27initscript_.C3.A0_bootlevel)
    -   [[4.4] [Afficher les nœuds de périphériques déchiffrés]](#Afficher_les_n.C5.93uds_de_p.C3.A9riph.C3.A9riques_d.C3.A9chiffr.C3.A9s)
-   [[5] [Montage des volumes TrueCrypt/tcplay/VeraCrypt]](#Montage_des_volumes_TrueCrypt.2Ftcplay.2FVeraCrypt)
-   [[6] [Voir également]](#Voir_.C3.A9galement)
-   [[7] [Ressources externes]](#Ressources_externes)

## [Configuration]

Il y a deux prérequis avant de pouvoir commencer à utiliser dm-crypt :

1.  Configuration du noyau Linux
2.  Installation du paquet [[[sys-fs/cryptsetup]](https://packages.gentoo.org/packages/sys-fs/cryptsetup)[]]

### [Configuration du noyau]

Pour utiliser dm-crypt, un certain nombre de paramètres de configuration sont nécessaires.

Tout d\'abord, la prise en charge de l\'infrastructure de *mappage des périphériques* et de la *cible de chiffrement* doit être incluse :

[`#`]`cryptsetup benchmark`

    # Tests are approximate using memory only (no storage IO).
    PBKDF2-sha1      1707778 iterations per second for 256-bit key
    PBKDF2-sha256    2131252 iterations per second for 256-bit key
    PBKDF2-sha512    1630755 iterations per second for 256-bit key
    PBKDF2-ripemd160  882639 iterations per second for 256-bit key
    PBKDF2-whirlpool  664496 iterations per second for 256-bit key
    argon2i       9 iterations, 1048576 memory, 4 parallel threads (CPUs) for 256-bit key (requested 2000 ms time)
    argon2id      9 iterations, 1048576 memory, 4 parallel threads (CPUs) for 256-bit key (requested 2000 ms time)
    #     Algorithm |       Key |      Encryption |      Decryption
            aes-cbc        128b      1197.2 MiB/s      3788.1 MiB/s
        serpent-cbc        128b               N/A               N/A
        twofish-cbc        128b               N/A               N/A
            aes-cbc        256b       888.2 MiB/s      3011.1 MiB/s
        serpent-cbc        256b               N/A               N/A
        twofish-cbc        256b               N/A               N/A
            aes-xts        256b      3670.7 MiB/s      3708.4 MiB/s
        serpent-xts        256b               N/A               N/A
        twofish-xts        256b               N/A               N/A
            aes-xts        512b      2929.2 MiB/s      2974.0 MiB/s
        serpent-xts        512b               N/A               N/A
        twofish-xts        512b               N/A               N/A

### [][Fichier de clé ou phrase de passe]

Pour commencer avec un stockage chiffré, l\'administrateur devra décider de la méthode à utiliser pour la clé de chiffrement. Avec [cryptsetup], il a le choix entre une phrase de passe et un fichier clé. Dans le cas d\'un fichier clé, il peut s\'agir de n\'importe quel fichier, mais il est recommandé d\'utiliser un fichier contenant des données aléatoires correctement protégé (étant donné que l\'accès à ce fichier clé signifie l\'accès aux données chiffrées).

Pour créer un fichier clé, on peut utiliser la commande [dd] :

`root `[`#`]`dd if=/dev/urandom of=/etc/keys/enc.key bs=1 count=4096`

Dans les sections suivantes, nous montrerons toutes les commandes pour les deux situations - phrase de passe et fichier de clé. Bien entendu, une seule méthode est nécessaire.

### [][Création d\'une plateforme de stockage chiffrée]

Pour créer une plate-forme de stockage chiffrée (qui peut être un disque, une partition, un fichier, \...), utilisez la commande [cryptsetup] avec l\'action `luksFormat`.

Par exemple, pour définir [/dev/vdb2] comme support de stockage des données chiffrées :

`root `[`#`]`cryptsetup -c aes-xts-plain64 -s 512 -y luksFormat /dev/vdb2`

    This will overwrite data on /dev/vdb2 irrevocably.

    Are you sure? (Type uppercase yes): YES
    Enter LUKS passphrase: ...
    Verify passphrase: ...

Pour utiliser un fichier clé plutôt qu\'une phrase de passe :

`root `[`#`]`cryptsetup -c aes-xts-plain64 -s 512 -y luksFormat /dev/vdb2 /etc/keys/enc.key`

    This will overwrite data on /dev/vdb2 irrevocably.

    Are you sure? (Type uppercase yes): YES

L\'option `-c aes-xts-plain64` indique à [cryptsetup] la norme de chiffrement utilisée pour chiffrer le disque (`cat /proc/crypto` vous montrera toutes les possibilités). `-s 512` indique à cryptsetup la longueur de clé à utiliser pour la clé de chiffrement réelle (contrairement à la phrase de passe ou au fichier de clés, qui sont utilisés pour accéder à cette véritable clé de chiffrement). Enfin, `-y` vous oblige à taper deux fois votre mot de passe.

** Note**\
[XTS](https://en.wikipedia.org/wiki/Disk_encryption_theory#XTS) divise la clé en deux moitiés, dont une seule est utilisée pour le chiffrement proprement dit. Cela signifie que \"aes-xts\" avec une clé de 512 bits utilise en fait 256 bits pour la partie AES.

** Important**\
Si l\'en-tête LUKS est endommagé, vos données chiffrées seront perdues à jamais, même si vous disposez d\'une sauvegarde de la clé GPG et de la phrase de passe. Par conséquent, vous pouvez envisager de sauvegarder cet en-tête sur un périphérique séparé et de le stocker en toute sécurité. Consultez la [de LUKS](https://gitlab.com/cryptsetup/cryptsetup/wikis/FrequentlyAskedQuestions#6-backup-and-data-recoveryFAQ) pour plus de détails sur la manière de procéder.

`root `[`#`]`cryptsetup luksHeaderBackup /dev/sdXn --header-backup-file /tmp/efiboot/luks-header.img`

Sachez que si vous conservez une sauvegarde de l\'en-tête LUKS de cette manière et que vous révoquez ultérieurement l\'un des lots de clés, les anciennes clés seront *toujours* utilisables pour déverrouiller la partition LUKS par les personnes ayant accès à ce fichier de sauvegarde de l\'en-tête.

#### [][Démarrage avec chiffrement intégral du disque]

Pour démarrer le système à partir d\'un périphérique entièrement chiffré (y compris /boot chiffré) à l\'aide de [GRUB](https://wiki.gentoo.org/wiki/GRUB "GRUB"), chiffrez à l\'aide de luks1, puisque luks2 n\'est pas encore entièrement pris en charge. Exemple de commande :

### [][Ouverture du stockage chiffré]

Pour ouvrir le stockage chiffré (c\'est-à-dire rendre les données réelles accessibles grâce à un déchiffrement transparent), utilisez l\'action `luksOpen` .

`root `[`#`]`cryptsetup luksOpen /dev/vdb2 myname`

    Enter passphrase for /dev/vdb2: ...

Si un fichier clé est utilisé, la commande se présente comme suit :

`root `[`#`]`cryptsetup luksOpen -d /etc/keys/enc.key /dev/vdb2 myname`

Lorsque la commande est exécutée avec succès, un nouveau fichier de périphérique appelé [/dev/mapper/myname] est mis à disposition.

Si c\'est la première fois que ce périphérique chiffré est utilisé, il doit être formaté. L\'exemple suivant utilise le système de fichiers [Btrfs](https://wiki.gentoo.org/wiki/Btrfs "Btrfs"), mais tout autre système de fichiers peut être utilisé :

`root `[`#`]`mkfs.btrfs /dev/mapper/myname`

Une fois que le système de fichiers est formaté, ou que le formatage a déjà été effectué dans le passé, le fichier du périphérique peut être monté sur le système :

`root `[`#`]`mount /dev/mapper/myname /home`

### [][Fermeture du stockage chiffré]

Pour verrouiller le stockage chiffré (c\'est-à-dire s\'assurer que les données réelles ne sont plus accessibles par un déchiffrement transparent), utilisez l\'action `luksClose` :

`root `[`#`]`cryptsetup luksClose myname`

Bien entendu, assurez-vous que l\'appareil n\'est plus utilisé.

## [][Manipulation des clés LUKS]

Les clés LUKS sont utilisées pour accéder à la véritable clé de chiffrement. Elles sont stockées dans des emplacements situés dans l\'en-tête de la partition, du disque ou du fichier (chiffré).

### [Liste des emplacements]

La commande luksDump permet d\'afficher des informations sur la partition, le disque ou le fichier chiffré. Cela inclut les emplacements :

`root `[`#`]`cryptsetup luksDump /dev/vdb2`

    LUKS header information for /dev/vdb2

    Version:        1
    Cipher name:    aes
    Cipher mode:    xts-plain64
    Hash spec:      sha1
    Payload offset: 4096
    MK bits:        512
    MK digest:      34 3b ec ac 10 af 19 e7 e2 d4 c8 90 eb a8 da 3c e4 4f 2e ce
    MK salt:        ff 7c 7f 53 db 53 48 02 a4 32 dc e0 22 fc a3 51
                    06 ba b3 48 b3 28 13 a8 7a 68 43 d6 46 79 14 fe
    MK iterations:  59375
    UUID:           2921a7c9-7ccb-4300-92f4-38160804e08c

    Key Slot 0: ENABLED
            Iterations:             241053
            Salt:                   90 0f 0f db cf 66 ea a9 6c 7c 0c 0d b0 28 05 2f
                                    8a 5c 14 54 98 62 1a 29 f3 08 25 0c ec c2 b1 68
            Key material offset:    8
            AF stripes:             4000
    Key Slot 1: ENABLED
            Iterations:             273211
            Salt:                   01 4c 26 ed ff 18 75 31 b9 89 5d a6 e0 b5 f4 14
                                    48 d0 23 47 a9 85 78 fb 76 c4 a9 d0 cd 63 fb d7
            Key material offset:    512
            AF stripes:             4000
    Key Slot 2: DISABLED
    Key Slot 3: DISABLED
    Key Slot 4: DISABLED
    Key Slot 5: DISABLED
    Key Slot 6: DISABLED
    Key Slot 7: DISABLED

Dans l\'exemple ci-dessus, deux emplacements sont utilisés. Notez que luksDump ne divulgue rien de sensible - il affiche simplement le contenu de l\'en-tête LUKS. Aucune clé de décryptage ne doit être fournie pour utiliser luksDump.

Ajout d\'un fichier clé ou d\'une phrase de passe

Afin d\'ajouter un fichier clé ou une phrase de passe supplémentaire pour accéder au stockage chiffré, utilisez la commande `luksAddKey` :

`root `[`#`]`cryptsetup luksAddKey /dev/vdb2`

    Enter any passphrase: (Enter a valid, previously used passphrase to unlock the key)
    Enter new passphrase for key slot: ...
    Verify passphrase: ...

Pour utiliser un fichier de clé afin de déverrouiller la clé (tout en ajoutant une phrase de passe) :

`root `[`#`]`cryptsetup luksAddKey -d /etc/keys/enc.key /dev/vdb2`

    Enter new passphrase for key slot: ...
    Verify passphrase: '''

Si un fichier clé doit être ajouté (par exemple [/etc/keys/backup.key]) :

`root `[`#`]`cryptsetup luksAddKey /dev/vdb2 /etc/keys/backup.key`

Ou, pour utiliser le premier fichier de clé pour déverrouiller la clé principale :

`root `[`#`]`cryptsetup luksAddKey -d /etc/keys/enc.key /dev/vdb2 /etc/keys/backup.key`

### [][Suppression d\'un fichier de clé ou d\'une phrase de passe]

La commande `luksRemoveKey` permet de supprimer un fichier de clé ou une phrase de passe (qui ne peuvent donc plus être utilisés pour déchiffrer l\'espace de stockage) :

`root `[`#`]`cryptsetup luksRemoveKey /dev/vdb2`

    Enter LUKS passphrase to be deleted: ...

Ou pour supprimer un fichier de clé :

`root `[`#`]`cryptsetup luksRemoveKey -d /etc/keys/backup.key /dev/vdb2`

Assurez-vous qu\'au moins une méthode d\'accès aux données est encore disponible. Une fois qu\'une phrase de passe ou un fichier clé a été supprimé, il ne peut plus être récupéré.

### [Vider un emplacement]

Si la phrase de passe ou le fichier clé n\'est plus connu, l\'emplacement peut être libéré. Bien entendu, il faut pour cela savoir à l\'avance dans quel emplacement la phrase de passe ou le fichier clé a été stocké.

Par exemple, pour vider l\'emplacement 2 (qui est le troisième emplacement puisque les emplacements sont numérotés à partir de 0) :

`root `[`#`]`cryptsetup luksKillSlot /dev/vdb2 2`

Cette commande demandera une phrase d\'authentification valide avant de continuer. Il est également possible de transmettre le fichier clé à utiliser :

`root `[`#`]`cryptsetup luksKillSlot -d /etc/keys/enc.key /dev/vdb2 2`

## [][Automatiser le montage des systèmes de fichiers chiffrés]

Jusqu\'à présent, l\'article se concentrait sur la configuration manuelle et le montage/démontage des systèmes de fichiers chiffrés. Il existe un service init [dmcrypt] qui automatise le déchiffrement et le montage des systèmes de fichiers chiffrés.

### [Configuration de dm-crypt]

Éditez le fichier [/etc/conf.d/dmcrypt] et ajoutez des entrées pour chaque système de fichiers. Les entrées prises en charge sont bien documentées dans le fichier, l\'exemple ci-dessous n\'est qu\'un exemple :

[FILE] **`/etc/conf.d/dmcrypt`Ouverture automatique de deux systèmes de fichiers chiffrés**

    # Definition for /dev/mapper/home (for /home)
    target=home
    source=UUID="abcdef12-321a-a324-a88c-cac412befd98"
    key=/etc/keys/home.key

    # Definition for /dev/mapper/local (for /usr/local)
    target=local
    source=UUID="fedcba34-4823-b423-a94c-cadbefda2943"
    key=/etc/keys/local.key

    # Using an encrypted partition as key source.
    target=other
    source=UUID="ff24303e-49e1-4d13-b8ad-fc6b7e1d8174"
    key=/keys/other.key                                # Relative to the root of the encrypted partition.
    remdev=/dev/mapper/home                            # The recently decrypted partition.

    # An empty line is important at the end of the file

### [Configuration de fstab]

L\'étape suivante consiste à configurer /etc/fstab pour monter automatiquement les systèmes de fichiers (déchiffrés) dès qu\'ils sont disponibles. Il est recommandé de commencer par obtenir l\'UUID du système de fichiers décrypté (monté) :

`root `[`#`]`blkid /dev/mapper/home`

    /dev/mapper/home: UUID="4321421a-4321-a6c9-de52-ba6421efab76" TYPE="ext4"

Mettez ensuite à jour le fichier [/etc/fstab] en conséquence :

[FILE] **`/etc/fstab`Automounting the decrypted file systems**

    UUID="4321421a-4321-a6c9-de52-ba6421efab76"   /home        ext4   defaults   0   0
    UUID="bdef2432-3bd1-4ab4-523d-badcf234a342"   /usr/local   ext4   defaults   0   0

### [][Ajout de l\'initscript à bootlevel]

N\'oubliez pas de lancer le service init dmcrypt au démarrage :

`root `[`#`]`rc-update add dmcrypt boot`

### [][Afficher les nœuds de périphériques déchiffrés]

Si vous avez déchiffré ou déverrouillé un périphérique avant le démarrage des services, par exemple votre disque racine avec un initramfs, il est possible que le périphérique mappé ne soit pas visible. Dans ce cas, vous pouvez exécuter la procédure suivante pour le recréer.

`root `[`#`]`dmsetup mknodes`

## [][Montage des volumes TrueCrypt/tcplay/VeraCrypt]

`root `[`#`]`cryptsetup --type tcrypt open `*`container-to-mount`*` `*`container-name`*

Remplacez container-to-mount par le fichier de périphérique sous [/dev] ou le chemin du fichier que vous souhaitez ouvrir. Une fois l\'ouverture réussie, le périphérique en clair apparaîtra sous la forme [/dev/mapper/container-name], sur lequel vous pourrez utiliser la commande `mount` comme n\'importe quel périphérique normal.

Si vous utilisez des fichiers clés, transmettez-les à l\'aide de l\'option `--key-file`, pour ouvrir un volume caché, transmettez l\'option `--tcrypt-hidden` et pour une partition ou un disque entier chiffré en mode système, utilisez l\'option `--tcrypt-system`.

Lorsque vous avez terminé, utilisez la commande `unmount` pour démonter le volume et fermez le conteneur à l\'aide de la commande suivante :

`root `[`#`]`cryptsetup close `*`container-name`*

## [][Voir également]

-   [Full Disk Encryption From Scratch Simplified](https://wiki.gentoo.org/wiki/Full_Disk_Encryption_From_Scratch_Simplified "Full Disk Encryption From Scratch Simplified") --- a guide which covers the process of configuring a drive to be encrypted using LUKS and btrfs.
-   [Dm-crypt full disk encryption](https://wiki.gentoo.org/wiki/Dm-crypt_full_disk_encryption "Dm-crypt full disk encryption") --- a guide which covers the process of configuring a drive to be encrypted using LUKS and btrfs.
-   [User:Sakaki/Sakaki\'s EFI Install Guide/Preparing the LUKS-LVM Filesystem and Boot USB Key](https://wiki.gentoo.org/wiki/User:Sakaki/Sakaki%27s_EFI_Install_Guide/Preparing_the_LUKS-LVM_Filesystem_and_Boot_USB_Key "User:Sakaki/Sakaki's EFI Install Guide/Preparing the LUKS-LVM Filesystem and Boot USB Key")

## [Ressources externes]

-   The [cryptsetup FAQ](https://gitlab.com/cryptsetup/cryptsetup/wikis/FrequentlyAskedQuestions) hosted on GitLab covers a wide range of frequently asked questions.