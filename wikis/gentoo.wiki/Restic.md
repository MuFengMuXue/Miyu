[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Restic&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://restic.net/)

[[]][Official documentation](https://restic.readthedocs.io/en/stable/)

[[]][Package information](https://packages.gentoo.org/packages/app-backup/restic)

[[]][GitHub](https://github.com/restic/restic)

[[]][Bugs (upstream)](https://github.com/restic/restic/issues)

[[]][[#restic](ircs://irc.libera.chat/#restic)] ([[webchat](https://web.libera.chat/#restic)])

[[]][Blog](https://restic.net/#blog)

**Restic** is a [Go](https://wiki.gentoo.org/wiki/Go "Go")-based backup tool built simplicity, scalability, and verifiability in mind. Backups must be sent to a storage repository which can be a local file system or a remote system accessible via [SFTP](https://wiki.gentoo.org/wiki/SFTP "SFTP").

## Contents

-   [[1] [Features]](#Features)
-   [[2] [Installation]](#Installation)
-   [[3] [Configuration]](#Configuration)
    -   [[3.1] [Environment variables]](#Environment_variables)
        -   [[3.1.1] [Restic configuration]](#Restic_configuration)
        -   [[3.1.2] [Amazon Web Services integration]](#Amazon_Web_Services_integration)
        -   [[3.1.3] [OpenStack integration]](#OpenStack_integration)
        -   [[3.1.4] [Backblaze integration]](#Backblaze_integration)
        -   [[3.1.5] [Microsoft Azure integration]](#Microsoft_Azure_integration)
        -   [[3.1.6] [Google Cloud storage integration]](#Google_Cloud_storage_integration)
        -   [[3.1.7] [Vendor agnostic cloud storage integration]](#Vendor_agnostic_cloud_storage_integration)
-   [[4] [Compatibility]](#Compatibility)
-   [[5] [Usage]](#Usage)
    -   [[5.1] [Invocation]](#Invocation)
    -   [[5.2] [Initializing a new local repository]](#Initializing_a_new_local_repository)
    -   [[5.3] [Back up to local storage]](#Back_up_to_local_storage)
    -   [[5.4] [Restore from local storage]](#Restore_from_local_storage)
-   [[6] [Removal]](#Removal)
    -   [[6.1] [Unmerge]](#Unmerge)
-   [[7] [See also]](#See_also)

### [Features]

-   Snapshot-based.
-   Data deduplication.
-   Emphasis on speed of recovery and verifiability of the data integrity.
-   Scriptability.

## [Installation]

`root `[`#`]`emerge --ask app-backup/restic`

## [Configuration]

### [Environment variables]

#### [Restic configuration]

-   `RESTIC_REPOSITORY_FILE` --- Name of file containing the repository location (replaces `--repository-file`)
-   `RESTIC_REPOSITORY` --- Location of repository (replaces `-r`)
-   `RESTIC_PASSWORD_FILE` --- Location of password file (replaces `--password-file`)
-   `RESTIC_PASSWORD` --- The actual password for the repository
-   `RESTIC_PASSWORD_COMMAND` --- Command printing the password for the repository to stdout
-   `RESTIC_KEY_HINT` --- ID of key to try decrypting first, before other keys
-   `RESTIC_CACHE_DIR` --- Location of the cache directory
-   `RESTIC_COMPRESSION` --- Compression mode (only available for repository format version 2)
-   `RESTIC_PROGRESS_FPS` --- Frames per second by which the progress bar is updated
-   `RESTIC_PACK_SIZE` --- Target size for pack files
-   `RESTIC_READ_CONCURRENCY` --- Concurrency for file reads
-   `TMPDIR` --- Location for temporary files

#### [Amazon Web Services integration]

-   `AWS_ACCESS_KEY_ID` --- Amazon S3 access key ID
-   `AWS_SECRET_ACCESS_KEY` --- Amazon S3 secret access key
-   `AWS_SESSION_TOKEN` --- Amazon S3 temporary session token
-   `AWS_DEFAULT_REGION` --- Amazon S3 default region
-   `AWS_PROFILE` --- Amazon credentials profile (alternative to specifying key and region)
-   `AWS_SHARED_CREDENTIALS_FILE` --- Location of the AWS CLI shared credentials file (default: [\~/.aws/credentials])

#### [OpenStack integration]

-   `ST_AUTH` --- Auth URL for keystone v1 authentication
-   `ST_USER` --- Username for keystone v1 authentication
-   `ST_KEY` --- Password for keystone v1 authentication
-   `OS_AUTH_URL` --- Auth URL for keystone authentication
-   `OS_REGION_NAME` --- Region name for keystone authentication
-   `OS_USERNAME` --- Username for keystone authentication
-   `OS_USER_ID` --- User ID for keystone v3 authentication
-   `OS_PASSWORD` --- Password for keystone authentication
-   `OS_TENANT_ID` --- Tenant ID for keystone v2 authentication
-   `OS_TENANT_NAME` --- Tenant name for keystone v2 authentication
-   `OS_USER_DOMAIN_NAME` --- User domain name for keystone authentication
-   `OS_USER_DOMAIN_ID` --- User domain ID for keystone v3 authentication
-   `OS_PROJECT_NAME` --- Project name for keystone authentication
-   `OS_PROJECT_DOMAIN_NAME — ` Project domain name for keystone authentication
-   `OS_PROJECT_DOMAIN_ID` --- Project domain ID for keystone v3 authentication
-   `OS_TRUST_ID` --- Trust ID for keystone v3 authentication
-   `OS_APPLICATION_CREDENTIAL_ID` --- Application Credential ID (keystone v3)
-   `OS_APPLICATION_CREDENTIAL_NAME` --- Application Credential Name (keystone v3)
-   `OS_APPLICATION_CREDENTIAL_SECRET` --- Application Credential Secret (keystone v3)
-   `OS_STORAGE_URL` --- Storage URL for token authentication
-   `OS_AUTH_TOKEN` --- Auth token for token authentication

#### [Backblaze integration]

-   `B2_ACCOUNT_ID` --- Account ID or applicationKeyId for Backblaze B2
-   `B2_ACCOUNT_KEY` --- Account Key or applicationKey for Backblaze B2

#### [Microsoft Azure integration]

-   `AZURE_ACCOUNT_NAME` --- Account name for Azure
-   `AZURE_ACCOUNT_KEY` --- Account key for Azure
-   `AZURE_ACCOUNT_SAS` --- Shared access signatures (SAS) for Azure

#### [Google Cloud storage integration]

-   `GOOGLE_PROJECT_ID` --- Project ID for Google Cloud Storage
-   `GOOGLE_APPLICATION_CREDENTIALS` ---Application Credentials for Google Cloud Storage (e.g. [\$HOME/.config/gs-secret-restic-key.json])

#### [Vendor agnostic cloud storage integration]

-   `RCLONE_BWLIMIT` --- rclone bandwidth limit

## [Compatibility]

restic documents its compatibility [position](https://restic.net/#compatibility) as:

-   reserving the right to break compatibility before 1.0.0;
-   compatibility may break between major versions after 1.0.0 (so e.g. between 1.0.0 and 2.0.0)

restic has not yet reached 1.0.0. Previously, the compatibility docs didn\'t reference 1.0.0, but it was later [changed](https://github.com/restic/restic.net/pull/22) to carve out \<1.0.0 versions.

## [Usage]

### [Invocation]

`user `[`$`]`restic --help`

    restic is a backup program which allows saving multiple revisions of files and
    directories in an encrypted repository stored on different backends.

    Usage:
      restic [command]

    Available Commands:
      backup        Create a new backup of files and/or directories
      cache         Operate on local cache directories
      cat           Print internal objects to stdout
      check         Check the repository for errors
      copy          Copy snapshots from one repository to another
      diff          Show differences between two snapshots
      dump          Print a backed-up file to stdout
      find          Find a file, a directory or restic IDs
      forget        Remove snapshots from the repository
      generate      Generate manual pages and auto-completion files (bash, fish, zsh)
      help          Help about any command
      init          Initialize a new repository
      key           Manage keys (passwords)
      list          List objects in the repository
      ls            List files in a snapshot
      migrate       Apply migrations
      mount         Mount the repository
      prune         Remove unneeded data from the repository
      rebuild-index Build a new index
      recover       Recover data from the repository not referenced by snapshots
      restore       Extract the data from a snapshot
      self-update   Update the restic binary
      snapshots     List all snapshots
      stats         Scan the repository and show basic statistics
      tag           Modify tags on snapshots
      unlock        Remove locks other processes created
      version       Print version information

    Flags:
          --cacert file                file to load root certificates from (default: use system certificates)
          --cache-dir directory        set the cache directory. (default: use system default cache directory)
          --cleanup-cache              auto remove old cache directories
          --compression mode           compression mode (only available for repository format version 2), one of (auto|off|max) (default auto)
      -h, --help                       help for restic
          --insecure-tls               skip TLS certificate verification when connecting to the repository (insecure)
          --json                       set output mode to JSON for commands that support it
          --key-hint key               key ID of key to try decrypting first (default: $RESTIC_KEY_HINT)
          --limit-download int         limits downloads to a maximum rate in KiB/s. (default: unlimited)
          --limit-upload int           limits uploads to a maximum rate in KiB/s. (default: unlimited)
          --pack-size uint             set target pack size in MiB. (default: $RESTIC_PACK_SIZE)
          --no-cache                   do not use a local cache
          --no-lock                    do not lock the repository, this allows some operations on read-only repositories
      -o, --option key=value           set extended option (key=value, can be specified multiple times)
          --password-command command   shell command to obtain the repository password from (default: $RESTIC_PASSWORD_COMMAND)
      -p, --password-file file         file to read the repository password from (default: $RESTIC_PASSWORD_FILE)
      -q, --quiet                      do not output comprehensive progress report
      -r, --repo repository            repository to backup to or restore from (default: $RESTIC_REPOSITORY)
          --repository-file file       file to read the repository location from (default: $RESTIC_REPOSITORY_FILE)
          --tls-client-cert file       path to a file containing PEM encoded TLS client certificate and private key
      -v, --verbose n                  be verbose (specify multiple times or a level using --verbose=n, max level/times is 3)

    Use "restic [command] --help" for more information about a command.

### [Initializing a new local repository]

See the upstream documentation for [additional initialization options](https://restic.readthedocs.io/en/latest/030_preparing_a_new_repo.html). In short:

`user `[`$`]`restic init --repo /srv/restic-repo`

### [Back up to local storage]

See the upstream documentation for [additional backup options](https://restic.readthedocs.io/en/latest/040_backup.html). In short, to backup a directory named [\~/work] to local storage:

`user `[`$`]`restic -r /srv/restic-repo --verbose backup ~/work`

### [Restore from local storage]

See the upstream documentation for [additional restore options](https://restic.readthedocs.io/en/latest/050_restore.html). In short, to restore the latest snapshot a directory named [/home/work] to a target directory of [/tmp/restore-work]:

`user `[`$`]`restic -r /srv/restic-repo restore latest --target /tmp/restore-work --path "/home/work"`

## [Removal]

### [Unmerge]

`root `[`#`]`emerge --ask --depclean --verbose app-backups/restic`

## [See also]

-   [dd](https://wiki.gentoo.org/wiki/Dd "Dd") --- a utility used to copy raw data from a source into sink, where source and sink can be a block device, file, or piped input/output.
-   [rsnapshot](https://wiki.gentoo.org/wiki/Rsnapshot "Rsnapshot") --- an automated [backup](https://wiki.gentoo.org/wiki/Backup "Backup") tool based on the [rsync](https://en.wikipedia.org/wiki/Rsync "wikipedia:Rsync") protocol and written in Perl.