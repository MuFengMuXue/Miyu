# NAME

tlp - apply laptop power saving settings

# SYNOPSIS

**tlp *command* \[*parameters*\] \[**--** *CONFIG_PARAM***=***value* ... \]**

# DESCRIPTION

**tlp** applies power saving settings manually and controls battery care features.

# COMMANDS

## Profile Management

**start**
Start **tlp** and apply the appropriate TLP profile. Also use to apply a changed configuration or to leave manual mode.

**performance**
Apply the performance profile. Parameters ending in \_AC are used.

**balanced**
Apply the balanced profile. Parameters ending in \_BAT are used.

**power-saver**
Apply the power-saver profile. Parameters ending in \_SAV are used. If there is no \_SAV parameter available for a feature, the \_BAT parameter will be used instead.

**ac**
Apply profile for AC power and enter manual mode. Manual mode means that changes to the power source will be ignored until the next reboot or **tlp start** is run to resume automatic mode.

**bat**
Apply profile for battery power and enter manual mode. Manual mode means that changes to the power source will be ignored until the next reboot or **tlp start** is run to resume automatic mode.

## Battery Care

**setcharge \[*start_threshold* stop_threshold\] \[*battery*\]**
Change battery charge thresholds temporarily. If your hardware supports only a stop threshold, set the start value to 0. Configured charge thresholds will be restored at the next boot or by using **tlp setcharge** again but without the threshold arguments.

**fullcharge \[*battery*\]**
Charge battery to full capacity. This is done by applying vendor presets to the charge thresholds temporarily. Configured charge thresholds will be restored at the next boot or by using **tlp setcharge** without the threshold arguments.

**chargeonce \[*battery*\]**
Charge battery to the stop charge threshold once. This is done by temporarily lifting the start charge threshold. The configured start charge threshold will be restored at the next boot or by using **tlp setcharge** without the threshold arguments.

**discharge \[*battery*\] \[*target_charge_level*\]**
Force a complete or partial discharge of the battery while on AC power.

**recalibrate \[*battery*\]**
Perform a battery recalibration while on AC power: completely discharge the battery and recharge to 100%. The latter is done by temporarily applying vendor presets to the thresholds. Configured thresholds will be restored at the next boot or by using **tlp setcharge**.

## Device Power Management

**usb**
Enable autosuspend for all USB devices except those excluded by default or via configuration.

**bayoff**
Turn off optical drive in UltraBay/MediaBay. The drive may be re-enabled by pulling the eject lever or pushing the media eject button on newer models.

## Information

**diskid**
Print disk ids for configured drives.

**--version**
Print TLP version.

## Configuration

**-- *CONFIG_PARAM***="***value*" ...**
Append configuration parameters to a command. These temporarily override the system configuration during execution of that command only and are not kept afterwards. Disclaimer: this feature exists for the sole purpose of test automation during TLP's development. It is provided as is and there is no support whatsoever.

# AUTHORIZATION

Almost all **tlp** commands require root privileges. To change the TLP profile without root, you may use **tplctl**.

# BATTERY CARE

Availability of the above battery care commands and the possible charge threshold values always depends on laptop vendor or brand, Linux kernel version and TLP version. Check for actual availability, threshold ranges and battery names with **tlp-stat -b**. Follow the link in the **SEE ALSO** section for details.

For laptops with two batteries, the secondary battery must be specified as a command parameter in order to select it. In many cases the main battery will be **BAT0**, the secondary battery **BAT1**. When in doubt, the output of **tlp-stat -b**, which lists all batteries, can help.

# POWER PROFILES

**performance**
Optimizes the system for maximum performance at the cost of higher power consumption. Recommended for demanding workloads. TLP default when running on AC power.

**balanced**
Provides a balance between performance and power consumption. Suitable for general-purpose use. TLP default when running on battery power.

**power-saver**
Optimizes the system for maximum battery life at the cost of reduced performance. Recommended for maximizing battery runtime.

# EXAMPLES

Change thresholds of the main battery to 70 / 90% temporarily:
    tlp setcharge 70 90

Charge the secondary battery to full capacity:
    tlp fullcharge BAT1

Recalibrate the main battery:
    tlp recalibrate

# FILES

*/etc/tlp.conf*

> System-wide user configuration file, uncomment parameters here to override default settings and customization files below.

*/etc/tlp.d/\*.conf*

> System-wide drop-in customization files, overriding defaults below.

*/usr/share/tlp/defaults.conf*

> Intrinsic default settings. DO NOT EDIT this file, instead use one of the above alternatives.

*/run/tlp/run.conf*

> Effective settings consolidated from all above files. DO NOT CHANGE this file, it is for reference only and regenerated on every invocation of TLP.

# EXIT STATUS

On success, 0 is returned, a non-zero failure code otherwise.

# SEE ALSO

**tlpctl**(1), **tlp-stat**(8), **bluetooth**(1), **nfc**(1), **wifi**(1), **wwan**(1).

- TLP documentation: \<https://linrunner.de/tlp\>

- Battery care specifics: \<https://linrunner.de/tlp/settings/bc-vendors.html\>

# BUGS

Report bugs to: \<https://github.com/linrunner/TLP/issues\>.

# AUTHOR

\(c\) 2026 Thomas Koch \<linrunner at gmx.net\>
