[] This article is a **work in progress**; treat its contents with caution - [MGorny](https://wiki.gentoo.org/wiki/User:MGorny "User:MGorny") ([talk](https://wiki.gentoo.org/wiki/User_talk:MGorny "User talk:MGorny") \| [contribs](https://wiki.gentoo.org/wiki/Special:Contributions/MGorny "Special:Contributions/MGorny")).

This article describes the new profile layout idea by [Michał Górny](https://wiki.gentoo.org/wiki/User:MGorny "User:MGorny") ([talk](https://wiki.gentoo.org/wiki/User_talk:MGorny "User talk:MGorny")). It is based on [Funtoo 1.0 profiles](http://www.funtoo.org/Funtoo_1.0_Profile), however it tries to generalize the idea.

## Contents

-   [[1] [Basic assumptions]](#Basic_assumptions)
    -   [[1.1] [Hierarchical layers]](#Hierarchical_layers)
    -   [[1.2] [Mix-ins]](#Mix-ins)
-   [[2] [Necessary tool changes]](#Necessary_tool_changes)
    -   [[2.1] [Package Managers (core)]](#Package_Managers_.28core.29)
    -   [[2.2] [eselect profile]](#eselect_profile)
    -   [[2.3] [Repoman]](#Repoman)
-   [[3] [Implementation details]](#Implementation_details)
    -   [[3.1] [Directory structure]](#Directory_structure)
    -   [[3.2] [Profile metadata]](#Profile_metadata)
    -   [[3.3] [Gentoo profile structure]](#Gentoo_profile_structure)

## [Basic assumptions]

### [Hierarchical layers]

The profile layout is based on a number of *hierarchical layers* followed by a *mix-in layer*. Each of the hierarchical layers defines a number of *profile variants*. For example, the profile tree could define the following layers (with variants listed):

1.  system layer (linux, bsd, ...),
2.  arch layer (x86, ppc, ...).

All profile variants are exclusive. That is, the user must always choose exactly one variant in each hierarchical layer.

The layers are ordered, and the selected profiles are applied in the order of layers. The profiles in following layers may interact with the layers preceding them in two manners:

-   via excludes/conflicts: for example, the bsd system may exclude the ppc arch. In this case, the choice of bsd system makes it disallowed to select ppc, and possibly hides the choice.
-   via profile *subvariants*. Subvariants are subprofiles that are used instead of the main profile when a particular profile was selected in preceding layer. For example, if x86 defines a linux subvariant, it is used when linux system is combined with x86 arch.

** Note**\
It is important that subvariants are transparent to the user. In particular, the system tools (eselect profile update?) need to be able to transparently switch to another profile subvariant if the current subvariant is removed or a better-matching subvariant is introduced.

### [Mix-ins]

All of the hierarchical layers are followed by a *mix-in layer*. The mix-in layer represents a inclusive tree of profiles. The user may enable any number of mix-ins, as long as they do not collide with the selected hierarchical profiles or other mix-ins.

Each mix-in may have three specific properties:

1.  collisions with hierarchical profiles. In this case, a particular choice of hierarchical profile makes it impossible to enable a particular mix-in. The relevant mix-ins may be hidden from the user\'s choice.
2.  Collisions with other mix-ins. In this case, a choice of colliding mix-in makes it impossible to select the mix-in in question without deselecting the other. The UI may provide an ability to automatically deselect colliding mix-ins.
3.  Dependencies on other mix-ins (inheritance). In this case, a choice of mix-in implies loading all required (parent) mix-ins. The UI should highlight the mix-ins that are loaded automatically.

\

## [Necessary tool changes]

### [][Package Managers (core)]

The layout can successfully be implemented using current profile handling code in Package Managers. It is only necessary for an external tool (eselect profile) to maintain a custom make.profile directory, with parent file referencing all the enabled profiles.

### [eselect profile]

The eselect module for profile selection needs to be rewritten completely. In particular, the module needs to:

1.  support discovery of profile layers and variants,
2.  allow selecting hierarchical profile variants,
3.  allow enabling and disabling mix-ins,
4.  process profile collision specifications (and dependencies, as necessary),
5.  support discovery and choice of sub-variants.

### [Repoman]

Repoman needs to be updated to handle the new profile structure. In particular it needs to:

1.  support discovery of profiles layers and variants,
2.  support testing packages against combinations of profiles.

\

## [Implementation details]

### [Directory structure]

TODO: define directory layout for layers, profiles, sub-variants

### [Profile metadata]

TODO: define profile discovery or description file

The profile variant inheritance is established using parent files. The parent file specifies all profile directories the current profile inherits. Those directories may correspond to available profile variants or non-public profile directories (not listed in eselect profile list, used purely for inheritance).

In mix-in profiles, eselect profile can trace parent inheritance to highlight implicitly enabled profiles appropriately.

TODO: define profile collision format

### [Gentoo profile structure]

TODO!