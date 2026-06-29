# MuPDF

MuPDF is a lightweight document viewer and toolkit written in portable C. It can render PDF, XPS, EPUB, XHTML, CBZ, and various image formats such as PNG, JPEG, GIF, and TIFF. Native Wayland support is not planned yet.

The renderer in MuPDF is tailored for high quality anti-aliased graphics. It renders text with metrics and spacing accurate to within fractions of a pixel for the highest fidelity in reproducing the look of a printed page on screen.

MuPDF supports all static functions required by PDF 1.7 and is a lightweight alternative to poppler based pdf applications. It also support standard PDF annotations such as highlight, shape tools, drawing, notes and file attachment.

## Installation
Install the  package or  for the OpenGL backend and  for the development version. For the document manipulation tools install the  package.

## Usage
See  or  and  for more information.

The application is started either from the command-line with  or from a file manager.

Navigation within a document works with standard keyboard shortcuts and mouse interaction. For example,  and  scroll up and down.

## MuPDF
Supported arguments are  for required passwords,  for the zoom level and  for the first selected page and more.

When zoomed in, the document can be moved by using the left mouse button. Pressing the right mouse button while moving the mouse will mark an area, and all text will be copied and can be inserted by clicking the middle mouse button.

## MuPDF GL
Press  to invert colours. See https://mupdf.readthedocs.io/en/latest/tools/mupdf-gl.html for the manual or press  for help.

## Set as default PDF viewer
 $ xdg-mime default mupdf.desktop application/pdf

For more information on setting default applications see XDG MIME Applications.

## Annotation Support
To access annotation menu, simply press , a sidebar for annotation will appear which support almost all standard PDF annotations tools (available at least in ) .
