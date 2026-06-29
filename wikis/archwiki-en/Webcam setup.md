# Webcam setup

This is a guide to setting up your webcam. Most probably your webcam will work out of the box. Permissions to access video devices—e.g. —are handled by udev, there is no configuration necessary.

## Loading
Most recent webcams are USB video device class (UVC) compliant and are supported by the generic  kernel driver module. To check that your webcam is recognized, see the journal just after you plug the webcam in. You should see something like this:

Some pre-UVC webcams are also supported via the  kernel driver module. See the gspca cards list for a non-exhaustive list of supported devices under this framework.

Otherwise, if your webcam is not supported by the kernel drivers, an external driver is necessary:

* The first step is to identify the name of the webcam, using for example .
* Then you can check Webcam devices for information and resources about webcams.
* Once you find a driver compatible with the webcam, you can load the module at boot.

## Configuration
If you want to configure brightness, color and other webcam parameters (e.g. in the case when out-of-the-box colors are too bluish/reddish/greenish) you may use a variety of applications. Some specific webcams such as the Logitech Brio or the Razer Kiyo Pro might require a specific application for some of their specific options such as HDR. Changing any settings in an application that configures V4L settings will generally change those settings for all applications using those cameras unless they override those settings themselves.

## Command line
 installs a command line tool, v4l2-ctl.

To list all video devices:

 $ v4l2-ctl --list-devices

To list the configurable settings of a video device:

 $ v4l2-ctl -d /dev/video0 --list-ctrls

You can change the settings of the video device by doing the following:

 $ v4l2-ctl -c brightness=128

Alternatively, you can use :

 $ cameractrls -c brightness=128

## Graphical
For generic graphical webcam configuration tools you can use either qv4l2 from  or . In addition to this,  contains cameractrlsgtk4 which allows you to configure some camera-specific features for the Logitech Brio as well as the Razer Kiyo Pro on top of supporting all the other V4L options.

## Persisting configuration changes
Configuration made via V4L2 does not persist after the webcam is disconnected and reconnected. It is possible to use  with udev rules in order to set some configuration each time a particular camera is connected.

For example, to set a default zoom setting on a particular Logitech webcam each time it is connected, add a udev rule like this:

{{hc|/etc/udev/rules.d/99-logitech-default-zoom.rules|2=
SUBSYSTEM=="video4linux", KERNEL=="videoATTR{index}=="0", ATTRS{idVendor}=="046d", ATTRS{idProduct}=="0892", RUN+="/usr/bin/v4l2-ctl -d $devnode --set-ctrl=zoom_absolute=170"
}}

The above rule is valid for the Logitech C920 HD Pro Webcam - hardware ID 046d:0892.

The device's vendor id and product id can be found using . These are unique per product and do not change unless the product gets a new hardware revision.

To find udev attributes like the product name and serial, see udev#List the attributes of a device. It is also possible to set a static name for a video device).

## Disable internal laptop webcam
Sometimes we might want to disable a laptop's internal webcam so that only the one attached via USB is showing. This can be done with a udev rule. First we will need the device's vendor id and the product id:

Then we add new udev rule to remove the device as soon as it is detected:

{{hc|/etc/udev/rules.d/40-disable-internal-webcam.rules|2=
ACTION=="add", ATTR{idVendor}=="1bcf", ATTR{idProduct}=="28c1", RUN="/bin/sh -c 'echo 1 >/sys/\$devpath/remove'"
}}

## Disable webcam completely
To disable webcam completely, you can blacklist the  kernel module. For example:

## Applications
See also List of applications/Multimedia#Webcam.

## FFmpeg
See v4l2loopback#Use cases for various examples, where FFmpeg is used to output video to a v4l2 device, which can be used as a webcam.

