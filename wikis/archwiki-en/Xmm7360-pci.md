# Xmm7360-pci

Thinkpads with an AMD processor since 2020 (e.g. Lenovo Thinkpad L/T14 (AMD) Gen 1, Lenovo ThinkPad T14s (AMD) Gen 1, Lenovo Thinkpad L15 (AMD) Gen 1) connect only PCIe to the LTE modem.

Fibocom "supports" Linux only in USB mode. There is no sign of an official driver being developed. For newer generations (L860 ?),  Lenovo is developing a driver.

To get this hardware working on Linux, the only solution is an alpha stage driver, written with Python 3, found at https://github.com/xmm7360/xmm7360-pci.

This driver is intended to work with Fibocom L850-GL LTE, without switching to USB (since it is not supported on AMD models) but with direct commands to the modem. To verify if you have this hardware, do the following:

## Preparation
Install  and  along with ,  and .

Remove the PIN in Windows and check that it is a working card.

Alternatively echo the PIN with

 # echo "AT+CPIN=\"0000\"" >> /dev/ttyXMM1

after the  steps.

Replace  with your pin code. (c.f. https://github.com/xmm7360/xmm7360-pci/pull/21/files)

## Installation
## Linux Kernel support and Modem Manager integration
Support for this device has been added since Linux 5.18 (see torvalds/linux@1f52d7b). ModemManager accesses such WWAN modems via MBIM interface, provided by the iosm kernel module. The GL-860 does provide a MBIM interface, the GL-850 does not. Fibocom/Intel don't seem to care, there is no announcement/rumor that they will be implementing it.

That is why xmm7360-pci/issue/31 correctly states that even with the kernel driver, the modem doesn't work: With iosm kernel module loaded, the interface shows up as /dev/wwan0at0 and /dev/wwan0at1, and is seen by mmcli -L, but journalctl yields SIM not inserted:

 ModemManager:     /sys/devices/pci0000:00/0000:00:02.5/0000:05:00.0
                         creating modem with plugin 'Intel' and '3' ports
 ModemManager:     could not grab port wwan0at0:
                         Cannot add port 'wwan/wwan0at0', unhandled port type
 ModemManager:     [base-manager modem for device '/sys/devices/pci0000:00/0000:00:02.5/0000:05:00.0'
                         successfully created
 ModemManager:     couldn't load supported IP families: SIM not inserted
 ModemManager:     [modem3 state changed (unknown -> locked)
 ModemManager:     modem couldn't be initialized: Couldn't check unlock status: SIM not inserted
 ModemManager:     [modem3 state changed (locked -> failed)
 ModemManager:     error initializing: Modem in failed state: sim-missing
 ModemManager:     [1673136941.3379 manager: (wwan0at1): new Broadband device
                         (/org/freedesktop/NetworkManager/Devices/11)
 NetworkManager:   device (wwan0at1): state change: unmanaged -> unavailable
                         (reason 'managed', sys-iface-state: 'external')
 NetworkManager:   [1673136941.3385 device (wwan0at1): modem state 'failed'
 NetworkManager:   modem-broadband[wwan0at1:
                         failed to retrieve SIM object: No SIM object available

There is ongoing development in ModemManager/issue/612: A patch was accepted in Linux 6.2rc1 that adds a low-level mbim.rpc interface intended to ultimately be used as kernel module which shall be script-glued into ModemManager (and be compatible to the xmm7360-pci python3 rpc/open_xdatachannel.py script). However, that repo is no longer maintained. However, some users did manage to get the module to work within ModemManager.
