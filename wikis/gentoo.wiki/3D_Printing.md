[] This article has been flagged for not conforming to the [wiki guidelines](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Guidelines "Gentoo Wiki:Guidelines"). Please [help Gentoo out](https://wiki.gentoo.org/wiki/Help_improve_Gentoo_by_getting_involved_with_documentation!#Make_articles_conform_to_the_guidelines "Help improve Gentoo by getting involved with documentation!") by starting fixing things.

**Resources**

[[]][Wikipedia](https://en.wikipedia.org/wiki/3D_Printing "wikipedia:3D Printing")

[[![Gentoo peach graphic](/images/thumb/a/ad/Gentoo-logo-peach.svg/25px-Gentoo-logo-peach.svg.png)](https://wiki.gentoo.org/wiki/Project:3dprint "Project:3dprint")][Project](https://wiki.gentoo.org/wiki/Project:3dprint "Project:3dprint")

[[]][Packages](https://packages.gentoo.org/maintainer/3dprint@gentoo.org)

This article is an overview of 3D printing with Gentoo.

## Contents

-   [[1] [Introduction]](#Introduction)
    -   [[1.1] [Modeling]](#Modeling)
    -   [[1.2] [Slicing]](#Slicing)
    -   [[1.3] [Printing]](#Printing)
        -   [[1.3.1] [Firmware and firmware development]](#Firmware_and_firmware_development)
-   [[2] [External resources]](#External_resources)
-   [[3] [References]](#References)

## [Introduction]

The process of 3D printing can be divided into three stages:

-   Modelling
-   Slicing
-   Printing

### [Modeling]

Printing starts with a 3D model (most commonly a .3mf or .stl file), which represents the shape and size of a three-dimensional object. While there are other ways to create 3D models (such as \"3D scanning\" of physical objects), they are usually designed using special 3D modelling software - that is, Computer-Aided Design (CAD) software.

Modeling software often creates more complex shapes from simpler ones. The simpler software is usually more limited in this regard and allows one to create shapes from dragging geometric primitives (cubes, cylinders, etc.) and then adding or subtracting further shapes from them like sculpting. More advanced software allows scripting aspects of this process.

Options packaged in Gentoo include:

  --------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------
  Name                                                                                                                              Package                                                                                                                                                                                                                                                                                                                                                                              Homepage                                                                               Description
  [Solvespace](https://wiki.gentoo.org/index.php?title=Solvespace&action=edit&redlink=1 "Solvespace (page does not exist)")   [[[media-gfx/solvespace]](https://packages.gentoo.org/packages/media-gfx/solvespace)[]]   [https://solvespace.com](https://solvespace.com)       Relatively small and simple 2D/3D CAD program based on geometric constraints.
  [FreeCAD](https://wiki.gentoo.org/index.php?title=FreeCAD&action=edit&redlink=1 "FreeCAD (page does not exist)")            [[[media-gfx/freecad]](https://packages.gentoo.org/packages/media-gfx/freecad)[]]            [https://www.freecad.org](https://www.freecad.org)     Large, complex CAD system meant to compete directly with commercial CAD packages.
  [OpenSCAD](https://wiki.gentoo.org/index.php?title=OpenSCAD&action=edit&redlink=1 "OpenSCAD (page does not exist)")         [[[media-gfx/openscad]](https://packages.gentoo.org/packages/media-gfx/openscad)[]]         [https://openscad.org](https://openscad.org)           Parametric, scriptable modeler based on a domain-specific language (with [C](https://wiki.gentoo.org/wiki/C "C")-style syntax) instead of a traditional GUI.
  [Blender](https://wiki.gentoo.org/wiki/Blender "Blender")                                                                         [[[media-gfx/blender]](https://packages.gentoo.org/packages/media-gfx/blender)[]]            [https://www.blender.org/](https://www.blender.org/)   Comprehensive suite for 3D art and animation. Not primarily intended for designing mechanical parts, unlike other options on this list.
  --------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------

There are also a few commercial Web-based CAD packages available gratis for personal use:

-   [Autodesk Tinkercad](https://www.tinkercad.com/3d-design) is a simple modeler designed for children to use.
-   [Onshape](https://onshape.com) is a \"cloud-based\" professional-level commercial CAD system.

### [Slicing]

3D printers generally do not work with 3D models directly. Instead, a separate software program called a \"slicer\" takes a 3D model and generates instructions the 3D printer can use to make it into a physical part - a form of Computer-Aided Manufacturing (CAM). This generally involves \"slicing\" the 3D model into layers, and then either tracing a precise path for the printer\'s extruder and generating [G-code](https://en.wikipedia.org/wiki/G-code) instructions to make the printer follow it (for [filament printers](https://en.wikipedia.org/wiki/Fused_filament_fabrication)), or converting the slices into photomask images (for common [masked-SLA](https://en.wikipedia.org/wiki/Stereolithography) resin printers). The final result is a file the printer can use to make the part.

Gentoo currently packages two closely related slicers:

  ------------------------------------------------------------------------------------------------------------------------------------ --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Name                                                                                                                                 Package                                                                                                                                                                                                                                                                                                                                                                                 Homepage                                                                                                                     Description
  [PrusaSlicer](https://wiki.gentoo.org/index.php?title=PrusaSlicer&action=edit&redlink=1 "PrusaSlicer (page does not exist)")   [[[media-gfx/prusaslicer]](https://packages.gentoo.org/packages/media-gfx/prusaslicer)[]]   [https://www.prusa3d.com/prusaslicer](https://www.prusa3d.com/prusaslicer)                   Primary slicer solution from Prusa Research, originally based on the venerable [Slic3r](https://slic3r.org). Supports a wide range of both filament and resin printers.
  [Superslicer](https://wiki.gentoo.org/index.php?title=Superslicer&action=edit&redlink=1 "Superslicer (page does not exist)")   [[[media-gfx/superslicer]](https://packages.gentoo.org/packages/media-gfx/superslicer)[]]   [https://github.com/supermerill/SuperSlicer/](https://github.com/supermerill/SuperSlicer/)   Community fork of PrusaSlicer with some added features and other changes.
  ------------------------------------------------------------------------------------------------------------------------------------ --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Ultimaker Cura](https://ultimaker.com/software/ultimaker-cura/) is another popular open-source option, not currently packaged for Gentoo.

### [Printing]

A slicer\'s output file can usually be processed directly by the printer by copying it via a USB drive or SD card, or perhaps over the network. [OctoPrint](https://wiki.gentoo.org/wiki/OctoPrint "OctoPrint") is a widely used program for controlling one or more 3D printers directly connected to a server. Previous work was begun to create an ebuild for it, but never completed.

#### [Firmware and firmware development]

[Marlin](https://marlinfw.org/) or [Klipper](https://www.klipper3d.org/Installation.html) are examples of printer firmware. The main difference between these two is that Marlin runs only on the microcontroller from the printer, whereas Klipper also requires a general-purpose computer.

To create a necessary toolchain for a Cortex microcontroller (used on most 32-bit Printer mainboards), see [How to build a toolchain for arm cortex-m and cortex-r](https://wiki.gentoo.org/wiki/How_to_build_a_toolchain_for_arm_cortex-m_and_cortex-r "How to build a toolchain for arm cortex-m and cortex-r").

## [External resources]

-   [Basics of 3D printing with Josef Prusa](https://www.prusa3d.com/page/basics-of-3d-printing-with-josef-prusa_490/)
-   An [extensive list of 3D printing and CAD programs](https://reprap.org/wiki/Useful_Software_Packages) is maintained by the [RepRap](https://reprap.org) project.
-   [The Best Free 3D Printing Software in 2023](https://all3dp.com/1/best-free-3d-printing-software-3d-printer-program/)
-   An [email discussion of 3D printing from 2013](https://archives.gentoo.org/gentoo-user/message/7f910aec0e3c286754290d043cfd0199) may be of interest.
-   [3d printing with Printrboj Jr](https://forums.gentoo.org/viewtopic-p-8449614.html)

## [References]