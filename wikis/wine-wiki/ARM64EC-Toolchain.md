This document is meant to describe how ARM64EC code is compiled and
linked. There is a limited official documentation available: [Overview
of ARM64EC ABI
conventions](https://learn.microsoft.com/en-us/cpp/build/arm64ec-windows-abi-conventions)
and [Understanding Arm64EC ABI and assembly
code](https://learn.microsoft.com/en-us/windows/arm/arm64ec-abi). Please
read it before continuing to get an overview of the ABI. This document
focuses on how the compiler and linker work and interact with each other
to produce ARM64EC executables.

DISCLAIMER: It's mostly based on experimentation with MSVC by feeding it
with various test cases and analysing results. Presented reasoning for
the observed behaviour is just a best guess and should be treated as
such.

## CHPE metadata

The output of ARM64EC linking is a PE file that uses x86_64 as a machine
type (it's different for [ARM64X](#arm64x)). Its headers are
valid x86_64 PE headers and it may be distinguished from pure x86_64
module by presence of CHPE metadata pointer in its load config. CHPE
metadata is a
[structure](https://llvm.org/doxygen/structllvm_1_1object_1_1chpe__metadata.html)
containing:

- [A code map](#code-layout)
- [Entry point and redirection metadata](#entry-points)
- [Auxiliary IAT](#importlibs)
- [Extra RFE table](#exception-data)
- A number of pointers that loader fills with runtime support functions

CHPE metadata structure is provided by CRT libs. It references a number
of synthetic symbols provided by linker (see [Code
layout](#code-layout), [Exception
data](#exception-data), [Entry
points](#entry-points), [Importlibs](#importlibs))
to provide the necessary information for the system loader and emulator.

## Mixing ARM64EC and x86_64 code

ARM64EC has an unique feature that allows porting code from x86_64 to
ARM64 one object file at a time. This implies that the linker must be
able to link a mixture of x86_64 and ARM64EC code within a single
module, where they may call each other. An important implication of that
is that any time ARM64EC function calls an external symbol, it needs to
be prepared for the fact that the function may be implemented in x86_64
code in which case the call needs to be thunked to emulator.

## Code layout

Mixing data sections among architectures is generally fine and linker
doesn't do any attempt to separate them. However, code sections need
additional linker attention. Code chunks within a section are sorted
according to their [range
type](https://llvm.org/doxygen/namespacellvm_1_1object.html#af5be62ab63193e82a4329358fe5d3cec):

- Arm64: pure ARM64 code, see [ARM64X](#arm64x)
- Arm64EC: ARM64 code built in EC mode
- Amd64: x86_64 code

Additionally, after sorting, linker applies additional 4KB alignment to
code range boundaries. This is probably meant to make it easy for JIT
engine to watch for writes in relevant parts of the code.

Linker then constructs a code map in a form of an array of [code range
entry](https://llvm.org/doxygen/structllvm_1_1object_1_1chpe__range__entry.html)
structs containing RVA of start of the range, range length and range
type. It sets `__hybrid_code_map` symbol to the first entry of the map
and `__hybrid_code_map_count` symbol to number of map entries. Those
symbols are used by CHPE metadata.

Example (disassembler output stripped to important parts):

    $ cat aarch64-func.s
        .text
        .globl arm64_func
        .p2align 2, 0x0
    arm64_func:
        mov w0, #0
        ret
    $ cat arm64ec-func.s
        .text
        .globl arm64ec_func
        .p2align 2, 0x0
    arm64ec_func:
        mov w0, #1
        ret
    $ cat x86_64-func.s
        .text
        .globl x86_64_func
        .p2align 2, 0x0
    x86_64_func:
        movl $2, %eax
        retq
    $ llvm-mc -filetype=obj -triple=aarch64-windows aarch64-func.s -o aarch64-func.obj
    $ llvm-mc -filetype=obj -triple=arm64ec-windows arm64ec-func.s -o arm64ec-func.obj
    $ llvm-mc -filetype=obj -triple=x86_64-windows x86_64-func.s -o x86_64-func.obj
    $ link -dll -machine:arm64x -noentry -out:test.dll x86_64-func.obj arm64ec-func.obj aarch64-func.obj msvcrt.lib
    $ llvm-objdump -d test.dll

    test.dll:       file format coff-arm64x

    Disassembly of section .text:

    0000000180001000 <.text>:
    180001000: 52800000     mov     w0, #0x0                // =0
    180001004: d65f03c0     ret
                    ...
    180002000: 52800020     mov     w0, #0x1                // =1
    180002004: d65f03c0     ret
                    ...
    180003000: b8 02 00 00 00               movl    $0x2, %eax
    180003005: c3                           retq
                    ...

    $ llvm-readobj --coff-load-config test.dll
    ...
    CHPEMetadata [
      Version: 0x1
      CodeMap [
        0x1000 - 0x1014  ARM64
        0x2000 - 0x2074  ARM64EC
        0x3000 - 0x3046  X64
      ]
      ...
    ]

Side note: Sections containing only empty chunks are discarded by
linker. This is true on all architectures, but on ARM64EC MSVC still
emits a code map entries for discarded sections with 0 length and RVA
occupied by the next non-discarded section.

Side note: Code map on MSVC link.exe is apparently generated before
range extension thunk. If a range extension thunk is added after the
last chunk in range, it will end up out of any range in the code map.

## Exception data

ARM64EC object files use the same `.pdata` section format as ARM64,
which differs from that of x86_64. Linker separates them and exposes
only x86_64 variant in PE header (in a spirit of PE headers being valid
x86_64 headers). It also sets `__arm64x_extra_rfe_table` symbol to
exception data in ARM64 format and `__arm64x_extra_rfe_table_size` to
size of that data. Those symbols are used by CHPE metadata.

On [ARM64X](#arm64x) this applies to x86_64 header, ARM64
header uses ARM64 format.

## x86_64 thunks

ARM64EC aims to support x86_64 applications that do hotpatching. For
example web browsers use patching for sandboxing, Microsoft Office uses
patching for virtualization, games anti-cheat/DRM protections use
patching for their protection schemes. Such patchers need a limited
knowledge about the patched function's machine code and, since such
applications are unaware of ARM code, they would be unable to properly
patch ARM64EC machine code. That's why linker generates simple x86_64
thunks with canonical prologue that just jumps to EC function. Those
chunks are put into `.hexpthk` section:

    movq    %rsp, %rax
    movq    %rbx, 0x20(%rax)
    pushq   %rbp
    popq    %rbp
    jmp ec_func
    int3
    int3

Target of the jump is an address of ARM64EC code (see [Entry
thunks](#entry-thunks) for how such jumps work). Such chunks
are created by linker for [entry points](#entry-points) and
[patchable functions](#patchable-functions). x86_64 chunks
may be referenced by symbols with `EXP+` prefix, for example a thunk of
function `func` (with ARM64EC implementation symbol `#func`) uses symbol
`EXP+#func`.

x86_64 thunks have additional metadata associated that loader and
emulator may use for optimizations. In fact, under usual conditions,
those thunks may be skipped in runtime if the caller is also EC code and
target function may be called directly. In case of imported symbols,
this is realized by [auxiliary IAT](#importlibs). For
[patchable functions](#patchable-functions), this needs an
explicit runtime check. If OS emulator notices that the function was
patched, then all subsequent calls will go through the chunk, even if
they were pure EC calls before patching.

Metadata contains:

- Code range to entry point table. Linker generates an array of [CHPE
  code
  range](https://llvm.org/doxygen/structllvm_1_1object_1_1chpe__code__range__entry.html)
  entries. Each entry contains a region start and end RVAs of x86_64
  thunk and RVA the same thunk as entry point. It means that `StartRva`
  and `EntryPoint` are equal. Linker sets
  `__x64_code_ranges_to_entry_points` symbol to the first entry and
  `__x64_code_ranges_to_entry_points_count` symbol to entry count.

- Redirection metadata. Linker generates an array of [CHPE redirection
  entries](https://llvm.org/doxygen/structllvm_1_1object_1_1chpe__redirection__entry.html).
  Each entry contains RVA of x86_64 thunk as a source and RVA of EC
  function (`ec_func` in the above example) as a destination. Linker
  sets `__arm64x_redirection_metadata` symbol to the first entry and
  `__arm64x_redirection_metadata_count` symbol to entry count.

Example:

    $ cat test.c
    void test(void) {}
    $ cl -arm64EC -c test.c
    $ link -out:test.dll -machine:arm64ec -dll -noentry test.obj -export:test
    $ llvm-objdump -d --section=.hexpthk test.dll

    test.dll:       file format coff-arm64ec

    Disassembly of section .hexpthk:

    0000000180004000 <test>:
    180004000: 48 8b c4                     movq    %rsp, %rax
    180004003: 48 89 58 20                  movq    %rbx, 0x20(%rax)
    180004007: 55                           pushq   %rbp
    180004008: 5d                           popq    %rbp
    180004009: e9 0a e0 ff ff               jmp     0x180002018
    18000400e: cc                           int3
    18000400f: cc                           int3

    $ llvm-readobj --coff-load-config test.dll
    ...
      CodeRangesToEntryPoints [
        0x4000 - 0x4010 -> 0x4000
      ]
      RedirectionMetadata [
        0x4000 -> 0x2018
      ]
    ...

## Entry points

For each EC function exported from PE file and PE entry point, linker
generates [x86_64 thunks](#x86_64-thunks) and uses that in PE
header and export table. Loader may use associated metadata to figure
out ARM64EC function and fill [auxiliary IAT](#importlibs) of
importing module if needed.

Side note: If EC function is expoted as data (replacing `-export:test`
with `-export:#test,DATA` in the above example), x86_64 thunk will not
be generated, so patching will not work, but it's still possible to call
such function from both EC and x86_64 code (see [Entry
thunks](#entry-thunks)).

## .hybmp\$x section

EC object files have a special section called `.hybmp$x`, which contains
a list of thunks. It's an array of entries containing three 32-bit
values: function symbol index, thunk symbol index and thunk type. Thunk
type may be one of:

- 0: [Guest exit thunks](#guest-exit-thunks)
- 1: [Entry thunks](#entry-thunks)
- 4: [Exit thunks](#exit-thunks)

Example:

    $ cat extcall.c
    extern void extfunc(void);
    void func(void) { extfunc(); }
    $ dumpbin -all extcall.obj
    ...
    HYBRID INFO MAP:

      Offset           Type             From       To
     --------  ---------------------  --------  --------
     00000000  exitthunk_to_guest            E        16  #extfunc$exit_thunk -> extfunc
     0000000C  native_to_entrythunk         15        11  #func -> $ientry_thunk$cdecl$v$v
     00000018  native_to_icall_thunk        16        12  extfunc -> $iexit_thunk$cdecl$v$v
     00000024  native_to_icall_thunk        16        12  extfunc -> $iexit_thunk$cdecl$v$v
    ...

## Symbol namespace

Function symbols in ARM64EC have additional complication comparing to
usual targets. During compilation, compiler doesn't know if an external
function will be ARM64EC or x86_64 code. ARM64EC introduces additional
symbol mangling. Mangled C functions have `#` prefix before function
name or additional `$$h` component for C++ functions.

Since x86_64 code has no knowledge about ARM64EC nor its symbol
mangling, it always uses unmangled symbols. Whenever ARM64EC code uses
an unmangled symbol, it needs to treat it as a possibly emulated
function and needs to be prepared to perform a call to the emulator if
that's the case (see [Exit thunks](#exit-thunks) and [Guest
exit thunks](#guest-exit-thunks)).

Mangled functions are used only in ARM64EC object files. They are an
addition to unmangled symbol: every function symbol used by ARM64EC code
has both mangled and unmangled form. They may be aliases to each other,
but may be separated things. Unlike unmangled symbols (which may be
x86_64), mangled symbols are always directly callable from ARM64EC code.

This convention is maintained almost entirely by the compiler. Linker
has very little understanding of mangled symbols. In many cases,
compiler emits weak antidependency symbols to achieve that.
Antidependency symbols are very similar to weak references, but they
don't allow chaining, so cyclic references are not a problem when they
happen.

When a non-patchable function `func` is implemented in ARM64EC object
file, the compiler uses symbol `#func` for its implementation and adds
an antidependency symbol, which links `func` to `#func`. In this case
both symbols are essentially equal.

However, in other cases those symbols may be different, see [Guest exit
thunks](#guest-exit-thunks) and [Patchable
functions](#patchable-functions) for such cases. Whenever
compiler needs a function address, it uses the unmangled symbol to make
sure that the pointer is the actual function, not a thunk. Similarly,
when compiler performs a function call, it uses a mangled symbol. It may
end up linking to a thunk instead of the actual function, but it
guarantees EC code will not try to jump directly to x86_64 code.

## Entry thunks

As mentioned by [Overview of ARM64EC ABI
conventions](https://learn.microsoft.com/en-us/cpp/build/arm64ec-windows-abi-conventions),
the compiler generates a special entry thunks that emulator may use
whenever ARM64EC function is called from x86_64 code. The compiler puts
those thunks in a section called `.wowthk$aa` and adds an entry to
`.hybmp$x` section.

When linker pulls a function from an object file, it checks if it has an
entry thunk. When it does, it pulls entry thunk as well. It then adds an
extra padding to function code and places an offset to entry thunk
there. It means that in the final executable for function `func`, the
offset is at `#func-4` address. RVA of the thunk may be calculated from
function address:
`thunk_rva = rva(#func) + ((uint32_t *)#func)[-1] - 1`.

This is enough for emulator to be able to call ARM64EC function. It
knows from the code map that when there is an attempt to jump to `#func`
address from x86_64, it's ARM64EC call. It may then retrieve entry thunk
offset from `#func-4` address and use it to perform the call (TODO: CFG
validation). Since this is enough for x86_64 to ARM64EC calls to work,
it's fine to alias unmangled symbols to mangled ones (see [Symbol
namespace](#symbol-namespace)).

## Exit thunks

As mentioned by [Overview of ARM64EC ABI
conventions](https://learn.microsoft.com/en-us/cpp/build/arm64ec-windows-abi-conventions),
the compiler generates a special exit thunk that's used whenever ARM64EC
code needs to call emulator to execute x86_64 code. The compiler puts
this code in a section called `.wowthk$aa` and adds an entry to
`.hybmp$x` section.

An example of exit thunk use is whenever ARM64EC code needs to call a
function pointer (see [Guest exit
thunks](#guest-exit-thunks), [Patchable
functions](#patchable-functions) and
[Importlibs](#importlibs) for other use cases). In this case,
instead of calling the pointer directly, compiler will use
`__os_arm64x_dispatch_icall`. `__os_arm64x_dispatch_icall` takes a
targget function as an argument in `x11` and exit thunk in `x10`. The
thunk then calls the address from `x11`. If target function ARM64EC
code, `__os_arm64x_dispatch_icall` will just leave `x11` unchanged.
Otherwise, it will replace it with a thunk that calls the emulator.

Example:

    $ cat ptrcall.c
    extern void (*fptr)(void);
    void ptrcall(void) { fptr(); }
    $ cl -c -arm64EC ptrcall.c -FA
    $ cat ptrcall.asm
    ...
    |#ptrcall| PROC
    ; File ptrcall.c
    ; Line 2
    |$LN3|
            stp         fp,lr,[sp,#-0x10]!
            mov         fp,sp
            adrp        x8,__os_arm64x_dispatch_icall
            ldr         x9,[x8,__os_arm64x_dispatch_icall]
            adrp        x8,fptr
            ldr         x11,[x8,fptr]
            adrp        x8,|$iexit_thunk$cdecl$v$v|
            add         x10,x8,|$iexit_thunk$cdecl$v$v|
            blr         x9
            blr         x11
            ldp         fp,lr,[sp],#0x10
            ret

            ENDP  ; |#ptrcall|
    ...

## Guest exit thunks

When ARM64EC compiler encounters an external function call, it can not
assume that the target is ARM64EC as well, it may be x86_64 function.
While in theory it could always use `__os_arm64x_dispatch_icall` for
direct calls like it does for function pointers, it would be quite
inefficient in cases when the target is ARM64EC code. Instead, it just
calls the mangled symbol, generates yet another thunk and setups symbols
in a way that allows linker to do the right thing at link time, when
more information is available.

Using a simple example:

    // build: cl -c -arm64EC extcall.c -FA
    extern void extfunc(void);
    void func(void) { extfunc(); }

`func` just calls `#extfunc` using mangled symbol:

    |#func| PROC
    ; File extcall.c
    ; Line 3
    |$LN3|
        stp         fp,lr,[sp,#-0x10]!
        mov         fp,sp
        bl          |#extfunc|
        ldp         fp,lr,[sp],#0x10
        ret

        ENDP  ; |#func|

Usual targets would emit `#extfunc` symbol as an undefined symbol.
However, ARM64EC defines it as yet another antidependency symbol:

    $ llvm-readobj --symbols extcall.obj
    ...
      Symbol {
        Name: #extfunc
        Value: 0
        Section: IMAGE_SYM_UNDEFINED (0)
        BaseType: Null (0x0)
        ComplexType: Function (0x2)
        StorageClass: WeakExternal (0x69)
        AuxSymbolCount: 1
        AuxWeakExternal {
          Linked: #extfunc$exit_thunk (14)
          Search: AntiDependency (0x4)
        }
      }
    ...

Linked `#extfunc$exit_thunk` is a symbol of guest exit thunk:

    |#extfunc$exit_thunk| PROC
    |$LN1|
        stp         fp,lr,[sp,#-0x10]!
        adrp        x9,__os_arm64x_dispatch_icall
        ldr         x9,[x9,__os_arm64x_dispatch_icall]
        adrp        x10,|$iexit_thunk$cdecl$v$v|
        add         x10,x10,|$iexit_thunk$cdecl$v$v|
        adrp        x11,extfunc
        add         x11,x11,extfunc
        blr         x9
        ldp         fp,lr,[sp],#0x10
        br          x11

        ENDP  ; |#extfunc$exit_thunk|

Note that this thunk will be skipped if `extfunc` is implemented as
ARM64EC function. In that case, when an object file containing its
implementation is pulled by linker, the actual implementation will
define `#extfunc` symbol instead.

However, if `extfunc` is implemented in x86_64 object file, then only
unmangled symbol will be present in its object file. In that case,
linker resolves `#extfunc` to the above thunk using the antidependency
symbol. The thunk calls emulator via `__os_arm64x_dispatch_icall`,
passing exit thunk and target function in `x10` and `x11`, just like
function pointer call would do.

The compiler also defines unmangled `extfunc` symbol as an
antidependency symbol as well, as a link to mangled symbol:

    $ llvm-readobj --symbols extcall.obj
    ...
      Symbol {
        Name: extfunc
        Value: 0
        Section: IMAGE_SYM_UNDEFINED (0)
        BaseType: Null (0x0)
        ComplexType: Function (0x2)
        StorageClass: WeakExternal (0x69)
        AuxSymbolCount: 1
        AuxWeakExternal {
          Linked: #extfunc (19)
          Search: AntiDependency (0x4)
        }
      }
    ...

Note that if regular weak references would be used, this would create a
circular dependency:
`extfunc -> #extfunc -> #extfunc$exit_thunk -> extfunc`. It's not a
problem with antidependency symbols.

Guest exit thunks also add an exntry in `hybmp$x` section:

    dumpbin.exe -all extcall.obj
    ...
    HYBRID INFO MAP:

      Offset           Type             From       To
     --------  ---------------------  --------  --------
     00000000  exitthunk_to_guest            E        16  #extfunc$exit_thunk -> extfunc
    ...

Side note: the way those symbols are set up makes the job of linker
easy. Linker does the right thing based on regular symbol resolution, no
special logic is needed for that.

## Patchable functions

It's fairly common for Windows applications to patch functions in
runtime. While x86_64 generated for entry points solve part of that
problem, it's not a complete solution. Patching entry point will not
affect internal ARM64EC calls within the module that never go through
x86_64 thunks. Applications may also want to patch non-exported
functions (for example COM functions).

To solve that problem, MSVC support a new attribute
`__declspec(hybrid_patchable)`. When this attribute is used, MSVC
assumes that x86_64 thunk will be generated for this function by linker
and all calls to that function will check if the thunk was modified. If
it was patched, it will call the emulator instead of direct EC call.

Using a simple code as an example:

    // build: cl -c -arm64EC patchable.c -FA
    int __declspec(hybrid_patchable) func(void) { return 1; }

MSVC will setup symbols differently than it does for regular functions:

    $ llvm-readobj --symbols patchable.obj
    ...
      Symbol {
        Name: #func
        Value: 0
        Section: IMAGE_SYM_UNDEFINED (0)
        BaseType: Null (0x0)
        ComplexType: Function (0x2)
        StorageClass: WeakExternal (0x69)
        AuxSymbolCount: 1
        AuxWeakExternal {
          Linked: #func$hybpatch_thunk (14)
          Search: Alias (0x3)
        }
      }
      Symbol {
        Name: #func$hp_target
        Value: 0
        Section: .text$mn (3)
        BaseType: Null (0x0)
        ComplexType: Function (0x2)
        StorageClass: External (0x2)
        AuxSymbolCount: 0
      }
      Symbol {
        Name: EXP+#func
        Value: 0
        Section: IMAGE_SYM_UNDEFINED (0)
        BaseType: Null (0x0)
        ComplexType: Function (0x2)
        StorageClass: External (0x2)
        AuxSymbolCount: 0
      }
      Symbol {
        Name: func
        Value: 0
        Section: IMAGE_SYM_UNDEFINED (0)
        BaseType: Null (0x0)
        ComplexType: Function (0x2)
        StorageClass: WeakExternal (0x69)
        AuxSymbolCount: 1
        AuxWeakExternal {
          Linked: EXP+#func (22)
          Search: Alias (0x3)
        }
      }
    ...

The unmangled symbol `func` is an alias to `EXP+#func` symbol. This
symbol is not defined anywhere in the object file. When linker processes
such unresolved symbol, it generates a x86_64 thunk for it:

    $ link patchable.obj -noentry -out:patchable.dll -dll -machine:arm64ec
    $ llvm-objdump -d patchable.dll
    ...
    Disassembly of section .hexpthk:

    0000000180004000 <.hexpthk>:
    180004000: 48 8b c4                     movq    %rsp, %rax
    180004003: 48 89 58 20                  movq    %rbx, 0x20(%rax)
    180004007: 55                           pushq   %rbp
    180004008: 5d                           popq    %rbp
    180004009: e9 0a e0 ff ff               jmp     0x180002018 <.text+0x1018>
    18000400e: cc                           int3
    18000400f: cc                           int3

The mangled symbol `#func` is an alias to `#func$hybpatch_thunk`:

    |#func$hybpatch_thunk| PROC
    |$LN1|
        stp         fp,lr,[sp,#-0x10]!
        adrp        xip0,__os_arm64x_dispatch_call
        ldr         xip0,[xip0,__os_arm64x_dispatch_call]
        adrp        x9,|#func$hp_target|
        add         x9,x9,|#func$hp_target|
        adrp        x10,|$iexit_thunk$cdecl$i8$v|
        add         x10,x10,|$iexit_thunk$cdecl$i8$v|
        adrp        x11,func
        add         x11,x11,func
        blr         xip0
        ldp         fp,lr,[sp],#0x10
        br          x11

        ENDP  ; |#func$hybpatch_thunk|

This thunk uses `__os_arm64x_dispatch_call` to perform the call. It
passes an address of the actual ARM64EC implementation
(`#func$hp_target`) in `x9`, exit thunk in `x10` and x86_64 thunk in
`x11`. `__os_arm64x_dispatch_call` checks if the code was patched and
depending on its status, setups a direct EC call or an emulator call to
patched x86_64 thunk.

Finally, `#func$hp_target` is the actual `func` implementation:

    |#func$hp_target| PROC
    ; File patchable.c
    ; Line 2
        mov         w0,#1
        ret

Note that patchable functions need both entry and exit to guest thunks:

    dumpbin.exe -all patchable.obj
    ...
    HYBRID INFO MAP:

      Offset           Type             From       To
     --------  ---------------------  --------  --------
     00000000  exitthunk_to_guest            E        17  #func$hybpatch_thunk -> func
     0000000C  native_to_entrythunk         15        11  #func$hp_target -> $ientry_thunk$cdecl$i8$v
    ...

## Static libs

Similar to ARM64X for executables, static libraries may contain both
ARM64EC (that includes x86_64) object files and pure ARM64 object files.
In fact, MSVC doesn't provide a separate set of static libraries for
ARM64EC. Instead, its ARM64 static libraries contain both pure ARM64 and
ARM64EC versions in the same file.

Since ARM64 and ARM64EC use different symbol namespaces, they need
separated symbol maps. MSVC introduced a new section called
`/<ECSYMBOLS>/`. EC objects are added to the offset table of regular
map, but the symbols themselves are added to the new section instead.
The format of the new section is similar to the regular map, except it
doesn't contain object offset table. It starts with a 32-bit integer `N`
containing a number of symbols, followed by `N` 16-bit indices to object
files, followed by `N` null-terminated strings containing symbol names.

Example:

    $ cat test.c
    void test(void) {}
    $ cl -c test.c -Fo:artest-arm64.obj
    $ cl -c test.c -Fo:artest-arm64ec.obj -arm64EC
    $ lib -machine:arm64ec -out:artest.lib artest-arm64.obj artest-arm64ec.obj
    $ llvm-nm --print-armap lartest.lib
    Archive map
    test in artest-arm64.obj

    Archive EC map
    #test in artest-arm64ec.obj
    $ientry_thunk$cdecl$v$v in artest-arm64ec.obj

    ...

TODO: Describe linking to x86_64 libraries.

## Importlibs

### Importlib layout

ARM64EC importlibs use mangled symbol names in their importlib object
files. This is different than the actual export name, so a new
`IMPORT_OBJECT_NAME_EXPORTAS` name type was introduced. This export name
type adds a null terminated string stored in the end of importlib object
file (after module name). For ARM64EC importlibs, this contains the
unmangled symbol name. See [winedump
implementation](https://gitlab.winehq.org/wine/wine/-/commit/6892434b22baff054da67c0fac75fcd49a674074).

Example:

    $ cat imptest.def
    NAME test.dll
    EXPORTS
    test

    $ lib -machine:arm64ec -def:imptest.def -out:test.lib
    $ winedump test.lib
    ...
      Version      : 0
      Machine      : A641 (ARM64EC)
      TimeDateStamp: 64E7C2EE Thu Aug 24 22:51:58 2023
      SizeOfData   : 00000014
      DLL name     : test.dll
      Symbol name  : #test
      Type         : code
      Name type    : export as
      Export name  : test
      Hint         : 0

When such library is read (by lib.exe or link.exe), it is treated as
having 4 symbols. In addition to the usual `test` and `__imp_test`
symbols, it also contains `__imp_aux_test` and `#test` symbols.

### Regular IAT and Auxiliary IAT

In addition to the regular import address table (IAT), ARM64EC images
have an additional auxiliary IAT. Similarly to regular mangled and
unmangled symbols (see [Symbol
namespace](#symbol-namespace)), this is meant to provide
separated symbols for actual imported function addresses and function
addresses that are guaranteed to be directly callable by ARM64EC code
(possibly thunks). The meaning of symbols is, perhaps
counterintuitively, swapped between IATs: the usual `__imp_*` symbols
address auxiliary IAT (so they possibly point to thunks, but may be used
by ARM64EC to perform imported function calls without worrying about
thunking), while `__imp_aux_*` symbols are used to address regular IATs
(so they are used by ARM64EC to get imported function pointers). Note
that this wouldn't work out out of the box when linking x86_64 code into
ARM64EC image. In that case, x86_64 code uses `__imp_*` and expects it
to be the actual function address, not ARM64EC thunks. This is taken
care of by a linker special-case: when linker resolves such symbols from
x86_64 object files, it replaces them with `__imp_aux_*` symbols.

The above does not apply to imported data: in that case linker resolves
`__imp_*` symbols to regular IAT and `__imp_aux_*` symbols to auxiliary
IAT. This doesn't matter much in practice since both IATs will contain
the same data pointer at runtime.

IATs on ARM64EC are placed differently to other targets. The regular IAT
is always at the beginning of `.rdata` section and its size is aligned
to 4KB. Similarly auxiliary IAT is placed at the end of `.rdata` section
with an additional 4KB offset alignment. This guarantees that both IATs
are placed in their own memory pages when mapped, which is probably
meant to make catching patching easier.

### Import thunks

Remaining importlib symbols are counterparts of usual linker-generated
thunks that make imported symbols work when `__declspec(dllimport)` is
missing. `test` symbol from the above example is the usual x86_64 thunk,
except it needs to use `__imp_aux_test` symbol to get imported address:

    test:
            jmp *__imp_aux_test

Mangled thunk symbol is ARM64EC thunk (similar to ARM64 thunks):

    "#test":
            adrp    x16, __imp_test
            ldr     x16, [x16, :lo12:__imp_test]
            br      x16

Content of the regular IAT is the same as seen on other targets: RVA of
hint name chunk or an ordinal value. Auxiliary IAT contains an address
of yet another import thunk. That import thunk is exposed using
`__impchk_*` symbols and it can be used in case the imported function is
a x86_64 code:

    __impchk_test:
            adrp    x11, __imp_aux_test
            ldr     x11, [x11, :lo12:__imp_aux_test]
            adrp    x10, exit_thunk
            add     x10, x10, :lo12:exit_thunk
            b       __icall_helper_arm64ec

It sets `x11` register value to imported function address using
`__imp_aux_*` symbol and `x10` to [function exit
thunk](#exit-thunks) using `__imp_*` symbol to lookup
[.hybmp\$x sections](#.hybmp$x-section). The thunk then uses
CRT-provided `__icall_helper_arm64ec` helper to perform a call to the
emulator.

### Auxiliary IAT copy and linker symbols

When imported function is x86_64 code, loader may simply leave auxiliary
IAT unchanged and the above thunk will be used to call x86_64 function
using the regular IAT. When loader detects that the imported function is
a ARM64EC function, it may override the entry in auxiliary IAT with a
pointer to the actual function, so the thunk may be skipped in runtime.
When patching is detected, loader may need to revert that optimization.
This is probably the reason why there is an additional copy of auxiliary
IAT table. Its content is exactly the same as auxiliary IAT (a set of
pointers to import thunks) and its placed in `.idata$a` section,
together with the rest of import metadata with no special alignment. Its
entries may be referenced using `__auximpcopy_*` symbols. The loader may
use it to revert changes made to the auxiliary IAT.

The linker provides two additional symbols: `__hybrid_auxiliary_iat`
addressing auxiliary IAT and `__hybrid_auxiliary_iat_copy` addressing
auxiliary IAT copy. Those are used by CRT to fill [CHPE
metadata](#chpe-metadata).

## Delayed imports

TODO

## ARM64X

Windows allows combining ARM64EC code (which may also include x86_64)
with pure ARM64 code within a single module. Such modules use ARM64 as
PE machine type, so there is no extra work needed when such module is
loaded into ARM64 process. When loaded into an x86_64 process, the
loader applies additional relocations to replace PE headers with their
ARM64EC versions. TODO: describe more details

From toolchain point of view, this is a linker feature. A typical way to
produce ARM64X binary is to build source twice: as ARM64 and as ARM64EC
binaries and pass both of them to linker. Since, other than being stored
in the same module, ARM64 and ARM64EC code is totally separated, linker
needs to handle two separated symbol tables and pick the right one
depending on the context. TODO: describe more details.
