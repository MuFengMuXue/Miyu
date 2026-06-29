# Xrdp

xrdp is a daemon that supports Microsoft's Remote Desktop Protocol (RDP).
It uses Xvnc or xorgxrdp as a backend.

## Installation
Install the  package. This only supports Xvnc as the backend.

## Xorg backend
To use xorgxrdp instead for the backend, install the  package.

## Usage
First, start the  service. You should be able to connect an RDP client to the host on the default RDP port (3389). If successful, you will be greeted with the xrdp session manager window which allows you to choose between Xorg or Xvnc sessions and provides inputs for user authentication. The session manager UI can be highly customized by modifying .

The parameters used to start Xorg and Xvnc display servers can be configured in .

After successfully starting a display server, xrdp will execute  by default. This script is meant to start a window manager (similar to .xinitrc) and will read from  or  if they exist. It is recommended to edit  to start your desktop environment or window manager, but you can also edit .

If you just close the session window and RDP connection, you can access the same session again next time you connect with RDP. When you exit the window manager or desktop environment from the session window, the session will close and a new session will be opened the next time.

## Configuration
## Running as unprivileged user and group
It is highly recommended to set the user and group under which the xrdp daemon is run to an unprivileged user. To do this, first create the  user and group:

Then uncomment the following values in  to set the user which will run the daemon:

Also ensure that the value of  in  matches the runtime group above.

After making these changes, check the file permissions required by the daemon using the script  and correct any issues detected.

Finally, restart the  daemon.

## Tips and tricks
## Autostart at boot
The  package contains service files for systemd. Enable .

## Graphical acceleration
For Xorg sessions, you can enable OpenGL and Vulkan graphical acceleration by installing  for Intel and AMD GPUs and  for NVIDIA GPUs.

## Sound
Install the necessary PulseAudio modules with .

for PipeWire user, install .

## Non-root user
Include the following lines in :

If the above lines are not present, the remote desktop connection from applications like Remmina will start with an empty screen.

## Access via SSH tunnel
For added security, if the server offers SSH connections you may choose to only allow local connections and then tunnel the connection over SSH. This has the advantage that you don't need to expose the xrdp port to the public internet.

Set the port for the xrdp daemon to only monitor local connections:

On the client, open an SSH connection with TCP forwarding to the xrdp server:

In the RDP client, connect to  to access xrdp over the SSH tunnel.

For more information, see OpenSSH#Forwarding other ports and .

## Troubleshooting
## Black box around cursor
If you encounter black box around mouse pointer create  with line  and load it in  like

You may need to install .

## Black screen
You may get a black screen after logging into the session manager.

The last line in  may look like . It needs a default parameter, if not supplied in .

One can edit the last line of  to be {{ic|exec $(get_session "${1:-"$SESSION"}")}} or {{ic|exec $(get_session "${1:-xfce}")}}, depending on your preference.

Alternatively, you can also edit your call to  in ; eg. . This will affect all users.

## Black screen with a desktop environment
If you get a black screen and you use a desktop environment, it may be a result of D-Bus not being properly initialized. Some DEs (like KDE Plasma) might also be able to restore fully working applications/windows from a previous session, which makes it seem that "only plasmashell" is missing.

Try running the desktop environment with  in your  file. For KDE Plasma, you can use the command  or .

## Green screen
If the login dialog appears, but no desktop environment starts when you click OK, change  to  in .

## loginctl or systemctl --user not working
Try commenting out all the references to  in . See this issue.

## Prompts for gnome-keyring or KDE Wallet
If you are prompted to login to gnome-keyring or Wallet when your session starts, modify the file  as follows:

Then, add  (no leading slash) to  in . If you only use gnome-keyring it is not necessary to include the kwallet5 lines, and vice versa.

## Prevent autostart items from starting
To prevent user defined  items from starting you can set the autostart directory param on the session in the  to use only the global  directory.

{{bc|
get_session(){
    local dbus_args=(--sh-syntax)
    case "$SESSION" in
        awesome) dbus_args+=(awesome) ;;
        bspwm) dbus_args+=(bspwm-session) ;;
        budgie) dbus_args+=(budgie-desktop) ;;
        cinnamon) dbus_args+=(cinnamon-session -a /etc/xdg/autostart) ;;
}}

## No sound
If you are using pipewire or pulseaudio, check if your modules are installed. In AUR, it's  and . Remember to logout and login for them to take effect

This could also be a symptom of an issue with loginctl, so try that fix above. The following error may be encountered in the system journal:

 Failed to load module "module-x11-publish" (argument: "display=:10.0 xauthority="): initialization failed.

This is the result of systemd improperly starting PulseAudio. One workaround is to disable the user unit files  and  either for your own user or for all users, and make PulseAudio start when needed by setting  to  in .

If sound still does not work, try manually starting PulseAudio with  in your .

## Two-finger scrolling is too fast
Use the xorg backend, make sure xorgxrdp is 0.9.19 or newer. Then add  to the  section of .

See upstream issue #150 for details.

## Restricted functionality within remote system
A user may not have the same access permissions when logged into a system remotely as the same user does when logged in locally. Additional configuration may be required of the polkit permissions policies to grant access, including to mounted drives or to control network connections.

## Mounted drives
For remote access permissions to mounted drives see udisks#Permissions.

## NetworkManager
For remote access permissions to NetworkManager see NetworkManager#Set up PolicyKit permissions.

## H.264 codec
xrdp since 0.10.2 offers H.264 as the preferred codec. The default is turned for performance and may cause video quality degradation or sluggish, depending on the GPU. You can tune this by editing
. See  for the list of options. Usually, you could try  if video quality is not good, or  if you are in a good network and H.264 is causing more latency.

## Cannot use podman
podman relies on DBUS_SESSION_BUS_ADDRESS being correctly set, like  However, xrdp requires a new dbus-session and set it to a temporary location.

The solution is to set it again in your
