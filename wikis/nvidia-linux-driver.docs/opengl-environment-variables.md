## Chapter 11. Specifying OpenGL Environment Variable Settings

### Full scene antialiasing

Antialiasing is a technique used to smooth the edges of objects in a scene to reduce the jagged "stairstep" effect that sometimes appears. By setting the appropriate environment variable, you can enable full-scene antialiasing in any OpenGL application on these GPUs.

Several antialiasing methods are available and you can select between them by setting the \_\_GL_FSAA_MODE environment variable appropriately. Note that increasing the number of samples taken during FSAA rendering may decrease performance.

To see the available values for \_\_GL_FSAA_MODE along with their descriptions, run:

``` screen
    nvidia-settings --query=fsaa --verbose
```

The \_\_GL_FSAA_MODE environment variable uses the same integer values that are used to configure FSAA through nvidia-settings and the NV-CONTROL X extension. In other words, these two commands are equivalent:

``` screen
    export __GL_FSAA_MODE=5

    nvidia-settings --assign FSAA=5
```

Note that there are three FSAA related configuration attributes (FSAA, FSAAAppControlled and FSAAAppEnhanced) which together determine how a GL application will behave. If FSAAAppControlled is 1, the FSAA specified through nvidia-settings will be ignored, in favor of what the application requests through FBConfig selection. If FSAAAppControlled is 0 but FSAAAppEnhanced is 1, then the FSAA value specified through nvidia-settings will only be applied if the application selected a multisample FBConfig.

Therefore, to be completely correct, the nvidia-settings command line to unconditionally assign FSAA should be:

``` screen
    nvidia-settings --assign FSAA=5 --assign FSAAAppControlled=0 --assign FSAAAppEnhanced=0
```

The driver may not be able to support a particular FSAA mode for a given application due to video or system memory limitations. In that case, the driver will silently fall back to a less demanding FSAA mode.

### Fast approximate antialiasing (FXAA)

Fast approximate antialiasing is an antialiasing mode supported by the NVIDIA graphics driver that offers advantages over traditional multisampling and supersampling methods. This mode is incompatible with UBB, triple buffering, and other antialiasing methods. To enable this mode, run:

``` screen
 nvidia-settings --assign FXAA=1
```

nvidia-settings will automatically disable incompatible features when this command is run. Users may wish to disable use of FXAA for individual applications when FXAA is globally enabled. This can be done by setting the environment variable \_\_GL_ALLOW_FXAA_USAGE to 0. \_\_GL_ALLOW_FXAA_USAGE has no effect when FXAA is globally disabled.

### Anisotropic texture filtering

Automatic anisotropic texture filtering can be enabled by setting the environment variable \_\_GL_LOG_MAX_ANISO. The possible values are:

| \_\_GL_LOG_MAX_ANISO | Filtering Type            |
|----------------------|---------------------------|
| 0                    | No anisotropic filtering  |
| 1                    | 2x anisotropic filtering  |
| 2                    | 4x anisotropic filtering  |
| 3                    | 8x anisotropic filtering  |
| 4                    | 16x anisotropic filtering |

### Vblank syncing

The \_\_GL_SYNC_TO_VBLANK (boolean) environment variable can be used to control whether swaps are synchronized to a display device's vertical refresh.

- Setting \_\_GL_SYNC_TO_VBLANK=0 allows glXSwapBuffers to swap without waiting for vblank.

- Setting \_\_GL_SYNC_TO_VBLANK=1 forces glXSwapBuffers to synchronize with the vertical blanking period. This is the default behavior.

When sync to vblank is enabled with TwinView, OpenGL can only sync to one of the display devices; this may cause tearing corruption on the display device to which OpenGL is not syncing. You can use the environment variable \_\_GL_SYNC_DISPLAY_DEVICE to specify which display device should be synchronized to for OpenGL or Vulkan. You should set this environment variable to the name of a display device; for example "CRT-1". Look for the line "Connected display device(s):" in your X log file for a list of the display devices present and their names. You may also find it useful to review [Chapter 12, *Configuring Multiple Display Devices on One X Screen*](configtwinview.html "Chapter 12. Configuring Multiple Display Devices on One X Screen") "Configuring Twinview" and the section on Ensuring Identical Mode Timings in [Chapter 18, *Programming Modes*](programmingmodes.html "Chapter 18. Programming Modes"). This environment variable is only applicable to Vulkan while using either VK_PRESENT_MODE_FIFO_KHR or VK_PRESENT_MODE_FIFO_RELAXED_KHR.

