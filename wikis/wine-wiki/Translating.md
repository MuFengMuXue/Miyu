## How is Wine translated?

*For translating the WineHQ.org website see
[here](Writers#translating).*

Nowadays Wine is completely localized through standard gettext PO files.
If you check out the Wine source you will find these in the
[po/](https://gitlab.winehq.org/wine/wine/-/tree/master/po)
directory. You can see the status of each translation along with a list
of potential consistency and spelling issues on the [Wine
PO](https://fgouget.free.fr/wine-po/) site.

Now for some more developer oriented details that you can skip:

All of the Wine dialogs and strings that need to be translated are
stored in standard .rc Windows resource files. These are then compiled
to the binary .res format using Wine's wrc compiler and linked with
Wine's libraries and programs. These resources can contain both
language-neutral and language-specific data. So the scheme is as
follows. Wine's .rc resource files only contain the English resources.
Then, during the compilation step, wrc looks up translations from the PO
files for the strings it finds, generates additional translated binary
resources. This way Wine ends up with resources for each language and
then uses the most appropriate one at run time based on the current
locale.

## How to improve the translation?

Wine is an Open Source project, thus anyone can download the source
code, modify the translations and send them to the wine-devel mailing
list for inclusion into the official Wine tree.

Note that translating Wine to a new language from scratch can take many
weeks. As for many other coding projects, it is recommended to send
patches often, here this would be as soon as you have a fair set of
translations you are happy with. This will reduce the risk and scope of
conflicts you may have to resolve.

It will also help if you fix or report all issues you find in the
English strings. Think of it as improving the 'English translation', and
helping your fellow translators by fixing the source before they base
their work on it.

### Using Wine's source

It is recommended to build Wine from source, so you can test the
translations. The recommended way to get the latest Wine source is to
use Git. (See [Git Wine Tutorial](Git-Wine-Tutorial) for a
guide to Git.)

To build Wine, follow the instructions on the [Building
Wine](Building-Wine) page. If your distro has its own page on
this wiki with distro-specific instructions, follow those.

After building Wine you can run it from the source directory without
installing it - e.g. run `~/wine-git/wine` or `~/wine-git/wine
program.exe` (if the Wine sources are in `~/wine-git`). You can also
start built-in programs by running e.g. `~/wine-git/wine notepad`. If
you don't already have Wine installed, you can install it by running
`make install` as root from the main source directory. Then the Wine
you have built can be started as just `wine`. However, if you have
installed another version of Wine don't run `make install` (unless you
remove the other Wine first) as this may lead to conflicts.

Once the above works you can edit your PO file, recompile Wine and check
that the new strings were taken into account.

Once you are satisfied with your translations, you can send a merge
request for inclusion into the official Wine Git. Read [Submitting
Patches](Submitting-Patches) about how to do it and how to check if
your merge request got applied.

### Using the Wine PO script

It is recommended for translators to get Wine's source and build it as
described above. However if that does not work for you, a script is now
available that will help you work on your translation. For instance,
let's assume you want to work on the Hungarian translation:

- First save the script below as 'winepo'.

``` bash
#!/bin/sh
# Copyright (C) 2012-2013 Francois Gouget
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301, USA


#
# Logging and error reporting
#

name0=`basename "$0"`
error()
{
    echo "$name0:error:" "$@" >&2
}


#
# Command line processing
#

opt_po=""
usage=""
while [ $# -gt 0 ]
do
    arg="$1"
    shift
    case "$arg" in
    -\?|-h|--help)
        usage=0
        ;;

    -*)
        error "unknown option '$arg'"
        usage=2
        ;;

    *)
        if [ -z "$opt_po" ]
        then
            opt_po="$arg"
        else
            error "only one PO file can be processed at a time"
            usage=2
            break
        fi
        ;;
    esac
done

if [ -z "$usage" ]
then
    if [ -z "$opt_po" ]
    then
        error "you must specify the PO file to work on"
        usage=2
    fi
fi

if [ -n "$usage" ]
then
    if [ "$usage" != "0" ]
    then
        error "try '$name0 --help' for more information"
        exit $usage
    fi
    cat <<EOF
Usage: $name0 LOCALE.po

Gets, updates and diffs the specified Wine PO file.

Where:
  LOCALE.po     The PO file to work on.
  --help, -h    Shows this help message.
EOF
    exit 0
fi


# Make sure the state is sane

rm -f "$opt_po.diff"
if egrep "(<<<<<<<|=======|>>>>>>>)" "$opt_po" >/dev/null 2>&1
then
    error "you must resolve the conflicts before running $name0 again (look for '<<<<<<<')"
    if [ -f "$opt_po.old" ]
    then
        echo "As a last resort you will find a backup of your PO file in '$opt_po.old'." >&2
    fi
    exit 1
fi
if [ -f "$opt_po.old" ]
then
    # The conflicts have been resolved so there is no point keeping this backup
    rm "$opt_po.old"
fi
if [ -f "$opt_po" -a ! -f "$opt_po.orig" ]
then
    error "the unmodified '$opt_po.orig' file is missing. Cannot update the PO file"
    exit 1
fi

# Make sure the files have regular linefeeds
# (otherwise the diffs will be unusable)

if which fromdos >/dev/null 2>&1
then
    # This should not hurt if it's already the case.
    if [ -f "$opt_po.orig" ]
    then
        chmod u+w "$opt_po.orig"
        fromdos "$opt_po.orig"
        chmod a-w "$opt_po.orig"
    fi
    if [ -f "$opt_po" ]
    then
        fromdos "$opt_po"
    fi
fi
if LANG= file "$opt_po.orig" | grep "CRLF" >/dev/null
then
    error "the '$opt_po.orig' file has CRLF line endings"
    exit 1
fi
if LANG= file "$opt_po" | grep "CRLF" >/dev/null
then
    error "the '$opt_po' file has CRLF line endings"
    exit 1
fi

# Save the previous changes

if [ -f "$opt_po" ]
then
    cp "$opt_po" "$opt_po.old"
    diff -u "$opt_po.orig" "$opt_po" >"$opt_po.diff"
fi


# Download the latest updates

echo "Updating $opt_po..."
if ! wget --no-verbose -O "$opt_po.new" "https://gitlab.winehq.org/wine/wine/-/raw/HEAD/po/$opt_po"
then
    error "unable to download the latest version of '$opt_po'"
    rm -f "$opt_po.diff"
    exit 1
fi
[ -f "$opt_po.orig" ] && chmod u+w "$opt_po.orig"
mv "$opt_po.new" "$opt_po.orig"
cp "$opt_po.orig" "$opt_po"
chmod a-w "$opt_po.orig"


# Reapply the previous changes if any

if [ -f "$opt_po.diff" ]
then
    if ! patch --merge <"$opt_po.diff"
    then
        echo
        error "'$opt_po' contains conflict(s) that you must now resolve (look for '<<<<<<<', as a last resort you will find a backup of your PO file in '$opt_po.old')"
        rm "$opt_po.diff"
        exit 0
    fi
    echo
    echo "'$opt_po' has been updated successfully and is ready for edition."
    rm -f "$opt_po.old"
fi


# Generate a new diff

dirname=`dirname "$opt_po"`
cd "$dirname"
opt_po=`basename "$opt_po"`

tmpdir="winepo.tmp.$$"
mkdir -p "$tmpdir/a/po" "$tmpdir/b/po"
cp "$opt_po.orig" "$tmpdir/a/po/$opt_po"
cp "$opt_po" "$tmpdir/b/po/$opt_po"

(cd "$tmpdir" && diff -u "a/po/$opt_po" "b/po/$opt_po") >"$opt_po.diff"
rm -rf "$tmpdir"
if [ -s "$opt_po.diff" ]
then
    echo "'$opt_po.diff' is ready for submission to wine-devel@winehq.org."
else
    rm "$opt_po.diff"
    echo "When the translation is ready, run '$name0 $opt_po' again."
fi

exit 0
```

- Make it executable by running 'chmod +x winepo' on the command line.
- Then on the
  [po/](https://gitlab.winehq.org/wine/wine/-/tree/master/po)
  page, identify which PO file corresponds to your language. For
  Hungarian this would be the 'hu.po' file.
- So then you would run 'winepo hu.po'.
- You can then edit the hu.po file to improve the translation. However
  make sure not to modify the 'hu.po.orig' file next to it.
- From time to time run 'winepo hu.po' again to resynchronize with any
  changes that occurred on the Wine side.
- This command will also generate a patch in 'hu.po.diff'.

When you feel you have something worth submitting, send the .diff file
to the [wine-devel](https://www.winehq.org/pipermail/wine-devel/) mailing
list.

### Translating po files

PO files are regular UTF‑8 text files which makes working with them
straightforward. PO entries have generally the following form:

```
#: hhctrl.rc:62 winhlp32.rc:31
msgid "&Print..."
msgstr ""
```

The above means that the files 'hhctrl.rc' and 'winhlp32.rc' contain the
English string '&Print...' on lines 62 and 31 respectively, and that it
has not been translated yet since *msgstr* is empty. To translate that
message just change the string after *msgstr*:

```
#: hhctrl.rc:62 winhlp32.rc:31
msgid "&Print..."
msgstr "&Imprimer..."
```

Note that some parts of the original string are important and must be
preserved in the translation:

- The ampersand '&' precedes the character to be used as the shortcut
  for this widget. So here, in an English locale pressing 'p' is the
  same as clicking on '&Print...'. The translation should usually
  specify its own shortcut, not necessarily for the same character. The
  tricky part is avoiding collisions between shortcuts. So here the
  French translator would have made sure none of the other dialog's
  widgets uses 'i' as its shortcut.
- The ellipsis means additional information will be asked before the
  action is taken. So if you click on a 'Print...' button you know you
  will have an opportunity to cancel the action before anything is done.
  Not so if you click on a 'Print' button. So preserving the ellipsis in
  the translation is very important.
- Also, double quotes must be escaped with a backslash so the string can
  be parsed by the PO tools.

Occasionally you will see entries like:

```
#: comdlg32.rc:195
#, fuzzy
msgid "Print"
msgstr "&Imprimer..."
```

This typically happens when a developer alters the original string so
that your translation is now outdated, or when a developer adds a new
string that looks like an already translated one. In the latter case
this is how the PO tools suggest using that other translation as a basis
for the new one. In any case a 'fuzzy' tag means the translation will no
longer be used by Wine. It also means that before removing it you should
carefully review and possibly update your translation as the changes are
sometimes hard to notice. In this case one would obviously have to
remove the ampersand and ellipsisis.

You can also see entries like:

```
#: foo.rc:123
#, fuzzy
#| msgid "old_string"
msgid "new_string"
msgstr "old_translation"
```

The `#| msgid` comment line indicates the previous msgid, which can
help updating the translation. It should be removed along with the
`fuzzy` line once the entry is updated.

### Adding po message contexts

[Message
contexts](https://www.gnu.org/s/hello/manual/gettext/Contexts.html#Contexts)
are normally used to disambiguate messages for the same untranslated
string. You can have several entries with the same untranslated string
in a PO file, provided that they each have a different context.

**Prerequisite**: enable *maintainer mode* using

`./configure --enable-maintainer-mode`

1. Locate strings to be "altered"

   Say for instance you have the following in your localized po file:

   ```
   #: file1.rc:123 file2.rc:456
   msgid "ambiguous terms"
   msgstr "translation"
   ```

2. Find appropriate translations by checking the respective rc
   entries, *e.g.*

   ```
   FOO "ambiguous terms" in file1.rc:123
   ```

   ```
   BAR "ambiguous terms" in file2.rc:456
   ```

   and determine their meaning/context (e.g. using some code browsing tools
   like [cscope](https://cscope.sourceforge.net/) to find references;
   running the program is recommended, ...)

3. Add the messages contexts

   - The following syntax is used:

    `translation` -> `#msgctxt#your context#translation`

   - You end up with something like

    `FOO "#msgctxt#context 1#ambiguous terms#"` in file1.rc:123

   - Similarly

    `BAR "#msgctxt#context 2#ambiguous terms#"` in file2.rc:456

4. Run `make`

5. Edit your po file to add the new translations, resulting in
   something like

   ```
   #: file1.rc:123
   msgctxt "context 1"
   msgid "ambiguous terms"
   msgstr "translation 1"
   ```

   and

   ```
   #: file2.rc:456
   msgctxt "context 2"
   msgid "ambiguous terms"
   msgstr "translation 2"
   ```

6. Ideally, remove the "#, fuzzy" automatically inserted in the
   en_US.po reference file (and en.po).

7. Run `make` again and test your changes.

In Wine the message context is sometimes also used to simply clarify the
meaning of the string to be translated. Here are a couple of examples:

```
#: sane.rc:32
msgctxt "unit: bits"
msgid "b"
msgstr ""
```

```
#: wordpad.rc:283
msgctxt "accelerator Bold"
msgid "B"
msgstr ""
```

### Dealing with strings that should not be translated

If a regular string resource should not be translated, first check to
see if it would make sense to remove it from the resources. Similarly,
if a label in a dialog should not be translated, it may mean that its
content is in fact supplied at runtime. In such a case the label should
be an empty string, and possibly have a comment next to it to identify
its function (though normally its id, e.g. MSGBOX_IDTEXT, should be
descriptive enough).

There are some cases where the above approaches don't work though. When
set the string context to 'do not translate'. This will tell wrc to not
include it in the PO files which will save much puzzling and work for
the translators. Here are a couple of examples:

```
/* GetSizeMax is the name of a COM method so it makes no sense to translate it */
PUSHBUTTON  "#msgctxt#do not translate#&GetSizeMax", IDC_GETSIZEMAX_BUTTON, 6, 49, 50, 14
```

```
/* '&u', '&b' and '&d' are formatting directives and thus should not be translated.
 * It's also unlikely their order would need to be modified.
 */
IDS_PRINT_FOOTER_TEMPLATE "#msgctxt#do not translate#&u&b&d"
```

## Resources

- [Wine PO](https://fgouget.free.fr/wine-po/)
- Microsoft's language-specific [Style
  Guides](https://www.microsoft.com/Language/en-US/StyleGuides.aspx)
- Microsoft's
  [Terminology](https://www.microsoft.com/Language/en-US/Terminology.aspx)
  reference translations

## Web-based translations systems

The Wine project would be very interested in making its PO files
available on web-based community translations systems such as
[Pootle](https://translate.sourceforge.net/wiki/pootle/index) or
[Launchpad](https://translations.launchpad.net/). Our hope is that this
would make translating Wine even easier and engage new translators.

The reason why it has not happened yet is that all Wine contributions,
including for translations, must be attributable to a specific author
and that these tools don't make that possible yet. For more details see
the wine-devel discussion
[here](https://www.winehq.org/pipermail/wine-devel/2011-September/092047.html)
and
[here](https://www.winehq.org/pipermail/wine-devel/2012-January/093908.html).
Any contributions that would solve this issue would be very welcome.

## Where can I find more help on translation?

Translating or localizing for those who are new to it can be daunting.
The [Localization
Guide](https://translate.sourceforge.net/wiki/guide/start#translation)
provides much help for those who are starting to translate for the first
time.

## How do I test my translation?

Wine uses the operating system's locale to decide what language to
use, but this can be overridden by changing the `LANG` environment
variable.  You may change `LC_ALL` instead of `LANG`, which will
override all locale settings (not just the language). To test a
particular language, you only need to set `LANG` to the appropriate
Unix locale and run the application.  Note that the locale must be
installed in your operating system. For Debian based systems you need
e.g. the package language-pack-fr for french.

If you translated a program you can (should) run it and check the
translation. If instead you translated a DLL, and you don't know what
programs use it, then it is good to at least check that the text in
dialogs isn't too big for the control rectangles. This can be done by
using a resource viewer/editor on the fake DLL. (Fake DLLs are created
while Wine is being built. They have a .dll.fake extension, and they
contain no code, only the resources.)

Resources inside such a file can be viewed by special programs. An
example of such a program that I know of and that can be freely
downloaded is [ResHacker](https://www.angusj.com/resourcehacker/). It's
an ANSI program, and cannot display UTF‑8 correctly (although it worked
for files converted from ISO‑8859‑1 if `#pragma code_page(65001)` is
used). You can view all the dialogs to check if they display fine.
Languages are on the third level of the tree on the left and are
identified by numeric IDs. Such an ID can be computed as (language_id +
1024 \* sublang_id) where the numerical language and sublanguage ids are
defined in
[include/winnt.h](https://gitlab.winehq.org/wine/wine/-/blob/HEAD/include/winnt.h)

Another method to check your translation is to use a resource editor,
e.g. [XN Resource
Editor](https://www.wilsonc.demon.co.uk/d10resourceeditor.htm) to open
the compiled resource files (.res) or even the dll (.dll.so). At least
XN Resource Editor opens them both without any problems.

## How to deal with truncated translations?

There is one hitch with the way Wine handles translations: it cannot
resize the dialogs so the translated labels fit. This is because the
Windows resource format relies entirely on hard-coded widgets positions
and sizes so that the information needed to redo the dialog layout is
missing. So sometimes a translation ends up being too large and is
truncated on display.

To keep things simple the way Wine deals with such issues is to have
someone make the dialog a bit larger so its widgets fit all
translations.

## See also

- [Adding New
  Languages](Wine-Developer's-Guide/Coding-Practice#adding-new-languages)
