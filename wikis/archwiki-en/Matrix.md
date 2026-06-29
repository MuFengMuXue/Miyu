# Matrix

Matrix is an ambitious new ecosystem for open federated instant messaging and VoIP. It consists of servers, clients and bridge software to connect to existing messaging solutions like IRC.

A Matrix space for Arch Linux exists at #public-space:archlinux.org. Please contact any existing member or   @heftig:archlinux.org for an invite. Some international communities have their own matrix rooms; see International communities for details.

For clients, see List of applications/Internet#Matrix clients.

You can either use an existing homeserver like https://matrix.org or host your own homeserver. The process for setting up a widely used homeserver can be found below.

## Installation
The reference server implementation Synapse is available as , which creates a synapse user.

## Configuration
After installation, a configuration file needs to be generated. It should be readable by the synapse user:

 # generate_log_config -o /etc/synapse/my.domain.name.log.config \
                       -f /var/log/synapse/homeserver.log

 # generate_signing_key --output_file /etc/synapse/my.domain.name.signing.key

 # chown -R synapse:synapse /etc/synapse /var/log/synapse

Note that this will generate corresponding SSL keys and self-signed certificates for the specified server name. You have to regenerate those if you change the server name.

## Databases
Synapse uses SQLite only to test the server, Postgres is used for operation.

To use Postgres you will need to install the  package.

## Service
The  systemd service is included in the  package. It will start the synapse server as user synapse and use the configuration file .

## User management
You need at least one user on your fresh synapse server. You may create one as your normal non-root user with the command

 register_new_matrix_user -c /etc/synapse/homeserver.yaml http://127.0.0.1:8008

or using one of the [https://matrix.org/ecosystem/clients/ matrix clients, for example , or the  plug-in for .

## Spider webcrawler
To enable the webcrawler, for server generated link previews, the additional packages  and  have to be installed. After that, the option  can be set in your . To prevent the synapse server from issuing arbitrary GET requests to internal hosts, the  has to be set.

There are some examples that can be uncommented. Add your local IP ranges to that list to prevent the synapse server from trying to crawl them. After changing the , the service has to be restarted.

## Interesting channels
KDE community has a wide variety of matrix rooms for specific applications, languages, events and etc. See https://community.kde.org/Matrix for details.

The GNOME Community also has a Matrix instance for its instant communications with a wide variety of matrix rooms. See https://wiki.gnome.org/GettingInTouch/Matrix for details.

## Troubleshooting
## Read-only file system
By default, synapse can only write to the working-directory () set in its service file. A write-error may occur if synapse writes to a different path (e.g. your media-store is in ).

You can allow access to other directories by creating a replacement unit file for  and by adding  to the  section.

## High memory consumption
The memory consumption of Synapse can be significantly reducedby installing . To enable it, the environment variable  must be set accordingly. This can be done by creating , which will be applied by the systemd unit file.[https://gitlab.archlinux.org/archlinux/packaging/packages/matrix-synapse/-/blob/main/synapse.service?ref_type=heads#L18

After enabling jemalloc, the memory footprint can be reduced further by tuning cache settings: https://element-hq.github.io/synapse/latest/usage/configuration/config_documentation.html#caches-and-associated-values

The configuration options under  will not work unless jemalloc is enabled.
