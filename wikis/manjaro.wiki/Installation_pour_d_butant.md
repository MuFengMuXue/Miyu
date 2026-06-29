## Contents

-   [[1] [Installation pour débutant]](#Installation_pour_d.C3.A9butant)
    -   [[1.1] [Téléchargement et Vérification]](#T.C3.A9l.C3.A9chargement_et_V.C3.A9rification)
        -   [[1.1.1] [Téléchargement]](#T.C3.A9l.C3.A9chargement)
        -   [[1.1.2] [Vérification]](#V.C3.A9rification)
    -   [[1.2] [Utilisation de l\'image]](#Utilisation_de_l.27image)
        -   [[1.2.1] [Virtualisation]](#Virtualisation)
        -   [[1.2.2] [Graver l\'image sur un disque]](#Graver_l.27image_sur_un_disque)
    -   [[1.3] [Démarrer sur le disque]](#D.C3.A9marrer_sur_le_disque)
        -   [[1.3.1] [Modifier les options du BIOS/UEFI]](#Modifier_les_options_du_BIOS.2FUEFI)
        -   [[1.3.2] [Démarrer sur le disque]](#D.C3.A9marrer_sur_le_disque_2)
    -   [[1.4] [Gestionnaire d\'installation]](#Gestionnaire_d.27installation)
        -   [[1.4.1] [Installer Manjaro à côté d\'un autre système]](#Installer_Manjaro_.C3.A0_c.C3.B4t.C3.A9_d.27un_autre_syst.C3.A8me)
        -   [[1.4.2] [Installer Manjaro sur mon disque dur]](#Installer_Manjaro_sur_mon_disque_dur)
        -   [[1.4.3] [Installer Manjaro sur un disque externe]](#Installer_Manjaro_sur_un_disque_externe)
        -   [[1.4.4] [Partitionnement manuel]](#Partitionnement_manuel)
    -   [[1.5] [Renseignement des informations complémentaires]](#Renseignement_des_informations_compl.C3.A9mentaires)
    -   [[1.6] [Résumé]](#R.C3.A9sum.C3.A9)
-   [[2] [Après l\'installation]](#Apr.C3.A8s_l.27installation)

Pour un autre type d\'installation, consultez la page [Manjaro architect](//wiki.manjaro.org/index.php?title=Installation_with_Manjaro_Architect/fr "Installation with Manjaro Architect/fr").

# [][Installation pour débutant]

Cette page regroupe toutes les instructions nécessaires pour bien installer Manjaro sur votre système.

## [][Téléchargement et Vérification]

Dans cette partie, nous allons télécharger une image disque de Manjaro et vérifier son intégrité.

### [][Téléchargement]

Dans un premier temps, vous aurez besoin d\'une image disque de Manjaro. Ce genre de fichiers sont facilement reconnaissables à leur extension en .iso. Vous n\'avez qu\'à consulter ce **[lien](//wiki.manjaro.org/index.php?title=Download_Manjaro/fr "Download Manjaro/fr")** pour savoir comment faire.

Je vous conseille de choisir un téléchargement par torrent si vous en avez la possibilité, ce dernier permettant une rapidité de réception des données plus accrue que par le navigateur. Si vous vous sentez d\'une âme charitable, vous en profiterez pour laisser le logiciel ouvert un petit temps après, afin de faire bénéficier les autres d\'un temps encore plus rapide.

### [][Vérification]

Une fois l\'image disque téléchargé, il va falloir vérifier son intégrité, c\'est-à-dire, si elle nous a bien été livrée en entier, et ce dans le but d\'éviter les erreurs au démarrage. Si ce n\'est pas le cas, il vous faudra donc recommencer le téléchargement.

Pas d'inquiétudes à avoir, la vérification est assez facile, pour peu que vous lisiez **[cette page](//wiki.manjaro.org/index.php?title=Check_a_Downloaded_ISO_Image_For_Errors/fr "Check a Downloaded ISO Image For Errors/fr")**

## [][Utilisation de l\'image]

Vous avez à présent une image téléchargée sur votre bureau, vous l\'avez vérifié, mais ne savez pas trop quoi en faire. Eh bien, deux options s\'offrent à vous : la virtualisation ou la gravure.

### [Virtualisation]

La virtualisation permet à une machine hôte le lancement d\'une machine fille dans une boîte où aucune intéraction n\'est possible entre les deux sans l\'accord préalable de l\'utilisateur. Cette technique permet d\'utiliser une image disque sans avoir à altérer votre disque dur ni le système d\'exploitation principal de votre machine. Cependant, les performances ne seront pas les meilleurs, car la machine fille ne pourra pas tirer toute la puissance potentielle de son hôte...

Une image disque de Manjaro peut tout à fait être utilisée pour de la virtualisation à l\'aide d\'un logiciel comme **[Virtualbox](https://www.virtualbox.org/)**. Nous ne donnerons pas les instructions ici, mais pouvons vous rediriger vers le **[manuel du logiciel](http://www.virtualbox.org/manual/)**.

### [][Graver l\'image sur un disque]

Finalement vous avez décidé d\'utiliser Manjaro comme un vrai système d\'exploitation et pas seulement comme une vulgaire machine qu\'on visualise. Félicitations !

Graver l\'image, téléchargée au préalable, sur un disque, ou tout autre périphérique de stockage, vous permettra d\'y accéder depuis votre machine en démarrant directement sur le nouveau système. Si le mot peut faire peur, les instructions, elles, sont très simples, et répertoriés sur **[cette page](//wiki.manjaro.org/index.php?title=Burn_an_ISO_File/fr "Burn an ISO File/fr")**.

## [][Démarrer sur le disque]

Maintenant que notre petit disque est prêt, nous allons pouvoir enfin démarrer dessus !

### [][Modifier les options du BIOS/UEFI]

Lorsque nous allons démarrer sur le disque, il y a de forte possibilité pour que votre ordinateur affiche un message peu amical contenant une indication comme quoi Secure Boot aurait été malmené. C\'est une erreur qui n\'est pas très grave, mais qui levée par le système, vous empêchera d\'accéder à Manjaro.

Il va donc falloir accéder au firmware de votre ordinateur, c\'est-à-dire, le logiciel fabriqué par le constructeur de votre machine, et sur lequel vous allez pouvoir modifier certaines options pour que ce genre d\'erreurs ne se reproduisent plus. Les deux systèmes les plus utilisés sont **[BIOS et UEFI](//wiki.manjaro.org/index.php?title=BIOS_and_UEFI/fr "BIOS and UEFI/fr")** (nous ne nommerons que BIOS afin de simplifier la lecture), et l\'accès à ce genre de programme dépend du système. Internet reste votre plus grand ami pour répondre à vos questions.

### [][Démarrer sur le disque]

Puisque vous savez comment accéder au BIOS, vous en profiterez pour modifier l\'ordre de démarrage sur le système. Pour ce faire, branchez votre disque à l\'ordinateur, revenez sur le BIOS, et faites en sorte que le périphérique soit en haut de la liste dans l\'onglet \"Boot Order\" (ou tout autre onglet similaire).

Vous pouvez dès lors redémarrer le système en laissant le disque branché, et admirez le démarrage de Manjaro.

[![Kde desktop screenshot.jpg](/images/thumb/1/15/Kde_desktop_screenshot.jpg/700px-Kde_desktop_screenshot.jpg)](//wiki.manjaro.org/index.php?title=File:Kde_desktop_screenshot.jpg)

## [][Gestionnaire d\'installation]

[![Installer homepage.png](/images/thumb/1/1b/Installer_homepage.png/450px-Installer_homepage.png)](//wiki.manjaro.org/index.php?title=File:Installer_homepage.png)

[](//wiki.manjaro.org/index.php?title=File:Installer_homepage.png "Enlarge")

Ça y est, vous êtes enfin sur le bureau de Manjaro, et, peu importe l\'édition que vous avez choisie, une icône vous proposant d\'installer Manjaro se trouve sur l\'écran.

Cliquez dessus pour commencer l\'installation de votre tout nouveau système d\'exploitation. Une fenêtre comme celle présente sur la gauche devrait alors apparaître.

Changeons dans un premier temps la langue pour la mettre en français, cette étape n\'est pas obligatoire, mais permettra à ceux moins à l\'aise avec la langue de Shakespeare d\'avoir une utilisation compréhensible de leur ordinateur.

[![Installer homepage fr.png](/images/thumb/2/2a/Installer_homepage_fr.png/450px-Installer_homepage_fr.png)](//wiki.manjaro.org/index.php?title=File:Installer_homepage_fr.png)

[](//wiki.manjaro.org/index.php?title=File:Installer_homepage_fr.png "Enlarge")

Le gestionnaire vous précise également que l\'ordinateur n\'est pas connecté à Internet, et s\'il n\'est pas branché à une source de courant par la même occasion. Connecter votre ordinateur à Internet lui permettra d\'exécuter une mise à jour simultanément à l\'installation, le système sera alors pleinement opérationnel, là où sans Internet, vous n\'aurez les versions des paquets disponibles qu\'à partir de la création de l\'image disque par Manjaro. De même, brancher votre ordinateur pour que l\'énergie ne lui manque pas est fortement recommandé, cela évitera les mauvaises surprises comme l\'extinction en plein processus (qui peut prendre de 5 à 30 minutes en fonction des machines).

\

Les deux fenêtres qui viennent ensuite vous proposent d\'indiquer votre lieu de résidence, et ce afin de vous proposer une heure cohérente à votre situation, ainsi que de changer la disposition de votre clavier, en l\'occurrence pour nous, en AZERTY.

[![Installer location fr.png](/images/thumb/3/31/Installer_location_fr.png/400px-Installer_location_fr.png)](//wiki.manjaro.org/index.php?title=File:Installer_location_fr.png)

[![Installer keyboard fr.png](/images/thumb/c/cc/Installer_keyboard_fr.png/400px-Installer_keyboard_fr.png)](//wiki.manjaro.org/index.php?title=File:Installer_keyboard_fr.png)

\
\
\
\
\
\
\
\
\

L\'étape suivante concerne la gestion des disques. C\'est une étape un peu plus complexe que les précédentes mais pas du tout insurmontable, et qui va surtout vous contrarier par le nombre incalculable de possibilités. En effet, partitionner ses disques est un cas personnel pour chaque utilisateur de Manjaro, et nous allons tenter ici de vous aiguiller sur celle qui vous correspondra le mieux.

### [][Installer Manjaro à côté d\'un autre système]

Pour ce faire, sélectionner l\'option \"Installer à côté\", cliquez sur une des partitions que vous voudriez réduire ou ne touchez à rien si vous souhaitez que le travail soit fait automatiquement par Manjaro. Vous pouvez valider votre choix et passer à la suite.

[![Installer partition sideToSide fr.png](/images/thumb/8/87/Installer_partition_sideToSide_fr.png/500px-Installer_partition_sideToSide_fr.png)](//wiki.manjaro.org/index.php?title=File:Installer_partition_sideToSide_fr.png)

[](//wiki.manjaro.org/index.php?title=File:Installer_partition_sideToSide_fr.png "Enlarge")

### [Installer Manjaro sur mon disque dur]

Vous n\'avez qu\'à sélectionner \"Effacer le disque\" dans la liste et Manjaro s\'occupera de tout ; vous pouvez passer à la suite ;)

[![Installer partition replace fr.png](/images/thumb/0/06/Installer_partition_replace_fr.png/500px-Installer_partition_replace_fr.png)](//wiki.manjaro.org/index.php?title=File:Installer_partition_replace_fr.png)

[](//wiki.manjaro.org/index.php?title=File:Installer_partition_replace_fr.png "Enlarge")

### [Installer Manjaro sur un disque externe]

[![Installer partition diskChoose fr.png](/images/thumb/b/ba/Installer_partition_diskChoose_fr.png/400px-Installer_partition_diskChoose_fr.png)](//wiki.manjaro.org/index.php?title=File:Installer_partition_diskChoose_fr.png)

[](//wiki.manjaro.org/index.php?title=File:Installer_partition_diskChoose_fr.png "Enlarge")

C\'est tout à fait possible de le faire : branchez votre disque avant de lancer la partie sur la gestion des partitions de l\'installateur, et sélectionnez-le dans la liste qui se trouve en haut à droite. Généralement, les disques sont renommés avec des noms assez compréhensibles (cf : capture d\'écran à droite), mais si ce n\'est pas le cas, repérez celui qui a à peu près la même taille que celle mentionnée sur votre périphérique physique.

Après l\'avoir sélectionné, les mêmes options s\'offrent à vous, je vous recommande cependant d\'installer Manjaro sur l\'entièreté du disque dans ces cas-là.

### [Partitionnement manuel]

Ce cas est un peu plus dur et concerne les utilisateurs un peu plus expérimentés dans l\'utilisation de Linux et des disques. Cependant, si vous vous retrouvez dans la situation où plusieurs partitions doivent être altérées, ce **[lien](//wiki.manjaro.org/index.php?title=Partitioning_Overview_and_Existing_Partition_Tables/fr "Partitioning Overview and Existing Partition Tables/fr")** est fait pour vous.

De la même manière, si vous étiez déjà un utilisateur d\'une autre distribution GNU/Linux avant de venir sur Manjaro, **[garder vos dotfiles](//wiki.manjaro.org/index.php?title=Important_hidden_.dot_files_in_your_home_partition/fr "Important hidden .dot files in your home partition/fr")** quelque part devrait bien vous aider.

## [][Renseignement des informations complémentaires]

L\'installateur va vous demander de rentrer quelques informations à propos de vous, ou plutôt, à propos de l\'utilisateur qui va être créé. Les informations sont les suivantes :

[![Installer informations fr.png](/images/thumb/7/7c/Installer_informations_fr.png/400px-Installer_informations_fr.png)](//wiki.manjaro.org/index.php?title=File:Installer_informations_fr.png)

-   Votre nom, c'est celui qui s'affichera lors de vos connexions et navigations sur l'interface graphique.
-   Votre nom pour la connexion, c'est le nom d'utilisateur que vous utiliserez pour vous connecter à la machine, par terminal ou par interface graphique.
-   Le nom de la machine, laissez libre coure à votre imagination pour celui-là.
-   Votre mot de passe
-   Je vous conseille également de cocher la dernière case afin d'avoir le même mot de passe pour votre compte et celui de l'administrateur, même si ce n\'est pas la meilleure des pratiques pour sécuriser le système.

## [][Résumé]

La dernière fenêtre avant la validation de l\'installation fait le résumé de tout ce que l\'installateur va modifier sur votre système et vos disques. Lisez le bien attentivement afin d\'être sûr et certain qu\'aucun disque ne va être complètement formaté par erreur.

[![Installer checkup fr.png](/images/thumb/7/75/Installer_checkup_fr.png/500px-Installer_checkup_fr.png)](//wiki.manjaro.org/index.php?title=File:Installer_checkup_fr.png)

Il n\'y a plus qu\'à attendre ! Quand l\'installateur aura fini son travail, vous pourrez bénéficier d\'un installation fraîche et fonctionnelle de Manjaro.

# [][Après l\'installation]

Après avoir installé Manjaro, il y a une multitude de choses à faire pour bénéficier à 100 % de votre expérience sur votre nouveau système, les quelques liens ci-dessous vous permettront sûrement de créer et innover en termes d\'utilisation de Linux\...

Dans un premier temps, je vous suggère de vous renseigner un peu plus sur les différents **[environnements](//wiki.manjaro.org/index.php?title=Desktop_Environments_and_Window_Managers/fr "Desktop Environments and Window Managers/fr")** disponibles, mais aussi sur **[Pamac](//wiki.manjaro.org/index.php?title=Pamac/fr "Pamac/fr")**, le gestionnaire de paquet possédant une interface graphique, et son homologue fonctionnant par ligne de commande, **[Pacman](//wiki.manjaro.org/index.php?title=Pacman/fr "Pacman/fr")**.

Si c\'est vraiment la personnalisation qui vous a attiré sur Manjaro, modifier votre **[écran de connexion](//wiki.manjaro.org/index.php?title=Display_Managers_/_Login_Screens/fr "Display Managers / Login Screens/fr")** vous sera peut-être utile. De même, un petit logiciel nommé conky vous permettra d\'afficher plein d\'informations sur le système, le tout sur votre fond d\'écran, alors **[quelques conseils pour le paramétrer](//wiki.manjaro.org/index.php?title=Basic_Tips_for_conky/fr "Basic Tips for conky/fr")** ne seraient pas de trop.