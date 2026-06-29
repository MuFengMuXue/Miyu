**翻译状态：**

  * 本文（或部分内容）译自 [JupyterHub](<https://wiki.archlinux.org/title/JupyterHub> "arch:JupyterHub")，最近一次同步于 2024-4-30，若英文版本有所[更改](<https://wiki.archlinux.org/title/JupyterHub?diff=0&oldid=807130>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/JupyterHub_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[![](../File:Tango-preferences-desktop-locale.png)](<../File:Tango-preferences-desktop-locale.png>)**本文或本节需要[翻译](<../Project:Contributing_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\).html#%E7%BF%BB%E8%AF%91> "Project:Contributing \(简体中文\)")。要贡献翻译，请访问[简体中文翻译团队](<../Project:%E7%BF%BB%E8%AF%91%E5%9B%A2%E9%98%9F.html> "Project:翻译团队")。**

**附注：** 需要翻译。（在 [Talk:JupyterHub#](<../zh-cn/Talk:JupyterHub.html>) 中讨论）

[JupyterHub](<https://jupyterhub.readthedocs.io/>) 是用于 [Jupyter](<../zh-cn/Jupyter.html> "Jupyter") 笔记本的多用户 Web 服务器。它由四个子系统组成： 

  1. 主集线器（hub）进程。
  2. 对用户进行身份验证的[身份验证器](<#Authenticators>)。
  3. [生成器](<#Spawners>)可为每个已连接的用户启动并监控单用户服务器。
  4. 一个 HTTP 代理，用于接收传入请求并将其路由到集线器或相应的单用户服务器。

有关详细信息，请参阅 JupyterHub 文档中的[技术概述](<https://jupyterhub.readthedocs.io/en/stable/reference/technical-overview.html>)。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [jupyterhub](<https://aur.archlinux.org/packages/jupyterhub/>)AUR 软件包。 在大多数情况下，您还需要安装 [jupyter-notebook](<https://archlinux.org/packages/?name=jupyter-notebook>)包 包（一些更高级的[生成器](<#Spawners>)可能不需要它）。还可以安装 [jupyterlab](<https://archlinux.org/packages/?name=jupyterlab>)包 软件包以使 [JupyterLab](<https://jupyterlab.readthedocs.io/>) 接口可用。 

##  运行

[启动/启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动/启用") `jupyterhub.service` 。使用默认配置，您可以通过在浏览器中转到 127.0.0.1:8000 来访问集线器。 

##  配置

JupyterHub 配置文件位于 `/etc/jupyterhub/jupyterhub_config.py` 。这是一个修改配置对象 `c` 的 Python 脚本。软件包提供的配置文件显示可用的配置选项及其默认值。 

配置中的任何相对路径都是从运行集线器的工作目录开始解析的。软件包提供的 systemd 服务用 `/etc/jupyterhub` 作为工作目录。这意味着，例如，默认数据库 URL `c.JupyterHub.db_url = 'sqlite:///jupyterhub.sqlite'` 对应于文件 `/etc/jupyterhub/jupyterhub.sqlite` 。 

所有配置选项都可以在命令行中覆盖。例如，配置文件中的 `c.Application.show_config = True` 设置可以用命令行标志 `--Application.show_config=True` 代替。请注意，所提供的 systemd 服务会使用命令行将 `c.JupyterHub.pid_file` 和 `c.ConfigurableHTTPProxy.pid_file` 明确设置到合适的运行时目录，因此配置文件中的任何值都会被忽略。 

##  身份验证器

身份验证器控制对集线器和单用户服务器的访问。文档的[身份验证器部分](<https://jupyterhub.readthedocs.io/en/stable/reference/authenticators.html>)包含有关身份验证器如何工作以及如何编写自定义身份验证器的详细信息。[身份验证器 wiki 页面](<https://github.com/jupyterhub/jupyterhub/wiki/Authenticators>)包含身份验证器列表;其中一些是打包的，如下所述。 

请注意，用户状态存储在 cookie 中，由 [cookie 密钥加密](<https://jupyterhub.readthedocs.io/en/stable/tutorial/getting-started/security-basics.html#cookie-secret>)。如果切换到其他身份验证器，或修改所选身份验证器的设置，导致允许的用户列表可能发生变化，则应更改 Cookie 密钥。这将注销所有当前用户，并强制他们使用新设置重新进行身份验证。这可以通过删除 cookie 密钥文件并重新启动集线器来执行，该中心将自动生成新密钥。在默认配置中，cookie 密钥存储在 `/etc/jupyterhub/jupyterhub_cookie_secret`。 

###  PAM 身份验证器

PAM 身份验证器使用 [PAM](<../zh-cn/PAM.html> "PAM") 允许本地用户登录集线器。它包含在 JupyterHub 中，是默认的身份验证器。使用它要求集线器拥有 `/etc/shadow`（包含用户密码的散列版本）的读取权限，以便对用户进行身份验证。默认情况下，`/etc/shadow` 由 root 拥有，[文件权限](<../zh-cn/Users_and_groups.html#Permissions_and_ownership> "Users and groups")为 `-rw------`，因此以 root 身份运行集线器将满足这一要求。[一些资料](<https://fedoraproject.org/wiki/Features/LowerProcessCapabilities> "fedora:Features/LowerProcessCapabilities")主张删除 `/etc/shadow` 中的所有权限，使其无法被受损的守护进程读取，并授予需要访问的进程 `DAC_OVERRIDE` [功能](<../zh-cn/Capabilities.html> "Capabilities")。如果你的 `/etc/shadow` 是这样设置的，请为服务创建一个[插入文件](</wzh/index.php?title=%E6%8F%92%E5%85%A5%E6%96%87%E4%BB%B6&action=edit&redlink=1> "插入文件（页面不存在）")，将此功能授予 JupyterHub： 
    
    /etc/systemd/system/jupyterhub.service.d/override.conf
    
    [Service]
    CapabilityBoundingSet=CAP_DAC_OVERRIDE

The PAM authenticator relies on the Python package [pamela](<https://github.com/minrk/pamela>). For basic troubleshooting this can be tested on the commandline. To attempt authentication as user `testuser`, run the following command: 
    
    # python -m pamela -a testuser
    
(If you run JupyterHub as a non-root user, run the command as that user instead of root). If the authentication succeeds, no output will be printed. If it failed an error message will be printed. 

#### PAM authentication as non-root user

If you run JupyterHub as a non-root user, you will need to give that user read permissions to the shadow file. The [method recommended by the JupyterHub documentation](<https://jupyterhub.readthedocs.io/en/stable/reference/config-sudo.html#enable-pam-for-non-root>) is to create a `shadow` group, make the shadow file readable by this group, and add the JupyterHub user to this group. 

**警告：** This allows read-only access to the hashed passwords in `/etc/shadow` to anybody running code as the JupyterHub user. Note that each single-user server is run under their own account and so code executed in those servers will not have access. Also note that a security exploit in JupyterHub would allow the same access to the hashed passwords if JupyterHub was being run as root.

Creating the group, modifying the shadow file permissions and adding the user `jupyterhub` to the group can be accomplished with the following four commands: 
    
    # groupadd shadow
    # chgrp shadow /etc/shadow
    # chmod g+r /etc/shadow
    # usermod -aG shadow jupyterhub

## Spawners

Spawners are responsible for starting and monitoring each user's notebook server. The [spawners section of the documentation](<https://jupyterhub.readthedocs.io/en/stable/reference/spawners.html>) contains more details about how they work and how to write a custom spawner. The [spawners wiki page](<https://github.com/jupyterhub/jupyterhub/wiki/Spawners>) has a list of spawners; some of these are packaged and are described below. 

### LocalProcessSpawner

This is the default spawner included with JupyterHub. It runs each single-user server in a separate local process under their [user account](</wzh/index.php?title=User_account&action=edit&redlink=1> "User account（页面不存在）") (this means each JupyterHub user must correspond to a local user account). It also requires JupyterHub to be run as root so it can spawn the processes under the different user accounts. The [jupyter-notebook](<https://archlinux.org/packages/?name=jupyter-notebook>)包 package must be installed for this spawner to work. 

### SudoSpawner

The [SudoSpawner](<https://github.com/jupyterhub/sudospawner>) uses an intermediate process created with [sudo](<../zh-cn/Sudo.html> "Sudo") to spawn the single-user servers. This allows the JupyterHub process to be [run as a non-root user](<#Running_as_non-root_user>). To use it install the [jupyterhub-sudospawner](<https://aur.archlinux.org/packages/jupyterhub-sudospawner/>)AUR package. 

To use it, [create a system user account](<../zh-cn/Users_and_groups.html> "Users and groups") (the following assumes the account is named `jupyterhub`) and a group whose membership will define which users can access the hub (here assumed to be called `jupyterhub-users`). First, we have to configure sudo to allow the `jupyterhub` user to spawn a server without a password. Create a [drop-in sudo configuration file](<../zh-cn/Sudo.html#Configure_sudo_using_drop-in_files_in_/etc/sudoers.d> "Sudo") with [visudo](<../zh-cn/Sudo.html#%E4%BD%BF%E7%94%A8_visudo> "Visudo"): 
    
    # visudo -f /etc/sudoers.d/jupyterhub-sudospawner
    
    # The command the hub is allowed to run.
    Cmnd_Alias SUDOSPAWNER_CMD = /usr/bin/sudospawner
    
    # Allow the jupyterhub user to run this command on behalf of anybody
    # in the jupyterhub-users group.
    jupyterhub ALL=(%jupyterhub-users) NOPASSWD:SUDOSPAWNER_CMD

The default service file runs the hub as root. It also applies a number of hardening options to the service to restrict its capabilities. This hardening prevents sudo from working; to allow it, the `NoNewPrivileges` service option (plus any other options which implicitly set it, see [systemd.exec(5)](<https://man.archlinux.org/man/systemd.exec.5>) for a list of service options) needs to be off. Create a [drop-in file](<../zh-cn/Drop-in_file.html> "Drop-in file") to run the hub using the `jupyterhub` user instead: 
    
    /etc/systemd/system/jupyterhub.service.d/override.conf
    
    [Service]
    User=jupyterhub
    Group=jupyterhub
    
    # Required for sudo.
    NoNewPrivileges=false
    
    # Setting the following would implicitly set NoNewPrivileges.
    PrivateDevices=false
    ProtectKernelTunables=false
    ProtectKernelModules=false
    LockPersonality=false
    RestrictRealtime=false
    RestrictSUIDGID=false
    SystemCallFilter=
    SystemCallArchitectures=

If you have previously run the hub as the root user, you will need to [change the ownership](<../zh-cn/File_permissions_and_attributes.html#Changing_ownership> "File permissions and attributes") of the user database and [cookie secret](<https://jupyterhub.readthedocs.io/en/stable/tutorial/getting-started/security-basics.html#cookie-secret>) files: 
    
    # chown jupyterhub:jupyterhub /etc/jupyterhub/{jupyterhub_cookie_secret,jupyterhub.sqlite}
    
If you are using the PAMAuthenticator, you will need to [configure your system to allow it to work as a non-root user](<#PAM_authentication_as_non-root_user>). 

Finally, edit the JupyterHub configuration and change the spawner class to SudoSpawner: 
    
    /etc/jupyterhub/jupyterhub_config.py
    
    c.JupyterHub.spawner_class='sudospawner.SudoSpawner'

To give a user access to the hub, add them to the `jupyterhub-users` group: 
    
    # usermod -aG jupyterhub-users <username>
    
### systemdspawner

The [systemdspawner](<https://github.com/jupyterhub/systemdspawner>) uses [systemd](<../zh-cn/Systemd.html> "Systemd") to manage each user's notebook which allows configuring resource limitations, better process isolation and sandboxing, and dynamically allocated users. To use it install the [jupyterhub-systemdspawner](<https://aur.archlinux.org/packages/jupyterhub-systemdspawner/>)AUR package and set the spawner class in the configuration file: 
    
    /etc/jupyterhub/jupyterhub_config.py
    
    c.JupyterHub.spawner_class = 'systemdspawner.SystemdSpawner'

Note that as per [systemdspawner's readme](<https://github.com/jupyterhub/systemdspawner/blob/master/README.md#root-access>) using it currently requires JupyterHub to be run as root. 

## Services

A [JupyterHub service](<https://jupyterhub.readthedocs.io/en/stable/getting-started/services-basics.html>) is defined as a process which interacts with the Hub through its API. Services can either be run by the hub or as standalone processes. 

### Idle culler

The [idle culler](<https://github.com/jupyterhub/jupyterhub-idle-culler>) service can be used to automatically shut down idle single-user servers. To use it, install the [jupyterhub-idle-culler](<https://aur.archlinux.org/packages/jupyterhub-idle-culler/>)AUR package. To run the service through the hub, add a service description to the `c.JupyterHub.services` configuration variable: 
    
    /etc/jupyterhub/jupyterhub_config.py
    
    import sys
    c.JupyterHub.services = [
        {
            'name': 'idle-culler',
            'admin': True,
            'command': [
                sys.executable,
                '-m', 'jupyterhub_idle_culler',
                '--timeout=3600'
            ],
        }
    ]

See the service documentation or the output of `python -m jupyterhub_idle_culler --help` for a description of command-line options and details of how to run the service as a standalone process. 

##  提示与技巧

###  以非 root 用户身份运行

By default, the main hub process is run as the root user (the individual user servers are run under the corresponding local user as set by the spawner). To run as a non-root user, you need to use the [SudoSpawner](<#SudoSpawner>) (the other spawners listed above require running as root). If you are using the PAM authenticator, you will also need to [configure it for a non-root user](<#PAM_authentication_as_non-root_user>). 

###  使用反向代理

A reverse proxy can be used to redirect external requests to the JupyterHub instance. This can be useful if you want to serve multiple sites from one machine, or use an existing server to handle [SSL](</wzh/index.php?title=SSL&action=edit&redlink=1> "SSL（页面不存在）"). The [using a reverse proxy](<https://jupyterhub.readthedocs.io/en/stable/reference/config-proxy.html>) section of the JupyterHub documentation has example configuration for using either [nginx](<../zh-cn/Nginx.html> "Nginx") or [Apache](<../zh-cn/Apache_HTTP_Server.html> "Apache HTTP Server") as a reverse proxy. 

**注意：** This does not replace the proxy component of JupyterHub which is responsible for routing requests to either the main hub or the single-user servers. Rather, the reverse proxy passes external requests to the JupyterHub proxy.

### Proxy other web services

The Jupyter Server Proxy extension allows you to run other web services such as Code Server or RStudio alongside JupyterHub and provide authenticated web access to them. To use it, install [python-jupyter-server-proxy](<https://aur.archlinux.org/packages/python-jupyter-server-proxy/>)AUR and configure it with the `/etc/jupyter/jupyter_notebook_config.py` file. For instance, to proxy [code-server](<https://aur.archlinux.org/packages/code-server/>)AUR: 
    
    /etc/jupyter/jupyter_notebook_config.py
    
    c.ServerProxy.servers = {
      'code-server': {
        'command': [
          'code-server',
            '--auth=none',
            '--disable-telemetry',
            '--disable-update-check',
            '--bind-addr=localhost:{port}',
            '--user-data-dir=.config/Code - OSS/',
            '--extensions-dir=.vscode-oss/extensions/'
        ],
        'timeout': 20,
        'launcher_entry': {
          'title': 'VS Code'
        }
      }
    }

See the [documentation](<https://jupyter-server-proxy.readthedocs.io/en/latest/>) for more details about configuring the Jupyter Server Proxy. 

###  访问 GPU

If you receive errors when accessing GPUs (for instance, if `nvidia-smi` reports it cannot communicate with the NVIDIA driver), you must consider the hardening that is shipped with the JupyterHub [systemd unit file](<https://aur.archlinux.org/cgit/aur.git/tree/jupyterhub.service?h=jupyterhub>). To allow access to GPUs (and other hardware) broadly, you can add this to a [drop-in file](<../zh-cn/Drop-in_file.html> "Drop-in file"): 
    
    /etc/systemd/system/jupyterhub.service.d/override.conf
    
    [Service]
    PrivateDevices=false
