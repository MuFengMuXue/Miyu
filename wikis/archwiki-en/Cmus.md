# Cmus

cmus (C* MUsic Player) is a small, fast and powerful console audio player which supports most major audio formats. Various features include gapless playback, ReplayGain support, MP3 and Ogg streaming, live filtering, instant startup, customizable key-bindings, and vi-style default key-bindings.

## Installation
Install the  package.

See the optional dependencies for available codecs and output plugins (installed can be listed with ).

## Using cmus with ALSA
Install the  package.

When using cmus with ALSA the default configuration does not allow playing music. What you might encounter when trying to start cmus is a blank terminal line with no output whatsoever. To fix it, create a new configuration file and set the following variables:

## Usage
See ,  and .

## Configuration
To configure cmus, see .

## Remote control
Cmus can be controlled externally through a unix-socket with . This makes it easy to control playback through an external application or key-binding.

One such usage of this feature is to control playback in Cmus with the XF86 keyboard events. The following script when run will start Cmus in an xterm terminal if it is not running, otherwise it will will toggle play/pause:

Copy the code above into a file  and make it executable.

To use cmus-remote in Openbox, see Openbox#rc.xml.

## JACK
To make cmus work with JACK server run the above command in cmus:

## Audio scrobbling
Cmus does not support audio scrobbling itself, but there is third party solutions. Install  for Last.fm or Libre.fm scrobbling. For initial configuration run  and follow link to perform authentication.

By default cmusfm scrobbles to the Last.fm service. However, it is possible to change this behavior by modifying service-api-url and service-auth-url options in the configuration file (). Afterwards, one should reinitialize cmusfm  in order to authenticate with new scrobbling service. In order to use Libre.fm as a scrobbling service, one shall use configuration as follows:

Next step is to set cmusfm as status program for cmus. Execute command in main cmus window

## Troubleshooting
## Cannot see tracks after adding
If you cannot see tracks just added, that can be because you did not install  package. You can see available files extension with:

 $ cmus --plugins
