# Tomu

The Tomu is a family of open-source FIDO2 security keys. This article describes how to set up and use it. So far this page is limited to The original Tomu – help to expand it.

## The original Tomu
## Dependencies
To build Tomu images, you will need to install  and . To flash software on the Tomu, use .

## Verifying
Your Tomu should arrive with dfu-util installed. If you insert Tomu into the USB port and toboot starts, the green and red led should flash alternately. To check if your Tomu is running the boot loader toboot, and which version, run:

## Update the boot loader (toboot)
If the boot loader of your Tomu is not the newest version, you should update it. You can compile it yourself, or download a prebuilt version. Install the update like this:

 # dfu-util -d 1209:70b1 -D toboot-booster.dfu

## Installing other software
If you do not want to use Tomu as U2F token but use it for different purposes, you can find example applications on GitHub. They can be installed with df-util:

 # dfu-util -d 1209:70b1 -D application.dfu

## Installing U2F firmware (chopstx port)
The code for the U2F firmware for Tomu can be found on GitHub. Clone it with git and compile it:

You have two options:

* Flash it without a key: If flashed without a key, the firmware generates EC private key on its first boot and erases it when it enters the boot loader! You cannot create a backup. But this has the advantage that the key will never exist outside Tomu. Make sure to have an alternative second factor or recovery possibility. You cannot update the software without losing the private key.
* Inject a private key: Generate a key on your computer, inject it into the firmware and flash them together to the Tomu.

## Injecting a private key (optional)
Generate your private key:

 $ openssl ecparam -name prime256v1 -genkey -noout -outform der -out key.der

You may want to back it up encrypted and/or offline. Inject it to the build:

 $ ./inject_key.py --key key.der

## Flashing
You can flash the software to the device:

 # dfu-util -v -d 1209:70b1 -D build/u2f.bin

When the flashing is successful, the LEDs should have stopped flashing. Remove it and plug it in again – with the U2F software the red LED should flash only very shortly and quickly.

## Updating or restoring
If you have injected a private key, you can build the software again and inject the key. You must however set the counter to a value at least 1 higher than it was on the Tomu:

 $ ./inject_key.py --key key.der --ctr 1001

If you still have the original Tomu (i.e. you want to update) you can find out the counter in the Yubikey demo site. Otherwise, set it to a value "big enough".

## Usage
You can use https://webauthn.io/ or the Yubikey demo site to test your U2F key or with pamu2fcfg on terminal:

Plug the Tomu in. When the application (for example your browser) asks you to press the button, the red LED on the Tomu starts to blink. You have now to press the "lower button". The capacitive buttons are the four contact areas on the end of the Tomu. The "lower" one is from watching at it from the side with the chip on it. Press it with your finger – it can be tricky to reach – in worst case use a metal screwdriver or similar. When you pressed it, the red LED stays on for a few seconds then the application receives the answer.
