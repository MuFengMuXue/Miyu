# COSMIC

COSMIC is the desktop environment made for Pop!_OS. It was originally a heavily modified version of GNOME but was later remade from scratch in the Rust programming language, using the iced cross platform GUI library for Rust, and Smithay as building blocks for its compositor, cosmic-comp. Cosmic-comp is comparable to smithay's own anvil compositor demonstration, just like the Wayland project uses Weston as a demo compositor. Its first release is called Epoch.

## Installation
COSMIC can be installed via  or the  group.

## Individual components coming as dependencies of cosmic-session
COSMIC comprises a compositor, library, and applets, which may be installed as parts. , , , , , , , on screen display to overlay messages with , a dock and panel with , , and others.

## Independent components
An editor, , a file manager , a terminal, , a multimedia player , and wallpapers,  are provided.

## Network shares in COSMIC Files
To connect to network shares in COSMIC Files, the relevant GVFS package needs to be installed:

{| class="wikitable"
|-
! Protocol !! Package
|-
| AppleTalk ||
|-
| File Transfer Protocol (FTP) ||
|-
| Network File System (NFS) ||
|-
| Server Message Block (SMB) ||
|-
| SSH ||
|-
| WebDAV ||
|}

COSMIC doesn't provide a secrets store/keyring, so to remember passwords, install a secrets storage component such as . See also GNOME/Keyring.

## Starting
The easiest way to start COSMIC is through a display manager, where it will show up as an additional option after installation, alongside GNOME, KDE Plasma, etc.

To start COSMIC directly from the console, run:

 $ start-cosmic

## Using Cosmic Greeter
COSMIC ships , a display manager based on greetd. To use it, enable .

## Configuration
The panel can be used to configure besides using the settings applet, examples of applets are provided.

## SSH_AUTH_SOCK not set
The  message appears briefly at login with Cosmic Login Manager when the variable has not been properly configured for use with SSH.

To use the GNOME Keyring as a wrapper around ssh-agent that automatically sets this variable, see GNOME/Keyring#Setup gcr

To use the systemd service and manually set the environment variable, see SSH keys#Start ssh-agent with systemd user.

## Night light
Because COSMIC DE does not yet implement the  Wayland protocol (see pop-os/cosmic-comp#2059), tools like wlsunset and gammastep cannot control backlight color temperature from within a COSMIC session.

To work around this issue, you can directly adjust DRM gamma tables via libdrm from a TTY before the COSMIC DE compositor launches, using tools like  or . Another option is to use drm-colortemp or  which rely on a systemd service to automate the process.
