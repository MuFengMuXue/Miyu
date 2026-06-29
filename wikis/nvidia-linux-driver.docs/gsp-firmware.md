## Chapter 44. GSP Firmware

Some GPUs include a GPU System Processor (GSP) which can be used to offload GPU initialization and management tasks. This processor is driven by firmware files distributed with the driver. The GSP firmware is used by default on GPUs which support it.

Offloading tasks which were traditionally performed by the driver on the CPU can improve performance due to lower latency access to GPU hardware internals.

Firmware files `gsp_*.bin` are installed in `/lib/firmware/nvidia/580.105.08/`. Each GSP firmware file is named after a GPU architecture (for example,`gsp_tu10x.bin` is named after Turing) and supports GPUs from one or more architectures.

### Query Mode

The nvidia-smi utility can be used to query the current use of GSP firmware. It will display a valid version if GSP firmware is enabled, or “N/A” if disabled:

``` screen
    $ nvidia-smi -q
    ...
       GSP Firmware Version                  : 580.105.08
    ...
```

This information is also present in the per-GPU information file in the `/proc` file system.

``` screen
    $ cat /proc/driver/nvidia/gpus/PCI-BUS-ID/information
    ...
       GSP Firmware:    580.105.08
```

See [“What is the format of a PCI Bus ID?”](faq.html#busid) for information on how to determine the PCI-BUS-ID.

### Disabling GSP Mode

The driver can be forced to disable use of GSP firmware by setting the kernel module parameter NVreg_EnableGpuFirmware=0.

### Enabling GSP Mode

The GSP firmware will be used by default for all Turing and later GPUs. The driver can be explicitly configured to use the GSP firmware by setting the kernel module parameter NVreg_EnableGpuFirmware=1.
