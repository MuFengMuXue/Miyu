# TurboVNC

TurboVNC is a high-performance VNC implementation derived from TightVNC. It provides both VNC server and VNC viewer functionalities. According to the official site, it is better than TigerVNC in multiple aspects https://turbovnc.org/About/TigerVNC.

## Installation
Install the  package.

## Running vncserver
Simply runing  as the normal user that will later use VNC, and you will be prompted to set a password. Then configure which desktop environment to use in . For example, edit the file below as root to use KDE plasma:

You can also use any different file than  with the  option of  to avoid modifying the script provided by the package.
Then run  again to start it, you should see it binds to the port 5901. You should always wrap it in a SSH tunnel as what is done with any other VNC software(see TigerVNC#Accessing vncserver via SSH tunnels).
