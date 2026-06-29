# Localization/Bengali

This article describes how to set up a Wikipedia:Bengali language environment. It does not cover setting up Bengali/Bangla input on the console.

## Fonts
*  - Font for Bangla
* Avro Unicode Fonts & Lipighor free fonts - Install following Fonts#Manual installation

## Locale
Open  with your favorite text editor. And then uncomment  or :

and then run . For more information please read this article

## Input methods
There are multiple open source input method engines available:

* Avro supports phonetic input for Bangla in IBus via .
* OpenBangla Keyboard supports Bangla phonetic (Avro phonetic), Probhat, Munir Optima layout for Bangla in IBus via .
*  provider for Unijoy, Inscript, Probhat, Disha and ITRANS

See IBus to set up the engines above.

See also Input method for a list of available input-method frameworks.

## Troubleshooting
## Broken fonts in Firefox
Some applications (like Firefox) and Desktop Environments will use  (, , , , , , , ) by default. The  do not have full support for Bengali characters alignment. Consider using  over  or  as a  source.

## No IBus Support in GNOME
The IBus preferences does not work with GNOME. Make sure to enable Avro/OpenBangla from .
