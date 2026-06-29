# Custom configuration

This page describes how to add a *custom* keyboard layout or option so that it
will be parsed by libxkbcommon.

@attention 👋 First time hacking your keyboard layout?

@attention 📝 Read the @ref important-notes "" below before proceeding to
@ref custom-config-quick-start ""!

@attention 💡 See also the @ref faq "FAQ".

## Important notes

@note For an *introduction* to XKB and keymap components, please see
“@ref xkb-intro ""”.

@note For the complete *XKB text format specification*, see
@ref keymap-text-format-v1-v2 "".

@note For *distributing* keyboard layouts, see @ref packaging-keyboard-layouts "".

@note The following instructions focus on a *user* configuration; it can be
extended to a *system-wide* configuration by replacing `$XDG_CONFIG_HOME` with
the [system configuration directory](@ref system-configuration) in the file
locations. See @ref xkb-data-locations "" for further details.

@note Applying layout changes depends on the setup: most desktop environments
propose a dedicated GUI to configure it. Please consult the corresponding
configuration.

@warning The instructions of this page requires libxkbcommon as keymap compiler
and **does not work in _X11_** sessions, because X servers have hard-coded paths.
Check your session type in the “information” or “about” screen of you desktop
environment, or execute the following command: `echo $XDG_SESSION_TYPE`.

@warning In particular neither `setxkbmap` nor `xkbcomp` does work in Wayland
sessions.

@important An erroneous XKB configuration may make your keyboard unusable.
Therefore it is advised to try custom configurations safely in user-space using
`xkbcli` tools; see “@ref testing-custom-config ""” for further details.

@tableofcontents{html:2}

## Quick start: your first custom layout

This example creates a minimal custom layout that swaps the number row (numbers
require <kbd>Shift</kbd>).

This works by defining a new [symbols] file, which tells XKB how keys
map to characters.

[symbols]: @ref config-symbols-def

### Step 1: Create directory for testing

Create a temporary XKB directory (used later via `--include`):

```shell
mkdir -p "/tmp/xkb/symbols"
```

### Step 2: Define a symbols file

Create the file: `/tmp/xkb/symbols/test` with the following content:

```c
default partial alphanumeric_keys
xkb_symbols "basic" {
    include "us(basic)" // Use the US Qwerty layout as a base
    name[Group1]= "Test (Swapped numbers)";

    // Map keys <XXXX> to key symbols, ordered by their shift level
    key <AE01> { [ exclam,          1]     };
    key <AE02> { [ at,              2]     };
    key <AE03> { [ numbersign,      3]     };
    key <AE04> { [ dollar,          4]     };
    key <AE05> { [ percent,         5]     };
    key <AE06> { [ asciicircum,     6]     };
    key <AE07> { [ ampersand,       7]     };
    key <AE08> { [ asterisk,        8]     };
    key <AE09> { [ parenleft,       9]     };
    key <AE10> { [ parenright,      0]     };
};
```

### Step 3: Test the layout

Use the `xkbcli` tool provided by the `libxkbcommon-tools` package (or similar)
to compile and inspect the new layout:

```shell
xkbcli compile-keymap --include /tmp/xkb \
                      --include-defaults \
                      --test \
                      --layout test \
&& echo "valid!" || echo "invalid!"
```

Compilation should succeed and print “valid!”.

@note If something goes wrong, your system layout is unaffected as long as you
only use the layout with `xkbcli` in the `/tmp` directory.

To preview how keys behave interactively, use the following command. It will
open a window that needs to *stay focused* and log the keys in the terminal.
Use <kbd>Esc</kbd> to quit.

```shell
xkbcli compile-keymap --include /tmp/xkb \
                      --include-defaults \
                      --layout test \
| xkbcli interactive
```

If everything worked, you now have a working custom keyboard layout named `test`!

### Step 4: Use the layout

@important This step does affect your system. Ensure that the layout *compiles*
(see the previous step) before going further.
*An erroneous layout may make your keyboard __unusable__!*

1. The layout needs to be moved to `$XDG_CONFIG_HOME/xkb/symbols/test` –
   where `$XDG_CONFIG_HOME` is usually `$HOME/.config` – so it is in the
   *default* libxkbcommon [include paths](@ref xkb-data-locations).
2. Enabling the keyboard layout depends on your environment. On desktop
   environments (e.g. GNOME, KDE), the GUI configuration tools require a
   further step: see @ref discoverable-layouts "". Other configuration methods
   depend on your environment and are not covered here.

   @note If the layout is not available, try restarting your session.

### Step 5: Going further

This example defines a single simple layout. Read on to discover more advanced
customizations:

Explains how to make the customizations available in the keyboard configuration
tools of your desktop environment

