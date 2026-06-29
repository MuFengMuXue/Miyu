# Professional audio/Hardware

## M-Audio Delta 1010
The M-Audio Delta series cards are based on the VIA Ice1712 audio chipset.
Cards using this chip require that you install the  package, because
it contains the  program. Envy24control is a hardware level
mixer/controller. You can use alsa-mixer but you will save yourself some
hassle not to try it. Note that this section has no information on MIDI setup or
usage.

Open the mixer application:

 $ envy24control

This application can be more than a bit confusing; see envy24control for guidance
on its use. That said, here is a very simple working setup for multitracking with Ardour.

# On the "Monitor Inputs" and "Monitor PCMs" tabs, set all monitor inputs and monitor PCMs to around 20.
# On the "Patchbay / Router" tab, set all to PCM out.
# On the "Hardware Settings" tab, verify that the Master Clock setting matches what is set in Qjackctl. If these do not match you will have xruns out of control!

## M-Audio Fast Track Pro
The M-Audio Fast Track Pro is an USB 4x4 audio interface, working at 24bit/96kHz. Due to limitation of USB 1, this device requires additional setup to get access to all its features. Device works in one of two configuration:

* Configuration 1, or "Class compliant mode" - with reduced functionality, only 16bit, 48kHz, analogue input (2 channels) and digital/analogue output (4 channels).
* Configuration 2 - with access to all features of interface.

Currently with stock kernel it runs in configuration 2, but if you want to make sure in what mode you are, you can check kernel log for entries:

 usb-audio: Fast Track Pro switching to config #2
 usb-audio: Fast Track Pro config OK

The interface also needs extra step of configuration to switch modes. It is done using option  during module loading. The recommended way to setup the interface is using file in :

where  and  are vendor and product id for M-Audio Fast Track Pro,  is desired device number and  is desired device setup. Possible values for  are:

{| class="wikitable"
|+ device modes
! device_setup value !! bit depth !! frequency !! analog output !! digital output !! analog input !! digital input !! IO mode
|-
| 0x0 || 16 bit || 48kHz || + || + || + || + || 4x4
|-
| 0x9 || 24 bit || 48kHz || + || + || + || - || 2x4
|-
| 0x13 || 24 bit || 48kHz || + || + || - || + || 2x4
|-
| 0x5 || 24 bit || 96kHz || * || * || * || * || 2x0 or 0x2
|}

The 24 bit/96kHz mode is special: it provides all input/output, but you can open only one of 4 interfaces at a time. If you for example open output interface and then try to open second output or input interface, you will see error in kernel log:

 cannot submit datapipe for urb 0, error -28: not enough bandwidth

which is perfectly normal, because this is USB 1 device and cannot provide enough bandwidth to support more than single (2 channel) destination/source of that quality at a time.

Depending on the value of  it will setup two devices:  and , which will contain available inputs and outputs. First device is most likely to contain analog output and digital input, while second one will contain analog input and digital output. To find out which devices are linked where and if they are setup correctly, you can check {{ic|/proc/asound/cardYYY/stream{0,1} }}. Below is list of important endpoints that will help in correctly identifying card connections (it easy to mistake analog and digital input or output connections before you get used to the device):

 EP 3 (analgoue output = TRS on back, mirrored on RCA outputs 1 and 2 on back)
 EP 4 (digital output = S/PDIF output on back, mirrored on RCA outputs 3 and 4 on back)
 EP 5 (analogue input = balanced TRS or XLR microphone, unbalanced TS line on front)
 EP 6 (digital input = S/PDIF input on back)

