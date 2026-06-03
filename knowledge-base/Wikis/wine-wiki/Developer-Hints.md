This document should help new developers get started.

## Source tree structure

*See [Source Tree Structure](Source-Tree-Structure) page.*

## Implementing new API calls

This is the simple version, and covers only Win32. Win16 is slightly
uglier, because of the Pascal heritage and the segmented memory model.
All of the Win32 APIs known to Wine are listed in the .spec file of
their corresponding dll. An unimplemented call will look like (from
`gdi32.spec`)

```
@ stub PolyPatBlt
```

To implement this call, you need to do the following four things:

1. Find the appropriate parameters for the call, and add a prototype to
the correct header file. In this case, that means `include/wingdi.h`,
and it might look like

```c
BOOL WINAPI PolyPatBlt(HDC, LPCVOID, DWORD);
```

If the function has both an ASCII and a Unicode version, you need to
define both and add a `#define WINELIB_NAME_AW` declaration. See
below for discussion of function naming conventions.

2. Modify the .spec file to tell Wine that the function has an
implementation, what the parameters look like and what Wine function to
use for the implementation. In Win32, things are simple--everything is
32-bits. However, the relay code handles pointers and pointers to
strings slightly differently, so you should use `str` and `wstr` for
strings, `ptr` for other pointer types, and `long` for everything else:

```
@ stdcall PolyPatBlt(long ptr long)
```

The `PolyPatBlt` at the end of the line is which Wine function to use
for the implementation.

3. Implement the function as a stub. Once you add the function to the
.spec file, you must add the function to the Wine source before it will
link. Add a function called `PolyPatBlt` somewhere. Good things to put
into a stub:

 -  a correct prototype, including the WINAPI
 -  header comments, including full documentation for the function and
    arguments
 -  A FIXME message and an appropriate return value are good things to
    put in a stub. NOTE: When submitting documentation changes, you must
    clearly state that when creating your patch that you did not copy
    the function documentation from MSDN. When implementing a new
    function it is fine to look at the API documentation on MSDN however
    the api documentation must be written in your own words.

```c
/************************************************************
 *                    PolyPatBlt   (GDI32.@)
 *
 * Draw many Bezier curves.
 *
 * PARAMS
 *   hdc   [I] Device context to draw to
 *   p     [I] Array of POINT structs
 *   count [I] Number of points in p
 *
 * RETURNS
 *   Success: Non-zero.
 *   Failure: FALSE. Use GetLastError() to find the error cause.
 *
 * BUGS
 *   Unimplemented
 */
BOOL WINAPI PolyPatBlt(HDC hdc, LPCVOID p, DWORD count)
{
    /* tell the user they've got a substandard implementation */
    FIXME("(%x,%p,%d): stub\n", hdc, p, count);
    /* some programs may be able to compensate,
     * if they know what happened
     */
    SetLastError(ERROR_CALL_NOT_IMPLEMENTED);
    return FALSE;    /* error value */
}
```

4. Implement and test the rest of the function:

 -  Add a test to the Wine test suite, when possible.
 -  Learn from the test results, what Windows does (MSDN is sometimes
    incomplete or wrong).
 -  It's a good idea to ask for test results for other Windows versions
    in wine-devel.
 -  Try to limit the supported formats/versions in a function for a
    single patch.
 -  Add support for additional formats/versions in the next patches,
    when needed.

## Implementing a new DLL

### Generic directions

Apart from writing the set of needed .c files, you also need to do the
following:

1.  Create a directory `<MyDll>` where to store the implementation of
    the DLL. This directory has to be put under the `dlls/` directory.
    If the DLL exists under Windows also as a 16 bit DLL, use a seperate
    directory with `16` added to the extension for the 16 bit
    implementation (Example: `<MyDll.dll16>`).
2.  Create the `Makefile.in` in the `./dlls/<MyDll>/` directory. You
    can copy an existing `Makefile.in` from another `./dlls/`
    subdirectory. You need at least to change the `MODULE` and
    `SOURCES` macros.
