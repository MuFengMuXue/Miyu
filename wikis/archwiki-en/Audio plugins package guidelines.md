# Audio plugins package guidelines

This document covers proposed standards and guidelines on writing PKGBUILDs for plugins for Professional audio.

## Destination directory and naming rules
{| class="wikitable"
|-
! Plugin format !! Package naming !! Destination directory !! File naming !! Directory naming !! Groups !! Optdepends
|-
|  CLAP ||  || /usr/lib/clap/ ||  ||  ||  ||
|-
|  DSSI ||   || /usr/lib/dssi/ ||  ||  ||  ||
|-
|  LADSPA ||   || /usr/lib/ladspa/ ||  ||  ||  ||
|-
|  LV2 ||   || /usr/lib/lv2/ || ||  ||  ||
|-
|  VCV Rack ||   || /usr/lib/vcvrack/plugins/ || ||  ||  ||
|-
|  VST 2 ||   || /usr/lib/vst/ ||  ||  ||  ||
|-
|  VST 3 ||   || /usr/lib/vst3/ ||  ||  ||  ||
|}

## Package description
The package description should at least contain the word  and what type of plugin it is: , , , , , , .

## Windows plugins
Some plugins, which are not available in a native Linux version, but are available for Windows, can be used on Linux via Wine and  or other bridging solutions,

Also read the Wine package guidelines.

{| class="wikitable"
|-
! Architecture !! Plugin format !! Package naming !! Destination directory !! File naming !! Directory naming !! Application data !! Groups !! Optdepends
|-
| x86_64 || CLAP ||  || /usr/lib/wine/x86_64-windows/clap/ ||  ||  || /usr/share/wine/clap/ ||  ||
|-
| x86_64 || VST 2 ||   || /usr/lib/wine/x86_64-windows/vst/ ||  ||  || /usr/share/wine/vst/ ||  ||
|-
| x86_64 || VST 3 [https://steinbergmedia.github.io/vst3_dev_portal/pages/Technical+Documentation/Locations+Format/Plugin+Format.html#for-the-windows-platform ||   || /usr/lib/wine/x86_64-windows/vst3/ ||  ||  || /usr/share/wine/vst3/ ||  ||
|-
| i386 ||  CLAP ||  || /usr/lib32/wine/i386-windows/clap/ ||  ||  || /usr/share/wine/clap/ ||  ||
|-
| i386 ||  VST 2 ||   || /usr/lib32/wine/i386-windows/vst/ ||  ||  || /usr/share/wine/vst/ ||  ||
|-
| i386 ||  VST 3 https://steinbergmedia.github.io/vst3_dev_portal/pages/Technical+Documentation/Locations+Format/Plugin+Format.html#for-the-windows-platform ||   || /usr/lib32/wine/i386-windows/vst3/ ||  ||  || /usr/share/wine/vst3/ ||  ||
|}

## Package description
The package description should at least contain the word ,  and what type of plugin it is: , , .