@note It is advised to try configurations safely in user-space using a
*dedicated directory* that is not in the libxkbcommon default paths (e.g. *not*
`$XDG_CONFIG_HOME`); see “@ref testing-custom-config ""” for further details.

## XKB data locations

libxkbcommon searches the following paths for XKB configuration files:

@anchor user-configuration
`$XDG_CONFIG_HOME/xkb/`, or `$HOME/.config/xkb/` if the `$XDG_CONFIG_HOME`
environment variable is not defined. See the [XDG Base Directory Specification]
for further details.
@deprecated `$HOME/.xkb/` as a *legacy* alternative to the previous XDG option.
@anchor system-configuration
`$XKB_CONFIG_EXTRA_PATH` if set, otherwise `<sysconfdir>/xkb` – where
`<sysconfdir>` is a placeholder for the system configuration directory
(`/etc` on most distributions). Example: `/etc/xkb`.
See @ref packaging-keyboard-layouts "".
`$XKB_CONFIG_ROOT` if set, otherwise the data directory of the `xkeyboard-config`
(or `xkb-data`) package (denoted `<xkb-config-root>` in the rest of the page):
`<datadir>/xkeyboard-config-<VERSION>` or `<datadir>/X11/xkb` on older setups.
`<datadir>` is a placeholder for the package data; on most distributions this is
`/usr/share`. Example: `/usr/share/xkeyboard-config-2` and `/usr/share/X11/xkb`.

@warning Do not modify the system XKB root files, because they will be
overwritten by any update of the `xkeyboard-config` (also: `xkb-data`) package.

[XDG Base Directory Specification]: https://specifications.freedesktop.org/basedir-spec/latest/

A keymap created with `xkb_keymap::xkb_keymap_new_from_names2()` will look up
those paths in order until the required data is found.

@note Where libxkbcommon runs in a privileged context (e.g. as `root`), only the
system path is available (`<xkb-config-root>`).

@note The rest of the page assumes configuring a *user* configuration; it can
be extended to a *system-wide* configuration by replacing `$XDG_CONFIG_HOME`
with `<sysconfdir>` in the file locations (see in the table above).

Each directory should have one or more of the following subdirectories:
- [`compat`](@ref config-compat-def)
- [`geometry`](@ref config-geometry-def) (libxkbcommon ignores this directory)
- [`keycodes`](@ref config-keycodes-def)
- [`rules`](@ref config-rules-def)
- [`symbols`](@ref config-symbols-def)
- [`types`](@ref config-types-def)

The majority of user-specific configurations involve modifying [key symbols] and
this is what this document focuses on. For use-cases where a user may need to
add new [key types] or [compat entries] the general approach remains the same. See
“@ref keymap-text-format-v1-v2 ""” for detailed descriptions for how to add
those types or compat entries.

You should never need to add user-specific [keycodes]. Where a keycode is missing,
the addition should be filed in the upstream [xkeyboard-config] project.

[xkeyboard-config]: https://gitlab.freedesktop.org/xkeyboard-config/xkeyboard-config
[key symbols]: @ref keysym-def
[key types]: @ref key-type-def
[compat entries]: @ref the-xkb_compat-section
[keycodes]: @ref keycode-def

## How keyboard layout and options names map to keyboard data (RMLVO vs KcCGST)

Due to how XKB is configured, there is no such thing as a “layout” in XKB
itself, or, indeed, any of the rules, models, variant, options ([RMLVO]) described
in `struct xkb_rule_names`. [RMLVO] names are merely lookup keys in the
rules file provided by [xkeyboard-config] to map to the correct keycode, compat,
geometry (ignored by libxkbcommon), symbols and types ([KcCGST]). The [KcCGST]
data is the one used by XKB and libxkbcommon to map keys to actual symbols.

[RMLVO]: @ref RMLVO-intro
[KcCGST]: @ref KcCGST-intro

For example, a common [RMLVO] configuration is layout `us`, variant `dvorak` and
option `terminate:ctrl_alt_bksp`. Using the default rules file and model
this maps into the following [KcCGST] components:

@figure@figcaption
Output of the command:
`xkbcli compile-keymap --kccgst --layout us --variant dvorak --options terminate:ctrl_alt_bksp`
@endfigcaption
```c
xkb_keymap {
	xkb_keycodes  { include "evdev+aliases(qwerty)"	};
	xkb_types     { include "complete"	};
	xkb_compat    { include "complete"	};
	xkb_symbols   { include "pc+us(dvorak)+inet(evdev)+terminate(ctrl_alt_bksp)"	};
	xkb_geometry  { include "pc(pc105)"	};
};
```
@endfigure

A detailed explanation of how rules files convert [RMLVO] to [KcCGST] is out of
scope for this document. See [the rules file](@ref rule-file-format) page instead.


## Adding a layout

Adding a layout requires that the user adds [symbols] in the
correct location.

