[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Logitech_G533&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

This is a wiki entry about using [Logitech G533](https://www.logitechg.com/en-roeu/products/gaming-audio/g533-wireless-gaming-headset.html) wireless headset on Gentoo.

## Contents

-   [[1] [Requirements]](#Requirements)
    -   [[1.1] [Software]](#Software)
    -   [[1.2] [Kernel]](#Kernel)
-   [[2] [Troubleshooting]](#Troubleshooting)
    -   [[2.1] [USB Receiver]](#USB_Receiver)
        -   [[2.1.1] [LED is blinking]](#LED_is_blinking)
        -   [[2.1.2] [LED is ON]](#LED_is_ON)
        -   [[2.1.3] [LED is OFF]](#LED_is_OFF)

## [Requirements]

### [Software]

[ALSA](https://wiki.gentoo.org/wiki/ALSA "ALSA")

[PulseAudio](https://wiki.gentoo.org/wiki/PulseAudio "PulseAudio")

pavucontrol is recommended.

**dts** USE is recommended for virtual sound functionality.

### [Kernel]

[KERNEL]

    Device Drivers ->
      Sound card support ->
        Advanced Linux Sound Architecture ->
          USB sound devices ->
            <*/M> USB Audio/MIDI driver
          HD-Audio ->
            <*/M> Build Realtek HD-audio codec support

## [Troubleshooting]

### [USB Receiver]

USB receiver has green LED under \"G\" logo we assume that USB receiver is plugged in system\'s USB port.

#### [LED is blinking]

1.  There is no drivers for USB receiver detected.
    -   Check requirements above.
    -   If you confirmed that software + kernel configuration is present share your experience in talk page.
2.  USB Receiver is not paired.
    -   There are two \"holes\" on USB receiver and headset. Take a paper clip and insert it in USB receiver and headset.
        -   Holes are located:
        -   USB receiver = above LED and under \"G\" logo.
        -   Headset = Left reproducer above \"G\" logo. Note that it is hidden under plastic piece of skeleton, NO disassembly is required.
        -   Press and hold until both USB receiver and headset are blinking rapidly which indicated pairing mode.

** Warning**\
USE light pressure or you might damage the hardware button forcing it in constant ON position which results in permanent pairing mode

#### [LED is ON]

1.  Connection with headset is successful and there is no issue from headset and USB receiver.
    -   If the headset is still not working check \`pavucontrol\`. We can eliminate issue with USB receiver and headset from troubleshooting.

#### [LED is OFF]

1.  Corrupted firmware.
    -   Logitech provides software called \"Logitech Gaming Software\" which support only windows. If you install it using wine or VirtualBox on windows there is \"FWupdate\" folder in it\'s root directory which has firmware recovery software for all supported hardware saved in .exe to recover your firmware. Warning: if using VirtualBox you need to remount the USB connection for USB receiver and headset multiple times. Installation will freeze until remount it completed.
2.  Hardware damage.
    -   USB receiver - New USB receiver costs around 50\$ on websites like eBay, etc.. If you have experience with micro-solder you can probably fix it yourself.

**Photos of stripped USB receiver:**\
[![G533 USB Reciever front.jpg](/images/c/cd/G533_USB_Reciever_front.jpg)](https://wiki.gentoo.org/wiki/File:G533_USB_Reciever_front.jpg) [![G533 USB Reciever back.jpg](/images/9/96/G533_USB_Reciever_back.jpg)](https://wiki.gentoo.org/wiki/File:G533_USB_Reciever_back.jpg)

**Recommended approach:** Best practice is to attack from USB side to split open the plastic casing which has the least possibility of damaging the receiver and it\'s casing. Note photos above to avoid any components during this attack.

Receivers are made by Avnera you can probably get same receiver from other headset (which are widely-used across multiple vendors) and reverse-engineer firmware from mentioned software above to reprogram it.