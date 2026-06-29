[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Remote_desktop&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

This page is a guide to **[remote desktop](https://en.wikipedia.org/wiki/Remote_desktop_software "wikipedia:Remote desktop software")** software on Gentoo.

Remote desktop software is generally used to access a graphical interface running on a distant device (for example over a local network or the Internet) from the machine in front of which the user is present.

There are many different remote desktop applications available, they often offer different features, supported platforms, performance, etc. Which system to chose will usually depend on user requirements.

## Contents

-   [[1] [Remote desktop protocols]](#Remote_desktop_protocols)
    -   [[1.1] [VNC (RFB protocol)]](#VNC_.28RFB_protocol.29)
    -   [[1.2] [RDP]](#RDP)
    -   [[1.3] [SPICE]](#SPICE)
-   [[2] [Available software]](#Available_software)
    -   [[2.1] [Server software]](#Server_software)
    -   [[2.2] [Client software]](#Client_software)
    -   [[2.3] [Screen sharing]](#Screen_sharing)

## [Remote desktop protocols]

A given piece of remote desktop software may be implemented in many ways, but over the years several protocols have gained enough traction to have several remote desktop applications built around them.

The protocol used by a given remote desktop application will often determine much of it\'s functionality. Different applications that use the same protocol will often be compatible.

Here are some examples of remote desktop protocols, each having several packages available on Gentoo:

### [][VNC (RFB protocol)]

[VNC](https://en.wikipedia.org/wiki/VNC "wikipedia:VNC") clients and servers are built around the relatively simple [RFB](https://en.wikipedia.org/wiki/RFB_(protocol) "wikipedia:RFB (protocol)") protocol that exchanges graphical information over the network.

The RFB specification is public and free to use, so is seemingly a good match for open source software.

### [RDP]

[RDP](https://en.wikipedia.org/wiki/Remote_Desktop_Protocol "wikipedia:Remote Desktop Protocol") (Remote Desktop Protocol) is a proprietary protocol owned by Microsoft.

### [SPICE]

The [SPICE](https://en.wikipedia.org/wiki/Simple_Protocol_for_Independent_Computing_Environments "wikipedia:Simple Protocol for Independent Computing Environments") protocol is available under an open-source license, and has a published standard specification.

SPICE is often used to access virtual machines. It has built-in optional security.

## [Available software]

### [Server software]

  --------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------
  Name                                                                                                                        Package                                                                                                                                                                                                                                                                                                                                                                                                                            Protocol
  [X2Go](https://wiki.gentoo.org/index.php?title=X2Go&action=edit&redlink=1 "X2Go (page does not exist)")               [[[net-misc/x2goserver]](https://packages.gentoo.org/packages/net-misc/x2goserver)[]]                                                    NX
  [xrdp](https://wiki.gentoo.org/wiki/Xrdp "Xrdp")                                                                            [[[net-misc/xorgxrdp::dilfridge]](https://gpo.zugaina.org/Overlays/dilfridge/net-misc/xorgxrdp)[]]   RDP
  [Xspice](https://wiki.gentoo.org/index.php?title=Xspice&action=edit&redlink=1 "Xspice (page does not exist)")         [[[x11-drivers/xf86-video-qxl]](https://packages.gentoo.org/packages/x11-drivers/xf86-video-qxl)[]]                               SPICE
  [TigerVNC](https://wiki.gentoo.org/wiki/TigerVNC "TigerVNC")                                                                [[[net-misc/tigervnc]](https://packages.gentoo.org/packages/net-misc/tigervnc)[]]                                                          VNC
  [TurboVNC](https://wiki.gentoo.org/index.php?title=TurboVNC&action=edit&redlink=1 "TurboVNC (page does not exist)")   [[[net-misc/turbovnc]](https://packages.gentoo.org/packages/net-misc/turbovnc)[]]                                                          VNC
  [wayvnc](https://wiki.gentoo.org/index.php?title=Wayvnc&action=edit&redlink=1 "Wayvnc (page does not exist)")         [[[gui-apps/wayvnc]](https://packages.gentoo.org/packages/gui-apps/wayvnc)[]]                                                                VNC
  --------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------

### [Client software]

  ------------------------------------------------------------------------------------------------------------------------------------ --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------
  Name                                                                                                                                 Package                                                                                                                                                                                                                                                                                                                                                                                             Protocol
  [NX Player](https://wiki.gentoo.org/index.php?title=NoMachine_NX&action=edit&redlink=1 "NoMachine NX (page does not exist)")   [[[net-misc/nxplayer]](https://packages.gentoo.org/packages/net-misc/nxplayer)[]]                           NX
  [X2Go](https://wiki.gentoo.org/index.php?title=X2Go&action=edit&redlink=1 "X2Go (page does not exist)")                        [[[net-misc/x2goclient]](https://packages.gentoo.org/packages/net-misc/x2goclient)[]]                     NX
  [FreeRDP](https://wiki.gentoo.org/index.php?title=FreeRDP&action=edit&redlink=1 "FreeRDP (page does not exist)")               [[[net-misc/freerdp]](https://packages.gentoo.org/packages/net-misc/freerdp)[]]                              RDP
  [Spicy](https://wiki.gentoo.org/index.php?title=Spicy&action=edit&redlink=1 "Spicy (page does not exist)")                     [[[net-misc/spice-gtk]](https://packages.gentoo.org/packages/net-misc/spice-gtk)[]]                        SPICE
  [Virt Viewer](https://wiki.gentoo.org/wiki/Virt-manager "Virt-manager")                                                              [[[app-emulation/virt-viewer]](https://packages.gentoo.org/packages/app-emulation/virt-viewer)[]]   SPICE, VNC
  [Remmina](https://wiki.gentoo.org/wiki/Remmina "Remmina")                                                                            [[[net-misc/remmina]](https://packages.gentoo.org/packages/net-misc/remmina)[]]                              RDP, SPICE, VNC
  ------------------------------------------------------------------------------------------------------------------------------------ --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------

### [Screen sharing]

  --------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------
  Name                                                                                                                                                            Package                                                                                                                                                                                                                                                                                                                                                                                                                            Protocol
  [x11vnc](https://wiki.gentoo.org/index.php?title=X11vnc&action=edit&redlink=1 "X11vnc (page does not exist)")                                             [[[x11-misc/x11vnc]](https://packages.gentoo.org/packages/x11-misc/x11vnc)[]]                                                                VNC
  [x2vnc](https://wiki.gentoo.org/index.php?title=X2vnc&action=edit&redlink=1 "X2vnc (page does not exist)")                                                [[[x11-misc/x2vnc]](https://packages.gentoo.org/packages/x11-misc/x2vnc)[]]                                                                   VNC
  [GNOME Remote Desktop](https://wiki.gentoo.org/index.php?title=GNOME_Remote_Desktop&action=edit&redlink=1 "GNOME Remote Desktop (page does not exist)")   [[[net-misc/gnome-remote-desktop]](https://packages.gentoo.org/packages/net-misc/gnome-remote-desktop)[]]                      RDP, VNC
  [TeamViewer](https://wiki.gentoo.org/wiki/TeamViewer "TeamViewer")                                                                                              [[[net-misc/teamviewer]](https://packages.gentoo.org/packages/net-misc/teamviewer)[]]                                                    Proprietary
  [AnyDesk](https://wiki.gentoo.org/wiki/AnyDesk "AnyDesk")                                                                                                       [[[net-misc/anydesk]](https://packages.gentoo.org/packages/net-misc/anydesk)[]]                                                             Proprietary
  [RustDesk](https://wiki.gentoo.org/index.php?title=RustDesk&action=edit&redlink=1 "RustDesk (page does not exist)")                                       [[[net-misc/rustdesk::gentoo-zh]](https://gpo.zugaina.org/Overlays/gentoo-zh/net-misc/rustdesk)[]]
  --------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------