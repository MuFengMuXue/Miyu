**Resources**

[[]][Home](https://pdfbox.apache.org/)

[[]][GitHub](https://github.com/apache/pdfbox)

[[]][dev-java/pdfbox](https://packages.gentoo.org/packages/dev-java/pdfbox)

[[]][Bugs](https://bugs.gentoo.org/buglist.cgi?quicksearch=dev-java%2fpdfbox)

The Apache PDFBox™ library is an open source Java tool for working with PDF documents. This project allows creation of new PDF documents, manipulation of existing documents and the ability to extract content from documents. Apache PDFBox also includes several command line utilities.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
-   [[3] [External resources]](#External_resources)

## [Installation]

### [USE flags]

### [USE flags for] [dev-java/pdfbox](https://packages.gentoo.org/packages/dev-java/pdfbox) [[]] [Java library and utilities for working with PDF documents]

  ----------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`+tools`](https://packages.gentoo.org/useflags/+tools)           Build and install pdfbox-tools
  [`doc`](https://packages.gentoo.org/useflags/doc)                 Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`source`](https://packages.gentoo.org/useflags/source)           Zip the sources and install them
  [`test`](https://packages.gentoo.org/useflags/test)               Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`verify-sig`](https://packages.gentoo.org/useflags/verify-sig)   Verify upstream signatures on distfiles
  ----------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-02-06 09:12] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask dev-java/pdfbox`

## [Usage]

If compiled with USE=tools it provides a series of command-line utilities. They are available as standard Java applications. Invocations shown below are from version 2.0.26.

`user `[`$`]`pdfbox Decrypt`

    Usage: pdfbox Decrypt [options] <inputfile> [outputfile]

    Options:
      -alias    : The alias of the key in the certificate file (mandatory if several keys are available
      -password : The password to open the certificate and extract the private key from it.
      -keyStore : The KeyStore that holds the certificate.

`user `[`$`]`pdfbox Encrypt`

    Usage: pdfbox Encrypt [options] <inputfile> [outputfile]

    Options:
      -O                             : Set the owner password (ignored if certFile is set)
      -U                             : Set the user password (ignored if certFile is set)
      -certFile                  : Path to X.509 certificate (repeat both if needed)
      -canAssemble <true|false>                : Set the assemble permission
      -canExtractContent <true|false>          : Set the extraction permission
      -canExtractForAccessibility <true|false> : Set the extraction permission
      -canFillInForm <true|false>              : Set the fill in form permission
      -canModify <true|false>                  : Set the modify permission
      -canModifyAnnotations <true|false>       : Set the modify annots permission
      -canPrint <true|false>                   : Set the print permission
      -canPrintDegraded <true|false>           : Set the print degraded permission
      -keyLength <length>                      : Key length in bits (valid values: 40, 128 or 256, default is 256)

    Note: By default all permissions are set to true

`user `[`$`]`pdfbox ExtractText`

    Usage: pdfbox ExtractText [options] <inputfile> [output-text-file]

    Options:
      -password         : Password to decrypt document
      -encoding <output encoding> : UTF-8 (default) or ISO-8859-1, UTF-16BE,
                                    UTF-16LE, etc.
      -console                    : Send text to console instead of file
      -html                       : Output in HTML format instead of raw text
      -sort                       : Sort the text before writing
      -ignoreBeads                : Disables the separation by beads
      -debug                      : Enables debug output about the time consumption
                                    of every stage
      -alwaysNext                 : Process next page (if applicable) despite
                                    IOException (ignored when -html)
      -rotationMagic              : Analyze each page for rotated/skewed text,
                                    rotate to 0° and extract separately
                                    (slower, and ignored when -html)
      -startPage <number>         : The first page to start extraction (1 based)
      -endPage <number>           : The last page to extract (1 based, inclusive)
      <inputfile>                 : The PDF document to use
      [output-text-file]          : The file to write the text to

`user `[`$`]`pdfbox ExtractImages`

    Usage: pdfbox ExtractImages [options] <inputfile>

    Options:
      -password    : Password to decrypt document
      -prefix <image-prefix> : Image prefix (default to pdf name)
      -directJPEG            : Forces the direct extraction of JPEG/JPX images
                               regardless of colorspace or masking
      -noColorConvert        : Images are extracted with their
                               original colorspace if possible.
      <inputfile>            : The PDF document to use

`user `[`$`]`pdfbox OverlayPDF`

    Usage: pdfbox OverlayPDF <inputfile> [options] <outputfile>

    Options:
      <inputfile>                                  : input file
      <defaultOverlay.pdf>                         : default overlay file
      -odd <oddPageOverlay.pdf>                    : overlay file used for odd pages
      -even <evenPageOverlay.pdf>                  : overlay file used for even pages
      -first <firstPageOverlay.pdf>                : overlay file used for the first page
      -last <lastPageOverlay.pdf>                  : overlay file used for the last page
      -useAllPages <allPagesOverlay.pdf>           : overlay file used for overlay, all pages are used by simply repeating them
      -page  <specificPageOverlay.pdf> : overlay file used for the given page number, may occur more than once
      -position foreground|background              : where to put the overlay file: foreground or background
      <outputfile>                                 : output file

`user `[`$`]`pdfbox PrintPDF`

    Usage: pdfbox PrintPDF [options] <inputfile>

    Options:
      -password                  : Password to decrypt document
      -printerName <name>                  : Print to specific printer
      -orientation auto|portrait|landscape : Print using orientation
                                               (default: auto)
      -border                              : Print with border
      -dpi                                 : Render into intermediate image with
                                               specific dpi and then print
      -noColorOpt                          : Disable color optimizations
                                               (useful when printing barcodes)
      -silentPrint                         : Print without printer dialog box

    Available printer names:
        Brother

`user `[`$`]`pdfbox PDFDebugger`

`user `[`$`]`pdfbox PDFMerger`

    Usage: pdfbox PDFMerger <inputfiles 2..n> <outputfile>

    Options:
      <inputfiles 2..n> : 2 or more source PDF documents to merge
      <outputfile>      : The PDF document to save the merged documents to

`user `[`$`]`pdfbox PDFReader`

`user `[`$`]`pdfbox PDFSplit`

    Usage: pdfbox PDFSplit [options] <inputfile>

    Options:
      -password    : Password to decrypt document
      -split     <integer>   : split after this many pages (default 1, if startPage and endPage are unset)
      -startPage <integer>   : start page
      -endPage   <integer>   : end page
      -outputPrefix  : Filename prefix for split files
      <inputfile>            : The PDF document to use

`user `[`$`]`pdfbox PDFToImage`

    Usage: pdfbox PDFToImage [options] <inputfile>

    Options:
      -password              : Password to decrypt document
      -format <string>                 : Available image formats: JPG, jpg, tiff, bmp, BMP, gif, GIF, WBMP, png, PNG, JPEG, tif, TIF, TIFF, wbmp, jpeg
      -prefix <string>                 : Filename prefix for image files
      -page <int>                      : The only page to extract (1-based)
      -startPage <int>                 : The first page to start extraction (1-based)
      -endPage <int>                   : The last page to extract (inclusive)
      -color <string>                  : The color depth (valid: bilevel, gray, rgb (default), rgba)
      -dpi <int>                       : The DPI of the output image, default: screen resolution or 96 if unknown
      -quality <float>                 : The quality to be used when compressing the image (0 <= quality <= 1)
                                         (default: 0 for PNG and 1 for the other formats)
      -cropbox <int> <int> <int> <int> : The page area to export
      -time                            : Prints timing information to stdout
      -subsampling                     : Activate subsampling (for PDFs with huge images)
      <inputfile>                      : The PDF document to use

`user `[`$`]`pdfbox TextToPDF`

    Usage: pdfbox TextToPDF [options] <outputfile> <textfile>

    Options:
      -standardFont <name> : Helvetica (default)
                             Courier-Bold
                             Courier-BoldOblique
                             Times-Roman
                             Helvetica-Oblique
                             Courier-Oblique
                             Symbol
                             Times-Italic
                             Helvetica
                             Helvetica-Bold
                             Times-BoldItalic
                             ZapfDingbats
                             Times-Bold
                             Helvetica-BoldOblique
                             Courier
      -ttf <ttf file>      : The TTF font to use.
      -fontSize <fontSize> : default: 10
      -pageSize  : Letter (default)
                             Legal
                             A0
                             A1
                             A2
                             A3
                             A4
                             A5
                             A6
      -landscape           : sets orientation to landscape

`user `[`$`]`pdfbox WriteDecodedDoc`

    Usage: pdfbox WriteDecodedDoc [options] <inputfile> [outputfile]

    Options:
      -password  : Password to decrypt the document
      -skipImages          : Don't uncompress images
      <inputfile>          : The PDF document to be decompressed
      [outputfile]         : The filename for the decompressed pdf

## [External resources]

-   [https://pdfbox.apache.org/2.0/commandline.html](https://pdfbox.apache.org/2.0/commandline.html)