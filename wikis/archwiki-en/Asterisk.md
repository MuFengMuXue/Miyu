# Asterisk

Asterisk is a complete PBX (private branch exchange) in software. It runs on Linux, BSD, Windows and macOS and provides all of the features you would expect from a PBX and more. Asterisk does voice over IP in four protocols, and can interoperate with almost all standards-based telephony equipment using relatively inexpensive hardware.

Asterisk provides voice-mail services with directory, call conferencing, interactive voice response and call queuing. It has support for three-way calling, caller ID services, ADSI, IAX, SIP, H.323 (as both client and gateway), MGCP (call manager only) and SCCP/Skinny.

This article will show you how to configure a simple in house network enabling us to use a SIP softphone to talk to another SIP softphone on your LAN.

## Installation
Install the  package.

Alternatively, you can install the  or  package to have a long-term support release (current latest LTS major version is Asterisk 20). Asterisk LTS releases tend to have fewer features, but will be maintained for much longer. See the Asterisk Versions page for complete details about the release cycle for all Asterisk versions.

Enable/start .

You will also need a SIP softphone and at least two machines. Recommendations for SIP phones are Blink () or Linphone ().

To enable ilbc codec support add the following to the very beginning of the  section of the PKGBUILD:

 cd ${pkgname}-${pkgver}/contrib/scripts
 echo | ./get_ilbc_source.sh

## Configuration
As of Asterisk 20, the legacy  module is no longer compiled by default. If you would rather use  than , please install , which was the last LTS release to build .

 is the newer, more performant Asterisk channel module that supports the standard SIP (Session Initiation Protocol) protocol, the primary VoIP (Voice over Internet Protocol) protocol in use by many carriers, telcos, Internet telephony service providers (ITSPs), and enterprises. However,  is considerably more complicated to set up than the older .

The prevailing wisdom of the wider Asterisk community suggests to only use  if you already have an existing configuration for it, while also planning the upgrade to . For any new installations,  is recommended. As mentioned above,  is no longer maintained, not even for security fixes (except in older LTS releases), so new Asterisk PBX administrators should go with a supported SIP channel driver (i.e., ).

If you have an existing  configuration, to build it in Asterisk 20 LTS, you can do the following:  Edit the  PKGBUILD, in the  function. Modify the following line:

Prefix it with a call to build the menuselect tool, and enable :

Note that this will need to be done with every update of the  package.

## PJSIP
Once installed, Asterisk has the  configuration in . The sample file included with Asterisk gives several basic examples, but is not exhaustive for all pjsip options. Readers are encouraged to read the Asterisk Wiki Security best practices article, and Configuring res_pjsip before continuing.

This article contains a basic single SIP phone, multiple SIP trunk example, using SIP Station SIP trunks, from Sangoma. Two SIP trunks with SIP Station are configured for redundancy, as recommended by SIP Station. The following example was tested using a Sangoma/Digium D60 hardware phone, but any SIP 2.0 compliant hard- or softphone should suffice.

This example assumes the Asterisk PBX server and SIP phone are on a private IPv4 LAN, with a NAT router between the server/phone and the WAN/Internet. If you would like to use IPv6, please read the Configuring res_pjsip for IPv6 article.

## modules.conf
First, ensure  is not prefixed with . In this example, the  prefix makes Asterisk fail to load if  fails to load. This is not absolutely necessary, but unless you are using other VoIP protocols it may not make sense for Asterisk to load if  does not load.

## pjsip.conf
Before diving into configuring , review the PJSIP Configuration Wizard. It is useful for the simple use case of only one SIP provider/ITSP, and handles many of the pjsip objects for this automatically.

The file  is an ini-style configuration file, with , and either a hash () or a semicolon () as the comment character. Each line under a section header is a  pair, with section-specific keys set to the specified values. Note that section headers can have  appended after the closing square bracket, which indicates the section is a template, for later use within . To instantiate a section using a previously defined template, suffix the section header with the .

