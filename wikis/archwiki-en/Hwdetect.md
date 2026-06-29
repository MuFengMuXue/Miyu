# Hwdetect

hwdetect is a hardware detection script primarily used to load or list modules for use in mkinitcpio.conf. As such, it informs its user about which kernel modules are required to drive the hardware. This is in contrast to many other tools, that only query the hardware, and show raw information, leaving the user with the task to associate that information with the required drivers. The script makes use of information exported by the sysfs subsystem employed by the Linux kernel.

## Installation
Install the  package.

## Usage
See the hwdetect source, or run .

## Examples
You can use the following method to populate  in mkinitcpio.conf.

 # hwdetect --show-modules

The command should have similar output to the following (system-dependant):

 SOUND    : pcspkr
 OTHER    : 8139cp 8139too ac

Depending on what is used, copy the module names to replace the  section in . The system should now boot faster, as some, or all, of the hardware detection and modules dependencies calculations is already stated.

## Tips and tricks
## Unused modules
To generate a list of modules currently not used, use the following script:

{{bc|
#!/bin/bash
modules=($(awk '{print $1}' /proc/modules))

for hw in $(hwdetect --show-modules | awk -F: '{gsub("-","_"); print $2}'); do
    if ! grep -q "$hw" <(printf '%s\n' "${modulesthen
        printf '%s\n' "$hw";
    fi
done
}}

## Higher level modules
The converse script is also of interest as it lists modules which are higher level, in the sense that they are less related to specific pieces of hardware:

{{bc|
#!/bin/bash
lowlevel=($(hwdetect --show-modules | awk -F: '{gsub("-","_"); print $2}'))

for mod in $(awk '{print $1}' /proc/modules); do
    if ! grep -q "$mod" <(printf '%s\n' "${lowlevel[@}"); then
        printf '%s\n' "$mod";
    fi
done
}}
