Many software vendors include [copy
protection](https://en.wikipedia.org/wiki/Copy_prevention) in their
applications (mostly in games). For the most part, copy protection
focuses on establishing that the user has an original disc (i.e. a CD or
DVD as supplied by the manufacture and not a copy supplied by someone
else). This adds inconvenience for the end user, but grants the software
vendors some peace of mind knowing that fewer people are
[pirating](https://en.wikipedia.org/wiki/Software_piracy) their software.

In an effort to make copy protection more effective (i.e. resistant to
cracks), the methods used by many copy protection products have become
complex, difficult to understand (obfuscated), and hard to debug. In
some cases Wine would need to be altered to allow for almost
[rootkit](https://en.wikipedia.org/wiki/Rootkit)-like functionality of
programs to get some of these copy protection schemes to work. To
support copy protection Wine developers have to contend with
undocumented interfaces, code obfuscation, and maintaining compatibility
with \*nix security models.

Wine cannot and will not break the functionality of these copy
protection products. Wine's goal is to be compatible with Windows
software, including copy protection. Although some would advocate the
use of illegally modified or "cracked" games, Wine does not support,
advocate, or even view this as a solution. The use of cracks is
considered off topic on the forums, IRC channels, etc and will not be
tolerated (summarily dismissed and deleted).

That said, there are some forms of copy protection that do work in Wine
and some that do not (resulting in applications refusing to run or to
crash altogether). This page identifies which copy protection products
work in Wine, which ones do not, and what
[Bugzilla](https://bugs.winehq.org/) entries are used to track issues.

## Copy protection that works:

- Safedisc 1.x: see bug #9925 -- FIXED
  (2008-01-04) used for example in: Age Of Empires 2, System Shock 2,
  Heroes of Might and Magic II, III
- Safedisc 2.x: works since 0.9.49 used for example in: Max Payne,
  Battlefield 1942 might have problems when using certain (newer)
  *gcc* versions.
- older Securom 4.xx: not working with linux: 2.6.9,2.6.10(x86) and
  2.6.9-2.6.15(x86_64) (ptrace bug) or when using gcc 4.0.x used for
  example in: Diablo II, Warcraft III (appdb pages for these have more
  details about problematic configurations), Pharoh, Sierra's Emperor,
  RollerCoaster 2

May face trouble when installing two of these simultaneously.

- Ring Protech: used for example in german titles: Ronja Räubertochter,
  Fritz und Fertig Schach, Felix abenteuerliche Reise auf 5 Kontinenten

It uses the standard mcicda dll to check something on the CD. This dll
serves to play music off a CD's audio tracks. If Wine cannot play audio
tracks using mcicda on your machine for whatever reason, then apps
protected with Ring Protech will fail to start.

## Copy protection that doesn't work:

- Safedisc 3.x: see bug #219 -- FIXED
- Securom 5.xx (and higher): see bug #7065 -- FIXED
- Starforce: used in big number of racing games, see bug #3260
- ProtectCD/ProtectDISC: see bug #9484
- XStreamlok
- GameGuard
- PunkBuster: see bug #9685 -- WONTFIX
- Protect DiSC: see bug #9484
- Tages: see bug #10264 -- FIXED
- Pace Interlok: see bug #12297 -- FIXED
- Oreans (oreans32.sys): see bug #21959 -- ABANDONED
- UPlay for Rocksmith (Win32_PnPEntity WMI class): see bug #35224 --
  INVALID; see AppDB page
  [here](https://appdb.winehq.org/objectManager.php?sClass=version&iId=29238)
