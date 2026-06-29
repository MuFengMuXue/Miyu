# AVR

AVR is a family of microcontrollers (MCUs) developed by Microchip Technology (former AVR). AVRs are especially common in hobbyist and educational embedded applications, popularized by Arduino project. This page deals with 8-bit series of these MCUs.

## Toolchain
Install  to get toolchain and GNU compiler.

## Programmers
To flash compiled firmware to the AVR chip you will need programmer and software to rule it. Most popular programmers are USBasp, AVRISP mkII, Atmel-ICE and STK500. There also exists a simple DIY-programmer which works with LPT port.  supports them all great.

## udev rules
To be able to run  without superuser rights, a Udev rule needs to be created to change ownership of the usb device to another group (the commonly used group for this is ):

{{hc|/etc/udev/rules.d/99-avrprogrammer.rules|2=
 # Set group for a programmer matching with vendor and product IDs
 SUBSYSTEM=="usb", ATTRS{idVendor}=="your Vendor ID", ATTRS{idProduct}=="your Product ID", GROUP="uucp", MODE="0666"
}}

Replace the italic parts with your programmer's vendor and product IDs (these can be found with the lsusb command from ) and add the  group to your user's supplementary groups.

## Usage
To compile C program for AVR chip (let us consider ATmega8A running at 8 MHz as example) you can use  directly. You should only specify target MCU (full list of supported MCUs could be found with ) and its working frequency:

 $ avr-gcc -DF_CPU=8000000UL -mmcu=atmega8a -std=gnu99 main.c -o main.elf

avrdude is smart enough to work with the resulting ELF file but you can convert it explicitly to Intel HEX:

 $ avr-objcopy -O ihex -j .text -j .data main.elf main.hex

Then run avrdude and specify flash ROM as destination for firmware burning (in this example AVRISP mkII is used and clock speed is lowered to the 125 kHz to be on safe side):

 $ avrdude -p atmega8 -c avrispmkII -B 125kHz -U flash:w:main.hex

That's all. Among other things avrdude can work with EEPROM memory, fuse and lock bits. For example, to set up low and high fuses to the 0x9F and 0xD1 respectively use the following incantation:

 $ avrdude -p atmega8 -c avrispmkII -B 125kHz -U lfuse:w:0x9F:m -U hfuse:w:0xD1:m

Just remember that ISP programming speed should not exceed 1/8 of MCU's working frequency. A lot of new chips comes with 1 MHz speed settings so using 125 kHz as starting value should be fine enough.

## Tips and tricks
## Optimization
Because AVRs come with tight flash ROM size and relatively weak CPUs you can consider some optimizations to improve space usage and overall performance of your device. It is common practice to enable GCC optimization level  and turn on some extra features: . To exclude unnecessary library references perform garbage collection: .

## Sample Makefile
Managing huge project could be tedious and Makefile workflow is the most efficient way to deal with it. Here are sample Makefile based on AVRfreaks version:

 CC = avr-gcc
 OBJCOPY = avr-objcopy
 SIZE = avr-size
 NM = avr-nm
 AVRDUDE = avrdude
 REMOVE = rm -f

 MCU = atmega8a
 F_CPU = 8000000

 LFUSE = 0x9f
 HFUSE = 0xd1

 TARGET = firmware
 SRC = main.c lcd.c twi.c
 OBJ = $(SRC:.c=.o)
 LST = $(SRC:.c=.lst)

 FORMAT = ihex

 OPTLEVEL = s

 CDEFS =

 CFLAGS = -DF_CPU=$(F_CPU)UL
 CFLAGS += $(CDEFS)
 CFLAGS += -O$(OPTLEVEL)
 CFLAGS += -mmcu=$(MCU)
 CFLAGS += -std=gnu99
 CFLAGS += -funsigned-char -funsigned-bitfields -fpack-struct -fshort-enums
 CFLAGS += -ffunction-sections -fdata-sections
 CFLAGS += -Wall -Wstrict-prototypes
 CFLAGS += -Wa,-adhlns=$(<:.c=.lst)

 LDFLAGS = -Wl,--gc-sections
 LDFLAGS += -Wl,--print-gc-sections

 AVRDUDE_MCU = atmega8
 AVRDUDE_PROGRAMMER = avrispmkII
 AVRDUDE_SPEED = -B 1MHz

 AVRDUDE_FLAGS = -p $(AVRDUDE_MCU)
 AVRDUDE_FLAGS += -c $(AVRDUDE_PROGRAMMER)
 AVRDUDE_FLAGS += $(AVRDUDE_SPEED)

 MSG_LINKING = Linking:
 MSG_COMPILING = Compiling:
 MSG_FLASH = Preparing HEX file:

 all: gccversion $(TARGET).elf $(TARGET).hex size

 .SECONDARY: $(TARGET).elf
 .PRECIOUS: $(OBJ)

 %.hex: %.elf
         @echo
         @echo $(MSG_FLASH) $@
         $(OBJCOPY) -O $(FORMAT) -j .text -j .data $< $@

 %.elf: $(OBJ)
         @echo
         @echo $(MSG_LINKING) $@
         $(CC) -mmcu=$(MCU) $(LDFLAGS) $^ --output $(@F)

 %.o : %.c
         @echo $(MSG_COMPILING) $<
         $(CC) $(CFLAGS) -c $< -o $(@F)

 gccversion:
         @$(CC) --version

 size: $(TARGET).elf
         @echo
         $(SIZE) -C --mcu=$(AVRDUDE_MCU) $(TARGET).elf

 analyze: $(TARGET).elf
         $(NM) -S --size-sort -t decimal $(TARGET).elf

 isp: $(TARGET).hex
         $(AVRDUDE) $(AVRDUDE_FLAGS) -U flash:w:$(TARGET).hex

 fuses:
         $(AVRDUDE) $(AVRDUDE_FLAGS) -U lfuse:w:$(LFUSE):m -U hfuse:w:$(HFUSE):m

 release: fuses isp

 clean:
         $(REMOVE) $(TARGET).hex $(TARGET).elf $(OBJ) $(LST) *~

## Calculating control register values
To speed up development of your projects you can use  utility which helps to calculate different parameters for control registers regarding timers, frequencies etc.
