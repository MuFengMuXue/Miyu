**Resources**

[[]][Home](https://about.gitlab.com/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/GitLab "wikipedia:GitLab")

[[]][GitLab (community ebuild repo)](https://gitlab.awesome-it.de/overlays/gitlab)

[[]][GitWeb](https://gitlab.com/gitlab-org/gitlab)

[[]][GitHub](https://github.com/gitlabhq/gitlabhq)

This article explains how to set up a self hosted **GitLab** instance.

The Gitlab overlay, originally the CVUT overlay, is currently on par with the latest GitLab version (16.6.0 as of November 2023). The repo and issues can be found [here](https://gitlab.awesome-it.de/overlays/gitlab).

With version 13.8.3 the former [[[www-apps/gitlabhq]](https://packages.gentoo.org/packages/www-apps/gitlabhq)[]] package was renamed to [[[www-apps/gitlab]](https://packages.gentoo.org/packages/www-apps/gitlab)[]]. Since the [gitlab] core and [gitlab-gitaly] must necessarily have the same version the former [[[dev-vcs/gitlab-gitaly]](https://packages.gentoo.org/packages/dev-vcs/gitlab-gitaly)[]] package was abandoned and [gitlab-gitaly] is now included in the [[[www-apps/gitlab]](https://packages.gentoo.org/packages/www-apps/gitlab)[]] package.

By means of \"Post Deployment Migrations\" as described [here](https://gitlab.com/gitlab-org/gitlab-foss/-/blob/master/doc/development/database/post_deployment_migrations.md) starting with version 13.8.4 upgrading takes place without downtime (Nearly: The still required restart needs some time). This made the slots obsolete and so the upgrade procedure less complicated.

The migration from a [[[www-apps/gitlabhq]](https://packages.gentoo.org/packages/www-apps/gitlabhq)[]] installation to a [[[www-apps/gitlab]](https://packages.gentoo.org/packages/www-apps/gitlab)[]] one is supported by all [www-apps/gitlab-13.8.x] ebuilds.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Preparations]](#Preparations)
    -   [[1.3] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Files]](#Files)
    -   [[2.2] [Web server]](#Web_server)
-   [[3] [Testing]](#Testing)
    -   [[3.1] [Diagnostics]](#Diagnostics)
-   [[4] [Usage]](#Usage)
    -   [[4.1] [Service]](#Service)
        -   [[4.1.1] [OpenRC]](#OpenRC)
        -   [[4.1.2] [systemd]](#systemd)
-   [[5] [Upgrade]](#Upgrade)
-   [[6] [Backup]](#Backup)
-   [[7] [External resources]](#External_resources)

## [Installation]

The [gitlab](https://repos.gentoo.org/#gitlab) ebuild repository must first be configured to be used by Portage. It can be added [manually](https://wiki.gentoo.org/wiki//etc/portage/repos.conf "/etc/portage/repos.conf"), but is more easily configured using [eselect repository](https://wiki.gentoo.org/wiki/Eselect/Repository "Eselect/Repository") (this may need to be installed, see preceding article).

To add using [eselect repository]:

`root `[`#`]`eselect repository enable gitlab `

`root `[`#`]`emaint sync -r gitlab `

GitLab requires the use of a database backend. Since version 12 [PostgreSQL](https://wiki.gentoo.org/wiki/PostgreSQL "PostgreSQL") is the only supported database.

### [USE flags]

[USE flags] www-apps/gitlab

    U I
    - - favicon       : For the Custom Favicon to work, GraphicsMagick needs to be installed
    + + gitaly_git    : Use the Git version provided by Gitaly
    - - gitlab-config : Config in /opt/gitlab/gitlab/config instead of /etc/gitlab (s. news 2021-02-22-etc-gitlab)
    - - kerberos      : Add kerberos support
    - - mail_room     : Enables support for GitLab MailRoom
    - - pages         : Pulls in the compatible version of www-apps/gitlab-pages
    - - prometheus    : Enables support for the Prometheus monitoring system
    - - relative_url  : Support for relative url
    + + systemd       : Enable use of systemd-specific libraries and features like socket activation or session tracking

The `gitaly-config` USE flag is explained in the [2021-02-22-etc-gitlab](https://gitlab.awesome-it.de/overlays/gitlab/-/blob/master/metadata/news/2021-02-22-etc-gitlab/2021-02-22-etc-gitlab.en.txt) news of the overlay (since version 13.11.4 its default changed to *on*, as recommended by upstream). The `gitaly_git` USE flag uses the bundled Git from gitlab-gitaly instead of [[[dev-vcs/git]](https://packages.gentoo.org/packages/dev-vcs/git)[]]. The former `puma` and `unicorn` USE flags were removed because with GitLab 14.0 Unicorn was removed by upstream and Puma is now the only supported web server. The `systemd` USE flag is preselected since the maintainer of the overlay ran out of OpenRC hosts for init script testing. :-) But with the help of some users of the overlay the OpenRC init scripts will be provided further on.

### [Preparations]

Add the following keywords to be accepted by Portage (we use amd64 as architecture here; x86 is also available):

[FILE] **`/etc/portage/package.accept_keywords/gitlab`Keywords**

    www-apps/gitlab ~amd64
    dev-vcs/gitlab-shell ~amd64
    =dev-ruby/rubygems-3.5* ~amd64

The overlay overrides the gentoo [[[acct-user/git]](https://packages.gentoo.org/packages/acct-user/git)[]] package introducing a new USE flag `gitlab` which creates the [git] user as required by [[[www-apps/gitlab]](https://packages.gentoo.org/packages/www-apps/gitlab)[]] with `HOME` in [/var/lib/gitlab/] and as member in the [redis] group. Add the USE Flag:

`root `[`#`]`echo "acct-user/git gitlab" >> /etc/portage/package.use/gitlab`

### [Emerge]

After emerging the package the ebuild will give detailed instructions for the initial setup. This will cover:

1.  Creating and preparing the Postres database
2.  Editing [/etc/gitlab/database.yml] in order to configure database settings for \"production\" environment
3.  Editing [/etc/gitlab/gitlab.yml] in order to configure the GitLab settings
4.  Configuring and restarting redis
5.  Applying config changes and starting Gitaly
6.  Finally running [emerge \--config]

Note that the database specified in [/etc/gitlab/database.yml] will be deleted by the *Initializing database* step of [emerge \--config]!

Also the [emerge \--config] will ask for password and email of the initial administrator account of the GitLab web application. It should be a working email address as on startup GitLab will send an *Access to the GitLab Instance group was grante* mail to this address.

Now copy one of the nginx example configs, at least [gitlab-ssl], (plus [gitlab-pages-ssl] if pages is used) from [/opt/gitlab/gitlab/lib/support/nginx/] to [/etc/nginx/sites/] and adopt them as needed.

Finally start Nginx and GitLab, log in with the administrator account and check/adopt the default settings.

## [Configuration]

### [Files]

GitLab expects the parent directory of the config files to be its base directory, so the config has to stay in [/opt/gitlab/gitlab/config/]. Symlinking [/opt/gitlab/gitlab/config -\> /etc/gitlab] doesn\'t work as GitLab uses the real path of the config files to get the parent directory. In order to use the standard Gentoo way of managing config files, the config files are copied to [/etc/gitlab/] where they are edited and then synced back to [/opt/gitlab/gitlab/config/] each time the service is (re)started or by running:

`root `[`#`]`rsync -aHAX /etc/gitlab/ /opt/gitlab/gitlab/config/`

** Note**\
Note that the trailing slashes are important here!

This [rsync] command is run automatically on start/restart of Gitlab. Only before the [emerge \--config] of the first installation this has to be run manually as GitLab was\'n started yet but the [emerge \--config] needs the up-to-date config. The [rsync] command updates only those config files in [/opt/gitlab/gitlab/config/] that exist in [/etc/gitlab/], so it suffices to have only the changed ones in [/etc/gitlab/].

When the `gitlab-config` USE flag is set [/etc/gitlab/] isn\'t used and the config files must be edited in [/opt/gitlab/gitlab/config/] directly.

### [Web server]

NGINX is the officially supported web server for GitLab. See [opt/gitlab/gitlab/lib/support/nginx/gitlab-ssl] for an example site configuration. For using a different web server, see [GitLab recipes](https://gitlab.com/gitlab-org/gitlab-recipes/).

The web interface is available at the URL configured here:

[FILE] **`/etc/gitlab/gitlab.yml`**

    ## GitLab settings
      gitlab:
        ## Web server settings (note: host is the FQDN, do not include http://)
        host: gitlab.<sample-domain>
        port: 443 # Set to 443 if using HTTPS, see installation.md#using-https for additional HTTPS configuration details
        https: true # Set to true if using HTTPS, see installation.md#using-https for additional HTTPS configuration details

With the above the URL would be [https://gitlab.\<sample-domain\>].

## [Testing]

### [Diagnostics]

Run this command as user [git] to get a full diagnostic.

`git #``cd /opt/gitlab/gitlab`

`git #``bundle exec rake gitlab:env:info RAILS_ENV=production `

`git #``bundle exec rake gitlab:check RAILS_ENV=production `

## [Usage]

### [Service]

#### [OpenRC]

Starting *gitlab*:

`root `[`#`]`rc-service gitlab start`

Current status:

`root `[`#`]`rc-service gitlab status`

Starting automatically at system boot:

`root `[`#`]`rc-update add gitlab default`

#### [systemd]

Starting *gitlab:*

`root `[`#`]`systemctl start gitlab.target`

Current status:

`root `[`#`]`systemctl list-dependencies gitlab.target`

Starting automatically at system boot:

`root `[`#`]`systemctl enable gitlab.target`

## [Upgrade]

The [www-apps/gitlab] ebuild will check if one is on a supported \"Upgrade path\" (see the upstream update [doc/update/index.md#upgrade-paths](https://gitlab.com/gitlab-org/gitlab-foss/-/blob/master/doc/update/index.md#upgrade-paths)) to ensure that the requirements for \"Upgrading without downtime\" are met. The upgrade steps are:

`root `[`#`]`emerge -u gitlab`

1.

<!-- -->

    ...
    * Migrating database without post deployment migrations ...
    *
    * Update the config in /etc/gitlab and then run
    *      systemctl restart gitlab.target
    *
    * To complete the upgrade of this GitLab instance, run:
    *     emerge --config "=www-apps/gitlab-16.6.0"
    *
    *
    * Note: With gitaly_git USE flag enabled the included git was installed to
    *       /opt/gitlab/gitlab-gitaly/bin/. In order to use it set the
    *       [git] "bin_path" variable in "/etc/gitlab-gitaly/config.toml" and in
    *       "/etc/gitlab/gitlab.yml" to "/opt/gitlab/gitlab-gitaly/bin/git"

1.

If there are config updates (there were none in the above example output), do a [dispatch-conf] before the restart:

`root `[`#`]`dispatch-conf`

`root `[`#`]`systemctl daemon-reload`

`root `[`#`]`systemctl restart gitlab.target`

Then do the database migrations **with** post deployment migrations by executing:

`root `[`#`]`emerge --config "=www-apps/gitlab-16.6.0"`

1.

<!-- -->

    Configuring pkg...

    * Migrating database ...
    * Clean up cache ...
    *
    * To check the application status run this:
    * $ cd /opt/gitlab/gitlab
    * $ sudo -u git ruby /usr/bin/bundle exec rake gitlab:check RAILS_ENV=production
    *
    * GitLab is prepared now.
    * Ensure beeing still up-to-date with the latest NGINX configuration changes:
    * $ cd /opt/gitlab/gitlab
    * $ git -P diff v16.5.2:lib/support/nginx/ v16.6.0:lib/support/nginx/

1.

## [Backup]

Besides the regular (daily) backup of the database server it\'s also recommended to do a backup with the GitLab backup tool:

`git #``cd /opt/gitlab/gitlab`

`git #``bundle exec rake gitlab:backup:create RAILS_ENV=production`

This creates a complete GitLab-Backup (see the [GitLab-Docs](https://docs.gitlab.com/ee/raketasks/backup_gitlab.html) for what\'s included) to the backup path configured in [/etc/gitlab/gitlab.yml]. Just create a systemd timer or cron job to run this e. g. daily.

## [External resources]

-   [ArchWiki GitLab](https://wiki.archlinux.org/index.php/GitLab) - can be helpful while configuration section is incomplete in Gentoo wiki.
-   [Official documentation](https://docs.gitlab.com/)
-   [Configuration files Documentation](https://gitlab.com/gitlab-org/gitlab-foss/-/blob/master/config/README.md)