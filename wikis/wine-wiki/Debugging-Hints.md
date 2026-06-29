Debugging Wine is often a very different process than debugging any
other application. While you have access to Wine's source, you almost
always don't have access to the source of the application you're trying
to run under Wine. This means that finding the point of failure is often
much harder.

The following is a collection of tips, processes, and things to try, in
order to find a problem.

## General

The general process of debugging goes something like: locate a point of
failure, try to find the reason for it in terms of misbehaviour of
Windows APIs, test that Wine's behaviour in the specified case is
actually wrong, try to fix it if so, and see if that makes the problem
go away.

## Debugging exceptions

Many if not most bugs take the form of an unhandled exception, also
known as a crash. When this happens, you'll usually (though not always)
see a dialog window from winedbg pop up telling you that a crash has
occurred. If you click "Show Details", you'll see information and a
backtrace in the window; if you click "Close" the same information will
be printed to stderr, but only if you don't click "Show Details".

This is often the best kind of issue to debug, since it means you have a
clear *terminus ante quem* point of failure. Whatever went wrong went
wrong no later than the exception. It might have gone wrong much
earlier, but often it didn't, so you can start close to the point of
failure and work backward.

Sometimes an exception is the symptom of a problem, but the program
hides this by handling the crash gracefully. If a program is failing
for some indeterminate reason, often the best thing to try is to grab
a log with `WINEDEBUG=+seh`, and look for exceptions near the failure
point.  Always look for `0xc0000005`, aka a page fault, because that's
the most common type of exception, and it almost always means
something went wrong in an unintended way. Many other exceptions are
generated as part of the language, but a page fault is
not. Unfortunately +seh alone will not give you a backtrace, so if a
program is handling a crash gracefully (especially a crash in Wine)
and you need a backtrace, use winedbg to attach to the program and
grab one using the "bt" command.

### Page fault

This is by far the most common type of crash. On Linux, you would see
"Segmentation fault" (aka SIGSEGV), but Wine translates Unix signals
to Windows exceptions and uses those even internally, so instead
you'll see the code `0xc0000005` or `STATUS_ACCESS_VIOLATION`. Start by
looking at the backtrace, and see whether the crash is in Wine or in a
native application.

#### Page faults in Wine

If it's in Wine's code, you're in luck, because that probably means—if
the crash is consistent—that the error is very close to the crash
location, and you can start working backward from there, tracing
variables and parameters until you find the point where they are set to
the wrong things. Here are some tips for specific kinds of page faults:

- If you see a crash in ntdll/heap.c, then the heap implementation isn't
  broken, but rather something is corrupting the heap. See below for how
  to debug heap corruption. Often this will manifest as a crash in
  include/wine/list.h, since the heap uses linked lists internally.
- If something is trying to dereference a pointer, and the value of that
  pointer looks like garbage, then probably it's either not being
  initialized properly, or something is corrupting it. If it's a heap
  pointer, then you have heap corruption. If it's a stack pointer, you
  have stack corruption, which is similar, but often a lot easier to
  debug.

  Generally, though, debugging things inside of Wine's code means
  knowing what variables should look like if things are correct, and
  then working from there.

- A crash in RtlRaiseException() is really more of an assertion failure
  than anything else, and it usually is something the program did.

#### Page faults in the application

- If the application is trying to dereference a NULL pointer, or a small
  integer value (i.e. an offset from a NULL pointer), it's probable that
  it wanted a pointer from us that we didn't provide.
- Check if the pointer looks like ASCII; that usually indicates heap (or
  stack) corruption.
- An error from CoGetClassObject() followed by a NULL pointer
  dereference almost always means that the application tried to create a
  COM object that Wine doesn't implement and assumed it would succeed.

Start looking backward from the crash to find things that look like they
could be responsible for the failure. More details on this process
below.

### Stack overflow

Like elsewhere, this usually means that a recursive function got out of
hand. This is signified by `0xc00000fd`, i.e. `STATUS_STACK_OVERFLOW`.

### Breakpoint

This is `0x80000003`, or `STATUS_BREAKPOINT`. If a program crashes on
an unhandled breakpoint, that usually means an assertion failed.

- If libcef or qt5webengine is involved, try installing corefonts. If
  that fixes it, it's bug #34342.

### Other exceptions

Some other notable exceptions:

- `0xe06d7363` - This is a C++ exception. Usually these are meant to be
  handled by the program, but not always.
