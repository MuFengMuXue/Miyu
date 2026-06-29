# Zathura

zathura is a customizable document viewer with vi-like keybindings. It provides a minimalistic and space-saving interface. Users interact with zathura primarily with the keyboard. Different file formats are supported through plugins. Support is available for PDF, PS, DjVu and comic book files.

See  for more information.

## Installation
Install the  package along with the desired optional dependencies:

*  — Comic book support
*  — DjVu support
*  — EPUB, PDF and XPS support based on MuPDF
*  — PDF support based on Poppler
*  — PostScript support

## Configuration
See  for more information.

## Enable copy to clipboard
## Make zathura the default pdf viewer
Ensures, for example, that  will open pdf files with zathura.

First, ensure a desktop entry for zathura exists at  . If it does not, download the desktop entry from the zathura repo to .

Then, set zathura as default using
 $ xdg-mime default org.pwmt.zathura.desktop application/pdf

## Emacs keymap
zathura uses Vi-like keybindings by default.  Emacs-like keybindings can be configured separately.  An example can be found here.

## Usage
Commands may be entered directly into zathura by pressing , just like in vi.

zathura automatically reloads documents. When working in compiled documents such as those written in LaTeX, zathura will refresh the output whenever compilation takes place. zathura has the option of enabling inverse search (using SyncTeX).

zathura can adjust the document to page-fit () or to fit width (), and it can rotate pages (). It can view pages side-by-side () and has a fullscreen mode. Pages can also be recolored to have a black background and white foreground (). Most of vis movement/scrolling commands are supported.

Links can be followed by clicking them. Additionally, one can press  to highlight all links on the page and assign them a number, typing the number of the link and pressing enter will then jump to the link's location. If  is used, only the location of the link will be shown in the status bar.

zathura can search for text and copy text to the primary X selection. It supports bookmarks and can open password-encrypted files.

zathura has the ability to execute external shell commands. It can be opened in tabs using tabbed.

zathura provides an optional sandbox mode by using seccomp filter to provide a hardened runtime environment, see #Sandbox.

## Page number offset
Many editions of printed books only start counting page numbering at the beginning of the text. However, zathura counts all pages of the PDF, including pages some editions do not: the front cover, edition notice, the initial couple of blank pages, etc. For this reason, zathuras page numbering is sometimes misaligned with the edition, which makes it a hassle to follow page numbers used by the table of contents, or citations.

The command  will make zathura take into account an offset when jumping to a page number (by typing , the command  will not mind the offset For example, a given book begins counting its pages on the PDF's 17th page (so on page 17, the index is 1; on 18 it is 2, and so on). On setting ,  will jump to the 261st page of the PDF rather than the 245th.

## Sandbox
zathura comes with an additional zathura-sandbox binary that provides a secure runtime environment by using seccomp filter and landlock. This sandboxed version of zathura runs without network access, with read only filesystem permissions and a severely limited number of permitted system calls, reducing the kernel attack surface significantly.

Some features are disabled when using zathura-sandbox, such as writing files, printing and bookmarks.

## Read Microsoft Office/LibreOffice documents within zathura
The  script allows for opening Microsoft Office/LibreOffice documents with zathura.

To use it, run

 $ zaread /path/to/document.docx

## Troubleshooting
## Low font rendering quality
* Try to change the backend from  to .
* Try to use [https://github.com/mozilla/pdf.js PDF.js instead.

## High memory usage with Poppler
According to the issue, switching from  to  might solve the problem. However, if you are searching in a large document, a lot of memory will still be used.
