The key repeat rate controls how quickly a key press on the keyboard will repeat if the key is pressed and held for a period of time. This time delay value is adjusted differently depending on the environment in which the keyboard is providing input.

## [Console]

On Gentoo the [[[sys-apps/kbd]](https://packages.gentoo.org/packages/sys-apps/kbd)[]] package includes utilities to adjust the consolefont, keymaps, and key repeat rate. By default on the **[x86]** architecture, the characters per second value of 30. This is the highest value. Note that in this environment, a characters per second rate is used, whereas another environment may use different unit of measurement.

The following command will decease the character repeat rate on the console to 25 characters per second:

`root `[`#`]`kbdrate --rate=25`

See [man 8 kbdrate] for additional details.

## [GNOME]

Within a [GNOME](https://wiki.gentoo.org/wiki/GNOME "GNOME") environment, the key repeat rate is controlled as a delay between key repeats in milliseconds. This means a smaller number will mean a *faster* key repeat rate. The default amount of delay between key presses is 30 milliseconds:

`user `[`$`]`gsettings get org.gnome.desktop.peripherals.keyboard repeat-interval`

30

The following command uses [gsettings] (included in [[[dev-libs/glib]](https://packages.gentoo.org/packages/dev-libs/glib)[]]) to *decrease* the time between key repeats by 10 milliseconds, which will therefore *increase* the overall output when pressing and holding a key:

`user `[`$`]`gsettings set org.gnome.desktop.peripherals.keyboard repeat-interval 25`

## [See also]

-   [Keyboard layout switching](https://wiki.gentoo.org/wiki/Keyboard_layout_switching "Keyboard layout switching") --- maps scancodes from a keyboard into characters sent to an application.