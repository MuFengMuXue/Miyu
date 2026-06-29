# Package Maintainer guidelines

Package Maintainers are Arch Linux staff members charged with keeping the AUR in working order. They maintain popular packages (communicating with and sending patches upstream as needed), and vote in administrative matters. A Package Maintainer is elected from active community members by current Package Maintainers in a democratic process. Package Maintainers are the only members who have a final say in the direction of the AUR.

The Package Maintainers are governed using the Package Maintainer bylaws

## TODO list for new Package Maintainers
# Read this entire wiki article.
# Read the Package Maintainer Bylaws.
# Make sure your account details on the AUR are up-to-date.
# Ask one of your sponsors to give you the Package Maintainer status on the AUR.
# Remind a bureaucrat (see ArchWiki:Maintenance Team#Active maintainers for the list of active ones) to add your wiki account to the  group.
# Remind a BBS admin to change your account on forums.
# Ask one of your sponsors for the #archlinux-staff and #archlinux-packaging keys and join us in the channels (this is not mandatory, but a great way of getting to know parts of the team and collaborate).
#* If you need a bouncer, ask heftig for a Matrix invite.
#* If you want an  cloak, ask our group contacts to get you one.
# Ask one of your sponsors to create a ticket in the infrastructure repository issue tracker (using the  template) and provide them with the following information:
#* An SSH public key. If you do not have one, follow SSH keys#Generating an SSH key pair to create one.
#* A username which will be used for your SSO account and for your (to be created)  email address.
#* Your full name.
#* Your (personal) e-mail address and a valid PGP public key ID for it, which will be used to provide the initial password for the developer interface (archweb) to you and which will be linked to your (to be created) SSO account.
#* Whether your private or your (to be created)  email address should be used for the non-public mailing lists and be allowed to post to the arch-dev-public mailing list.
# Set the password for your  e-mail address by following developer-manual:staff-services#email.
# Create a PGP key pair for package signing by following the workflow for adding a new packager key (using your new  address as uid).
# Ask one of your sponsors to create a ticket in the archlinux-keyring repository issue tracker (using the  template) in order to have your PGP key signed by (at least) three main key holders.
# Optionally enable bugbuddy to get assigned to unconfirmed issues and bumpbuddy to get assigned to out-of-date issues for your packages by reacting with the related emojis to this issue.
# Install the  package.
# Configure your private ssh key for .
# Ssh to  (once you have permissions).
# Start contributing!

## Junior maintainership
Since the ratification of RFC 0014, new Package Maintainers will be marked as "junior" for their first two months of packaging. During this time, the new Package Maintainer may only push to the extra-testing repository. Your sponsors can review your packages as-needed and move them to extra.

## The Package Maintainer and the AUR
The Package Maintainers should also make an effort to check package submissions in the AUR for malicious code and good PKGBUILDing standards.  In around 80% of cases the PKGBUILDs in the AUR are very simple and can be quickly checked for sanity and malicious code by the Package Maintainer team.

Package Maintainers should also check PKGBUILDs for minor mistakes, suggest corrections and improvements.  The Package Maintainer should endeavor to confirm that all packages follow the Arch Packaging Guidelines/Standards and in doing so share their skills with other package builders in an effort to raise the standard of package building across the distribution.

Package Maintainers are also in an excellent position to document recommended practices.

## Rewriting git history
In some cases rewriting the history of an AUR repository is required, for example when a user inadvertently uses their legal name in a published commit. This can be automated with .

To force push the new history, forward the  environment variable to .

In detail this includes adding  to your AUR SSH config and setting the env var on your push command: .
See for details.

; Modify committer or author identity

Install  and run:

 $ git-filter-repo --name-callback 'return name.replace(b"Old name", b"New name")' --email-callback 'return email.replace(b"old@email.com", b"new@email.com")'

Alternatively, use  with the , ,  and  environment variables. For example:

