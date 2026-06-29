## B Historically Reserved Items

For historical reasons both KDE and GNOME are using (or have used) some desktop-specific extensions without the appropriate `X-KDE-` or `X-GNOME-` prefixes.

- KDE specific keys: `ServiceTypes`, `DocPath`, `InitialPreference`

- GNOME specific keys: `AutostartCondition`

- KDE specific types: `ServiceType`, `Service` and `FSDevice`

KDE also used the `Keywords` key before it was standardized, using commas instead of semi-colons as separators. At the time of standardization, the field had been prefixed with a `X-KDE` prefix, but the Trinity fork still used the non-prefixed variant.

KDE uses the following additional keys for desktop entries of the `FSDevice` type.

###### Table B.1: FSDevice Specific Keys

| Key | Description | Value Type |
|----|----|----|
| `Dev` | The device to mount. | string |
| `FSType` | The type of file system to try to mount. | string |
| `MountPoint` | The mount point of the device in question. | string |
| `ReadOnly` | Specifies whether or not the device is read only. | boolean |
| `UnmountIcon` | Icon to display when device is not mounted. Mounted devices display icon from the `Icon` key. | iconstring |
