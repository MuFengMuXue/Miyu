Pull request [8080](https://github.com/obsproject/obs-studio/pull/8080) introduced compatibility notices for Window and Game Capture directly in the UI:

![216831602-4e1844d6-057c-4b38-be35-b0e848f66d23](https://user-images.githubusercontent.com/3123295/222756141-d15c9b6e-f8f6-486a-a673-4903e0169ed0.png)

These messages are intended to reduce support requests by informing the user about possible compatibility issues - and their resolutions - directly in the UI.

This data can be updated independently of OBS Studio itself in response to new game releases or incompatibilities due to third-party application updates.

## Addings new entries

New entries are added via pull requests to the obs-studio repository. To create a new entry, the following steps must be taken:

0. Fork the OBS repo
1. Clone your fork and create a new branch, e.g. `compatibility-<app name>`
2. Add a new entry to `plugins/win-capture/data/compatibility.json`
    + The easiest way of doing this is by copying an existing entry and adjusting it
    + Entries are grouped by translation key and sorted by name within those groups, this is not enforced, but please try to keep things ordered!
3. (Optional) Add new translation key to `plugins/win-capture/data/locale/en-US.ini`
4. Increment the version number in `plugins/win-capture/data/package.json`
5. Add and commit your changes with a brief message explaining the change (e.g. `win-capture: Add compatibility entry for <Game>`)
6. Submit a pull request

Note that entries should only be added for reasonably popular applications that often come up in support channels such as the forums or Discord.

## JSON Format

The compatibility information is stored in a JSON file. While not necessarily intended to be a human-readable format, it is still fairly easy to add a new entry.

Each entry in the file consists of the following fields:

| **Field**                   | **Description**                                                |
|-----------------------------|----------------------------------------------------------------|
| `name`                      | Name of the affected application(s)                            |
| `translation_key`           | Translatable message to use                                    |
| `message`                   | Fallback in case translation key is unavailable (English only) |
| `url`                       | Optional URL providing additional information                  |
| `severity` (integer)        | Severity (0 = Notice, 1 = Warning, 2 = Error)                  |
| `match_flags` (integer)     | Matching type (see previous section)                           |
| `excutable`                 | Executable name including extension (case-insensitive)         |
| `window_class`              | Window class (case-sensitive)                                  |
| `window_title`              | Window title (case-sensitive)                                  |
| `game_capture` (bool)       | Whether or not this entry affects game capture                 |
| `window_capture` (bool)     | Whether or not this entry affects BitBlt Window Capture        |
| `window_capture_wgc` (bool) | Whether or not this entry affects WGC Window Capture           |

At least `name`, `message`, `match_flags`, and one of `executable`/`window_class`/`window_title` must be specified.

### Matching method

The matching done is decided via flags that are as follows:

| **Type**         | **Value** |
|------------------|-----------|
| Match executable | `1`       |
| Match title      | `2`       |
| Match class      | `4`       |

These behave as bitflags, and may be combined via `a | b`. For instance, if you wish to match both window name and executable specify it as `1 | 4 = 5`.

Note that class and title are matched case-sensitively, but executables are matched insensitively. Executable names must also contain the file extension.

Window titles support prefix matches, i.e. if the window title starts with the specified string it is considered a match. This is useful for applications that have additional information after the title, such as a version number, like "Minecraft 1.18".

### Severity

An entry's severity level is an integer with the following values:

| **Severity** | **Value** |
|--------------|-----------|
| Info         | 0         |
| Warning      | 1         |
| Error        | 2         |

Severity levels decide how the message is presented to the user. "Info" messages are displayed in plain text, while "Warning" and "Error" messages are highlighted in different colours (orange and red, respectively). 

They should be used as follows:
* `Error` should be used if an application cannot be captured using the affected source type(s)
* `Warning` should be used for correctable errors (e.g., change a game or source setting)
* `Info` should be used to provide tips in cases where there is no strict incompatibility.

### Translatable messages

Each entry shoud specify a `translation_key` that matches one of the `Compatibility.*` entries in `en-US.ini`. If none exists, a new one should be created when the compatibility list is updated. The `message` value is used as fallback until an OBS update containing the updated localisation data is shipped.

The translatable messages are split into two categories:
* Generic entries are for common issues (e.g. requiring running as admin, BitBlt capture not working) and can be reused as they support replacing a placeholder with the name specified in the compatibility entry.
* Application specific entries should only be added if fitting generic messages exist, and the issue is not something expected to affect other applications

## Translation Format

When adding new messages, they should follow the same pattern of `Compatibility.<Method>.<Issue>` for generic messages, and `Compatibility.Application.<App Name>` for application-specific messages.

Translation texts support the `%name%` placeholder, this is mostly used in generic messages like so:
```ini
Compatibility.GameCapture.Admin="%name% may require OBS to be run as admin to use Game Capture."
```

Specific messages should use the application name as the key and may not contain spaces. If the name consists of more than one word, then a commonly used abbreviation should be used instead, for instance, "Counter-Strike: Global Offensive" can be shortened to "CSGO":
```ini
Compatibility.Application.CSGO="CS:GO may require the <code>--allow_third_party_software</code> launch option to use Game Capture."
```
