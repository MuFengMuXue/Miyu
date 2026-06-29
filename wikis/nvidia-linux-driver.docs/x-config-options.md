## Appendix B. X Config Options

The following driver options are supported by the NVIDIA X driver. They may be specified either in the Screen or Device sections of the X config file.

**X Config Options**

`Option "Accel" "boolean"`
Controls whether the X driver uses the GPU for graphics processing. Disabling acceleration is useful when another component, such as CUDA, requires exclusive use of the GPU's processing cores. Performance of the X server will be reduced when acceleration is disabled, and some features may not be available.

OpenGL and VDPAU are not supported when Accel is disabled.

When this option is set for an X screen, it will be applied to all X screens running on the same GPU.

Default: acceleration is enabled.

`Option "RenderAccel" "boolean"`
Enable or disable hardware acceleration of the RENDER extension. Default: hardware acceleration of the RENDER extension is enabled.

`Option "NoRenderExtension" "boolean"`
Disable the RENDER extension. Other than recompiling it, the X server does not seem to have another way of disabling this. Fortunately, we can control this from the driver so we export this option. This is useful in depth 8 where RENDER would normally steal most of the default colormap. Default: RENDER is offered when possible.

`Option "UBB" "boolean"`
Enable or disable the Unified Back Buffer on NVIDIA RTX/Quadro-based GPUs (Quadro NVS excluded); see [Chapter 19, *Configuring Flipping and UBB*](flippingubb.html "Chapter 19. Configuring Flipping and UBB") for a description of UBB. This option has no effect on non-NVIDIA RTX/Quadro GPU products. Default: UBB is on for NVIDIA RTX/Quadro GPUs.

`Option "NoFlip" "boolean"`
Disable OpenGL flipping; see [Chapter 19, *Configuring Flipping and UBB*](flippingubb.html "Chapter 19. Configuring Flipping and UBB") for a description. Default: OpenGL will swap by flipping when possible.

`Option "GLShaderDiskCache" "boolean"`
This option controls whether the OpenGL driver will utilize a disk cache to save and reuse compiled shaders. See the description of the \_\_GL_SHADER_DISK_CACHE and \_\_GL_SHADER_DISK_CACHE_PATH environment variables in [Chapter 11, *Specifying OpenGL Environment Variable Settings*](openglenvvariables.html "Chapter 11. Specifying OpenGL Environment Variable Settings") for more details.

`Option "Overlay" "boolean"`
Enables RGB workstation overlay visuals. This is only supported on NVIDIA RTX/Quadro GPUs (Quadro NVS GPUs excluded) in depth 24. This option causes the server to advertise the SERVER_OVERLAY_VISUALS root window property and GLX will report single- and double-buffered, Z-buffered 16-bit overlay visuals. The transparency key is pixel 0x0000 (hex). There is no gamma correction support in the overlay plane. RGB workstation overlays are not supported when the Composite extension is enabled.

UBB must be enabled when overlays are enabled (this is the default behavior).

`Option "CIOverlay" "boolean"`
Enables Color Index workstation overlay visuals with identical restrictions to Option "Overlay" above. This option causes the server to advertise the SERVER_OVERLAY_VISUALS root window property. Some of the visuals advertised that way may be listed in the main plane (layer 0) for compatibility purposes. They however belong to the overlay (layer 1). The server will offer visuals both with and without a transparency key. These are depth 8 PseudoColor visuals. Color Index workstation overlays are not supported when the Composite extension is enabled. Default: off.

UBB must be enabled when overlays are enabled (this is the default behavior).

