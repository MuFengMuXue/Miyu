# Scanner Button Daemon

The majority of the desktop scanners are more or less "passive" devices: They might function with a suitable application but are unable to be used by buttons only.

scanbd tries to solve the problem with managing such scanners to make use of the scanner-buttons they have (only when the buttons are supported by sane).

## How does it work?
scanbd (the scanner button daemon) opens and polls the scanner and therefore locks the device. So no other application can access the device directly (open the /dev/..., or via libusb, etc).

To solve this, a second daemon is used (in the so called "manager-mode" of scanbd): scanbm is configured as a "proxy" to access the scanner and, if another application tries to use the scanner, the polling daemon is ordered to disable polling for the time the other scan-application wants to use the scanner.

To make this happen, scanbm is configured instead of saned as the network scanning daemon. If a scan request arrives on the sane-port, scanbm stops the polling by sending a dbus-signal to the polling scanbd-daemon. Then it starts the real saned which scans and sends the data back to the requesting application. Afterwards the scanbd-manager scanbm restarts the polling by sending another dbus-signal to scanbd.

Due to the above, the set up of the scanbd requires changes in default configuration of SANE and also definition of own action scripts (defining what should be done when a button on the scanner is pressed).

There are also alternatives to scanbd, eg. scanbuttond, however these seem to be unmaintained nowadays.

## Installation
Install the  package.

## Sane configuration
Since scanbd and saned are running on the same machine as the scanner is connected to, we need to have two sets of saned configurations - one in the default location (), which would redirect local applications to a network socket, that systemd is listening on, and another one (e.g. ), which will be actually used by sane backend to access the attached scanner.

First, copy all configuration files from  to  (these will be needed later):

 # cp -r /etc/sane.d/* /etc/scanbd/sane.d/

Modify  so that it includes only the "net" directive (either delete the other directives (printers), or comment them with # symbol):

Modify the net-backend configuration file (see scanbd's README.txt for more complicated setups):

Now the desktop applications (which use libsane) are forced (by the above dll.conf) to use the net-backend only. This prevents them from using the locally attached scanners directly (and blocking them).

Whenever there is a connection to the standard sane network socket, systemd starts scanbm ("manager mode" of scanbd), which in turn tells (the already running) scanbd to stop polling the scanner and then it starts saned with the alternative configuration directory.

The last step is to modify the alternative configuration of sane in : just make sure that the "net" directive is commented and the corresponding scanner-backends are uncommented:

Now it is time to start/enable  and start .

You can check the  and  unit status to see if the scanbd service and scanbm socket were started. To increase debugging verbosity, change  in  and restart the scanbd service.

If keeping the default user daemon and group scanner in , make sure you've added daemon to the scanner group, otherwise scanbm won't work.

## scanbd configuration
If you are lucky, your scanner might work almost out of the box and you would only want to modify the action scripts, which define what is done when a particular button is pressed.

scanbm listens to scanner's status and on the basis of messages received, it decides what to do. The standard behaviour is defined in . E.g. the action scan:

 action scan {
         filter = "^scan.*"
         numerical-trigger {
                from-value = 1
                to-value   = 0
                }
         desc   = "Scan to file"
         script = "test.script"
        }

Whenever the message from the scanner includes word "scan" (see reg-exp for more details on filters) and the value changes from 1 to 0, then it runs script .

 does not do anything but sends a message to syslog:

There are a few other scripts available in  that actually do something - have a look yourself.

Also,  has "include" directives at the end, which refer to preconfigured button definitions of a few printers.

 $ cat /etc/scanbd/scanbd.conf | grep include\(
 # include("scanner.d/myscanner.conf")
 # include("/my/long/path/myscanner.conf")
 include(scanner.d/avision.conf)
 include(scanner.d/fujitsu.conf)
 include(scanner.d/hp.conf)
 include(scanner.d/pixma.conf)
 include(scanner.d/snapscan.conf)
