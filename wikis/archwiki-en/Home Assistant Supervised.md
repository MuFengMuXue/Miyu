# Home Assistant Supervised

Home Assistant is an open source home automation software that puts local control and privacy first. Powered by a worldwide community of tinkerers and DIY enthusiasts. Supervised is a type of installation that provides the ability to use more features, like Addons installation from UI.

## Install
Install the  package.

And guarantee that AppArmor is correctly installed and configured.

## Configuration
Supervised configuration files are stored at . If no configuration exists, a default configuration will be written at startup.
To access just Home Assistant's configuration files go to .

## If installed before v3.0.0
Supervised configuration files were changed from  to . You can keep the old configuration. You can change the location by setting the data value in the config file .

## Usage
To start Home Assistant, start/enable  and .

The first start may take up to 20 minutes because the required packages will be downloaded and installed.By default, the web interface is available at http://localhost:8123.

## Troubleshooting
Before doing anything, check if supervisor is Connected and the installation Healthy. You can do that by accessing the [https://github.com/home-assistant/plugin-observer Observable Plugin, which can be accessed at http://localhost:4357.

## Supervisor not connected
# Check if  is started/enabled.
# Check if your supervisor container is up and running.

:

## Supervisor connected but installation Unhealth
# Check if your AppArmor#Display current status is correctly installed and configured.
# Check if you start/enable  service.
# Look at Supervisor logs for additional information:
 # docker logs -f hassio_supervisor

## file /etc/hassio.json does not exist
Make sure you have the  configuration file.

If not, create it and fill it with sample data:

{{bc|
{
    "supervisor": "ghcr.io/home-assistant/amd64-hassio-supervisor",
    "machine": "generic-x86-64",
    "data": "/var/lib/homeassistant"
}
}}
