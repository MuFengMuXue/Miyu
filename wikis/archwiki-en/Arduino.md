# Arduino

Arduino is an open-source electronics prototyping platform based on flexible, easy-to-use hardware and software. It is intended for artists, designers, hobbyists, and anyone interested in creating interactive objects or environments.

Once hooked up and configured the user may perform read/write tasks over the established serial connection. Examples are interfacing over UART using a serial monitoring program, or programming the microcontroller. Writing, compiling and uploading your code is facilitated by using the official Arduino IDE, which is available in the official repositories. Equally the user may use a compiler and programmer of choice to program the microcontroller.

## Installation
* Install  for the official CLI.
* Install  for the official GUI.
* Enable user access to the device.
* You may need to load the  module.

## Arduino IDE 1.x
The following section only applies to the 1.x version of the IDE. However, it may be possible to adapt some of this for the new IDE.

## AVR Boards
To use AVR boards such as the Arduino Uno you can install  optionally to use Arch Linux upstream avr-gcc instead of the bundled older avr-core. If you still want to use the older arduino-core you need to install it in the board manager. You can always switch between the different cores in the Tools > Board menu.

## Pinoccio Scout
Pinoccio Scouts can also be programmed using the Arduino IDE. Instructions can be found here.
Alternative you can install .

## Intel Galileo
To use the Intel Galileo boards with Arch Linux install the Arduino IDE and download the Galileo tools package via Tools > Board > Boards Manager.
To fix the installation you can follow this github post.

## Arduino IDE 1.x or 2.x
These steps should be valid for both versions of the IDE.

## AVR Boards
AVR boards are automatically installed by the 2.x release of the IDE however on both the 1.x and 2.x releases the AVR boards can be managed from the boards manager.

## SparkFun
To use SparkFun boards such as the Pro Micro you need to download their board definitions. More information here and here.

## RedBear Duo
You might need to install  or you will get an error about missing crc32.

## Configuration
Most Arduino boards have a USB port which can be used for establishing a serial connection. This serial connection allows the user to program the board. The main microcontroller of most Arduinos, however, does not have a USB interface built-in. Hence, the board is usually equipped with a USB to serial chip in between the main microcontroller and the USB port.

To achieve the serial connection over USB, most genuine Arduino boards are equipped with another ATmega microcontroller (e.g. ATmega16U2) or an FTDI USB UART converter (e.g. FT232RL). Both of these chips register themselves over USB as an ACM device, and as such, Linux will use the  module. The Arduino will then show up as .

Non-genuine Arduino boards cheap out on the interfacing chip. They are typically equipped with a Chinese WCH CH340x or a counterfeit of the aforementioned models. The CH340x exposes itself as a proprietary UART over USB device. Here the  module is used, making such Arduinos show up as . This naming pattern may be customized by altering udev rules.

Some boards may be equipped with a main microcontroller which does expose a native USB interface by itself. Whether the board has a dedicated interface chip or not, genuine boards will come out of the factory with a proper boot loader preinstalled. Such boot loaders automatically establish a serial connection over USB once they are connected.

## Accessing serial
For the boards that expose a UART over USB, it is  necessary to allow read/write access to the serial port to usersAs explained in Udev#Allowing regular users to use devices, create a file containing:

Reload the udev rules and replug the Arduino device. Before uploading to the Arduino, be sure to set the correct serial port, board, and processor from the Tools menu in 1.x and the Select board option (located at the top of the IDE) in 2.x.

