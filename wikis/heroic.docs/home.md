# Home

Welcome to the Heroic Games Launcher wiki!

### What is the Heroic Games Launcher?
Heroic Games Launcher, or simply "Heroic", is a native GUI alternative to multiple launchers for Linux, Windows and MacOS.
It is open source under GPLv3 and is maintained by a community of developers that work **for free on their free time**.

Currently, Heroic supports Epic games (through Legendary, a CLI tool that deals with authentication, downloading, and launching Epic Games), GOG games (through GOGdl, a CLI tool that deals with authentication, downloading, and launching GOG games), and Amazon games (through Nile, a CLI tool that deals with authentication, downloading, and launching Amazon games).

Support to add your own games and websites (think Steam's "Add Non-Steam Game" feature) is also available.

### Why should you use _**Heroic?**_


Heroic is a community-built, open-source launcher. This means that anyone can suggest changes or find optimizations, and can check what the code is like under the hood!

Because of that, Heroic uses less resources than the Epic Games Launcher, and is, in general, a lot snappier:

|         Task                     |  Heroic |    EGL     |
| -------------------------------- | ------- | ---------- |
| Installer size                   | 92MB    | 150MB      |
| First-launch updates             | N / A   | 529MB      |
| Disk space used                  | 344MB   | 929MB      |
| RAM Usage (library - Grid View)  | ~190MB* | ~306MB*    |
| RAM Usage (library - List View)  | ~223MB* | ~368.7MB*  |
| RAM Usage (store)                | 210MB*  | 450MB*     |
| RAM Usage (In-game)              | ~230MB* | ~232MB*    |
| CPU Usage when Idle In-game      | 0-2%**  | 0-2%**     |
| Linux support?                   | Yes     | No         |

### Launcher Launch Time Tests:
Everything non-essential program-wise was closed to prevent interference. EGL and Heroic were set up to load into whatever is the default (EGL goes to EGS, and Heroic goes to the Library in List View).

**For EGL:** The launch time was 16.45 seconds to open EGS. Note that this open the Store, and there's no option to go to the library on startup; as a matter of note, the EGL does have a persistent quick launch sidebar for the last four games you've played that displays on all pages.

**For Heroic:** The Launch time is 14.37 seconds to open Heroic. Note that this opens to the library, and had it opened to the store page, it would've been slower.

### Store Switching Tests:
All Footnotes above apply, as well as the human factor of "I'm not a robot" so the timings are a little off. For testing, the timer was stopped when all images had loaded onto the store preview.

**For EGL:** Switching from the Store to the Library took 2.02 seconds when in List View. In Grid View, this was extended to 2.31 seconds. Doing the reverse (Library to Store) netted 2.02 seconds for both List View and Grid View.

**For Heroic:** Switching from the Store to the Library is practically instant in either List View or Grid View (both are 0.5 seconds or below). Doing the reverse (Library to Store) netted 5.3 seconds (List View) and 5.8 seconds (Grid View).

The reason EGS is faster in this regard is simply because the launcher was made to load images at the same rate as anything else on the page, Heroic is slower in this regard. For the curious, if you tweaked the restriction to "loading the page to being recognisably the EGS site", then the numbers are about the same (2.7 seconds for list view, 2.9 seconds for Grid View).

### Can Heroic use EOS?
Yes! As of 18/07/2022 ([2.4.0 - beta 2](https://github.com/Heroic-Games-Launcher/HeroicGamesLauncher/releases/tag/v2.4.0-beta.2)), Heroic has made it easy to enable support, as long as DXVK is updated to its latest version, and will apply for that Wine prefix. It can be downloaded via the Heroic Settings and can be found on the Game Page, then in the "Tools" menu. You may also need to install `corefonts` from winetricks.

Legendary had already added support for it via it's 20.24 version on 09/01/2022 ([see here](https://github.com/derrod/legendary/releases/tag/0.20.24)), but it was only for Windows.

# Footnotes:
\* Initially, RAM usage was higher for both Heroic and the EGL. After around a minute, these values shown were recorded.
\** Tested on a Ryzen 5 1500x (4 cores, 8 threads; Windows counts the threads as cores on Task Manager weirdly) running Windows 10 Pro, and 8GB DDR4 RAM. [All data collected can be found here](https://imgur.com/a/jfV48v7), and was run on [2.0.2 Zoro Hotfix #2](https://github.com/Heroic-Games-Launcher/HeroicGamesLauncher/releases/tag/v2.0.2). This graph will be updated after 2.4.0 gets out of beta, so watch this space!
\
