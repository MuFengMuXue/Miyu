# Powertop

Powertop is a tool provided by Intel to enable various powersaving modes in userspace, kernel and hardware. It is possible to monitor processes and show which of them are utilizing the CPU and wake it from its Idle-States, allowing to identify applications with particular high power demands.

## Installation
Install the  package.

## Usage
Powertop's interactive mode can be invoked with:

 # powertop

In interactive mode, you can modify recommended settings in the Tunables and WakeUp tabs. This allows you to change settings and monitor how they affect your power consumption in the Overview tab. However this does not persist any settings and the changes will be lost on reboot.

## Generate reports
Powertop can generate reports in either CSV or HTML format. The HTML export is an interactive document that shows recommended settings. Make sure to reboot to revert to system defaults before generating a report!

You can also extract the recommended parameters by following these steps:
# Use powertop to produce a report on parameters:
# Open the report in your favorite web browser. The "Tuning" tab of the report now shows the actual parameters suggested by the tool to apply to save power. You may extract the commands with {{bc|$ awk -F '' '/tune/ { print $4 }' powerreport.html}}

Newer versions of Powertop include the  option which will output the commands Powertop's  would have run. This is useful for including in a script in case you do not want to run all of Powertop's recommendations.

## Apply settings
There are two ways to automatically apply the suggested settings:

* Recommended: You can apply these settings at boot by using module parameters, udev rules and sysctl. For details, see the power management page. You can also use the  helper to apply the settings via systemd-tmpfiles.
* You can use the  feature from powertop which sets all tunable options to their GOOD setting. This can be combined with the systemd service to have the tunables set on boot. Remember to enable/start the service.

You can also add this line to the  section in order to prevent your plugged-in USB input devices from getting disconnected on boot:

 ExecStartPost=/bin/sh -c 'for f in $(find /sys/bus/usb/drivers/usbhid -regex '.*\/-printf '%f\n' | cut -d ":" -f 1 | sort -u); do echo on >| "/sys/bus/usb/devices/$f/power/control"; done'

## Troubleshooting
## Error: Cannot load from file
If you receive an error like the following when starting powertop, it is likely that powertop has not collected enough measurement data yet. To fix this, keep powertop running for a certain time connected to battery power only.

 Loaded 39 prior measurements
 Cannot load from file /var/cache/powertop/saved_parameters.powertop
 Cannot load from file /var/cache/powertop/saved_parameters.powertop

## Calibration to prevent inaccurate measurement
If you experience inaccurate measurement, then it is likely that you need to calibrate powertop first. This can be done by running powertop with the  parameter.

 # powertop --calibrate

## Display power estimation
Prior to displaying the power usage estimation column, powertop needs to run 270 measurements. Each one lasts 20 seconds, which means you need to let powertop run for 1h30 in total.
