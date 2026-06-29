# LilyPond

LilyPond is a free score writing application.
Its input is a plain text file in the LilyPond music writing format, and its output is in either PostScript or PDF.

## Installation
Install the  package.

## Front-ends
*
*

## Usage
Create a test file like:

{{hc|test.ly|
{
 c' e' g' e'
}
}}

To compile it, use:

 $ lilypond test.ly

It will create  and  files that contain your score.

LilyPond provides  to convert MusicXML to the LilyPond format.

For more information, see ,  and the documentation.

## Text editor support
LilyPond comes with modes for Emacs and Vim, see the documentation.

For Vim see the filetype plugin  for the available key mappings.

## Emacs lilypond-mode
 package installs some Emacs files including .

To use , firstly  then again .

## NeoVim
nvim-lilypond-suite is a plugin for writing LilyPond scores with asynchronous make, midi/MP3 player, "hyphenation" function for lyrics, fast syntax highlighting... This repository also contains an ftplugin for LaTeX files which allows embedded LilyPond syntax highlighting, and makeprg which support  or  package out of the box.