For laptops without a webcam, an IP camera can be used as an alternative to droidcam which does not keep the extra webcam device hanging around. For android, something like [https://play.google.com/store/apps/details?id=com.pas.webcam IP webcam can be hosted on the phone, then use the IP camera as a video input for the laptop. First, install  and , then connect to the video source as  using  with  being the IP address of the phone:

 # modprobe v4l2loopback exclusive_caps=1
 $ ffmpeg -i http://192.168.1.xxx:8080/video -vf format=yuv420p -f v4l2 /dev/video0

## Firefox
Firefox may use not the highest resolution possible by default, leading to 4:3 image being captured from a 16:9 capable webcam. You can force specific resolution in  via  and  settings.

For example, to force 1920x1080 captured output, set  to .

## MPlayer
To use MPlayer to take snapshots from your webcam run this command from the terminal:

 $ mplayer tv:// -tv driver=v4l2:width=640:height=480:device=/dev/video0 -fps 15 -vf screenshot
From here you have to press  to take the snapshot. The snapshot will be saved in the current folder as .
If you want to record video continuous:

 $ mencoder tv:// -tv driver=v4l2:width=640:height=480:device=/dev/video0:forceaudio:adevice=/dev/dsp -ovc lavc -oac mp3lame -lameopts cbr:br=64:mode=3 -o filename.avi
Press  to end the recording.

To play video with MPlayer using MJPEG as the pixelformat instead of the default, which in most cases is YUYV, you can run the following:

 $ mplayer tv:// -tv driver=v4l2:width=640:height=480:device=/dev/video0:outfmt=mjpeg -fps 15

## mpv
To use mpv to take snapshots from your webcam, run this command from the terminal:

 $ mpv av://v4l2:/dev/video0 --profile=low-latency --untimed

From here you have to press  to take the snapshot. The snapshot will be saved in your current folder as .

To use MJPEG as the pixelformat instead of the default, which in most cases is YUYV, you can run the following instead:

 $ mpv --demuxer-lavf-format=video4linux2 --demuxer-lavf-o-set=input_format=mjpeg av://v4l2:/dev/video0

In some cases this can lead to drastic improvements in quality and performance (5FPS -> 30FPS for example).

To adjust webcam settings, including the resolution, see the mpv documentation.

## VLC
VLC can also be used to view and record your webcam. In VLC's Media menu, open the Capture Device... dialog and enter the video and audio device files. Or from the command line, for example:

 $ vlc v4l2://:input-slave=alsa://:v4l-vdev="/dev/video0"

This will make VLC mirror your webcam.

* To take stills, simply choose Snapshot in the Video menu.
* To record the stream, add a  argument to the command line, e.g.

 $ vlc v4l2://:v4l-vdev="/dev/video0":v4l-adev="/dev/audio2" --sout "#transcode{vcodec=mp1v,vb=1024,scale=1,acodec=mpga,ab=192,channels=2}:duplicate{dst=std{access=file,mux=mpeg1,dst=/tmp/test.mpg}}"

Note that by default this will not display the video. In order to see what you are recording, you need to add the display as a destination to the argument (which will slow down the operation):

 ... :duplicate{dst=display,dst=std{access= ....

## xawtv
This is a basic Video4Linux2 device viewer, and although it is intended for use with TV tuner cards, it works well with webcams. It will display what your webcam sees in a window.

Install  and run it with:

 $ xawtv -c /dev/video0

In case of error see #xawtv with NVIDIA card.

## Troubleshooting
## xawtv with NVIDIA card
If you are using an NVIDIA graphics card, and get an error like:

 X Error of failed request:  XF86DGANoDirectVideoMode
  Major opcode of failed request:  139 (XFree86-DGA)
  Minor opcode of failed request:  1 (XF86DGAGetVideoLL)
  Serial number of failed request:  69
  Current serial number in output stream:  69

you should instead run it as .

## Microsoft Lifecam Studio/Cinema
Under certain configurations, the Microsoft lifecam studio/cinema may request too much usb bandwidth and fail see Uvcvideo FAQ. In this case, change the buffering by loading the  driver with . Add it to  :

## Check bandwidth used by USB webcams
When running multiple webcams on a single USB bus, they may saturate the bandwidth of the USB bus and not work properly. You can diagnose this with the usbtop tool from the  package.

## Invert the video stream
If your video stream is inverted, you can make a new virtual video camera which inverts the inverted video. You need to install  and also . Create the virtual video camera:

 # modprobe v4l2loopback

Check the name of the newly created camera:

 $ v4l2-ctl --list-devices
 Dummy video device (0x0000) (platform:v4l2loopback-000):
    	/dev/video1

Then you can run  to read from your actual webcam (here ) and invert it and feed it to the virtual camera:

 $ ffmpeg -f v4l2 -i /dev/video0 -vf "vflip" -f v4l2 /dev/video1

Here  inverts the video stream vertically. Use  to invert it horizontally.

Note that the format argument  might be needed to avoid an error, otherwise there might not be any video stream and a black screen will be shown https://stackoverflow.com/questions/61485726/ffmpeg-flip-horizontally-webcam-to-virtual-video-camera/63943783#63943783. In other words:

 $ ffmpeg -f v4l2 -i /dev/video0 -vf "hflip,format=yuv420p" -f v4l2 /dev/video1

You can then use the "Dummy" camera in your applications instead of the "Integrated" camera.

## Bad image quality
If you experience images being too bright, too dark, too exposed or any other, you can install  to tweak your image output.

## Logitech Quickcam Pro 9000
Install  to enable autofocus control. After the installation, disconnect and reconnect your camera to trigger the newly added udev rules.

## Creality Webcam
Creality webcam is based on the Fullhan FH8852 chip used in many cheap 2MP cameras (USB ID ), but its firmware requires a special sequence to enable it, otherwise you'll get a black screen. Trying to grab a frame using FFmpeg seems to properly initialize the device, making it work on other apps. You might have to try the following on both  and , and see which one produces a correct  image:

 $ ffmpeg -i /dev/video0 /tmp/test_img.jpg

Once done, the camera should work on web browser, applications like Cheese, etc.
