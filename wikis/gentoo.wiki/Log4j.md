[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Log4j&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://logging.apache.org/log4j/2.x/)

[[]][GitWeb](https://gitbox.apache.org/repos/asf?p=logging-log4j2.git)

[[]][GitHub](https://github.com/apache/logging-log4j2)

[[]][dev-java/log4j-api](https://packages.gentoo.org/packages/dev-java/log4j-api)

[[]][dev-java/log4j-core](https://packages.gentoo.org/packages/dev-java/log4j-core)

[[]][dev-java/log4j-12-api](https://packages.gentoo.org/packages/dev-java/log4j-12-api)

Apache Log4j is a Java-based [logging](https://wiki.gentoo.org/wiki/Logging "Logging") utility. It consists of several modules the most important which of are already available as packages in Gentoo:

-   [[[dev-java/log4j-api]](https://packages.gentoo.org/packages/dev-java/log4j-api)[]]
-   [[[dev-java/log4j-core]](https://packages.gentoo.org/packages/dev-java/log4j-core)[]]
-   [[[dev-java/log4j-12-api]](https://packages.gentoo.org/packages/dev-java/log4j-12-api)[]]

\
These packages do not yet have [tests enabled](https://bugs.gentoo.org/784263) because of still missing dependencies, e.g. [[[bug #829070]](https://bugs.gentoo.org/show_bug.cgi?id=829070)[]], [[[bug #833456]](https://bugs.gentoo.org/show_bug.cgi?id=833456)[]]. Engaged hackers are welcome to make themselves familiar with the [Gentoo Java Packing Policy](https://wiki.gentoo.org/wiki/Gentoo_Java_Packing_Policy "Gentoo Java Packing Policy") and [pullrequest](https://wiki.gentoo.org/wiki/GitHub_Pull_Requests "GitHub Pull Requests") their [contributions](https://wiki.gentoo.org/wiki/Contributing_to_Gentoo "Contributing to Gentoo").

## [Installation]

The log4j-\* packages like libraries in general are pulled-in by their [reverse dependencies](https://packages.gentoo.org/packages/dev-java/log4j-12-api/reverse-dependencies) so that there is no need to emerge them directly and recording them in [/var/lib/portage/world](https://wiki.gentoo.org/wiki//var/lib/portage "/var/lib/portage") is a bad idea.

### [USE flags]

USE flags are the same as for [most java packages](https://wiki.gentoo.org/wiki/Gentoo_Java_USE_flags "Gentoo Java USE flags").

### [USE flags for] [dev-java/log4j-api](https://packages.gentoo.org/packages/dev-java/log4j-api) [[]] [The Apache Log4j API]

  ----------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`doc`](https://packages.gentoo.org/useflags/doc)                 Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`source`](https://packages.gentoo.org/useflags/source)           Zip the sources and install them
  [`test`](https://packages.gentoo.org/useflags/test)               Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`verify-sig`](https://packages.gentoo.org/useflags/verify-sig)   Verify upstream signatures on distfiles
  ----------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-02-03 10:39] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [USE flags for] [dev-java/log4j-core](https://packages.gentoo.org/packages/dev-java/log4j-core) [[]] [The Apache Log4j Implementation]

  ----------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`doc`](https://packages.gentoo.org/useflags/doc)                 Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`source`](https://packages.gentoo.org/useflags/source)           Zip the sources and install them
  [`test`](https://packages.gentoo.org/useflags/test)               Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`verify-sig`](https://packages.gentoo.org/useflags/verify-sig)   Verify upstream signatures on distfiles
  ----------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-02-06 09:12] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [USE flags for] [dev-java/log4j-12-api](https://packages.gentoo.org/packages/dev-java/log4j-12-api) [[]] [The Apache Log4j 1.x Compatibility API]

  ----------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`doc`](https://packages.gentoo.org/useflags/doc)                 Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`source`](https://packages.gentoo.org/useflags/source)           Zip the sources and install them
  [`test`](https://packages.gentoo.org/useflags/test)               Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`verify-sig`](https://packages.gentoo.org/useflags/verify-sig)   Verify upstream signatures on distfiles
  ----------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-02-06 09:12] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]