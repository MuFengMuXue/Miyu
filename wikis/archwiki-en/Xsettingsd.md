# Xsettingsd

Xsettingsd is a lightweight xsettings daemon which provides settings to Xorg applications via the XSETTINGS specification.

Some desktop environments (such as Plasma by default, or a custom one) do not include this. In such environments running an xsettings daemon is necessary for some applications (most notably GTK–, Java– and Wine–based) to use the selected theme, cursor, font, and other settings.

## Installation
Install  or .

## Configuration
 contains just brief intro, see README for details.

An example configuration to X FreeType font rendering (you can use your preferred config file path):

## Usage
Start the user unit .

This unit is static, so it cannot be enabled directly. You can autostart it (or  binary) on Xorg, desktop environment or window manager startup.

The unit is configured as  the , so it stops (restarts) when  is stopped (restarted), see  and .

## Troubleshooting
## Unable to open connection to X server
Check that  and  environment variables are set.

If you are starting the systemd unit, check that  was executed (it can be done by  invoked from your ).
