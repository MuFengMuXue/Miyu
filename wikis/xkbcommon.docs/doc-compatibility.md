# XKB Compatibility

@tableofcontents{html:2}

This page presents the differences between the [XKB 1.0 specification][XKB Protocol]
implemented in current X servers and its implementation in libxkbcommon.

xkbcommon has *removed* support for some parts of the specification which
introduced unnecessary complications.  Many of these removals were in fact
not implemented, or half-implemented at best, as well as being totally
unused in the standard keyboard layout database, [xkeyboard-config].

On the other hand, xkbcommon has notable additions that lift hard-coded
limitation of the [X11 Protocol].

@todo This page is work in progress. It aims to be exhaustive.
Please [report any issue](https://github.com/xkbcommon/libxkbcommon/issues).

[X11 Protocol]: https://www.x.org/releases/current/doc/xproto/x11protocol.html#Keyboards
[XKB Protocol]: https://www.x.org/releases/current/doc/kbproto/xkbproto.html
[xkeyboard-config]: https://gitlab.freedesktop.org/xkeyboard-config/xkeyboard-config

## Keymap support

### General features


Wayland support requires the XWayland compatibility layer.


libxkbcommon is the *reference* implementation of the keyboard keymap handling
(parsing/serializing, state) for Wayland.


Layout database path is *hard-coded* in xserver.

`xkbcomp` enables path configuration, but `setxkbmap` support is incomplete.


Multiple layout database paths can be used simultaneously, enabling user-space
configuration.

See @ref custom-option "" for further information.


Layout database path is *hard-coded* in xserver.

`xkbcomp` enables path configuration, but `setxkbmap` support is incomplete.


Multiple layout database paths can be used simultaneously, enabling third-party
packages to extend the base configuration without hacking its files.

See @ref packaging-keyboard-layouts "" for further information.


Keycodes have always priority over aliases.


Keycodes and aliases share the same namespace.


Limited to **8**-bit keycodes.


Support all Linux keycodes using **32**-bit keycodes.


Limited to **4**-character names.


- *Parse* keys and aliases names of any length.
- *Serialize* names > 4 characters by renaming them (since 1.14)


Support any key and aliases names of any length.


Limited to **4** layouts.


Limited to **4** layouts.


Enable up to **32** layouts when using `::XKB_KEYMAP_FORMAT_TEXT_V2`.


Clear separation between *real* (i.e. core) and *virtual* modifiers.


Real and virtual modifiers have been collapsed into the same namespace, with a
“significant” flag that largely parallels the core/virtual split.

Real modifiers are predefined modifiers with fixed encoding and considered merely
as an X11 compatibility feature.


Limited to up to **8** *independent* modifiers.


Enable up to **32** *independent* modifiers.


Virtual modifiers can only mapped to *real* modifiers (8 bits).


Only if using explicit mapping: e.g. `virtual_modifiers M = 0x100;` if `M` has
the modifier index 8.


Virtual modifiers that are not mapped either *explicitly* (using e.g.
`virtual_modifiers M = …`) or *implicitly* (using `modifier_map` and
`virtualModifier`) [automatically](@ref auto-modifier-encoding) use to
their [canonical mapping](@ref canonical-modifier-def).


Contiguous identical groups are merged together.


Since version 1.8 the [RMLVO] API does not support parsing multiple groups per
key anymore, because it may break the expectation of most desktop environments and
tools that the number of groups should be equal to the number of configured
layouts.

See @ref how-do-i-define-multiple-groups-per-key "" for migration instructions.


Ignored: fallback to `NoSymbol`.


@todo rationale


- xkbcomp \< 1.5: Parse error
- xkbcomp ≥ 1.5: Parsing only


Currently limited to 1 action for each action type “group” and “modifier”.

@since 1.8: Enable multiple actions per level (parsing, serializing & handling).
@since 1.11: Serialize to `VoidAction()` for compatibility with X11.


Currently limited to 1 action for each action type “group” and “modifier”.

@since 1.11


Only *overlay* controls [`1`][Overlay1] and [`2`][Overlay2] are supported,
consistent with the [keyboard overlay](@ref key-behavior-overlay) support.


Only *overlay* controls [`1`][Overlay1] and [`2`][Overlay2] are supported,
consistent with the [keyboard overlay](@ref key-behavior-overlay) support.


See the supported keyboard controls in `xkb_keyboard_control_flags`, as well as
the [corresponding actions](@ref compatibility-key-actions).

*Overlay* controls [`1`][Overlay1] to [`8`][Overlay8] are supported.


- Only **2** overlays
- [Disjoint overlays][Overlapping overlays]

- libxkbcommon \< 1.14: Parsing overlays 1-2 only.
- libxkbcommon ≥ 1.14: Supported. Note that the API support requires using
  the `xkb_machine` API.
  - Only **2** overlays
  - [Disjoint overlays][Overlapping overlays]


- libxkbcommon \< 1.14: Parsing overlays 1-2 only.
- libxkbcommon ≥ 1.14: Full support. Note that the API support requires using
  the `xkb_machine` API.
  - **8** overlays
  - [Overlapping overlays]


Unused in [xkeyboard-config] layouts.


Unused in [xkeyboard-config] layouts.


E.g. LED-controls-key behavior (X11’s `IM_LEDDrivesKB` flag enabled) is not
supported.

The only supported LED behavior is *key-controls-LED*.

Unused in [xkeyboard-config] layouts.


Rational:
- There were very few geometry definitions available in [xkeyboard-config], and
  while xkbcommon was responsible for parsing this insanely complex format,
  it never actually did anything with it.
- Hopefully someone will develop a companion library which supports keyboard
  geometries in a more useful format, e.g. SVG.


[Indicator behaviors]: https://www.x.org/releases/current/doc/kbproto/xkbproto.html#:~:text=IM_LEDDrivesKB
[Overlay1]: @ref XKB_KEYBOARD_CONTROL_OVERLAY1
[Overlay2]: @ref XKB_KEYBOARD_CONTROL_OVERLAY2
[Overlay8]: @ref XKB_KEYBOARD_CONTROL_OVERLAY8
[Overlapping overlays]: @ref overlapping-overlays


### Key actions


- `unlockOnPress` parameter is not supported.


- `unlockOnPress` parameter is not supported. Use `::XKB_KEYMAP_FORMAT_TEXT_V2`.


- `unlockOnPress` parameter (since 1.11). See @ref set-mods-action "its documentation"
  for further details.


- `latchOnPress` parameter is not supported.
- `unLockOnPress` parameter is not supported.


- `latchOnPress` parameter is not supported. Use `::XKB_KEYMAP_FORMAT_TEXT_V2`.
- `unLockOnPress` parameter is not supported. Use `::XKB_KEYMAP_FORMAT_TEXT_V2`.


- `latchOnPress` parameter (since 1.11). See @ref latch-mods-action "its documentation"
  for further details.
- `unLockOnPress` parameter (since 1.11). See @ref latch-mods-action "its documentation"
  for further details.


- `unlockOnPress` parameter is not supported.


- `unlockOnPress` parameter is not supported. Use `::XKB_KEYMAP_FORMAT_TEXT_V2`.


- `unlockOnPress` parameter (since 1.11). See @ref lock-mods-action "its documentation"
  for further details.


- `lockOnRelease` parameter is not supported. Use `::XKB_KEYMAP_FORMAT_TEXT_V2`.


- `lockOnRelease` parameter is not supported. Use `::XKB_KEYMAP_FORMAT_TEXT_V2`.


- `lockOnRelease` (since 1.11). See @ref lock-group-action "its documentation"
  for further details.


- libxkbcommon \< 1.14: Parsing and serializing only, no API support
- libxkbcommon ≥ 1.14: API support for a limited number of controls:
  see `xkb_keyboard_control_flags`.


- libxkbcommon \< 1.14: Parsing and serializing only, no API support
- libxkbcommon ≥ 1.14: API support for a limited number of controls:
  see `xkb_keyboard_control_flags`.


Note that the <code>[auto](@ref redirect-key-auto)</code> value for the `keycode`
parameter is not supported: the default value is 0, an invalid X11 keycode.


- libxkbcommon \< 1.14: Parsing only.
- libxkbcommon ≥ 1.14: Full support. Note that the API support requires using
  the `xkb_machine` API.


### Keymap text format


Keymap components are no longer mandatory, e.g. a keymap without a
`xkb_types` section is legal.


Floating-point numbers cannot be used where an integer is expected.


Supported using the prefix `^`, in addition to the standard *merge* `|` and
*override* `+` modes.


Keysyms can be written as their corresponding string, e.g. `udiaeresis` can be
written `"ü"`. A string with multiple Unicode code points denotes a list of the
corresponding keysyms. An empty string denotes the keysym `NoSymbol`.


`\u{NNNN}`.

See @ref keymap-string-literal "string literal" for further information.


Enable to define e.g. a proper interpretation entry of the keysym `ISO_Last_Group`:

```c
interpret ISO_Last_Group {
    action= LockGroup(group=last);
};
```

Note that contrary to `First`, `Last` cannot be used as an *array* index, i.e.
`symbols[Last]` will be discarded or raise an error, depending of the API used.

These constants are parsed but never used for *serialization*, in order to
maintain compatibility with xkbcomp and older libxkbcommon versions.


Only `Group1`..`Group8` are supported, although the resulting group must be in
the range 1..4.


Only `Group1`..`Group4` are supported.

Use `::XKB_KEYMAP_FORMAT_TEXT_V2` in order to support further groups.


The pattern `Group<INDEX>` can be used for any valid group index `<INDEX>`.


Only `Level1`..`Level8` are supported.


Since 1.11, the pattern `Level<INDEX>` can be used for any valid level index
`<INDEX>`.

Before 1.11, only `Level1`..`Level8` were supported.


Enable *absolute* paths and *`%`-expansion*.

See @ref keymap-include-percent-expansion "" for further details.


The modern approach is to use [RMLVO].


@todo syntax description


`alternate` was used in `xkb_keycodes` type sections and meant that if a new
keycode name conflicts with an old one, consider it as a keycode *alias*.


Since 1.8, only 1 group per symbol section is supported in the [RMLVO] API, to
avoid unintuitive results.

Multiple groups per symbol section is supported when parsing a [KcCGST] keymap.


### API


Full support of simple case mappings for `xkb_keysym_to_lower()` and
`xkb_keysym_to_upper()`.


- [KcCGST] is considered an implementation detail, use [RMLVO] instead.
- Use `xkb_component_names::xkb_components_names_from_rules()` for
  debugging purposes.


Obsolete legacy file format tied to X11 ecosystem.


[KcCGST]: @ref KcCGST-intro
[RMLVO]: @ref RMLVO-intro


## Rules support


See @ref rmlvo-resolution "" for further details.


See @ref rules-include-expansion "rules include statement" for further details.


Support the merge mode *replace* via the prefix `^`, in addition to
the standard *merge* `|` and *override* `+` modes.


- *single*: matches a single layout; `layout[single]` is the same as without
explicit index: `layout`.
- *first*: matches the first layout/variant, no matter how many layouts are in
the RMLVO configuration. Acts as both `layout` and `layout[1]`.
- *later*: matches all but the first layout. This is an index range. Acts as
`layout[2]` .. `layout[MAX_LAYOUT]`, where `MAX_LAYOUT` is currently 4.
- *any*: matches layout at any position. This is an index range.

- the `:all` qualifier: it applies the qualified item to all layouts.

See @ref rules-extended-layout-indices "extended layout indices" for further
details.


the `:all` qualifier: it applies the qualified item to all layouts.

See @ref rules-all-qualifier ":all qualifier" for further
details.


- `<none>` matches *empty* value;
- `<some>` matches *non-empty* value in *every* context.
- `<any>` matches *optionally empty* value in *every* context, contrary to the
  legacy `*` wild card which does not match empty values for layout and variant.

See @ref rules-wildcard-def "rules wildcards" for further information.


## Keyboard layout registry


@todo rationale


## Compose support

Relative to the standard implementation in libX11 (described in the
Compose(5) man-page):


Syntax: `[([!] ([~] MODIFIER)...) | None] <keysym>`

If the modifier list is preceded by `!` it must match exactly. MODIFIER may be
one of `Ctrl`, `Lock`, `Caps`, `Shift`, `Alt` or `Meta`. Each modifier may be
preceded by a `~` character to indicate that the modifier must not be present.
If `None` is specified, no modifier may be present.

@todo removal rationale


Modifiers should not be used in Compose sequences. Use keymap’s features or
a keysym with more appropriate semantics.


@todo feature description, removal rationale
