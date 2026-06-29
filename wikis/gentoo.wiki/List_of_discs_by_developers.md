[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=List_of_discs_by_developers&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

[] This article has been flagged for not conforming to the [wiki guidelines](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Guidelines "Gentoo Wiki:Guidelines"). Please [help Gentoo out](https://wiki.gentoo.org/wiki/Help_improve_Gentoo_by_getting_involved_with_documentation!#Make_articles_conform_to_the_guidelines "Help improve Gentoo by getting involved with documentation!") by starting fixing things.

Some bugs such as [[[bug #716898]](https://bugs.gentoo.org/show_bug.cgi?id=716898)[]] are trivial to fix, if we can confirm the situation with an original CD/DVD.

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------- ---------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Package                                                                                                                                                                                                                                                                                                                                                                                                   Developers who own this disc                                                                                                            Checksum   Comment
  [[[games-fps/duke3d-data]](https://packages.gentoo.org/packages/games-fps/duke3d-data)[]]                     [Chewi](https://wiki.gentoo.org/wiki/User:Chewi "User:Chewi"), [ConiKost](https://wiki.gentoo.org/wiki/User:ConiKost "User:ConiKost")   \~         ConiKost: Duke3D Atomic Edition Retail
  [[[games-fps/quake1-data]](https://packages.gentoo.org/packages/games-fps/quake1-data)[]]                     [Chewi](https://wiki.gentoo.org/wiki/User:Chewi "User:Chewi")                                                                           \~
  [[[games-fps/quake2-data]](https://packages.gentoo.org/packages/games-fps/quake2-data)[]]                     ?                                                                                                                                       \~         Needed for [[[bug #716898]](https://bugs.gentoo.org/show_bug.cgi?id=716898)[]].
  [[[games-fps/quake3-data]](https://packages.gentoo.org/packages/games-fps/quake3-data)[]]                     [ConiKost](https://wiki.gentoo.org/wiki/User:ConiKost "User:ConiKost")                                                                  \~         Was last-rited but could bring it back with [ioq3](https://github.com/ioquake/ioq3) (git snapshot, as latest stable release contains security problems). Maybe overlay?
  [[[games-fps/return-to-na-pali]](https://packages.gentoo.org/packages/games-fps/return-to-na-pali)[]]   [Chewi](https://wiki.gentoo.org/wiki/User:Chewi "User:Chewi"), [ConiKost](https://wiki.gentoo.org/wiki/User:ConiKost "User:ConiKost")   \~         Chewi: Unreal Anthology DVD. Never added but want to, maybe in overlay. ConiKost: Unreal Gold Retail
  [[[games-fps/rtcw-data]](https://packages.gentoo.org/packages/games-fps/rtcw-data)[]]                           [Chewi](https://wiki.gentoo.org/wiki/User:Chewi "User:Chewi")                                                                           \~         Was last-rited but could bring it back with [iortcw](https://github.com/iortcw/iortcw).
  [[[games-fps/unreal]](https://packages.gentoo.org/packages/games-fps/unreal)[]]                                    [Chewi](https://wiki.gentoo.org/wiki/User:Chewi "User:Chewi"), [ConiKost](https://wiki.gentoo.org/wiki/User:ConiKost "User:ConiKost")   \~         Chewi: Unreal Anthology DVD. Was last-rited but want to restore it, maybe in overlay. ConiKost: Unreal Gold Retail
  [[[games-fps/unreal-tournament]](https://packages.gentoo.org/packages/games-fps/unreal-tournament)[]]   [Chewi](https://wiki.gentoo.org/wiki/User:Chewi "User:Chewi"), [ConiKost](https://wiki.gentoo.org/wiki/User:ConiKost "User:ConiKost")   \~         Chewi: Unreal Anthology DVD. Was last-rited but want to restore it, maybe in overlay. ConiKost: Unreal Tournament GOTY Retail
  [[[games-fps/ut2004-data]](https://packages.gentoo.org/packages/games-fps/ut2004-data)[]]                     [Chewi](https://wiki.gentoo.org/wiki/User:Chewi "User:Chewi"), [ConiKost](https://wiki.gentoo.org/wiki/User:ConiKost "User:ConiKost")   \~         Chewi: Unreal Anthology DVD. ConiKost: UT2004 Retail Discs
  [[[games-rpg/comi]](https://packages.gentoo.org/packages/games-rpg/comi)[]]                                          [Chewi](https://wiki.gentoo.org/wiki/User:Chewi "User:Chewi"), [ConiKost](https://wiki.gentoo.org/wiki/User:ConiKost "User:ConiKost")   \~         ConiKost: MI1+2 Value Pack
  [[[games-action/rune]](https://packages.gentoo.org/packages/games-action/rune)[]]                                 ?                                                                                                                                       \~         Needed for [[[bug #154735]](https://bugs.gentoo.org/show_bug.cgi?id=154735)[]].
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------- ---------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Developers, who have no CD/DVD/.. media: [Jstein](https://wiki.gentoo.org/wiki/User:Jstein "User:Jstein")

### [Brainstorming for the checksum]

A checksum can indicate, if the developer uses the same media as the user who reports a bug. A user can also verify the media. Broken media, or different release can result in strange bugs which are hard to track.

Requirements on the checksum:

-   all users and developers should be able to generate and verify the checksum
-   the checksum does not need to be secure. Just want to check if we have the right CD at hand.
-   md5 is probably strong enough and short
-   checksum must be independent of the user environment (i.e. localization)
-   checksum method must work on media with copyright protection

Ideas:

-   :::: cmd-box


    `user `[`$`]`find -printf "%P\0%s\0" | md5sum`


    ::::

-   :::: cmd-box


    `user `[`$`]`isoinfo`


    ::::