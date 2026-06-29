# Debug startup performance

Sometimes a snap is slow to start. This may be related to the helper scripts that are used when creating the snap. To help pinpoint these issues, from snapd 2.36 on it is possible to use `snap run --trace-exec` to see what helpers are launched and how long they run. This can be useful when debugging why a app start-up is slow. Here is an example:

```
$ snap run --trace-exec  test-snapd-tools.echo hello
hello
Slowest 3 exec calls during snap run:
  0.010s snap-update-ns
  0.177s /snap/core/6135/usr/lib/snapd/snap-confine
  0.086s /usr/lib/snapd/snap-exec
Total time: 0.270s
```

This example shows that there are 3 helpers executed. First snap-update-ns which takes 0.010s to run, then snap-confine and finally snap-exec. This examples shows the minimum amount of setup that each snap requires. Some snap that use desktop components may have extra scripts running (e.g. via the desktop-helpers component).

At most the slowest 10 execve() calls will be displayed.