## Handling AUR requests
Package Maintainers should periodically check the [https://aur.archlinux.org/requests requests filed on the AUR. For that there are some generic rules what to check for each request type:

; Orphan request

* check if the request is older then 14 days (the date column turns red in the overview) (you cannot accept it before that anyway)
* check if there was no update to the package itself (commit or release) done in the past 14 days
* check if there was no comment from the AUR package maintainer done in the past 14 days

If all of the above points are true then you can accept the Orphan Request.

## The Package Maintainer and extra, guidelines for package maintenance
## Rules for packages entering the extra repository
* A package must not already exist in any of the Arch Linux repositories. You should take necessary precautions to ensure no other packager is in the process of promoting the same package. Double-check the AUR package comments, read the latest subject headings in aur-general, grep the , and send a quick message to the private packaging IRC channel.
* Pacman wrappers, as a special exception, will never be permitted. If wanting to otherwise add an AUR helper, write an email to  with the proposed addition, and respect any objections provided by team members.

* Only "popular" packages may enter the repository, as defined by 1% usage from pkgstats or 10 votes on the AUR.
* Automatic exceptions to this rule are:
** i18n packages
** accessibility packages
** drivers
** dependencies of packages who satisfy the definition of popular, including makedeps and optdeps
** packages that are part of a collection and are intended to be distributed together, provided a part of this collection satisfies the definition of popular
* Any additions not covered by the above criteria must first be proposed on the aur-general mailing list, explaining the reason for the exemption (e.g. renamed package, new package). The agreement of three other Package Maintainers is required for the package to be accepted into extra. Proposed additions from Package Maintainers with large numbers of "non-popular" packages are more likely to be rejected.
* Package Maintainers are strongly encouraged to move packages they currently maintain from extra if they have low usage. No enforcement will be made, although resigning Package Maintainers packages may be filtered before adoption can occur.
* It is good practice to always bump the pkgrel by 1 (in other words, set it to n + 1) when promoting a package from AUR. This is to facilitate automatic updates for those who already have the package installed, so that they may continue to receive updates from the official channel. Another positive effect of this is that users are not warned that their local copy is newer, as is the case if a packager does reset the pkgrel to 1.
* Build scripts for all official packages are provided under the 0BSD licenseIf build scripts in the AUR package are not explicitly licensed under 0BSD, they need to be rewritten.

## Accessing and updating the repository
See the packager guide.

## Disowning packages
If a Package Maintainer cannot or does not want to maintain a package any longer, a notice should be posted to the AUR Mailing List, so another package maintainer can
maintain it. A package can still be disowned even if no other Package Maintainer wants to maintain it, but the Package Maintainers should try not to drop many packages (they should not take on more than they have time for). If a package has become obsolete or is not used any longer, it can be removed completely as well.

If a package has been removed completely, it can be uploaded once again (fresh) to the AUR, where a regular user can maintain the package instead of the Package Maintainer.

## Moving packages from the AUR to extra
Follow the normal procedures for adding a package to extra using the instructions in the packager guide, but remember to delete the corresponding package from the AUR!

## Moving packages from extra to the AUR
Remove the package using the instructions in the packager guide and upload your source to the AUR.

## Moving packages from extra-testing to extra
Move the package from the extra-testing to the extra repository using the instructions in the packager guide.

## Remote build on build.archlinux.org
Package Maintainers and Developers can connect to build.archlinux.org via SSH to, among others, build packages using the devtools.
This has numerous advantages over a local setup:

* Builds are fast and network speed is high.
* The environment needs setup only once.
* Your local system need not be Arch Linux.

The process is similar to that of a local setup with devtools.  Your GnuPG private is required for signing but you do not want to upload it for obvious security reasons.  As such, you will need to forward the GnuPG agent socket from your local machine to the server: this will allow you to sign packages on the build server without communicating your key.  This also means that we need to disable the agent on the server before we can run anything.

First, connect to build.archlinux.org and disable

 $ ssh build.archlinux.org
 $ systemctl --user mask gpg-agent.service

Make sure gpg-agent is not running ().  At this point, make sure that no sockets exist in the folder pointed by .  If they do, remove them or log out and in again.
If you have a custom $GNUPGHOME (eg. to move it to ), you will need to unset that, as it is not possible in gnupg to set the homedir without setting the socketdir.
On build.archlinux.org,  is set in , therefore removing the sockets manually on logout is not necessary.

While the PGP private keys remain on your local machine, the public keys must be on the build server.  Export your public ring to the build server, e.g. from you local machine

 $ scp ~/.gnupg/pubring.gpg build.archlinux.org:~/.gnupg/pubring.gpg

SSH is required to checkout and commit to the Git repository.  You can either set up a new SSH key pair on the server (it is highly discouraged to put your local private key on a server for security reasons) or reuse your local keys via socket forwarding.  If you opt for the latter, make sure to disable ssh-agent on the build server if you had enabled it previously (it is not running by default).

Configure you build environment on the build server:

Disable passphrase caching with the following settings:

Because we will want to keep our usual GPG agent running with its current settings, we are going to run another GPG agent dedicated to the task at hand.  Create a  folder and symlink everything from  there, except . Configure the new GPG agent:

The  will be forwarded to build.archlinux.org.

Start the dedicated agent with

 $ gpg-agent --homedir ~/.gnupg-archlinux --daemon

Connect with:

 $ ssh -R REMOTE_SSH_AUTH_SOCK:$SSH_AUTH_SOCK -R /run/user/REMOTE_UID/gnupg/S.gpg-agent:/home/doe/.gnupg-archlinux/S.gpg-agent.extra build.archlinux.org

or, if using GnuPG as your SSH agent:

 $ ssh -R /run/user/REMOTE_UID/gnupg/S.gpg-agent.ssh:/run/user/LOCAL_UID/gnupg/S.gpg-agent.ssh -R /run/user/REMOTE_UID/gnupg/S.gpg-agent:/home/doe/.gnupg-archlinux/S.gpg-agent.extra build.archlinux.org

Replace  and  by your user identifier as returned by  on the build server and locally, respectively.
If using ssh-agent, replace  by the path to the SSH socket on the remote host (it can be anything).

You can make the forwarding permanent for that host.  For instance with gpg-agent.ssh:

Again, replace  with the user UID on the build server.

From then on, the procedure should be exactly the same as a local build:

 $ ssh build.archlinux.org
 $ pkgctl repo clone existing-package
 $ ...

## TODO list retiring a Package Maintainer
When a Package Maintainer resigns the following list has be followed, these steps do not apply when a Package Maintainer resigns but is still a Developer.

# All packages packaged by the retiree should be resigned (so rebuild). Packages packaged by the retiree can be found in Archweb https://archlinux.org/packages/?sort=&q=&packager=$packager&flagged= where packager is the username on Archweb.
# The account of the retiree should be disabled on Archweb and added to the 'Retired Package maintainers' group. The retiree should be removed from the 'Package Maintainers' and the repository permissions should be reduced to none.
# The shell access to our servers should be disabled. (notably repos.archlinux.org, pkgbuild.com)
# The GPG key should be removed and a new archlinux-keyring package should be pushed to the repos. Create bug reports in the keyring project to remove the keys of the retired Package Maintainers.
# Remove the Package Maintainer group from their AUR account.
# A bureaucrat should remove their wiki account from the  group.
# A [https://bbs.archlinux.org/userlist.php?username=&show_group=1&sort_by=username&sort_dir=ASC&search=Submit BBS admin should change their account on forums.