@sa @ref the-xkb_symbols-section "" for the full syntax
@sa @ref keycode-naming-convention "" (e.g. `<AE01>`)
@sa The *default mappings* of keycodes are:
- `<xkb-config-root>/symbols/pc` for the basic system keys
- `<xkb-config-root>/symbols/inet` (section `evdev`) for the special function keys
- `<xkb-config-root>/symbols/us` for the US Qwerty layout
@sa The list of [keysym] (key symbols) at `xkbcommon-keysyms.h` (remove the
`XKB_KEY_` prefix to get the name). The *dead keys* follow the pattern
`dead_<diacritic name>`.

[keysym]: @ref keysym-def

The default [rules files](@ref rule-file-format) (usually `evdev`) have a
catch-all to map a layout, say `foo`, and a variant, say `bar`, into the `bar`
section in the file `<xkb-config-root>/symbols/foo`.
This is sufficient to define a new keyboard layout. The example below defines
the keyboard layout `banana` with an optional variant `orange`:

@figure@figcaption
Content of `$XDG_CONFIG_HOME/xkb/symbols/banana`
@endfigcaption
```c
// Like a US layout but swap the top row so numbers are on Shift
default partial alphanumeric_keys
xkb_symbols "basic" {
    include "us(basic)"
    name[Group1]= "Banana (US)";

    key <AE01> { [ exclam,          1]     };
    key <AE02> { [ at,              2]     };
    key <AE03> { [ numbersign,      3]     };
    key <AE04> { [ dollar,          4]     };
    key <AE05> { [ percent,         5]     };
    key <AE06> { [ asciicircum,     6]     };
    key <AE07> { [ ampersand,       7]     };
    key <AE08> { [ asterisk,        8]     };
    key <AE09> { [ parenleft,       9]     };
    key <AE10> { [ parenright,      0]     };
    key <AE11> { [ underscore,      minus] };
    key <AE12> { [ plus,            equal] };
};

// Same as banana but map the euro sign to the 5 key
partial alphanumeric_keys
xkb_symbols "orange" {
    include "banana(basic)"
    name[Group1] = "Banana (Eurosign on 5)";
    include "eurosign(5)"
};
```
@endfigure

The `default` section is loaded when no variant is given. The first example
section uses ``include`` to populate with a symbols list defined elsewhere
(here: section `basic` from the file `symbols/us`, aka. the default US keyboard
layout) and overrides parts of these symbols. The effect of this section is to
swap the numbers and symbols in the top-most row (compared to the US layout) but
otherwise use the US layout.

The `orange` variant uses the `banana` symbols and includes a different section
to define the `eurosign`. It does not specifically override any symbols.

The exact details of how `xkb_symbols` section works is detailed in
“@ref keymap-text-format-v1-v2 ""”.

@remark This example uses a file name `banana` that should not clash with the
system files in `<xkb-config-root>/symbols`. Using the same file name than
the system files is possible but may require special handling,
see: @ref custom-config-system-file-names "".

## Adding an option

[Options][options] are sets of changes of any keymap components that
affect the whole keyboard.

[options]: @ref config-options-def

For technical reasons, options do **not** have a catch-all to map option names
to files and sections and must be specifically mapped by the user. This requires
a custom rules file. As the `evdev` ruleset is hardcoded in many clients, the
custom rules file must usually be named `evdev`.

@figure@figcaption
Content of `$XDG_CONFIG_HOME/xkb/rules/evdev`
@endfigcaption
```
// Mandatory: include the system ruleset to *extend* it
! include %S/evdev

! option     = symbols
  custom:foo = +custom(bar)
  custom:baz = +other(baz)
```
@endfigure

The `include` statement includes the system-provided `evdev` ruleset. This
allows users to only override those options they need afterwards.

This rules file maps the [RMLVO] option `custom:foo` to the `bar` section in the
`symbols/custom` file and the `custom:baz` option to the `baz` section in the
`symbols/other` file. Note how the [RMLVO] option name may be different to the
file or section name.

@important The *order* of the options matters in the rule file! This is due to
the *sequential* processing of the rules. In the example, `custom:foo` will
*always* be applied *before* `custom:baz` and both options will *always* be
applied *after* the system ones, even if the order is different in the [RMLVO]
configuration passed to libxkbcommon (e.g. with `xkbcli`). See the
[related section][options-order] in the rules documentation for further details.

[options-order]: @ref irrelevant-options-order

The files themselves are similar to the layout examples in the previous section:

@figure@figcaption
Content of `$XDG_CONFIG_HOME/xkb/symbols/custom`
@endfigcaption
```c
// map the Tilde key to nothing on the first shift level
partial alphanumeric_keys
xkb_symbols "bar" {
    key <TLDE> {        [      VoidSymbol ]       };
};
```
@endfigure


