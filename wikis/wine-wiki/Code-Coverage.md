Code-coverage analysis is a debugging technique that tracks how often
code follows different execution paths. This is particularly useful for
digging up sneaky corner cases and identifying performance problems.

## Using Gcov

One reliable tool for this technique is
[gcov](https://gcc.gnu.org/onlinedocs/gcc/Gcov.html), the GNU test
coverage profiler, which can be used alongside the GCC compiler (sorry,
Clang fans). Using gcov requires compiling and linking with the
`--coverage` flag, which significantly increases compile and run times,
so we recommend first [Building Wine](Building-Wine)
normally. Then you can selectively rebuild whichever folder contains the
code you're interested in:

```sh
$ cd mydir/    # Directory that contains myfile.c and myfile.o`
$ make clean && make CFLAGS=--coverage LDFLAGS=--coverage`
```

After rebuilding with the hooks for gcov, run whatever program you want
to test the code (including Wine's [Conformance
Tests](Conformance-Tests)). Once you're done running your
test, call gcov in the **same** directory you rebuilt from to generate
the report:

```sh
$ gcov myfile.c
$ less myfile.c.gcov
```

The *.gcov* file should have three columns: the number of times each
line was run, its line number in the source file, and the actual line of
code. The execution count will contain one of three possible symbols:

- `-` for lines with purely syntactical code (`{` for example)
- `#####` if the line has code that was never executed
- A positive number counting the number of times that line was executed

If a line is optimized out by the compiler, it will appear as if it was
never run. For this reason, the gcov documentation recommends disabling
optimizations for any code you wish to analyze with gcov.

The `wine-preloader` currently requires building with `-nostartfiles`
and `-nodefaultlibs` flags; consequently, it cannot be rebuilt for
analyzing with gcov.

## An Example

We'll use the file *dlls/advapi32/registry.c* to give a detailed example
of how `gcov` can used to validate code in Wine. At the time of writing,
the `RegSetValueW` function included the following lines:

```c
if (name && name[0])  /* need to create the subkey */
{
    if ((ret = RegCreateKeyW( hkey, name, &subkey )) != ERROR_SUCCESS) return ret;
}
```

Although we have at least a few tests written for this function, they
can only check for cases that we're already aware of. But by using gcov,
we can tease out other cases and write appropriate tests to further
validate the code.

First, we can see what cases our tests already cover by running gcov as
described above:

```sh
$ cd dlls/advapi32
$ make clean && make CFLAGS=--coverage LDFLAGS=--coverage
$ cd tests
$ make test
$ cd ..
$ gcov registry.c
$ less registry.c.gcov
```

The part of the gcov results that we're interested in are these lines:

```
    4: 1273:    if (name && name[0])  /* need to create the subkey */
    -: 1274:    {
#####: 1275:        if ((ret = RegCreateKeyW( hkey, name, &subkey )) != ERROR_SUCCESS) return ret;
    -: 1276:    }
```

Line 1275 is never executed (!), most likely because the "name"
parameter was never passed to the function. In order to completely
validate this line, we need to trigger it. So we'll first sketch a quick
unit-test to add to the others:

```c
ret = RegSetValueW(hkey_main, name1W, REG_SZ, string1W, sizeof(string1W));
ok(ret == ERROR_SUCCESS, "RegSetValueW failed: %d, GLE=%d\n", ret, GetLastError());
test_hkey_main_Value_A(name1A, string1A, sizeof(string1A));
test_hkey_main_Value_W(name1W, string1W, sizeof(string1W));
```

Now we need to check that this test is actually activating our code as
expected. We'll re-run gcov like before, only we must first clean out
the *.gcda* and *.gcov* files so that gcov returns fresh results:

```sh
$ rm *.gcda *.gcov
$ cd tests
$ make test
$ cd ..
$ gcov registry.c
$ less registry.c.gcov
```

Behold! Line 1275 is being called exactly once, which we can safely
assume is due to our new test:

```
    5: 1273:    if (name && name[0])  /* need to create the subkey */
    -: 1274:    {
    1: 1275:        if ((ret = RegCreateKeyW( hkey, name, &subkey )) != ERROR_SUCCESS) return ret;
    -: 1276:    }
```

## Nice Reports with Lcov

If you're looking for something a little snazzier than gcov's plaintext
output, [lcov](https://ltp.sourceforge.net/coverage/lcov.php) is a
souped-up extension of gcov that pretty-prints html reports. Even if not
packaged for your distro, you should be able to install from source
(with `make install`) simply enough.

To adapt our above example for lcov, running the conformance tests to
ncheck the code, the commands go something like this:

```sh
$ cd dlls/advapi32
$ make clean
$ make CFLAGS="-g -O2 -fprofile-arcs -ftest-coverage" LDFLAGS="-lgcov -fprofile-arcs"
$ lcov --directory . --zerocounters
$ make -C tests/ testclean
$ make -C tests/ test -k
$ lcov --directory . --capture --output-file results.info
$ genhtml results.info
$ xdg-open index.html
```

## Profile-guided optimization

A closely related technique to code coverage is profile-guided
optimization. In this technique, the compiler selectively optimizes code
based on the likelihood of different execution paths. The goal here is
not so much about improving the quality of the source-code but rather to
allow the compiler to optimize a build more aggressively (though the
improved performance may bring previously unnoticed bugs to the
surface).

A few compilers provide this capability. For example, to optimize the
same dll as in our previous snippets with GCC:

```sh
$ cd dlls/advapi32
$ make clean && make EXTRACFLAGS=-fprofile-generate LDFLAGS=-fprofile-generate
$ make -C tests/ testclean    # Or if you're optimizing for a particular program...
$ make -C tests/ test -k      # ... run that one in wine instead
$ make clean && make EXTRACFLAGS=-fprofile-use LDFLAGS=-fprofile-use
```

## See also

- [Static Analysis](Static-Analysis)
- [Wine and Valgrind](Wine-and-Valgrind)
- [Debugging Hints](Debugging-Hints)
- [Performance](Performance)
- [GCC optimization
  options](https://gcc.gnu.org/onlinedocs/gcc/Optimize-Options.html)
