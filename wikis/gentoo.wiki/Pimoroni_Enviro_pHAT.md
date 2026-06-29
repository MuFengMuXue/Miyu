Enviro pHAT by Pimonori is a small and handy addition to Raspberry Pi versions 2, 3 and 4 as well as compact Raspberry Pi Zero. It features several sensors to measure various \"environmental\" variables such as temperature, pressure, light level and colour, 3-axis motion, compass heading, and input voltage^[\[1\]](#cite_note-1)^. Currently, this version is discontinued and [Enviro](https://shop.pimoroni.com/products/enviro) (which is a pHat too, technically) is suggested as more advanced replacement.

## Contents

-   [[1] [Overview]](#Overview)
-   [[2] [Hardware and config.txt]](#Hardware_and_config.txt)
-   [[3] [Configuring the kernel]](#Configuring_the_kernel)
-   [[4] [UDEV configuration]](#UDEV_configuration)
-   [[5] [Software installation]](#Software_installation)
-   [[6] [Further reading]](#Further_reading)
-   [[7] [References]](#References)

## [Overview]

Enviro pHAT is a HAT/pHAT board, which is connected to Raspberry Pi board via 40-pin GPIO header mount. Note that only difference between Hat and pHAT is that the latter has is designed especially to work Raspberry Pi Zero and fits its form factor. However, due to certain compatibility between the Raspberry Pi versions and revisions as well as other similar products (e.g. Orange, Banana Pi) it will work with them too. The pHat comes as a single board with separate pinout headers, which should be soldered prior to installation on Raspberry Pi board^[\[2\]](#cite_note-2)^. It uses 3 GPIO pins (#2,3,4) and 5V power and communicates over i2c interface^[\[3\]](#cite_note-3)^. To be mounted properly, the board should be oriented in a way so it is mounted \"atop\" the Raspberry Pi. To read the pHAT sensors one can use dedicated [python library](https://github.com/pimoroni/enviro-phat) or [[[dev-libs/pigpio]](https://packages.gentoo.org/packages/dev-libs/pigpio)[]] and [[[sys-apps/i2c-tools]](https://packages.gentoo.org/packages/sys-apps/i2c-tools)[]] packages for a direct access to the GPIO pins . The following instructions are tested on Raspberry Pi 2 Model B and Enviro pHAT. Modern Enviro (not tested due to the lack of equipment) will require different python library, however, general approach would be the same.

Installation consists of the following steps:

1.  enabling hardware configuration in [/boot/config.txt],
2.  checking kernel configuration and modules,
3.  UDEV configuration,
4.  software installation.

## [Hardware and config.txt]

The pHat communicates with Raspberry Pi via I2C interface, so it should be enabled in the [/boot/config.txt] file, used to configure interfaces and Pi itself on the boot. Add those lines in *addition* to the ones present:

[FILE] **`/boot/config.txt`**

    ## --- Enviro pHAT configuration ---
    ## enabling required interfaces
    dtparam=i2c_arm=on
    dtparam=i2c=on
    dtparam=i2c_arm_baudrate=100000

Last line sets the i2c speed with 100KHz ( default frequency) which can be changed if needed.

## [Configuring the kernel]

One needs essentially `i2c_dev` and `i2c_bcm2835` (and `i2c_bcmstb` on RPi 4) modules for I2C communication. Raspberry Pi kernel distribution^[\[4\]](#cite_note-4)^ already has necessary modules pre-compiled. Alternatively, using default kernel configuration `bcmrpi_defconfig`, `bcm2709_defconfig`, `bcm2711_defconfig` for the appropriate target will select necessary modules. Otherwise check if you have these modules selected.

[KERNEL] **Enabling appropriate modules**

    Device Drivers --->
      I2C support --->
        <M> I2C device interface
        I2C Hardware Bus support --->
            <M> Broadcom BCM2835 I2C controller
            <M> BRCM Settop/DSL I2C controller

While the `i2c_bcm2835` (and `i2c_bcmstb` on RPi 4) is normally loaded automatically during the boot, `i2c_dev` is not. Create a [/etc/modules-load.d/envirophat.conf] and add the module there:

`root `[`#`]`mkdir /etc/modules-load.d/`

`root `[`#`]`echo "i2c_dev" >> /etc/modules-load.d/envirophat.conf`

During the boot the modules the [modules] service will load it.

## [UDEV configuration]

When the [udev] service runs it populates /dev with existing devices, including [/dev/gpiomem] and [/dev/i2-\*] (normally, [/dev/i2-1]), which are the GPIO pins and i2c bus, which the Enviro pHat is connected to. Currently on Gentoo these devices are created with [root:root] ownership, however, it is more handy to change this policy so the devices are created with [gpio] and [i2c] groups, respectively, so the users can have access to them, given added to those groups.

`root `[`#`]`emerge acct-group/i2c acct-group/gpio`

`root `[`#`]`echo 'KERNEL=="i2c-[0-9]*", GROUP="i2c", MODE="0660"' >> /etc/udev/rules.d/60-i2c-tools.rules`

`root `[`#`]`echo 'KERNEL=="gpiomem", GROUP="gpio", MODE="0660"' >> /etc/udev/rules.d/60-gpiomem.rules`

`root `[`#`]`usermod -a -G i2c,gpio <your user>`

If the Enviro pHat is already installed on the Raspberry Pi board at this point, one can either simply reboot, or modprobe the modules and restart the udev.

`root `[`#`]`modprobe i2c_dev`

`root `[`#`]`/etc/init.d/udev restart`

Check if the devices are present and have correct permissions.

`root `[`#`]`ls /dev/i2* -al`

## [Software installation]

Install the [[[sys-apps/i2c-tools]](https://packages.gentoo.org/packages/sys-apps/i2c-tools)[]] to check whether pHat is detected via i2c.

`root `[`#`]`emerge sys-apps/i2c-tools`

`user `[`$`]`i2cdetect -y 1`

         0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
    00:                         -- -- -- -- -- -- -- --
    10: -- -- -- -- -- -- -- -- -- -- -- -- -- 1d -- --
    20: -- -- -- -- -- -- -- -- -- 29 -- -- -- -- -- --
    30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
    40: -- -- -- -- -- -- -- -- -- 49 -- -- -- -- -- --
    50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
    60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
    70: -- -- -- -- -- -- -- 77

There is an official python package used to interact with the Enviro pHat^[\[5\]](#cite_note-5)^, however it is not currently present in the main tree, so one may use [[[dev-python/pip]](https://packages.gentoo.org/packages/dev-python/pip)[]] to install them.

`root `[`#`]`emerge dev-python/pip`

Then, from the user added to the [i2c] and [gpio] groups in the previous section, install the required packages.

** Note**\
Currently (as of writing this page, Oct 2021) running just `pip install --user envirophat` will fail. The [smbus] package is not installed as a dependency and last stable version of [RPi.GPIO] fails with [[[dev-lang/python:3.9]](https://packages.gentoo.org/packages/dev-lang/python:3.9)[]], so alpha version should be manually installed instead.

`user `[`$`]`pip install --user RPi.GPIO==0.7.1a4`

`user `[`$`]`pip install --user smbus`

`user `[`$`]`pip install --user envirophat`

If the `import envirophat` works in [python] then, everything is configured correctly and works. E.g. create small python script file:

[FILE] **`~/env_pHat_check.py`**

    import envirophat
    print("Temperature reading is %2.2f°C" %(envirophat.weather.temperature()))

and check if the sensor reads the temperature outside the pHAT.

`user `[`$`]`python ~/env_pHat_check.py`

    Temperature reading is 27.30°C

** Note**\
The last line is an example output, your temperature will be different!

If it worked, then everything is set up for non-root user usage.

## [Further reading]

Checkout more for examples at official getting started page^[\[6\]](#cite_note-6)^ and an example of more depth-in applications ^[\[7\]](#cite_note-7)^.

## [References]

1.  [[[↑](#cite_ref-1)] [[\[1\]](https://shop.pimoroni.com/products/enviro-phat) Enviro pHAT in Pimonori shop.]]
2.  [[[↑](#cite_ref-2)] [[\[2\]](https://learn.pimoroni.com/article/soldering-phats) Some soldering instructions.]]
3.  [[[↑](#cite_ref-3)] [[\[3\]](https://pinout.xyz/pinout/enviro_phat) Pinout of the Enviro pHat.]]
4.  [[[↑](#cite_ref-4)] [[\[4\]](https://github.com/raspberrypi/firmware) Official Raspberry Pi repository containing pre-compiled binaries of the kernel and modules and more.]]
5.  [[[↑](#cite_ref-5)] [[\[5\]](https://github.com/pimoroni/enviro-phat) Github repository of the official python library.]]
6.  [[[↑](#cite_ref-6)] [[\[6\]](https://learn.pimoroni.com/article/getting-started-with-enviro-phat) Official getting started page]]
7.  [[[↑](#cite_ref-7)] [[\[7\]](https://medium.com/initial-state/tutorial-review-enviro-phat-for-raspberry-pi-4cd6d8c63441) Temperature Streamer/Logger example]]