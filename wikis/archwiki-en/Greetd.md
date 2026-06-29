# Greetd

greetd is a minimal, agnostic and flexible login manager daemon which does not make assumptions about what the user wants to launch, should it be console-based or graphical. Any script or program which can be started from the console may be launched by greetd, which makes it particularly suitable for Wayland compositors.  It can also launch a greeter to start user sessions, like any other display manager.

## Installation
Install the  or  packages.

The default greetd configuration file is located at .
PAM-specific configuration is set in .

## Greeters
Greetd has greetd-agreety as its built-in greeter, however this is a minimal implementation. You should consider using one of the several available greeters:

*
*
*
*
*
*
*
*
*
*
*
*

## Starting greetd
Enable  so greetd will be started at boot.

See also Display manager#Loading the display manager.

## Greeter configuration
Configuring the greeter run by greetd is done using the  option in the  section in .
The included  greeter will be used if no changes are made. Also see #agreety.

By default, greeters are run as the  user. This can be changed by editing the  option in the  section of the configuration file and replacing another_user with the chosen user:

 ...
 user = "another_user"
 ...

Make sure the ownership of the  directory is set accordingly.

## agreety
This is the default greeter. It is launched by greetd with the configuration file set as follows:

 ...
 [default_session
 command = "agreety --cmd $SHELL"
 ...

agreety can launch any arbitrary command once a user logs in. For example, in order to start Sway, replace  in the example above with .

## gtkgreet
In order to run, gtkgreet needs a compositor. For the full experience, a compositor with  support is required but others can work. As such, it is recommended to use , but something like  can also be used. Examples for both cage and sway are provided below.

In order to specify which login environments can be started by gtkgreet, list them in .
For example:

 sway
 bash

You can also invoke gtkgreet with the  parameter, replacing mycommand with the desired program (for example,  or ). Do so in the below compositor examples as desired.

## Using cage
Install  and set the  option as follows:

 ...
 command = "cage -s -- gtkgreet"
 ...

The  argument enables VT switching in cage (0.1.2 and newer only), which is highly recommended to prevent locking yourself out.

## Using sway
Install . When using Sway, it must be terminated once the user logs in. For that purpose, a specific configuration file must be created, for example in , with the following content:

Then, greetd must be set to start Sway with the configuration file above. Set the  option as follows:

 ...
 [default_session
 command = "sway --config /etc/greetd/sway-config"
 ...

## ReGreet
Similar to gtkgreet, ReGreet needs a compositor. For example, both Cage and Sway can be used just like they are used for gtkgreet, replacing the gtkgreet command with regreet. The config for Sway would thus look like:

ReGreet picks up available sessions from  (for X11 sessions) and  (for Wayland sessions). Thus, there is no need to list sessions in .

ReGreet can be configured through a TOML file in . A sample file is provided in  with all available options. Copy this to  and make the changes you want, commenting out or deleting the lines you do not need. Any invalid options are ignored.

## Using Hyprland
Set the  option as follows:

 ...
 command = "start-hyprland -- -c /etc/greetd/hyprland.conf"
 ...

Then create  as:

## wlgreet
In order to start wlgreet, a compositor with  is required. Follow the steps required to set up gtkgreet with Sway as described above but use the following for  instead:

## tuigreet
tuigreet does not require any special setup. Set the  option as follows, replacing sway if you use a different desktop environment/window manager:

 ...
 [default_session
 command = "tuigreet --cmd sway"
 ...

 will display customization options.

## ddlm
ddlm does not require any special setup, just set the  option as follows, replacing sway if you use a different desktop environment/window manager:

 ...
 command = "ddlm --target sway"
 ...

## qtgreet
In order to use qtgreet, you need a WLR based compositor (e.g. , ).

## Using Wayfire
Install  and set the  option as follows:

 ...
 [default_session
 command = "wayfire --config /etc/qtgreet/wayfire.ini"
 ...

The Wayfire configuration file referred to is included with qtgreet.

## Using Hyprland
Set the  option as follows:

 ...
 command = "start-hyprland -- -c /etc/greetd/hyprland.conf"
 ...

Then create  as:

## nwg-hello
In order to use nwg-hello, you either need  or .

## Using Sway
Install  and set the  option as follows:

 ...
 [default_session
 command = "sway -c /etc/nwg-hello/sway-config"
 ...

The Sway configuration file referred to is included with nwg-hello.

## Using Hyprland
Install  and set the  option as follows:

 ...
 command = "start-hyprland -- -c /etc/nwg-hello/hyprland.conf"
 ...

The Hyprland configuration file referred to is included with nwg-hello.

## Tips and tricks
## Enabling autologin
If you want a user to be logged in automatically, an  section must be defined in :

 ...
 [initial_session
 command = "sway"
 user = "myuser"
 ...

The  option may contain the name of any executable file. In the example above, Sway will be started by  at boot.

If you do not want to use greetd and always want autologin to be enabled, see autologin.

## Unlocking keyring on autologin using the cryptsetup password
Autologin is often used on a single-user system with full disk encryption.
Both GNOME/Keyring and KDE Wallet can be unlocked using the encryption password entered at boot.
In the case of other display managers, this typically requires an entry such as , , or similar, in the PAM config.

However, this setup does not work with greetd because it skips the  stack entirely.
Instead, use the pam_fde_boot_pw module (currently not packaged and not in AUR).

After installing the module to , use the following PAM config. Substitute  (GNOME Keyring) with  for KDE Wallet.

## Run local programs
Add the  environment variable to , or the desktop environment called by greetd will not be able to run local programs. Greetd will not source shell configuration files and thus not get any modified variables from these files.

## Setting the environment
By default greetd does not set environment variables such as  and , unless the greeter sets them based on the session you chose (for example TUI will set the session type based on the location of the session file chosen). One way to solve this is to use a wrapper script that sets any desired environment variables before running the actual command. For example to start sway:

then use this wrapper script as the command the greeter runs. For example with  you could use

or put  in .

See How to Set XDG_SESSION_TYPE=wayland

## Setting logind session type
The logind session type is set by the XDG_SESSION_TYPE environment variable. However, it must be set before the PAM session is opened. Because of this, setting the variable through  or a wrapper script will not work (both happen after session open).

The correct way to achieve this is through the environment variables sent by greeters (these are set before session open). So if your greeter supports it, just make it send the appropriate

If your greeter does not support this, it is also possible to use pam_env under the auth group. The drawback is that all the sessions spawned by greetd will use that session type, which may or may not be problematic depending on your use case.

Here is how one could use the pam_env method to have a Wayland session:

## Missing mouse cursor
If you are using  with a compositor such as  and generally need to export variables, such as  to get the mouse cursor working, one solution would be to create a separate executable script and then calling that from .

## Prevent systemd messages from overwriting console-based greeterd
If you are using console-based greeters such as  systemd messages can overwrite UI. To prevent this you may use  kernel parameter as it prevents display of any messages (also during boot).

If you still would like to see messages during boot, you could instead append  to kernel parameters. This would redirect all messages from  (which broadcasts to all ttys) to , which is utilized during boot. Now you just need to select any other TTY for greeter. Either specify particular tty (other than tty1) or use  option. According to  this must be in the  section