## transport section
In order to define a SIP trunk for use with Asterisk, PJSIP has the concept of a network . From the Asterisk Wiki, the transport section configures how  will operate at the transport layer. For example, it supports configuration options for protocols such as TCP, UDP, or WebSockets and encryption methods like TLS/SSL.

Transport sections can be named arbitrarily, but it is recommended to name the section that makes it easy to remember what it signifies. The following example names it  for identifying that this transport is using UDP for SIP, and is expected to traverse a NAT device.

Note that only one transport is allowed for each IP address/port or IP address/protocol mapping. If you would like to configure multiple transport protocols (e.g. both TCP and UDP), you will need to bind each protocol to a different IP address. Likewise if you want to define multiple transports using the same protocol, the ports used need to be different for each transport definition.

## registration section
Next, define the registrations the SIP trunks will use. Note that the SIP Station registrations are first defined via a template (with  appended to the section name). Each template defines the settings that are common for each section using the template;  the sections themselves only contain the options that need to be set for that section.

## authentication section
Here, define the authentication template, and the specific authentication sections for use with the SIP Station trunks.

## endpoint section
An endpoint is essentially a profile for the configuration of a SIP device such as a phone or remote server. This defines the transport, the Asterisk Dialplan context where calls originating from the endpoint gets handled, and the audio codecs allowed for the endpoint. For the SIP station trunks, define the following:

## identify section
Controls how the res_pjsip_endpoint_identifier_ip module determines what endpoint an incoming packet is from. For the SIP Station trunks, the following is defined:

## aor (Address Of Record) section
A primary feature of AOR objects (Address of Record) is to tell Asterisk where an endpoint can be contacted. Without an associated AOR section, an endpoint cannot be contacted. For the SIP Station trunks, define this:

## phone sections
Finally, define the necessary sections for the SIP phone that will register to Asterisk. It has several similar sections as with the SIP Station trunks. Expand these with templates if multiple local SIP phones are intended to register to your Asterisk PBX. Remote phones (from the WAN/Internet) can also be configured, but that iss outside the scope of this example.

## Managing PJSIP
There are several commands regarding  available in the Asterisk CLI, all prefixed with the  command. To get to the Asterisk CLI, enter the following command, as the  user:

 $ asterisk -rvvv

This assumes Asterisk is already running (e.g., via the systemd service unit). Once in the Asterisk CLI, you will see the prompt . To see a list of available PJSIP commands, type .

To see a list of PJSIP registrations, type the following:

To see a list of PJSIP endpoints, type the following:

## chan_sip
Note that the following instructions assume that you want to use already obsoleted  module. The  module is no longer maintained, but is easier to configure then the newer  module. There is a summary of configuration changes between two modules, as well as instructions on how to migrate to the newer module, on the  Asterisk documentation.

In order to use , you need to explicitly load the older module, and ensure that the newer  module is unloaded. In  adjust the following:

Add this to the following file:

This creates our two SIP users  and  with a password of  in the  context. The context will be defined next.

Add this to the following file:

This creates the context  and assigns extension 100 to the SIP user , and extension 101 to the SIP user .

Now all that is left is to see if it works.

## Music on hold
Music on hold is a really sweet feature. And once again easy to install and configure.
Edit  and add, or make sure it is uncommented:

And that is all there is to it. Just copy your favorite legally obtained MP3 to .

## Voicemail
Voicemail is another feature of asterisk. There are many ways to configure it, however this article only covers a simple approach.

Create/edit your :

What does this mean? Most of the  is pretty self-explanatory. However, do note that if you have postfix set up right the PBX will send an email notifying the user of a new voice-mail and if  is defined it will attach the file.

Now for the actual mailbox. The format is:

 mailbox => password,user,email

In this case, we gave 'Me' (email me@mydomain.com) mailbox 100, with a password of 1234.

Now we have to have a way to leave messages to this voice-mail, and a way to access it.
For this, we go back to the  and modify your existing entry as follows:

 exten => 100,1,Dial(SIP/me1,20)
 exten => 100,n,Voicemail(u100@default)

