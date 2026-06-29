# Localization/Indic

This page explains how setup your Arch installation in order to input Indic languages.

## All Indic
## Fonts
The following packages provide fonts for a variety of Indic scripts:

*  - Font for Bangla
*  - Indic OpenType Fonts collection (containing ttf-freebanglafont), provides the character U+0CA0 "ಠ"
*  - Indic TrueType fonts from Fedora Project (containing Oriya Fonts and more)
*  - Devanagari TrueType fonts (contains 283 fonts)
*  - TrueType Gurmukhi fonts (gurbaniwebthick,prabhki)
*  - TTF Gurmukhi / Punjabi (contains 252 fonts)
*  - TTF Gujarati fonts (Avantika,Gopika,Shree768)
*  - Kannada, the language of Karnataka state in India
*  - Sinhala Unicode font
*  - Tamil Unicode fonts
*  - Urdu fonts (Jameel Noori Nastaleeq (+kasheeda), Nafees Web Naskh, PDMS Saleem Quran Font) and font configuration to set Jameel Noori Nastaleeq as default font for Urdu
*  - Meta package providing all Malayalam Unicode Fonts released by Swathanthra Malayalam Computing packaged from upstream releases.

## Locale
Setting up the locale with the instructions from the dedicated page will ensure that applications use appropriate localization when available.

## Input methods
See Input method#List of available input method editors.

## Sinhalese
This section describes how to get Sinhalese Unicode support and Sinhalese Unicode input to work using IBus (sayura-ibus) or scim (sayura-scim).

## Fonts
For Sinhala support, you can install any of these fonts:

*  - Noto Sans Sinhala, a sans serif font.
*  - FreeSerif, a serif font.
*  - LKLUG, a serif font.

## Guide to install Sinhala Unicode Font
Download https://sinhala.sourceforge.net/files/lklug.ttf and place it in .

Then Run the following command
 fc-cache -fv

And proceed to the below steps..

## Locale
Edit /etc/locale.gen. Uncomment following line
 si_LK UTF-8
Run following program
 locale-gen

Immediately you will be able to read Sinhala Unicode in your programs (If not You may need to restart the relavent programs. eg: Firefox)

## Input methods
See Input method#List of available input method editors.
