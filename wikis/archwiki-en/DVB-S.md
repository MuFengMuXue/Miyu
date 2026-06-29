# DVB-S

DVB-S is a satellite television standard. This article describes the setup and use of DVB-S cards on Arch Linux.

## Load required kernel modules
You have to lookup the chipset of your specific card; tools like  may help you.

## Pinnacle PCTV Sat
This card uses bt878 and cx24110 as chipset. These require the  and  kernel modules.

Load them with modprobe:

 # modprobe dvb-bt8xx
 # modprobe cx24110

You can load the module at boot to automate this step.

## Additional modules: S2-liplianin
Some modules not included in the kernel are available from Igor M. Liplianin's git repository

## Setup
First of all, you have to download and prepare the source code.

 $ git clone https://github.com/crazycat69/szap-s2

To clone the repository will need to install  or alternatively you can download the source code from https://github.com/crazycat69/szap-s2/archive/refs/heads/master.zip and extract it manually.

After obtaining the code, change the working directory to the extracted folder:

 $ cd s2-liplianin

Unfortunately not all modules of liplianin are compatible with recent kernels and cause some trouble if you want to compile them hence you have to exclude these modules from the build process (if you do not need them). You can choose which modules you want to build by executing:

 $ make config

which will create a configuration file: .

After that, you have to build the chosen modules:

 $ make

If all configured modules were compiled successfully, you can install the modules at the kernel's default modules directory by executing:

 # make install

After that, reboot your machine.

## Additional firmware: LibreELEC DVB-firmware
The LibreELEC project provides additional firmware files for various DVB devices, eg. TechniSat SkyStar S2.
To use these firmware files you can install .

## Setup permissions
To use your DVB-S card as user add it to the  group:

 # gpasswd -a video

## Scanning channels
Most applications like szap or xine are needing a channel list created by scan, which is part of dvb-utils.
You will find the dvb-utils package under the name .

## Using scan
scan needs an channel to initialize scanning. In  are some files which contain these channels; you will need that one that fits the satellite you are watching from.

The following command will scan all channels and save them to :

 $ scan -x0 -t1 -s1 /usr/share/dvb/dvb-s/[your satellite | tee channels.conf

## Using w_scan_cpp
 allows for automatic scanning of channels without configuration. Install it then issue:

 # w_scan_cpp -c country > ~/someChannels.conf

Alternatively you can also scan using the satellite position like 19.5E for Astra 1. Scans like that can be done as follows:

 # w_scan_cpp -fs -s S19E5 > ~/someChannels.conf

You can also add the -X flag to generate tzap/czap/xine output instead of vdr output.

 # w_scan_cpp -X -c AU > ~/AustraliaChannels.conf

To get a file that can be loaded with VLC use the -L flag

 # w_scan_cpp -L > ~/AustraliaChannels.conf

## DiSEqC switch scanning (AKA multiple satellite LNB)
If you have a LNB with a DiSEqC switch in it you can manually select that using the -D option like so:

 # w_scan -fs -s S23E5 -D 1c > ~/someChannels.conf

The above line should work but not all found channels where actually saved. The line below worked perfectly for me:

 # w_scan -fs -s S23E5 -a 0 -D 1c -o 7 -e 2 > ~/someChannels.conf

## Switching channels
By using zap, which comes with dvb-utils, you can switch channels, so you do not have to rely on the abilities of your player.

szap needs the channel file we created earlier; it will try  by default. You can move the  there or you can use the  command-line option.

Switching channels works like this:

 $ szap -r You can list all available channels with:

 $ szap -q

Now you can watch the stream for example with xine:

 $ xine -g stdin://mpeg2 < /dev/dvb/adapter0/dvr0

or with mplayer:

 $ mplayer /dev/dvb/adapter0/dvr0

or with mplayer, but using DVB directly:

 $ mplayer "dvb://RTL Television"

You can find all the channel names by running  (assuming the channel list is also in ).

## Software
## Kaffeine
Kaffeine is a really nice player; it supports EPG, time-shifting, and recording. Additionally Kaffeine has built-in channel-searching.

Install it with the  package.

* [https://archlinux.org/packages/search/?q=kaffeine More Information
* Project page

## Me-tv
Me-tv is a simple but powerfull dvb-viewer, supporting EPG, recording and channel-searching with a light-weight gui.

Install Me-tv with the  package.

## Xine
Copy your channel file to .

Watch a specific channel with following command:

 $ xine dvb://or use the playlist editor in Xine
