# Bluetooth headset

There are three Bluetooth audio systems (profiles bluetooth):

* A2DP (advanced audio distribution) provides music-grade stereo output (sink), typically without input (source).
** A2DP can use a variety of codecs. The standard SBC has a poor quality-bitrate tradeoff, but much better, open-source alternatives (LDAC, AptX) have become widespread.
** AVRCP is used on top of A2DP to provide playback control.
* HFP/HSP (hands-free/headset) provides voice-grade mono output and input. HFP builds on top of HSP.
* LE Audio is a low-energy audio standard announced in 2020. The standard codec is LC3.

The kernel, BlueZ 5, and PipeWire support all three profiles. Older sound servers such as PulseAudio and ALSA only support A2DP and HFP/HSP. Although Bluetooth is infamous for being unreliable many implementations have seen massive improvements, making it a somewhat less excruciating experience on well-established hardware like Intel Bluetooth chips.

## Headset via PipeWire
PipeWire acts as a drop-in replacement for PulseAudio and offers an easy way to set up Bluetooth headsets. It includes out-of-the-box support for A2DP sink profiles using SBC/SBC-XQ, AptX, LDAC or AAC codecs, and HFP/HSP.

Install  (which replaces  and ).

The daemon will be started automatically as a user service. Use  or your desktop environment's settings for configuration. For more information, see PipeWire#Bluetooth devices.

