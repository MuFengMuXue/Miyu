## Chapter 35. PRIME Render Offload

PRIME render offload is the ability to have an X screen rendered by one GPU, but choose certain applications within that X screen to be rendered on a different GPU. This is particularly useful in combination with dynamic power management to leave an NVIDIA GPU powered off except when it is needed to render select performance-sensitive applications.

The GPU rendering the majority of the X screen is known as the "sink", and the GPU to which certain application rendering is "offloaded" is known as the "source". The render offload source produces content that is presented on the render offload sink. The NVIDIA driver can function as a PRIME render offload source, to offload rendering of GLX+OpenGL or Vulkan, presenting to an X screen driven by the xf86-video-modesetting X driver.

### X Server Requirements

NVIDIA's PRIME render offload support requires X.Org xserver version 1.20.7 or newer.

### Configure the X Server

On systems with both an integrated GPU and an NVIDIA discrete GPU, the X.Org X server version 1.20.7 and newer will automatically use NVIDIA's PRIME render offload support if the system BIOS is configured to boot on the iGPU and no other explicit configuration files are present. Note that some Linux distributions (such as Ubuntu) may configure the X server differently. Please refer to your distribution's documentation for details.

If GPU screen creation was successful, the log file `/var/log/Xorg.0.log` should contain lines with "NVIDIA(G0)", and querying the RandR providers with `xrandr --listproviders` should display a provider named "NVIDIA-G0" (for "NVIDIA GPU screen 0"). For example:

``` screen
Providers: number : 2
Provider 0: id: 0x221 cap: 0x9, Source Output, Sink Offload crtcs: 3 outputs: 6 associated providers: 0 name:modesetting
Provider 1: id: 0x1f8 cap: 0x0 crtcs: 0 outputs: 0 associated providers: 0 name:NVIDIA-G0
```

### Configure Graphics Applications to Render Using the GPU Screen

To configure a graphics application to be offloaded to the NVIDIA GPU screen, set the environment variable `__NV_PRIME_RENDER_OFFLOAD` to `1`. If the graphics application uses Vulkan or EGL, that should be all that is needed. If the graphics application uses GLX, then also set the environment variable `__GLX_VENDOR_LIBRARY_NAME` to `nvidia`, so that GLVND loads the NVIDIA GLX driver.

Examples:

``` screen
__NV_PRIME_RENDER_OFFLOAD=1 vkcube
__NV_PRIME_RENDER_OFFLOAD=1 __GLX_VENDOR_LIBRARY_NAME=nvidia glxinfo | grep vendor
```

### Finer-Grained Control of Vulkan

The `__NV_PRIME_RENDER_OFFLOAD` environment variable causes the special Vulkan layer `VK_LAYER_NV_optimus` to be loaded. Vulkan applications use the Vulkan API to enumerate the GPUs in the system and select which GPU to use; most Vulkan applications will use the first GPU reported by Vulkan. Newer Vulkan loaders can sort the GPU enumeration to put the preferred GPUs first, based on platform defined criteria. The `VK_LAYER_NV_optimus` layer causes the GPUs to be sorted such that the NVIDIA GPUs are enumerated first if the loader does not do its own sorting. For finer-grained control, the `VK_LAYER_NV_optimus` layer looks at the `__VK_LAYER_NV_optimus` environment variable. The value `NVIDIA_only` causes `VK_LAYER_NV_optimus` to always sort the GPUs so NVIDIA GPUs are enumerated first for the Vulkan application, overriding any Vulkan loader sorting. The value `non_NVIDIA_only` causes `VK_LAYER_NV_optimus` to always sort the GPUs so non-NVIDIA GPUs are enumerated first for to the Vulkan application, overriding any Vulkan loader sorting. Note that the `VK_LAYER_NV_optimus` layer affects the ordering of discrete and integrated GPUs but won't touch CPU devices.

Examples:

``` screen
__NV_PRIME_RENDER_OFFLOAD=1 __VK_LAYER_NV_optimus=NVIDIA_only vkcube
__NV_PRIME_RENDER_OFFLOAD=1 __VK_LAYER_NV_optimus=non_NVIDIA_only vkcube
```

### Finer-Grained Control of OpenGL

For OpenGL with either GLX or EGL, the environment variable `__NV_PRIME_RENDER_OFFLOAD_PROVIDER` provides finer-grained control. While `__NV_PRIME_RENDER_OFFLOAD=1` tells GLX or EGL to use the first NVIDIA GPU screen,`__NV_PRIME_RENDER_OFFLOAD_PROVIDER` can use an RandR provider name to pick a specific NVIDIA GPU screen, using the NVIDIA GPU screen names reported by `xrandr --listproviders`.

Examples:

``` screen
__NV_PRIME_RENDER_OFFLOAD=1 __GLX_VENDOR_LIBRARY_NAME=nvidia glxgears
__NV_PRIME_RENDER_OFFLOAD_PROVIDER=NVIDIA-G0 __GLX_VENDOR_LIBRARY_NAME=nvidia glxgears
__NV_PRIME_RENDER_OFFLOAD=1 eglinfo
__NV_PRIME_RENDER_OFFLOAD_PROVIDER=NVIDIA-G0 eglinfo
```

### Troubleshooting

After starting the X server, verify that the xf86-video-modesetting X driver is using "glamoregl". The log file `/var/log/Xorg.0.log` should contain something like this:

``` screen
[1272173.618] (II) Loading sub module "glamoregl"
[1272173.618] (II) LoadModule: "glamoregl"
[1272173.618] (II) Loading /usr/lib/xorg/modules/libglamoregl.so
[1272173.622] (II) Module glamoregl: vendor="X.Org Foundation"
[1272173.622]   compiled for 1.20.4, module version = 1.0.1
[1272173.622]   ABI class: X.Org ANSI C Emulation, version 0.4
[1272173.638] (II) modeset(0): glamor X acceleration enabled on Mesa DRI Intel(R) HD Graphics 630 (Kaby Lake GT2)
[1272173.638] (II) modeset(0): glamor initialized
```

If glamoregl could not be loaded, the X log may report something like:

``` screen
[1271802.673] (II) Loading sub module "glamoregl"
[1271802.673] (II) LoadModule: "glamoregl"
[1271802.673] (WW) Warning, couldn't open module glamoregl
[1271802.673] (EE) modeset: Failed to load module "glamoregl" (module does not exist, 0)
[1271802.673] (EE) modeset(0): Failed to load glamor module.
```

in which case, consult your distribution's documentation for how to (re-)install the package containing glamoregl.

If the server didn't create a GPU screen automatically, ensure that the nvidia_drm kernel module is loaded. This should normally happen by default, but you can confirm by running `lsmod | grep nvidia_drm` to see if the kernel module is loaded. Run `modprobe nvidia_drm` to load it.

If automatic configuration does not work, it may be necessary to explicitly configure the iGPU and dGPU devices in xorg.conf:

``` screen
    Section "ServerLayout"
      Identifier "layout"
      Screen 0 "iGPU"
    EndSection

    Section "Device"
      Identifier "iGPU"
      Driver "modesetting"
    EndSection

    Section "Screen"
      Identifier "iGPU"
      Device "iGPU"
    EndSection

    Section "Device"
      Identifier "dGPU"
      Driver "nvidia"
    EndSection
```