The 20 on the end of the first 'exten' tells 'Dial()' to call for 20 seconds. If no one answers it heads to voice-mail box 100 in the default context.

Next is actually accessing your voicemail. For this we add:

 exten => 600,1,VoiceMailMain,s100@default

So when we call 600, the application 'VoiceMailMain' goes to 100 in the default context. The  allows for automatic login.

## Connecting to the PSTN
Now that you have the previous setup, it is time to actually connect to the outside world. To do this, you will need a provider such as OnSIP. Your provider should have instructions on connecting to asterisk, so this section is very general.

## General set-up
## sip.conf
## extensions.conf
{{bc|1=
; this can be whatever
exten => _1NXXNXXXXXX,1,SetCIDNum(15555551234)
exten => _1NXXNXXXXXX,2,Dial(SIP/${EXTEN}@whatever)
exten => _1NXXNXXXXXX,3,Congestion()
exten => _1NXXNXXXXXX,103,Busy()

[default  ; This should be set in your sip.conf for incoming calls

;These should to be changed to your actual number
; ie     15555555555
exten => 1NXXNXXXXXX,1,Answer()
exten => 1NXXNXXXXXX,2,Playback(ttt-weasels)
exten => 1NXXNXXXXXX,3,HangUp()
}}

*In the outbound context, any number dialed will be sent out to your service provider. The 'whatever' in the 2 priority should match what you have in your .
*Of course, the inbound dial-plan can be modified to do what you want. For instance, you can have  so when someone calls your number they are routed to your SIP phone on your computer. Then add in voice-mail and so on.

## iax.conf
The first step is to log into FWD and enable their side of IAX. It is under extra features, and keep in mind that the authors claim it takes a little while to activate.

Now edit your  with the following in the 'general' section:

And at the bottom add:

This allows calls from FWD.

## extensions.conf
Place this at the top under 'Next, add this to a context for outgoing:

{{bc|1=
exten => _393.,1,SetCallerId,${FWDCIDNAME}
exten => _393.,2,Dial(IAX2/${FWDNUMBER}:${FWDPASSWORD}@iax2.fwdnet.net/${EXTEN:3},60,r)
exten => _393.,3,Congestion
}}

You can change the '393' to whatever you want. This is what you will dial before dialing a 'fwd' number. For instance, to dial '744561' you would dial '393744561'.

And lastly, the incoming calls:

{{bc|1=
[fromiaxfwd
exten => ${FWDNUMBER},1,Dial(${FWDRINGS},20,r)
exten => ${FWDNUMBER},2,Voicemail,u${FWDVMBOX}
exten => ${FWDNUMBER},102,Voicemail,b${FWDVMBOX}
}}

Extensions to try calling are 55555 (a volunteer maned test line) and 514 (conference).

## Sounds
Sounds are stored in the folder ,  stands for the code of the language for example "en" for English. To add new sounds copy them to the folder. Preserve the following folder structure:

Edit the language parameter in the

Possible sources for sounds are:

* https://downloads.asterisk.org/pub/telephony/sounds/
* https://packages.debian.org/wheezy/all/asterisk-prompt-xx
** fr
** de
** ...
* voip-info.org

## MeetMe
MeetMe is the application that allows you to do conference calling. Same as everything, basic setup is easy.

Edit :

 conf => 1000

Next is :

 exten => 999,1,MeetMe(1000|M)

Now dial 999 to get into conference 1000. The  enables music on hold if no one is in there. It will automatically go away when someone joins the conference.

## Asterisk console and softphones
Now lets get Asterisk going:

 # asterisk -vvvvvvc

This will give us the Asterisk CLI with verbose output. If Asterisk is already running you will need to use:

 # asterisk -r

Now fire up your SIP clients and set them up with the information in the sip.conf. Switch back to your Asterisk CLI and you should see:

 Registered SIP 'me1' at 192.168.0.142 port 5061 expires 60

Now you should be able to dial  from  and talk to .

## Troubleshooting
If you receive a 404 Not Found error check your  and the number you dialed.
