## 11 Additional applications actions

Desktop entries of type Application can include one or more actions. An action represents an additional way to invoke the application. Application launchers should expose them to the user (for example, as a submenu) within the context of the application. This is used to build so called "Quicklists" or "Jumplists".

### 11.1 Action identifier

Each action is identified by a string, following the same format as key names (see [Section 3.3, “Entries”](basic-format.md#entries "3.3. Entries")). Each identifier is associated with an action group that must be present in the `.desktop` file. The action group is a group named `Desktop Action %s`, where `%s` is the action identifier.

It is not valid to have an action group for an action identifier not mentioned in the `Actions` key. Such an action group must be ignored by implementors.

### 11.2 Action keys

The following keys are supported within each action group. If a REQUIRED key is not present in an action group, then the implementor should ignore this action.

###### Table 3: Action Specific Keys

| Key | Description | Value Type | REQ? |   |
|----|----|----|----|----|
| `Name` | Label that will be shown to the user. Since actions are always shown in the context of a specific application (that is, as a submenu of a launcher), this only needs to be unambiguous within one application and should not include the application name. | localestring | YES |   |
| `Icon` | Icon to be shown together with the action. If the name is an absolute path, the given file will be used. If the name is not an absolute path, the algorithm described in the [Icon Theme Specification (http://freedesktop.org/wiki/Standards/icon-theme-spec)](http://freedesktop.org/wiki/Standards/icon-theme-spec) will be used to locate the icon. Implementations may choose to ignore it. | iconstring | NO |   |
| `Exec` | Program to execute for this action, possibly with arguments. See the [`Exec` key](exec-variables.html "7. The Exec key") for details on how this key works. The `Exec` key is required if `DBusActivatable` is not set to `true` in the main desktop entry group. Even if `DBusActivatable` is `true`, `Exec` should be specified for compatibility with implementations that do not understand `DBusActivatable`. | string | NO |   |

### 11.3 Implementation notes

Application actions should be supported by implementors. However, in case they are not supported, implementors can simply ignore the `Actions` key and the associated `Desktop Action` action groups, and keep using the `Desktop Entry` group: the primary way to describe and invoke the application is through the Name, Icon and Exec keys from the `Desktop Entry` group.

It is not expected that other desktop components showing application lists (software installers, for instance) will provide any user interface for these actions. Therefore applications must only include actions that make sense as general launchers.
