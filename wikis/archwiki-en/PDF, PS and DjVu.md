# PDF, PS and DjVu

This article covers software to view, edit and convert PDF, PostScript (PS), DjVu (déjà vu) and XPS files.

## Engines
*
*
*
*
*
*

## Viewers
## Framebuffer
*
*
*

## Graphical
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*

## Comparison
{| class="wikitable sortable" style="text-align:center;"
! Name !! PDF !! PostScript !! DjVu !! XPS !! PDF forms !! PDF Annotation !! Non-rectangle selection !! License !! Wayland native
|-
! Adobe Reader
| Custom ||  ||  ||  ||  ||  ||  ||  ||
|-
! apvlv
| Poppler ||  || DjVuLibre ||  ||  ||  ||  (not by default, at least) ||  ||
|-
! Atril
| Poppler || libspectre || DjVuLibre || libgxps ||  ||  ||  ||  ||
|-
! DjView
|  ||  || DjVuLibre ||  ||  ||  ||  ||  ||
|-
! Emacs
| colspan=2 | Ghostscript1 || DjVuLibre1 ||  ||  ||  ||  ||  ||
|-
! Emacs pdf-tools
| Poppler ||  ||  ||  ||  ||  ||  ||  ||
|-
! ePDFView
| Poppler ||  ||  ||  ||  ||  ||  ||  ||
|-
! Foxit Reader
| Custom ||  ||  ||  ||  ||  ||  ||  ||
|-
! GNOME Document Viewer
| Poppler || libspectre || DjVuLibre || libgxps ||  ||  ||  ||  ||
|-
! gv
| colspan=2 | Ghostscript ||  ||  ||  ||  ||  ||  ||
|-
! llpp
| libmupdf ||  ||  || libmupdf ||  ||  ||  ||  ||
|-
! MuPDF
| Custom ||  ||  || Custom ||  () ||  () ||  () ||  ||
|-
! Okular
| Poppler || libspectre || DjVuLibre || Custom ||  ||  ||  ||  ||
|-
! PDF4QT
| Custom ||  ||  ||  ||  ||  ||  ||  ||
|-
! pdfpc
| Poppler ||  ||  ||  ||  ||  ||  ||  ||
|-
! qpdfview
| Poppler || libspectre1 || DjVuLibre1 ||  ||  ||  ||  ||  ||  (lacks scaling support)
|-
! Xpdf
| Custom ||  ||  ||  ||  ||  ||  ||  ||
|-
! Xreader
| Poppler || libspectre1 || DjVuLibre1 || libgxps1 ||  ||  ||  ||  ||
|-
! Zathura
| libmupdf1 / Poppler1 || libspectre1 || DjVuLibre1 || libmupdf1 ||  ||  ||  ||   ||
|}

# Optional dependency needs to be installed

## PDF forms
The PDF forms column in the above table refers to AcroForms support. If you do not need your input to be directly extractable from the PDF, you can also use the applications in #Graphical PDF editing to put text on top of a PDF. PDF forms can be created with LibreOffice Writer (View > Toolbars > Form Controls) and the advanced PDF editors.

The proprietary and deprecated XFA format for forms is not fully supported by Popplerand only supported by Adobe Reader and Master PDF Editor.

Alternatively, web browsers such as Firefox or Chromium feature a built-in PDF viewer capable of filling out forms.

