[[]][Wikipedia](https://en.wikipedia.org/wiki/Computer_fan_control "wikipedia:Computer fan control")

## Contents

-   [[1] [Introduction]](#Introduction)
-   [[2] [Requirements]](#Requirements)
-   [[3] [Sensors]](#Sensors)
-   [[4] [Fans]](#Fans)
-   [[5] [External resources]](#External_resources)

## [Introduction]

When a computer works it gets warm, when it works hard it may get hot. Too hot is not good for the electronics of a computer. Therefore most computers need active cooling, through fans or in some cases water. In x86 type of systems the speed of the fans is typically controlled by the [BIOS](https://wiki.gentoo.org/wiki/BIOS "BIOS"), but it may be possible to control the fan speed with the [kernel](https://wiki.gentoo.org/wiki/Kernel "Kernel") and userspace utilities.

Gentoo supports various of those userspace utilities, e.g. [fancontrol](https://wiki.gentoo.org/wiki/Fan_speed_control/lm_sensors%27_fancontrol "Fan speed control/lm sensors' fancontrol"), and [Thinkfan](https://wiki.gentoo.org/wiki/Fan_speed_control/thinkfan "Fan speed control/thinkfan").

Reasons for wanting to deviate from BIOS controlled fans could be that the BIOS makes them spin too much (resulting in too much noise), or too slow (resulting in too high temperatures).

** Warning**\
It is generally considered more safe to have the BIOS or dedicated hardware control the fans.

There are two risks when manually controlling fan speeds:

1.  What if the program controlling the fans fails? The computer could overheat and parts could be destroyed.
2.  Higher temperatures cause more wear on the electronics, resulting in a shorter lifespan.

## [Requirements]

Controlling fan speed is not supported on all computers. The computer needs to have:

-   A BIOS that allows users to control the fan speed
-   A motherboard capable of regulating fan speeds
-   Fans that allow their speed to be controlled

## [Sensors]

Specific hardware may have specific needs with respect to kernel configuration. See [lm_sensors](https://wiki.gentoo.org/wiki/Lm_sensors "Lm sensors") for generic details.

** Note**\
For some newer ASUS motherboards the nct6775 driver needs to be manualy set to id=0xd420 (usually enabled by `CONFIG_SENSORS_NCT6775`) for fan sensors and controls to appear.

## [Fans]

Fans have 2, 3, or 4 wires:

1.  ground
2.  fan voltage
3.  tacho
4.  PWM

\
Fans with 2 or 3 wires may have voltage regulation: higher voltage (typically up to 12 Volt) results in higher rotation per minute (RPM). Fans with 4 wires are controlled through pulse width modulation (PWM), in theory a more efficient way of controlling the fan speed. The third wire provides feedback on the actual RPM of the fan.

## [External resources]

-   [What is PWM and how does it work?](https://www.ekwb.com/blog/what-is-pwm-and-how-does-it-work/)