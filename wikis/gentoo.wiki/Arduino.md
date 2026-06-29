**Resources**

[[]][Home](https://www.arduino.cc/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Arduino "wikipedia:Arduino")

[[]][Package information](https://packages.gentoo.org/packages/dev-embedded/arduino)

**Arduino** is an open source development platform for microcontrollers based on [Atmel AVR](https://en.wikipedia.org/wiki/Atmel_AVR "wikipedia:Atmel AVR") microprocessors.

In addition to official and clone Arduino boards, the environment supports other microprocessors including: [ATtiny13](https://github.com/MCUdude/MicroCore), [STM32](https://www.stm32duino.com/viewtopic.php?f=42&t=97&sid=1f8f263f8c8283920499c949f059bad4), and [nRF52 SoCs](https://www.nordicsemi.com/Products/nRF52-Series-SoC).

This article describes the process of configuring a Gentoo system to connect to an Arduino, the installation of a cross-development toolchain, and the installation of the [Arduino IDE](https://en.wikipedia.org/wiki/Arduino_IDE "wikipedia:Arduino IDE").

## Contents

-   [[1] [Prepare the kernel for USB connection]](#Prepare_the_kernel_for_USB_connection)
    -   [[1.1] [Arduino NG (FTDI)]](#Arduino_NG_.28FTDI.29)
    -   [[1.2] [Arduino MEGA, UNO, Atmega8U2, Atmega16U2, Atmega32U4, Zero (CDC ACM)]](#Arduino_MEGA.2C_UNO.2C_Atmega8U2.2C_Atmega16U2.2C_Atmega32U4.2C_Zero_.28CDC_ACM.29)
    -   [[1.3] [Arduino NANO (CH340)]](#Arduino_NANO_.28CH340.29)
    -   [[1.4] [Arduino ESP32 (CP210)]](#Arduino_ESP32_.28CP210.29)
-   [[2] [Validate connectivity]](#Validate_connectivity)
-   [[3] [Grant access to non-root users]](#Grant_access_to_non-root_users)
-   [[4] [Prepare the toolchain]](#Prepare_the_toolchain)
    -   [[4.1] [Recommended: Install the toolchain using crossdev]](#Recommended:_Install_the_toolchain_using_crossdev)
        -   [[4.1.1] [Installing crossdev]](#Installing_crossdev)
        -   [[4.1.2] [Create an ebuild repository locally]](#Create_an_ebuild_repository_locally)
        -   [[4.1.3] [Build and install the toolchain]](#Build_and_install_the_toolchain)
            -   [[4.1.3.1] [AVR (Arduino/Genuino/ATmicro/ATmega/etc.)]](#AVR_.28Arduino.2FGenuino.2FATmicro.2FATmega.2Fetc..29)
            -   [[4.1.3.2] [ARM (STM32/GD32/etc.)]](#ARM_.28STM32.2FGD32.2Fetc..29)
            -   [[4.1.3.3] [Troubleshooting]](#Troubleshooting)
    -   [[4.2] [Discouraged: Install non-Gentoo toolchain]](#Discouraged:_Install_non-Gentoo_toolchain)
-   [[5] [Installing the Arduino IDE]](#Installing_the_Arduino_IDE)
    -   [[5.1] [Official sources]](#Official_sources)
    -   [[5.2] [Official download]](#Official_download)
-   [[6] [Configuring the Arduino IDE]](#Configuring_the_Arduino_IDE)
-   [[7] [Using Eclipse IDE]](#Using_Eclipse_IDE)
    -   [[7.1] [Arduino Eclipse Extension]](#Arduino_Eclipse_Extension)
    -   [[7.2] [AVR Eclipse Plugin]](#AVR_Eclipse_Plugin)
-   [[8] [Using Meson]](#Using_Meson)
-   [[9] [Tips and Tricks]](#Tips_and_Tricks)
    -   [[9.1] [udev rules]](#udev_rules)
        -   [[9.1.1] [Arduino NG]](#Arduino_NG)
        -   [[9.1.2] [Arduino MEGA]](#Arduino_MEGA)
-   [[10] [Troubleshooting]](#Troubleshooting_2)
    -   [[10.1] [Deprecated items in avr-libc v1.8.0 and above (and Mega 2560)]](#Deprecated_items_in_avr-libc_v1.8.0_and_above_.28and_Mega_2560.29)
    -   [[10.2] [Insufficient permissions for /dev/ttyACM0]](#Insufficient_permissions_for_.2Fdev.2FttyACM0)
    -   [[10.3] [Missing arduino-builder]](#Missing_arduino-builder)
    -   [[10.4] [Gray window, Arduino IDE not resizing with WM, menus immediately closing]](#Gray_window.2C_Arduino_IDE_not_resizing_with_WM.2C_menus_immediately_closing)
    -   [[10.5] [Arduino IDE fail to compile sketches due to missing \--tools parameter]](#Arduino_IDE_fail_to_compile_sketches_due_to_missing_--tools_parameter)
    -   [[10.6] [Arduino IDE fail to compile sketches due to cc1plus error]](#Arduino_IDE_fail_to_compile_sketches_due_to_cc1plus_error)
-   [[11] [See also]](#See_also)
-   [[12] [External resources]](#External_resources)

## [Prepare the kernel for USB connection]

Arduino boards are connected to a computer via [USB](https://wiki.gentoo.org/wiki/USB "USB"). With this connection it is possible to send compiled binaries \"sketches\" to the Arduino\'s microprocessor and receive debug messages from the board during execution. Each model of board features a different USB interface chip; consult the board\'s documentation if unsure about the USB interface in use. Check dmesg output as well for hints about the USB interface.

If [in-system programming](https://en.wikipedia.org/wiki/In-system_programming "wikipedia:In-system programming") with an external programmer is preferred the Arduino IDE is not required for programming the device, however it may still be required to receive debugging output.

In order to support Arduino devices the appropriate [kernel](https://wiki.gentoo.org/wiki/Kernel "Kernel") driver must be enabled; it may be built into the kernel or as a module.

### [][Arduino NG (FTDI)]

[KERNEL] **FTDI interface**

     Device Drivers  --->
       [*] USB support Search for <code>CONFIG_USB</code> to find this item. --->
         <*> USB Serial Converter support Search for <code>CONFIG_USB_SERIAL</code> to find this item. --->
           <*> USB FTDI Single Port Serial Driver Search for <code>CONFIG_USB_SERIAL_FTDI_SIO</code> to find this item.

### [][Arduino MEGA, UNO, Atmega8U2, Atmega16U2, Atmega32U4, Zero ([CDC ACM](https://wiki.openmoko.org/wiki/USB_CDC_ACM))]

[KERNEL] **CDC ACM**

     Device Drivers  --->
       [*] USB support Search for <code>CONFIG_USB</code> to find this item. --->
         <*> USB Modem (CDC ACM) support Search for <code>CONFIG_USB_ACM</code> to find this item.

### [][Arduino NANO (CH340)]

This series of boards has included a range of serial converter chips, however the most commonly used is the [CH340](https://www.wch.cn/product/CH340.html).

[KERNEL] **CH340 serial converter**

     Device Drivers  --->
       [*] USB support Search for <code>CONFIG_USB</code> to find this item. --->
         <*> USB Serial Converter support Search for <code>CONFIG_USB_SERIAL</code> to find this item. --->
           <*> USB Winchiphead CH341 Single Port Serial Driver Search for <code>CONFIG_USB_SERIAL_CH341</code> to find this item.

### [][Arduino ESP32 (CP210)]

[KERNEL] **CH340 serial converter**

     Device Drivers  --->
       [*] USB support Search for <code>CONFIG_USB</code> to find this item. --->
         <*> USB Serial Converter support Search for <code>CONFIG_USB_SERIAL</code> to find this item. --->
           <*> USB CP210x family of UART Bridge Controllers Search for <code>CONFIG_USB_SERIAL_CP210X</code> to find this item.

## [Validate connectivity]

After support for the device has been enabled, and the computer rebooted if necessary, connectivity to the board must be validated: connect the Arduino to an available USB port then check for messages in the kernel ring buffer:

For an Arduino NG:

`root `[`#`]`dmesg`

    usb 5-4: FTDI USB Serial Device converter now attached to ttyUSB0

For an Arduino MEGA:

`root `[`#`]`dmesg`

    cdc_acm 5-4:1.0: ttyACM0: USB ACM device

For an Arduino ESP32:

`root `[`#`]`dmesg`

    usb 3-11: cp210x converter now attached to ttyUSB0

## [Grant access to non-root users]

Any non-root user that wishes to connect to the device should be added to the `dialout` group, as the device\'s file (e.g. [/dev/ttyACM0]) is owned by that group.

To add Larry to the group run the following command:

`root `[`#`]`gpasswd -a larry dialout`

** Note**\
Larry will need to log off and back on before permissions granted by the group will take effect, until then he will be unable to access the device

## [Prepare the toolchain]

As Atmel AVR microprocessors require different compiled output from the development platform (most often [x86-64](https://wiki.gentoo.org/wiki/AMD64 "AMD64")) a cross development [toolchain](https://en.wikipedia.org/wiki/GNU_toolchain "wikipedia:GNU toolchain") must be installed.

### [Recommended: Install the toolchain using crossdev]

This section provides condensed instructions for creating a cross-compiler, originally found in the [Embedded Handbook](https://wiki.gentoo.org/wiki/Embedded_Handbook/General/Creating_a_cross-compiler "Embedded Handbook/General/Creating a cross-compiler"). Consult the handbook for an introduction to [crossdev](https://wiki.gentoo.org/wiki/Crossdev "Crossdev") and its operation.

#### [Installing crossdev]

Install [[[sys-devel/crossdev]](https://packages.gentoo.org/packages/sys-devel/crossdev)[]]:

`root `[`#`]`emerge --ask sys-devel/crossdev`

** Important**\
If issues are encountered installing crossdev, try unmasking a more recent (unstable) version.

#### [Create an ebuild repository locally]

Before the local toolchain can be built, an ebuild repository called `crossdev` must be created locally.

** Note**\
The `crossdev` ebuild repository will be automatically selected by the *crossdev* tool to build packages for all crossdev-targeted platforms --- creating this ebuild repository will ensure that all of the *crossdev* built packages remain completely separate from native packages on the development system.

** Note**\
These commands are a condensed form of the instructions available on the [creating an ebuild repository](https://wiki.gentoo.org/wiki/Creating_an_ebuild_repository#Crossdev "Creating an ebuild repository") article, which has more detailed information.

`root `[`#`]`mkdir -p /var/db/repos/portage-crossdev/ `

`root `[`#`]`echo 'crossdev' > /var/db/repos/portage-crossdev/profiles/repo_name `

`root `[`#`]`echo 'masters = gentoo' > /var/db/repos/portage-crossdev/metadata/layout.conf `

`root `[`#`]`chown -R portage:portage /var/db/repos/portage-crossdev `

If the [Gentoo ebuild repository](https://wiki.gentoo.org/wiki/Ebuild_repository#The_Gentoo_ebuild_repository "Ebuild repository") is synchronized using Git, or another method where Manifest files do not include ebuild checksums, Portage must be informed of this to prevent \"masked by: corruption\" errors:

`root `[`#`]`echo 'thin-manifests = true' >> /var/db/repos/portage-crossdev/metadata/layout.conf `

Instruct [Portage](https://wiki.gentoo.org/wiki/Portage "Portage") and *crossdev* to use this ebuild repository:

[FILE] **`/etc/portage/repos.conf/crossdev.conf`**

    [crossdev]
    location = /var/db/repos/portage-crossdev
    priority = 10
    masters = gentoo
    auto-sync = no

#### [Build and install the toolchain]

Select an appropriate toolchain for the targeted architecture (the board in use); Most Arduino users will only want the AVR toolchain.

##### [][AVR (Arduino/Genuino/ATmicro/ATmega/etc.)]

Build and install the AVR toolchain with this command:

`root `[`#`]`crossdev -s4 --stable --portage --verbose --target avr`

##### [][ARM (STM32/GD32/etc.)]

Build and install the ARM toolchain with this command:

`root `[`#`]`crossdev -s4 --stable --portage --verbose --target arm`

##### [Troubleshooting]

If issues are encountered when crossdev is compiling the [gcc](https://wiki.gentoo.org/wiki/C "C") stages, try:

`root `[`#`]`USE="-openmp -hardened -sanitize -vtv" crossdev -s4 --stable --portage --verbose --target avr`

### [Discouraged: Install non-Gentoo toolchain]

The vendor-provided [Atmel AVR toolchain](https://www.microchip.com/en-us/development-tool/atmel-avr-toolchain-for-linux) is available for use, however it is untested.

An (old) article describing the use of the precompiled Debian toolchain is available [here](https://blog.coldtobi.de/index.php?op=ViewArticle&articleId=21&blogId=1).

## [Installing the Arduino IDE]

### [Official sources]

The legacy 1.x [Arduino IDE](https://en.wikipedia.org/wiki/Arduino_IDE "wikipedia:Arduino IDE") is available in the official Gentoo repository:

`root `[`#`]`emerge --ask dev-embedded/arduino`

### [Official download]

-   **Benefit**: Current 2.x version.
-   **Drawback**: Not packaged for Gentoo. All or nothing. Not built from source. Requires manual updates.

[Official tarball downloads](https://www.arduino.cc/en/Main/Software) (including beta and hourly versions).

## [Configuring the Arduino IDE]

The Arduino IDE will create a default sketch directory on first launch, located at [\~/Arduino]. This location can be changed within the Arduino IDE\'s preferences.

If targeting any platforms that aren\'t included in the default distribution (E.g. ATtiny processors, or ARM processors such as the STM32 or GD32) new Arduino platform implementations (also known as \"cores\") must be installed. Cores can then be associated with board definitions.

Some example *cores*:

-   **ARM**
    -   **STM32/GD32**: [stm32duino](https://www.stm32duino.com/)
    -   **[Nordic Semiconductor](https://en.wikipedia.org/wiki/Nordic_Semiconductor "wikipedia:Nordic Semiconductor")**
        -   **[NRF51](https://en.wikipedia.org/wiki/NRF51_Series "wikipedia:NRF51 Series")/52**: [sandeepmistry/arduino-nRF5](https://github.com/sandeepmistry/arduino-nRF5)
-   **Atmel AVR**
    -   **ATtiny Series**
        -   **ATtiny13**: [MCUdude/MicroCore](https://github.com/MCUdude/MicroCore)
        -   **ATtiny24/25/44/45/85**: [damellis/attiny](https://github.com/damellis/attiny)
    -   **ATmega Series**
        -   **ATmega64/128/640/1280/1281/2560/2561**: [MCUdude/MegaCore](https://github.com/MCUdude/MegaCore)
        -   **ATmega16/32/164/324/644/1284/8535**: [MCUdude/MightyCore](https://github.com/MCUdude/MightyCore)
-   **XTensa** (see also [esp-open-sdk](https://github.com/pfalcon/esp-open-sdk))
    -   **Espressif**
        -   **ESP8266**: [esp8266/Arduino](https://github.com/esp8266/Arduino) (see also [esp8266.com](https://www.esp8266.com/))
        -   **ESP31B/32**: [espressif/arduino-esp32](https://github.com/espressif/arduino-esp32) (older [ESP31B support](https://github.com/me-no-dev/ESP31B))

## [Using Eclipse IDE]

Within the [Eclipse IDE](https://wiki.gentoo.org/wiki/Eclipse "Eclipse") there are two available plugins for Arduino development. Plugins can be installed via user-provided update sites: Add the required site to Eclipse via *Menu/Help/Software-updates/Add-site*.

** Note**\
Installation of the Eclipse IDE is out of scope for this article. Please see [Eclipse](https://wiki.gentoo.org/wiki/Eclipse "Eclipse") for that topic.

### [Arduino Eclipse Extension]

The **Arduino Eclipse Extension** is a free Eclipse IDE plugin for Arduino projects developed by Jantje. It depends on the installation of Arduino IDE.

Use the update site \"[https://www.baeyens.it/eclipse/update](https://www.baeyens.it/eclipse/update)\" for the installation of a plugin version which is compatible with Arduino 1.0.4 and Eclipse Helios and Indigo.

Use the update site \"[https://www.baeyens.it/eclipse/V2](https://www.baeyens.it/eclipse/V2)\" for installation of a plugin version which is compatible with Arduino 1.5.x and Eclipse Juno.

### [AVR Eclipse Plugin]

The **AVR Eclipse Plugin** is a free Eclipse IDE plugin used to develop for boards with AVR Atmel microprocessors. The plugin is not designed for Arduino boards, but can used with them and It is not necessary to install the Arduino IDE to use this plugin. More information can be found on the [official wiki](http://avr-eclipse.sourceforge.net/wiki/index.php/The_AVR_Eclipse_Plugin).

Use the update site \"[http://avr-eclipse.sourceforge.net/updatesite/](http://avr-eclipse.sourceforge.net/updatesite/)\" to install the plugin.

** Warning**\
The *Arduino Eclipse Extension V1* contains the *AVR Eclipse Plugin* as such it is not possible to have both installed simultaneously.

** Note**\
The *Arduino Eclipse Extension V2* does not contain the plugin, so the *AVR Eclipse Plugin* may be installed alongside the *Arduino Eclipse Extension*.

## [Using Meson]

Meson\'s support for cross compilation and the WrapDB entry arduinocore-avr [\[1\]](https://mesonbuild.com/Wrapdb-projects.html) can be used to compile and upload (with dev-embedded/avrdude) sketches as demonstrated by the mesonarduino project [\[2\]](https://github.com/jpakkane/mesonarduino).

## [Tips and Tricks]

### [udev rules]

A [udev](https://wiki.gentoo.org/wiki/Udev "Udev") rule can be used to create symlinks such as [/dev/arduino] when the board is connected. This is particularly useful in cases where more than one Arduino board will be connected simultaneously.

#### [Arduino NG]

Create the file [/etc/udev/rules.d/12-mikrocontroller.rules] and add following line to the file:

[FILE] **`/etc/udev/rules.d/12-mikrocontroller.rules`**

    SUBSYSTEMS=="usb", ATTRS=="FT232R USB UART", ATTRS=="FTDI", NAME="ttyUSB%n", SYMLINK+="arduino"

#### [Arduino MEGA]

Create the file [/etc/udev/rules.d/12-mikrocontroller.rules] and add following line to the file:

[FILE] **`/etc/udev/rules.d/12-mikrocontroller.rules`**

    SUBSYSTEMS=="usb", ATTRS=="Arduino Mega 2560", ATTRS=="Arduino (www.arduino.cc)", NAME="ttyACM%n", SYMLINK+="arduino"

## [Troubleshooting]

### [][Deprecated items in avr-libc v1.8.0 and above (and Mega 2560)]

If the following message is received, a known [compatibility issue](https://arduino.cc/forum/index.php/topic,92364.0.html) has been encountered.

[CODE] **Errors during compilation**

    /usr/share/arduino/hardware/arduino/cores/arduino/HardwareSerial.cpp:107:41: error: attempt to use poisoned "SIG_USART0_RECV"
    /usr/share/arduino/hardware/arduino/cores/arduino/HardwareSerial.cpp:117:15: error: attempt to use poisoned "SIG_USART0_RECV"
    /usr/share/arduino/hardware/arduino/cores/arduino/HardwareSerial.cpp:161:15: error: attempt to use poisoned "SIG_USART0_RECV"
    /usr/share/arduino/hardware/arduino/cores/arduino/HardwareSerial.cpp:178:15: error: attempt to use poisoned "SIG_USART0_RECV"
    /usr/share/arduino/hardware/arduino/cores/arduino/HardwareSerial.cpp:195:15: error: attempt to use poisoned "SIG_USART0_RECV"

To resolve this issue modify [Arduino.h] to the following:

[FILE] **`/usr/share/arduino/hardware/arduino/cores/arduino/Arduino.h`**

    #ifndef Arduino_h
    #define Arduino_h
    //start: fix the compatibility issue
    #define __AVR_LIBC_DEPRECATED_ENABLE__ 1
    //end: fix the compatibility issue
    #include <stdlib.h>
    ...

### [][Insufficient permissions for /dev/ttyACM0]

[CODE] **Error when accessing serial port**

    can't open device "/dev/ttyACM0": Permission denied

Users attempting to access the serial port in question must be a part of the `dialout` group.

Add a user to the `dialout` group by issuing:

`root `[`#`]`gpasswd -a larry dialout`

** Note**\
Larry will need to log off and back on before permissions granted by the group will take effect, until then he will be unable to access the device

### [Missing arduino-builder]

If the following error message is encountered, the arduino-builder binary is not in the location that the Arduino IDE expects.

[CODE] **No such file or catalogue**

    Caused by: java.io.IOException: Cannot run program "/usr/share/arduino/arduino-builder": error=2, No such file or directory

Run the following command to symlink the existing arduino-builder binary:

`root `[`#`]`ln -sf /usr/bin/arduino-builder /usr/share/arduino/arduino-builder`

### [][Gray window, Arduino IDE not resizing with WM, menus immediately closing]

If encountering weird window behavior with the Arduino IDE on the window manager:

`user `[`$`]`export _JAVA_AWT_WM_NONREPARENTING=1`

### [Arduino IDE fail to compile sketches due to missing \--tools parameter]

If the following message is received, a [known bug](https://bugs.archlinux.org/task/52377) has been encountered:

[CODE] **Parameter \'tools\' is mandatory**

    Parameter 'tools' is mandatory
    Usage of /usr/share/arduino/arduino-builder:
      -build-cache string
          builds of 'core.a' are saved into this folder to be cached and reused
      -build-options-file string
    ..........
    Error compiling for board Arduino Uno.

Create the [/usr/share/arduino/tools-builder] directory to fix it:

`root `[`#`]`mkdir /usr/share/arduino/tools-builder`

### [Arduino IDE fail to compile sketches due to cc1plus error]

During a *core* installation a crosscompiler is searched, if not found arduino will download its own. The use of the downloaded crosscompiler will lead to following error message when trying to build the sketch:

[CODE] **cc1plus not found**

    xtensa-lx106-elf-g++: fatal error: cannot execute 'cc1plus': execvp: No such file or directory

Make sure that the *core* installation was started after all the steps of the [\"Prepare the toolchain\" section](https://wiki.gentoo.org/wiki/Arduino#Prepare_the_toolchain "Arduino") where successful. You may need to reinstall the *core*.

## [See also]

-   [Embedded Handbook](https://wiki.gentoo.org/wiki/Embedded_Handbook "Embedded Handbook") --- a collection of community maintained documents providing a consolidation of embedded and SoC knowledge for Gentoo.

## [External resources]

-   [Energia](https://energia.nu/) - For MSP430 support.
-   [Outdated guide for Arduino on Gentoo](https://playground.arduino.cc/linux/gentoo) (Arduino official hosted site).
-   [Arduino eclipse extension](https://www.baeyens.it/eclipse/) main site.