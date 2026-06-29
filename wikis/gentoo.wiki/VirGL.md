[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=QEMU/VirGL&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

VirGL is a virtual 3D GPU for use inside [QEMU](https://wiki.gentoo.org/wiki/QEMU "QEMU") virtual machines, that allows the guest operating system to use the capabilities of the host GPU to accelerate 3D rendering.

## Contents

-   [[1] [Host System]](#Host_System)
-   [[2] [Guest System]](#Guest_System)
-   [[3] [See also]](#See_also)
-   [[4] [External resources]](#External_resources)

## [Host System]

On host system [[[app-emulation/qemu]](https://packages.gentoo.org/packages/app-emulation/qemu)[]] should be built with [[[opengl]](https://packages.gentoo.org/useflags/opengl)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] and [[[virgl]](https://packages.gentoo.org/useflags/virgl)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE flags.

When using [[[app-emulation/virt-manager]](https://packages.gentoo.org/packages/app-emulation/virt-manager)[]] Video Device model should be set to Virtio with 3D acceleration box checked.

Spice should be used for Display with Listen type set to None and with OpenGL box checked.

If using `virt-viewer` with multiple displays the above may not work, instead you can try editing the machine XML either via the Virtmanager gui or by `virsh edit` and edit the graphics and video sections to include:

     <graphics type='egl-headless'>
      <gl rendernode='/dev/dri/renderD128'/>
     </graphics>
     <video>
        <model type='virtio' heads='2' primary='yes'>
          <acceleration accel3d='yes'/>
        </model>
     </video>

Replacing `/dev/dri/renderD128` with the path to your video card. Also note that multiple heads only work when the guest is running Wayland.

## [Guest System]

** Important**\
VirGL currently only works with [Linux guests](https://wiki.gentoo.org/wiki/QEMU/Linux_guest "QEMU/Linux guest"). Windows VirGL components for Virtio are work in progress and haven\'t been merged yet

Mesa VirGL driver should be installed on the Guest system. On Gentoo this can be done by setting [VIDEO_CARDS](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Base#VIDEO_CARDS "Handbook:AMD64/Installation/Base") to `"virgl"` and ensuring that [[[media-libs/mesa]](https://packages.gentoo.org/packages/media-libs/mesa)[]] was recompiled with this flag enabled.

To test that everything works properly, the `glxinfo` command from the [[[x11-apps/mesa-progs]](https://packages.gentoo.org/packages/x11-apps/mesa-progs)[]] package can be used.

An example of working output of `glxinfo | grep 'OpenGL render'` is:

` OpenGL renderer string: virgl (Mesa Intel(R) Iris(R) Xe Graphics (RPL-P)) `

## [See also]

-   [QEMU](https://wiki.gentoo.org/wiki/QEMU "QEMU") --- a generic, open-source hardware emulator and virtualization suite.

## [External resources]

-   [https://docs.mesa3d.org/drivers/virgl.html](https://docs.mesa3d.org/drivers/virgl.html)