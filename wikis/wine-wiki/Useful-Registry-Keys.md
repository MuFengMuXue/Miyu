Users should never have to play with the registry. That said, sometimes
there's no other way to do what you need to do...

For a description of the registry, see [the Wine User
Guide](Wine-User's-Guide#using-the-registry-and-regedit) or
[Wikipedia](https://en.wikipedia.org/wiki/Windows_Registry).

Here you'll find useful registry keys that cannot be changed in
[winecfg](Commands/winecfg). You should edit the registry using
[regedit](Commands/regedit).

**If a key or value does not exist, create it. All values are strings
(REG_SZ) unless stated otherwise.**

To create a new key if it does not exist:

1.  In a terminal, type `wine regedit` and hit enter
2.  Open the tree on the left to the section where you need to add it
    (e.g., `HKEY_CURRENT_USER\Software\Wine`)
3.  Select the section you are going to add the new key to (e.g., `Wine`)
4.  Right click and select New→Key
5.  Type the name of the new key (taken from the list below)
6.  Hit enter

I'll try to keep this list accurate but you might want to check it
against current Wine source code (for Wine related keys that is):

```sh
$ find . -type f -exec grep "@@" {} \; | grep registry
```

In the following `├──` means key and `├─>` means value.

## HKEY_CURRENT_USER (a.k.a HKCU)

    │
    └──Software
       │
       └──Wine
          │
          ├──AppDefaults
          │  │
          │  └──*<app.exe>
          │       [Application specific defaults. Replace app.exe with the name of the
          │        application you want to override defaults for. And use the same subtrees
          │        as the Wine subtree (i.e. DllOverrides, X11 Driver, etc.).]
          │
          ├──Debug
          │  │
          │  ├─>RelayExclude
          │  │   [Use this key to exclude some calls from the (overwhelming) +relay debug logging. Example:
          │  │    "RelayExclude"="ntdll.RtlEnterCriticalSection;ntdll.RtlLeaveCriticalSection"]
          │  │
          │  ├─>RelayFromExclude
          │  │   [Exclude calls made from listed dlls in the the +relay debug log. Example:
          │  │    "RelayFromExclude"="kernel32" - omit all calls made from kernel32.dll]
          │  │
          │  ├─>SpyExclude
          │  │   [Exclude listed messages from the +message debug log. Example:
          │  │    "SpyExclude"="WM_TIMER;WM_MOUSEMOVE;WM_PAINT"]
          │  │
          │  └─>SpyInclude
          │      [Include only listed messages in the +message debug log. Example:
          │       "SpyInclude"="WM_CREATE"]
          │
          ├──Direct2D
          │  │
          │  └─>max_version_factory
          │      [DWORD Value (REG_DWORD): Limit the maximum supported Direct2D factory version.]
          │
          ├──Direct3D
          │  │
          │  ├─>CheckFloatConstants
          │  │   [Range check float constants in d3d9 shaders. Use this to workaround
          │  │    application bugs like #34052,
          │  │    usually resulting in geometry glitches. Enabling this has a small performance
          │  │    impact, default is disabled.]
          │  │
          │  ├─>csmt
          │  │   [DWORD Value (REG_DWORD): Enable (0x1, default) or disable (0x0) the multi-threaded
          │  │    command stream feature. This serialises rendering commands from different threads into
          │  │    a single rendering thread, in order to avoid the excessive synchronisation that would otherwise
          │  │    be required for correct rendering. This superseded the old "StrictDrawOrdering" setting.
          │  │    Introduced in Wine 2.6.
          │  │    Starting with Wine 6.0-rc1 this value is a bitmask, with bit 1 forcing serialisation
          │  │    of OpenGL or Vulkan commands between multiple command streams in the same application.
          │  │    This can be useful for applications using d3d from multiple threads, like MS Office 2013+,
          │  │    on drivers that are buggy in this regard, like Nouveau (as of the end of 2020). To enable this
          │  │    functionality you would set the registry key to 0x3, to enable both the command stream and the
          │  │    command serialisation.]
          │  │
          │  ├─>MaxShaderModelCS
          │  │   [DWORD Value (REG_DWORD): Limit the maximum supported shader model for compute shaders.
          │  │    Set to 0 to disable support for compute shaders.]
          │  │
          │  ├─>MaxShaderModelDS
          │  │   [DWORD Value (REG_DWORD): Limit the maximum supported shader model for domain shaders.
          │  │    Set to 0 to disable support for domain shaders.]
          │  │
          │  ├─>MaxShaderModelGS
          │  │   [DWORD Value (REG_DWORD): Limit the maximum supported shader model for geometry shaders.
          │  │    Set to 0 to disable support for geometry shaders.]
          │  │
          │  ├─>MaxShaderModelHS
          │  │   [DWORD Value (REG_DWORD): Limit the maximum supported shader model for hull shaders.
          │  │    Set to 0 to disable support for hull shaders.]
          │  │
          │  ├─>MaxShaderModelPS
          │  │   [DWORD Value (REG_DWORD): Limit the maximum supported shader model for pixel shaders.
          │  │    Set to 0 to disable support for pixel shaders.]
          │  │
          │  ├─>MaxShaderModelVS
          │  │   [DWORD Value (REG_DWORD): Limit the maximum supported shader model for vertex shaders.
          │  │    Set to 0 to disable support for vertex shaders.]
          │  │
          │  ├─>MaxVersionGL
          │  │   [DWORD Value (REG_DWORD): Choose the maximum OpenGL version to request.
          │  │    Defaults to OpenGL version 4.4 since Wine 3.9 (except for Nvidia GPUs where the default only changed with Wine 3.18).
          │  │    Set it to 30002 (hexadecimal) or greater to request a core profile context.]
          │  │
          │  ├─>MultisampleTextures
          │  │   [DWORD Value (REG_DWORD): Enable (0x1, default) or disable (0x0) multisample textures.
          │  │    If multisample textures are disabled, renderbuffers are used for multisampling.]
          │  │
          │  ├─>OffscreenRenderingMode
          │  │   [Select the offscreen rendering implementation.
          │  │        backbuffer - Render offscreen render targets in the backbuffer
          │  │        fbo - Use framebuffer objects for offscreen rendering (default)]
          │  │
          │  ├─>renderer
          │  │   [Select what backend to use for wined3d. Valid options are:
          │  │        gdi
          │  │        gl
          │  │        vulkan
          │  │    The "gdi" option (and its alias "no3d") mostly exists for legacy or test reasons.
          │  │     As of Wine 5.1, gl is the default and vulkan is still work in progress,
          │  │     so don't expect great results with it yet.]
          │  │
          │  ├─>SampleCount
          │  │   [DWORD Value (REG_DWORD): Override swapchain sample count. It can be used to force enable multisampling
          │  │    with applications that otherwise don't support it, like the similar control panel setting
          │  │    available with some GPU drivers. This one might work in more cases than the driver setting though.
          │  │    Not all applications are compatible with this setting.]
          │  │
          │  ├─>shader_backend
          │  │   [Valid options are:
          │  │        glsl
          │  │        arb
          │  │        none
          │  │    If not set, and UseGLSL is not set to "disabled", the shader backend will be determined automatically,
          │  │     with preference going to glsl.]
          │  │
          │  ├─>strict_shader_math
          │  │   [DWORD Value (REG_DWORD): Enable (0x1) or disable (0x0, default)
          │  │    generation of NVIDIA specific pragma in GLSL shader code to
          │  │    turn off aggressive optimization of the shader code by the driver.
          │  │    Use this to workaround bugs like #35207,
          │  │    usually resulting in incorrect rendering of some objects which is
          │  │    reproducible on NVIDIA GPU with proprietary driver only.]
          │  │
          │  ├─>UseGLSL
          │  │   [When set to "disabled", this disables the use of GLSL for shaders.
          │  │    In general disabling GLSL is not recommended, only use this for debugging purposes.]
          │  │
          │  ├─>VideoMemorySize
          │  │   [Set the amount of reported video memory (in megabytes). By default Wine will use
          │  │    GLX_MESA_query_renderer to determine the amount of video memory on the graphics
          │  │    card. On (mostly proprietary) drivers not supporting GLX_MESA_query_renderer, Wine
          │  │    will instead estimate the amount of video memory based on the card's PCI IDs. The
          │  │    The "VideoMemorySize" setting allows the value determined by Wine to be overridden.]
          │  │
          │  ├─>VideoPciDeviceID
          │  │   [DWORD Value (REG_DWORD): Set the PCI device ID of the graphics card. See "VideoPciVendorID".]
          │  │
          │  ├─>VideoPciVendorID
          │  │   [DWORD Value (REG_DWORD): Set the PCI vendor ID of the graphics card. By default
          │  │    Wine wil use GLX_MESA_query_renderer to determine the PCI IDs of the graphics card.
          │  │    On (mostly proprietary) drivers not supporting GLX_MESA_query_renderer, Wine will
          │  │    instead try to pick an appropriate set of PCI IDs based on the OpenGL GL_RENDERER,
          │  │    GL_VENDOR, and GL_EXTENSIONS strings. The "VideoPciVendorID" and "VideoPciDeviceID"
          │  │    settings allow the values determined by Wine to be overridden. For most applications
          │  │    there should be little reason to touch these settings, but there exists a limited set of
          │  │    applications that will choose a broken code path based on the PCI IDs. Note that only
          │  │    combinations listed in wined3d's gpu_description_table[] are valid here.]
          │  │
          │  └─>WineLogo
          │      [Path to image file to use as logo for Wine.]
          │
          ├──DirectInput
          │  │
          │  ├─>MouseWarpOverride
          │  │   [Override default mouse pointer warping behavior:
          │  │    enable:  (default) warp pointer when mouse exclusively acquired
          │  │    disable: never warp the mouse pointer
          │  │    force:   always warp the pointer]
          │  │
          │  ├─>*<joystick name> = <axes mapping>
          │  │   [This maps axes of joystick "joystick name". The "axes mapping" is
          │  │    comma-separated list of "axis type"s - one for each joystick axis (hat-pov uses 2 axes).
          │  │    "axis type" is one of: X, Y, Z, Rx, Ry, Rz, Slider1, Slider2, POV1, POV2, POV3, POV4.
          │  │    To find the joystick name run
          │  │    'WINEDEBUG=+dinput wine game.exe 2>&1 │ grep joydev_enum_device'
          │  │    Example output: trace:dinput:joydev_enum_deviceW Enumerating the linux Joystick device: /dev/input/js0 (Logitech Logitech Dual Action)
          │  │    Example registry entry: "Logitech Logitech Dual Action"="X,Y,Rz,Slider1,POV1". (two "Logitech"s not a typo)]
          │  │
          │  └─>DefaultDeadZone
          │      [Sets a default value for every joystick axis dead zone. Should be a value between 0 and 10000.
          │       The value represents the percentage of the axis which will seen as dead (applications will think of it as being centered).
          │       For example 3000 will extend the dead zone to only the first 30% of the axis, while 0 will use the whole axis extension.]
          │
          ├──DirectSound
          │  │
          │  └─>HelBuflen
          │       Hardware emulation buffer length - default is 65536
          │
          ├──Drivers
          │  │
          │  ├─>Audio
          │  │    Which audio backend to use. Should be a string such as "pulse" or "alsa" or "oss" or "coreaudio".
          │  │    Set to the empty string to disable audio entirely. Given a comma-separated list of
          │  │    drivers, Wine will attempt to make the most appropriate choice.
          │  │
          │  ├──winealsa.drv
          │  │  │
          │  │  ├─>ALSAOutputDevices (REG_MULTI_SZ, "Multi String Value")
          │  │  │    A list of auxiliary output devices, not enumerated by ALSA's hardware enumeration
          │  │  │    methods. For example, you might put software devices here.
          │  │  │
          │  │  └─>ALSAInputDevices (REG_MULTI_SZ, "Multi String Value")
          │  │       A list of auxiliary input devices, not enumerated by ALSA's hardware enumeration
          │  │       methods.
          │  │
          │  └─>Graphics
          │       Which graphic driver to use.
          │       mac: Use the native quartz driver (default on macOS)
          │       x11: Use the X11 driver
          │       null: Use the null driver (a virtual screen will be created, but not displayed; available since Wine 5.2)
          │
          ├──Explorer
          │  │
          │  ├─>Desktop
          │  │   [Title of the default virtual desktop window. The special value
          │  │    "shell" also causes the shell to be displayed, if the
          │  │    EnableShell value is not present (see below).]
          │  │
          │  ├─>Desktops
          │  │  │
          │  │  ├─>*<desktop name, most commonly "Default"> = <size>
          │  │  │   [String value such as "1024x768" or "1400x1050" that
          │  │  │    specifies the size of the virtual desktop. Defaults to
          │  │  │    800x600.]
          │  │  │
          │  │  └─>*<desktop name, most commonly "Default">
          │  │     │
          │  │     └─>EnableShell
          │  │         [DWORD value (REG_DWORD): Enable (0x1) or disable (0x0)
          │  │          the shell in the virtual desktop (i.e. Start menu,
          │  │          taskbar, system tray.) The default is 0x1 for the
          │  │          desktop named "shell" and 0x0 for all other desktops
          │  │          including the "Default" desktop.]
          │  │
          │  └─>ShowSystray
          │      [DWORD value (REG_DWORD): Enable (0x1, default) or disable
          │       (0x0) the floating system tray that appears if your Linux
          │       desktop environment doesn't have its own.]
          │
          ├──Fonts
          │  │
          │  ├──Replacements
          │  │  │
          │  │  └─>*<font name> = <replacement font name>
          │  │      ["Wingdings"="Winedings" would enumerate the Winedings font both as Winedings and
          │  │       Wingdings. However if a real Wingdings font is present the replacement does not
          │  │       take place.]
          │  │
          │  └──ExternalFonts
          │     │
          │     └─>*<font name>
          │         [ExternalFonts has a list of font names whose
          │          values are the name of the actual font]
          │
          ├──Mac Driver
          │  │
          │  ├─>AllowVerticalSync
          │  │   [Set to "n" to disable vsync support.]
          │  │
          │  ├─>CaptureDisplaysForFullscreen
          │  │   [Set to "y" to capture the displays when a full-screen window is presented even if
          │  │    the resolution hasn't been changed. Capturing the displays disables hot corners.]
          │  │
          │  ├─>UsePreciseScrolling
          │  │   [Set to "n" to emulate a "clicky" mouse wheel. Some programs react badly, usually
          │  │    by scrolling too far, when they get many small scroll wheel events.]
          │  │
          │  └─>WindowsFloatWhenInactive
          │      [Controls whether Win32 "TOPMOST" windows stay in front of other apps even when the
          │       Wine process is in the background. Set to "none" to prevent windows from floating
          │       when in the background. Set to "all" to have all TOPMOST windows float. Set to
          │       "nonfullscreen" (the default) to let TOPMOST windows float unless they cover the screen.]
          │
          ├──MSHTML
          │  │
          │  ├─>GeckoPath
          │  │   [Path to the where Gecko engine is installed. Example: "c:\Program Files\wine_gecko".]
          │  │
          │  ├─>GeckoUrl
          │  │   [This is the url to the Wine Gecko required by MSHTML.
          │  │    Default is https://source.winehq.org/winegecko.php.
          │  │    You can change it to a local file like file://Z:\path\to\wine_gecko.cab
          │  │    so you don't need to redownload it each time you create a new wineprefix.]
          │  │
          │  └─>CompatMode
          │       [Compatibility mode used by MSHTML. This is useful for web pages that work better in legacy
          │        compatibility modes. Set MaxCompatMode to string value specifying maximum IE you want to
          │        expose to web pages. You can also create subkeys to set compatibility mode of specific host
          │        name. If key name starts with '.', subdomains are also matched (for example .winehq.org will
          │        match both www.winehq.org and wiki.winehq.org). To limit compatibility mode to IE10 for all
          │        Wine web pages, create .winehq.org subkey and set its MaxCompatMode value to "10".]
          │
          ├──Network
          │  │
          │  └─>UseDnsComputerName
          │      [Set to N if you need a persistent NetBIOS ComputerName that possibly
          │       differs from the Unix host name. You'll need to set ComputerName in
          │       HKLM\System\CurrentControlSet\Control\ComputerName\ComputerName]
          │
          ├──OpenGL
          │  │
          │  ├─>DisabledExtensions
          │  │   [Space separated list of OpenGL extensions that are not reported to applications.
          │  │    Example: "GL_ARB_vertex_buffer_object GL_ATI_fragment_shader".]
          │  │
          │  └─>EnabledExtensions
          │      [Space separated list of the only OpenGL extensions which should be reported.
          │       Example: "GL_ARB_vertex_buffer_object GL_ATI_fragment_shader".]
          │
          ├──Printing
          │  │
          │  ├─>PPD Files
          │  │  │  [When CUPS does not find any printers (Wine compiled without CUPS,
          │  │  │   libcups not loadable or required functions not found in libcups),
          │  │  │   then this key must exist to use your printers from "/etc/printcap"]
          │  │  │
          │  │  ├─>*<printer name> = <PPD File with full Unix path>
          │  │  │    [If no value with the name "PPD file" is found in the registry in
          │  │  │     the settings for a printer ("<printer name>\\PrinterDriverData"),
          │  │  │     then this key is tried next.]
          │  │  │
          │  │  └─>"generic" = <the default PPD file with full Unix path>
          │  │        [This PPD file is used when every other key has failed.
          │  │         "wineps.drv" needs a PPD file for every printer.]
          │  │
          │  └─>Spooler
          │     │  [You can redirect any printer port to a Unix file or pipe it to a
          │     │   Unix application. This is also useful when a Windows program has
          │     │   disabled the "Redirect to File" option in the Print dialog.]
          │     │
          │     └─>*<portname> = <unixfile or "|unix_application">
          │         [All printers with the given portname can be redirected.
          │          Example of unixfile: "LPT1:" = "/tmp/printer_data.ps"
          │          Example of pipe: "LPR:Print with KDE" = "|kprinter" ]
          │
          ├─>Version
          │   [This is the version of Windows Wine will report.
          │    Values: win10, win81, win8, win7, win2008, vista, win2003, winxp, win2k
          │    Also supported, but less useful these days: nt40,  winme, win98, win95, win31]
          │
          ├──VDM
          │  │
          │  └──ppdev
          │     │
          │     └─>*<port_number> = </dev/parportN>
          │         [This sets mapping between port_number and /dev/parportN device.
          │           For example  "378  /dev/parport0".]
          │
          ├──WineBrowser
          │  │
          │  ├─>Browsers
          │  │   [List of browsers that Wine will attempt to launch when running winebrowser
          │  │    command or clicking on a link in a Windows application. Default value is
          │  │    xdg-open,firefox,konqueror,mozilla,netscape,galeon,opera,dillo]
          │  │
          │  └─>Mailers
          │      [List of mail clients that Wine will attempt to launch when running winebrowser
          │       Default value is xdg-email,mozilla-thunderbird,thunderbird,evolution]
          │
          ├──WineDbg
          │  │
          │  ├─>BreakOnFirstChance
          │  │   [DWORD value. Set this to "0" to let applications handle exceptions themselves.
          │  │    winedbg then only catches exceptions that are not handled by the app,
          │  │    which makes debugging a bit easier.
          │  │    Default value is "1" (enabled)]
          │  │
          │  └─>ShowCrashDialog
          │      [DWORD value. Set this to "0" to disable the GUI crash dialog.
          │       Default value is "1" (enabled)]
          │
          └──X11 Driver
             │
             ├─>ClientSideGraphics
             │   [Set this to "N" if you don't want to use the Dib engine to render client side windows]
             │
             ├─>ClientSideWithRender
             │   [Set this to "N" if you don't want to use the Render extension to render client side fonts]
             │
             ├─>ClientSideAntiAliasWithRender
             │   [Set this to "N" to disable font anti-aliasing when X-Render extension is present]
             │
             ├─>ClientSideAntiAliasWithCore
             │   [Set this to "N" to disable font anti-aliasing when X-Render extension is not present
             │    or disabled]
             │
             ├─>GrabFullscreen
             │   [Set this to "Y" to force full-screen windows to capture the mouse.]
             │
             ├─>GrabPointer
             │   [Set this to "N" to disallow mouse capture.]
             │
             ├─>Managed
             │   [Set this to "N" to disallow the window manager to control created windows.]
             │
             ├─>Decorated
             │   [Set this to "N" to disallow the window manager to decorate created windows.]
             │
             ├─>UseEGL
             │   [Set this to "N" to use GLX instead of EGL for OpenGL.]
             │
             ├─>UseXRandR
             │   [Set this to "N" to prevent wine from switching the resolution using XRandr extension.]
             │
             └─>UseXVidMode
                 [Set this to "Y" to allow wine switch the resolution using XVidMode extension.]

## HKEY_LOCAL_MACHINE (a.k.a HKLM)

    │
    ├──Software
    │  │
    │  ├──Microsoft
    │  │  │
    │  │  ├──DirectDraw
    │  │  │  │
    │  │  │  └─>ForceRefreshRate
    │  │  │      [DWORD value (REG_DWORD): Set this to the refresh rate you wish to
    │  │  │       force for DirectX games.  This is analogous to forcing the refresh
    │  │  │       rate in Windows using dxdiag as described in KB315614 (main article),
    │  │  │       KB230002, and KB217348.  If this key does not exist, the default
    │  │  │       refresh rate will be used.]
    │  │  │
    │  │  ├──Internet Explorer
    │  │  │  │
    │  │  │  ├─>Version
    │  │  │  ├─>W2kVersion
    │  │  │  │   [Useful to make application believe that you have Internet Explorer
    │  │  │  │   installed (if you set it manually, you might need some IE-provided
    │  │  │  │   dlls). Set them to "6.0.2800.1106" for IE6SP1.]
    │  │  │  │
    │  │  │  └─>Build
    │  │  │     [Same as above. Set it to "62800.1106" for IE6SP1.]
    │  │  │
    │  │  │
    │  │  ├──Windows
    │  │  │  │
    │  │  │  └──CurrentVersion
    │  │  │     │
    │  │  │     └──Add Paths
    │  │  │        │
    │  │  │        └──IExplore.exe
    │  │  │           [this key explains where to find iexplore.exe.
    │  │  │            It is needed if you install the gecko engine.
    │  │  │            Default: "C:\Program Files\Internet Explorer\iexplore.exe"
    │  │  │            "Path": "C:\Program Files\Internet Explorer;"]
    │  │  │
    │  │  └──Windows NT
    │  │     │
    │  │     └──CurrentVersion
    │  │        │
    │  │        ├─>FontSubstitutes
    │  │        │   [Define font substitutes.
    │  │        │    For example: "Tahoma"="Arial" will substitute 'Tahoma' font with 'Arial' font.]
    │  │        │
    │  │        └──AeDebug
    │  │           │
    │  │           └─>Debugger
    │  │               [Command to execute on unhandled exception. The environment
    │  │                variable WINEDEBUG is cleared before execution.
    │  │                Default: "winedbg --auto %ld %ld"]
    │  │
    │  └──Wine
    │     │
    │     └──Ports
    │        │
    │        └─>*<Win32 path> = <unix path>
    │          [Defines a fixed mapping from Unix serial or parallel port devices to
    │           Win32 device paths. Ports not mapped here will be automatically
    │           assigned in some order.
    │           Example: "COM3" = "/dev/ttyS5", "LPT1" = "/dev/lp4"]
    │
    └──System
       │
       └──CurrentControlSet
          │
          ├──Control
          │  │
          │  ├──Windows
          │  │  │
          │  │  └─>CSDVersion
          │  │      [Current service pack version.
          │  │       On Windows XP, SP2 is 0x00000200 and SP3 is 0x00000300]
          │  │
          │  ├──ComputerName
          │  │  │
          │  │  └─>ComputerName
          │  │      [Current computer name.
          │  │       Updated automatically from Unix host name unless UseDnsComputerName=N]
          │  │
          │  └──Session Manager
          │     │
          │     ├─>GlobalFlag
          │     │   [DWORD. Used to enable various internal diagnostics, such as heap checking.]
          │     │
          │     └──Environment
          │        │
          │        ├─>ComSpec
          │        │   [Location of the system's command prompt.
          │        │    Default: c:\windows\system32\cmd.exe]
          │        │
          │        ├─>PATH
          │        │   [Path environment variable for searching programs.
          │        │    Default: c:\windows\system32;c:\windows]
          │        │
          │        ├─>ProgramFiles
          │        │   [Location of the Program Files directory and ProgramFiles environment variable.
          │        │    Default for English: C:\Program Files]
          │        │
          │        ├─>SYSTEMROOT
          │        │   [Location of the windows system root and SYSTEMROOT environment variable.
          │        │    Default: c:\windows]
          │        │
          │        ├─>TEMP
          │        │   [Location of the temporary files directory and TEMP environment variable.
          │        │    Default: c:\windows\temp
          │        │
          │        ├─>TMP
          │        │   [Same as above.]
          │        │
          │        ├─>USERPROFILE
          │        │   [Location of the user's profile directory and USERPROFILE environment variable.
          │        │    Default: c:\users\<unix username>]
          │        │
          │        ├─>windir
          │        │   [Location of the windows system root
          │        │    Default: c:\windows]
          │        │
          │        └─>winsysdir
          │            [Location of the system libraries directory
          │             Default: c:\windows\system32]
          │
          ├──Hardware Profiles
          │  │
          │  └──Current
          │     │
          │     └──Software
          │        │
          │        └──Fonts
          │           │
          │           └─>LogPixels
          │               [DWORD value (REG_DWORD): Sets current DPI (font size).
          │                Some dialogs resize themselves according to this value.
          │                Default: 96 (decimal).]
          │
          └──Services
             │
             └──WineBus
                │
                ├──Devices
                │  │
                │  └─>*<VID>[/PID]
                │      │  [One key for each Vendor ID / Product ID for which the options below
                │      │   will apply. If </PID> is omitted, options apply to every device with
                │      │   the given VID]
                │      │
                │      └─>HidRaw
                │          [DWORD value (REG_DWORD): Enable (0x1) or disable (0x0, default) the
                │           use of hidraw to discover and communicate with HID devices.]
                │
                ├─>DisableHidraw
                │   [DWORD value (REG_DWORD): Disable (0x1) or enable (0x0, default) the use of hidraw
                │    to discover and communicate with HID devices.]
                │
                ├─>EnableHidraw
                │   [Comma separated list of VID:PID of the HID devices for which to enable the hidraw
                │    backends and expose them directly to the Windows world.]
                │
                ├─>DisableInput
                │   [DWORD value (REG_DWORD): Disable (0x1) or enable (0x0, default) the use of evdev
                │    to discover and communicate with HID devices.]
                │
                ├─>Enable SDL
                │   [DWORD value (REG_DWORD): Enable (0x1, default) or disable (0x0) the use of SDL to
                │    discover and communicate with HID devices.]
                │
                ├──Map
                │  │
                │  └─>*<unique value> = <mapping string>
                │      [One or more custom mappings for SDL joysticks. The name of the value is not
                │       used and may be anything. The data is passed directly into
                │       SDL_GameControllerAddMapping(); see the SDL documentation for the format.]
                │
                └─>Map Controllers
                    [DWORD value (REG_DWORD): Enable (0x1, default) or disable (0x0) conversion from
                     SDL controllers to XInput-compatible gamepads. Only applies to SDL backend.]

## See also

- [winecfg](Commands/winecfg) -- The Wine configuration tool
- [regedit](Commands/regedit) -- The Wine registry editor
- [Debug Channels](Debug-Channels) -- How to turn on and off
  debug channels (i.e. relay)
- [Wine Man Page](Man-Pages/wine) -- Documents environment variables
  which could be an alternative to editing the registry.