- `0x40010006` - This is an exception generated internally by
  OutputDebugString(). It should always be handled. Use
  `WINEDEBUG=+debugstr` to get the actual content of the debug string.
  Often it contains useful information.
- `0x406d1388` - This exception is used to name threads for debugging
  purposes. It should always be handled.
- `0x80000004` - This is `STATUS_SINGLE_STEP`, which is used for debugging,
  and by copy-protection/anticheat schemes that want to avoid being
  debugged.

Anything else is probably very idiosyncratic, so there's not much that
can be said here.

## Pointers

Knowing what specific pointers look like often helps. Most valid
pointers are 4-byte-aligned, or 8-byte-aligned on 64 bits. Here are some
specific patterns to watch out for:

|                  | x86                          | x86-64              | Extra tips                                                                                                                                                                                                                                                                                                                         |
|------------------|------------------------------|---------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Stack pointer    | 0x3#####                     | 0x3#####            | For the main thread's stack, at least. Check the value of %esp. If a pointer is passed to a function that returns an output parameter, it's usually a stack pointer. If you want to be sure, you'll have to add traces to virtual_alloc_thread_stack() in ntdll/thread.c, because for some reason we don't trace these by default. |
| Wine DLL         | 0x7#######                   | 0x7###########      | These are allocated top-down starting at 0x80000000 (x86) or 0x800000000000 (x86_64). Use WINEDEBUG=+loaddll to find out where exactly modules are loaded. This will also be visible in a crash dialog. Be warned that the position will change between runs.                                                                      |
| kernel32.dll     | 0x7b4#####                   | 0x7b4#####          | kernel32.dll has a fixed load address, 0x7b400000.                                                                                                                                                                                                                                                                                 |
| ntdll.dll        | 0x7bc#####                   | 0x7bc#####          | ntdll.dll has a fixed load address, 0x7bc00000.                                                                                                                                                                                                                                                                                    |
| Native library   | 0x7#######, 0xf7######       | 0x7###########      | +loaddll won't work for these, but on Unixes, you can use /proc/###/maps instead. On x86 some libraries (most notably libc) are loaded right near the top of the address space.                                                                                                                                                    |
| Application EXE  | 0x4#####, 0x10######, others | not very consistent | Check the binary's load address, using objdump -x.                                                                                                                                                                                                                                                                                 |
| Application DLLs | 0x10######, others           | not very consistent | Generally these are loaded in the lower end of the address space. Use +loaddll to find exactly where. You can also check the preferred address; sometimes they'll be loaded there.                                                                                                                                                 |
| Heap pointer     | 0x1#####, but anything goes  | not very consistent | Generally, if it's not anything else, it's a heap pointer.                                                                                                                                                                                                                                                                         |
|                  |                              |                     |                                                                                                                                                                                                                                                                                                                                    |

## Working backwards from a point of failure

Failure can be signaled in many ways: an unhandled exception, a handled
exception, a message box, a message printed to the terminal, a custom
window, or even the application tearing down everything and silently
quitting. Once you've identified, in any one of these ways, where
something went noticeably wrong, you have to trace back to where the
root of the problem is. This can be difficult, but here are some tips.

The first thing to try is usually to look at the default console output.

- Anything in the ERR or FIXME debug classes is at least somewhat likely
  to cause failure. That's not certain, though. We often stress when
  responding to bug reports that FIXMEs are not bugs. Some functions are
  unimplemented and applications don't care; often this results in the
  FIXME being downgraded to a WARN after some time.
- Start from the earliest point of failure. One exception might trigger
  others; try to find the earliest one. A message box might be an
  application's way of handling a chain of exceptions. The first
  instance of `0xc0000005` in a log with +seh is usually going to be the
  earliest clear point of failure.
- A NULL pointer dereference often means the game expected something out
  of Wine that it didn't provide. Look for an earlier function call that
  should have returned a pointer.
- In particular, CoGetClassObject failing is a big red flag that the
  application tried and failed to create an object. Often this means it
  just isn't implemented. Sometimes this means an interface is missing.
- A FIXME from QueryInterface() just before a NULL pointer dereference
  is a similar big red flag; an interface is missing. However, not all
  interfaces flag missing interfaces as FIXME. Usually the rest flag
  them as WARN, so one trick you can try if you see a NULL pointer
  dereference out of nowhere is to use WINEDEBUG=warn+all. This is
  generally a low-cost log to try; the default output from the WARN
  class won't slow down the application or bloat the log file very much.
