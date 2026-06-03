# What's this `icecream` about? I'm on a diet!
* It allows to distribute a build to multiple computers to:
  * Save time, especially when multiple builds are needed in a workday (even more so if they're clean builds), e.g. during a `git bisect`.
  * Alernatively, get fast builds without slowing down one's workstation (allocate less workstation CPU cores to the build).
  * See xkcd comic 303 for additional motivation.

* You might already know about doing this with `distcc`. See `icecream`'s [documentation](https://github.com/icecc/icecream?tab=readme-ov-file#i-use-distcc-why-should-i-change) for a comparison.

# Who can benefit from this?
A network with available but under-utilised computer resources, e.g.:
  - Multiple employee computers that are mostly idle during the day in an office setting.
  - A build machine with idle cores.
  - A Steam Deck (that you don't use anyway while working... right?) in your home network.

# Notes
As described in this page:
* `Submit node`: a computer that starts a build. This will typically be your workstation. Runs the `icecream` daemon (`iceccd`).
* `Execute node`: a computer on the network that (1) participates in the `icecream` cluster (i.e. runs `iceccd`) ***and*** (2) accepts remote compilation jobs from `submit node`s. It executes compilation jobs distributed to it by a `scheduler node`, then sends the output back to the appropriate `submit node`.
  This could be a colleague's computer, or some other idle machine on the network (e.g. a dedicated build machine with many cores).
* `Schedule node`: runs the scheduler (`icecc-scheduler`). Receives requests for compilation jobs from `submit node`s and distributes them to `execute node`s.
* There needs to be at least one `execute node` and at least one `schedule node` for distributed compilation to take place.
* A machine in the cluster can operate as *all three* types of nodes, if so desired.

# Using `icecream`
## All nodes
* Install `icecc` through your distribution's package manager. If it does not provide a package (or provides an outdated version), you can build and install [from source](https://github.com/icecc/icecream/blob/master/README).
* Consider running `icecream` using an unprivileged container solution like [distrobox](https://github.com/89luca89/distrobox). This ensures that the installation will be trivial - also see [Security considerations](#sec).
  Here's how to get a minimal container set up for an `execute`/`scheduler node` (you can do the same for your Wine [development environment](/Distrobox-development-environment)):
  ```shell
  DISTROBOX_NAME=wine-icecc-node
  DISTROBOX_HOME=$HOME/$DISTROBOX_NAME
  ADD_PKGS="icecc gcc-multilib gcc-mingw-w64 vim tmux ccache"

  distrobox create --image ubuntu:latest  \
                   --name $DISTROBOX_NAME \
                   --home $DISTROBOX_HOME \
                   --additional-packages $ADD_PKGS
  ```
  Then you can enter the container like so (the first time after `distrobox create` can take take a few minutes):
  ```shell
  distrobox enter wine-icecc-node --no-workdir
  ```
  Proceed to  run the daemon and/or scheduler as explained below.

## Submit node
### Wine
You will need to inform `./configure` of your intentions to build with `icecc`. Prepend the desired values of your `*CC` environment variables with `icecc `, e.g.:
```shell
# 64-bit build
CC="icecc gcc" x86_64_CC="icecc x86_64-w64-mingw32-gcc" $wine_src/configure <other-flags>

# 32-bit build
CC="icecc gcc" i386_CC="icecc i686-w64-mingw32-gcc" $wine_src/configure <other-flags>
```

### Icecream
* Run the daemon:
  ```shell
  iceccd
  ```
  Common options:
  * `-v`/`-vv`/`-vvv` to increase verbosity. Useful when debugging.
  * `-l <logfile>` to redirect output to a logfile.
  * `-d` to detach the process from the shell.
* It's highly recommended to also install [icemon](https://github.com/icecc/icemon) or [icecream-sundae](https://github.com/JPEWdev/icecream-sundae). They are monitoring tools that provide information about notes participating in the `icecream` cluster and can help you identify issues that might arise. See [icemon section](#icemon).

### Start the build
Run `make` as usual. Increase the number of parallel jobs accordingly, e.g.:
```shell
make -j 16
```

## Execute node
You need to instead run the daemon with `sudo` (see [Security considerations](#security-considerations)), as the daemon needs to be able to execute jobs in a `chroot` environment:
   ```shell
   sudo iceccd -m 8 -u $USER
   ```
   Common options:
   * `-m <num-jobs>` to set the maximum number of compile jobs that can be started in parallel on the machine. If omitted, it defaults to the number of logical cores of the machine.

## Schedule node
Run the scheduler
  ```shell
  icecc-scheduler
  ```
  Common options:
  * `-v`/`-vv`/`-vvv` to increase verbosity. Useful when debugging.
  * `-l <logfile>` to redirect output to a logfile.
  * `-d` to detach the process from the shell.

  The scheduler doesn't *have* to run on any specific machine. Quoting `icecream` documentation:
  > Recommended is to start the scheduler and daemon on everybody's machine. The icecream schedulers will choose one to be the master and everyone will connect to it. When the scheduler machine goes down a new master will be selected automatically.
  [...]
  > You may also designate a scheduler machine, and then for each client specify the scheduler to use[...]

# Security considerations
* `icecream` does not provide an authentication mechanism; an `execute node` will **blindly execute any compilation job it receives from any `submit node`**.
* You should, therefore, run the daemon and scheduler with an **unprivilleged user**.
* However, regarding the daemon:
  * TDLR; **It will not be possible for a node to accept remote jobs** when run by an unprivilleged user (i.e. it will not be a functional `execute node`, even though the daemon will be running on it).
  * The whole story: apparently, as mentioned in `icecream` [documentation](https://github.com/icecc/icecream?tab=readme-ov-file#how-to-use-icecream), running the daemon as a privilleged user should not be necessary for homogeneous compilation clusters (i.e. where `submit` and `execute node`s have the same compiler). However, in practice, I've found that a node will **not** accept remote jobs when `iceccd` is run by an unprivilleged user. Even `man iceccd` seems to imply that all compilation jobs are executed in a `chroot` environment, regardless of cluster homogeinity:
    > The Icecream daemon has to run on all nodes being part of the Icecream compile cluster. It receives compile jobs and executes them in a chroot environment. The compile clients send their compile environment the first time they send a job to a particular daemon, so that the environment of the daemon does not have to match the one of the client.
* Consider using an unprivilleged container when running `icecc` (e.g. `distrobox`, suggested above).

# Icemon
`icemon` views during a distributed build:
| **Star**              |  **List**  |
:-------------------------:|:-------------------------:
![icemon-star](uploads/368bdfb2d97f7180f284e2954a3e1a92/icemon-star.png){ width=350px }  |  ![icemon-list](uploads/9010ae1d892e7cbc35ce876b00221927/icemon-list.png){ width=350px }
| **Gantt**             |  **Summary**  |
![icemon-gantt](uploads/312c0e5ba9be1cbe36372aa0adeec1dd/icemon-gantt.png){ width=350px }  |  ![icemon-summary](uploads/1f0a945de77742ced366c7fef2c7ef41/icemon-summary.png){ width=350px }

# Caveats
* Some jobs are *always* done on the `submit node`:
  * Linking
  * Any jobs that an `execute node` cannot run (for lack of proper configuration, the compiler is missing, or otherwise). For example, when building Wine there are calls to `winegcc`, `winebuild`, `flex`, `bison`.

  During stages of the build that mostly handle such jobs, the `submit node` can take a performance hit, as it effectively has to handle the build alone. As if that wasn't enough, it has likely also bit off more than it can chew (remember: you called `make -j <big-number>`).
* There can be bottlenecks, for example:
  * Network latency.
  * The `submit node` needs to be fast enough to dispatch jobs to be executed. This is especially important when a large number of parallel jobs is defined.
  * See the `icecream` documentation [here](https://github.com/icecc/icecream?tab=readme-ov-file#what-is-the-best-environment-for-icecream) and [here](https://github.com/icecc/icecream?tab=readme-ov-file#some-advice-on-configuration) for more.
* Here's a [talk](https://www.youtube.com/watch?v=VpK27pI64jQ) that explains how `icecream` works. It was given by the author of [icecream-sundae](https://github.com/JPEWdev/icecream-sundae).

# Improvements to this guide
* Add section to configure homogeneous environments:
  * This can be useful when an `execute node` is shared between developers that use different (but still `x86[_64]`-targeting) compilers
  * Explore the possibility of [cross-compiling](https://github.com/icecc/icecream?tab=readme-ov-file#cross-compiling-using-icecream) `x86[_64]` Wine binaries on poweful yet power-efficient ARM-based computers, such as an ARM-based Apple Mac Mini.
* Investigate offloading all stages of the build to `execute node`s, e.g.: `winegcc`, `winebuild`, `flex`, `bison`.
* Add section for `ccache`. The `iceccream` documentation [mentions](https://github.com/icecc/icecream?tab=readme-ov-file#how-to-combine-icecream-with-ccache) that even though `icecc` and `ccache` can be used together, it doesn't necessarily pay off:
  > Note however that ccache isn't really worth the trouble if you're not recompiling your project three times a day from scratch (it adds some overhead in comparing the source files and uses quite some disk space).
* Explore alternative distribuited build systems:
  * [sccache](https://github.com/mozilla/sccache/)
  * [FASTBuild](https://github.com/fastbuild/fastbuild)
  * [xmake](https://github.com/xmake-io/xmake/)
* Run a performance test over a VPN. If the outcome is positive, such a setup can provide value to a geographically distributed team. From the documentation:
  > Icecream is very sensitive to latency between nodes, and packet loss. While icecream has been successfully used by people who are on opposite sides of the earth, when those users were isolated to their geographic location the speed improved for everyone. In most corporate environments within a single building everything works well, but between two buildings often is troublesome.
