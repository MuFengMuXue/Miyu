# JupyterHub

JupyterHub is a multi-user web server for Jupyter notebooks. It consists of four subsystems:

# The main hub process.
# Authenticators which authenticate users.
# Spawners which start and monitor a single-user server for each connected user.
# An HTTP proxy which receives incoming requests and routes them to either the hub or the appropriate single-user server.

See the technical overview in the JupyterHub documentation for more details.

## Installation
Install the  package. In most cases you will also need to install the  package (some more advanced spawners may not require it). The  package can also be installed to make the JupyterLab interface available.

## Running
Start/enable . With the default configuration you can access the hub by going to 127.0.0.1:8000 in your browser.

## Configuration
The JupyterHub configuration file is located at . This is a Python script which modifies the configuration object . The configuration file provided by the package shows the available configuration options and their default values.

Any relative paths in the configuration are resolved from the working directory that the hub is run from. The systemd service provided by the package uses  as the working directory. This means, for example, that the default database URL  corresponds to the file .

All configuration options can be overridden on the command line. For example, the configuration file setting  could instead be set with the command line flag . Note that the provided systemd service uses the command line to explicitly set the  and  values to a suitable runtime directory so any values for them in the configuration file will be ignored.

## Authenticators
Authenticators control access to the hub and the single-user servers. The authenticators section of the documentation contains details about how authenticators work and how to write a custom authenticator. The authenticators wiki page has a list of authenticators; some of these are packaged and are described below.

Note that user status is stored in cookies, encrypted by the cookie secret. If you switch to a different authenticator, or modify the settings of your chosen authenticator so that the list of allowed users might change, you should change the cookie secret. This logs out all current users and forces them to re-authenticate with your new settings. This can be performed by deleting the cookie secret file and restarting the hub which will automatically generate a new secret. With the default configuration, the cookie secret is stored at .

## PAM authenticator
The PAM authenticator uses PAM to allow local users to log in to the hub. It is included with JupyterHub and is the default authenticator. Using it requires the hub to have read permissions to  (which contains hashed versions of user passwords) in order to authenticate users. By default  is owned by root and has file permissions of , so running the hub as root will meet this requirement. Some sources advocate removing all permissions from  so it cannot be read by compromised daemons, and granting processes which require access the  capability. If your  is set up like this, create a drop-in file for the service to grant this capability to JupyterHub:

The PAM authenticator relies on the Python package pamela. For basic troubleshooting this can be tested on the commandline. To attempt authentication as user , run the following command:

 # python -m pamela -a testuser

(If you run JupyterHub as a non-root user, run the command as that user instead of root). If the authentication succeeds, no output will be printed. If it failed an error message will be printed.

## PAM authentication as non-root user
If you run JupyterHub as a non-root user, you will need to give that user read permissions to the shadow file. The method recommended by the JupyterHub documentation is to create a  group, make the shadow file readable by this group, and add the JupyterHub user to this group.

Creating the group, modifying the shadow file permissions and adding the user  to the group can be accomplished with the following four commands:

## Spawners
Spawners are responsible for starting and monitoring each user's notebook server. The spawners section of the documentation contains more details about how they work and how to write a custom spawner. The spawners wiki page has a list of spawners; some of these are packaged and are described below.

## LocalProcessSpawner
This is the default spawner included with JupyterHub. It runs each single-user server in a separate local process under their user account (this means each JupyterHub user must correspond to a local user account). It also requires JupyterHub to be run as root so it can spawn the processes under the different user accounts. The  package must be installed for this spawner to work.

## SudoSpawner
The SudoSpawner uses an intermediate process created with sudo to spawn the single-user servers. This allows the JupyterHub process to be run as a non-root user. To use it install the  package.

To use it, create a system user account (the following assumes the account is named ) and a group whose membership will define which users can access the hub (here assumed to be called ). First, we have to configure sudo to allow the  user to spawn a server without a password. Create a drop-in sudo configuration file with visudo:

The default service file runs the hub as root. It also applies a number of hardening options to the service to restrict its capabilities. This hardening prevents sudo from working; to allow it, the  service option (plus any other options which implicitly set it, see  for a list of service options) needs to be off. Create a drop-in file to run the hub using the  user instead:

If you have previously run the hub as the root user, you will need to change the ownership of the user database and cookie secret files:

 # chown jupyterhub:jupyterhub /etc/jupyterhub/{jupyterhub_cookie_secret,jupyterhub.sqlite}

If you are using the PAMAuthenticator, you will need to configure your system to allow it to work as a non-root user.

Finally, edit the JupyterHub configuration and change the spawner class to SudoSpawner:

To give a user access to the hub, add them to the  group:

 # usermod -aG jupyterhub-users

## systemdspawner
The systemdspawner uses systemd to manage each user's notebook which allows configuring resource limitations, better process isolation and sandboxing, and dynamically allocated users. To use it install the  package and set the spawner class in the configuration file:

Note that as per systemdspawner's readme using it currently requires JupyterHub to be run as root.

## Services
A JupyterHub service is defined as a process which interacts with the Hub through its API. Services can either be run by the hub or as standalone processes.

## Idle culler
The idle culler service can be used to automatically shut down idle single-user servers. To use it, install the  package. To run the service through the hub, add a service description to the  configuration variable:

{{hc|1=/etc/jupyterhub/jupyterhub_config.py|2=
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
}}

See the service documentation or the output of  for a description of command-line options and details of how to run the service as a standalone process.

## Tips and tricks
## Running as non-root user
By default, the main hub process is run as the root user (the individual user servers are run under the corresponding local user as set by the spawner). To run as a non-root user, you need to use the SudoSpawner (the other spawners listed above require running as root). If you are using the PAM authenticator, you will also need to configure it for a non-root user.

## Using a reverse proxy
A reverse proxy can be used to redirect external requests to the JupyterHub instance. This can be useful if you want to serve multiple sites from one machine, or use an existing server to handle SSL. The using a reverse proxy section of the JupyterHub documentation has example configuration for using either nginx or Apache as a reverse proxy.

## Proxy other web services
The Jupyter Server Proxy extension allows you to run other web services such as Code Server or RStudio alongside JupyterHub and provide authenticated web access to them. To use it, install  and configure it with the  file. For instance, to proxy :

{{hc|1=/etc/jupyter/jupyter_notebook_config.py|2=
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
}}

See the documentation for more details about configuring the Jupyter Server Proxy.

## Access to GPUs
If you receive errors when accessing GPUs (for instance, if  reports it cannot communicate with the NVIDIA driver), you must consider the hardening that is shipped with the JupyterHub systemd unit file.
To allow access to GPUs (and other hardware) broadly, you can add this to a drop-in file:
