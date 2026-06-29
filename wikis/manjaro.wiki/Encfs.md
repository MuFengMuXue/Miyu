Other languages:

[English] • ‎[Türkçe](//wiki.manjaro.org/index.php?title=Encfs/tr "Encfs (7% translated)") • ‎[русский](//wiki.manjaro.org/index.php?title=Encfs/ru "Encfs (100% translated)")

## Contents

-   [[1] [Introduction]](#Introduction)
-   [[2] [Installing]](#Installing)
-   [[3] [Using it - encrypting]](#Using_it_-_encrypting)
    -   [[3.1] [First time run]](#First_time_run)
    -   [[3.2] [Regular use]](#Regular_use)
-   [[4] [Encrypting Dropbox]](#Encrypting_Dropbox)
-   [[5] [GUI helpers]](#GUI_helpers)

## [Introduction]

Encfs is an encryption program that is suitable for encrypting content on an already installed system. It can be used for encrypting your /home or you can make smaller private directories that can hold your encrypted data. You can encrypt Dropbox with it and that has the advantage over Truecrypt that it does not require reserved valuable space that Truecrypt does (as of 05 2014 [Truecrypt is considered unsafe](http://truecrypt.sourceforge.net/index.html%7C)).

Encfs does not reserve a space on your HD and simply grows and shrinks with the files you put in there.

The one thing that can seem a bit confusing about it is that you need to make two directories (folders) to make it work: one encrypted and one un-encrypted.

*Why would we need an un-encrypted folder that contains the data we want to encrypt; is that not the mother of all security flaws?*

*The entire point with encryption is that the encrypted data should not be accessible in an un-encrypted form; right?*

The way Encfs works is that the un-encrypted directory is the mount point for the encrypted content.

If you do not mount it *nothing* will be visible. And to mount it; you need to enter a given password.

\

**Warning: [EncFS - ArchWiki](https://wiki.archlinux.org/title/EncFS#Installation) says:**

------------------------------------------------------------------------

A [security review (February 2014)](https://defuse.ca/audits/encfs.htm) of encfs discovered a number of security issues in the stable release 1.7.4 (June 2014). Please consider the report and the references in it for updated information before using the release. [see@forum](https://forum.manjaro.org/t/encfs-is-not-so-safe/84983/2)

## [Installing]

Encfs is in the community repo so you can simply install it with your favorite package manager or by using:

    pamac install encfs

\

## [Using it - encrypting]

We want to make a directory that we would call

    .secret

to keep our encrypted stuff, and we would make the mount point

    secret

To achieve this, we run the following command in a terminal:

    encfs ~/.secret ~/secret

You may also create the directories \~/.secret and \~/secret manually.

\

### [First time run]

This will create the hidden directory **.secret** and the mount point **secret** the first time you run it. Just answer yes to the prompts - twice. You need to use the full path. During first time run you will also be prompted for the encryption mode; **x** for expert or **p** for paranoia mode. We will pick **p** which is a good mode.

Next you will be prompted for your password. Make it long and hard to crack but don\'t forget it - if you do; there is no way of recovering your data.

Confirm the password and that\'s it you are finished.

\

### [Regular use]

We have created the directory **\~/.secret** that will contain the encrypted data and we have made it a hidden directory because we will never enter anything in it and the content will all be unreadable.

The content of **\~/.secret** will only be readable when mounted in the other directory we created: **\~/secret** The only difference between the two is the \".\" **\~/secret** will be the working directory where you put the files you want encrypted. To mount the directory we enter the command:

    encfs ~/.secret ~/secret

You may call your directories something completely different than .secret and secret; it is up to you. Enter the password and start entering content into \~/secret.

*We never enter data into \~/.secret - that is why we have hidden it with a \".\"*

To unmount \~/secret we enter the command:

    fusermount -u ~/secret

If you check the content of \~/secret now; it will be completely empty. In order to see the content again you need to mount again with

     encfs ~/.secret ~/secret

and enter the password. This will mount secret as a disk you can do a simple

    df

to check if **secret** is mounted

\

## [Encrypting Dropbox]

One of the strong points of Encfs is that it does not reserve a lot of valuable space. This makes it suitable for encrypting Dropbox content. There is no such thing as 100% security in the cloud, so remember that some things simply do not belong there.\
Keeping that in mind - we create a folder under \~/Dropbox that we call **encrypted** and we create a mount point that we call **Dropbox_unencrypted**. We can create the directories manually or let enfcs auto generate them:

    encfs ~/Dropbox/encrypted ~/Dropbox_unencrypted

Just like under any first time run you accept the creation of the directories with a \"y\" -twice and pick \"p\" for paranoid mode. Then you enter the password.

To access the Dropbox from another computer repeat the exact same procedure there and enter exactly the same password.

\
That is all there is to it - your jiberish unreadable data will now be on the web (in the cloud) in the Dropbox/encrypted folder.\
It will only be readable to you after you have mounted **\~/Dropbox_unencrypted** on your local computer. You will also have the synced **\~/Dropbox/encrypted** folder on your computer , and that will be as unreadable as the content on the web.\
As we have seen above; this content will only be visible when you mount it in \~/Dropbox_unencrypted.\
Again; do not put any content in \~/Dropbox/encrypted: All the content there will be added after you have mounted the working directory - **\~/Dropbox_unencrypted**. To test it you can unmount it with

    fusermount -u ~/Dropbox_unencrypted

and re-mount it with

    encfs ~/Dropbox/encrypted ~/Dropbox_unencrypted

at wich time you will be prompted for the password.

\

## [GUI helpers]

To mount and un-mount there are helpers in AUR that can make the handling easier.

-   cryptkeeper - A Linux system tray applet that manages EncFS encrypted folders
-   kencfs - GUI frontend for encfs. Create, mount, umount and delete your encrypted fs
-   encfsui - Encrypted filesystem encfs GUI wrapper