@figure@figcaption
Content of `$XDG_CONFIG_HOME/xkb/symbols/other`
@endfigcaption
```c
// map first key in bottom row (Z in the US layout) to k/K
partial alphanumeric_keys
xkb_symbols "baz" {
    key <AB01> {        [      k, K ]       };
};
```
@endfigure

With these in place, a user may select any layout/variant together with
the `custom:foo` and/or `custom:baz` options.

@remark This example uses file names `custom` and `other` that should not clash
with the system files in `<xkb-config-root>/symbols`. Using the same file
name than the system files is possible but may require special handling,
see: @ref custom-config-system-file-names "".

## Using system file names

The previous examples use custom keymap files with file name that do not clash
with the files in the *system* directory, `<xkb-config-root>`. It is possible to
add a custom variant/option using the *same* file name than the system file, e.g.
`$XDG_CONFIG_HOME/xkb/symbols/us` instead of `$XDG_CONFIG_HOME/xkb/symbols/banana`
for the example in @ref custom-layout "".

### Compatibility

@attention For **libxkbcommon \< 1.9**, the custom file must contain an
*explicit default* section if the system file has one, else it may break the
keyboard setup by including a section of the custom file instead of the system
one. The custom default section should enforce that the system default section
is included.
The following example defines a `broccoli` layout variant:
@figure@figcaption
Content of `$XDG_CONFIG_HOME/xkb/symbols/us`
@endfigcaption
```c
// Explicit default section with no name required
default partial alphanumeric_keys
xkb_symbols { include "us(basic)" };

partial alphanumeric_keys
xkb_symbols "broccoli" {
    include "us(basic)"
    name[Group1] = "Broccoli";
    key <AD05> { [ b, B, U1F966 ]}; // U1F966 = 🥦 (Unicode keysym)
    include "level3(ralt_switch)"
};
```
@endfigure

For **libxkbcommon ≥ 1.9** an explicit default section is not required
anymore: libxkbcommon will look up for the proper default section in the XKB
paths:
@figure@figcaption
Content of `$XDG_CONFIG_HOME/xkb/symbols/us`
@endfigcaption
```c
// No default section required

partial alphanumeric_keys
xkb_symbols "broccoli" {
    include "us(basic)"
    name[Group1] = "Broccoli";
    key <AD05> { [ b, B, U1F966 ]}; // U1F966 = 🥦 (Unicode keysym)
    include "level3(ralt_switch)"
};
```
@endfigure

### Overriding the system sections

One may override the system sections:
- Simply use the same section name.
- For the default section, additionally prepend the flag `default` before
  `xkb_symbols` in the custom file.

@warning It will affect *all* layouts/variants that depend on the system section.
@warning Including the *system* section can lead to a circular import.

Therefore is it **highly recommended to *not* override the system sections**
and prefer creating proper independent variants.

@since 1.11.0: It is possible to include the system section and avoid circular
include by prepending <code>\%S</code> to the included file.
See the @ref keymap-include-percent-expansion "corresponding documentation".

## Discoverable layouts

@warning The below requires `libxkbregistry` as XKB lookup tool and
**does not work where clients parse the XML file directly**.

The above sections apply only to the data files and require that the user knows
about the existence of the new entries. To make custom entries discoverable by
the configuration tools (e.g. the GNOME Control Center), the new entries must
also be added to the XML file that is parsed by `libxkbregistry`. In most cases,
this is the `evdev.xml` file in the rules directory.

The following tags are required:

- For *layouts*, this is the name of the corresponding *file*.
- For *variant*, this is the name of the corresponding *section* in the file.
- For *options*, this is the unique identifier used in the *rules* file
  (see @ref custom-option ""), usually following the pattern
  `<group>:<option_name>`.
For layout and variants, this is the [ISO 639] language code.
This is the text that will be displayed to label the entry. For layouts and
variants, this should be the same as `name[Group1]`.

See the [xkeyboard-config][xkeyboard-config-contrib] documentation for further
information.

[ISO 639]: https://en.wikipedia.org/wiki/ISO_639

The example below shows the XML file that would add the custom layout and custom
options as outlined above to the XKB registry:

@figure@figcaption
Content of `$XDG_CONFIG_HOME/xkb/rules/evdev.xml`
@endfigcaption
```xml
```
@endfigure

The default behavior of `libxkbregistry` ensures that the new layout and options
are added to the system-provided layouts and options.

For details on the XML format, see the DTD in `<xkb-config-root>/rules/xkb.dtd`
and the system-provided XML files `<xkb-config-root>/rules/*.xml`.

@note Depending on the desktop environment, it may require restarting the session
in order to make the configuration changes effective.

@note It is advised to try the custom configuration *before* restarting the
session using the various `xkbcli` tools. See “@ref testing-custom-config ""” for
further details.
