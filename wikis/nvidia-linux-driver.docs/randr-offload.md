## Chapter 34. Offloading Graphics Display with RandR 1.4

Version 1.4 of the X Resize, Rotate, and Reflect Extension (RandR 1.4 for short) adds a way for drivers to work together so that one graphics device can display images rendered by another.

### System Requirements

- For displaying NVIDIA GPU desktop contents on a screen connected to another graphics device, X.Org X server version 1.13 or higher.

- For displaying another graphics device's desktop contents on a screen connected to an NVIDIA GPU, X.Org X server version 1.20.7 or higher. X server version 1.20.6 is also supported using [`Option "AllowPRIMEDisplayOffloadSink" "boolean"`](xconfigoptions.html#AllowPRIMEDisplayOffloadSink).

- A Linux kernel, version 3.13 or higher, with CONFIG_DRM enabled.

- Version 1.4.0 of the xrandr command-line utility.

### Using the NVIDIA Driver as an RandR 1.4 Output Source or Output Sink Provider

To use the NVIDIA driver as an RandR 1.4 output source provider, also known as “PRIME”, the X server needs to be configured to use the NVIDIA driver for its primary screen and to use the “modesetting” driver for the other graphics device. This can be achieved by placing the following in `/etc/X11/xorg.conf`:

``` screen
Section "ServerLayout"
    Identifier "layout"
    Screen 0 "nvidia"
    Inactive "intel"
EndSection

Section "Device"
    Identifier "nvidia"
    Driver "nvidia"
    BusID "<BusID for NVIDIA device here>"
EndSection

Section "Screen"
    Identifier "nvidia"
    Device "nvidia"
    Option "AllowEmptyInitialConfiguration"
EndSection

Section "Device"
    Identifier "intel"
    Driver "modesetting"
EndSection

Section "Screen"
    Identifier "intel"
    Device "intel"
EndSection
```

To use the NVIDIA driver as an RandR 1.4 output sink provider, also known as “Reverse PRIME”, the X server needs to be configured to use the “modesetting” driver for its primary screen and to use the NVIDIA driver for the other graphics device. This can be achieved by placing the following in `/etc/X11/xorg.conf`:

``` screen
Section "ServerLayout"
    Identifier "layout"
    Screen 0 "intel"
    Inactive "nvidia"
    Option "AllowNVIDIAGPUScreens"
EndSection

Section "Device"
    Identifier "intel"
    Driver "modesetting"
    BusID "<BusID for Intel device here>"
EndSection

Section "Screen"
    Identifier "intel"
    Device "intel"
EndSection

Section "Device"
    Identifier "nvidia"
    Driver "nvidia"
EndSection

Section "Screen"
    Identifier "nvidia"
    Device "nvidia"
EndSection
```

When using the NVIDIA driver as a “Reverse PRIME” RandR 1.4 output sink provider combined with an application being run via [Chapter 35, *PRIME Render Offload*](primerenderoffload.html "Chapter 35. PRIME Render Offload"), an optimization known as “Reverse PRIME Bypass” may be used, bypassing the bandwidth overhead of both PRIME Render Offload and PRIME Display Offload. In order for Reverse PRIME Bypass to be used, a PRIME Render Offload application must be unredirected, fullscreen, and visible only on a single NVIDIA-driven PRIME Display Offload output. Usage of Reverse PRIME Bypass is printed to the X log when verbose logging is enabled in the X server.

If an NVIDIA Reverse PRIME output is the sole display in the system then special conditions apply. That configuration is supported if the NVIDIA driver version is 495.46 or later and the X.Org X server version is newer than 21.1.3. Failing these conditions the NVIDIA Reverse PRIME output will not be synchronized to the native refresh rate of the NVIDIA graphics card in which case X.Org will revert the display to a default rate of 1 frame per second.

Note that at the time of writing the latest X.Org X server is 21.1.3 so there is no official X.Org release yet where this configuration is supported. For maintainers of Linux distributions and others who are willing to compile the X.Org X server locally, please cherry-pick this Git commit to support the configuration: https://gitlab.freedesktop.org/xorg/xserver/-/commit/69774044716039fa70655b3bc6dd6a4ff4535cfd. The commit already lives in the branch where the next X.Org X server release after 21.1.3 will come from.

