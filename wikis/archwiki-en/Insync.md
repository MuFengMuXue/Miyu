# Insync

insync is an alternative Google Drive and Microsoft OneDrive client that is available for Windows, macOS, and Linux which allows you to sync a local folder or symlinked folders with your Google Drive or OneDrive. Whilst previous Beta versions used to be for free, the final release features a trial period after which a one-time payment per account is required.

## Installation
Install the  package. It contains the synchronization daemon, a systemd service file, and a command-line utility for configuration. It can be used and integrates nicely with different desktop environments such as KDE, Gnome, or Cinnamon.

## Configuration
Insync can be started with the  command and stopped with the  command. A shortcut for starting Insync should be available in the applications menu of your desktop environment.

## Running as a systemd service
Enable  or the systemd user service .

## Cinnamon
When you start insync from the start menu it may not appear in the taskbar. For that, you need to add the taskbar applet by right-clicking on your panel.

## Usage
The usage is self-explanatory. Copy files and folders from and to your local folder to sync it with your Google Drive.

## Control via CLI
CLI support was dropped in the latest versions. However, users who need CLI support or want to use Insync headless can use Insync 1.5.7.

See Headless and CLI community support and How to control Insync via command line (CLI).

## Troubleshooting
## Slow sync process
The default systemd service file provided in  uses the  flag to make sqlite transactions safer and prevent database corruption. However, for some users this might considerably slow down the sync process. If you do not need full synchronisation, use a drop-in file to modify the  variable:

## GUI not starting and failing silently
When running , the system tray icon does not appear and Insync does not start.

According to https://forums.insynchq.com/t/insync-arch-linux-not-starting-segfault-at-730-error-14/8893, this is due to . You will need to set the Qt4 theme to something other than GTK using .

This issue is sometimes observed when using the Nouveau driver for NVIDIA graphics cards, and can be resolved by using the proprietary NVIDIA drivers.

Running  from the terminal logs output to stdout and prevents the process from being detached. This makes troubleshooting much simpler.

## Missing system tray icon
If Insync is running, but it is not appearing in your system tray, try running it with the  environment variable.

If the system tray icon still is not showing, you can try running it a after rather than before starting your window manager. For example, do not run  from xinitrc, but from the window manager's autostart mechanism.

## System tray icon flickers between checkmark and inactive
This problem may occur due to Insync using Google's API telemetry for analytics, which could be blocked by a network installed Pi-hole. To fix, enter Insync's app settings and disable "Anonymously send usage data to Insync".
