# Font configuration/Examples

See Font configuration for the main article.

Configurations can vary to a degree.  Please post Fontconfig configurations with an explanation for why they were done.

## Hinted fonts
## No hinting for italic or bold
## Enable anti-aliasing only for bigger fonts or certain fonts
Some users prefer the sharper rendering that anti-aliasing does not offer:

You might also want to disable anti-aliasing only for fonts that look well without anti-aliasing. See Font configuration/Examples/No anti-aliasing.

## Disable bold font
For when a font does not present itself well in bold and you cannot disable bold fonts in the application (st for example).

## Disable ligatures for monospaced fonts
This prevents letter combinations like "ffi" from being squashed into a single-width character in some monospaced fonts.  The whole  block needs to be duplicated to include extra fonts.

Some other fonts may also require disabling features such as  and/or .

You can test the effectiveness of this with the following command:

 $ echo -e "| worksheet |\n| buffering |\n| difficult |\n| finishing |\n| different |\n| efficient |" | pango-view --font="Nimbus Mono PS" /dev/stdin

Some programs do not support the  tag, so for those replacing the font with another is the only option. See Font configuration#Set default or fallback fonts for details.

## Enable typographic features
Some fonts like  support many useful typographic features that are not enabled by default.

Those features can be managed system-wide (for all users) or per user using fontconfig, and/or per application, using applications internal setting. (For those programs which support configuring them internally, like LibreOffice.)

Below is an example of enabling , , ,  and  features for the Inter font. You can substitute them with any other feature of any other font supporting them. A complete list of all possible typographic features can be found at Wikipedia:List of typographic features, but check if your font of choice supports a feature, before trying to enable it.

Verification of those features being enabled can be done both visually or using  command.

## Default fonts
For font consistency, all applications should be set to use the serif, sans-serif, and monospace aliases, which are mapped to particular fonts by fontconfig. See Metric-compatible fonts for options and examples.

## The standard names
The standard names are the aliases , , and . Setting custom values for these aliases will change the defaults for almost all applications, including , , and . This example prefers  for everything except fixed-width fonts, for which  is preferred.

## Arabic
Example fonts.conf which specifies a default font for the Arabic language and keeps western style fonts for Latin letters. You will require either  or  for the below to work. You can also choose to install any other Arabic fonts and accordingly change the font name below based on your preference

The above should work for most applications but some applications like Chromium do not work with the language match test. If you find some applications not using your selected fonts, you can use the below alias and prefer tags which seems to work.

## Excluding Arabic script from other languages
Fonts using Arabic script but are of other languages can be excluded. For example, the Nastaliq Urdu fonts could be chosen by default for Arabic. Use the following configuration to blacklist them, ensuring the system uses a proper Arabic font.

## Japanese
Example fonts.conf which also specifies a default font for the Japanese locale (ja_JP) and keeps western style fonts for Latin letters.

## Chinese
## Chinese in Noto Fonts
Apply Noto Fonts while replacing Microsoft Fonts with WenQuanYi Micro Hei

## CJK, but other Latin fonts are preferred
Requires .

You can replace // with your favorite // fonts.

## Alternate stylistic sets for fonts
Certain fonts come with alternate stylistic sets for characters through an OpenType feature.
Generally these stylistic sets are named  and contain small changes to individual characters.
This shows how to change the default dotted zero to a slashed zero for the monospace version of .

See What are "Stylistic Sets?" for more information on this.
