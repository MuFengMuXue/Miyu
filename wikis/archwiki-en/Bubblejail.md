# Bubblejail

Bubblejail is a Bubblewrap based sandboxing utility.

Bubblejail has a resource oriented permission model. For example, x11 is a resource that can be added to sandbox. This will give sandbox access to X11 display server.

Bubblejail also uses seccomp and D-Bus filtering to enhance security and permission model.

Bubblejail also has a graphical interface that allows creating and configuring sandboxes.

## Installation
Install  or .

## Usage
Bubblejail sandboxes are separated in to instances. Each instance is a separate home directory and a permissions configuration.

Each instance usually sandboxes one application.

## Creating Instances
New instances are usually created from an available profiles. The profile is initial set of permissions and the desktop entry used. If a specific application is missing the profile a  profile or empty profile can be used and tweaked after creation.

## Using graphical interface
Run the Bubblejail Configuration application. On the first screen at the bottom there will be Create Instance button.

## Using command line
For example, creating a Firefox instance:

 $ bubblejail create --profile firefox instance_name

## Running instance
## Using desktop entry
When creating an instance a desktop entry will be generated unless  option was used.

Desktop entry would have the instance_name bubble name and can be launched from the desktop environment.

## Using command line
Once created the instance can be run with  subcommand:

 $ bubblejail run instance_name args

If no arguments are passed when the default arguments will be used based on the profile used.

If args are passed when those arguments will be executed inside the sandbox. First argument should be the binary name and following arguments will be passed to this binary.

## Configuration
Once the instance has been created its permissions and resources can be modified. For modified permissions to take effect the sandbox needs to be restarted.

The profile used when creating sandbox only affect the initial set of permissions. However, removing certain permissions might prevent targeted application from working correctly.

## Using graphical interface
Run the Bubblejail Configuration application. On the first screen click on the name of the sandbox you want to modify. This will bring up the list of all available permissions and a Save button.

## Using command line
Bubblejail provides  command that will open the configuration file in the editor defined  Environment variables.

 $ bubblejail edit instance_name

Bubblejail uses TOML for its configuration. The defined dictionaries gives permission for a specific resource and key value pairs inside dictionaries will set a specific resource settings.

For example:

This config defines two resources available to sandbox: the x11 windowing system and shares the Downloads directory in the home folder.

The available services and options are documented in  man page.

## Tips and tricks
## Running terminal inside sandbox
Using  command a terminal can be launched inside already running sandbox. The terminal can be used to debug the sandbox.

It is recommended to use the terminal application that requires minimal amount of permissions such as Alacritty which only requires access to windowing system. (either x11 or wayland)

 $ bubblejail run instance_name alacritty

## Re-using profile for similar applications
If an application is missing a profile but there is a related software with existing profile that profile can be used.

For example,  profile can be used on any chromium derived browser such as qutebrowser.

First, generate the instance using  profile but disable the desktop entry creation.

 $ bubblejail create --no-desktop-entry --profile chromium qutebrowser

Now a desktop entry can be created from the qutebrowser's desktop entry.

 $ bubblejail generate-desktop-entry --desktop-entry /usr/share/applications/org.qutebrowser.qutebrowser.desktop qutebrowser

Now the sandboxed qutebrowser can be launched with the  desktop entry.

## "Instance already running" error
It can happen sometimes, that the process started in the sandbox instance has ended, but Bubblejail does not recognize this. This makes it impossible to run the sandbox instance again. Bubblejail quits with an "Instance already running" error.

To fix this you can delete the contents of the run directory of the failed sandbox instance. The directories for all jails are located at .
