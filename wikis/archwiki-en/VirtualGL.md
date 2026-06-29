# VirtualGL

VirtualGL redirects an application's OpenGL/GLX commands to a separate X server (that has access to a 3D graphics card), captures the rendered images, and then streams them to the X server that actually handles the application.

The main use-case is to enable server-side hardware-accelerated 3D rendering for remote desktop set-ups where the X server that handles the application is either on the other side of the network (in the case of X11 forwarding), or a "virtual" X server that cannot access the graphics hardware (in the case of VNC).

## Installation and setup
Install the  package, then follow Configuring a Linux or Unix Machine as a VirtualGL Server to configure it. On arch,  is just  and  is .

## Usage
## With X11 forwarding
# "3D" rendering happens here
# "2D" rendering happens here

Advantages of this set-up, compared to using VirtualGL with VNC:

* seamless windows
* uses a little less CPU resources on the server side
* supports stereo rendering (for viewing with "3D glasses")

## Instructions
## Preparation
In addition to setting up VirtualGL on the remote server as described above, this usage scenario requires you to:

* install the  package on the client side as well (but no need to set it up like on the server side, we just need the  and  binaries on this end).
* set up SSH with X11 forwarding (confirm that connecting from the client to the server via  and running GUI applications in the resulting shell works)

## Connecting
Now you can use  on the client computer whenever you want to connect to the server:

 $ vglconnect user@server     # X11 traffic encrypted, VGL image stream unencrypted
 $ vglconnect -s user@server  # both X11 traffic and VGL image stream encrypted

This opens an SSH session with X11 forwarding just like  would, and also automatically starts the VirtualGL Client () with the right parameters as a background daemon. This daemon will handle incoming VirtualGL image streams from the server, and will keep running in the background even after you close the SSH shell - you can stop it with .

## Running applications
Once connected, you can run remote applications with VirtualGL rendering enabled for their OpenGL parts, by starting them inside the SSH shell with  as described in Running Applications below.

You do not need to restrict yourself to the shell that  opened for you; any  or  shell you open from the same X session on the client to the same user@server should work.  will detect that you are in an SSH shell, and make sure that the VGL image stream is sent over the network to the IP/hostname belonging to the SSH client (where the running  instance will intercept and process it).

## With VNC
# "3D" rendering happens here
# "2D" rendering happens here

Advantages of this set-up, compared to using VirtualGL with X11 Forwarding:

* can maintain better performance in case of low-bandwidth/high-latency networks
* can send the same image stream to multiple clients ("desktop sharing")
* the remote application can continue running even when the network connection drops
* better support for non-Linux clients, as the architecture does not depend on a client-side X server

## Instructions
After setting up VirtualGL on the remote server as described above, and establishing a working remote desktop connection using the VNC client/server implementation of your choice, no further configuration should be needed.

Inside the VNC session (e.g. in a terminal emulator within the VNC desktop or even directly in ), simply run selected applications with  as described in Running Applications below.

You can also run your entire session with , so that all opengl applications work by default. For example, if you use xfce, you can run  instead of  in your X startup scripts (,  or equivalent), or copy and edit a .desktop file in /usr/share/xsessions if you are using a display manager.

## Choosing an appropriate VNC package
VirtualGL can provide 3D rendering for any general-purpose vncserver implementation (e.g. TightVNC, RealVNC, ...).

However, if you want to really get good performance out of it (e.g. to make it viable to watch videos or play OpenGL games over VNC), you might want to use one of the VNC implementations that are specifically optimized for this use-case:

* : Developed by the same team as VirtualGL, with the explicit goal of providing the best performance in combination with it. However, its vncserver implementation does not support all features a normal Xorg server provides, thus some applications will run unusually slow or not at all in it.
* TigerVNC: Also developed with VirtualGL in mind and achieves good performance with it, while providing better Xorg compatibility than TurboVNC.

## With Xpra
## On your host
* Setup Xpra and run it manually or automatically by a systemd unit. Remember the specified Xorg display, e.g. .

* Prepare a minimal xinit resource file that just locks your Xorg server's display:

* Start an Xorg server using the prepared resource file . Now,  should return two Xorg instances.

* Run an application via vglrun command specifying the Xorg display used by your Xpra, e.g. . The application will not be visible yet.

## On your client
* Setup Xpra at the client and attach to it. Now you should see the glxspheres64 application started above.

## Running applications
Once you have set up your remote desktop connection with VirtualGL support, you can use  to run selected applications with VirtualGL-accelerated rendering of their OpenGL parts:

 $ vglrun glxgears

This has to be executed on the remote computer of course (where the application will run), i.e. inside your SSH or VNC session. The X servers that will be used, are determined from the following two environment variables:

; : The X server "2)" that will handle the application, and render its non-OpenGL parts. If using VNC, this refers to the VNC server. In the case of SSH forwarding, it is a virtual X server number on the remote computer that SSH internally maps to the real X server on the client. There is nothing VirtualGL-specific about this variable, and it will already be set to the correct value within your SSH or VNC session.
; : The X server "1)" to which VirtualGL should redirect OpenGL rendering. See Installation and setup above. If not set, the value  is assumed. Note that the number after the dot can be used to select the graphics card.

Many more environment variables and command-line parameters are available to fine-tune  - refer to the user manual and  for reference. VirtualGL's behavior furthermore depends on which of its two main modes of operation is active (which  will choose automatically, based on the environment in which it is executed):

* "VGL Transport" - default when using X11 forwarding

: In this mode, a compressed image stream of the rendered OpenGL scenes is sent through a custom network protocol to a  instance. By default it uses JPEG compression at 90% quality, but this can be fully customized, e.g.:

:
:

: There is also a GUI dialog that lets you change the most common VirtualGL rendering/compression options for an application on the fly, after you have already started it with  - simply press  while the application has keyboard focus, to open this dialog.

* "X11 Transport" - default when using VNC

: In this mode, VirtualGL feeds raw (uncompressed) images through the normal X11 protocol directly to the X server that handles the application - e.g. a VNC server running on the same machine. Many of 's command-line options (e.g. those relating to image stream compression or stereo rendering) are not applicable here, because there is no  running on the other end. It is now the VNC server that handles all the image stream optimization/compression, so it is there that you should turn to for fine-tuning.

{{Tip| is actually just a shell script that (temporarily) sets some environment variables before running the requested application - most importantly it adds the libraries that provide all the VirtualGL functionality to . If it better suits your workflow, you could just set those variables yourself instead. The following command lists all environment variables that vglrun would set for your particular set-up:

{{bc|comm -1 -3 {{bc|
$ chmod u+s /usr/lib/lib{rr,dl}faker.so    # for the native-architecture versions provided by
$ chmod u+s /usr/lib32/lib{rr,dl}faker.so  # for the multilib versions provided by
}}
: However, make sure you fully understand the security implications of setuid before deciding to do this in a server environment where security is critical.

* You might need to specify the full path of the VirtualGL libraries
: Open /usr/bin/vglrun and specify the libraries' full path in the LD_PRELOAD variable. Example:

## vglrun fails with ERROR: Could not connect to VGL client.
If your 'client' program is running on the same server as virtualGL (e.g. if you are using virtualGL for VNC), try using .

## Error messages about /etc/opt/VirtualGL/vgl_xauth_key not existing
This means that  is either not being run at all for your virtualGL X server, or that it is being run again by another X server. For me, lightdm was running  on the wrong (vnc remote) X servers, because  adds the following:

Changing it to

so it only runs on the first X server fixed my problem.

## vglrun fails with ERROR: VirtualGL attempted to load the real glXCreatePbuffer function and got the fake one instead.
This means that VirtualGL is trying to load a function from the wrong library. You can specify which OpenGL library to use by setting  to the path of the library.  appears to work for 64-bit applications. Keep in mind that 32-bit applications (like Steam or Wine) will require 32-bit OpenGL. If you need to use both 32-bit and 64-bit libraries, you can load them both with .

## All applications run with 1 frame per second
If you use newer NVIDIA drivers (e.g., version 440) you might be affected by a screen locking problem, which will reduce the framerate to approx. 1 frame per second according to the VirtualGL mailing list. Instead of downgrading the NVIDIA driver one workaround is to set  to  in your X server configuration (see NVIDIA/Troubleshooting#HardDPMS for details).

## rendering glitches, unusually poor performance, or application errors
OpenGL has a really low-level and flexible API, which means that different OpenGL applications may come up with very different rendering techniques. VirtualGL's default strategy for how to redirect rendering and how/when to capture a new frame works well with most interactive 3D programs, but may prove inefficient or even problematic for some applications. If you suspect that this may be the case, you can tweak VirtualGL's mode of operation by setting certain environment variables before starting your application with . For example you could try setting some of the following environment variables (try them one at a time, and be aware that each of them could also make things worse!):

 VGL_ALLOWINDIRECT=1
 VGL_FORCEALPHA=1
 VGL_GLFLUSHTRIGGER=0
 VGL_READBACK=pbo
 VGL_SPOILLAST=0
 VGL_SYNC=1  # use VNC with this one, it is very slow with X11 forwarding

A few OpenGL applications also make strong assumptions about their X server environment or loaded libraries, that may not be fulfilled by a VirtualGL set-up - thus causing those applications to fail. The environment variables , , , ,  can be used to fix this in some cases.

See the "Advanced Configuration" section in the user manual for a proper explanation of all supported environment variables, and the "Application Recipes" section for info on some specific applications that are known to require tweaking to work well with VirtualGL.

## Xpra: vglrun uses rendering device llvmpipe only
You need two Xorg servers running: One that Xpra attaches to, e.g. at display :10. And a second one to do the actual rendering using you graphics card, e.g. your default Xorg server that is run using startx at display :0.