## Graphical PDF editing
## Editors that can import PDF files
* Scribus can import and export PDF; text is imported as polygons.[https://wiki.scribus.net/canvas/Importing_PDF_files_as_Vector_Graphics
* LibreOffice Draw can import and export PDF; text is imported as text; embedded fonts are substituted.* Inkscape can import and export PDF; text is imported as cloned glyphs or text; with the latter embedded fonts are substituted.
* Graphics editors like GIMP and  can also import and export PDFs at the cost of rasterization.

## Basic editors
*
*
*
*
*
*
*
*
*
*
*
*

## Cropping tools
*
*
*
*

## Advanced editors
*
*
*

## Comparison of advanced editors
{| class="wikitable sortable" style="text-align:center;"
! Name !! Cost (USD, lifetime) !! Page Labels !! Form Designer !! Content Editing (Text and Images) !! Optimize PDFs !! Digitally Sign PDFs !! License
|-
! Master PDF Editor
| 85.34 ||  ||  ||  ||  ||  ||
|-
! Qoppa PDF Studio Standard
| 99 ||  ||  ||  ||  ||  ||
|-
! Qoppa PDF Studio Pro
| 139 ||  ||  ||  ||  ||  ||
|}

## PDF tools
See also Ghostscript.

*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*

## Command snippets
## Create a PDF from images
With GraphicsMagick:

 $ gm convert 1.jpg 2.jpg 3.jpg out.pdf

With ImageMagick:

 $ magick 1.jpg 2.jpg 3.jpg out.pdf

Note that ImageMagick's output is lossy. For lossless PDF creation from jpeg, use .

## Concatenate PDFs
With Ghostscript:

 $ gs -dNOPAUSE -sDEVICE=pdfwrite -sOUTPUTFILE=out.pdf -dBATCH 1.pdf 2.pdf 3.pdf

With PDFtk:

 $ pdftk 1.pdf 2.pdf 3.pdf cat output out.pdf

With Poppler:

 $ pdfunite 1.pdf 2.pdf 3.pdf out.pdf

With QPDF:

 $ qpdf --empty --pages 1.pdf 2.pdf 3.pdf -- out.pdf

## Extract text from PDF
With Poppler and maintaining the layout:

 $ pdftotext -layout in.pdf out.txt

See also .

With :

 $ ebook-convert in.pdf out.txt

Results vary between applications, depending on the PDF file.

## Decrypt a PDF
This section lists commands to decrypt a PDF to an unencrypted file.  Note that most PDF viewers also support encrypted PDFs.

With PDFtk:

 $ pdftk in.pdf input_pw password output out.pdf

With Poppler to PostScript:

 $ pdftops -upw password in.pdf out.ps

With QPDF:

 $ qpdf --decrypt --password=password in.pdf out.pdf

## Encrypt a PDF
The user password is used for encryption, the owner password to restrict operations once the document is decrypted, for more information, see Wikipedia:PDF#Encryption and signatures.

With PDFtk:

 $ pdftk in.pdf output out.pdf user_pw password

With PoDoFo:

 $ podofoencrypt -u user_password -o owner_password in.pdf out.pdf

With QPDF:

 $ qpdf --encrypt user_password owner_password key_length -- in.pdf out.pdf

where  can be 40, 128 or 256.

## Extract images from a PDF
With , saving images as JPEG:

 $ pdfimages infile.pdf -j outfileroot

## Extract page range from PDF, split multipage PDF document
With Ghostscript as a single file[https://forums.freebsd.org/threads/split-pdf-file.58902/#post-336971

 $ gs -sDEVICE=pdfwrite -dNOPAUSE -dBATCH -dSAFER -dFirstPage=first -dLastPage=last -sOutputFile=outfile.pdf infile.pdf

With PDFtk as a single file:

 $ pdftk infile.pdf cat first-last output outfile.pdf

With Poppler as separate files:

 $ pdfseparate -f first -l last infile.pdf outfileroot-%d.pdf

With QPDF as a single file:

 $ qpdf --empty --pages infile.pdf first-last -- outfile.pdf

With mutool as a single file:

 $ mutool clean -g infile.pdf outfile.pdf first-last

## Impose a PDF (nup)
PDF Imposition is the process by which multiple input pages are combined into one output page, layed out into a rowsxcolumns grid.

It can be done with pdfjam (notice that wrapper scripts such as pdfnup and pdfbook are deprecated):

 $ pdfjam --nup rowsxcolumns input.pdf --outfile output.pdf

or with pdfsak:

 $ pdfsak --input-file input.pdf --output output.pdf --nup rows columns

## Inspect metadata
With ExifTool:

 $ exiftool -All file.pdf

With Poppler:

 $ pdfinfo file.pdf

## Remove metadata
## Using ExifTool
With ExifTool:

 $ exiftool -All= -overwrite_original input.pdf
 $ mv input.pdf /tmp/temp.pdf
 $ qpdf --linearize /tmp/temp.pdf input.pdf

The linearize step is needed to prevent recovery of deleted metadata. See this SuperUser question and the related ExifTool forum thread.

## Using pdftk
Many  PDFs  store document metadata using both an Info dictionary (old school) and an XMP stream (new school). This pdftk command remove the XMP stream from the PDF altogether. It does not remove the Info dictionary.

Note that objects inside the PDF might have their own, separate XMP metadata streams, and that this command does not remove those. It only removes the PDF’s document‐level XMP stream.

 $ pdftk input.pdf drop_xmp output output.pdf

## Reduce size of a PDF
PDF size can be reduced by setting an appropriate optimization or compression level.

With Ghostscript one of:

 $ ps2pdf -dPDFSETTINGS=/screen in.pdf out.pdf

or

 $ gs -dNOPAUSE -dBATCH -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/printer -sOutputFile=out.pdf in.pdf

For different settings see the documentation.

There is also , a script wrapping gs.

## Rasterize a PDF
These commands will convert your PDF into images.

With GraphicsMagick to convert a specific page into an image file:

 $ gm convert -density dpi infile.pdfoutfile.jpg

With ImageMagick to convert a specific page into an image file:

 $ magick convert -density dpi infile.pdf[page outfile.jpg

With ImageMagick to convert all pages into another PDF file composed by an image file per page:

 $ magick convert -density dpi infile.pdf outfile.pdf

With Poppler to convert all pages into one image file per page:

 $ pdftoppm -jpeg -r dpi infile.pdf outfileroot

With Poppler to convert a specific page into an image file:

 $ pdftoppm -jpeg -r dpi -f page -singlefile infile.pdf outfileroot

## Split PDF pages
With mupdf-tools to split every page vertically into two pages:

 $ mutool poster -y 2 in.pdf out.pdf

Can be used to undo simple imposition.

## Add an image
Adding an image to any location in a PDF can be done

* with ImageMagick (convert),  and . (Wrapper script)
* with Xournal++
* with LibreOffice

Details on these and other solutions can be found on StackExchange.

## Add digital signature to PDF
 can digitally sign PDF files with X.509 certificates in GUI and CLI.

Readers such as Okular and MuPDF can sign PDFs with digital signatures. This requires a PFX certificate, which can be created with an OpenSSL command:

 $ openssl req -x509 -days 365 -newkey rsa:2048 -keyout cert.pem -out cert.pem
 $ openssl pkcs12 -export -in cert.pem -out cert.pfx

MuPDF users can then sign PDFs with the  using the graphical interface, or its mutool-sign tool.

Okular users must import  into a certificate store such as the one in the default Firefox profile.With Firefox this is done through Settings > Privacy & Security > View Certificates > Your Certificates > Import and selecting cert.pfx. Afterwards Okular will offer this certificate to be used when signing PDFs.

Libreoffice can also sign PDFs.[https://help.libreoffice.org/6.3/en-US/text/shared/guide/digital_signatures.html

## Removing annotations from a PDF
With  $ pdftk in.pdf output - uncompress | sed '/^\/Annots/d' | pdftk - output out.pdf compress

With :

 $ rewritepdf.pl -C in.pdf out.pdf

See https://superuser.com/a/1051543 for more information.

## Add page numbers
With [https://github.com/raffaem/pdfsak pdfsak:

 $ pdfsak --input-file input.pdf --output output.pdf --text "\large \$page/\$pages" br 0.99 0.99 --latex-engine xelatex --font "Noto Regular"

## Add page labels
Page labels are logical page numbers shown in the navigation bar of your PDF reader. They are useful for example if the first pages of the PDF are indices numbered with roman numbers (I, II, etc.), while the page numbered "1" corresponds to a PDF page greater than 1, and you want the page number shown in the navigation bar to corresponds to the page number shown in the physical page.

This should not be confused with adding page numbers into a physical page. See section 12.4.2 of PDF reference to better understand page labels.

# Using pagelabels-py, let's say we have a PDF named , that has 12 pages.
#* Pages 1 to 4 should be labelled  to .
#* Pages 5 to 9 should be labelled  to .
#* Pages 10 to 12 should be labelled  to
#* We can issue the following list of commands:
#*
# Using , create a  file with labels:
#* Where:
#*;PageLabelBegin: signal a new page label definition will follow
#*;PageLabelNewIndex: is the PDF page index from which the numbering style applies, counting from one. The numbering style will continue until the next page label or, if there are no more page labels, until the end of the document.
#*;PageLabelStart: is the starting number. For example, if you specify 5 here, the pages will be numbered 5, 6, 7, ...
#*;PageLabelPrefix: a text to put before the number in page labels.
#*;PageLabelNumStyle: can be , , , ,  or .
#* Then use:

See this SuperUser question for more details.

## Extract bookmarks
With pdftk:

 $ pdftk file.pdf dump_data_utf8 | grep '^Bookmark'

With qpdf:

 $ qpdf --json --json-key=outlines file.pdf

See https://unix.stackexchange.com/questions/143886/how-to-extract-bookmarks-from-a-pdf-file for more information.

## Add bookmarks
## With pdftk
Create a text file  with bookmark definitions in the following format:

Where
;BookmarkBegin: signal a new bookmark definition
;BookmarkTitle: the title of the bookmark
;BookmarkLevel: the level of the bookmark in the hierarchy
;BookmarkPageNumber: the page number the bookmark redirects to

In this example, the above file will create the following bookmark structure:

*Chapter 1
**Chapter 1.1
**Chapter 1.2
**Chapter 1.3
***Chapter 1.3.1
*Chapter 2

Apply the bookmarks with the following command:

 $ pdftk input.pdf update_info_utf8 bookmark_definitions.txt output output.pdf

## Extract pages contained within a bookmark
To extract the pages contained within a bookmark, you can use .

With  you will be prompted on what bookmark whose pages you want to extract and where to save it. To extract all bookmarks of a given hierarchical level:

 $ pdf_extbook file -a level output_file_stem

## Remove blank pages
One can use the following script to remove blank pages from a PDF file (credit: SuperUser post):

{{bc|
#!/bin/sh

IN="$1"
filename=$(basename "${IN}")
filename="${filename%.*}"
PAGES=$(pdfinfo "$IN" | grep ^Pages: | tr -dc '0-9')

non_blank() {
	for i in $(seq 1 $PAGES); do
		PERCENT=$(gs -o - -dFirstPage=${i} -dLastPage=${i} -sDEVICE=ink_cov "$IN" | grep CMYK | nawk 'BEGIN { sum=0; } {sum += $1 + $2 + $3 + $4;} END { printf "%.5f\n", sum } ')
		if [ $(echo "$PERCENT > 0.001" | bc) -eq 1 ]; then
			echo $i
			#echo $i 1>&2
		fi
		echo -n . 1>&2
	done | tee "$filename.tmp"
	echo 1>&2
}

set +x
pdftk "${IN}" cat $(non_blank) output "${filename}_noblanks.pdf"
}}

Use it like .

The script needs ,  and .

## Find fonts used in a PDF
The  command (from ), can be used to find which fonts a PDF uses and if they have been embedded in it or not:

This can be used when having issues displaying properly the text in a PDF, to determine if missing fonts or their metric-compatible equivalent need to be installed.

## Repair broken PDF file
With :

 $ gs -o repaired.pdf -sDEVICE=pdfwrite -dPDFSETTINGS=/prepress corrupted.pdf

With :

 $ pdftocairo -pdf corrupted.pdf repaired.pdf

With :

 $ mutool clean corrupted.pdf repaired.pdf

Reference: https://superuser.com/q/278562

## Convert PDF to PDF/A standard
With :

 $ ocrmypdf --tesseract-timeout=0 --remove-background document.pdf document_pdfa.pdf

Reference: https://ocrmypdf.readthedocs.io/en/latest/cookbook.html#don-t-actually-ocr-my-pdf

## Validate PDF/A compliance
Using  you can validate the compliance of your PDF to different flavours of the PDF/A standard:

 $ verapdf --flavour 1a --format text document.pdf

## DjVu tools
* DjVuLibre provides many command-line tools, like  for example.
*
*

## Convert DjVu to images
Break Djvu into separate pages:

 $ djvmcvt -i input.djvu /path/to/out/dir output-index.djvu

Convert Djvu pages into images:

 $ ddjvu --format=tiff page.djvu page.tiff

Convert Djvu pages into PDF:

 $ ddjvu --format=pdf inputfile.djvu ouputfile.pdf

You can also use --page to export specific pages:

 $ ddjvu --format=tiff --page=1-10 input.djvu output.tiff

this will convert pages from 1 to 10 into one tiff file.

## Processing images
You can use  to:

* fix orientation
* split pages
* deskew
* crop
* adjust margins

## Make DjVu from images
There is a useful script .

 $ img2djvu -c1 -d600 -v1 ./out

it will create 600 DPI  from all files in  directory.

Alternatively, you can try , which seems to create smaller files especially on images with well defined background.

## PostScript tools
* Ghostscript
*

## ps2pdf
ps2pdf is a wrapper around ghostscript to convert PostScript to PDF:

 $ ps2pdf -sPAPERSIZE=a4 -dOptimize=true -dEmbedAllFonts=true YourPSFile.ps

Explanation:

* with  you define the paper size. For valid PAPERSIZE values, see *  lets the created PDF be optimised for loading.
*  makes the fonts look always nice.

## Libraries
## C/C++
*
*

## Python
*
*
*
*
*

## Java
*
*
