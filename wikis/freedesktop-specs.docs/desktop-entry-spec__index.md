## Desktop Entry Specification

Authors:

Preston Brown `<pbrown@kde.org>`

Jonathan Blandford `<jrb@redhat.com>`

Owen Taylor `<otaylor@gtk.org>`

Vincent Untz `<vuntz@gnome.org>`

Waldo Bastian `<waldo.bastian@intel.com>`

Allison Lortie `<desrt@desrt.ca>`

David Faure `<faure@kde.org>`

Will Thompson `<wjt@endlessos.org>`

  

Publication Date: 2020-04-27, Version: Version 1.5

[1 Introduction](index.md#introduction)

[2 File naming](file-naming.md)

[3 Basic format of the file](basic-format.md)

[4 Possible value types](value-types.md)

[5 Localized values for keys](localized-keys.md)

[6 Recognized desktop entry keys](recognized-keys.md)

[7 The `Exec` key](exec-variables.md)

[8 D-Bus Activation](dbus.md)

[9 Interfaces](interfaces.md)

[10 Registering MIME Types](mime-types.md)

[11 Additional applications actions](extra-actions.md)

[12 Extending the format](extending.md)

[A Example Desktop Entry File](example.md)

[B Historically Reserved Items](historical-items.md)

[C Deprecated Items](deprecated-items.md)

[D The `Legacy-Mixed` Encoding (Deprecated)](legacy-mixed.md)

[E Changes to this Specification](ape.md)

[E.1 Changes from version 1.4 to 1.5](ape.md#id-1.18.2)

[E.2 Changes from version 1.3 to 1.4](apes02.md)

[E.3 Changes from version 1.2 to 1.3](apes03.md)

[E.4 Changes from version 1.1 to 1.2](apes04.md)

[E.5 Changes from version 1.0 to 1.1](apes05.md)

## 1 Introduction

Both the KDE and GNOME desktop environments have adopted a similar format for "desktop entries", or configuration files describing how a particular program is to be launched, how it appears in menus, etc. It is to the larger community's benefit that a unified standard be agreed upon by all parties such that interoperation between the two environments, and indeed any additional environments that implement the specification, becomes simpler.
