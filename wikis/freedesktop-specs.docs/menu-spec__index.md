## Desktop Menu Specification

Authors:

Waldo Bastian `<waldo.bastian@intel.com>`

Francois Gouget `<fgouget@codeweavers.com>`

Alex Graveley `<alex@ximian.com>`

George Lebl `<jirka@5z.com>`

Havoc Pennington `<hp@pobox.com>`

Heinrich Wendel `<h_wendel@cojobo.net>`

  

Publication Date: 20 August 2016, Version: Version 1.1

[1 Introduction](index.md#introduction)

[2 File locations](paths.md)

[3 Extensions to the desktop entry format](desktop-entry-extensions.md)

[4 Format of menu files](menu-file-format.md)

[5 Merging](merge-algorithm.md)

[6 Generating the menus](query-algorithm.md)

[7 Legacy Menu Hierarchies](legacy-hierarchies.md)

[8 Example Menu File](example.md)

[A Registered Categories](category-registry.md)

[A.1 Main Categories](category-registry.md#main-category-registry)

[A.2 Additional Categories](additional-category-registry.md)

[A.3 Reserved Categories](reserved-category-registry.md)

[B Registered OnlyShowIn Environments](onlyshowin-registry.md)

[C Integrating your application in the menus](third-party-howto.md)

[C.1 Adding menu items](third-party-howto.md#adding-items)

[C.2 Install Locations](locations.md)

[C.3 Example](menu-add-example.md)

[C.4 Backward Compatibility](compatibility.md)

[D Implementation notes](implementation-notes.md)

[D.1 Menu editing](implementation-notes.md#menu-editing)

[Glossary](go01.md)

## 1 Introduction

This document defines how to construct a user-visible hierarchy of applications, typically displayed as a menu. It allows third-party software to add menu items that work for all desktops, and allows system administrators to edit menus in a way that affects all desktops.

The basic scheme is very simple. Information about each application (menu item) is stored in a desktop entry (see [Desktop Entry Standard (http://www.freedesktop.org/Standards/desktop-entry-spec)](http://www.freedesktop.org/Standards/desktop-entry-spec)). Then an XML configuration file defines the hierarchical arrangement (layout) of menu items, and which menu items are actually displayed.

Things are complicated somewhat by the need to support legacy desktop entry hierarchies, and the need to allow third parties to extend the menu layout. Both of these issues are addressed by the idea of *merging* two menu layouts.

In addition to a strict definition of the contents of each menu this specification also foresees in a number of layout / presentation hints. This part of the specification is optional, implementations may chose to ignore these hints.
