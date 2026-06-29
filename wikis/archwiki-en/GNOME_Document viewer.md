# GNOME/Document viewer

Document viewer is specifically designed to support the following file formats: PDF, PostScript, DjVu, tiff, dvi, XPS, SyncTex support with gedit, comics books (cbr,cbz,cb7 and cbt). For a comprehensive list of formats supported, see Supported Document Formats.

Document viewer uses the poppler library as a backend.

## Installation
Install the  package.

## Troubleshooting
## Zoom-in is limited
Increasing Evince's page cache size allows you to zoom in further, which is handy for large documents. By default the setting is set to 50MiB. Increasing the page cache size obviously increases Evince's memory consumption when zoomed-in.

The following command increases the page cache size to one gigabyte:

 $ gsettings set org.gnome.Evince page-cache-size 'uint32 1000'

## PDF text is not shown correctly
Try setting  parameter to false:

 $ gsettings set org.gnome.Evince override-restrictions false

## Inverse search with SyncTeX  does not work
Check that  is installed. After that  should work.

## WebP comic book support
Some comic books files (cbr, cbz etc.) use WebP images. Install  for WebP comic book support.

## Annotations
Certain annotations created with Adobe Acrobat Reader are not displayed correctly. For annotations of type "insert text at cursor position" and "notice to replace text" only the visual part is displayed, while the text content of the comment appears wrongly to be empty. There currently is no solution for this problem.

## Tips and tricks
## Annotation handling
Evince v3.31.0 adds keyboard hotkeys  for adding note text annotations and  for adding a highlight text annotation.

The default author for note text animations is equal to the GECOS comment for the current user, to change this:

 # usermod -c "Your full new Real Name" yourusername

## Use as default PDF viewer
To set the default association for xdg-open,

 $ xdg-mime default org.gnome.Evince.desktop application/pdf

Other resource openers can be configured similarly.