- The more exotic a function is, the more likely it's to blame for a
  failure. Conversely, the more common and basic a function is, the less
  likely it's to blame, even if it spews FIXME. Well-worn code paths are
  less likely to have bugs in them.
  - Some well-worn and well-implemented DLLs are kernel32, ntdll,
    user32, gdi32, most wine-internal DLLs (e.g. winex11), ole32,
    rpcrt4, advapi32. Of course, these all contain some exotic
    functions, so don't just throw them away wholesale.
- If you see a FIXME (or ERR) from a certain function and it's likely to
  be to blame, try implementing it. That might be nontrivial to do
  fully, of course, so there are some quick hacks you can do:
  - Return success.
  - Set output parameters to a sentinel value, and see if the
    application subsequently tries to use those parameters. If it does,
    then the function is almost certainly to blame, and you should
    probably spend effort on implementing all that the program needs.
    You don't necessarily have to implement the whole function, even for
    what you send to upstream Wine, just implement what the program
    needs.
  - If the offending DLL is one that can be safely overridden, try
    dropping in the native DLL. winetricks has many verbs for this, but
    not all; you can try getting missing DLLs from a Windows
    installation, though be warned they may fail for other reasons. If
    dropping in the native DLL makes the bug go away, then you know for
    sure that you've found the problem.
- If there are no console messages, or none that look relevant, the
  first place to try looking is +relay. Often this is what will help you
  find a point of failure in the first place. Look backward from the
  point of failure for functions that fail; the more exotic the better.
  Make sure you never use +relay with native DLLs in the prefix, as this
  violates our clean room rules.
- If +relay is infeasible, try omitting certain anodyne and common
  function calls, either by using RelayExclude or by marking them as
  -norelay in the spec file.
- warn+all is a poor substitute. Most warnings are anodyne. Some may
  indicate failures, though, and if +relay doesn't work it may be your
  best option.
- Looking at the official documentation is often helpful, and may clue
  you in that some function is misbehaving. Be warned that the
  documentation is not always present or accurate, though. Always write
  tests to make sure.

## Debugging heap corruption

This can be tricky. There are a few tools at your disposal:

- `WINEDEBUG=warn+heap` enables heap validation. As soon as a heap
  function is called and the heap has corrupted state, it'll be printed
  to stderr. This may be much earlier than any other sign of heap
  corruption.
- `WINEDEBUG=+heap` (i.e. trace+heap) does the same thing, but also traces
  every heap allocation and free. When the heap is corrupted, it will
  dump the whole heap and assert(0).
- **valgrind** is an external tool which meticulously tracks heap state
  (among many other things). +heap alone won't let you know about
  corruption until the next heap call is made, but valgrind will find
  out immediately.

If you're not sure if there's heap corruption, warn+heap is probably a
great place to start, as it's low-cost (it won't slow down the program
or create huge log files) but as thorough as trace+heap. If that
confirms the corruption, the best thing to do is probably trace+heap.
You will probably want to combine this with other flags to determine
what is actually corrupting the memory, and what is allocating the
memory that's being corrupted. If you have no better ideas, +relay is
similarly a good start. Be warned that tracing every heap allocation
(even without +relay!) will often create huge log files and slow down
the program immensely. But sometimes you have no other option.

valgrind is very thorough. It's also very slow, and will output many
things that are not necessarily important, (e.g. use of uninitialized
memory, which may be important, but may not). It's best for finding heap
corruption within Wine's code. Use it if +heap isn't enough.

## Debugging race conditions

Any problem which only *sometimes* appears is both a blessing and a
curse.

The curse is that you often have to try several times to get a problem
to reproduce. The further curse is that often turning on heavy logging
channels (e.g. +relay, +heap, +d3d) will "fix" the problem. The blessing
is that you often have a way to reproduce good behaviour and bad
behaviour. That means that you can compare logs meticulously to find the
*earliest* point of divergence, and that will generally point you
straight towards the bug.

## Debugging hangs

Many hangs are really crashes in disguise; make sure you take a +seh
log.

If you really have a hang, the best log to take is +server, because it's
really the only way to trace synchronization calls. The goal is to try
to find the hung thread, and figure out why it's hung. Getting to the
first part can be tricky, but generally you want to do something like
this:

1.  Start by finding any hung thread. In particular, the main thread
    (usually, tid 0009, but check the top of your log) is often a good
    choice.
