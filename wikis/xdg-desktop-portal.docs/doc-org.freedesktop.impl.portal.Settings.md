# Settings

## Description

Settings portal backend interface

This interface provides read-only access to a small number of host settings required for toolkits similar to XSettings. It is not for general purpose settings.

Currently the interface provides the following keys:

- `org.freedesktop.appearance` `color-scheme` (`u`)

  Indicates the system’s preferred color scheme. Supported values are:

  - `0`: No preference

  - `1`: Prefer dark appearance

  - `2`: Prefer light appearance

  Unknown values should be treated as 0 (no preference).

- `org.freedesktop.appearance` `accent-color` (`(ddd)`)

  Indicates the system’s preferred accent color as a tuple of RGB values in the sRGB color space, in the range \[0,1\]. Out-of-range RGB values should be treated as an unset accent color.

- `org.freedesktop.appearance` `contrast` (`u`)

  Indicates the system’s preferred contrast level. Supported values are:

  - `0`: No preference (normal contrast)

  - `1`: Higher contrast

  Unknown values should be treated as 0 (no preference).

- `org.freedesktop.appearance` `reduced-motion` (`u`)

  Indicates the system’s preferred reduced motion setting. Supported values are:

  - `0`: No preference

  - `1`: Reduced motion

  Unknown values should be treated as 0 (no preference).

Implementations can provide other keys; they are entirely implementation details that are undocumented. If you are a toolkit and want to use this please open an issue.

Note that the Settings portal can operate without this backend, implementing it is optional.

## Properties

### org.freedesktop.impl.portal.Settings:version

    version readable u

## Methods

### org.freedesktop.impl.portal.Settings.ReadAll

    ReadAll (
      IN namespaces as,
      OUT value a{sa{sv}}
    )

If `namespaces` is an empty array or contains an empty string it matches all. Globbing is supported but only for trailing sections, e.g. “org.example.\*”.

namespaces  
List of namespaces to filter results by, supports simple globbing explained below.

value  
Dictionary of namespaces to its keys and values.

### org.freedesktop.impl.portal.Settings.Read

    Read (
      IN namespace s,
      IN key s,
      OUT value v
    )

Reads a single value. Returns an error on any unknown namespace or key.

namespace  
Namespace to look up `key` in.

key  
The key to get.

value  
The value `key` is set to.

## Signals

### org.freedesktop.impl.portal.Settings::SettingChanged

    SettingChanged (
      namespace s,
      key s,
      value v
    )

Emitted when a setting changes.

namespace  
Namespace of changed setting.

key  
The key of changed setting.

value  
The new value.
