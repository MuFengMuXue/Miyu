In the past, submitting code to wine had a reputation for being
difficult. We're trying several changes to make it easier for people to
contribute code, but one thing we don't want to let go of are high
standards for patches. Although we can't list all of the issues that
might come up, here are a few that drew a lot of attention in the past.

Many of these could theoretically be checked automatically, and there
are already basic scripts floating around for some of them. It hasn't
been discussed yet, but having our testbot check for these down the road
could be a worthwhile project.

## Learn to Love Compiler Warnings

Rather than suppressing compiler warnings by default, it's a good habit
to go the extra mile and fix them whenever possible.
[Gcc](Gcc) and [Clang](Clang) should use identical
(or pretty close) names for their warning options.

Of course, if you use the **-W** flag to return *all* possible warnings
when [Building Wine](Building-Wine) as a whole, that may
swamp you with too many errors at once to be useful. Enabling the
warnings and running `make` in a single directory with changes shouldn't
be overwhelming though:

```sh
$ cd dlls/one-I-changed/
$ make CFLAGS="-W"
```

At the very least, be sure to eliminate any warnings that weren't there
before. Now if you can fix some old warnings in the process, without
adding to the complexity of your patch, that never hurts. One other
small project, if you're looking for ideas for [Submitting
Patches](Submitting-Patches), is to build all of Wine with a
specific warning or set of warnings in mind, then write up simple
changes to fix them.

### Listen to Your Functions

Although not every function returns a value that is critical to your
function, the return values of some functions should always be used. For
example, it is dangerous to not check the return value of a `write()` or
`system()` call, and it's practically useless to throw away the one from
`strtoul()`.

Fortunately, since passing functions and parameters is one thing
compilers are built to understand, you can automatically check during
the build process for functions you should be listening to more
carefully. All you need to do is pass a few warning flags to your
compiler when you build:

```
CFLAGS="-O1 -Wp,-D_FORTIFY_SOURCE=1"    (minimum)
CFLAGS="-O2 -Wp,-D_FORTIFY_SOURCE=2"    (preferred)
```

This should give a warning for every important function call whose
return value is ignored. And don't just nod your head as you pass the
return value to a dummy variable; you really have to listen and process
the return value with the proper tests.

## Set Read-Only Data to const

This task actually isn't too difficult. After compiling whatever files
you're working on, you can use `objdump -x` on the resulting object
files, then cross-reference the *.data* and *.rodata* segments from the
dump. Any variables in *.data* that shouldn't be written to can be set
as `const` in your source, which should place them in *.rodata* once you
rebuild the files. Of course, be sure to fix any new compile warnings
your changes generate too.

After you've made your changes, rebuild and actually **run** your
modified version of wine to test. It's important you do some real-world
testing because a variable incorrectly set as const can often cause
segfaults.

## Avoid Superfluous Casts

Although clarity is a boon most of the time, it can actually be
counter-productive to explicitly cast variables from one type to another
when the compiler (and developers) implicitly understand it. Not only
does it clutter up your lines of code, but more importantly, it can
suppress compiler warnings that will otherwise warn you about casts you
probably *shouldn't* be making.

The most flagrant versions of this revolve around... nothing, as in
`void` functions, `NULL` values, etc. Here's a quick table of what these
look like and how to fix them...

| Description                                        | Solution                            | Before                                          | After                                  |
|----------------------------------------------------|-------------------------------------|-------------------------------------------------|----------------------------------------|
| Cast `void *` return value to another pointer type | Let the compiler cast it implicitly | `(WCHAR *)HeapAlloc(GetProcessHeap(), 0, size)` | `HeapAlloc(GetProcessHeap(), 0, size)` |
| Cast `NULL` to a pointer or handle type            | Let the compiler cast it implicitly | `(HWND)NULL`                                    | `NULL`                                 |
| Cast `NULL` to an integer value or handle          | Just use zero instead               | `(LRESULT)(HTREEITEM)NULL`                      | `0`                                    |

## Dealing with Strings

There are also a few specific rules to keep in mind for strings and
functions that handle them.

### Constants as Character Arrays

Note: This doesn't apply to modules that have been converted to PE format, since those are compiled for a Windows target, for which the compiler will correctly handle long string literals. This still applies to Unix modules.

On Windows, the C compilers will naturally produce Unicode literals of
the format needed by Windows / Wine. However, on unix systems, the
compilers won't necessarily produce strings with the correct format. As
a result, we manually define all "wide" string literals as constant
character arrays.

So instead of passing these string literals to a Unicode-capable
function...

```c
SomeRandomFunctionW( "Hello" );
SomeRandomFunctionW( L"Hello" );
```

You will need to create a constant *WCHAR* array:

```c
static const WCHAR helloW[] = {'H','e','l','l','o',0};
SomeRandomFunctionW( helloW );
```

No, this isn't convenient, but it keeps the code standards-compliant and
portable across build environments. If you'll have a particularly long
string or be entering these regularly, many text editors, such as emacs,
should allow you to setup a macro for automatically converting strings
to these arrays.

### Buffer Allocation

Another thing to watch out for in Wine's Unicode support is the string
size. When allocating buffers for Unicode strings, you should base your
buffer size on

```
sizeof(string)*sizeof(WCHAR)
```

### Function Duplication

In Wine, we shouldn't call any ASCII functions from within Unicode ones.
Not only is the conversion from Unicode to ASCII lossy (if even
possible), but it's actually slower nowadays with most unix systems
supporting Unicode by default.

