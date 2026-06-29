# Minecraft

Minecraft is a game about breaking and placing blocks. At first, people built structures to protect against nocturnal monsters, but as the game grew, players worked together to create wonderful, imaginative things.

There are two separate editions of this game: Minecraft Java Edition, and Bedrock Edition. Java Edition is the original version of the game, starting development back in 2009. This edition can be played on Mac, Windows and Linux. Bedrock Edition was originally Pocket Edition, but has since been ported to different platforms. It is currently supported on Windows 10 and 11, Amazon FireOS and FireTV, Android, iOS, Xbox One, Playstation 4, Nintendo Switch and Samsung Gear VR devices. The Bedrock Edition client is not supported on Linux officially, but Bedrock server software is available.

## Client
## Java Edition
## Installation
The Minecraft client can be installed via the  package. It provides the official game launcher, a script to launch it and a .desktop file. The package is officially recommended by Mojang on their website.

## Firewall configuration for Client/LAN worlds
Most shared Minecraft worlds are hosted using dedicated Minecraft servers. For more information about hosting dedicated servers, see the #Server section below.

A simpler way is to allow others to join your current Minecraft game. When playing, your Minecraft client also allows others to join the game in progress. Your client automatically broadcasts the info about your game on port 4445. It will also listen for TCP connections on which other players join. This TCP listening port is picked at random every time you start Minecraft. This works well if you do not have a firewall. But if your firewall blocks incoming TCP connections, then it is very tricky to allow this random port in.

To allow your client to host a local LAN game, your firewall needs to allow:
* UDP port  to broadcast your game.
* A TCP port to allow friends to join your game.

See also:
* Setting up a LAN world.

## Bedrock Edition
The unofficial Bedrock Minecraft client can be installed by  package, which is the UI interface for .

## Server
## Java Edition
See Minecraft/Java Edition server for more information on how to set up a Minecraft Java server.

## Bedrock Edition
## Installation
The Bedrock Minecraft server can be installed via the  package. It provides a systemd unit file. This package creates a separate  account.

To start the server, you may either use systemd or run it directly from the command line. Using systemd, you may start and enable the included . Alternatively, run the following as the minecraft-bedrock user inside the  directory:

 $ LD_LIBRARY_PATH=. ./bedrock_server

## Configuration
The configuration file  contains the server settings and additional documentation. Most importantly,  determines the  port at which the server will listen for incoming connections. The default port is  for IPv4, and  for IPv6. UDP ports  for IPv4 and  for IPv6 are required for authentication.

## Minecraft mod launchers
You can launch Minecraft from different so called launchers that often include an array of modpacks to enhance one's gameplay and add mods.

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
*
*
*
*

## Other programs and editors
There are several programs and editors which can make your Minecraft experience a little easier to navigate. The most common of these programs are map generators. Using one of these programs will allow you to load up a Minecraft world file and render it as a 2D image, providing you with a top-down map of the world.

*

*

*

*

## Tips and tricks
## Enable HRTF directional audio support
Edit the following file and then enable directional audio in the in-game sound settings:

## Troubleshooting
## Client or server does not start
It might be a problem with the Java version. Different Minecraft version numbers have different JRE requirements.

{| class="wikitable"
! Minecraft Version !! Minimum Compatible JRE Version
|-
| = 26.1 || 25
|}

## Broken fonts with MinecraftForge
Force Unicode fonts from the language menu.

Since you cannot read any of the menu options: in the main menu, choose the bottom-left most button is Options, second-from-the-bottom on the left side is the Language Button. From there, the Force Unicode Font button is on the bottom, on the left side.

## Cannot change pulseaudio sink
If you are unable to switch the audio output device (indicated by  flag in the output of ), then the following openalsoft config may help

## Audio missing/stutters on PipeWire or Java crashes with SIGFPE
OpenAL defaults to using JACK over PipeWire's PulseAudio backend. If that causes issues for you, you can tell OpenAL to use Pulse instead:

Alternatively, you can set the environment variable  for Minecraft if you do not want to configure this for all applications.

## Minecraft does not start on native Wayland
You may see an error like .

This is because of the version of GLFW bundled with Minecraft defaulting to X. If you do not want to use Xwayland, you can resolve this by using the system installation of :

* For MultiMC-based launchers (like ) check Workarounds > Native Settings > Use system GLFW in the instance settings.
* For others, add  to the java command in the settings.

## 2 and 6 do not work when pressed in combination with shift on legacy versions
This is a problem caused by LWGLJ2. There are a few ways to fix it:

* Use a client that uses an updated version of LWGLJ or adds the patch themselves.
* Switch keyboard layout to a different one (e.g. German).
* Use mods to fix it. On 1.8.9 Forge, you can use mckeyboardfix.
