# Freeswitch

The FreeSWITCH telephony engine is a powerful system enabling voice, video, presence, chat, and other media types via a variety of protocols.

## Installing
Install the 'release' version with .

You may wish to configure FreeSWITCH build options. Edit the PKGBUILD and change build configuration options to suit your desired usage.

## Configuring
The FreeSWITCH configuration files with the custom  and  reside in .  For following FreeSWITCH documentation, the base directory is  (generally seen as  in FreeSWITCH documentation).

FreeSWITCH comes out of the box with a default password for registrations to users 1000-1019 as '1234'.  You are advised to change this before running it.  This variable is set in .  The overall default configuration given is a kitchen sink featured PBX, likely many more things than are typically used.  Customizing the PBX (or non-PBX) features of FreeSWITCH is beyond the scope of this document; see the FreeSWITCH Wiki for in-depth documentation.

Upstream documentation as well as the original  directory are provided in .

## Running
Startup options are configured in .  You may wish to add  if you are not behind nat, see  for a full list of command line options.

FreeSWITCH can be started using the .

To start FreeSWITCH upon each boot, enable .  You will need to use the  and  options to the freeswitch command line to keep it running in the foreground as supervisors expect.

## Testing
* Fire up a SIP Client
* Register to your FreeSWITCH box as user 1000, password what you set as  in
* Dial 9196 (You should connect to an Echo Test)
* To measure call capacity, you can use StarTrinity SIP Tester (see an example performance report for 2250 G.711 channels)

## Hints
To see interesting things you can do with a dialplan, open up  and scroll through those examples.  Dialing the numbers that match the 'expression' of a condition from your SIP client will demonstrate their use.

You can dial into the FreeSWITCH public voice conference, for instance, by dialing 9888 (8k codec), 91616 (16k codec), or 93232 (32k codec)

FreeSWITCH support is available in #freeswitch on Libera Chat.