See [“What is the format of a PCI Bus ID?”](faq.html#busid) for information on determining the appropriate BusID string for your graphics card.

The nvidia-xconfig(1) utility can be used to update the X configuration file for using the NVIDIA driver as an output source provider.

``` screen
$ nvidia-xconfig --prime
```

See the nvidia-xconfig(1) man page for details.

The X server does not automatically enable displays attached using the output sink in this configuration. To do that, use the `xrandr` command line tool.

For NVIDIA as an output source:

``` screen
$ xrandr --setprovideroutputsource modesetting NVIDIA-0
$ xrandr --auto
```

For NVIDIA as an output sink:

``` screen
$ xrandr --setprovideroutputsource NVIDIA-G0 modesetting
$ xrandr --auto
```

This pair of commands can be added to your X session startup scripts, for example by putting them in `$HOME/.xinitrc` before running `startx`.

Use the

``` screen
$ xrandr --listproviders
```

command to query the capabilities of the graphics devices. If the system requirements are met and the X server is configured correctly, there should be a provider named `NVIDIA-0` or `NVIDIA-G0` with the `Source Output` or `Sink Output` capability, respectively, and one named `modesetting` with the `Sink Output` and/or `Source Output` capabilities. If either provider is missing or doesn't have the expected capability, check your system configuration.

### Synchronized RandR 1.4 Outputs

When running against X.Org X server with video driver ABI 23 or higher, synchronization is supported with compatible drivers. At the time of writing, synchronization is compatible with the “modesetting” driver with Intel devices on Linux version 4.5 or newer. If all requirements are met, synchronization will be used automatically.

X.Org X server version 1.19 or newer is required to support synchronization. Without synchronization, displays are prone to “tearing”. See [Caveats](randr14.html#caveats "Caveats") for details.

If synchronization is being used but is not desired, it can be disabled with:

``` screen
$ xrandr --output <output> --set "PRIME Synchronization" 0
```

and re-enabled with:

``` screen
$ xrandr --output <output> --set "PRIME Synchronization" 1
```

See [Vblank syncing](openglenvvariables.html#vblanksyncing "Vblank syncing") for information on how OpenGL applications can synchronize with sink-provided outputs.

### Caveats

- Support for PRIME Synchronization relies on DRM KMS support. See [Chapter 36, *Direct Rendering Manager Kernel Modesetting (DRM KMS)*](kms.html "Chapter 36. Direct Rendering Manager Kernel Modesetting (DRM KMS)") for more information.

- Some Intel i915 DRM driver versions, such as that included with Linux 4.5, have a bug where drmModeMoveCursor() and drmModePageFlip() interfere with each other, resulting in only one occurring per frame. If choppy performance is observed in configurations using PRIME Synchronization and i915, it is suggested to add `Option "SWCursor"` to Intel's device section in xorg.conf. The bug appears to be fixed as of Linux 4.6.

- When running against X.Org X server version 1.18.x or lower, there is no synchronization between the images rendered by the NVIDIA GPU and the output device. This means that the output device can start reading the next frame of video while it is still being updated, producing a graphical artifact known as “tearing”. Tearing is expected due to limitations in the design of the X.Org X server prior to video driver ABI 23.

- NVIDIA's implementation of PRIME requires support for DRM render nodes, a feature first merged in Linux 3.12. However, the feature was not enabled by default until Linux 3.17. To enable it on earlier supported kernels, specify the `drm.rnodes=1` kernel boot parameter.

- PRIME Synchronization is compatible with xf86-video-amdgpu as an output sink. xf86-video-amdgpu implements a separate interface for PRIME Synchronization that the RandR layer of the X server does not recognize. As a result, X will print "randr: falling back to unsynchronized pixmap sharing", despite the fact that PRIME is synchronized. Additionally, the "PRIME Synchronization" output property will not function to disable PRIME Synchronization when set to 0.

- The NVIDIA driver only exposes the `Output Sink` capability by default on X server version 1.20.7 or later, but can be used without issue on X server version 1.20.6 with `Option "AllowPRIMEDisplayOffloadSink"`. See [`Option "AllowPRIMEDisplayOffloadSink" "boolean"`](xconfigoptions.html#AllowPRIMEDisplayOffloadSink) for more information.

- The NVIDIA driver requires DRM KMS support to operate as an output sink when the output source driver is either NVIDIA or AMDGPU. See [Chapter 36, *Direct Rendering Manager Kernel Modesetting (DRM KMS)*](kms.html "Chapter 36. Direct Rendering Manager Kernel Modesetting (DRM KMS)") for more information.
