# Tectonic

Tectonic is a TeX distribution based on the XeTeX TeX engine.

It downloads the TeX software packages that are required to compile a document on-demand, powered by the TeX Live TeX distribution. An advantage of Tectonic is that it, unlike traditional TeX tools, avoids cluttering the working directory with unnecessary files while compiling the document.

However, the XeTeX engine, that Tectonic is based on, is not maintained and may have compatibility problems and missing features compared to other engines like pdfTeX or LuaTeX (both available through a standard TeX Live installation).

## Installation
The tectonic engine can be installed with the  package.

## Usage
Basic tectonic usage is made with

 $ tectonic main.tex

which will compile it into a fully-processed pdf, with only one run of the command.

While compiling, tectonic will automatically download the necessary LaTeX packages, with no need for configuration.

## V2 interface
The newer interface, accessible with the  flag, has more features compared to the default command-line interface. More information about it can be read in the official Tectonic Book.
