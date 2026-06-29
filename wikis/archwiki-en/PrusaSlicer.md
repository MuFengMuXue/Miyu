# PrusaSlicer

From the PrusaSlicer documentation:

:PrusaSlicer (formerly known as Slic3r Prusa Edition or Slic3r PE) is our own in-house developed slicer software based on the open-source project [https://slic3r.org/ Slic3r. PrusaSlicer is an open-source, feature-rich, frequently updated tool that contains everything you need to export the perfect print files for (not only) your Original Prusa 3D printer.

## Variants
The software comes in two variants, one being the official Flatpak package from Prusa, the other one the Arch Linux package integrated with the Arch Linux package manager.

This compares the two, also pointing out their specifics, advantages and disadvantages:
{| class="wikitable"
! Arch Linux Package !! Flatpak Package
|-
| Fully integrated into the distributions, using other libraries from the system installation. || Self-contained package, including relevant dependencies directly shipped from the vendor.
|-
| Avoids duplication of libraries by sharing them with other applications installed in the system. || Comes with a proprietary copy of each library tested by the Prusa developers.
|-
| Advantage: Lower disk usage || Disadvantage: Higher disk usage
|-
| Advantage: More up-to-date libraries || Advantage: Library versions used tested with the tool inside Prusa
|-
| Security vulnerabilities for the libraries are handled by the Arch Linux Security team. || Security vulnerabilities need to be handled separately by Prusa.
|-
| Risk: Incompatibilities between the core product and the used libraries might occur that need separate fixing from the Arch Linux packagers. || Risk: Incompatibilities between the bundled libraries and the hosting systems might occur.
|-
| Before reporting software issues to Prusa they should be verified with their Flatpak package since Prusa tends to reject reports not verified with their own package. Problems specific to the Arch Linux package should be directly reported to the Arch Linux packagers. || Problems with that package can be directly reported to Prusa.
|}

As Arch Linux packagers we obviously recommend using the directly integrated Arch Linux package, in particular because we believe to have a stronger security vulnerability handling process. We understand though that we tend to be biased here and such provided full transparency for you to decide in the table above.

## Installation
## Arch Linux package
PrusaSlicer can be installed with the  package.

## Flatpak package
The Flatpak package requires Flatpak to be installed first:

 # pacman -S flatpak

After this step you can install the Prusa-provided Flatpak package using:

 $ flatpak install flathub com.prusa3d.PrusaSlicer

After that installation step you can invoke the tool either through your graphical user interface or by invoking the command:

 $ flatpak run com.prusa3d.PrusaSlicer

## Troubleshooting
## Arch Linux Package
If you encounter an issue with the Arch Linux package you should first determine whether this is a packaging issue specific to that package or an issue with the generic implementation. To do so you should also install the official Prusa Flatpak packages following the installation instructions above and verify whether this comes with the same issue. Should this be the case proceed with the instructions below to report an issue with the Flatpak package directly to Prusa. Should the problem only occur with the Arch Linux package but not with the Flatpak package then you should open a ticket in the Arch Linux bug reporting system.

## Flatpak Package
Should the issue also or only occur in the Flatpak Package you should report the issue directly to Prusa. It is useful to mention that you observed the issue with their official Flatpak package.
