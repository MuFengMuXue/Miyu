Mono is an open-source and cross-platform implementation of the .NET
Framework. Wine Mono is a fork of Mono that Wine uses to run .NET
Framework applications.

## Installing

### From source

The source code can be obtained from a tarball in
<https://dl.winehq.org/wine/wine-mono/> or the development tree at
<https://gitlab.winehq.org/mono/wine-mono>.

From a source tree, you can use the "make dev" target to build Wine Mono
and configure the current Wine prefix (default or as set by the
WINEPREFIX environment variable) to use the build. The "make dev-setup"
target will just configure the Wine prefix without building.

### Shared Install

For packagers, and users with multiple prefixes, a shared install is
recommended.

To create a shared install, download the appropriate binary tarball from
<https://dl.winehq.org/wine/wine-mono/> (or build it from source with
"make bin") and extract it to the appropriate location.

Wine will search for Wine Mono in the following places (replacing 5.0.0
with the expected version from the version table below):

- `c:\windows\mono\mono-2.0`. Extracting a tarball here is not
  recommended. If you want to install into a specific prefix, use the
  [Prefix Local Install](#prefix-local-install) instructions
  below. It's only included in this list to make it clear that an
  installed .msi takes priority over the other locations.
- The directory specified in `HKEY_CURRENT_USER\Software\Wine\Mono`
  string value "RuntimePath".
- `${prefix}/share/wine/mono/wine-mono-5.0.0` or
  `${builddir}/../mono/wine-mono-5.0`.
- `/usr/share/wine/mono/wine-mono-5.0.0`
- `/opt/wine/mono/wine-mono-5.0.0`

When using a shared install, The "Wine Mono Windows Support" package
must still be installed in the prefix. This is handled automatically on
prefix update, so normally it shouldn't be a problem, but in some corner
cases you might have to run `wineboot -u` to set this up after creating
the shared install.

### Prefix Local Install

Wine will automatically download and install the appropriate Wine Mono
MSI on prefix update, so this shouldn't usually be necessary.

If you wish to use a different MSI installer than the one you'd get
automatically:

- Obtain the MSI file you wish to use, either from
  ```dl.winehq.org/wine/wine-mono/VERSION/wine-mono-VERSION-x86.msi``` (substitute the actual version number for VERSION) or by running `make msi` in a
  build tree. It's possible you already have the one you want in
  `~/.cache/wine`.
- Run `wine uninstaller` and remove "Wine Mono Runtime" and "Wine Mono
  Windows Support" if you have them.
- Run `wine path/to/wine-mono.msi`.

The installer normally gives no feedback when it succeeds. You can run
`wine uninstaller` again to check that you have the version you expect.

## Versions

| Wine Version | Wine Mono Version |
|--------------|-------------------|
| 11.8         | 11.1.0            |
| 11.3         | 11.0.0            |
| 11.0-rc4     | 10.4.1            |
| 11.0-rc1     | 10.4.0            |
| 10.17        | 10.3.0            |
| 10.14        | 10.2.0            |
| 10.10        | 10.1.0            |
| 10.5         | 10.0.0            |
| 10.0-rc1     | 9.4.0             |
| 9.17         | 9.3.0             |
| 9.12         | 9.2.0             |
| 9.8          | 9.1.0             |
| 9.2          | 9.0.0             |
| 8.19         | 8.1.0             |
| 8.9          | 8.0.0             |
| 7.20         | 7.4.0             |
| 7.10         | 7.3.0             |
| 7.6          | 7.2.0             |
| 7.2          | 7.1.1             |
| 6.22         | 7.0.0             |
| 6.18         | 6.4.0             |
| 6.14         | 6.3.0             |
| 6.10         | 6.2.0             |
| 6.6          | 6.1.1             |
| 6.2          | 6.0.0             |
| 5.19         | 5.1.1             |
| 5.11         | 5.1.0             |
| 5.7          | 5.0.0             |
| 4.20         | 4.9.4             |
| 4.17         | 4.9.3             |
| 4.14         | 4.9.2             |
| 4.11         | 4.9.0             |
| 4.7          | 4.8.3             |
| 4.6          | 4.8.1             |
| 4.3          | 4.8.0             |
| 4.0-rc6      | 4.7.5             |
| 3.13         | 4.7.3             |
| 2.14         | 4.7.1             |
| 2.4          | 4.7.0             |
| 2.0-rc1      | 4.6.4             |
| 1.9.12       | 4.6.3             |
| 1.9.8        | 4.6.2             |
| 1.9.5        | 4.6.0             |
| 1.7.37       | 4.5.6             |
| 1.7.32       | 4.5.4             |
| 1.7.7        | 4.5.2             |
| 1.5.16       | 0.0.8             |
| 1.5.5        | 0.0.4             |

## Building

For build instructions, see the readme at
<https://gitlab.winehq.org/mono/wine-mono>

## Debugging

The WINE_MONO_TRACE environment variable may be set as follows to trace
calls within Mono:

    all                  All assemblies
    none                 No assemblies
    program              Entry point assembly
    assembly             Specifies an assembly
    wrapper              All wrappers bridging native and managed code
    M:Type:Method        Specifies a method
    N:Namespace          Specifies a namespace
    T:Type               Specifies a type
    E:Type               Specifies stack traces for an exception type
    EXPR                 Includes expression
    -EXPR                Excludes expression
    EXPR,EXPR            Multiple expressions

This option is the same as the `--trace` option in Mono.

Note that "All assemblies" includes the program itself and all libraries
shipped with it. Mono is capable of tracing any .NET code. You probably
should avoid the "all" trace if there might be proprietary code running
in the process.

Activating any trace at all, even a bogus assembly name, will cause Mono
to print out all exceptions as they occur. This can be useful, but it
can also be misleading as some exceptions are perfectly normal.

Sometimes Mono's inlining can obscure the source of an exception,
especially NotImplementedException. This can be worked around by setting
`MONO_INLINELIMIT=0`.

Setting `WINE_MONO_VERBOSE=1` will display the addresses of all
JIT-compiled methods. Setting `MONO_VERBOSE_METHOD=MethodName` will
display detailed information about the method's compilation, and break
into the debugger if one is attached.

### GDB

If debugging with GDB, you can compile wine-mono with the following options (placed, for example, in your `user-config.make` file):
```
PREFER_DWARF_SYMBOLS=1
MINGW_PATH=/usr/bin
```

`PREFER_DWARF_SYMBOLS=1` configures `make` to use the `-gdwarf4` option and setting `MINGW_PATH=/usr/bin` will use the natively installed GCC MinGW. These combine to allow GDB to make use of XDEBUG, which allows for source level debugging of the C# code.

It also recommended to source `wine-mono/mono/data/gdb/mono-gdb.py` in your `gdbinit` file. For example, by adding the following to `~/.gdbinit`:
```
source <path_prefix>/wine-mono/mono/data/gdb/mono-gdb.py
```

If attaching to a process, ensure the process to which you will attach is ran with the following environment variable:
```
MONO_XDEBUG=gdb
```

This allows for a complete stack trace, which includes the C# code, like the following:

```
(gdb) bt
#0  0x00007ffff7d1ba9a in __GI___libc_read (nbytes=16, buf=0x7ffffe0fea60, fd=8) at ../sysdeps/unix/sysv/linux/read.c:26
#1  __GI___libc_read (fd=8, buf=buf@entry=0x7ffffe0fea60, nbytes=nbytes@entry=16) at ../sysdeps/unix/sysv/linux/read.c:24
#2  0x00007ffff7efd404 in wait_select_reply (cookie=cookie@entry=0x7ffffe0ff9ac) at ../../dlls/ntdll/unix/server.c:329
#3  0x00007ffff7effac6 in server_select (select_op=select_op@entry=0x7ffffe0ffa60, size=size@entry=8, flags=flags@entry=2, abs_timeout=abs_timeout@entry=9223372036854775807, 
    context=context@entry=0x0, user_apc=user_apc@entry=0x7ffffe0ffa00) at ../../dlls/ntdll/unix/server.c:748
#4  0x00007ffff7effbbe in server_wait (select_op=select_op@entry=0x7ffffe0ffa60, size=8, flags=2, timeout=<optimized out>) at ../../dlls/ntdll/unix/server.c:781
#5  0x00007ffff7f0dc59 in NtWaitForMultipleObjects (count=<optimized out>, handles=<optimized out>, wait_any=<optimized out>, alertable=<optimized out>, timeout=<optimized out>)
    at ../../dlls/ntdll/unix/sync.c:1587
#6  <signal handler called>
#7  0x00006fffffc96784 in NtWaitForMultipleObjects () from /usr/local/lib/wine/x86_64-windows/ntdll.dll
#8  0x00006fffff4c5190 in WaitForMultipleObjectsEx (count=count@entry=1, handles=handles@entry=0x11ee60, wait_all=wait_all@entry=0, timeout=<optimized out>, 
    alertable=alertable@entry=0) at ../../dlls/kernelbase/sync.c:56
#9  0x00006fffff4c5ace in WaitForMultipleObjectsEx (alertable=0, timeout=<optimized out>, wait_all=0, handles=0x11ee60, count=1) at ../../dlls/kernelbase/sync.c:365
#10 WaitForSingleObject (handle=<optimized out>, timeout=<optimized out>) at ../../dlls/kernelbase/sync.c:366
#11 0x00006ffff8a7ff3b in wined3d_cs_emit_present (cs=0x71c0040, swapchain=swapchain@entry=0x4b14b00, src_rect=src_rect@entry=0x11ef30, dst_rect=dst_rect@entry=0x11ef40, 
    dst_window_override=<optimized out>, dst_window_override@entry=0x0, swap_interval=<optimized out>, swap_interval@entry=1, flags=<optimized out>, flags@entry=0)
    at ../../dlls/wined3d/cs.c:777
#12 0x00006ffff8ae799d in wined3d_swapchain_present (swapchain=0x4b14b00, src_rect=0x11ef30, src_rect@entry=0x0, dst_rect=0x11ef40, dst_rect@entry=0x0, 
    dst_window_override=dst_window_override@entry=0x0, swap_interval=swap_interval@entry=1, flags=flags@entry=0) at ../../dlls/wined3d/swapchain.c:227
#13 0x00006ffffa03d185 in d3d11_swapchain_present (swapchain=0x4ad63f0, sync_interval=1, flags=<optimized out>) at ../../dlls/dxgi/swapchain.c:326
#14 0x00006ffffa4994cb in D3D11_SwapBuffers (driverData=0x32005d0, sourceRectangle=<optimized out>, destinationRectangle=<optimized out>, overrideWindowHandle=<optimized out>)
    at /home/codeweavers/wine-mono/FNA/lib/FNA3D/src/FNA3D_Driver_D3D11.c:1621
#15 0x000000000674e59b in (wrapper_managed-to-native)_Microsoft.Xna.Framework.Graphics.FNA3D:FNA3D_SwapBuffers (param0=62547344, param1=0, param2=0, param3=52770944)
    at /home/codeweavers/wine-mono/mono/external/corefx/src/Common/src/CoreLib/System/Int32.cs:2892
#16 0x000000000674e49b in Microsoft.Xna.Framework.Graphics.GraphicsDevice:Present (this=...)
    at /home/codeweavers/wine-mono/mono/external/corefx/src/Common/src/CoreLib/System/Int32.cs:2879
#17 0x000000000674e3d3 in Microsoft.Xna.Framework.GraphicsDeviceManager:Microsoft.Xna.Framework.IGraphicsDeviceManager.EndDraw (this=...)
    at /home/codeweavers/wine-mono/mono/external/corefx/src/Common/src/CoreLib/System/Int32.cs:2869
#18 0x000000000674e34f in Microsoft.Xna.Framework.Game:EndDraw (this=...) at /home/codeweavers/wine-mono/mono/external/corefx/src/Common/src/CoreLib/System/Int32.cs:2855
#19 0x0000000006740daa in Microsoft.Xna.Framework.Game:Tick (this=...) at /home/codeweavers/wine-mono/mono/mcs/class/corlib/System/Environment.cs:1724
#20 0x0000000006740653 in Microsoft.Xna.Framework.Game:RunLoop (this=...) at /home/codeweavers/wine-mono/mono/mcs/class/corlib/System/Environment.cs:1509
#21 0x0000000005178d4b in Microsoft.Xna.Framework.Game:Run (this=...) at /home/codeweavers/wine-mono/mono/mcs/class/corlib/System/Environment.cs:637
#22 0x0000000002c614d3 in XNAGame.Test:Main () at /home/codeweavers/XNAGame/XNAGame.cs:142
#23 0x0000000002c61625 in (wrapper_runtime-invoke)_object:runtime_invoke_void (this=<optimized out>, params=<optimized out>, exc=1177192, method=46535760)
    at /home/codeweavers/wine-mono/mono/external/corert/src/System.Private.CoreLib/shared/System/OutOfMemoryException.cs:181
#24 0x00006ffffc4cf4bd in mono_jit_runtime_invoke (method=<optimized out>, obj=<optimized out>, params=0x0, exc=<optimized out>, error=0x11f940)
    at /home/codeweavers/wine-mono/mono/mono/mini/mini-runtime.c:3457
#25 0x00006ffffc6b7021 in do_runtime_invoke (method=method@entry="XNAGame.Test:Main ()", obj=<optimized out>, obj@entry=0x0, params=<optimized out>, params@entry=0x11f8c8, 
    exc=<optimized out>, exc@entry=0x0, error=error@entry=0x11f940) at /home/codeweavers/wine-mono/mono/mono/metadata/object.c:3069
#26 0x00006ffffc6bcafe in mono_runtime_invoke_checked (method="XNAGame.Test:Main ()", obj=0x0, params=0x11f8c8, error=0x11f940)
    at /home/codeweavers/wine-mono/mono/mono/metadata/object.c:3237
#27 0x00006ffffc6bcb59 in do_exec_main_checked (method="XNAGame.Test:Main ()", args=<optimized out>, error=error@entry=0x11f940)
    at /home/codeweavers/wine-mono/mono/mono/metadata/object.c:5220
#28 0x00006ffffc6c0fd6 in mono_runtime_exec_main_checked (error=0x11f940, args=<optimized out>, method=<optimized out>)
    at /home/codeweavers/wine-mono/mono/mono/metadata/object.c:5317
#29 0x00006ffffc523953 in mono_jit_exec_internal (domain=domain@entry=0xb7b070, assembly=assembly@entry=0xbc0690, argc=argc@entry=1, argv=argv@entry=0x3b3c10)
    at /home/codeweavers/wine-mono/mono/mono/mini/driver.c:1395
#30 0x00006ffffc525833 in mono_jit_exec (domain=0xb7b070, assembly=0xbc0690, argc=1, argv=0x3b3c10) at /home/codeweavers/wine-mono/mono/mono/mini/driver.c:1340
#31 0x00006ffffb458baa in _CorExeMain () at ../../dlls/mscoree/corruntimehost.c:1507
#32 0x00006fffffa98e69 in BaseThreadInitThunk (unknown=<optimized out>, entry=<optimized out>, arg=<optimized out>) at ../../dlls/kernel32/thread.c:61
#33 0x00006fffffc96c2b in RtlUserThreadStart () from /usr/local/lib/wine/x86_64-windows/ntdll.dll
#34 0x0000000000000000 in ?? ()
```

## Documentation

Standard .NET namespaces and classes are documented at MSDN here:
<https://learn.microsoft.com/en-us/dotnet/api/?view=netframework-4.8.1>

## Test Suite

Wine Mono includes a test shell which can run tests from Mono and a few
of its own. (TODO: Bring in tests from .NET Core projects?)

The tests can be built using "make tests" in the build tree (they will
be found in wine-mono/tests) or downloaded from
<https://dl.winehq.org/wine/wine-mono/>. The `make tests-zip` target
will build a zip file for running outside the build tree.

To test a Wine Mono build from its source tree, use the `make test`
target.

To run the full test suite in Windows or Wine, use run-tests.exe with no
arguments.

Both of these methods use a default set of -skip-list, -pass-list, and
-fail-list command-line switches to skip certain unreliable tests and to
determine which tests are expected to pass or fail. Since these are only
tested on Esme's machines, GitLab CI, and GitHub CI, and even there they are
unpredictable, expect some unexpected results. The -nodefaults switch
will remove that default set of command-line switches, but it means
running all tests even if they may crash or hang, or be incorrect.

Specific test names can be passed to run-tests.exe as arguments, for
example:

```sh
$ wine tests/run-tests.exe System.Drawing # run all System.Drawing tests
$ wine tests/run-tests.exe x86.System.Drawing # run the System.Drawing tests only on x86
$ wine tests/run-tests.exe MonoTests.System.Drawing.GraphicsTest:Dpi_556181 # run one specific test
```

run-tests.exe can be used in the same way on native Linux Mono, or .NET
on Windows. It can also be used with the native Mono inside a Wine Mono
build tree with the mono-env script:

```sh
$ ./mono-env mono tests/run-tests.exe MonoTests.System.Drawing.GraphicsTest:Dpi_556181
```

Note that this particular Mono environment is only intended for building
Wine Mono components, and may not accurately reflect the state of
upstream Mono. Also, many of the tests only work in a Win32 environment.

Test source code can be found in tools/tests, mono/mono/tests,
mono/mini, and mono/mcs/class/\*/Test. See
<https://www.mono-project.com/community/contributing/test-suite/> for
information on Mono's tests.

### C# interpreter

A C# interactive interpreter is also included with the tests, in the
csharp directory.

## Configuration

### Assembly Overrides

By default, Wine Mono will look for assemblies (.NET dll's) in the following locations in order:
* The Windows GAC (C:\windows\assembly\GAC)
* The Mono GAC (lib/mono/gac in the Wine Mono install)
* The application directory or "private path".

This can be overridden using the WINE_MONO_OVERRIDES environment variable or a registry key.

The value of WINE_MONO_OVERRIDES has the format `name,setting=value;name,setting=value`. `name` is the name of the assembly without the .dll at the end. As a special case, the name may end with a `.*` wildcard or just be `*` to match all assemblies. The settings are `Gac`, `MonoGac`, and `PrivatePath`, and each setting can be 'y' or 'n'. This allows for disabling some search locations for some assemblies.

For example, to never search the Windows GAC for any Microsoft.DirectX dll: `WINE_MONO_OVERRIDES=Microsoft.DirectX.*,Gac=n`

## Microsoft .NET

If you need to use Microsoft's implementation of the .NET Framework, the
Microsoft runtimes can partly run on Wine. You can find tips and share
comments with other users at the [.NET AppDB
page](https://appdb.winehq.org/objectManager.php?sClass=application&iId=2586).

You can install the appropriate version of Microsoft's .NET runtime
(dotnet35, dotnet30, dotnet20, or dotnet11) through
[winetricks](Winetricks). Be aware though, that your .NET
application still might not work (at least not yet), and Microsoft's
.NET runtimes are *not* free software so be sure to read the EULA before
accepting. Wine Mono, on the other hand, is free software and probably a
better choice if it works with your application.

.NET Core and .NET 5.0 and later are different from .NET Framework 4.x
and earlier. They are no longer implemented as an OS component, and as
such they can work just fine alongside Wine Mono, or alongside earlier
.NET Framework versions. Applications relying on .NET Core or 5+ will
usually include the runtime, meaning that it won't be necessary for
users to install it, but the runtime installers should also work fine.

Wine Mono does not make any attempt to implement or replace .NET
Core/5+, nor are there any plans to do so. The architectures are very
different, and there hasn't been demand for a .NET Core/5+ replacement.
