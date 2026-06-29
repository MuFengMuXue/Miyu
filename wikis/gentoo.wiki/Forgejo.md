[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Forgejo&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://forgejo.org/)

[![Codeberg Logo](/images/thumb/c/cc/Codeberg-logo.png/30px-Codeberg-logo.png)][Codeberg](https://codeberg.org/forgejo/forgejo)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Forgejo "wikipedia:Forgejo")

**Forgejo** is a fork of [Gitea](https://wiki.gentoo.org/wiki/Gitea "Gitea").

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Official binaries]](#Official_binaries)
        -   [[1.1.1] [Forgejo]](#Forgejo)
        -   [[1.1.2] [Forgejo Actions (self-hosted)]](#Forgejo_Actions_.28self-hosted.29)
-   [[2] [SELinux policy]](#SELinux_policy)
    -   [[2.1] [Current state]](#Current_state)
    -   [[2.2] [Reproducible environment]](#Reproducible_environment)
    -   [[2.3] [Forgejo\'s policy]](#Forgejo.27s_policy)
    -   [[2.4] [Forgejo runner\'s policy]](#Forgejo_runner.27s_policy)
    -   [[2.5] [Installation of policies]](#Installation_of_policies)
    -   [[2.6] [Removal of policies]](#Removal_of_policies)
    -   [[2.7] [Usage of policies]](#Usage_of_policies)
-   [[3] [See also]](#See_also)

## [Installation]

As of 2024-09-18, Forgejo is not provided as a Gentoo package, but is available in the [GURU](https://wiki.gentoo.org/wiki/Project:GURU "Project:GURU") overlay. Alternatively, Forgejo is distributed as a single binary file.

### [Official binaries]

#### [Forgejo]

The Forgejo project distributes binaries for AMD64 and ARM64 architectures, which can be downloaded [here](https://codeberg.org/forgejo/forgejo/releases). The binaries are compatible with musl-based systems.

To download and verify the binary file, follow the instructions provided [here](https://forgejo.org/download/).

** Note**\
In case [GnuPG](https://wiki.gentoo.org/wiki/GnuPG "GnuPG") fails to retrieve the key, the key can be imported manually:

`user `[`$`]`wget -O - `[`https://keys.openpgp.org/vks/v1/by-fingerprint/EB114F5E6C0DC2BCDD183550A4B61A2DC5923710`](https://keys.openpgp.org/vks/v1/by-fingerprint/EB114F5E6C0DC2BCDD183550A4B61A2DC5923710)` | gpg --import`

The binary does not require root privileges to run and can be launched from any directory:

`user `[`$`]`./forgejo-*-linux-arm64`

If there is a plan to install the binary into the system, follow the steps provided [here](https://forgejo.org/docs/next/admin/installation-binary/).

#### [][Forgejo Actions (self-hosted)]

** Warning**\
This section describes a way to run Actions on bare hardware, without virtualization or containers. This means that everything that is uploaded to the repository will run on the same system that the server is running on. This can lead to any number of consequences (data loss, hardware damage, etc.). Only persons with the ultimate level of trust should be able to push data to repositories.

The runner can be downloaded from [here](https://code.forgejo.org/forgejo/runner/releases).

Once downloaded, create and copy the token via GUI as described [here](https://forgejo.org/docs/next/admin/actions/#registration).

Register the runner:

`user `[`$`]`./forgejo-runner-* register --no-interactive --token <OBTAINED TOKEN> --name self-hosted --instance `[`http://[::1]:3001/`](http://%5B::1%5D:3001/)

** Note**\
[`http://[::1]:3001/`](http://%5B::1%5D:3001/) is Forgejo\'s address.

Once registered, create the minimal configuration file:

[FILE] **`config.yml`**

    log:
      level: info

    runner:
      timeout: 1h
      labels:
        - self-hosted

    cache:
      enabled: false

And launch the runner as a daemon:

`user `[`$`]`./forgejo-runner-* --config config.yml daemon`

To test that everything works, push the following file to the repository:

[FILE] **`.forgejo/workflows/demo.yaml`**

    on: [push]
    jobs:
      test:
        runs-on: self-hosted
        steps:
          - run: echo Works

## [SELinux policy]

** Warning**\
As of 2024-12-08, there are no official [SELinux](https://wiki.gentoo.org/wiki/SELinux "SELinux") policies for Forgejo. The policies on this page are written by regular Gentoo Linux users and are provided \"as is\" without warranty of any kind. Any contribution is welcome.

### [Current state]

The policies are not ready to be used in production.

Almost every action produces a significant number of cosmetic AVC log messages, resulting in a fast-growing [/var/log/audit/audit.log] file that can lead to a denial of service if [/var] is not mounted as a separate partition.

### [Reproducible environment]

** Note**\
All tests were performed using official binaries downloaded directly from the Forgejo website.

Once the policies are installed and Forgejo is running, the following features must be configured in the initial setup window:

-   Database type: SQLite3
-   Git LFS root path: leave empty to disable
-   SSH server port: leave empty to disable (almost everything can be done through the REST API)
-   Enable OpenID sign-in: disable
-   Password hash algorithm: pbkdf2_hi (the default value)

\
The policies were tested in the following profiles:

  ------------------------------------------------ -------- -------------------- --------------------------- -------
  Profile name                                     Status   Forgejo\'s version   Forgejo runner\'s version   Notes
  default/linux/arm64/23.0/musl/hardened/selinux   Works    9.0.2                5.0.3
  ------------------------------------------------ -------- -------------------- --------------------------- -------

### [][Forgejo\'s policy]

[FILE] **`forgejo.te`**

    # License: 0BSD

    policy_module(forgejo, 1.0)

    gen_require(`
      attribute file_type, non_security_file_type, non_auth_file_type;
      role user_r;
      type user_t;
      type user_devpts_t;
      type sshd_t;
      type bin_t;
      type node_t;
      type ntop_port_t;
      type git_exec_t;
      type urandom_device_t;
      type shell_exec_t;
      type home_root_t;
      type ssh_exec_t;
      type user_home_dir_t;
      type ssh_home_t;
      type net_conf_t;
      type tmp_t;
    ')

    ##
    # Type declarations.
    #
      type forgejo_t;
      type forgejo_exec_t;
      type forgejo_config_t;
      type forgejo_www_t;
      domain_type(forgejo_t)
      domain_entry_file(forgejo_t, forgejo_exec_t)
      typeattribute forgejo_config_t file_type, non_security_file_type, non_auth_file_type;
      typeattribute forgejo_www_t file_type, non_security_file_type, non_auth_file_type;

    ##
    # Domain transition (user_t -> forgejo_t).
    #
      domtrans_pattern(user_t, forgejo_exec_t, forgejo_t)
      role user_r types forgejo_t;
      # Allow to run the binary file of Forgejo.
      allow user_t forgejo_exec_t:file mmap_exec_file_perms;

    ##
    # Data files.
    #
      allow forgejo_t forgejo_www_t:file ;
      allow forgejo_t forgejo_www_t:lnk_file ;
      allow forgejo_t forgejo_www_t:dir manage_dir_perms;
      allow user_t forgejo_www_t:dir list_dir_perms;

      # Self-utilization
      allow forgejo_t forgejo_exec_t:file execute_no_trans;

    ##
    # Forgejo requirements (external).
    #
      allow forgejo_t self:fifo_file ;
      allow forgejo_t self:process ;

      # External tools
        allow forgejo_t bin_t:dir search;
        allow forgejo_t bin_t:file ;
        allow forgejo_t bin_t:lnk_file read;

      # PTY
        # FIXME: Optional?
          allow forgejo_t sshd_t:fd use;
        allow forgejo_t user_devpts_t:chr_file ;

      # TCP
        allow forgejo_t self:tcp_socket ;
        allow forgejo_t node_t:tcp_socket node_bind;
        allow forgejo_t ntop_port_t:tcp_socket ;

      # Git
        allow forgejo_t git_exec_t:file ;

      # Password creation (admin user creation)
        allow forgejo_t urandom_device_t:chr_file ;

      # Shell
        allow forgejo_t shell_exec_t:file ;

      # SSH keys (always required)
        allow forgejo_t home_root_t:dir ;
        allow forgejo_t user_home_dir_t:dir ;
        allow forgejo_t ssh_exec_t:file ;
        allow forgejo_t ssh_home_t:dir ;
        allow forgejo_t ssh_home_t:file ;

      # Repo administration
        allow forgejo_t net_conf_t:file ;
        allow forgejo_t tmp_t:dir ;
        allow forgejo_t tmp_t:file ;
        allow forgejo_t tmp_t:lnk_file ;

[FILE] **`forgejo.fc`**

    /opt/forgejo(/.*)?  gen_context(system_u:object_r:forgejo_www_t)
    /opt/forgejo/forgejo  gen_context(system_u:object_r:forgejo_exec_t)

### [][Forgejo runner\'s policy]

[FILE] **`forgejo-runner.te`**

    # License: 0BSD

    policy_module(forgejo-runner, 1.0)

    gen_require(`
      attribute file_type, non_security_file_type, non_auth_file_type;
      role user_r;
      type user_t;
      type sshd_t;
      type user_devpts_t;
      type ntop_port_t;
      type home_root_t;
      type user_home_dir_t;
      type xdg_cache_t;
      type xdg_config_t;
      type bin_t;
      type shell_exec_t;
      type git_exec_t;
      type urandom_device_t;
    ')

    ##
    # Type declarations.
    #
      type forgejo_runner_t;
      type forgejo_runner_exec_t;
      type forgejo_runner_data_t;
      domain_type(forgejo_runner_t)
      domain_entry_file(forgejo_runner_t, forgejo_runner_exec_t)
      typeattribute forgejo_runner_data_t file_type, non_security_file_type, non_auth_file_type;

    ##
    # Domain transition (user_t -> forgejo_runner_t).
    #
      domtrans_pattern(user_t, forgejo_runner_exec_t, forgejo_runner_t)
      role user_r types forgejo_runner_t;

    ##
    # Data files.
    #
      allow forgejo_runner_t forgejo_runner_data_t:file ;
      allow forgejo_runner_t forgejo_runner_data_t:dir manage_dir_perms;
      allow user_t forgejo_runner_data_t:dir list_dir_perms;
      allow user_t forgejo_runner_exec_t:file mmap_exec_file_perms;

    ##
    # Requirements (external)
    #
      allow forgejo_runner_t self:fifo_file ;
      allow forgejo_runner_t self:process ;

      # PTY
        allow forgejo_runner_t user_devpts_t:chr_file ;
        # FIXME: Optional?
          allow forgejo_runner_t sshd_t:fd use;

      # TCP
        allow forgejo_runner_t self:tcp_socket ;
        allow forgejo_runner_t ntop_port_t:tcp_socket name_connect;

      allow forgejo_runner_t home_root_t:dir ;
      allow forgejo_runner_t user_home_dir_t:dir ;

      allow forgejo_runner_t xdg_cache_t:dir ;
      allow forgejo_runner_t xdg_cache_t:file ;
      allow forgejo_runner_t xdg_cache_t:lnk_file ;
      allow forgejo_runner_t xdg_config_t:dir search;

      allow forgejo_runner_t bin_t:dir search;
      allow forgejo_runner_t bin_t:file ;
      allow forgejo_runner_t bin_t:lnk_file ;
      allow forgejo_runner_t shell_exec_t:file ;

      # Git
        allow forgejo_runner_t git_exec_t:file ;
        allow forgejo_runner_t urandom_device_t:chr_file ;

[FILE] **`forgejo-runner.fc`**

    /opt/forgejo-runner(/.*)?  gen_context(system_u:object_r:forgejo_runner_data_t)
    /opt/forgejo-runner/forgejo-runner  gen_context(system_u:object_r:forgejo_runner_exec_t)

### [Installation of policies]

All [.te] and [.fc] files defined above should be in the same directory (forgejo and forgejo-runner can be separated if desired).

`root `[`#`]`make -f /usr/share/selinux/strict/include/Makefile`

`root `[`#`]`semodule --install forgejo*.pp`

`root `[`#`]`restorecon -R /opt/forgejo`

`root `[`#`]`restorecon -R /opt/forgejo-runner`

### [Removal of policies]

`root `[`#`]`semodule --remove forgejo`

`root `[`#`]`semodule --remove forgejo-runner`

`root `[`#`]`restorecon -R /opt/forgejo`

`root `[`#`]`restorecon -R /opt/forgejo-runner`

### [Usage of policies]

The [forgejo.fc] file requires the [forgejo] binary file to be placed in the [/opt/forgejo] directory.

The [forgejo-runner.fc] file requires the [forgejo-runner] binary file to be placed in the [/opt/forgejo-runner] directory.

The execution must be performed as regular users in the mentioned above directories.

The paths can be modified as desired in the appropriate [.fc] file.

## [See also]

-   [Node.js as a reverse proxy for Forgejo](https://wiki.gentoo.org/wiki/Node.js#Node.js_as_a_reverse_proxy_for_Forgejo.5CGitea_.28or_anything_else.29 "Node.js")
-   [Gitea](https://wiki.gentoo.org/wiki/Gitea "Gitea") --- painless self-hosted [git](https://wiki.gentoo.org/wiki/Git "Git") service, a fork of gogs