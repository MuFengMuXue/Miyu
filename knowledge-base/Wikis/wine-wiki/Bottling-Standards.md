In the past several years, many of the old wine front-ends that existed
have been abandoned, with active development concentrated on the few
that remain. Even then, neither prefix management nor workaround recipes
are mutually compatible across the different front-ends.

Think of this page as a working draft (feel free to edit it) for a
unified approach to these problems.

For a list that includes all of the active front-ends, see [Third Party
Applications](Third-Party-Applications). Since
[winetricks](Winetricks) is arguably the lowest-level and
communicates the most with us at wine, they would be a prime candidate
for patches. Contributions and ideas are welcome from any of the
projects though (so long as any code has a compatible license).

## Prefix Locations

For different wrappers to recognize prefixes created by each other, some
sort of standard is necessary. While other methods are possible (a
registry? gulp), the current method used in at least winetricks is
pretty sensible.

First, a single directory is created in the standard user data
directory, `$XDG_DATA_HOME/wineprefixes`, then individual prefixes are
installed within the `wineprefixes` directory. If a user chooses to
install a prefix elsewhere, then a symlink can be added to this
directory instead.

On systems where `$XDG_DATA_HOME` is not set by default, front-ends
should use `$HOME/.local/share/` by default

## Prefix & Recipe Metadata

To keep prefix names simple and stay true to unix design ideas, any
prefix metadata should be kept in plaintext (UTF‑8) files and somehow
confined to the wine prefix, or at least wine-related directories. These
files will hopefully also be as minimal as possible, and new metadata
tags should not be added lightly.

Winetrick's current approach is a good foundation. Every prefix includes
a file named *wrapper.cfg* (at the top-level of a prefix next to
*user.reg*), which stores the prefix's longer title. Then whenever a new
verb is installed in a prefix, metadata *specific to the verb* is
registered in a new file, according to the convention
*current_prefix/verb_category/verb_name.vars*

Here is a list of metadata tags (not necessarily complete or formatted
exactly) currently used in at least winetricks and/or PlayOnLinux...

|                   |                                                                      |                                                                            |
|-------------------|----------------------------------------------------------------------|----------------------------------------------------------------------------|
| title             | Name of the app (ideally the same as on AppDB)                       |                                                                            |
| publisher         | E.g. "Adobe" or "Electronic Arts"                                    |                                                                            |
| year              | Year title was released **for PC**                                   |                                                                            |
| media             | Typically "download" or "dvd"                                        | If empty, the verb may be interpreted as not installable                   |
| conflicts         | A space-separated list of verbs that cannot share the same prefix    |                                                                            |
| file*n*           | The filename (and relative path if needed) of the installer          | May have multiple tags beginning with *n = 1*                              |
| installed_exe*n*  | Filename (and rel-path) of a binary installed by the verb            | Multiple tags begin with *n = 1*                                           |
| installed_file*n* | Filename (and rel-path) of libraries and other files installed       | Multiple tags begin with *n = 1*                                           |
| homepage          | The active webpage for the title                                     | Not necessarily the download page or the company's main page               |
| unattended        | Enter "no" if the verb requires user input                           | Not using this tag equivalent to "yes"                                     |
| wine_showstoppers | Report number (no pound sign or other text) of a blocking WineHQ bug | Suppresses the verb on menus unless the front-end is in an "advanced" mode |
| wineversion       | A version of wine known to work with the recipe                      | Not required and some front-ends (like winetricks) may ignore it           |

Some value strings are parsed by functions and scripts, and special
characters like `$` or `..` may still have their typical shell
semantics.

## Removing Prefixes

So long as the above guidelines are followed, with all files (or
symlinks) maintained in a prefix, front-ends should be able to remove
prefixes cleanly and easily. Just don't forget to have your front-end
handle symlinks appropriately when deleting a prefix.

Perhaps the main complication is handling any menu items and icons
registered with the user's desktop environment. At least on environments
that follow the freedesktop specs for [desktop
entries](https://www.freedesktop.org/wiki/Specifications/desktop-entry-spec/)
and [menus](https://www.freedesktop.org/wiki/Specifications/menu-spec/),
this should not be too difficult. A previous suggestion was to have
[winemenubuilder](Commands/winemenubuilder) place *.desktop* and
*.directory* files in each prefix, then symlink to them from the
appropriate folders in the user's environment. The idea was that this
way, deleting the prefix would remove the actual files, and under the
freedesktop specs, the user's environment should just ignore the
dangling symlinks.

However, as long as a front-end's delete procedure can trace symlinks
correctly, keeping *.desktop* files in the user's environment and
tracking them with symlinks *from* the prefix might be cleaner. Since
menu entries map one-to-one to a specific command (with unique options
and context), sharing menu items between prefixes shouldn't be an issue.
For *.directory* files, a check-and-delete for empty menu folders is
worth considering too.

## Workaround Recipes

Right now, at least winetricks and PlayOnLinux v4 verbs (aka recipes)
consist of a metadata statement followed by a shell script that uses
pre-defined functions to carry out the verb. Unfortunately, while the
pre-defined functions are used very similarly, they do not form a
unified API.

Beyond settling on standard functions for scripts, making the recipe
itself declarative as possible would be nice. If a default logical flow
could handle most recipes, then only metadata flags and quick shell
fragments for exceptional steps would be necessary. A first step towards
this might be to include dependency entries in the metadata (some
recipes in winetricks already make use of a "conflicts" list).

Finally, if the goal is to offer a single library of recipes, AppDB
would arguably be the most natural place to keep them. There hasn't been
any discussion of this though, and even if WineHQ were willing to
consider the idea, updates or an overhaul of AppDB may be necessary.
