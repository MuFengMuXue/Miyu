## Chapter 25. Using the nvidia-settings Utility

A graphical configuration utility, **nvidia-settings**, is included with the NVIDIA Linux graphics driver. After installing the driver and starting X, you can run this configuration utility by running:

``` screen
    % nvidia-settings
```

in a terminal window. nvidia-settings requires version 2.4 or later of the GTK+ 2 library.

Some architectures of Linux support the GTK+ 3 library and would require version 3.0 or later if available.

Detailed information about the configuration options available are documented in the help window in the utility.

For more information, see the nvidia-settings man page.

The source code to nvidia-settings is released as GPL and is available here: https://download.nvidia.com/XFree86/nvidia-settings/
