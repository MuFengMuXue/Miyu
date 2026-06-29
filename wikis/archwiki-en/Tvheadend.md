# Tvheadend

Tvheadend is a TV streaming server and recorder. Tvheadend supports DVB-S/S2, DVB-C/C2, DVB-T, ATSC, ISDB-T, IPTV, SAT>IP and HDHomeRun as input sources.

## Installation
Tvheadend can be installed with  or  (development branch).

## HDHomeRun
HDHomeRun support should be working out-of-the-box in both  and .

## Playback clients
* Kodi —  or

* Smplayer In your web browser open http://localhost:9981 and grab the stream from the channel you want to watch, one way of doing this is on the electronic program guide tab, under details click on the icon beside the TV icon and click play program, your web browser should then download the stream info, then in smplayer click on open url and paste the stream, to save it, under the TV option click on add current media.

## Usage
Once Tvheadend is installed start/enable the .

To be able to login on first run, one needs to edit  and add the  () argument to :

## Configuration
Once the service is running, configuration of Tvheadend is done through a web interface on localhost:9981.

## XMLTV
If you want to obtain schedule data from an outside source like Schedules Direct, then you should also install .

## Tips and tricks
## Create M3U compatible playlist file
To export all channels as a M3U playlist file, one may want to use the following URL http://:@:9981/playlist/channels.m3u?profile=

## Use hardware video acceleration
When using  it is possible to enable hardware video acceleration.

Support depends on selected the codec and capabilities of the video device in use.

To enable hardware acceleration, check Hardware acceleration for a codec profile on the Codec Profiles page.

## Enable VA-API support transcoding
It is possible to use VA-API for transcoding streams when using , support depends on capabilities of the video device and the selected codec.

To enable VA-API create a new Codec Profile and select a codec with VAAPI on the Codec Profiles page. On the next screen check Hardware acceleration, select the correct Device Name, e.g.  and click on Create.

Finally, create a Stream Profile and select the previously created Codec Profile as Video codec profile. The Audio codec profile and Subtitle codec profile depend on the user preferences and as stated support by the video device.

To test the newly created profile, you may want to use the following URL:

 http://:@:9981/stream/channelnumber/?profile=

Use journalctl to check for Tvheadend debug info. The error tvheadend[..: transcode: no AVHWAccel indicates the stream profile does not use hardware acceleration and one should adjust the codec configuration.

## Use CAPMT (Linux Network DVBAPI) with OSCam
Install  to provide a softcam for Tvheadend. See the Tvheadend docs for configuration details.

Restart  and  to apply the changes.

## Troubleshooting
## Unable to authenticate/play stream
Try to use Matroska as stream profile when unable to start playback on video players like VLC.

Authentication issues can occur when using digest as Authentication type.

Change this to Both plain and digest to allow browsers/players that do not support the digest protocol.

## DVB-T2 HD in Germany
The German broadcast of DVB-T2 HD is a deviation of the official standard inasmuch as it is using the more modern H.265 codec. Somehow, tvheadend doesn’t detect the channels automatically. You first need to run the configuration wizard, choose no pre-defined muxes, just --Generic--: auto-Default. After the search run, save and go to Configuration, DVB Inputs, Muxes. Select all listed muxes (might be on two pages, batch selection via shift key possible) and edit them from DVB-T to DVB-T2 – you need to check the Delivery system checkmark in the edit dialog. Then go to Network, select the DVB-T entry and click Force scan. Observe the rescan via the Muxes tab as several of the former "FAIL" results become "OK". If this doesn’t happen, make sure you have the necessary firmware blob for your DVB-T2 receiver, e.g. by Hauppauge, manually installed first, followed by a system restart. This will get you the channels under Services which you can use to create an actual channel list of the unencrypted TV channels. Click on "Map selected", "Map selected services". Now, the channels should appear in the tab "Channel / EPG","Channels". Shortly after, the EPG view should be populated in tab "Electronic Program Guide".
