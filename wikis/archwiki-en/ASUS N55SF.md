# ASUS N55SF

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| Intel graphics || ||
|-
| NVIDIA graphics || ||
|-
| Graphic outputs || ||
|-
| Ethernet || ||
|-
| Wireless || ||
|-
| Audio || ||
|-
| Touchpad || ||
|-
| Camera || ||
|-
| USB 3.0 || ||
|-
| Card Reader || ||
|-
| Special Keys || ||
|-
| Power management || ||
|}

## Hardware
CPU: Intel Core i7-2630QM @ 2.00GHz

Mainboard: Intel HM65 Express

RAM: 6/8GB DDR3

Display: 15,6" HD LED (1920x1080)

Graphics adapter: Intel Core Processor Integrated Graphics Controller, NVIDIA GeForce GT 555M

Soundcard: Integrated Intel HDA, Bang & Olufsen speakers with external subwoofer

Network: Atheros Gigabit Ethernet Controller, Intel Centrino Wireless-N 1030

Hard disk: Seagate Momentus 750GB 5400rpm SATA

Webcam: IMC Networks

Touchpad: Synaptics

There is a BIOS update (v207) on ASUS support website (go to the English one if you do not find) that fix the numpad bug.

## Audio
Follow the official documentation: ALSA or/and PulseAudio.

## Subwoofer
## PulseAudio
We need PulseAudio profile which will use  ALSA device:

Lfe remixing must be enabled for remixing third channel:

To prevent volume changing of PCM set volume to ignore in:

Install ,  and  and append these lines to your default.pa if you want to configure subwoofer on every PulseAudio daemon start:

Commands to control volume:

## ALSA
External subwoofer + low pass filter configuration. Configuration uses ,  and .

{{hc|/etc/asound.conf|2=
# upmix 2channels to 3, one for LFE
pcm.upmix2021 {
    type plug
    slave.pcm lowpass2121
    slave.channels 3
    ttable {
        0.0    1
        1.1    1
        0.2    1
        1.2    1
    }
}

# low pass filter for LFE channel
pcm.lowpass2121 {
    type ladspa
    slave.pcm upmix2121
    path "/usr/lib/ladspa"
    channels 3
    plugins {
        0 {
            id 1672 # 4 Pole Low-Pass Filter with Resonance (FCRCIA) (1672/lp4pole_fcrcia_oa)
            policy none
            input.bindings.2 "Input";
            output.bindings.2 "Output";
            input { controls [ 200 0 ] }
        }
        1 {
            id 1098
            policy duplicate
            input.bindings.0 "Input";
            output.bindings.0 "Output";
        }
    }
}

pcm.upmix2121 {
    type plug
    slave.pcm surround21
    slave.channels 3
    ttable {
        0.0 1
        1.1 1
        2.2 1
    }
}

pcm.!default upmix2021
}}