When Microsoft implemented Unicode support, they decided just to
duplicate every API call that accepts strings, whether directly as a
parameter or within a structure. Then, extra conversion functions were
added to convert between them. Windows also decided on UCS-2 (a
predecessor to UTF-16) rather than UTF-8 for its Unicode strings so
Unicode-compatible functions have names ending with *W* (for "wide" 2
byte characters), while non-Unicode functions (that take strings encoded
in whatever the current codepage is) end in *A* for ANSI.

Because there is no overlap between the two like with UTF-8, you'll need
to use "wide" versions of *every* string function when handling Unicode,
e.g. `strlenW` rather than `strlen`. Any functions that expect
null-terminated strings also require a wide equivalent, since the ANSI
functions are not designed to expect null bytes.

Messages that deal with strings also have A/W versions, and both Wine
and Windows have a good deal of infrastructure for converting between
them as needed. You should always check the encoding of your target
window before sending such messages, though exactly how depends on the
messaging component. Some widgets use the `IsWindowUnicode` function,
while others send a preliminary message to the window to ask what format
it wants.

Because "wide" strings contain embedded null bytes, you can't print them
with a normal printf, which is used by [Winedbg](Commands/winedbg). If
you need to inject a "wide" string into a debug message, we've written a
special conversion function `debugstr_w` that you can use like this:

```c
TRACE("this is a wide string: %s\n", debugstr_w(widestr));
```

## Handling Duplicate Code

When working on a problem that's similar to one addressed elsewhere,
"cut-and-paste" coding can be a kludgy but very effective way to
prototype. The goal should always be to minimize duplication in your
patches though, bundling common code into distinct modules whenever
possible. That said, you can have situations where the current structure
of the source or the build process would make this kind of refactoring a
significant project.

In developing wine, we've come across a few situations like this, where
refactoring still isn't expedient. So in the meanwhile, we try to at
least keep the code in sync. Here is a list of current "cut-and-paste"
relationships in the wine source tree:

| Purpose                                          | File A                                                                                                  | File B                                                                                                              | Current Status                                                       |
|--------------------------------------------------|---------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------|
| Demangle VC++ symbols into C function prototypes | [dlls/msvcrt/undname.c](https://gitlab.winehq.org/wine/wine/-/blob/HEAD/dlls/msvcrt/undname.c)         | [tools/winedump.msmangle.c](https://gitlab.winehq.org/wine/wine/-/blob/HEAD/tools/winedump/msmangle.c)             | Memory allocation needs to be rewritten to allow for a complete sync |
| Read dwarf2 info from ELF modules                | [dlls/dbghelp/dwarf.c](https://gitlab.winehq.org/wine/wine/-/blob/HEAD/dlls/dbghelp/dwarf.c)           | [dlls/ntdll/signal_x86_64.c](https://gitlab.winehq.org/wine/wine/-/blob/HEAD/dlls/ntdll/signal_x86_64.c)           | 100% synced since 27 Mar 2010                                        |
| Use the minidump method for debug info           | [tools/winedump/minidump.c](https://gitlab.winehq.org/wine/wine/-/blob/HEAD/tools/winedump/minidump.c) | [programs/winedbg/tgt_minidump.c](https://gitlab.winehq.org/wine/wine/-/blob/HEAD/programs/winedbg/tgt_minidump.c) | 100% synced since 29 Aug 2015                                        |

Remember that these duplications are seen as necessary evils, but if you
sincerely believe something similar is the best solution for your
problem at the moment, definitely discuss it with the other developers
on the [wine developers' mailing
list](https://list.winehq.org/mailman3/postorius/lists/wine-devel.winehq.org/). Also, if you
do get your patch submitted, please add an entry for your duplication to
the above table.

## Debug Info in Critical Sections

If you ever need to implement or improve a `CRITICAL_SECTION` in wine,
you should definitely set some debug info from the very get-go. This
applies to both static `CRITICAL_SECTION` instances ...

```c
static CRITICAL_SECTION foo_cs;
static CRITICAL_SECTION_DEBUG foo_cs_debug =
{
    0, 0, &foo_cs,
    { &foo_cs_debug.ProcessLocksList,
      &foo_cs_debug.ProcessLocksList },
    0, 0, { (DWORD_PTR)(__FILE__ ": foo_cs") }
};
static CRITICAL_SECTION foo_cs = { &foo_cs_debug, -1, 0, 0, 0, 0 };
```

... and dynamic ones (which happen to look much neater)

```c
CRITICAL_SECTION cs;
InitializeCriticalSection(&cs);
if (name.DebugInfo) name.DebugInfo->Spare[0] = (DWORD_PTR)(__FILE__ ": cs");
```

Of course, don't forget to do the right thing for your dynamic variables
and unset `DebugInfo` before deleting the variable

```c
if (name.DebugInfo) name.DebugInfo->Spare[0] = 0;
DeleteCriticalSection(&cs);
```

Keep in mind that not all `CRITICAL_SECTION` objects use these exact
constructors and destructors

## 16-bit Separation

Wine supports old 16-bit executables, but since many users might not be
interested in this feature, we have a build option to disable it:
`--disable-win16`. However, especially in its early versions, wine had a
significant amount of overlap between its 16 and 32-bit functions.

This shouldn't be nearly as much of a problem now (it might be resolved
entirely), but any changes should respect the separation so be sure that
your submission:

- Places code for 16-bit support in its own file in the appropriate
  16-bit dll
- Doesn't call 16-bit DLLs from a 32-bit one (with `LoadLibrary16` or
  `GetModuleHandle16`)
- Doesn't use a 16-bit include file for any 32-bit code
- Doesn't implement a 16-bit function in a file for 32-bit code

If you come across what you believe is a necessary exception, you can
always discuss it on the wine developer's mailing list.

## See Also

- [Developer FAQ](Developer-FAQ)
- [Developer Hints](Developer-Hints)
