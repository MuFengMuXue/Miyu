# Print

## Description

Portal for printing

The Print portal allows sandboxed applications to print.

Due to the way in which printing requires bi-directional communication, using this portal will often require applications to make multiple requests. First, use [org.freedesktop.portal.Print.PreparePrint](#org-freedesktop-portal-print-prepareprint) to obtain print settings, use them to format your output, then use [org.freedesktop.portal.Print.Print](#org-freedesktop-portal-print-print) to print the formatted document. It is expected that high-level toolkit APIs such as GtkPrintOperation will hide most of this complexity.

This documentation describes version 4 of this interface.

## Properties

### org.freedesktop.portal.Print:version

    version readable u

## Methods

### org.freedesktop.portal.Print.PreparePrint

    PreparePrint (
      IN parent_window s,
      IN title s,
      IN settings a{sv},
      IN page_setup a{sv},
      IN options a{sv},
      OUT handle o
    )

Presents a print dialog to the user and returns print settings and page setup.

Supported keys in the `options` vardict:

- `handle_token` (`s`)

  A string that will be used as the last element of the `handle`. Must be a valid object path element. See the [Request](doc-org.freedesktop.portal.Request.md#org-freedesktop-portal-request) documentation for more information about the `handle`.

- `modal` (`b`)

  Whether to make the dialog modal. Defaults to yes.

- `accept_label` (`s`)

  Label for the accept button. Mnemonic underlines are allowed.

  This option was added in version 2.

- `supported_output_file_formats` (`as`)

  File formats supported by the app to use for print-to-file. If not set, all formats are assumed to be supported. The following values are allowed: “pdf”, “ps”, and “svg”.

  This option was added in version 3.

- `has_current_page` (`b`)

  Whether it makes sense to return “current” for the `print-pages` setting.

  This option was added in version 4.

- `has_selected_pages` (`b`)

  Whether it makes sense to return “selection” for the `print-pages` setting.

  This option was added in version 4.

The `settings` and `page_setup` vardict contain hints for the initial state of the print dialog.

The following keys are supported in the `settings` vardict:

- `orientation` (`s`)

  One of `landscape`, `portrait`, `reverse_landscape` or `reverse_portrait`.

- `paper-format` (`s`)

  A paper name according to [PWG 5101.1-2002](ftp://ftp.pwg.org/pub/pwg/candidates/cs-pwgmsn10-20020226-5101.1.pdf).

- `paper-width` (`s`)

  Paper width, in millimeters.

- `paper-height` (`s`)

  Paper height, in millimeters.

- `n-copies` (`s`)

  The number of copies to print.

- `default-source` (`s`)

  The default paper source.

- `quality` (`s`)

  Print quality, one of normal, high, low or draft.

- `resolution` (`s`)

  The resolution, sets both resolution-x and resolution-y.

- `use-color` (`s`)

  Whether to use color, one of true or false.

- `duplex` (`s`)

  Duplex printing mode, one of simplex, horizontal or vertical.

- `collate` (`s`)

  Whether to collate copies, one of true or false.

- `reverse` (`s`)

  Whether to reverse the order of printed pages, one of true or false.

- `media-type` (`s`)

  A media type according to [PWG 5101.1-2002](ftp://ftp.pwg.org/pub/pwg/candidates/cs-pwgmsn10-20020226-5101.1.pdf).

- `dither` (`s`)

  The dithering to use, one of `fine`, `none`, `coarse`, `lineart`, `grayscale` or `error-diffusion`.

- `scale` (`s`)

  The scale in percent.

- `print-pages` (`s`)

  What pages to print, one of all, selection, current or ranges.

- `page-ranges` (`s`)

  A list of page ranges, formatted like this: 0-2,4,9-11.

  Note

  Page ranges are 0-based, even if the are displayed as 1-based when presented to the user.

- `page-set` (`s`)

  What pages to print, one of all, even or odd.

- `finishings` (`s`)

  Finishings.

- `number-up` (`s`)

  The number of pages per sheet.

- `number-up-layout` (`s`)

  One of `lrtb`, `lrbt`, `rltb`, `rlbt`, `tblr`, `tbrl`, `btlr`, `btrl`.

- `output-bin` (`s`)

- `resolution-x` (`s`)

  The horizontal resolution in dpi.

- `resolution-y` (`s`)

  The vertical resolution in dpi.

- `printer-lpi` (`s`)

  The resolution in lpi (lines per inch).

- `output-basename` (`s`)

  Basename to use for print-to-file.

- `output-file-format` (`s`)

  Format to use for print-to-file, one of PDF, PS, SVG.

- `output-uri` (`s`)

  The uri used for print-to-file.

The following keys are supported in the `page_setup` vardict:

- `PPDName` (`s`)

  The PPD name.

- `Name` (`s`)

  The name of the page setup.

- `DisplayName` (`s`)

  User-visible name for the page setup.

- `Width` (`d`)

  Paper width in millimeters.

- `Height` (`d`)

  Paper height in millimeters.

- `MarginTop` (`d`)

  Top margin in millimeters.

- `MarginBottom` (`d`)

  Bottom margin in millimeters.

- `MarginLeft` (`d`)

  Left margin in millimeters.

- `MarginRight` (`d`)

  Right margin in millimeters.

- `Orientation` (`s`)

  Orientation, one of portrait, landscape, reverse-portrait or reverse-landscape.

The following results get returned via the [org.freedesktop.portal.Request::Response](doc-org.freedesktop.portal.Request.md#org-freedesktop-portal-request-response) signal:

- `settings` (`a{sv}`)

  Print settings as set up by the user in the print dialog. The same keys as in `settings` are supported (see above).

- `page-setup` (`a{sv}`)

  Page setup as set up by the user in the print dialog. The same keys as in `page_setup` are supported (see above).

- `token` (`u`)

  Token that can be passed to a subsequent [org.freedesktop.portal.Print.Print](#org-freedesktop-portal-print-print) call to bypass the print dialog.

parent_window  
Identifier for the application window, see [Window Identifiers](window-identifiers.md)

title  
Title for the print dialog

settings  
Serialized print settings

page_setup  
Serialized page setup

options  
Vardict with optional further information

handle  
Object path for the [Request](doc-org.freedesktop.portal.Request.md#org-freedesktop-portal-request) object representing this call

### org.freedesktop.portal.Print.Print

    Print (
      IN parent_window s,
      IN title s,
      IN fd h,
      IN options a{sv},
      OUT handle o
    )

Asks to print a file.

The file must be passed in the form of a file descriptor open for reading. This ensures that sandboxed applications only print files that they have access to.

If a valid token is present in the `options`, then this call will print with the settings from the Print call that the token refers to. If no token is present, then a print dialog will be presented to the user.

Note that it is up to the portal implementation to determine how long it considers tokens valid.

Supported keys in the `options` vardict:

- `handle_token` (`s`)

  A string that will be used as the last element of the `handle`. Must be a valid object path element. See the [Request](doc-org.freedesktop.portal.Request.md#org-freedesktop-portal-request) documentation for more information about the `handle`.

- `modal` (`b`)

  Whether to make the dialog modal. Defaults to yes.

- `token` (`u`)

  Token that was returned by a previous [org.freedesktop.portal.Print.PreparePrint](#org-freedesktop-portal-print-prepareprint) call.

- `supported_output_file_formats` (`as`)

  File formats supported by the app to use for print-to-file. If not set, all formats are assumed to be supported. The following values are allowed: “pdf”, “ps”, and “svg”.

  This option was added in version 3.

parent_window  
Identifier for the application window, see [Window Identifiers](window-identifiers.md)

title  
Title for the print dialog

fd  
File descriptor for reading the content to print

options  
Vardict with optional further information

handle  
Object path for the [Request](doc-org.freedesktop.portal.Request.md#org-freedesktop-portal-request) object representing this call
