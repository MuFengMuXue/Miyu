# Laptop/MSI

## Model list
| GE75 Raider 8SX
| 2019-01-08
|
|
|
|
|
|
|
| See dedicated page.
|-
| Modern 15 - A11S
| 2021-06-01
|
|
|
|
|
|
|
|
|-
| P14 A10RB/A10SC/A10RAS
| 2020-06-11
|
|
|
|
|
|
| No fingerprint driver for Linux.
|
|-
| P15 A10SC
| 2020-05-29
|
|
|
|
|
|
| No fingerprint driver for Linux.See #BisonCam.
| Some Fn keys do not work.  Always on Fn keys can be disabled via .
|-
| GV62 7RE
| 2025-02-12
|
|
|
|
|
|
| See #BisonCam
| See #Intel Management Engine For NVIDIA see Optimus.
|-
| PS63 Modern
| 2019-12-22
|
|
|
|
|
|
| See #BisonCam
| Touchpad is disable when wake up from suspend, needs to reset the i2c bus. See custom script.
|-
| GS63VR
| 2019-08-15
|
|
|
|
|
|
|
|
|-
| GS65
| 2018-06-01
|
|
|
|
|
|
|
| Sleep turns on airplane mode.Nouveau does not work.
|-
| GS73VR
| 2017-03-06
|
|
|
|
|
|
|
| See Map scancodes to keycodes for P1  and ECO  key.
|-
| GS75
| 2022-07-017
|
|
|
|
|
|
|
| Sleep turns on airplane mode. NVIDIA preferred for battery life.
|-
| GP602QF
| 2018-06-20
|
|
|
|
|
|
| See #BisonCam.
| For NVIDIA see Optimus.
|-
| GE60-0ND
| 2019-01-30
|
|
|
|
|
|
| See #BisonCam.
| For NVIDIA see Optimus.
|-
| GE66 Raider 10UH-14BE
| 2022-12-05
|
|
|
|
|
|
|
| For NVIDIA see Optimus.
|-
| GF75 Thin 10SC
| 2021-08-16
|
|
|
|
|
|
| See #BisonCam.
|
|-
| GS66 11UX
| 2021-11-24
|
|
|
|
|
|
|
| NVMe drive, Screen refresh rate, and Audio have caveats.
|-
| Alpha 15/17 B5EEK
| 2022-06-09
|
|
|
|
|
|
| MSI Mystic Light is unsupported. You can turn mystic light off. Changing color is not officially supported by Open RGB, but its possible using HID Interface.
| Some Fn keys do not work.Sound quality worse than Windows: absent Nahimic support.
|-
| GP66 Leopard 11UH
| 2023-01-08
|
|
|
|
|
|
|
|
|-
| GF65 Thin 10SER
| 2023-02-06
|
|
|
|
|
|
|
|
|-
| Delta 15 A5EFK
| 2023-12-03
|
|
|
|
|
|
|  can be used to control keyboard lighting. Supergfxctl can be used to switch between the GPUs, as well as PCI passthrough via OVMF.
| Audio/Mic mute LEDs do not work.
|-
| Creator Z16
| 2024-02-24
|
|
|
|
|
|
| No fingerprint driver for Linux.See #BisonCam.
| See BBS#293009 to get keyboard lighting working.
|-
| GP62 7QF
| 2024-09-03
|
|
|
|
|
| *
| colspan=2 | *Hibernation needs tweak
Advanced UEFI settings needed to disable the dGPU
|-
| Bravo 15 B7EDP-024US
| 2024-09-24
|
|
|
|
|
|
|
| Fails to wake up from suspend.
|-
| Prestige 13 AI+ Evo A2VM
| 2024-09-03
|
|
|
|
|
|
| No webcam support
|
|-
| Vector A18 HX A9WX
| 2025-06-15
|
|
|
|
|
|
|
|
|-
| Crosshair 16 HX AI D2XWGKG-054
| 2025-12-30
|
|
|
|
|
|
|
|
|-
|}

## Tips and tricks
## BisonCam
Models with a BisonCam integrated webcam just need to activate it with .

## Embedded Controller
Some models are supported by a community developed driver.

If you need the added functionality, you can install it with  or .

## Intel Management Engine
Intel ME firmware needs to be updated from Windows.

See Windows PE/Tips and tricks#Update Intel Management Engine firmware with the files provided by MSI on their BIOS Update webpage.

It may still reported as vulnerable after update. Intel ME may be disabled in the advanced UEFI settings.

## Advanced UEFI settings
An unlocked version of the UEFI settings is available on most MSI laptops since 2019. To access it, press  or  then  once inside the UEFI.
