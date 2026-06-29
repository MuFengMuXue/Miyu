This guide describes managing [AWS](https://en.wikipedia.org/wiki/Amazon_Web_Services "wikipedia:Amazon Web Services") keys in [MariaDB](https://wiki.gentoo.org/wiki/MariaDB "MariaDB").

## Contents

-   [[1] [Important]](#Important)
-   [[2] [The Challenges]](#The_Challenges)
    -   [[2.1] [awscli v2 source build]](#awscli_v2_source_build)
    -   [[2.2] [AWS default SDK paths]](#AWS_default_SDK_paths)
-   [[3] [Installation]](#Installation)
-   [[4] [Configuration]](#Configuration)
    -   [[4.1] [AWS SDK]](#AWS_SDK)
    -   [[4.2] [MariaDB]](#MariaDB)
        -   [[4.2.1] [OpenRC]](#OpenRC)
        -   [[4.2.2] [systemd]](#systemd)
        -   [[4.2.3] [Enabling AWS support in MariaDB]](#Enabling_AWS_support_in_MariaDB)
        -   [[4.2.4] [Encrypting MariaDB]](#Encrypting_MariaDB)
-   [[5] [Security considerations]](#Security_considerations)
    -   [[5.1] [MariaDB encryption requirements]](#MariaDB_encryption_requirements)
    -   [[5.2] [Encryption at rest]](#Encryption_at_rest)
    -   [[5.3] [Protecting \.../.aws/]](#Protecting_....2F.aws.2F)
-   [[6] [IAM User Permissions]](#IAM_User_Permissions)

# [Important]

Much of what is described here should be considered a hack. It is not neat. It is not pretty. And improving it (though it would be appreciated) is a rabbit hole you likely do not want to descend into.

** Warning**\
There are no guarantees on the security of the MariaDB encryption described. For 100% confidence the trust also rests on the protections of AWS SSO, or on the system being properly secured from physical or electronic access for example via [rootfs encryption](https://wiki.gentoo.org/wiki/Rootfs_encryption "Rootfs encryption").

# [The Challenges]

## [awscli v2 source build]

As of right now, it seems packaging awscli:2 is challenging. Instead the recommendation is to use the v2 binary package.

** Note**\
Help on figuring out the recursive dependencies of awscli:2 would be appreciated. Confirmation that the instructions work on awscli v1 would also be helpful.

## [AWS default SDK paths]

By default the AWS SDK loads configuration and SSO information from [\~/.aws/]. Unfortunately, the home directory of the mysql user is [/dev/null]. For unknown reasons, this makes the AWS SDK use [/.aws/]. If mariadb was started from a root-shell, it can also end up using [/root/.aws/] due to inheritance of the environment.

# [Installation]

Install [[[dev-db/mariadb]](https://packages.gentoo.org/packages/dev-db/mariadb)[]] with flag `aws-km` (available from version 11.4.8-r2), and [[[app-admin/awscli-bin]](https://packages.gentoo.org/packages/app-admin/awscli-bin)[]] which likely needs to be unmasked with **[\~amd64]**.

`root `[`#`]`emerge --ask mariadb awscli-bin`

# [Configuration]

## [AWS SDK]

SSO credentials have to be created in AWS. For this, follow the [instructions from the MariaDB docs](https://mariadb.com/docs/server/security/securing-mariadb/encryption/data-at-rest-encryption/key-management-and-encryption-plugins/aws-key-management-encryption-plugin#preparation).

You should obtain 4 pieces of information:

1.  [Access Key ID]
2.  [Secret Access Key]
3.  [Region]
4.  [Key ID] or [Key Alias] (Alias is recommended).

\
Now follow [AWS\'s Quick Start guide](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-quickstart.html) section *long-term credentials* which states to enter the 4 values into:

`user `[`$`]` awscli configure`

## [MariaDB]

To make the AWS credentials accessible to MariaDB, and since MariaDB has no home directory, a directory needs to be selected. [/etc/mysql] seems as good as any.

After creation with `awscli`, the files and credentials are stored in [\~/.aws] of the user that ran the command.

`root `[`#`]`cp -a /home/<user>/.aws /etc/mysql/ `

`root `[`#`]`chown -R mysql: /etc/mysql/.aws `

### [OpenRC]

On [OpenRC](https://wiki.gentoo.org/wiki/OpenRC "OpenRC"), we overwrite the `HOME` environment variable manually in the mariadb service by editing /etc/conf.d/mysql and adding:

[FILE] **`/etc/conf.d/mysql`set home in openrc service**

    export HOME="$(dirname "$")"

The dir [/etc/mysql] that [/etc/mysql/my.cnf] (the value of `MY_CNF`) resides in can also be hardcoded:

[FILE] **`/etc/conf.d/mysql`set home to confdir**

    export HOME=/etc/mysql

### [systemd]

On [systemd](https://wiki.gentoo.org/wiki/Systemd "Systemd"), run

`root `[`#`]`systemctl edit mariadb.service`

and input

[FILE] **`/etc/systemd/system/mariadb.service.d/override.conf`set home in systemd service**

    [Service]
    Environment="HOME=/etc/mysql"

### [Enabling AWS support in MariaDB]

From here we follow [the instructions from the MariaDB docs](https://mariadb.com/docs/server/security/securing-mariadb/encryption/data-at-rest-encryption/key-management-and-encryption-plugins/aws-key-management-encryption-plugin#configuring-the-aws-key-management-plugin). A minimal configuration whilst still getting sensible logs to troubleshoot is:

[FILE] **`/etc/mysql/mariadb.d/90-aws-keys.cnf`**

    [mariadb]
    plugin_load_add = aws_key_management
    aws_key_management_master_key_id = alias/<key alias>
    aws_key_management_log_level = info
    aws_key_management_region = af-south-1

Once MariaDB starts successfully, run `show variables like '%aws%';` to confirm the plugin is operational. I that state the output will appear incomplete:

`MariaDB [(none)]>``show variables like '%aws%';`

    +------------------------------------+--------------------------+
    | Variable_name                      | Value                    |
    +------------------------------------+--------------------------+
    | aws_key_management_endpoint_url    |                          |
    | aws_key_management_key_spec        | AES_128                  |
    | aws_key_management_keyfile_dir     |                          |
    | aws_key_management_log_level       | Info                     |
    | aws_key_management_master_key_id   | alias/<go for it>        |
    | aws_key_management_region          | af-south-1               |
    | aws_key_management_request_timeout | 0                        |
    | aws_key_management_rotate_key      | 0                        |
    +------------------------------------+--------------------------+
    8 rows in set (0.001 sec)

** Note**\
[jkroon](https://wiki.gentoo.org/index.php?title=User:Jkroon&action=edit&redlink=1 "User:Jkroon (page does not exist)") ([talk](https://wiki.gentoo.org/index.php?title=User_talk:Jkroon&action=edit&redlink=1 "User talk:Jkroon (page does not exist)")): This has to be revisited once my own setup is operational.

### [Encrypting MariaDB]

Database binlogs (writing out recent database actions in case of unexpected shutdown) can now be encrypted:

[FILE] **`/etc/mysql/mariadb.d/99-binlog-encryption.cnf`**

    [mariadb]
    encrypt_binlog = 1

Relevant tables have to be encrypted individually by setting `encrypted=yes`, depending on whether it\'s a new or existing table one of the following should do the trick:

`MariaDB [(none)]>``CREATE TABLE foo(bar int) ENCRYPTED=YES;`

`MariaDB [(none)]>``ALTER TABLE foo ENCRYPTED=YES;`

** Note**\
There are a few engine specific variables that can be tweaked, which have not been investigated yet. Feel free to research and experiment yourself (and to share your findings).

# [Security considerations]

## [MariaDB encryption requirements]

A simple test using [grep] found that MariaDB data can be written to up to three places in [/var/lib/mysql]:

1.  [ib_logfile0]
2.  [mysqld-bin.??????] (eg. [mysqld-bin.000001], [mysqld-bin.000002], \...)
3.  [\<db\>/\<table\>.ibd]

Basically the binlog, then the innodb logfile to which pages is written first, and finally to the table `ibd` itself (or `ibdata` if you\'re still not using file per table).

It\'s recommended that you perform a test similar to this to ensure that your encryption is working properly:

`MariaDB [test]>``|create table crypt_test (val varchar(1024)) ENCRYPTED=YES;`\

Query OK, 0 rows affected (0.192 sec)\
\
\|insert into crypt_test values(\'CRYPT TEST PLAINTEXT 01\');\
Query OK, 1 row affected (0.031 sec)\
\
\|flush tables crypt_test for export;\

Query OK, 0 rows affected (0.055 sec)

Which should not show up on your filesystem as:

`root `[`#`]` grep -r 'CRYPT TEST PLAINTEXT 01' /var/lib/mysql `

    grep: ib_logfile0: binary file matches
    grep: mysqld-bin.001752: binary file matches
    grep: test/crypt_test.ibd: binary file matches

For repeat tests, change the string. Upon correct configuration, [grep] should not return any matches.

## [Encryption at rest]

Encryption at rest intends to protect against physical theft, or against your VM provider being a bad actor/compromised themselves. Nothing more. Nothing less.

I would recommend rather looking at full disk encryption using LUKS with a TPM2.0 based unlock if possible. If you don\'t have access to a functional TPM2.0 setup \... you\'re probably at the mercy of a password during boot, or only encrypting part of your disk which can be done via ssh post boot. You will somehow (especially in the case of a VM) verify the legitimacy of the boot image and non-encrypted parts of the operating system. Both of those have surety issues that your boot path has not been compromised (and I\'ve personally seen cases where even with changes to the BIOS the TPM will still consider the boot path as valid, and thus unlock and provide keys).

## [][Protecting \.../.aws/]

The credentials in [\.../.aws/] are long-term. This means that should an attacker lay hands on them - it\'s game over. This can be done if this itself isn\'t encrypted, and if it is, those keys has to be well protected - which brings us back to TPM.

Either way: It\'s important to revoke access to the AWS user that\'s used by mariadb the moment you become aware of theft or compromise of these.

# [IAM User Permissions]

The IAM user should also have various rights, which I\'m unclear on, but you\'ll get errors in the mariadb log files if this isn\'t set up, eg:

    WARN] 2025-11-13 12:21:28.880 AWSErrorMarshaller [139631421925376] Encountered AWSError 'AccessDeniedException': User: arn:aws:iam::123456:user/mariadb-kms-user is not authorized to perform: kms:GenerateDataKeyWithoutPlaintext on resource: arn:aws:kms:af-south-1:329992286798:key/b145837b-bcbe-47f0-9d64-d6ed83641bfb because no identity-based policy allows the kms:GenerateDataKeyWithoutPlaintext action
    [ERROR] 2025-11-13 12:21:28.880 AWSJsonClient [139631421925376] HTTP response code: 400
    Resolved remote host IP address: 13.246.244.67
    Request ID:
    Exception name: AccessDeniedException
    Error message: User: arn:aws:iam::123456:user/mariadb-kms-user is not authorized to perform: kms:GenerateDataKeyWithoutPlaintext on resource: arn:aws:kms:af-south-1:123456:key/ because no identity-based policy allows the kms:GenerateDataKeyWithoutPlaintext action

You will unfortunately have to dig through those, what I know about AWS is extremely dangerous, I just pass these errors on to the people that manage the account and have them sort it out.