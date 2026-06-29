The source code for Wine, all Wine websites, and supplementary web tools
can be found online. You can explore the project's main source tree and
commit history (all the way back to the first version in 1993) at the
[Wine git tree](https://gitlab.winehq.org/wine/wine). You can also use
the [Wine cross-reference](https://source.winehq.org), although this only
goes back to Wine v1.0.

If you are interested in downloading the Wine source code, you can
clone portions of the source tree to your computer with
[Git](https://git-scm.com/). There is a [tutorial](Git-Wine-Tutorial)
on how to use Git with the Wine program source. The repositories are
hosted on the [WineHQ Gitlab](https://gitlab.winehq.org):

|                                                                 |                                                                                                                |
|-----------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| [appdb.git](https://gitlab.winehq.org/winehq/appdb)             | Code for the AppDB site and database                                                                           |
| [bugzilla.git](https://gitlab.winehq.org/winehq/bugzilla)       | Code for Wine's bugzilla site and database                                                                     |
| [fontforge.git](https://gitlab.winehq.org/wine/fontforge)       | A custom version of the [FontForge editor](https://fontforge.sourceforge.net/) for Wine fonts                  |
| [tools.git](https://gitlab.winehq.org/winehq/tools)             | The various webtools used to maintain parts of the Wine site                                                   |
| [vkd3d.git](https://gitlab.winehq.org/wine/vkd3d)               | 3D graphics library with an API similar to Direct3D 12 but a [Vulkan](https://www.khronos.org/vulkan/) backend |
| [website.git](https://gitlab.winehq.org/winehq/winehq)          | The WineHQ website code                                                                                        |
| [wine.git](https://gitlab.winehq.org/wine/wine)                 | The source for the actual Wine program                                                                         |
| [wine-gecko.git](https://gitlab.winehq.org/wine/wine-gecko)     | The source code for the Wine Gecko engine                                                                      |
| [wine-staging.git](https://gitlab.winehq.org/wine/wine-staging) | The Wine staging code                                                                                          |
| [mono](https://gitlab.winehq.org/mono)                          | The various Mono source repositories, including [wine-mono](Wine-Mono)                                         |

## Alternative Repositories

There are actually several other repositories for Wine scattered
around the internet, and in some situations, these alternative repos
can be very useful. However, if you want to submit patches to the
official upstream version of Wine, remember you must send a merge
request on the WineHQ Gitlab (as described in [Submitting
Patches](Submitting-Patches)).

- (Via HTTPS) You can find (bcompressed) copies of all Wine releases,
  either as complete code or incremental diffs, in the [source folder of
  WineHQ's Download site](https://dl.winehq.org/wine/source/).
- (Github Fans) The WineHQ git repo also has an [official mirror on
  Github](https://github.com/mirrors/wine).
- (Sundry Forks and Hacks) Jan Zerebecki maintains an up-to-date
  mirror of [Wine at repo.or.cz](https://repo.or.cz/w/wine.git), along
  with several branches that developers have created over the years to
  test ideas.
