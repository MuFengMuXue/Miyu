# SABnzbd

SABnzbd is an open-source binary newsreader written in Python.

From sabnzbd.org:
:It's totally free, incredibly easy to use, and works practically everywhere. SABnzbd makes Usenet as simple and streamlined as possible by automating everything we can. All you have to do is add an .nzb. SABnzbd takes over from there, where it will be automatically downloaded, verified, repaired, extracted and filed away with zero human interaction.

## Installation
Install  or .

## SSL Support
Install  to enable SSL support for news servers:
* Transmission of data from the server to the NNTP client is encrypted, protecting your privacy
* Decreasing the chances of throttling NNTP traffic done by the ISP.

## Archive unpacking
*Install  and  to allow unpacking of archives.

## Usage
SABnzbd is able to run globally (settings apply to all users) and locally (per user settings). The way of setting up SABnzbd depends on the way it is intended to be used. A local configuration may prove more useful on a desktop system when used by several people simultaneously.

If SABnzbd is started for the first time, the webinterface will present a setup wizard for configuring UI language and a single news server.

Further configuration can be done from within the UI (adding additional servers, setting folder paths etc.) or by editing .

## Global usage
Start/enable .

Add users to the  user group to allow read/write access to SABnzbd files.

## Running as a user
Alternatively, enable and start the  to run SABnzbd under the preferred user.

## Stopping SABnzbd
SABnzbd can be easily shutdown in the web-interface or the systemd  unit.

It is also possible to shutdown a running (remote) SABnzbd client using the provided API:

 $ curl "http(s)://host:port/sabnzbd/api?mode=shutdown&apikey=API-key"

## Accessing the web-interface
After starting SABnzbd, access the web-interface by browsing to http://127.0.0.1:8080.
