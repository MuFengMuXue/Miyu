# ESP32

ESP32 is a family of low-cost, energy-efficient microcontrollers with built-in Wi-Fi and Bluetooth connectivity. Different variants use different CPU cores — for example, the Tensilica Xtensa LX6, the Xtensa LX7 dual-core, or a single-core RISC-V — and include on-chip RF components needed for wireless operation such as antenna switching, an RF balun, power amplifiers, low-noise receivers, filters and power-management circuitry.

ESP32 silicon is commonly shipped on application-specific PCBs or as development modules that expose GPIOs and various connectors; exact pinouts and features depend on the model and vendor. Designed by Espressif and manufactured by TSMC on a 40 nm process, the ESP32 family is the successor to the ESP8266.

## Installation
The following IDEs and toolchains are commonly used to develop for ESP32:
* PlatformIO:  Install Visual Studio Code, then install the PlatformIO extension.

* Arduino IDE:  Install Arduino IDE

* ESP-IDF :  Install Visual Studio Code, then install the ESP-IDF extension.

## Alternative Installation Method
Install . ESP-IDF will be installed into .
After installation, add this snippet to :

{{bc|
esp() {
  git config --global --get-all safe.directory \
    | grep -q '^/opt/esp-idf$' \
    || git config --global --add safe.directory /opt/esp-idf
  source /opt/esp-idf/export.sh
}
}}

Use this snippet instead if you would like to use the alias  in place of , complete with command-line completion:

{{bc|
esp() {
  git config --global --get-all safe.directory \
    | grep -q '^/opt/esp-idf$' \
    || git config --global --add safe.directory /opt/esp-idf
  source /opt/esp-idf/export.sh
  alias idf=idf.py
  eval "$(env LANG=en \
              _IDF.PY_COMPLETE=bash_source \
              idf.py \
    | sed -e 's,$1,$1.py,' \
          -e 's,idf\.py$,idf,' \
          -e 's,_idfpy_completion,_idfpy_completion2,')"
}
}}

Every time you would like to use ESP-IDF in a new terminal session, call the function  to enable it:

## Configuration
## Configure Arduino IDE
After installing the Arduino IDE, add Espressif's board package and select the correct serial port:
* Go to File > Preferences and add https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json to "Additional Boards Manager URLs."

* Go to Tools > Board > Boards Manager, search for "esp32", and install the "esp32" boards package by Espressif.

* Select your specific board (e.g., "ESP32 Dev Module," "ESP32S3 Dev Module," "ESP32C3 Dev Module") and the correct serial port under Tools > Board and Tools > Port.

## Troubleshooting
## First Flash/Upload Issues
* "Failed to connect to ESP32: Timed out waiting for packet header." This is the most frequent error.
** Boot Mode: Most ESP32 boards need GPIO0 pulled low (by pressing and holding the "BOOT" button) during connection and until the upload process begins. Release the button once the upload starts.
** Correct serial port: Double-check that you've selected the correct serial port in your IDE (Tools > Port in Arduino, or in PlatformIO's configuration).
** Reset/Enable Sequence: Sometimes, you need to hold BOOT, then press and release EN (or RESET), and then release BOOT after the upload starts.
** USB-to-Serial Drivers: Many older ESP32 boards use specific USB-to-serial chips (e.g., CH340G, CP2102, FTDI). Ensure you have the latest drivers installed for your chip. Newer boards (especially S2/S3 with native USB) generally don't require external drivers.
*** Resource: Search for "CP210x driver" or "CH340G driver" from Silicon Labs or WCH, respectively.
** USB Cable Quality: Many USB cables are "charge-only" or have poor data lines. Try a different, known-good data cable. Keep the cable as short as possible.
** Serial Port Busy: Ensure no other program (e.g., another instance of your IDE, a serial terminal, a previously crashed sketch) is using the serial port. Close Arduino's Serial Monitor if it's open.
** Insufficient Power: Some boards (especially ESP32-CAM) require more current than a standard USB port can provide, leading to flaky uploads or brownouts. Try a powered USB hub or an external 5V power supply connected to the board's 5V pin.
