This document describes how to compile U-Boot for linux-sunxi devices

## [Prerequisites]

-   crossdev toolchain for target (for example, armv7a-unknown-linux-gnueabihf is used for cubietruck)
-   python:2.7 python swig dev-python/pip dev-python/setuptools bc dev-python/python-distutils-extra dtc git

## [U-Boot compilation]

Prepare working environment:

`user `[`$`]`git clone `[`https://github.com/linux-sunxi/u-boot-sunxi.git`](https://github.com/linux-sunxi/u-boot-sunxi.git)

`user `[`$`]`cd u-boot-sunxi`

`user `[`$`]`export CROSS_COMPILE="armv7a-unknown-linux-gnueabihf-"`

`user `[`$`]`virtualenv -p /usr/bin/python2.7 venv`

`user `[`$`]`source venv/bin/activate`

Remove line from scripts/dtc/dtc-lexer.lex.c

[FILE] **`scripts/dtc/dtc-lexer.l`dtc-lexer.l**

    YYLTYPE yyloc;

Compile:

`user `[`$`]`make Cubietruck_config`

`user `[`$`]`make clean`

`user `[`$`]`make all`

## [U-Boot installation]

dd u-boot-sunxi-with-spl.bin into SD card you\'re going to be using for your machine

`root `[`#`]`dd if=u-boot-sunxi-with-spl.bin of=/dev/mmcblk0 bs=1024 seek=8`