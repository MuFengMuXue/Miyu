**Resources**

[[]][Home](https://zoom-na.com/products/field-video-recording/field-recording/zoom-h1-handy-recorder)

Zoom H1 Handy Recorder is a mobile sound recording device. When connected via USB and then turned on, the user can choose between:

-   USB card reader
-   USB audio card

Press the big red record button to select the mode. Both modes work well with Gentoo, even with a deblobbed kernel.

## [Modes]

### [USB card reader]

This modes gives access to the inserted memory micro SD card, or built-in memory when card is not present.

### [USB audio card]

In this mode, the device functions as an external sound card, and works well with ALSA.

Input comes from H1\'s built-in high quality stereo microphone. Recording volume can be adjusted with +/- INPUT LEVEL buttons.

Output is sent to H1\'s LINE OUT mini-jack. Playback volume can be adjusted with +/- VOLUME buttons.

The following kernel option is enough:

    CONFIG_SND_USB_AUDIO=y

lsusb should show:

    Bus 001 Device 024: ID 1686:0045 ZOOM Corporation H4 Digital Recorder

aplay \--list-devices gives:

    card 2: H1 [H1], device 0: USB Audio [USB Audio]
     Subdevices: 1/1
     Subdevice #0: subdevice #0

Then you can select H1 as the recording device in most programs. If your audio program lacks a drop-down selection and requires specifying the device, you can write:

    iec958:CARD=H1,DEV=0