This .asoundrc file enables 24-bit IO on the fast-track pro (and I'm sure it could be modified to work with other 3-byte usb devices) within the context of jack's 32-bit interface while routing default ALSA traffic to jack outputs on the audio interface. ALSA will be in S24_3BE mode but jack can plug S32_LE data in and out of the interface and other ALSA programs will be able to plug almost anything into jack.

{{bc|
### ~/.asoundrc
### default ALSA config file, for a fast-track pro configured in 24-bit mode as so:
### options snd_usb_audio device_setup=0x9
### invoke jack with: (if you use -r48000, change the rate in the plugs as well)
### $jackd -dalsa -P"hw:Pro" -C"hw:Pro,1" -r44100

## setup input and output plugs so jack can write S24_3BE data to the audio interface

pcm.maud0 {
	type hw
	card Pro
}

#jack_out plug makes sure that S32_LE data can be written to hw:Pro
pcm.jack_out{
	type plug
	format S32_LE
	channels 2
	rate 44100
	slave pcm.maud0
}

pcm.maud1 {
	type hw
	card Pro
	device 1
}
## jack_in plug makes sure that hw:Pro,1 can read S32_LE data
pcm.jack_in {
	type plug
	format S32_LE
	channels 2
	rate 44100
	slave pcm.maud1
}
#####
# route default ALSA traffic through jack system io

pcm.jack {
    type jack
    playback_ports {
        0 system:playback_1
        1 system:playback_2
    }
    capture_ports {
        0 system:capture_1
        1 system:capture_2
    }
}
pcm.amix {
	type asym
	playback.pcm "jack"
	capture.pcm "jack"
	}
pcm.!default {
	type plug
	slave.pcm amix
}
}}

## Tascam US-122
Required packages:

*
*
*

Create the following rules file:

{{hc|/etc/udev/rules.d/51-tascam-us-122.rules|2=
SUBSYSTEMS=="usb", ACTION=="add", ATTRS{idProduct}=="8006", ATTRS{idVendor}=="1604", RUN+="/bin/sh -c '/sbin/fxload -D %N -s /usr/share/alsa/firmware/usx2yloader/tascam_loader.ihx -I /usr/share/alsa/firmware/usx2yloader/us122fw.ihx'"
SUBSYSTEMS=="usb", ACTION=="add", ATTRS{idProduct}=="8007", ATTRS{idVendor}=="1604", RUN+="/bin/sh -c '/usr/bin/usx2yloader'"
}}

Then reload udev rules and plug in the unit. The device should now be working, there are no software mixer controls.

## RME Babyface
It works very well at low latencies (~5ms) with ,  and . Running on ALSA only with the standard kernel may cause crackling at lower latencies.

To be recognized and work, the firmware version of the Babyface needs to be >= 200, which introduces the Class Compliant Mode. To enter Class Compliant Mode hold the "Select" and "Recall" buttons while connecting the Babyface to the computer via USB. It should now be recognized.

To check if it is recognized:

 $ grep -i baby /proc/asound/cards

For more info about the Class Compliant Mode visit RME's website, they have PDF which covers all the functionality.

The Babyface does not need any special Jack Settings. But if you want to use the built in MIDI In/Out then you need to set the "MIDI Driver" to "seq" and optionally disable "Enable ALSA Sequencer Support" to use it in combination with other MIDI Devices (a USB Midi Keyboard for example).

## Behringer UMC202HD/UMC204HD
Some Behringer UMC audio interfaces are known to hang up after sleepReloading the  module may resolve the issue. But usually it is enough to reset the USB device:

# Install .
# Find a device name with  command, it gives 3 columns of bus numbers, IDs and product names.
# Run the command with an argument e.g. with a product name: .

It can be done automatically with a systemd service:

Do a daemon-reload, then enable .

## Focusrite
Many of Focusrite USB interfaces works out-of-the-box. Therefore some interfaces has inner digital mixer which usage depends on a native proprietary utility unsupported for GNU/Linux. The solution is Open Source ALSA Scarlett Control Panel . Utility provides advanced GUI to rule the device mixer, also some knobs and buttons (depends on model).

ALSA Scarlett Control Panel currently supports following Focusrite devices:

* Scarlett 1st Gen: 6i6, 8i6, 18i6, 18i8, 18i20.
* Scarlett 2nd Gen: 6i6, 18i8, 18i20.
* Scarlett 3rd Gen: Solo, 2i2, 4i4, 8i6, 18i8, 18i20.
* Scarlett 4th Gen: Solo, 2i2, 4i4, 16i16, 18i16, 18i20.
* Clarett: 2Pre, 4Pre, 8Pre USB.
* Clarett+: 2Pre, 4Pre, 8Pre.
* Vocaster One, Vocaster Two.

For model specific details take a look at the [https://github.com/geoffreybennett/alsa-scarlett-gui/blob/master/README.md#user-content-documentation README.md.

The ALSA Scarlett Control Panel can upgrade firmware of a supported device. Latest firmwares may be found e. g. in . Also CLI firmware upgrade utility  exists.
