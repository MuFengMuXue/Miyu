# Install Arch Linux with accessibility options

The official Arch Linux installation medium supports various Accessibility features:

* speech is provided by the  package
* braille terminal support is handled by the  package

This document describes how to install Arch Linux using these features.

## Pre-installation
## Boot the live environment
When the installation medium starts booting, press  followed by
 to boot with speech enabled.

USB braille displays should be detected automatically via udev.

## Multiple sound cards
If your computer has several sound cards, you will hear the following message: Please select your sound card for speech output.

When you hear a beep on the output that you would like to use, press  to select the card.

## Change speech language
To change the espeak-ng language/voice used by , edit the unit so that the language code is appended to  in the  directive.

You can also change the espeak-ng voice variant by appending  to the language code. See  and  for more information.

## Installation
## Install essential packages
For speech support in the installed system, you need  and . If you use a braille display, install the  package.

Append the required packages to the  call when installing:

 # pacstrap -K /mnt base linux linux-firmware espeakup alsa-utils

## Configure the system
## Sound card
If #Multiple sound cards were detected, copy the  file, which has been generated in the installation medium:

 # cp /etc/asound.conf /mnt/etc/

## Enable the services
To have speech support after booting into the installed system you need to enable . See also #Change speech language.

## Reboot
After booting into the newly installed system it should start speaking automatically.

## Troubleshooting
See Accessibility#Troubleshooting.