2.  Determine what that thread is waiting on, i.e. look for the "select"
    call.
3.  For each handle, check what kind of handle it is.
    1.  If it's a thread or process handle, then you want to figure out
        why that thread or process isn't exiting. Pick that thread and
        go to 2.
    2.  If it's an event or other synchronization primitive, you want to
        figure out why that object isn't being signaled. Grep through
        the log for threads that signal the event or other primitive.
        Failing that, find which thread created the event. If that
        thread is hung, go to 2. If it's exited, see if it's possibly
        exited prematurely. Sometimes you may not find anything, in
        which case just drop this thread of investigation and go on to
        the next.

You should hopefully eventually find threads clearly deadlocked against
each other, or something similarly anomalous.

- Critical sections are a (slightly) special case; essentially they're
  the other way that threads can get stuck. If a thread is stuck waiting
  on a critical section, you'll see an error. If it's one of Wine's
  threads (which will *always* be the case if the critical section is
  labeled something other than "?"), then that's already a great clue as
  to where the deadlock is.
- There are some other synchronization primitives in ntdll that don't go
  through to the server. Mainly, these are SRW locks,
  WaitOnAddress()/WakeByAddress(), and condition variables.
  Unfortunately, at the time of this writing none of these are
  adequately traced. You may need to add tracing yourself.

## Debugging poor graphical performance

Here's a little overview of the graphics specific parts that can go
wrong and some rules of thumb to start pinning them down:

The first thing to check is how the game performs on Windows. Games and
drivers are not perfect and we have had many bugs filed for things that
happen on Windows too. Test *on the same hardware*, not something that
has similar specs. Even if the specs match perfectly, differences in
cooling and power supply can make a massive difference.

1.  Classic CPU limitations can occur in the 3D components as well -
    e.g. the driver having too much overhead in draw calls, some
    emulation codepath being hit, copying resource data from A to B.
    Usually a CPU limited game will not see a performance change when
    the rendering resolution is changed.
2.  Games can be purely GPU limited. This is very common at high
    resolutions, e.g. my middle class Geforce 1060-something is
    struggling to render semi-modern games like StarCraft 2 at 4k
    resolutions. Like indicated in (1), if decreasing the resolution
    causes a noticeable performance gain you're likely GPU limited. If
    you do a CPU side sample and see a lot of time spent in
    glSwapBuffers that's an indication of a GPU limit too.
3.  The most common issue nowadays, tricky to debug and fix, are
    excessive synchronization between CPU and GPU. Generally the CPU
    produces data, sends it to the GPU and moves on to the next task
    while the GPU is doing the requested draws. If the game reads back
    data from the GPU or modifies a resource that is referenced in a
    scheduled but not yet executed GPU operation, the resource map call
    has to wait until the GPU has caught up or rendering problems will
    occur. After the CPU continues, the GPU is idle until new commands
    arrive, so you're throwing away processing on both ends.
    - The usual way to recognize this kind of issue is a lot of CPU time
      spent in wined3d_resource_map, glMapBufferRange, glSubTexImage2D,
      Query::GetData or similar calls.
    - Games are getting this wrong on Windows too. So just because you
      see such a CPU/GPU sync doesn't mean we can fix it on our side.
      Inefficient drivers might stall on calls that should be
      asynchronous (I am looking at you, Apple).
    - I usually try to hack away the sync points by adding NOOVERWRITE
      or MAP_UNSYNCHRONIZED flags, hacking event queries to return that
      the query is ready, hacking occlusion queries to pretend to be
      ready and return a dummy samples_passed value. Eventually
      rendering will most likely break, and eventually performance
      should go up. If performance does not increase and the CPU spends
      more and more time in Present/SwapBuffers you're probably GPU
      limited.
4.  The video memory might be exhausted. Debug tools that tell you the
    amount of vidmem used and the amount of data sent over the PCIe bus
    is a good starting point to detect that. The effect is similar to
    your computer starting swapping while you're compiling something -
    performance goes south fast.
5.  Even if the vidmem is not exhausted the PCIe bandwidth could be your
    limit. I have never actually seen this as a genuine issue, but it
    can happen with odd hardware configurations like a
    Thunderbolt-connected external GPU, plugging a GPU into a PCIe 1x
    slot or using a relatively powerful GPU with an old-style
    non-express PCI connector.
