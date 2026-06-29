**Resources**

[[]][Home](http://www.dell.com/support/home/us/en/04/product-support/product/inspiron-15-3537/manuals)

## Contents

-   [[1] [Hardware]](#Hardware)
    -   [[1.1] [Standard]](#Standard)
-   [[2] [Firmware]](#Firmware)
-   [[3] [Kernel]](#Kernel)
-   [[4] [Configuration]](#Configuration)
    -   [[4.1] [Configuring Xorg]](#Configuring_Xorg)
    -   [[4.2] [Hybrid Graphics]](#Hybrid_Graphics)
    -   [[4.3] [Configuring the touchpad]](#Configuring_the_touchpad)
-   [[5] [Troubleshooting]](#Troubleshooting)
    -   [[5.1] [Wrong turbo multipliers]](#Wrong_turbo_multipliers)
    -   [[5.2] [Touchpad doesn\'t work after resume]](#Touchpad_doesn.27t_work_after_resume)
-   [[6] [See also]](#See_also)
-   [[7] [References]](#References)

## [Hardware]

### [Standard]

  ------------ ---------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------- ----------- ----------------------------------------------------------------------------------------------------------------------------- ----------------
  Device       Make/model                                                                                                                                     Status                                             Bus ID      Kernel driver(s)                                                                                                              Kernel version
  CPU          [Intel i7-4500U](https://ark.intel.com/products/75460/Intel-Core-i7-4500U-Processor-4M-Cache-up-to-3_00-GHz)   Works ^[\[table\ 1\]](#cite_note-wrongturbo-1)^    N/A         N/A                                                                                                                           5.6
  Video card   Intel Integrated HD 4400                                                                                                                       Works                                              8086:0a16   [i915](https://wiki.gentoo.org/wiki/Intel "Intel")                                                                            5.6
  Video card   [AMD Radeon HD 8850M](https://www.amd.com/en-us/products/graphics/notebook/8700m-8800m)                        Works                                              1002:6823   [radeon](https://wiki.gentoo.org/wiki/Radeon "Radeon")/[amdgpu](https://wiki.gentoo.org/wiki/Amdgpu "Amdgpu")   5.6
  Ethernet     Realtek RTL8101E/RTL8102E                                                                                                                      Works                                              10ec:8136   r8169                                                                                                                         5.6
  Touchpad     Synaptics TM2382-001                                                                                                                           Works                                              N/A         [synaptics](https://wiki.gentoo.org/wiki/Synaptics "Synaptics")                                                               5.6
  Wireless     Broadcom BCM43142                                                                                                                              Works ^[\[table\ 2\]](#cite_note-wl-2)^            14e4:4365   [wl](https://packages.gentoo.org/packages/net-wireless/broadcom-sta)                          5.6
  ------------ ---------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------- ----------- ----------------------------------------------------------------------------------------------------------------------------- ----------------

1.  [[[↑](#cite_ref-wrongturbo_1-0)] [ See [Wrong turbo multipliers](#Wrong_turbo_multipliers) ]]
2.  [[[↑](#cite_ref-wl_2-0)] [ Requires closed-source binary driver. ]]

## [Firmware]

Due to errata in the processor, it is advised to install and keep the CPU microcode up-to-date. See [intel microcode](https://wiki.gentoo.org/wiki/Intel_microcode "Intel microcode").

## [Kernel]

Follow the [intel](https://wiki.gentoo.org/wiki/Intel "Intel") and [radeon](https://wiki.gentoo.org/wiki/Radeon "Radeon") articles to enable the required kernel options.

[KERNEL] **Enable ethernet support**

    Device Drivers --->
      Network device support --->
        Ethernet Driver Support --->
          [*] Realtek Devices
          [*] Realtek 8169 gigabit ethernet support

## [Configuration]

### [Configuring Xorg]

A barebone config is needed:

[CODE] **/etc/X11/xorg.conf.d/20-intel.conf**

    Section "Device"
       Identifier "Intel Graphics"
       Driver "intel"
       Option "TearFree" "true"
       Option "DRI" "3"
       Option "AccelMethod" "SNA"
    EndSection

### [Hybrid Graphics]

To offload applications to the dedicated GPU, add the PRIME prefix before the command:

`user `[`$`]`DRI_PRIME=1 command_here`

### [Configuring the touchpad]

This enables horizontal scrolling. Tapping with two fingers acts as a rightclick, and a tap with three fingers acts as a middleclick.

[CODE] **/etc/X11/xorg.conf.d/40-synaptics.conf**

    Section "InputClass"
        Identifier "Touchpad Catchall"
        Driver "synaptics"
        MatchIsTouchpad "yes"
        Option "TapButton1" "1"
        Option "TapButton2" "3"
        Option "TapButton3" "2"
        Option "CornerCoasting" "1"
        Option "AccelFactor" "0.05"
        Option "HorizTwoFingerScroll" "1"
        Option "FingerHigh" "40"
        Option "CoastingSpeed" "0"
        Option "CoastingFriction" "0"
        Option "ClickTime" "15"
    EndSection

It is also possible to enable Synpatics InterTouch which uses RMI4 over SMBus by adding \`psmouse.synaptics_intertouch=1\` to the kernel command line.

## [Troubleshooting]

### [Wrong turbo multipliers]

Dell seems to have changed the [MSR](https://en.wikipedia.org/wiki/Model-specific_register) controlling Turbo multipliers and effectively downclocked the processor compared to the stock multipliers. The stock Intel configuration is 30x/27x/27x/27x, Dell changes this to 27x/25x/25x/25x, ie. 2.7GHz with a single core, and 2.5GHz with 2+ cores.

This can be reverted back to the default with the use of [msr-tools](https://github.com/01org/msr-tools).

** Warning**\
The following is for experienced users only. Misuse of these tools can potentially damage/brick your CPU. Proceed only if you know what you are doing.

First, we use the `rdmsr` utility to read the current value of the MSR register:

`root `[`#`]`sudo rdmsr 0x01ad`

This should return the value `1919191b` which corresponds to 27/25/25/25. Note that the order is reversed, the highest multiplier (for single core) in this case is last (1b). Next, we write the new multiplier configuration:

`root `[`#`]`sudo wrmsr 0x01ad 0x1b1b1b1e`

This will set the multipliers to 30/27/27/27.

** Note**\
Setting the wrong multiplier will downclock the CPU to its lowest multiplier. The current configuration can be viewed with [i7z](https://github.com/DimitryAndric/i7z).

### [][Touchpad doesn\'t work after resume]

Sometimes when using RMI4 (Synaptics \"InterTouch\") the touchpad might randomly stop working and requires reinitialization:

`root `[`#`]` echo -n "none" | tee /sys/bus/serio/devices/serio1/drvctl `

`root `[`#`]` echo -n "reconnect" | tee /sys/bus/serio/devices/serio1/drvctl`

## [See also]

-   [Intel](https://wiki.gentoo.org/wiki/Intel "Intel")
-   [Radeon](https://wiki.gentoo.org/wiki/Radeon "Radeon")

## [References]