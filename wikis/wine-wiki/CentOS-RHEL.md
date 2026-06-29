---
title: CentOS/RHEL
---

[CentOS](https://www.centos.org/) is a community-based rebuild of the
source published by [Red Hat](https://www.redhat.com/en) with each
release. Consequently, Red Hat itself and other community rebuilds like
[Scientific Linux](https://www.scientificlinux.org/) should have very
similar instructions. In fact, at the very beginning of 2014, [Red Hat
Inc.
announced](https://www.redhat.com/en/about/press-releases/red-hat-and-centos-join-forces)
that they would officially sponsor and collaborate with the CentOS
project, much as they do with [Fedora](Fedora).

Rather than `sudo`, a common convention in Red Hat and related distros
has been to acquire super-user rights with `su -l`, then carry out the
necessary actions. The installation and repo-management commands listed
here presume you're in a terminal session as a super-user. However,
remember that you should **never** build wine as root or a super-user,
especially on Red Hat-like distros where it can particularly wreak
havoc.

## Installation

For those on **release 7**, be sure to read the next sub-section. As of
Mar. 2016, installing wine on CentOS 7 is a bit more involved; read
below for the reasons.

For any work with packages, you'll definitely want to be familiar with
your package manager. Up through release 7, the standard package manager
has been `yum`, but with Fedora adopting the leaner, meaner `dnf`
package manager, there's a good chance this will be increasingly
preferred, possibly even the default in release 8.

Since some releases of enterprise linux might not even include a wine
package by default, your best bet for finding a fresh package is
probably Fedora's [EPEL](https://fedoraproject.org/wiki/EPEL) repo
("Extra Packages for Enterprise Linux"). This repo contains updates and
extra packages backported from Fedora to more stable Red Hat-based
distros. If you want to enable the EPEL repo, all you need to do is
install the *epel-release* meta-package:

```sh
yum install epel-release    (if using yum)
dnf install epel-release    (if using dnf)
```

Then if you want the wine package from the EPEL, it's as simple as
another install command:

```sh
yum install wine    (yum users)
dnf install wine    (dnf users)
```

If your distro does include a wine package by default, you should be
able to use the above install command without even enabling the EPEL.

### Notes on EPEL 7

At the time of this writing, **EPEL 7** still has no 32-bit packages
(including wine and its dependencies). There is a 64-bit version of
wine, but without the 32-bit libraries needed for WoW64 capabilities, it
cannot support **any** 32-bit Windows apps (the vast majority) and even
many 64-bit ones (that still include 32-bit components).

This is primarily because with release 7, Red Hat didn't have enough
customer demand to justify an i386 build. While Red Hat itself still
comes with lean multilib and 32-bit support for legacy needs, this is
part of Red Hat's release process, not the packages themselves.
Therefore CentOS 7 had to develop its own workflow for building an i386
release, a process that was [completed in Oct
2015](https://seven.centos.org/2015/10/centos-linux-7-32-bit-x86-i386-architecture-released/).

With its i386 release, CentOS has cleared a major hurdle on the way to
an EPEL with 32-bit libraries, and now the ball is in the Fedora
project's court (as the maintainers of the EPEL). Once a i386 version of
the EPEL becomes available, you should be able to follow the same
instructions above to install a fully functional wine package for CentOS
7 and its siblings.

Thankfully, this also means that EPEL 8 shouldn't suffer from this same
problem. In the meantime though, you can keep reading for some hints on
getting a recent version of wine from the source code.

### Special Considerations for Red Hat

Those with a Red Hat subscription should have access to enhanced help
and support, but we wanted to provide some very quick notes on enabling
the EPEL for your system. Before installing the *epel-release* package,
you'll first need to activate some additional repositories.

On release 6 and older, which used the Red Hat Network Classic system
for package subscriptions, you need to activate the *optional* repo with
`rhn-channel`

```sh
rhn-channel -a -c rhel-6-server-optional-rpms -u `<your-RHN-username>` -p `<your-RHN-password>
```

Starting with release 7 and the Subscription Manager system, you'll need
to activate both the *optional* and *extras* repos with
`subscription-manager`

```sh
subscription-manager repos --enable=rhel-7-server-optional-rpms
subscription-manager repos --enable=rhel-7-server-extras-rpms
```

As for source RPMs signed by Red Hat, there doesn't seem to be much
public-facing documentation. With a subscription, you should be able to
login and [browse the repos](https://access.redhat.com/downloads/);
[this post on LWN](https://lwn.net/Articles/603865/) also has some
background.

## Building from Source

Now if you want a bleeding-edge wine release, or you just want to work
with the source code, [Building Wine](Building-Wine) from
source is probably your best bet. This has a few idiosyncrasies no
matter which version of CentOS / Scientific Linux you may be on, which
we'll go over.

One issue with extremely stable distros like CentOS is that your
libraries may be older versions than those required by the newest wine
release or the tip of the WineHQ git tree. In that case, you may need to
debug the build process a little and possibly build newer versions of a
library or two from source.

If you do build wine from source, it's **strongly suggested** that you
**don't install** it into your system but rather run it from within the
build-directory.

### Releases Other Than 7

On releases **5 and 6** (and hopefully 8+) of CentOS, multilib
capabilities should make installing the necessary build dependencies a
breeze (no chroot needed)... you just have to find them first. One
approach is the trial-and-error method of simply re-running *configure*
from the wine source code, installing whatever libraries it complains
are missing.

Another method is to use a build-dependency tool for your package
manager. If that's `yum`, you'll need to install the *yum-utils*
package, while `dnf` on the other hand needs *dnf-plugins-core*. One
minor annoyance is that if you haven't used source repos before on
CentOS, you'll also need to enable those in your package manager.
Otherwise your `builddep` tool won't be able to automatically resolve
dependencies.

- For packages from the EPEL, this is a breeze:

  ```sh
  yum-config-manager --enable epel-source    (for yum users)
  dnf config-manager --set-enabled epel-source    (for dnf users)
  ```

- For packages actually in CentOS proper... it's a bit more involved.
  You'll essentially need to:
  - Get a *.repo* file for your distro's source-RPMs
  - Copy it into your */etc/yum.repos.d/* directory
  - Enable the various repos with a *config-manager* command like above

  For now, [CentOS Bug
  \#1646](https://bugs.centos.org/view.php?id=1646) is probably the
  best source for what your *.repo* file should look like and other
  details. However, we may provide an updated *.repo* file for further
  refinement in the future.

Once you do have the source repos enabled, the actual installation
should take only a single command:

```sh
yum-builddep wine    (for yum users)
dnf builddep wine    (for dnf users)
```

Anyone that has recently built the latest version of wine from source on
CentOS / Scientific Linux / Red Hat is welcome to list all the
dependencies here. Then other users can try copying the list and passing
it directly to `yum` or `dnf` to install any build deps. However, note
that these lists are often out-of-date or incomplete, in which case
you'll have to fall back on one of the previous methods.

### For Release 7

For the same reasons that a functional wine package in EPEL 7 is still a
no-go, it used to be a labyrinth trying to build wine on CentOS 7. The
same lack of 32-bit libraries mentioned above is still a potential
obstacle. Fortunately, most of the necessary libraries are part of the
CentOS base repository, so with the 32-bit release of CentOS 7, only a
few extra libraries need to be built manually.

According to user "gcomes" [on the CentOS
forums](https://www.centos.org/forums/viewtopic.php?f=48&t=49542&sid=ca2d5867ab81661479f5d897ef2e9c80&start=10),
as of Feb. 2016, the only two libraries not provided in the i386 version
of CentOS 7 are *openal-soft* and *nss-mdns*. You should only need to
install the i386 release of CentOS (possibly to a
[chroot](Building-Wine#Chroot) or
[container](Building-Wine#Containers)) and wine's
dependencies, compile and install these additional two libraries, then
build wine from source. You can package the build results as a vanilla
32-bit RPM for your amd64 system.

If you want a WoW64 version, that should be possible too. Just place a
completed build directory for 64-bit wine somewhere your 32-bit image
can still access, then follow the [Shared
WoW64](Building-Wine#Shared-WoW64) instructions to complete
your build.

The multilib capabilities of Red Hat-based distros should theoretically
allow installing packages from i386 CentOS into an existing amd64
installation, then building everything without a chroot. However, we
have **not** tested this yet.

## See Also

- [Building Wine](Building-Wine)
- [Packaging](Packaging)

**Some Notes for Package Management on Red Hat:**

- [What is the command *rhn-channel* and how is it
  used?](https://access.redhat.com/solutions/57504)
- [How to enable/disable a repository using Red Hat Subscription
  Manager?](https://access.redhat.com/solutions/265523)
- [How to subscribe a system to a child channel using Red Hat Network
  (RHN) Classic?](https://access.redhat.com/solutions/11312)
