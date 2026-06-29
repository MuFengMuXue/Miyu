# DocBook

From Wikipedia:

:DocBook is a semantic markup language for technical documentation. It was originally intended for writing technical documents related to computer hardware and software, but it can be used for any other sort of documentation.
:As a semantic language, DocBook enables its users to create document content in a presentation-neutral form that captures the logical structure of the content; that content can then be published in a variety of formats, including HTML, XHTML, EPUB, PDF, man pages, Web help and HTML Help, without requiring users to make any changes to the source. In other words, when a document is written in DocBook format it becomes easily portable into other formats, rather than needing to be rewritten.

## Installation
Install  and .

## Usage
## Validating XML file
To validate the XML file, use:

 $ xmllint --valid --noout /path/to/file.xml

This will generate no output if the file is proper XML.

## Converting into XHTML
## Single file
To convert into a XHTML file (single file), use:

 $ xsltproc /usr/share/xml/docbook/$(pacman -Q docbook-xsl | cut -d ' ' -f 2 | cut -d '-' -f 1)/xhtml/docbook.xsl /path/to/file.xml > output.html

## Segmented
To convert into a segmented XHTML file (each section in its own file), use:

 $ xsltproc /usr/share/xml/docbook/$(pacman -Q docbook-xsl | cut -d ' ' -f 2 | cut -d '-' -f 1)/xhtml/chunk.xsl /path/to/file.xml

## Automating
Add the following to your shell configuration file:

 alias doc2html1="xsltproc /usr/share/xml/docbook/xhtml/docbook.xsl"
 alias doc2multihtml="xsltproc /usr/share/xml/docbook/xhtml/chunk.xsl"
 alias docvalidate="xmllint --valid --noout"

## Troubleshooting
## Compilation errors
If you have already installed the packages above, but begin to see compilation errors such as:

Reinstall DocBook, if something has corrupted the catalog file, this will run  and rebuild , which may resolve these compile errors.

## Tips and tricks
## Comments
Comments are somewhat problematic within an XML file. One possibility is to use a non-existing processing-instruction, e.g.:

See https://stackoverflow.com/a/14650451 for more information on this problem.
