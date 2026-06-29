# Shinobi

Shinobi is a modern, Open Source NVR (Network Video Recorder) written in Node.js. For personal or educational use, the Pro version does not require a license key. See upstream documentation if the intended use is for commercial purposes.

## Installation
Install .

Finally populate the database with tables:

 # mysql ccio < /usr/share/shinobi/sql/framework.sql

## Setup Shinobi
Customize  as desired.

Optionally setup the mail section accordingly as well as replacing the cron key with something random as indicated in the comments.

Optionally change the super admin password by editing  and replacing the value for "pass" with an md5sum hashed password. Generate one like this:

 $ echo -n PASSWORD | md5sum

Start and enable shinobi with the  unit.  will start/stop  and . Browse to http://localhost:8080/super to perform initial setup including creating a user/users. See the official configure guide for a walk-through. Once finished, browse to http://localhost:8080 and log in as the non-admin user.

## Android and iOS apps
Shinobi Mobile Apps for both Android and iOS are available though this public test.

## Tips and tricks
## Delay between camera video and Shinobi
Some level of a lag or delay between the camera and the Shinobi dashboard is normal and dependent on stream type and video settings. See upstream documentation for some tips on minimizing the delay.

## Motion/object detection natively in Shinobi
Shinobi can monitor a video feed and only record if motion is detected. Full frame or trigger areas are natively supported. See the setting-up-motion-detection article of upstream's documentation.

## Motion/object detection from within the camera
Some camera manufactures offer native motion/object detection within the firmware of the camera itself. Shinobi can accept external event to trigger a record when motion is detected by the camera and these events are communicated by either SMTP or FTP.

Since our package is not running  as root, it cannot use the native ports for these services (25 for STMP and 21 for FTP).

It is recommended to simply select a port above 1,000 for these services on Shinobi and within the camera.

If using the native ports is a hard requirement, use a drop-in snippet for :

 AmbientCapabilities=CAP_NET_BIND_SERVICE

## Resources
* [https://shinobi.video/docs/ Shinobi docs - Official docs and guides.
* iSpy camera database - Large database of URLs for various cameras.
* Shinobi camera database - Searchable database of supported cameras including things such as protocols, URLs for streams, and other technical specs.
* Home assistant camera database - Another resource for finding URLs for streams.
