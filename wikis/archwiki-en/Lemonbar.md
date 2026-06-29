# Lemonbar

lemonbar is a lightweight bar based on XCB. It provides foreground/background color switching along with text alignment and colored under/overlining of text, full UTF-8 support and reduced memory footprint. Nothing less and nothing more.

## Installation
Install the  package.

## Configuration
Configuration of lemonbar is now completely done via -like format strings and command line options as opposed to older versions, where configuration took place at compile-time.

See  for a short overview of those configuration options.

## Usage
 prints no information on its own. To get any text into  you need to pipe text into it. The following example would write the text "Hello World" into your bar.

If you want the text in  to update through a script, you need to add the  option. This prevents  from exiting after stdin is closed.

## Colors
 uses the following commands to color the text, background or the under/overline. Colors can be specified via the formats ,  (with an alpha channel; this requires a compositor to be running), or even .

The special color  indicates the default color (which is set by command-line flags, or is otherwise the default white text on a black background).

{| class="wikitable"
! Command !! Meaning
|-
| {{ic|%{Fcolor} }} || Use color as the foreground/font color
|-
| {{ic|%{Bcolor} }} || Use color as the background
|-
| {{ic|%{Ucolor} }} || Use color for under/overlining the text
|}

## Text alignment
 also supports alignment of text. It uses the following commands to align the text

{| class="wikitable"
! Command !! Meaning
|-
| {{ic|%{l} }} || Aligns the text to the left
|-
| {{ic|%{c} }} || Aligns the text to the center
|-
| {{ic|%{r} }} || Aligns the text to the right
|}

## Examples
The following example prints the date and time in the middle of the bar, the font's color being  and the background  and changes the font/background color back to the default color afterwards. Run it with

{{hc|example.sh|2=
#!/bin/sh

# Define the clock
Clock() {
        DATETIME=$(date "+%a %b %d, %T")

        printf "$DATETIME"
}

# Print the clock

while true; do
        echo "%{c}%{F#FFFF00}%{B#0000FF} $(Clock) %{F-}%{B-}"
        sleep 1
done
}}

Another example showing the battery percentage. To use this script you need to install .

{{hc|example.sh|2=
#!/bin/sh

#Define the battery
Battery() {
        BATPERC=$(acpi --battery  cut -d, -f2)
        echo "$BATPERC"
}

# Print the percentage
while true; do
        echo "%{r}$(Battery)"
        sleep 1;
done
}}

## XFT fonts
The default lemonbar version does not support XFT fonts. To get support for XFT fonts, you need to install the  fork.

To use different font with lemonbar, you need to pass  option when starting lemonbar e.g. .

## Font Awesome icons
With XFT support, you can also add Font Awesome icons to your bar. You need to install  before using the icons and pass  (or the appropriate version instead of '6') to lemonbar. Please note, that you also need to specify one more font (e.g. ) to be used for other symbols than font awesome icons if you want something else visible in your lemonbar as font awesome does not contain other symbols.

Before adding an icon to lemonbar, you need to look up its unicode id on the icon list and pass it to lemonbar string. Here is a script that displays icon with Unicode id  in lemonbar:

Pay extra attention to  flag, as it is necessary to properly use echo with escape sequences.

And corresponding lemonbar command:

 lemonbar -f "Roboto Medium" -f 'Font Awesome 6 Free' -f 'Font Awesome 6 Brands' -f 'Font Awesome 6 Free Solid'
