# Undervolting CPU

Undervolting is a process where voltage to CPU is reduced in order to reduce its energy consumption and heat without affecting performance. Note that most desktop motherboards allow tweaking CPU voltage settings in BIOS as well.

## Background
Modern CPUs implement frequency scaling, where the operating frequency is dynamically adjusted to save power when idle and increase performance when under use. As frequency increases, the voltage required to switch the gate quickly enough also increases, so CPUs also scale their voltage alongside the frequency. The default frequency-voltage curve is relatively conservative, and depending on the silicon lottery (how much your CPU's logic gates outperform the curve's expected parameters), a lower voltage can be used without lowering the frequency.

Because power dissipation is related to the square of voltage, undervolting can cause significant power savings and heat reduction. A lower voltage is also usually associated with a longer lifespan of the device, as most semiconductor deterioration mechanisms (BTI, electromigration) are at least partly temperature and voltage-dependent.

Risks of undervolting include incorrect calculation results (possibly complete failure to boot) due to using voltages that are not sufficient for a frequency. Be prepared to reboot your system or reset your BIOS through the JBAT jumper to undo your undervolt.

To test the stability and correctness of an undervolt, stress testing using an application with built-in numerical checks (mprime, linpack) is strongly recommended. Just booting isn't sufficient as calculation errors can result in unexpected, potentially dangerous, program behavior (as demonstrated by "undervolt attacks"). As CPUs age, the gates may also become more sluggish and require higher voltage to stabilize, so be prepared to revise your undervolting settings.

## The voltages
On Intel CPUs you can separately control the core, cache, System Agent (also known as NB/SOC/Uncore) and the integrated GPU voltages. If there is integrated analog I/O you can control that part's voltage too. The core and the cache are self-explanatory. The System Agent includes the memory controller.

On Zen-based AMD CPUs you can separately control core, NB/SOC/Uncore, VDDG_CCD, VDDG_IOD, VDDP_CLDO, and PLL/1P8. The first two are similar to their Intel counterparts. VDDG_CCD is for signaling from cores to the IO die. VDDG_IOD is for signaling from the IO die to the cores. VDDP_CLDO is for the memory controller. The PLL/1P8 voltage is the voltage of the base clock signal.

When you lower one voltage, make sure to run the corresponding test in mprime. For example, if you touch the memory controller or SOC-related voltages, run the Large test.

## How far can you go?
Decreasing Intel CPU and CPU Cache by 100 to 200 mV is usually (outwardly) stable. Going above 200 mV may result in a crash, or may not have any effect at all.

## When undervolting is necessary
A number of AM5 (Ryzen 7xxx, 9xxx) motherboards are known to apply an overly high SOC/Uncore voltage when EXPO is enabled. This has lead to a number of CPU failures with discolored areas or even bulges corresponding to the IO die. A BIOS update should be applied to fix the problem. If no update is available and the SOC voltage remains above 1.3&nbsp;V, manual undervolting should be performed in BIOS.

There is a similar issue in 13th and 14th generation Intel CPUs where the core voltage is too high, causing accelerated aging. A microcode update should fix this issue.

## intel-undervolt
Intel-undervolt is a tool based on this article for undervolting Haswell and newer Intel CPUs using MSR and MCHBAR registers. In addition, it also allows to change power and temperature limits. It is not compatible with Tiger Lake and above, but is compatible with .

## Installation
The tool can be installed as .

## Configuration and usage
The following command prints in use voltage settings:

 # intel-undervolt read

Now edit the configuration file . Example configuration with undervolted CPU Cache by -100mV:

Once you saved configuration file - test it:

 # intel-undervolt apply

It will print Success if settings were applied. You can double check in use configuration using the following command:

 # intel-undervolt read

Once you find stable configuration, you can also enable  to make changes persistent.

## amdctl
amdctl is a tool for undervolting K10 and newer AMD CPUs.

## Installation
The tool can be installed as .
