# MathJax

MathJax is a JavaScript display engine for mathematics that works in all browsers.
It is able to parse TeX input in html files to produce svg output, amongst other supported formats. The higher-level Jupyter notebook depends on MathJax and other modules for plotting, running interactive code, etc.

MathJax can easily be embedded on any website to typeset your TeX.
It is possible to quickly integrate MathJax with a distributed network service, see here for the currently available CDN.

This article assumes you want a hard copy of MathJax on your system.

## Installation
Install one of the following;

*  - Version 3
*  - Version 2

## Configuration
## Local Usage
The scripts for MathJax are located in  for both version 2 and 3. There are some differences in using the scripts between the versions. For version 3 there are a number of pre built components with different output results and functionality, click here for a list and explanation of the components.

To have MathJax parse the TeX code in  and produce SVG output:

     ...
     Version 2

     ...
     ...
     Version 3

     ...

Do not forget to include a configuration query string to tell MathJax about your desired i/o formats.

You can also configure MathJax inline, see here for more details and configuration options.

Your browser should now render the symbols at .

Note that the TeX delimiters MathJax uses by default are  for inline math and ,  for outline math.

## Server Usage
In order to serve your clients with MathJax processed documents, you need your scripts to access its main file:

 (or  for version 2).

Let us assume the server's root directory is set to , creating symlinks will grant your scripts access to the installed package:

 $ cp -rs /usr/share/mathjax /srv/http/mathjax

You can now have MathJax parse the TeX code in, say,  by including in its head:

or for version 2:

## Troubleshooting
## MathJax and Plotly
If you are using  as well, loading MathJax before Plotly might fail to render TeX code. Loading Plotly before MathJax should work. For example:

You may also try different MathJax output.

## TeX raw code visible while page is loading
It can happen that MathJax takes some time to typeset and raw TeX code appears during the while, producing an unpleasant result.

You can fix this by setting  in some element's  properties, and catch the event MathJax emits after typesetting is done to show it:

 MathJax.Hub.Queue( function () {
     document.getElementById("myID").visibility = "visible";
 });
