This page is for notes on porting the 64-bit version of Wine to the
AMD64 architecture (a.k.a. x64 or x86-64) and the
[WoW64](Building-Wine#shared-wow64) setup, which allows
running both 32 and 64-bit Windows apps from the same instance of Wine.

## ABI Differences

There are some major differences between the x86-64 ABI on Windows and
other operating systems. Here's a short list of some of the major ones:

- The **long** datatype is 32 bits on Windows but is 64 bits on some
  OSes (such as Linux)
- Calling conventions often differ
- Different registers may be used for passing parameters

See the reference documents at the bottom of this page for the complete
picture

## Consistent 32-bit Support

Ideally, [Building Wine](Building-Wine), running the
[Conformance Tests](Conformance-Tests), and execution should
be consistent across configurations. That's just as relevant when
comparing 32-bit and 64-bit apps, or running apps on a stand-alone
32-bit build of Wine vs. the 32-bit components of a WoW64 setup.

One quick way to see simpler differences between the vanilla 32-bit and
WoW64 builds is to scan the make and test logs from separate build
directories. Here's a simple script that simply outputs message counts
for different directories...

```
for dir in wine32 wine64
do
    echo $dir
    cd $dir
    echo -n "ok:  "; find . -name '*.ok' | wc -l
    echo -n "err: "; grep ok.*Error test.log | wc -l
    cd ..
done
```

This is actually a pretty good idea; if expanded upon, it could be
pretty effective, maybe even for the automated test suite

## See Also

#### On Wine Wiki:

- [Building Wine](Building-Wine)
- [Multiarch](Multiarch)
- [Compatibility](Compatibility)
- [Packaging](Packaging)
- Info about porting Wine to the [ARM64](ARM64) architecture

#### Porting Guides:

- [Common AMD64 porting problems](https://www.viva64.com/en/a/0004/),
  from the makers of the PVS-Studio static analyzer
- [MS Programming Guide for 64-bit
  Windows](https://msdn.microsoft.com/en-us/library/bb427430%28VS.85%29.aspx)
- [Why did the Win64 team choose the LLP64
  model?](https://blogs.msdn.com/b/oldnewthing/archive/2005/01/31/363790.aspx),
  from the MSDN Old New Thing blog

#### Reference Documents:

- [Linux x86-64 ABI
  Reference](https://www.x86-64.org/documentation/abi.pdf)
- [Visual C++ Calling Conventions for
  x86-64](https://msdn.microsoft.com/en-us/library/7kcdt6fy.aspx)
