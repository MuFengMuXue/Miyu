Now that Wine has matured to the point of running many applications
correctly, people are expecting them to run as fast as on Windows.
Sadly, this is not always the case. Here are a few notes related to
tracking down performance issues.

# User Tips

Surprising as it may be, there really isn't a magic toggle to make
everything faster. Anyway, for games, you can experiment with the
following short list of settings:

- if the game has an OpenGL or Vulkan mode, you could try using that.
  Notice that sometimes it enables code paths that aren't well tested
  (or are plain broken) in the game

otherwise

- enable the Vulkan wined3d backend in the [registry](Useful-Registry-Keys)
- if you run your game from the command line, run it with
  `WINEDEBUG=-all`. That disables a bunch of error checking and validation
- enable threaded optimization in the GL drivers: you can do that with
  environment variables, that's `mesa_glthread=true` for Mesa drivers or
  `__GL_THREADED_OPTIMIZATIONS=1` for Nvidia proprietary drivers
- anything listed in the appdb as helping your particular game. For
  instance,
  <https://appdb.winehq.org/objectManager.php?sClass=version&iId=19065>
  says Batman Arkham Asylum runs a lot faster if you set
  AmbientOcclusion=False in UserEngine.ini.
- anything listed on the web as speeding up the Windows version. (For
  instance,
  <https://www.hardocp.com/article/2009/10/19/batman_arkham_asylum_physx_gameplay_review/3>
  suggests Batman Arkman Asylum runs a lot faster if you set
  MotionBlur=False in that same file.)

The rest of this document is meant for developers more than users.

# Performance-related bugs

Here are some performance-related bugzilla queries:

- [keyword
  'performance'](https://bugs.winehq.org/buglist.cgi?keywords=performance)
- ['slow' or 'performance' in
  title](https://bugs.winehq.org/buglist.cgi?query_format=advanced&short_desc=slow%20performance&bug_status=UNCONFIRMED&bug_status=NEW&bug_status=ASSIGNED&bug_status=REOPENED&short_desc_type=anywordssubstr&product=Wine)
- [keyword
  'source'](https://bugs.winehq.org/buglist.cgi?keywords=source&query_format=advanced&keywords_type=allwords&short_desc=slow%20performance&bug_status=UNCONFIRMED&bug_status=NEW&bug_status=ASSIGNED&bug_status=REOPENED&short_desc_type=anywordssubstr&product=Wine)
- [component contains
  d3d](https://bugs.winehq.org/buglist.cgi?query_format=advanced&short_desc=slow%20performance&field0-0-0=component&bug_status=UNCONFIRMED&bug_status=NEW&bug_status=ASSIGNED&bug_status=REOPENED&short_desc_type=anywordssubstr&type0-0-0=substring&value0-0-0=d3d&product=Wine)
- [component
  unknown](https://bugs.winehq.org/buglist.cgi?query_format=advanced&short_desc=slow%20performance&bug_status=UNCONFIRMED&bug_status=NEW&bug_status=ASSIGNED&bug_status=REOPENED&short_desc_type=anywordssubstr&component=-unknown&product=Wine)
- [component does not contain d3d or
  unknown](https://bugs.winehq.org/buglist.cgi?query_format=advanced&short_desc=slow%20performance&field0-0-0=component&bug_status=UNCONFIRMED&bug_status=NEW&bug_status=ASSIGNED&bug_status=REOPENED&short_desc_type=anywordssubstr&type0-0-0=nowordssubstr&value0-0-0=d3d%20unknown&product=Wine)

# Known Bottlenecks

- applications that frequently compile D3D shaders may suffer from
  stuttering; see e.g. bug #23832
- applications that rely on precise thread scheduling will be
  disappointed (see e.g.
  <https://hisouten.koumakan.jp/wiki/Linux_support#Resolved_bugs>)
- applications that use kernel events heavily may run slowly (e.g.
  Unreal Tournament 3 - Stefan?)
- applications that are picky about what core a thread runs on may be
  disappointed
- some applications don't interact well with power management

# Kernel?

The linux kernel might have something to do with performance.
CONFIG_NO_HZ might make a difference, for instance. Here are a few notes
on the subject:

- World of Warcraft supposedly had pauses every 15 seconds unless you
  modify /etc/sysctl to change kernel.sched_batch_wakeup_granularity_ns
  and a couple other parameters (see
  <https://wiki.archlinux.org/index.php/World_of_Warcraft#Kernel_Timing_Bug>)
- <https://forums.gentoo.org/viewtopic-t-789725.html> is a thread about
  kernel configuration and Doom3/Quake4/Prey performance.
- <https://code.google.com/p/realtimeconfigquickscan/> (you have to check
  the whole tree out) is a little script to check whether your system is
  set up for low latency (mostly for audio)

# Measuring Performance

## Benchmarking Tools

If you're making a tweak that speeds up one application, you probably
want to run a bunch of different performance benchmarks before and
after, to make sure it doesn't slow other applications down.

There are numerous open source and commercial benchmarks for all
platforms. Windows benchmarks are most relevant for Wine. Many games
have built-in benchmarking features. Some examples:

- Various 3DMark versions: <https://www.3dmark.com/>
- Geekbench: <https://www.geekbench.com/>
- Timedemos in the Source Engine:
  <https://developer.valvesoftware.com/wiki/Demo_Recording_Tools>
- And many others:
  <https://www.google.com/search?q=windows+benchmarks>

The merits of various benchmarks are subject of discussion, in
particular Geekbench is a hot button issue (see e.g.
<https://www.realworldtech.com/forum/?threadid=136526&curpostid=136666>).
Therefore it is essential to use a number of benchmarks and games to get
a realistic evaluation and avoid over-optimizing a narrow use case.

For optimizing specific codepaths or having very sensitive regression
detection microbenchmarks are an option. They test a very narrow aspect
of the 3D APIs. Some d3d and opengl microbenchmarks can be found at
<https://github.com/stefand/perftest>.

## Windows Comparisons, Establishing Expectations

When optimizing a certain game it is vital to know what level of
performance can be achieved. A general guideline is to aim for
performance parity with Windows on the same hardware. While beating
Windows is possible and has been achieved in some narrow cases
\[Citation Needed\], it is not something that can be expected across the
board.

Achievable performance depends on a lot more than just Wine:

- The OpenGL and Vulkan drivers
- The Linux kernel, in particular the scheduler and memory manager
- Background processes eating hardware resources
- Game bugs
- Thermal management

To get a rough idea what performance is achievable it is important to
test the same game with the same settings on Windows. On a laptop also
run the game for a while. Different platforms (in particular MacOS) may
have higher or lower performance when the hardware is cold and slow down
to different degrees once the CPU and GPU hit their thermal limit.

## Beyond FPS: Power consumption and cooling

Merely increasing the framerate of a game is of limited use once it hits
the refresh rate limit, usually 60 Hz on most monitors. Any additional
frames will either be discarded (triple buffering), cause tearing (vsync
off) or stall the game (vsync on). That doesn't mean improvements won't
matter though:

- Monitors with 120 Hz or 144 Hz refresh rate are increasingly common
- Weaker hardware will profit from improvements
- Stalling for vsync allows to reduce power consumption and heat

The last point is especially important to keep in mind. A change that
improves performance on a well-cooled desktop computer may reduce
performance on an extra-thin laptop if the laptop cannot sustain its
performance due to lack of cooling. Rendering frames faster and allowing
the hardware to go idle while waiting for vsync reduces thermal pressure
and extends battery life.

# Debugging Bottlenecks

There are many [profiling
tools](https://en.wikipedia.org/wiki/List_of_performance_analysis_tools)
that can help find bottlenecks in Wine.

Here are a few that have been used with some success:

- [perf](https://perf.wiki.kernel.org/index.php/Main_Page)
- [Apple Instruments](https://help.apple.com/instruments)
- [Radeon GPU profiler](https://gpuopen.com/rgp/)
- Nvidia Nsight - tricky to run on Linux though
- renderdoc can provide timing information in a platform independent way

It's possible to build wined3d and many other Wine parts for Windows;
Thus using Windows-specific tools is possible.

# Game Performance Debugging Tutorial

First, the bad news: often there is no magic bullet to improve
performance. It needs careful debugging and may be tricky to fix.

Note that "unlikely" below doesn't mean "impossible", neither does
"likely" mean "always". Rules of thumb can be wrong, so some intuition,
double-checking of assumptions and deviations from the guide are
necessary.

1. Basic steps for debugging Direct3D performance problems:

   Before digging too deep check a few common issues:

   - Keep your software up to date
   - Make sure you actually have a problem: Test the game on Windows on the
     same hardware. If it runs at the same speed there's probably nothing
     Wine can do to fix it. You're free to try though.
   - Make sure your System is OK. No background processes consuming CPU
     time, etc. Try disabling Desktop compositing
   - Check for log messages. Sometimes Wine knows it hits a slow path and
     writes a FIXME or WARN. Don't fix too much on such warnings, they may
     indicate a comparatively minor problem.
   - Watch out for high wineserver CPU usage
   - Currently 80% of Windows performance is a high water mark, few games
     run faster. Many games run around 50%, which means there's a lot of
     room for improvement. If your game runs even slower there are probably
     some nasty bugs around.

   Some words about CSMT. The basic idea is to segregate wined3d's GL calls
   to a separate thread: wined3d functions indirectly called by the
   application threads queue messages to the command stream thread which,
   on its part, essentially keeps checking the queue and executing whatever
   instruction it finds there.
   CSMT has been initially developed as a way to enhance wined3d
   performance, with the "theory" being that by splitting the potentially
   expensive GL calls out of the application thread we can quickly return
   to the application code and hopefully lessen our CPU-side woes. That
   turned out to work pretty well but with a caveat: some commands (e.g.
   mapping buffers) actually NEED to wait for the operation to complete
   since they have to return data to the application. Without some "tricks"
   when we get one of those commands we have to effectively wait until all
   the commands queued before it complete their execution, which means that
   the application thread has to block and wait, potentially throwing a lot
   of the performance improvement out of the window.
   The version of CSMT initially introduced in "official" Wine does without
   some of those tricks (specifically, those that weren't generally safe)
   and has some room for further performance improvements. It still works
   perfectly fine as a better replacement of the StrictDrawOrdering option.

2. GPU, CPU or sync limited?

   3D rendering is a complex process where multiple components have to play
   together:

   - The GPU has to render the scene fast enough
   - Software on the CPU side(driver, game, ...) has to generate rendering
     commands fast enough
   - Software and GPU should, as much as possible, not have to wait for
     each other

   If your game slows down if you increase the screen resolution (or speeds
   up when you lower it) you are probably GPU limited. This is because the
   CPU rarely touches single pixels, so with increased resolution only the
   strain on the GPU increases. Exceptions may apply especially in older
   ddraw/d3d7 based games..

   Figuring out if the issue is excessive synchronization is a bit harder.
   A significant portion of wined3d time being spent in
   wined3d_cs_mt_finish() (with CSMT enabled) might hint in this direction,
   although that isn't necessarily the case and there might be
   synchronization points hidden in other spots.

3. GPU limited situation:

   If you're GPU limited the problem could be inefficient shaders, or
   incorrectly configured render target formats. Try ARB shaders (if the
   game is happy with Shader Model 2.0 or you have a Nvidia GPU), and check
   logs for usage of 16 bit per channel or floating point render targets.

   Unless you have a low end GPU or play at a very high resolution GPU
   limitations are rare. A seeming GPU limitation may also be a sign of a
   software rendering fallback in the fragment pipeline.

4. CPU limitation

   Most performance issues on Mid-End or High-End systems are CPU side
   bottlenecks. The problem can be in pretty much every component involved
   in running the game:

   - The Linux Kernel
   - The X server
   - The 3D parts of Wine
   - The non-3D parts of Wine
   - The 3D driver

   It is tricky to tell those apart. A useful first test is comparing the
   following 3 metrics:

   1.  The performance on a normal Windows system
   2.  The performance on Windows while running the game with wined3d
   3.  The performance on Linux/macOS with Wine
   4.  If you are on macOS: The performance with Wine+macOS.

   If there is a noticeable difference between (1) and (2) the problem is
   likely in the 3D related parts(wined3d, OpenGL driver). That's because
   all the other components haven't been changed. If there is a noticeable
   difference between (2) and (3) the problem is either in the non-3D
   parts(Rest of Wine, Linux kernel, ...). Make sure the game runs in the
   same codepath in all 4(or 3) cases - some games can use both d3d9 and
   d3d10 for example.

   A difference between (2) and (3) may also indicate a problem in the
   Linux 3D driver that does not occur on Windows. If you are using AMD's
   or Nvidia's binary drivers this is unlikely because the Windows and
   Linux drivers share a pretty big common core. On macOS there is less
   code sharing, so if you're debugging performance issues on macOS the
   difference between (3) and (4) can matter.

5. Limited by CPU-GPU synchronization

   Ideally GPU and CPU should run as independent of each other as possible,
   to allow them to work at the same time without interruptions and exploit
   the available resources to the fullest. It's the application that
   ultimately decides how to set up its rendering pipeline, which means
   that sometimes there isn't much that Wine can do to avoid costly CPU-GPU
   synchronization points. That's one more reason why comparing performance
   with Windows is important. Assuming a well-behaved application, wined3d
   should strive to avoid introducing its own synchronization points. To
   figure out if there is room for improvement, the only practical thing to
   do is to look at the d3d log by hand (probably with some additional
   traces around wined3d_cs_finish() or its callers or other interesting
   points). I've also found it useful to make a log with just those ad-hoc
   traces (so to not slow down the game too much) and check it "realtime"
   with the game and maybe perf.

6. Profilers

   Now that you have a rough idea if you're looking for issues in 3D or non
   3D parts it's time to separate modules further. perf, sysprof or other
   profilers can help here.

   Case A: 3D related problems:

   The main question is if the GPU time is spent in wined3d.dll or the
   driver. If more than 5% CPU time are spent in wined3d this is
   suspicious. If a lot of CPU time is spent in the driver libraries(\> 30%
   if you need some threshold) it may indicate a bug in the driver itself,
   or inefficient GL calls made by wined3d. With binary drivers the
   difference doesn't matter much since you can't change the driver anyway.

   Specifically for CSMT, a high wined3d_cs_run() CPU usage most likely
   means that the command stream thread is spinning a lot waiting for new
   commands to execute. That in turn points to the application thread not
   being able to keep up with the pace of the command stream / GPU
   execution (possibly because of wined3d stuff in the application thread)
   or that there is a lot of synchronization with the command stream thread
   and the queue is flushed a lot. A lot of time being spent in
   wined3d_cs_emit_present(), instead, suggests that the command stream
   thread is the bottleneck. In turn, that might be busy on the GPU or CPU
   side. In the latter case, driver's threaded optimizations might help, if
   available.

   Case B: Non 3D related problems:

   Usual suspects are ntdll.dll, kernel32.dll, wineserver, various C/C++
   runtime libraries, the Linux kernel. You may be able to use the native
   version of the library in Wine. If that fixes your issues you know where
   to fix it in Wine. Again note that a high CPU usage in the Linux kernel
   or in low level Wine libs may be caused by inefficient calls to that
   library from a higher level, so be careful before taking out the
   pitchforks.

7. Telling wined3d problems from driver problems

   Telling those apart is not easy. A driver may not support OpenGL
   extensions used for speedups, causing high CPU usage in wined3d(e.g.
   GL_ARB_vertex_buffer_object, GL_ARB_vertey_array_bgra). WineD3D may make
   inefficient calls causing high CPU usage in the driver.

   A rule of thumb way is to try a different GPU/driver. If a game is slow
   on Nvidia GPUs (compared to Windows) and fast on AMD GPUs (compared to
   Windows on the same card) then the problem may be in the driver. If you
   have a binary driver you may as well just assume that the problem is in
   wined3d since otherwise you're mostly out of luck anyway.

   If you isolate a problem in the driver don't forget to report it to the
   driver vendor.

8. Other hints:

   - GPU vendors offer various performance debugging tools. Those can be
     helpful for debugging GPU or bandwidth limitations. They're usually
     focused on Windows, so you're probably better off by debugging wined3d
     on Windows
   - Windows has helpful tools as well, for example
     \[<https://msdn.microsoft.com/en-us/library/ms182404(VS.80>).aspx
     VsPerfMon\] (Kinda like oprofile). To use those you may have to
     compile wined3d with Visual Studio to get Microsoft-Style debug
     symbols.
   - Don't hesitate to contact wine-devel for help.
   - Do your homework before contacting driver developers or other
     projects. Installing Wine and a Windows Game means a lot of work for
     non-Wine people, so make sure you're not wasting their time.

*Tutorial by Stefan Dösinger*