As of February 2025, the LE audio system is still experimental and therefore the LC3 codec is disabled by default, but with some effort it could be used. See the PipeWire wiki [https://gitlab.freedesktop.org/pipewire/pipewire/-/wikis/LE-Audio-+-LC3-support for updates. Alternatively, monitor this thread === Troubleshooting ===

## High audio volume due to synchronization between headphones and PipeWire
Since [https://gitlab.freedesktop.org/pipewire/pipewire/-/releases/0.3.26 version 0.3.26, PipeWire uses "hardware volume" to link the volume of the headphones with the system, making it impossible to change one without the other. On some devices, this may result in the lowest possible volume being uncomfortably loud, and volume controls becoming too coarse. Hardware volume can be disabled using either WirePlumber or Pipewire Media Session.

## Using WirePlumber
If it does not exist, create the directory and file  to disable hardware volume system-wide, or  to disable it only for your user. Edit the file to contain the following:

 monitor.bluez.properties = {
   bluez5.enable-hw-volume = false
 }

If you want to disable hardware volume for a specific device, add the following rule:

 monitor.bluez.rules = [
   {
     matches = [
       {
         device.name = "~bluez_card.XX_XX_XX_XX_XX_XX"
       }
     ]
     actions = {
       update-props = {
         bluez5.hw-volume = }
     }
   }

Reboot the system or restart the PipeWire and WirePlumber services for the changes to take effect.

## Using Pipewire Media Session
If it does not exist, create the directory  to disable hardware volume system-wide, or  to disable it only for your user. Then, copy  to the directory you created. Edit the file, and add the line
 bluez5.enable-hw-volume = false

Reboot the system or the PipeWire services for the changes to take effect.

## Headset via Bluez5/PulseAudio
Install the ,  and  packages, the last of which provides the  utility.

## Configuration via CLI
Start .

Now we can use the bluetoothctl command line utility to pair and connect. For troubleshooting and more detailed explanations of bluetoothctl see the Bluetooth article. Run

 $ bluetoothctl

to be greeted by its internal command prompt. Then enter:

 power on
 [bluetooth# agent on
 default-agent
 [bluetooth# scan on

Now make sure that your headset is in pairing mode. It should be discovered shortly. For example,

 Device 00:1D:43:6D:03:26 Lasmex LBT10

shows a device that calls itself "Lasmex LBT10" and has MAC address "00:1D:43:6D:03:26". We will now use that MAC address to initiate the pairing:

 [bluetooth# pair 00:1D:43:6D:03:26

After pairing, you also need to explicitly connect the device (if this does not work, try the  command below before attempting to connect):

 connect 00:1D:43:6D:03:26

If you are getting a connection error  retry by killing existing PulseAudio daemon first:

 $ pulseaudio -k
 [bluetooth# connect 00:1D:43:6D:03:26

Finally, if you want to automatically connect to this device in the future:

 trust 00:1D:43:6D:03:26

If everything works correctly, you now have a separate output device in PulseAudio.

You can now redirect any audio through that device using the "Playback" and "Recording" tabs of .

You can now disable scanning again and exit the program:

 [bluetooth# scan off
 exit

## Setting up auto connection
To make your headset auto connect you need to enable PulseAudio's switch-on-connect module. Do this by adding the following lines to :

## Configuration via GNOME Bluetooth
You can use GNOME Bluetooth graphical front-end to easily configure your bluetooth headset.

First, you need to be sure that  systemd unit is running.

Open GNOME Bluetooth and activate the bluetooth. After scanning for devices, you can connect to your headset selecting it on the device list. You can directly access to sound configuration panel from the device menu. On the sound panel, a new sink should appear when your device is connected.

## LDAC/aptX
LDAC/aptX codecs are supported as of [https://www.freedesktop.org/wiki/Software/PulseAudio/Notes/15.0/#supportforldacandaptxbluetoothcodecsplussbcxqsbcwithhigher-qualityparameters PulseAudio 15.0. You can verify the codec you are using for connection as follows:

 $ pactl list | grep a2dp_codec

## Troubleshooting
## Bad sound / Static noise / "Muddy" sound
If you experience bad sound quality with your headset, it could in all likelihood be because your headset is not set to the correct profile.
See #Switch between HSP/HFP and A2DP setting to solve the problem.

If you suspect the bad sound quality is due to a poor bluetooth connection, you might compensate for it by switching to a lower bit-rate and lower audio quality codec such as SBC or aptX using :

 $ pactl send-message /card/bluez_card.XX_XX_XX_XX_XX_XX/bluez switch-codec '"sbc"'

where a list of available codecs can be obtained by:

 $ pactl send-message /card/bluez_card.XX_XX_XX_XX_XX_XX/bluez list-codecs

## Selected audio profile, but headset inactive and audio cannot be redirected
Deceptively, this menu is available before the device has been connected; annoyingly it will have no effect. The menu seems to be created as soon as the receiver recognizes the device.

Make sure to run  as root and connect the device manually. There may be configuration options to remove the need to do this each time, but neither pairing nor trusting induce automatic connecting for me.

## Pairing fails with AuthenticationFailed
If pairing fails, you can try enabling or disabling SSPMode with:

 # btmgmt ssp off

or

 # btmgmt ssp on

You may need to turn off Bluetooth while you run this command.

## Pairing works, but connecting does not
You might see the following error in bluetoothctl:

 connect 00:1D:43:6D:03:26
 Attempting to connect to 00:1D:43:6D:03:26
 Failed to connect: org.bluez.Error.Failed

To further investigate, check the unit status of  or have a look at the log as follows:

 # journalctl -n 20

You might see a message like this:

 bluetoothd[5556: a2dp-sink profile connect failed for 00:1D:43:6D:03:26: Protocol not available

This may be due to the  package not being installed. Install it if it is missing, then restart PulseAudio.

It can also be due to permission, especially if starting PulseAudio as root allows you to connect.
See  for reference.

If the issue is not due to the missing package, the problem in this case is that PulseAudio is not catching up. A common solution to this problem is to restart PulseAudio. Note that it is perfectly fine to run bluetoothctl as root while PulseAudio runs as user. After restarting PulseAudio, retry to connect. It is not necessary to repeat the pairing.

If restarting PulseAudio does not work, you need to load module-bluetooth-discover.

 # pactl load-module module-bluetooth-discover

The same load-module command can be added to .

If that still does not work, or you are using PulseAudio system-wide mode, also load the following PulseAudio modules (again these can be loaded via your  or ):

 module-bluetooth-policy
 module-bluez5-device
 module-bluez5-discover

It is also possible there are no write permissions for the owner of . If this is the case, you may get the device to work by removing and re-pairing it, but the issue will return after rebooting. Restoring write permissions fixes this issue:

 # chmod -R u+w /var/lib/bluetooth

## Connecting works, but there are sound glitches all the time
This is very likely to occur when the Bluetooth and the Wi-Fi share the same chip as they share the same physical antenna and possibly band range (2.4GHz). Although this works seamlessly on Windows, this is not the case on Linux.

A possible solution is to move your Wi-Fi network to 5GHz so that there will be no interference. If your card/router does not support this, you can upgrade your Wi-Fi drivers/firmware.

If nothing of the previous is possible, a less effective mitigation is to tweak the fragment size and the latency on PulseAudio output port, trying to compensate interference. Reasonable values must be chosen, because these settings can make the audio out of sync (e.g. when playing videos). To change the latency of the bluetooth headset's port (e.g. to 125000 microseconds in the following example):

 $ pactl set-port-latency-offset  headset-output 125000

where the identifier of the card can be found with

 $ pacmd list-sinks | grep -Eo 'bluez_cardThe fragment size can be set in  and takes effect after a restart of PulseAudio (for more details please see PulseAudio/Troubleshooting#Setting the default fragment number and buffer size in PulseAudio).

Perhaps it will help to add  to the  (with the appropriate bluetooth adapter):

Then restart.

Severe stuttering has also been reported on certain bluetooth adapters when bluetooth scanning is on, and several devices are broadcasting their presence.

To confirm, disable bluetooth scanning:

 $ bluetoothctl
 [bluetooth# scan off
 exit

Ensure no other bluetooth manager such as  is overriding this. For instance, if the "search" function is triggered.

## Connecting works, but there is no sound
Make sure that you see the following messages in your journal:

 bluetoothd[5556: Endpoint registered: sender=:1.83 path=/MediaEndpoint/A2DPSource
 bluetoothdEndpoint registered: sender=:1.83 path=/MediaEndpoint/A2DPSink

If you see a message similar to this, you can go on and investigate your PulseAudio configuration. Otherwise, go back and ensure the connection is successful.

When using GDM, another instance of PulseAudio is started, which "captures" your bluetooth device connection. This can be prevented by masking the PulseAudio socket for the GDM user by doing the following:

 # mkdir -p  /var/lib/gdm/.config/systemd/user
 # ln -s /dev/null  /var/lib/gdm/.config/systemd/user/pulseaudio.socket

On next reboot the second instance of PulseAudio will not be started.

It may happen that bluez wrongly considers a headset as not a2dp capable. In this case, search the index of the bluetooth device with

 $ pacmd ls

Among the output there should be a section related to the bluetooth headset, containing something similar to

To manually set the profile, run

 $ pacmd set-card-profile 2 a2dp_sink

where 2 is the index of the device retrieved through .

## Connecting works, but the device does not show up in PulseAudio sinks
If the headphones connect successfully (which can be confirmed via ) but do not show up as an output/input sink in , you can try adding (or creating) the following policy to your Bluetooth configuration file :

Restart the , then reconnect the headphones.

Some users [https://bbs.archlinux.org/viewtopic.php?id=234790 report that this has solved their problem.

## Connecting works, sound plays fine until headphones become idle, then stutters
If the headphones play sound correctly until they become idle and then stutter on resume (e.g. because the sound is paused, or because no sound is played for a while), try disabling PulseAudio's automatic sink/source suspension on idle.

Some user reports huge delays or even no sound when the Bluetooth connection does not send any data. This is due to the  module, which automatically suspends sinks/sources on idle. As this can cause problems with headset, the responsible module can be deactivated.

To disable loading of the  module, comment out the following line in the configuration file in use ( or ):

Finally restart PulseAudio to apply the changes.

## UUIDs has unsupported type
During pairing you might see this output in bluetoothctl:

 Device 00:1D:43:6D:03:26 UUIDs has unsupported type

This message is a very common one and can be ignored.

## PC shows device as paired, but is not recognized by device
This may be due to the device not supporting Bluetooth LE for pairing, but it attempts to connect in LE mode by default.
Most likely error:

Try setting  in . See [https://unix.stackexchange.com/questions/292189/pairing-bose-qc-35-over-bluetooth-on-fedora.

## Device connects, then disconnects after a few moments
If you see messages like the following in the journal, and your device fails to connect or disconnects shortly after connecting:

 bluetoothd: Unable to get connect data for Headset Voice gateway: getpeername: Transport endpoint is not connected (107)
 bluetoothd: connect error: Connection refused (111)

This may be because you have already paired the device with another operating system using the same bluetooth adapter (e.g., dual-booting).  Some devices cannot handle multiple pairings associated with the same MAC address (i.e., bluetooth adapter).  You can fix this by re-pairing the device.  Start by removing the device:

 $ bluetoothctl
 devices
 Device XX:XX:XX:XX:XX:XX My Device
 [bluetooth# remove XX:XX:XX:XX:XX:XX

Then restart , turn on your bluetooth adapter, make your device discoverable, re-scan for devices, and re-pair your device.  Depending on your bluetooth manager, you may need to perform a full reboot in order to re-discover the device.

## Apple AirPods have low volume
Create a drop-in file for  with the following contents:

Then, restart , reload its configuration, and reconnect your headset.

This can also solve issues with some devices that are unable to be controlled through AVRCP.

## Apple AirPods Pro working with PulseAudio as A2DP Sink but not with HSP/HFP
If you find that AirPods Pro are working with PulseAudio, but are incapable of using the HSP/HFP configurations (in pavucontrols Configurations tab, usually listed as unavailable), try switching to .

Note that switching to pipewire-pulse (and restarting your computer or the appropriate user-level systemd services) should enable HSP/HFP, but may also disable A2DP. (When selecting A2DP Sink in the Configurations tab, the option is instantly deselected and becomes Off.) If you encounter this issue, try removing/renaming the  folder like so:

 # mv /var/lib/bluetooth /var/lib/bluetooth.bak

Re-pair your AirPods Pro (and other devices) afterwards. This should make all configurations (HSP/HFP and A2DP) available again and easily accessible from pavucontrol and pacmd.

## HSP problem: the bluetooth sink and source are created, but no audio is being transmitted
You may be missing firmware or the SCO (audio protocol of HSP and HFP) routing might be wrong. See the PulseAudio documentation on this matter - firmware for Broadcom chips can be installed with .

## Error: Failed to start discovery org.bluez.Error.InProgress
On old Bluetooth versions like 4.0, if your headset is discovered, but fails to connect with the error , install  and run

 $ hciconfig hciX up
 $ hciconfig hciX reset

where X is the identifier of your computer's bluetooth device (typically 0).

You should then be able to connect following the steps in #Configuration via CLI.

Headsets using BT 4.1 and later should reset fine via the  and  commands via .

## High audio volume due to synchronization between headphones and PulseAudio
As of PulseAudio 15, "Absolute Volume" interlocks the audio volume of your headphones with PulseAudio, making it impossible to change one without the other. On some headphones, e.g. on the Hoco W25, this may result in irritating loudness. To disable "Absolute Volume", edit  and change the line
 load-module module-bluetooth-discover
to
 load-module module-bluetooth-discover avrcp_absolute_volume=false

The same feature is present in PipeWire and can be disabled if you are using WirePlubmer. Create and populate the  file as shown below:

{{hc|~/.config/wireplumber/wireplumber.conf.d/bluez-monitor.conf|
monitor.bluez.properties  {
    bluez5.enable-hw-volume  false
}
}}

## Switch between HSP/HFP and A2DP setting
This can easily be achieved by the following command where the  can be obtained by running .

 $ pacmd set-card-profile card_number a2dp_sink

Note that the different profiles might have different volumes and you need to increase the volume of the new profile before you hear something again.

For enabling automatic profile switching from A2DP to HSP when a recording stream appears without any role set, you can append  to  in .

For more information about PulseAudio profiles, see PulseAudio Documentation.

## A2DP not working with PulseAudio
## Socket interface problem
If PulseAudio fails when changing the profile to A2DP with bluez 4.1+ and PulseAudio 3.0+, you can try disabling the Socket interface from  by removing the line  and adding line .

## A2DP sink profile is unavailable
When the A2DP sink profile is unavailable it will not be possible to switch to the A2DP sink (output) with a PulseAudio front-end and the A2DP sink will not even be listed. This can be confirmed with .

 $ pactl list | grep -C2 A2DP
      Profiles:
              headset_head_unit: Headset Head Unit (HSP/HFP) (sinks: 1, sources: 1, priority: 30, available: yes)
              a2dp_sink: High Fidelity Playback (A2DP Sink) (sinks: 1, sources: 0, priority: 40, available: no)
              off: Off (sinks: 0, sources: 0, priority: 0, available: yes)
         Active Profile: headset_head_unit

Trying to manually set the card profile with  will fail.

 $ pacmd set-card-profile bluez_card.C4_45_67_09_12_00 a2dp_sink
 Failed to set card profile to 'a2dp_sink'.

This is known to happen from version 10.0 of PulseAudio when connecting to Bluetooth headphones via Bluedevil or another BlueZ front-end. See related bug report.

This issue also appears after initial pairing of Headphones with some Bluetooth controllers (e.g. ) which might default to the  or  service and will not allow switching to the A2DP PulseAudio sink that requires the  service.

Possible solutions:

* For some headsets, using the headset's volume or play/pause controls while connected can trigger the A2DP profile to become available.
* Try starting with the normal linux or linux-lts kernel if you are using something else.
* It is possible that connecting to a headset via  from  will make the A2DP sink profile available. There is an automation for this every time a bluetooth device is connected:  (detailed usage)

 connect headset_MAC_address

* Manually switching to Bluetooth's  service which would make the A2DP profile and its A2DP PulseAudio sink available. This can be done with blueman-manager which included in  or by registering the UUID of the AudioSink service with .

 $ bluetoothctl
 [bluetooth# menu gatt
 register-service 0000110b-0000-1000-8000-00805f9b34fb
 [bluetooth# quit

* Disable the headset profile

* Enable MultiProfile support. This may help with headsets that support A2DP as well as Headset audio.

* Sometimes, none of the steps above will work. You may have tried rebooting and powering bluetooth off and on to no avail. In this case, try restarting the .
* For some headphone models with audio control panel, the A2DP profile must be enabled by pressing the Play/Pause button on the panel.

## Gnome with GDM
The instructions below were tested on Gnome 3.24.2 and PulseAudio 10.0 however they may still be applicable and useful for other versions.

If PulseAudio fails when changing the profile to A2DP while using GNOME with GDM, you need to prevent GDM from starting its own instance of PulseAudio:

* Prevent PulseAudio clients from automatically starting a server if one is not running by adding the following:

* Prevent systemd from starting PulseAudio anyway with socket activation:

 $ sudo -ugdm mkdir -p /var/lib/gdm/.config/systemd/user
 $ sudo -ugdm ln -s /dev/null /var/lib/gdm/.config/systemd/user/pulseaudio.socket

* Restart, and check that there is no PulseAudio process for the  user using:

 $ pgrep -u gdm pulseaudio

Further discussion about this problem and alternative fixes can be found at and [https://bbs.archlinux.org/viewtopic.php?id=196689. Alternatively, one may try and install .

## HFP not working with PulseAudio
HFP-only bluetooth headsets may not be usable in the standard configuration of PulseAudio. The respective profiles occur, but they are not available:

To solve the respective issue, update PulseAudio and BlueZ to latest versions. Then install  and   then create / activate a fake modem as described here * Create  with:

 [phonesim
 Address=127.0.0.1
 Driver=phonesim
 Port=12345

* Start as user:

 $ phonesim -p 12345 /usr/share/phonesim/default.xml &

* Enable/start the .
* Power modem:

 $ dbus-send --print-reply --system --dest=org.ofono /phonesim org.ofono.Modem.SetProperty string:"Powered" variant:boolean:true

* Activate modem:

 $ dbus-send --print-reply --system --dest=org.ofono /phonesim org.ofono.Modem.SetProperty string:"Online" variant:boolean:true

* To check the results, use the test commands from  installed in . To power, activate, and test the modem you can use:

 $ /usr/lib/ofono/test/enable-modem /phonesim
 $ /usr/lib/ofono/test/online-modem /phonesim
 $ /usr/lib/ofono/test/list-modems

The output of the respective modem section should be like this:

 ...
 [ /phonesim ]
   Online = 1
   Powered = 1
   Lockdown = 0
   Emergency = 0
   Manufacturer = MeeGo
   ...

* Finally, restart PulseAudio and reconnect headset. Now, HFP should be available:

 headset_head_unit: Headset Head Unit (HSP/HFP) (sinks: 1, sources: 1, priority: 30, available: yes)

## Disable PulseAudio auto switching headset to HSP/HFP
When using a bluetooth headset that supports multiple profiles, some applications switch to HSP/HFP profile automatically. If this behaviour is undesired you can disable this by appending the auto_switch=false parameter to the bluetooth-policy module:

## Disable WirePlumber auto-switching
WirePlumber has profile auto-switching enabled by default. It can automatically switch between HSP/HFP and A2DP profiles whenever an input stream is detected. You can disable it with the following command:

 $ wpctl settings --save bluetooth.autoswitch-to-headset-profile false

## Disable PipeWire HSP/HFP profile
Unlike PulseAudio, PipeWire does not automatically switch between A2DP and HSP/HFP in response to input events. However, rather than to enable automatically switching to the (lower audio quality) HSP/HFP profile if A2DP fails, you may prefer to disable the former altogether. To do so, create or edit a bluez configuration as shown below.

{{hc|/etc/wireplumber/wireplumber.conf.d/51-mitigate-annoying-profile-switch.conf (or ~/.config/wireplumber/wireplumber.conf.d/51-mitigate-annoying-profile-switch.conf)|2=
## In WirePlumber there's a bug where some applications trigger switching to Headset Profile
## --
## See issue #634, #645, #630, #629, #613
## --
## This config mitigates the issue by completely disabling the switching and support for Headset Profile (HFP)
## Using this would only make sense if you never plan on using the microphone that comes with your headset.

wireplumber.settings = {
  ## Whether to use headset profile in the presence of an input stream.
  ## --
  ## Disable for now, as it causes issues. See note at the top as to why.
  bluetooth.autoswitch-to-headset-profile = false
}

monitor.bluez.properties = {
  ## Enabled roles (default: [ a2dp_sink a2dp_source bap_sink bap_source hfp_hf hfp_ag ])
  ##
  ## Currently some headsets (Sony WH-1000XM3) are not working with
  ## both hsp_ag and hfp_ag enabled, so by default we enable only HFP.
  ##
  ## Supported roles: hsp_hs (HSP Headset),
  ##                  hsp_ag (HSP Audio Gateway),
  ##                  hfp_hf (HFP Hands-Free),
  ##                  hfp_ag (HFP Audio Gateway)
  ##                  a2dp_sink (A2DP Audio Sink)
  ##                  a2dp_source (A2DP Audio Source)
  ##                  bap_sink (LE Audio Basic Audio Profile Sink)
  ##                  bap_source (LE Audio Basic Audio Profile Source)
  ## --
  ## Only enable A2DP here and disable HFP. See note at the top as to why.
  bluez5.roles = [ a2dp_sink a2dp_source ]
}
}}

As suggested in this comment on the Wireplumber issue tracker.

## Alternative: A2DP duplex channel
FastStream, AptX LL, and "Opus 05 Pro" (a pipewire invention) have a "duplex" channel that allows for sending microphone audio back without needing to go into HSP/HFP and tolerate the sound quality degradation. PipeWire, but not PulseAudio, has support for this feature. Support is automatic upon feature detection. Interaction with existing profile switcher (WirePlumber) is unknown.

## Tips and tricks
The following applies to both PipeWire and PulseAudio.

## Battery level reporting
To get the current battery level of your headset reported to , you must enable bluez' D-Bus experimental features as described in Bluetooth#Enabling experimental features.

## Media controls
To use the media controls they may be forwarded to MPRIS, where they can be picked up by media players that support MPRIS for external control. See MPRIS#Bluetooth for details.

## AVRCP Media controls
This may be desired for bluetooth headsets with overly sensitive touch controls, and AVRCP playback controls can be disabled through the  sysfs file corresponding to the virtual AVRCP input device, for example . The correct virtual input can be identified via the  attribute, , which may for example be "Soundcore Life P3 (AVRCP)". Echoing  to this file inhibits/disables AVRCP, and echoing  re-enables it. This can be changed dynamically at runtime without restarting bluetoothd or disconnecting your device.

This will be reset on device disconnect and reconnect, so it is likely desired to automatically set it via a udev rule such as:

 SUBSYSTEM=="input" ATTR{name}=="Soundcore Life P3 (AVRCP)" ATTR{inhibited}="1"

If you want to be able to change this attribute as a regular user, see udev#Allowing regular users to use devices
