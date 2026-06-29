\

  ------------------------------ ------------------------------------
   GLEP 1005: Tags for packages
               Type                        Standards Track
              Status                            Draft
              Author              Alec Warner \<antarus@gentoo.org\>
              Editor
             Replaces
           Replaced by                          (none)
             Requires
           Post History
  ------------------------------ ------------------------------------

## Contents

-   [[1] [Abstract]](#Abstract)
-   [[2] [Motivation]](#Motivation)
-   [[3] [NonGoals]](#NonGoals)
-   [[4] [Design]](#Design)
    -   [[4.1] [Metadata.dtd]](#Metadata.dtd)
-   [[5] [Tool Support]](#Tool_Support)
-   [[6] [Copyright]](#Copyright)

## [Abstract]

This GLEP offers a modest proposal to annotate packages with tags.

## [Motivation]

Provide an additional place for package maintainers to provided descriptive metadata so that users can easily locate packages.

## [NonGoals]

This GLEP author would love to blight categories out of gentoo history as a giant mistake. However it turns out that package name sharding is nominally required at some level to continue support of unambiguous package names (for example: app-emulation/fuse and sys-fs/fuse would collide if categories did not exist.) Since that is a lot of work for very little gain, I have opted to simply add tags and keep categories as is.

## [Design]

The main question is whether to store tags in the ebuilds themselves, or in the metadata.xml for packages. This GLEP provides for storing tags in metadata.xml. The rationale for this decision is somewhat simple. Tags are likely more common for packages, then for specific versions of packages. In addition, there is already per-version support for tags in metadata.xml for USE flags, and we can adopt those restrictions for tags as well if required. Ebuild files themselves should primary deal with building packages, as opposed to holding metadata that is unrelated to building or installing packages. Finally, having the tags in ebuilds would duplicate data across many ebuild files, which seems a bad practice to encourage when we can store the vast majority of tags once in metadata.xml

### [Metadata.dtd]

Update the pkgmetadata ELEMENT to hold tags:

     <!ELEMENT pkgmetadata ( (herd|maintainer|natural-name|longdescription|use|upstream|tag)* )>
     <!ATTLIST pkgmetadata pkgname CDATA "">

Update the pkgmetadata ATTLIST to also hold tags:

     <!ATTLIST tag restrict CDATA #IMPLIED >

## [Tool Support]

Once the metadata.dtd is updated, developers can begin adding tags to ebuilds and tool support should shortly follow.

## [Copyright]

This work is licensed under the Creative Commons Attribution-ShareAlike 3.0 Unported License. To view a copy of this license, visit [http://creativecommons.org/licenses/by-sa/3.0/](https://creativecommons.org/licenses/by-sa/3.0/).