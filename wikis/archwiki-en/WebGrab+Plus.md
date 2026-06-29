# WebGrab+Plus

WebGrab+Plus is a Freeware, closed-source multi-site incremental XMLTV EPG grabber. It collects TV program guide data from selected TV guide sites for your favorite channels.

* Fast through its incremental mode in which it grabs only what is new or changed.
* Rich in detail and highly configurable.
* Optional post-processors to add IMDb data or to customize your XMLTV listing.

It can later be used by Kodi, MythTV, Tvheadend and other compatible Television and Home Theater front-end media players.

A licensing model is introduced starting from version 3.1. The different license models are un_registrd_user, registered_user, donator, donator_license and developer.
Registration is required, for more information please check WebGrab+Plus FAQ.

{| class="wikitable"
|+ License Table
|-
! !! default !! un_registrd_user !! registered_user !! donator !! donator_license !! developer
|-
| channels/ini || 20 || 20 || 30 || 50 || 250 || 1000
|-
| channels total || 20 || 20 || 30 || 50 || 250 || 1000
|-
| siteinis || 2 || 2 || 3 || 10 || 15 || 100
|-
| decryption keys || without userkey || without userkey || enabled || enabled || enabled || enabled
|-
| decryption mode || legacy (V2) || legacy (V2) || legacy (V2) || legacy (V2) || new (V3) & (V2) || new (V3) & (V2)
|-
| index only || yes || yes || no || no || no || no
|-
| postprocess MDB || disabled || disabled || disabled || enabled || enabled || enabled
|-
| postprocess REX || disabled || enabled || disabled || enabled || enabled || enabled
|-
| debug || False || False || False || False || False || True
|-
| show details ★ || ttd || ttd || ttsd || full || full || full
|-
| update mode || force || force || light || all || all || all
|-
| channel delay || 4 secs || 4 secs || 2 secs || 0 secs || 0 secs || 0 secs
|-
| index delay || 4 secs || 4 secs || 4 secs || 0 secs || 0 secs || 0 secs
|-
| show delay || 2 secs || 2 secs || 1 secs || 0 secs || 0 secs || 0 secs
|}
★ showdetails : 'tt = times & title, 's' = subtitle, 'd' = description

## Installation
Install the  package.

## Usage
First step is to create a working directory for  EPG/XMLTV grabber. The working directory will be saved to the home directory of the active user.

To create a configuration directory type:

 $ wg++ -g

At this point all necessary files are created and it's now possible to configure .

To generate EPG guide file , type:

 $ wg++

The EPG guide  will be stored in the location, which is defined in configuration file .

To see what options can be used with , type:

 $ wg++ -h

## Configuration
All configuration files will be placed in  directory. The main configuration file is . See the upstream documentation for the available options.

## Finding and adding channels
Channel entries defines what TV programs needs to be included in EPG guide.

To list all possible TV programs, use this command:

 $ grep site_id ~/wg++/siteini.pack/*/*channels.xml

To list all possible TV programs by country:

 $ grep site_id ~/wg++/siteini.pack/Country/*channels.xml

To filter TV programs by keyword:

 $ grep site_id ~/wg++/siteini.pack/*/*channels.xml | grep -i "keyword"

And paste as many  entries as you want into the configuration file.

## Troubleshooting
## Different channel names
Your IPTV provider might use different channel names from what WebGrabber+Plus offers. For example - TV3 channel exists in WebGrabber+Plus channels list, but your IPTV provider uses TV3 4K, which refers to the same channel, but cannot be found in WebGrabber+Plus channels list. If the channel name is not changed, then it will not be picked up by IPTV player either.

To resolve this, take the actual WebGrabber+Plus channel element:

 TV3

and change value accordingly:

 TV3 4K

## Same channels under different names
Your IPTV provider might provide backup channels or channels with different quality, therefore ending up with duplicating channels under different names. In order to generate EPG guide efficiently, modify configuration file as per below example:

 SPORT TV 1
 SPORT TV 1 HD
 SPORT TV 1 FHD
 SPORT TV 1 XXX

## Tips and tricks
## Alternative configuration directory
You can specify and use alternative configuration directory. Copy default configuration directory to your desired destination:

 $ cp -r /usr/share/wg++ /path/to/configuration_directory

It's also possible to create an alternative configuration directory with , type:

 $ wg++ -d /path/to/configuration_directory -g

To generate EPG guide, run:

 $ wg++ -d /path/to/configuration_directory

## Update channels list
As of version 5.5.0, the update is no longer possible to make via the wrapper scripts but is embedded in the dotnet binary framework for automatic update of the  folder.

Update yourself for specific TV guide providers. See WebGrab+Plus EPG-channels
