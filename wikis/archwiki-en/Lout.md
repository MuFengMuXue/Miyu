# Lout

Lout is a lightware document formatting system invented by Jeffrey H. Kingston. It reads a high-level description of a document similar in style to LaTeX and produces a PostScript.

## Installation
Install the  package.

In order to enable cyrillic printout, fonts need to be installed separately (e.g ).

## Usage
Lout supports only one byte encoding, thus you need to use specific character map in case of non-english input.

{{hc|example.lout|
@SysInclude {doc}
@SysInclude {dejavu}
@Document
  @InitialFont { DejaVuSerif Base 12p}
  @InitialLanguage { Russian }
@Text @Begin

@Display @Heading {Russian language example}

@LP
Параграф на русском языке.

@End @Text
}}

iconv could be used to obtain required encoding, before feed source to lout:

 $ iconv -f utf-8 -t koi8-r example.lout example.koi8-r.lout
 $ lout  example.koi8-r.lout example.ps

Ps2pdf can be used to convert postscript to pdf:

 $ ps2pdf example.ps example.pdf