6.  A sub-class of the CPU limitation are cases where games use multiple
    threads that do real work and the synchronization between the
    threads is too slow - thread 1 calls SetEvent and thread 2 takes
    some time to wake up. Android's systrace tool is a really nice one
    to debug thread dependencies and scheduling. Unfortunately I don't
    know an equivalent for regular Linux.
7.  Scheduling, CPU cache etc is also related to (6). It's possible to
    get big performance boosts for particular games out of tweaking some
    Linux scheduler settings, around 30% in some games. The impact is
    very game and hardware specific, but it is worth experimenting with.
8.  Cooling and power supply can be limiting. E.g. Macbooks have some
    really nice performance for a minute or so until thermal throttling
    slows everything down by 50%. In such a situation it may be
    beneficial to slow down the CPU in a GPU limited game to reduce the
    heat the CPU produces so the GPU can clock higher. Vsync is a good
    way to keep heat down, but it kinda requires that the game runs at
    \>= 60 fps already. E.g. if you have a game that runs at 90 fps on a
    cold laptop but drops down to 45 after a while, you might be able to
    stay at 60 fps with vsync on. Again, very hardware and game
    specific. You'd hope the drivers figure these kinds of things out.
9.  If a drop in CPU speed is instant when the GPU starts doing real
    work, or vice versa, it is probably not a matter of cooling but
    providing power. Similar considerations, and also much more likely
    to affect laptops than desktops.

This is not an exhaustive list. More specialized things can happen as
well, like Wine somehow triggering a broken codepath in the game (e.g.
triggering an abandoned codepath for Windows \<= XP in the game), not
supporting a particular texture format the game wants, etc.

My general advice is to first start debugging on a well-cooled desktop
and move on to laptops once you've ruled out software problems. After
that you can look into laptop heat troubles.

## Other general tips

- Try finding the most exotic DLLs that the program uses with +loaddll.
  Drop in as many native substitutes as you can using winetricks, and
  see if you can fix the problem that way.
- Keeping log output clean:
  - Start the wineprefix beforehand, by just running e.g. 'wine
    winecfg'. This ensures that any automatically started services won't
    pollute the log output.
  - RelayExclude is a good way to get unimportant function calls out of
    +relay, but you have to reset it for each prefix. I keep a patch in
    my local tree that adds -norelay to the .spec entries of many DLLs.
- When a program crashes with the builtin "Comctl32" but works with
  the native one, this can often indicate a missing
  notification/callback or an out of order message stream. Most GUI apps
  are very sensitive to callback ordering and if a callback is not run,
  or run out of sequence, some software won't initialize internal
  structures properly leading to a crash at some unspecified future
  time. The solution? Write test cases to show we have the message
  ordering right (or wrong). There are examples of how to do this in the
  user32 tests.
- Windows that don't accept keyboard focus (typical symptom: what you
  type goes to the terminal) have been made unmanaged for some reason.
  Each WM can treat this differently but the most common response is
  that the window becomes always on top, appears on every desktop and
  cannot accept focus. Sometimes this is desirable: for menus and
  tooltips it's what you want. Often it isn't. Managed vs unmanaged is a
  rather difficult problem, ask on the wine-devel list for help if you
  wish to change the mode heuristics.
- Visual glitches in windows are best debugged by looking at the styles
  given by the application to the offending control, rather than simply
  reading the widget code by hand. There are no fancy tricks you can use
  here, you just have to play with the drawing code and see if you can
  figure out where the problem is. Fortunately, native Windows 98
  "Comctl32" works well, so you can always use that as a reference.
- Be careful with error codes. Unfortunately, while MSDN documents what
  error codes a function can return, this information is often wrong,
  and even when correct, it rarely says exactly what each error code
  means. Many apps rely on particular codes being returned in particular
  scenarios so the best way to be sure is to [write a test
  case](Wine-Developer's-Guide/Writing-Conformance-Tests).
- If a program is complaining about a debugger being present, you need
  to find out why it thinks that and fix it. Wine does not report a
  debugger by default, but unfortunately as IsDebuggerPresent() is so
  easy to work around, many programs, especially games, use more devious
  techniques. Some contain anti-disassembly code. You can find common
  anti-debugger techniques by reading blackhat/warez cracking sites.
  Just don't do it at work! If you see attempts to load SICE.VXD or
  NTICE.VXD, you're seeing a check for the popular SoftIce debugger and
  should be able to ignore it.

## See Also

- [Developer Hints](Developer-Hints)
