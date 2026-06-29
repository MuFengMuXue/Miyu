**Resources**

[[]][GitHub](https://github.com/makkarpov/msi-keyboard)

[[]][Package information](https://packages.gentoo.org/packages/app-laptop/msi-keyboard)

**msi-keyboard** is a command line program to interact and control the backlight of MSI laptop keyboards. This program is written in C++ by Maxim Karpov, and uses the [[[dev-libs/hidapi]](https://packages.gentoo.org/packages/dev-libs/hidapi)[]] library.

## [Installation]

### [Emerge]

To install [[[app-laptop/msi-keyboard]](https://packages.gentoo.org/packages/app-laptop/msi-keyboard)[]]:

`root `[`#`]`emerge --ask app-laptop/msi-keyboard`

## [Usage]

To get information about how to use this program, just type this command in a terminal:

`user `[`$`]`msi-keyboard`

    msi-keyboard normal <left> <middle> <right>
    msi-keyboard gaming <left>
    msi-keyboard breathing <left> <middle> <right>
    msi-keyboard wave <left> <middle> <right>

    All colors can be specified either in HEX form (rrggbb) or as hue (hXXX)
    Breathing and wave mode also accepts color pairs (first-second) as argument

For example, to change the actual keyboards colors to the classic red, blue and green keyboard, with normal mode, type:

`user `[`$`]`msi-keyboard normal ff0000 0000ff 00ff00`