3.  Create the .spec file for the DLL exported functions in your
    directory. Refer to [Implementing new API
    calls](#implementing-new-api-calls)
    earlier in this document for more information on this part.
4.  **Important note, when using git:** you must do `git add
    dlls/<MyDll>/Makefile.in` before you call
    `./tools/make_makefiles`, or make_makefiles won't know about
    your dll
5.  Call `./tools/make_makefiles` from the top of the Wine tree. Your
    new dll is now integrated in the Wine build environment. Verify this
    by making sure the name of your dll directory appears in
    configure.ac.
6.  If you added new test(s) in configure.ac, run `autoheader` to add
    the needed variables to include/config.in.h
7.  Regenerate the configure script with `autoconf`.
8.  Run `./configure` from the top of the Wine tree. You should now
    have a `Makefile` file in `./dlls/<MyDll>/`
9.  To include a Windows DLL in the official Wine tree, please submit
    the smallest possible implementation first:
    1.  only "DllMain" in a single .c file
    2.  the .spec file with the exported functions declared as stub
    3.  your `Makefile.in`
    4.  **do not include any autogenerated source**
10. You can now start adding .c files. For the .h files, if they are
    standard Windows one, put them in `include/`. If they are linked
    to **your** implementation of the dll, put them in your newly
    created directory
11. Pick only one function or a small set of functions for a patch:
    - reduced patch size
    - reduced complexity
    - increased motivation to review

- Add a set of [tests](#adding-a-tests-directory) as explained below

- **You should not include any autogenerated source**, that was created
from 'autoconf' or a tool inside 'tools/' (`make_makefiles` or
`winedump` as examples), when you submit your merge request.

### Debug channels

If you need to create a new debug channel, just add

```c
#include "wine/debug.h"
```

and macro

```c
WINE_DEFAULT_DEBUG_CHANNEL(mydll)
```

to your .c file(s), and use them (the preferred name for the
debug-channel is your DLL name). All the housekeeping will happen
automatically.

See the examples in [Debug Messages](#debug-messages) later in this
Document.

### Makefiles

The Makefile.in is a bit different from the generated Makefile. Have a
good look at an example and use the right values otherwise it won't
necessarily be recognised. If your `.dlls/<MyDll>/<MyDll>.spec`
exports any functions then you need a

```
IMPORTLIB = <MyDll>
```

statement. Otherwise leave it out as you will get warnings that the dll
does not export anything.

### Resources

If you also need to add resources to your DLL, then create the .rc file.
Add to your `./dlls/<MyDll>/Makefile.in`, in the `SOURCES` macro, the
list of .rc files to add to the DLL. See `dlls/comctl32/` for an example
of this.

## Adding a tests directory

If you want to add tests to an existing dll and there is already a tests
directory things should be clear enough. However if the dll does not yet
have a tests subdirectory you will need to add one and set it up.

1.  In the dll's subdirectory create a subdirectory named `tests`.
2.  In that tests subdirectory copy a `Makefile.in` from some other
    tests subdirectory and edit it.
      - Change the TESTDLL to the dll you are testing
      - Change the IMPORTS to the dll you are testing and also anything
        it requires
      - EXTRALIBS is sometimes needed (if the DLL uses COM for instance)
      - Change the SOURCES entry to the list of c source files you will
        provide containing the tests.
3.  Write the c source files that you added to the SOURCES entry above.
4.  **Important note, when using git:** `Makefile.in` must be added to
    the index before you call `./tools/make_makefiles`
5.  Call `./tools/make_makefiles` from the top of the Wine tree. Your
    new tests are now integrated in the Wine build environment
6.  Regenerate the configure script with `autoconf`.
7.  Run `./configure` from the top of the Wine tree. You should now have
    a `Makefile` file in `./dlls/<MyDll>/tests/`.
8.  You should now be able to run `make`.
9.  With a recent Cross-Compiler (MinGW), you can build your tests as
    Windows binary.
10. Make sure that your tests works without failure on different systems.
    (Windows and Wine, and there is a `todo_wine` macro).
11. Ask other people for help to run your tests.
12. You should not include any autogenerated code, that was created from
    `autoconf` or a tool inside `tools/` (`tools/make_makefiles` as
    example), when you submit your merge request.

## Writing conformance tests

Wine uses test-driven development to a large extent; we write a test,
make sure it passes on Windows, and then get it to pass on Wine by
fixing Wine.

See the [Wine Developer's Guide](Wine-Developer's-Guide) section on
the [writing of Conformance
Tests](Wine-Developer's-Guide/Writing-Conformance-Tests) for the
details.

See also [Conformance Tests](Conformance-Tests) for more notes.

## Memory and segments

NE (Win16) executables consist of multiple segments. The Wine loader
loads each segment into a unique location in the Wine processes memory
and assigns a selector to that segment. Because of this, it's not
possible to exchange addresses freely between 16-bit and 32-bit code.
Addresses used by 16-bit code are segmented addresses (16:16), formed by
a 16-bit selector and a 16-bit offset. Those used by the Wine code are
regular 32-bit linear addresses.

There are three ways to obtain a segmented pointer:

1.  Using the MapLS function (recommended).
2.  Allocate a block of memory from the global heap and use
    `WIN16_GlobalLock` to get its segmented address.
3.  Declare the argument as `segptr` instead of 'ptr' in the spec file
    for a given API function.

Once you have a segmented pointer, it must be converted to a linear
pointer before you can use it from 32-bit code. This can be done with
the `MapSL` function. The linear pointer can then be used freely with
standard Unix functions like `memcpy()` etc. without worrying about 64k
boundaries. Note: there's no easy way to convert back from a linear to a
segmented address.

In most cases, you don't need to worry about segmented address, as the
conversion is made automatically by the callback code and the API
functions only see linear addresses. However, in some cases it is
necessary to manipulate segmented addresses; the most frequent cases
are:

1.  API functions that return a pointer
2.  lParam of Windows messages that point to a structure
3.  Pointers contained inside structures accessed by 16-bit code.

It is usually a good practice to used the type `SEGPTR` for segmented
pointers, instead of something like `LPSTR` or `char *`. As `SEGPTR` is
defined as a `DWORD`, you'll get a compilation warning if you mistakenly
use it as a regular 32-bit pointer.

## Structure packing

By default both Microsoft and gcc compilers align structure members
(e.g. WORDs are on a WORD boundary, etc.). This means that a structure
like

```c
struct { BYTE x; WORD y; };
```

will take 4 bytes, because a compiler will add a dummy byte between x
and y. Sometimes to have the correct layout for structures used by
Windows code, you need to embed the struct within two special
\#include's which will take care of the packing for you:

```c
#include "pshpack1.h"
struct { BYTE x; WORD y; };
#include "poppack1.h"
```

For alignment on a 2-byte boundary, there is a `pshpack2.h`, etc.

## Naming conventions for API functions and types

In order to support both Win16 and Win32 APIs within the same source
code, the following convention must be used in naming all API functions
and types. If the Windows API uses the name 'xxx', the Wine code must
use:

```
 'xxx16'   for the Win16 version,
 'xxx'     for the Win32 version when no strings are involved,
 'xxxA'    for the Win32 version with ASCII strings,
 'xxxW'    for the Win32 version with Unicode strings.
```

If the function has both ASCII and Unicode version, you should then use
the macros `WINELIB_NAME_AW(xxx)` or `DECL_WINELIB_TYPE_AW(xxx)`
(defined in `include/windef.h`) to define the correct 'xxx' function or
type for Winelib. When compiling Wine itself, 'xxx' is *not* defined,
meaning that code inside of Wine must always specify explicitly the
ASCII or Unicode version.

If 'xxx' is the same in Win16 and Win32, you can simply use the same
name as Windows, i.e. just 'xxx'. If 'xxx' is Win16 only, you could use
the name as is, but it's preferable to use 'xxx16' to make it clear it
is a Win16 function.

For example:

```c
typedef struct { /* Win32 ASCII data structure */ } WNDCLASSA;
typedef struct { /* Win32 Unicode data structure */ } WNDCLASSW;
typedef struct { /* Win16 data structure */ } WNDCLASS16;
DECL_WINELIB_TYPE_AW(WNDCLASS);
ATOM RegisterClass16( WNDCLASS16 * );
ATOM RegisterClassA( WNDCLASSA * );
ATOM RegisterClassW( WNDCLASSW * );
#define RegisterClass WINELIB_NAME_AW(RegisterClass)
```

The Winelib user can then say:

```c
WNDCLASS wc = { ... };
RegisterClass( &wc );
```

and this will use the correct declaration depending on the definition of
the UNICODE symbol.

## Debug messages

To display a message only during debugging, you normally write something
like this:

```c
TRACE("abc...\n");
FIXME("abc...\n");
WARN("abc...\n");
ERR("abc...\n");
```

depending on the seriousness of the problem. You need to declare the
debug channel name at the top of the file (after the includes) using the
`WINE_DEFAULT_DEBUG_CHANNEL` macro, like so:

```c
WINE_DEFAULT_DEBUG_CHANNEL(win);
```

If your debugging code is more complex than just printf, you can use the
macros:

```c
TRACE_ON(xxx), WARN_ON(xxx), ERR_ON(xxx) and FIXME_ON(xxx)
```

to test if the given channel is enabled. Thus, you can write:

```c
if (TRACE_ON(win)) DumpSomeStructure(&str);
```

Don't worry about the inefficiency of the test. If it is permanently
disabled (that is `TRACE_ON(win)` is 0 at compile time), the compiler
will eliminate the dead code.

For more info about debugging messages, see the [corresponding
chapter](Wine-Developer's-Guide/Debug-Logging) in the developer's
guide.

## Translating resource files

Nowadays Wine is completely localized through standard gettext PO
files.  If you check out the Wine source you will find these in the
[po/](https://gitlab.winehq.org/wine/wine/-/tree/master/po)
directory. See the [Translating](Translating) page for more details.

## Using only C89-compliant code

  - *See also [Code guidelines](Submitting-Patches#code-guidelines)*

For compatibility with a wide range of compilers (both new and old),
code in Wine should be written to the original C89 standard (where
possible) with portability in mind:

  - Use only C-style comments, not C++ ones (use `/* */`, never `//`)
  - Use `void` when defining parameter-less functions

```c
int foo() { }                   /* Incorrect */
int foo(void) { }               /* Much better */
```

  - Always put variable declarations at the beginning of a block

```c
int bar1(void)
{
    do_something();
    int number1 = 5;            /* Not C89 compliant */
}

int bar2(void)
{
    int number2 = 17;           /* Much better */
    int number3 = 550;          /* Ditto */
    do_something();
}
```

  - Avoid all compiler extensions

```c
ch += offset ?: size            /* GCC-specific extension */
dh += offset ? offset : size    /* Standards compliant */
```

  - Use types with standard definitions

```c
long wrong;                     /* long is different in Win64 and Unix64 */
LONG right;                     /* LONG is the same on both platforms */
```

  - Use WCHAR and array syntax for Unicode string literals in non-PE
    modules ([helpful
    tool](https://gitlab.com/mywinetools/mywinetools/raw/master/wstr.py))

```c
const WCHAR str1[] = L"Hello";  /* Preferred on PE modules. But it won't compile on non-PE modules.*/
const WCHAR str2[] = {          /* Tedious, but correct */
    'H','e','l','l','o',0
};
```

## More info

  - Win32 API documentation on MSDN: <http://msdn.microsoft.com/>
  - Analyse by Geoff Chappell: <http://www.geoffchappell.com/>
  - <http://www.sonic.net/~undoc/bookstore.html>
  - <http://www.geocities.com/SiliconValley/4942/>
  - Undocumented Windows 2000 Secrets : <http://undocumented.rawol.com/>
  - In 1993 Dr. Dobbs Journal published a column called "Undocumented
    Corner".
  - <http://msdn2.microsoft.com/en-us/library/cc230273.aspx> - Windows
    Data Types
