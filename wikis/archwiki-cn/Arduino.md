相关文章

  * [AVR](</wzh/index.php?title=AVR&action=edit&redlink=1> "AVR（页面不存在）")

**翻译状态：**

  * 本文（或部分内容）译自 [Arduino](<https://wiki.archlinux.org/title/Arduino> "arch:Arduino")，最近一次同步于 2024-11-27，若英文版本有所[更改](<https://wiki.archlinux.org/title/Arduino?diff=0&oldid=817817>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Arduino_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[Arduino](<https://en.wikipedia.org/wiki/Arduino> "wikipedia:Arduino") 是一款便捷灵活、方便上手的开源电子原型平台。它适用于艺术家，设计师，业余爱好者以及任何对创建交互式对象或环境感兴趣的人。 

在连接并完成配置后，用户可以通过建立好的串行接口进行多种读写操作。例如，可以使用[串行监视器](</wzh/index.php?title=Working_with_the_serial_console&action=edit&redlink=1> "Working with the serial console（页面不存在）")操控 UART 或是对微控制器进行编程。编程，编译及上传程序需要用到官方 Arduino IDE，可通过官方软件源获得。另外，用户也可以自行选择编译器和编程器对微控制器进行编程。 

##  安装

  * 需要官方 CLI 请安装 [arduino-cli](<https://archlinux.org/packages/?name=arduino-cli>)包，需要新的 2.x 版本官方 IDE 请安装 [arduino-ide](<https://archlinux.org/packages/?name=arduino-ide>)包。
  * 启用到设备的[#访问串口|用户访问权限]]。
  * 你可能需要[加载](<../zh-cn/%E5%86%85%E6%A0%B8%E6%A8%A1%E5%9D%97.html> "内核模块") `cdc_acm` 模块。

### Arduino IDE 1.x

以下部分只适用于 1.x 版本的 IDE。不过，可能也有部分内容可用于新 IDE。 

####  AVR 开发板

要使用Arduino Uno等AVR板，您可以选择安装 [arduino-avr-core](<https://archlinux.org/packages/?name=arduino-avr-core>)包，以使用Arch Linux上游avr-gcc代替捆绑的旧版avr-core。如果您仍然想使用较旧的arduino-core，则需要将它安装在arduino的开发板管理器中[[1]](<https://www.arduino.cc/en/Guide/Cores>)。您始终可以在“工具>面板”菜单中的不同内核之间切换。 

#### Pinoccio Scout

[Pinoccio Scouts](<https://pinocc.io/>)[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2024-01-13 ⓘ] 也可以使用Arduino IDE编写程序。可以在[这里](<https://pinocc.io/solo>)[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2024-01-13 ⓘ]找到相关介绍。 此外你可以通过[AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR")来安装[arduino-pinoccio](<https://aur.archlinux.org/packages/arduino-pinoccio/>)AUR。 

#### Intel Galileo

要将Intel Galileo开发板与Arch Linux一起使用，请安装Arduino IDE，然后通过“工具->板->板管理器”下载Galileo工具包。 修复安装问题，请访问[github](<https://github.com/arduino/Arduino/issues/5523>)。 

###  Arduino IDE 1.x 或 2.x

以下内容应同时适用于两个版本的 IDE。 

####  AVR 开发板

AVR 开发板在 2.x 版本的 IDE 上应已自动安装，但在 1.x 和 2.x 版本上都可以通过开发板管理器管理 AVR 开发板。 

#### SparkFun

如果要使用 Pro Micro 等 SparkFun 开发板，需要先下载开发板定义。更多信息请参考[这里](<https://learn.sparkfun.com/tutorials/pro-micro--fio-v3-hookup-guide/installing-mac--linux>)和[这里](<https://github.com/sparkfun/Arduino_Boards>)。 

### RedBear Duo

你可能需要安装 [perl-archive-zip](<https://archlinux.org/packages/?name=perl-archive-zip>)包，否则可能会出现 crc32 缺失错误。 

##  配置

大多数 Arduino 开发板都提供了 USB 接口，以提供串行连接对开发板进行编程。然而，多数 Arduino 开发板使用的微控制器缺乏内置 USB 接口，因此板上通常会使用 USB 转串行芯片来连接 USB 接口和微控制器。 

为了通过 USB 传输串行信号，大部分官方 Arduino 开发板会使用一颗额外的 ATmega 微控制器（例如 ATmega16U2），或是使用 FTDI USB UART 转换器（如 FT232RL）。这两者都会将自身注册为 ACM 设备，因此 Linux 将会使用到 `cdc_acm` [内核模块](<../zh-cn/%E5%86%85%E6%A0%B8%E6%A8%A1%E5%9D%97.html> "内核模块")。这一类的 Arduino 开发板会在系统中显示为 `/dev/ttyACMx`。 

非官方的 Arduino 开发板通常会在接口芯片上扣成本，将其替换为中国产的 CH340 芯片或其仿冒品。CH340 会将自己描述为 USB 上的 UART 专有传输设备，因此 Linux 会使用到 `ch341` [内核模块](<../zh-cn/%E5%86%85%E6%A0%B8%E6%A8%A1%E5%9D%97.html> "内核模块")，这一类的开发板在系统中会显示为 `/dev/ttyUSBx`。该命名规则可通过 [udev 规则进行修改](<#Arduino_%E8%AE%BE%E5%A4%87%E5%91%BD%E5%90%8D%E6%8C%81%E4%B9%85%E5%8C%96>)。 

有些开发板使用的微控制器自带 USB 接口。无论开发板是否使用独立的接口芯片，官方开发板出厂都会预装启动引导器，引导器会在连接到 USB 时自动建立串行连接。 

**注意：** 类似 Pro Mini 这样的板子不提供 USB 接口，需要通过外部硬件进行编程。

###  访问串口

对于通过 USB 暴露 UART 接口的板子，需要给予用户串口的读写权限 [[2]](<https://arduino.stackexchange.com/a/21219>)。根据 [Udev#Allowing regular users to use devices](<../zh-cn/Udev.html#Allowing_regular_users_to_use_devices> "Udev") 的说明，需要创建如下文件： 
    
    /etc/udev/rules.d/01-ttyusb.rules
    
    SUBSYSTEMS=="usb-serial", TAG+="uaccess"

[重新加载 udev 规则](<../zh-cn/Udev.html#%E5%8A%A0%E8%BD%BD%E6%96%B0%E8%A7%84%E5%88%99> "Udev")，然后重新连接 Arduino 设备。在上传程序到 Arduino 前，请确保已在 1.x 的工具菜单和 2.x 的“选择开发板”选项（位于 IDE 顶部）设置了正确的串行接口、开发板及处理器。 

**注意：** 在上传代码时，请确保已关闭所有串行监视器来为编程器释放串行端口。

## stty

设置: 
    
    # stty -F /dev/ttyACM0 cs8 9600 ignbrk -brkint -imaxbel -opost -onlcr -isig -icanon -iexten -echo -echoe -echok -echoctl -echoke noflsh -ixon -crtscts
    
通过终端发送命令，无换行 
    
    # echo -n "Hello World" > /dev/ttyACM0
    
**注意：** 由于大多数板上默认情况下会激活串行连接上的自动重置功能，因此，如果要使用最后一条命令而不是终端仿真器（arduino IDE，屏幕，picocom ...）直接与您的板通信，则需要禁用此功能。如果您有Leonardo面板，则不必担心，因为它不会自动重置。如果您有Uno板，请在RESET和GND引脚之间连接一个10 µF电容器。如果有另一块板，则在RESET和5V引脚之间连接一个120欧姆的电阻。 有关更多详细信息，请参见 <https://playground.arduino.cc/Main/DisablingAutoResetOnSerialConnection>

读取Arduino发送的信息 
    
    $ cat /dev/ttyACM0
    
## Arduino-Builder

[![](../File:Tango-view-refresh-red.png)](<../File:Tango-view-refresh-red.png>)**本文或本节内容已经过时。**

**原因：** 该部分写于 2.x 版本 IDE 发布前，因此相关功能描述可能有错。在 GitHub 页面上 Arduino-Builder 已被标记为过时，并将被 Arduino CLI 替代。 (在[Talk:Arduino](<../zh-cn/Talk:Arduino.html>)讨论)

您也可以使用[arduino-builder](<https://archlinux.org/packages/?name=arduino-builder>)包命令行工具来构建Arduino的内置例程。 为了使用所提供的[arduino-avr-core](<https://archlinux.org/packages/?name=arduino-avr-core>)包与上游[avr-gcc](<https://archlinux.org/packages/?name=avr-gcc>)包和[avrdude](<https://archlinux.org/packages/?name=avrdude>)包你需要创建一个小的设置文件： 
    
    build.options.json
    
    {
        "fqbn": "archlinux-arduino:avr:uno",
        "hardwareFolders": "/usr/share/arduino/hardware",
        "toolsFolders": "/usr/bin"
    }

通过下面的命令来编译一个内置例程: 
    
    $ arduino-builder -build-options-file build.options.json blink.ino
    
或通过命令行传递所有选项: 
    
    $ arduino-builder -fqbn archlinux-arduino:avr:uno -hardware /usr/share/arduino/hardware -tools /usr/bin blink.ino
    
##  IDE 替代

### Arduino-CMake

通过 [Arduino-CMake-Toolchain](<https://github.com/a9183756-gh/Arduino-CMake-Toolchain>) 和 [CMake](<https://www.cmake.org/cmake/resources/software.html>)，你可以在命令行下使用多个构建系统来构建 Arduino 固件。CMake 可以让您使用自己喜欢的工具生成适合您需求的构建系统。它可以生成任何类型的构建系统，从简单的 Makefile 到 Eclipse，Visual Studio，XCode 等完整项目。 

需求：[cmake](<https://archlinux.org/packages/?name=cmake>)包, [arduino](<https://archlinux.org/groups/x86_64/arduino/>)包组, [avr-gcc](<https://archlinux.org/packages/?name=avr-gcc>)包, [avr-binutils](<https://archlinux.org/packages/?name=avr-binutils>)包, [avr-libc](<https://archlinux.org/packages/?name=avr-libc>)包, [avrdude](<https://archlinux.org/packages/?name=avrdude>)包. 

### Makefile

除了使用 Arduino IDE，还可以使用其他编辑器搭配上 Makefile。 

设置目录以对Arduino进行编程，然后将 Makefile 复制到该目录中。可以从[该 GitHub 示例](<https://github.com/tomswartz07/arduino-makefile>)获取 Makefile 的副本。 

您必须在此稍作修改以反映您的设置。Makefile应该很容易说明。这是您可能需要编辑的几行: 
    
    PORT = usually /dev/ttyUSBx, where x is the usb serial port your arduino is plugged into
    TARGET = your sketch's name
    ARDUINO = /usr/share/arduino/lib/targets/arduino
    
根据您在例程代码中调用的库函数，您可能需要编译库的某些部分。为此，您需要编辑SRC和CXXSRC以包括所需的库。 

现在，您应该可以`make && make upload`编译并上传您的程序到板子了。 

### Arduino-mk

[arduino-mk](<https://github.com/sudar/Arduino-Makefile>) 是另一种Makefile方法。它允许用户使用包含Arduino.mk的本地Makefile。具体用法参见[项目页](<https://github.com/sudar/Arduino-Makefile>)。 

对于Arduino 1.5，请尝试以下本地Makefile（因为Arduino 1.5的库目录结构略有不同）: 
    
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
    
在某些情况下，您可能需要安装[avr-libc](<https://archlinux.org/packages/?name=avr-libc>)包和[avrdude](<https://archlinux.org/packages/?name=avrdude>)包。 

### Scons

结合使用[scons](<https://www.scons.org/>)和[arscons](<https://github.com/suapapa/arscons>)，可以很容易地从命令行编译和上传Arduino项目。 Scons基于python，您将需要python-pyserial才能使用串行接口。安装[python-pyserial](<https://archlinux.org/packages/?name=python-pyserial>)包和[scons](<https://archlinux.org/packages/?name=scons>)包。 

这也将同时获得您需要的依赖项。您还将需要Arduino本身，请参考上所述进行安装。创建项目目录(例如test)，然后在新目录中创建arduino项目文件。使用与目录相同的名称并添加.ino(例如test.ino)。从arscons获取[SConstruct](<https://github.com/suapapa/arscons/blob/master/SConstruct>)脚本并将其放在目录中。大致看一下内容，如有必要，对其进行编辑。这是一个python脚本。根据需要编辑项目，然后运行 
    
    $ scons                # This will build the project
    $ scons upload         # This will upload the project to your Arduino
    
### PlatformIO

[PlatformIO](<https://docs.platformio.org/en/latest/core/quickstart.html>) 是一个 [python](<../zh-cn/Python.html> "Python") 工具，用于为多个硬件平台构建和上传程序，在编写本文时，它支持基于 Arduino/AVR，TI MSP430 和 TI TM4C12x 的开发板。作者计划在不久的将来添加一个库功能，该功能允许直接从 GitHub 搜索和导入库。 

####  安装

安装 [platformio-core](<https://archlinux.org/packages/?name=platformio-core>)包 或 {[platformio-git](<https://aur.archlinux.org/packages/platformio-git/>)AUR。 

####  使用

一线内容基于官方 [PlatformIO 入门指南](<https://docs.platformio.org/en/latest/core/quickstart.html>)，展示了如何创建和上传示例项目。 

为 platformio 项目创建一个新文件夹，并进入到目录内。 然后执行以下命令来为特定开发板初始化项目（此处为 megaatmega2560）： 
    
    $ pio project init --board megaatmega2560
    
这将下载所需工具链和依赖，并创建 `platformio.ini` 文件： 
    
    platformio.ini
    
    ; PlatformIO Project Configuration File
    [env:megaatmega2560]
    platform = atmelavr
    board = megaatmega2560
    framework = arduino

创建并将代码添加到 src/ 目录下的 main.cpp 文件内，可参考[快速入门指南](<https://docs.platformio.org/en/latest/core/quickstart.html>)中的示例代码。 

然后编译代码并将其上传到 platformio.ini 中指定的设备上： 
    
    $ pio run
    $ pio run --target upload
    
### Emacs

当然可以将 [Emacs](<../zh-cn/Emacs.html> "Emacs") 配置为IDE。 

安装 [emacs-arduino-mode-git](<https://aur.archlinux.org/packages/emacs-arduino-mode-git/>)AUR，以便在 emacs 中启用 `arduino-mode`。 

在初始化脚本添加下列内容： 
    
    ~/.emacs
    
    ;; arduino-mode
    (require 'cl)
    (autoload 'arduino-mode "arduino-mode" "Arduino editing mode." t)
    (add-to-list 'auto-mode-alist '("\.ino$" . arduino-mode))

您可以使用 `M-x compile` `make upload` 和 `Arduino-mk`（见上文）来编译和上传程序。 

参见: [[3]](<https://www.emacswiki.org/emacs/ArduinoSupport>). 

##  排障

###  Arduino 设备命名持久化

如果您有多个arduino，您可能已经注意到，它们的名称 `/dev/ttyUSB[0-9]` 是按连接顺序分配的。在IDE中，这并不是什么大问题，但是当您编写了自己的软件以在后台与arduino项目进行通信时，这可能会很烦人。使用以下 _udev_ 规则为arduino分配静态符号链接： 
    
    /etc/udev/rules.d/52-arduino.rules
    
    SUBSYSTEMS=="usb", KERNEL=="ttyUSB[0-9]*", ATTRS{idVendor}=="0403", ATTRS{idProduct}=="6001", SYMLINK+="sensors/ftdi_%s{serial}"
    
您的arduino将以 `/dev/sensors/ftdi_A700dzaF` 之类的名称提供。如果您愿意，还可以为多个设备分配更有意义的名称，如下所示： 
    
    /etc/udev/rules.d/52-arduino.rules
    
    SUBSYSTEMS=="usb", KERNEL=="ttyUSB[0-9]*", ATTRS{idVendor}=="0403", ATTRS{idProduct}=="6001", ATTRS{serial}=="A700dzaF", SYMLINK+="arduino/nano"
    
这将在 `/dev/arduino/nano` 中创建到具有指定序列号的设备的符号链接。 

您需要将 arduino 拔出并重新插入才能使它生效，也可以运行： 
    
    # udevadm trigger
    
常见的 `idVendor`/`idProduct` 对可在发行包中的 `/usr/share/arduino/hardware/archlinux-arduino/avr/boards.txt`中找到。请注意，其中一些（尤其是 [FTDI](<https://en.wikipedia.org/wiki/FTDI> "wikipedia:FTDI")）并不是Arduino平台所独有的。使用 `serial` 属性是区分各种设备的好方法。 

###  无法开启串口

在 IDE 启动时，您可能最初会看到串行端口，但是在上传固件时，TX/RX 指示灯无任何变化。您可能之前将串口监视器中的波特率更改为了它不喜欢的内容。编辑 `~/.arduino/preferences.txt`，将 `serial.debug_rate` 修改为不同的速度，例如 115200。 

###  使用 Uno/Mega2560

Arduino Uno 和 Mega2560 具有一个板载 USB 接口（Atmel 8U2），用来接收串口数据，因此，在 USB 插入后，可以通过 cdc-acm 内核模块创建的 `/dev/ttyACM0` 来访问它们。 

8U2 固件可能需要更新才能方便串行通信，详细信息可参考 [[4]](<https://forum.arduino.cc/t/easy-to-brick-arduino-uno-on-linux/47039>)，并在回复 #11 中找到修复方法。最早在 Arduino bbs 上有一张图解释了如何将 Uno 启动到 DFU 模式，但现在已进入只读状态。如果你没有查看该图所需的账号，可以参考 [[5]](<https://www.scribd.com/doc/45913857/Arduino-UNO>)。 

您可以通过将 Uno 置于环回模式并在 115200 波特的 arduino 串行监视器中键入字符来对 Uno 进行常规功能测试。它应将字符回显给您。要将其置于环回状态，请在数字端短接引脚 0->1，并在键入时按住复位按钮或将 GND->RESET 引脚短路。 

###  无法识别中国制廉价 Mega2560 的 USB 连接

试试安装驱动: [i2c-ch341-dkms](<https://aur.archlinux.org/packages/i2c-ch341-dkms/>)AUR

###  上传失败：编程器无响应

将处理器设置从 `ATmega328P` 更改为 `ATmega328P (Old Bootloader)`（请参阅Arduino IDE中的“工具”->“处理器”）可能有助于解决上传失败的问题。 

###  串口与 brltty 冲突

如果未找到 arduino 的 `/dev/ttyUSB*` 串口，且在设备已连接时 [journal](<../zh-cn/Systemd/Journal.html> "Journal") 包含如下内容： 
    
    usb 3-1: usbfs: interface 0 claimed by ch341 while 'brltty' sets config #1
    ch341-uart ttyUSB0: ch341-uart converter now disconnected from ttyUSB0
    
你可能需要卸载 [brltty](<https://archlinux.org/packages/?name=brltty>)包。详细信息参见 [[6]](<https://forum.manjaro.org/t/cant-connect-serial-port-error-ch341-uart-disconnected-from-ttyusb0/87208>)。 

###  无法上传到连接中的 Nano RP2040

如果你在上传时出现： 
    
    Failed uploading: uploading error: exit status 1
    
你没有进行[#访问串口]]中的步骤：请跟随文档步骤授予用户串口的读写操作权限。 

##  参见

  * [官方网站](<https://www.arduino.cc/>)
  * [IDE v2 入门指南](<https://docs.arduino.cc/software/ide-v2/tutorials/getting-started-ide-v2>)
  * <https://answers.ros.org/question/9097/how-can-i-get-a-unique-device-path-for-my-arduinoftdi-device/>