If a display device is being provided by a synchronized RandR 1.4 Output Sink, it will not be listed under "Connected display device(s):", but can still be used with \_\_GL_SYNC_DISPLAY_DEVICE. The names of these display devices can be found using the `xrandr` command line tool. See [Synchronized RandR 1.4 Outputs](randr14.html#randr14sync "Synchronized RandR 1.4 Outputs") for information on synchronized RandR 1.4 Output Sinks.

### Controlling the sorting of OpenGL FBConfigs

The NVIDIA GLX implementation sorts FBConfigs returned by glXChooseFBConfig() as described in the GLX specification. To disable this behavior set \_\_GL_SORT_FBCONFIGS to 0 (zero), then FBConfigs will be returned in the order they were received from the X server. To examine the order in which FBConfigs are returned by the X server run:

``` screen
nvidia-settings --glxinfo
```

This option may be be useful to work around problems in which applications pick an unexpected FBConfig.

### OpenGL yield behavior

There are several cases where the NVIDIA OpenGL driver needs to wait for external state to change before continuing. To avoid consuming too much CPU time in these cases, the driver will sometimes yield so the kernel can schedule other processes to run while the driver waits. For example, when waiting for free space in a command buffer, if the free space has not become available after a certain number of iterations, the driver will yield before it continues to loop.

By default, the driver calls sched_yield() to do this. However, this can cause the calling process to be scheduled out for a relatively long period of time if there are other, same-priority processes competing for time on the CPU. One example of this is when an OpenGL-based composite manager is moving and repainting a window and the X server is trying to update the window as it moves, which are both CPU-intensive operations.

You can use the \_\_GL_YIELD environment variable to work around these scheduling problems. This variable allows the user to specify what the driver should do when it wants to yield. The possible values are:

| \_\_GL_YIELD | Behavior                                             |
|--------------|------------------------------------------------------|
| \<unset\>    | By default, OpenGL will call sched_yield() to yield. |
| "NOTHING"    | OpenGL will never yield.                             |
| "USLEEP"     | OpenGL will call usleep(0) to yield.                 |

### Controlling which OpenGL FBConfigs are available

The NVIDIA GLX implementation will hide FBConfigs that are associated with a 32-bit ARGB visual when the XLIB_SKIP_ARGB_VISUALS environment variable is defined. This matches the behavior of libX11, which will hide those visuals from XGetVisualInfo and XMatchVisualInfo. This environment variable is useful when applications are confused by the presence of these FBConfigs.

### Using Unofficial GLX protocol

By default, the NVIDIA GLX implementation will not expose GLX protocol for GL commands if the protocol is not considered complete. Protocol could be considered incomplete for a number of reasons. The implementation could still be under development and contain known bugs, or the protocol specification itself could be under development or going through review. If users would like to test the client-side portion of such protocol when using indirect rendering, they can set the \_\_GL_ALLOW_UNOFFICIAL_PROTOCOL environment variable to a non-zero value before starting their GLX application. When an NVIDIA GLX server is used, the related X Config option [AllowUnofficialGLXProtocol](xconfigoptions.html#AllowUnofficialGLXProtocol) will need to be set as well to enable support in the server.

### Overriding driver detection of SELinux policy booleans

On Linux, the NVIDIA GLX implementation will attempt to detect whether SELinux is enabled and modify its behavior to respect SELinux policy. By default, the driver adheres to SELinux policy boolean settings at the beginning of a client process's execution; due to shared library limitations, these settings remain fixed throughout the lifetime of the driver instance. Additionally, the driver will adhere to policy boolean settings regardless of whether SELinux is running in permissive mode or enforcing mode. The \_\_GL_SELINUX_BOOLEANS environment variable allows the user to override driver detection of specified SELinux booleans so the driver acts as if these booleans were set or unset. This allows the user, for example, to run the driver under a more restrictive policy than specified by SELinux, or to work around problems when running the driver under SELinux while operating in permissive mode.

\_\_GL_SELINUX_BOOLEANS should be set to a comma-separated list of key/value pairs:

``` screen
 __GL_SELINUX_BOOLEANS="key1=val1,key2=val2,key3=val3,..."
```

Valid keys are any SELinux booleans specified by "getsebool -a", and valid values are 1, true, yes, or on to enable the boolean, and 0, false, no, or off to disable it. There should be no whitespace between any key, value, or delimiter. If this environment variable is set, the driver assumes that SELinux is enabled on the system. Currently, the driver only uses the "allow_execmem" and "deny_execmem" booleans to determine whether it can apply optimizations that use writable, executable memory. Users can explicitly request that these optimizations be turned off by using the \_\_GL_WRITE_TEXT_SECTION environment variable (see [Disabling executable memory optimizations](openglenvvariables.html#disableexecmem "Disabling executable memory optimizations") below). By default, if the driver cannot detect the value of one or both of these booleans, it assumes the most permissive setting (i.e. executable memory is allowed).

### Limiting heap allocations in the OpenGL driver

The NVIDIA OpenGL implementation normally does not enforce limits on dynamic system memory allocations (i.e., memory allocated by the driver from the C library via the malloc(3) memory allocation package). The \_\_GL_HEAP_ALLOC_LIMIT environment variable enables the user to specify a per-process heap allocation limit for as long as libGL is loaded in the application.

\_\_GL_HEAP_ALLOC_LIMIT is specified in the form BYTES SUFFIX, where BYTES is a nonnegative integer and SUFFIX is an optional multiplicative suffix: kB = 1000, k = 1024, MB = 1000\*1000, M = 1024\*1024, GB = 1000\*1000\*1000, and G = 1024\*1024\*1024. SUFFIX is not case-sensitive. For example, to specify a heap allocation limit of 20 megabytes:

``` screen
__GL_HEAP_ALLOC_LIMIT="20 MB"
```

If SUFFIX is not specified, the limit is assumed to be given in bytes. The minimum heap allocation limit is 12 MB. If a lower limit is specified, the limit is clamped to the minimum.

The GNU C library provides several hooks that may be used by applications to modify the behavior of malloc(3), realloc(3), and free(3). In addition, an application or library may specify allocation symbols that the driver will use in place of those exported by libc. Heap allocation tracking is incompatible with these features, and the driver will disable the heap allocation limit if it detects that they are in use.

WARNING: Enforcing a limit on heap allocations may cause unintended behavior and lead to application crashes, data corruption, and system instability. ENABLE AT YOUR OWN RISK.

### OpenGL Shader Disk Cache

The NVIDIA OpenGL driver utilizes a shader disk cache. This optimization benefits some applications, by reusing shader binaries instead of compiling them repeatedly. The related environment variables \_\_GL_SHADER_DISK_CACHE, \_\_GL_SHADER_DISK_CACHE_PATH, and \_\_GL_SHADER_DISK_CACHE_SIZE as well as the GLShaderDiskCache X configuration option, allow fine-grained configuration of the shader cache behavior. The shader disk cache:

1.  is always disabled for indirect rendering

2.  is always disabled for setuid and setgid binaries

3.  by default, is disabled for direct rendering when the OpenGL application is run as the root user

4.  by default, is enabled for direct rendering when the OpenGL application is run as a non-root user

The GLShaderDiskCache X configuration option forcibly enables or disables the shader disk cache, for direct rendering as a non-root user.

The following environment variables configure shader disk cache behavior, and override the GLShaderDiskCache configuration option:

| Environment Variable | Description |
|----|----|
| \_\_GL_SHADER_DISK_CACHE (boolean) | Enables or disables the shader cache for direct rendering. |
| \_\_GL_SHADER_DISK_CACHE_PATH (string) | Enables configuration of where shader caches are stored on disk. |
| \_\_GL_SHADER_DISK_CACHE_SIZE (integer) |   |

If \_\_GL_SHADER_DISK_CACHE_PATH is unset, caches will be stored in \$XDG_CACHE_HOME/nvidia/GLCache/ if XDG_CACHE_HOME is set, or in \$HOME/.cache/nvidia/GLCache/ if HOME is set. If none of the environment variables \_\_GL_SHADER_DISK_CACHE_PATH, XDG_CACHE_HOME, or HOME is set, the shader cache will be disabled. Caches are persistent across runs of an application. Cached shader binaries are specific to each driver version; changing driver versions will cause binaries to be recompiled.

Note that earlier driver versions kept the default caches in \$XDG_CACHE_HOME/.nv/GLCache/ or \$HOME/.nv/GLCache/ instead of \$XDG_CACHE_HOME/nvidia/GLCache/ or \$HOME/.cache/nvidia/GLCache/, respectively. If these earlier locations exist they will be reused instead. It is safe to remove any .nv/GLCache/ directory, after which the driver will populate a fresh cache in the new locations as described in the previous paragraph.

If the default cache is used and \_\_GL_SHADER_DISK_CACHE_SIZE is set locally: any applications that subsequently run without setting it will revert the cache to the default size and cause the cache to be wiped if it now goes over. To increase the cache size globally, \_\_GL_SHADER_DISK_CACHE_SIZE can be set in e.g. $HOME/.bashrc or $HOME/.profile.

### Threaded Optimizations

The NVIDIA OpenGL driver supports offloading its CPU computation to a worker thread. These optimizations typically benefit CPU-intensive applications, but might cause a decrease of performance in applications that heavily rely on synchronous OpenGL calls such as glGet\*. Because of this, they are currently disabled by default.

Setting the \_\_GL_THREADED_OPTIMIZATIONS environment variable to "1" before loading the NVIDIA OpenGL driver library will enable these optimizations for the lifetime of the application.

Please note that these optimizations will only work if the target application dynamically links against pthreads. If this isn't the case, the dynamic loader can be instructed to do so at runtime by setting the LD_PRELOAD environment variable to include the pthreads library.

Additionally, these optimizations require Xlib to function in thread-safe mode. The NVIDIA OpenGL driver cannot reliably enable Xlib thread-safe mode itself, therefore the application needs to call XInitThreads() before making any other Xlib call. Otherwise, the threaded optimizations in the NVIDIA driver will not be enabled.

### Conformant glBlitFramebuffer() scissor test behavior

This option enables the glBlitFramebuffer() scissor test, which must be enabled for glBlitFramebuffer() to behave in a conformant manner. Setting the \_\_GL_ConformantBlitFramebufferScissor environment variable to 0 disables the glBlitFramebuffer() scissor test, and setting it to 1 enables it. By default, the glBlitFramebuffer() scissor test is enabled.

Some applications have bugs which cause them to not display properly with a conformant glBlitFramebuffer(). See [Chapter 9, *Known Issues*](knownissues.html "Chapter 9. Known Issues") for more details.

### G-SYNC

When a G-SYNC or G-SYNC Compatible monitor is attached, and G-SYNC or G-SYNC Compatible mode was allowed when the mode was set, this option controls whether these “variable refresh rate”, or VRR, features can be used. Setting the \_\_GL_VRR_ALLOWED environment variable to 0 disables VRR flipping for the application on any G-SYNC or G-SYNC Compatible monitors. Setting the \_\_GL_VRR_ALLOWED environment variable to 1 has no effect on non-VRR monitors, or monitors that disallowed G-SYNC or G-SYNC Compatible mode when the mode was set.

When G-SYNC is active on a G-SYNC or G-SYNC Compatible display and \_\_GL_SYNC_TO_VBLANK is disabled, applications rendering faster than the maximum refresh rate will tear. This eliminates tearing for frame rates below the monitor's maximum refresh rate while minimizing latency for frame rates above it. When \_\_GL_SYNC_TO_VBLANK is enabled, the frame rate is limited to the monitor's maximum refresh rate to eliminate tearing completely. When a G-SYNC Compatible display is in use, applications rendering slower than the minimum refresh rate may tear when \_\_GL_SYNC_TO_VBLANK is disabled, and their swaps may not complete until the next vblank when \_\_GL_SYNC_TO_VBLANK is enabled.

G-SYNC and G-SYNC Compatible mode cannot be used when workstation stereo or workstation overlays are enabled, or when there is more than one X screen.

### Disabling executable memory optimizations

By default, the NVIDIA driver will attempt to use optimizations which rely on being able to write to executable memory. This may cause problems in certain system configurations (e.g., on SELinux when the "allow_execmem" boolean is disabled or "deny_execmem" boolean is enabled, and on grsecurity kernels configured with CONFIG_PAX_MPROTECT). When possible, the driver will attempt to detect when it is running on an unsupported configuration and disable these optimizations automatically. If the \_\_GL_WRITE_TEXT_SECTION environment variable is set to 0, the driver will unconditionally disable these optimizations.

### Ignoring GLSL (OpenGL Shading Language) extension checks

Some applications may use GLSL shaders that reference global variables defined only in an OpenGL extension without including a corresponding \#extension directive in their source code. Additionally, some applications may use GLSL shaders version 150 or greater that reference global variables defined in a compatibility profile, without specifying that a compatibility profile should be used in their \#version directive. Setting the \_\_GL_IGNORE_GLSL_EXT_REQS environment variable to 1 will cause the driver to ignore this class of errors, which may allow these shaders to successfully compile.

### Showing the Graphics API Visual Indicator

The \_\_GL_SHOW_GRAPHICS_OSD (boolean) environment variable can be used to control whether the graphics API visual indicator is rendered on top of OpenGL and Vulkan applications.

This indicator displays various information such as the graphics API in use, instantaneous frame rate, whether the application is synced to vblank, and whether the application is blitting or flipping.

### Image Sharpening

The \_\_GL_SHARPEN_ENABLE environment variable can be used to enable image sharpening for OpenGL and Vulkan applications. Setting \_\_GL_SHARPEN_ENABLE=1 enables image sharpening, while setting \_\_GL_SHARPEN_ENABLE=0 (default) disables image sharpening. The amount of sharpening can be controlled by setting the \_\_GL_SHARPEN_VALUE environment variable to a value between 0 and 100, with 0 being no sharpening, 100 being maximum sharpening, and 50 being the default. The amount of denoising done on the sharpened image can be controlled with the \_\_GL_SHARPEN_IGNORE_FILM_GRAIN environment variable, with 0 being no denoising, 100 being maximum denoising, and 17 being the default.
