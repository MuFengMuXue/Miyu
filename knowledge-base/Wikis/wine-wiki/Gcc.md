## The GNU Compiler Collection

The [GNU compiler collection](https://gcc.gnu.org/) is one of the
flagship projects of the free-software world. It regularly integrates
cutting-edge techniques and optimizations from research, plus it
compiles 7 languages for over 45 host architectures. Due to its
prevalence on unix, gcc is also the standard tool for compiling wine.

### Important Features

The build process for Wine depends on a couple newer features in gcc.
You can read a little about them and related bugs here:

**ms_hook_prologue**: The steam overlay requires ms_hook_prologue
support, which is only available in gcc 4.5 or greater. It appears to
have broken in gcc 4.6, see bug #22053 for more information.

**builtin_ms_va_list**: Required to build the 64-bit version of Wine;
it's been supported since gcc 4.4.

### Copy Protection

Sometimes copy protection systems, like SafeDisc2, wouldn't work with
Wine built by older versions of gcc.

### GCC versions and Wine

#### Working

- 4.5: This should work with both copy protection and ms_hook_prologue
- 4.7: Some distros packaged Wine built with this and no known bugs
  appeared
- 4.8: This should work (the one noticeable bug, #33307, was fixed)
- 4.9: This should work with wine-1.7.20 and later (see bug #36139)
- 5.3: Bug #38653 was fixed in this version; no new problems have yet appeared.

#### Known to Have Issues

- 4.4 and earlier: regardless of how they worked with copy protection,
  ms_hook_prologue support was broken
- 4.6: see bugs #22053 and #28753
- 5.0 - 5.2: Broken for 64 bit Wine when compiled with `-O2`
  optimization (see bug #38653)

## See Also

- [Building Wine](Building-Wine)
- [Clang](Clang) is another very effective open-source
  compiler
- [Compatibility](Compatibility)