## Communicating with the device
## Using the CLI
More documentation about the  can be found at the [https://arduino.github.io/arduino-cli/1.4/getting-started/ official arduino-cli website.

Start with listing the boards connected to your computer:
 $ arduino-cli board list

 # example output
 Port         Protocol Type              Board Name              FQBN                 Core
 /dev/ttyUSB0 serial   Serial Port (USB) Arduino/Genuino MKR1000 arduino:samd:mkr1000 arduino:samd
 /dev/ttyUSB1 serial   Serial Port (USB) Unknown

Then, after creating a sketch, compile it with:
 $ arduino-cli compile --fqbn  MySketch

Finally, upload the compiled sketch with:
 $ arduino-cli upload -p  --fqbn  MySketch

If the upload command fails with insufficient permissions, make sure that regular users have read/write access to USB ports. If it fails with DEVICE_BUSY, make sure that no other program like  is currently using the device.

## stty
Preparing:

 # stty -F /dev/ttyACM0 cs8 9600 ignbrk -brkint -imaxbel -opost -onlcr -isig -icanon -iexten -echo -echoe -echok -echoctl -echoke noflsh -ixon -crtscts

Sending commands through Terminal without new line after command

 # echo -n "Hello World" > /dev/ttyACM0

Reading what your Arduino has to tell you:

 $ cat /dev/ttyACM0

## Arduino-Builder
You can also build Arduino sketches with the  command line tool. In order to use the provided  with upstream  and  you need to create a small settings file:

{{hc|head=build.options.json |2=
{
    "fqbn": "archlinux-arduino:avr:uno",
    "hardwareFolders": "/usr/share/arduino/hardware",
    "toolsFolders": "/usr/bin"
}
}}

Compile a sketch with:

 $ arduino-builder -build-options-file build.options.json blink.ino

Or pass all options via command line:

 $ arduino-builder -fqbn archlinux-arduino:avr:uno -hardware /usr/share/arduino/hardware -tools /usr/bin blink.ino

## Alternatives to the IDE
## Arduino-CMake
Using Arduino-CMake-Toolchain and CMake you can build Arduino firmware from the command line using multiple build systems. CMake lets you generate the build system that fits your needs, using the tools you like. It can generate any type of build system, from simple Makefiles, to complete projects for Eclipse, Visual Studio, XCode, etc.

Requirements: , , , , , .

## Makefile
Instead of using the Arduino IDE it is possible to use another editor and a Makefile.

Set up a directory to program your Arduino and copy the Makefile into this directory. A copy of the Makefile can be obtained from this GitHub template.
You will have to modify this a little bit to reflect your settings. The makefile should be pretty self explanatory. Here are some lines you may have to edit.

 PORT = usually /dev/ttyUSBx, where x is the usb serial port your arduino is plugged into
 TARGET = your sketch's name
 ARDUINO = /usr/share/arduino/lib/targets/arduino

Depending on which library functions you call in your sketch, you may need to compile parts of the library. To do that you need to edit your SRC and CXXSRC to include the required libraries.

Now you should be able to  to your board to execute your sketch.

## Arduino-mk
arduino-mk is another alternative Makefile approach. It allows users to have a local Makefile that includes Arduino.mk.

For Arduino 1.5, try the following local Makefile (because Arduino 1.5's library directory structure is slightly different):

 ARDUINO_DIR = /usr/share/arduino
 ARDMK_DIR = /usr/share/arduino
 AVR_TOOLS_DIR = /usr
 AVRDUDE_CONF = /etc/avrdude.conf
 ARDUINO_CORE_PATH = /usr/share/arduino/hardware/archlinux-arduino/avr/cores/arduino
 ARDUINO_PLATFORM_LIB_PATH = /usr/share/arduino/hardware/archlinux-arduino/avr/libraries
 BOARDS_TXT = /usr/share/arduino/hardware/archlinux-arduino/avr/boards.txt
 ARDUINO_VAR_PATH = /usr/share/arduino/hardware/archlinux-arduino/avr/variants
 BOOTLOADER_PARENT = /usr/share/arduino/hardware/archlinux-arduino/avr/bootloaders

 BOARD_TAG    = uno
 ARDUINO_LIBS =

 include /usr/share/arduino/Arduino.mk

In some cases you could need to install  and .

## Scons
Using scons together with arscons it is very easy to use to compile and upload Arduino projects from the command line. Scons is based on python and you will need python-pyserial to use the serial interface. Install , , and .

That will get the dependencies you need too. Create project directory (eg. test), then create an arduino project file in your new directory. Use the same name as the directory and add .ino (eg. test.ino). Get the SConstruct script from arscons and put it in your directory. Have a peek in it and, if necessary, edit it. It is a python script. Edit your project as you please, then run

 $ scons                # This will build the project
 $ scons upload         # This will upload the project to your Arduino

## PlatformIO
PlatformIO is a python tool to build and upload sketches for multiple Hardware Platforms, at the moment of writing these are Arduino/AVR based boards, TI MSP430 and TI TM4C12x Boards. In the near future the author plans to add a library function that allows to search and include libraries directly from GitHub.

## Installation
Install the  package.

## Usage
The following is based on the official PlatformIO quickstart guide, which shows how to create and upload an example project.

Create a new directory for the platformio project and enter the directory.
Then run the following command to initialize the project for a specific board (here the megaatmega2560):

 $ pio project init --board megaatmega2560

This downloads the tool chain and dependencies, and creates :

Create and add code to main.cpp in the src/ folder such as the example code in the quickstart guide.

Then compile the code and upload it to the devices specified in platformio.ini:
 $ pio run
 $ pio run --target upload

## Emacs
It is possible to configure Emacs as IDE.

Install the package  in order to enable the  in emacs.

Add to the init script:

You can compile and upload the sketches using  (see above) with  .

Main resource: here.

## Troubleshooting
## Consistent naming of Arduino devices
If you have more than one Arduino you may have noticed that they names  are assigned in the order of connection. In the IDE this is not so much of a problem, but when you have programmed your own software to communicate with an Arduino project in the background this can be annoying. Use the following udev rules to assign static symlinks to your Arduino's:

{{hc|/etc/udev/rules.d/52-arduino.rules|
SUBSYSTEMS=="usb", KERNEL=="ttyUSBATTRS{idVendor}=="0403", ATTRS{idProduct}=="6001", SYMLINK+="sensors/ftdi_%s{serial}"
}}

Your Arduino's will be available under names like . If you want you can also assign more meaningful names to several devices like this:

{{hc|/etc/udev/rules.d/52-arduino.rules|
SUBSYSTEMS=="usb", KERNEL=="ttyUSB[0-9*", ATTRS{idVendor}=="0403", ATTRS{idProduct}=="6001", ATTRS{serial}=="A700dzaF", SYMLINK+="arduino/nano"
}}

which will create a symlink in  to the device with the specified serialnumber.
You do need to unplug and replug your Arduino for this to take effect or run

 # udevadm trigger

Common / pairs can be found in  in the distribution package. Note that some of them (notably FTDI ones) are not unique to the Arduino platform. Using  attribute is a good way to distinguish between various devices.

## Error opening serial port
You may see the serial port initially when the IDE starts, but the TX/RX leds do nothing when uploading. You may have previously changed the baudrate in the serial monitor to something it does not like. Edit  so that  is a different speed, like 115200.

## Working with Uno/Mega2560
The Arduino Uno and Mega2560 have an onboard USB interface (an Atmel 8U2) that accepts serial data, so they are accessed through  created by the cdc-acm kernel module when it is plugged in.

The 8U2 firmware may need an update to ease serial communications. See for more details and reply #11 for a fix. The original arduino bbs, where you can find an image explaining how to get your Uno into DFU, is now in a read-only state. If you do not have an account to view the image, see [https://www.scribd.com/doc/45913857/Arduino-UNO.

You can perform a general function test of the Uno by putting it in loopback mode and typing characters into the arduino serial monitor at 115200 baud. It should echo the characters back to you. To put it in loopback, short pins 0 -> 1 on the digital side and either hold the reset button or short the GND -> RESET pins while you type.

## Not recognizing USB port with Mega2560 cheap Chinese clones
Try installing its driver: .

## Fails to upload: programmer is not responding
Changing processor setting from  to  (See Tools->Processor in Arduino IDE) may help with upload failures.

## Serial port conflict with brltty
If the serial port for the arduino is not visible at , and the journal contains the following when the device is connected:

 usb 3-1: usbfs: interface 0 claimed by ch341 while 'brltty' sets config #1
 ch341-uart ttyUSB0: ch341-uart converter now disconnected from ttyUSB0

Then you may need to uninstall the  package. See for more details.

## Failure to upload with Nano RP2040 Connect
If your upload fails with:

 Failed uploading: uploading error: exit status 1

you have skipped #Accessing serial: follow its directions to allow read/write access to the serial port to users.
