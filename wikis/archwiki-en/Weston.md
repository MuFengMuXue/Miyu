# Weston

Weston is a Wayland compositor designed for correctness, reliability, predictability, and performance.

## Installation
Install the  package.

## Usage
To launch Weston natively (from a TTY) or to run Weston inside a running X session:

 $ weston

See  for details and configuration flags.

## Demo applications
Then within Weston, you can run the demos. To launch a terminal emulator:

 $ weston-terminal

To move flowers around the screen:

 $ weston-flower

To display images:

 $ weston-image image1.jpg image2.jpg...

## Shortcuts
{| class="wikitable"
|+ Keyboard Shortcuts
!Command
!Action
|-
|
|Quit Weston
|-
| (or /)
|Zoom in/out of desktop
|-
|
|Switch windows
|-
|
|Move Window
|-
|
|Rotate Window
|-
|
|Resize Window
|-
|
|Change window opacity
|-
|
|Force Kill Active Window
|-
|
|Switch Prev/Next Workspace
|-
|
|Grab Current Window and Switch Workspace
|-
|
|Switch to Workspace n (e.g. F2)
|-
|
|Take a screenshot
|-
|
|Record a screencast
|}

## Configuration
Following is an example configuration file. See  for more.

Minimal :

## Monitors
Weston's outputs differ slightly from those of  Monitors:

 is the unused built-in video adapter. The add-on adapter  is cabled to one HDMI and one DVI monitor, so the output names are  and .

## Xwayland
See Wayland#Xwayland for details and an overview of available packages.

Set the following to activate the use of Xwayland:

## High DPI displays
For Retina or HiDPI displays, use:

## Shell font
Weston uses the default sans-serif font for window title bars, clocks, etc. See Font configuration#Set default or fallback fonts for instructions on how to change this font.

## Tips and tricks
## Screencast recording
Weston has built-in screencast recording which can be started and stopped by pressing the  key combination. Screencasts are saved to the file  in the current working directory of Weston. The WCAP format is a lossless video format specific to Weston, which only records the difference in frames. To be able to play the recorded screencast, the WCAP file will need to be converted to a format which a media player can understand. First, convert the capture to the YUV pixel format:

 $ wcap-decode --yuv4mpeg2 capture.wcap > capture.y4m

The YUV file can then be transcoded to other formats using FFmpeg or  (see  for more).

## Window switching
To switch windows with  instead of  change  to  in  and recompile .

## Touch display mapping
Touch display mapping can be achieved through the use of udev rules. Just like the  or  device environment variable binds the device to a specified seat, the  variable may be used to bind the device to the appropriate output. This variable should match a monitor name. See #Monitors for an explanation of the monitor naming convention.