`Option "TransparentIndex" "integer"`
When color index overlays are enabled, use this option to choose which pixel is used for the transparent pixel in visuals featuring transparent pixels. This value is clamped between 0 and 255 (Note: some applications such as Alias's Maya require this to be zero in order to work correctly). Default: 0.

`Option "OverlayDefaultVisual" "boolean"`
When overlays are used, this option sets the default visual to an overlay visual thereby putting the root window in the overlay. This option is not recommended for RGB overlays. Default: off.

`Option "EmulatedOverlaysTimerMs" "integer"`
Enables the use of a timer within the X server to perform the updates to the emulated overlay or CI overlay. This option can be used to improve the performance of the emulated or CI overlays by reducing the frequency of the updates. The value specified indicates the desired number of milliseconds between overlay updates. To disable the use of the timer either leave the option unset or set it to 0. Default: off.

`Option "EmulatedOverlaysThreshold" "boolean"`
Enables the use of a threshold within the X server to perform the updates to the emulated overlay or CI overlay. The emulated or CI overlay updates can be deferred but this threshold will limit the number of deferred OpenGL updates allowed before the overlay is updated. This option can be used to trade off performance and animation quality. Default: on.

`Option "EmulatedOverlaysThresholdValue" "integer"`
Controls the threshold used in updating the emulated or CI overlays. This is used in conjunction with the EmulatedOverlaysThreshold option to trade off performance and animation quality. Higher values for this option favor performance over quality. Setting low values of this option will not cause the overlay to be updated more often than the frequence specified by the EmulatedOverlaysTimerMs option. Default: 5.

`Option "SWCursor" "boolean"`
Enable or disable software rendering of the X cursor. Default: off.

`Option "HWCursor" "boolean"`
Enable or disable hardware rendering of the X cursor. Default: on.

`Option "ConnectedMonitor" "string"`
Allows you to override what the NVIDIA kernel module detects is connected to your graphics card. This may be useful, for example, if you use a KVM (keyboard, video, mouse) switch and you are switched away when X is started. It may also be useful in situations where you wish to simulate the presence of a monitor when none are connected. When simulating the presence of a monitor, it may be useful to combine this option with the "CustomEDID" option to provide the simulated display device with an EDID.

Valid values for this option are "CRT" (cathode ray tube) or "DFP" (digital flat panel); if using multiple display devices, this option may be a comma-separated list of display devices; e.g.: "CRT, CRT" or "CRT, DFP". The display device name used in this option may also include a numeric suffix (e.g., "DFP-1") to refer to a specific display connector; check your X log to determine which display device identifiers are valid for your particular GPU.

It is generally recommended to not use this option, but instead use the "UseDisplayDevice" option.

NOTE: anything attached to a 15 pin VGA connector is regarded by the driver as a CRT. "DFP" should only be used to refer to digital flat panels connected via DVI, HDMI, or DisplayPort.

When this option is set for an X screen, it will be applied to all X screens running on the same GPU.

Default: string is NULL (the NVIDIA driver will detect the connected display devices).

`Option "UseDisplayDevice" "string"`
The "UseDisplayDevice" X configuration option is a list of one or more display devices, which limits the display devices the NVIDIA X driver will consider for an X screen. The display device names used in the option may be either specific (with a numeric suffix; e.g., "DFP-1") or general (without a numeric suffix; e.g., "DFP").

When assigning display devices to X screens, the NVIDIA X driver walks through the list of all (not already assigned) display devices detected as connected. When the "UseDisplayDevice" X configuration option is specified, the X driver will only consider connected display devices which are also included in the "UseDisplayDevice" list. This can be thought of as a "mask" against the connected (and not already assigned) display devices.

Note the subtle difference between this option and the "ConnectedMonitor" option: the "ConnectedMonitor" option overrides which display devices are actually detected, while the "UseDisplayDevice" option controls which of the detected display devices will be used on this X screen.

Of the list of display devices considered for this X screen (either all connected display devices, or a subset limited by the "UseDisplayDevice" option), the NVIDIA X driver first looks at CRTs, then at DFPs. For example, if both a CRT and a DFP are connected, by default the X driver would assign the CRT to this X screen. However, by specifying:

``` screen
    Option "UseDisplayDevice" "DFP"
```

the X screen would use the DFP instead. Or, if CRT-0, DFP-0, and DFP-1 are connected, the X driver would assign CRT-0 and DFP-0 to the X screen. However, by specifying:

``` screen
    Option "UseDisplayDevice" "CRT-0, DFP-1"
```

the X screen would use CRT-0 and DFP-1 instead.

Additionally, the special value "none" can be specified for the "UseDisplayDevice" option. When this value is given, any programming of the display hardware is disabled. The NVIDIA driver will not perform any mode validation or mode setting for this X screen. This is intended for use in conjunction with CUDA or in remote graphics solutions such as VNC or Hewlett Packard's Remote Graphics Software (RGS); however, note that this configuration option may not interact well with some desktop environments or window managers (See [“My remote desktop software doesn't work when no displays are attached.”](commonproblems.html#headlessremotedesktop) for more information).

"UseDisplayDevice" defaults to "none" on GPUs that have no display capabilities, such as some Tesla GPUs and some mobile GPUs used in Optimus notebook configurations.

Note the following restrictions for setting the "UseDisplayDevice" to "none":

- OpenGL SyncToVBlank will have no effect.

- None of Stereo, Overlay, CIOverlay, or SLI are allowed when "UseDisplayDevice" is set to "none".

`Option "UseEdidFreqs" "boolean"`
This option controls whether the NVIDIA X driver will use the HorizSync and VertRefresh ranges given in a display device's EDID, if any. When UseEdidFreqs is set to True, EDID-provided range information will override the HorizSync and VertRefresh ranges specified in the Monitor section. If a display device does not provide an EDID, or the EDID does not specify an hsync or vrefresh range, then the X server will default to the HorizSync and VertRefresh ranges specified in the Monitor section of your X config file. These frequency ranges are used when validating modes for your display device.

Default: True (EDID frequencies will be used)

`Option "UseEDID" "boolean"`
By default, the NVIDIA X driver makes use of a display device's EDID, when available, during construction of its mode pool. The EDID is used as a source for possible modes, for valid frequency ranges, and for collecting data on the physical dimensions of the display device for computing the DPI (see [Appendix E, *Dots Per Inch*](dpi.html "Appendix E. Dots Per Inch")). However, if you wish to disable the driver's use of the EDID, you can set this option to False:

``` screen
    Option "UseEDID" "FALSE"
```

Note that, rather than globally disable all uses of the EDID, you can individually disable each particular use of the EDID; e.g.,

``` screen
    Option "UseEDIDFreqs" "FALSE"
    Option "UseEDIDDpi" "FALSE"
    Option "ModeValidation" "NoEdidModes"
```

When this option is set for an X screen, it will be applied to all X screens running on the same GPU.

Default: True (use EDID).

`Option "MetaModeOrientation" "string"`
Controls the default relationship between display devices when using multiple display devices on a single X screen. Takes one of the following values: "RightOf" "LeftOf" "Above" "Below" "SamePositionAs". For backwards compatibility, "TwinViewOrientation" is a synonym for "MetaModeOrientation", and "Clone" is a synonym for "SamePositionAs". See [Chapter 12, *Configuring Multiple Display Devices on One X Screen*](configtwinview.html "Chapter 12. Configuring Multiple Display Devices on One X Screen") for details. Default: string is NULL.

`Option "MetaModes" "string"`
This option describes the combination of modes to use on each monitor. See [Chapter 12, *Configuring Multiple Display Devices on One X Screen*](configtwinview.html "Chapter 12. Configuring Multiple Display Devices on One X Screen") and [Chapter 31, *Configuring SLI Mosaic*](sli.html "Chapter 31. Configuring SLI Mosaic") for details. Default: string is NULL.

`Option "nvidiaXineramaInfo" "boolean"`
The NVIDIA X driver normally provides a Xinerama extension that X clients (such as window managers) can use to discover the current layout of display devices within an X screen. Some window mangers get confused by this information, so this option is provided to disable this behavior. Default: true (NVIDIA Xinerama information is provided).

On X servers with RandR 1.2 support, the X server's RandR implementation may provide its own Xinerama implementation if NVIDIA Xinerama information is not provided. So, on X servers with RandR 1.2, disabling "nvidiaXineramaInfo" causes the NVIDIA X driver to still register its Xinerama implementation but report a single screen-sized region. On X servers without RandR 1.2 support, disabling "nvidiaXineramaInfo" causes the NVIDIA X driver to not register its Xinerama implementation.

For backwards compatibility, "NoTwinViewXineramaInfo" is a synonym for disabling "nvidiaXineramaInfo".

`Option "nvidiaXineramaInfoOrder" "string"`
When the NVIDIA X driver provides nvidiaXineramaInfo (see the nvidiaXineramaInfo X config option), it by default reports the currently enabled display devices in the order "CRT, DFP". The nvidiaXineramaInfoOrder X config option can be used to override this order.

The option string is a comma-separated list of display device names. The display device names can either be general (e.g, "CRT", which identifies all CRTs), or specific (e.g., "CRT-1", which identifies a particular CRT). Not all display devices need to be identified in the option string; display devices that are not listed will be implicitly appended to the end of the list, in their default order.

Note that nvidiaXineramaInfoOrder tracks all display devices that could possibly be connected to the GPU, not just the ones that are currently enabled. When reporting the Xinerama information, the NVIDIA X driver walks through the display devices in the order specified, only reporting enabled display devices.

Some high-resolution "tiled" monitors are represented internally as multiple display devices. These will be combined by default into a single Xinerama screen. The position of the device in nvidiaXineramaInfoOrder corresponding to the top-left tile will determine when the screen will be reported.

Examples:

``` screen
        "DFP"
        "DFP-1, DFP-0, CRT"
```

In the first example, any enabled DFPs would be reported first (any enabled CRTs would be reported afterwards). In the second example, if DFP-1 were enabled, it would be reported first, then DFP-0, and then any enabled CRTs; finally, any other enabled DFPs would be reported.

For backwards compatibility, "TwinViewXineramaInfoOrder" is a synonym for "nvidiaXineramaInfoOrder".

Default: "CRT, DFP"

`Option "nvidiaXineramaInfoOverride" "string"`
This option overrides the values reported by the NVIDIA X driver's nvidiaXineramaInfo implementation. This disregards the actual display devices used by the X screen and any order specified in nvidiaXineramaInfoOrder.

The option string is interpreted as a comma-separated list of regions, specified as '\[width\]x\[height\]+\[x-offset\]+\[y-offset\]'. The regions' sizes and offsets are not validated against the X screen size, but are directly reported to any Xinerama client.

Examples:

``` screen
        "1600x1200+0+0, 1600x1200+1600+0"
        "1024x768+0+0, 1024x768+1024+0, 1024x768+0+768, 1024x768+1024+768"
```

For backwards compatibility, "TwinViewXineramaInfoOverride" is a synonym for "nvidiaXineramaInfoOverride".

`Option "Stereo" "integer"`
Enable offering of quad-buffered stereo visuals on NVIDIA RTX/Quadro. Integer indicates the type of stereo equipment being used:

| Value | Equipment |
|----|----|
| 3 | Onboard stereo support. This is usually only found on professional cards. The glasses connect via a DIN connector on the back of the graphics card. |
| 4 | One-eye-per-display passive stereo. This mode allows each display to be configured to statically display either left or right eye content. This can be especially useful with multi-display configurations (TwinView or SLI Mosaic). For example, this is commonly used in conjunction with special projectors to produce 2 polarized images which are then viewed with polarized glasses. To use this stereo mode, it is recommended that you configure TwinView (or pairs of displays in SLI Mosaic) in clone mode with the same resolution, panning offset, and panning domains on each display. See [MetaModes](configtwinview.html#metamodes) for more information about configuring multiple displays. |
| 5 | Vertical interlaced stereo mode, for use with SeeReal Stereo Digital Flat Panels. |
| 6 | Color interleaved stereo mode, for use with Sharp3D Stereo Digital Flat Panels. |
| 7 | Horizontal interlaced stereo mode, for use with Arisawa, Hyundai, Zalman, Pavione, and Miracube Digital Flat Panels. |
| 8 | Checkerboard pattern stereo mode, for use with 3D DLP Display Devices. |
| 9 | Inverse checkerboard pattern stereo mode, for use with 3D DLP Display Devices. |
| 10 | NVIDIA 3D Vision mode for use with NVIDIA 3D Vision glasses. The NVIDIA 3D Vision infrared emitter must be connected to a USB port of your computer, and to the 3-pin DIN connector of an NVIDIA RTX/Quadro graphics board before starting the X server. Hot-plugging the USB infrared stereo emitter is not yet supported. Also, 3D Vision Stereo Linux support requires a Linux kernel built with USB device filesystem (usbfs) and USB 2.0 support. Not presently supported on FreeBSD or Solaris. |
| 11 | NVIDIA 3D VisionPro mode for use with NVIDIA 3D VisionPro glasses. The NVIDIA 3D VisionPro RF hub must be connected to a USB port of your computer, and to the 3-pin DIN connector of an NVIDIA RTX/Quadro graphics board before starting the X server. Hot-plugging the USB RF hub is not yet supported. Also, 3D VisionPro Stereo Linux support requires a Linux kernel built with USB device filesystem (usbfs) and USB 2.0 support. When RF hub is connected and X is started in NVIDIA 3D VisionPro stereo mode, a new page will be available in nvidia-settings for various configuration settings. Some of these settings can also be done via nvidia-settings command line interface. Refer to the corresponding Help section in nvidia-settings for further details. Not presently supported on FreeBSD or Solaris. |
| 12 | HDMI 3D mode for use with HDMI 3D compatible display devices with their own stereo emitters. |
| 13 | Tridelity SL stereo mode, for use with Tridelity SL display devices. |
| 14 | Generic active stereo with in-band DisplayPort stereo signaling, for use with DisplayPort display devices with their own stereo emitters. See the documentation for the "InbandStereoSignaling" X config option for more details. |

Default: 0 (Stereo is not enabled).

Stereo options 3, 10, 11, 12, and 14 are known as "active" stereo. Other options are known as "passive" stereo.

When active stereo is used with multiple display devices, it is recommended that modes within each MetaMode have identical timing values (modelines). See [Chapter 18, *Programming Modes*](programmingmodes.html "Chapter 18. Programming Modes") for suggestions on making sure the modes within your MetaModes are identical.

The following table summarizes the available stereo modes, their supported GPUs, and their intended display devices:

| Stereo mode (value) | Graphics card supported \[1\] | Display supported |
|----|----|----|
| Onboard DIN (3) | NVIDIA RTX/Quadro graphics cards | Displays with high refresh rate |
| One-eye-per-display (4) | NVIDIA RTX/Quadro graphics cards | Any |
| Vertical Interlaced (5) | NVIDIA RTX/Quadro graphics cards | SeeReal Stereo DFP |
| Color Interleaved (6) | NVIDIA RTX/Quadro graphics cards | Sharp3D stereo DFP |
| Horizontal Interlaced (7) | NVIDIA RTX/Quadro graphics cards | Arisawa, Hyundai, Zalman, Pavione, and Miracube |
| Checkerboard Pattern (8) | NVIDIA RTX/Quadro graphics cards | 3D DLP display devices |
| Inverse Checkerboard (9) | NVIDIA RTX/Quadro graphics cards | 3D DLP display devices |
| NVIDIA 3D Vision (10) | NVIDIA RTX/Quadro graphics cards \[2\] | Supported 3D Vision ready displays \[3\] |
| NVIDIA 3D VisionPro (11) | NVIDIA RTX/Quadro graphics cards \[2\] | Supported 3D Vision ready displays \[3\] |
| HDMI 3D (12) | NVIDIA RTX/Quadro graphics cards | Supported HDMI 3D displays \[4\] |
| Tridelity SL (13) | NVIDIA RTX/Quadro graphics cards | Tridelity SL DFP |
| Generic active stereo (in-band DP) (14) | NVIDIA RTX/Quadro graphics cards | DisplayPort displays with in-band stereo support |
|   |   |   |

|  |
|----|
| \[1\] NVIDIA RTX/Quadro graphics cards excluding Quadro NVS cards. |
| \[2\] http://www.nvidia.com/object/quadro_pro_graphics_boards_linux.html |
| \[3\] http://www.nvidia.com/object/3D_Vision_Requirements.html |
| \[4\] Supported 3D TVs, Projectors, and Home Theater Receivers listed on http://www.nvidia.com/object/3dtv-play-system-requirements.html and Desktop LCD Monitors with 3D Vision HDMI support listed on http://www.nvidia.com/object/3D_Vision_Requirements.html |

UBB must be enabled when stereo is enabled (this is the default behavior).

Active stereo can be enabled on digital display devices (connected via DVI, HDMI, or DisplayPort). However, some digital display devices might not behave as desired with active stereo:

- Some digital display devices may not be able to toggle pixel colors quickly enough when flipping between eyes on every vblank.

- Some digital display devices may have an optical polarization that interferes with stereo goggles.

- Active stereo requires high refresh rates, because a vertical refresh is needed to display each eye. Some digital display devices have a low refresh rate, which will result in flickering when used for active stereo.

- Some digital display devices might internally convert from other refresh rates to their native refresh rate (e.g., 60Hz), resulting in incompatible rates between the stereo glasses and stereo displayed on screen.

These limitations do not apply to any display devices suitable for stereo options 10, 11, or 12.

Interlaced modes are disabled when active stereo is enabled.

Stereo option 12 (HDMI 3D) is also known as HDMI Frame Packed Stereo mode, where the left and right eye images are stacked into a single frame with a doubled pixel clock and refresh rate. This doubled refresh rate is used for Frame Lock and in refresh rate queries through NV-CONTROL clients, and the doubled pixel clock and refresh rate are used in mode validation. Interlaced modes are not supported with this stereo mode. The following nvidia-settings command line can be used to determine whether a display's current mode is an HDMI 3D mode with a doubled refresh rate:

``` screen
    nvidia-settings --query=Hdmi3D
```

Stereo applies to an entire X screen, so it will apply to all display devices on that X screen, whether or not they all support the selected Stereo mode.

`Option "ForceStereoFlipping" "boolean"`
Stereo flipping is the process by which left and right eyes are displayed on alternating vertical refreshes. Normally, stereo flipping is only performed when a stereo drawable is visible. This option forces stereo flipping even when no stereo drawables are visible.

This is to be used in conjunction with the "Stereo" option. If "Stereo" is 0, the "ForceStereoFlipping" option has no effect. If otherwise, the "ForceStereoFlipping" option will force the behavior indicated by the "Stereo" option, even if no stereo drawables are visible. This option is useful in a multiple-screen environment in which a stereo application is run on a different screen than the stereo master.

Possible values:

| Value | Behavior |
|----|----|
| 0 | Stereo flipping is not forced. The default behavior as indicated by the "Stereo" option is used. |
| 1 | Stereo flipping is forced. Stereo is running even if no stereo drawables are visible. The stereo mode depends on the value of the "Stereo" option. |

Default: 0 (Stereo flipping is not forced).

`Option "XineramaStereoFlipping" "boolean"`
By default, when using Stereo with Xinerama, all physical X screens having a visible stereo drawable will stereo flip. Use this option to allow only one physical X screen to stereo flip at a time.

This is to be used in conjunction with the "Stereo" and "Xinerama" options. If "Stereo" is 0 or "Xinerama" is 0, the "XineramaStereoFlipping" option has no effect.

If you wish to have all X screens stereo flip all the time, see the "ForceStereoFlipping" option.

Possible values:

| Value | Behavior |
|----|----|
| 0 | Stereo flipping is enabled on one X screen at a time. Stereo is enabled on the first X screen having the stereo drawable. |
| 1 | Stereo flipping in enabled on all X screens. |

Default: 1 (Stereo flipping is enabled on all X screens).

`Option "MultisampleCompatibility" "boolean"`
Enable or disable the use of separate front and back multisample buffers. Enabling this will consume more memory but is necessary for correct output when rendering to both the front and back buffers of a multisample or FSAA drawable. This option is necessary for correct operation of SoftImage XSI. Default: false (a single multisample buffer is shared between the front and back buffers).

`Option "NoPowerConnectorCheck" "boolean"`
The NVIDIA X driver will fail initialization on a GPU if it detects that the GPU that requires an external power connector does not have an external power connector plugged in. This option can be used to bypass this test.

When this option is set for an X screen, it will be applied to all X screens running on the same GPU.

Default: false (the power connector test is performed).

`Option "ThermalConfigurationCheck" "boolean"`
The NVIDIA X driver will fail initialization on a GPU if it detects that the GPU has a bad thermal configuration. This may indicate a problem with how your graphics board was built, or simply a driver bug. It is recommended that you contact your graphics board vendor if you encounter this problem.

When this option is set for an X screen, it will be applied to all X screens running on the same GPU.

This option can be set to False to bypass this test. Default: true (the thermal configuration test is performed).

`Option "DamageEvents" "boolean"`
Use OS-level events to efficiently notify X when a client has performed direct rendering to a window that needs to be composited. This will significantly improve performance and interactivity when using GLX applications with a composite manager running. It will also affect applications using GLX when rotation is enabled. Enabled by default.

`Option "ExactModeTimingsDVI" "boolean"`
Forces the initialization of the X server with the exact timings specified in the ModeLine. Default: false (for DVI devices, the X server initializes with the closest mode in the EDID list).

The "AllowNonEdidModes" token in the "ModeValidation" X configuration option has the same effect as "ExactModeTimingsDVI", but "AllowNonEdidModes" has per-display device granularity.

`Option "Coolbits" "integer"`
Enables various unsupported features, such as support for GPU clock manipulation in the NV-CONTROL X extension. This option accepts a bit mask of features to enable.

WARNING: this may cause system damage and void warranties. This utility can run your computer system out of the manufacturer's design specifications, including, but not limited to: higher system voltages, above normal temperatures, excessive frequencies, and changes to BIOS that may corrupt the BIOS. Your computer's operating system may hang and result in data loss or corrupted images. Depending on the manufacturer of your computer system, the computer system, hardware and software warranties may be voided, and you may not receive any further manufacturer support. NVIDIA does not provide customer service support for the Coolbits option. It is for these reasons that absolutely no warranty or guarantee is either express or implied. Before enabling and using, you should determine the suitability of the utility for your intended use, and you shall assume all responsibility in connection therewith.

When "8" (Bit 3) is set in the "Coolbits" option value, the PowerMizer page in the nvidia-settings control panel will display a table that allows setting per-clock domain and per-performance level offsets to apply to clock values. This is allowed on certain GeForce GPUs. Not all clock domains or performance levels may be modified. On GPUs based on the Pascal architecture the offset is applied to all performance levels.

When "16" (Bit 4) is set in the "Coolbits" option value, the nvidia-settings command line interface allows setting GPU overvoltage. This is allowed on certain GeForce GPUs.

When this option is set for an X screen, it will be applied to all X screens running on the same GPU.

The default for this option is 0 (unsupported features are disabled).

`Option "SLI" "string"`
This option controls the configuration of SLI rendering in supported configurations.

| Value | Behavior |
|----|----|
| 0, no, off, false, Single | Use only a single GPU when rendering |
| Mosaic | Enable SLI and use SLI Mosaic Mode. Use this in conjunction with the MetaModes X configuration option to specify the combination of mode(s) used on each display. |

`Option "TripleBuffer" "boolean"`
Enable or disable the use of triple buffering. If this option is enabled, OpenGL windows that sync to vblank and are double-buffered will be given a third buffer. This decreases the time an application stalls while waiting for vblank events, but increases latency slightly (delay between user input and displayed result).

`Option "DPI" "string"`
This option specifies the Dots Per Inch for the X screen; for example:

``` screen
    Option "DPI" "75 x 85"
```

will set the horizontal DPI to 75 and the vertical DPI to 85. By default, the X driver will compute the DPI of the X screen from the EDID of any connected display devices. See [Appendix E, *Dots Per Inch*](dpi.html "Appendix E. Dots Per Inch") for details. Default: string is NULL (disabled).

`Option "UseEdidDpi" "string"`
By default, the NVIDIA X driver computes the DPI of an X screen based on the physical size of the display device, as reported in the EDID, and the size in pixels of the first mode to be used on the display device. If multiple display devices are used by the X screen, then the NVIDIA X screen will choose which display device to use. This option can be used to specify which display device to use. The string argument can be a display device name, such as:

``` screen
    Option "UseEdidDpi" "DFP-0"
```

or the argument can be "FALSE" to disable use of EDID-based DPI calculations:

``` screen
    Option "UseEdidDpi" "FALSE"
```

See [Appendix E, *Dots Per Inch*](dpi.html "Appendix E. Dots Per Inch") for details. Default: string is NULL (the driver computes the DPI from the EDID of a display device and selects the display device).

`Option "ConstantDPI" "boolean"`
By default on X.Org 6.9 or newer, the NVIDIA X driver recomputes the size in millimeters of the X screen whenever the size in pixels of the X screen is changed using XRandR, such that the DPI remains constant.

This behavior can be disabled (which means that the size in millimeters will not change when the size in pixels of the X screen changes) by setting the "ConstantDPI" option to "FALSE"; e.g.,

``` screen
    Option "ConstantDPI" "FALSE"
```

ConstantDPI defaults to True.

On X releases older than X.Org 6.9, the NVIDIA X driver cannot change the size in millimeters of the X screen. Therefore the DPI of the X screen will change when XRandR changes the size in pixels of the X screen. The driver will behave as if ConstantDPI was forced to FALSE.

`Option "CustomEDID" "string"`
This option forces the X driver to use the EDID specified in a file rather than the display's EDID. You may specify a semicolon separated list of display names and filename pairs. Valid display device names include "CRT-0", "CRT-1", "DFP-0", "DFP-1", "TV-0", "TV-1", or one of the generic names "CRT", "DFP", "TV", which apply the EDID to all devices of the specified type. Additionally, if SLI Mosaic is enabled, this name can be prefixed by a GPU name (e.g., "GPU-0.CRT-0"). The file contains a raw EDID (e.g., a file generated by nvidia-settings).

For example:

``` screen
    Option "CustomEDID" "CRT-0:/tmp/edid1.bin; DFP-0:/tmp/edid2.bin"
```

will assign the EDID from the file /tmp/edid1.bin to the display device CRT-0, and the EDID from the file /tmp/edid2.bin to the display device DFP-0. Note that a display device name must always be specified even if only one EDID is specified.

Caution: Specifying an EDID that doesn't exactly match your display may damage your hardware, as it allows the driver to specify timings beyond the capabilities of your display. Use with care.

When this option is set for an X screen, it will be applied to all X screens running on the same GPU.

`Option "IgnoreEDIDChecksum" "string"`
This option forces the X driver to accept an EDID even if the checksum is invalid. You may specify a comma separated list of display names. Valid display device names include "CRT-0", "CRT-1", "DFP-0", "DFP-1", "TV-0", "TV-1", or one of the generic names "CRT", "DFP", "TV", which ignore the EDID checksum on all devices of the specified type. Additionally, if SLI Mosaic is enabled, this name can be prefixed by a GPU name (e.g., "GPU-0.CRT-0").

For example:

``` screen
    Option "IgnoreEDIDChecksum" "CRT, DFP-0"
```

will cause the nvidia driver to ignore the EDID checksum for all CRT monitors and the displays DFP-0 and TV-0.

Caution: An invalid EDID checksum may indicate a corrupt EDID. A corrupt EDID may have mode timings beyond the capabilities of your display, and using it could damage your hardware. Use with care.

When this option is set for an X screen, it will be applied to all X screens running on the same GPU.

`Option "ModeValidation" "string"`
This option provides fine-grained control over each stage of the mode validation pipeline, disabling individual mode validation checks. This option should only very rarely be used.

The option string is a semicolon-separated list of comma-separated lists of mode validation arguments. Each list of mode validation arguments can optionally be prepended with a display device name and GPU specifier.

``` screen
    "<dpy-0>: <tok>, <tok>; <dpy-1>: <tok>, <tok>, <tok>; ..."
```

Possible arguments:

- "NoMaxPClkCheck": each mode has a pixel clock; this pixel clock is validated against the maximum pixel clock of the hardware (for a DFP, this is the maximum pixel clock of the TMDS encoder, for a CRT, this is the maximum pixel clock of the DAC). This argument disables the maximum pixel clock checking stage of the mode validation pipeline.

- "NoEdidMaxPClkCheck": a display device's EDID can specify the maximum pixel clock that the display device supports; a mode's pixel clock is validated against this pixel clock maximum. This argument disables this stage of the mode validation pipeline.

- "NoMaxSizeCheck": each NVIDIA GPU has a maximum resolution that it can drive; this argument disables this stage of the mode validation pipeline.

- "NoHorizSyncCheck": a mode's horizontal sync is validated against the range of valid horizontal sync values; this argument disables this stage of the mode validation pipeline.

- "NoVertRefreshCheck": a mode's vertical refresh rate is validated against the range of valid vertical refresh rate values; this argument disables this stage of the mode validation pipeline.

- "NoVirtualSizeCheck": if the X configuration file requests a specific virtual screen size, a mode cannot be larger than that virtual size; this argument disables this stage of the mode validation pipeline.

- "NoVesaModes": when constructing the mode pool for a display device, the X driver uses a built-in list of VESA modes as one of the mode sources; this argument disables use of these built-in VESA modes.

- "NoEdidModes": when constructing the mode pool for a display device, the X driver uses any modes listed in the display device's EDID as one of the mode sources; this argument disables use of EDID-specified modes.

- "NoXServerModes": when constructing the mode pool for a display device, the X driver uses the built-in modes provided by the core Xorg X server as one of the mode sources; this argument disables use of these modes. Note that this argument does not disable custom ModeLines specified in the X config file; see the "NoCustomModes" argument for that.

- "NoCustomModes": when constructing the mode pool for a display device, the X driver uses custom ModeLines specified in the X config file (through the "Mode" or "ModeLine" entries in the Monitor Section) as one of the mode sources; this argument disables use of these modes.

- "NoPredefinedModes": when constructing the mode pool for a display device, the X driver uses additional modes predefined by the NVIDIA X driver; this argument disables use of these modes.

- "NoUserModes": additional modes can be added to the mode pool dynamically, using the NV-CONTROL X extension; this argument prohibits user-specified modes via the NV-CONTROL X extension.

- "NoExtendedGpuCapabilitiesCheck": allow mode timings that may exceed the GPU's extended capability checks.

- "ObeyEdidContradictions": an EDID may contradict itself by listing a mode as supported, but the mode may exceed an EDID-specified valid frequency range (HorizSync, VertRefresh, or maximum pixel clock). Normally, the NVIDIA X driver prints a warning in this scenario, but does not invalidate an EDID-specified mode just because it exceeds an EDID-specified valid frequency range. However, the "ObeyEdidContradictions" argument instructs the NVIDIA X driver to invalidate these modes.

- "NoTotalSizeCheck": allow modes in which the individual visible or sync pulse timings exceed the total raster size.

- "NoDualLinkDVICheck": for mode timings used on dual link DVI DFPs, the driver must perform additional checks to ensure that the correct pixels are sent on the correct link. For some of these checks, the driver will invalidate the mode timings; for other checks, the driver will implicitly modify the mode timings to meet the GPU's dual link DVI requirements. This token disables this dual link DVI checking.

- "NoDisplayPortBandwidthCheck": for mode timings used on DisplayPort devices, the driver must verify that the DisplayPort link can be configured to carry enough bandwidth to support a given mode's pixel clock. For example, some DisplayPort-to-VGA adapters only support 2 DisplayPort lanes, limiting the resolutions they can display. This token disables this DisplayPort bandwidth check.

- "AllowNon3DVisionModes": modes that are not optimized for NVIDIA 3D Vision are invalidated, by default, when 3D Vision (stereo mode 10) or 3D Vision Pro (stereo mode 11) is enabled. This token allows the use of non-3D Vision modes on a 3D Vision monitor. (Stereo behavior of non-3D Vision modes on 3D Vision monitors is undefined.)

- "AllowNonHDMI3DModes": modes that are incompatible with HDMI 3D are invalidated, by default, when HDMI 3D (stereo mode 12) is enabled. This token allows the use of non-HDMI 3D modes when HDMI 3D is selected. HDMI 3D will be disabled when a non-HDMI 3D mode is in use.

- "AllowNonEdidModes": if a mode is not listed in a display device's EDID mode list, then the NVIDIA X driver will discard the mode if the EDID 1.3 "GTF Supported" flag is unset, if the EDID 1.4 "Continuous Frequency" flag is unset, or if the display device is connected to the GPU by a digital protocol (e.g., DVI, DP, etc). This token disables these checks for non-EDID modes.

- "NoEdidHDMI2Check": HDMI 2.0 adds support for 4K@60Hz modes with either full RGB 4:4:4 pixel encoding or YUV (also known as YCbCr) 4:2:0 pixel encoding. Using these modes with RGB 4:4:4 pixel encoding requires GPU support as well as display support indicated in the display device's EDID. This token allows the use of these modes at RGB 4:4:4 as long as the GPU supports them, even if the display device's EDID does not indicate support. Otherwise, these modes will be displayed in the YUV 4:2:0 color space.

- "AllowDpInterlaced": When driving interlaced modes over DisplayPort protocol, NVIDIA GPUs do not provide all the spec-mandated metadata. Some DisplayPort monitors are tolerant of this missing metadata. But, in the interest of DisplayPort specification compliance, the NVIDIA driver prohibits interlaced modes over DisplayPort protocol by default. Use this mode validation token to allow interlaced modes over DisplayPort protocol anyway.

- "NoInterlacedModes": Use this mode validation token to prohibit interlaced modes.

- "MaxOneHardwareHead": The display hardware of the GPU has a pipeline that produces the images that are sent to each display device. One unit within this pipeline is the "head", which generates the mode timings for the display device. Some extremely high pixel clock mode timings, such as 8K @ 60Hz, exceed the capabilities of a single head. On Turing and later GPUs, the NVIDIA GPU driver can use multiple heads within the GPU to produce the mode timings for one of these display devices; the driver will do so implicitly when needed. In the "Display Device Information" pages within nvidia-settings, this case will be indicated by reporting "Number of Hardware Heads Used" as "2" rather than "1". However, NVIDIA GPUs have a total of four hardware heads. Using two of them to drive one high pixel clock display device will mean that there are only two available to drive other display devices in the desktop (thus, the GPU may only be able to drive a total of three display devices if one of them requires the use of two hardware heads, or the GPU may only be able to drive a total of two display devices if each of them requires the use of two hardware heads). Set the "MaxOneHardwareHead" ModeValidation token to force the driver to use at most one hardware head to drive the display device, falling back to a lower refresh rate or resolution, if necessary.

  Note that the ability to use two hardware heads to drive one display device requires hardware support only available in Turing and later GPUs. Also, the use of two hardware heads with one display device is not currently compatible with RTX PRO Sync.

- "PreferHDMIFrlMode": Fixed Rate Link (FRL) is a high-bandwidth data transmission mode introduced in HDMI 2.1, as an alternative to Transition-Minimized Differential Signaling (TMDS). Normally, HDMI defaults to TMDS, unless the needed bandwidth of the mode requires FRL. Use this token to prefer the use of FRL, if possible, regardless of the mode's needed bandwidth.

Examples:

``` screen
    Option "ModeValidation" "NoMaxPClkCheck"
```

disable the maximum pixel clock check when validating modes on all display devices.

``` screen
    Option "ModeValidation" "CRT-0: NoEdidModes, NoMaxPClkCheck; GPU-0.DFP-0: NoVesaModes"
```

do not use EDID modes and do not perform the maximum pixel clock check on CRT-0, and do not use VESA modes on DFP-0 of GPU-0.

`Option "ColorSpace" "string"`
This option sets the preferred color space for all or a subset of the connected flat panels.

The option string is a semicolon-separated list of device specific options. Each option can optionally be prepended with a display device name and a GPU specifier.

``` screen
    "<dpy-0>: <tok>; <dpy-1>: <tok>; ..."
```

Possible arguments:

- "RGB": sets color space to RGB. RGB color space supports two valid color ranges; full and limited. By default, full color range is set when the color space is RGB.

- "YCbCr444": sets color space to YCbCr 4:4:4. YCbCr supports only limited color range. It is not possible to set this color space if the GPU or display is not capable of limited range.

If the ColorSpace option is not specified, or is incorrectly specified, then the color space is set to RGB by default. If driving the current mode in the RGB 4:4:4 color space would require a pixel clock that exceeds the display's or GPU's capabilities, and the display and GPU are capable of driving that mode in the YCbCr 4:2:0 color space, then the color space will be overridden to YCbCr 4:2:0. The current actual color space in use on the display can be queried with the following nvidia-settings command line:

``` screen
    nvidia-settings --query=CurrentColorSpace
```

Examples:

``` screen
    Option "ColorSpace" "YCbCr444"
```

set the color space to YCbCr 4:4:4 on all flat panels.

``` screen
    Option "ColorSpace" "GPU-0.DFP-0: YCbCr444"
```

set the color space to YCbCr 4:4:4 on DFP-0 of GPU-0.

`Option "ColorRange" "string"`
This option sets the preferred color range for all or a subset of the connected flat panels.

The option string is a semicolon-separated list of device specific options. Each option can optionally be prepended with a display device name and a GPU specifier.

``` screen
    "<dpy-0>: <tok>; <dpy-1>: <tok>; ..."
```

Either full or limited color range may be selected as the preferred color range. The actual color range depends on the current color space, and will be overridden to limited color range if the current color space requires it. The current actual color range in use on the display can be queried with the following nvidia-settings command line:

``` screen
    nvidia-settings --query=CurrentColorRange
```

Possible arguments:

- "Full": sets color range to full range. By default, full color range is set when the color space is RGB.

- "Limited": sets color range to limited range. YCbCr444 supports only limited color range. Consequently, limited range is selected by the driver when color space is set to YCbCr444, and can not be changed.

If the ColorRange option is not specified, or is incorrectly specified, then an appropriate default value is selected based on the selected color space.

Examples:

``` screen
    Option "ColorRange" "Limited"
```

set the color range to limited on all flat panels.

``` screen
    Option "ColorRange" "GPU-0.DFP-0: Limited"
```

set the color range to limited on DFP-0 of GPU-0.

`Option "ModeDebug" "boolean"`
This option causes the X driver to print verbose details about mode validation to the X log file. Note that this option is applied globally: setting this option to TRUE will enable verbose mode validation logging for all NVIDIA X screens in the X server.

`Option "FlatPanelProperties" "string"`
This option requests particular properties for all or a subset of the connected flat panels.

The option string is a semicolon-separated list of comma-separated property=value pairs. Each list of property=value pairs can optionally be prepended with a flat panel name and GPU specifier.

``` screen
    "<DFP-0>: <property=value>, <property=value>; <DFP-1>: <property=value>; ..."
```

Recognized properties:

- "Dithering": controls the flat panel dithering configuration; possible values are: 'Auto' (the driver will decide when to dither), 'Enabled' (the driver will always dither, if possible), and 'Disabled' (the driver will never dither).

- "DitheringMode": controls the flat panel dithering mode; possible values are: 'Auto' (the driver will choose possible default mode), 'Dynamic-2x2' (a 2x2 dithering pattern is updated for every frame), 'Static-2x2' (a 2x2 dithering pattern remains constant throughout the frames), and 'Temporal' (a pseudo-random dithering algorithm is used).

Examples:

``` screen
    Option "FlatPanelProperties" "DitheringMode = Static-2x2"
```

set the flat panel dithering mode to Static-2x2 on all flat panels.

``` screen
    Option "FlatPanelProperties" "GPU-0.DFP-0: Dithering = Disabled; DFP-1: Dithering = Enabled, DitheringMode = Static-2x2"
```

set dithering to disabled on DFP-0 on GPU-0, set DFP-1's dithering to enabled and dithering mode to static 2x2.

`Option "ProbeAllGpus" "boolean"`
When the NVIDIA X driver initializes, it probes all GPUs in the system, even if no X screens are configured on them. This is done so that the X driver can report information about all the system's GPUs through the NV-CONTROL X extension. This option can be set to FALSE to disable this behavior, such that only GPUs with X screens configured on them will be probed.

Note that disabling this option may affect configurability through nvidia-settings, since the X driver will not know about GPUs that aren't currently being used or the display devices attached to them.

Default: all GPUs in the system are probed.

`Option "IncludeImplicitMetaModes" "boolean"`
When the X server starts, a mode pool is created per display device, containing all the mode timings that the NVIDIA X driver determined to be valid for the display device. However, the only MetaModes that are made available to the X server are the ones explicitly requested in the X configuration file.

It is convenient for fullscreen applications to be able to change between the modes in the mode pool, even if a given target mode was not explicitly requested in the X configuration file.

To facilitate this, the NVIDIA X driver will implicitly add MetaModes for all modes in the primary display device's mode pool. This makes all the modes in the mode pool available to full screen applications that use the XF86VidMode extension or RandR 1.0/1.1 requests.

Further, to make sure that fullscreen applications have a reasonable set of MetaModes available to them, the NVIDIA X driver will also add implicit MetaModes for common resolutions: 1920x1200, 1920x1080, 1600x1200, 1280x1024, 1280x720, 1024x768, 800x600, 640x480. For these common resolution implicit MetaModes, the common resolution will be the ViewPortIn, and nvidia-auto-select will be the mode. The ViewPortOut will be configured such that the ViewPortIn is aspect scaled within the mode. Each common resolution implicit MetaMode will be added if there is not already a MetaMode with that resolution, and if the resolution is not larger than the nvidia-auto-select mode of the display device. See [MetaModes](configtwinview.html#metamodes) for details of the relationship between ViewPortIn, ViewPortOut, and the mode within a MetaMode.

The IncludeImplicitMetaModes X configuration option can be used to disable the addition of implicit MetaModes. Or, it can be used to alter how implicit MetaModes are added. The option can have either a boolean value or a comma-separated list of token=value pairs, where the possible tokens are:

- "DisplayDevice": specifies the display device for which the implicit MetaModes should be created. Any name that can be used to identify a display device can be used here; see [Appendix C, *Display Device Names*](displaydevicenames.html "Appendix C. Display Device Names") for details.

- "Mode": specifies the name of the mode to use with the common resolution-based implicit MetaModes. The default is "nvidia-auto-select". Any mode in the display device's mode pool can be used here.

- "Scaling": specifies how the ViewPortOut should be configured between the ViewPortIn and the mode for the common resolution-based implicit MetaModes. Possible values are "Scaled", "Aspect-Scaled", or "Centered". The default is "Aspect-Scaled".

- "UseModePool": specifies whether modes from the display device's mode pool should be used to create implicit MetaModes. The default is "true".

- "UseCommonResolutions": specifies whether the common resolution list should be used to create implicit MetaModes. The default is "true".

- "Derive16x9Mode": specifies whether to create an implicit MetaMode with a resolution whose aspect ratio is 16:9, using the width of nvidia-auto-select. E.g., using a 2560x1600 monitor, this would create an implicit MetaMode of 2560x1440. The default is "true".

- "ExtraResolutions": a comma-separated list of additional resolutions to use for creating implicit MetaModes. These will be created in the same way as the common resolution implicit MetaModes: the resolution will be used as the ViewPortIn, the nvidia-auto-select mode will be used as the mode, and the ViewPortOut will be computed to aspect scale the resolution within the mode. Note that the list of resolutions must be enclosed in parentheses, so that the commas are not interpreted as token=value pair separators.

Some examples:

``` screen
Option "IncludeImplicitMetaModes" "off"
Option "IncludeImplicitMetaModes" "on" (the default)
Option "IncludeImplicitMetaModes" "DisplayDevice = DVI-I-2, Scaling=Aspect-Scaled, UseModePool = false"
Option "IncludeImplicitMetaModes" "ExtraResolutions = ( 2560x1440, 320x200 ), DisplayDevice = DVI-I-0"
```

`Option "AllowSHMPixmaps" "boolean"`
This option controls whether applications can use the MIT-SHM X extension to create pixmaps whose contents are shared between the X server and the client. These pixmaps prevent the NVIDIA driver from performing a number of optimizations and degrade performance in many circumstances.

Disabling this option disables only shared memory pixmaps. Applications can still use the MIT-SHM extension to transfer data to the X server through shared memory using XShmPutImage.

Default: off (shared memory pixmaps are not allowed).

`Option "SoftwareRenderCacheSize" "boolean"`
This option controls the size of a cache in system memory used to accelerate software rendering. The size is specified in bytes, but may be rounded or capped based on inherent limits of the cache.

Default: 0x800000 (8 Megabytes).

`Option "AllowIndirectGLXProtocol" "boolean"`
There are two ways that GLX applications can render on an X screen: direct and indirect. Direct rendering is generally faster and more featureful, but indirect rendering may be used in more configurations. Direct rendering requires that the application be running on the same machine as the X server, and that the OpenGL library have sufficient permissions to access the kernel driver. Indirect rendering works with remote X11 connections as well as unprivileged clients like those in a chroot with no access to device nodes.

For those who wish to disable the use of indirect GLX protocol on a given X screen, setting the "AllowIndirectGLXProtocol" to a true value will cause GLX CreateContext requests with the `direct` parameter set to `False` to fail with a BadValue error.

Starting with X.Org server 1.16, there are also command-line switches to enable or disable use of indirect GLX contexts. `-iglx` disables use of indirect GLX protocol, and `+iglx` enables use of indirect GLX protocol. +iglx is the default in server 1.16. -iglx is the default in server 1.17 and newer.

The NVIDIA GLX implementation will prohibit creation of indirect GLX contexts if the AllowIndirectGLXProtocol option is set to False, or the -iglx switch was passed to the X server (X.Org server 1.16 or higher), or the X server defaulted to '-iglx'.

Default: enabled (indirect protocol is allowed, unless disabled by the server).

`Option "AllowUnofficialGLXProtocol" "boolean"`
By default, the NVIDIA GLX implementation will not expose GLX protocol for GL commands if the protocol is not considered complete. Protocol could be considered incomplete for a number of reasons. The implementation could still be under development and contain known bugs, or the protocol specification itself could be under development or going through review. If users would like to test the server-side portion of such protocol when using indirect rendering, they can enable this option. If any X screen enables this option, it will enable protocol on all screens in the server.

When an NVIDIA GLX client is used, the related environment variable [\_\_GL_ALLOW_UNOFFICIAL_PROTOCOL](openglenvvariables.html#unofficialprotoenv) will need to be set as well to enable support in the client.

`Option "PanAllDisplays" "boolean"`
When this option is enabled, all displays in the current MetaMode will pan as the pointer is moved. If disabled, only the displays whose panning domain contains the pointer (at its new location) are panned.

Default: enabled (all displays are panned when the pointer is moved).

`Option "Interactive" "boolean"`
This option controls the behavior of the driver's watchdog, which attempts to detect and terminate GPU programs that get stuck, in order to ensure that the GPU remains available for other processes. GPU compute applications, however, often have long-running GPU programs, and killing them would be undesirable. If you are using GPU compute applications and they are getting prematurely terminated, try turning this option off.

When this option is set for an X screen, it will be applied to all X screens running on the same GPU.

Default: on. The driver will attempt to detect and terminate GPU programs that cause excessive delays for other processes using the GPU.

`Option "BaseMosaic" "boolean"`
This option can be used to extend a single X screen transparently across display outputs on each GPU. This is like SLI Mosaic mode except that it does not require a video bridge or nvlink bridge connected to the graphics cards. Due to this Base Mosaic does not guarantee there will be no tearing between the display boundaries.

Use this in conjunction with the MetaModes X configuration option to specify the combination of mode(s) used on each display. nvidia-xconfig can be used to configure Base Mosaic via a command like **nvidia-xconfig --base-mosaic --metamodes=METAMODES** where the METAMODES string specifies the desired grid configuration. For example, to configure four DFPs in a 2x2 configuration, each running at 1920x1024, with two DFPs connected to two cards, the command would be:

``` screen
    nvidia-xconfig --base-mosaic --metamodes="GPU-0.DFP-0: 1920x1024+0+0, GPU-0.DFP-1: 1920x1024+1920+0, GPU-1.DFP-0: 1920x1024+0+1024, GPU-1.DFP-1: 1920x1024+1920+1024"
```

`Option "ConstrainCursor" "boolean"`
When this option is enabled, the mouse cursor will be constrained to the region of the desktop that is visible within the union of all displays' panning domains in the current MetaMode. When it is disabled, it may be possible to move the cursor to regions of the X screen that are not visible on any display.

Note that if this would make a display's panning domain inaccessible (in other words, if the union of all panning domains is disjoint), then the cursor will not be constrained.

This option has no effect if the X server doesn't support cursor constraint. This support was added in X.Org server version 1.10.

Default: on, if the X server supports it. The cursor will be constrained to the panning domain of each monitor, when possible.

`Option "UseHotplugEvents" "boolean"`
When this option is enabled, the NVIDIA X driver will generate RandR display changed events when displays are plugged into or unplugged from an NVIDIA GPU. Some desktop environments will listen for these events and dynamically reconfigure the desktop when displays are added or removed.

Disabling this option suppresses the generation of these RandR events for non-DisplayPort displays, i.e., ones connected via VGA, DVI, or HDMI. Hotplug events cannot be suppressed for displays connected via DisplayPort.

Note that probing the display configuration (e.g. with xrandr or nvidia-settings) may cause RandR display changed events to be generated, regardless of whether this option is enabled or disabled. Additionally, some VGA ports are incapable of hotplug detection: on such ports, the addition or removal of displays can only be detected by re-probing the display configuration.

Default: on. The driver will generate RandR events when displays are added or removed.

`Option "AllowEmptyInitialConfiguration" "boolean"`
Normally, the NVIDIA X driver will start even if there are no display devices connected to the NVIDIA GPU. Manually disabling AllowEmptyInitialConfiguration will prevent the NVIDIA X driver from loading if it cannot find any display devices.

Disabling this option makes sense in configurations where X should not start without any displays connected. It would also make sense to disable this option to preserve behavior on older systems.

Default: on. The driver will start even if it cannot find any connected display devices.

`Option "InbandStereoSignaling" "boolean"`
This option can be used to enable the DisplayPort in-band stereo signaling done via the MISC1 field in the main stream attribute (MSA) data that's sent once per frame during the vertical blanking period of the main video stream. DisplayPort in-band stereo signaling is only available on certain NVIDIA RTX/Quadro boards. This option is implied by stereo mode 14 (Generic active stereo with in-band DP), and selecting that stereo mode will override this option.

Default: off. DisplayPort in-band stereo signaling will be disabled.

`Option "UseSysmemPixmapAccel" "boolean"`
For discrete GPUs with dedicated video memory, this option allows the GPU to accelerate X drawing operations using system memory in addition to memory on the GPU. Disabling this option is generally not recommended, but it may reduce X driver memory usage in some situations at the cost of some performance.

This option does not affect the usage of GPU acceleration for pixmaps bound to GLX drawables, EGL surfaces, or EGL images. GPU acceleration of such pixmaps is critical for interactive performance.

Default: on. When video memory is unavailable, the GPU will still attempt to accelerate X drawing operations on pixmaps allocated in system memory.

This option is not applicable for Tegra integrated graphics as it does not have dedicated video memory.

`Option "ForceCompositionPipeline" "string"`
The NVIDIA X driver can use a composition pipeline to apply X screen transformations and rotations. Normally, this composition pipeline is enabled implicitly when necessary, or when the MetaMode token "ForceCompositionPipeline" is specified. This X configuration option can be used to explicitly enable the composition pipeline, even if the corresponding MetaMode token is not specified.

The option value is a comma-separated list of display device names. The composition pipeline will be forced on for all display devices in the comma-separated list.

Alternatively, the option value can be any boolean true string ("1", "on", "true", "yes"), in which case all display devices will have their composition pipeline enabled.

By default, the option value is NULL.

`Option "ForceFullCompositionPipeline" "string"`
This option has the same possible values and semantics as "ForceCompositionPipeline", but it additionally makes use of the composition pipeline to apply ViewPortOut scaling.

`Option "AllowHMD" "string"`
Most Virtual Reality Head Mounted Displays (HMDs), such as the HTC VIVE, require special image processing. This means it is usually undesirable to display the X11 desktop on an HMD. By default, the NVIDIA X driver will treat any detected HMDs as disconnected. To override this behavior, set the X configuration option "AllowHMD" to "yes", or explicitly list the HMDs to allow (any other HMDs will continue to be ignored).

Examples:

``` screen
    Option "AllowHMD" "yes"
```

``` screen
    Option "AllowHMD" "HDMI-0, HDMI-1"
```

`Option "AllowExternalGpus" "boolean"`
This option allows the NVIDIA X driver to configure X screens on external GPUs, also known as eGPUs. Note that this option is applied globally: setting this option to true will enable the use of all eGPUs.

"AllowExternalGpus" defaults to false, to avoid putting the X server in a situation where a GPU it is actively using can be hot-unplugged. External GPUs are often used in short-running compute scenarios, which better tolerate the eGPU being hot-unplugged. In such cases, a different GPU may be used to display the X11 desktop.

In addition to eGPUs, "AllowExternalGpus" set to false may prevent the NVIDIA X driver from configuring X screens on GPUs attached to internal PCIe slots with surprise removal/hot-unplug support, such as in some enterprise systems.

This option can be placed either in the "Device" or "ServerLayout" section of the X.Org configuration file.

Default: false. The NVIDIA X driver will not configure X screens on eGPUs.

`Option "LimitFrameRateWhenHeadless" "boolean"`
When there are no active displays, the resulting configuration is "headless". In a headless configuration, OpenGL and Vulkan applications are not able to sync to vblank, and without framerate limiting will run unbounded, potentially wasting system resources and power.

To prevent this from happening unintentionally, OpenGL and Vulkan applications that sync to vblank are restricted to 1 frame per second when there are no active displays. If X starts without displays, framerate limiting is disabled to avoid interfering with intended headless configurations.

Default: true. OpenGL and Vulkan applications will be limited to 1 frame per second when there are no active displays. If no displays are configured when the NVIDIA X driver initializes, the option will be forced to false.

`Option "HardDPMS" "boolean"`
By default, the NVIDIA X driver puts displays to sleep using modesets rather than the VESA DPMS ("Display Power Management Signaling") standard. There should be no visible difference to users of LCDs -- DPMS was originally designed for CRT monitors, and includes intermediate states that are redundant for LCDs.

When displays are put to sleep using modesets, they are completely shut down. As a result, OpenGL and Vulkan applications will behave as though the system were headless, and will not be able to sync to vblank, instead being subject to automatic framerate limiting where applicable; see [LimitFrameRateWhenHeadless](xconfigoptions.html#LimitFrameRateWhenHeadless).

When "HardDPMS" is set to false, the NVIDIA X driver will put displays to sleep using the VESA DPMS standard rather than modesets. Some LCDs may fail to respond correctly to VESA DPMS, which leaves them powered on when they should be in a sleep state.

Default: true. The NVIDIA X driver will put displays to sleep using modesets.

`Option "SidebandSocketPath" "string"`
The NVIDIA X driver uses a UNIX domain socket to pass information to other driver components. If unable to connect to this socket, some driver features, such as G-Sync, may not work correctly. The socket will be bound to a file with a name unique to the X server instance created in the directory specified by this option. Note that on Linux, an additional abstract socket (not associated with a file) will also be created, with this pathname socket serving as a fallback if connecting to the abstract socket fails.

Default: /var/run bind the pathname socket to a file created in this directory.

`Option "ConnectToAcpid" "boolean"`
The ACPI daemon (acpid) receives information about ACPI events like AC/Battery power, docking, etc. acpid will deliver these events to the NVIDIA X driver via a UNIX domain socket connection. By default, the NVIDIA X driver will attempt to connect to acpid to receive these events. Set this option to "off" to prevent the NVIDIA X driver from connecting to acpid. Default: on (the NVIDIA X driver will attempt to connect to acpid).

`Option "AcpidSocketPath" "string"`
The NVIDIA X driver attempts to connect to the ACPI daemon (acpid) via a UNIX domain socket. The default path to this socket is "/var/run/acpid.socket". Set this option to specify an alternate path to acpid's socket. Default: "/var/run/acpid.socket".

`Option "EnableACPIBrightnessHotkeys" "boolean"`
Enable or disable handling of ACPI brightness change hotkey events. Default: enabled

`Option "3DVisionUSBPath" "string"`
When NVIDIA 3D Vision is enabled, the X driver searches through the usbfs to find the connected USB dongle. Set this option to specify the sysfs path of the dongle, from which the X driver will infer the usbfs path.

Example:

``` screen
Option "3DVisionUSBPath" "/sys/bus/usb/devices/1-1"
```

`Option "3DVisionProConfigFile" "string"`
NVIDIA 3D VisionPro provides various configuration options and pairs various glasses to sync to the hub. It is convenient to store this configuration information to re-use when X restarts. Filename provided in this option is used by NVIDIA X driver to store this information. Ensure that X server has read and write access permissions to the filename provided. Default: No configuration is stored.

Example:

``` screen
Option "3DVisionProConfigFile" "/etc/nvidia_3d_vision_pro_config_filename"
```

`Option "3DVisionDisplayType" "integer"`
When NVIDIA 3D Vision is enabled with a non 3D Vision ready display, use this option to specify the display type.

| Value | Behavior                                                  |     |
|-------|-----------------------------------------------------------|-----|
| 1     | Assume it is a CRT.                                       |     |
| 2     | Assume it is a DLP.                                       |     |
| 3     | Assume it is a DLP TV and enable the checkerboard output. |     |

Default: 1

Example:

``` screen
Option "3DVisionDisplayType" "1"
```

`Option "3DVisionProHwButtonPairing" "boolean"`
When NVIDIA 3D Vision Pro is enabled, use this option to disable hardware button based pairing. Single click button on the hub to enter into pairing mode which pairs single pair of glasses at a time. Double click button on the hub to enter into a pairing mode which pairs multiple pairs of glasses at a time.

Default: True

Example:

``` screen
Option "3DVisionProHwButtonPairing" "False"
```

`Option "3DVisionProHwSinglePairingTimeout" "integer"`
When NVIDIA 3D Vision Pro and hardware button based pairing are enabled, use this option to set timeout in seconds for pairing single pair of glasses.

Default: 6

Example:

``` screen
Option "3DVisionProHwSinglePairingTimeout" "10"
```

`Option "3DVisionProHwMultiPairingTimeout" "integer"`
When NVIDIA 3D Vision Pro and hardware button based pairing is enabled, use this option to set timeout in seconds for pairing multiple pairs of glasses.

Default: 10

Example:

``` screen
Option "3DVisionProHwMultiPairingTimeout" "10"
```

`Option "3DVisionProHwDoubleClickThreshold" "integer"`
When NVIDIA 3D Vision Pro and hardware button based pairing is enabled, use this option to set the threshold for detecting double click event of the button. Threshold is time in ms. within which user has to click the button twice to generate double click event.

Default: 1000 ms

Example:

``` screen
Option "3DVisionProHwDoubleClickThreshold" "1500"
```

`Option "DisableBuiltin3DVisionEmitter" "boolean"`
This option can be used to disable the NVIDIA 3D Vision infrared emitter that is built into some 3D Vision ready display panels. This can be useful when an external NVIDIA 3D Vision emitter needs to be used with such a panel.

Default: False

Example:

``` screen
Option "DisableBuiltin3DVisionEmitter" "True"
```

The following NVIDIA X driver options are global to the X server, and should be specified in the "ServerLayout" section of the X configuration file.

`Option "AllowNVIDIAGPUScreens" "boolean"`
When this option is enabled, and the X server version supports GPU screens (xorg-server 1.13 or newer), the NVIDIA X driver will allow GPU screens to be created for each NVIDIA GPU detected in the system for which there is no X screen configured or auto-configured.

GPU screens within the X server are generally not directly addressable by X11 applications: the 'screen' index in any X protocol request can only specify X screens, not GPU screens. But, GPU screens are useful for PRIME render offload configurations.

Default: The NVIDIA X driver will allow GPU screens on X.Org xserver version 1.20.7 and higher.

`Option "AllowPRIMEDisplayOffloadSink" "boolean"`
RandR PRIME Display Offload Sink support, also known as "Reverse PRIME", is disabled by default for NVIDIA RandR providers on X.Org X servers prior to version 1.20.7 due to latent bugs that can result in crashes when used with the NVIDIA driver. X server version 1.20.6 contains fixes for the crashing, but cannot be detected automatically.

This option overrides the default behavior, allowing PRIME Display Offload Sink to be used regardless of X server version.

Default: PRIME Display Offload Sink will be allowed only for X server 1.20.7 or newer.
