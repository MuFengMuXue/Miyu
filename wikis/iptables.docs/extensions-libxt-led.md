# Extensions / Libxt LED

This creates an LED-trigger that can then be attached to system indicator lights, to blink or illuminate them when certain packets pass through the system. One example might be to light up an LED for a few minutes every time an SSH connection is made to the local machine. The following options control the trigger behavior:

**--led-trigger-id** *name*
This is the name given to the LED trigger. The actual name of the trigger will be prefixed with "netfilter-".

**--led-delay** *ms*
This indicates how long (in milliseconds) the LED should be left illuminated when a packet arrives before being switched off again. The default is 0 (blink as fast as possible.) The special value *inf* can be given to leave the LED on permanently once activated. (In this case the trigger will need to be manually detached and reattached to the LED device to switch it off again.)

**--led-always-blink**
Always make the LED blink on packet arrival, even if the LED is already on. This allows notification of new packets even with long delay values (which otherwise would result in a silent prolonging of the delay time.)

Example:
Create an LED trigger for incoming SSH traffic:
iptables -A INPUT -p tcp --dport 22 -j LED --led-trigger-id ssh

Then attach the new trigger to an LED:
echo netfilter-ssh \>/sys/class/leds/*ledname*/trigger
