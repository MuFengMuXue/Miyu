[Translate this page](//wiki.manjaro.org/index.php?title=Special:Translate&group=page-Undervolt+intel+CPU&language=en&action=page&filter= "Special:Translate")

Other languages:

[English](//wiki.manjaro.org/index.php?title=Undervolt_intel_CPU "Undervolt intel CPU (100% translated)") • ‎[Türkçe](//wiki.manjaro.org/index.php?title=Undervolt_intel_CPU/tr "Düşük voltajlı Intel CPU (16% translated)") • ‎[русский](//wiki.manjaro.org/index.php?title=Undervolt_intel_CPU/ru "Понижение напряжения процессора Intel (100% translated)")

## Contents

-   [[1] [Introduction]](#Introduction)
    -   [[1.1] [Undervolt]](#Undervolt)
    -   [[1.2] [Intel P-state vs cpufreq]](#Intel_P-state_vs_cpufreq)
    -   [[1.3] [Method / Software / History]](#Method_.2F_Software_.2F_History)
-   [[2] [PState undervolt]](#PState_undervolt)
    -   [[2.1] [Method description]](#Method_description)
    -   [[2.2] [Software]](#Software)
        -   [[2.2.1] [kernel module]](#kernel_module)
        -   [[2.2.2] [wrmsr/rdmsr]](#wrmsr.2Frdmsr)
        -   [[2.2.3] [The python soft I mentioned earlier]](#The_python_soft_I_mentioned_earlier)
    -   [[2.3] [Hardware known to work]](#Hardware_known_to_work)

# [Introduction]

## [Undervolt]

Undervolting your CPU reduce its power consumption and heat without harming performance if well done.

If voltage is set too low it can lead to error, crash and reboot.

\

**Warning**

------------------------------------------------------------------------

It\'s not a trivial thing to do, used software can physically harm your computer if wrong value are set.

## [Intel P-state vs cpufreq]

\"CPUfreq --- also referred to as CPU speed scaling --- is the infrastructure in the Linux kernel that enables to scale the CPU frequency in order to save power.\" *Redhat.com docs.*

\"intel_pstate is a part of the CPU performance scaling subsystem in the Linux kernel (CPUFreq). It is a scaling driver for the Sandy Bridge and later generations of Intel processors.\" *Kernel.org docs*

Method to undervolt differ depending on which \"scaling\" is used by your processor, Intel PState start with 2nd gen Intel Core i3/5/7 (Sandy Bridge).

## [][Method / Software / History]

1\. For CPUfreq, PHC is used and method is well documented on arch wiki ([https://wiki.archlinux.org/index.php/PHC](https://wiki.archlinux.org/index.php/PHC)), I will not focus on it as I got no experience with it and no hardware to acquire it.

2\. For PState, a method appeared in August 2017 ([https://github.com/mihic/linux-intel-undervolt](https://github.com/mihic/linux-intel-undervolt)) and shortly after a python soft got written ([https://github.com/xdever/linux-intel-undervolt-tool](https://github.com/xdever/linux-intel-undervolt-tool)).

# [PState undervolt]

## [Method description]

I will take the example of a 0.175V **decrease**: **-** 0.175V.

To achieve that I will need two commands, one for **CPU Core** and the other for **CPU Cache**. (CPU Core and Cache share the voltage plane on my machine, that\'s why two commands instead of one).

\

**Warning**

------------------------------------------------------------------------

These commands are shown for illustrative purpose.

    sudo wrmsr 0x150 0x80000011E9A00000
    sudo wrmsr 0x150 0x80000211E9A00000

explanation:

    # wrmsr is a tool used for writing values to a CPU's machine specific registers (MSR).

    # First value is the register number.
        # It's always 0x150

    # Second value is where and what we write in it.
        # 0x mean hexadecimal.
        # 80000 is constant, meaning is unknown.
        # X <- It's the plane index, it can be (not exhaustive):
            # 0 CPU Core
            # 1 GPU
            # 2 CPU Cache
        # 1 is constant, meaning is unknown.
        # 1 write/read <- I don't know what that mean.
        # E9A00000 offset, it's -0.175V after some magic calculation.
            # -175*1.024 = -179.2 -> -179
            # 179  = 1011 0011
            # -179 = 0100 1101         # invert bits+1 to get negative value.

            # Bits tagged with "c" are constant value, bits tagged with "o" are the calculated offset.
            # ccco oooo oooc cccc cccc cccc cccc cccc
            # 1110 1001 1010 0000 0000 0000 0000 0000
            #    E    9    A    0    0    0    0    0

            # 0xE9A00000

## [Software]

### [kernel module]

You need to have module **msr** enabled for **wrmsr** to work

    modprobe msr

### [][wrmsr/rdmsr]

wrmsr is provided by package **msr-tools** in **AUR**

### [The python soft I mentioned earlier]

If you don\'t want to make the calculation yourself or want to automate undervolt at boot you can use: [https://github.com/xdever/linux-intel-undervolt-tool](https://github.com/xdever/linux-intel-undervolt-tool)

It\'s not heavily used and ~~not available as a package for now~~ it got forked [https://github.com/hedgepigdaniel/linux-intel-undervolt-tool/](https://github.com/hedgepigdaniel/linux-intel-undervolt-tool/) and is available in **AUR** as **linux-intel-undervolt-tool**.

My quick look at **linux-intel-undervolt-tool** files and behaviour:

    /usr/bin/undervolt
      # program written in python
      # if run without elevated right it give command to apply yourself with wrmsr
      # options:
        '-gpu', type=int, help='Undervolt GPU by this amount of millivolts. Must be negative.'
        '-cpu', type=int, help='Undervolt CPU by this amount of millivolts. Must be negative.'
        '-config', type=str, help='Config file to load. Other flags has priority over -config.'
    /etc/undervolt.json
      # contain voltage parameters "cpu" and "gpu"
    /usr/lib/systemd/system/undervolt.service
      # a systemd service enabled and started which restart after suspend/hibernate/hybrid-sleep with: -config /etc/undervolt.json
    /etc/modules-load.d/undervolt-msr.conf
      # load msr module at startup

## [Hardware known to work]

  -------------- ------------- ----------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Manufacturer   Model         CPU         Info source
  MSI            GS40 6QE      I5-6300HQ   [https://forum.manjaro.org/t/undervolt-recent-intel-cpu/41948/5](https://forum.manjaro.org/t/undervolt-recent-intel-cpu/41948/5) (This wiki page author)
  DELL           XPS 15 9560   I7-??????   [https://github.com/xdever/linux-intel-undervolt-tool](https://github.com/xdever/linux-intel-undervolt-tool) (linux-intel-undervolt-tool author)
  ???            ???           I7-6700HQ   [https://github.com/mihic/linux-intel-undervolt](https://github.com/mihic/linux-intel-undervolt) (undervolt method author)
  -------------- ------------- ----------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Feel free to report [here](https://forum.manjaro.org/t/undervolt-recent-intel-cpu/41948) with \"@Yoy0\" if you want me to append this list.