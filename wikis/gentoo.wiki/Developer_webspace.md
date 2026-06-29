This guide documents how a Gentoo developer can configure their personal webspace on dev.gentoo.org.

## Contents

-   [[1] [Developer web space]](#Developer_web_space)
    -   [[1.1] [Use and policy]](#Use_and_policy)
    -   [[1.2] [Uploading files]](#Uploading_files)
    -   [[1.3] [Supported languages]](#Supported_languages)
    -   [[1.4] [External resources]](#External_resources)

## [Developer web space]

### [Use and policy]

Within your devspace on woodpecker (dev.gentoo.org) you may create a [public_html] directory accessible at: [[https://dev.gentoo.org/\~username](https://dev.gentoo.org/~username)]. You may store any Gentoo related files in this space such as project documentation, ebuilds/packages you are testing, etc\...

The devspace is for Gentoo related files. You may not host files for your company/home business, pornography, or any file that is considered illegal in the United States (woodpecker is located in the USA). Pages in your [public_html] folder are viewable by the world and their contents should follow the same rules. Devspace may not be used to make money in any way. This includes banner swapping, auctions (or hosting images for your auctions) or Google ads. As usual, common sense should apply to this restriction.

If any files in your space are found to be harmful towards other developers or users on the box or pose a risk to the Gentoo project (such as illegal torrents, pornography, etc\...), Gentoo Infrastructure will suspend your account which will only be unlocked after investigation from Gentoo Developer Relations. In most cases, your developership will be suspended if such files are found. If you are unsure of the impact a file may have on another developer or Gentoo in general please ask your Mentor or someone else appropriate to review it for you.

### [Uploading files]

If your recruiter didn\'t set up the [public_html] directory for you do via the following instructions. For convenience, export your username to a `USERNAME` variable. This will enable you to copy and paste the commands that follow. Be sure to substitute `larry` in the command below for the user name specific to you (most likely your developer nickname):

`user `[`$`]`export USERNAME="larry"`

Logging on to dev.gentoo.org is performed using the ssh keys you have generated and submitted to your mentor with your quiz (or that you have updated in LDAP if your previous key reached expiration):

`user `[`$`]`ssh $@dev.gentoo.org`

    Enter passphrase for key '/home/$/.ssh/id_rsa': (Enter your passphrase)

`user@woodpecker home$``cd ~/ `

`user@woodpecker ~$``mkdir public_html `

`user@woodpecker ~$``chmod -R 755 public_html `

To enable dir indexing if desired:

`user@woodpecker ~$``echo "Options +Indexes" > public_html/.htaccess`

The Infrastructure Project does not make backups of developer files. You are responsible for making backups of any and all files contained in your developer space. I suggest creating a mirror on your local box: [\~/devspace].

Now copy your files using [scp]:

`user `[`$`]`scp index.htm $@dev.gentoo.org:~/public_html`

    Enter passphrase for key '/home/$/.ssh/id_rsa': (Enter your passphrase)

Alternatively the [rsync] command be used:

`user `[`$`]`rsync -ruav -e ssh ~/devspace $@dev.gentoo.org:~/`

    Enter passphrase for key '/home/$/.ssh/id_rsa': (Enter your passphrase)

If either of the above commands failed see the [export] command in the section above in order to properly export your user name. It can also manually substituted into the command. Your choice.

### [Supported languages]

dev.gentoo.org has HTML, SHTML, and PHP available for you to write your web pages.

### [External resources]

-   [https://www.openssh.com](https://www.openssh.com)
-   [https://rsync.samba.org](https://rsync.samba.org)
-   [https://httpd.apache.org/docs/current/howto/htaccess.html](https://httpd.apache.org/docs/current/howto/htaccess.html)

\

Authorship information[]

This page is based on a document formerly found on [gentoo.org](https://www.gentoo.org/).\
The following people contributed to the original document: **Jeffrey Forman, Curtis Napier**\
\
*[Editors: please do **not** add yourself here. Contributions are recorded on each article\'s associated history page, this list is only present to preserve authorship information, as wiki history does not allow for any external attribution.]*