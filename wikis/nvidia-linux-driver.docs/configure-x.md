## Chapter 6. Configuring X for the NVIDIA Driver

## Using nvidia-xconfig to configure the X server

nvidia-xconfig will find the X configuration file and modify it to use the NVIDIA X driver. In most cases, you can simply answer "Yes" when the installer asks if it should run it. If you need to reconfigure your X server later, you can run nvidia-xconfig again from a terminal. nvidia-xconfig will make a backup copy of your configuration file before modifying it.

Note that the X server must be restarted for any changes to its configuration file to take effect.

More information about nvidia-xconfig can be found in the nvidia-xconfig manual page by running.

``` screen
    % man nvidia-xconfig
```

## Manually Editing the Configuration File

If you do not have a working X config file, there are a few different ways to obtain one. A sample config file is included both with the X.Org distribution and with the NVIDIA driver package (at `/usr/share/doc/NVIDIA_GLX-1.0/`). The **nvidia-xconfig** utility, provided with the NVIDIA driver package, can generate a new X configuration file. Additional information on the X config syntax can be found in the xorg.conf manual page (**`man xorg.conf`**).

If you have a working X config file for a different driver (such as the “vesa” or “fbdev” driver), then simply edit the file as follows.

Remove the line:

``` screen
      Driver "vesa"
  (or Driver "fbdev")
```

and replace it with the line:

``` screen
    Driver "nvidia"
```

Remove the following lines:

``` screen
    Load "dri"
    Load "GLCore"
```

In the `Module` section of the file, add the line (if it does not already exist):

``` screen
    Load "glx"
```

If the X config file does not have a `Module` section, you can safely skip the last step.

There are numerous options that may be added to the X config file to tune the NVIDIA X driver. See [Appendix B, *X Config Options*](xconfigoptions.html "Appendix B. X Config Options") for a complete list of these options.

Once you have completed these edits to the X config file, you may restart X and begin using the accelerated OpenGL libraries. After restarting X, any OpenGL application should automatically use the new NVIDIA libraries. (NOTE: If you encounter any problems, see [Chapter 8, *Common Problems*](commonproblems.html "Chapter 8. Common Problems") for common problem diagnoses.)

## Restoring the X Configuration after Uninstalling the Driver

If X is explicitly configured to use the NVIDIA driver, then the X config file should be edited to use a different X driver after uninstalling the NVIDIA driver. Otherwise, X may fail to start, since the driver it was configured to use will no longer be present on the system after uninstallation.

If you edited the file manually, revert any edits you made. If you used the **nvidia-xconfig** utility, either by answering "Yes" when prompted to configure the X server by the installer, or by running it manually later on, then you may restore the backed-up X config file, if it exists and reflects the X config state that existed before the NVIDIA driver was installed.

If you do not recall any manual changes that you made to the file, or do not have a backed-up X config file that uses a non-NVIDIA X driver, you may want to try simply renaming the X configuration file, to see if your X server loads a sensible default.
