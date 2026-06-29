# Minecraft/Java Edition server

Minecraft is a multiplayer game. It uses the client-server model in which the game itself is a client which can be played standalone, or can be played with other players when the client connects to a public server.

## Installation
The Java Edition Minecraft server can be installed via the  package. It provides additional systemd unit files and includes a small control script.

Also see #Alternatives for an overview of alternative programs to host Minecraft.

## Configuration
In the installation process, the  user and group are created. Establishing a Minecraft-specific user is recommended for security reasons. By running Minecraft under an unprivileged user account, anyone who successfully exploits your Minecraft server will only get access to that user account, and not yours.
However, you may safely add your user to the  group and add group write permission to the directory  (default) to modify Minecraft server settings. Make sure that all files in the  directory are either owned by the  user, or that the user has by other means read and write permissions. The server will error out if it is unable to access certain files and might even have insufficient rights to write an according error message to the log.

The package provides a systemd service and timer to take automatic backups. By default, the backups are located in the  folder under the server root directory. Though to keep the disk footprint small only the 10 most recent backups are preserved (configurable via ). The related systemd files are  and . They may easily be adapted to your liking, e.g. to follow a custom backup interval.

## Starting the server
To start the server, you may either use systemd or run it directly from the command line. Either way, the server is encapsulated in a tmux session which is owned by the  user. Using systemd, you may start/enable the included . Alternatively, run

 # minecraftd start

## Accepting the EULA
In order to run the Minecraft server, you must accept the End User License Agreement. This only needs to happen once after installation. The EULA file resides under  after being created by the package. You will need to edit this file to state that you have agreed to the contract in order to run the server. All you need to do is change:

 eula=false

to the value . Here is an example of an accepted EULA:

## Firewall configuration
There are three settings in the  which determine ports that your server will use.

 determines the  port at which the server will listen for incoming connections. The default port is .

 determines the  port at which the server will share game info/advertising information. The default port is . Note that since the server and query ports are TCP and UDP, they can share the same port. To enable query, you also have to specify .

 determines the  port if you choose to allow remote access to admin console. The default port is . To enable rcon, you also have to specify  and .

You will need to allow incoming connections at least on the . It is advisable to allow query and its . On the other hand, enabling remote console access is a security risk, and you should be careful of allowing it.

The above information is for the official Minecraft server. If you are using an alternative server, please see its documentation for details about its configuration.

See and [https://minecraft.wiki/Server.properties for more information.

## Server management script
To easily control the server, you may use the provided  script. It is capable of doing basic commands like , ,  or attaching to the session with . Moreover, it may be used to display status information with , backup the server world directory with , restore world data from backups with  or run single commands in the server console with .

## Tweaking
To tweak the default settings (e.g. the maximum RAM, number of threads etc.), edit the file .

For example, more advanced users may wish to enable  by setting it to . This will enable the management script to suspend the server if no player was online for at least  (defaults to 20 minutes). When the server is suspended, an  will listen on the Minecraft port using  from  (or any other implementation of netcat) and will immediately start the server at the first incoming connection. Though this obviously delays joining for the first time after suspension, it significantly decreases the CPU and memory usage leading to more reasonable resource and power consumption levels.

## Alternatives
## Spigot (respectively Craftbukkit)
Spigot is the most widely-used modded Minecraft server in the world. It can be installed with the  package. The spigot PKGBUILD builds on top of the files from the  package. This means that the spigot server provides its own systemd unit files, spigot script and  corresponding script configuration file. The binary is called  and is capable of fulfilling the same commands as . The configuration file resides under .

Be sure to read #Configuration and replace  with  wherever you encounter it.

It is somewhat affiliated with Bukkit and has grown in popularity since Bukkit's demise.

## Cuberite
Cuberite is a highly efficient and extensively moddable Minecraft server, written in C++ and Lua. It achieves much better performances than the vanilla Minecraft server, but it is not fully compatible with the latest Minecraft client (some game aspects might be missing or not working).

The Cuberite Minecraft server can be installed as a  package, which provides a simple web interface by default at port  with which most server operations can easily be done through the browser. The cuberite PKGBUILD builds on top of the files from the  package. This means that the cuberite server provides its own systemd unit files, cuberite script and corresponding script configuration file. The binary is called  and is capable of fulfilling the same commands as . The configuration file resides under .

Be sure to read #Configuration and replace  with  wherever you encounter it.

## PaperMC
PaperMC is a Minecraft server, compatible with Spigot plugins which aims to offer better performance. It can be installed via .

Be sure to read #Configuration and replace  with  wherever you encounter it.

## Forge
Forge is a widely used Minecraft modding API. The server package can be installed via . Alternatively the AUR also provides packages for older versions of Minecraft:

*
*
*
*
*
*
*
*
*

Be sure to read #Configuration and replace  with  ( for legacy versions) wherever you encounter it.

## Fabric
Fabric is a lightweight, experimental modding toolchain for Minecraft. The server package can be installed via .

Be sure to read #Configuration and replace  with  wherever you encounter it.

## Quilt
Quilt is an open-source, community-driven modding toolchain designed primarily for Minecraft. The server package can be installed via .

Be sure to read #Configuration and replace  with  wherever you encounter it.

It is originally forked from Fabric, meaning it is mostly backwards compatible with Fabric mods.

## Tips and tricks
## Minecraft server port
By default Minecraft servers run on port , this port is assumed if an address is entered without a port specified.

Most Minecraft server providers will charge a premium for a server with the default minecraft port, therefore if your port differs from  you must specify the port by appending a colon (:) to the end of the hostname or address followed by the port which was allocated to your server, for example if you address was  and port was  you would connect to .

## Troubleshooting
## Logs
If systemctl fails to start the service, inspect the screen logs at .

Journal logs are under .
