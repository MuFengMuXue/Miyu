# Libcamera

Libcamera is a camera support library. It includes support for cameras that have poor or no support by upstream drivers.

## Installation
Install the  package. Install the  package to add support for PipeWire.

## Usage
For applications that support it, libcamera can be used as is. Some applications need to use V4L2, so  from  can use LD_PRELOAD to add a virtual V4L2 device that points to libcamera, for example running  through this virtual device:

 $ libcamerify cheese

## Debugging
Running  as provided by  can show whether the camera in use is working even if other software does not support the libcamera APIs.
