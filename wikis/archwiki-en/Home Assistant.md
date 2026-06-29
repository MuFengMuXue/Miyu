# Home Assistant

Home Assistant is an open-source home automation software that puts local control and privacy first.

## Installation
The  core package has been dropped from the official repositories. The recommended method for running Home Assistant is now via a container, such as Docker or Podman.

## Docker
## Prerequisites
Install the  and  packages.

Start/enable the .

Add your user to the  user group to manage Docker without .

You must log out and log back in for this change to take effect.

## Setup
1. Create a project directory to hold your configuration and the  file.

2. Create a  file.

3. Start Home Assistant.

Docker will download the image and start the container. The first start may take several minutes.

The web interface will be available at http://localhost:8123. All configuration files will be stored in .

## Podman
Podman is a daemonless alternative to Docker with native systemd integration via Quadlets.

## Prerequisites
Install the  package.

## Setup
1. Create a directory for the configuration.

2. Create a Quadlet file:

3. Reload systemd and start the service.

The Quadlet will automatically generate a systemd service that starts on boot. Check status with:

The web interface will be available at http://localhost:8123. All configuration files will be stored in .

## Updating
To update Home Assistant:

## Migrating from the home-assistant-core package
If you were previously using the official  package, follow these steps to migrate to a Docker setup.

1. Create a full backup of the .

2. Stop and disable the old service.

3. Follow the "Initial Setup" steps in the section above to create your  directory and  file. Do not start the container yet.

4. Move your existing configuration to the new location.

5. Correct the file permissions. Replace  with your own username.

6. Now, start your new container.

Home Assistant will start using your existing configuration.

## Usage
Manage your Home Assistant container from your project directory () using .

* To stop the container:

* To start the container:

* To view the logs:

* To update Home Assistant to the latest stable version:

## Configuration
## Using an external database
Using an external database like MariaDB or PostgreSQL can improve performance. The required Python drivers are already included in the Home Assistant Docker image.

1. Install your chosen database server. Refer to the MariaDB or PostgreSQL pages for setup instructions.

2. Create a database and user for Home Assistant.
* For MariaDB:

* For PostgreSQL:

3. Add the recorder configuration to :

Replace  with the connection string for your database:
* MariaDB/MySQL:
* PostgreSQL:

## Troubleshooting
## Access to USB devices (Zigbee/Z-Wave)
To use a USB device like a Zigbee dongle, it must be passed from the host to the container.

1. Find the device's persistent path.

2. Add the user running Docker to the  or  group, which typically owns serial devices. Check the device's group with .

You will need to log out and back in for this to take effect.

3. Uncomment and edit the  section in your  file to map your host device to a path inside the container.

4. Recreate the container to apply the changes.
