# SpeedyNote

SpeedyNote is a cross-platform note-taking application for stylus input, written in C++ with Qt 6. It supports pressure-sensitive inking, multi-layer editing, PDF annotation and an edgeless infinite canvas mode. The application is released under the GNU General Public License v3.

## Installation
Install the  package.

Alternatively, SpeedyNote is available as a Flatpak from Flathub:

## File formats
SpeedyNote uses two native file formats:

;  : Bundle directory containing tiled page data. Used for both paged notebooks and edgeless canvas documents.
;  : Compressed archive of an  bundle, intended for sharing and backup.

The legacy  format from the 0.x series is no longer supported.

## Command-line interface
The  executable provides subcommands for batch operations on notebooks. Run  for the full reference.

## Export to PDF
The  argument accepts either a single  bundle or a directory; in the latter case  must also be a directory. Common options include  to set the export resolution,  to select a page range and  to omit the PDF background.

## Export to SNBX
The  option excludes the embedded source PDF, producing smaller archives.

## Import SNBX
The  option registers imported notebooks in the launcher timeline. Without it, the files are placed in  but not surfaced in the UI.

All subcommands accept  to preview the operation,  to descend into subdirectories, and  for machine-readable output suitable for scripting.
