# PeerTube

From Wikipedia:PeerTube:

:PeerTube is a free and open-source, decentralized, federated video platform powered by ActivityPub and WebTorrent, that uses peer-to-peer technology to reduce load on individual servers when viewing videos.

## Installation
Install the  package.

## Configuration
Follow the configuration steps of the production guide:

# Create a database and user with a password in PostgreSQL, following the instructions on the GitHub link.
# Edit the first section of the . Make sure you change the database password to match the one you set earlier.
# Start/enable the Redis service.
# If you want to edit the settings through the web UI, you must change the ownership of the configuration folder:
# (Optional) Configure and start a reverse proxy. PeerTube has official support for nginx, and the configuration file can be found at  Make sure you change the file paths to the ones used by this package.
# (Optional) If you are having trouble with getting the package to work, fix possible permissions problems:

Finally, start the  service and point your browser to the URL from the configuration file (http://localhost:9000 by default without a reverse proxy).
