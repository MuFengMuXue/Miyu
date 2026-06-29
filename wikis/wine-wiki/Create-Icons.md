## Drawing New Icons

Wine cannot reuse Windows icons verbatim because of copyright issues so
we have to redraw them. They should have a similar design to keep from
confusing users, but they must be unique works. Ideally, they'll be
nicer than the Windows icons too. B-) These icons will appear in both
menus and file selection dialogs. In addition, some programs may need
special icons for the system tray, or internal icons for toolbars and
buttons.

**Note: Wine currently has a complete icon set that follows
[Tango](https://tango.freedesktop.org/) design guidelines for icons.**
For reference, some quick information about how the icon files are
formatted has been retained. However, more icons may be necessary in
the future as Windows changes or adds new core applications.

## Current Tango-Style Icons

### Creating an .svg Icon Set

All icon files for a given component of wine are stored in that
component's folder in the source tree. In order to allow for re-scaling
without distortion, most icons were first created as scalable vector
graphics, which also means an icon can be comfortably designed at a
larger size to start.

The first version should be created in Truecolor (24-bit [color
depth](https://en.wikipedia.org/wiki/Color_depth) with an 8-bit [alpha
channel](https://en.wikipedia.org/wiki/Alpha_channel)). Copies of the
icon can then be made at the 256 (8-bit) and 16 (4-bit) color-depths
respectively. It is important to check the simplified copies for
artifacts, making touch-ups in the smaller color palette if necessary.
Also, be sure not to replace the alpha channel with an inappropriate
background color by accident.

Although scaling is not an issue for the vector draft, Wine currently
mimics Windows by using raster icons. Because of this and the fact that
very small icons are often simplified for readability, the preceding
steps should be repeated for icons that are designed to be read at sizes
of 32x32 and 16x16 pixels. The first set of icons should be rescaled to
48x48 pixels, giving 9 different versions of the icon, one for each size
and color-depth.

Finally, to match the format currently used in the Wine source tree,
arrange these icons into a single row in a single .svg file, with the
48x48 versions on the left, then the 32x32 and 16x16 ones respectively.
The bottoms of the icons should be aligned, and within each set, the
icons should be ordered left-to-right, starting with the deepest colors.
After this, ensure the icons are evenly spaced, using an 8 pixel strip
between each copy and for the file's left and right border, then 16
pixel strips for the top and bottom borders.

### Converting to Windows .ico Format

The initial .svg source copy of an icon set can be converted with any
image editor (such as GIMP) that supports saving to Windows .ico format.
Simply export the .svg image as a raster image, then split each of the
nine copies of the icon into separate layers. Crop each layer to the
size of its icon, then stack the layers on top of each other, aligning
the top-left corners of each layer. Although the layer order may not be
strict, it is preferred to mirror the order of the .svg file, with the
largest, Truecolor icon on bottom and the smallest, 16 color icon on
top. Then simply save everything as one .ico file.

### Icons for Toolbars, Trays, & Buttons

Other types of icons used by Wine currently have a simpler structure.
For an initial draft, just design your icons in .svg, with Truecolor and
for viewing at 16x16 pixels. Arrange them in one file, using the
intended display order for toolbars, with no separation or borders. For
lone icons, such as those used for the system tray, they should be saved
in their own separate files, again only 16x16 pixels. Then export your
.svg files to Windows bitmap file.

## Newer Windows Themes

Starting with Vista, Windows switched over to the Aero user-interface
style, which prescribed much larger and more detailed icons in certain
cases. Beginning with Windows 8, the user-interface has undergone even
more radical changes with the new Metro guidelines. While adding such
icons and features are at most a low priority for now, if and when Wine
does adopt them, further work on program icons and graphics will be
needed.

## See Also

- [MSDN resource on designing Windows XP style
  icons](https://msdn.microsoft.com/en-us/library/ms997636)
- [MSDN resource on Aero icons for Windows
  Vista/7](https://msdn.microsoft.com/en-us/library/windows/desktop/aa511280.aspx)
- [MSDN index for Metro-style design
  features](https://msdn.microsoft.com/en-us/library/windows/apps/hh465424.aspx)
  (still in flux)
