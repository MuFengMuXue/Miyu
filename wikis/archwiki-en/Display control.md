# Display control

Display control protocols facilitate software defined manipulation of monitor parameters via auxiliary signalling channels, specifically DDC/CI over I²C or DisplayPort AUX. These permit programmatic adjustment of luminance, contrast, input switching, and power states.
Feature parity and functional availability are strictly governed by the hardware's adherence to the MCCS specification and can vary widely.

In modern Linux environments, display device access is mediated dynamically via  and  device ACLs. This architecture supersedes the requirement for manual assignment to the legacy  group, ensuring granular, session-based permission management.

## Hardware-only
These limited implementations can mostly be found in older laptops. Hardware-only meaning there is no software interface for backlight control so the user can only use preset keyboard keys/combinations or a dedicated rotating-type/sliding-type switch or a knob. Old CRT computer monitors also had hardware brightness control.

## Vendor-specific
Vendor-specific implementations and also some related tools are well presented in Backlight. Vendor-specific ACPI implementations and GPU hacks without a standard kernel interface also fall in this limited category, as do external displays with a custom protocol over UART/USB and similar. These are typically not supported in desktop environments.

## ACPI
ACPI-module implementations are only found in laptops and PCs with integrated displays (such as AIOs), but partially standardized and accessible from software. ACPI implementations with  interface are usually well-supported in desktop environments, but no other display control features are available.

## DPMS
While omnipresent in computer hardware and well-supported in software for a long time, the Display Power Management Signaling only allows for display power management into 2-4 states, but no finer backlight or other control. In TV setups it can switch the panel state at best, but it cannot wake or suspend a TV.

## (E-)DDC/CI
The (Enhanced) Display Data Channel / Command Interface interface carries Monitor Control Command Set (MCCS) over I2C and can complement or even replace DPMS in computer hardware. Even though DDC 1.0 was published in 1994 and E-DDC 1.0 in 1999, the feature has only started to appear in standalone computer monitors in 2010s. Besides power and backlight management it has an extensive command set for controlling all display settings supported in its controller.  (GUI: ) and  (GUI: ) are the tools to look at. For backlight control it is possible to create  interface with , which enables desktop integration, but still needs mainlining.

## eDP v1.2
Embedded Display Port (eDP) introduced a display control protocol in version 1.2 working through the auxiliary DisplayPort channel, superseding DDC/CI in embedded/laptop displays.== HDMI-CEC ==

HDMI - Consumer Electronics Control is an additional I2C-like, but very slow bus for waking and controlling standalone enduser devices such as TVs. Available from HDMI 1.0, it uses pin 13 in a HDMI connector and it needs a tiny bit of additional hardware to drive the bus. Somehow it is typically not supported in PC GPUs so additional hardware is needed. Specialised USB-CEC adapters are not cheap and abundant, a better alternative is to use kernel driver which uses auxiliary channel of DisplayPort for HDMI-CEC signalling, but it works only with [https://docs.kernel.org/admin-guide/media/cec.html#displayport-to-hdmi-adapters-with-working-cec a select few DP-to-HDMI adapters. On the other hand native HDMI-CEC support is normal in ARM single-board computers and certain Android devices. Desktop HDMI-CEC integration in Arch Linux is currently manual, but manageable for simple setups such as waking TV from standby. Supported in userspace primarily through  from  or alternatively with  from .
