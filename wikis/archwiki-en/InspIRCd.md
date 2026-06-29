# InspIRCd

InspIRCd (Inspire IRC daemon) is a modular and lightweight IRC daemon written in C++. As it is one of the few IRCd projects written from scratch, it avoids a number of design flaws and speed issues that plague other more established IRCd projects with the same or less features, such as UnrealIRCd 3. It is the IRCd used by the Chatspike IRC network.

## Installing
Install the  package.

## Configuring
The configuration file  is mandatory, XML-formatted and needs to be created when installing.

How you set your configuration file will depend a lot on your needs and system configuration, reason why there is no configuration file set by default.

Its markup language format may be somewhat different of what most of the people is used to. The format of an instruction within the configuration file looks like the following:

Make sure to set the pidfile to , as explained in the package's install script.

Further information is available at the InspIRCd configuration wiki page.

## Loading modules
By default, InspIRCd loads no modules. As every feature outside of RFC 1459 is actually a module, by loading no modules your ircd really will not do anything impressive.
You can load modules by adding for instance:

This will load the m_silence module (which provides the somewhat standard SILENCE list facility). You must restart the daemon for changes to take effect.
A list of the available modules is available at the InspIRCd modules wiki page.

## Third-party modules
To install a third-party module, save the  within  and continue the build process. If you have already built and installed InspIRCd and have the source files intact, compile the module with  and copy to: .

## Starting/Stopping the daemon
Start or stop .

The first start fails sometimes so try restarting until you get no errors. After this you shall have no further problems.
The reason behind this is because of security reasons the daemon does not run as root as you normally would see, so the script must ensure that the user irc has permission to write/read the pid and log files.
