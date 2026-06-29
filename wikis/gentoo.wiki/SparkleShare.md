**Resources**

[[]][Home](http://sparkleshare.org/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/SparkleShare "wikipedia:SparkleShare")

[[]][GitHub](https://github.com/hbons/SparkleShare)

SparkleShare is a cross platform, free, open source, Dropbox-like, git-based collaboration and file sharing tool. SparkleShare harnesses the powerful back end of the Git version control system and OpenSSH to provide version controlled backups of each file placed in its repository. The SparkleShare client provides a super simple user interface in the form of a small tray applet.

SparkleShare is broken into two components: a *client* and a *host*. This article will help the user install and configure both components in order to obtain a working SparkleShare environment.

## Contents

-   [[1] [USE Configuration]](#USE_Configuration)
-   [[2] [Features and limitations]](#Features_and_limitations)
    -   [[2.1] [Future]](#Future)
-   [[3] [Client]](#Client)
-   [[4] [Host]](#Host)
-   [[5] [See also]](#See_also)

## [USE Configuration]

There are currently no USE flags for SparkleShare.

## [Features and limitations]

Version control is built into SparkleShare which makes it perfect for the self-hosting of text-based files, office documents, and small image files. Since Git does not do well handling binary or compressed files, SparkleShare does **not** make a good full computer backup utility. It also does not do well handling binary files or files in semi-compressed or compressed states. Most modern media files (such as [.ogg], [.mp3], [.aac], [.mpeg], [.jpeg], etc.) are already in semi-compressed or compressed states and should not be added to SparkleShare repositories.

### [Future]

There are plans to include [git-bin](https://github.com/Mighty-M/git-bin) in SparkleShare which would greatly improve its capabilities in dealing with binary and any files in compressed states, however the implementation of git-bin into SparkleShare is yet to be complete. The developer may never integrate this feature.

## [Client]

As with most packages in the Portage Tree, SparkleShare can be installed with a simple emerge command. Emerging [[[net-misc/sparkleshare]](https://packages.gentoo.org/packages/net-misc/sparkleshare)[]] will install both the host and the client SparkleShare components:

`root `[`#`]`emerge --ask net-misc/sparkleshare`

If the current PC is a client, the installation is now complete. The client should now show up in the desktop environment\'s list of installed programs. After it is started a small applet should appear in the panel.

For host installation and configuration continue reading.

## [Host]

Installing the SparkleShare *host* requires a bit more configuration than the client.

The first step in host configuration is to download the Dazzle script from the [Dazzle GitHub page](https://github.com/hbons/Dazzle). This will require the use of web browser or a command line download utility (`curl` or `wget`).

** Note**\
In order to use [wget] command install the [[[net-misc/wget]](https://packages.gentoo.org/packages/net-misc/wget)[]] package. This package should come installed on Gentoo systems by default.

`root `[`#`]`wget https://raw.github.com/hbons/Dazzle/master/dazzle.sh -O /usr/local/bin/dazzle`

Next make the script executable by using [chmod]:

`root `[`#`]`chmod +x /usr/local/bin/dazzle`

Update the system profile to make the Dazzle script located in [/usr/local/bin] visible as a system command:

`root `[`#`]`source /etc/profile`

After that run [dazzle setup] to setup the SparkleShare *host*:

`root `[`#`]`dazzle setup`

Add each user\'s SSH key to the SparkleShare host by using [dazzle link].

The SparkleShare *client* will generate a SSH key pair combination on the client system. Right click the notification tray icon to copy the SSH key to the clipboard. It is then possible to use [ssh] to run the [dazzel link] on the host system, and the ssh key can be copied into the [dazzel] script.

Alternatively the users\' SSH key can be put on a USB drive or transferred using [scp]. Ultimately it does not matter how the key is transfers, as long as it can be entered on the host when [dazzle] prompts.

`root `[`#`]`dazzle link`

After the user has been granted access to the SparkleShare service on the host system one more more projects will need to be created. Each project is new a repository. Use [dazzle create] on the *host* followed by the project name to generate the project(s):

`root `[`#`]`dazzle create PROJECT_NAME`

** Note**\
Run the above step for as many projects as desired.

That is it! The host has successfully been configured!

## [See also]

-   [Dropbox](https://wiki.gentoo.org/wiki/Dropbox "Dropbox") --- a closed source file synchronization and cloud service utility built from open and closed source software.
-   [Owncloud](https://wiki.gentoo.org/wiki/Owncloud "Owncloud") --- a free, open source, Dropbox-like file synchronization and cloud service.